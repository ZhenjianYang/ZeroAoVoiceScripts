from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0110.bin",                # FileName
        "m0110",                    # MapName
        "m0110",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0110",                  # 0
        "MapThread",              # 1
        "bm0111",                 # 2
        "bm0111",                 # 3
        "bm0111",                 # 4
        "bm0111",                 # 5
        "bm0110",                 # 6
        "bm0110",                 # 7
        "bm0110",                 # 8
        "bm0110",                 # 9
    ))

    ATBonus("ATBonus_3B0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2B8D", 1,   8,   6,   1,   1,   1,   2)
    Sepith("Sepith_2B95", 1,   8,   6,   1,   1,   1,   2)
    Sepith("Sepith_2B9D", 0,   1,   0,   2,   0,   0,   0)
    Sepith("Sepith_2BA5", 1,   1,   0,   1,   1,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_450", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_46C", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_494", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_49C", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_470", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_474", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_478", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_47C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_480", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_484", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_488", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 5, 5, 45)

    # monster count: 7

    BattleInfo(
        "BattleInfo_578", 0x0000, 48, 6, 60, 6, 1, 25, 0, "bm0111", "Sepith_2B8D", 30, 45, 20, 5,
        (
            ("ms60200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_450", "MonsterBattlePostion_490", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_490", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_450", "MonsterBattlePostion_490", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms60200.dat", "ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_490", "ed7400", "ed7403", "ATBonus_3B0"),
        )
    )

    BattleInfo(
        "BattleInfo_960", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0110", "Sepith_2B95", 30, 45, 20, 5,
        (
            ("ms61900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_450", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms61900.dat", "ms61900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms61900.dat", "ms61900.dat", "ms61900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_450", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms61900.dat", "ms61900.dat", "ms61900.dat", "ms61900.dat", 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
        )
    )

    BattleInfo(
        "BattleInfo_898", 0x0000, 48, 6, 60, 6, 1, 25, 0, "bm0110", "Sepith_2B8D", 30, 45, 20, 5,
        (
            ("ms60200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_450", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_450", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms60200.dat", "ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
        )
    )

    BattleInfo(
        "BattleInfo_7D0", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0110", "Sepith_2B9D", 30, 45, 20, 5,
        (
            ("ms68000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_450", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms68000.dat", "ms68000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms68000.dat", "ms68000.dat", "ms68000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_450", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms68000.dat", "ms68000.dat", "ms68000.dat", "ms68000.dat", 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
        )
    )

    BattleInfo(
        "BattleInfo_A28", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0110", "Sepith_2BA5", 30, 45, 20, 5,
        (
            ("ms71200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_450", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_450", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, "MonsterBattlePostion_430", "MonsterBattlePostion_470", "ed7400", "ed7403", "ATBonus_3B0"),
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
        "monster/ch68050.itc",               # 10
        "monster/ch68050.itc",               # 11
        "monster/ch60250.itc",               # 12
        "monster/ch60250.itc",               # 13
        "monster/ch61950.itc",               # 14
        "monster/ch61950.itc",               # 15
        "monster/ch71250.itc",               # 16
        "monster/ch71251.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-30,     105700,  0,       0x1010000,    "BattleInfo_578", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(98240,   89740,   -2000,   0x1010000,    "BattleInfo_960", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(197650,  -2330,   0,       0x1010000,    "BattleInfo_898", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(200360,  188330,  -2000,   0x1010000,    "BattleInfo_7D0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(185760,  212770,  -2000,   0x1010000,    "BattleInfo_7D0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(215980,  204420,  -2000,   0x1010000,    "BattleInfo_A28", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(200370,  219440,  -6000,   0x1010000,    "BattleInfo_7D0", 0,   16,  0xFFFF, 0,  1)

    DeclActor(199980,  0,       30,      1200,    199980,  1000,    30,      0x007C, 0,  4,  0x0000)
    DeclActor(399160,  0,       200440,  1200,    399160,  1000,    200440,  0x007C, 0,  5,  0x0000)
    DeclActor(299900,  0,       299870,  1200,    299900,  1000,    299870,  0x007C, 0,  6,  0x0000)
    DeclActor(20,      0,       200000,  1200,    20,      1000,    200000,  0x007C, 0,  7,  0x0000)
    DeclActor(0,       0,       -2000,   1200,    0,       1000,    -2500,   0x007C, 0,  15, 0x0000)
    DeclActor(1800,    0,       94000,   1200,    1800,    1000,    94000,   0x007C, 0,  8,  0x0000)
    DeclActor(184000,  -6000,   189000,  1200,    184000,  -5000,   189000,  0x007C, 0,  9,  0x0000)
    DeclActor(189500,  -2000,   202500,  1200,    189500,  -1000,   202500,  0x007C, 0,  10, 0x0000)
    DeclActor(225500,  -2000,   209500,  1200,    225500,  -1000,   209500,  0x007C, 0,  11, 0x0000)
    DeclActor(199000,  -2000,   205500,  1200,    199000,  -1000,   205500,  0x007C, 0,  12, 0x0000)
    DeclActor(202000,  0,       100000,  1200,    202000,  1000,    100000,  0x007C, 0,  13, 0x0000)
    DeclActor(110000,  0,       2000,    1200,    110000,  1000,    2000,    0x007C, 0,  14, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_B94",          # 00, 0
        "Function_1_BBF",          # 01, 1
        "Function_2_BE8",          # 02, 2
        "Function_3_1547",         # 03, 3
        "Function_4_1602",         # 04, 4
        "Function_5_174F",         # 05, 5
        "Function_6_189C",         # 06, 6
        "Function_7_19E9",         # 07, 7
        "Function_8_1B5A",         # 08, 8
        "Function_9_1D0E",         # 09, 9
        "Function_10_1EE3",        # 0A, 10
        "Function_11_20E7",        # 0B, 11
        "Function_12_22BC",        # 0C, 12
        "Function_13_24C0",        # 0D, 13
        "Function_14_26B8",        # 0E, 14
        "Function_15_286C",        # 0F, 15
        "Function_16_29FE",        # 10, 16
    ))


    def Function_0_B94(): pass

    label("Function_0_B94")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BB6")
    Sound(150, 0, 100, 0)
    Sleep(900)
    Jump("loc_BB9")

    label("loc_BB6")

    Sleep(30)

    label("loc_BB9")

    Jump("Function_0_B94")

    label("loc_BBE")

    Return()

    # Function_0_B94 end

    def Function_1_BBF(): pass

    label("Function_1_BBF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE7")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE7")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)

    label("loc_BE7")

    Return()

    # Function_1_BBF end

    def Function_2_BE8(): pass

    label("Function_2_BE8")

    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 0, 0, 98000, 4000, 2000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 0, 0, 100000, 4000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 0)), scpexpr(EXPR_END)), "loc_C68")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0x17, "m01gim02", 0x2, "stop_kp")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    Jump("loc_CAD")

    label("loc_C68")

    SetMapObjFrame(0x10, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0x17, "m01gim02", 0x2, "loop")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CAD")
    SetScenarioFlags(0x0, 0)

    label("loc_CAD")

    SetBarrier(0x0, 0x2, 0x1, 0x0, 180000, -6000, 190000, 4000, 2000, 0)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 180000, -6000, 194000, 4000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 1)), scpexpr(EXPR_END)), "loc_D24")
    SetMapObjFrame(0x11, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xD, "m01gim00", 0x2, "stop_kp")
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    Jump("loc_D72")

    label("loc_D24")

    SetMapObjFrame(0x11, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xD, "m01gim00", 0x2, "loop")
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D72")
    SetScenarioFlags(0x0, 0)

    label("loc_D72")

    SetBarrier(0x0, 0x4, 0x1, 0x0, 194000, -1850, 200000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 198000, -2000, 200000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x6, 0x1, 0x0, 196000, -6000, 198000, 4000, 2000, 0)
    SetBarrier(0x0, 0x7, 0x1, 0x0, 196000, -6000, 202000, 4000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 2)), scpexpr(EXPR_END)), "loc_E5C")
    SetMapObjFrame(0x12, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0x14, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xE, "m01gim00", 0x2, "loop")
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E57")
    SetScenarioFlags(0x0, 0)

    label("loc_E57")

    Jump("loc_EA6")

    label("loc_E5C")

    SetMapObjFrame(0x12, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0x14, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xE, "m01gim00", 0x2, "stop_kp")
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)

    label("loc_EA6")

    SetBarrier(0x0, 0x8, 0x1, 0x0, 220000, 0, 214000, 4000, 2000, 0)
    SetBarrier(0x0, 0x9, 0x1, 0x0, 218000, 0, 216000, 4000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 3)), scpexpr(EXPR_END)), "loc_F1D")
    SetMapObjFrame(0x13, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xF, "m01gim00", 0x2, "stop_kp")
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)
    Jump("loc_F6B")

    label("loc_F1D")

    SetMapObjFrame(0x13, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xF, "m01gim00", 0x2, "loop")
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F6B")
    SetScenarioFlags(0x0, 0)

    label("loc_F6B")

    SetBarrier(0x0, 0xA, 0x1, 0x0, 200000, 0, 91000, 4000, 2000, 0)
    SetBarrier(0x0, 0xB, 0x1, 0x0, 200000, 0, 93000, 4000, 2000, 0)
    SetBarrier(0x0, 0xC, 0x1, 0x0, 200000, 0, 109000, 4000, 2000, 0)
    SetBarrier(0x0, 0xD, 0x1, 0x0, 200000, 0, 111000, 4000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 5)), scpexpr(EXPR_END)), "loc_1038")
    SetMapObjFrame(0x15, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0x18, "m01gim02", 0x2, "stop_kp")
    SetMapObjFrame(0x19, "m01gim02", 0x2, "stop_kp")
    SetBarrier(0x2, 0xA, 0x1)
    SetBarrier(0x2, 0xB, 0x1)
    SetBarrier(0x2, 0xC, 0x1)
    SetBarrier(0x2, 0xD, 0x1)
    Jump("loc_109F")

    label("loc_1038")

    SetMapObjFrame(0x15, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0x18, "m01gim02", 0x2, "loop")
    SetMapObjFrame(0x19, "m01gim02", 0x2, "loop")
    SetBarrier(0x3, 0xA, 0x1)
    SetBarrier(0x3, 0xB, 0x1)
    SetBarrier(0x3, 0xC, 0x1)
    SetBarrier(0x3, 0xD, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_109F")
    SetScenarioFlags(0x0, 0)

    label("loc_109F")

    SetBarrier(0x0, 0xE, 0x1, 0x0, 105000, 300, 0, 4000, 2000, 90000)
    SetBarrier(0x0, 0xF, 0x1, 0x0, 103000, 300, 0, 4000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 6)), scpexpr(EXPR_END)), "loc_1116")
    SetMapObjFrame(0x16, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0x1A, "m01gim02", 0x2, "stop_kp")
    SetBarrier(0x2, 0xE, 0x1)
    SetBarrier(0x2, 0xF, 0x1)
    Jump("loc_1164")

    label("loc_1116")

    SetMapObjFrame(0x16, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0x1A, "m01gim02", 0x2, "loop")
    SetBarrier(0x3, 0xE, 0x1)
    SetBarrier(0x3, 0xF, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1164")
    SetScenarioFlags(0x0, 0)

    label("loc_1164")

    SetMapObjFrame(0xC, "m00ele00", 0x2, "down_kp")
    OP_10(0x18, 0x0)
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
    SetMapObjFrame(0xB, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xB, "light01", 0x0, 0x1)
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14FA")
    OP_70(0x1B, 0x0)
    Jump("loc_14FE")

    label("loc_14FA")

    OP_70(0x1B, 0x1E)

    label("loc_14FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1511")
    OP_70(0x1C, 0x0)
    Jump("loc_1515")

    label("loc_1511")

    OP_70(0x1C, 0x1E)

    label("loc_1515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1528")
    OP_70(0x1D, 0x0)
    Jump("loc_152C")

    label("loc_1528")

    OP_70(0x1D, 0x1E)

    label("loc_152C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153F")
    OP_70(0x1E, 0x0)
    Jump("loc_1543")

    label("loc_153F")

    OP_70(0x1E, 0x1E)

    label("loc_1543")

    Call(0, 3)
    Return()

    # Function_2_BE8 end

    def Function_3_1547(): pass

    label("Function_3_1547")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1568")
    SetChrFlags(0x9, 0x8)
    Jump("loc_156D")

    label("loc_1568")

    ClearChrFlags(0x9, 0x8)

    label("loc_156D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1594")
    SetChrFlags(0xB, 0x8)
    SetMapObjFlags(0x1B, 0x4)
    Jump("loc_159F")

    label("loc_1594")

    ClearChrFlags(0xB, 0x8)
    ClearMapObjFlags(0x1B, 0x4)

    label("loc_159F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D3")
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    Jump("loc_15E2")

    label("loc_15D3")

    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)

    label("loc_15E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FB")
    SetMapObjFlags(0x1C, 0x4)
    Jump("loc_1601")

    label("loc_15FB")

    ClearMapObjFlags(0x1C, 0x4)

    label("loc_1601")

    Return()

    # Function_3_1547 end

    def Function_4_1602(): pass

    label("Function_4_1602")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FE")
    Sound(14, 0, 100, 0)
    OP_71(0x1B, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1687")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10E, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_16F9")

    label("loc_1687")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1B, 0x1E, 0x0, 0x0, 0x0)

    label("loc_16F9")

    Jump("loc_1743")

    label("loc_16FE")

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

    label("loc_1743")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1602 end

    def Function_5_174F(): pass

    label("Function_5_174F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184B")
    Sound(14, 0, 100, 0)
    OP_71(0x1C, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_17D4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10E, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1846")

    label("loc_17D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1C, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1846")

    Jump("loc_1890")

    label("loc_184B")

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

    label("loc_1890")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_174F end

    def Function_6_189C(): pass

    label("Function_6_189C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1998")
    Sound(14, 0, 100, 0)
    OP_71(0x1D, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x7E, 1)"), scpexpr(EXPR_END)), "loc_1921")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10E, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1993")

    label("loc_1921")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1D, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1993")

    Jump("loc_19DD")

    label("loc_1998")

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

    label("loc_19DD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_189C end

    def Function_7_19E9(): pass

    label("Function_7_19E9")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B23")
    Sound(14, 0, 100, 0)
    OP_71(0x1E, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1E, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×２００\x01\x07\x02",

            "#57I水のセピス×２００\x01\x07\x02",

            "#58I火のセピス×２００\x01\x07\x02",

            "#59I風のセピス×２００\x01\x07\x02",

            "#60I時のセピス×２００\x01\x07\x02",

            "#61I空のセピス×２００\x01\x07\x02",

            "#62I幻のセピス×２００\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10E, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1B48")

    label("loc_1B23")


    #A0011
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

    label("loc_1B48")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_19E9 end

    def Function_8_1B5A(): pass

    label("Function_8_1B5A")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水流調整用の制御装置がある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D06")
    Fade(500)
    SetChrPos(0x0, 430, 0, 93860, 90)
    SetChrPos(0x1, 60, 0, 91600, 0)
    SetChrPos(0x2, -1600, 0, 91600, 0)
    SetChrPos(0x3, -650, 0, 90580, 0)
    OP_68(-210, 1500, 95550, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 0)), scpexpr(EXPR_END)), "loc_1CB1")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    SetMapObjFrame(0x17, "m01gim02", 0x2, "start")
    Sleep(1000)
    SetMapObjFrame(0x17, "m01gim02", 0x2, "loop")
    Sleep(500)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    ClearScenarioFlags(0x55, 0)
    Jump("loc_1D06")

    label("loc_1CB1")

    SetMapObjFrame(0x10, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    ClearScenarioFlags(0x0, 0)
    SetMapObjFrame(0x17, "m01gim02", 0x2, "stop")
    Sleep(1200)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetScenarioFlags(0x55, 0)

    label("loc_1D06")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1B5A end

    def Function_9_1D0E(): pass

    label("Function_9_1D0E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水流調整用の制御装置がある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EDB")
    Fade(500)
    SetChrPos(0x0, 184100, -6000, 187510, 0)
    SetChrPos(0x1, 181160, -6000, 188120, 90)
    SetChrPos(0x2, 181160, -6000, 186500, 90)
    SetChrPos(0x3, 179590, -6000, 187220, 90)
    OP_68(180400, -5000, 188010, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 1)), scpexpr(EXPR_END)), "loc_1E6B")
    SetMapObjFrame(0x11, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    Sound(151, 0, 100, 0)
    SetMapObjFrame(0xD, "m01gim00", 0x2, "start")
    Sleep(1000)
    SetMapObjFrame(0xD, "m01gim00", 0x2, "loop")
    Sleep(500)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    ClearScenarioFlags(0x55, 1)
    Jump("loc_1EDB")

    label("loc_1E6B")

    SetMapObjFrame(0x11, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0x55, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EB6")
    ClearScenarioFlags(0x0, 0)

    label("loc_1EB6")

    SetMapObjFrame(0xD, "m01gim00", 0x2, "stop")
    Sleep(800)
    Sound(151, 0, 100, 0)
    Sleep(500)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)

    label("loc_1EDB")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1D0E end

    def Function_10_1EE3(): pass

    label("Function_10_1EE3")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水流調整用の制御装置がある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DF")
    Fade(500)
    SetChrPos(0x0, 188000, -2000, 202500, 90)
    SetChrPos(0x1, 188290, -2000, 200200, 0)
    SetChrPos(0x2, 186590, -2000, 200200, 0)
    SetChrPos(0x3, 187540, -2000, 199050, 0)
    OP_68(195960, -1000, 200430, 0)
    MoveCamera(45, 57, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 2)), scpexpr(EXPR_END)), "loc_2059")
    SetMapObjFrame(0x12, "m01gim01", 0x2, "off")
    SetMapObjFrame(0x14, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    ClearScenarioFlags(0x55, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2027")
    ClearScenarioFlags(0x0, 0)

    label("loc_2027")

    SetMapObjFrame(0xE, "m01gim00", 0x2, "stop")
    Sleep(800)
    Sound(151, 0, 100, 0)
    Sleep(500)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    Jump("loc_20DF")

    label("loc_2059")

    SetMapObjFrame(0x12, "m01gim01", 0x2, "on")
    SetMapObjFrame(0x14, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    Sound(151, 0, 100, 0)
    SetMapObjFrame(0xE, "m01gim00", 0x2, "start")
    Sleep(1000)
    SetMapObjFrame(0xE, "m01gim00", 0x2, "loop")
    Sleep(500)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetScenarioFlags(0x55, 2)

    label("loc_20DF")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1EE3 end

    def Function_11_20E7(): pass

    label("Function_11_20E7")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水流調整用の制御装置がある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B4")
    Fade(500)
    SetChrPos(0x0, 223890, -2000, 209460, 89)
    SetChrPos(0x1, 224030, -2000, 207170, 0)
    SetChrPos(0x2, 222400, -2000, 207290, 0)
    SetChrPos(0x3, 223410, -2000, 205540, 0)
    OP_68(219460, 1500, 214580, 0)
    MoveCamera(45, 59, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 3)), scpexpr(EXPR_END)), "loc_2244")
    SetMapObjFrame(0x13, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    Sound(151, 0, 100, 0)
    SetMapObjFrame(0xF, "m01gim00", 0x2, "start")
    Sleep(1000)
    SetMapObjFrame(0xF, "m01gim00", 0x2, "loop")
    Sleep(500)
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    ClearScenarioFlags(0x55, 3)
    Jump("loc_22B4")

    label("loc_2244")

    SetMapObjFrame(0x13, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0x55, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228F")
    ClearScenarioFlags(0x0, 0)

    label("loc_228F")

    SetMapObjFrame(0xF, "m01gim00", 0x2, "stop")
    Sleep(800)
    Sound(151, 0, 100, 0)
    Sleep(500)
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)

    label("loc_22B4")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_20E7 end

    def Function_12_22BC(): pass

    label("Function_12_22BC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水流調整用の制御装置がある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B8")
    Fade(500)
    SetChrPos(0x0, 199040, -2000, 203950, 0)
    SetChrPos(0x1, 201500, -2000, 204750, 270)
    SetChrPos(0x2, 201500, -2000, 203420, 270)
    SetChrPos(0x3, 202430, -2000, 204640, 270)
    OP_68(195960, -1000, 200430, 0)
    MoveCamera(45, 57, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 2)), scpexpr(EXPR_END)), "loc_2432")
    SetMapObjFrame(0x12, "m01gim01", 0x2, "off")
    SetMapObjFrame(0x14, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    ClearScenarioFlags(0x55, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2400")
    ClearScenarioFlags(0x0, 0)

    label("loc_2400")

    SetMapObjFrame(0xE, "m01gim00", 0x2, "stop")
    Sleep(800)
    Sound(151, 0, 100, 0)
    Sleep(500)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    Jump("loc_24B8")

    label("loc_2432")

    SetMapObjFrame(0x12, "m01gim01", 0x2, "on")
    SetMapObjFrame(0x14, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    Sound(151, 0, 100, 0)
    SetMapObjFrame(0xE, "m01gim00", 0x2, "start")
    Sleep(1000)
    SetMapObjFrame(0xE, "m01gim00", 0x2, "loop")
    Sleep(500)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetScenarioFlags(0x55, 2)

    label("loc_24B8")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_22BC end

    def Function_13_24C0(): pass

    label("Function_13_24C0")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水流調整用の制御装置がある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B0")
    Fade(500)
    SetChrPos(0x0, 200360, 0, 100000, 90)
    SetChrPos(0x1, 199500, 0, 101200, 90)
    SetChrPos(0x2, 199500, 0, 98800, 90)
    SetChrPos(0x3, 198120, 310, 100000, 90)
    OP_68(198460, 1650, 99180, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(37500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 5)), scpexpr(EXPR_END)), "loc_2642")
    SetMapObjFrame(0x15, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    SetMapObjFrame(0x18, "m01gim02", 0x2, "start")
    SetMapObjFrame(0x19, "m01gim02", 0x2, "start")
    Sleep(1000)
    SetMapObjFrame(0x18, "m01gim02", 0x2, "loop")
    SetMapObjFrame(0x19, "m01gim02", 0x2, "loop")
    Sleep(500)
    SetBarrier(0x3, 0xA, 0x1)
    SetBarrier(0x3, 0xB, 0x1)
    SetBarrier(0x3, 0xC, 0x1)
    SetBarrier(0x3, 0xD, 0x1)
    ClearScenarioFlags(0x55, 5)
    Jump("loc_26B0")

    label("loc_2642")

    SetMapObjFrame(0x15, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    ClearScenarioFlags(0x0, 0)
    SetMapObjFrame(0x18, "m01gim02", 0x2, "stop")
    SetMapObjFrame(0x19, "m01gim02", 0x2, "stop")
    Sleep(1200)
    SetBarrier(0x2, 0xA, 0x1)
    SetBarrier(0x2, 0xB, 0x1)
    SetBarrier(0x2, 0xC, 0x1)
    SetBarrier(0x2, 0xD, 0x1)
    SetScenarioFlags(0x55, 5)

    label("loc_26B0")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_24C0 end

    def Function_14_26B8(): pass

    label("Function_14_26B8")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水流調整用の制御装置がある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2864")
    Fade(500)
    SetChrPos(0x0, 110000, 0, 160, 0)
    SetChrPos(0x1, 111200, 0, -890, 0)
    SetChrPos(0x2, 108800, 0, -1130, 0)
    SetChrPos(0x3, 110000, 0, -1650, 0)
    OP_68(107460, 1500, 680, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(37500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 6)), scpexpr(EXPR_END)), "loc_280F")
    SetMapObjFrame(0x16, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    SetMapObjFrame(0x1A, "m01gim02", 0x2, "start")
    Sleep(1000)
    SetMapObjFrame(0x1A, "m01gim02", 0x2, "loop")
    Sleep(500)
    SetBarrier(0x3, 0xE, 0x1)
    SetBarrier(0x3, 0xF, 0x1)
    ClearScenarioFlags(0x55, 6)
    Jump("loc_2864")

    label("loc_280F")

    SetMapObjFrame(0x16, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    ClearScenarioFlags(0x0, 0)
    SetMapObjFrame(0x1A, "m01gim02", 0x2, "stop")
    Sleep(1200)
    SetBarrier(0x2, 0xE, 0x1)
    SetBarrier(0x2, 0xF, 0x1)
    SetScenarioFlags(0x55, 6)

    label("loc_2864")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_26B8 end

    def Function_15_286C(): pass

    label("Function_15_286C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0019
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29F6")
    Fade(500)
    SetChrPos(0x0, 600, 0, -3400, 0)
    SetChrPos(0x1, -600, 0, -3400, 0)
    SetChrPos(0x2, -600, 0, -4600, 0)
    SetChrPos(0x3, 600, 0, -4600, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2956")
    SetChrPos(0x4, -600, 0, -5800, 0)
    SetChrPos(0x5, 600, 0, -5800, 0)
    Jump("loc_2975")

    label("loc_2956")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2975")
    SetChrPos(0x4, 0, 0, -5800, 0)

    label("loc_2975")

    OP_68(600, 1000, -5000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(600, 6000, -5000, 3000)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0100", 0, 0, 0)
    IdleLoop()

    label("loc_29F6")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_286C end

    def Function_16_29FE(): pass

    label("Function_16_29FE")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, -5000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, -3400, 0)
    OP_90(0x1, -600, 30000, -3400, 0)
    OP_90(0x2, -600, 30000, -4600, 0)
    OP_90(0x3, 600, 30000, -4600, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AD1")
    OP_90(0x4, -600, 30000, -5800, 0)
    OP_90(0x5, 600, 30000, -5800, 0)
    Jump("loc_2AF0")

    label("loc_2AD1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AF0")
    OP_90(0x4, 0, 30000, -5800, 0)

    label("loc_2AF0")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, -5000, 3000)
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

    # Function_16_29FE end

    SaveToFile()

Try(main)
