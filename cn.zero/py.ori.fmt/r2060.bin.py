from ZeroScenarioHelper import *

def main():
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
        "蔡特",                   # 1
        "br2060",                 # 2
        "br2060",                 # 3
        "br2060",                 # 4
        "br2060",                 # 5
        "克洛斯贝尔市方向",       # 6
        "矿山镇玛因兹方向",       # 7
    ))

    ATBonus("ATBonus_374", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2BEA", 0,   9,   3,   1,   5,   5,   0)
    Sepith("Sepith_2C12", 0,   0,   0,   6,   6,   6,   6)
    Sepith("Sepith_2BD2", 0,   10,  3,   0,   2,   0,   5)
    Sepith("Sepith_2C0A", 14,  4,   9,   5,   7,   12,  9)

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
        "BattleInfo_5E4", 0x0000, 14, 6, 45, 10, 1, 50, 0, "br2060", "Sepith_2BEA", 30, 40, 20, 10,
        (
            ("ms64400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
        )
    )

    BattleInfo(
        "BattleInfo_454", 0x0000, 14, 6, 45, 10, 1, 30, 0, "br2060", "Sepith_2C12", 30, 40, 20, 10,
        (
            ("ms71700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms71700.dat", "ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
        )
    )

    BattleInfo(
        "BattleInfo_51C", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2060", "Sepith_2BD2", 30, 40, 20, 10,
        (
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_434", "ed7400", "ed7403", "ATBonus_374"),
        )
    )

    BattleInfo(
        "BattleInfo_6AC", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br2060", "Sepith_2C0A", 40, 35, 25, 0,
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

    PlaceName(-3.0, 0.0, -15.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(87.0, 6.0, 122.0, 0x0000, 0x0000, "矿山镇玛因兹方向")

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
        "Function_3_F23",          # 03, 3
        "Function_4_F37",          # 04, 4
        "Function_5_F5A",          # 05, 5
        "Function_6_28BF",         # 06, 6
        "Function_7_296A",         # 07, 7
        "Function_8_299A",         # 08, 8
        "Function_9_29B6",         # 09, 9
        "Function_10_2A21",        # 0A, 10
        "Function_11_2B41",        # 0B, 11
        "Function_12_2B6B",        # 0C, 12
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDA")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('复苏药', 1)"), scpexpr(EXPR_END)), "loc_E6C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_ED5")

    label("loc_E6C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_ED5")

    Jump("loc_F17")

    label("loc_EDA")

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

    label("loc_F17")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_DED end

    def Function_3_F23(): pass

    label("Function_3_F23")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_3_F23 end

    def Function_4_F37(): pass

    label("Function_4_F37")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F59")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_F59")

    Return()

    # Function_4_F37 end

    def Function_5_F5A(): pass

    label("Function_5_F5A")

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

    def lambda_104E():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_104E)

    def lambda_1063():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1063)

    def lambda_1078():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1078)

    def lambda_108D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_108D)
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

    def lambda_113E():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_113E)

    def lambda_1158():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1158)

    def lambda_1172():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1172)

    def lambda_118C():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_118C)
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
        "#0007F#11P啊……！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        "#0101F有了……！\x02",
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
    SetChrName("白狼")
    #Sound(2055, 255, 90, 0)    #voice#Zeit

    #A0006
    AnonymousTalk(
        0xFF,
        "……呜噜噜噜…………\x02",
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

    def lambda_13A6():
        OP_95(0xFE, -1720, 0, 23100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13A6)

    def lambda_13C0():
        OP_95(0xFE, 260, 0, 21430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13C0)

    def lambda_13DA():
        OP_95(0xFE, -1490, 0, 21240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13DA)

    def lambda_13F4():
        OP_95(0xFE, 70, 0, 23420, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13F4)
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
        "#0013F#12P呜……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0101F#11P白色鬃毛……\x01",
            "与『神狼』传说中描述的一样呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#0304F#11P嘿……\x01",
            "终于现身了啊！\x02\x03",

            "#0307F在这里被我们撞到，就是你的末日了！\x01",
            "快点接受制裁──\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0205F#12P……请等一下。\x02\x03",

            "这孩子……\x01",
            "并没有散发出敌意。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_156F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_156F)

    def lambda_157C():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_157C)
    Sleep(50)

    def lambda_158C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_158C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0011
    ChrTalk(
        0x104,
        "#0305F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x103,
        (
            "#0201F#12P……这里\x01",
            "就交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15DF():

        label("loc_15DF")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_15DF")

    QueueWorkItem2(0x101, 1, lambda_15DF)

    def lambda_15F1():

        label("loc_15F1")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_15F1")

    QueueWorkItem2(0x102, 1, lambda_15F1)

    def lambda_1603():

        label("loc_1603")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_1603")

    QueueWorkItem2(0x104, 1, lambda_1603)
    OP_68(-480, 600, 26430, 4000)
    BeginChrThread(0x103, 3, 0, 7)
    Sleep(500)

    #C0013
    ChrTalk(
        0x101,
        "#0007F#5P喂、喂……！？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        "#0307F#11P笨蛋，你要做什么！？\x02",
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
        "#0204F#5P不要紧……没关系的。\x02",
    )

    CloseMessageWindow()

    #N0016
    NpcTalk(
        0x8,
        "白狼",
        "#5412F#5P#30W……………………………………\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#0204F#12P……终于见面了呢。\x02\x03",

            "#0202F你似乎\x01",
            "是来见我们的……\x02\x03",

            "是有什么事\x01",
            "想告诉我们吗……？\x02",
        )
    )

    CloseMessageWindow()
    #Sound(2053, 255, 90, 0)    #voice#Zeit

    #N0018
    NpcTalk(
        0x8,
        "白狼",
        "#5412F#5P#30W呜噜……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        "#0203F#12P……是吗……果然。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        "#0105F缇、缇欧！？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#0005F#12P它的话──你听得懂吗！？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#0204F#12P只是大致能明白\x01",
            "它想表达什么的程度吧……\x02\x03",

            "#0201F那么……你要告诉我们什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0023
    NpcTalk(
        0x8,
        "白狼",
        (
            "#5412F#5P#30W呜噜噜噜噜……呜噜……\x02\x03",

            "………呜噜噜噜噜呜…………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0024
    ChrTalk(
        0x103,
        "#0205F#12P哎……这个……\x02",
    )

    CloseMessageWindow()

    def lambda_189F():

        label("loc_189F")

        TurnDirection(0x101, 0x8, 500)
        Yield()
        Jump("loc_189F")

    QueueWorkItem2(0x101, 1, lambda_189F)

    def lambda_18B1():

        label("loc_18B1")

        TurnDirection(0x102, 0x8, 500)
        Yield()
        Jump("loc_18B1")

    QueueWorkItem2(0x102, 1, lambda_18B1)

    def lambda_18C3():

        label("loc_18C3")

        TurnDirection(0x103, 0x8, 500)
        Yield()
        Jump("loc_18C3")

    QueueWorkItem2(0x103, 1, lambda_18C3)

    def lambda_18D5():

        label("loc_18D5")

        TurnDirection(0x104, 0x8, 500)
        Yield()
        Jump("loc_18D5")

    QueueWorkItem2(0x104, 1, lambda_18D5)
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
        "#0105F#5P#10A啊……！\x02",
    )
    #Auto

    Sleep(2000)

    #C0026
    ChrTalk(
        0x101,
        "#0011F#5P#12A糟了……！\x02",
    )
    #Auto

    Sleep(2400)

    #C0027
    ChrTalk(
        0x104,
        (
            "#0307F#5P#14A嘁……\x01",
            "竟然跑到那种地方去了！？\x02",
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

    def lambda_1B03():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B03)

    def lambda_1B10():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B10)
    Sleep(50)

    def lambda_1B20():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B20)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    #C0029
    ChrTalk(
        0x101,
        (
            "#0001F#12P缇欧……\x01",
            "『它』说了什么？\x02\x03",

            "看上去，似乎\x01",
            "想告诉我们什么啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0030
    ChrTalk(
        0x103,
        (
            "#0206F#5P那个……\x01",
            "从语气上来判断，应该是……\x02\x03",

            "#0201F『最后的碎片就在这前方』……\x02\x03",

            "『之后就看你们的了』……\x02\x03",

            "──好像是这样。\x02",
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
        "#0005F#12P最后的碎片……！？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        (
            "#0203F#5P嗯……\x01",
            "大概就是这种感觉。\x02\x03",

            "#0200F要不要相信，\x01",
            "就由大家来决定了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#0006F#12P啊，我不是\x01",
            "这个意思。\x02\x03",

            "#0008F『最后的碎片就在这前方』……\x02\x03",

            "#0001F也就是说，在对于魔兽灾害的调查中\x01",
            "所欠缺的最后情报就要凑齐了，\x01",
            "是这个意思吗……？\x02",
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
            "#0105F#11P等、等一下。\x02\x03",

            "#0101F就算缇欧\x01",
            "真的听懂了它的意思……\x02\x03",

            "但是，那只狼所说的话，\x01",
            "我们可以就这么相信吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0035
    ChrTalk(
        0x104,
        (
            "#0301F#11P嗯……\x01",
            "毕竟是袭击了各地的罪魁祸首啊。\x02\x03",

            "先不说它是否有这种智慧，\x01",
            "即使有，也可能只是在欺骗我们吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0036
    ChrTalk(
        0x101,
        (
            "#0003F#6P不……\x02\x03",

            "#0000F看样子，刚才那只狼\x01",
            "与袭击各地的狼形魔兽\x01",
            "很可能是两回事。\x02",
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
        "#0105F#11P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        (
            "#0305F#11P喂喂……\x01",
            "这是怎么回事啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#0000F#6P嗯，因为……\x02",
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
            "#1K两者不同的根据是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【远吠】\x01",            # 0
            "【毛色和外形】\x01",      # 1
            "【以上两者】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1FFC"),
        (1, "loc_211F"),
        (2, "loc_2256"),
        (SWITCH_DEFAULT, "loc_2350"),
    )


    label("loc_1FFC")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0041
    ChrTalk(
        0x101,
        (
            "#0000F#6P根据在村子和医院里的调查……\x02\x03",

            "遇袭的夜晚，并没有证言表示\x01",
            "有人听到了远吠。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0101F#11P这、这么一说……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#0203F#5P而且，据在医院楼顶上\x01",
            "遇袭的实习医生利顿先生所说……\x02\x03",

            "#0201F袭击他的似乎是纯黑色的\x01",
            "狼形魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0301F#11P原来如此……\x01",
            "颜色完全不同吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2350")

    label("loc_211F")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x101,
        (
            "#0000F#6P据在医院楼顶上\x01",
            "遇袭的实习医生利顿先生所说……\x02\x03",

            "袭击他的似乎是纯黑色的\x01",
            "狼形魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0101F#11P这、这么一说，的确……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        (
            "#0203F#5P而且，根据在村子和医院里的调查……\x02\x03",

            "#0201F遇袭的夜晚，并没有证言表示\x01",
            "有人听到了像刚才那样的远吠。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0301F#11P原来如此……\x01",
            "这点确实有点奇怪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2350")

    label("loc_2256")

    OP_2C(0x3F, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0049
    ChrTalk(
        0x101,
        (
            "#0003F#6P根据在村子和医院里的调查，\x01",
            "并没有证言表示\x01",
            "有人听到了像刚才那样的远吠。\x02\x03",

            "#0000F而且，据实习医生利顿先生所说，\x01",
            "袭击他的似乎是纯黑色的\x01",
            "狼形魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#0101F#11P这、这么一说，的确……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        "#0301F#11P的确有很大区别啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2350")

    label("loc_2350")


    #C0052
    ChrTalk(
        0x101,
        (
            "#0006F#6P当然，也不能\x01",
            "就因此而断定刚才的魔兽\x01",
            "绝不是犯人。\x02\x03",

            "#0001F那家伙也有可能是首领，\x01",
            "让手下的黑狼们\x01",
            "下手行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        (
            "#0208F#5P既然是群体行动，\x01",
            "便也有这种可能呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        (
            "#0103F#11P可是，如果真的不同，\x01",
            "似乎就需要改变想法了。\x02\x03",

            "#0101F……狼形魔兽有两种，\x01",
            "各自分别行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0004F#6P嗯，就是这样。\x02\x03",

            "#0001F其中，包括刚才那个家伙在内的\x01",
            "白狼是传说中的『神狼』……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#0303F#11P而至今还没出现的黑狼\x01",
            "就是在各地作恶的家伙吗？\x02\x03",

            "#0302F原来如此……合情合理啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#0204F#5P是的……\x01",
            "我也有这种感觉。\x02\x03",

            "#0202F从刚才的孩子身上……至少\x01",
            "感觉不到有任何恶意。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0058
    ChrTalk(
        0x101,
        "#0000F#12P嗯……我也这么想。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#0103F#11P『最后的碎片就在这前方』……\x02\x03",

            "#0101F所谓这前方，\x01",
            "应该就是指矿山镇吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_25FD():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25FD)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0060
    ChrTalk(
        0x101,
        (
            "#0004F#6P嗯，应该没错。\x02\x03",

            "#0000F反正已经到附近了……\x01",
            "就按照原定计划，前去拜访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#0104F#11P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        (
            "#0306F#11P话说回来……\x01",
            "『之后就看你们的了』……\x02\x03",

            "#0301F虽然无所谓，\x01",
            "不过它的说话口气还真是高高在上啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        (
            "#0203F#5P是呀……\x02\x03",

            "#0200F该怎么说呢，\x01",
            "我们好像有点被它小看了呢。\x02",
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
            "#0006F#12P这、这个就先放一边吧……\x02\x03",

            "#0001F看样子，我们的调查工作\x01",
            "直到最后也都不能掉以轻心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        (
            "#0101F#11P嗯，希望能\x01",
            "找到什么线索……\x02",
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

    # Function_5_F5A end

    def Function_6_28BF(): pass

    label("Function_6_28BF")

    OP_93(0x8, 0xE1, 0x12C)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x1)

    def lambda_28E3():
        OP_9D(0xFE, 0xFFFFFA10, 0x0, 0x6E5A, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_28E3)
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

    # Function_6_28BF end

    def Function_7_296A(): pass

    label("Function_7_296A")

    OP_95(0xFE, -3510, 0, 23390, 2000, 0x0)
    OP_95(0xFE, -980, 0, 25900, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_7_296A end

    def Function_8_299A(): pass

    label("Function_8_299A")

    OP_97(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_8_299A end

    def Function_9_29B6(): pass

    label("Function_9_29B6")

    OP_93(0x8, 0x2D, 0x1F4)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x1)

    def lambda_29DA():
        OP_9D(0xFE, 0x1194, 0xF3C, 0x84D0, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29DA)
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

    # Function_9_29B6 end

    def Function_10_2A21(): pass

    label("Function_10_2A21")

    OP_95(0xFE, 8000, 3900, 30000, 6000, 0x0)
    ClearChrFlags(0x8, 0x1)

    def lambda_2A3F():
        OP_9D(0xFE, 0x3C8C, 0x1EDC, 0x61A8, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A3F)
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

    def lambda_2AAA():
        OP_9D(0xFE, 0x45D8, 0x2EE0, 0x7602, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2AAA)
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

    def lambda_2AFA():
        OP_9D(0xFE, 0x4132, 0x3EE4, 0x95B0, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2AFA)
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

    # Function_10_2A21 end

    def Function_11_2B41(): pass

    label("Function_11_2B41")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B4C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B6A")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_2B4C")

    label("loc_2B6A")

    Return()

    # Function_11_2B41 end

    def Function_12_2B6B(): pass

    label("Function_12_2B6B")

    TalkBegin(0xFF)
    SetChrName("")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎是旧矿山。\x01",
            "门紧紧关着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_12_2B6B end

    SaveToFile()

Try(main)
