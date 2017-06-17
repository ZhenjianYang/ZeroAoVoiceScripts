from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "マルコーニ会長",         # 1
        "マフィア",               # 2
        "マフィア",               # 3
        "マフィア",               # 4
        "シームーン",             # 5
        "シームーン",             # 6
        "bm3020",                 # 7
        "bm3020",                 # 8
        "bm3020",                 # 9
    ))

    ATBonus("ATBonus_38C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_3D46", 0,   4,   12,  0,   24,  8,   16)
    Sepith("Sepith_3D56", 2,   0,   4,   14,  16,  9,   18)

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
        "BattleInfo_534", 0x0000, 40, 6, 60, 4, 1, 40, 0, "bm3020", "Sepith_3D46", 60, 25, 10, 5,
        (
            ("ms71100.dat", "ms71100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7402", "ed7403", "ATBonus_38C"),
        )
    )

    BattleInfo(
        "BattleInfo_46C", 0x0000, 40, 6, 60, 4, 1, 50, 0, "bm3020", "Sepith_3D56", 60, 25, 10, 5,
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
        "Function_5_DA8",          # 05, 5
        "Function_6_EF5",          # 06, 6
        "Function_7_1108",         # 07, 7
        "Function_8_1279",         # 08, 8
        "Function_9_148C",         # 09, 9
        "Function_10_151B",        # 0A, 10
        "Function_11_1DC4",        # 0B, 11
        "Function_12_1EB1",        # 0C, 12
        "Function_13_1F37",        # 0D, 13
        "Function_14_1FFF",        # 0E, 14
        "Function_15_210A",        # 0F, 15
        "Function_16_225A",        # 10, 16
        "Function_17_23AA",        # 11, 17
        "Function_18_23E2",        # 12, 18
        "Function_19_2532",        # 13, 19
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D57")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_CE0")
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
    SetScenarioFlags(0x11B, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_D52")

    label("loc_CE0")

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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D52")

    Jump("loc_D9C")

    label("loc_D57")

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

    label("loc_D9C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C5B end

    def Function_5_DA8(): pass

    label("Function_5_DA8")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA4")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_E2D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
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
    SetScenarioFlags(0x11B, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_E9F")

    label("loc_E2D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E9F")

    Jump("loc_EE9")

    label("loc_EA4")

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

    label("loc_EE9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_DA8 end

    def Function_6_EF5(): pass

    label("Function_6_EF5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C2")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x77, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF0")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F4E():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_F4E)

    def lambda_F68():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_F68)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_FD1"),
        (2, "loc_FE0"),
        (1, "loc_FED"),
        (SWITCH_DEFAULT, "loc_FF0"),
    )


    label("loc_FD1")

    SetScenarioFlags(0x77, 1)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_FF0")

    label("loc_FE0")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_FED")

    OP_B7(0x0)
    Return()

    label("loc_FF0")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5EE, 1)"), scpexpr(EXPR_END)), "loc_104D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5EE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11B, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_10BD")

    label("loc_104D")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5EE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5EE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_10BD")

    Jump("loc_10FC")

    label("loc_10C2")

    FadeToDark(300, 0, 100)

    #A0010
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

    label("loc_10FC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_EF5 end

    def Function_7_1108(): pass

    label("Function_7_1108")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1242")
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
    SetScenarioFlags(0x11D, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1267")

    label("loc_1242")


    #A0012
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

    label("loc_1267")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1108 end

    def Function_8_1279(): pass

    label("Function_8_1279")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1446")
    Sound(14, 0, 100, 0)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x77, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1374")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_12D2():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12D2)

    def lambda_12EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_12EC)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_1355"),
        (2, "loc_1364"),
        (1, "loc_1371"),
        (SWITCH_DEFAULT, "loc_1374"),
    )


    label("loc_1355")

    SetScenarioFlags(0x77, 2)
    OP_70(0xC, 0x1E)
    Sleep(500)
    Jump("loc_1374")

    label("loc_1364")

    OP_70(0xC, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1371")

    OP_B7(0x0)
    Return()

    label("loc_1374")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x443, 1)"), scpexpr(EXPR_END)), "loc_13D1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x443),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11D, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1441")

    label("loc_13D1")

    FadeToDark(300, 0, 100)

    #A0015
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x443),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x443),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xC, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1441")

    Jump("loc_1480")

    label("loc_1446")

    FadeToDark(300, 0, 100)

    #A0016
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

    label("loc_1480")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1279 end

    def Function_9_148C(): pass

    label("Function_9_148C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 4)), scpexpr(EXPR_END)), "loc_1514")

    #C0017
    ChrTalk(
        0x8,
        (
            "#3005Fし、信じてくれ……\x01",
            "あの捜査官を殺ったのは\x01",
            "ワシらではない！\x02\x03",

            "#3007Fヨアヒムだ！\x01",
            "全てはヨアヒムの仕業なのだ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1517")

    label("loc_1514")

    Call(0, 10)

    label("loc_1517")

    TalkEnd(0xFE)
    Return()

    # Function_9_148C end

    def Function_10_151B(): pass

    label("Function_10_151B")

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
            "#0003F……マルコーニ会長。\x01",
            "一応、聞いておきます。\x02\x03",

            "#0001Fこれに見覚えはありますか？\x02",
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
            "#3005F#11P警察のバッジ……？\x01",
            "どこかで見たような……\x02\x03",

            "#3001F！！！\x02\x03",

            "#3007Fそ、それはあの忌々しい捜査官の……！\x02\x03",

            "ど、どうしてお前たちが\x01",
            "それを持っている！？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #C0020
    ChrTalk(
        0x101,
        (
            "#0006F……それはこちらの台詞です。\x02\x03",

            "#0001Fこのバッジを持っていた捜査官……\x01",
            "やはり貴方たちが始末したんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#3002F#11Pさ、さあな。\x01",
            "何のことやらサッパリ……\x02\x03",

            "#3004Fフン、お前たちも調子に乗っていると\x01",
            "そいつと同じ目に遭うかもしれんぞ？\x02\x03",

            "#3002F少しは自分たちの立場を弁#2Rわきま#えて\x01",
            "我々に配慮を──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0022
    ChrTalk(
        0x101,
        "#0010F……………………（ギッ）\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#3005F#11P……ひっ……\x01",
            "分かった、正直に言う！\x02\x03",

            "あのガイという捜査官を\x01",
            "殺ったのはワシらではない！\x02\x03",

            "#3003Fた、確かに色々嗅ぎ回って\x01",
            "恐ろしく厄介な相手だったから\x01",
            "始末するつもりだったが……\x02\x03",

            "#3007Fその前に、どこぞの連中に\x01",
            "先に殺られてしまったんだ！\x02\x03",

            "そのバッジはウチの人間が\x01",
            "現場から持ち去った物にすぎん！\x02",
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
        "#0108F#6P本当……なのかしら？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        (
            "#0203F#5P……嘘を言っている気配は\x01",
            "感じられません。\x02\x03",

            "#0211Fまあ、そう装っている\x01",
            "だけかもしれませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0306F#5Pしかし、それが本当なら\x01",
            "他人が殺った標的の遺品を手に入れて\x01",
            "悦に入ってたってことか。\x02\x03",

            "#0301Fなかなか良い趣味してんな、\x01",
            "ルバーチェの会長さんよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#3001F#11Pぐうっ……\x02\x03",

            "#3003Fと、とにかく本当に\x01",
            "ワシらが殺ったのではない！\x02\x03",

            "#3005Fそ、そうだ……\x01",
            "ヨアヒムが殺ったに違いない！\x02\x03",

            "#3000Fあの捜査官、ワシらの他に\x01",
            "ヨアヒムのことも\x01",
            "探っていたそうだからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#0005F兄貴が……？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x108,
        (
            "#0903Fそんな昔から今回の黒幕を\x01",
            "マークしていたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x107,
        (
            "#0802Fロイド君のお兄さん、\x01",
            "すっごく優秀だったのね……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#0008F………………………………\x02\x03",

            "#0006Fいずれにせよ、その辺りの真偽は\x01",
            "黒幕を追い詰めれば判ることだ。\x02\x03",

            "#0000F……時間を取らせた。\x01",
            "みんな、先に進もう。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#0100F#6Pええ……！\x02",
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

    # Function_10_151B end

    def Function_11_1DC4(): pass

    label("Function_11_1DC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E08")

    #C0034
    ChrTalk(
        0xFE,
        (
            "操られた仲間は……\x01",
            "若頭は無事なんだろうな！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1E08")


    #C0035
    ChrTalk(
        0xFE,
        "こんな筈じゃなかったんだ。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "あの薬を使えば\x01",
            "黒月だろうが楽に潰せる。\x01",
            "ミラだってたんまり入る。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "それが……クソ！！\x01",
            "やっぱ考えが\x01",
            "甘かったんじゃねえか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1EAD")

    TalkEnd(0xFE)
    Return()

    # Function_11_1DC4 end

    def Function_12_1EB1(): pass

    label("Function_12_1EB1")

    TalkBegin(0xFE)

    #C0038
    ChrTalk(
        0xFE,
        (
            "いくらルバーチェとはいえ\x01",
            "やりすぎだったかもな……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "ここから出られたとしても……\x01",
            "俺たちこの先も\x01",
            "やっていけんのか……？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1EB1 end

    def Function_13_1F37(): pass

    label("Function_13_1F37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F71")

    #C0040
    ChrTalk(
        0xFE,
        (
            "若頭……\x01",
            "どうしてらっしゃるんだ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFB")

    label("loc_1F71")


    #C0041
    ChrTalk(
        0xFE,
        (
            "若頭は最初から\x01",
            "反対しておられたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "ヤクに手をだすと\x01",
            "ろくなことがねえってな……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "……全て若頭の\x01",
            "言うとおりだったぜ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1FFB")

    TalkEnd(0xFE)
    Return()

    # Function_13_1F37 end

    def Function_14_1FFF(): pass

    label("Function_14_1FFF")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0044
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20EC")
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

    label("loc_20EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2108")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2108")

    Return()

    # Function_14_1FFF end

    def Function_15_210A(): pass

    label("Function_15_210A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 0)), scpexpr(EXPR_END)), "loc_214F")
    TalkBegin(0xFF)
    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにレバーは下りている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_2259")

    label("loc_214F")

    EventBegin(0x1)

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レバーがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2252")
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

    label("loc_2252")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_2259")

    Return()

    # Function_15_210A end

    def Function_16_225A(): pass

    label("Function_16_225A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 1)), scpexpr(EXPR_END)), "loc_229F")
    TalkBegin(0xFF)
    SetChrName("")

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにレバーは下りている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_23A9")

    label("loc_229F")

    EventBegin(0x1)

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レバーがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A2")
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

    label("loc_23A2")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_23A9")

    Return()

    # Function_16_225A end

    def Function_17_23AA(): pass

    label("Function_17_23AA")

    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにレバーは下りている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    # Function_17_23AA end

    def Function_18_23E2(): pass

    label("Function_18_23E2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 2)), scpexpr(EXPR_END)), "loc_2427")
    TalkBegin(0xFF)
    SetChrName("")

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにレバーは下りている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_2531")

    label("loc_2427")

    EventBegin(0x1)

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レバーがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_252A")
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

    label("loc_252A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_2531")

    Return()

    # Function_18_23E2 end

    def Function_19_2532(): pass

    label("Function_19_2532")

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
        "#5P#0001Fここも牢屋か……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#5P#0108Fこちらは誰も\x01",
            "いないみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x10E, 0x1F4)

    #C0054
    ChrTalk(
        0x103,
        "#0211F#11Pいえ──\x02",
    )

    CloseMessageWindow()

    #N0055
    NpcTalk(
        0x8,
        "男の声",
        "だ、誰かいるのか……！？\x02",
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

    def lambda_27C0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27C0)
    Sleep(50)

    def lambda_27D0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_27D0)
    Sleep(50)

    def lambda_27E0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_27E0)
    Sleep(50)

    def lambda_27F0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_27F0)
    Sleep(50)

    def lambda_2800():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2800)
    OP_6F(0x79)

    #C0056
    ChrTalk(
        0x101,
        "#3P#0011Fマルコーニ会長……！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x107,
        (
            "#0805Fえ……\x01",
            "あの《ルバーチェ》の！？\x02",
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
            "#3005F#5Pお、お前たち\x01",
            "どこかで見たような……\x02",
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
        "#5Pお、お前らは……！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        "#5P特務支援課のガキども……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x8,
        (
            "#3007F#5Pなに……！？\x02\x03",

            "《黒の競売会#10Rシュバルツオークション#》を\x01",
            "台無しにした連中だと！？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#12P#0006F別に台無しにするつもりは\x01",
            "ありませんでしたが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2B15")

    #C0063
    ChrTalk(
        0x102,
        (
            "#0101F#12Pいずれにしても\x01",
            "自業自得ではないかと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7C")

    label("loc_2B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2B49")

    #C0064
    ChrTalk(
        0x103,
        "#12P#0211Fまあ、自業自得ですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B7C")

    label("loc_2B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2B7C")

    #C0065
    ChrTalk(
        0x104,
        "#12P#0309Fま、自業自得じゃねえのか？\x02",
    )

    CloseMessageWindow()

    label("loc_2B7C")


    #C0066
    ChrTalk(
        0x8,
        (
            "#3001F#5Pええい、黙るがいい！\x02\x03",

            "#3003Fお、お前たちのせいで\x01",
            "ワシは議長の機嫌を損ねて\x01",
            "危ない橋を渡ることに……\x02\x03",

            "#3007Fす、全ては貴様らのせいだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x107,
        "#0806F#11P物凄い責任転嫁っぷりね……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x108,
        (
            "#0901F#11Pヨアヒム氏と共謀していた訳では\x01",
            "ないと言い張るつもりですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#3007F#5Pも、もちろんだとも！\x02\x03",

            "#3003F《グノーシス》……\x01",
            "ま、まさかあんな\x01",
            "恐ろしい薬だったとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "#5Pさ、最初は潜在能力を\x01",
            "高める薬という話だった……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "#5P《黒月》の襲撃も成功して\x01",
            "皆、競い合って服用したが……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "#5P昨日の夜、服用した連中の様子が\x01",
            "全員おかしくなってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        "#5Pそ、それでこんな事に……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "#5P……それどころか……\x01",
            "化物みたいになったヤツも……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        (
            "#5Pおお女神#4Rエイドス#よ……！\x01",
            "我らの罪をお許しください……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        "#12P#0303F……なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        "#12P#0201F大方、睨んだ通りですね。\x02",
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
            "#3002F#5Pこ、これで分かったろう！\x01",
            "ワシも被害者の一人なのだ！\x02\x03",

            "とっととここを開けて\x01",
            "安全な場所に連れて──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0080
    ChrTalk(
        0x101,
        "#12P#0010F#4S──ふざけるな！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x8,
        "#3005F#5Pな……！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#12P#0010F元凶は確かにヨアヒムだろう！\x02\x03",

            "だが、あんたたちに\x01",
            "責任が無いと言わせるものか！\x02\x03",

            "市民たちに薬を流したのは\x01",
            "他ならぬあんたたちだろうが！？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        "#5Pそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#12P#0003F……その狙いも判っている。\x02\x03",

            "《グノーシス》に危険が無いか\x01",
            "市民を使ってテストしたんだろう。\x02\x03",

            "#0013Fあわよくば販売ルートを確保して、\x01",
            "抗争後には広めようとすらした……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0085
    ChrTalk(
        0x101,
        "#12P#0007F#4S違うか──！？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        "#3001F#5Pぐっ……\x02",
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
            "#5P……さすがに\x01",
            "やりすぎだったかもな……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#0103F#12P……今度ばかりは貴方がたを\x01",
            "かばう議員は現れないでしょう。\x02\x03",

            "#0101Fハルトマン議長に至っては\x01",
            "ヨアヒム氏との関係について\x01",
            "幾つもの疑惑が持たれています。\x02\x03",

            "もう後ろ盾は無くなったと\x01",
            "覚悟した方がいいでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        "#3007F#5Pぐぐぐぐぐぐ……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#12P#0306Fま、それはともかく……\x02\x03",

            "#0301Fガルシアのオッサンは\x01",
            "どうしたんだ？\x02\x03",

            "てっきり一緒に\x01",
            "捕まってるものと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "#5P……若頭は最後まで\x01",
            "ヨアヒムに抵抗していた……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "#5Pだが、化物になった仲間たちに\x01",
            "力ずくで押さえ込まれて……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        "#5Pその後は見かけていない……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        "#12P#0303Fフン……そうか。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        "#12P#0208F……ちょっと心配ですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 500)

    #C0097
    ChrTalk(
        0x107,
        (
            "#0806F#11Pうーん、確かに……\x02\x03",

            "#0801F──ねえ、ロイド君。\x02\x03",

            "この牢屋の扉、どうするつもり？\x02",
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

    def lambda_3502():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3502)
    Sleep(50)

    def lambda_3512():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3512)
    Sleep(50)

    def lambda_3522():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3522)
    Sleep(50)

    def lambda_3532():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3532)
    Sleep(50)

    def lambda_3542():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3542)
    Sleep(50)

    def lambda_3552():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3552)
    Sleep(50)

    def lambda_3562():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_3562)

    #C0098
    ChrTalk(
        0x8,
        "#3005F#5Pなっ……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x107,
        (
            "#0806F#11Pこのままにしておいたら\x01",
            "ちょっと危険な気もするし……\x02\x03",

            "#0808Fかといって扉を開けたら\x01",
            "逃げられちゃうかもしれないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#6P#0008F……ああ。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x108,
        (
            "#0903F#11P正直、難しい判断だと思う。\x02\x03",

            "#0901F僕たちは君の判断に従うよ。\x02\x03",

            "さすがに遊撃士が守るべき\x01",
            "民間人とは言いにくいからね。\x02",
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

    def lambda_3701():
        OP_95(0xFE, -16500, -54000, -108000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3701)
    Sleep(50)

    def lambda_371E():

        label("loc_371E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_371E")

    QueueWorkItem2(0x102, 2, lambda_371E)

    def lambda_3730():

        label("loc_3730")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3730")

    QueueWorkItem2(0x8, 2, lambda_3730)
    Sleep(50)

    def lambda_3745():

        label("loc_3745")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3745")

    QueueWorkItem2(0x103, 2, lambda_3745)
    Sleep(50)

    def lambda_375A():

        label("loc_375A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_375A")

    QueueWorkItem2(0x104, 2, lambda_375A)

    def lambda_376C():

        label("loc_376C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_376C")

    QueueWorkItem2(0x9, 2, lambda_376C)

    def lambda_377E():

        label("loc_377E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_377E")

    QueueWorkItem2(0xA, 2, lambda_377E)

    def lambda_3790():

        label("loc_3790")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3790")

    QueueWorkItem2(0xB, 2, lambda_3790)
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
            "ロイドはレバーを下ろした。\x07\x00\x02",
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
        "#3002F#12Pは、ははは……！\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        "おお……！\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xB,
        "お、恩に着る……！\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x103,
        "#0205Fロイドさん……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        "#0304Fやれやれ、甘いねぇ。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#0102Fふふ……仕方ないわね。\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0xFFFFD314, 0xFFFE5F34, 0x1F4)
    OP_68(-10900, -53100, -105500, 2500)

    def lambda_39C5():

        label("loc_39C5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_39C5")

    QueueWorkItem2(0x102, 2, lambda_39C5)

    def lambda_39D7():

        label("loc_39D7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_39D7")

    QueueWorkItem2(0x103, 2, lambda_39D7)

    def lambda_39E9():

        label("loc_39E9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_39E9")

    QueueWorkItem2(0x104, 2, lambda_39E9)

    def lambda_39FB():

        label("loc_39FB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_39FB")

    QueueWorkItem2(0x8, 2, lambda_39FB)

    def lambda_3A0D():

        label("loc_3A0D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3A0D")

    QueueWorkItem2(0x9, 2, lambda_3A0D)

    def lambda_3A1F():

        label("loc_3A1F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3A1F")

    QueueWorkItem2(0xA, 2, lambda_3A1F)

    def lambda_3A31():

        label("loc_3A31")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3A31")

    QueueWorkItem2(0xB, 2, lambda_3A31)

    def lambda_3A43():
        OP_95(0xFE, -11500, -54000, -106700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A43)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)

    def lambda_3A79():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3A79)
    EndChrThread(0xB, 0x2)
    OP_6F(0x1)
    OP_93(0x101, 0x0, 0x1F4)

    #C0110
    ChrTalk(
        0x101,
        (
            "#12P#0006F……あくまで緊急措置だ。\x02\x03",

            "#0001Fそれに、丸腰で脱出できるほど\x01",
            "この遺跡の魔獣は生易しくはない。\x02\x03",

            "大人しく警察の救出を待った方が\x01",
            "身のためだと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#3001F#5Pフ、フン……\x01",
            "ワシに指図をするな！\x02\x03",

            "#3007Fこれで貴様らも用済みだ！\x01",
            "とっとと行ってしまえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        "#0103F#11P……行きましょう。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(150)

    #C0113
    ChrTalk(
        0x101,
        "#6P#0013Fああ……先を急ごう！\x02",
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

    # Function_19_2532 end

    SaveToFile()

Try(main)
