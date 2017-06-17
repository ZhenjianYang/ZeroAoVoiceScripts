from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3000.bin",                # FileName
        "m3000",                    # MapName
        "m3000",                    # Location
        0x007B,                     # MapIndex
        "ed7510",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -210000, 27000, 0, 0, 0, 1, 123, 0, 1, 0, 2],
    )

    BuildStringList((
        "m3000",                  # 0
        "ボス１",                 # 1
        "ティオ",                 # 2
        "bm3000",                 # 3
        "bm3000",                 # 4
        "bm3000",                 # 5
        "bm3000",                 # 6
    ))

    ATBonus("ATBonus_31C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_33C", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_31EA", 24,  0,   0,   2,   8,   14,  14)
    Sepith("Sepith_31DA", 4,   4,   20,  0,   16,  12,  7)
    Sepith("Sepith_31E2", 0,   29,  0,   0,   9,   3,   19)

    MonsterBattlePostion("MonsterBattlePostion_37C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 5, 5, 45)

    # monster count: 6

    BattleInfo(
        "BattleInfo_58C", 0x0000, 37, 6, 60, 4, 1, 35, 0, "bm3000", "Sepith_31EA", 60, 25, 10, 5,
        (
            ("ms70900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
            ("ms70900.dat", "ms60600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
            ("ms70900.dat", "ms60600.dat", "ms60600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
            ("ms70900.dat", "ms60600.dat", "ms60600.dat", "ms60600.dat", 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
        )
    )

    BattleInfo(
        "BattleInfo_4C4", 0x0000, 37, 6, 60, 4, 1, 30, 0, "bm3000", "Sepith_31DA", 60, 25, 10, 5,
        (
            ("ms60600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
            ("ms60600.dat", "ms60600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
            ("ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
            ("ms60600.dat", "ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
        )
    )

    BattleInfo(
        "BattleInfo_3FC", 0x0000, 37, 6, 60, 4, 1, 40, 0, "bm3000", "Sepith_31E2", 60, 25, 10, 5,
        (
            ("ms68600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
            ("ms68600.dat", "ms68600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
            ("ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
            ("ms68600.dat", "ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7402", "ed7403", "ATBonus_31C"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_654", 0x0042, 37, 6, 60, 0, 1, 0, 0, "bm3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3DC", "ed7405", "ed7000", "ATBonus_33C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00200.itc",                   # 00
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
        "monster/ch68850.itc",               # 10
        "monster/ch68850.itc",               # 11
        "monster/ch68650.itc",               # 12
        "monster/ch68651.itc",               # 13
        "monster/ch60650.itc",               # 14
        "monster/ch60650.itc",               # 15
        "monster/ch70950.itc",               # 16
        "monster/ch70951.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-4850,   19250,   3040,    0x1010000,    "BattleInfo_58C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-2260,   26030,   9040,    0x1010000,    "BattleInfo_4C4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-450,    149030,  9040,    0x1010000,    "BattleInfo_3FC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(12520,   -18730,  9040,    0x1010000,    "BattleInfo_4C4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-630,    -136810, 9040,    0x1010000,    "BattleInfo_58C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-280,    -155150, 9040,    0x1010000,    "BattleInfo_58C", 0,   22,  0xFFFF, 6,  7)

    DeclActor(-4500,   3000,    -19500,  1200,    -4500,   4000,    -19500,  0x007C, 0,  3,  0x0000)
    DeclActor(-5600,   9000,    25500,   1200,    -5600,   10000,   25500,   0x007C, 0,  4,  0x0000)
    DeclActor(11250,   9000,    0,       1200,    11250,   10000,   0,       0x007C, 0,  5,  0x0000)
    DeclActor(0,       9000,    154500,  1200,    0,       10000,   154500,  0x007C, 0,  6,  0x0000)
    DeclActor(251250,  2500,    10750,   1200,    251250,  3500,    10750,   0x007C, 0,  7,  0x0000)
    DeclActor(253000,  2500,    -7000,   1200,    253000,  3500,    -7000,   0x007C, 0,  8,  0x0000)
    DeclActor(6000,    9000,    -150000, 1200,    6000,    10000,   -150000, 0x007C, 0,  10, 0x0000)
    DeclActor(5000,    3000,    3500,    1200,    5000,    4500,    3500,    0x007C, 0,  9,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_73C",          # 00, 0
        "Function_1_759",          # 01, 1
        "Function_2_797",          # 02, 2
        "Function_3_B7F",          # 03, 3
        "Function_4_CCC",          # 04, 4
        "Function_5_E19",          # 05, 5
        "Function_6_F66",          # 06, 6
        "Function_7_10B3",         # 07, 7
        "Function_8_1200",         # 08, 8
        "Function_9_134D",         # 09, 9
        "Function_10_1458",        # 0A, 10
        "Function_11_1632",        # 0B, 11
        "Function_12_1DB1",        # 0C, 12
        "Function_13_28C7",        # 0D, 13
        "Function_14_2900",        # 0E, 14
        "Function_15_2B77",        # 0F, 15
        "Function_16_30EB",        # 10, 16
    ))


    def Function_0_73C(): pass

    label("Function_0_73C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_758")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_73C")

    label("loc_758")

    Return()

    # Function_0_73C end

    def Function_1_759(): pass

    label("Function_1_759")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_773")
    Event(0, 12)

    label("loc_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_787")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 11)
    Jump("loc_796")

    label("loc_787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_796")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 15)

    label("loc_796")

    Return()

    # Function_1_759 end

    def Function_2_797(): pass

    label("Function_2_797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 7)), scpexpr(EXPR_END)), "loc_7A9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BC")
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7BC")

    ClearMapObjFlags(0x22, 0x10)
    OP_70(0x22, 0x41)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D8")
    OP_70(0x22, 0x0)

    label("loc_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 0)), scpexpr(EXPR_END)), "loc_7EE")
    OP_70(0x18, 0x0)
    OP_70(0x23, 0x41)
    Jump("loc_7F6")

    label("loc_7EE")

    OP_70(0x18, 0x5)
    OP_70(0x23, 0x0)

    label("loc_7F6")

    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A66")
    OP_70(0x8, 0x0)
    Jump("loc_A6A")

    label("loc_A66")

    OP_70(0x8, 0x1E)

    label("loc_A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7D")
    OP_70(0x9, 0x0)
    Jump("loc_A81")

    label("loc_A7D")

    OP_70(0x9, 0x1E)

    label("loc_A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A94")
    OP_70(0xA, 0x0)
    Jump("loc_A98")

    label("loc_A94")

    OP_70(0xA, 0x1E)

    label("loc_A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAB")
    OP_70(0x15, 0x0)
    Jump("loc_AAF")

    label("loc_AAB")

    OP_70(0x15, 0x1E)

    label("loc_AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC2")
    OP_70(0x21, 0x0)
    Jump("loc_AC6")

    label("loc_AC2")

    OP_70(0x21, 0x1E)

    label("loc_AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD9")
    OP_70(0x24, 0x0)
    Jump("loc_ADD")

    label("loc_AD9")

    OP_70(0x24, 0x1E)

    label("loc_ADD")

    Sound(129, 1, 100, 0)
    OP_1B(0x0, 0x0, 0x10)
    SetMapObjFlags(0x26, 0x4)
    ClearMapObjFlags(0x26, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7E")
    OP_65(0x6, 0x1)
    OP_70(0x18, 0x0)
    OP_70(0x23, 0x41)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetMapObjFlags(0x24, 0x4)
    SetMapObjFlags(0x25, 0x4)
    OP_65(0x7, 0x1)
    ClearMapObjFlags(0x26, 0x4)
    SetMapObjFlags(0x26, 0x2)

    label("loc_B7E")

    Return()

    # Function_2_797 end

    def Function_3_B7F(): pass

    label("Function_3_B7F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7B")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_C04")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
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
    SetScenarioFlags(0x11E, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_C76")

    label("loc_C04")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
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
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C76")

    Jump("loc_CC0")

    label("loc_C7B")

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

    label("loc_CC0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_B7F end

    def Function_4_CCC(): pass

    label("Function_4_CCC")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC8")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x48, 1)"), scpexpr(EXPR_END)), "loc_D51")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x48),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11E, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_DC3")

    label("loc_D51")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x48),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x48),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_DC3")

    Jump("loc_E0D")

    label("loc_DC8")

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

    label("loc_E0D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_CCC end

    def Function_5_E19(): pass

    label("Function_5_E19")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F15")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x59, 1)"), scpexpr(EXPR_END)), "loc_E9E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x59),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11E, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_F10")

    label("loc_E9E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x59),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x59),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F10")

    Jump("loc_F5A")

    label("loc_F15")

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

    label("loc_F5A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E19 end

    def Function_6_F66(): pass

    label("Function_6_F66")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1062")
    Sound(14, 0, 100, 0)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_FEB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11E, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_105D")

    label("loc_FEB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x15, 0x1E, 0x0, 0x0, 0x0)

    label("loc_105D")

    Jump("loc_10A7")

    label("loc_1062")

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

    label("loc_10A7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_F66 end

    def Function_7_10B3(): pass

    label("Function_7_10B3")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AF")
    Sound(14, 0, 100, 0)
    OP_71(0x21, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1138")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0013
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
    SetScenarioFlags(0x11E, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_11AA")

    label("loc_1138")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0014
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
    OP_71(0x21, 0x1E, 0x0, 0x0, 0x0)

    label("loc_11AA")

    Jump("loc_11F4")

    label("loc_11AF")

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

    label("loc_11F4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_10B3 end

    def Function_8_1200(): pass

    label("Function_8_1200")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FC")
    Sound(14, 0, 100, 0)
    OP_71(0x24, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_1285")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0016
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
    SetScenarioFlags(0x11E, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_12F7")

    label("loc_1285")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0017
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
    OP_71(0x24, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12F7")

    Jump("loc_1341")

    label("loc_12FC")

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

    label("loc_1341")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1200 end

    def Function_9_134D(): pass

    label("Function_9_134D")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0019
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143A")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x25, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x25, 0x0)
    OP_71(0x25, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x25)
    OP_71(0x25, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x25, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_143A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1456")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1456")

    Return()

    # Function_9_134D end

    def Function_10_1458(): pass

    label("Function_10_1458")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 0)), scpexpr(EXPR_END)), "loc_149B")
    TalkBegin(0xFF)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "剣を構えた騎士像がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_1631")

    label("loc_149B")

    EventBegin(0x1)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "騎士像の剣を動かすことができそうだ。\x01",
            "動かしますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162A")
    Fade(500)
    SetChrPos(0x0, 4460, 9040, -150060, 89)
    SetChrPos(0x1, 2510, 9040, -148900, 89)
    SetChrPos(0x2, 2510, 9040, -151310, 89)
    SetChrPos(0x3, 920, 9040, -150530, 89)
    OP_68(4110, 10290, -150590, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0x18, 0x5, 0x23, 0x0, 0x0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)
    Sleep(500)
    Fade(500)
    OP_68(9520, 4290, 340, 0)
    MoveCamera(55, 33, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(27000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    OP_82(0x0, 0x64, 0x7D0, 0xC8)
    OP_71(0x23, 0x0, 0x41, 0x0, 0x0)
    OP_79(0x23)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0xF4, 0)

    label("loc_162A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_1631")

    Return()

    # Function_10_1458 end

    def Function_11_1632(): pass

    label("Function_11_1632")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-194000, 24040, 0, 0)
    MoveCamera(35, 35, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -203400, 27040, 0, 90)
    SetChrPos(0x102, -204900, 27040, -900, 90)
    SetChrPos(0x104, -204900, 27040, 900, 90)
    SetChrPos(0x103, -206200, 27040, 0, 90)
    SetChrPos(0x107, -207200, 27040, 500, 90)
    SetChrPos(0x108, -206900, 27040, 1600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_16ED():
        OP_96(0xFE, 0xFFFD7218, 0x3AC0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16ED)
    Sleep(120)

    def lambda_170A():
        OP_96(0xFE, 0xFFFD6980, 0x3AC0, 0x384, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_170A)
    Sleep(30)

    def lambda_1727():
        OP_96(0xFE, 0xFFFD6980, 0x3AC0, 0xFFFFFC7C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1727)
    Sleep(30)

    def lambda_1744():
        OP_96(0xFE, 0xFFFD6728, 0x3AC0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1744)
    Sleep(50)

    def lambda_1761():
        OP_96(0xFE, 0xFFFD646C, 0x3AC0, 0x640, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1761)
    Sleep(50)

    def lambda_177E():
        OP_96(0xFE, 0xFFFD6340, 0x3AC0, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_177E)
    SetCameraDistance(13000, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(-184600, 18440, 0, 0)
    MoveCamera(325, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15000, 0)
    OP_68(-179600, 16440, 0, 4000)
    MoveCamera(310, 13, 0, 4000)
    SetCameraDistance(16000, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-168720, 16040, 710, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x108, 1)
    WaitChrThread(0x107, 1)
    Sleep(500)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0022
    ChrTalk(
        0x101,
        "#0001F#11Pどうだ……ティオ？\x02",
    )

    CloseMessageWindow()

    def lambda_1882():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1882)
    Sleep(50)

    def lambda_1892():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1892)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0023
    ChrTalk(
        0x103,
        (
            "#6P#0206F……悪い予感が的中です。\x02\x03",

            "#0208F時・空・幻……\x01",
            "上位三属性が働いています。\x02\x03",

            "#0201F《塔》や《僧院》と同じですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#12P#0106Fそう、やっぱり……\x02\x03",

            "#0101Fどうやらこの先は\x01",
            "一筋縄では行かないみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#0306F#5Pって事は、あの得体の知れない\x01",
            "化物どもが徘徊してるってことか。\x02\x03",

            "#0301Fやれやれ、ゾッとしない話だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x107,
        (
            "#6P#0801F……あたしたちも前に\x01",
            "似たような不思議な場所を\x01",
            "探索した事があるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x108,
        (
            "#0903F正直、どんな魔物が現れても\x01",
            "不思議じゃないだろう。\x02\x03",

            "#0901F万全の体制で臨んだ方がいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0013F#11Pそうか……分かった。\x02\x03",

            "#0003F当然、敵による\x01",
            "待ち伏せもあるはずだ……\x02\x03",

            "#0007Fみんな、気を引き締めて行こう！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B33():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1B33)
    Sleep(50)

    def lambda_1B43():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1B43)
    Sleep(50)
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0x9, -169120, 12600, 220, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    #Sound(1153, 255, 100, 0)    #voice#Elie
    #Sound(1249, 255, 100, 1)    #voice#Tio
    #Sound(1343, 255, 100, 2)    #voice#Randy
    #Sound(1689, 255, 100, 3)    #voice#Estelle
    #Sound(1759, 255, 100, 4)    #voice#Joshua

    #C0029
    ChrTalk(
        0x108,
        "#0901F#1K#N#1Pああ……！\x02",
    )


    #C0030
    ChrTalk(
        0x9,
        "#0201F#1K#N#5Pはい……！\x02",
    )


    #C0031
    ChrTalk(
        0x102,
        "#0107F#1K#N#4Pええ！\x02",
    )


    #N0032
    NpcTalk(
        0x101,
        "ランディ",
        "#0307F#1K#N#2Pおおっ！\x02",
    )


    #C0033
    ChrTalk(
        0x107,
        "#0807F#1K#N#3Pうんっ！\x02",
    )

    OP_57(0x1)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0034
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エステルとヨシュアがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キャンプメニューの[TACTICS]で\x01",
            "アタックメンバーに加える事が出来ます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-168500, 16040, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x0, -168500, 15040, 0, 90)
    SetChrPos(0x1, -168500, 15040, 0, 90)
    SetChrPos(0x2, -168500, 15040, 0, 90)
    SetChrPos(0x3, -168500, 15040, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetScenarioFlags(0xE4, 5)
    OP_29(0x4F, 0x4, 0x2)
    OP_29(0x4F, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D9A")
    OP_29(0x31, 0x4, 0x40)
    Jump("loc_1DAC")

    label("loc_1D9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DAC")
    OP_29(0x31, 0x4, 0x40)

    label("loc_1DAC")

    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_11_1632 end

    def Function_12_1DB1(): pass

    label("Function_12_1DB1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00650.itc", 0x22)
    LoadChrToIndex("chr/ch00750.itc", 0x23)
    LoadChrToIndex("monster/ch68852.itc", 0x24)
    OP_68(238000, 4000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 238100, 3500, -1300, 90)
    SetChrPos(0x102, 237800, 3500, -300, 90)
    SetChrPos(0x103, 236500, 3500, -1800, 90)
    SetChrPos(0x104, 236200, 3500, -800, 90)
    SetChrPos(0x107, 237900, 3500, 1500, 90)
    SetChrPos(0x108, 236900, 3500, 1900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x10)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 272000, 1500, 0, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "event\\ev501_00.eff")
    SetCameraDistance(17500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0036
    ChrTalk(
        0x101,
        "#0005F#6Pここは……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        (
            "#6P#0101Fどうやらこの砦の\x01",
            "城主の間みたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x103,
        "#6P#0201Fあ……！\x02",
    )

    CloseMessageWindow()
    OP_68(279000, 6500, 0, 4000)
    MoveCamera(65, 10, 0, 4000)
    SetCameraDistance(23000, 4000)
    OP_6F(0x79)

    #C0039
    ChrTalk(
        0x101,
        "#0013Fあれは……！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#0107F《僧院》の礼拝堂の\x01",
            "奥にあった紋章と同じ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(272000, 5500, 0, 0)
    MoveCamera(55, 12, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 262100, 3500, -1300, 90)
    SetChrPos(0x102, 261800, 3500, -300, 90)
    SetChrPos(0x103, 260500, 3500, -1800, 90)
    SetChrPos(0x104, 260200, 3500, -800, 90)
    SetChrPos(0x107, 261899, 3500, 1500, 90)
    SetChrPos(0x108, 260899, 3500, 1900, 90)

    def lambda_20BD():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20BD)
    Sleep(50)

    def lambda_20DA():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20DA)

    def lambda_20F4():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_20F4)
    Sleep(50)

    def lambda_2111():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2111)

    def lambda_212B():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_212B)
    Sleep(50)

    def lambda_2148():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2148)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x108, 1)
    WaitChrThread(0x104, 1)

    #C0041
    ChrTalk(
        0x107,
        (
            "#0808F#5Pこれって……\x01",
            "例の《教団》の紋章よね？\x02\x03",

            "#0801F６年前の事件の資料に\x01",
            "あったものとは少し違うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0303F#5Pヨアヒムの野郎が置いて行った\x01",
            "ファイルの表紙とも少し違うな。\x02\x03",

            "#0301F確か翼が付いてた気がするが……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x108,
        (
            "#0901F#5P多分、こちらは簡略化された\x01",
            "《教団》の紋章なんでしょう。\x02\x03",

            "ひょっとしたら、現在の紋章の\x01",
            "原型になったものかもしれません。\x02\x03",

            "#0908Fそれがこの場にあるという事は……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#0006F#5P……《教団》のルーツは\x01",
            "５００年以上昔に遡#2Rさかのぼ#る……\x02\x03",

            "#0013Fしかも、このクロスベルが\x01",
            "発祥の地かもしれないってことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x108,
        (
            "#0903F#5Pああ、君たちが発見した\x01",
            "《僧院》の紋章もしかり……\x02\x03",

            "#0901F５００年前の戦乱の時代、\x01",
            "この地の有力者を取り込んで\x01",
            "勢力を拡大したのかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0106F#5Pなんてこと……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#0008F#5Pいずれきちんと歴史を\x01",
            "紐解く必要がありそうだな……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0048
    ChrTalk(
        0x103,
        "#0207F#5P気をつけてください……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    ReplaceBGM("ed7000", "ed7000")
    Fade(250)
    OP_68(272000, 4000, 0, 0)
    MoveCamera(33, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    OP_0D()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13500, 1000)
    Sleep(900)

    def lambda_253A():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_253A)

    def lambda_2554():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2554)
    Sleep(50)

    def lambda_2571():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2571)

    def lambda_258B():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_258B)
    Sleep(50)

    def lambda_25A8():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_25A8)

    def lambda_25C2():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_25C2)
    OP_6F(0x10)
    OP_68(272000, 5000, 0, 3500)
    MoveCamera(33, 30, 0, 3500)
    SetCameraDistance(18000, 3500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    BeginChrThread(0x101, 3, 0, 13)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 272000, 3500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    OP_24(0x81)
    Sleep(500)

    def lambda_2668():
        OP_96(0xFE, 0x42680, 0xDAC, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2668)

    def lambda_2682():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2682)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x107, 1)
    SetChrChipByIndex(0x107, 0x22)
    SetChrSubChip(0x107, 0x0)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x108, 1)
    SetChrChipByIndex(0x108, 0x23)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x8, 1)
    Sleep(500)
    CancelBlur(2000)
    OP_68(268300, 4900, 0, 2000)
    MoveCamera(55, 15, 0, 2000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    OP_6F(0x79)

    #C0049
    ChrTalk(
        0x101,
        "#0007F#6P#N出たか……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0050
    ChrTalk(
        0x107,
        (
            "#0813F#6P《影の国》で現れた\x01",
            "悪魔たちの仲間……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0051
    ChrTalk(
        0x108,
        (
            "#0907F#6Pやはりこの一帯が\x01",
            "異界化しているのか……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0052
    ChrTalk(
        0x104,
        "#0307F#6P#Nとにかくブチ倒すぞ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    OP_68(272000, 4900, 0, 0)
    MoveCamera(90, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    Sleep(170)
    SetChrSubChip(0x8, 0x1)
    Sleep(170)

    def lambda_2833():
        OP_A6(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2833)
    Sleep(1000)
    Sound(948, 0, 100, 0)
    OP_68(269000, 4900, 0, 400)
    SetCameraDistance(15000, 400)
    SetChrFlags(0x8, 0x20)
    SetChrSubChip(0x8, 0x2)

    def lambda_2878():
        OP_98(0xFE, 0xFFFFF060, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2878)
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(400)
    EndChrThread(0x101, 0x3)
    Battle("BattleInfo_654", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    StopEffect(0x0, 0x2)
    Call(0, 14)
    Return()

    # Function_12_1DB1 end

    def Function_13_28C7(): pass

    label("Function_13_28C7")

    OP_82(0x96, 0x96, 0xBB8, 0xDAC)
    Sleep(3500)

    label("loc_28DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28FF")
    OP_82(0x64, 0x64, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("loc_28DB")

    label("loc_28FF")

    Return()

    # Function_13_28C7 end

    def Function_14_2900(): pass

    label("Function_14_2900")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    OP_68(272000, 4500, 0, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 268100, 3500, -1300, 90)
    SetChrPos(0x102, 267800, 3500, -300, 90)
    SetChrPos(0x103, 266500, 3500, -1800, 90)
    SetChrPos(0x104, 266200, 3500, -800, 90)
    SetChrPos(0x107, 267900, 3500, 1500, 90)
    SetChrPos(0x108, 266900, 3500, 1900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(155, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xFA0)
    OP_74(0x22, 0xF)
    OP_71(0x22, 0x0, 0x41, 0x0, 0x0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_79(0x22)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)

    #C0053
    ChrTalk(
        0x107,
        "#0801F#5Pこれって……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x108,
        (
            "#0901F#5P……どうやらこの先が\x01",
            "真の意味での拠点#4Rロッジ#みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#0013F#5Pああ……入ってみよう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 268000, 3500, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0xE4, 6)
    OP_29(0x4F, 0x1, 0x1)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_14_2900 end

    def Function_15_2B77(): pass

    label("Function_15_2B77")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x0)
    SetScenarioFlags(0x5A, 0)
    OP_C7(0x0, 0x1000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_68(-194000, 24040, 0, 0)
    MoveCamera(35, 35, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -203400, 27040, 0, 90)
    SetChrPos(0x102, -204900, 27040, -900, 90)
    SetChrPos(0x104, -204900, 27040, 900, 90)
    SetChrPos(0x103, -206200, 27040, 0, 90)
    SubItemNumber(0x270F, 99)
    OP_32(0x0, 0x10, 0x28)
    AddCraft(0x0, 0xFFFF)
    RemoveCraft(0x0, 0xFFFF)
    OP_38(0x0, 0x80, 0x2)
    OP_38(0x0, 0x81, 0x2)
    OP_38(0x0, 0x82, 0x2)
    OP_38(0x0, 0x83, 0x2)
    OP_38(0x0, 0x84, 0x2)
    OP_38(0x0, 0x85, 0x2)
    OP_38(0x0, 0x86, 0x2)
    OP_42(0x0, 0x3F2, 0xFF)
    OP_42(0x0, 0x5EC, 0xFF)
    OP_42(0x0, 0x650, 0xFF)
    OP_32(0x1, 0x10, 0x28)
    AddCraft(0x1, 0xFFFF)
    RemoveCraft(0x1, 0xFFFF)
    OP_38(0x1, 0x80, 0x2)
    OP_38(0x1, 0x81, 0x2)
    OP_38(0x1, 0x82, 0x2)
    OP_38(0x1, 0x83, 0x2)
    OP_38(0x1, 0x84, 0x2)
    OP_38(0x1, 0x85, 0x2)
    OP_38(0x1, 0x86, 0x2)
    OP_42(0x1, 0x406, 0xFF)
    OP_42(0x1, 0x5EC, 0xFF)
    OP_42(0x1, 0x650, 0xFF)
    OP_32(0x2, 0x10, 0x28)
    AddCraft(0x2, 0xFFFF)
    RemoveCraft(0x2, 0xFFFF)
    OP_38(0x2, 0x80, 0x2)
    OP_38(0x2, 0x81, 0x2)
    OP_38(0x2, 0x82, 0x2)
    OP_38(0x2, 0x83, 0x2)
    OP_38(0x2, 0x84, 0x2)
    OP_38(0x2, 0x85, 0x2)
    OP_38(0x2, 0x86, 0x2)
    OP_42(0x2, 0x41A, 0xFF)
    OP_42(0x2, 0x5EC, 0xFF)
    OP_42(0x2, 0x650, 0xFF)
    OP_32(0x3, 0x10, 0x28)
    AddCraft(0x3, 0xFFFF)
    RemoveCraft(0x3, 0xFFFF)
    OP_38(0x3, 0x80, 0x2)
    OP_38(0x3, 0x81, 0x2)
    OP_38(0x3, 0x82, 0x2)
    OP_38(0x3, 0x83, 0x2)
    OP_38(0x3, 0x84, 0x2)
    OP_38(0x3, 0x85, 0x2)
    OP_38(0x3, 0x86, 0x2)
    OP_42(0x3, 0x42E, 0xFF)
    OP_42(0x3, 0x5EC, 0xFF)
    OP_42(0x3, 0x650, 0xFF)
    OP_C5(0x1, 0x0)
    OP_C5(0x1, 0x1F)

    def lambda_2CFC():
        OP_96(0xFE, 0xFFFD7218, 0x3AC0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CFC)
    Sleep(120)

    def lambda_2D19():
        OP_96(0xFE, 0xFFFD6980, 0x3AC0, 0x384, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D19)
    Sleep(30)

    def lambda_2D36():
        OP_96(0xFE, 0xFFFD6980, 0x3AC0, 0xFFFFFC7C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D36)
    Sleep(30)

    def lambda_2D53():
        OP_96(0xFE, 0xFFFD6728, 0x3AC0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D53)
    SetCameraDistance(13000, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(-184600, 18440, 0, 0)
    MoveCamera(325, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15000, 0)
    OP_68(-179600, 16440, 0, 4000)
    MoveCamera(310, 13, 0, 4000)
    SetCameraDistance(16000, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-168720, 16040, 710, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(500)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0056
    ChrTalk(
        0x101,
        "#0001F#11Pどうだ……ティオ？\x02",
    )

    CloseMessageWindow()

    def lambda_2E4F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2E4F)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0057
    ChrTalk(
        0x103,
        (
            "#6P#0206F……悪い予感が的中です。\x02\x03",

            "#0208F時・空・幻……\x01",
            "上位三属性が働いています。\x02\x03",

            "#0201F《塔》や《僧院》と同じですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#12P#0106Fそう、やっぱり……\x02\x03",

            "#0101Fどうやらこの先は\x01",
            "一筋縄では行かないみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#0306F#5Pって事は、あの得体の知れない\x01",
            "化物どもが徘徊してるってことか。\x02\x03",

            "#0301Fやれやれ、ゾッとしない話だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0013F#11Pそうか……分かった。\x02\x03",

            "#0003F当然、敵による\x01",
            "待ち伏せもあるはずだ……\x02\x03",

            "#0007Fみんな、気を引き締めて行こう！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_303E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_303E)
    Sleep(50)
    OP_93(0x104, 0x5A, 0x1F4)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    #Sound(1153, 255, 100, 0)    #voice#Elie
    #Sound(1249, 255, 100, 1)    #voice#Tio
    #Sound(1343, 255, 100, 2)    #voice#Randy

    #C0061
    ChrTalk(
        0x103,
        "#0201F#1K#6Pはい……！\x02",
    )


    #C0062
    ChrTalk(
        0x104,
        "#0307F#1K#1Pおおっ！\x02",
    )


    #C0063
    ChrTalk(
        0x102,
        "#0107F#1K#2Pええ！\x02",
    )

    OP_57(0x1)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -168500, 15040, 0, 90)
    SetScenarioFlags(0x40, 0)
    Sleep(500)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_15_2B77 end

    def Function_16_30EB(): pass

    label("Function_16_30EB")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315A")

    #C0064
    ChrTalk(
        0x101,
        (
            "#0001F戻っている場合じゃない……\x02\x03",

            "この事件を解決するためにも\x01",
            "今は先に進まないと……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_319B")

    label("loc_315A")


    #C0065
    ChrTalk(
        0x101,
        (
            "#0001F戻っている場合じゃない……\x01",
            "この遺跡の奥へ急ごう……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_319B")

    Sleep(50)
    SetChrPos(0x0, -211500, 27040, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_16_30EB end

    SaveToFile()

Try(main)
