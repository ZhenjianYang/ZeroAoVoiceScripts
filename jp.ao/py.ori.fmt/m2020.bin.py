from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m2020.bin",                # FileName
        "m2020",                    # MapName
        "m2020",                    # Location
        0x0078,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x23,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 120, 0, 1, 0, 2],
    )

    BuildStringList((
        "m2020",                  # 0
        " ",                      # 1
        " ",                      # 2
        "bm2020",                 # 3
        "bm2020",                 # 4
        "bm2020",                 # 5
        "bm2020",                 # 6
        "bm2020",                 # 7
        "bm2020",                 # 8
    ))

    ATBonus("ATBonus_280", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_290", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_15CE", 13,  0,   8,   8,   13,  8,   0)
    Sepith("Sepith_15C6", 12,  0,   0,   7,   16,  16,  0)
    Sepith("Sepith_15DE", 0,   27,  0,   0,   20,  1,   2)
    Sepith("Sepith_15D6", 10,  6,   6,   5,   5,   8,   15)

    MonsterBattlePostion("MonsterBattlePostion_2D0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_334", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_338", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_33C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_340", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_344", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_348", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 0, 0, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_40C", 0x0000, 88, 6, 60, 6, 1, 35, 0, "bm2020", "Sepith_15CE", 40, 35, 25, 0,
        (
            ("ms73700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2D0", "MonsterBattlePostion_330", "ed7450", "ed7453", "ATBonus_280"),
            ("ms73700.dat", "ms73700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_330", "ed7450", "ed7453", "ATBonus_280"),
            ("ms73700.dat", "ms73700.dat", "ms73700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2D0", "MonsterBattlePostion_330", "ed7450", "ed7453", "ATBonus_280"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_370", 0x0000, 88, 6, 60, 6, 1, 35, 0, "bm2020", "Sepith_15C6", 40, 35, 25, 0,
        (
            ("ms73600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2D0", "MonsterBattlePostion_330", "ed7450", "ed7453", "ATBonus_280"),
            ("ms73600.dat", "ms73600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_330", "ed7450", "ed7453", "ATBonus_280"),
            ("ms73600.dat", "ms73600.dat", "ms73600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2D0", "MonsterBattlePostion_330", "ed7450", "ed7453", "ATBonus_280"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4EC", 0x0000, 88, 6, 60, 6, 1, 40, 0, "bm2020", "Sepith_15DE", 40, 35, 25, 0,
        (
            ("ms73000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2D0", "MonsterBattlePostion_330", "ed7450", "ed7453", "ATBonus_280"),
            ("ms73000.dat", "ms73000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_330", "ed7450", "ed7453", "ATBonus_280"),
            ("ms73000.dat", "ms73000.dat", "ms73000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2D0", "MonsterBattlePostion_330", "ed7450", "ed7453", "ATBonus_280"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4A8", 0x0000, 88, 6, 60, 6, 1, 30, 0, "bm2020", "Sepith_15D6", 100, 0, 0, 0,
        (
            ("ms74000.dat", "ms73000.dat", "ms73000.dat", "ms73000.dat", 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_330", "ed7450", "ed7453", "ATBonus_280"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_5CC", 0x0002, 255, 6, 0, 6, 3, 0, 0, "bm2020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80200.dat", "ms80200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_350", "MonsterBattlePostion_330", "ed7451", "ed7453", "ATBonus_290"),
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
        "monster/ch73650.itc",               # 10
        "monster/ch73651.itc",               # 11
        "monster/ch73750.itc",               # 12
        "monster/ch73751.itc",               # 13
        "monster/ch74050.itc",               # 14
        "monster/ch74051.itc",               # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "monster/ch73050.itc",               # 18
        "monster/ch73050.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(18720,   107870,  4000,    0x1010000,    "BattleInfo_40C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(107540,  110600,  8000,    0x1010000,    "BattleInfo_370", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(114280,  210730,  12000,   0x1010000,    "BattleInfo_4EC", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(16960,   -4670,   0,       0x1010000,    "BattleInfo_40C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(111200,  4130,    12000,   0x1010000,    "BattleInfo_4EC", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(207130,  -2710,   16000,   0x1010000,    "BattleInfo_4A8", 0,   20,  0xFFFF, 4,  5)

    DeclActor(116750,  16000,   316750,  1200,    116750,  17000,   316750,  0x007C, 0,  3,  0x0000)
    DeclActor(10000,   4000,    116000,  1200,    10000,   5000,    116000,  0x007C, 0,  4,  0x0000)
    DeclActor(208700,  16850,   211000,  2000,    208700,  18000,   211000,  0x007C, 0,  7,  0x0000)

    ChipFrameInfo(800, 0, [0, 1, 2, 1])                          # 0
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 2
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_690",          # 00, 0
        "Function_1_6AD",          # 01, 1
        "Function_2_6F2",          # 02, 2
        "Function_3_BD6",          # 03, 3
        "Function_4_D27",          # 04, 4
        "Function_5_E78",          # 05, 5
        "Function_6_133F",         # 06, 6
        "Function_7_13B3",         # 07, 7
    ))


    def Function_0_690(): pass

    label("Function_0_690")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AC")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_690")

    label("loc_6AC")

    Return()

    # Function_0_690 end

    def Function_1_6AD(): pass

    label("Function_1_6AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C8")
    Event(0, 5)

    label("loc_6C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6D7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 6)

    label("loc_6D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F1")
    SetScenarioFlags(0x0, 0)

    label("loc_6F1")

    Return()

    # Function_1_6AD end

    def Function_2_6F2(): pass

    label("Function_2_6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_704")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_704")

    Sound(129, 1, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_71C")
    ClearScenarioFlags(0x0, 0)
    Sound(202, 0, 100, 0)

    label("loc_71C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_730")
    SetMapObjFlags(0x2, 0x4)

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 5)), scpexpr(EXPR_END)), "loc_77C")
    SetMapObjFrame(0x2, "b_in", 0x0, 0x1)
    SetMapObjFrame(0x2, "b_in2", 0x0, 0x1)
    SetMapObjFrame(0x2, "b_out", 0x0, 0x1)
    SetMapObjFrame(0x2, "b_out2", 0x0, 0x1)
    SetMapObjFrame(0x2, "b_light", 0x0, 0x1)

    label("loc_77C")

    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2F, 0x0, 0xA, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x1, 0xB, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x2, 0xC, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x3, 0xD, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x4, 0xE, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x5, 0xF, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBA")
    OP_70(0x0, 0x0)
    Jump("loc_BBE")

    label("loc_BBA")

    OP_70(0x0, 0x1E)

    label("loc_BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD1")
    OP_70(0x1, 0x0)
    Jump("loc_BD5")

    label("loc_BD1")

    OP_70(0x1, 0x1E)

    label("loc_BD5")

    Return()

    # Function_2_6F2 end

    def Function_3_BD6(): pass

    label("Function_3_BD6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD6")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_C5F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EE, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_CD1")

    label("loc_C5F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_CD1")

    Jump("loc_D1B")

    label("loc_CD6")

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

    label("loc_D1B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_BD6 end

    def Function_4_D27(): pass

    label("Function_4_D27")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E27")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5F0, 1)"), scpexpr(EXPR_END)), "loc_DB0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5F0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EE, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_E22")

    label("loc_DB0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5F0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5F0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E22")

    Jump("loc_E6C")

    label("loc_E27")

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

    label("loc_E6C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_D27 end

    def Function_5_E78(): pass

    label("Function_5_E78")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("monster/ch80250.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA2")
    LoadChrToIndex("chr/ch00050.itc", 0x1F)

    label("loc_EA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBA")
    LoadChrToIndex("chr/ch00150.itc", 0x1F)

    label("loc_EBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED2")
    LoadChrToIndex("chr/ch00250.itc", 0x1F)

    label("loc_ED2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EEA")
    LoadChrToIndex("chr/ch00350.itc", 0x1F)

    label("loc_EEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F02")
    LoadChrToIndex("chr/ch02950.itc", 0x1F)

    label("loc_F02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F1A")
    LoadChrToIndex("chr/ch03150.itc", 0x1F)

    label("loc_F1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F32")
    LoadChrToIndex("chr/ch03250.itc", 0x1F)

    label("loc_F32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F4A")
    LoadChrToIndex("chr/ch00950.itc", 0x1F)

    label("loc_F4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F62")
    LoadChrToIndex("chr/ch00050.itc", 0x20)

    label("loc_F62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F7A")
    LoadChrToIndex("chr/ch00150.itc", 0x20)

    label("loc_F7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F92")
    LoadChrToIndex("chr/ch00250.itc", 0x20)

    label("loc_F92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FAA")
    LoadChrToIndex("chr/ch00350.itc", 0x20)

    label("loc_FAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FC2")
    LoadChrToIndex("chr/ch02950.itc", 0x20)

    label("loc_FC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FDA")
    LoadChrToIndex("chr/ch03150.itc", 0x20)

    label("loc_FDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FF2")
    LoadChrToIndex("chr/ch03250.itc", 0x20)

    label("loc_FF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_100A")
    LoadChrToIndex("chr/ch00950.itc", 0x20)

    label("loc_100A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1022")
    LoadChrToIndex("chr/ch00050.itc", 0x21)

    label("loc_1022")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_103A")
    LoadChrToIndex("chr/ch00150.itc", 0x21)

    label("loc_103A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1052")
    LoadChrToIndex("chr/ch00250.itc", 0x21)

    label("loc_1052")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106A")
    LoadChrToIndex("chr/ch00350.itc", 0x21)

    label("loc_106A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1082")
    LoadChrToIndex("chr/ch02950.itc", 0x21)

    label("loc_1082")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_109A")
    LoadChrToIndex("chr/ch03150.itc", 0x21)

    label("loc_109A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B2")
    LoadChrToIndex("chr/ch03250.itc", 0x21)

    label("loc_10B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10CA")
    LoadChrToIndex("chr/ch00950.itc", 0x21)

    label("loc_10CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10E2")
    LoadChrToIndex("chr/ch00050.itc", 0x22)

    label("loc_10E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10FA")
    LoadChrToIndex("chr/ch00150.itc", 0x22)

    label("loc_10FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1112")
    LoadChrToIndex("chr/ch00250.itc", 0x22)

    label("loc_1112")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112A")
    LoadChrToIndex("chr/ch00350.itc", 0x22)

    label("loc_112A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1142")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_1142")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_115A")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_115A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1172")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_1172")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_118A")
    LoadChrToIndex("chr/ch00950.itc", 0x22)

    label("loc_118A")

    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 105000, 18000, 310000, 180)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 115000, 18000, 310000, 180)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0x0, 112000, 16000, 303500, 0)
    SetChrPos(0x1, 110000, 16000, 303500, 0)
    SetChrPos(0x2, 112000, 16000, 302000, 0)
    SetChrPos(0x3, 110000, 16000, 302000, 0)
    OP_68(110610, 21000, 309030, 0)
    MoveCamera(34, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(28560, 0)
    OP_68(110610, 18000, 309030, 4000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12F4")
    Sound(540, 0, 50, 0)

    label("loc_12F4")

    SetChrChipByIndex(0x0, 0x1F)
    SetChrChipByIndex(0x1, 0x20)
    SetChrChipByIndex(0x2, 0x21)
    SetChrChipByIndex(0x3, 0x22)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    OP_0D()
    Sleep(1000)
    Battle("BattleInfo_5CC", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x22, 0)
    NewScene("m2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_E78 end

    def Function_6_133F(): pass

    label("Function_6_133F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, 110610, 16000, 306080, 0)
    SetChrPos(0x1, 110610, 16000, 306080, 0)
    SetChrPos(0x2, 110610, 16000, 306080, 0)
    SetChrPos(0x3, 110610, 16000, 306080, 0)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "封印が解除された。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x5)
    Return()

    # Function_6_133F end

    def Function_7_13B3(): pass

    label("Function_7_13B3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 5)), scpexpr(EXPR_END)), "loc_13EA")
    TalkBegin(0xFF)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_1575")

    label("loc_13EA")

    EventBegin(0x1)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座の上に宝珠が置かれている。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "宝珠を手に取る\x01",      # 0
            "やめておく\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156E")
    Fade(500)
    SetChrPos(0x0, 206500, 16000, 211000, 90)
    SetChrPos(0x1, 205500, 16000, 210000, 90)
    SetChrPos(0x2, 205500, 16000, 212000, 90)
    SetChrPos(0x3, 204500, 16000, 211000, 90)
    OP_68(207290, 16600, 210610, 0)
    MoveCamera(42, 31, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(200)
    SetMapObjFrame(0x2, "b_in", 0x0, 0x1)
    SetMapObjFrame(0x2, "b_in2", 0x0, 0x1)
    SetMapObjFrame(0x2, "b_out", 0x0, 0x1)
    SetMapObjFrame(0x2, "b_out2", 0x0, 0x1)
    SetMapObjFrame(0x2, "b_light", 0x0, 0x1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x33E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1B7, 5)
    OP_E2(0x2)

    label("loc_156E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_1575")

    Return()

    # Function_7_13B3 end

    SaveToFile()

Try(main)
