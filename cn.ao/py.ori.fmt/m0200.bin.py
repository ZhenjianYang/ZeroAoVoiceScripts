from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0200.bin",                # FileName
        "m0200",                    # MapName
        "m0200",                    # Location
        0x00A7,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 167, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0200",                  # 0
        "恐怖分子",               # 1
        "恐怖分子",               # 2
        "恐怖分子",               # 3
        "恐怖分子",               # 4
        "恐怖分子",               # 5
        "恐怖分子",               # 6
        "恐怖分子",               # 7
        "亚里欧斯",               # 8
        "达德利搜查官",           # 9
        "银",                     # 10
        "曹",                     # 11
        "刘",                     # 12
        "黑月成员",               # 13
        "黑月成员",               # 14
        "黑月成员",               # 15
        "黑月成员",               # 16
        "黑月成员",               # 17
        "SE控制",                 # 18
        "bm0200",                 # 19
        "bm0200",                 # 20
        "bm0200",                 # 21
    ))

    ATBonus("ATBonus_59C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_44FF", 8,   6,   10,  4,   4,   4,   4)
    Sepith("Sepith_44EF", 2,   0,   20,  2,   4,   5,   2)
    Sepith("Sepith_44F7", 6,   6,   0,   14,  4,   4,   6)

    MonsterBattlePostion("MonsterBattlePostion_5FC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_604", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_608", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_60C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_610", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_614", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_618", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_65C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_660", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_664", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_668", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_66C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_670", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_674", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_678", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5EC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 2, 13, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_80C", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_44FF", 40, 30, 20, 10,
        (
            ("ms84900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84900.dat", "ms84900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84900.dat", "ms84900.dat", "ms84900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84900.dat", "ms84900.dat", "ms84900.dat", "ms84900.dat", 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
        )
    )

    BattleInfo(
        "BattleInfo_67C", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_44EF", 40, 30, 20, 10,
        (
            ("ms84800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84800.dat", "ms84800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84800.dat", "ms84800.dat", "ms84800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
        )
    )

    BattleInfo(
        "BattleInfo_744", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_44F7", 40, 30, 20, 10,
        (
            ("ms79000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms79000.dat", "ms79000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms79000.dat", "ms79000.dat", "ms79000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
            ("ms79000.dat", "ms79000.dat", "ms79000.dat", "ms79000.dat", 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_59C"),
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
        "monster/ch84850.itc",               # 10
        "monster/ch84850.itc",               # 11
        "monster/ch79050.itc",               # 12
        "monster/ch79050.itc",               # 13
        "monster/ch84950.itc",               # 14
        "monster/ch84951.itc",               # 15
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-200000, -199600, 4000,    0x10100E1,    "BattleInfo_80C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-404090, -192150, 0,       0x1010087,    "BattleInfo_67C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-402310, -207460, -6000,   0x101013B,    "BattleInfo_744", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-204160, -5390,   -2000,   0x10100A0,    "BattleInfo_80C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-200370, -208600, -2000,   0x101010A,    "BattleInfo_67C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-216200, -208060, -2000,   0x1010047,    "BattleInfo_744", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-196370, -400520, 0,       0x1010001,    "BattleInfo_80C", 0,   20,  0xFFFF, 4,  5)

    DeclEvent(0x0000, 0, 8,   -6.5,                  0.0,                   1.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   3.25,                  -0.0,                  -0.19999998807907104,  1.0])

    DeclActor(2500,    2000,    5500,    1200,    2500,    3000,    5500,    0x007C, 0,  11, 0x0000)
    DeclActor(2500,    -20000,  5500,    1200,    2500,    -19000,  5500,    0x007C, 0,  12, 0x0000)
    DeclActor(-190110, 6000,    -591770, 1200,    -190110, 8000,    -591770, 0x007C, 0,  10, 0x0000)
    DeclActor(-388000, 0,       -762500, 1200,    -388000, 1000,    -762500, 0x007C, 0,  13, 0x0000)
    DeclActor(187500,  0,       242000,  1200,    187500,  1000,    242000,  0x007C, 0,  15, 0x0000)
    DeclActor(-400000, -6000,   -208000, 1200,    -400000, -5000,   -208000, 0x007C, 0,  3,  0x0000)
    DeclActor(-406000, 0,       -400000, 1200,    -406000, 1000,    -400000, 0x007C, 0,  4,  0x0000)
    DeclActor(-195500, 6000,    -9000,   1200,    -195500, 7000,    -9000,   0x007C, 0,  5,  0x0000)
    DeclActor(-397000, 0,       -778000, 1200,    -397000, 1000,    -778000, 0x007C, 0,  6,  0x0000)
    DeclActor(204000,  -2000,   -203000, 1200,    204000,  -1000,   -203000, 0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 5

    ScpFunction((
        "Function_0_9B0",          # 00, 0
        "Function_1_A60",          # 01, 1
        "Function_2_B61",          # 02, 2
        "Function_3_DFB",          # 03, 3
        "Function_4_F36",          # 04, 4
        "Function_5_109D",         # 05, 5
        "Function_6_11D8",         # 06, 6
        "Function_7_1313",         # 07, 7
        "Function_8_144E",         # 08, 8
        "Function_9_15E8",         # 09, 9
        "Function_10_1771",        # 0A, 10
        "Function_11_17F6",        # 0B, 11
        "Function_12_1986",        # 0C, 12
        "Function_13_1B0B",        # 0D, 13
        "Function_14_1C94",        # 0E, 14
        "Function_15_1DC4",        # 0F, 15
        "Function_16_1F4D",        # 10, 16
        "Function_17_207D",        # 11, 17
        "Function_18_2996",        # 12, 18
        "Function_19_29D9",        # 13, 19
        "Function_20_2A77",        # 14, 20
        "Function_21_2B15",        # 15, 21
        "Function_22_2C04",        # 16, 22
        "Function_23_2E08",        # 17, 23
        "Function_24_3013",        # 18, 24
        "Function_25_3050",        # 19, 25
        "Function_26_30A1",        # 1A, 26
        "Function_27_389D",        # 1B, 27
        "Function_28_40BE",        # 1C, 28
        "Function_29_410C",        # 1D, 29
        "Function_30_415A",        # 1E, 30
        "Function_31_41AF",        # 1F, 31
        "Function_32_4204",        # 20, 32
        "Function_33_4259",        # 21, 33
        "Function_34_42AE",        # 22, 34
        "Function_35_4366",        # 23, 35
        "Function_36_43C7",        # 24, 36
    ))


    def Function_0_9B0(): pass

    label("Function_0_9B0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_9E8"),
        (1, "loc_9F4"),
        (2, "loc_A00"),
        (3, "loc_A0C"),
        (4, "loc_A18"),
        (5, "loc_A24"),
        (6, "loc_A30"),
        (SWITCH_DEFAULT, "loc_A3C"),
    )


    label("loc_9E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_9F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A00")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A0C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A18")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A24")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A30")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A3C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A5F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A48")

    label("loc_A5F")

    Return()

    # Function_0_9B0 end

    def Function_1_A60(): pass

    label("Function_1_A60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x84), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A7D")
    OP_C9(0x1, 0x1000)

    label("loc_A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA8")
    SetMapFlags(0x10000000)
    Event(0, 9)

    label("loc_AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_ABC")
    ClearScenarioFlags(0x22, 0)
    Event(0, 34)
    Jump("loc_ACB")

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_ACB")
    ClearScenarioFlags(0x22, 1)
    Event(0, 17)

    label("loc_ACB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE5")
    Event(0, 26)

    label("loc_AE5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFF")
    Event(0, 27)

    label("loc_AFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B10")
    SetScenarioFlags(0x194, 0)

    label("loc_B10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B2F")
    ClearScenarioFlags(0x0, 0)
    Jump("loc_B32")

    label("loc_B2F")

    SetScenarioFlags(0x0, 0)

    label("loc_B32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B49")
    Event(0, 14)

    label("loc_B49")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B60")
    Event(0, 16)

    label("loc_B60")

    Return()

    # Function_1_A60 end

    def Function_2_B61(): pass

    label("Function_2_B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 0)), scpexpr(EXPR_END)), "loc_B91")
    SetMapObjFrame(0x3, "lock_g", 0x1, 0x1)
    SetMapObjFrame(0x3, "lock_r", 0x0, 0x1)
    SetMapObjFlags(0x3, 0x10)
    Jump("loc_BB3")

    label("loc_B91")

    SetMapObjFrame(0x3, "lock_g", 0x0, 0x1)
    SetMapObjFrame(0x3, "lock_r", 0x1, 0x1)
    ClearMapObjFlags(0x3, 0x10)

    label("loc_BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCE")
    OP_71(0x10, 0x0, 0x5, 0x0, 0x20)
    Jump("loc_BDA")

    label("loc_BCE")

    OP_71(0x10, 0x78, 0x7D, 0x0, 0x20)

    label("loc_BDA")

    OP_10(0x1, 0x0)
    OP_10(0x18, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3D")
    SetMapObjFrame(0x12, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)
    SetMapObjFrame(0x11, "Null_color2", 0x0, 0x1)
    SetMapObjFrame(0x11, "Null_color", 0x0, 0x1)
    Jump("loc_D03")

    label("loc_C3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7B")
    SetMapObjFrame(0x12, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x1, 0x1)
    Jump("loc_CA0")

    label("loc_C7B")

    SetMapObjFrame(0x12, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)

    label("loc_CA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDE")
    SetMapObjFrame(0x11, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x11, "Null_color2", 0x0, 0x1)
    Jump("loc_D03")

    label("loc_CDE")

    SetMapObjFrame(0x11, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x11, "Null_color2", 0x1, 0x1)

    label("loc_D03")

    ClearMapObjFlags(0x5, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D22")
    OP_70(0x5, 0x0)
    SetMapObjFlags(0x14, 0x4)
    Jump("loc_D3B")

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D3B")
    SetMapObjFlags(0x14, 0x4)
    OP_70(0x5, 0x28)
    ClearMapObjFlags(0x5, 0x2)

    label("loc_D3B")

    OP_10(0x20, 0x0)
    OP_10(0x22, 0x0)
    OP_10(0x0, 0x0)
    OP_10(0x21, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A")
    OP_70(0x0, 0x0)
    Jump("loc_D5E")

    label("loc_D5A")

    OP_70(0x0, 0x1E)

    label("loc_D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D71")
    OP_70(0x1, 0x0)
    Jump("loc_D75")

    label("loc_D71")

    OP_70(0x1, 0x1E)

    label("loc_D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D88")
    OP_70(0x13, 0x0)
    Jump("loc_D8C")

    label("loc_D88")

    OP_70(0x13, 0x1E)

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9F")
    OP_70(0x15, 0x0)
    Jump("loc_DA3")

    label("loc_D9F")

    OP_70(0x15, 0x1E)

    label("loc_DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB6")
    OP_70(0x16, 0x0)
    Jump("loc_DBA")

    label("loc_DB6")

    OP_70(0x16, 0x1E)

    label("loc_DBA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x84), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DF4")
    OP_24(0x85)
    Jump("loc_DFA")

    label("loc_DF4")

    Sound(133, 1, 100, 0)

    label("loc_DFA")

    Return()

    # Function_2_B61 end

    def Function_3_DFB(): pass

    label("Function_3_DFB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EED")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('星辰灵摆', 1)"), scpexpr(EXPR_END)), "loc_E7E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '星辰灵摆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_EE8")

    label("loc_E7E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '星辰灵摆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '星辰灵摆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EE8")

    Jump("loc_F2A")

    label("loc_EED")

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

    label("loc_F2A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_DFB end

    def Function_4_F36(): pass

    label("Function_4_F36")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106E")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 100)
    AddSepith(0x1, 100)
    AddSepith(0x2, 100)
    AddSepith(0x3, 100)
    AddSepith(0x4, 100)
    AddSepith(0x5, 100)
    AddSepith(0x6, 100)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×１００\x01\x07\x02",

            "#57I水之耀晶片×１００\x01\x07\x02",

            "#58I火之耀晶片×１００\x01\x07\x02",

            "#59I风之耀晶片×１００\x01\x07\x02",

            "#60I时之耀晶片×１００\x01\x07\x02",

            "#61I空之耀晶片×１００\x01\x07\x02",

            "#62I幻之耀晶片×１００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1FC, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_108B")

    label("loc_106E")


    #A0005
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

    label("loc_108B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_F36 end

    def Function_5_109D(): pass

    label("Function_5_109D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118F")
    Sound(14, 0, 100, 0)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('龙华树之服', 1)"), scpexpr(EXPR_END)), "loc_1120")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '龙华树之服'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_118A")

    label("loc_1120")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '龙华树之服'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '龙华树之服'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x13, 0x1E, 0x0, 0x0, 0x0)

    label("loc_118A")

    Jump("loc_11CC")

    label("loc_118F")

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

    label("loc_11CC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_109D end

    def Function_6_11D8(): pass

    label("Function_6_11D8")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CA")
    Sound(14, 0, 100, 0)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅲ', 1)"), scpexpr(EXPR_END)), "loc_125B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E9, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_12C5")

    label("loc_125B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x15, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12C5")

    Jump("loc_1307")

    label("loc_12CA")

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

    label("loc_1307")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_11D8 end

    def Function_7_1313(): pass

    label("Function_7_1313")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1405")
    Sound(14, 0, 100, 0)
    OP_74(0x16, 0x1E)
    OP_71(0x16, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药·改', 1)"), scpexpr(EXPR_END)), "loc_1396")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E9, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1400")

    label("loc_1396")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x16, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1400")

    Jump("loc_1442")

    label("loc_1405")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0014
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

    label("loc_1442")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1313 end

    def Function_8_144E(): pass

    label("Function_8_144E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15E7")
    EventBegin(0x0)
    Fade(500)
    OP_68(-3720, 2000, 1200, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17960, 0)
    SetChrPos(0x101, -5200, 2000, 0, 90)
    SetChrPos(0x104, -5200, 2000, -1200, 90)
    SetChrPos(0x102, -5200, 2000, 1200, 90)
    SetChrPos(0x109, -6200, 2000, 0, 90)
    SetChrPos(0x103, -6200, 2000, -1200, 90)
    SetChrPos(0x105, -6200, 2000, 1200, 90)
    SetChrPos(0x13E, -2930, 2000, 40, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0015
    ChrTalk(
        0x13E,
        "#11P#02305F嗯？你们要出去吗？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，稍微有点事情。\x01",
            "准备完毕之后，马上就会回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x13E,
        (
            "#11P#02306F啧，动作要快点哦，\x01",
            "我就在这里等你们。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    RemoveParty(0x3D, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c120D", 0, 0, 0)
    IdleLoop()

    label("loc_15E7")

    Return()

    # Function_8_144E end

    def Function_9_15E8(): pass

    label("Function_9_15E8")

    EventBegin(0x0)
    AddParty(0x3D, 0xFF, 0xFF)
    Fade(500)
    OP_68(-3720, 2000, 1200, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17960, 0)
    SetChrPos(0x101, -5200, 2000, 0, 90)
    SetChrPos(0x104, -5200, 2000, -1200, 90)
    SetChrPos(0x102, -5200, 2000, 1200, 90)
    SetChrPos(0x109, -6200, 2000, 0, 90)
    SetChrPos(0x103, -6200, 2000, -1200, 90)
    SetChrPos(0x105, -6200, 2000, 1200, 90)
    SetChrPos(0x13E, -2930, 2000, 40, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0018
    ChrTalk(
        0x13E,
        (
            "#11P#02305F哦，你们回来了啊。\x02\x03",

            "#02302F好，那我们就赶快去\x01",
            "第四终端的控制室吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，知道了，\x01",
            "要跟紧我们哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -5200, 2000, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    ClearMapFlags(0x10000000)
    Return()

    # Function_9_15E8 end

    def Function_10_1771(): pass

    label("Function_10_1771")

    EventBegin(0x1)

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有个梯子。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F3")
    FadeToDark(500, 0, -1)
    OP_0D()
    EventEnd(0x5)
    OP_C9(0x0, 0x1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_17E5")
    NewScene("c120D", 105, 0, 0)
    IdleLoop()
    Jump("loc_17EE")

    label("loc_17E5")

    NewScene("c1200", 108, 0, 0)
    IdleLoop()

    label("loc_17EE")

    Jump("loc_17F5")

    label("loc_17F3")

    EventEnd(0x5)

    label("loc_17F5")

    Return()

    # Function_10_1771 end

    def Function_11_17F6(): pass

    label("Function_11_17F6")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以操作导力梯的控制面板。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197E")
    Fade(500)
    SetChrPos(0x0, 1400, 2000, 5300, 90)
    SetChrPos(0x1, 1400, 2000, 6300, 90)
    SetChrPos(0x2, 0, 2000, 5300, 90)
    SetChrPos(0x3, 0, 2000, 6300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18BF")
    SetChrPos(0x13E, -1000, 2000, 5800, 90)

    label("loc_18BF")

    OP_68(1280, 2000, 6880, 0)
    MoveCamera(21, 44, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14970, 0)
    OP_0D()
    Sleep(500)
    Sound(143, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x10, 0x5, 0x78, 0x0, 0x0)
    Sleep(200)
    Sound(145, 0, 100, 0)
    Sleep(800)
    Fade(500)
    OP_68(1280, -10000, 6880, 0)
    MoveCamera(21, 38, 0, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_68(1280, -20000, 6880, 1800)
    Sleep(2200)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x10)
    OP_6F(0x1)
    SetScenarioFlags(0x0, 0)

    label("loc_197E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_17F6 end

    def Function_12_1986(): pass

    label("Function_12_1986")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以操作导力梯的控制面板。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B03")
    Fade(500)
    SetChrPos(0x0, 1400, -20000, 5300, 90)
    SetChrPos(0x1, 1400, -20000, 6300, 90)
    SetChrPos(0x2, 200, -20000, 5300, 90)
    SetChrPos(0x3, 200, -20000, 6300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A4F")
    SetChrPos(0x13E, -1000, -20000, 5800, 90)

    label("loc_1A4F")

    OP_68(1280, -20000, 6880, 0)
    MoveCamera(21, 44, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14970, 0)
    OP_0D()
    Sleep(500)
    Sound(143, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x10, 0x7D, 0xF5, 0x0, 0x0)
    OP_68(1280, -12000, 6880, 2000)
    Sleep(200)
    Sound(145, 0, 100, 0)
    Sleep(1800)
    Fade(500)
    OP_68(1280, 2000, 6880, 0)
    SetCameraDistance(16970, 0)
    OP_0D()
    Sleep(1300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x10)
    OP_6F(0x1)
    ClearScenarioFlags(0x0, 0)

    label("loc_1B03")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_1986 end

    def Function_13_1B0B(): pass

    label("Function_13_1B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B1D")
    Call(0, 36)
    Return()

    label("loc_1B1D")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0023
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C8C")
    Fade(500)
    SetChrPos(0x0, -387500, 0, -764000, 0)
    SetChrPos(0x1, -388500, 0, -764000, 0)
    SetChrPos(0x2, -387500, 0, -765000, 0)
    SetChrPos(0x3, -388500, 0, -765000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE9")
    SetChrPos(0x13E, -388000, 0, -766000, 0)

    label("loc_1BE9")

    OP_68(-387800, 0, -763430, 0)
    MoveCamera(50, 53, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x12, 0x104, 0x1C2, 0x0, 0x0)
    Sleep(200)
    OP_68(-387600, 0, -753410, 3800)
    MoveCamera(31, 61, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0202", 100, 0, 0)
    IdleLoop()

    label("loc_1C8C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_1B0B end

    def Function_14_1C94(): pass

    label("Function_14_1C94")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x12, 0x64)
    Sleep(1)
    OP_68(-385270, 0, -759650, 0)
    MoveCamera(35, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, -390000, -1290, -754000, 270)
    OP_90(0x1, -390000, -1290, -755000, 270)
    OP_90(0x2, -389000, -1290, -754000, 270)
    OP_90(0x3, -389000, -1290, -755000, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D41")
    SetChrPos(0x13E, -388500, -2500, -753000, 270)

    label("loc_1D41")

    Sound(145, 0, 100, 0)
    OP_68(-390500, 0, -764340, 3200)
    MoveCamera(43, 43, 0, 3200)
    OP_71(0x12, 0x15E, 0x104, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x12)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x12, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_1C94 end

    def Function_15_1DC4(): pass

    label("Function_15_1DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DD6")
    Call(0, 36)
    Return()

    label("loc_1DD6")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0024
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F45")
    Fade(500)
    SetChrPos(0x0, 189000, 0, 241500, 270)
    SetChrPos(0x1, 189000, 0, 242500, 270)
    SetChrPos(0x2, 190000, 0, 241500, 270)
    SetChrPos(0x3, 190000, 0, 242500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EA2")
    SetChrPos(0x13E, 192500, 0, 242000, 270)

    label("loc_1EA2")

    OP_68(190000, 0, 242550, 0)
    MoveCamera(42, 49, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x11, 0x2F8, 0x3B6, 0x0, 0x0)
    Sleep(200)
    OP_68(177000, -2000, 241550, 3800)
    MoveCamera(62, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(7000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0209", 101, 0, 0)
    IdleLoop()

    label("loc_1F45")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_1DC4 end

    def Function_16_1F4D(): pass

    label("Function_16_1F4D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x11, 0x352)
    Sleep(1)
    OP_68(180000, -2500, 240000, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 178000, -2500, 239500, 180)
    OP_90(0x1, 177000, -2500, 239500, 180)
    OP_90(0x2, 178000, -2500, 240500, 180)
    OP_90(0x3, 177000, -2500, 240500, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFA")
    SetChrPos(0x13E, 177500, -2500, 250500, 180)

    label("loc_1FFA")

    Sound(145, 0, 100, 0)
    OP_68(193500, 0, 239000, 3200)
    MoveCamera(43, 43, 0, 3200)
    OP_71(0x11, 0x352, 0x2F8, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x11)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x11, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x11, "Null_color2", 0x1, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_16_1F4D end

    def Function_17_207D(): pass

    label("Function_17_207D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch42500.itc", 0x20)
    LoadChrToIndex("chr/ch00500.itc", 0x21)
    LoadChrToIndex("chr/ch06300.itc", 0x22)
    LoadChrToIndex("chr/ch31400.itc", 0x23)
    LoadChrToIndex("chr/ch31500.itc", 0x24)
    LoadChrToIndex("chr/ch12500.itc", 0x25)
    LoadChrToIndex("chr/ch42553.itc", 0x26)
    LoadChrToIndex("apl/ch50220.itc", 0x27)
    SoundLoad(844)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -212000, -2000, -207300, 90)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -212200, -2000, -208600, 90)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -205000, -2000, -208800, 270)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -205000, -2000, -206500, 180)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x3)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -203600, -2000, -208800, 0)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -203600, -2000, -206500, 225)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x3)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -202300, -2000, -208000, 135)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x3)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -202600, -2000, -210000, 315)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x3)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -204600, -2000, -210200, 270)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -206600, -2000, -206600, 270)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -207400, -2000, -208000, 270)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -206900, -2000, -209000, 270)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -204800, -2000, -211600, 0)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -204300, -2000, -205100, 180)
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -202900, -2000, -211400, 0)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -201800, -2000, -206400, 225)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -201000, -2000, -208900, 270)
    OP_68(-208800, 9500, -208000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(22000, 0)
    OP_68(-208800, -500, -208000, 10000)
    SetCameraDistance(17000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    PlaceName2(100, 40, "c_plac54", 0x0, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-208300, -1100, -208000, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    def lambda_23C1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_23C1)
    Sleep(500)

    #C0025
    ChrTalk(
        0x8,
        (
            "#5P#30W啧……\x01",
            "是『黑月』的人……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2405():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2405)
    Sleep(500)

    #C0026
    ChrTalk(
        0xE,
        (
            "#11P#30W怎么会……\x01",
            "这些家伙为何出现在这里……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0027
    ChrTalk(
        0x10,
        (
            "#6P#00607F──曹先生！\x01",
            "那些人有重大犯罪嫌疑！\x02\x03",

            "就算你们有共和国政府的委托书，\x01",
            "也无权将他们带走！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x12,
        (
            "#03204F#11P呵呵，话虽如此，\x01",
            "但这是公司上层──也就是长老们的命令。\x02\x03",

            "#03210F如果你们无法接受，\x01",
            "就算动用武力也无妨哦。\x02\x03",

            "凭『风之剑圣』先生的实力，想必可以\x01",
            "和我们的朋友展开一场精彩的对决呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#5P…………哼………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xF,
        (
            "#6P#01401F……传说中的刺客『银』，\x01",
            "我们还是初次见面呢。\x02\x03",

            "#01403F其他人似乎也都是高手……\x01",
            "看来形势对我们有些不利。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x10,
        "#6P#00610F……啧……………\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x12,
        (
            "#03209F#11P呵呵，不必担心。\x01",
            "他们的下场并不会像\x01",
            "另一批恐怖分子那么悲惨。\x02\x03",

            "#03202F我们只会将他们作为政治犯\x01",
            "来利用，以便牵制那些\x01",
            "民族主义者。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0033
    ChrTalk(
        0x8,
        "#5P别、别开玩笑了！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xE,
        (
            "#11P都是因为你们这群可恶的东方人，\x01",
            "我们卡尔瓦德才会——\x02",
        )
    )

    CloseMessageWindow()

    def lambda_273B():
        OP_99(0xFE, 0xE, 0x258, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_273B)
    WaitChrThread(0x14, 1)

    def lambda_2753():
        OP_96(0xFE, 0xFFFCE000, 0xFFFFF830, 0xFFFCC570, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2753)
    Sound(811, 0, 100, 0)

    def lambda_2773():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2773)
    Sleep(500)

    #C0035
    ChrTalk(
        0xE,
        "#11P唔……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x10,
        (
            "#6P#00606F洛克史密斯总统……\x01",
            "似乎是一只比想象中更加狡猾的老狐狸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x12,
        (
            "#03204F#11P呵呵，我个人却觉得\x01",
            "和总统大人很有亲近感呢。\x02\x03",

            "#03210F如果你们有什么不满，\x01",
            "请去总统府抗议……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0x5A, 0x1F4)
    Sleep(150)

    #C0038
    ChrTalk(
        0x12,
        "#6P#03209F我们走吧。\x02",
    )

    CloseMessageWindow()

    def lambda_2878():
        TurnDirection(0x13, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2878)
    Sleep(50)

    def lambda_2888():
        TurnDirection(0x14, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2888)
    Sleep(50)

    def lambda_2898():
        TurnDirection(0x15, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2898)
    Sleep(50)

    def lambda_28A8():
        TurnDirection(0x16, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_28A8)
    Sleep(50)

    def lambda_28B8():
        TurnDirection(0x17, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_28B8)
    Sleep(50)

    def lambda_28C8():
        TurnDirection(0x18, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_28C8)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    WaitChrThread(0x16, 0)
    WaitChrThread(0x17, 0)
    WaitChrThread(0x18, 0)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("众成员")

    #A0039
    AnonymousTalk(
        0xFF,
        "#4S是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0040
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#5P………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20500, 5500)
    BeginChrThread(0xF, 3, 0, 18)
    Sleep(3500)
    StopSound(133, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    SetScenarioFlags(0x23, 1)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_207D end

    def Function_18_2996(): pass

    label("Function_18_2996")

    BeginChrThread(0x17, 3, 0, 23)
    Sleep(300)
    BeginChrThread(0x18, 3, 0, 21)
    Sleep(300)
    BeginChrThread(0x11, 3, 0, 25)
    BeginChrThread(0x15, 3, 0, 22)
    Sleep(600)
    BeginChrThread(0x14, 3, 0, 19)
    Sleep(200)
    BeginChrThread(0x16, 3, 0, 20)
    Sleep(1400)
    BeginChrThread(0x12, 3, 0, 24)
    Sleep(800)
    BeginChrThread(0x13, 3, 0, 24)
    Return()

    # Function_18_2996 end

    def Function_19_29D9(): pass

    label("Function_19_29D9")


    def lambda_29DE():
        OP_95(0xFE, -204700, -2000, -210900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_29DE)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    OP_93(0xE, 0x0, 0x1F4)

    def lambda_2A0B():
        OP_98(0xFE, 0x0, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2A0B)

    def lambda_2A25():
        OP_98(0xFE, 0x0, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2A25)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x14, 1)

    def lambda_2A47():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2A47)

    def lambda_2A61():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2A61)
    Return()

    # Function_19_29D9 end

    def Function_20_2A77(): pass

    label("Function_20_2A77")


    def lambda_2A7C():
        OP_95(0xFE, -202800, -2000, -210500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2A7C)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xD, 0x0, 0x1F4)

    def lambda_2AA9():
        OP_98(0xFE, 0x0, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2AA9)

    def lambda_2AC3():
        OP_98(0xFE, 0x0, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2AC3)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x16, 1)

    def lambda_2AE5():
        OP_97(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2AE5)

    def lambda_2AFF():
        OP_97(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2AFF)
    Return()

    # Function_20_2A77 end

    def Function_21_2B15(): pass

    label("Function_21_2B15")


    def lambda_2B1A():
        OP_95(0xFE, -202200, -2000, -207400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2B1A)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x0, 0x1F4)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    OP_93(0xC, 0xB4, 0x0)

    def lambda_2B4E():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B4E)

    def lambda_2B68():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2B68)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x18, 1)

    def lambda_2B8A():
        OP_98(0xFE, 0x0, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B8A)

    def lambda_2BA4():
        OP_98(0xFE, 0x0, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2BA4)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x18, 1)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0x18, 0x10E, 0x0)

    def lambda_2BD4():
        OP_97(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2BD4)

    def lambda_2BEE():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2BEE)
    Return()

    # Function_21_2B15 end

    def Function_22_2C04(): pass

    label("Function_22_2C04")


    def lambda_2C09():
        OP_95(0xFE, -204200, -2000, -205900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2C09)
    WaitChrThread(0x15, 1)
    Fade(250)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, -204300, -2200, -206700, 180)

    def lambda_2C46():
        OP_98(0xFE, 0x0, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2C46)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    SetChrPos(0xB, -203500, -2200, -206700, 180)

    def lambda_2C7A():
        OP_98(0xFE, 0x0, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2C7A)

    def lambda_2C94():
        OP_98(0xFE, 0x0, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2C94)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 1)

    def lambda_2CBA():
        OP_9E(0xFE, 0xFFFCE258, 0xFFFD04B8, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2CBA)

    def lambda_2CD5():
        OP_9E(0xFE, 0xFFFCE258, 0xFFFD04B8, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2CD5)

    def lambda_2CF0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2CF0)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 2)

    def lambda_2D09():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2D09)

    def lambda_2D23():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D23)

    def lambda_2D3D():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2D3D)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 1)

    def lambda_2D63():
        OP_9E(0xFE, 0xFFFCF5E0, 0xFFFD04B8, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2D63)

    def lambda_2D7E():
        OP_9E(0xFE, 0xFFFCF5E0, 0xFFFD04B8, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D7E)

    def lambda_2D99():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2D99)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 2)

    def lambda_2DB2():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2DB2)

    def lambda_2DCC():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2DCC)

    def lambda_2DE6():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2DE6)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x15, 1)
    Return()

    # Function_22_2C04 end

    def Function_23_2E08(): pass

    label("Function_23_2E08")


    def lambda_2E0D():
        OP_95(0xFE, -204400, -2000, -208000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2E0D)
    WaitChrThread(0x17, 1)
    OP_93(0x17, 0xB4, 0x1F4)
    Fade(250)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, -204500, -2200, -208800, 180)

    def lambda_2E51():
        OP_98(0xFE, 0x0, 0x0, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2E51)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    SetChrPos(0xA, -203700, -2200, -208800, 180)

    def lambda_2E85():
        OP_98(0xFE, 0x0, 0x0, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2E85)

    def lambda_2E9F():
        OP_98(0xFE, 0x0, 0x0, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2E9F)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 1)

    def lambda_2EC5():
        OP_9E(0xFE, 0xFFFCE190, 0xFFFD006C, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2EC5)

    def lambda_2EE0():
        OP_9E(0xFE, 0xFFFCE190, 0xFFFD006C, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2EE0)

    def lambda_2EFB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2EFB)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 2)

    def lambda_2F14():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F14)

    def lambda_2F2E():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2F2E)

    def lambda_2F48():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2F48)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 1)

    def lambda_2F6E():
        OP_9E(0xFE, 0xFFFCF518, 0xFFFD006C, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F6E)

    def lambda_2F89():
        OP_9E(0xFE, 0xFFFCF518, 0xFFFD006C, 0xFFFEA070, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2F89)

    def lambda_2FA4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2FA4)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 2)

    def lambda_2FBD():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2FBD)

    def lambda_2FD7():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2FD7)

    def lambda_2FF1():
        OP_98(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2FF1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x17, 1)
    Return()

    # Function_23_2E08 end

    def Function_24_3013(): pass

    label("Function_24_3013")


    def lambda_3018():
        OP_95(0xFE, -204700, -2000, -207600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3018)
    WaitChrThread(0xFE, 1)

    def lambda_3036():
        OP_95(0xFE, -204700, -2000, -197300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3036)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_3013 end

    def Function_25_3050(): pass

    label("Function_25_3050")

    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(700)
    SetChrSubChip(0x11, 0x0)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(844, 0, 100, 0)

    def lambda_3084():
        OP_9C(0xFE, 0x0, 0x1B58, 0x2710, 0x2328, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3084)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_3050 end

    def Function_26_30A1(): pass

    label("Function_26_30A1")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -182900, 4000, -199900, 270)
    SetChrPos(0x102, -182900, 4000, -201200, 270)
    SetChrPos(0x103, -181800, 4000, -200000, 270)
    SetChrPos(0x104, -181800, 4000, -198700, 270)
    SetChrPos(0x109, -180700, 4000, -199900, 270)
    SetChrPos(0x105, -180700, 4000, -201200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x13E, -179400, 4000, -200000, 270)
    OP_68(-191500, -1000, -201500, 0)
    MoveCamera(55, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_68(-191500, -1000, -201500, 6000)
    MoveCamera(65, 19, 0, 6000)
    SetCameraDistance(20500, 6000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-182000, 4000, -199500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(15000, 0)
    OP_68(-211000, 4000, -196000, 9000)
    MoveCamera(65, 13, 0, 9000)
    SetCameraDistance(23000, 9000)
    OP_0D()
    Sleep(5500)
    PlaceName2(340, 200, "c_plac54", 0x0, 0)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-180900, 5000, -200350, 0)
    MoveCamera(60, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    #C0041
    ChrTalk(
        0x101,
        "#11P#00011F这……真是一处很惊人的场所。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        (
            "#11P#00200F据资料库的记载，\x01",
            "这里是热处理设备及\x01",
            "垃圾焚化场所在的区域。\x02\x03",

            "#00203F据说，通过引入羽扇河的水，\x01",
            "可以对设备进行冷却处理……\x02\x03",

            "而且今后甚至有可能实现\x01",
            "将蒸气覆盖至整个都市\x01",
            "进行中央供暖。\x02\x03",

            "#00211F但这终究只是当初的预想而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        (
            "#00306F#5P该怎么说呢……\x01",
            "这种面子工程真是很要命啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#11P#00106F是啊……\x01",
            "看来这个区域也没有\x01",
            "被有效利用到。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10305F#11P话说回来……\x02\x03",

            "#10301F这里不就是达德利他们\x01",
            "在通商会议时追击\x01",
            "恐怖分子的地方吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_348C():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_348C)
    Sleep(50)

    def lambda_349C():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_349C)
    Sleep(50)

    def lambda_34AC():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_34AC)
    Sleep(50)

    def lambda_34BC():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_34BC)
    Sleep(50)

    def lambda_34CC():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_34CC)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    #C0046
    ChrTalk(
        0x101,
        "#6P#00001F如此说来，还真是呢……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x109,
        (
            "#10106F他们当时似乎让\x01",
            "『黑月』捷足先登了……\x02\x03",

            "#10108F总觉得好像是\x01",
            "发生在很久以前的事情一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#6P#00108F但其实刚刚\x01",
            "过去两个月左右……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x13E, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0049
    ChrTalk(
        0x13E,
        (
            "#02311F#11P好啦好啦，现在可不是\x01",
            "多愁善感的时候啊！\x02\x03",

            "#02310F这里又热又闷，难受死了，\x01",
            "所以我才讨厌现实世界……\x02\x03",

            "#02306F但愿终端室中的\x01",
            "冷气设备不要坏掉……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_36F2():
        TurnDirection(0x102, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_36F2)
    Sleep(50)

    def lambda_3702():
        TurnDirection(0x109, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3702)
    Sleep(50)

    def lambda_3712():
        TurnDirection(0x105, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3712)
    Sleep(50)

    def lambda_3722():
        TurnDirection(0x104, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3722)
    Sleep(50)

    def lambda_3732():
        TurnDirection(0x103, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3732)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0050
    ChrTalk(
        0x101,
        "#6P#00006F我说你啊……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x103,
        (
            "#00211F#6P既然你有这么多不满，\x01",
            "我们不如回去好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x13E,
        (
            "#02309F#11P没、没有没有！\x01",
            "我连半点不满也没有啊！\x02\x03",

            "#02302F『第四控制终端』应该在\x01",
            "这个区域的最深处。\x02\x03",

            "我们赶快过去\x01",
            "吹吹冷风吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        "#00306F真是的……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x109,
        (
            "#10112F#6P呵呵……\x01",
            "那就走吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -181000, 4000, -200000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x181, 5)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_26_30A1 end

    def Function_27_389D(): pass

    label("Function_27_389D")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    OP_68(-400000, -900, -579300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -400000, -2000, -577000, 180)
    SetChrPos(0x102, -400000, -2000, -577000, 180)
    SetChrPos(0x103, -400000, -2000, -577000, 180)
    SetChrPos(0x104, -400000, -2000, -577000, 180)
    SetChrPos(0x109, -400000, -2000, -577000, 180)
    SetChrPos(0x105, -400000, -2000, -577000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x13E, -400000, -2000, -577000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-399150, -900, -583440, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(102, 0, 100, 0)
    ClearMapObjFlags(0xC, 0x10)
    OP_71(0xC, 0x0, 0xA, 0x0, 0x0)
    OP_79(0xC)
    BeginChrThread(0x101, 3, 0, 28)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 29)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 30)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 32)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 33)
    Sleep(700)

    def lambda_3A2D():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71D64, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_3A2D)

    def lambda_3A47():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13E, 2, lambda_3A47)
    Sleep(1000)
    Sound(102, 0, 100, 0)
    OP_71(0xC, 0xA, 0x0, 0x0, 0x0)
    OP_79(0xC)
    SetMapObjFlags(0xC, 0x10)
    WaitChrThread(0x13E, 1)

    #C0055
    ChrTalk(
        0x101,
        (
            "#5P#00006F话说回来，这里也有一些\x01",
            "古怪的机械在游荡呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#5P#00108F还有些地方喷着火……\x01",
            "实在是很危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#5P#00211F那些机械似乎不是\x01",
            "『结社』的智能兵器……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B21():
        TurnDirection(0x101, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3B21)
    Sleep(0)

    def lambda_3B31():
        TurnDirection(0x102, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3B31)
    Sleep(0)

    def lambda_3B41():
        TurnDirection(0x103, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3B41)
    Sleep(0)

    def lambda_3B51():
        TurnDirection(0x104, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3B51)
    Sleep(0)

    def lambda_3B61():
        TurnDirection(0x109, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3B61)
    Sleep(0)

    def lambda_3B71():
        TurnDirection(0x105, 0x13E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3B71)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x13E)
    OP_63(0x13E, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0058
    ChrTalk(
        0x13E,
        (
            "#02305F#5P和、和我完全无关哦！\x02\x03",

            "#02306F虽说Ｂ区域的扫除型设备\x01",
            "确实是被我改造到失控的……\x02\x03",

            "#02310F但这个区域我还是第一次来！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x13E)

    #C0059
    ChrTalk(
        0x104,
        "#00303F#11P好可疑啊……\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x109,
        (
            "#6P#10112F我们不会生气的，如果是你\x01",
            "做的，就老老实实地承认吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x109, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0061
    ChrTalk(
        0x13E,
        "#11P#02311F#4S都说了不是啦～！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        (
            "#11P#10305F说起来……\x02\x03",

            "#10300F这个区域好像通往\x01",
            "兰花塔的底部吧？\x02\x03",

            "我们可不可以\x01",
            "从那边过去？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x105, 500)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 4)), scpexpr(EXPR_END)), "loc_3F28")

    #C0063
    ChrTalk(
        0x13E,
        (
            "#02306F#6P哦，自从那起恐怖分子事件发生之后，\x01",
            "兰花塔的地下入口就被封锁了。\x02\x03",

            "不然的话，那里离\x01",
            "『第四控制终端』很近，\x01",
            "我一个人就可以过去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        (
            "#6P#00203F确实，Ｄ区域那边的\x01",
            "通行口也被封锁了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x101, 500)
    Sleep(100)

    #C0065
    ChrTalk(
        0x13E,
        (
            "#02300F#5P好啦，『第四控制终端』附近\x01",
            "应该也有个直达出口的升降机。\x02\x03",

            "#02309F只要将它启动，\x01",
            "以后我再过来就不用麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_402D")

    label("loc_3F28")


    #C0066
    ChrTalk(
        0x13E,
        (
            "#02306F#6P哦，自从那起恐怖分子事件发生之后，\x01",
            "兰花塔的地下入口就被封锁了。\x02\x03",

            "不然的话，那里离\x01",
            "『第四控制终端』很近，\x01",
            "我一个人就可以过去了。\x02\x03",

            "#02300F好啦，『第四控制终端』附近\x01",
            "应该也有个直达出口的升降机。\x02\x03",

            "#02309F只要将它启动，\x01",
            "以后我再过来就不用麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402D")


    #C0067
    ChrTalk(
        0x101,
        "#12P#00006F真是个得意忘形的小子。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#12P#00102F呵呵……\x01",
            "那我们就赶快行动吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -400000, -2000, -583500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x181, 6)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_27_389D end

    def Function_28_40BE(): pass

    label("Function_28_40BE")


    def lambda_40C3():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40C3)

    def lambda_40DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40DD)
    WaitChrThread(0xFE, 1)

    def lambda_40F2():
        OP_96(0xFE, 0xFFF9E2F6, 0xFFFFF830, 0xFFF71594, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40F2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_40BE end

    def Function_29_410C(): pass

    label("Function_29_410C")


    def lambda_4111():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4111)

    def lambda_412B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_412B)
    WaitChrThread(0xFE, 1)

    def lambda_4140():
        OP_96(0xFE, 0xFFF9E80A, 0xFFFFF830, 0xFFF71594, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4140)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_410C end

    def Function_30_415A(): pass

    label("Function_30_415A")


    def lambda_415F():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_415F)

    def lambda_4179():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4179)
    WaitChrThread(0xFE, 1)

    def lambda_418E():
        OP_95(0xFE, -401650, -2000, -583700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_418E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_415A end

    def Function_31_41AF(): pass

    label("Function_31_41AF")


    def lambda_41B4():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41B4)

    def lambda_41CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41CE)
    WaitChrThread(0xFE, 1)

    def lambda_41E3():
        OP_95(0xFE, -398350, -2000, -583700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41E3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_41AF end

    def Function_32_4204(): pass

    label("Function_32_4204")


    def lambda_4209():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4209)

    def lambda_4223():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4223)
    WaitChrThread(0xFE, 1)

    def lambda_4238():
        OP_95(0xFE, -401300, -2000, -582300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4238)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_4204 end

    def Function_33_4259(): pass

    label("Function_33_4259")


    def lambda_425E():
        OP_96(0xFE, 0xFFF9E580, 0xFFFFF830, 0xFFF71E90, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_425E)

    def lambda_4278():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4278)
    WaitChrThread(0xFE, 1)

    def lambda_428D():
        OP_95(0xFE, -398700, -2000, -582300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_428D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_4259 end

    def Function_34_42AE(): pass

    label("Function_34_42AE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    SoundLoad(931)
    SoundLoad(825)
    OP_68(-183000, 6000, -200000, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(19000, 0)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    ClearMapObjFlags(0x17, 0x4)
    OP_75(0x17, 0x2, 0x2328)
    OP_7D(0xFF, 0x7D, 0x69, 0x0, 0x2328)
    Sound(930, 0, 100, 0)
    OP_68(-212000, 6000, -200000, 9000)
    MoveCamera(33, 33, 0, 9000)
    SetCameraDistance(24000, 9000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x19, 1, 0, 35)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_42AE end

    def Function_35_4366(): pass

    label("Function_35_4366")

    Sound(931, 2, 30, 0)
    Sound(825, 2, 30, 0)
    Sleep(400)
    OP_25(0x3A3, 0x28)
    OP_25(0x339, 0x28)
    Sleep(400)
    OP_25(0x3A3, 0x32)
    OP_25(0x339, 0x32)
    Sleep(400)
    OP_25(0x3A3, 0x3C)
    OP_25(0x339, 0x3C)
    Sleep(400)
    OP_25(0x3A3, 0x46)
    OP_25(0x339, 0x46)
    Sleep(400)
    OP_25(0x3A3, 0x50)
    OP_25(0x339, 0x50)
    Sleep(400)
    OP_25(0x339, 0x5A)
    Sleep(400)
    OP_25(0x339, 0x64)
    Sleep(4200)
    StopSound(931, 1000, 80)
    StopSound(825, 1000, 100)
    Return()

    # Function_35_4366 end

    def Function_36_43C7(): pass

    label("Function_36_43C7")

    TalkBegin(0xFF)
    SetChrName("")

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力似乎已经停止了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C3")

    #C0070
    ChrTalk(
        0x101,
        "#00005F……纹丝不动。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        (
            "#00100F这个地方和兰花塔\x01",
            "底部区域相连……\x02\x03",

            "#00103F多半是总统他们\x01",
            "把开关都锁住了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        "#00200F原来如此，很有可能呢。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x104,
        (
            "#00306F还是放弃\x01",
            "由地下空间潜入\x01",
            "兰花塔的想法吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 5)

    label("loc_44C3")

    TalkEnd(0xFF)
    Return()

    # Function_36_43C7 end

    SaveToFile()

Try(main)
