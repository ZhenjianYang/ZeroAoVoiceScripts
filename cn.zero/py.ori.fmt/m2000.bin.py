from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m2000.bin",                # FileName
        "M2000",                    # MapName
        "M2000",                    # Location
        0x0077,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 119, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2000",                  # 0
        "剧情事件用魔兽",         # 1
        "剧情事件用魔兽",         # 2
        "剧情事件用魔兽",         # 3
        "bm2000",                 # 4
        "bm2000",                 # 5
    ))

    ATBonus("ATBonus_21C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_20C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2719", 0,   0,   22,  0,   14,  14,  0)

    MonsterBattlePostion("MonsterBattlePostion_26C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_270", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_274", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_24C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_250", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_254", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_258", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_25C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_268", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_2EC", 0x0000, 30, 6, 45, 6, 1, 30, 0, "bm2000", "Sepith_2719", 40, 30, 20, 10,
        (
            ("ms73400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2CC", "ed7400", "ed7403", "ATBonus_21C"),
            ("ms73400.dat", "ms73400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_24C", "MonsterBattlePostion_2CC", "ed7400", "ed7403", "ATBonus_21C"),
            ("ms73400.dat", "ms73400.dat", "ms73400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2CC", "ed7400", "ed7403", "ATBonus_21C"),
            ("ms73400.dat", "ms73400.dat", "ms73400.dat", "ms73400.dat", 0, 0, 0, 0, "MonsterBattlePostion_24C", "MonsterBattlePostion_2CC", "ed7400", "ed7403", "ATBonus_21C"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_3B4", 0x0002, 30, 6, 45, 0, 1, 0, 0, "bm2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73400.dat", "ms73400.dat", "ms73400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2CC", "ed7401", "ed7403", "ATBonus_20C"),
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
        "monster/ch73450.itc",               # 10
        "monster/ch73450.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(112650,  -360,    0,       0x1010000,    "BattleInfo_2EC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(111370,  -16710,  0,       0x1010000,    "BattleInfo_2EC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(110950,  10260,   0,       0x1010000,    "BattleInfo_2EC", 0,   16,  0xFFFF, 0,  1)

    DeclActor(113500,  9630,    8130,    1200,    113500,  10630,   8130,    0x007C, 0,  4,  0x0000)
    DeclActor(113500,  9650,    -8160,   1200,    113500,  10650,   -8160,   0x007C, 0,  5,  0x0000)
    DeclActor(34000,   0,       4000,    1200,    34000,   1500,    4000,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 1

    ScpFunction((
        "Function_0_454",          # 00, 0
        "Function_1_4A7",          # 01, 1
        "Function_2_A2F",          # 02, 2
        "Function_3_A8E",          # 03, 3
        "Function_4_B81",          # 04, 4
        "Function_5_D48",          # 05, 5
        "Function_6_F0C",          # 06, 6
        "Function_7_16F7",         # 07, 7
        "Function_8_170F",         # 08, 8
        "Function_9_1734",         # 09, 9
        "Function_10_178D",        # 0A, 10
        "Function_11_1D21",        # 0B, 11
        "Function_12_2541",        # 0C, 12
        "Function_13_256E",        # 0D, 13
        "Function_14_25AF",        # 0E, 14
        "Function_15_2604",        # 0F, 15
        "Function_16_2674",        # 10, 16
    ))


    def Function_0_454(): pass

    label("Function_0_454")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_478")
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_497")

    label("loc_478")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_497")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_4A6")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 10)

    label("loc_4A6")

    Return()

    # Function_0_454 end

    def Function_1_4A7(): pass

    label("Function_1_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_4B9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_4C8")
    StopEffect(0x80, 0x0)
    StopEffect(0x81, 0x0)

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_52E")
    SetMapObjFrame(0xFF, "object02_smoke", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_particle", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_fire", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model04_glow", 0x0, 0x1)
    Jump("loc_53C")

    label("loc_52E")

    SetMapObjFrame(0xFF, "glow02", 0x0, 0x1)

    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_563")
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    label("loc_563")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 120500, 9000, 9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 115000, 9000, 9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 132500, 9000, 5000, 2000, 2000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 132500, 9000, -5000, 2000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 0)), scpexpr(EXPR_END)), "loc_616")
    SetMapObjFrame(0x6, "root", 0x2, "on")
    SetMapObjFrame(0x4, "root", 0x2, "on")
    SetMapObjFrame(0x9, "root", 0x2, "on")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    Jump("loc_64A")

    label("loc_616")

    SetMapObjFrame(0x6, "root", 0x2, "off")
    SetMapObjFrame(0x4, "root", 0x2, "off")
    SetMapObjFrame(0x9, "root", 0x2, "off")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)

    label("loc_64A")

    SetBarrier(0x0, 0x2, 0x1, 0x0, 120500, 9000, -9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 115000, 9000, -9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x6, 0x1, 0x0, 136950, 9000, 2160, 3000, 2000, 150000)
    SetBarrier(0x0, 0x7, 0x1, 0x0, 136950, 9000, -2160, 3000, 2000, 30000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 1)), scpexpr(EXPR_END)), "loc_6FD")
    SetMapObjFrame(0x7, "root", 0x2, "on")
    SetMapObjFrame(0x5, "root", 0x2, "on")
    SetMapObjFrame(0xA, "root", 0x2, "on")
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    Jump("loc_731")

    label("loc_6FD")

    SetMapObjFrame(0x7, "root", 0x2, "off")
    SetMapObjFrame(0x5, "root", 0x2, "off")
    SetMapObjFrame(0xA, "root", 0x2, "off")
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)

    label("loc_731")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_766")
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    label("loc_766")

    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1D, 0x0, 0xB, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x1, 0xC, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x2, 0xD, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2B")
    Sound(129, 1, 100, 0)

    label("loc_A2B")

    Call(0, 2)
    Return()

    # Function_1_4A7 end

    def Function_2_A2F(): pass

    label("Function_2_A2F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7E")
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    Jump("loc_A8D")

    label("loc_A7E")

    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)

    label("loc_A8D")

    Return()

    # Function_2_A2F end

    def Function_3_A8E(): pass

    label("Function_3_A8E")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B63")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0xB, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0xB, 0x0)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xB)
    OP_71(0xB, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0xB, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_B63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_B7F")

    Return()

    # Function_3_A8E end

    def Function_4_B81(): pass

    label("Function_4_B81")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 0)), scpexpr(EXPR_END)), "loc_BBA")
    TalkBegin(0xFF)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开关已被按下。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_D47")

    label("loc_BBA")

    EventBegin(0x1)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个开关。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D40")
    Fade(500)
    SetChrPos(0x0, 113260, 9000, 9260, 180)
    SetChrPos(0x1, 110400, 9000, 9300, 90)
    SetChrPos(0x2, 108400, 9000, 9300, 90)
    SetChrPos(0x3, 106400, 9000, 9300, 90)
    OP_68(113920, 11500, 9260, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    Sound(141, 0, 100, 0)
    SetMapObjFrame(0x6, "root", 0x2, "on")
    Sleep(1200)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x9, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(500)
    Fade(500)
    OP_68(133890, 11500, -180, 0)
    MoveCamera(64, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x4, "root", 0x2, "move")
    Sleep(1000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetScenarioFlags(0xD4, 0)

    label("loc_D40")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_D47")

    Return()

    # Function_4_B81 end

    def Function_5_D48(): pass

    label("Function_5_D48")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 1)), scpexpr(EXPR_END)), "loc_D81")
    TalkBegin(0xFF)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开关已被按下。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_F0B")

    label("loc_D81")

    EventBegin(0x1)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个开关。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F04")
    Fade(500)
    SetChrPos(0x0, 113660, 9000, -9380, 0)
    SetChrPos(0x1, 110400, 9000, -10100, 90)
    SetChrPos(0x2, 108400, 9000, -10100, 90)
    SetChrPos(0x3, 106400, 9000, -10100, 90)
    OP_68(114150, 11500, -10180, 0)
    MoveCamera(50, 31, 0, 0)
    OP_6E(630, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    Sound(141, 0, 100, 0)
    SetMapObjFrame(0x7, "root", 0x2, "on")
    Sleep(1200)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0xA, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(500)
    Fade(500)
    OP_68(133890, 11500, -180, 0)
    MoveCamera(64, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x5, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetScenarioFlags(0xD4, 1)

    label("loc_F04")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_F0B")

    Return()

    # Function_5_D48 end

    def Function_6_F0C(): pass

    label("Function_6_F0C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    LoadChrToIndex("monster/ch73450.itc", 0x23)
    LoadChrToIndex("monster/ch73450.itc", 0x24)
    LoadEffect(0x0, "event\\ev602_00.eff")
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0x8, 112860, 2500, -230, 270)
    SetChrPos(0x9, 114450, 2500, 920, 270)
    SetChrPos(0xA, 114450, 2500, -1260, 270)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 7)
    BeginChrThread(0x9, 0, 0, 7)
    BeginChrThread(0xA, 0, 0, 7)
    SetChrPos(0x101, 103040, 0, 300, 135)
    SetChrPos(0x102, 100740, 0, -250, 135)
    SetChrPos(0x103, 102170, 0, 1300, 135)
    SetChrPos(0x104, 102270, 0, -760, 135)
    SetChrPos(0x109, 99960, 0, 360, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_68(115890, 11300, 1670, 0)
    MoveCamera(65, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30100, 0)
    OP_68(115890, 1100, 1670, 12000)
    Sleep(8000)

    def lambda_10A4():
        OP_95(0xFE, 107910, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10A4)

    def lambda_10BE():
        OP_95(0xFE, 105330, 0, -660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10BE)

    def lambda_10D8():
        OP_95(0xFE, 106880, 0, 820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10D8)

    def lambda_10F2():
        OP_95(0xFE, 106050, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10F2)

    def lambda_110C():
        OP_95(0xFE, 104410, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_110C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    OP_6F(0x1)
    OP_0D()

    #C0006
    ChrTalk(
        0x101,
        "#0005F#5P这里是……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#0101F#5P看、看上去似乎是\x01",
            "礼拜堂……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            "#0506F#5P……根据古代流传下来的记录，\x01",
            "这里似乎是中世纪的僧院遗迹呢。\x02\x03",

            "#0501F──『月之僧院』。\x02\x03",

            "与那个『星见之塔』，还有\x01",
            "位于古战场深处的堡垒好像是\x01",
            "同一时代的建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#0108F#5P也就是说……\x01",
            "是大约五百年前的遗迹吧。\x02\x03",

            "#0103F那是个战争不断的\x01",
            "动乱时代……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(100)
    Sound(935, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0010
    ChrTalk(
        0x109,
        "#0505F#5P这、这是……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#0013F#5P钟声……！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x103,
        (
            "#0201F#5P……！\x02\x03",

            "#0207F要来了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x101, 3, 0, 8)
    Sound(934, 0, 100, 0)
    OP_68(109000, 1600, 0, 0)
    OP_68(112450, 1600, 0, 4000)
    MoveCamera(90, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(27500, 0)
    OP_6F(0x79)
    Fade(1000)
    SetCameraDistance(21500, 2000)
    Sleep(300)
    Sound(868, 0, 100, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    PlayEffect(0x1D, 0xFF, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(250)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    PlayEffect(0x1D, 0xFF, 0x9, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x9, 3, 0, 9)
    Sleep(250)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    PlayEffect(0x1D, 0xFF, 0xA, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xA, 3, 0, 9)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x79)
    OP_0D()
    EndChrThread(0x101, 0x3)
    OP_68(107910, 1600, -1240, 2000)
    MoveCamera(53, 20, 0, 2000)
    SetCameraDistance(15500, 2000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7401", 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0013
    ChrTalk(
        0x101,
        "#0011F#6P#N什么……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sound(1182, 255, 100, 0)    #voice#Elie
    Sleep(1000)

    #C0014
    ChrTalk(
        0x102,
        "#0107F#6P#N亡、亡灵……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0015
    ChrTalk(
        0x109,
        "#0507F#6P#N果然出现了……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0016
    ChrTalk(
        0x104,
        (
            "#0307F#6P#N没有害怕的时间了！\x01",
            "要来了！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetCameraDistance(12000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)

    def lambda_169C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_169C)

    def lambda_16B1():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_16B1)

    def lambda_16C6():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16C6)
    Sleep(500)
    Battle("BattleInfo_3B4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 10)
    Return()

    # Function_6_F0C end

    def Function_7_16F7(): pass

    label("Function_7_16F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_170E")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("Function_7_16F7")

    label("loc_170E")

    Return()

    # Function_7_16F7 end

    def Function_8_170F(): pass

    label("Function_8_170F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1733")
    OP_82(0x46, 0x46, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("Function_8_170F")

    label("loc_1733")

    Return()

    # Function_8_170F end

    def Function_9_1734(): pass

    label("Function_9_1734")

    ClearChrFlags(0xFE, 0x1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChip(0x0, 0xFE, 0x96, 0x12C)

    def lambda_1751():
        OP_98(0xFE, 0x0, 0xFFFFF63C, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1751)

    def lambda_176B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_176B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_9_1734 end

    def Function_10_178D(): pass

    label("Function_10_178D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    OP_68(109140, 1000, -40, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17850, 0)
    OP_68(107180, 1000, -140, 2500)
    SetChrPos(0x101, 107910, 0, -100, 90)
    SetChrPos(0x102, 105240, 0, -330, 90)
    SetChrPos(0x103, 107120, 0, 1380, 90)
    SetChrPos(0x104, 106840, 0, -1310, 90)
    SetChrPos(0x109, 103830, 0, 100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0017
    ChrTalk(
        0x101,
        (
            "#0006F#6P呼……\x01",
            "总算收拾掉了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)

    #C0018
    ChrTalk(
        0x101,
        "#0001F#11P艾莉，没事吧？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#0106F#6P嗯、嗯，还算没事……\x02\x03",

            "#0107F比、比比比、\x01",
            "比起那个，刚才的是！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0020
    ChrTalk(
        0x104,
        (
            "#0306F#11P是彻头彻尾的亡灵啊……\x02\x03",

            "#0308F而且还随着那片诡异的光芒\x01",
            "一起消失不见了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)

    #C0021
    ChrTalk(
        0x103,
        (
            "#0203F#5P话说回来……上级三属性的影响\x01",
            "果然很明显呢。\x02\x03",

            "#0201F看起来，这个遗迹\x01",
            "或许是出于某种原因\x01",
            "才变成了『灵异地点』。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0003F#11P灵异地点吗……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x109,
        (
            "#0508F#6P说起来……\x02\x03",

            "刚才，塔顶的钟\x01",
            "发出了响声……\x02\x03",

            "#0501F敲响它的莫非是\x01",
            "幽──\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1ADA():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1ADA)
    TurnDirection(0x102, 0x109, 500)
    WaitChrThread(0x103, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0024
    ChrTalk(
        0x102,
        (
            "#0107F#11P停，诺艾尔小姐！\x02\x03",

            "#0109F大、大概只是被风吹响的吧！\x01",
            "嗯，一定就是这样！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        "#0306F#11P大小姐，你还真够拼命的。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#0006F#11P虽然也不是不理解你的心情……\x02\x03",

            "#0001F但不管怎么说，凭我们目前的战斗力，\x01",
            "应该足以完成探索任务了。\x02\x03",

            "上士，就这样直接前进吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x109,
        "#0501F#6P是的──拜托大家了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0028
    ChrTalk(
        0x102,
        (
            "#0106F#11P呜呜……\x01",
            "好像只能前进了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        (
            "#0203F#5P算啦，至少我们的攻击\x01",
            "还对它们有效。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0301F#11P哎呀哎呀……\x01",
            "开始有种在鬼屋探险的\x01",
            "感觉了。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18100, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_37()
    SetChrPos(0x0, 106000, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC0, 4)
    OP_29(0x49, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_178D end

    def Function_11_1D21(): pass

    label("Function_11_1D21")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("apl/ch50109.itc", 0x1E)
    OP_68(103440, 11600, -2110, 0)
    MoveCamera(66, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15200, 0)
    SetChrPos(0x101, 127760, 9000, 150, 270)
    SetChrPos(0x102, 128639, 9000, 1980, 270)
    SetChrPos(0x103, 128380, 9000, -920, 270)
    SetChrPos(0x104, 128160, 9000, -2340, 270)
    SetChrPos(0x109, 129520, 9000, -3410, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_68(103440, 3400, -2110, 12000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(123610, 11200, -1950, 0)
    MoveCamera(54, 18, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16280, 0)
    OP_0D()

    #C0031
    ChrTalk(
        0x109,
        "#0505F#11P这是……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        "#0102F#11P有阳光照射下来……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#0304F#11P似乎……\x01",
            "也没有怪物的气息了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#0000F#11P是啊……下去看看吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(106000, 2500, 0, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 106000, 0, 0, 270)
    SetChrPos(0x102, 105000, 0, 0, 270)
    SetChrPos(0x103, 104000, 0, 0, 270)
    SetChrPos(0x104, 103000, 0, 0, 270)
    SetChrPos(0x109, 102000, 0, 0, 270)
    FadeToBright(1000, 0)
    OP_68(106910, 3200, 9230, 0)
    MoveCamera(54, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22100, 0)
    OP_68(106910, 200, 9230, 6000)
    BeginChrThread(0x101, 3, 0, 13)
    BeginChrThread(0x102, 3, 0, 15)
    BeginChrThread(0x103, 3, 0, 14)
    BeginChrThread(0x104, 3, 0, 16)
    BeginChrThread(0x109, 3, 0, 12)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    OP_0D()

    #C0035
    ChrTalk(
        0x103,
        (
            "#0204F#6P时、空、幻这三种属性的影响\x01",
            "也消失了。\x02\x03",

            "#0202F看起来，这里似乎已经\x01",
            "恢复为『普通空间』了呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2017():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2017)
    Sleep(50)

    def lambda_2027():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2027)
    Sleep(50)

    def lambda_2037():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2037)
    Sleep(50)

    def lambda_2047():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2047)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0036
    ChrTalk(
        0x101,
        (
            "#0004F#11P是吗……\x02\x03",

            "#0001F──不过，这到底是\x01",
            "什么构造啊？\x02\x03",

            "关于那个钟的共鸣，\x01",
            "似乎是有什么原因吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#0206F#6P我也不是很清楚……\x02\x03",

            "#0200F不过，那个钟\x01",
            "很有可能是\x01",
            "『古代遗物』呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#0005F#11P『古代遗物』……？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#0103F#5P是指存在于一千两百年前的\x01",
            "『古代塞姆里亚文明』的遗物吧。\x02\x03",

            "#0101F似乎有着不可思议的力量，\x01",
            "所以是由教会全权管理的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0040
    ChrTalk(
        0x104,
        (
            "#0303F#5P是啊，偶尔会听说这种事件。\x02\x03",

            "#0301F某处的贵族收藏了有着\x01",
            "恐怖力量的遗物，然后\x01",
            "受到教会的调查就被没收了之类的。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#0008F#11P还有那种事啊……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        "#0506F#11P我也没听说过……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#0206F#6P无论怎么说，以现代的技术\x01",
            "似乎完全无法对其进行解析……\x02\x03",

            "#0200F在这种意义上，它们好像也几乎\x01",
            "不为一般人所知呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0006F#11P嗯、嗯……\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x109)

    #C0045
    ChrTalk(
        0x109,
        (
            "#0503F#11P──不管怎么说，\x01",
            "有关这处遗迹的线索， \x01",
            "我觉得已经收集够了。\x02\x03",

            "#0501F接下来就是将其整理成报告书，\x01",
            "再委托专家进行调查\x01",
            "比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23BE():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23BE)
    Sleep(50)

    def lambda_23CE():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23CE)
    Sleep(50)

    def lambda_23DE():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23DE)
    Sleep(50)

    def lambda_23EE():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23EE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0046
    ChrTalk(
        0x101,
        "#0000F#5P是啊……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        "#0202F#5P嗯，我也觉得那样比较妥当。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0300F#5P那么，遗迹的调查\x01",
            "就到此为止了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        "#0504F#11P是啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(105730, 200, 5520, 0)
    MoveCamera(111, 18, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17860, 0)
    OP_0D()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0050
    ChrTalk(
        0x109,
        (
            "#0502F#11P──各位，\x01",
            "感谢你们的协助！\x02\x03",

            "遗迹调查的任务\x01",
            "就此结束！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("r2070", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1D21 end

    def Function_12_2541(): pass

    label("Function_12_2541")

    SetChrPos(0xFE, 104660, 0, 12870, 0)
    OP_95(0xFE, 102510, 0, 4220, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_12_2541 end

    def Function_13_256E(): pass

    label("Function_13_256E")

    SetChrPos(0xFE, 106840, 0, 14160, 0)
    OP_95(0xFE, 104660, 0, 12870, 2000, 0x0)
    OP_95(0xFE, 102840, 0, 6380, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_13_256E end

    def Function_14_25AF(): pass

    label("Function_14_25AF")

    SetChrPos(0xFE, 109730, 1580, 14140, 0)
    OP_95(0xFE, 106840, 0, 14160, 2000, 0x0)
    OP_95(0xFE, 104660, 0, 12870, 2000, 0x0)
    OP_95(0xFE, 102160, 0, 7740, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_14_25AF end

    def Function_15_2604(): pass

    label("Function_15_2604")

    SetChrPos(0xFE, 111930, 3230, 14120, 0)
    OP_95(0xFE, 109730, 1580, 14140, 2000, 0x0)
    OP_95(0xFE, 106840, 0, 14160, 2000, 0x0)
    OP_95(0xFE, 104660, 0, 12870, 2000, 0x0)
    OP_95(0xFE, 104460, 0, 8570, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_15_2604 end

    def Function_16_2674(): pass

    label("Function_16_2674")

    SetChrPos(0xFE, 114370, 5060, 14180, 0)
    OP_95(0xFE, 111930, 3230, 14120, 2000, 0x0)
    OP_95(0xFE, 109730, 1580, 14140, 2000, 0x0)
    OP_95(0xFE, 106840, 0, 14160, 2000, 0x0)
    OP_95(0xFE, 104660, 0, 12870, 2000, 0x0)
    OP_95(0xFE, 103920, 0, 10210, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_16_2674 end

    SaveToFile()

Try(main)
