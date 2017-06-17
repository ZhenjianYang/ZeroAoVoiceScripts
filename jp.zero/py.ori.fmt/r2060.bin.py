from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2060.bin",                # FileName
        "r2060",                    # MapName
        "r2060",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2060", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 0, 0, 1],
    )

    BuildStringList((
        "r2060",                  # 0
        "ツァイト",               # 1
        "br2060",                 # 2
        "br2060",                 # 3
        "br2060",                 # 4
        "br2060",                 # 5
        "クロスベル市方面",       # 6
        "鉱山町マインツ方面",     # 7
    ))

    ATBonus("ATBonus_374", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2EB5", 0,   9,   3,   1,   5,   5,   0)
    Sepith("Sepith_2EDD", 0,   0,   0,   6,   6,   6,   6)
    Sepith("Sepith_2E9D", 0,   10,  3,   0,   2,   0,   5)
    Sepith("Sepith_2ED5", 14,  4,   9,   5,   7,   12,  9)

    MonsterBattlePostion("MonsterBattlePostion_3D4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_438", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_43C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_440", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_444", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_448", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_44C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 2, 13, 180)

    # monster count: 14

    BattleInfo(
        "BattleInfo_5E4", 0x0000, 14, 6, 45, 10, 1, 50, 0, "br2060", "Sepith_2EB5", 30, 40, 20, 10,
        (
            ("ms64400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
        )
    )

    BattleInfo(
        "BattleInfo_454", 0x0000, 14, 6, 45, 10, 1, 30, 0, "br2060", "Sepith_2EDD", 30, 40, 20, 10,
        (
            ("ms71700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms71700.dat", "ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
        )
    )

    BattleInfo(
        "BattleInfo_51C", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2060", "Sepith_2E9D", 30, 40, 20, 10,
        (
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
        )
    )

    BattleInfo(
        "BattleInfo_6AC", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br2060", "Sepith_2ED5", 40, 35, 25, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
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
        "monster/ch71750.itc",               # 10
        "monster/ch71751.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch64450.itc",               # 14
        "monster/ch64450.itc",               # 15
        "monster/ch76050.itc",               # 16
        "monster/ch76051.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(690,     27940,   0,       0x1010000,    "BattleInfo_5E4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-39910,  61380,   0,       0x1010000,    "BattleInfo_5E4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-42170,  79460,   0,       0x1010000,    "BattleInfo_5E4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(350,     141340,  0,       0x1010000,    "BattleInfo_454", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(5600,    124460,  0,       0x1010000,    "BattleInfo_5E4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(23790,   135160,  0,       0x1010000,    "BattleInfo_51C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-23150,  170010,  7400,    0x1010000,    "BattleInfo_5E4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(15210,   144180,  6000,    0x1010000,    "BattleInfo_5E4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(12090,   156500,  10000,   0x1010000,    "BattleInfo_454", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-39940,  194050,  8000,    0x1010000,    "BattleInfo_454", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-13710,  39330,   0,       0x1010000,    "BattleInfo_6AC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-32470,  88800,   0,       0x1010000,    "BattleInfo_6AC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-20640,  138730,  0,       0x1010000,    "BattleInfo_6AC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(14120,   125230,  0,       0x1010000,    "BattleInfo_6AC", 0,   22,  0xFFFF, 6,  7)

    DeclActor(18120,   10000,   151900,  1200,    18120,   11000,   151900,  0x007C, 0,  2,  0x0000)
    DeclActor(-20040,  8000,    199730,  1200,    -20040,  9500,    199730,  0x007C, 0,  12, 0x0000)
    DeclActor(-44060,  0,       71300,   1200,    -44060,  0,       71300,   0x007C, 0,  3,  0x0000)

    PlaceName(-3.0, 0.0, -15.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(87.0, 6.0, 122.0, 0x0000, 0x0000, "鉱山町マインツ方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_7DC",          # 00, 0
        "Function_1_A74",          # 01, 1
        "Function_2_DED",          # 02, 2
        "Function_3_F3A",          # 03, 3
        "Function_4_F4E",          # 04, 4
        "Function_5_F71",          # 05, 5
        "Function_6_2B7C",         # 06, 6
        "Function_7_2C27",         # 07, 7
        "Function_8_2C57",         # 08, 8
        "Function_9_2C73",         # 09, 9
        "Function_10_2CDE",        # 0A, 10
        "Function_11_2DFE",        # 0B, 11
        "Function_12_2E28",        # 0C, 12
    ))


    def Function_0_7DC(): pass

    label("Function_0_7DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F2")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_7F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A70")
    ClearScenarioFlags(0x7A, 0)
    ClearScenarioFlags(0x7A, 1)
    ClearScenarioFlags(0x7A, 2)
    ClearScenarioFlags(0x7A, 3)
    ClearScenarioFlags(0x7A, 4)
    ClearScenarioFlags(0x7A, 5)
    ClearScenarioFlags(0x7A, 6)
    ClearScenarioFlags(0x7A, 7)
    ClearScenarioFlags(0x7B, 0)
    ClearScenarioFlags(0x7B, 1)
    ClearScenarioFlags(0x7B, 2)
    ClearScenarioFlags(0x7B, 3)
    ClearScenarioFlags(0x7B, 4)
    ClearScenarioFlags(0x7B, 5)
    ClearScenarioFlags(0x7B, 6)
    ClearScenarioFlags(0x7B, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84F")
    SetScenarioFlags(0x7A, 0)

    label("loc_84F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_865")
    SetScenarioFlags(0x7A, 1)

    label("loc_865")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87B")
    SetScenarioFlags(0x7A, 2)

    label("loc_87B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_891")
    SetScenarioFlags(0x7A, 3)

    label("loc_891")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A7")
    SetScenarioFlags(0x7A, 4)

    label("loc_8A7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BD")
    SetScenarioFlags(0x7A, 5)

    label("loc_8BD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D3")
    SetScenarioFlags(0x7A, 6)

    label("loc_8D3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E9")
    SetScenarioFlags(0x7A, 7)

    label("loc_8E9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FF")
    SetScenarioFlags(0x7B, 0)

    label("loc_8FF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_915")
    SetScenarioFlags(0x7B, 1)

    label("loc_915")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92B")
    SetScenarioFlags(0x7B, 2)

    label("loc_92B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_941")
    SetScenarioFlags(0x7B, 3)

    label("loc_941")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_957")
    SetScenarioFlags(0x7B, 4)

    label("loc_957")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96D")
    SetScenarioFlags(0x7B, 5)

    label("loc_96D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_983")
    SetScenarioFlags(0x7B, 6)

    label("loc_983")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_999")
    SetScenarioFlags(0x7B, 7)

    label("loc_999")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D4")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_A70")

    label("loc_9D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EB")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_A70")

    label("loc_9EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A02")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_A70")

    label("loc_A02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A19")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_A70")

    label("loc_A19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A30")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_A70")

    label("loc_A30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A47")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_A70")

    label("loc_A47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5E")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_A70")

    label("loc_A5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A70")
    SetScenarioFlags(0x7C, 7)

    label("loc_A70")

    Call(0, 4)
    Return()

    # Function_0_7DC end

    def Function_1_A74(): pass

    label("Function_1_A74")

    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D78")
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)

    label("loc_D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8B")
    OP_70(0x0, 0x0)
    Jump("loc_D8F")

    label("loc_D8B")

    OP_70(0x0, 0x1E)

    label("loc_D8F")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 3)), scpexpr(EXPR_END)), "loc_DEC")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -44060, 0, 71300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_DEC")

    Return()

    # Function_1_A74 end

    def Function_2_DED(): pass

    label("Function_2_DED")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE9")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_E72")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_EE4")

    label("loc_E72")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EE4")

    Jump("loc_F2E")

    label("loc_EE9")

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

    label("loc_F2E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_DED end

    def Function_3_F3A(): pass

    label("Function_3_F3A")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_3_F3A end

    def Function_4_F4E(): pass

    label("Function_4_F4E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F70")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_F70")

    Return()

    # Function_4_F4E end

    def Function_5_F71(): pass

    label("Function_5_F71")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch02600.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00051.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00351.itc", 0x22)
    LoadChrToIndex("chr/ch02651.itc", 0x23)
    LoadChrToIndex("chr/ch02602.itc", 0x24)
    OP_68(340, 1000, 3460, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23550, 0)
    SetChrPos(0x101, -60, 0, 2870, 0)
    SetChrPos(0x102, 1300, 0, 2029, 0)
    SetChrPos(0x103, -630, 0, 1060, 0)
    SetChrPos(0x104, 220, 0, 180, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01200.itp")
    FadeToBright(1000, 0)
    OP_68(-60, 1000, 6310, 4000)

    def lambda_1065():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1065)

    def lambda_107A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_107A)

    def lambda_108F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_108F)

    def lambda_10A4():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10A4)
    Sleep(3000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_0D()
    Fade(1000)
    OP_68(1500, 900, 17380, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24640, 0)
    OP_68(1680, 900, 20780, 3000)
    SetChrPos(0x101, -650, 0, 12520, 0)
    SetChrPos(0x102, 830, 0, 10910, 0)
    SetChrPos(0x103, -720, 0, 10890, 0)
    SetChrPos(0x104, 830, 0, 12550, 0)

    def lambda_1155():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1155)

    def lambda_116F():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_116F)

    def lambda_1189():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1189)

    def lambda_11A3():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11A3)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 11)
    SetChrPos(0x8, 7000, 3900, 32000, 180)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x101,
        "#0007F#11Pあっ……！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        "#0101Fいた……！\x02",
    )

    CloseMessageWindow()
    OP_68(6950, 4600, 31420, 2000)
    SetCameraDistance(18070, 2000)
    OP_6F(0x11)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("白い狼")
    #Sound(2055, 255, 90, 0)    #voice#Zeit

    #A0006
    AnonymousTalk(
        0xFF,
        "……グルルル…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    EndChrThread(0x8, 0x0)
    ClearChrFlags(0x8, 0x20)
    BeginChrThread(0x8, 3, 0, 6)
    Sleep(650)
    Fade(1000)
    OP_68(-360, 600, 25160, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)

    def lambda_13C1():
        OP_95(0xFE, -1720, 0, 23100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13C1)

    def lambda_13DB():
        OP_95(0xFE, 260, 0, 21430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13DB)

    def lambda_13F5():
        OP_95(0xFE, -1490, 0, 21240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13F5)

    def lambda_140F():
        OP_95(0xFE, 70, 0, 23420, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_140F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 3)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0007
    ChrTalk(
        0x101,
        "#0013F#12Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0101F#11P白い毛並み……\x01",
            "《神狼》の伝承の通りね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#0304F#11Pへっ……\x01",
            "ようやく現れたかよ！\x02\x03",

            "#0307Fここで会ったが百年目だ！\x01",
            "とっとと成敗して──\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0205F#12P……待ってください。\x02\x03",

            "その子……\x01",
            "敵意を発していません。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1594():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1594)

    def lambda_15A1():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15A1)
    Sleep(50)

    def lambda_15B1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15B1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0011
    ChrTalk(
        0x104,
        "#0305F#5Pへっ……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x103,
        (
            "#0201F#12P……ここは\x01",
            "わたしに任せてください。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1614():

        label("loc_1614")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_1614")

    QueueWorkItem2(0x101, 1, lambda_1614)

    def lambda_1626():

        label("loc_1626")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_1626")

    QueueWorkItem2(0x102, 1, lambda_1626)

    def lambda_1638():

        label("loc_1638")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_1638")

    QueueWorkItem2(0x104, 1, lambda_1638)
    OP_68(-480, 600, 26430, 4000)
    BeginChrThread(0x103, 3, 0, 7)
    Sleep(500)

    #C0013
    ChrTalk(
        0x101,
        "#0007F#5Pお、おい……！？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        "#0307F#11P馬鹿、何やってやがる！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)
    OP_6F(0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    #C0015
    ChrTalk(
        0x103,
        "#0204F#5P大丈夫……平気です。\x02",
    )

    CloseMessageWindow()

    #N0016
    NpcTalk(
        0x8,
        "白い狼",
        "#5412F#5P#30W……………………………………\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#0204F#12P……やっと会えましたね。\x02\x03",

            "#0202Fわたしたちに会いに\x01",
            "来てくれたみたいですが……\x02\x03",

            "何か伝えたい事でも\x01",
            "あるんですか……？\x02",
        )
    )

    CloseMessageWindow()
    #Sound(2053, 255, 90, 0)    #voice#Zeit

    #N0018
    NpcTalk(
        0x8,
        "白い狼",
        "#5412F#5P#30Wウルゥ……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        "#0203F#12P……そう……やっぱり。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        "#0105Fティ、ティオちゃん！？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#0005F#12P言葉が──分かるのか！？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#0204F#12P言ってることが何となく、\x01",
            "分かるという程度ですが……\x02\x03",

            "#0201Fそれで……何を伝えたいの？\x02",
        )
    )

    CloseMessageWindow()

    #N0023
    NpcTalk(
        0x8,
        "白い狼",
        (
            "#5412F#5P#30Wグルルルル……ウルゥ……\x02\x03",

            "………グルルルルゥ…………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0024
    ChrTalk(
        0x103,
        "#0205F#12Pえ……それって……\x02",
    )

    CloseMessageWindow()

    def lambda_1924():

        label("loc_1924")

        TurnDirection(0x101, 0x8, 500)
        Yield()
        Jump("loc_1924")

    QueueWorkItem2(0x101, 1, lambda_1924)

    def lambda_1936():

        label("loc_1936")

        TurnDirection(0x102, 0x8, 500)
        Yield()
        Jump("loc_1936")

    QueueWorkItem2(0x102, 1, lambda_1936)

    def lambda_1948():

        label("loc_1948")

        TurnDirection(0x103, 0x8, 500)
        Yield()
        Jump("loc_1948")

    QueueWorkItem2(0x103, 1, lambda_1948)

    def lambda_195A():

        label("loc_195A")

        TurnDirection(0x104, 0x8, 500)
        Yield()
        Jump("loc_195A")

    QueueWorkItem2(0x104, 1, lambda_195A)
    EndChrThread(0x8, 0x0)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 8)
    WaitChrThread(0x8, 3)
    Sound(2060, 255, 100, 0)    #voice#Zeit
    Sleep(1700)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)
    Sleep(800)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x8, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    BeginChrThread(0x8, 3, 0, 10)
    Fade(500)
    OP_68(-4830, 5800, 20720, 0)
    MoveCamera(54, 10, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21420, 0)
    OP_68(-4830, 12100, 20720, 5000)

    #C0025
    ChrTalk(
        0x102,
        "#0105F#5P#10Aあっ……！\x02",
    )
    #Auto

    Sleep(2000)

    #C0026
    ChrTalk(
        0x101,
        "#0011F#5P#12Aしまった……！\x02",
    )
    #Auto

    Sleep(2400)

    #C0027
    ChrTalk(
        0x104,
        (
            "#0307F#5P#14Aちっ……\x01",
            "あんな所を行くのかよ！？\x02",
        )
    )
    #Auto

    Sleep(2800)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    OP_5A()
    Fade(1000)
    OP_68(-480, 600, 26430, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    OP_68(390, 600, 25160, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0028
    ChrTalk(
        0x103,
        "#0205F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()

    def lambda_1B90():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B90)

    def lambda_1B9D():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B9D)
    Sleep(50)

    def lambda_1BAD():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BAD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    #C0029
    ChrTalk(
        0x101,
        (
            "#0001F#12Pティオ……\x01",
            "“彼”は何を言ってたんだ？\x02\x03",

            "たしかに俺たちに\x01",
            "何か伝えたいみたいだったけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0030
    ChrTalk(
        0x103,
        (
            "#0206F#5Pその……\x01",
            "ニュアンスだけを伝えると。\x02\x03",

            "#0201F『最後の欠片はこの先に』……\x02\x03",

            "『後はお前たち次第だ』……\x02\x03",

            "──だそうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x101,
        "#0005F#12P最後の欠片……！？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        (
            "#0203F#5Pええ……\x01",
            "そんなニュアンスでした。\x02\x03",

            "#0200F信じるも信じないも\x01",
            "ロイドさんたち次第ですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#0006F#12Pああ、そういう事を\x01",
            "言ってるんじゃないって。\x02\x03",

            "#0008F『最後の欠片はこの先に』……\x02\x03",

            "#0001Fつまり一連の魔獣被害で\x01",
            "不足していた最後の情報が\x01",
            "揃うって意味じゃないか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x102, 0x101, 500)
    Sleep(500)

    #C0034
    ChrTalk(
        0x102,
        (
            "#0105F#11Pちょ、ちょっと待って。\x02\x03",

            "#0101Fティオちゃんが聞いた言葉が\x01",
            "本当だったとしても……\x02\x03",

            "あの狼の言ってることを\x01",
            "そのまま信じてもいいの？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0035
    ChrTalk(
        0x104,
        (
            "#0301F#11Pああ……\x01",
            "各地を襲っていた張本人だ。\x02\x03",

            "そんな知能があるかどうかともかく\x01",
            "ダマしてる可能性はねぇのかよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0036
    ChrTalk(
        0x101,
        (
            "#0003F#6Pいや……\x02\x03",

            "#0000Fどうやらさっきの狼は\x01",
            "各地を襲っていた狼型魔獣とは\x01",
            "別物の可能性が高そうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x102,
        "#0105F#11Pえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        (
            "#0305F#11Pおいおい……\x01",
            "どうしてそうなるんだよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#0000F#6Pああ、それは……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K別物である根拠は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【遠吠え】\x01",        # 0
            "【色と外見】\x01",      # 1
            "【その両方】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2117"),
        (1, "loc_227E"),
        (2, "loc_23ED"),
        (SWITCH_DEFAULT, "loc_250D"),
    )


    label("loc_2117")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0041
    ChrTalk(
        0x101,
        (
            "#0000F#6P村と病院での調査によれば……\x02\x03",

            "襲撃された夜、遠吠えのようなものが\x01",
            "聞こえたという証言はなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0101F#11Pそ、そういえば……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#0203F#5Pそれに、病院の屋上で襲われた\x01",
            "研修医のリットンさんによれば……\x02\x03",

            "#0201F襲ってきたのは、真っ黒な姿の\x01",
            "狼みたいな魔獣だったそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0301F#11Pなるほど……\x01",
            "色が全然違うってわけか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_227E")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x101,
        (
            "#0000F#6P病院の屋上で襲われた\x01",
            "研修医のリットンさんによれば……\x02\x03",

            "襲ってきたのは、真っ黒な姿の\x01",
            "狼みたいな魔獣だったそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0101F#11Pそ、そういえば……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        (
            "#0203F#5Pそれに、村と病院での調査によれば……\x02\x03",

            "#0201F襲撃された夜、先ほどのような遠吠えが\x01",
            "聞こえたという証言はありませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0301F#11Pなるほど……\x01",
            "そいつはちょっと妙だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_23ED")

    OP_2C(0x3F, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0049
    ChrTalk(
        0x101,
        (
            "#0003F#6P村と病院での調査では、\x01",
            "さっきみたいな遠吠えが\x01",
            "聞こえたという証言はなかった。\x02\x03",

            "#0000Fそれに、研修医のリットンさんの話では\x01",
            "襲ってきたのは真っ黒な姿の\x01",
            "狼みたいな魔獣だったそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#0101F#11Pそ、そういえば……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        "#0301F#11P確かに結構、違いがあるな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_250D")


    #C0052
    ChrTalk(
        0x101,
        (
            "#0006F#6Pまあ、だからといって\x01",
            "さっきの魔獣が犯人じゃないと\x01",
            "断定までは出来ないけどね。\x02\x03",

            "#0001Fあいつがボスで、\x01",
            "手下の黒い狼にやらせていた\x01",
            "可能性だってあるわけだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        (
            "#0208F#5P群れで行動している以上、\x01",
            "その可能性もあるわけですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        (
            "#0103F#11Pでも、本当に違うのなら\x01",
            "考えを改める必要がありそうね。\x02\x03",

            "#0101F……狼型魔獣は２種類いて、\x01",
            "それぞれ別々に動いているって。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0004F#6Pああ、そういうことだ。\x02\x03",

            "#0001Fそのうち、さっきの彼も含めた\x01",
            "白い狼が伝承にある《神狼》で……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#0303F#11P未だ尻尾を出してない黒いヤツが\x01",
            "各地で悪さをしてた連中ってわけか。\x02\x03",

            "#0302Fなるほど……辻褄#4Rつじつま#は合うな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#0204F#5Pはい……\x01",
            "わたしもそんな感じがします。\x02\x03",

            "#0202Fさっきの子……少なくとも\x01",
            "悪意は感じられませんでした。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0058
    ChrTalk(
        0x101,
        "#0000F#12Pああ……俺もそう思うよ。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#0103F#11P『最後の欠片はこの先に』……\x02\x03",

            "#0101Fこの先というのは、\x01",
            "やっぱり鉱山町のことかしら？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2876():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2876)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0060
    ChrTalk(
        0x101,
        (
            "#0004F#6Pああ、間違いないだろう。\x02\x03",

            "#0000F近くまで来たことだし……\x01",
            "予定通りこのまま訪ねてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#0104F#11Pええ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        (
            "#0306F#11Pしかし……\x01",
            "『後はお前たち次第だ』ねぇ。\x02\x03",

            "#0301Fどうでもいいけど、\x01",
            "やたらと偉そうな物言いだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        (
            "#0203F#5Pそうですね……\x02\x03",

            "#0200F何というか、少しばかり\x01",
            "ナメられていたとは思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0064
    ChrTalk(
        0x101,
        (
            "#0006F#12Pま、まあそれはともかく……\x02\x03",

            "#0001F最後まで気を抜かずに\x01",
            "調査した方が良さそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        (
            "#0101F#11Pええ、何とか手がかりを\x01",
            "見つけられるといいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_37()
    OP_68(-800, 600, 22500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, -800, 0, 22500, 0)
    SetChrPos(0x1, -800, 0, 22500, 0)
    SetChrPos(0x2, -800, 0, 22500, 0)
    SetChrPos(0x3, -800, 0, 22500, 0)
    SetScenarioFlags(0x65, 0)
    OP_29(0x40, 0x1, 0x6)
    OP_E0(0x0)
    Call(0, 4)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_5_F71 end

    def Function_6_2B7C(): pass

    label("Function_6_2B7C")

    OP_93(0x8, 0xE1, 0x12C)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x1)

    def lambda_2BA0():
        OP_9D(0xFE, 0xFFFFFA10, 0x0, 0x6E5A, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2BA0)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x1)
    Sound(820, 0, 100, 0)
    Sound(832, 0, 100, 0)
    Sound(38, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    BeginChrThread(0x8, 0, 0, 11)
    Return()

    # Function_6_2B7C end

    def Function_7_2C27(): pass

    label("Function_7_2C27")

    OP_95(0xFE, -3510, 0, 23390, 2000, 0x0)
    OP_95(0xFE, -980, 0, 25900, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_7_2C27 end

    def Function_8_2C57(): pass

    label("Function_8_2C57")

    OP_97(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_8_2C57 end

    def Function_9_2C73(): pass

    label("Function_9_2C73")

    OP_93(0x8, 0x2D, 0x1F4)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x1)

    def lambda_2C97():
        OP_9D(0xFE, 0x1194, 0xF3C, 0x84D0, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C97)
    Sound(814, 0, 100, 0)
    Sound(38, 0, 100, 0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_9_2C73 end

    def Function_10_2CDE(): pass

    label("Function_10_2CDE")

    OP_95(0xFE, 8000, 3900, 30000, 6000, 0x0)
    ClearChrFlags(0x8, 0x1)

    def lambda_2CFC():
        OP_9D(0xFE, 0x3C8C, 0x1EDC, 0x61A8, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2CFC)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x1)
    Sound(39, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    OP_95(0xFE, 18180, 8000, 23720, 6000, 0x0)
    OP_93(0x8, 0x0, 0x0)
    ClearChrFlags(0x8, 0x1)

    def lambda_2D67():
        OP_9D(0xFE, 0x45D8, 0x2EE0, 0x7602, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2D67)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x1)
    Sound(39, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x1)

    def lambda_2DB7():
        OP_9D(0xFE, 0x4132, 0x3EE4, 0x95B0, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2DB7)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x1)
    Sound(39, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_10_2CDE end

    def Function_11_2DFE(): pass

    label("Function_11_2DFE")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E27")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_2E09")

    label("loc_2E27")

    Return()

    # Function_11_2DFE end

    def Function_12_2E28(): pass

    label("Function_12_2E28")

    TalkBegin(0xFF)
    SetChrName("")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旧鉱山のようだ。\x01",
            "扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_12_2E28 end

    SaveToFile()

Try(main)
