from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m0001.bin",                # FileName
        "m0001",                    # MapName
        "m0001",                    # Location
        0x0067,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 103, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0001",                  # 0
        "亨利",                   # 1
        "bm0001",                 # 2
        "bm0001",                 # 3
        "bm0001",                 # 4
        "bm0001",                 # 5
        "bm0000",                 # 6
        "bm0000",                 # 7
        "bm0000",                 # 8
        "bm0000",                 # 9
    ))

    ATBonus("ATBonus_320", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_3486", 1,   2,   0,   4,   1,   1,   0)
    Sepith("Sepith_347E", 3,   1,   2,   0,   1,   2,   1)
    Sepith("Sepith_348E", 1,   4,   0,   2,   0,   2,   1)
    Sepith("Sepith_3496", 2,   0,   3,   2,   1,   0,   2)

    MonsterBattlePostion("MonsterBattlePostion_3C0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_404", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_40C", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_410", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_414", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_418", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_360", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 2, 13, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_490", 0x0000, 3, 6, 45, 10, 1, 30, 0, "bm0001", "Sepith_3486", 75, 25, 0, 0,
        (
            ("ms60300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_400", "ed7400", "ed7403", "ATBonus_320"),
            ("ms60300.dat", "ms60300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3A0", "MonsterBattlePostion_400", "ed7400", "ed7403", "ATBonus_320"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5B4", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0000", "Sepith_347E", 75, 25, 0, 0,
        (
            ("ms60100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            ("ms60100.dat", "ms60100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_360", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_694", 0x0000, 3, 6, 45, 10, 1, 25, 0, "bm0000", "Sepith_348E", 100, 0, 0, 0,
        (
            ("ms73100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_544", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0001", "Sepith_3496", 75, 25, 0, 0,
        (
            ("ms61700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_400", "ed7400", "ed7403", "ATBonus_320"),
            ("ms61700.dat", "ms61700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3A0", "MonsterBattlePostion_400", "ed7400", "ed7403", "ATBonus_320"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6D8", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0000", "Sepith_3496", 75, 25, 0, 0,
        (
            ("ms61700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            ("ms61700.dat", "ms61700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3A0", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_624", 0x0000, 3, 6, 45, 10, 1, 30, 0, "bm0000", "Sepith_3486", 75, 25, 0, 0,
        (
            ("ms60300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            ("ms60300.dat", "ms60300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_360", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch22200.itc",                   # 00
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
        "monster/ch60150.itc",               # 10
        "monster/ch60151.itc",               # 11
        "monster/ch60350.itc",               # 12
        "monster/ch60351.itc",               # 13
        "monster/ch73150.itc",               # 14
        "monster/ch73151.itc",               # 15
        "monster/ch61750.itc",               # 16
        "monster/ch61750.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(40,      97290,   0,       0x1010000,    "BattleInfo_490", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(6830,    199320,  12000,   0x1010000,    "BattleInfo_5B4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-7490,   199510,  12000,   0x1010000,    "BattleInfo_694", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(98790,   -400,    0,       0x1010000,    "BattleInfo_544", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(199650,  -460,    100,     0x1010000,    "BattleInfo_6D8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(2370,    202390,  -2000,   0x1010000,    "BattleInfo_624", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-4410,   195610,  -2000,   0x1010000,    "BattleInfo_6D8", 0,   22,  0xFFFF, 6,  7)

    DeclActor(14000,   0,       502000,  1200,    14000,   1000,    502500,  0x007C, 0,  8,  0x0000)
    DeclActor(2000,    0,       0,       1200,    2500,    1000,    0,       0x007C, 0,  10, 0x0000)
    DeclActor(0,       0,       522000,  1200,    0,       1000,    522500,  0x007C, 0,  12, 0x0000)
    DeclActor(3230,    0,       309620,  1200,    3230,    1500,    309620,  0x007C, 0,  7,  0x0000)
    DeclActor(6870,    12000,   206910,  1200,    6870,    13000,   206910,  0x007C, 0,  3,  0x0000)
    DeclActor(198210,  3800,    193730,  1200,    198210,  4800,    193730,  0x007C, 0,  4,  0x0000)
    DeclActor(202520,  0,       5210,    1200,    202520,  1000,    5210,    0x007C, 0,  5,  0x0000)
    DeclActor(0,       -2000,   192500,  1200,    0,       -1000,   192500,  0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3])                         # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_7F0",          # 00, 0
        "Function_1_890",          # 01, 1
        "Function_2_CC4",          # 02, 2
        "Function_3_DB0",          # 03, 3
        "Function_4_F05",          # 04, 4
        "Function_5_103B",         # 05, 5
        "Function_6_1171",         # 06, 6
        "Function_7_1222",         # 07, 7
        "Function_8_1315",         # 08, 8
        "Function_9_1497",         # 09, 9
        "Function_10_15DE",        # 0A, 10
        "Function_11_1760",        # 0B, 11
        "Function_12_18A7",        # 0C, 12
        "Function_13_1AA4",        # 0D, 13
        "Function_14_1BEB",        # 0E, 14
        "Function_15_1F9C",        # 0F, 15
        "Function_16_3176",        # 10, 16
        "Function_17_33EF",        # 11, 17
    ))


    def Function_0_7F0(): pass

    label("Function_0_7F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_856")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81D")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)
    Jump("loc_856")

    label("loc_81D")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83C")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_856")

    label("loc_83C")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_856")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)

    label("loc_856")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x81), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_875")
    Event(0, 15)
    Jump("loc_88F")

    label("loc_875")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88F")
    Event(0, 14)

    label("loc_88F")

    Return()

    # Function_0_7F0 end

    def Function_1_890(): pass

    label("Function_1_890")

    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0xD, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x3, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x3, "light01", 0x0, 0x1)
    SetMapObjFrame(0x4, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x4, "light01", 0x0, 0x1)
    SetMapObjFrame(0x5, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x5, "light01", 0x0, 0x1)
    SetMapObjFrame(0x6, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x6, "light01", 0x0, 0x1)
    SetMapObjFrame(0x7, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x7, "light01", 0x0, 0x1)
    SetMapObjFrame(0x8, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x8, "light01", 0x0, 0x1)
    SetMapObjFrame(0x9, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x9, "light01", 0x0, 0x1)
    SetMapObjFrame(0xA, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xA, "light01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3C")
    SetMapObjFrame(0xD, "up", 0x0, 0x1)
    SetMapObjFrame(0xD, "down", 0x0, 0x1)
    SetMapObjFrame(0xD, "gauge", 0x0, 0x1)

    label("loc_A3C")

    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5F")
    OP_70(0xF, 0x0)
    Jump("loc_C63")

    label("loc_C5F")

    OP_70(0xF, 0x1E)

    label("loc_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C76")
    OP_70(0x10, 0x0)
    Jump("loc_C7A")

    label("loc_C76")

    OP_70(0x10, 0x1E)

    label("loc_C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8D")
    OP_70(0x11, 0x0)
    Jump("loc_C91")

    label("loc_C8D")

    OP_70(0x11, 0x1E)

    label("loc_C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA4")
    OP_70(0x12, 0x0)
    Jump("loc_CA8")

    label("loc_CA4")

    OP_70(0x12, 0x1E)

    label("loc_CA8")

    OP_1B(0xA, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC0")
    OP_1B(0xA, 0x0, 0x11)

    label("loc_CC0")

    Call(0, 2)
    Return()

    # Function_1_890 end

    def Function_2_CC4(): pass

    label("Function_2_CC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE5")
    SetChrFlags(0xC, 0x8)
    Jump("loc_CEA")

    label("loc_CE5")

    ClearChrFlags(0xC, 0x8)

    label("loc_CEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D11")
    SetChrFlags(0xD, 0x8)
    SetMapObjFlags(0x11, 0x4)
    Jump("loc_D1C")

    label("loc_D11")

    ClearChrFlags(0xD, 0x8)
    ClearMapObjFlags(0x11, 0x4)

    label("loc_D1C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D50")
    SetMapObjFlags(0x10, 0x4)
    Jump("loc_D56")

    label("loc_D50")

    ClearMapObjFlags(0x10, 0x4)

    label("loc_D56")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D95")
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetMapObjFlags(0xF, 0x4)
    Jump("loc_DAF")

    label("loc_D95")

    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearMapObjFlags(0xF, 0x4)

    label("loc_DAF")

    Return()

    # Function_2_CC4 end

    def Function_3_DB0(): pass

    label("Function_3_DB0")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED6")
    Sound(14, 0, 100, 0)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xF, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 20)
    AddSepith(0x1, 20)
    AddSepith(0x2, 20)
    AddSepith(0x3, 20)
    AddSepith(0x4, 20)
    AddSepith(0x5, 20)
    AddSepith(0x6, 20)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２０\x01\x07\x02",

            "#57I水之耀晶片×２０\x01\x07\x02",

            "#58I火之耀晶片×２０\x01\x07\x02",

            "#59I风之耀晶片×２０\x01\x07\x02",

            "#60I时之耀晶片×２０\x01\x07\x02",

            "#61I空之耀晶片×２０\x01\x07\x02",

            "#62I幻之耀晶片×２０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_EF3")

    label("loc_ED6")


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

    label("loc_EF3")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_DB0 end

    def Function_4_F05(): pass

    label("Function_4_F05")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF2")
    Sound(14, 0, 100, 0)
    OP_71(0x10, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('打火机', 1)"), scpexpr(EXPR_END)), "loc_F84")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10A, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_FED")

    label("loc_F84")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x10, 0x1E, 0x0, 0x0, 0x0)

    label("loc_FED")

    Jump("loc_102F")

    label("loc_FF2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
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

    label("loc_102F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_F05 end

    def Function_5_103B(): pass

    label("Function_5_103B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1128")
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('回复药', 1)"), scpexpr(EXPR_END)), "loc_10BA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10A, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1123")

    label("loc_10BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x11, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1123")

    Jump("loc_1165")

    label("loc_1128")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
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

    label("loc_1165")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_103B end

    def Function_6_1171(): pass

    label("Function_6_1171")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F3")
    Sound(14, 0, 100, 0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x12, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddItemNumber('战斗探测器', 5)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#14I战斗探测器×５\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1210")

    label("loc_11F3")


    #A0010
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

    label("loc_1210")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1171 end

    def Function_7_1222(): pass

    label("Function_7_1222")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0011
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F7")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0xE, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0xE, 0x0)
    OP_71(0xE, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xE)
    OP_71(0xE, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0xE, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_12F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1313")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1313")

    Return()

    # Function_7_1222 end

    def Function_8_1315(): pass

    label("Function_8_1315")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以操作升降机的控制面板。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148F")
    Fade(500)
    SetChrPos(0x0, 13400, 0, 500600, 0)
    SetChrPos(0x1, 14600, 0, 500600, 0)
    SetChrPos(0x2, 13400, 0, 499400, 0)
    SetChrPos(0x3, 14600, 0, 499400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13EF")
    SetChrPos(0x4, 13400, 0, 498200, 0)
    SetChrPos(0x5, 14600, 0, 498200, 0)
    Jump("loc_140E")

    label("loc_13EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140E")
    SetChrPos(0x4, 14000, 0, 498200, 0)

    label("loc_140E")

    OP_68(14000, 1000, 500000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(14000, 6000, 500000, 3000)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0000", 0, 0, 0)
    IdleLoop()

    label("loc_148F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1315 end

    def Function_9_1497(): pass

    label("Function_9_1497")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(14000, 11000, 500000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 13400, 30000, 500600, 0)
    OP_90(0x1, 14600, 30000, 500600, 0)
    OP_90(0x2, 13400, 30000, 499400, 0)
    OP_90(0x3, 14600, 30000, 499400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156A")
    OP_90(0x4, 13400, 30000, 498200, 0)
    OP_90(0x5, 14600, 30000, 498200, 0)
    Jump("loc_1589")

    label("loc_156A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1589")
    OP_90(0x4, 14000, 30000, 498200, 0)

    label("loc_1589")

    Sound(145, 0, 100, 0)
    OP_68(14000, 1000, 500000, 3000)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xB)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1497 end

    def Function_10_15DE(): pass

    label("Function_10_15DE")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以操作升降机的控制面板。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1758")
    Fade(500)
    SetChrPos(0x0, 600, 0, -600, 90)
    SetChrPos(0x1, 600, 0, 600, 90)
    SetChrPos(0x2, -600, 0, -600, 90)
    SetChrPos(0x3, -600, 0, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B8")
    SetChrPos(0x4, -1800, 0, -600, 90)
    SetChrPos(0x5, -1800, 0, 600, 90)
    Jump("loc_16D7")

    label("loc_16B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D7")
    SetChrPos(0x4, -1800, 0, 0, 90)

    label("loc_16D7")

    OP_68(600, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(600, 6000, 0, 3000)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0000", 0, 0, 0)
    IdleLoop()

    label("loc_1758")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_15DE end

    def Function_11_1760(): pass

    label("Function_11_1760")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, -600, 90)
    OP_90(0x1, 600, 30000, 600, 90)
    OP_90(0x2, -600, 30000, -600, 90)
    OP_90(0x3, -600, 30000, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1833")
    OP_90(0x4, -1800, 30000, -600, 90)
    OP_90(0x5, -1800, 30000, 600, 90)
    Jump("loc_1852")

    label("loc_1833")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1852")
    OP_90(0x4, -1800, 30000, 0, 90)

    label("loc_1852")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 0, 3000)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xC)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_1760 end

    def Function_12_18A7(): pass

    label("Function_12_18A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18BD")
    Call(0, 16)
    Jump("loc_1AA3")

    label("loc_18BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_END)), "loc_1A4E")
    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以操作升降机的控制面板。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A42")
    Fade(500)
    SetChrPos(0x0, -600, 0, 520600, 0)
    SetChrPos(0x1, 600, 0, 520600, 0)
    SetChrPos(0x2, -600, 0, 519400, 0)
    SetChrPos(0x3, 600, 0, 519400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A0")
    SetChrPos(0x4, -600, 0, 518200, 0)
    SetChrPos(0x5, 600, 0, 518200, 0)
    Jump("loc_19BF")

    label("loc_19A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19BF")
    SetChrPos(0x4, 0, 0, 518200, 0)

    label("loc_19BF")

    OP_68(0, 0, 520000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(0, -5000, 520000, 2000)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0010", 0, 0, 0)
    IdleLoop()

    label("loc_1A42")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_1AA3")

    label("loc_1A4E")

    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "升降机好像被锁定了，\x01",
            "按下按钮也毫无反应。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9B")
    SetScenarioFlags(0x53, 3)

    label("loc_1A9B")

    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)

    label("loc_1AA3")

    Return()

    # Function_12_18A7 end

    def Function_13_1AA4(): pass

    label("Function_13_1AA4")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(0, -5000, 520000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, -600, -10000, 520600, 0)
    OP_90(0x1, 600, -10000, 520600, 0)
    OP_90(0x2, -600, -10000, 519400, 0)
    OP_90(0x3, 600, -10000, 519400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B79")
    OP_90(0x4, -600, -10000, 518200, 0)
    OP_90(0x5, 600, -10000, 518200, 0)
    Jump("loc_1B98")

    label("loc_1B79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B98")
    OP_90(0x4, 0, -10000, 518200, 0)

    label("loc_1B98")

    Sound(145, 0, 100, 0)
    OP_68(0, 0, 520000, 3000)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "up")
    FadeToBright(1000, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xD)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_1AA4 end

    def Function_14_1BEB(): pass

    label("Function_14_1BEB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(200000, 900, 191200, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 199400, 0, 190000, 0)
    SetChrPos(0x102, 200600, 0, 190000, 0)
    SetChrPos(0x103, 199400, 0, 190000, 0)
    SetChrPos(0x104, 200600, 0, 190000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(200000, 900, 193200, 3000)

    def lambda_1CB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CB6)

    def lambda_1CC7():
        OP_95(0xFE, 199400, 0, 193200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CC7)
    Sleep(300)

    def lambda_1CE4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CE4)

    def lambda_1CF5():
        OP_95(0xFE, 200600, 0, 193200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CF5)
    Sleep(1000)

    def lambda_1D12():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1D12)

    def lambda_1D23():
        OP_95(0xFE, 199400, 0, 192000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D23)
    Sleep(300)

    def lambda_1D40():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1D40)

    def lambda_1D51():
        OP_95(0xFE, 200600, 0, 192000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D51)
    WaitChrThread(0x101, 1)
    SetMessageWindowPos(16, 16, -1, -1)
    SetChrName("声音")

    #A0016
    AnonymousTalk(
        0xFF,
        "#2S……呜……呜……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
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
    Sleep(1000)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0017
    ChrTalk(
        0x101,
        "#12P#0001F这声音是……！？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#0105F#11P是、是孩子的哭声……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)
    Sleep(300)

    #C0019
    ChrTalk(
        0x104,
        (
            "#11P#0306F喂喂，这是怎么回事？\x02\x03",

            "#0301F不是说地下空间的内部\x01",
            "被封锁了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(300)

    #C0020
    ChrTalk(
        0x103,
        (
            "#6P#0206F#6P……问我也没用啊。\x02\x03",

            "#0200F那应该只是\x01",
            "官方的对外措辞吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F0D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F0D)
    Sleep(100)
    TurnDirection(0x102, 0x103, 500)

    #C0021
    ChrTalk(
        0x101,
        (
            "#6P#0001F以后再说这些吧！\x02\x03",

            "总之，赶快去找到那个\x01",
            "哭泣的孩子吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        "#5P#0101F嗯……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 200000, 0, 192200, 0)
    SetScenarioFlags(0x40, 6)
    OP_29(0x3C, 0x1, 0x2)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_14_1BEB end

    def Function_15_1F9C(): pass

    label("Function_15_1F9C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(201300, 5500, 399300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 210700, 4500, 399300, 90)
    OP_A7(0x8, 0x0, 0x0, 0x0, 0xFF, 0x0)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x104, 0x40)
    SetChrPos(0x101, 199800, 4500, 399000, 90)
    SetChrPos(0x102, 199500, 4500, 399800, 90)
    SetChrPos(0x103, 198400, 4500, 399000, 90)
    SetChrPos(0x104, 197800, 4500, 399800, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #N0023
    NpcTalk(
        0x8,
        "男孩",
        "#3P呜……呜……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_20C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_20C5)
    OP_68(210700, 5500, 399300, 3000)
    SetCameraDistance(24000, 3000)
    OP_6F(0x11)

    #N0024
    NpcTalk(
        0x8,
        "男孩",
        (
            "……怎么办啊……\x01",
            "这样下去的话……呜……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#0007F喂，有人在吗！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xC8, 0xBB8)
    Sleep(500)
    OP_93(0x8, 0x10E, 0x1F4)

    #N0026
    NpcTalk(
        0x8,
        "男孩",
        "#11P！！！\x02",
    )

    CloseMessageWindow()

    #N0027
    NpcTalk(
        0x8,
        "男孩",
        "#11P是、是谁～！？\x02",
    )

    CloseMessageWindow()
    OP_68(209000, 5500, 399300, 2000)

    def lambda_21BA():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21BA)
    Sleep(50)

    def lambda_21D7():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_21D7)
    Sleep(50)

    def lambda_21F4():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21F4)
    Sleep(50)

    def lambda_2211():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2211)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0028
    ChrTalk(
        0x101,
        (
            "#6P#0006F太好了，\x01",
            "原来在这里吗。\x02\x03",

            "#0001F你还好吗？\x01",
            "有没有受伤？\x02",
        )
    )

    CloseMessageWindow()

    #N0029
    NpcTalk(
        0x8,
        "男孩",
        "#11P呜呜呜呜呜……\x02",
    )

    CloseMessageWindow()

    def lambda_229F():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_229F)
    OP_82(0x0, 0x64, 0xBB8, 0x3E8)

    #N0030
    NpcTalk(
        0x8,
        "男孩",
        "#11P#4S呜哇哇哇哇哇哇……！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#6P#0011F哇哇……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        "#3P#0305F哎呀呀……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#0106F一看到我们，\x01",
            "就安心地哭出来了吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0034
    ChrTalk(
        0x102,
        "#0100F#5P罗伊德，交给我吧。\x02",
    )

    CloseMessageWindow()

    def lambda_2377():

        label("loc_2377")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2377")

    QueueWorkItem2(0x101, 2, lambda_2377)
    Sleep(100)

    #C0035
    ChrTalk(
        0x101,
        "#12P#0005F啊，好的……\x02",
    )

    CloseMessageWindow()
    OP_68(209710, 5500, 399580, 1500)

    def lambda_23B9():
        OP_95(0xFE, 210300, 4500, 399700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23B9)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x2)

    def lambda_23DB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23DB)
    TurnDirection(0x102, 0x8, 500)

    #C0036
    ChrTalk(
        0x102,
        (
            "#5P#0104F……好了好了，很害怕吧。\x02\x03",

            "现在已经没事啦……\x01",
            "有哥哥姐姐们陪着你哦。\x02",
        )
    )

    CloseMessageWindow()

    #N0037
    NpcTalk(
        0x8,
        "男孩",
        "呜……呜……\x02",
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x8,
        "男孩",
        "……嗯、嗯……！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#5P#0102F哥哥姐姐们已经把\x01",
            "外面那些可怕的魔兽消灭了哦。\x02\x03",

            "这里狭窄阴暗，\x01",
            "还是先离开吧。\x02\x03",

            "来，我抱着你，\x01",
            "抓稳了哦。\x02",
        )
    )

    CloseMessageWindow()

    #N0040
    NpcTalk(
        0x8,
        "男孩",
        "没、没关系……\x02",
    )

    CloseMessageWindow()

    #N0041
    NpcTalk(
        0x8,
        "男孩",
        "我……可以站起来！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    #C0042
    ChrTalk(
        0x102,
        (
            "#5P#0109F是吗……\x01",
            "呵呵，真是个男子汉呢。\x02\x03",

            "#0102F你叫什么名字呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0043
    NpcTalk(
        0x8,
        "男孩",
        (
            "那个……\x01",
            "我叫亨利！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#6P#0012F（嗯……）\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        "#3P#0302F（哈哈，大小姐真厉害呢。）\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(198000, 900, 202000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x8, 198000, 0, 203200, 180)
    SetChrPos(0x101, 199700, 0, 201300, 315)
    SetChrPos(0x102, 198000, 0, 201200, 0)
    SetChrPos(0x103, 197400, 0, 199800, 0)
    SetChrPos(0x104, 198700, 0, 199600, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    SetCameraDistance(21000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0046
    ChrTalk(
        0x102,
        (
            "#12P#0100F──那么，亨利。\x01",
            "你怎么会在这种地方？\x02\x03",

            "这里的入口应该被上了锁，\x01",
            "你从哪里进来的？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "#5P呃，那个……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#5P我们在中央广场的\x01",
            "大钟附近玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#5P然后，打开了那里的盖子，\x01",
            "发现有个梯子……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        "#5P所、所以就……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27ED")

    #C0051
    ChrTalk(
        0x104,
        (
            "#4P#0300F原来如此，\x01",
            "是冒险心在作祟啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        (
            "#12P#0205F那种地方竟然有入口……\x02\x03",

            "#0203F看来有必要\x01",
            "添加到资料库中呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2867")

    label("loc_27ED")


    #C0053
    ChrTalk(
        0x104,
        (
            "#4P#0300F原来如此，是从那个\x01",
            "地下道出入口进来的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        (
            "#12P#0203F……看来有必要\x01",
            "把那个入口的信息\x01",
            "添加到资料库中呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2867")


    #C0055
    ChrTalk(
        0x101,
        (
            "#11P#0001F等、等一下！\x02\x03",

            "你说『我们』……\x01",
            "还有其他孩子也进来了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0056
    ChrTalk(
        0x102,
        "#6P#0105F啊……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0057
    ChrTalk(
        0x8,
        "#5P是、是的……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#5P一起来这里探险，其实是\x01",
            "我朋友隆的提议……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#5P但、但是……\x01",
            "路上遇到了可怕的魔兽，\x01",
            "我们就逃散了……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        "#5P呜呜呜……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#12P#0103F是这样啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0062
    ChrTalk(
        0x102,
        "#6P#0101F──罗伊德，该怎么办呢？\x02",
    )

    CloseMessageWindow()

    def lambda_2A08():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A08)
    Sleep(50)

    def lambda_2A18():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2A18)
    Sleep(50)

    def lambda_2A28():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2A28)
    WaitChrThread(0x104, 2)

    #C0063
    ChrTalk(
        0x101,
        "#11P#0003F这样啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【先带着男孩回去】\x01",                # 0
            "【带着男孩一起找另一个孩子】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2AB8"),
        (1, "loc_2CF8"),
        (SWITCH_DEFAULT, "loc_2EDE"),
    )


    label("loc_2AB8")


    #C0064
    ChrTalk(
        0x101,
        (
            "#11P#0008F先带着孩子\x01",
            "返回到入口比较好吧……\x02\x03",

            "#0001F毕竟不能把他留在这里，\x01",
            "而且，带着他去找另一个孩子\x01",
            "也是很危险的。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#6P#0200F……但是，这样合适吗？\x02\x03",

            "在带他回去的这段时间里，\x01",
            "如果另一个孩子遭遇不测的话……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B94():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B94)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0066
    ChrTalk(
        0x101,
        (
            "#5P#0005F也对……\x02\x03",

            "#0008F但是，在这里分头行动\x01",
            "应该也并非良策。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#4P#0306F嗯，大家目前\x01",
            "对彼此的能力还不太了解，\x01",
            "最好不要贸然分散行动。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    #C0068
    ChrTalk(
        0x102,
        (
            "#6P#0103F……没时间了，\x01",
            "快点带着亨利行动吧。\x02\x03",

            "#0101F如果发生战斗的话，\x01",
            "我是不会让魔兽接近这孩子的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0069
    ChrTalk(
        0x101,
        "#11P#0003F我知道了……走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EDE")

    label("loc_2CF8")

    OP_2C(0x3C, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0070
    ChrTalk(
        0x101,
        (
            "#11P#0003F──没时间了，\x01",
            "带着这孩子往深处走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0071
    ChrTalk(
        0x103,
        (
            "#6P#0205F……这样没关系吗？\x01",
            "不用先带着这孩子离开吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        (
            "#4P#0301F而且，我们也可以兵分两路，\x01",
            "分头进行搜索吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0073
    ChrTalk(
        0x101,
        (
            "#5P#0001F眼下的状况可谓分秒必争，\x01",
            "贸然分散战斗力\x01",
            "恐怕并非良策吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0074
    ChrTalk(
        0x101,
        (
            "#11P#0001F……艾莉。\x01",
            "这孩子就交给你保护了，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#6P#0104F嗯，交给我吧。\x02\x03",

            "#0100F如果发生战斗的话，\x01",
            "我是不会让魔兽接近这孩子的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EDE")

    label("loc_2EDE")

    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0076
    ChrTalk(
        0x101,
        (
            "#11P#0000F──亨利。\x01",
            "接下来，哥哥姐姐们\x01",
            "就要去找你的朋友了。\x02\x03",

            "这附近很危险，\x01",
            "所以希望你跟着我们一起行动。\x02\x03",

            "……可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        "#5P嗯……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "#5P我很担心隆，\x01",
            "我也一起去……！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#11P#0002F嗯，真是好孩子。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0080
    ChrTalk(
        0x101,
        (
            "#5P#0003F要在保护孩子安全的同时，仔细进行搜索。\x02\x03",

            "#0001F从现在开始，\x01",
            "更加慎重地前进吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        "#6P#0100F嗯……！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        "#6P#0204F……明白。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#4P#0300F那么，赶快去找\x01",
            "另一个淘气小鬼吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "亨利作为保护对象\x01",
            "加入到了队伍中。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※保护对象一旦陷入无法战斗的状态，\x01",
            "  游戏就将结束。\x01",
            "  在努力保护他的同时，小心前进吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrFlags(0x8, 0x80)
    AddParty(0x96, 0xFF, 0xFF)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x104, 0x40)
    OP_49()
    OP_37()
    SetChrPos(0x0, 198000, 0, 201000, 0)
    SetScenarioFlags(0x40, 7)
    OP_1B(0xA, 0xFF, 0xFFFF)
    OP_29(0x3C, 0x1, 0x3)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_15_1F9C end

    def Function_16_3176(): pass

    label("Function_16_3176")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_68(0, 1000, 521299, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 0, 0, 520100, 0)
    SetChrPos(0x103, 0, 0, 521299, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "升降机好像被锁定了，\x01",
            "按下按钮也毫无反应。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0087
    ChrTalk(
        0x103,
        (
            "#0200F这就是下降到\x01",
            "Ａ区域下层的升降机了。\x02\x03",

            "要输入认证密码。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧打开控制面板，\x01",
            "输入了８个数字。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Fade(500)
    SetMapObjFrame(0xD, "down", 0x1, 0x1)
    SetMapObjFrame(0xD, "gauge", 0x1, 0x1)
    Sound(72, 0, 100, 0)
    OP_0D()
    TurnDirection(0x103, 0x101, 500)

    #C0089
    ChrTalk(
        0x103,
        "#0202F……启动了。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#12P#0004F好，我们下去吧。\x02\x03",

            "#0000F那个终端到底在\x01",
            "下层区域的什么地方呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        (
            "#0203F恐怕是在下层区域的最深处。\x02\x03",

            "#0201F应该还要走很远，\x01",
            "路上小心一点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#12P#0005F啊，好的……\x01",
            "（她之前竟然打算一个人\x01",
            "　前往那种地方吗……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 520000, 0)
    SetScenarioFlags(0xA0, 7)
    OP_29(0x45, 0x1, 0x3)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_16_3176 end

    def Function_17_33EF(): pass

    label("Function_17_33EF")

    EventBegin(0x1)

    #C0093
    ChrTalk(
        0x101,
        (
            "#0001F……刚才听到了孩子的声音呢，不能放着不管。\x02\x03",

            "好像……就在这附近吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 191670, 0, 200070, 90)
    EventEnd(0x4)
    Return()

    # Function_17_33EF end

    SaveToFile()

Try(main)
