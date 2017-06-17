from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9070.bin",                # FileName
        "m9070",                    # MapName
        "m9070",                    # Location
        0x00C2,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 194, 0, 3, 0, 4],
    )

    BuildStringList((
        "m9070",                  # 0
        "MapThread",              # 1
        "ピットフィーンド",       # 2
        "ピットフィーンド",       # 3
        "bm9050",                 # 4
        "bm9050",                 # 5
        "bm9050",                 # 6
        "bm9050",                 # 7
        "bm9050",                 # 8
        "bm9050",                 # 9
    ))

    ATBonus("ATBonus_5B8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_5C8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_4250", 13,  3,   21,  13,  4,   7,   9)
    Sepith("Sepith_4248", 10,  16,  12,  10,  10,  8,   4)
    Sepith("Sepith_4258", 17,  17,  17,  17,  8,   8,   8)
    Sepith("Sepith_4240", 16,  8,   16,  10,  8,   6,   6)

    MonsterBattlePostion("MonsterBattlePostion_608", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_60C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_610", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_614", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_618", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_61C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_620", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_624", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_668", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_66C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_670", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_674", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_678", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_67C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_680", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_684", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_5E8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5EC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5FC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_604", 2, 13, 180)

    # monster count: 21

    BattleInfo(
        "BattleInfo_818", 0x0000, 107, 6, 60, 10, 1, 40, 0, "bm9050", "Sepith_4250", 40, 30, 20, 10,
        (
            ("ms81900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_608", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
            ("ms81900.dat", "ms81900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
            ("ms81900.dat", "ms81900.dat", "ms81700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_608", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
            ("ms81900.dat", "ms81700.dat", "ms81900.dat", "ms81700.dat", 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
        )
    )

    BattleInfo(
        "BattleInfo_750", 0x0000, 107, 6, 60, 10, 1, 30, 0, "bm9050", "Sepith_4248", 40, 30, 20, 10,
        (
            ("ms81700.dat", "ms81700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
            ("ms81700.dat", "ms81700.dat", "ms81700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_608", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
            ("ms81700.dat", "ms81700.dat", "ms81700.dat", "ms81700.dat", 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
            ("ms81700.dat", "ms81700.dat", "ms81700.dat", "ms81700.dat", "ms81700.dat", 0, 0, 0, "MonsterBattlePostion_608", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
        )
    )

    BattleInfo(
        "BattleInfo_8E0", 0x0000, 107, 6, 60, 10, 1, 50, 0, "bm9050", "Sepith_4258", 100, 0, 0, 0,
        (
            ("ms86101.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_608", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_688", 0x0000, 107, 6, 60, 10, 1, 30, 0, "bm9050", "Sepith_4240", 40, 30, 20, 10,
        (
            ("ms85600.dat", "ms85600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
            ("ms85600.dat", "ms85600.dat", "ms85600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_608", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
            ("ms85600.dat", "ms85600.dat", "ms85600.dat", "ms85600.dat", 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
            ("ms85600.dat", "ms85600.dat", "ms85600.dat", "ms85600.dat", "ms85600.dat", 0, 0, 0, "MonsterBattlePostion_608", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5B8"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_924", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9050", 0x00000000, 100, 0, 0, 0,
        (
            ("ms81900.dat", "ms81900.dat", "ms85600.dat", "ms85600.dat", "ms81900.dat", "ms85600.dat", "ms81900.dat", "ms85600.dat", "MonsterBattlePostion_5E8", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5C8"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_968", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9050", 0x00000000, 100, 0, 0, 0,
        (
            ("ms81900.dat", "ms81900.dat", "ms81700.dat", "ms81700.dat", "ms81900.dat", "ms81700.dat", "ms81900.dat", "ms81700.dat", "MonsterBattlePostion_5E8", "MonsterBattlePostion_668", "ed7452", "ed7453", "ATBonus_5C8"),
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
        "monster/ch85650.itc",               # 10
        "monster/ch85650.itc",               # 11
        "monster/ch81750.itc",               # 12
        "monster/ch81750.itc",               # 13
        "monster/ch81950.itc",               # 14
        "monster/ch81950.itc",               # 15
        "monster/ch86150.itc",               # 16
        "monster/ch86151.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(25000,   3000,    80000,   0,    484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-64000,  6000,    127000,  0,    484,  0x0, 0,   20,  0,   0,   2,   255, 255, 255,  0)

    DeclMonster(-19980,  37260,   500,     0x10100A9,    "BattleInfo_818", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-42830,  30100,   1490,    0x1010043,    "BattleInfo_750", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-37770,  62890,   2500,    0x10100FF,    "BattleInfo_8E0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-11380,  51220,   2500,    0x101013A,    "BattleInfo_688", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-46190,  106380,  2500,    0x10100A5,    "BattleInfo_818", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(1430,    96450,   3500,    0x10100F7,    "BattleInfo_750", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(18770,   89060,   3500,    0x1010114,    "BattleInfo_8E0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(8580,    22420,   1500,    0x1010143,    "BattleInfo_688", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-4610,   28140,   1500,    0x1010023,    "BattleInfo_688", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(27210,   36340,   2500,    0x101011C,    "BattleInfo_818", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(25350,   73220,   2510,    0x10100A4,    "BattleInfo_8E0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(69890,   70250,   3500,    0x10100E9,    "BattleInfo_750", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(38600,   89700,   4490,    0x10100C1,    "BattleInfo_8E0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(54830,   120470,  5490,    0x10100C3,    "BattleInfo_688", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4700,    115890,  6500,    0x10100B5,    "BattleInfo_818", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(9000,    139120,  6500,    0x10100E0,    "BattleInfo_750", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(29320,   151760,  6500,    0x101008E,    "BattleInfo_688", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-27720,  102310,  6000,    0x1010050,    "BattleInfo_750", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-55090,  125520,  5510,    0x1010038,    "BattleInfo_818", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-22550,  146620,  8500,    0x10100AE,    "BattleInfo_750", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-9320,   133780,  8500,    0x1010165,    "BattleInfo_8E0", 0,   22,  0xFFFF, 6,  7)

    DeclActor(-7500,   1500,    25500,   1200,    -7500,   2500,    25500,   0x007C, 0,  5,  0x0000)
    DeclActor(25000,   2500,    80000,   1200,    25000,   3500,    80000,   0x007C, 0,  6,  0x0000)
    DeclActor(22000,   3500,    96000,   1200,    22000,   4500,    96000,   0x007C, 0,  7,  0x0000)
    DeclActor(64000,   2500,    43000,   1200,    64000,   3500,    43000,   0x007C, 0,  8,  0x0000)
    DeclActor(61000,   5500,    124000,  1200,    61000,   6500,    124000,  0x007C, 0,  9,  0x0000)
    DeclActor(42000,   6500,    126000,  1200,    42000,   7500,    126000,  0x007C, 0,  10, 0x0000)
    DeclActor(-64000,  5500,    127000,  1200,    -64000,  6500,    127000,  0x007C, 0,  11, 0x0000)
    DeclActor(-15000,  8500,    131000,  1200,    -15000,  9500,    131000,  0x007C, 0,  12, 0x0000)
    DeclActor(-41000,  2500,    111000,  1200,    -41000,  3500,    111000,  0x007C, 0,  15, 0x0000)
    DeclActor(-5250,   2500,    53500,   1200,    -5250,   3500,    53500,   0x007C, 0,  16, 0x0000)
    DeclActor(34500,   4500,    80000,   1200,    34500,   5500,    80000,   0x007C, 0,  17, 0x0000)
    DeclActor(-32000,  6000,    138500,  1200,    -32000,  7000,    138500,  0x007C, 0,  18, 0x0000)

    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 5, 6])                 # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6])                # 1
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_A74",          # 00, 0
        "Function_1_1014",         # 01, 1
        "Function_2_1031",         # 02, 2
        "Function_3_104E",         # 03, 3
        "Function_4_1071",         # 04, 4
        "Function_5_2326",         # 05, 5
        "Function_6_23EF",         # 06, 6
        "Function_7_2606",         # 07, 7
        "Function_8_2757",         # 08, 8
        "Function_9_28A8",         # 09, 9
        "Function_10_29F9",        # 0A, 10
        "Function_11_2B4A",        # 0B, 11
        "Function_12_2D61",        # 0C, 12
        "Function_13_2EB2",        # 0D, 13
        "Function_14_313A",        # 0E, 14
        "Function_15_32AD",        # 0F, 15
        "Function_16_3408",        # 10, 16
        "Function_17_3563",        # 11, 17
        "Function_18_36BA",        # 12, 18
        "Function_19_3815",        # 13, 19
        "Function_20_3F0C",        # 14, 20
        "Function_21_3F76",        # 15, 21
        "Function_22_3FE0",        # 16, 22
        "Function_23_404A",        # 17, 23
        "Function_24_40B4",        # 18, 24
        "Function_25_411E",        # 19, 25
    ))


    def Function_0_A74(): pass

    label("Function_0_A74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1013")
    Sleep(700)
    Sound(195, 0, 80, 0)
    OP_C3(0x0, 0x1, 0x3, 0x5DC, 0x0, 0x1, -3500, -1000, 12500, 3500, 3000, 0)
    OP_C3(0x1, 0x1, 0x3, 0x5DC, 0x0, 0x1, -35500, 1500, 65000, 3500, 3000, 0)
    OP_C3(0x2, 0x1, 0x3, 0x5DC, 0x0, 0x1, 9000, 2500, 96000, 3500, 3000, 0)
    OP_C3(0x3, 0x1, 0x3, 0x5DC, 0x0, 0x1, 10000, 500, 42000, 3500, 3000, 0)
    OP_C3(0x4, 0x1, 0x3, 0x5DC, 0x0, 0x1, 65000, 2500, 68000, 3500, 3000, 0)
    OP_C3(0x5, 0x1, 0x3, 0x5DC, 0x0, 0x1, -2000, 5500, 114000, 3500, 3000, 0)
    Sleep(400)
    OP_C3(0x0, 0x1, 0x0, 0x5DC, 0x0, 0x1, -3500, 0, 12500, 3500, 3000, 0)
    OP_C3(0x1, 0x1, 0x0, 0x5DC, 0x0, 0x1, -35500, 2500, 65000, 3500, 3000, 0)
    OP_C3(0x2, 0x1, 0x0, 0x5DC, 0x0, 0x1, 9000, 3500, 96000, 3500, 3000, 0)
    OP_C3(0x3, 0x1, 0x0, 0x5DC, 0x0, 0x1, 10000, 1500, 42000, 3500, 3000, 0)
    OP_C3(0x4, 0x1, 0x0, 0x5DC, 0x0, 0x1, 65000, 3500, 68000, 3500, 3000, 0)
    OP_C3(0x5, 0x1, 0x0, 0x5DC, 0x0, 0x1, -2000, 6500, 114000, 3500, 3000, 0)
    Sleep(500)
    Sleep(100)
    Sound(195, 0, 60, 0)
    OP_C3(0x6, 0x1, 0x3, 0x5DC, 0x0, 0x1, -20000, -500, 38000, 3500, 3000, 0)
    OP_C3(0x7, 0x1, 0x3, 0x5DC, 0x0, 0x1, 3000, 2500, 90000, 3500, 3000, 0)
    OP_C3(0x8, 0x1, 0x3, 0x5DC, 0x0, 0x1, 47000, 1500, 24000, 3500, 3000, 0)
    OP_C3(0x9, 0x1, 0x3, 0x5DC, 0x0, 0x1, 40000, 3500, 102000, 3500, 3000, 0)
    Sleep(400)
    OP_C3(0x6, 0x1, 0x0, 0x5DC, 0x0, 0x1, -20000, 500, 38000, 3500, 3000, 0)
    OP_C3(0x7, 0x1, 0x0, 0x5DC, 0x0, 0x1, 3000, 3500, 90000, 3500, 3000, 0)
    OP_C3(0x8, 0x1, 0x0, 0x5DC, 0x0, 0x1, 47000, 2500, 24000, 3500, 3000, 0)
    OP_C3(0x9, 0x1, 0x0, 0x5DC, 0x0, 0x1, 40000, 4500, 102000, 3500, 3000, 0)
    Sleep(500)
    Sleep(100)
    Sound(195, 0, 80, 0)
    OP_C3(0xA, 0x1, 0x3, 0x5DC, 0x0, 0x1, -38500, 1500, 58500, 3500, 3000, 0)
    OP_C3(0xB, 0x1, 0x3, 0x5DC, 0x0, 0x1, -48000, 1500, 97000, 3500, 3000, 0)
    OP_C3(0xC, 0x1, 0x3, 0x5DC, 0x0, 0x1, -4000, 2500, 92000, 3500, 3000, 0)
    OP_C3(0xD, 0x1, 0x3, 0x5DC, 0x0, 0x1, 5000, 500, 33000, 3500, 3000, 0)
    OP_C3(0xE, 0x1, 0x3, 0x5DC, 0x0, 0x1, 45000, 1500, 51000, 3500, 3000, 0)
    OP_C3(0xF, 0x1, 0x3, 0x5DC, 0x0, 0x1, -22000, 6500, 121000, 3500, 3000, 0)
    Sleep(400)
    OP_C3(0xA, 0x1, 0x0, 0x5DC, 0x0, 0x1, -38500, 2500, 58500, 3500, 3000, 0)
    OP_C3(0xB, 0x1, 0x0, 0x5DC, 0x0, 0x1, -48000, 2500, 97000, 3500, 3000, 0)
    OP_C3(0xC, 0x1, 0x0, 0x5DC, 0x0, 0x1, -4000, 3500, 92000, 3500, 3000, 0)
    OP_C3(0xD, 0x1, 0x0, 0x5DC, 0x0, 0x1, 5000, 1500, 33000, 3500, 3000, 0)
    OP_C3(0xE, 0x1, 0x0, 0x5DC, 0x0, 0x1, 45000, 2500, 51000, 3500, 3000, 0)
    OP_C3(0xF, 0x1, 0x0, 0x5DC, 0x0, 0x1, -22000, 7500, 121000, 3500, 3000, 0)
    Sleep(500)
    Sleep(100)
    Sound(195, 0, 60, 0)
    OP_C3(0x10, 0x1, 0x3, 0x5DC, 0x0, 0x1, -41000, 1500, 68000, 3500, 3000, 0)
    OP_C3(0x11, 0x1, 0x3, 0x5DC, 0x0, 0x1, 1000, 2000, 75000, 3500, 3000, 0)
    OP_C3(0x12, 0x1, 0x3, 0x5DC, 0x0, 0x1, 34000, 3500, 99000, 3500, 3000, 0)
    OP_C3(0x13, 0x1, 0x3, 0x5DC, 0x0, 0x1, 2000, 5500, 126000, 3500, 3000, 0)
    Sleep(400)
    OP_C3(0x10, 0x1, 0x0, 0x5DC, 0x0, 0x1, -41000, 2500, 68000, 3500, 3000, 0)
    OP_C3(0x11, 0x1, 0x0, 0x5DC, 0x0, 0x1, 1000, 3000, 75000, 3500, 3000, 0)
    OP_C3(0x12, 0x1, 0x0, 0x5DC, 0x0, 0x1, 34000, 4500, 99000, 3500, 3000, 0)
    OP_C3(0x13, 0x1, 0x0, 0x5DC, 0x0, 0x1, 2000, 6500, 126000, 3500, 3000, 0)
    Sleep(800)
    Sleep(100)
    Jump("Function_0_A74")

    label("loc_1013")

    Return()

    # Function_0_A74 end

    def Function_1_1014(): pass

    label("Function_1_1014")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1030")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_1014")

    label("loc_1030")

    Return()

    # Function_1_1014 end

    def Function_2_1031(): pass

    label("Function_2_1031")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_104D")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_2_1031")

    label("loc_104D")

    Return()

    # Function_2_1031 end

    def Function_3_104E(): pass

    label("Function_3_104E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105F")
    Event(0, 13)

    label("loc_105F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1070")
    Event(0, 19)

    label("loc_1070")

    Return()

    # Function_3_104E end

    def Function_4_1071(): pass

    label("Function_4_1071")

    OP_F0(0x1, 0x320)
    OP_1B(0x0, 0x0, 0xE)
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_1F84")
    SetMapObjFrame(0xFF, "point16_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x0, 0x1)
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
    SetMapObjFlags(0x20, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetMapObjFlags(0x22, 0x4)
    SetMapObjFlags(0x23, 0x4)
    SetMapObjFlags(0x24, 0x4)
    SetMapObjFlags(0x25, 0x4)
    SetMapObjFlags(0x26, 0x4)
    SetMapObjFlags(0x27, 0x4)
    Jump("loc_1F9E")

    label("loc_1F84")

    BeginChrThread(0x8, 0, 0, 0)
    LoadEffect(0x11, "eff\\\\trapdmg1.eff")

    label("loc_1F9E")

    OP_1C(0x0, 0xC, 0x0, 0x0, 0x0, 0x0, 0x1082, 0x0)
    OP_1C(0x0, 0xE, 0x0, 0x0, 0x0, 0x0, 0x1083, 0x0)
    OP_1C(0x0, 0x10, 0x0, 0x0, 0x0, 0x0, 0x1084, 0x0)
    OP_1C(0x0, 0x12, 0x0, 0x0, 0x0, 0x0, 0x1085, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 5)), scpexpr(EXPR_END)), "loc_2017")
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x800000)
    SetMapObjFrame(0xFF, "CA_stop1", 0x1, 0x2)
    SetMapObjFrame(0x8, "black_add", 0x2, "day")
    SetMapObjFrame(0x8, "blue", 0x2, "day")
    Jump("loc_205A")

    label("loc_2017")

    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x800000)
    SetMapObjFrame(0xFF, "CA_stop1", 0x0, 0x2)
    SetMapObjFrame(0x8, "black_add", 0x2, "night")
    SetMapObjFrame(0x8, "blue", 0x2, "night")

    label("loc_205A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 6)), scpexpr(EXPR_END)), "loc_20A7")
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x800000)
    SetMapObjFrame(0xFF, "CA_stop2", 0x1, 0x2)
    SetMapObjFrame(0x9, "black_add", 0x2, "day")
    SetMapObjFrame(0x9, "blue", 0x2, "day")
    Jump("loc_20EA")

    label("loc_20A7")

    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xE, 0x800000)
    SetMapObjFrame(0xFF, "CA_stop2", 0x0, 0x2)
    SetMapObjFrame(0x9, "black_add", 0x2, "night")
    SetMapObjFrame(0x9, "blue", 0x2, "night")

    label("loc_20EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 7)), scpexpr(EXPR_END)), "loc_2137")
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x800000)
    SetMapObjFrame(0xFF, "CA_stop3", 0x1, 0x2)
    SetMapObjFrame(0xA, "black_add", 0x2, "day")
    SetMapObjFrame(0xA, "blue", 0x2, "day")
    Jump("loc_217A")

    label("loc_2137")

    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x10, 0x800000)
    SetMapObjFrame(0xFF, "CA_stop3", 0x0, 0x2)
    SetMapObjFrame(0xA, "black_add", 0x2, "night")
    SetMapObjFrame(0xA, "blue", 0x2, "night")

    label("loc_217A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 0)), scpexpr(EXPR_END)), "loc_21C7")
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x800000)
    SetMapObjFrame(0xFF, "CA_stop4", 0x1, 0x2)
    SetMapObjFrame(0xB, "black_add", 0x2, "day")
    SetMapObjFrame(0xB, "blue", 0x2, "day")
    Jump("loc_220A")

    label("loc_21C7")

    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x12, 0x800000)
    SetMapObjFrame(0xFF, "CA_stop4", 0x0, 0x2)
    SetMapObjFrame(0xB, "black_add", 0x2, "night")
    SetMapObjFrame(0xB, "blue", 0x2, "night")

    label("loc_220A")

    SetMapObjFrame(0xFF, "CA_stop1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_stop2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_stop3", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_stop4", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225D")
    OP_70(0x0, 0x0)
    Jump("loc_2261")

    label("loc_225D")

    OP_70(0x0, 0x1E)

    label("loc_2261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2274")
    OP_70(0x1, 0x0)
    Jump("loc_2278")

    label("loc_2274")

    OP_70(0x1, 0x1E)

    label("loc_2278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_228B")
    OP_70(0x2, 0x0)
    Jump("loc_228F")

    label("loc_228B")

    OP_70(0x2, 0x1E)

    label("loc_228F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A2")
    OP_70(0x3, 0x0)
    Jump("loc_22A6")

    label("loc_22A2")

    OP_70(0x3, 0x1E)

    label("loc_22A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B9")
    OP_70(0x4, 0x0)
    Jump("loc_22BD")

    label("loc_22B9")

    OP_70(0x4, 0x1E)

    label("loc_22BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D0")
    OP_70(0x5, 0x0)
    Jump("loc_22D4")

    label("loc_22D0")

    OP_70(0x5, 0x1E)

    label("loc_22D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E7")
    OP_70(0x6, 0x0)
    Jump("loc_22EB")

    label("loc_22E7")

    OP_70(0x6, 0x1E)

    label("loc_22EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FE")
    OP_70(0x7, 0x0)
    Jump("loc_2302")

    label("loc_22FE")

    OP_70(0x7, 0x1E)

    label("loc_2302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_2319")
    OP_24(0x82)
    Sound(825, 1, 40, 0)
    Jump("loc_2325")

    label("loc_2319")

    Sound(130, 1, 100, 0)
    Sound(825, 1, 60, 0)

    label("loc_2325")

    Return()

    # Function_4_1071 end

    def Function_5_2326(): pass

    label("Function_5_2326")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B8")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x2, 2000)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火のセピス×２０００\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x205, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_23DD")

    label("loc_23B8")


    #A0002
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

    label("loc_23DD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_2326 end

    def Function_6_23EF(): pass

    label("Function_6_23EF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25C0")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x219, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24EE")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_244C():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_244C)

    def lambda_2466():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2466)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x9, 1)
    Battle("BattleInfo_924", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_24CF"),
        (2, "loc_24DE"),
        (1, "loc_24EB"),
        (SWITCH_DEFAULT, "loc_24EE"),
    )


    label("loc_24CF")

    SetScenarioFlags(0x219, 5)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_24EE")

    label("loc_24DE")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_24EB")

    OP_B9(0x0)
    Return()

    label("loc_24EE")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5F2, 1)"), scpexpr(EXPR_END)), "loc_254B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5F2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x205, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_25BB")

    label("loc_254B")

    FadeToDark(300, 0, 100)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5F2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5F2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_25BB")

    Jump("loc_25FA")

    label("loc_25C0")

    FadeToDark(300, 0, 100)

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

    label("loc_25FA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_23EF end

    def Function_7_2606(): pass

    label("Function_7_2606")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2706")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_268F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x205, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_2701")

    label("loc_268F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2701")

    Jump("loc_274B")

    label("loc_2706")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_274B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_2606 end

    def Function_8_2757(): pass

    label("Function_8_2757")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2857")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xC3, 1)"), scpexpr(EXPR_END)), "loc_27E0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xC3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x205, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_2852")

    label("loc_27E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xC3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xC3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2852")

    Jump("loc_289C")

    label("loc_2857")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
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

    label("loc_289C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_2757 end

    def Function_9_28A8(): pass

    label("Function_9_28A8")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A8")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_2931")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x205, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_29A3")

    label("loc_2931")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_29A3")

    Jump("loc_29ED")

    label("loc_29A8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
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

    label("loc_29ED")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_28A8 end

    def Function_10_29F9(): pass

    label("Function_10_29F9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF9")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x57, 1)"), scpexpr(EXPR_END)), "loc_2A82")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x57),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x205, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_2AF4")

    label("loc_2A82")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x57),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x57),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2AF4")

    Jump("loc_2B3E")

    label("loc_2AF9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0018
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

    label("loc_2B3E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_29F9 end

    def Function_11_2B4A(): pass

    label("Function_11_2B4A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D1B")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x219, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C49")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2BA7():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2BA7)

    def lambda_2BC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2BC1)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    #A0019
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
    Battle("BattleInfo_968", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2C2A"),
        (2, "loc_2C39"),
        (1, "loc_2C46"),
        (SWITCH_DEFAULT, "loc_2C49"),
    )


    label("loc_2C2A")

    SetScenarioFlags(0x219, 6)
    OP_70(0x6, 0x1E)
    Sleep(500)
    Jump("loc_2C49")

    label("loc_2C39")

    OP_70(0x6, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2C46")

    OP_B9(0x0)
    Return()

    label("loc_2C49")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x430, 1)"), scpexpr(EXPR_END)), "loc_2CA6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0020
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x430),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x206, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_2D16")

    label("loc_2CA6")

    FadeToDark(300, 0, 100)

    #A0021
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x430),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x430),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2D16")

    Jump("loc_2D55")

    label("loc_2D1B")

    FadeToDark(300, 0, 100)

    #A0022
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

    label("loc_2D55")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_2B4A end

    def Function_12_2D61(): pass

    label("Function_12_2D61")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E61")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_2DEA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0023
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x206, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_2E5C")

    label("loc_2DEA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0024
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2E5C")

    Jump("loc_2EA6")

    label("loc_2E61")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0025
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

    label("loc_2EA6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_2D61 end

    def Function_13_2EB2(): pass

    label("Function_13_2EB2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_69(0x1, 0x0)
    OP_68(-590, 750, -4200, 0)
    MoveCamera(16, 45, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13520, 0)
    SetChrPos(0x0, 0, 0, -5000, 315)
    SetChrPos(0x1, 0, 0, -5000, 315)
    SetChrPos(0x2, 0, 0, -5000, 315)
    SetChrPos(0x3, 0, 0, -5000, 315)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2FC6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2FC6)

    def lambda_2FD7():
        OP_95(0xFE, -1610, 0, -2960, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2FD7)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_302E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_302E)

    def lambda_303F():
        OP_95(0xFE, -670, 0, -2690, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_303F)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_309C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_309C)

    def lambda_30AD():
        OP_95(0xFE, -2140, 0, -4080, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_30AD)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3104():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_3104)

    def lambda_3115():
        OP_95(0xFE, 430, 0, -2680, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3115)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_13_2EB2 end

    def Function_14_313A(): pass

    label("Function_14_313A")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3193():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3193)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_31DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_31DE)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3229():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_3229)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3274():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_3274)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_3294")
    StopSound(825, 1000, 40)
    Jump("loc_32A0")

    label("loc_3294")

    StopSound(130, 1000, 100)
    StopSound(825, 1000, 60)

    label("loc_32A0")

    Sleep(1000)
    NewScene("m9005", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_14_313A end

    def Function_15_32AD(): pass

    label("Function_15_32AD")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 5)), scpexpr(EXPR_END)), "loc_32F0")
    TalkBegin(0xFF)
    SetChrName("")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もう反応しないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_33FC")

    label("loc_32F0")


    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クリスタルがある。\x01",
            "触れますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33FC")
    SetMapObjFrame(0x8, "black_add", 0x2, "to_d")
    SetMapObjFrame(0x8, "blue", 0x2, "to_d")
    Sleep(1000)
    Sound(211, 0, 100, 0)
    Sleep(2200)
    SetMapObjFrame(0x8, "black_add", 0x2, "day")
    SetMapObjFrame(0x8, "blue", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_stop1", 0x1, 0x2)
    Fade(500)
    OP_69(0x1, 0x0)
    OP_68(-31640, 6750, 115640, 0)
    MoveCamera(359, 39, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21540, 0)
    OP_0D()
    Sleep(1000)
    Fade(2000)
    Sound(153, 0, 100, 0)
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x800000)
    OP_0D()
    Sleep(1500)
    SetScenarioFlags(0x1B0, 5)

    label("loc_33FC")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_15_32AD end

    def Function_16_3408(): pass

    label("Function_16_3408")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 6)), scpexpr(EXPR_END)), "loc_344B")
    TalkBegin(0xFF)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もう反応しないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3557")

    label("loc_344B")


    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クリスタルがある。\x01",
            "触れますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3557")
    SetMapObjFrame(0x9, "black_add", 0x2, "to_d")
    SetMapObjFrame(0x9, "blue", 0x2, "to_d")
    Sleep(1000)
    Sound(211, 0, 100, 0)
    Sleep(2200)
    SetMapObjFrame(0x9, "black_add", 0x2, "day")
    SetMapObjFrame(0x9, "blue", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_stop2", 0x1, 0x2)
    Fade(500)
    OP_69(0x1, 0x0)
    OP_68(2790, 3080, 56190, 0)
    MoveCamera(14, 37, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20450, 0)
    OP_0D()
    Sleep(1000)
    Fade(2000)
    Sound(153, 0, 100, 0)
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x800000)
    OP_0D()
    Sleep(1500)
    SetScenarioFlags(0x1B0, 6)

    label("loc_3557")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_16_3408 end

    def Function_17_3563(): pass

    label("Function_17_3563")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 7)), scpexpr(EXPR_END)), "loc_35A6")
    TalkBegin(0xFF)
    SetChrName("")

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もう反応しないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_36AE")

    label("loc_35A6")


    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クリスタルがある。\x01",
            "触れますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36AE")
    SetMapObjFrame(0xA, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xA, "blue", 0x2, "to_d")
    Sleep(1000)
    Sound(211, 0, 100, 0)
    Sleep(2200)
    SetMapObjFrame(0xA, "black_add", 0x2, "day")
    SetMapObjFrame(0xA, "blue", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_stop3", 0x1, 0x2)
    Fade(500)
    OP_68(28670, 3250, 71660, 0)
    MoveCamera(332, 41, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20450, 0)
    OP_0D()
    Sleep(1000)
    Fade(2000)
    Sound(153, 0, 100, 0)
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x800000)
    OP_0D()
    Sleep(1500)
    SetScenarioFlags(0x1B0, 7)

    label("loc_36AE")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_17_3563 end

    def Function_18_36BA(): pass

    label("Function_18_36BA")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 0)), scpexpr(EXPR_END)), "loc_36FD")
    TalkBegin(0xFF)
    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もう反応しないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3809")

    label("loc_36FD")


    #A0033
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クリスタルがある。\x01",
            "触れますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3809")
    SetMapObjFrame(0xB, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xB, "blue", 0x2, "to_d")
    Sleep(1000)
    Sound(211, 0, 100, 0)
    Sleep(2200)
    SetMapObjFrame(0xB, "black_add", 0x2, "day")
    SetMapObjFrame(0xB, "blue", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_stop4", 0x1, 0x2)
    Fade(500)
    OP_69(0x1, 0x0)
    OP_68(-25700, 6750, 138750, 0)
    MoveCamera(333, 48, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20450, 0)
    OP_0D()
    Sleep(1000)
    Fade(2000)
    Sound(153, 0, 100, 0)
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x800000)
    OP_0D()
    Sleep(1500)
    SetScenarioFlags(0x1B1, 0)

    label("loc_3809")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_36BA end

    def Function_19_3815(): pass

    label("Function_19_3815")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_69(0x3, 0x0)
    SetChrPos(0x104, 0, 50, -3000, 340)
    SetChrPos(0x101, 0, 50, -3000, 359)
    SetChrPos(0x102, 0, 50, -3000, 322)
    SetChrPos(0x103, 0, 50, -3000, 346)
    SetChrPos(0xF4, 0, 50, -3000, 12)
    SetChrPos(0xF5, 0, 50, -3000, 312)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-3230, 1850, 46220, 0)
    MoveCamera(331, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29560, 0)
    OP_68(9660, 1850, 53520, 5000)
    MoveCamera(14, 9, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(29560, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(-7710, -150, 32549, 0)
    MoveCamera(346, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27520, 0)
    OP_68(-1550, 450, 7690, 6500)
    MoveCamera(352, 12, 0, 6500)
    OP_6E(700, 6500)
    SetCameraDistance(35560, 6500)
    Fade(500)
    Sleep(1500)
    PlaceName2(340, 200, "c_plac60", 0x0, 0)
    Sleep(500)
    BeginChrThread(0x104, 0, 0, 20)
    Sleep(600)
    Sound(920, 0, 100, 0)
    BeginChrThread(0x101, 0, 0, 21)
    Sleep(600)
    BeginChrThread(0x102, 0, 0, 22)
    Sleep(600)
    Sound(920, 0, 100, 0)
    BeginChrThread(0x103, 0, 0, 23)
    Sleep(600)
    BeginChrThread(0xF4, 0, 0, 24)
    Sleep(600)
    Sound(920, 0, 100, 0)
    BeginChrThread(0xF5, 0, 0, 25)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-1930, 1450, 3770, 0)
    MoveCamera(13, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16920, 0)
    OP_68(-1930, 1250, 3770, 0)
    MoveCamera(9, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15270, 0)
    OP_68(-2770, 1350, 1990, 0)
    MoveCamera(6, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13780, 0)
    OP_0D()
    Sleep(300)

    #C0034
    ChrTalk(
        0x101,
        "#00011F#12P……これは……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        "#00108F#6Pなんて光景……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        "#00206F#12P……とんでもないです……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B3C")

    #C0037
    ChrTalk(
        0x109,
        "#10108F#12Pここは……地獄……？\x02",
    )

    CloseMessageWindow()

    label("loc_3B3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B77")

    #C0038
    ChrTalk(
        0x105,
        "#10403F#12P煉獄の炎もかくや、だね……\x02",
    )

    CloseMessageWindow()

    label("loc_3B77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BB0")

    #C0039
    ChrTalk(
        0x106,
        "#10708F#12Pこれが《戦鬼》の内面……\x02",
    )

    CloseMessageWindow()

    label("loc_3BB0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BE5")

    #C0040
    ChrTalk(
        0x10A,
        "#00606F#12Pまさに“業”だな……\x02",
    )

    CloseMessageWindow()

    label("loc_3BE5")

    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)

    #C0041
    ChrTalk(
        0x104,
        (
            "#00304F#11P#30Wクク……参ったな。\x02\x03",

            "#00312Fこの光景……俺にもどこか\x01",
            "懐かしいものを感じるぜ……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C65():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C65)
    Sleep(50)

    def lambda_3C75():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3C75)
    Sleep(50)

    def lambda_3C85():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3C85)
    Sleep(50)

    def lambda_3C95():
        TurnDirection(0xF4, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3C95)
    Sleep(50)

    def lambda_3CA5():
        TurnDirection(0xF5, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3CA5)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0042
    ChrTalk(
        0x102,
        "#00108F#6P……ランディ。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#00208F#12Pランディさん……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00003F#12Pでも……それもまた、\x01",
            "ランディの一部なんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        (
            "#00306F#11P#30Wああ……そうだ。\x02\x03",

            "#00308F２年前、俺はこんな光景から\x01",
            "目を逸らすために逃げた……\x02\x03",

            "#00311Fだがいい加減、自分の“業#2Rごう#”と\x01",
            "向き合う時が来たみてぇだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x8C, 0x1F4)
    Sleep(300)

    #C0046
    ChrTalk(
        0x104,
        (
            "#00303F#5P──全てを打ち砕く化物、\x01",
            "《赤の戦鬼#8Rオーガ・ロッソ#》の“戦場”だ。\x02\x03",

            "#00307F呑みこまれないよう、\x01",
            "腹を括って突き進むぞ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(260, 150, -1, -1)
    SetChrName("メンバーたち")
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #A0047
    AnonymousTalk(
        0xFF,
        "#4Sおおっ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -1000, 0, -3300, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A8, 7)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_19_3815 end

    def Function_20_3F0C(): pass

    label("Function_20_3F0C")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3F4B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F4B)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_20_3F0C end

    def Function_21_3F76(): pass

    label("Function_21_3F76")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3FB5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FB5)
    OP_9B(0x0, 0xFE, 0x0, 0x11F8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x155, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_21_3F76 end

    def Function_22_3FE0(): pass

    label("Function_22_3FE0")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_401F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_401F)
    OP_9B(0x0, 0xFE, 0x0, 0x1036, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x12, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_22_3FE0 end

    def Function_23_404A(): pass

    label("Function_23_404A")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4089():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4089)
    OP_9B(0x0, 0xFE, 0x0, 0xD48, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x162, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_23_404A end

    def Function_24_40B4(): pass

    label("Function_24_40B4")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_40F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40F3)
    OP_9B(0x0, 0xFE, 0x0, 0xC4E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x148, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_24_40B4 end

    def Function_25_411E(): pass

    label("Function_25_411E")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_415D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_415D)
    OP_9B(0x0, 0xFE, 0x0, 0xA28, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1C, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_25_411E end

    SaveToFile()

Try(main)
