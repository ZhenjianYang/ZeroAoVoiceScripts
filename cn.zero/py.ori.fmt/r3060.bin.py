from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r3060.bin",                # FileName
        "r3060",                    # MapName
        "r3060",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -62000, -2000, 40000, 0, 0, 1, 101, 0, 3, 0, 4],
    )

    BuildStringList((
        "r3060",                  # 0
        "活图腾",                 # 1
        "MapThread",              # 2
        "游击士斯克特",           # 3
        "游客",                   # 4
        "br3000",                 # 5
        "br3000",                 # 6
        "br3000",                 # 7
        "br3000",                 # 8
        "br3000",                 # 9
        "阿尔摩利卡古道方向",     # 10
    ))

    ATBonus("ATBonus_418", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2D7E", 8,   16,  0,   10,  5,   3,   0)
    Sepith("Sepith_2D86", 0,   0,   6,   17,  6,   6,   6)
    Sepith("Sepith_2D96", 7,   7,   7,   7,   7,   7,   7)
    Sepith("Sepith_2D8E", 10,  6,   2,   0,   8,   8,   8)

    MonsterBattlePostion("MonsterBattlePostion_478", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_47C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4EC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4F0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_458", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_46C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_470", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 2, 13, 180)

    # monster count: 10

    BattleInfo(
        "BattleInfo_750", 0x0000, 25, 6, 60, 8, 1, 20, 0, "br3000", "Sepith_2D7E", 30, 40, 20, 10,
        (
            ("ms69500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms69500.dat", "ms69500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms69500.dat", "ms63400.dat", "ms69500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms69500.dat", "ms64100.dat", "ms64100.dat", "ms64100.dat", 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
        )
    )

    BattleInfo(
        "BattleInfo_688", 0x0000, 25, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_2D86", 30, 40, 20, 10,
        (
            ("ms63400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
        )
    )

    BattleInfo(
        "BattleInfo_4F8", 0x0000, 25, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_2D96", 30, 40, 20, 10,
        (
            ("ms66800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms66800.dat", "ms66800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", "ms69500.dat", 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
        )
    )

    BattleInfo(
        "BattleInfo_5C0", 0x0000, 25, 6, 60, 8, 1, 10, 0, "br3000", "Sepith_2D8E", 30, 40, 20, 10,
        (
            ("ms63500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms63500.dat", "ms63500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms63500.dat", "ms63400.dat", "ms63500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms63500.dat", "ms63500.dat", "ms63400.dat", "ms63500.dat", 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_818", 0x0000, 25, 6, 60, 0, 1, 0, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63500.dat", "ms63500.dat", "ms63400.dat", "ms63500.dat", "ms63500.dat", "ms63400.dat", 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7401", "ed7403", "ATBonus_418"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch27200.itc",                   # 00
        "apl/ch50156.itc",                   # 01
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
        "monster/ch66850.itc",               # 10
        "monster/ch66851.itc",               # 11
        "monster/ch63550.itc",               # 12
        "monster/ch63550.itc",               # 13
        "monster/ch63450.itc",               # 14
        "monster/ch63450.itc",               # 15
        "monster/ch69550.itc",               # 16
        "monster/ch69550.itc",               # 17
    ))

    DeclNpc(-33919,  -1399,   2369,    0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-23600,  6000,    21239,   225,  389,  0x0, 0,   0,   0,   0,   2,   0,   8,   255,  0)
    DeclNpc(-24590,  6000,    20239,   135,  439,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)

    DeclMonster(-48580,  33400,   -2000,   0x1010000,    "BattleInfo_750", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-61000,  11790,   -2000,   0x1010000,    "BattleInfo_688", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-9170,   -11260,  6000,    0x1010000,    "BattleInfo_4F8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(990,     -1770,   6000,    0x1010000,    "BattleInfo_5C0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(12630,   -29610,  6000,    0x1010000,    "BattleInfo_688", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(24750,   -32600,  6000,    0x1010000,    "BattleInfo_750", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(46240,   -12720,  6000,    0x1010000,    "BattleInfo_4F8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-11670,  20490,   6000,    0x1010000,    "BattleInfo_688", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(25610,   11790,   14000,   0x1010000,    "BattleInfo_5C0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(51790,   19370,   14000,   0x1010000,    "BattleInfo_750", 0,   22,  0xFFFF, 6,  7)

    DeclEvent(0x0000, 0, 11,  -28.5,                 10.4399995803833,      5.0,                   225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   9.5,                   -1.0440000295639038,   -0.7142857313156128,   1.0])
    DeclEvent(0x0000, 0, 10,  79.0,                  13.75,                 17.0,                  1156.0,                [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.05882353335618973,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   -19.75,                -0.8088235855102539,   -2.4285714626312256,   1.0])

    DeclActor(68000,   14100,   21000,   1200,    68000,   15100,   21000,   0x007C, 0,  5,  0x0000)
    DeclActor(-33920,  -1900,   2370,    1200,    -33920,  -900,    2370,    0x007C, 0,  6,  0x0000)
    DeclActor(50000,   6100,    -10000,  1200,    50000,   7100,    -10000,  0x007C, 0,  7,  0x0000)
    DeclActor(80450,   18000,   13990,   1200,    80450,   19000,   13990,   0x007C, 0,  12, 0x0000)

    PlaceName(-84.0, 0.0, 48.0, 0x0000, 0x0000, "阿尔摩利卡古道方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_8F0",          # 00, 0
        "Function_1_90F",          # 01, 1
        "Function_2_989",          # 02, 2
        "Function_3_A41",          # 03, 3
        "Function_4_A6F",          # 04, 4
        "Function_5_F0F",          # 05, 5
        "Function_6_1045",         # 06, 6
        "Function_7_123F",         # 07, 7
        "Function_8_1375",         # 08, 8
        "Function_9_13CA",         # 09, 9
        "Function_10_13DF",        # 0A, 10
        "Function_11_182D",        # 0B, 11
        "Function_12_1DAC",        # 0C, 12
    ))


    def Function_0_8F0(): pass

    label("Function_0_8F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_8F0")

    label("loc_90E")

    Return()

    # Function_0_8F0 end

    def Function_1_90F(): pass

    label("Function_1_90F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 1)), scpexpr(EXPR_END)), "loc_988")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_988")
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(131, 1, 100, 0)
    Sleep(1000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
    StopEffect(0x0, 0x2)
    OP_24(0x83)
    ClearScenarioFlags(0xBA, 1)
    Jump("loc_988")

    label("loc_988")

    Return()

    # Function_1_90F end

    def Function_2_989(): pass

    label("Function_2_989")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_9C9"),
        (1, "loc_9D5"),
        (2, "loc_9E1"),
        (3, "loc_9ED"),
        (4, "loc_9F9"),
        (5, "loc_A05"),
        (6, "loc_A11"),
        (SWITCH_DEFAULT, "loc_A1D"),
    )


    label("loc_9C9")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A29")

    label("loc_9D5")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A29")

    label("loc_9E1")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A29")

    label("loc_9ED")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A29")

    label("loc_9F9")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A29")

    label("loc_A05")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A29")

    label("loc_A11")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A29")

    label("loc_A1D")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A29")

    label("loc_A29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A40")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A29")

    label("loc_A40")

    Return()

    # Function_2_989 end

    def Function_3_A41(): pass

    label("Function_3_A41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A52")
    Jump("loc_A6E")

    label("loc_A52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_A6E")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_A6E")

    Return()

    # Function_3_A41 end

    def Function_4_A6F(): pass

    label("Function_4_A6F")

    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1E")
    OP_70(0x0, 0x0)
    Jump("loc_E22")

    label("loc_E1E")

    OP_70(0x0, 0x1E)

    label("loc_E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E35")
    OP_70(0x1, 0x0)
    Jump("loc_E39")

    label("loc_E35")

    OP_70(0x1, 0x1E)

    label("loc_E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4C")
    OP_70(0x2, 0x0)
    Jump("loc_E50")

    label("loc_E4C")

    OP_70(0x2, 0x1E)

    label("loc_E50")

    LoadEffect(0x0, "map/mpr3000.eff")
    BeginChrThread(0x9, 0, 0, 1)
    OP_65(0x3, 0x1)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E89")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_E89")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E9F")
    Jump("loc_EC3")

    label("loc_E9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_EB1")
    Jump("loc_EC3")

    label("loc_EB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_EC3")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_ED1")
    Jump("loc_F0E")

    label("loc_ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_F0E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EEB")
    Jump("loc_F0E")

    label("loc_EEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_EFD")
    Jump("loc_F0E")

    label("loc_EFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_F0E")
    OP_66(0x3, 0x1)

    label("loc_F0E")

    Return()

    # Function_4_A6F end

    def Function_5_F0F(): pass

    label("Function_5_F0F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FFC")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('中回复药', 1)"), scpexpr(EXPR_END)), "loc_F8E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x106, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_FF7")

    label("loc_F8E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_FF7")

    Jump("loc_1039")

    label("loc_FFC")

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

    label("loc_1039")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F0F end

    def Function_6_1045(): pass

    label("Function_6_1045")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1201")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_113E")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_109E():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_109E)

    def lambda_10B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_10B8)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_818", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_111F"),
        (2, "loc_112E"),
        (1, "loc_113B"),
        (SWITCH_DEFAULT, "loc_113E"),
    )


    label("loc_111F")

    SetScenarioFlags(0x75, 4)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_113E")

    label("loc_112E")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_113B")

    OP_B7(0x0)
    Return()

    label("loc_113E")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('金耀珠', 1)"), scpexpr(EXPR_END)), "loc_1195")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x95),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x106, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_11FC")

    label("loc_1195")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x95),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x95),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_11FC")

    Jump("loc_1233")

    label("loc_1201")

    FadeToDark(300, 0, 100)

    #A0007
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

    label("loc_1233")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1045 end

    def Function_7_123F(): pass

    label("Function_7_123F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132C")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('土人偶', 1)"), scpexpr(EXPR_END)), "loc_12BE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x106, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1327")

    label("loc_12BE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1327")

    Jump("loc_1369")

    label("loc_132C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_1369")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_123F end

    def Function_8_1375(): pass

    label("Function_8_1375")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xA,
        (
            "我打算再照顾一下\x01",
            "这位女性。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "你们先去前方搜索吧，\x01",
            "稍后我一定追上去。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1375 end

    def Function_9_13CA(): pass

    label("Function_9_13CA")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xFE,
        "呜呜……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_13CA end

    def Function_10_13DF(): pass

    label("Function_10_13DF")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    OP_68(76250, 21000, 17830, 0)
    MoveCamera(78, 8, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 80450, 18000, 13220, 45)
    SetChrPos(0x102, 80450, 18000, 12220, 45)
    SetChrPos(0x103, 80450, 18000, 14220, 45)
    SetChrPos(0x104, 80450, 18000, 15220, 45)
    SetCameraDistance(20000, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0014
    ChrTalk(
        0x101,
        (
            "#12P#N#0005F那座遗迹是……？\x01",
            "好像很大呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0015
    ChrTalk(
        0x102,
        (
            "#12P#N#0103F我记得……\x01",
            "这座遗迹叫做『太阳堡垒』。\x02\x03",

            "#0101F详细情况不太清楚……\x01",
            "不过，据说是五百多年以前就存在的遗迹。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0016
    ChrTalk(
        0x104,
        (
            "#12P#N#0305F不愧是『堡垒』，\x01",
            "建造得真坚固啊。\x02\x03",

            "#0303F在中世纪的战争时也曾使用过吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0017
    ChrTalk(
        0x103,
        "#12P#N#0205F………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x101, 0x103, 500)

    #C0018
    ChrTalk(
        0x101,
        "#12P#0005F#N……缇欧，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_15E1():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15E1)
    Sleep(50)

    def lambda_15F1():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15F1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0019
    ChrTalk(
        0x103,
        (
            "#12P#0208F#N不……没什么。\x02\x03",

            "#0200F只是觉得从遗迹那边\x01",
            "传来了奇怪的感觉……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    def lambda_169E():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_169E)

    def lambda_16AB():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16AB)

    def lambda_16B8():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16B8)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x101,
        "#12P#0005F#N奇怪的感觉……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0021
    ChrTalk(
        0x104,
        (
            "#12P#0305F#N唔……\x01",
            "那里看上去好像只是个普通的堡垒遗迹……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0022
    ChrTalk(
        0x103,
        (
            "#12P#0206F#N……不，抱歉。\x01",
            "一定是我的心理作用吧。\x02\x03",

            "#0201F话说回来，\x01",
            "游客要是进入了那种地方，\x01",
            "搜索起来可就很困难了。\x02\x03",

            "我们还是尽快行动吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0023
    ChrTalk(
        0x101,
        "#12P#0001F#N……嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 80450, 18000, 14340, 45)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_17FE")
    Jump("loc_1821")

    label("loc_17FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_1810")
    Jump("loc_1821")

    label("loc_1810")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_1821")
    OP_66(0x3, 0x1)

    label("loc_1821")

    SetScenarioFlags(0xB7, 4)
    ClearMapFlags(0x8000000)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_10_13DF end

    def Function_11_182D(): pass

    label("Function_11_182D")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    OP_4B(0xA, 0xFF)
    OP_68(-28620, 6600, 10120, 0)
    MoveCamera(98, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18600, 0)
    SetChrPos(0x101, -29550, 6000, 10270, 45)
    SetChrPos(0x102, -31360, 5320, 9380, 45)
    SetChrPos(0x103, -30590, 5700, 11140, 45)
    SetChrPos(0x104, -32430, 4780, 10350, 45)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0024
    ChrTalk(
        0x101,
        "#11P#0005F那是……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-25410, 6600, 17600, 0)
    MoveCamera(98, 32, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19860, 0)
    OP_68(-24440, 6600, 19080, 3000)
    OP_0D()
    SetChrPos(0x101, -28140, 6000, 11070, 45)
    SetChrPos(0x102, -29740, 6000, 10070, 45)
    SetChrPos(0x103, -27950, 6000, 9070, 45)
    SetChrPos(0x104, -29560, 6000, 8070, 45)

    def lambda_19A4():
        OP_95(0x101, -25140, 6000, 18180, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19A4)
    Sleep(50)

    def lambda_19C1():
        OP_95(0x102, -26740, 6000, 17790, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19C1)
    Sleep(50)

    def lambda_19DE():
        OP_95(0x103, -24950, 6000, 16860, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19DE)
    Sleep(50)

    def lambda_19FB():
        OP_95(0x104, -26560, 6000, 16460, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19FB)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xA, 0)
    WaitChrThread(0x102, 1)
    TurnDirection(0x102, 0xA, 0)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0xA, 0)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0xA, 0)
    OP_6F(0x79)

    #C0025
    ChrTalk(
        0x101,
        "#12P#0001F斯克特先生！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 750)

    #C0026
    ChrTalk(
        0xA,
        (
            "#5P……是你们啊，\x01",
            "来得真快呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#12P#0304F我们毕竟也\x01",
            "经历过不少大场面嘛。\x02\x03",

            "#0301F话说，\x01",
            "这位女性莫非就是……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0028
    ChrTalk(
        0xA,
        (
            "#5P我检查了她的随身物品，\x01",
            "发现她带着\x01",
            "共和国发放的护照。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        (
            "#5P看来是游客\x01",
            "之一啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#12P#0005F……她不要紧吗？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        (
            "#5P没事，只是被魔兽袭击，\x01",
            "由于惊吓过度而晕了过去而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        (
            "#5P魔兽已经被我解决了，\x01",
            "她连一点伤也没有呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#12P#0106F呼，是这样吗……\x01",
            "那就放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#11P#0200F游客应该是一对情侣……\x01",
            "但却没看到另一个人呢。\x02\x03",

            "说不定已经跑到\x01",
            "遗迹的深处去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#12P#0008F是啊……\x01",
            "得赶快找到他才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#12P#0306F真是的，居然丢下女士，\x01",
            "一个人逃跑，\x01",
            "真是个不合格的护花使者啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        (
            "#12P#0106F算啦，要从魔兽的口中逃脱，\x01",
            "这也是没办法的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "#5P我先来确保这位女士\x01",
            "的安全，然后再继续前进。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "#5P你们先去\x01",
            "里面搜索吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#12P#0000F明白了，那就拜托啦。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -25140, 6000, 18180, 45)
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0x1F, 0x1, 0x2)
    OP_4C(0xA, 0xFF)
    ClearMapFlags(0x8000000)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_11_182D end

    def Function_12_1DAC(): pass

    label("Function_12_1DAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2CAB")
    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    OP_68(90290, 21000, 26800, 0)
    MoveCamera(78, 8, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 80450, 18000, 13220, 45)
    SetChrPos(0x102, 80450, 18000, 15220, 45)
    SetChrPos(0x103, 80450, 18000, 14220, 45)
    SetChrPos(0x104, 80450, 18000, 12220, 45)
    OP_68(76180, 20400, 17600, 8000)
    MoveCamera(81, 9, 0, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 4)), scpexpr(EXPR_END)), "loc_20AE")

    #C0041
    ChrTalk(
        0x102,
        (
            "#6P#0100F那座建筑物……就是『太阳堡垒』啊。\x02\x03",

            "之前的任务实在是太过紧急，\x01",
            "都没能仔细观察……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F02():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F02)
    WaitChrThread(0x101, 1)

    #C0042
    ChrTalk(
        0x101,
        (
            "#12P#0005F如此说来，缇欧……\x01",
            "你之前不是说对那座建筑\x01",
            "有奇怪的感觉吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F5D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F5D)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1F91():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F91)
    Sleep(50)

    def lambda_1FA1():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1FA1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0043
    ChrTalk(
        0x104,
        "#12P#0305F这么一提，好像确实是说过呢。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#6P#0105F现在怎么样了，缇欧？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#6P#0203F……不，现在没问题了。\x01",
            "可能只是习惯了而已吧。\x02\x03",

            "#0200F说起来，格蕾丝小姐\x01",
            "委托我们拍摄的照片，\x01",
            "在这里似乎能拍到很不错的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#12P#0000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x2D, 0x1F4)
    Jump("loc_23E4")

    label("loc_20AE")


    #C0047
    ChrTalk(
        0x101,
        (
            "#12P#0005F那座遗迹是……？\x01",
            "好像很大呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#6P#0103F我记得……\x01",
            "是叫『太阳堡垒』的遗迹。\x02\x03",

            "#0101F详细情况不太清楚……\x01",
            "不过，据说是五百多年以前就存在的遗迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#12P#0305F不愧是『堡垒』，\x01",
            "建造得真坚固啊。\x02\x03",

            "#0303F在中世纪的战争时也曾使用过吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        "#6P#0205F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x101, 0x103, 500)

    #C0051
    ChrTalk(
        0x101,
        "#12P#0005F……缇欧，怎么了？\x02",
    )

    CloseMessageWindow()

    def lambda_2211():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2211)
    Sleep(50)

    def lambda_2221():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2221)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0052
    ChrTalk(
        0x103,
        (
            "#6P#0208F不……没什么。\x02\x03",

            "#0200F只是觉得从遗迹中\x01",
            "传来了奇怪的感觉……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    def lambda_22C8():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22C8)

    def lambda_22D5():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22D5)

    def lambda_22E2():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22E2)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x101,
        "#12P#0005F奇怪的感觉……？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#12P#0305F唔……\x01",
            "那里看上去好像只是个普通的堡垒遗迹……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#6P#0206F……不，抱歉。\x01",
            "一定是我的心理作用吧。\x02\x03",

            "#0200F说起来，格蕾丝小姐\x01",
            "委托我们拍摄的照片，\x01",
            "在这里似乎能拍到很不错的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#12P#0000F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_23E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_295E")
    TurnDirection(0x101, 0x102, 500)

    #C0057
    ChrTalk(
        0x101,
        (
            "#12P#0000F那么艾莉，\x01",
            "可以拜托你来拍照吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0058
    ChrTalk(
        0x102,
        (
            "#6P#0108F哎，好的。\x01",
            "虽然我没什么自信……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0059
    ChrTalk(
        0x104,
        (
            "#12P#0300F哪里哪里，应该没问题吧。\x02\x03",

            "只要看看镜头，\x01",
            "然后咔嚓一下拍下来\x01",
            "不就搞定了嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0060
    ChrTalk(
        0x102,
        (
            "#6P#0103F我说你啊……\x01",
            "要拍出好照片，\x01",
            "可没有那么简单哦。\x02\x03",

            "#0100F要注意确认\x01",
            "拍摄对象有没有被收入取景框中，\x01",
            "还要构思摄影角度……\x02\x03",

            "而且受到天气和风的影响，\x01",
            "照片所呈现出的感觉也会有很大不同。\x02\x03",

            "有时只要错过那一瞬的时机，\x01",
            "就再也拍不到\x01",
            "那么好的风景了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#6P#0203F外行和专家所拍出的照片，\x01",
            "差别可是一目了然的。\x02\x03",

            "#0200F不过，某些粗神经的人\x01",
            "大概无法理解这种细致的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0062
    ChrTalk(
        0x104,
        (
            "#12P#0306F唔……\x01",
            "你在说谁啊，说谁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#12P#0000F好啦好啦，\x01",
            "总之就交给艾莉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#6P#0100F那么……\x01",
            "我来试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x2D, 0x1F4)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_93(0x103, 0x2D, 0x1F4)
    OP_93(0x104, 0x2D, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0065
    ChrTalk(
        0x102,
        (
            "#6P#0103F……呼，\x01",
            "为了保险起见，我多拍了几张。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#12P#0000F看样子，似乎已经拍好了呢。\x02\x03",

            "感觉怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#6P#0100F在没有实际显像出来之前，\x01",
            "还无法确定……\x02\x03",

            "不过，我觉得至少\x01",
            "不会很差吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#6P#0200F艾莉前辈似乎\x01",
            "找回感觉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#12P#0300F哼……\x01",
            "反正只有我完全搞不懂。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#12P#0000F如果发现了这种风景漂亮的地方，\x01",
            "就再拍些照片吧。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C6B")

    label("loc_295E")

    TurnDirection(0x101, 0x102, 500)

    #C0071
    ChrTalk(
        0x101,
        (
            "#12P#0000F那么……\x01",
            "艾莉，麻烦你拍照了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        "#6P#0100F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x2D, 0x1F4)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_93(0x103, 0x2D, 0x1F4)
    OP_93(0x104, 0x2D, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x102,
        (
            "#6P#0103F……呼，\x01",
            "大概就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2AE1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2AE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_2AF8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2AF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2B0F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_2B26")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2B3D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_2B54")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2B6B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2B82")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_2B99")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2A")

    #C0074
    ChrTalk(
        0x101,
        (
            "#12P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "这样一来，就拍完了格蕾丝小姐\x01",
            "所要求的五张照片了。\x01",
            "现在随时都可以去交付了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C6B")

    label("loc_2C2A")


    #C0075
    ChrTalk(
        0x101,
        (
            "#12P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 80450, 18000, 14340, 45)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0xA)
    Sleep(500)
    ClearMapFlags(0x8000000)
    OP_37()
    OP_65(0x3, 0x1)
    EventEnd(0x5)
    Jump("loc_2D55")

    label("loc_2CAB")

    TalkBegin(0xFF)
    OP_93(0x101, 0x2D, 0x0)

    #C0076
    ChrTalk(
        0x101,
        (
            "#0005F（格蕾丝小姐委托的照片，\x01",
            "  在这里拍摄好像很不错……）\x02\x03",

            "#0003F（但现在可不是\x01",
            "  拍照的时候啊。）\x02\x03",

            "#0001F（必须要争分夺秒，\x01",
            "  尽早救出游客才行……）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_2D55")

    Return()

    # Function_12_1DAC end

    SaveToFile()

Try(main)
