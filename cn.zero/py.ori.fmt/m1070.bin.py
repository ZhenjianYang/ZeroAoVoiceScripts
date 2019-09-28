from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m1070.bin",                # FileName
        "m1070",                    # MapName
        "m1070",                    # Location
        0x0070,                     # MapIndex
        "ed7304",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, -18000, -35000, 0, 0, 1, 112, 0, 1, 0, 2],
    )

    BuildStringList((
        "m1070",                  # 0
        "ＤＳ模拟",               # 1
        "bm1020",                 # 2
        "bm1020",                 # 3
        "bm1040",                 # 4
        "bm1040",                 # 5
        "bm1020",                 # 6
    ))

    ATBonus("ATBonus_238", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_CFE", 6,   6,   6,   12,  2,   2,   2)
    Sepith("Sepith_CF6", 4,   4,   0,   0,   9,   9,   9)
    Sepith("Sepith_CEE", 6,   6,   15,  9,   0,   0,   0)
    Sepith("Sepith_CD6", 13,  0,   0,   6,   6,   5,   5)

    MonsterBattlePostion("MonsterBattlePostion_288", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_300", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_268", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_26C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_270", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_274", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 2, 13, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_3D0", 0x0000, 21, 6, 60, 6, 1, 30, 0, "bm1020", "Sepith_CFE", 40, 30, 20, 10,
        (
            ("ms75200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms75200.dat", "ms62700.dat", "ms62700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_268", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms75200.dat", "ms62700.dat", "ms62700.dat", "ms62700.dat", 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms75200.dat", "ms62700.dat", "ms62700.dat", "ms62700.dat", "ms62700.dat", 0, 0, 0, "MonsterBattlePostion_268", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
        )
    )

    BattleInfo(
        "BattleInfo_560", 0x0000, 21, 6, 60, 8, 1, 25, 0, "bm1040", "Sepith_CF6", 40, 30, 20, 10,
        (
            ("ms62700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms62700.dat", "ms62700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_268", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms62700.dat", "ms65000.dat", "ms62700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms62700.dat", "ms62700.dat", "ms65000.dat", "ms62700.dat", 0, 0, 0, 0, "MonsterBattlePostion_268", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
        )
    )

    BattleInfo(
        "BattleInfo_498", 0x0000, 21, 6, 60, 8, 1, 25, 0, "bm1040", "Sepith_CEE", 40, 30, 20, 10,
        (
            ("ms65000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_268", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms65000.dat", "ms62700.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms65000.dat", "ms65000.dat", "ms62700.dat", "ms65000.dat", 0, 0, 0, 0, "MonsterBattlePostion_268", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
        )
    )

    BattleInfo(
        "BattleInfo_308", 0x0000, 21, 6, 60, 6, 1, 25, 0, "bm1020", "Sepith_CD6", 40, 30, 20, 10,
        (
            ("ms63300.dat", "ms63300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms63300.dat", "ms64600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_268", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms63300.dat", "ms64600.dat", "ms62800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
            ("ms63300.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_268", "MonsterBattlePostion_2E8", "ed7400", "ed7403", "ATBonus_238"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_628", 0x0000, 21, 6, 60, 0, 1, 0, 0, "bm1020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75200.dat", "ms75200.dat", "ms75200.dat", "ms75200.dat", "ms62700.dat", "ms62700.dat", 0, 0, "MonsterBattlePostion_268", "MonsterBattlePostion_2E8", "ed7401", "ed7403", "ATBonus_238"),
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
        "monster/ch63350.itc",               # 10
        "monster/ch63351.itc",               # 11
        "monster/ch75250.itc",               # 12
        "monster/ch75250.itc",               # 13
        "monster/ch65050.itc",               # 14
        "monster/ch65050.itc",               # 15
        "monster/ch62750.itc",               # 16
        "monster/ch62750.itc",               # 17
    ))

    DeclNpc(25500,   -14000,  0,       0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-20340,  5580,    -19380,  0x1010000,    "BattleInfo_3D0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-8170,   23150,   -17260,  0x1010000,    "BattleInfo_560", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(7250,    23220,   -17260,  0x1010000,    "BattleInfo_498", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(17630,   -60,     -15130,  0x1010000,    "BattleInfo_308", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-8350,   -25600,  -17250,  0x1010000,    "BattleInfo_498", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-26390,  -7480,   -19380,  0x1010000,    "BattleInfo_3D0", 0,   18,  0xFFFF, 2,  3)

    DeclActor(25500,   -15100,  0,       1200,    25500,   -14100,  0,       0x007C, 0,  3,  0x0000)
    DeclActor(-29150,  -19400,  6300,    1200,    -29150,  -18400,  6300,    0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_6E0",          # 00, 0
        "Function_1_6FC",          # 01, 1
        "Function_2_6FD",          # 02, 2
        "Function_3_97E",          # 03, 3
        "Function_4_B78",          # 04, 4
    ))


    def Function_0_6E0(): pass

    label("Function_0_6E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FB")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_6E0")

    label("loc_6FB")

    Return()

    # Function_0_6E0 end

    def Function_1_6FC(): pass

    label("Function_1_6FC")

    Return()

    # Function_1_6FC end

    def Function_2_6FD(): pass

    label("Function_2_6FD")

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
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_962")
    OP_70(0x0, 0x0)
    Jump("loc_966")

    label("loc_962")

    OP_70(0x0, 0x1E)

    label("loc_966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_979")
    OP_70(0x1, 0x0)
    Jump("loc_97D")

    label("loc_979")

    OP_70(0x1, 0x1E)

    label("loc_97D")

    Return()

    # Function_2_6FD end

    def Function_3_97E(): pass

    label("Function_3_97E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3A")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A77")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_9D7():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9D7)

    def lambda_9F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9F1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

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
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_628", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_A58"),
        (2, "loc_A67"),
        (1, "loc_A74"),
        (SWITCH_DEFAULT, "loc_A77"),
    )


    label("loc_A58")

    SetScenarioFlags(0x75, 1)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_A77")

    label("loc_A67")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_A74")

    OP_B7(0x0)
    Return()

    label("loc_A77")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('神圣之链', 1)"), scpexpr(EXPR_END)), "loc_ACE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x46),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11A, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_B35")

    label("loc_ACE")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x46),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x46),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_B35")

    Jump("loc_B6C")

    label("loc_B3A")

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

    label("loc_B6C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_97E end

    def Function_4_B78(): pass

    label("Function_4_B78")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C65")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('中回复药', 1)"), scpexpr(EXPR_END)), "loc_BF7")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11A, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_C60")

    label("loc_BF7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C60")

    Jump("loc_CA2")

    label("loc_C65")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
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

    label("loc_CA2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_B78 end

    SaveToFile()

Try(main)
