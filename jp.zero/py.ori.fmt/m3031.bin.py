from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3031.bin",                # FileName
        "m3031",                    # MapName
        "m3031",                    # Location
        0x007E,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -3000, -7000, -9000, 0, 0, 1, 126, 0, 0, 0, 1],
    )

    BuildStringList((
        "m3031",                  # 0
        "bm3040",                 # 1
        "bm3040",                 # 2
        "bm3030",                 # 3
        "bm3030",                 # 4
    ))

    ATBonus("ATBonus_210", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_F85", 12,  0,   0,   8,   18,  10,  16)
    Sepith("Sepith_F8D", 9,   9,   9,   9,   10,  10,  10)
    Sepith("Sepith_FA5", 7,   7,   14,  7,   9,   12,  12)
    Sepith("Sepith_FAD", 5,   18,  5,   5,   12,  12,  12)

    MonsterBattlePostion("MonsterBattlePostion_270", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_274", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_250", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_254", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_258", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_25C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_268", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_26C", 2, 13, 180)

    # monster count: 5

    BattleInfo(
        "BattleInfo_2F0", 0x0000, 43, 6, 60, 4, 1, 30, 0, "bm3040", "Sepith_F85", 60, 25, 10, 5,
        (
            ("ms60700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_270", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms60700.dat", "ms77300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_250", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms60700.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_270", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms60700.dat", "ms77300.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, "MonsterBattlePostion_250", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
        )
    )

    BattleInfo(
        "BattleInfo_548", 0x0000, 43, 6, 60, 4, 1, 30, 0, "bm3030", "Sepith_F8D", 60, 25, 10, 5,
        (
            ("ms61500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_270", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms61500.dat", "ms77300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_250", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms61500.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_270", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms61500.dat", "ms77300.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, "MonsterBattlePostion_250", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
        )
    )

    BattleInfo(
        "BattleInfo_480", 0x0000, 43, 6, 60, 4, 1, 60, 0, "bm3030", "Sepith_FA5", 60, 25, 10, 5,
        (
            ("ms72500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_270", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms72500.dat", "ms77300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_250", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms72500.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_270", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms72500.dat", "ms77300.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, "MonsterBattlePostion_250", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
        )
    )

    BattleInfo(
        "BattleInfo_3B8", 0x0000, 43, 6, 60, 4, 1, 30, 0, "bm3040", "Sepith_FAD", 60, 25, 10, 5,
        (
            ("ms75300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_270", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms75300.dat", "ms77300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_250", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms75300.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_270", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
            ("ms75300.dat", "ms77300.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, "MonsterBattlePostion_250", "MonsterBattlePostion_2D0", "ed7402", "ed7403", "ATBonus_210"),
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
        "monster/ch60750.itc",               # 10
        "monster/ch60750.itc",               # 11
        "monster/ch75350.itc",               # 12
        "monster/ch75350.itc",               # 13
        "monster/ch72550.itc",               # 14
        "monster/ch72551.itc",               # 15
        "monster/ch61550.itc",               # 16
        "monster/ch61550.itc",               # 17
    ))

    DeclMonster(-28800,  -14090,  -7000,   0x1010000,    "BattleInfo_2F0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-40820,  -520,    3000,    0x1010000,    "BattleInfo_548", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(133590,  14320,   0,       0x1010000,    "BattleInfo_480", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(144880,  -29970,  -4500,   0x1010000,    "BattleInfo_3B8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(169360,  -1300,   -4500,   0x1010000,    "BattleInfo_2F0", 0,   16,  0xFFFF, 0,  1)

    DeclActor(-48250,  3000,    0,       1200,    -48250,  4000,    0,       0x007C, 0,  2,  0x0000)
    DeclActor(144140,  -4500,   -35640,  1200,    144140,  -3500,   -35640,  0x007C, 0,  3,  0x0000)
    DeclActor(185700,  1030,    16500,   2500,    185700,  2029,    16500,   0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7

    ScpFunction((
        "Function_0_684",          # 00, 0
        "Function_1_685",          # 01, 1
        "Function_2_AFF",          # 02, 2
        "Function_3_C4C",          # 03, 3
        "Function_4_D99",          # 04, 4
    ))


    def Function_0_684(): pass

    label("Function_0_684")

    Return()

    # Function_0_684 end

    def Function_1_685(): pass

    label("Function_1_685")

    ClearMapObjFlags(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 5)), scpexpr(EXPR_END)), "loc_6A1")
    OP_70(0x6, 0x96)
    OP_70(0x3, 0x1E)
    Jump("loc_6A9")

    label("loc_6A1")

    OP_70(0x6, 0x78)
    OP_70(0x3, 0x0)

    label("loc_6A9")

    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9A")
    OP_70(0x4, 0x0)
    Jump("loc_A9E")

    label("loc_A9A")

    OP_70(0x4, 0x1E)

    label("loc_A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB1")
    OP_70(0x5, 0x0)
    Jump("loc_AB5")

    label("loc_AB1")

    OP_70(0x5, 0x1E)

    label("loc_AB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AF8")
    OP_24(0x82)
    Jump("loc_AFE")

    label("loc_AF8")

    Sound(130, 1, 100, 0)

    label("loc_AFE")

    Return()

    # Function_1_685 end

    def Function_2_AFF(): pass

    label("Function_2_AFF")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFB")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_B84")
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
    SetScenarioFlags(0x11D, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_BF6")

    label("loc_B84")

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
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_BF6")

    Jump("loc_C40")

    label("loc_BFB")

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

    label("loc_C40")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_AFF end

    def Function_3_C4C(): pass

    label("Function_3_C4C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D48")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_CD1")
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
    SetScenarioFlags(0x11D, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_D43")

    label("loc_CD1")

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
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D43")

    Jump("loc_D8D")

    label("loc_D48")

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

    label("loc_D8D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_C4C end

    def Function_4_D99(): pass

    label("Function_4_D99")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 5)), scpexpr(EXPR_END)), "loc_DDE")
    TalkBegin(0xFF)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにレバーは下りている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_EFC")

    label("loc_DDE")

    EventBegin(0x1)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レバーがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF5")
    Fade(500)
    SetChrPos(0x0, 184570, 0, 16470, 89)
    SetChrPos(0x1, 183000, 0, 17440, 89)
    SetChrPos(0x2, 183000, 0, 15470, 89)
    SetChrPos(0x3, 181500, 0, 16440, 89)
    OP_68(184180, 1800, 17890, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0x6, 0x78, 0x96, 0x0, 0x0)
    OP_79(0x6)
    Sleep(500)
    Sound(155, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x3)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    SetScenarioFlags(0xF5, 5)

    label("loc_EF5")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_EFC")

    Return()

    # Function_4_D99 end

    SaveToFile()

Try(main)
