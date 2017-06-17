from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ボス１",                 # 1
        "ボス２",                 # 2
        "ボス３",                 # 3
        "ボス４",                 # 4
        "ボス５",                 # 5
        "ボス６",                 # 6
        "ボス７",                 # 7
        "ボス８",                 # 8
        "bc0540",                 # 9
        "bc0540",                 # 10
        "bc0540",                 # 11
        "bc0540",                 # 12
        "bc0550",                 # 13
    ))

    ATBonus("ATBonus_330", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_13DB", 10,  0,   24,  0,   7,   7,   7)
    Sepith("Sepith_13D3", 0,   10,  20,  5,   20,  0,   0)
    Sepith("Sepith_13CB", 16,  0,   0,   0,   12,  12,  12)
    Sepith("Sepith_13BB", 12,  7,   0,   18,  0,   0,   18)

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
        "BattleInfo_5C0", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_13DB", 40, 30, 20, 10,
        (
            ("ms76600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76600.dat", "ms76700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_370", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76600.dat", "ms76700.dat", "ms76700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76600.dat", "ms76700.dat", "ms76700.dat", "ms76700.dat", 0, 0, 0, 0, "MonsterBattlePostion_370", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
        )
    )

    BattleInfo(
        "BattleInfo_4F8", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_13D3", 40, 30, 20, 10,
        (
            ("ms76800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76800.dat", "ms76800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76800.dat", "ms76800.dat", "ms76800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76800.dat", "ms76800.dat", "ms76800.dat", "ms76800.dat", 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
        )
    )

    BattleInfo(
        "BattleInfo_688", 0x0000, 33, 6, 60, 4, 1, 30, 0, "bc0540", "Sepith_13CB", 40, 30, 20, 10,
        (
            ("ms76500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76500.dat", "ms76500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_370", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76500.dat", "ms76700.dat", "ms76500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
            ("ms76500.dat", "ms76500.dat", "ms76700.dat", "ms76500.dat", 0, 0, 0, 0, "MonsterBattlePostion_370", "MonsterBattlePostion_3F0", "ed7400", "ed7403", "ATBonus_330"),
        )
    )

    BattleInfo(
        "BattleInfo_430", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_13BB", 40, 30, 20, 10,
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
        "Function_4_B88",          # 04, 4
        "Function_5_C93",          # 05, 5
        "Function_6_1005",         # 06, 6
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B51")
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
            "#60I時のセピス×２００\x01\x07\x02",

            "#61I空のセピス×２００\x01\x07\x02",

            "#62I幻のセピス×２００\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x113, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_B76")

    label("loc_B51")


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

    label("loc_B76")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_A8B end

    def Function_4_B88(): pass

    label("Function_4_B88")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0003
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C75")
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

    label("loc_C75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C91")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_C91")

    Return()

    # Function_4_B88 end

    def Function_5_C93(): pass

    label("Function_5_C93")

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

    def lambda_E7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E7F)
    Sleep(100)

    def lambda_E93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E93)

    def lambda_EA4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EA4)
    Sleep(100)

    def lambda_EB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_EB8)

    def lambda_EC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_EC9)
    Sleep(100)

    def lambda_EDD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_EDD)
    Sleep(100)

    def lambda_EF1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_EF1)

    def lambda_F02():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_F02)
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

    # Function_5_C93 end

    def Function_6_1005(): pass

    label("Function_6_1005")

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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32C, 1)
    OP_29(0x4C, 0x1, 0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1192")

    #C0005
    ChrTalk(
        0x101,
        (
            "#0000F#5Pずいぶん大きな鍵だけど\x01",
            "ひょっとして……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        (
            "#6P#0202Fええ、応接間のギミックを\x01",
            "解除するものでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1369")

    label("loc_1192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1205")
    OP_29(0x4C, 0x1, 0x17)

    #C0007
    ChrTalk(
        0x101,
        "#0000F#5P２つ目の鍵か……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        (
            "#6P#0202Fこれで応接間のギミックを\x01",
            "解除できそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1369")

    label("loc_1205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1302")
    OP_29(0x4C, 0x1, 0x18)

    #C0009
    ChrTalk(
        0x101,
        (
            "#0000F#5Pまた似たような\x01",
            "鍵を見つけたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        (
            "#6P#0100Fどこかで使う場所が\x01",
            "あるのかもしれないわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x10A,
        (
            "#12P#0603F──倉庫も一通り調べた。\x02\x03",

            "#0600Fいったん戻って\x01",
            "ルバーチェのビルをもう一度\x01",
            "調べてみるべきかもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1369")

    label("loc_1302")


    #C0012
    ChrTalk(
        0x101,
        (
            "#0005F#5Pずいぶん大きな鍵だけど\x01",
            "何に使うものなんだ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        "#6P#0101F一応、持っておきましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_1369")

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

    # Function_6_1005 end

    SaveToFile()

Try(main)
