from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "リヴィングトーテム",     # 1
        "MapThread",              # 2
        "遊撃士スコット",         # 3
        "観光客",                 # 4
        "br3000",                 # 5
        "br3000",                 # 6
        "br3000",                 # 7
        "br3000",                 # 8
        "br3000",                 # 9
        "アルモリカ古道方面",     # 10
    ))

    ATBonus("ATBonus_418", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_308F", 8,   16,  0,   10,  5,   3,   0)
    Sepith("Sepith_3097", 0,   0,   6,   17,  6,   6,   6)
    Sepith("Sepith_30A7", 7,   7,   7,   7,   7,   7,   7)
    Sepith("Sepith_309F", 10,  6,   2,   0,   8,   8,   8)

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
        "BattleInfo_750", 0x0000, 25, 6, 60, 8, 1, 20, 0, "br3000", "Sepith_308F", 30, 40, 20, 10,
        (
            ("ms69500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms69500.dat", "ms69500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms69500.dat", "ms63400.dat", "ms69500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms69500.dat", "ms64100.dat", "ms64100.dat", "ms64100.dat", 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
        )
    )

    BattleInfo(
        "BattleInfo_688", 0x0000, 25, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_3097", 30, 40, 20, 10,
        (
            ("ms63400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
        )
    )

    BattleInfo(
        "BattleInfo_4F8", 0x0000, 25, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_30A7", 30, 40, 20, 10,
        (
            ("ms66800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms66800.dat", "ms66800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_478", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", "ms69500.dat", 0, 0, 0, 0, "MonsterBattlePostion_458", "MonsterBattlePostion_4D8", "ed7400", "ed7403", "ATBonus_418"),
        )
    )

    BattleInfo(
        "BattleInfo_5C0", 0x0000, 25, 6, 60, 8, 1, 10, 0, "br3000", "Sepith_309F", 30, 40, 20, 10,
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

    PlaceName(-84.0, 0.0, 48.0, 0x0000, 0x0000, "アルモリカ古道方面")

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
        "Function_6_105C",         # 06, 6
        "Function_7_126F",         # 07, 7
        "Function_8_13BC",         # 08, 8
        "Function_9_1435",         # 09, 9
        "Function_10_144A",        # 0A, 10
        "Function_11_18F4",        # 0B, 11
        "Function_12_1F19",        # 0C, 12
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100B")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_F94")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x106, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1006")

    label("loc_F94")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1006")

    Jump("loc_1050")

    label("loc_100B")

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

    label("loc_1050")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F0F end

    def Function_6_105C(): pass

    label("Function_6_105C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1229")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1157")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_10B5():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10B5)

    def lambda_10CF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_10CF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_1138"),
        (2, "loc_1147"),
        (1, "loc_1154"),
        (SWITCH_DEFAULT, "loc_1157"),
    )


    label("loc_1138")

    SetScenarioFlags(0x75, 4)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1157")

    label("loc_1147")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1154")

    OP_B7(0x0)
    Return()

    label("loc_1157")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x95, 1)"), scpexpr(EXPR_END)), "loc_11B4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x95),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x106, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_1224")

    label("loc_11B4")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x95),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x95),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1224")

    Jump("loc_1263")

    label("loc_1229")

    FadeToDark(300, 0, 100)

    #A0007
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

    label("loc_1263")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_105C end

    def Function_7_126F(): pass

    label("Function_7_126F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_136B")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x55, 1)"), scpexpr(EXPR_END)), "loc_12F4")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x106, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1366")

    label("loc_12F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1366")

    Jump("loc_13B0")

    label("loc_136B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_13B0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_126F end

    def Function_8_13BC(): pass

    label("Function_8_13BC")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xA,
        (
            "俺はもう少し、この女性を\x01",
            "介抱しているつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "先に奥のほうを捜索してくれ。\x01",
            "あとで必ず追いつくからさ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_13BC end

    def Function_9_1435(): pass

    label("Function_9_1435")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xFE,
        "うぅ……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_1435 end

    def Function_10_144A(): pass

    label("Function_10_144A")

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
            "#12P#N#0005Fあの遺跡は……？\x01",
            "随分大きなものみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0015
    ChrTalk(
        0x102,
        (
            "#12P#N#0103Fたしか……\x01",
            "《太陽の砦》と呼ばれる遺跡よ。\x02\x03",

            "#0101F詳しい謂れは分かっていないけど……\x01",
            "５００年以上前の遺跡らしいわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0016
    ChrTalk(
        0x104,
        (
            "#12P#N#0305Fさすがに《砦》ってだけあって\x01",
            "堅牢な作りをしてやがるな。\x02\x03",

            "#0303F中世の戦にでも使われてたんだろう。\x02",
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
        "#12P#0005F#N……ティオ？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_167A():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_167A)
    Sleep(50)

    def lambda_168A():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_168A)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0019
    ChrTalk(
        0x103,
        (
            "#12P#0208F#Nいえ……何でもありません。\x02\x03",

            "#0200Fただちょっと、あの遺跡の方から\x01",
            "妙なものを感じたんですが……\x02",
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

    def lambda_1757():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1757)

    def lambda_1764():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1764)

    def lambda_1771():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1771)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x101,
        "#12P#0005F#N妙なもの……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0021
    ChrTalk(
        0x104,
        (
            "#12P#0305F#Nふむ……\x01",
            "ただの古い砦跡っぽいが……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0022
    ChrTalk(
        0x103,
        (
            "#12P#0206F#N……いえ、すみません。\x01",
            "きっと気のせいでしょう。\x02\x03",

            "#0201Fそれよりも、\x01",
            "あんなところに観光客が\x01",
            "入っていたら捜索が困難です。\x02\x03",

            "急いだ方がいいでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0023
    ChrTalk(
        0x101,
        "#12P#0001F#N……ああ、そうだな。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 80450, 18000, 14340, 45)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_18C5")
    Jump("loc_18E8")

    label("loc_18C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_18D7")
    Jump("loc_18E8")

    label("loc_18D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_18E8")
    OP_66(0x3, 0x1)

    label("loc_18E8")

    SetScenarioFlags(0xB7, 4)
    ClearMapFlags(0x8000000)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_10_144A end

    def Function_11_18F4(): pass

    label("Function_11_18F4")

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
        "#11P#0005Fあれは……\x02",
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

    def lambda_1A6D():
        OP_95(0x101, -25140, 6000, 18180, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A6D)
    Sleep(50)

    def lambda_1A8A():
        OP_95(0x102, -26740, 6000, 17790, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A8A)
    Sleep(50)

    def lambda_1AA7():
        OP_95(0x103, -24950, 6000, 16860, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AA7)
    Sleep(50)

    def lambda_1AC4():
        OP_95(0x104, -26560, 6000, 16460, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1AC4)
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
        "#12P#0001Fスコットさん！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 750)

    #C0026
    ChrTalk(
        0xA,
        (
            "#5P……君たちか。\x01",
            "結構早かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#12P#0304F俺らもこれで\x01",
            "結構場数をふんでるんでね。\x02\x03",

            "#0301Fンなことより、\x01",
            "そっちの彼女はもしかして……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0028
    ChrTalk(
        0xA,
        (
            "#5P持ち物を調べたら\x01",
            "共和国で発行された\x01",
            "パスポートを持っていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        (
            "#5Pどうやら、観光客の\x01",
            "片割れらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#12P#0005F……大丈夫、なんですか？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        (
            "#5P大丈夫、魔獣に襲われた\x01",
            "ショックで気絶しただけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        (
            "#5P魔獣の方は俺が仕留めたから\x01",
            "カスリ傷すらないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#12P#0106Fほっ、そうですか……\x01",
            "一安心ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#11P#0200F観光客はカップルとのことでしたが……\x01",
            "もう１人は見えませんね。\x02\x03",

            "もっと奥のほうに\x01",
            "入り込んでしまったのかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#12P#0008Fそうだな……\x01",
            "早く見つけ出してやらないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#12P#0306Fったく、レディを置いて\x01",
            "一人で行っちまうとは\x01",
            "エスコートがなってねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        (
            "#12P#0106Fまあ、魔獣から逃げてたなら\x01",
            "仕方がないと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "#5P俺はこの女性の安全を\x01",
            "確保してから先に進む。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "#5P君たちは先に奥の方を\x01",
            "捜索していてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#12P#0000F分かりました、よろしくお願いします。\x02",
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

    # Function_11_18F4 end

    def Function_12_1F19(): pass

    label("Function_12_1F19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FA0")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 4)), scpexpr(EXPR_END)), "loc_225F")

    #C0041
    ChrTalk(
        0x102,
        (
            "#6P#0100Fあの建物は……《太陽の砦》ね。\x02\x03",

            "この前は緊急性の高い要請だったから\x01",
            "じっくり見なかったけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_207B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_207B)
    WaitChrThread(0x101, 1)

    #C0042
    ChrTalk(
        0x101,
        (
            "#12P#0005Fそういえばティオ……\x01",
            "あの建物に妙な感じがするとか\x01",
            "言ってたっけ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20DC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20DC)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2110():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2110)
    Sleep(50)

    def lambda_2120():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2120)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0043
    ChrTalk(
        0x104,
        "#12P#0305Fそういやぁ、そんなこと言ってたな。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#6P#0105F今はどうなの、ティオちゃん？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#6P#0203F……いえ、今は大丈夫です。\x01",
            "単に慣れただけかもしれませんが。\x02\x03",

            "#0200Fそれより、グレイスさんに\x01",
            "依頼されている写真……\x01",
            "ここなら撮れそうじゃないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#12P#0000Fあ、ああ、そうだな。\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x2D, 0x1F4)
    Jump("loc_25FB")

    label("loc_225F")


    #C0047
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあの遺跡は……？\x01",
            "随分大きなものみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#6P#0103Fたしか……\x01",
            "《太陽の砦》と呼ばれる遺跡よ。\x02\x03",

            "#0101F詳しい謂れは分かっていないけど……\x01",
            "５００年以上前の遺跡らしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#12P#0305Fさすがに《砦》ってだけあって\x01",
            "堅牢な作りをしてやがるな。\x02\x03",

            "#0303F中世の戦にでも使われてたんだろう。\x02",
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
        "#12P#0005F……ティオ？\x02",
    )

    CloseMessageWindow()

    def lambda_23F2():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23F2)
    Sleep(50)

    def lambda_2402():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2402)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0052
    ChrTalk(
        0x103,
        (
            "#6P#0208Fいえ……何でもありません。\x02\x03",

            "#0200Fただちょっと、あの遺跡の方から\x01",
            "妙なものを感じたんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    def lambda_24CB():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24CB)

    def lambda_24D8():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24D8)

    def lambda_24E5():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_24E5)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x101,
        "#12P#0005F妙なもの……？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#12P#0305Fふむ……\x01",
            "ただの古い砦跡っぽいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#6P#0206F……いえ、すみません。\x01",
            "きっと気のせいでしょう。\x02\x03",

            "#0200Fそれより、グレイスさんに\x01",
            "依頼されている写真……\x01",
            "ここなら撮れそうじゃないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#12P#0000Fあ、ああ、そうだな。\x02",
    )

    CloseMessageWindow()

    label("loc_25FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C11")
    TurnDirection(0x101, 0x102, 500)

    #C0057
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれじゃあエリィ、\x01",
            "撮影をお願いできるかな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0058
    ChrTalk(
        0x102,
        (
            "#6P#0108Fえ、ええ。\x01",
            "ちょっと自信はないけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0059
    ChrTalk(
        0x104,
        (
            "#12P#0300Fいやいや、大丈夫だろ。\x02\x03",

            "ちょっとレンズを覗いて\x01",
            "パチリと撮っちまえば\x01",
            "終わりじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0060
    ChrTalk(
        0x102,
        (
            "#6P#0103Fあのねぇ……\x01",
            "いい写真を撮るのは\x01",
            "そんな簡単なことじゃないのよ。\x02\x03",

            "#0100Fフレームの中に\x01",
            "対象物をどう収めるか、\x01",
            "構成を練らなきゃいけないし……\x02\x03",

            "天気や風の影響で\x01",
            "写真の印象もガラリと変わってしまう。\x02\x03",

            "ある一瞬を逃したら\x01",
            "二度と撮れないことだって\x01",
            "あるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#6P#0203F素人とプロの写真を見比べると\x01",
            "一目で違いが分かりますからね。\x02\x03",

            "#0200F粗雑な人には、その繊細さが\x01",
            "理解できないかも知れませんが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0062
    ChrTalk(
        0x104,
        (
            "#12P#0306Fぐっ……\x01",
            "誰のことを言ってんだ、誰の。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#12P#0000Fま、まぁまぁ。\x01",
            "ここはエリィに任せてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#6P#0100Fそれじゃあ……\x01",
            "やってみるわね。\x02",
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
            "#6P#0103F……ふぅ。\x01",
            "念のため何枚か撮っておいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#12P#0000Fどうやら撮れたみたいだな。\x02\x03",

            "出来栄えはどんな感じだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#6P#0100F実際に現像してみないと\x01",
            "分からないけど……\x02\x03",

            "少なくとも、\x01",
            "悪い写真ではないとは思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#6P#0200Fエリィさんも\x01",
            "カンを取り戻せたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#12P#0300Fふーん……\x01",
            "俺にはさっぱりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#12P#0000Fまたこういう場所を見つけたら\x01",
            "写真に収めていこう。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F60")

    label("loc_2C11")

    TurnDirection(0x101, 0x102, 500)

    #C0071
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれじゃあ……\x01",
            "エリィ、撮影を頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        "#6P#0100Fええ、分かったわ。\x02",
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
            "#6P#0103F……ふぅ。\x01",
            "こんなところかしら。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2DA8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_2DBF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2DD6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_2DED")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2E04")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_2E1B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2E32")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2E49")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_2E60")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F0B")

    #C0074
    ChrTalk(
        0x101,
        (
            "#12P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "これでグレイスさんに提示された\x01",
            "５枚ってノルマは達成できた。\x01",
            "これでいつでも提出できそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F60")

    label("loc_2F0B")


    #C0075
    ChrTalk(
        0x101,
        (
            "#12P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F60")

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
    Jump("loc_3066")

    label("loc_2FA0")

    TalkBegin(0xFF)
    OP_93(0x101, 0x2D, 0x0)

    #C0076
    ChrTalk(
        0x101,
        (
            "#0005F（グレイスさんに依頼された写真、\x01",
            "  ここなら撮れそうだけど……）\x02\x03",

            "#0003F（今はそんなことをしている\x01",
            "  場合じゃないな。）\x02\x03",

            "#0001F（一刻も早く観光客を\x01",
            "  保護してやらないと……）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_3066")

    Return()

    # Function_12_1F19 end

    SaveToFile()

Try(main)
