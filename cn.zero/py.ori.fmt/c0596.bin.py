from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0596.bin",                # FileName
        "c0596",                    # MapName
        "c0596",                    # Location
        0x0029,                     # MapIndex
        "ed7122",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0596",                  # 0
        "ＢＯＳＳ１",             # 1
        "ＢＯＳＳ２",             # 2
        "ＢＯＳＳ３",             # 3
        "ＢＯＳＳ４",             # 4
        "ＢＯＳＳ５",             # 5
        "ＢＯＳＳ６",             # 6
        "ＢＯＳＳ７",             # 7
        "ＢＯＳＳ８",             # 8
        "bc0540",                 # 9
        "bc0540",                 # 10
        "bc0540",                 # 11
        "bc0540",                 # 12
        "bc0550",                 # 13
    ))

    ATBonus("ATBonus_330", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1341", 10,  0,   24,  0,   7,   7,   7)
    Sepith("Sepith_1339", 0,   10,  20,  5,   20,  0,   0)
    Sepith("Sepith_1331", 16,  0,   0,   0,   12,  12,  12)
    Sepith("Sepith_1321", 12,  7,   0,   18,  0,   0,   18)

    MonsterBattlePostion("MonsterBattlePostion_390", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_400", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_404", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_408", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_370", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 10, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 4, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 9, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 5, 13, 180)

    # monster count: 4

    BattleInfo(
        "BattleInfo_5C0", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_1341", 40, 30, 20, 10,
        (
            ("ms76600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76600.dat", "ms76700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_370", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76600.dat", "ms76700.dat", "ms76700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76600.dat", "ms76700.dat", "ms76700.dat", "ms76700.dat", 0, 0, 0, 0, "MonsterBattlePostion_370", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
        )
    )

    BattleInfo(
        "BattleInfo_4F8", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_1339", 40, 30, 20, 10,
        (
            ("ms76800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76800.dat", "ms76800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76800.dat", "ms76800.dat", "ms76800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76800.dat", "ms76800.dat", "ms76800.dat", "ms76800.dat", 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
        )
    )

    BattleInfo(
        "BattleInfo_688", 0x0000, 33, 6, 60, 4, 1, 30, 0, "bc0540", "Sepith_1331", 40, 30, 20, 10,
        (
            ("ms76500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76500.dat", "ms76500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_370", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76500.dat", "ms76700.dat", "ms76500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76500.dat", "ms76500.dat", "ms76700.dat", "ms76500.dat", 0, 0, 0, 0, "MonsterBattlePostion_370", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
        )
    )

    BattleInfo(
        "BattleInfo_430", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_1321", 40, 30, 20, 10,
        (
            ("ms76900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76900.dat", "ms76900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76900.dat", "ms76700.dat", "ms76900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76900.dat", "ms76900.dat", "ms76700.dat", "ms76900.dat", 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_750", 0x0002, 33, 6, 90, 0, 1, 0, 0, "bc0550", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76600.dat", "ms76600.dat", "ms76600.dat", "ms76600.dat", "ms76600.dat", "ms76600.dat", "ms76600.dat", "ms76600.dat", "MonsterBattlePostion_410", "MonsterBattlePostion_3F0", "ed7401", "ed7403", "ATBonus_330"),
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
        "monster/ch76850.itc",               # 12
        "monster/ch76850.itc",               # 13
        "monster/ch76650.itc",               # 14
        "monster/ch76650.itc",               # 15
        "monster/ch76550.itc",               # 16
        "monster/ch76551.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-18350,  -10000,  1500,    0x1010000,    "BattleInfo_5C0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-21220,  11200,   20,      0x1010000,    "BattleInfo_4F8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-32619,  -3000,   0,       0x1010000,    "BattleInfo_688", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-15810,  -15040,  0,       0x1010000,    "BattleInfo_430", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 5,   -15.0,                 12.0,                  2.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   7.5,                   -2.3999998569488525,   -0.3999999761581421,   1.0])

    DeclActor(-34000,  0,       16000,   1200,    -34000,  1000,    16000,   0x007C, 0,  3,  0x0000)
    DeclActor(-4500,   3000,    13800,   1200,    -4500,   4500,    13800,   0x007C, 0,  6,  0x0000)
    DeclActor(-26000,  3000,    16000,   1200,    -26000,  4500,    16000,   0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_810",          # 00, 0
        "Function_1_82D",          # 01, 1
        "Function_2_82E",          # 02, 2
        "Function_3_A8B",          # 03, 3
        "Function_4_B7A",          # 04, 4
        "Function_5_C6D",          # 05, 5
        "Function_6_FDF",          # 06, 6
    ))


    def Function_0_810(): pass

    label("Function_0_810")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_82C")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_810")

    label("loc_82C")

    Return()

    # Function_0_810 end

    def Function_1_82D(): pass

    label("Function_1_82D")

    Return()

    # Function_1_82D end

    def Function_2_82E(): pass

    label("Function_2_82E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_846")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_863")
    OP_65(0x1, 0x1)
    SetMapObjFrame(0xFF, "key_blue", 0x0, 0x1)

    label("loc_863")

    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A86")
    OP_70(0x0, 0x0)
    Jump("loc_A8A")

    label("loc_A86")

    OP_70(0x0, 0x1E)

    label("loc_A8A")

    Return()

    # Function_2_82E end

    def Function_3_A8B(): pass

    label("Function_3_A8B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4B")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    #A0001
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
    SetScenarioFlags(0x113, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_B68")

    label("loc_B4B")


    #A0002
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

    label("loc_B68")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_A8B end

    def Function_4_B7A(): pass

    label("Function_4_B7A")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0003
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4F")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x1, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x1, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_C4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_C6B")

    Return()

    # Function_4_B7A end

    def Function_5_C6D(): pass

    label("Function_5_C6D")

    EventBegin(0x0)
    OP_E0(0x1)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-15400, 3600, 12000, 0)
    MoveCamera(40, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, -15400, 3000, 12500, 90)
    SetChrPos(0x1, -15400, 3000, 11500, 90)
    SetChrPos(0x2, -16600, 3000, 12500, 90)
    SetChrPos(0x3, -16600, 3000, 11500, 90)
    OP_68(-12000, 3600, 12000, 2000)
    SetCameraDistance(23000, 2000)
    OP_0D()
    SetChrPos(0x8, -12000, 3000, 12000, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x9, -11500, 3000, 14200, 225)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0xA, -11500, 3000, 9800, 315)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xB, -10000, 3000, 12900, 270)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xC, -10000, 3000, 11100, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xD, -8000, 3000, 12000, 270)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xE, -7500, 3000, 14200, 225)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xF, -7500, 3000, 9800, 315)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    Sound(202, 0, 100, 0)

    def lambda_E59():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E59)
    Sleep(100)

    def lambda_E6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E6D)

    def lambda_E7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E7E)
    Sleep(100)

    def lambda_E92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E92)

    def lambda_EA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_EA3)
    Sleep(100)

    def lambda_EB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_EB7)
    Sleep(100)

    def lambda_ECB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_ECB)

    def lambda_EDC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_EDC)
    Sleep(100)
    WaitChrThread(0xF, 2)
    OP_6F(0x11)
    Sleep(300)
    Battle("BattleInfo_750", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    OP_68(-15000, 3500, 12000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x0, -15000, 3000, 12000, 90)
    SetChrPos(0x1, -15000, 3000, 12000, 90)
    SetChrPos(0x2, -15000, 3000, 12000, 90)
    SetChrPos(0x3, -15000, 3000, 12000, 90)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xC5, 0)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_5_C6D end

    def Function_6_FDF(): pass

    label("Function_6_FDF")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_68(-4500, 3700, 13800, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -5500, 3000, 13800, 90)
    SetChrPos(0x102, -6700, 3000, 13600, 90)
    SetChrPos(0x103, -6700, 3000, 12500, 90)
    SetChrPos(0x104, -6700, 3000, 14700, 135)
    SetChrPos(0x10A, -5500, 3000, 12500, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    Sleep(300)
    Fade(250)
    SetMapObjFrame(0xFF, "key_blue", 0x0, 0x1)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32C, 1)
    OP_29(0x4C, 0x1, 0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1146")

    #C0005
    ChrTalk(
        0x101,
        (
            "#0000F#5P好大的钥匙，\x01",
            "难道说……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        (
            "#6P#0202F嗯，应该是用来\x01",
            "解除客厅机关的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CF")

    label("loc_1146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11B3")
    OP_29(0x4C, 0x1, 0x17)

    #C0007
    ChrTalk(
        0x101,
        "#0000F#5P第二把钥匙吗……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        (
            "#6P#0202F这样的话，客厅的机关\x01",
            "应该就能解除了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CF")

    label("loc_11B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_127E")
    OP_29(0x4C, 0x1, 0x18)

    #C0009
    ChrTalk(
        0x101,
        (
            "#0000F#5P又发现了\x01",
            "相似的钥匙……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        (
            "#6P#0100F也许会在其它地方\x01",
            "派上用场吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x10A,
        (
            "#12P#0603F──仓库也大致调查过了。\x02\x03",

            "#0600F或许应该先回去一趟，\x01",
            "再调查一遍\x01",
            "鲁巴彻的大厅。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CF")

    label("loc_127E")


    #C0012
    ChrTalk(
        0x101,
        (
            "#0005F#5P好大的钥匙，\x01",
            "是用来做什么的呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        "#6P#0101F总之，先拿着吧。\x02",
    )

    CloseMessageWindow()

    label("loc_12CF")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -6000, 3000, 13800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x1, 0x1)
    SetScenarioFlags(0xC5, 1)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_6_FDF end

    SaveToFile()

Try(main)
