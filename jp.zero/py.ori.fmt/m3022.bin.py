from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3022.bin",                # FileName
        "m3022",                    # MapName
        "m3022",                    # Location
        0x007D,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 125, 0, 1, 0, 2],
    )

    BuildStringList((
        "m3022",                  # 0
        "シームーン",             # 1
        "bm3020",                 # 2
        "bm3020",                 # 3
        "bm3020",                 # 4
        "bm3020",                 # 5
    ))

    ATBonus("ATBonus_3C4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_20B1", 0,   4,   12,  0,   24,  8,   16)
    Sepith("Sepith_20C1", 2,   0,   4,   14,  16,  9,   18)
    Sepith("Sepith_20C9", 12,  6,   0,   2,   9,   18,  16)

    MonsterBattlePostion("MonsterBattlePostion_404", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_488", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_48C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_490", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_494", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_498", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_49C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_424", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 8, 14, 180)

    # monster count: 11

    BattleInfo(
        "BattleInfo_56C", 0x0000, 40, 6, 60, 4, 1, 40, 0, "bm3020", "Sepith_20B1", 60, 25, 10, 5,
        (
            ("ms71100.dat", "ms71100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
        )
    )

    BattleInfo(
        "BattleInfo_4A4", 0x0000, 40, 6, 60, 4, 1, 50, 0, "bm3020", "Sepith_20C1", 60, 25, 10, 5,
        (
            ("ms77100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
            ("ms77100.dat", "ms77100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
            ("ms77100.dat", "ms71100.dat", "ms77100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
            ("ms77100.dat", "ms77100.dat", "ms71100.dat", "ms77100.dat", 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
        )
    )

    BattleInfo(
        "BattleInfo_634", 0x0000, 40, 6, 60, 4, 1, 30, 0, "bm3020", "Sepith_20C9", 60, 25, 10, 5,
        (
            ("ms77200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
            ("ms77200.dat", "ms71100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
            ("ms77200.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
            ("ms77200.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_6FC", 0x0010, 40, 6, 60, 4, 1, 0, 0, "bm3020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68400.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", 0, "ms75700.dat", 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7402", "ed7403", "ATBonus_3C4"),
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
        "monster/ch77150.itc",               # 10
        "monster/ch77150.itc",               # 11
        "monster/ch71150.itc",               # 12
        "monster/ch71151.itc",               # 13
        "monster/ch77250.itc",               # 14
        "monster/ch77250.itc",               # 15
        "monster/ch68450.itc",               # 16
        "monster/ch68450.itc",               # 17
    ))

    DeclNpc(-3000,   -55750,  31500,   0,    484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(24180,   210,     -54000,  0x1010000,    "BattleInfo_56C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(25210,   -39010,  -54000,  0x1010000,    "BattleInfo_4A4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(14760,   800,     -57250,  0x1010000,    "BattleInfo_56C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(36740,   25490,   -57250,  0x1010000,    "BattleInfo_634", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-12780,  20680,   -54000,  0x1010000,    "BattleInfo_56C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-13140,  -17280,  -57250,  0x1010000,    "BattleInfo_634", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-20570,  -29460,  -57250,  0x1010000,    "BattleInfo_56C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-3560,   9080,    -57250,  0x1010000,    "BattleInfo_56C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-35980,  32860,   -57250,  0x1010000,    "BattleInfo_56C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-22640,  31590,   -57250,  0x1010000,    "BattleInfo_56C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-38340,  -21670,  -57250,  0x1010000,    "BattleInfo_634", 0,   20,  0xFFFF, 4,  5)

    DeclActor(40250,   -54000,  -39250,  1200,    40250,   -53000,  -39250,  0x007C, 0,  3,  0x0000)
    DeclActor(23500,   -54000,  40250,   1200,    23500,   -53000,  40250,   0x007C, 0,  4,  0x0000)
    DeclActor(-29500,  -54000,  -21750,  1200,    -29500,  -53000,  -21750,  0x007C, 0,  5,  0x0000)
    DeclActor(16250,   -57250,  -34500,  1200,    16250,   -56250,  -34500,  0x007C, 0,  6,  0x0000)
    DeclActor(37250,   -57250,  -28250,  1200,    37250,   -56250,  -28250,  0x007C, 0,  7,  0x0000)
    DeclActor(40250,   -57250,  10250,   1200,    40250,   -56250,  10250,   0x007C, 0,  8,  0x0000)
    DeclActor(-3000,   -57250,  31500,   1200,    -3000,   -56250,  31500,   0x007C, 0,  9,  0x0000)
    DeclActor(-29500,  -57250,  40500,   1200,    -29500,  -56250,  40500,   0x007C, 0,  10, 0x0000)
    DeclActor(0,       -53000,  0,       1200,    0,       -52000,  0,       0x007C, 0,  11, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5

    ScpFunction((
        "Function_0_7B8",          # 00, 0
        "Function_1_7D4",          # 01, 1
        "Function_2_7D5",          # 02, 2
        "Function_3_126E",         # 03, 3
        "Function_4_13BB",         # 04, 4
        "Function_5_1508",         # 05, 5
        "Function_6_1655",         # 06, 6
        "Function_7_17A2",         # 07, 7
        "Function_8_18EF",         # 08, 8
        "Function_9_1A3C",         # 09, 9
        "Function_10_1C4F",        # 0A, 10
        "Function_11_1D9C",        # 0B, 11
    ))


    def Function_0_7B8(): pass

    label("Function_0_7B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D3")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_7B8")

    label("loc_7D3")

    Return()

    # Function_0_7B8 end

    def Function_1_7D4(): pass

    label("Function_1_7D4")

    Return()

    # Function_1_7D4 end

    def Function_2_7D5(): pass

    label("Function_2_7D5")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 5000, -55000, -12000, 5000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 15000, -55000, 18000, 5000, 2000, 0)
    SetBarrier(0x0, 0x2, 0x1, 0x0, 28000, -55000, 26500, 5000, 2000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, -12000, -55000, 15000, 5000, 2000, 0)
    SetBarrier(0x0, 0x4, 0x1, 0x0, -12000, -55000, -6000, 5000, 2000, 0)
    SetBarrier(0x0, 0x5, 0x1, 0x0, -29500, -55000, 18000, 5000, 2000, 0)
    SetBarrier(0x0, 0x6, 0x1, 0x0, -39000, -55000, -5000, 5000, 2000, 0)
    SetBarrier(0x0, 0x7, 0x1, 0x0, 24000, -53050, -5500, 4000, 2000, 0)
    SetBarrier(0x0, 0x8, 0x1, 0x0, 24000, -53100, -18500, 4000, 2000, 0)
    SetBarrier(0x0, 0x9, 0x1, 0x0, 2500, -53050, 21000, 4000, 2000, 90000)
    SetBarrier(0x0, 0xA, 0x1, 0x0, -9500, -53050, 21000, 4000, 2000, 90000)
    SetBarrier(0x0, 0xB, 0x1, 0x0, -15000, -53050, 0, 4000, 2000, 90000)
    SetBarrier(0x0, 0xC, 0x1, 0x0, -27000, -53050, 0, 4000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 7)), scpexpr(EXPR_END)), "loc_9AF")
    OP_70(0x8, 0x3C)
    SetMapObjFrame(0xFF, "brighe", 0x2, "low")
    SetMapObjFrame(0xFF, "mizu1", 0x2, "low")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    SetBarrier(0x3, 0xA, 0x1)
    SetBarrier(0x3, 0xB, 0x1)
    SetBarrier(0x3, 0xC, 0x1)
    Jump("loc_A04")

    label("loc_9AF")

    OP_70(0x8, 0xA0)
    SetMapObjFrame(0xFF, "brighe", 0x2, "high")
    SetMapObjFrame(0xFF, "mizu1", 0x2, "high")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)
    SetBarrier(0x2, 0xA, 0x1)
    SetBarrier(0x2, 0xB, 0x1)
    SetBarrier(0x2, 0xC, 0x1)

    label("loc_A04")

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
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C8")
    OP_70(0x0, 0x0)
    Jump("loc_11CC")

    label("loc_11C8")

    OP_70(0x0, 0x1E)

    label("loc_11CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DF")
    OP_70(0x1, 0x0)
    Jump("loc_11E3")

    label("loc_11DF")

    OP_70(0x1, 0x1E)

    label("loc_11E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F6")
    OP_70(0x2, 0x0)
    Jump("loc_11FA")

    label("loc_11F6")

    OP_70(0x2, 0x1E)

    label("loc_11FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120D")
    OP_70(0x3, 0x0)
    Jump("loc_1211")

    label("loc_120D")

    OP_70(0x3, 0x1E)

    label("loc_1211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1224")
    OP_70(0x4, 0x0)
    Jump("loc_1228")

    label("loc_1224")

    OP_70(0x4, 0x1E)

    label("loc_1228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123B")
    OP_70(0x5, 0x0)
    Jump("loc_123F")

    label("loc_123B")

    OP_70(0x5, 0x1E)

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1252")
    OP_70(0x6, 0x0)
    Jump("loc_1256")

    label("loc_1252")

    OP_70(0x6, 0x1E)

    label("loc_1256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1269")
    OP_70(0x7, 0x0)
    Jump("loc_126D")

    label("loc_1269")

    OP_70(0x7, 0x1E)

    label("loc_126D")

    Return()

    # Function_2_7D5 end

    def Function_3_126E(): pass

    label("Function_3_126E")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_136A")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_12F3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10D, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1365")

    label("loc_12F3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1365")

    Jump("loc_13AF")

    label("loc_136A")

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

    label("loc_13AF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_126E end

    def Function_4_13BB(): pass

    label("Function_4_13BB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B7")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_1440")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10D, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_14B2")

    label("loc_1440")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14B2")

    Jump("loc_14FC")

    label("loc_14B7")

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

    label("loc_14FC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_13BB end

    def Function_5_1508(): pass

    label("Function_5_1508")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1604")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_158D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10D, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_15FF")

    label("loc_158D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_15FF")

    Jump("loc_1649")

    label("loc_1604")

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

    label("loc_1649")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1508 end

    def Function_6_1655(): pass

    label("Function_6_1655")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1751")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x56, 1)"), scpexpr(EXPR_END)), "loc_16DA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x56),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10D, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_174C")

    label("loc_16DA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x56),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x56),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_174C")

    Jump("loc_1796")

    label("loc_1751")

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

    label("loc_1796")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1655 end

    def Function_7_17A2(): pass

    label("Function_7_17A2")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189E")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x6C, 1)"), scpexpr(EXPR_END)), "loc_1827")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10D, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1899")

    label("loc_1827")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x6C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x6C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1899")

    Jump("loc_18E3")

    label("loc_189E")

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

    label("loc_18E3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_17A2 end

    def Function_8_18EF(): pass

    label("Function_8_18EF")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19EB")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x57, 1)"), scpexpr(EXPR_END)), "loc_1974")
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
    SetScenarioFlags(0x11B, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_19E6")

    label("loc_1974")

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

    label("loc_19E6")

    Jump("loc_1A30")

    label("loc_19EB")

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

    label("loc_1A30")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_18EF end

    def Function_9_1A3C(): pass

    label("Function_9_1A3C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C09")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x77, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B37")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1A95():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A95)

    def lambda_1AAF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1AAF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

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
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_6FC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1B18"),
        (2, "loc_1B27"),
        (1, "loc_1B34"),
        (SWITCH_DEFAULT, "loc_1B37"),
    )


    label("loc_1B18")

    SetScenarioFlags(0x77, 0)
    OP_70(0x6, 0x1E)
    Sleep(500)
    Jump("loc_1B37")

    label("loc_1B27")

    OP_70(0x6, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1B34")

    OP_B7(0x0)
    Return()

    label("loc_1B37")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x448, 1)"), scpexpr(EXPR_END)), "loc_1B94")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0020
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x448),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11B, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1C04")

    label("loc_1B94")

    FadeToDark(300, 0, 100)

    #A0021
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x448),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x448),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1C04")

    Jump("loc_1C43")

    label("loc_1C09")

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

    label("loc_1C43")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1A3C end

    def Function_10_1C4F(): pass

    label("Function_10_1C4F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4B")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x7B, 1)"), scpexpr(EXPR_END)), "loc_1CD4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0023
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11B, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1D46")

    label("loc_1CD4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0024
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x7B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x7B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D46")

    Jump("loc_1D90")

    label("loc_1D4B")

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

    label("loc_1D90")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1C4F end

    def Function_11_1D9C(): pass

    label("Function_11_1D9C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水位調整用のバルブがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2031")
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 7)), scpexpr(EXPR_END)), "loc_1F21")
    Sound(138, 2, 100, 0)
    OP_71(0x8, 0x64, 0xA0, 0x0, 0x0)
    Sleep(2000)
    OP_24(0x8A)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    OP_68(-1680, -53000, -1710, 0)
    MoveCamera(45, 41, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(58500, 0)
    OP_11(0xB1, 0x36, 0x46, 0x14, 0x96, 0x0)
    OP_0D()
    Sound(157, 2, 100, 0)
    Fade(500)
    SetMapObjFrame(0xFF, "brighe", 0x2, "up")
    SetMapObjFrame(0xFF, "mizu1", 0x2, "up")
    Sleep(6600)
    SetMapObjFrame(0xFF, "brighe", 0x2, "high")
    SetMapObjFrame(0xFF, "mizu1", 0x2, "high")
    OP_24(0x9D)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)
    SetBarrier(0x2, 0xA, 0x1)
    SetBarrier(0x2, 0xB, 0x1)
    SetBarrier(0x2, 0xC, 0x1)
    ClearScenarioFlags(0xF4, 7)
    Jump("loc_2031")

    label("loc_1F21")

    Sound(138, 2, 100, 0)
    OP_71(0x8, 0x0, 0x3C, 0x0, 0x0)
    Sleep(2000)
    OP_24(0x8A)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    OP_68(-1680, -53000, -1710, 0)
    MoveCamera(45, 41, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(58500, 0)
    OP_11(0xB1, 0x36, 0x46, 0x14, 0x96, 0x0)
    OP_0D()
    Sound(157, 2, 100, 0)
    Fade(500)
    SetMapObjFrame(0xFF, "brighe", 0x2, "down")
    SetMapObjFrame(0xFF, "mizu1", 0x2, "down")
    Sleep(6600)
    SetMapObjFrame(0xFF, "brighe", 0x2, "low")
    SetMapObjFrame(0xFF, "mizu1", 0x2, "low")
    OP_24(0x9D)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    SetBarrier(0x3, 0xA, 0x1)
    SetBarrier(0x3, 0xB, 0x1)
    SetBarrier(0x3, 0xC, 0x1)
    SetScenarioFlags(0xF4, 7)

    label("loc_2031")

    OP_11(0xB1, 0x36, 0x46, 0x14, 0x4B, 0x0)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_1D9C end

    SaveToFile()

Try(main)
