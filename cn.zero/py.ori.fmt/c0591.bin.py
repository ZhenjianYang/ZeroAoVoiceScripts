from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0591.bin",                # FileName
        "c0591",                    # MapName
        "c0591",                    # Location
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
        "c0591",                  # 0
        "MapThread",              # 1
        "bc0520",                 # 2
        "bc0520",                 # 3
        "bc0520",                 # 4
        "bc0520",                 # 5
    ))

    ATBonus("ATBonus_24C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1359", 9,   9,   9,   9,   0,   0,   19)
    Sepith("Sepith_1351", 9,   9,   9,   9,   0,   19,  0)
    Sepith("Sepith_1349", 9,   9,   9,   9,   19,  0,   0)

    MonsterBattlePostion("MonsterBattlePostion_2AC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_310", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_314", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_318", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_31C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_320", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_324", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 5, 5, 45)

    # monster count: 6

    BattleInfo(
        "BattleInfo_4BC", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_1359", 40, 30, 20, 10,
        (
            ("ms67800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms67800.dat", "ms67800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms67800.dat", "ms67900.dat", "ms67800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms67800.dat", "ms67800.dat", "ms67900.dat", "ms67800.dat", 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
        )
    )

    BattleInfo(
        "BattleInfo_3F4", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_1351", 40, 30, 20, 10,
        (
            ("ms67700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms67700.dat", "ms67700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms67700.dat", "ms67900.dat", "ms67700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms67700.dat", "ms67700.dat", "ms67900.dat", "ms67700.dat", 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
        )
    )

    BattleInfo(
        "BattleInfo_32C", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_1349", 40, 30, 20, 10,
        (
            ("ms67600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms67600.dat", "ms67600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms67600.dat", "ms67900.dat", "ms67600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms67600.dat", "ms67600.dat", "ms67900.dat", "ms67600.dat", 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_30C", "ed7400", "ed7403", "ATBonus_24C"),
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
        "monster/ch67650.itc",               # 10
        "monster/ch67650.itc",               # 11
        "monster/ch67750.itc",               # 12
        "monster/ch67750.itc",               # 13
        "monster/ch67850.itc",               # 14
        "monster/ch67850.itc",               # 15
        "monster/ch67950.itc",               # 16
        "monster/ch67950.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-10710,  -1000,   0,       0x1010000,    "BattleInfo_4BC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(5840,    -15170,  0,       0x1010000,    "BattleInfo_3F4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-52330,  19460,   20,      0x1010000,    "BattleInfo_32C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-44450,  65640,   30,      0x1010000,    "BattleInfo_4BC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-56410,  61600,   30,      0x1010000,    "BattleInfo_3F4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(21830,   49490,   0,       0x1010000,    "BattleInfo_32C", 0,   16,  0xFFFF, 0,  1)

    DeclActor(-44000,  0,       68000,   1200,    -44000,  1000,    68000,   0x007C, 0,  4,  0x0000)
    DeclActor(-37400,  0,       54410,   1200,    -37400,  1000,    54410,   0x007C, 0,  5,  0x0000)
    DeclActor(-54020,  0,       72660,   1200,    -54020,  1000,    72660,   0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_6C8",          # 00, 0
        "Function_1_6F3",          # 01, 1
        "Function_2_6F4",          # 02, 2
        "Function_3_D12",          # 03, 3
        "Function_4_DEF",          # 04, 4
        "Function_5_F25",          # 05, 5
        "Function_6_110F",         # 06, 6
    ))


    def Function_0_6C8(): pass

    label("Function_0_6C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6EA")
    Sound(154, 0, 100, 0)
    Sleep(900)
    Jump("loc_6ED")

    label("loc_6EA")

    Sleep(30)

    label("loc_6ED")

    Jump("Function_0_6C8")

    label("loc_6F2")

    Return()

    # Function_0_6C8 end

    def Function_1_6F3(): pass

    label("Function_1_6F3")

    Return()

    # Function_1_6F3 end

    def Function_2_6F4(): pass

    label("Function_2_6F4")

    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 4)), scpexpr(EXPR_END)), "loc_768")
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lgt1a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    Jump("loc_7C5")

    label("loc_768")

    SetMapObjFrame(0xFF, "lgt1_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lgt1a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x1, 0x1)

    label("loc_7C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 5)), scpexpr(EXPR_END)), "loc_830")
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lgt2a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari12_add", 0x0, 0x1)
    Jump("loc_88D")

    label("loc_830")

    SetMapObjFrame(0xFF, "lgt2_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lgt2a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari11_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari12_add", 0x1, 0x1)

    label("loc_88D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A5")
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_8D7")

    label("loc_8A5")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D7")
    SetScenarioFlags(0x0, 0)

    label("loc_8D7")

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
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0A")
    OP_70(0x0, 0x0)
    Jump("loc_D0E")

    label("loc_D0A")

    OP_70(0x0, 0x1E)

    label("loc_D0E")

    Call(0, 3)
    Return()

    # Function_2_6F4 end

    def Function_3_D12(): pass

    label("Function_3_D12")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D38")
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    Jump("loc_D42")

    label("loc_D38")

    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)

    label("loc_D42")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D75")
    SetChrFlags(0xB, 0x8)
    Jump("loc_D7A")

    label("loc_D75")

    ClearChrFlags(0xB, 0x8)

    label("loc_D7A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB8")
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_DC8")

    label("loc_DB8")

    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearMapObjFlags(0x0, 0x4)

    label("loc_DC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE9")
    SetChrFlags(0xE, 0x8)
    Jump("loc_DEE")

    label("loc_DE9")

    ClearChrFlags(0xE, 0x8)

    label("loc_DEE")

    Return()

    # Function_3_D12 end

    def Function_4_DEF(): pass

    label("Function_4_DEF")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDC")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('痊愈之药', 1)"), scpexpr(EXPR_END)), "loc_E6E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x112, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_ED7")

    label("loc_E6E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_ED7")

    Jump("loc_F19")

    label("loc_EDC")

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

    label("loc_F19")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_DEF end

    def Function_5_F25(): pass

    label("Function_5_F25")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 4)), scpexpr(EXPR_END)), "loc_F62")
    TalkBegin(0xFF)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开关已经被关闭了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_110E")

    label("loc_F62")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1107")
    Fade(500)
    SetChrPos(0x0, -37760, 0, 54500, 89)
    SetChrPos(0x1, -39200, 30, 55000, 89)
    SetChrPos(0x2, -39200, 30, 54000, 89)
    SetChrPos(0x3, -40530, 30, 54500, 89)
    OP_68(-36470, 500, 54740, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-36220, 1000, 59940, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0xD4, 4)
    Fade(500)
    Sound(161, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1098")
    ClearScenarioFlags(0x0, 0)

    label("loc_1098")

    SetMapObjFrame(0xFF, "lgt1a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1101")
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_1107")

    label("loc_1101")

    ClearMapObjFlags(0x1, 0x10)

    label("loc_1107")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_110E")

    Return()

    # Function_5_F25 end

    def Function_6_110F(): pass

    label("Function_6_110F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 5)), scpexpr(EXPR_END)), "loc_114C")
    TalkBegin(0xFF)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开关已经被关闭了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_12F8")

    label("loc_114C")

    EventBegin(0x1)

    #A0007
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F1")
    Fade(500)
    SetChrPos(0x0, -54440, 0, 71670, 0)
    SetChrPos(0x1, -53660, 0, 70000, 0)
    SetChrPos(0x2, -55590, 0, 70000, 0)
    SetChrPos(0x3, -54990, 0, 68710, 0)
    OP_68(-54500, 500, 71550, 0)
    MoveCamera(45, 44, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-36220, 1000, 59940, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0xD4, 5)
    Fade(500)
    Sound(161, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1282")
    ClearScenarioFlags(0x0, 0)

    label("loc_1282")

    SetMapObjFrame(0xFF, "lgt2a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari12_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12EB")
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_12F1")

    label("loc_12EB")

    ClearMapObjFlags(0x1, 0x10)

    label("loc_12F1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_12F8")

    Return()

    # Function_6_110F end

    SaveToFile()

Try(main)
