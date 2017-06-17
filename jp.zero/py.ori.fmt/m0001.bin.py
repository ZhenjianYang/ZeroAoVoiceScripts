from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "アンリ",                 # 1
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

    Sepith("Sepith_3870", 1,   2,   0,   4,   1,   1,   0)
    Sepith("Sepith_3868", 3,   1,   2,   0,   1,   2,   1)
    Sepith("Sepith_3878", 1,   4,   0,   2,   0,   2,   1)
    Sepith("Sepith_3880", 2,   0,   3,   2,   1,   0,   2)

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
        "BattleInfo_490", 0x0000, 3, 6, 45, 10, 1, 30, 0, "bm0001", "Sepith_3870", 75, 25, 0, 0,
        (
            ("ms60300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_400", "ed7400", "ed7403", "ATBonus_320"),
            ("ms60300.dat", "ms60300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3A0", "MonsterBattlePostion_400", "ed7400", "ed7403", "ATBonus_320"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5B4", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0000", "Sepith_3868", 75, 25, 0, 0,
        (
            ("ms60100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            ("ms60100.dat", "ms60100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_360", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_694", 0x0000, 3, 6, 45, 10, 1, 25, 0, "bm0000", "Sepith_3878", 100, 0, 0, 0,
        (
            ("ms73100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_544", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0001", "Sepith_3880", 75, 25, 0, 0,
        (
            ("ms61700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_400", "ed7400", "ed7403", "ATBonus_320"),
            ("ms61700.dat", "ms61700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3A0", "MonsterBattlePostion_400", "ed7400", "ed7403", "ATBonus_320"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6D8", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0000", "Sepith_3880", 75, 25, 0, 0,
        (
            ("ms61700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            ("ms61700.dat", "ms61700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3A0", "MonsterBattlePostion_3E0", "ed7400", "ed7403", "ATBonus_320"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_624", 0x0000, 3, 6, 45, 10, 1, 30, 0, "bm0000", "Sepith_3870", 75, 25, 0, 0,
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
        "Function_4_F13",          # 04, 4
        "Function_5_1060",         # 05, 5
        "Function_6_11AD",         # 06, 6
        "Function_7_1270",         # 07, 7
        "Function_8_137B",         # 08, 8
        "Function_9_150D",         # 09, 9
        "Function_10_1654",        # 0A, 10
        "Function_11_17E6",        # 0B, 11
        "Function_12_192D",        # 0C, 12
        "Function_13_1B52",        # 0D, 13
        "Function_14_1C99",        # 0E, 14
        "Function_15_2084",        # 0F, 15
        "Function_16_34E6",        # 10, 16
        "Function_17_37D9",        # 11, 17
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDC")
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
            "#56I地のセピス×２０\x01\x07\x02",

            "#57I水のセピス×２０\x01\x07\x02",

            "#58I火のセピス×２０\x01\x07\x02",

            "#59I風のセピス×２０\x01\x07\x02",

            "#60I時のセピス×２０\x01\x07\x02",

            "#61I空のセピス×２０\x01\x07\x02",

            "#62I幻のセピス×２０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_F01")

    label("loc_EDC")


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

    label("loc_F01")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_DB0 end

    def Function_4_F13(): pass

    label("Function_4_F13")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100F")
    Sound(14, 0, 100, 0)
    OP_71(0x10, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x41, 1)"), scpexpr(EXPR_END)), "loc_F98")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10A, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_100A")

    label("loc_F98")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x10, 0x1E, 0x0, 0x0, 0x0)

    label("loc_100A")

    Jump("loc_1054")

    label("loc_100F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
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

    label("loc_1054")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_F13 end

    def Function_5_1060(): pass

    label("Function_5_1060")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115C")
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F4, 1)"), scpexpr(EXPR_END)), "loc_10E5")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10A, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1157")

    label("loc_10E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x11, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1157")

    Jump("loc_11A1")

    label("loc_115C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_11A1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1060 end

    def Function_6_11AD(): pass

    label("Function_6_11AD")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1239")
    Sound(14, 0, 100, 0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x12, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddItemNumber(0x20E, 5)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#14Iバトルスコープ×５\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_125E")

    label("loc_1239")


    #A0010
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

    label("loc_125E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_11AD end

    def Function_7_1270(): pass

    label("Function_7_1270")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0011
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135D")
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

    label("loc_135D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1379")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1379")

    Return()

    # Function_7_1270 end

    def Function_8_137B(): pass

    label("Function_8_137B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの制御パネルがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1505")
    Fade(500)
    SetChrPos(0x0, 13400, 0, 500600, 0)
    SetChrPos(0x1, 14600, 0, 500600, 0)
    SetChrPos(0x2, 13400, 0, 499400, 0)
    SetChrPos(0x3, 14600, 0, 499400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1465")
    SetChrPos(0x4, 13400, 0, 498200, 0)
    SetChrPos(0x5, 14600, 0, 498200, 0)
    Jump("loc_1484")

    label("loc_1465")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1484")
    SetChrPos(0x4, 14000, 0, 498200, 0)

    label("loc_1484")

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

    label("loc_1505")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_137B end

    def Function_9_150D(): pass

    label("Function_9_150D")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E0")
    OP_90(0x4, 13400, 30000, 498200, 0)
    OP_90(0x5, 14600, 30000, 498200, 0)
    Jump("loc_15FF")

    label("loc_15E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FF")
    OP_90(0x4, 14000, 30000, 498200, 0)

    label("loc_15FF")

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

    # Function_9_150D end

    def Function_10_1654(): pass

    label("Function_10_1654")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの制御パネルがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DE")
    Fade(500)
    SetChrPos(0x0, 600, 0, -600, 90)
    SetChrPos(0x1, 600, 0, 600, 90)
    SetChrPos(0x2, -600, 0, -600, 90)
    SetChrPos(0x3, -600, 0, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_173E")
    SetChrPos(0x4, -1800, 0, -600, 90)
    SetChrPos(0x5, -1800, 0, 600, 90)
    Jump("loc_175D")

    label("loc_173E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_175D")
    SetChrPos(0x4, -1800, 0, 0, 90)

    label("loc_175D")

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

    label("loc_17DE")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1654 end

    def Function_11_17E6(): pass

    label("Function_11_17E6")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B9")
    OP_90(0x4, -1800, 30000, -600, 90)
    OP_90(0x5, -1800, 30000, 600, 90)
    Jump("loc_18D8")

    label("loc_18B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18D8")
    OP_90(0x4, -1800, 30000, 0, 90)

    label("loc_18D8")

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

    # Function_11_17E6 end

    def Function_12_192D(): pass

    label("Function_12_192D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1943")
    Call(0, 16)
    Jump("loc_1B51")

    label("loc_1943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_END)), "loc_1AE4")
    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの制御パネルがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD8")
    Fade(500)
    SetChrPos(0x0, -600, 0, 520600, 0)
    SetChrPos(0x1, 600, 0, 520600, 0)
    SetChrPos(0x2, -600, 0, 519400, 0)
    SetChrPos(0x3, 600, 0, 519400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A36")
    SetChrPos(0x4, -600, 0, 518200, 0)
    SetChrPos(0x5, 600, 0, 518200, 0)
    Jump("loc_1A55")

    label("loc_1A36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A55")
    SetChrPos(0x4, 0, 0, 518200, 0)

    label("loc_1A55")

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

    label("loc_1AD8")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_1B51")

    label("loc_1AE4")

    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターはロックされているらしく\x01",
            "ボタンを押しても反応しない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B49")
    SetScenarioFlags(0x53, 3)

    label("loc_1B49")

    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)

    label("loc_1B51")

    Return()

    # Function_12_192D end

    def Function_13_1B52(): pass

    label("Function_13_1B52")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C27")
    OP_90(0x4, -600, -10000, 518200, 0)
    OP_90(0x5, 600, -10000, 518200, 0)
    Jump("loc_1C46")

    label("loc_1C27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C46")
    OP_90(0x4, 0, -10000, 518200, 0)

    label("loc_1C46")

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

    # Function_13_1B52 end

    def Function_14_1C99(): pass

    label("Function_14_1C99")

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

    def lambda_1D64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D64)

    def lambda_1D75():
        OP_95(0xFE, 199400, 0, 193200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D75)
    Sleep(300)

    def lambda_1D92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1D92)

    def lambda_1DA3():
        OP_95(0xFE, 200600, 0, 193200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DA3)
    Sleep(1000)

    def lambda_1DC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1DC0)

    def lambda_1DD1():
        OP_95(0xFE, 199400, 0, 192000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DD1)
    Sleep(300)

    def lambda_1DEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1DEE)

    def lambda_1DFF():
        OP_95(0xFE, 200600, 0, 192000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DFF)
    WaitChrThread(0x101, 1)
    SetMessageWindowPos(16, 16, -1, -1)
    SetChrName("声")

    #A0016
    AnonymousTalk(
        0xFF,
        "#2S……ヒック……ヒック……\x02",
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
        "#12P#0001Fこの声は……！？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#0105F#11Pこ、子供の泣き声……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)
    Sleep(300)

    #C0019
    ChrTalk(
        0x104,
        (
            "#11P#0306Fおいおい、どういう事だよ？\x02\x03",

            "#0301F確かジオフロント内部は\x01",
            "封鎖されてるんじゃないのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(300)

    #C0020
    ChrTalk(
        0x103,
        (
            "#6P#0206F#6P……わたしに言われても。\x02\x03",

            "#0200Fあくまで公式的に\x01",
            "そうなっているだけの話です。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FEF():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FEF)
    Sleep(100)
    TurnDirection(0x102, 0x103, 500)

    #C0021
    ChrTalk(
        0x101,
        (
            "#6P#0001F話は後だ！\x02\x03",

            "とにかく一刻も早く\x01",
            "泣き声の主を探してみよう！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        "#5P#0101Fええ……！\x02",
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

    # Function_14_1C99 end

    def Function_15_2084(): pass

    label("Function_15_2084")

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
        "男の子",
        "#3Pヒック……ううう……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_21B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_21B7)
    OP_68(210700, 5500, 399300, 3000)
    SetCameraDistance(24000, 3000)
    OP_6F(0x11)

    #N0024
    NpcTalk(
        0x8,
        "男の子",
        (
            "……どうしよう……\x01",
            "このままじゃ……ヒック……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#0007Fおーい、誰かいるのか！\x02",
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
        "男の子",
        "#11P！！！\x02",
    )

    CloseMessageWindow()

    #N0027
    NpcTalk(
        0x8,
        "男の子",
        "#11Pだ、だれ～っ！？\x02",
    )

    CloseMessageWindow()
    OP_68(209000, 5500, 399300, 2000)

    def lambda_22C2():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22C2)
    Sleep(50)

    def lambda_22DF():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22DF)
    Sleep(50)

    def lambda_22FC():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22FC)
    Sleep(50)

    def lambda_2319():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2319)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0028
    ChrTalk(
        0x101,
        (
            "#6P#0006Fよかった。\x01",
            "こんな所にいたのか。\x02\x03",

            "#0001F大丈夫かい？\x01",
            "どこかケガしていないか？\x02",
        )
    )

    CloseMessageWindow()

    #N0029
    NpcTalk(
        0x8,
        "男の子",
        "#11Pうううううっ……\x02",
    )

    CloseMessageWindow()

    def lambda_23C1():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_23C1)
    OP_82(0x0, 0x64, 0xBB8, 0x3E8)

    #N0030
    NpcTalk(
        0x8,
        "男の子",
        "#11P#4Sふええええええっ……！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#6P#0011Fわわっ……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        "#3P#0305Fあらら……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#0106F安心したとたん、\x01",
            "気が緩んじゃったのね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0034
    ChrTalk(
        0x102,
        "#0100F#5Pロイド、私が代わるわ。\x02",
    )

    CloseMessageWindow()

    def lambda_24A9():

        label("loc_24A9")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_24A9")

    QueueWorkItem2(0x101, 2, lambda_24A9)
    Sleep(100)

    #C0035
    ChrTalk(
        0x101,
        "#12P#0005Fあ、ああ……\x02",
    )

    CloseMessageWindow()
    OP_68(209710, 5500, 399580, 1500)

    def lambda_24EB():
        OP_95(0xFE, 210300, 4500, 399700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24EB)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x2)

    def lambda_250D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_250D)
    TurnDirection(0x102, 0x8, 500)

    #C0036
    ChrTalk(
        0x102,
        (
            "#5P#0104F……よしよし、恐かったね。\x02\x03",

            "もう大丈夫だから……\x01",
            "お姉さんたちが付いてるからね。\x02",
        )
    )

    CloseMessageWindow()

    #N0037
    NpcTalk(
        0x8,
        "男の子",
        "ううううっ……ヒック……\x02",
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x8,
        "男の子",
        "……う、うんっ……！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#5P#0102F外にいた恐い魔獣は\x01",
            "お姉さんたちが退治したわ。\x02\x03",

            "ここは暗くて狭いから\x01",
            "いったん外に出ましょう。\x02\x03",

            "さ、抱っこしてあげるから\x01",
            "しっかりと掴まっていてね。\x02",
        )
    )

    CloseMessageWindow()

    #N0040
    NpcTalk(
        0x8,
        "男の子",
        "だ、だいじょうぶです……\x02",
    )

    CloseMessageWindow()

    #N0041
    NpcTalk(
        0x8,
        "男の子",
        "ボク……もう立てますから！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    #C0042
    ChrTalk(
        0x102,
        (
            "#5P#0109Fそっか……\x01",
            "ふふっ、男の子だもんね。\x02\x03",

            "#0102F名前はなんていうのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #N0043
    NpcTalk(
        0x8,
        "男の子",
        (
            "えとえと……\x01",
            "アンリっていいます！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#6P#0012F（うーん……）\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        "#3P#0302F（はは、鮮やかなもんだねぇ。）\x02",
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
            "#12P#0100F──それで、アンリ君。\x01",
            "どうしてこんな場所に？\x02\x03",

            "鍵がかかってはずだけど\x01",
            "どこから入ってきたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "#5Pえと、その……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#5Pボクたち、中央広場の\x01",
            "鐘のある場所で遊んでて……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#5Pそこにあった蓋を開いたら\x01",
            "ハシゴがあるのを見つけて……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        "#5Pそ、それで……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F5")

    #C0051
    ChrTalk(
        0x104,
        (
            "#4P#0300Fなるほど、冒険心を\x01",
            "くすぐられちまったわけだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        (
            "#12P#0205Fそんなところにも入口が……\x02\x03",

            "#0203Fデータベースに追記する\x01",
            "必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A87")

    label("loc_29F5")


    #C0053
    ChrTalk(
        0x104,
        (
            "#4P#0300Fなるほど、あのマンホールから\x01",
            "入って来ちまったわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        (
            "#12P#0203F……あの入り口は\x01",
            "データベースに追記する\x01",
            "必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A87")


    #C0055
    ChrTalk(
        0x101,
        (
            "#11P#0001Fちょ、ちょっと待った！\x02\x03",

            "『ボクたち』っていうことは……\x01",
            "他の子も一緒に入ったのか！？\x02",
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
        "#6P#0105Fあ……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0057
    ChrTalk(
        0x8,
        "#5Pは、はい……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#5P友だちのリュウが\x01",
            "一緒に冒険してみようって……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#5Pで、でも……\x01",
            "途中でコワイ魔獣に見つかって\x01",
            "逃げてるうちにはぐれちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        "#5Pうううっ……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#12P#0103Fそうだったの……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0062
    ChrTalk(
        0x102,
        "#6P#0101F──ねえロイド、どうする？\x02",
    )

    CloseMessageWindow()

    def lambda_2C64():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C64)
    Sleep(50)

    def lambda_2C74():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2C74)
    Sleep(50)

    def lambda_2C84():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2C84)
    WaitChrThread(0x104, 2)

    #C0063
    ChrTalk(
        0x101,
        "#11P#0003Fそうだな……\x02",
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
            "【男の子を連れていったん戻る】\x01",            # 0
            "【男の子と一緒にもう一人の子を捜す】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D2A"),
        (1, "loc_2FC2"),
        (SWITCH_DEFAULT, "loc_31D6"),
    )


    label("loc_2D2A")


    #C0064
    ChrTalk(
        0x101,
        (
            "#11P#0008Fいったん、その子を連れて\x01",
            "入口まで戻った方がいいか……\x02\x03",

            "#0001Fここには置いていけないし、\x01",
            "もう一人の子を捜すにしても\x01",
            "一緒に連れて行くのは危険だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#6P#0200F……でも、いいんですか？\x02\x03",

            "送り届けている間にも\x01",
            "もう一人に何かあったら……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E26():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E26)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0066
    ChrTalk(
        0x101,
        (
            "#5P#0005Fそうか……\x02\x03",

            "#0008Fだが、ここで手分けするのも\x01",
            "あまり得策じゃ無さそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#4P#0306Fま、お互いのことを\x01",
            "まだロクに判ってない状態で\x01",
            "戦力分散ってのも無いわな。\x02",
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
            "#6P#0103F……時間がないわ。\x01",
            "アンリ君を連れて行きましょう。\x02\x03",

            "#0101Fもし魔獣と戦闘になっても\x01",
            "私がこの子に近づけないわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0069
    ChrTalk(
        0x101,
        "#11P#0003F分かった……それで行こう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_31D6")

    label("loc_2FC2")

    OP_2C(0x3C, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0070
    ChrTalk(
        0x101,
        (
            "#11P#0003F──時間がない。\x01",
            "この子と一緒に奥まで行こう。\x02",
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
            "#6P#0205F……いいんですか？\x01",
            "その子を先に脱出させなくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        (
            "#4P#0301Fいったん二手に分かれて\x01",
            "捜索を続けるって手もあるぜ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0073
    ChrTalk(
        0x101,
        (
            "#5P#0001Fとにかく一刻を争う。\x01",
            "いきなり戦力分散するのも\x01",
            "あまり得策じゃないだろう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0074
    ChrTalk(
        0x101,
        (
            "#11P#0001F……エリィ。\x01",
            "この子の守りを頼んでいいか？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#6P#0104Fええ、任せておいて。\x02\x03",

            "#0100Fもし魔獣と戦闘になっても\x01",
            "私がこの子に近づけないわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D6")

    label("loc_31D6")

    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0076
    ChrTalk(
        0x101,
        (
            "#11P#0000F──アンリ。\x01",
            "これからお兄さんたちは\x01",
            "君の友だちを捜しに行く。\x02\x03",

            "ここにいたら君も危ないから\x01",
            "できれば付いてきて欲しいんだ。\x02\x03",

            "……どうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        "#5Pう、うん……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "#5Pボク、リュウのことが心配だし、\x01",
            "いっしょに行きます……！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#11P#0002Fよし、いい子だ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0080
    ChrTalk(
        0x101,
        (
            "#5P#0003F護衛対象を守りながらの捜索だ。\x02\x03",

            "#0001F今まで以上に慎重に\x01",
            "進んでいくことにしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        "#6P#0100Fええ……！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        "#6P#0204F……了解です。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#4P#0300Fそんじゃ、もう一人の\x01",
            "ワンパク小僧を捜すとしますか。\x02",
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
            "アンリが護衛対象として\x01",
            "パーティに加わりました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※護衛対象のキャラが戦闘不能になると\x01",
            "  ゲームオーバーになってしまいます。\x01",
            "  上手く守りながら進みましょう。\x07\x00\x02",
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

    # Function_15_2084 end

    def Function_16_34E6(): pass

    label("Function_16_34E6")

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
            "エレベーターはロックされているらしく\x01",
            "ボタンを押しても反応しない。\x07\x00\x02",
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
            "#0200FこれがＡ区画の下層に降りる\x01",
            "エレベーターですね。\x02\x03",

            "認証コードを打ち込みます。\x02",
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
            "ティオは制御パネルを開いて\x01",
            "８ケタの数字を打ち込んでいった。\x07\x00\x02",
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
        "#0202F……起動しました。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#12P#0004Fよし、それじゃあ降りるか。\x02\x03",

            "#0000Fその端末っていうのは\x01",
            "下層のどこにあるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        (
            "#0203Fおそらく下層の最奥にあるかと。\x02\x03",

            "#0201Fそれなりに歩くとは思うので\x01",
            "気をつけた方がよさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあ、ああ……\x01",
            "（そんな場所に一人で\x01",
            "  行こうとしてたのか……？）\x02",
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

    # Function_16_34E6 end

    def Function_17_37D9(): pass

    label("Function_17_37D9")

    EventBegin(0x1)

    #C0093
    ChrTalk(
        0x101,
        (
            "#0001F……さっきの子供の声が気になる。\x02\x03",

            "確か……この近くじゃなかったか？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 191670, 0, 200070, 90)
    EventEnd(0x4)
    Return()

    # Function_17_37D9 end

    SaveToFile()

Try(main)
