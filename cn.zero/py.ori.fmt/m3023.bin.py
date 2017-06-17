from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m3023.bin",                # FileName
        "m3023",                    # MapName
        "m3023",                    # Location
        0x007D,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 125, 0, 2, 0, 3],
    )

    BuildStringList((
        "m3023",                  # 0
        "马尔克尼会长",           # 1
        "黑手党",                 # 2
        "黑手党",                 # 3
        "黑手党",                 # 4
        "海洋月魔",               # 5
        "海洋月魔",               # 6
        "bm3020",                 # 7
        "bm3020",                 # 8
        "bm3020",                 # 9
    ))

    ATBonus("ATBonus_38C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_3AF1", 0,   4,   12,  0,   24,  8,   16)
    Sepith("Sepith_3B01", 2,   0,   4,   14,  16,  9,   18)

    MonsterBattlePostion("MonsterBattlePostion_3CC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_450", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_454", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_458", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_45C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_460", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_464", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 8, 14, 180)

    # monster count: 4

    BattleInfo(
        "BattleInfo_534", 0x0000, 40, 6, 60, 4, 1, 40, 0, "bm3020", "Sepith_3AF1", 60, 25, 10, 5,
        (
            ("ms71100.dat", "ms71100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
        )
    )

    BattleInfo(
        "BattleInfo_46C", 0x0000, 40, 6, 60, 4, 1, 50, 0, "bm3020", "Sepith_3B01", 60, 25, 10, 5,
        (
            ("ms77100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
            ("ms77100.dat", "ms77100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
            ("ms77100.dat", "ms71100.dat", "ms77100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
            ("ms77100.dat", "ms77100.dat", "ms71100.dat", "ms77100.dat", 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_5FC", 0x0010, 40, 6, 60, 4, 1, 0, 0, "bm3020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68400.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", 0, "ms75700.dat", 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch06200.itc",                   # 00
        "chr/ch36000.itc",                   # 01
        "chr/ch36100.itc",                   # 02
        "chr/ch36200.itc",                   # 03
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
        "monster/ch77150.itc",               # 10
        "monster/ch77150.itc",               # 11
        "monster/ch71150.itc",               # 12
        "monster/ch71151.itc",               # 13
        "monster/ch68450.itc",               # 14
        "monster/ch68450.itc",               # 15
    ))

    DeclNpc(-10899,  -54000,  -104500, 180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-12000,  -54000,  -103599, 180,  261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-9800,   -54000,  -103599, 180,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-10899,  -54000,  -102699, 180,  261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-10250,  -52500,  -116500, 0,    484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-148250, -55500,  -46250,  0,    484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(14110,   2110,    -54000,  0x1010000,    "BattleInfo_534", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-161850, -18710,  -54000,  0x1010000,    "BattleInfo_46C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(161530,  -121810, -54000,  0x1010000,    "BattleInfo_46C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(205280,  -121920, -60000,  0x1010000,    "BattleInfo_534", 0,   18,  0xFFFF, 2,  3)

    DeclActor(31500,   -54000,  1500,    1200,    31500,   -53000,  1500,    0x007C, 0,  4,  0x0000)
    DeclActor(-161500, -54000,  -47750,  1200,    -161500, -53000,  -47750,  0x007C, 0,  5,  0x0000)
    DeclActor(-10250,  -54000,  -116500, 1200,    -10250,  -53000,  -116500, 0x007C, 0,  6,  0x0000)
    DeclActor(28000,   -54000,  -101500, 1200,    28000,   -53000,  -101500, 0x007C, 0,  7,  0x0000)
    DeclActor(-148250, -57000,  -46250,  1200,    -148250, -56000,  -46250,  0x007C, 0,  8,  0x0000)
    DeclActor(19500,   -54000,  -106400, 1200,    19500,   -53000,  -106400, 0x007C, 0,  15, 0x0000)
    DeclActor(6750,    -54000,  -114350, 1200,    6750,    -53000,  -114350, 0x007C, 0,  16, 0x0000)
    DeclActor(-16500,  -54000,  -106400, 1200,    -16500,  -53000,  -106400, 0x007C, 0,  17, 0x0000)
    DeclActor(158250,  -54000,  -98400,  1200,    158250,  -53000,  -98400,  0x007C, 0,  18, 0x0000)
    DeclActor(233500,  -60000,  -121500, 1200,    233500,  -58500,  -121500, 0x007C, 0,  14, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3

    ScpFunction((
        "Function_0_6C0",          # 00, 0
        "Function_1_778",          # 01, 1
        "Function_2_794",          # 02, 2
        "Function_3_7FC",          # 03, 3
        "Function_4_C5B",          # 04, 4
        "Function_5_D91",          # 05, 5
        "Function_6_EC7",          # 06, 6
        "Function_7_10C1",         # 07, 7
        "Function_8_1224",         # 08, 8
        "Function_9_141E",         # 09, 9
        "Function_10_149F",        # 0A, 10
        "Function_11_1CBE",        # 0B, 11
        "Function_12_1D9F",        # 0C, 12
        "Function_13_1E15",        # 0D, 13
        "Function_14_1EDB",        # 0E, 14
        "Function_15_1FCE",        # 0F, 15
        "Function_16_2108",        # 10, 16
        "Function_17_2242",        # 11, 17
        "Function_18_2272",        # 12, 18
        "Function_19_23AC",        # 13, 19
    ))


    def Function_0_6C0(): pass

    label("Function_0_6C0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_700"),
        (1, "loc_70C"),
        (2, "loc_718"),
        (3, "loc_724"),
        (4, "loc_730"),
        (5, "loc_73C"),
        (6, "loc_748"),
        (SWITCH_DEFAULT, "loc_754"),
    )


    label("loc_700")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_70C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_718")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_724")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_730")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_73C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_748")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_754")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_760")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_777")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_777")

    Return()

    # Function_0_6C0 end

    def Function_1_778(): pass

    label("Function_1_778")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_793")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_778")

    label("loc_793")

    Return()

    # Function_1_778 end

    def Function_2_794(): pass

    label("Function_2_794")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AE")
    Event(0, 19)

    label("loc_7AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 2)), scpexpr(EXPR_END)), "loc_7FB")
    SetChrPos(0x8, 4300, -54000, -106450, 225)
    SetChrPos(0x9, 5080, -54000, -108260, 180)
    SetChrPos(0xA, 6480, -54000, -109660, 315)
    SetChrPos(0xB, 4250, -54000, -110050, 45)

    label("loc_7FB")

    Return()

    # Function_2_794 end

    def Function_3_7FC(): pass

    label("Function_3_7FC")

    ClearMapObjFlags(0x6, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 0)), scpexpr(EXPR_END)), "loc_818")
    OP_70(0x7, 0x1E)
    OP_70(0x6, 0x1E)
    Jump("loc_820")

    label("loc_818")

    OP_70(0x7, 0x0)
    OP_70(0x6, 0x0)

    label("loc_820")

    ClearMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 1)), scpexpr(EXPR_END)), "loc_83C")
    OP_70(0x8, 0x1E)
    OP_70(0x4, 0x1E)
    Jump("loc_844")

    label("loc_83C")

    OP_70(0x8, 0x0)
    OP_70(0x4, 0x0)

    label("loc_844")

    ClearMapObjFlags(0x5, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 2)), scpexpr(EXPR_END)), "loc_860")
    OP_70(0x9, 0x1E)
    OP_70(0x5, 0x32)
    Jump("loc_868")

    label("loc_860")

    OP_70(0x9, 0x0)
    OP_70(0x5, 0x0)

    label("loc_868")

    ClearMapObjFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 2)), scpexpr(EXPR_END)), "loc_884")
    OP_70(0xA, 0x1E)
    OP_70(0xB, 0x1E)
    Jump("loc_88C")

    label("loc_884")

    OP_70(0xA, 0x0)
    OP_70(0xB, 0x0)

    label("loc_88C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8AF")
    SetMapFlags(0x2000)
    OP_E0(0x0)
    Jump("loc_8B4")

    label("loc_8AF")

    ClearMapFlags(0x2000)

    label("loc_8B4")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -150000, -55000, -4000, 5000, 2000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, -150000, -55000, -17000, 5000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 7)), scpexpr(EXPR_END)), "loc_911")
    SetMapObjFrame(0xFF, "mizu1", 0x2, "low")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    Jump("loc_927")

    label("loc_911")

    SetMapObjFrame(0xFF, "mizu1", 0x2, "high")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)

    label("loc_927")

    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFA")
    OP_70(0x0, 0x0)
    Jump("loc_BFE")

    label("loc_BFA")

    OP_70(0x0, 0x1E)

    label("loc_BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C11")
    OP_70(0x1, 0x0)
    Jump("loc_C15")

    label("loc_C11")

    OP_70(0x1, 0x1E)

    label("loc_C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C28")
    OP_70(0x2, 0x0)
    Jump("loc_C2C")

    label("loc_C28")

    OP_70(0x2, 0x1E)

    label("loc_C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3F")
    OP_70(0x3, 0x0)
    Jump("loc_C43")

    label("loc_C3F")

    OP_70(0x3, 0x1E)

    label("loc_C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C56")
    OP_70(0xC, 0x0)
    Jump("loc_C5A")

    label("loc_C56")

    OP_70(0xC, 0x1E)

    label("loc_C5A")

    Return()

    # Function_3_7FC end

    def Function_4_C5B(): pass

    label("Function_4_C5B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D48")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('痊愈之药', 1)"), scpexpr(EXPR_END)), "loc_CDA")
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
    SetScenarioFlags(0x11B, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_D43")

    label("loc_CDA")

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

    label("loc_D43")

    Jump("loc_D85")

    label("loc_D48")

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

    label("loc_D85")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C5B end

    def Function_5_D91(): pass

    label("Function_5_D91")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7E")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('痊愈之药', 1)"), scpexpr(EXPR_END)), "loc_E10")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
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
    SetScenarioFlags(0x11B, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_E79")

    label("loc_E10")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E79")

    Jump("loc_EBB")

    label("loc_E7E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_EBB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_D91 end

    def Function_6_EC7(): pass

    label("Function_6_EC7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1083")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x77, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC0")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F20():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_F20)

    def lambda_F3A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_F3A)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_5FC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_FA1"),
        (2, "loc_FB0"),
        (1, "loc_FBD"),
        (SWITCH_DEFAULT, "loc_FC0"),
    )


    label("loc_FA1")

    SetScenarioFlags(0x77, 1)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_FC0")

    label("loc_FB0")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_FBD")

    OP_B7(0x0)
    Return()

    label("loc_FC0")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('邪恶胸甲', 1)"), scpexpr(EXPR_END)), "loc_1017")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '邪恶胸甲'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11B, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_107E")

    label("loc_1017")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '邪恶胸甲'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '邪恶胸甲'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_107E")

    Jump("loc_10B5")

    label("loc_1083")

    FadeToDark(300, 0, 100)

    #A0010
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

    label("loc_10B5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_EC7 end

    def Function_7_10C1(): pass

    label("Function_7_10C1")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F5")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x3, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２００\x01\x07\x02",

            "#57I水之耀晶片×２００\x01\x07\x02",

            "#58I火之耀晶片×２００\x01\x07\x02",

            "#59I风之耀晶片×２００\x01\x07\x02",

            "#60I时之耀晶片×２００\x01\x07\x02",

            "#61I空之耀晶片×２００\x01\x07\x02",

            "#62I幻之耀晶片×２００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x11D, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1212")

    label("loc_11F5")


    #A0012
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

    label("loc_1212")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_10C1 end

    def Function_8_1224(): pass

    label("Function_8_1224")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E0")
    Sound(14, 0, 100, 0)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x77, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131D")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_127D():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_127D)

    def lambda_1297():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1297)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xD, 1)
    Battle("BattleInfo_5FC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_12FE"),
        (2, "loc_130D"),
        (1, "loc_131A"),
        (SWITCH_DEFAULT, "loc_131D"),
    )


    label("loc_12FE")

    SetScenarioFlags(0x77, 2)
    OP_70(0xC, 0x1E)
    Sleep(500)
    Jump("loc_131D")

    label("loc_130D")

    OP_70(0xC, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_131A")

    OP_B7(0x0)
    Return()

    label("loc_131D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('灵光护手', 1)"), scpexpr(EXPR_END)), "loc_1374")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '灵光护手'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11D, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_13DB")

    label("loc_1374")

    FadeToDark(300, 0, 100)

    #A0015
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '灵光护手'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '灵光护手'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xC, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13DB")

    Jump("loc_1412")

    label("loc_13E0")

    FadeToDark(300, 0, 100)

    #A0016
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

    label("loc_1412")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1224 end

    def Function_9_141E(): pass

    label("Function_9_141E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 4)), scpexpr(EXPR_END)), "loc_1498")

    #C0017
    ChrTalk(
        0x8,
        (
            "#3005F相、相信我吧……\x01",
            "杀死那个搜查官的人\x01",
            "真的不是我们！\x02\x03",

            "#3007F是约亚西姆！\x01",
            "全部都是约亚西姆干的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149B")

    label("loc_1498")

    Call(0, 10)

    label("loc_149B")

    TalkEnd(0xFE)
    Return()

    # Function_9_141E end

    def Function_10_149F(): pass

    label("Function_10_149F")

    EventBegin(0x0)
    Fade(500)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis093.itp")
    OP_68(3080, -52600, -107620, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13750, 0)
    SetChrPos(0x101, 2950, -54000, -107770, 45)
    SetChrPos(0x102, 3750, -54000, -108770, 0)
    SetChrPos(0x103, 2500, -54000, -106500, 90)
    SetChrPos(0x104, 2100, -54000, -107980, 45)
    SetChrPos(0x107, 1500, -54000, -108750, 45)
    SetChrPos(0x108, 600, -54000, -108790, 45)
    SetChrPos(0x9, 6080, -54000, -108260, 180)
    SetChrPos(0xA, 7480, -54000, -109660, 315)
    SetChrPos(0xB, 5250, -54000, -110050, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x8, 0xE1, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0003F……马尔克尼会长，\x01",
            "还有件事情要问你。\x02\x03",

            "#0001F这个东西，你有印象吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #A0019
    AnonymousTalk(
        0x8,
        (
            "#3005F#11P警察的徽章……？\x01",
            "好像在什么地方见过……\x02\x03",

            "#3001F！！！\x02\x03",

            "#3007F是、是那个可憎的搜查官佩戴的……！\x02\x03",

            "为、为什么会在\x01",
            "你们的手里！？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #C0020
    ChrTalk(
        0x101,
        (
            "#0006F……那是我要说的台词。\x02\x03",

            "#0001F佩戴这枚徽章的搜查官……\x01",
            "果然是被你们杀害的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#3002F#11P这、这个嘛，\x01",
            "完全听不懂你在说些什么……\x02\x03",

            "#3004F哼，你们要是太过得意忘形，\x01",
            "说不定就会遭遇和那家伙一样的下场哦。\x02\x03",

            "#3002F你们最好还是弄清自己的立场，\x01",
            "用心照料好我们──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0022
    ChrTalk(
        0x101,
        "#0010F……………………（怒视）\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#3005F#11P……呜哇……\x01",
            "明白了，我坦白交代！\x02\x03",

            "那个叫盖伊的搜查官\x01",
            "并不是被我们杀死的！\x02\x03",

            "#3003F他、他是个喜欢到处打探，\x01",
            "令人恐惧的危险对手，所以\x01",
            "我们原本确实打算把他做掉……\x02\x03",

            "#3007F但在我们动手之前，他就被某个\x01",
            "组织的家伙们抢先一步杀死了！\x02\x03",

            "那个徽章，只是我们的人\x01",
            "从现场带回来的东西而已！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0013F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        "#0108F#6P这些……都是实话吗？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        (
            "#0203F#5P……感觉确实\x01",
            "不像在说谎。\x02\x03",

            "#0211F但也说不定\x01",
            "只是装出来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0306F#5P不过，如果这些都是真的，\x01",
            "在目标被别人抢先下手后，\x01",
            "亏你们还能捡了他的遗物暗自得意啊。\x02\x03",

            "#0301F这还真是令人大开眼界的爱好，\x01",
            "马尔克尼会长先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#3001F#11P呜……\x02\x03",

            "#3003F总、总之，那个人\x01",
            "真的不是我们杀的！\x02\x03",

            "#3005F对、对了……\x01",
            "肯定是约亚西姆杀的！\x02\x03",

            "#3000F那个搜查官，除了在\x01",
            "调查我们之外，好像\x01",
            "也在调查约亚西姆呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#0005F大哥他……？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x108,
        (
            "#0903F在那么久以前，就已经盯住\x01",
            "这次的幕后真凶了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x107,
        (
            "#0802F罗伊德的哥哥，\x01",
            "真的是个非常优秀的搜查官啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#0008F………………………………\x02\x03",

            "#0006F不管怎么说，关于这些事情的真伪，\x01",
            "只要抓住幕后黑手，就会全部真相大白了。\x02\x03",

            "#0000F……我们已经耽误了不少时间。\x01",
            "各位，继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#0100F#6P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 3390, -54000, -105640, 135)
    SetChrPos(0x9, 5080, -54000, -108260, 180)
    SetChrPos(0xA, 6480, -54000, -109660, 315)
    SetChrPos(0xB, 4250, -54000, -110050, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0xEF, 4)
    EventEnd(0x5)
    Return()

    # Function_10_149F end

    def Function_11_1CBE(): pass

    label("Function_11_1CBE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CFE")

    #C0034
    ChrTalk(
        0xFE,
        (
            "被操纵的伙伴们……\x01",
            "还有副头目都没事吧！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D9B")

    label("loc_1CFE")


    #C0035
    ChrTalk(
        0xFE,
        "不应该发生这种事啊。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "只要服用那种药物，\x01",
            "应该就能轻松击溃黑月，\x01",
            "然后赚到很多米拉才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "结果竟然……可恶啊！！\x01",
            "这种想法果然\x01",
            "还是太天真了吗！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D9B")

    TalkEnd(0xFE)
    Return()

    # Function_11_1CBE end

    def Function_12_1D9F(): pass

    label("Function_12_1D9F")

    TalkBegin(0xFE)

    #C0038
    ChrTalk(
        0xFE,
        (
            "就算是我们鲁巴彻，这下干得\x01",
            "好像也太过火了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "即使能从这里逃出去……\x01",
            "我们今后\x01",
            "还有未来可言吗……？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1D9F end

    def Function_13_1E15(): pass

    label("Function_13_1E15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E49")

    #C0040
    ChrTalk(
        0xFE,
        (
            "副头目……\x01",
            "到底怎么样了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED7")

    label("loc_1E49")


    #C0041
    ChrTalk(
        0xFE,
        (
            "副头目从最初\x01",
            "就一直持反对态度。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "他说，只要跟违禁药物扯上关系，\x01",
            "就绝对不会有什么好下场……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "……一切都和副头目\x01",
            "说的一样啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1ED7")

    TalkEnd(0xFE)
    Return()

    # Function_13_1E15 end

    def Function_14_1EDB(): pass

    label("Function_14_1EDB")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0044
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB0")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0xD, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0xD, 0x0)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xD)
    OP_71(0xD, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0xD, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1FB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FCC")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1FCC")

    Return()

    # Function_14_1EDB end

    def Function_15_1FCE(): pass

    label("Function_15_1FCE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 0)), scpexpr(EXPR_END)), "loc_200B")
    TalkBegin(0xFF)
    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉杆已经被扳下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_2107")

    label("loc_200B")

    EventBegin(0x1)

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个拉杆。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2100")
    Fade(500)
    SetChrPos(0x0, 19740, -53940, -108080, 0)
    SetChrPos(0x1, 21500, -53990, -108010, 270)
    SetChrPos(0x2, 21500, -53990, -109380, 270)
    SetChrPos(0x3, 22680, -53990, -108600, 270)
    OP_68(16410, -52910, -107880, 0)
    MoveCamera(45, 37, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27500, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    Sound(155, 0, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x6)
    Sleep(500)
    SetScenarioFlags(0xF5, 0)

    label("loc_2100")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_2107")

    Return()

    # Function_15_1FCE end

    def Function_16_2108(): pass

    label("Function_16_2108")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 1)), scpexpr(EXPR_END)), "loc_2145")
    TalkBegin(0xFF)
    SetChrName("")

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉杆已经被扳下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_2241")

    label("loc_2145")

    EventBegin(0x1)

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个拉杆。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223A")
    Fade(500)
    SetChrPos(0x0, 5090, -54000, -114250, 89)
    SetChrPos(0x1, 3700, -54000, -115420, 89)
    SetChrPos(0x2, 3700, -54000, -113640, 89)
    SetChrPos(0x3, 2700, -54000, -114250, 89)
    OP_68(6060, -53000, -116870, 0)
    MoveCamera(45, 36, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x8)
    Sound(155, 0, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    SetScenarioFlags(0xF5, 1)

    label("loc_223A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_2241")

    Return()

    # Function_16_2108 end

    def Function_17_2242(): pass

    label("Function_17_2242")

    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉杆已经被扳下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    # Function_17_2242 end

    def Function_18_2272(): pass

    label("Function_18_2272")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 2)), scpexpr(EXPR_END)), "loc_22AF")
    TalkBegin(0xFF)
    SetChrName("")

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉杆已经被扳下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_23AB")

    label("loc_22AF")

    EventBegin(0x1)

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个拉杆。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A4")
    Fade(500)
    SetChrPos(0x0, 158000, -54000, -100000, 0)
    SetChrPos(0x1, 158900, -54000, -102000, 0)
    SetChrPos(0x2, 156840, -54000, -102000, 0)
    SetChrPos(0x3, 158000, -54000, -103560, 0)
    OP_68(160990, -53000, -99920, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xA)
    Sound(155, 0, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xB)
    Sleep(500)
    SetScenarioFlags(0xF5, 2)

    label("loc_23A4")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_23AB")

    Return()

    # Function_18_2272 end

    def Function_19_23AC(): pass

    label("Function_19_23AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1500, -52900, -102000, 0)
    MoveCamera(40, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 900, -54000, -100200, 180)
    SetChrPos(0x102, 2100, -54000, -100200, 180)
    SetChrPos(0x103, 900, -54000, -98900, 180)
    SetChrPos(0x104, 2100, -54000, -98900, 180)
    SetChrPos(0x107, 4200, -54000, -99700, 180)
    SetChrPos(0x108, 3500, -54000, -99000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrPos(0x8, -10900, -54000, -104500, 90)
    SetChrPos(0x9, -12000, -54000, -103600, 90)
    SetChrPos(0xA, -9800, -54000, -103600, 90)
    SetChrPos(0xB, -10900, -54000, -102700, 90)
    OP_68(1500, -52900, -100000, 4000)
    MoveCamera(35, 35, 0, 4000)
    SetCameraDistance(20500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0052
    ChrTalk(
        0x101,
        "#5P#0001F这里也是牢房吗……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#5P#0108F这边好像\x01",
            "没关着人呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x10E, 0x1F4)

    #C0054
    ChrTalk(
        0x103,
        "#0211F#11P不──\x02",
    )

    CloseMessageWindow()

    #N0055
    NpcTalk(
        0x8,
        "男人的声音",
        "有、有人来了吗……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-10900, -52900, -103500, 3000)
    MoveCamera(35, 30, 0, 3000)
    SetCameraDistance(17500, 3000)

    def lambda_2630():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2630)
    Sleep(50)

    def lambda_2640():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2640)
    Sleep(50)

    def lambda_2650():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2650)
    Sleep(50)

    def lambda_2660():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2660)
    Sleep(50)

    def lambda_2670():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2670)
    OP_6F(0x79)

    #C0056
    ChrTalk(
        0x101,
        "#3P#0011F马尔克尼会长……！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x107,
        (
            "#0805F哎……\x01",
            "是那个『鲁巴彻』的…！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-10900, -53100, -105500, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -11500, -54000, -106700, 0)
    SetChrPos(0x102, -10300, -54000, -106700, 0)
    SetChrPos(0x103, -11500, -54000, -108000, 0)
    SetChrPos(0x104, -10300, -54000, -108000, 0)
    SetChrPos(0x107, -8500, -54000, -106800, 315)
    SetChrPos(0x108, -8400, -54000, -107800, 315)
    SetChrPos(0x8, -10900, -54000, -104500, 180)
    SetChrPos(0x9, -12000, -54000, -103600, 180)
    SetChrPos(0xA, -9800, -54000, -103600, 180)
    SetChrPos(0xB, -10900, -54000, -102700, 180)
    Sleep(500)
    SetCameraDistance(20000, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0058
    ChrTalk(
        0x8,
        (
            "#3005F#5P好、好像在什么地方\x01",
            "见过你们几个啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0059
    ChrTalk(
        0x9,
        "#5P你、你们是……！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        "#5P特别任务支援科的那些小鬼……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x8,
        (
            "#3007F#5P什么……！？\x02\x03",

            "是把『黑之竞拍会』搅黄的\x01",
            "那些家伙！？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#12P#0006F其实我们也不是\x01",
            "有意去搅局的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2952")

    #C0063
    ChrTalk(
        0x102,
        (
            "#0101F#12P再怎么说，\x01",
            "也是你们自作自受吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29BF")

    label("loc_2952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_298A")

    #C0064
    ChrTalk(
        0x103,
        "#12P#0211F不过，那是你们自作自受呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29BF")

    label("loc_298A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_29BF")

    #C0065
    ChrTalk(
        0x104,
        "#12P#0309F哈，那还不是你们自作自受吗？\x02",
    )

    CloseMessageWindow()

    label("loc_29BF")


    #C0066
    ChrTalk(
        0x8,
        (
            "#3001F#5P可恶，给我闭嘴吧！\x02\x03",

            "#3003F都、都是因为你们，\x01",
            "我才会惹恼了议长阁下，\x01",
            "迫不得已，只能挺而走险……\x02\x03",

            "#3007F全、全都是你们不好！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x107,
        "#0806F#11P推卸责任的本事可真大啊……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x108,
        (
            "#0901F#11P你是想说，\x01",
            "自己并不是约亚西姆的共犯吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#3007F#5P那、那是当然的啊！\x02\x03",

            "#3003F『真知』……\x01",
            "真、真没想到竟然是\x01",
            "那么恐怖的药物……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "#5P一、一开始只知道\x01",
            "它是可以提高潜在能力的药……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "#5P而且服用后，我们也成功袭击了『黑月』，\x01",
            "所、所以大家就都争先恐后地服用了……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "#5P结果，就在昨天晚上，服用过药物\x01",
            "的那些人都变得很奇怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        "#5P然、然后事态就演变至此……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "#5P……而且还不止如此……\x01",
            "有些人甚至变得像怪物一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        (
            "#5P噢噢，女神啊……！\x01",
            "请宽恕我们的罪行吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        "#12P#0303F……原来如此啊。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        "#12P#0201F基本上，和我们预料的一样啊。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#12P#0008F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "#3002F#5P这、这样一来，你们就明白了吧！\x01",
            "我也只是一位受害人而已！\x02\x03",

            "赶快把门打开，\x01",
            "然后把我们送到安全的地方──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0080
    ChrTalk(
        0x101,
        "#12P#0010F#4S──别开玩笑了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x8,
        "#3005F#5P什么……！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#12P#0010F元凶也许确实是约亚西姆！\x02\x03",

            "但是，难道能说你们\x01",
            "连一点责任都没有吗！\x02\x03",

            "将药物流向市民的，\x01",
            "并不是别人，就是你们吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        "#5P那、那个……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#12P#0003F……我明白你们的目的。\x02\x03",

            "你们想利用市民来做试验，\x01",
            "确认服用『真知』究竟有没有危险吧？\x02\x03",

            "#0013F如果一切顺利，就稳固贩卖渠道，\x01",
            "在争斗之后，进一步扩大销售……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0085
    ChrTalk(
        0x101,
        "#12P#0007F#4S难道不是吗──！？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        "#3001F#5P呜……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        "#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "#5P……我们也许确实是\x01",
            "做得太过分了……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#0103F#12P……这次恐怕就没有\x01",
            "议员敢挺身庇护你们了吧。\x02\x03",

            "#0101F至于哈尔特曼议长，\x01",
            "他与约亚西姆之间的关系\x01",
            "也有很多可疑之处。\x02\x03",

            "你们大概已经失去这个后盾了，\x01",
            "最好提前做好觉悟哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        "#3007F#5P呜呜呜呜呜呜呜……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#12P#0306F算了，先不说这些……\x02\x03",

            "#0301F加尔西亚那个大叔\x01",
            "现在如何了？\x02\x03",

            "本以为他肯定也一起被捕了，\x01",
            "但好像不在这里啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "#5P……副头目向约亚西姆\x01",
            "抵抗到了最后一刻……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "#5P但最后还是被那些变成怪物\x01",
            "的同伴们使用武力制服了……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        "#5P之后就再也没有见到过他……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        "#12P#0303F哼……是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        "#12P#0208F……稍微有点担心呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 500)

    #C0097
    ChrTalk(
        0x107,
        (
            "#0806F#11P嗯～确实……\x02\x03",

            "#0801F──那个，罗伊德。\x02\x03",

            "这间牢房的大门，你打算怎么处理？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_32C9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_32C9)
    Sleep(50)

    def lambda_32D9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_32D9)
    Sleep(50)

    def lambda_32E9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_32E9)
    Sleep(50)

    def lambda_32F9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_32F9)
    Sleep(50)

    def lambda_3309():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3309)
    Sleep(50)

    def lambda_3319():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3319)
    Sleep(50)

    def lambda_3329():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_3329)

    #C0098
    ChrTalk(
        0x8,
        "#3005F#5P什么……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x107,
        (
            "#0806F#11P就这么一直关着他们的话，\x01",
            "处境好像稍微有些危险……\x02\x03",

            "#0808F但如果把大门打开，\x01",
            "他们又说不定会逃跑。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#6P#0008F……嗯。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x108,
        (
            "#0903F#11P老实说，真是很难判断呢。\x02\x03",

            "#0901F我们就遵从你的判断好了。\x02\x03",

            "再怎么说，他们好像也算不上是\x01",
            "游击士所应保护的民间人士啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#6P#0003F…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_92(0x101, 0xFFFFC0B8, 0xFFFE5A20, 0x1F4)
    OP_68(-15000, -53100, -106500, 2500)

    def lambda_34B6():
        OP_95(0xFE, -16500, -54000, -108000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34B6)
    Sleep(50)

    def lambda_34D3():

        label("loc_34D3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_34D3")

    QueueWorkItem2(0x102, 2, lambda_34D3)

    def lambda_34E5():

        label("loc_34E5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_34E5")

    QueueWorkItem2(0x8, 2, lambda_34E5)
    Sleep(50)

    def lambda_34FA():

        label("loc_34FA")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_34FA")

    QueueWorkItem2(0x103, 2, lambda_34FA)
    Sleep(50)

    def lambda_350F():

        label("loc_350F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_350F")

    QueueWorkItem2(0x104, 2, lambda_350F)

    def lambda_3521():

        label("loc_3521")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3521")

    QueueWorkItem2(0x9, 2, lambda_3521)

    def lambda_3533():

        label("loc_3533")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3533")

    QueueWorkItem2(0xA, 2, lambda_3533)

    def lambda_3545():

        label("loc_3545")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3545")

    QueueWorkItem2(0xB, 2, lambda_3545)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    OP_6F(0x1)
    OP_93(0x101, 0x0, 0x1F4)
    SetChrName("")

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德拉下了拉杆。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-21500, -53100, -105000, 0)
    MoveCamera(0, 36, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(21500, 3000)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x9)
    Sound(155, 0, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0x5, 0x0, 0x32, 0x0, 0x0)
    OP_79(0x5)
    OP_6F(0x10)
    Fade(500)
    OP_68(-15000, -53100, -106500, 0)
    MoveCamera(43, 29, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0104
    ChrTalk(
        0x8,
        "#3002F#12P哈、哈哈哈……！\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        "噢噢……！\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xB,
        "多、多谢你……！\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x103,
        "#0205F罗伊德前辈……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        "#0304F哎呀呀，真是个老好人。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#0102F呵呵……没办法啊。\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0xFFFFD314, 0xFFFE5F34, 0x1F4)
    OP_68(-10900, -53100, -105500, 2500)

    def lambda_376E():

        label("loc_376E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_376E")

    QueueWorkItem2(0x102, 2, lambda_376E)

    def lambda_3780():

        label("loc_3780")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3780")

    QueueWorkItem2(0x103, 2, lambda_3780)

    def lambda_3792():

        label("loc_3792")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3792")

    QueueWorkItem2(0x104, 2, lambda_3792)

    def lambda_37A4():

        label("loc_37A4")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_37A4")

    QueueWorkItem2(0x8, 2, lambda_37A4)

    def lambda_37B6():

        label("loc_37B6")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_37B6")

    QueueWorkItem2(0x9, 2, lambda_37B6)

    def lambda_37C8():

        label("loc_37C8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_37C8")

    QueueWorkItem2(0xA, 2, lambda_37C8)

    def lambda_37DA():

        label("loc_37DA")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_37DA")

    QueueWorkItem2(0xB, 2, lambda_37DA)

    def lambda_37EC():
        OP_95(0xFE, -11500, -54000, -106700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37EC)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)

    def lambda_3822():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3822)
    EndChrThread(0xB, 0x2)
    OP_6F(0x1)
    OP_93(0x101, 0x0, 0x1F4)

    #C0110
    ChrTalk(
        0x101,
        (
            "#12P#0006F……这只是特殊情况下的紧急措施。\x02\x03",

            "#0001F而且这遗迹中的魔兽可没那么容易对付，\x01",
            "在手无寸铁的情况下很难逃脱。\x02\x03",

            "从安全角度考虑，我建议你们最好\x01",
            "老老实实待在原地，等待警察的救援哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#3001F#5P哼、哼……\x01",
            "不要对我指手划脚的！\x02\x03",

            "#3007F现在已经不需要你们了！\x01",
            "快走吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        "#0103F#11P……我们走吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(150)

    #C0113
    ChrTalk(
        0x101,
        "#6P#0013F是啊……赶快前进吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1000, -53000, -108000, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 1000, -54000, -108000, 90)
    SetChrPos(0x1, 1000, -54000, -108000, 90)
    SetChrPos(0x2, 1000, -54000, -108000, 90)
    SetChrPos(0x3, 1000, -54000, -108000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetChrPos(0x8, 4300, -54000, -106450, 225)
    SetChrPos(0x9, 5080, -54000, -108260, 180)
    SetChrPos(0xA, 6480, -54000, -109660, 315)
    SetChrPos(0xB, 4250, -54000, -110050, 45)
    SetScenarioFlags(0xE6, 2)
    OP_29(0x4F, 0x1, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_19_23AC end

    SaveToFile()

Try(main)
