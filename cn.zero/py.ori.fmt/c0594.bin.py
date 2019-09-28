from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0594.bin",                # FileName
        "c0594",                    # MapName
        "c0594",                    # Location
        0x0029,                     # MapIndex
        "ed7122",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0594",                  # 0
        "事件用魔兽",             # 1
        "事件用魔兽",             # 2
        "事件用魔兽",             # 3
        "食人鲨",                 # 4
        "bc0540",                 # 5
        "bc0540",                 # 6
        "bc0540",                 # 7
        "bc0540",                 # 8
        "bc0540",                 # 9
    ))

    ATBonus("ATBonus_288", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1C75", 0,   15,  0,   20,  20,  0,   0)
    Sepith("Sepith_1C6D", 12,  7,   0,   18,  0,   0,   18)
    Sepith("Sepith_1C7D", 16,  0,   0,   0,   12,  12,  12)

    MonsterBattlePostion("MonsterBattlePostion_2E8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_34C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_350", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_354", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_358", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_35C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_360", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_430", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_1C75", 40, 30, 20, 10,
        (
            ("ms76700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
            ("ms76700.dat", "ms76700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
            ("ms76700.dat", "ms76700.dat", "ms76700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
            ("ms76700.dat", "ms76700.dat", "ms76700.dat", "ms76700.dat", 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
        )
    )

    BattleInfo(
        "BattleInfo_368", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_1C6D", 40, 30, 20, 10,
        (
            ("ms76900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
            ("ms76900.dat", "ms76900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
            ("ms76900.dat", "ms76900.dat", "ms76900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
            ("ms76900.dat", "ms76900.dat", "ms76900.dat", "ms76900.dat", 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
        )
    )

    BattleInfo(
        "BattleInfo_4F8", 0x0000, 33, 6, 60, 4, 1, 30, 0, "bc0540", "Sepith_1C7D", 40, 30, 20, 10,
        (
            ("ms76500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
            ("ms76500.dat", "ms76500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2C8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
            ("ms76500.dat", "ms76500.dat", "ms76500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
            ("ms76500.dat", "ms76500.dat", "ms76500.dat", "ms76500.dat", 0, 0, 0, 0, "MonsterBattlePostion_2C8", "MonsterBattlePostion_348", "ed7400", "ed7403", "ATBonus_288"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_604", 0x0000, 33, 6, 45, 0, 1, 0, 0, "bc0540", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76800.dat", "ms76800.dat", "ms76800.dat", "ms76800.dat", 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7401", "ed7403", "ATBonus_288"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5C0", 0x0002, 33, 6, 45, 0, 1, 0, 0, "bc0540", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76900.dat", "ms76900.dat", "ms76900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_348", "ed7401", "ed7403", "ATBonus_288"),
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
        "monster/ch76950.itc",               # 10
        "monster/ch76951.itc",               # 11
        "monster/ch76750.itc",               # 12
        "monster/ch76750.itc",               # 13
        "monster/ch76550.itc",               # 14
        "monster/ch76551.itc",               # 15
        "monster/ch76850.itc",               # 16
        "monster/ch76850.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   16,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   16,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   16,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-2000,   3500,    12000,   0,    484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-14380,  10040,   500,     0x1010000,    "BattleInfo_430", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-31150,  10850,   30,      0x1010000,    "BattleInfo_368", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-28130,  -2100,   20,      0x1010000,    "BattleInfo_4F8", 0,   20,  0xFFFF, 4,  5)

    DeclActor(-34000,  6000,    16000,   1200,    -34000,  7000,    16000,   0x007C, 0,  4,  0x0000)
    DeclActor(-18000,  1500,    500,     1200,    -18000,  2500,    500,     0x007C, 0,  5,  0x0000)
    DeclActor(-2000,   3000,    12000,   1200,    -2000,   4000,    12000,   0x007C, 0,  6,  0x0000)
    DeclActor(-14000,  500,     13000,   1200,    -14000,  1500,    13000,   0x007C, 0,  7,  0x0000)
    DeclActor(-5000,   500,     -8000,   1200,    -5000,   1500,    -8000,   0x007C, 0,  8,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_6C8",          # 00, 0
        "Function_1_6E5",          # 01, 1
        "Function_2_702",          # 02, 2
        "Function_3_714",          # 03, 3
        "Function_4_AA6",          # 04, 4
        "Function_5_BDC",          # 05, 5
        "Function_6_CCB",          # 06, 6
        "Function_7_EC5",          # 07, 7
        "Function_8_F9A",          # 08, 8
        "Function_9_106F",         # 09, 9
        "Function_10_1289",        # 0A, 10
        "Function_11_1714",        # 0B, 11
        "Function_12_1762",        # 0C, 12
        "Function_13_17B0",        # 0D, 13
    ))


    def Function_0_6C8(): pass

    label("Function_0_6C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E4")
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_6C8")

    label("loc_6E4")

    Return()

    # Function_0_6C8 end

    def Function_1_6E5(): pass

    label("Function_1_6E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_701")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_6E5")

    label("loc_701")

    Return()

    # Function_1_6E5 end

    def Function_2_702(): pass

    label("Function_2_702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_713")
    Event(0, 10)

    label("loc_713")

    Return()

    # Function_2_702 end

    def Function_3_714(): pass

    label("Function_3_714")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -16000, 0, 16000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, -12000, 0, 16000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x2, 0x1, 0x0, -16000, 3000, 16000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, -12000, 3000, 16000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x4, 0x1, 0x0, -16000, 3000, -16000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, -12000, 3000, -16000, 3000, 1000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 2)), scpexpr(EXPR_END)), "loc_810")
    SetMapObjFrame(0xFF, "lgt1_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    OP_70(0x3, 0x2D)
    OP_70(0x4, 0x2D)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    Jump("loc_850")

    label("loc_810")

    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x1, 0x1)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)

    label("loc_850")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A73")
    OP_70(0x0, 0x0)
    Jump("loc_A77")

    label("loc_A73")

    OP_70(0x0, 0x1E)

    label("loc_A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8A")
    OP_70(0x1, 0x0)
    Jump("loc_A8E")

    label("loc_A8A")

    OP_70(0x1, 0x1E)

    label("loc_A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA1")
    OP_70(0x2, 0x0)
    Jump("loc_AA5")

    label("loc_AA1")

    OP_70(0x2, 0x1E)

    label("loc_AA5")

    Return()

    # Function_3_714 end

    def Function_4_AA6(): pass

    label("Function_4_AA6")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B93")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('魔防１', 1)"), scpexpr(EXPR_END)), "loc_B25")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x78),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x112, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_B8E")

    label("loc_B25")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x78),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x78),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_B8E")

    Jump("loc_BD0")

    label("loc_B93")

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

    label("loc_BD0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_AA6 end

    def Function_5_BDC(): pass

    label("Function_5_BDC")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9C")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I时之耀晶片×２００\x01\x07\x02",

            "#61I空之耀晶片×２００\x01\x07\x02",

            "#62I幻之耀晶片×２００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x113, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_CB9")

    label("loc_C9C")


    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_CB9")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_BDC end

    def Function_6_CCB(): pass

    label("Function_6_CCB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E87")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC4")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_D24():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D24)

    def lambda_D3E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_D3E)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xB, 1)
    Battle("BattleInfo_604", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_DA5"),
        (2, "loc_DB4"),
        (1, "loc_DC1"),
        (SWITCH_DEFAULT, "loc_DC4"),
    )


    label("loc_DA5")

    SetScenarioFlags(0x76, 1)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_DC4")

    label("loc_DB4")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_DC1")

    OP_B7(0x0)
    Return()

    label("loc_DC4")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('驱动２', 1)"), scpexpr(EXPR_END)), "loc_E1B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x90),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x113, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_E82")

    label("loc_E1B")

    FadeToDark(300, 0, 100)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x90),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x90),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E82")

    Jump("loc_EB9")

    label("loc_E87")

    FadeToDark(300, 0, 100)

    #A0009
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

    label("loc_EB9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_CCB end

    def Function_7_EC5(): pass

    label("Function_7_EC5")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有升降机控制装置。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F92")
    Fade(500)
    SetChrPos(0x0, -14290, 500, 11950, 0)
    SetChrPos(0x1, -13300, 500, 10400, 0)
    SetChrPos(0x2, -14700, 500, 10400, 0)
    SetChrPos(0x3, -14170, 500, 9040, 0)
    OP_68(-14130, 1000, 11990, 0)
    MoveCamera(45, 36, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Call(0, 9)

    label("loc_F92")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_EC5 end

    def Function_8_F9A(): pass

    label("Function_8_F9A")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有升降机控制装置。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1067")
    Fade(500)
    SetChrPos(0x0, -6280, 500, -8440, 89)
    SetChrPos(0x1, -8000, 500, -7280, 89)
    SetChrPos(0x2, -8000, 500, -8730, 89)
    SetChrPos(0x3, -9640, 500, -8320, 89)
    OP_68(-6670, 1000, -8280, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Call(0, 9)

    label("loc_1067")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_F9A end

    def Function_9_106F(): pass

    label("Function_9_106F")

    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 2)), scpexpr(EXPR_END)), "loc_1184")
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x1, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-14240, 750, 16100, 0)
    MoveCamera(45, 49, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x3, 0x2D, 0x0, 0x0, 0x0)
    OP_79(0x3)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    OP_68(-12930, 1000, -14980, 0)
    MoveCamera(45, 49, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x4, 0x2D, 0x0, 0x0, 0x0)
    OP_79(0x4)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    ClearScenarioFlags(0xD5, 2)
    Jump("loc_1288")

    label("loc_1184")

    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt1_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-14240, 750, 16100, 0)
    MoveCamera(45, 49, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x3, 0x0, 0x2D, 0x0, 0x0)
    OP_79(0x3)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    OP_68(-12930, 1000, -14980, 0)
    MoveCamera(45, 49, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x4, 0x0, 0x2D, 0x0, 0x0)
    OP_79(0x4)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetScenarioFlags(0xD5, 2)

    label("loc_1288")

    Return()

    # Function_9_106F end

    def Function_10_1289(): pass

    label("Function_10_1289")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    OP_68(-12000, 1000, 2500, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(40500, 0)
    SetChrPos(0x101, -3700, 30, 700, 270)
    SetChrPos(0x102, -2000, 0, 0, 270)
    SetChrPos(0x103, -1800, 0, -1100, 270)
    SetChrPos(0x104, -2200, 0, 1100, 270)
    SetChrPos(0x10A, -3500, 20, -700, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x10)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -2000, 0, 15500, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x10)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -2000, 0, 15500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x10)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -2000, 0, 15500, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-17000, 500, 2500, 8000)
    MoveCamera(30, 7, 0, 8000)
    SetCameraDistance(34500, 8000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-6000, 1000, 0, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    OP_68(-3000, 1000, 0, 2000)
    OP_6F(0x1)

    #C0012
    ChrTalk(
        0x102,
        (
            "#0101F#11P这里是……\x01",
            "放置走私货物用的仓库吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x10A,
        (
            "#11P#0603F应该没错吧。\x02\x03",

            "#0610F哼，如果有搜查令的话，\x01",
            "就可以彻底查个遍了……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#11P#0008F是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x104, 0x0, 0x1F4)

    #C0015
    ChrTalk(
        0x104,
        "#12P#0301F喂……好像有什么东西！\x02",
    )

    CloseMessageWindow()

    def lambda_151F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_151F)
    Sleep(50)

    def lambda_152F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_152F)
    Sleep(50)

    def lambda_153F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_153F)
    Sleep(50)
    OP_93(0x102, 0x0, 0x1F4)

    #C0016
    ChrTalk(
        0x103,
        "#0205F#12P那是……\x02",
    )

    CloseMessageWindow()
    OP_68(-2400, 700, 3000, 2500)
    MoveCamera(35, 20, 0, 2500)
    SetCameraDistance(20500, 2500)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x8, 3, 0, 11)
    Sleep(300)
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0x9, 3, 0, 12)
    Sleep(300)
    BeginChrThread(0xA, 0, 0, 1)

    def lambda_15D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15D5)

    def lambda_15E6():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15E6)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 1)
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
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0017
    ChrTalk(
        0x101,
        "#6P#0005F魔、魔兽！？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x10A,
        "#0607F#12P嘁……干掉它们！\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(19000, 300)

    def lambda_169E():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_169E)

    def lambda_16B8():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_16B8)

    def lambda_16D2():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16D2)
    Sleep(300)
    Battle("BattleInfo_5C0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    Call(0, 13)
    Return()

    # Function_10_1289 end

    def Function_11_1714(): pass

    label("Function_11_1714")


    def lambda_1719():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1719)

    def lambda_172A():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x2134, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_172A)
    WaitChrThread(0xFE, 1)

    def lambda_1748():
        OP_96(0xFE, 0xFFFFF2B8, 0x0, 0x1194, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1748)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_1714 end

    def Function_12_1762(): pass

    label("Function_12_1762")


    def lambda_1767():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1767)

    def lambda_1778():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x2134, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1778)
    WaitChrThread(0xFE, 1)

    def lambda_1796():
        OP_96(0xFE, 0xFFFFED40, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1796)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_1762 end

    def Function_13_17B0(): pass

    label("Function_13_17B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    OP_68(-1650, 700, 2590, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20850, 0)
    SetChrPos(0x101, -3700, 30, 700, 0)
    SetChrPos(0x102, -2000, 0, 0, 0)
    SetChrPos(0x103, -1800, 0, -1100, 0)
    SetChrPos(0x104, -2200, 0, 1100, 0)
    SetChrPos(0x10A, -3500, 20, -700, 0)
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
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_E0(0x1)
    OP_68(-1650, 700, 1590, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0019
    ChrTalk(
        0x101,
        (
            "#6P#0005F为、为什么……\x01",
            "这种地方会有魔兽……！？\x02\x03",

            "#0001F而且是在克洛斯贝尔地区\x01",
            "从没见过的种类……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        (
            "#0108F#11P刚才那种魔兽很像是\x01",
            "栖息在利贝尔的『飞行猫』……\x02\x03",

            "#0101F但是，应该没有\x01",
            "这么厉害才对……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x10A,
        (
            "#12P#0603F……那些家伙有时候也会做些\x01",
            "走私魔兽之类的生意。\x02\x03",

            "#0601F就像把那些军犬\x01",
            "走私入境一样。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A41():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A41)
    Sleep(50)

    def lambda_1A51():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1A51)
    Sleep(50)

    def lambda_1A61():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1A61)
    Sleep(50)
    TurnDirection(0x102, 0x10A, 500)

    #C0022
    ChrTalk(
        0x101,
        (
            "#5P#0011F走私魔兽……\x01",
            "还有这种市场需要吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x10A,
        (
            "#12P#0606F基本都是卖给那些爱好特殊的资产家吧。\x02\x03",

            "#0601F当然，在大多数国家中，\x01",
            "这种行为都是违法的。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#5P#0306F哎呀呀，真是不得了啊。\x02\x03",

            "#0301F话说回来，总感觉还有其它\x01",
            "东西在附近徘徊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#0211F#11P……看来，想继续前进的话，\x01",
            "似乎不是那么简单呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_37()
    OP_68(-2500, 500, 0, 0)
    MoveCamera(45, 36, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -2500, 0, 0, 270)
    SetChrPos(0x1, -2500, 0, 0, 270)
    SetChrPos(0x2, -2500, 0, 0, 270)
    SetChrPos(0x3, -2500, 0, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC4, 7)
    OP_29(0x4C, 0x1, 0x11)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_17B0 end

    SaveToFile()

Try(main)
