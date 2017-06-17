from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3020.bin",                # FileName
        "m3020",                    # MapName
        "m3020",                    # Location
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
        "m3020",                  # 0
        "シームーン",             # 1
        "bm3020",                 # 2
        "bm3020",                 # 3
        "bm3020",                 # 4
    ))

    ATBonus("ATBonus_244", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_129F", 0,   4,   12,  0,   24,  8,   16)
    Sepith("Sepith_12A7", 0,   13,  2,   4,   14,  20,  9)

    MonsterBattlePostion("MonsterBattlePostion_284", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_308", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_30C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_310", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_314", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_318", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_31C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 8, 14, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_324", 0x0000, 40, 6, 60, 4, 1, 40, 0, "bm3020", "Sepith_129F", 60, 25, 10, 5,
        (
            ("ms71100.dat", "ms71100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_284", "MonsterBattlePostion_304", "ed7402", "ed7403", "ATBonus_244"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2A4", "MonsterBattlePostion_304", "ed7402", "ed7403", "ATBonus_244"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, "MonsterBattlePostion_284", "MonsterBattlePostion_304", "ed7402", "ed7403", "ATBonus_244"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, "MonsterBattlePostion_2A4", "MonsterBattlePostion_304", "ed7402", "ed7403", "ATBonus_244"),
        )
    )

    BattleInfo(
        "BattleInfo_3EC", 0x0000, 40, 6, 60, 4, 1, 40, 0, "bm3020", "Sepith_12A7", 60, 25, 10, 5,
        (
            ("ms75700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2A4", "MonsterBattlePostion_304", "ed7402", "ed7403", "ATBonus_244"),
            ("ms75700.dat", "ms75700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_284", "MonsterBattlePostion_304", "ed7402", "ed7403", "ATBonus_244"),
            ("ms75700.dat", "ms71100.dat", "ms75700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2A4", "MonsterBattlePostion_304", "ed7402", "ed7403", "ATBonus_244"),
            ("ms75700.dat", "ms75700.dat", "ms71100.dat", "ms75700.dat", 0, 0, 0, 0, "MonsterBattlePostion_284", "MonsterBattlePostion_304", "ed7402", "ed7403", "ATBonus_244"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_4B4", 0x0010, 40, 6, 60, 4, 1, 0, 0, "bm3020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68400.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", 0, "ms75700.dat", 0, "MonsterBattlePostion_284", "MonsterBattlePostion_304", "ed7402", "ed7403", "ATBonus_244"),
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
        "monster/ch71150.itc",               # 10
        "monster/ch71151.itc",               # 11
        "monster/ch75750.itc",               # 12
        "monster/ch75750.itc",               # 13
        "monster/ch68450.itc",               # 14
        "monster/ch68450.itc",               # 15
    ))

    DeclNpc(163000,  7550,    -13500,  0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-300,    -17930,  0,       0x1010000,    "BattleInfo_324", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(680,     17060,   0,       0x1010000,    "BattleInfo_3EC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(138060,  18110,   0,       0x1010000,    "BattleInfo_324", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(138800,  -11650,  0,       0x1010000,    "BattleInfo_3EC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(151260,  17220,   3000,    0x1010000,    "BattleInfo_324", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(11100,   1880,    0,       0x1010000,    "BattleInfo_3EC", 0,   18,  0xFFFF, 2,  3)

    DeclActor(12000,   0,       8000,    1200,    12000,   1000,    8000,    0x007C, 0,  3,  0x0000)
    DeclActor(0,       0,       -19750,  1200,    0,       1000,    -19750,  0x007C, 0,  4,  0x0000)
    DeclActor(163000,  6050,    -13500,  1200,    163000,  7050,    -13500,  0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_544",          # 00, 0
        "Function_1_560",          # 01, 1
        "Function_2_577",          # 02, 2
        "Function_3_9DD",          # 03, 3
        "Function_4_A92",          # 04, 4
        "Function_5_B47",          # 05, 5
        "Function_6_D5A",          # 06, 6
    ))


    def Function_0_544(): pass

    label("Function_0_544")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55F")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_544")

    label("loc_55F")

    Return()

    # Function_0_544 end

    def Function_1_560(): pass

    label("Function_1_560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_576")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_576")

    Return()

    # Function_1_560 end

    def Function_2_577(): pass

    label("Function_2_577")

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
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x109, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AA")
    OP_70(0x0, 0x0)
    Jump("loc_9AE")

    label("loc_9AA")

    OP_70(0x0, 0x1E)

    label("loc_9AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x109, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C1")
    OP_70(0x1, 0x0)
    Jump("loc_9C5")

    label("loc_9C1")

    OP_70(0x1, 0x1E)

    label("loc_9C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x109, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D8")
    OP_70(0x2, 0x0)
    Jump("loc_9DC")

    label("loc_9D8")

    OP_70(0x2, 0x1E)

    label("loc_9DC")

    Return()

    # Function_2_577 end

    def Function_3_9DD(): pass

    label("Function_3_9DD")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x109, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5B")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(10000)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１００００ミラ\x07\x00",
            "入手した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x109, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_A80")

    label("loc_A5B")


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

    label("loc_A80")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_9DD end

    def Function_4_A92(): pass

    label("Function_4_A92")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x109, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B10")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(10000)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１００００ミラ\x07\x00",
            "入手した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x109, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_B35")

    label("loc_B10")


    #A0004
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

    label("loc_B35")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A92 end

    def Function_5_B47(): pass

    label("Function_5_B47")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x109, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D14")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C42")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_BA0():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BA0)

    def lambda_BBA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BBA)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0005
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
    Battle("BattleInfo_4B4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C23"),
        (2, "loc_C32"),
        (1, "loc_C3F"),
        (SWITCH_DEFAULT, "loc_C42"),
    )


    label("loc_C23")

    SetScenarioFlags(0x76, 6)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_C42")

    label("loc_C32")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_C3F")

    OP_B7(0x0)
    Return()

    label("loc_C42")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x42F, 1)"), scpexpr(EXPR_END)), "loc_C9F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x42F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x109, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_D0F")

    label("loc_C9F")

    FadeToDark(300, 0, 100)

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x42F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x42F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D0F")

    Jump("loc_D4E")

    label("loc_D14")

    FadeToDark(300, 0, 100)

    #A0008
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

    label("loc_D4E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_B47 end

    def Function_6_D5A(): pass

    label("Function_6_D5A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(6500, 0, 4000, 0)
    MoveCamera(20, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 300, 0, -300, 90)
    SetChrPos(0x102, 0, 0, 700, 90)
    SetChrPos(0x103, -1300, 0, -800, 90)
    SetChrPos(0x104, -1600, 0, 200, 90)
    SetChrPos(0x107, 100, 0, 2500, 90)
    SetChrPos(0x108, -900, 0, 2900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x107, 0x8)
    SetChrFlags(0x108, 0x8)
    OP_68(6500, 0, -6000, 7000)
    MoveCamera(20, 19, 0, 7000)
    SetCameraDistance(23000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_11(0xB1, 0x36, 0x46, 0xF, 0x32, 0x0)
    OP_68(1800, 600, 1000, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x108, 0x8)
    OP_0D()

    #C0009
    ChrTalk(
        0x101,
        "#6P#0010Fこれは……！？\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        "#6P#0108Fま、まさか血の池……！？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        (
            "#6P#0303Fいや、血の匂いじゃねぇな。\x02\x03",

            "#0301F随分と怪しげな液体みてぇだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x108,
        (
            "#0908F……ひょっとしたら\x01",
            "何かの排水かもしれません。\x02\x03",

            "#0903Fちょうどこの上の設備で\x01",
            "《グノーシス》を大量に\x01",
            "製造していたみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#6P#0203F確かに、色は違いますが\x01",
            "あの薬と似た匂いを感じます……\x02\x03",

            "#0201F毒性は強くなさそうですが\x01",
            "直接、触れない方がいいかと。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1065():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1065)
    Sleep(50)

    def lambda_1075():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1075)
    Sleep(50)

    def lambda_1085():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1085)
    Sleep(50)

    def lambda_1095():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1095)
    Sleep(50)

    def lambda_10A5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_10A5)
    Sleep(150)

    #C0014
    ChrTalk(
        0x101,
        (
            "#11P#0001F分かった、足元には\x01",
            "気をつけた方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#11P#0106Fそ、そうよね……\x01",
            "こんな量が血であるはずが……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x107,
        (
            "#5P#0806Fここまで見た目が似てると\x01",
            "精神的にはちょっと辛いけど……\x02\x03",

            "#0801Fめげずに先に進むしかないわね！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_119D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_119D)
    Sleep(50)

    def lambda_11AD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11AD)
    Sleep(50)

    def lambda_11BD():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11BD)
    Sleep(50)

    def lambda_11CD():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11CD)
    Sleep(150)

    #C0017
    ChrTalk(
        0x101,
        "#12P#0007Fああ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -500, 0, 1000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_11(0xB1, 0x36, 0x46, 0x14, 0x41, 0x0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xE5, 5)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_6_D5A end

    SaveToFile()

Try(main)
