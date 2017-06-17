from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0010.bin",                # FileName
        "m0010",                    # MapName
        "m0010",                    # Location
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
        "m0010",                  # 0
        "bm0011",                 # 1
        "bm0011",                 # 2
        "bm0011",                 # 3
        "bm0011",                 # 4
        "bm0010",                 # 5
        "bm0010",                 # 6
        "bm0010",                 # 7
        "bm0010",                 # 8
        "bm0013",                 # 9
        "bm0013",                 # 10
        "bm0013",                 # 11
        "bm0013",                 # 12
    ))

    ATBonus("ATBonus_35C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_288C", 14,  2,   10,  8,   2,   2,   0)
    Sepith("Sepith_287C", 4,   10,  14,  5,   2,   0,   2)
    Sepith("Sepith_2884", 7,   14,  6,   4,   0,   3,   3)
    Sepith("Sepith_2894", 0,   0,   0,   14,  8,   8,   8)

    MonsterBattlePostion("MonsterBattlePostion_3FC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_420", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_424", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_428", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_42C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_430", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_434", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_440", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_448", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_44C", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_450", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_454", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 0, 0, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_A74", 0x0000, 22, 6, 45, 4, 1, 25, 0, "bm0013", "Sepith_288C", 60, 30, 10, 0,
        (
            ("ms60400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms60400.dat", "ms60400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms60400.dat", "ms60400.dat", "ms60400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9D8", 0x0000, 22, 6, 45, 4, 1, 30, 0, "bm0013", "Sepith_287C", 60, 30, 10, 0,
        (
            ("ms62000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms62000.dat", "ms62000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms62000.dat", "ms62000.dat", "ms62000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_45C", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0011", "Sepith_2884", 60, 30, 10, 0,
        (
            ("ms69000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms69000.dat", "ms69000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_43C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms69000.dat", "ms75500.dat", "ms69000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7400", "ed7403", "ATBonus_35C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_8A0", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0010", "Sepith_2894", 60, 30, 10, 0,
        (
            ("ms75500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms75500.dat", "ms75500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms75500.dat", "ms75500.dat", "ms75500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_594", 0x0000, 22, 6, 45, 4, 1, 25, 0, "bm0011", "Sepith_288C", 60, 30, 10, 0,
        (
            ("ms60400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms60400.dat", "ms60400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_43C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms60400.dat", "ms62000.dat", "ms60400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7400", "ed7403", "ATBonus_35C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_93C", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0013", "Sepith_2884", 60, 30, 10, 0,
        (
            ("ms69000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms69000.dat", "ms69000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms69000.dat", "ms69000.dat", "ms69000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_41C", "ed7400", "ed7403", "ATBonus_35C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_630", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0011", "Sepith_2894", 60, 30, 10, 0,
        (
            ("ms75500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms75500.dat", "ms75500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3DC", "MonsterBattlePostion_43C", "ed7400", "ed7403", "ATBonus_35C"),
            ("ms75500.dat", "ms60400.dat", "ms75500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_43C", "ed7400", "ed7403", "ATBonus_35C"),
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
        "monster/ch69050.itc",               # 10
        "monster/ch69051.itc",               # 11
        "monster/ch62050.itc",               # 12
        "monster/ch62051.itc",               # 13
        "monster/ch60450.itc",               # 14
        "monster/ch60450.itc",               # 15
        "monster/ch75550.itc",               # 16
        "monster/ch75550.itc",               # 17
    ))

    DeclMonster(197620,  197110,  0,       0x1010000,    "BattleInfo_A74", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(202780,  202660,  0,       0x1010000,    "BattleInfo_9D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-420,    -202500, 0,       0x1010000,    "BattleInfo_45C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(2070,    -398070, 100,     0x1010000,    "BattleInfo_8A0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(98120,   -400140, 0,       0x1010000,    "BattleInfo_594", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(203150,  -203670, 0,       0x1010000,    "BattleInfo_9D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(196930,  -197950, 0,       0x1010000,    "BattleInfo_93C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(199720,  -498190, 100,     0x1010000,    "BattleInfo_8A0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(596800,  -203330, 0,       0x1010000,    "BattleInfo_A74", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(601260,  -198470, 0,       0x1010000,    "BattleInfo_9D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(493500,  -398740, 0,       0x1010000,    "BattleInfo_45C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(499960,  -401800, 0,       0x1010000,    "BattleInfo_630", 0,   22,  0xFFFF, 6,  7)

    DeclActor(200000,  0,       0,       1200,    200000,  1000,    0,       0x007C, 0,  3,  0x0000)
    DeclActor(100000,  0,       -100000, 1200,    100000,  1000,    -100000, 0x007C, 0,  4,  0x0000)
    DeclActor(200000,  0,       -500000, 1200,    200000,  1000,    -500000, 0x007C, 0,  5,  0x0000)
    DeclActor(0,       0,       2000,    1200,    0,       1000,    2500,    0x007C, 0,  6,  0x0000)
    DeclActor(602000,  0,       -400000, 1200,    602500,  1000,    -400000, 0x007C, 0,  8,  0x0000)
    DeclActor(207100,  12000,   -393000, 2000,    207100,  13000,   -393000, 0x007C, 0,  10, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_C3C",          # 00, 0
        "Function_1_CAF",          # 01, 1
        "Function_2_1406",         # 02, 2
        "Function_3_14BE",         # 03, 3
        "Function_4_160B",         # 04, 4
        "Function_5_1758",         # 05, 5
        "Function_6_18A5",         # 06, 6
        "Function_7_1A37",         # 07, 7
        "Function_8_1B7E",         # 08, 8
        "Function_9_1D12",         # 09, 9
        "Function_10_1E59",        # 0A, 10
        "Function_11_20BE",        # 0B, 11
    ))


    def Function_0_C3C(): pass

    label("Function_0_C3C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C83")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C69")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_C83")

    label("loc_C69")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C83")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)

    label("loc_C83")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C94")
    SetScenarioFlags(0x54, 0)

    label("loc_C94")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CAE")
    Event(0, 11)

    label("loc_CAE")

    Return()

    # Function_0_C3C end

    def Function_1_CAF(): pass

    label("Function_1_CAF")

    SetMapObjFrame(0x9, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0xA, "m00ele00", 0x2, "up_kp")
    SetBarrier(0x0, 0x0, 0x1, 0x0, 196000, 12000, -400000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 200000, 12000, -396000, 4000, 2000, 0)
    SetBarrier(0x0, 0x2, 0x1, 0x0, 204000, 12000, -400000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 196000, -2000, -400000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 200000, -2000, -396000, 4000, 2000, 0)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 204000, -2000, -400000, 4000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 1)), scpexpr(EXPR_END)), "loc_DCA")
    SetMapObjFrame(0xB, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "obj01", 0x2, "up_kp")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    Jump("loc_E06")

    label("loc_DCA")

    SetMapObjFrame(0xB, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "obj01", 0x2, "down_kp")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)

    label("loc_E06")

    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 0)), scpexpr(EXPR_END)), "loc_E71")
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x1, "light00", 0x1, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_EB1")

    label("loc_E71")

    SetMapObjFrame(0x1, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x1, "light00", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x1, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_EB1")

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
    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D0")
    OP_70(0xC, 0x0)
    Jump("loc_13D4")

    label("loc_13D0")

    OP_70(0xC, 0x1E)

    label("loc_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E7")
    OP_70(0xD, 0x0)
    Jump("loc_13EB")

    label("loc_13E7")

    OP_70(0xD, 0x1E)

    label("loc_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FE")
    OP_70(0xE, 0x0)
    Jump("loc_1402")

    label("loc_13FE")

    OP_70(0xE, 0x1E)

    label("loc_1402")

    Call(0, 2)
    Return()

    # Function_1_CAF end

    def Function_2_1406(): pass

    label("Function_2_1406")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x91), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1428")
    SetMapObjFlags(0xC, 0x4)
    Jump("loc_142E")

    label("loc_1428")

    ClearMapObjFlags(0xC, 0x4)

    label("loc_142E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_144F")
    SetChrFlags(0xB, 0x8)
    Jump("loc_1454")

    label("loc_144F")

    ClearChrFlags(0xB, 0x8)

    label("loc_1454")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1475")
    SetChrFlags(0xD, 0x8)
    Jump("loc_147A")

    label("loc_1475")

    ClearChrFlags(0xD, 0x8)

    label("loc_147A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1492")
    SetChrFlags(0xF, 0x8)
    Jump("loc_1497")

    label("loc_1492")

    ClearChrFlags(0xF, 0x8)

    label("loc_1497")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x81), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B8")
    SetChrFlags(0x10, 0x8)
    Jump("loc_14BD")

    label("loc_14B8")

    ClearChrFlags(0x10, 0x8)

    label("loc_14BD")

    Return()

    # Function_2_1406 end

    def Function_3_14BE(): pass

    label("Function_3_14BE")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BA")
    Sound(14, 0, 100, 0)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_1543")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10B, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_15B5")

    label("loc_1543")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xC, 0x1E, 0x0, 0x0, 0x0)

    label("loc_15B5")

    Jump("loc_15FF")

    label("loc_15BA")

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

    label("loc_15FF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_14BE end

    def Function_4_160B(): pass

    label("Function_4_160B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1707")
    Sound(14, 0, 100, 0)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3E, 1)"), scpexpr(EXPR_END)), "loc_1690")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10B, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1702")

    label("loc_1690")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x3E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x3E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1702")

    Jump("loc_174C")

    label("loc_1707")

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

    label("loc_174C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_160B end

    def Function_5_1758(): pass

    label("Function_5_1758")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1854")
    Sound(14, 0, 100, 0)
    OP_71(0xE, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E4, 1)"), scpexpr(EXPR_END)), "loc_17DD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10B, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_184F")

    label("loc_17DD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5E4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5E4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xE, 0x1E, 0x0, 0x0, 0x0)

    label("loc_184F")

    Jump("loc_1899")

    label("loc_1854")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_1899")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1758 end

    def Function_6_18A5(): pass

    label("Function_6_18A5")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0010
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A2F")
    Fade(500)
    SetChrPos(0x0, -600, 0, 600, 0)
    SetChrPos(0x1, 600, 0, 600, 0)
    SetChrPos(0x2, -600, 0, -600, 0)
    SetChrPos(0x3, 600, 0, -600, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_198F")
    SetChrPos(0x4, -600, 0, -1800, 0)
    SetChrPos(0x5, 600, 0, -1800, 0)
    Jump("loc_19AE")

    label("loc_198F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19AE")
    SetChrPos(0x4, 0, 0, -1800, 0)

    label("loc_19AE")

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
    SetMapObjFrame(0x9, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0001", 0, 0, 0)
    IdleLoop()

    label("loc_1A2F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_18A5 end

    def Function_7_1A37(): pass

    label("Function_7_1A37")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x9, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, -600, 30000, 600, 0)
    OP_90(0x1, 600, 30000, 600, 0)
    OP_90(0x2, -600, 30000, -600, 0)
    OP_90(0x3, 600, 30000, -600, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0A")
    OP_90(0x4, -600, 30000, -1800, 0)
    OP_90(0x5, 600, 30000, -1800, 0)
    Jump("loc_1B29")

    label("loc_1B0A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B29")
    OP_90(0x4, 0, 30000, -1800, 0)

    label("loc_1B29")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 0, 3000)
    SetMapObjFrame(0x9, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x9)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_1A37 end

    def Function_8_1B7E(): pass

    label("Function_8_1B7E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0011
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D0A")
    Fade(500)
    SetChrPos(0x0, 600600, 0, -400600, 90)
    SetChrPos(0x1, 600600, 0, -399400, 90)
    SetChrPos(0x2, 599400, 0, -400600, 90)
    SetChrPos(0x3, 599400, 0, -399400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C68")
    SetChrPos(0x4, 598200, 0, -400600, 90)
    SetChrPos(0x5, 598200, 0, -399400, 90)
    Jump("loc_1C87")

    label("loc_1C68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C87")
    SetChrPos(0x4, 598200, 0, -400000, 90)

    label("loc_1C87")

    OP_68(600000, 0, -400000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(600000, -5000, -400000, 2000)
    SetMapObjFrame(0xA, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0011", 0, 0, 0)
    IdleLoop()

    label("loc_1D0A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1B7E end

    def Function_9_1D12(): pass

    label("Function_9_1D12")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xA, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(600000, -5000, -400000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600600, -10000, -400600, 90)
    OP_90(0x1, 600600, -10000, -399400, 90)
    OP_90(0x2, 599400, -10000, -400600, 90)
    OP_90(0x3, 599400, -10000, -399400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE7")
    OP_90(0x4, 598200, 30000, -400600, 90)
    OP_90(0x5, 598200, 30000, -399400, 90)
    Jump("loc_1E06")

    label("loc_1DE7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E06")
    OP_90(0x4, 598200, 30000, -400000, 90)

    label("loc_1E06")

    Sound(145, 0, 100, 0)
    OP_68(600000, 0, -400000, 3000)
    SetMapObjFrame(0xA, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xA)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1D12 end

    def Function_10_1E59(): pass

    label("Function_10_1E59")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "リフトの制御装置がある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B6")
    Fade(500)
    SetChrPos(0x0, 205650, 12000, -394120, 45)
    SetChrPos(0x1, 204410, 12000, -393450, 90)
    SetChrPos(0x2, 204340, 12000, -392080, 90)
    SetChrPos(0x3, 202600, 12000, -393170, 90)
    OP_68(205850, 13000, -393690, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 1)), scpexpr(EXPR_END)), "loc_1FFE")
    SetMapObjFrame(0xB, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    Fade(500)
    OP_68(198660, 13000, -400580, 0)
    MoveCamera(45, 56, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(29000, 0)
    Sleep(500)
    OP_0D()
    Sound(146, 2, 100, 0)
    SetMapObjFrame(0xFF, "obj01", 0x2, "down")
    Sleep(5000)
    OP_24(0x92)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_6F(0x1)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    ClearScenarioFlags(0x54, 1)
    Jump("loc_20B6")

    label("loc_1FFE")

    SetMapObjFrame(0xB, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    Fade(500)
    OP_68(198660, 13000, -400580, 0)
    MoveCamera(45, 56, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(29000, 0)
    Sleep(500)
    OP_0D()
    Sound(146, 2, 100, 0)
    SetMapObjFrame(0xFF, "obj01", 0x2, "up")
    Sleep(6000)
    OP_24(0x92)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_6F(0x1)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetScenarioFlags(0x54, 1)

    label("loc_20B6")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1E59 end

    def Function_11_20BE(): pass

    label("Function_11_20BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(106000, 1800, 0, 0)
    MoveCamera(55, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 83500, 150, -400, 90)
    SetChrPos(0x103, 83500, 150, 400, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(100000, 1800, 0, 8000)
    MoveCamera(65, 11, 0, 8000)
    SetCameraDistance(21000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(85800, 1100, 0, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)

    def lambda_219B():
        OP_96(0xFE, 0x14F28, 0x0, 0xFFFFFDA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_219B)

    def lambda_21B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_21B5)
    Sleep(400)

    def lambda_21C9():
        OP_96(0xFE, 0x14F28, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21C9)

    def lambda_21E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_21E3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0013
    ChrTalk(
        0x101,
        (
            "#6P#0008Fしかし上の階層と比べると\x01",
            "照明とかが古いタイプみたいだな……\x02\x03",

            "#0000Fもしかして建造された時期が違うのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        (
            "#0203F#5Pええ、この辺りは初期の頃に\x01",
            "建造されたエリアみたいですね。\x02\x03",

            "#0200Fジオフロント自体、２０年前から\x01",
            "続いている都市計画の産物ですが……\x02\x03",

            "割と場当たり的な仕様変更で\x01",
            "複雑な構造になったみたいですね。\x02\x03",

            "#0206F工事の発注に関しては\x01",
            "議員の利権が絡んでいるという話を\x01",
            "エリィさんから聞いた事があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        "#6P#0006Fはぁ……なるほどね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0016
    ChrTalk(
        0x101,
        (
            "#12P#0001F──それにしても、\x01",
            "かなり広そうな場所じゃないか。\x02\x03",

            "こんな所に一人で\x01",
            "来ようなんて思ったのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0017
    ChrTalk(
        0x103,
        (
            "#0208F#5P……それは……\x02\x03",

            "#0206Fその、済みません……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#12P#0012Fはは、いいよ。\x02\x03",

            "#0000Fとにかくケガしないように\x01",
            "それだけは心がけてくれ。\x02\x03",

            "俺の方も全力で守るからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        "#0202F#5P…………はい。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    Sleep(500)

    #C0020
    ChrTalk(
        0x103,
        (
            "#0203F#5Pあの、ロイドさん。\x02\x03",

            "#0201Fでしたら……\x01",
            "コンビネーションを使った戦技#4Rクラフト#を\x01",
            "試してみませんか？\x02\x03",

            "エリィさんやランディさんみたいに\x01",
            "上手くは出来ないかもしれませんが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0021
    ChrTalk(
        0x101,
        (
            "#12P#0002Fああ……いいかもしれないな！\x02\x03",

            "#0014Fよし、せっかく２人きりだし\x01",
            "この際しっかり練習しておくか！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        "#0202F#5P………はい……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 3)), scpexpr(EXPR_END)), "loc_275F")
    AddCraft(0x0, 0x155)
    AddCraft(0x2, 0x155)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとティオがコンビクラフト\x01\x07\x02",

            "『Ω#2Rオメガ#ストライクⅡ』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＣＰを１００ずつ消費することで\x01",
            "強力なコンビネーション攻撃が繰り出せます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_281B")

    label("loc_275F")

    AddCraft(0x0, 0x14B)
    AddCraft(0x2, 0x14B)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとティオがコンビクラフト\x01\x07\x02",

            "『Ω#2Rオメガ#ストライク』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＣＰを１００ずつ消費することで\x01",
            "強力なコンビネーション攻撃が繰り出せます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_281B")

    SetChrPos(0x0, 85800, 0, 0, 90)
    SetScenarioFlags(0xA1, 0)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_11_20BE end

    SaveToFile()

Try(main)
