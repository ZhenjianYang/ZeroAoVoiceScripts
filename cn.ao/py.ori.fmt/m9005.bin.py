from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9005.bin",                # FileName
        "m9005",                    # MapName
        "m9005",                    # Location
        0x00BF,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 191, 0, 1, 0, 2],
    )

    BuildStringList((
        "m9005",                  # 0
        "幻兽",                   # 1
        "百臂巨魔",               # 2
        "百臂巨魔",               # 3
        "bm9010",                 # 4
        "bm9010",                 # 5
        "bm9010",                 # 6
        "bm9010",                 # 7
        "bm9010",                 # 8
        "bm9010",                 # 9
        "bm9010",                 # 10
        "bm9010",                 # 11
    ))

    ATBonus("ATBonus_564", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_574", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_44BF", 12,  23,  0,   16,  0,   0,   20)
    Sepith("Sepith_44AF", 8,   8,   18,  8,   2,   8,   16)
    Sepith("Sepith_44B7", 8,   4,   4,   16,  15,  17,  4)
    Sepith("Sepith_449F", 14,  14,  14,  14,  4,   9,   6)
    Sepith("Sepith_44A7", 9,   9,   9,   9,   13,  13,  13)

    MonsterBattlePostion("MonsterBattlePostion_5B4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_614", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_618", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_61C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_620", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_624", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_628", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_62C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_630", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_594", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_634", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_638", 1, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_63C", 15, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_640", 2, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_644", 14, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 1, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_64C", 15, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_650", 0, 0, 180)

    # monster count: 20

    BattleInfo(
        "BattleInfo_8F0", 0x0000, 105, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_44BF", 100, 0, 0, 0,
        (
            ("ms85201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_78C", 0x0000, 105, 6, 60, 10, 1, 40, 0, "bm9010", "Sepith_44AF", 40, 35, 25, 0,
        (
            ("ms87900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms87900.dat", "ms87900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms87900.dat", "ms87900.dat", "ms87900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_828", 0x0000, 105, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_44B7", 40, 30, 20, 10,
        (
            ("ms85700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms85700.dat", "ms85700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms85700.dat", "ms85700.dat", "ms85700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_654", 0x0000, 105, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_449F", 40, 35, 25, 0,
        (
            ("ms85400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms85400.dat", "ms85700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms85400.dat", "ms85700.dat", "ms85700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6F0", 0x0000, 105, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_44A7", 40, 35, 25, 0,
        (
            ("ms81100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms81100.dat", "ms81100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms81100.dat", "ms81100.dat", "ms81100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_978", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms81100.dat", "ms85700.dat", "ms81100.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_574"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9BC", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms81100.dat", "ms85700.dat", "ms81100.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_574"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_934", 0x0040, 255, 6, 45, 10, 1, 30, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89301.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", 0, "MonsterBattlePostion_634", "MonsterBattlePostion_614", "ed7554", "ed7453", "ATBonus_574"),
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
        "monster/ch85450.itc",               # 10
        "monster/ch85450.itc",               # 11
        "monster/ch81150.itc",               # 12
        "monster/ch81151.itc",               # 13
        "monster/ch87950.itc",               # 14
        "monster/ch87951.itc",               # 15
        "monster/ch85750.itc",               # 16
        "monster/ch85751.itc",               # 17
        "monster/ch85250.itc",               # 18
        "monster/ch85251.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(68459,   30500,   -13479,  0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(56000,   30500,   100000,  0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(31750,   -61980,  30000,   0x10100D1,    "BattleInfo_8F0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(48570,   -40240,  30020,   0x1010081,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(55920,   -51070,  30030,   0x101013D,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-103180, -88280,  25000,   0x1010168,    "BattleInfo_828", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-118280, -48840,  25520,   0x101009C,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-127920, 1890,    25500,   0x10100B4,    "BattleInfo_8F0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-85040,  -790,    25500,   0x1010107,    "BattleInfo_654", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-63620,  -15690,  25000,   0x101013A,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-62490,  23830,   25000,   0x10100B7,    "BattleInfo_828", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-45920,  48720,   25050,   0x10100E1,    "BattleInfo_828", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-8570,   62070,   25020,   0x101000C,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(22610,   71520,   25020,   0x101010E,    "BattleInfo_8F0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(34590,   50000,   25000,   0x1010137,    "BattleInfo_828", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(79910,   84020,   30020,   0x101010E,    "BattleInfo_654", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(80100,   62070,   30020,   0x1010011,    "BattleInfo_6F0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(103300,  39430,   30000,   0x1010111,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(108520,  7040,    30000,   0x1010168,    "BattleInfo_828", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(103990,  -21260,  30000,   0x1010009,    "BattleInfo_8F0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(98580,   -60280,  30020,   0x1010168,    "BattleInfo_654", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(70180,   -85610,  30000,   0x101005A,    "BattleInfo_6F0", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 13,  -44.5,                 -97.0,                 44.5,                  81.0,                  [0.2730506658554077,   0.09559610486030579,   -0.0,                  0.0,                   -0.19119220972061157,  0.13652533292770386,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -6.394889831542969,    17.496984481811523,    -8.90000057220459,     1.0])
    DeclEvent(0x0040, 0, 6,   31.079999923706055,    -106.05000305175781,   34.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -3.884999990463257,    13.256250381469727,    -8.5,                  1.0])

    DeclActor(68460,   30000,   -13480,  1200,    68460,   31000,   -13480,  0x007C, 0,  3,  0x0000)
    DeclActor(56000,   30000,   100000,  1200,    56000,   31000,   100000,  0x007C, 0,  4,  0x0000)
    DeclActor(-22000,  25000,   69500,   1200,    -22000,  26000,   69500,   0x007C, 0,  5,  0x0000)
    DeclActor(0,       35000,   -110000, 1200,    0,       35000,   -110000, 0x007C, 0,  9,  0x0000)
    DeclActor(0,       30250,   -56000,  1200,    0,       30250,   -56000,  0x007C, 0,  11, 0x0000)

    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 4
    ChipFrameInfo(899, 0, [0, 1, 2, 3, 4])                       # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9

    ScpFunction((
        "Function_0_AE0",          # 00, 0
        "Function_1_AFC",          # 01, 1
        "Function_2_B75",          # 02, 2
        "Function_3_1D6F",         # 03, 3
        "Function_4_1F6D",         # 04, 4
        "Function_5_216B",         # 05, 5
        "Function_6_22A6",         # 06, 6
        "Function_7_231F",         # 07, 7
        "Function_8_259F",         # 08, 8
        "Function_9_26F2",         # 09, 9
        "Function_10_2822",        # 0A, 10
        "Function_11_2911",        # 0B, 11
        "Function_12_2A42",        # 0C, 12
        "Function_13_2B31",        # 0D, 13
        "Function_14_398D",        # 0E, 14
        "Function_15_399D",        # 0F, 15
        "Function_16_39B0",        # 10, 16
        "Function_17_39E1",        # 11, 17
        "Function_18_39F4",        # 12, 18
        "Function_19_3A07",        # 13, 19
        "Function_20_3A29",        # 14, 20
        "Function_21_3ACA",        # 15, 21
        "Function_22_3ADF",        # 16, 22
        "Function_23_3B20",        # 17, 23
        "Function_24_3B42",        # 18, 24
        "Function_25_3C27",        # 19, 25
    ))


    def Function_0_AE0(): pass

    label("Function_0_AE0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AFB")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_AE0")

    label("loc_AFB")

    Return()

    # Function_0_AE0 end

    def Function_1_AFC(): pass

    label("Function_1_AFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0D")
    Event(0, 7)

    label("loc_B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1E")
    Event(0, 25)

    label("loc_B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B2D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 24)

    label("loc_B2D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B74")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5A")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)
    Jump("loc_B74")

    label("loc_B5A")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B74")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)

    label("loc_B74")

    Return()

    # Function_1_AFC end

    def Function_2_B75(): pass

    label("Function_2_B75")

    OP_F0(0x1, 0x320)
    OP_1B(0x5, 0x0, 0x8)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B9A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_B9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BBC")
    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_C25")

    label("loc_BBC")

    OP_78(0x7, 0x8)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1)
    SetChrPos(0x8, 31080, 35000, -106050, 67)
    OP_93(0x8, 0x43, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, 31080, 34000, -106050, 3000, 3000, 90000)

    label("loc_C25")

    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x4, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x1000)
    OP_10(0x7, 0x0)
    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 3)), scpexpr(EXPR_END)), "loc_1CA3")
    ClearMapObjFlags(0x2, 0x4)
    OP_71(0x2, 0x0, 0x0, 0x0, 0x1000)
    SetMapObjFrame(0xFF, "CA_stop", 0x1, 0x2)
    Jump("loc_1CC4")

    label("loc_1CA3")

    SetMapObjFlags(0x2, 0x4)
    OP_71(0x2, 0x0, 0x0, 0x0, 0x1000)
    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x2)

    label("loc_1CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 6)), scpexpr(EXPR_END)), "loc_1CD9")
    ClearMapObjFlags(0x6, 0x2)
    SetMapObjFlags(0x6, 0x4)

    label("loc_1CD9")

    SetMapObjFrame(0xFF, "CA_stop2", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_1D02")
    SetMapObjFrame(0xFF, "CA_stop2", 0x1, 0x2)

    label("loc_1D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D23")
    SetMapObjFrame(0xFF, "magi_07c_add", 0x0, 0x1)

    label("loc_1D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D36")
    OP_70(0x3, 0x0)
    Jump("loc_1D3A")

    label("loc_1D36")

    OP_70(0x3, 0x1E)

    label("loc_1D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4D")
    OP_70(0x4, 0x0)
    Jump("loc_1D51")

    label("loc_1D4D")

    OP_70(0x4, 0x1E)

    label("loc_1D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D64")
    OP_70(0x5, 0x0)
    Jump("loc_1D68")

    label("loc_1D64")

    OP_70(0x5, 0x1E)

    label("loc_1D68")

    Sound(112, 1, 100, 0)
    Return()

    # Function_2_B75 end

    def Function_3_1D6F(): pass

    label("Function_3_1D6F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2F")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x219, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6C")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1DCC():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1DCC)

    def lambda_1DE6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1DE6)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x9, 1)
    Battle("BattleInfo_978", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1E4D"),
        (2, "loc_1E5C"),
        (1, "loc_1E69"),
        (SWITCH_DEFAULT, "loc_1E6C"),
    )


    label("loc_1E4D")

    SetScenarioFlags(0x219, 3)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_1E6C")

    label("loc_1E5C")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1E69")

    OP_B9(0x0)
    Return()

    label("loc_1E6C")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x656, 1)"), scpexpr(EXPR_END)), "loc_1EC3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x656),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x201, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1F2A")

    label("loc_1EC3")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x656),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x656),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1F2A")

    Jump("loc_1F61")

    label("loc_1F2F")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_1F61")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1D6F end

    def Function_4_1F6D(): pass

    label("Function_4_1F6D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212D")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x219, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_206A")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1FCA():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1FCA)

    def lambda_1FE4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1FE4)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    #A0005
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
    Battle("BattleInfo_9BC", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_204B"),
        (2, "loc_205A"),
        (1, "loc_2067"),
        (SWITCH_DEFAULT, "loc_206A"),
    )


    label("loc_204B")

    SetScenarioFlags(0x219, 4)
    OP_70(0x4, 0x1E)
    Sleep(500)
    Jump("loc_206A")

    label("loc_205A")

    OP_70(0x4, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2067")

    OP_B9(0x0)
    Return()

    label("loc_206A")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x41C, 1)"), scpexpr(EXPR_END)), "loc_20C1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x202, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_2128")

    label("loc_20C1")

    FadeToDark(300, 0, 100)

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x41C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x41C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2128")

    Jump("loc_215F")

    label("loc_212D")

    FadeToDark(300, 0, 100)

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

    label("loc_215F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1F6D end

    def Function_5_216B(): pass

    label("Function_5_216B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225D")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_21EE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x202, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_2258")

    label("loc_21EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2258")

    Jump("loc_229A")

    label("loc_225D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0011
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

    label("loc_229A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_216B end

    def Function_6_22A6(): pass

    label("Function_6_22A6")

    Battle("BattleInfo_934", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22ED")
    OP_90(0x0, 38360, 34570, -103390, 66)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Jump("loc_231E")

    label("loc_22ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2300")
    Jump("loc_231E")

    label("loc_2300")

    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0x7, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetScenarioFlags(0x1B8, 3)
    EventEnd(0x5)

    label("loc_231E")

    Return()

    # Function_6_22A6 end

    def Function_7_231F(): pass

    label("Function_7_231F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event/ev202_00.eff")
    OP_68(-54730, 46000, -89080, 0)
    MoveCamera(31, 51, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13870, 0)
    SetChrPos(0x0, -54250, 45500, -86750, 165)
    SetChrPos(0x1, -54250, 45500, -86750, 165)
    SetChrPos(0x2, -54250, 45500, -86750, 165)
    SetChrPos(0x3, -54250, 45500, -86750, 165)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_242F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_242F)

    def lambda_2440():
        OP_95(0xFE, -53260, 45000, -91480, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2440)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2497():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2497)

    def lambda_24A8():
        OP_95(0xFE, -54540, 45000, -91510, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_24A8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2505():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_2505)

    def lambda_2516():
        OP_95(0xFE, -51990, 45000, -90960, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2516)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_256D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_256D)

    def lambda_257E():
        OP_95(0xFE, -55840, 45000, -91280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_257E)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_7_231F end

    def Function_8_259F(): pass

    label("Function_8_259F")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_25F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_25F8)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2643():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2643)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_268E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_268E)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_26D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_26D9)
    Sleep(1000)
    NewScene("m9070", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_259F end

    def Function_9_26F2(): pass

    label("Function_9_26F2")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一台升降机。\x01",
            "要乘坐吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281A")
    Fade(500)
    SetChrPos(0x0, 0, 35000, -111000, 180)
    SetChrPos(0x1, -1000, 35000, -110000, 180)
    SetChrPos(0x2, 1000, 35000, -110000, 180)
    SetChrPos(0x3, 0, 35000, -109000, 180)
    OP_68(0, 35000, -111000, 0)
    MoveCamera(341, 45, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(29410, 0)
    OP_0D()
    Sleep(500)
    Sound(832, 2, 100, 0)
    Sound(935, 0, 70, 0)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x3C, 0x5A, 0x0, 0x0)
    OP_68(0, 15000, -108000, 4000)
    MoveCamera(5, 55, 0, 4000)
    Sleep(1800)
    StopSound(832, 500, 100)
    StopSound(112, 500, 100)
    SetScenarioFlags(0x1B0, 2)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m9004", 0, 0, 0)
    IdleLoop()

    label("loc_281A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_26F2 end

    def Function_10_2822(): pass

    label("Function_10_2822")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_71(0x1, 0x5A, 0x5A, 0x0, 0x1000)
    OP_49()
    OP_68(0, 35000, -111000, 0)
    MoveCamera(6, 57, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(22000, 0)
    OP_90(0x0, 0, 35000, -111000, 0)
    OP_90(0x1, -1000, 35000, -110000, 0)
    OP_90(0x2, 1000, 35000, -110000, 0)
    OP_90(0x3, 0, 35000, -109000, 0)
    Sound(832, 2, 100, 0)
    OP_68(0, 40000, -114000, 3000)
    MoveCamera(0, 40, 0, 3000)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x5A, 0x78, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(2000)
    OP_24(0x340)
    Sound(149, 0, 60, 0)
    Sleep(1400)
    Sleep(500)
    OP_79(0x1)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_2822 end

    def Function_11_2911(): pass

    label("Function_11_2911")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一台升降机。\x01",
            "要乘坐吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A3A")
    Fade(500)
    OP_69(0x0, 0x0)
    SetChrPos(0x0, 0, 30250, -57000, 180)
    SetChrPos(0x1, -1000, 30250, -56000, 180)
    SetChrPos(0x2, 1000, 30250, -56000, 180)
    SetChrPos(0x3, 0, 30250, -55000, 180)
    OP_68(0, 31250, -56000, 0)
    MoveCamera(16, 40, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(20650, 0)
    OP_0D()
    Sleep(500)
    Sound(832, 2, 100, 0)
    Sound(935, 0, 70, 0)
    OP_74(0x2, 0xF)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    OP_68(0, 35000, -56000, 4000)
    MoveCamera(5, 35, 0, 4000)
    Sleep(1800)
    StopSound(832, 500, 100)
    StopSound(112, 500, 100)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m9007", 0, 0, 0)
    IdleLoop()

    label("loc_2A3A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_2911 end

    def Function_12_2A42(): pass

    label("Function_12_2A42")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_71(0x2, 0x1E, 0x1E, 0x0, 0x1000)
    OP_49()
    OP_68(80, 35090, -57000, 0)
    MoveCamera(346, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(19850, 0)
    OP_90(0x0, 0, 46000, -57000, 180)
    OP_90(0x1, -1000, 46000, -56000, 180)
    OP_90(0x2, 1000, 46000, -56000, 180)
    OP_90(0x3, 0, 46000, -55000, 180)
    Sound(832, 2, 100, 0)
    OP_68(0, 31250, -56000, 3000)
    MoveCamera(0, 35, 0, 3000)
    OP_74(0x2, 0xF)
    OP_71(0x2, 0x1E, 0x3C, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(2000)
    OP_24(0x340)
    Sound(149, 0, 60, 0)
    Sleep(1400)
    Sleep(500)
    OP_79(0x2)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_2A42 end

    def Function_13_2B31(): pass

    label("Function_13_2B31")

    SetMapFlags(0x80)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    FadeToBright(0, -1)
    OP_E2(0x3)
    SoundLoad(3840)
    SoundLoad(3841)
    SoundLoad(3842)
    SoundLoad(3843)
    SoundLoad(3844)
    SoundLoad(3845)
    SoundLoad(3846)
    OP_69(0x0, 0x0)
    LoadChrToIndex("apl/ch51741.itc", 0x1E)
    LoadChrToIndex("apl/ch51768.itc", 0x1F)
    SetChrPos(0x101, -46490, 45000, -96480, 305)
    SetChrPos(0x102, -45190, 45430, -95980, 305)
    SetChrPos(0x103, -45390, 45500, -96980, 305)
    SetChrPos(0x104, -46090, 45500, -98480, 305)
    SetChrPos(0xF4, -43890, 45500, -96980, 305)
    SetChrPos(0xF5, -44490, 45500, -98780, 305)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-44890, 45600, -96900, 0)
    MoveCamera(348, 41, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17450, 0)
    Sleep(500)
    OP_68(-53480, 45300, -89160, 4500)
    MoveCamera(346, 25, 0, 4500)
    OP_6E(800, 4500)
    SetCameraDistance(17450, 4500)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 0, 0, 14)
    BeginChrThread(0x102, 0, 0, 15)
    BeginChrThread(0x103, 0, 0, 16)
    BeginChrThread(0x104, 0, 0, 17)
    BeginChrThread(0xF4, 0, 0, 18)
    BeginChrThread(0xF5, 0, 0, 19)
    OP_0D()
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_68(-53480, 45800, -89160, 1500)
    MoveCamera(346, 21, 0, 1500)
    OP_6E(800, 1500)
    SetCameraDistance(16750, 1500)

    def lambda_2CD1():
        OP_93(0x101, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CD1)
    Sleep(50)

    def lambda_2CE1():
        OP_93(0x102, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2CE1)
    Sleep(50)

    def lambda_2CF1():
        OP_93(0x103, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2CF1)
    Sleep(50)

    def lambda_2D01():
        OP_93(0x104, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2D01)
    Sleep(50)

    def lambda_2D11():
        OP_93(0xF4, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2D11)
    Sleep(50)

    def lambda_2D21():
        OP_93(0xF5, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2D21)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0014
    ChrTalk(
        0x101,
        "#00013F#6P这是……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#00101F#12P……新的『门』啊。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#00200F#12P周围还有『结界』……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    BeginChrThread(0x101, 0, 0, 20)
    WaitChrThread(0x101, 0)
    Sleep(300)

    #C0017
    ChrTalk(
        0x101,
        (
            "#00006F#5P不行……\x01",
            "这扇门对我不起反应。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-53960, 46200, -86710, 2000)
    MoveCamera(346, 13, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(17500, 2000)
    OP_6F(0x79)
    Sound(921, 0, 100, 0)
    Sound(921, 0, 100, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3840V#40W#20A……呵呵…………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3841V#40W#38A看来你们已经放倒了谢莉和\x01",
            "那个小鬼，抵达这里了啊……\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x159, 0x1F4)

    #C0020
    ChrTalk(
        0x104,
        "#00307F#6P#N你是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00005F#6P难道你能看到\x01",
            "我们的行动吗！？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3842V#40W#32A呵呵，这简直轻而易举。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3843V#40W#37A好了，\x01",
            "兰道夫，快来吧。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3844V#40W#30A让我们彻底做个了断。\x07\x00\x02",
        )
    )
    #Auto

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_24(0xF04)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_C9(0x1, 0x800)

    #C0025
    ChrTalk(
        0x104,
        "#00311F#6P#N……哈，正合我意。\x02",
    )

    CloseMessageWindow()

    def lambda_30B9():
        OP_96(0xFE, 0xFFFF2B1C, 0xAFC8, 0xFFFE9A94, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30B9)

    def lambda_30D3():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30D3)

    def lambda_30E0():

        label("loc_30E0")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_30E0")

    QueueWorkItem2(0x102, 2, lambda_30E0)

    def lambda_30F2():

        label("loc_30F2")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_30F2")

    QueueWorkItem2(0x103, 2, lambda_30F2)

    def lambda_3104():

        label("loc_3104")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3104")

    QueueWorkItem2(0xF4, 2, lambda_3104)

    def lambda_3116():

        label("loc_3116")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3116")

    QueueWorkItem2(0xF5, 2, lambda_3116)
    Sleep(300)
    OP_68(-54120, 46300, -86290, 2000)
    MoveCamera(346, 13, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(17500, 2000)
    BeginChrThread(0x104, 0, 0, 21)
    Sleep(300)
    WaitChrThread(0x101, 2)

    def lambda_3166():

        label("loc_3166")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3166")

    QueueWorkItem2(0x101, 2, lambda_3166)
    WaitChrThread(0x104, 0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    BeginChrThread(0x104, 0, 0, 22)
    WaitChrThread(0x104, 0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_75(0x6, 0x1, 0x3E8)
    Sleep(2000)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    BeginChrThread(0x104, 0, 0, 23)
    WaitChrThread(0x104, 0)
    ClearMapObjFlags(0x6, 0x2)
    SetMapObjFlags(0x6, 0x4)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3845V#40W#50A呵呵……\x01",
            "那么，我们的『战争』就此开始了。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3846V#40W#47A抛弃一切迷茫与不舍，\x01",
            "飞身冲过来吧。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_24(0xF06)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_C9(0x1, 0x800)
    OP_68(-53550, 46000, -88660, 3500)
    MoveCamera(346, 18, 0, 3500)
    OP_6E(800, 3500)
    SetCameraDistance(16750, 3500)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)

    #C0028
    ChrTalk(
        0x104,
        "#00306F#5P……真是的，父女两人全都一个样子……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        "#00208F#12P#N兰迪前辈……\x02",
    )

    CloseMessageWindow()
    OP_0D()
    OP_5A()

    #C0030
    ChrTalk(
        0x102,
        "#00106F#12P……虽然早有心理准备……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#00006F#6P嗯……\x01",
            "老实说，这个对手实在太难对付了。\x02\x03",

            "#00008F从他在ＩＢＣ门前展现出来的\x01",
            "压倒性实力来判断，\x01",
            "我们的胜算恐怕很低。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34A1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3468")
    OP_FC(0xC)
    Jump("loc_346B")

    label("loc_3468")

    OP_FC(0xFFFA)

    label("loc_346B")


    #C0032
    ChrTalk(
        0x109,
        (
            "#10108F#13P……是啊……\x01",
            "战斗经验差太多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_356A")

    label("loc_34A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3500")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34CB")
    OP_FC(0xC)
    Jump("loc_34CE")

    label("loc_34CB")

    OP_FC(0xFFFA)

    label("loc_34CE")


    #C0033
    ChrTalk(
        0x105,
        (
            "#10408F#13P确实……\x01",
            "实战经验差太多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_356A")

    label("loc_3500")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_356A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_352A")
    OP_FC(0xC)
    Jump("loc_352D")

    label("loc_352A")

    OP_FC(0xFFFA)

    label("loc_352D")


    #C0034
    ChrTalk(
        0x106,
        (
            "#10708F#13P『赤色战鬼』……\x01",
            "我也听说过有关他的传闻……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_356A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3594")
    OP_FC(0xC)
    Jump("loc_3597")

    label("loc_3594")

    OP_FC(0xFFFA)

    label("loc_3597")


    #C0035
    ChrTalk(
        0x10A,
        (
            "#00606F#13P真不愧是大陆最强\x01",
            "猎兵团的首领人物啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_36A8")

    label("loc_35D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3644")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35FF")
    OP_FC(0xC)
    Jump("loc_3602")

    label("loc_35FF")

    OP_FC(0xFFFA)

    label("loc_3602")


    #C0036
    ChrTalk(
        0x106,
        (
            "#10703F#13P『赤色战鬼』……\x01",
            "我也听说过有关他的传闻……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_36A8")

    label("loc_3644")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_366E")
    OP_FC(0xC)
    Jump("loc_3671")

    label("loc_366E")

    OP_FC(0xFFFA)

    label("loc_3671")


    #C0037
    ChrTalk(
        0x105,
        (
            "#10406F#13P真不愧为大陆最强\x01",
            "猎兵团的首领人物啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_36A8")


    #C0038
    ChrTalk(
        0x104,
        (
            "#00303F#5P但是，如果不跨越这道壁障，\x01",
            "我就……我们就无法继续前进。\x02\x03",

            "#00308F另外，还有我自身的问题……\x01",
            "为了给两年前未能做出了断的事情\x01",
            "画上一个完整的句号……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xA0, 0x1F4)
    Sleep(300)

    #C0039
    ChrTalk(
        0x104,
        (
            "#00301F#5P请大家……\x01",
            "助我一臂之力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00000F#6P嗯，当然！\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        "#00202F#12P#N就算你不说，我们也会这么做的。\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_5A()

    #C0042
    ChrTalk(
        0x102,
        (
            "#00109F#12P呵呵……\x01",
            "这不是理所当然的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3849")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3822")
    OP_FC(0xC)
    Jump("loc_3825")

    label("loc_3822")

    OP_FC(0xFFFA)

    label("loc_3825")


    #C0043
    ChrTalk(
        0x109,
        "#10100F#13P请让我也尽一份力！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3849")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38A4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3873")
    OP_FC(0xC)
    Jump("loc_3876")

    label("loc_3873")

    OP_FC(0xFFFA)

    label("loc_3876")


    #C0044
    ChrTalk(
        0x105,
        "#10402F#13P呵呵，就让我略尽绵薄之力吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_38A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38CE")
    OP_FC(0xC)
    Jump("loc_38D1")

    label("loc_38CE")

    OP_FC(0xFFFA)

    label("loc_38D1")


    #C0045
    ChrTalk(
        0x10A,
        "#00604F#13P哼……好吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_38EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3944")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3919")
    OP_FC(0xC)
    Jump("loc_391C")

    label("loc_3919")

    OP_FC(0xFFFA)

    label("loc_391C")


    #C0046
    ChrTalk(
        0x106,
        "#10702F#13P请让我也贡献一份力量。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3944")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, -52940, 45100, -91520, 340)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A8, 6)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_2B31 end

    def Function_14_398D(): pass

    label("Function_14_398D")

    OP_9B(0x0, 0xFE, 0x5, 0x1B58, 0x7D0, 0x0)
    Return()

    # Function_14_398D end

    def Function_15_399D(): pass

    label("Function_15_399D")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x5, 0x1C20, 0x7D0, 0x0)
    Return()

    # Function_15_399D end

    def Function_16_39B0(): pass

    label("Function_16_39B0")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x5, 0xB54, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x163, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x163, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_16_39B0 end

    def Function_17_39E1(): pass

    label("Function_17_39E1")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x5, 0x2198, 0x7D0, 0x0)
    Return()

    # Function_17_39E1 end

    def Function_18_39F4(): pass

    label("Function_18_39F4")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x5, 0x1D4C, 0x7D0, 0x0)
    Return()

    # Function_18_39F4 end

    def Function_19_3A07(): pass

    label("Function_19_3A07")

    Sleep(250)
    OP_9B(0x0, 0xFE, 0x5, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x15A, 0x11C6, 0x7D0, 0x0)
    Return()

    # Function_19_3A07 end

    def Function_20_3A29(): pass

    label("Function_20_3A29")

    OP_95(0xFE, -53580, 45500, -89410, 2000, 0x0)
    OP_93(0xFE, 0x159, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x5)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Return()

    # Function_20_3A29 end

    def Function_21_3ACA(): pass

    label("Function_21_3ACA")

    OP_95(0xFE, -53580, 45500, -89410, 2000, 0x0)
    Return()

    # Function_21_3ACA end

    def Function_22_3ADF(): pass

    label("Function_22_3ADF")

    OP_93(0xFE, 0x159, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_22_3ADF end

    def Function_23_3B20(): pass

    label("Function_23_3B20")

    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    Return()

    # Function_23_3B20 end

    def Function_24_3B42(): pass

    label("Function_24_3B42")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x2, "event/ev17017.eff")
    OP_69(0x0, 0x0)
    OP_68(-61000, 46900, -105500, 0)
    MoveCamera(30, 16, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17850, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(22850, 5000)
    OP_0D()
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -62600, 47500, -108215, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(202, 0, 50, 0)
    Sound(223, 0, 100, 0)
    Sleep(300)
    SetMapObjFrame(0xFF, "magi_07c_add", 0x0, 0x1)
    Sleep(3000)
    StopSound(112, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m9072", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3B42 end

    def Function_25_3C27(): pass

    label("Function_25_3C27")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event/ev202_00.eff")
    OP_69(0x0, 0x0)
    OP_68(-54730, 46000, -89080, 0)
    MoveCamera(31, 42, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13700, 0)
    SetChrPos(0x101, -54250, 45500, -86750, 165)
    SetChrPos(0x102, -54250, 45500, -86750, 165)
    SetChrPos(0x103, -54250, 45500, -86750, 165)
    SetChrPos(0x104, -54250, 45500, -86750, 165)
    SetChrPos(0xF4, -54250, 45500, -86750, 165)
    SetChrPos(0xF5, -54250, 45500, -86750, 165)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFrame(0xFF, "magi_07c_add", 0x0, 0x1)
    SetCameraDistance(14700, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3DA4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3DA4)

    def lambda_3DB5():
        OP_95(0xFE, -53260, 45000, -91480, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DB5)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3E0C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3E0C)

    def lambda_3E1D():
        OP_95(0xFE, -54540, 45000, -91510, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E1D)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3E7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3E7A)

    def lambda_3E8B():
        OP_95(0xFE, -51990, 45000, -90960, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E8B)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3EE2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3EE2)

    def lambda_3EF3():
        OP_95(0xFE, -55840, 45000, -91280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3EF3)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3F50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_3F50)

    def lambda_3F61():
        OP_95(0xFE, -54850, 45600, -90050, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_3F61)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3FB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_3FB8)

    def lambda_3FC9():
        OP_95(0xFE, -53270, 45600, -89890, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_3FC9)
    WaitChrThread(0xF5, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_405C():
        OP_93(0x101, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_405C)
    Sleep(50)

    def lambda_406C():
        OP_93(0x102, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_406C)
    Sleep(50)

    def lambda_407C():
        OP_93(0x103, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_407C)
    Sleep(50)

    def lambda_408C():
        OP_93(0x104, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_408C)
    Sleep(50)

    def lambda_409C():
        OP_93(0xF4, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_409C)
    Sleep(50)

    def lambda_40AC():
        OP_93(0xF5, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_40AC)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_68(-55500, 47000, -99000, 3000)
    MoveCamera(19, 8, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(24100, 3000)
    OP_6F(0x79)

    #C0047
    ChrTalk(
        0x103,
        "#00205F#11P『结界』已经……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#00102F#5P果然如此，只要使『领域』开放，\x01",
            "结界就会随之消除呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#00304F#5P好……！\x01",
            "这样就可以继续前进了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4253")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41B9")
    OP_FC(0x5)
    Jump("loc_41BC")

    label("loc_41B9")

    OP_FC(0xB)

    label("loc_41BC")


    #C0050
    ChrTalk(
        0x109,
        (
            "#10106F#13P不过，刚刚那场战斗\x01",
            "实在太激烈了……\x02\x03",

            "#10100F还是先回梅尔卡瓦\x01",
            "休息一下比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#00000F#11P说的也是……\x01",
            "顺便回去汇报一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D0")

    label("loc_4253")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4317")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_427D")
    OP_FC(0x5)
    Jump("loc_4280")

    label("loc_427D")

    OP_FC(0xB)

    label("loc_4280")


    #C0052
    ChrTalk(
        0x105,
        (
            "#10406F#13P呼……但刚刚那场战斗\x01",
            "实在太激烈了……\x02\x03",

            "#10400F还是先回梅尔卡瓦\x01",
            "休息一下为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00000F#11P说的也是……\x01",
            "顺便回去汇报一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D0")

    label("loc_4317")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43D0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4341")
    OP_FC(0x5)
    Jump("loc_4344")

    label("loc_4341")

    OP_FC(0xB)

    label("loc_4344")


    #C0054
    ChrTalk(
        0x10A,
        (
            "#00606F#13P但我们在刚才一战中\x01",
            "消耗过大……\x02\x03",

            "#00600F还是先返回梅尔卡瓦，\x01",
            "稍作休息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#00000F#11P说的也是……\x01",
            "顺便回去汇报一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -54000, 45200, -91100, 165)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A9, 1)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_3C27 end

    SaveToFile()

Try(main)
