from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0112.bin",                # FileName
        "m0112",                    # MapName
        "m0112",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0112",                  # 0
        "氷魔獣",                 # 1
        "bm0114",                 # 2
        "bm0114",                 # 3
        "bm0114",                 # 4
        "bm0114",                 # 5
        "bm0113",                 # 6
        "bm0113",                 # 7
        "bm0113",                 # 8
        "bm0113",                 # 9
        "bm0114",                 # 10
        "bm0113",                 # 11
    ))

    ATBonus("ATBonus_580", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_34F0", 1,   1,   0,   1,   1,   0,   0)
    Sepith("Sepith_3500", 1,   8,   6,   1,   1,   1,   2)
    Sepith("Sepith_34F8", 1,   8,   6,   1,   1,   1,   2)
    Sepith("Sepith_3508", 2,   0,   0,   1,   1,   0,   1)

    MonsterBattlePostion("MonsterBattlePostion_620", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_624", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_628", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_62C", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_630", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_634", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_638", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_63C", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_660", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_664", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_668", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_66C", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_670", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_674", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_678", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_67C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_604", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_608", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_60C", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_610", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_614", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_618", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_61C", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_640", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_644", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_648", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_64C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_650", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_654", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_658", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_65C", 5, 5, 45)

    # monster count: 13

    BattleInfo(
        "BattleInfo_8D8", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0114", "Sepith_34F0", 30, 45, 20, 5,
        (
            ("ms71200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_600", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, "MonsterBattlePostion_600", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
        )
    )

    BattleInfo(
        "BattleInfo_A68", 0x0010, 48, 6, 60, 6, 1, 25, 0, "bm0113", "Sepith_3500", 30, 45, 20, 5,
        (
            ("ms71000.dat", 0, 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_620", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71000.dat", "ms71000.dat", 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_600", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71000.dat", "ms71000.dat", 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_620", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71000.dat", "ms71000.dat", "ms71000.dat", 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_600", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
        )
    )

    BattleInfo(
        "BattleInfo_9A0", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0113", "Sepith_34F8", 30, 45, 20, 5,
        (
            ("ms70600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms70600.dat", "ms70600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_600", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms70600.dat", "ms70600.dat", "ms70600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms70600.dat", "ms70600.dat", "ms70600.dat", "ms70600.dat", 0, 0, 0, 0, "MonsterBattlePostion_600", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
        )
    )

    BattleInfo(
        "BattleInfo_B30", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0113", "Sepith_3508", 30, 45, 20, 5,
        (
            ("ms73200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms73200.dat", "ms73200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_600", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms73200.dat", "ms73200.dat", "ms73200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms73200.dat", "ms73200.dat", "ms73200.dat", "ms73200.dat", 0, 0, 0, 0, "MonsterBattlePostion_600", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
        )
    )

    BattleInfo(
        "BattleInfo_748", 0x0010, 48, 6, 60, 6, 1, 25, 0, "bm0114", "Sepith_3500", 30, 45, 20, 5,
        (
            ("ms71000.dat", 0, 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_620", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71000.dat", "ms71000.dat", 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_600", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71000.dat", "ms71000.dat", 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_620", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71000.dat", "ms71000.dat", "ms71000.dat", 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_600", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
        )
    )

    BattleInfo(
        "BattleInfo_680", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0114", "Sepith_34F8", 30, 45, 20, 5,
        (
            ("ms70600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
            ("ms70600.dat", "ms70600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_600", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
            ("ms70600.dat", "ms70600.dat", "ms70600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
            ("ms70600.dat", "ms70600.dat", "ms70600.dat", "ms70600.dat", 0, 0, 0, 0, "MonsterBattlePostion_600", "MonsterBattlePostion_660", "ed7400", "ed7403", "ATBonus_580"),
        )
    )

    BattleInfo(
        "BattleInfo_BF8", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0113", "Sepith_34F0", 30, 45, 10, 5,
        (
            ("ms71200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_600", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, "MonsterBattlePostion_600", "MonsterBattlePostion_640", "ed7400", "ed7403", "ATBonus_580"),
        )
    )

    BattleInfo(
        "BattleInfo_CC0", 0x0812, 255, 6, 0, 0, 0, 0, 0, "bm0114", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_640", "ed7401", "ed7403", "ATBonus_580"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D04", 0x0812, 255, 6, 0, 0, 0, 0, 0, "bm0113", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_640", "ed7401", "ed7403", "ATBonus_580"),
            (),
            (),
            (),
        )
    )

    # event battle count: 5

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
        "monster/ch70650.itc",               # 10
        "monster/ch70651.itc",               # 11
        "monster/ch71050.itc",               # 12
        "monster/ch71050.itc",               # 13
        "monster/ch73250.itc",               # 14
        "monster/ch73250.itc",               # 15
        "monster/ch71250.itc",               # 16
        "monster/ch71251.itc",               # 17
        "monster/ch73350.itc",               # 18
        "monster/ch73350.itc",               # 19
    ))

    DeclNpc(10699,   1000,    -100000, 270,  469,  0x0, 0,   24,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-11090,  -100100, -200,    0x1010000,    "BattleInfo_8D8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-88770,  -105390, -8000,   0x1010000,    "BattleInfo_A68", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-102320, -96220,  -2000,   0x1010000,    "BattleInfo_9A0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-16550,  -299530, -6000,   0x1010000,    "BattleInfo_B30", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-7990,   -306140, 2000,    0x1010000,    "BattleInfo_748", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(8090,    -311820, -6000,   0x1010000,    "BattleInfo_680", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(27520,   -311100, -3010,   0x1010000,    "BattleInfo_BF8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(99810,   -299980, 0,       0x1010000,    "BattleInfo_BF8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(10700,   -100000, 0,       0x115010E,    "BattleInfo_CC0", 0,   24,  0xFFFF, 0,  0)
    DeclMonster(-197500, -200000, 0,       0x115005A,    "BattleInfo_D04", 0,   24,  0xFFFF, 0,  0)
    DeclMonster(-16000,  -292500, -6000,   0x11500B4,    "BattleInfo_CC0", 0,   24,  0xFFFF, 0,  0)
    DeclMonster(10000,   -300000, -2000,   0x115010E,    "BattleInfo_CC0", 0,   24,  0xFFFF, 0,  0)
    DeclMonster(23500,   -300000, -2000,   0x115010E,    "BattleInfo_CC0", 0,   24,  0xFFFF, 0,  0)

    DeclEvent(0x0000, 0, 10,  10.699999809265137,    -100.0,                0.0,                   324.0,                 [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.7833333015441895,   16.666667938232422,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 11,  -197.5,                -200.0,                0.0,                   14.2978515625,         [0.3636363744735718,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3636363744735718,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   71.81818389892578,     72.7272720336914,      -0.0,                  1.0])
    DeclEvent(0x0000, 0, 12,  -16.0,                 -292.5,                -6.0,                  144.0,                 [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   2.6666667461395264,    73.125,                1.2000000476837158,    1.0])
    DeclEvent(0x0000, 0, 13,  10.0,                  -300.0,                -2.0,                  64.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.5,                  75.0,                  0.4000000059604645,    1.0])
    DeclEvent(0x0000, 0, 14,  23.5,                  -300.0,                -2.0,                  64.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.875,                75.0,                  0.4000000059604645,    1.0])

    DeclActor(99830,   0,       -99820,  1200,    99830,   1000,    -99820,  0x007C, 0,  5,  0x0000)
    DeclActor(-199530, 0,       -200180, 1200,    -199530, 1000,    -200180, 0x007C, 0,  6,  0x0000)
    DeclActor(-16350,  -2000,   -303820, 1200,    -16350,  -1000,   -303820, 0x007C, 0,  7,  0x0000)
    DeclActor(24300,   -3000,   -311950, 1200,    24300,   -2000,   -311950, 0x007C, 0,  8,  0x0000)
    DeclActor(0,       0,       102000,  1200,    0,       1000,    102500,  0x007C, 0,  15, 0x0000)
    DeclActor(102000,  0,       -500000, 1200,    102500,  1000,    -500000, 0x007C, 0,  17, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_DF4",          # 00, 0
        "Function_1_E13",          # 01, 1
        "Function_2_E30",          # 02, 2
        "Function_3_EFB",          # 03, 3
        "Function_4_191E",         # 04, 4
        "Function_5_1A6F",         # 05, 5
        "Function_6_1BBC",         # 06, 6
        "Function_7_1D09",         # 07, 7
        "Function_8_1E56",         # 08, 8
        "Function_9_1FA3",         # 09, 9
        "Function_10_250E",        # 0A, 10
        "Function_11_26A5",        # 0B, 11
        "Function_12_291B",        # 0C, 12
        "Function_13_2AF7",        # 0D, 13
        "Function_14_2CEA",        # 0E, 14
        "Function_15_2EDC",        # 0F, 15
        "Function_16_306E",        # 10, 16
        "Function_17_31B5",        # 11, 17
        "Function_18_3349",        # 12, 18
    ))


    def Function_0_DF4(): pass

    label("Function_0_DF4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E12")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_DF4")

    label("loc_E12")

    Return()

    # Function_0_DF4 end

    def Function_1_E13(): pass

    label("Function_1_E13")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E2F")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_E13")

    label("loc_E2F")

    Return()

    # Function_1_E13 end

    def Function_2_E30(): pass

    label("Function_2_E30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E77")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5D")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)
    Jump("loc_E77")

    label("loc_E5D")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E77")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)

    label("loc_E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_EB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_EB4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_E9B")
    Jump("loc_EB4")

    label("loc_E9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x0)"), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB4")
    Event(0, 9)

    label("loc_EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 3)), scpexpr(EXPR_END)), "loc_EC2")
    SetChrFlags(0x11, 0x80)

    label("loc_EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 4)), scpexpr(EXPR_END)), "loc_ED0")
    SetChrFlags(0x12, 0x80)

    label("loc_ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 5)), scpexpr(EXPR_END)), "loc_EDE")
    SetChrFlags(0x13, 0x80)

    label("loc_EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 6)), scpexpr(EXPR_END)), "loc_EEC")
    SetChrFlags(0x14, 0x80)

    label("loc_EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 7)), scpexpr(EXPR_END)), "loc_EFA")
    SetChrFlags(0x15, 0x80)

    label("loc_EFA")

    Return()

    # Function_2_E30 end

    def Function_3_EFB(): pass

    label("Function_3_EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 3)), scpexpr(EXPR_END)), "loc_F52")
    SetMapObjFrame(0xD, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0xD, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "off_kp")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_FA9")

    label("loc_F52")

    SetMapObjFrame(0xD, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0xD, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "on_kp")
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 4)), scpexpr(EXPR_END)), "loc_1000")
    SetMapObjFrame(0xF, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0xF, 0x2)
    SetMapObjFrame(0xFF, "simo01", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo01ice02_add", 0x2, "off_kp")
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_1060")

    label("loc_1000")

    SetMapObjFrame(0xF, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0xF, 0x2)
    SetMapObjFrame(0xFF, "simo01", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo01ice02_add", 0x2, "on_kp")
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x1, 0x1)
    OP_1B(0x8, 0x0, 0xB)

    label("loc_1060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 5)), scpexpr(EXPR_END)), "loc_1105")
    SetMapObjFrame(0x11, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x12, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x13, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0x11, 0x2)
    ClearMapObjFlags(0x12, 0x2)
    ClearMapObjFlags(0x13, 0x2)
    SetMapObjFrame(0xFF, "simo02", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo02ice02_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo02ice03_01add", 0x2, "off_kp")
    ModifyEventFlags(0, 2, 0x80)
    Jump("loc_11A7")

    label("loc_1105")

    SetMapObjFrame(0x11, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x12, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x13, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0x11, 0x2)
    SetMapObjFlags(0x12, 0x2)
    SetMapObjFlags(0x13, 0x2)
    SetMapObjFrame(0xFF, "simo02", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo02ice02_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo02ice03_01add", 0x2, "on_kp")
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 6)), scpexpr(EXPR_END)), "loc_1266")
    SetMapObjFrame(0x14, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x15, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x1C, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0x14, 0x2)
    ClearMapObjFlags(0x15, 0x2)
    ClearMapObjFlags(0x1C, 0x2)
    SetMapObjFrame(0xFF, "simo03", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo03ice02_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo03ice03_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo03ice03_01add", 0x2, "off_kp")
    ModifyEventFlags(0, 3, 0x80)
    Jump("loc_1321")

    label("loc_1266")

    SetMapObjFrame(0x14, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x15, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x1C, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0x14, 0x2)
    SetMapObjFlags(0x15, 0x2)
    SetMapObjFlags(0x1C, 0x2)
    SetMapObjFrame(0xFF, "simo03", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo03ice02_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo03ice03_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo03ice03_01add", 0x2, "on_kp")
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 7)), scpexpr(EXPR_END)), "loc_13DF")
    SetMapObjFrame(0x19, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x1A, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x1B, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x1D, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0x19, 0x2)
    ClearMapObjFlags(0x1A, 0x2)
    ClearMapObjFlags(0x1B, 0x2)
    ClearMapObjFlags(0x1D, 0x2)
    SetMapObjFrame(0xFF, "simo04", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo04ice02_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo04ice03_01add", 0x2, "off_kp")
    ModifyEventFlags(0, 4, 0x80)
    Jump("loc_1499")

    label("loc_13DF")

    SetMapObjFrame(0x19, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x1A, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x1B, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x1D, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0x19, 0x2)
    SetMapObjFlags(0x1A, 0x2)
    SetMapObjFlags(0x1B, 0x2)
    SetMapObjFlags(0x1D, 0x2)
    SetMapObjFrame(0xFF, "simo04", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo04ice02_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo04ice03_01add", 0x2, "on_kp")
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1499")

    SetMapObjFrame(0xB, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
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
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D1")
    OP_70(0x1E, 0x0)
    Jump("loc_18D5")

    label("loc_18D1")

    OP_70(0x1E, 0x1E)

    label("loc_18D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E8")
    OP_70(0x1F, 0x0)
    Jump("loc_18EC")

    label("loc_18E8")

    OP_70(0x1F, 0x1E)

    label("loc_18EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FF")
    OP_70(0x20, 0x0)
    Jump("loc_1903")

    label("loc_18FF")

    OP_70(0x20, 0x1E)

    label("loc_1903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1916")
    OP_70(0x21, 0x0)
    Jump("loc_191A")

    label("loc_1916")

    OP_70(0x21, 0x1E)

    label("loc_191A")

    Call(0, 4)
    Return()

    # Function_3_EFB end

    def Function_4_191E(): pass

    label("Function_4_191E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_194D")
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0x11, 0x8)
    Jump("loc_1961")

    label("loc_194D")

    ClearChrFlags(0x9, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1961")
    ClearChrFlags(0x11, 0x8)

    label("loc_1961")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7B), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_197A")
    SetMapObjFlags(0x1E, 0x4)
    Jump("loc_1980")

    label("loc_197A")

    ClearMapObjFlags(0x1E, 0x4)

    label("loc_1980")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19A6")
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    Jump("loc_19B0")

    label("loc_19A6")

    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)

    label("loc_19B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19FB")
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetMapObjFlags(0x20, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    Jump("loc_1A48")

    label("loc_19FB")

    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearMapObjFlags(0x20, 0x4)
    ClearMapObjFlags(0x21, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A2A")
    ClearChrFlags(0x13, 0x8)

    label("loc_1A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A39")
    ClearChrFlags(0x14, 0x8)

    label("loc_1A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A48")
    ClearChrFlags(0x15, 0x8)

    label("loc_1A48")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A69")
    SetChrFlags(0x10, 0x8)
    Jump("loc_1A6E")

    label("loc_1A69")

    ClearChrFlags(0x10, 0x8)

    label("loc_1A6E")

    Return()

    # Function_4_191E end

    def Function_5_1A6F(): pass

    label("Function_5_1A6F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6B")
    Sound(14, 0, 100, 0)
    OP_71(0x1E, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1AF4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10F, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1B66")

    label("loc_1AF4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1E, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1B66")

    Jump("loc_1BB0")

    label("loc_1B6B")

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

    label("loc_1BB0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1A6F end

    def Function_6_1BBC(): pass

    label("Function_6_1BBC")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB8")
    Sound(14, 0, 100, 0)
    OP_71(0x1F, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x50, 1)"), scpexpr(EXPR_END)), "loc_1C41")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10F, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1CB3")

    label("loc_1C41")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1F, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1CB3")

    Jump("loc_1CFD")

    label("loc_1CB8")

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

    label("loc_1CFD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1BBC end

    def Function_7_1D09(): pass

    label("Function_7_1D09")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E05")
    Sound(14, 0, 100, 0)
    OP_71(0x20, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x51, 1)"), scpexpr(EXPR_END)), "loc_1D8E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x51),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10F, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1E00")

    label("loc_1D8E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x51),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x51),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x20, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E00")

    Jump("loc_1E4A")

    label("loc_1E05")

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

    label("loc_1E4A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1D09 end

    def Function_8_1E56(): pass

    label("Function_8_1E56")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F52")
    Sound(14, 0, 100, 0)
    OP_71(0x21, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_1EDB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10F, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1F4D")

    label("loc_1EDB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x21, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1F4D")

    Jump("loc_1F97")

    label("loc_1F52")

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

    label("loc_1F97")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1E56 end

    def Function_9_1FA3(): pass

    label("Function_9_1FA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-640, 1500, -100980, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21990, 0)
    SetChrPos(0x101, -500, 200, -96250, 0)
    SetChrPos(0x102, 500, 200, -96000, 0)
    SetChrPos(0x103, -500, 200, -94750, 0)
    SetChrPos(0x104, 500, 200, -94500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x1)
    OP_68(0, 1700, -101250, 3000)

    def lambda_2096():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2096)

    def lambda_20B0():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20B0)
    Sleep(50)

    def lambda_20C4():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20C4)

    def lambda_20DE():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_20DE)
    Sleep(50)

    def lambda_20F2():
        OP_97(0x103, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20F2)

    def lambda_210C():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_210C)
    Sleep(50)

    def lambda_2120():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2120)

    def lambda_213A():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_213A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    def lambda_2153():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2153)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x102, 2)

    def lambda_2168():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2168)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)

    def lambda_217D():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_217D)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)

    def lambda_2192():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2192)
    OP_71(0x1, 0x14, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_79(0x1)
    OP_68(10670, 1500, -98680, 3000)
    SetCameraDistance(27840, 3000)
    OP_6F(0x79)

    #C0013
    ChrTalk(
        0x102,
        "#2P#0105Fこ、これって……！？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#2P#0001Fもしかしてこれが\x01",
            "上水道の異常の原因か……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#2P#0301Fしかも、見たことねえ\x01",
            "魔獣までいやがるぜ。\x02\x03",

            "#0303Fどうやら人形兵器の一種みてえだが……\x01",
            "多分、この氷もコイツの仕業だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        (
            "#2P#0203Fええ、その可能性は高いかと。\x02\x03",

            "#0200Fデータベースによれば\x01",
            "こんな状態を引き起こすような\x01",
            "冷却設備は無かったはずです。\x02\x03",

            "しかも、上水道を断水させる程となると\x01",
            "同じタイプのものがこのエリアに\x01",
            "複数存在しているとみていいでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-640, 1500, -100980, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21990, 0)
    OP_0D()

    #C0017
    ChrTalk(
        0x101,
        (
            "#6P#0003Fだったら、何としてもやつらを\x01",
            "止める必要があるな。\x02\x03",

            "#0001Fみんな、気を抜かずに行こう！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#0101F#4Pええ！\x02",
    )


    #C0019
    ChrTalk(
        0x103,
        "#0200F#3Pはい。\x02",
    )


    #C0020
    ChrTalk(
        0x104,
        "#0307F#11Pおお！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1250, 0, -100000, 90)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_29(0x34, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_9_1FA3 end

    def Function_10_250E(): pass

    label("Function_10_250E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    TurnDirection(0x0, 0x11, 0)
    TurnDirection(0x1, 0x11, 0)
    TurnDirection(0x2, 0x11, 0)
    TurnDirection(0x3, 0x11, 0)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が徘徊#4Rはいかい#している。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268C")
    Battle("BattleInfo_CC0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x1)
    OP_E0(0x2)
    SetChrFlags(0x11, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 7000, 0, -100500, 90)
    SetChrPos(0x1, 6750, 0, -99500, 90)
    SetChrPos(0x2, 5500, 0, -100500, 90)
    SetChrPos(0x3, 5250, 0, -99500, 90)
    OP_68(9810, 1500, -98880, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0xD, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0xD, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "off")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "off")
    Sleep(2000)
    SetScenarioFlags(0x56, 3)

    label("loc_268C")

    SetChrPos(0x0, 7000, 0, -100000, 90)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_250E end

    def Function_11_26A5(): pass

    label("Function_11_26A5")

    EventBegin(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMapFlags(0x8000000)
    OP_68(-196220, 1150, -199880, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x0, -195220, 150, -199880, 270)
    SetChrPos(0x1, -195220, 150, -199880, 270)
    SetChrPos(0x2, -195220, 150, -199880, 270)
    SetChrPos(0x3, -195220, 150, -199880, 270)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    TurnDirection(0x0, 0x12, 0)
    TurnDirection(0x1, 0x12, 0)
    TurnDirection(0x2, 0x12, 0)
    TurnDirection(0x3, 0x12, 0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が徘徊#4Rはいかい#している。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28D4")
    Battle("BattleInfo_D04", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x1)
    OP_E0(0x2)
    SetChrFlags(0x12, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_66(0x1, 0x1)
    OP_1B(0x8, 0xFF, 0xFFFF)
    SetChrPos(0x0, -197000, 0, -200500, 270)
    SetChrPos(0x1, -196750, 0, -199500, 270)
    SetChrPos(0x2, -195500, 0, -200500, 270)
    SetChrPos(0x3, -195250, 0, -199500, 270)
    OP_68(-199000, 1000, -200000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0xF, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0xF, 0x2)
    SetMapObjFrame(0xFF, "simo01", 0x2, "off")
    SetMapObjFrame(0xFF, "simo01ice02_add", 0x2, "off")
    Sleep(2000)
    SetChrPos(0x0, -195250, 0, -200000, 270)
    SetScenarioFlags(0x56, 4)
    Jump("loc_2913")

    label("loc_28D4")

    OP_68(-105610, 3500, -199960, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x0, -105610, 2000, -199960, 90)

    label("loc_2913")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_26A5 end

    def Function_12_291B(): pass

    label("Function_12_291B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    TurnDirection(0x0, 0x13, 0)
    TurnDirection(0x1, 0x13, 0)
    TurnDirection(0x2, 0x13, 0)
    TurnDirection(0x3, 0x13, 0)

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が徘徊#4Rはいかい#している。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ADE")
    Battle("BattleInfo_D04", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x1)
    OP_E0(0x2)
    SetChrFlags(0x13, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    SetChrPos(0x0, -16500, -6000, -295500, 0)
    SetChrPos(0x1, -15500, -6000, -295750, 0)
    SetChrPos(0x2, -16500, -6000, -297000, 0)
    SetChrPos(0x3, -15500, -6000, -297250, 0)
    OP_68(-16650, -5000, -299430, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0x11, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x12, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x13, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0x11, 0x2)
    ClearMapObjFlags(0x12, 0x2)
    ClearMapObjFlags(0x13, 0x2)
    SetMapObjFrame(0xFF, "simo02", 0x2, "off")
    SetMapObjFrame(0xFF, "simo02ice02_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo02ice03_01add", 0x2, "off")
    Sleep(2000)
    SetScenarioFlags(0x56, 5)

    label("loc_2ADE")

    SetChrPos(0x0, -16000, -6000, -295500, 0)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_291B end

    def Function_13_2AF7(): pass

    label("Function_13_2AF7")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    TurnDirection(0x0, 0x14, 0)
    TurnDirection(0x1, 0x14, 0)
    TurnDirection(0x2, 0x14, 0)
    TurnDirection(0x3, 0x14, 0)

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が徘徊#4Rはいかい#している。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD1")
    Battle("BattleInfo_CC0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x1)
    OP_E0(0x2)
    SetChrFlags(0x14, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    SetChrPos(0x0, 6250, -2000, -300500, 90)
    SetChrPos(0x1, 6000, -2000, -299500, 90)
    SetChrPos(0x2, 4750, -2000, -300500, 90)
    SetChrPos(0x3, 4500, -2000, -299500, 90)
    OP_68(15720, -1000, -296640, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(60000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0x14, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x15, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x1C, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0x14, 0x2)
    ClearMapObjFlags(0x15, 0x2)
    ClearMapObjFlags(0x1C, 0x2)
    SetMapObjFrame(0xFF, "simo03", 0x2, "off")
    SetMapObjFrame(0xFF, "simo03ice02_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo03ice03_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo03ice03_01add", 0x2, "off")
    Sleep(2000)
    SetScenarioFlags(0x56, 6)

    label("loc_2CD1")

    SetChrPos(0x0, 6250, -2000, -300000, 90)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_2AF7 end

    def Function_14_2CEA(): pass

    label("Function_14_2CEA")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    TurnDirection(0x0, 0x15, 0)
    TurnDirection(0x1, 0x15, 0)
    TurnDirection(0x2, 0x15, 0)
    TurnDirection(0x3, 0x15, 0)

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が徘徊#4Rはいかい#している。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC3")
    Battle("BattleInfo_D04", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x1)
    OP_E0(0x2)
    SetChrFlags(0x15, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    SetChrPos(0x0, 19750, -2000, -300500, 90)
    SetChrPos(0x1, 19500, -2000, -299500, 90)
    SetChrPos(0x2, 18250, -2000, -300500, 90)
    SetChrPos(0x3, 18000, -2000, -299500, 90)
    OP_68(29410, -5000, -301840, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(58500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0x19, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x1A, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x1B, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x1D, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0x19, 0x2)
    ClearMapObjFlags(0x1A, 0x2)
    ClearMapObjFlags(0x1B, 0x2)
    ClearMapObjFlags(0x1D, 0x2)
    SetMapObjFrame(0xFF, "simo04", 0x2, "off")
    SetMapObjFrame(0xFF, "simo04ice02_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo04ice03_01add", 0x2, "off")
    Sleep(2000)
    SetScenarioFlags(0x56, 7)

    label("loc_2EC3")

    SetChrPos(0x0, 19750, -2000, -300000, 90)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2CEA end

    def Function_15_2EDC(): pass

    label("Function_15_2EDC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの制御パネルがある。\x01",
            "操作しますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3066")
    Fade(500)
    SetChrPos(0x0, 600, 0, 100600, 0)
    SetChrPos(0x1, -600, 0, 100600, 0)
    SetChrPos(0x2, -600, 0, 99400, 0)
    SetChrPos(0x3, 600, 0, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FC6")
    SetChrPos(0x4, -600, 0, 98200, 0)
    SetChrPos(0x5, 600, 0, 98200, 0)
    Jump("loc_2FE5")

    label("loc_2FC6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FE5")
    SetChrPos(0x4, 0, 0, 98200, 0)

    label("loc_2FE5")

    OP_68(600, 1000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(600, 6000, 100000, 3000)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0111", 0, 0, 0)
    IdleLoop()

    label("loc_3066")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_2EDC end

    def Function_16_306E(): pass

    label("Function_16_306E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, 100600, 0)
    OP_90(0x1, -600, 30000, 100600, 0)
    OP_90(0x2, -600, 30000, 99400, 0)
    OP_90(0x3, 600, 30000, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3141")
    OP_90(0x4, -600, 30000, 98200, 0)
    OP_90(0x5, 600, 30000, 98200, 0)
    Jump("loc_3160")

    label("loc_3141")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3160")
    OP_90(0x4, 0, 30000, 98200, 0)

    label("loc_3160")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 100000, 3000)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xB)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_16_306E end

    def Function_17_31B5(): pass

    label("Function_17_31B5")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの制御パネルがある。\x01",
            "操作しますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3341")
    Fade(500)
    SetChrPos(0x0, 100600, 0, -499400, 90)
    SetChrPos(0x1, 100600, 0, -500600, 90)
    SetChrPos(0x2, 99400, 0, -500600, 90)
    SetChrPos(0x3, 99400, 0, -499400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_329F")
    SetChrPos(0x4, 98200, 0, -500600, 90)
    SetChrPos(0x5, 98200, 0, -499400, 90)
    Jump("loc_32BE")

    label("loc_329F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32BE")
    SetChrPos(0x4, 98200, 0, -500000, 90)

    label("loc_32BE")

    OP_68(100000, 1000, -500000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(100000, -4000, -500000, 2000)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0113", 0, 0, 0)
    IdleLoop()

    label("loc_3341")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_31B5 end

    def Function_18_3349(): pass

    label("Function_18_3349")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(100000, -4000, -500000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 100600, -10000, -499400, 90)
    OP_90(0x1, 100600, -10000, -500600, 90)
    OP_90(0x2, 99400, -10000, -500600, 90)
    OP_90(0x3, 99400, -10000, -499400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_341E")
    OP_90(0x4, 98200, -10000, -500600, 90)
    OP_90(0x5, 98200, -10000, -499400, 90)
    Jump("loc_343D")

    label("loc_341E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_343D")
    OP_90(0x4, 98200, -10000, -500000, 90)

    label("loc_343D")

    Sound(145, 0, 100, 0)
    OP_68(100000, 1000, -500000, 3000)
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

    # Function_18_3349 end

    SaveToFile()

Try(main)
