from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r3080.bin",                # FileName
        "r3080",                    # MapName
        "r3080",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -74000, 0, -2000, 0, 0, 1, 101, 0, 5, 0, 6],
    )

    BuildStringList((
        "r3080",                  # 0
        "リヴィングトーテム",     # 1
        "MapThread",              # 2
        "魔獣",                   # 3
        "魔獣",                   # 4
        "魔獣",                   # 5
        "魔獣",                   # 6
        "観光客",                 # 7
        "観光客",                 # 8
        "アリオス",               # 9
        "遊撃士スコット",         # 10
        "br3000",                 # 11
        "br3000",                 # 12
        "br3000",                 # 13
        "br3000",                 # 14
        "br3000",                 # 15
        "br3000",                 # 16
        "アルモリカ古道方面",     # 17
        "太陽の砦",               # 18
    ))

    ATBonus("ATBonus_3E0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_3CCB", 8,   16,  0,   10,  5,   3,   0)
    Sepith("Sepith_3CE3", 7,   7,   7,   7,   7,   7,   7)
    Sepith("Sepith_3D03", 15,  0,   0,   15,  5,   5,   2)

    MonsterBattlePostion("MonsterBattlePostion_440", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_420", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 3, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4EC", 13, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 0, 0, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_638", 0x0000, 25, 6, 60, 10, 1, 20, 0, "br3000", "Sepith_3CCB", 30, 40, 20, 10,
        (
            ("ms69500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_440", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms69500.dat", "ms69500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms69500.dat", "ms63400.dat", "ms69500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_440", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms69500.dat", "ms64100.dat", "ms64100.dat", "ms64100.dat", 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
        )
    )

    BattleInfo(
        "BattleInfo_500", 0x0000, 25, 6, 60, 10, 1, 30, 0, "br3000", "Sepith_3CE3", 30, 40, 20, 10,
        (
            ("ms66800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_440", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms66800.dat", "ms66800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms66800.dat", "ms63400.dat", "ms66800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_440", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms66800.dat", "ms63400.dat", "ms66800.dat", "ms63400.dat", 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
        )
    )

    BattleInfo(
        "BattleInfo_5C8", 0x0000, 25, 6, 60, 10, 1, 40, 0, "br3000", "Sepith_3D03", 75, 25, 0, 0,
        (
            ("ms71600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_440", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms71600.dat", "ms71600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_788", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms61501.dat", "ms61501.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4C0", "MonsterBattlePostion_4A0", "ed7401", "ed7403", "ATBonus_3E0"),
            (),
            (),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_700", 0x0000, 25, 6, 60, 0, 1, 0, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63500.dat", "ms63500.dat", "ms63400.dat", "ms63500.dat", "ms63500.dat", "ms63400.dat", 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_4A0", "ed7401", "ed7403", "ATBonus_3E0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_744", 0x0022, 26, 6, 0, 0, 1, 0, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76200.dat", "ms76200.dat", "ms76200.dat", "ms76200.dat", 0, 0, 0, 0, "MonsterBattlePostion_4E0", "MonsterBattlePostion_4A0", "ed7402", "ed7403", "ATBonus_3E0"),
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
        "monster/ch66850.itc",               # 10
        "monster/ch66851.itc",               # 11
        "monster/ch71650.itc",               # 12
        "monster/ch71650.itc",               # 13
        "monster/ch76250.itc",               # 14
        "monster/ch76251.itc",               # 15
        "monster/ch69550.itc",               # 16
        "monster/ch69550.itc",               # 17
        "monster/ch63550.itc",               # 18
        "monster/ch63550.itc",               # 19
        "monster/ch61550.itc",               # 1A
        "monster/ch61550.itc",               # 1B
    ))

    DeclNpc(54990,   10500,   98699,   0,    484,  0x0, 0,   24,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    501,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    501,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    501,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    501,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-41710,  -32650,  10,      0x1010000,    "BattleInfo_638", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-42160,  36440,   10,      0x1010000,    "BattleInfo_500", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-1780,   57680,   6250,    0x1010000,    "BattleInfo_5C8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(40790,   54660,   12500,   0x1010000,    "BattleInfo_500", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(38370,   94280,   10000,   0x1010000,    "BattleInfo_638", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(50320,   90510,   10000,   0x185010E,    "BattleInfo_788", 0,   26,  0xFFFF, 8,  9)

    DeclEvent(0x0040, 0, 9,   50.31999969482422,     90.51000213623047,     10.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -6.289999961853027,    -11.313750267028809,   -2.5,                  1.0])

    DeclActor(-40000,  100,     -42000,  1200,    -40000,  1100,    -42000,  0x007C, 0,  7,  0x0000)
    DeclActor(54990,   10100,   98700,   1200,    54990,   11100,   98700,   0x007C, 0,  8,  0x0000)
    DeclActor(-24540,  500,     -2060,   1200,    -24540,  2000,    -2060,   0x007C, 0,  16, 0x0000)

    PlaceName(-94.0, 0.0, -5.0, 0x0000, 0x0000, "アルモリカ古道方面")
    PlaceName(68.0, 0.0, -1.0, 0x0000, 0x0000, "太陽の砦")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 3, 2, 1])              # 9

    ScpFunction((
        "Function_0_888",          # 00, 0
        "Function_1_8A7",          # 01, 1
        "Function_2_8C6",          # 02, 2
        "Function_3_8E3",          # 03, 3
        "Function_4_900",          # 04, 4
        "Function_5_97A",          # 05, 5
        "Function_6_994",          # 06, 6
        "Function_7_E92",          # 07, 7
        "Function_8_FDF",          # 08, 8
        "Function_9_11F2",         # 09, 9
        "Function_10_186B",        # 0A, 10
        "Function_11_231E",        # 0B, 11
        "Function_12_3ACE",        # 0C, 12
        "Function_13_3B2A",        # 0D, 13
        "Function_14_3BBB",        # 0E, 14
        "Function_15_3C28",        # 0F, 15
        "Function_16_3C77",        # 10, 16
    ))


    def Function_0_888(): pass

    label("Function_0_888")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8A6")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_888")

    label("loc_8A6")

    Return()

    # Function_0_888 end

    def Function_1_8A7(): pass

    label("Function_1_8A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8C5")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_8A7")

    label("loc_8C5")

    Return()

    # Function_1_8A7 end

    def Function_2_8C6(): pass

    label("Function_2_8C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E2")
    OP_A1(0xFE, 0x4E2, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_2_8C6")

    label("loc_8E2")

    Return()

    # Function_2_8C6 end

    def Function_3_8E3(): pass

    label("Function_3_8E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FF")
    OP_A1(0xFE, 0x2EE, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_3_8E3")

    label("loc_8FF")

    Return()

    # Function_3_8E3 end

    def Function_4_900(): pass

    label("Function_4_900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 1)), scpexpr(EXPR_END)), "loc_979")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_979")
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(131, 1, 100, 0)
    Sleep(1000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
    StopEffect(0x0, 0x2)
    OP_24(0x83)
    ClearScenarioFlags(0xBA, 1)
    Jump("loc_979")

    label("loc_979")

    Return()

    # Function_4_900 end

    def Function_5_97A(): pass

    label("Function_5_97A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_993")
    Event(0, 10)

    label("loc_993")

    Return()

    # Function_5_97A end

    def Function_6_994(): pass

    label("Function_6_994")

    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E18")
    SetChrFlags(0x17, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_E2C")

    label("loc_E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2C")
    ClearChrFlags(0x17, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E2C")

    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x17, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4F")
    OP_70(0x0, 0x0)
    Jump("loc_E53")

    label("loc_E4F")

    OP_70(0x0, 0x1E)

    label("loc_E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E66")
    OP_70(0x3, 0x0)
    Jump("loc_E6A")

    label("loc_E66")

    OP_70(0x3, 0x1E)

    label("loc_E6A")

    LoadEffect(0x0, "map/mpr3000.eff")
    BeginChrThread(0x9, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E91")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_E91")

    Return()

    # Function_6_994 end

    def Function_7_E92(): pass

    label("Function_7_E92")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8E")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_F17")
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
    SetScenarioFlags(0x107, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_F89")

    label("loc_F17")

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

    label("loc_F89")

    Jump("loc_FD3")

    label("loc_F8E")

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

    label("loc_FD3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_E92 end

    def Function_8_FDF(): pass

    label("Function_8_FDF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AC")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DA")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1038():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1038)

    def lambda_1052():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1052)
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
    Battle("BattleInfo_700", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_10BB"),
        (2, "loc_10CA"),
        (1, "loc_10D7"),
        (SWITCH_DEFAULT, "loc_10DA"),
    )


    label("loc_10BB")

    SetScenarioFlags(0x75, 5)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_10DA")

    label("loc_10CA")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_10D7")

    OP_B7(0x0)
    Return()

    label("loc_10DA")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA0, 1)"), scpexpr(EXPR_END)), "loc_1137")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x107, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_11A7")

    label("loc_1137")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_11A7")

    Jump("loc_11E6")

    label("loc_11AC")

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

    label("loc_11E6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_FDF end

    def Function_9_11F2(): pass

    label("Function_9_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 4)), scpexpr(EXPR_END)), "loc_11FC")
    Return()

    label("loc_11FC")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型の魔獣が徘徊#4Rはいかい#している。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_12DE"),
        (SWITCH_DEFAULT, "loc_12F5"),
    )


    label("loc_12DE")

    Sleep(500)
    OP_90(0x0, 45210, 10000, 90260, 270)
    EventEnd(0x5)
    Return()

    label("loc_12F5")

    Battle("BattleInfo_788", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(45210, 11000, 90260, 0)
    OP_90(0x0, 45210, 10000, 90260, 270)
    OP_90(0x1, 45210, 10000, 90260, 270)
    OP_90(0x2, 45210, 10000, 90260, 270)
    OP_90(0x3, 45210, 10000, 90260, 270)
    OP_90(0x4, 45210, 10000, 90260, 270)
    OP_90(0x5, 45210, 10000, 90260, 270)
    OP_90(0x6, 45210, 10000, 90260, 270)
    OP_90(0x7, 45210, 10000, 90260, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_13B7"),
        (1, "loc_13BA"),
        (SWITCH_DEFAULT, "loc_13BD"),
    )


    label("loc_13B7")

    EventEnd(0x5)
    Return()

    label("loc_13BA")

    OP_B7(0x0)
    Return()

    label("loc_13BD")

    FadeToDark(0, 0, -1)
    OP_68(49920, 11500, 89700, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18070, 0)
    EventBegin(0x0)
    SetChrFlags(0x17, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手配魔獣を退治した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xC, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_150A")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 50320, 10000, 92510, 180)
    SetChrPos(0x102, 52220, 10000, 91130, 252)
    SetChrPos(0x103, 51600, 10000, 88890, 324)
    SetChrPos(0x104, 49140, 10000, 88890, 36)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14F4")
    SetChrPos(0x10A, 48420, 10000, 91130, 108)
    Jump("loc_1505")

    label("loc_14F4")

    SetChrPos(0x109, 48420, 10000, 91130, 108)

    label("loc_1505")

    Jump("loc_154E")

    label("loc_150A")

    SetChrPos(0x101, 50320, 10000, 92510, 180)
    SetChrPos(0x102, 52320, 10000, 90510, 270)
    SetChrPos(0x103, 50320, 10000, 88510, 0)
    SetChrPos(0x104, 48320, 10000, 90510, 90)

    label("loc_154E")

    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B0")

    #C0011
    ChrTalk(
        0x101,
        (
            "#5P#0005F戦術書#6Rクラフトブック#……\x01",
            "随分と古い書物みたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F6")

    label("loc_15B0")


    #C0012
    ChrTalk(
        0x101,
        (
            "#5P#0000F戦術書#6Rクラフトブック#……\x01",
            "これも古い書物みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F6")


    #C0013
    ChrTalk(
        0x102,
        (
            "#11P#0103Fクラフトを組み合わせた戦い方について\x01",
            "記されているようね。\x02\x03",

            "#0100Fランディとティオちゃんの技が\x01",
            "ここに書かれているものに\x01",
            "近いんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x104,
        (
            "#6P#0305Fおお、確かにそうみたいだな。\x02\x03",

            "#0300Fちょいと難しそうだが……\x01",
            "ティオすけ、試してみるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#12P#0202Fはい、やってみましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_177B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_177B")

    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x2, 0x14F)
    AddCraft(0x3, 0x14F)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディとティオがコンビクラフト\x01\x07\x02",

            "『ハーケンストーム』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0017
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
    SetScenarioFlags(0x79, 4)
    SetScenarioFlags(0xD8, 7)
    OP_29(0x33, 0x4, 0x10)
    OP_29(0x33, 0x4, 0x2)
    OP_29(0x33, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE(0x22, 0x0)
    EventEnd(0x5)
    Return()

    # Function_9_11F2 end

    def Function_10_186B(): pass

    label("Function_10_186B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("monster/ch76252.itc", 0x26)
    LoadChrToIndex("chr/ch33100.itc", 0x27)
    SetChrChipByIndex(0xA, 0x14)
    SetChrChipByIndex(0xB, 0x14)
    SetChrChipByIndex(0xC, 0x14)
    SetChrChipByIndex(0xD, 0x14)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 1, 0, 2)
    BeginChrThread(0xB, 1, 0, 2)
    BeginChrThread(0xC, 1, 0, 2)
    BeginChrThread(0xD, 1, 0, 2)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    OP_68(-77000, 1500, -2000, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -77000, 0, -2000, 90)
    SetChrPos(0x102, -77500, 0, -1000, 90)
    SetChrPos(0x103, -78500, 0, -3000, 90)
    SetChrPos(0x104, -79250, 0, -2000, 90)
    SetChrPos(0xE, -31500, 500, -2000, 270)
    SetChrPos(0xA, -36000, 550, 500, 135)
    SetChrPos(0xB, -36000, 550, -4500, 45)
    SetChrPos(0xC, -34000, 550, 2500, 135)
    SetChrPos(0xD, -34000, 550, -6500, 45)

    def lambda_1A32():
        OP_98(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A32)
    Sleep(50)

    def lambda_1A4F():
        OP_98(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A4F)
    Sleep(50)

    def lambda_1A6C():
        OP_98(0x103, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A6C)
    Sleep(50)

    def lambda_1A89():
        OP_98(0x104, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A89)
    OP_68(-70000, 1500, -2000, 4500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    #N0018
    NpcTalk(
        0xE,
        "男の声",
        "#2P#4Sだ……誰か助けてくれぇ～！！\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
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

    #C0019
    ChrTalk(
        0x102,
        "#5P#0107Fロイド、あれ！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#6P#0007Fああ！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_68(-32450, 1500, -2000, 4000)
    MoveCamera(90, 25, 0, 4000)
    SetCameraDistance(20230, 4000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    OP_6F(0x79)
    OP_98(0xE, 0x1F4, 0x0, 0x0, 0x1F4, 0x0)

    #C0021
    ChrTalk(
        0xE,
        "な、なんで俺がこんな目に……！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xE,
        (
            "……誰か～！！\x01",
            "誰かいないのか～！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C77():
        OP_9B(0x0, 0xA, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1C77)
    SetChrChipByIndex(0xA, 0x15)
    BeginChrThread(0xA, 1, 0, 3)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    def lambda_1CA4():
        OP_9B(0x0, 0xB, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1CA4)
    SetChrChipByIndex(0xB, 0x15)
    BeginChrThread(0xB, 1, 0, 3)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)

    def lambda_1CD1():
        OP_9B(0x0, 0xC, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1CD1)
    SetChrChipByIndex(0xC, 0x15)
    BeginChrThread(0xC, 1, 0, 3)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)

    def lambda_1CFE():
        OP_9B(0x0, 0xD, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1CFE)
    SetChrChipByIndex(0xD, 0x15)
    BeginChrThread(0xD, 1, 0, 3)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xA, 2)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xB, 2)
    SetChrChipByIndex(0xB, 0x14)
    BeginChrThread(0xB, 1, 0, 2)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xC, 2)
    SetChrChipByIndex(0xC, 0x14)
    BeginChrThread(0xC, 1, 0, 2)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xD, 2)
    SetChrChipByIndex(0xD, 0x14)
    BeginChrThread(0xD, 1, 0, 2)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(948, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x14)
    Fade(1000)
    OP_82(0x96, 0x64, 0xBB8, 0x320)
    EndChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x1)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(19750, 1000)
    OP_A6(0xA, 0x5, 0x5, 0x3E8, 0x3E8)
    Fade(500)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CancelBlur(0)
    OP_0D()

    #C0023
    ChrTalk(
        0xE,
        (
            "ひ、ひぃぃぃ……！！\x01",
            "女神様、お助けを……！！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -45000, 0, -1500, 90)
    SetChrPos(0x102, -45500, 0, -500, 90)
    SetChrPos(0x103, -46500, 0, -3500, 90)
    SetChrPos(0x104, -47250, 0, -2500, 90)

    #C0024
    ChrTalk(
        0x101,
        "#5P#0007F──待て！！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    def lambda_1EBF():
        OP_98(0x101, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EBF)
    Sleep(50)

    def lambda_1EDC():
        OP_98(0x102, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1EDC)
    Sleep(50)

    def lambda_1EF9():
        OP_98(0x103, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1EF9)
    Sleep(50)

    def lambda_1F16():
        OP_98(0x104, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F16)

    def lambda_1F30():
        OP_93(0xA, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1F30)
    Sleep(50)

    def lambda_1F40():
        OP_93(0xB, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1F40)
    Sleep(50)

    def lambda_1F50():
        OP_93(0xC, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1F50)
    Sleep(50)

    def lambda_1F60():
        OP_93(0xD, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1F60)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_68(-38540, 1500, -1750, 2500)
    MoveCamera(90, 13, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(18000, 2500)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0025
    ChrTalk(
        0x104,
        (
            "#6P#0302Fハハッ、どうやら……\x01",
            "最高のタイミングに\x01",
            "出くわしたみたいだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        "#12P#0206F……最悪の間違いかと。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#6P#0007Fクロスベル警察の者です！\x02\x03",

            "俺たちが魔獣を\x01",
            "ひきつけているうちに、早く！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xE,
        "#5Pあ、ああ……！\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_97(0xE, 0x0, 0x0, 0x3A98, 0x1388, 0x0)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetCameraDistance(17000, 2000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    Sound(948, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x14)
    Fade(1000)
    OP_82(0x96, 0x64, 0xBB8, 0x320)
    EndChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x1)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(16000, 1000)
    OP_A6(0xB, 0x5, 0x5, 0x3E8, 0x3E8)
    Fade(500)
    SetChrChipByIndex(0xB, 0x14)
    BeginChrThread(0xB, 1, 0, 2)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CancelBlur(0)
    OP_0D()

    #C0029
    ChrTalk(
        0x101,
        (
            "#6P#0010Fくっ……！？\x02\x03",

            "なんだ、この魔獣……\x01",
            "迫力が半端じゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#6P#0107Fこの辺りに棲息している\x01",
            "どの魔獣とも違うみたい……！\x02\x03",

            "もしかして、太古の時代の……？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#12P#0303Fどうやら、ナメてかかるわけには\x01",
            "いかねぇようだな。\x02\x03",

            "#0307Fハッ……上等じゃねぇか！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        "#12P#0207F……来ます！\x02",
    )

    CloseMessageWindow()

    def lambda_2271():
        OP_9B(0x0, 0xA, 0x0, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2271)
    SetChrChipByIndex(0xA, 0x15)
    BeginChrThread(0xA, 1, 0, 3)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)

    def lambda_229E():
        OP_9B(0x0, 0xB, 0x0, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_229E)
    SetChrChipByIndex(0xB, 0x15)
    BeginChrThread(0xB, 1, 0, 3)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    EndChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x1)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x1)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_744", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)
    Return()

    # Function_10_186B end

    def Function_11_231E(): pass

    label("Function_11_231E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00053.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00153.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00253.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00353.itc", 0x25)
    LoadChrToIndex("monster/ch76252.itc", 0x26)
    LoadChrToIndex("monster/ch76253.itc", 0x27)
    LoadChrToIndex("apl/ch50540.itc", 0x28)
    LoadChrToIndex("chr/ch27200.itc", 0x29)
    LoadChrToIndex("chr/ch33100.itc", 0x2A)
    LoadChrToIndex("chr/ch34300.itc", 0x2B)
    LoadChrToIndex("apl/ch50376.itc", 0x2C)
    LoadEffect(0x1, "battle\\btgun00.eff")
    LoadEffect(0x2, "event\\ev001_00.eff")
    LoadEffect(0x3, "event\\ev000_00.eff")
    LoadEffect(0x4, "event\\eva04_00.eff")
    OP_68(-38540, 1200, -2000, 0)
    MoveCamera(90, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(16500, 2000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01400.itp")
    SetChrPos(0x101, -39000, 0, -1500, 90)
    SetChrPos(0x102, -39500, 0, -500, 90)
    SetChrPos(0x103, -40500, 0, -3500, 90)
    SetChrPos(0x104, -41250, 0, -2500, 90)
    SetChrPos(0xA, -36000, 550, 500, 225)
    SetChrPos(0xB, -36000, 550, -4500, 315)
    SetChrPos(0xC, -34000, 550, 2500, 225)
    SetChrPos(0xD, -34000, 550, -6500, 315)
    SetChrPos(0x10, -70000, 0, -2000, 90)
    SetChrPos(0x11, -71500, 0, -2000, 90)
    SetChrPos(0xE, -72500, 0, -2500, 90)
    SetChrPos(0xF, -72750, 0, -1500, 90)
    SetChrChipByIndex(0x10, 0x28)
    SetChrSubChip(0x10, 0x6)
    SetChrFlags(0x10, 0x8000)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 0x2C)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0xE, 0x2A)
    SetChrChipByIndex(0xF, 0x2B)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25EF")
    SetChrChipByIndex(0x101, 0x1F)
    SetChrChipByIndex(0x102, 0x21)
    SetChrChipByIndex(0x103, 0x23)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x103, 0x3)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0xA, 0x14)
    SetChrChipByIndex(0xB, 0x14)
    SetChrChipByIndex(0xC, 0x14)
    SetChrChipByIndex(0xD, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    BeginChrThread(0xB, 1, 0, 2)
    BeginChrThread(0xC, 1, 0, 2)
    BeginChrThread(0xD, 1, 0, 2)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Jump("loc_265B")

    label("loc_25EF")

    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xA, 0x27)
    SetChrChipByIndex(0xB, 0x27)
    SetChrChipByIndex(0xC, 0x27)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xA, 0x1)
    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0xC, 0x1)
    SetChrSubChip(0xD, 0x1)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)

    label("loc_265B")

    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1B")
    OP_2C(0x1F, 0x3)
    OP_6F(0x10)

    #C0033
    ChrTalk(
        0x101,
        "#6P#0010Fや、やったか……！？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#6P#0108Fこの魔獣……見た目よりも\x01",
            "さらに手強かったわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#12P#0301F……チッ、気にいらねぇな。\x01",
            "一体何だってんだ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        "#12P#0208F………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(848, 0, 100, 0)

    def lambda_27C0():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_27C0)
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
    PlayBGM("ed7511", 0)

    #C0037
    ChrTalk(
        0x101,
        "#6P#0005Fな、なにッ……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 1)
    Fade(500)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2888():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2888)
    Sleep(100)

    def lambda_28A4():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_28A4)
    Sleep(100)

    def lambda_28C0():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_28C0)
    WaitChrThread(0xB, 1)
    SetChrChipByIndex(0xB, 0x14)
    BeginChrThread(0xB, 1, 0, 2)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xC, 1)
    SetChrChipByIndex(0xC, 0x14)
    BeginChrThread(0xC, 1, 0, 2)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xD, 1)
    SetChrChipByIndex(0xD, 0x14)
    BeginChrThread(0xD, 1, 0, 2)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sound(948, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x14)
    Fade(1000)
    OP_82(0x96, 0x64, 0xBB8, 0x320)
    EndChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x1)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(17000, 1000)
    OP_A6(0xA, 0x5, 0x5, 0x3E8, 0x3E8)
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
    SetChrChipByIndex(0x101, 0x1F)
    SetChrChipByIndex(0x102, 0x21)
    SetChrChipByIndex(0x103, 0x23)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x103, 0x3)
    SetChrSubChip(0x104, 0x2)
    Sound(514, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CancelBlur(0)
    OP_0D()
    Sleep(300)

    #C0038
    ChrTalk(
        0x102,
        "#6P#0106Fきゃあっ！！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        "#12P#0210Fっ……！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#12P#0310Fチッ……\x01",
            "化物どもが……！\x02\x03",

            "こんなヘトヘト状態で\x01",
            "もう一戦ってか……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#6P#0010F（まずい、このままじゃ……！）\x02\x03",

            "（何とかこの場を切り抜ける方法は……！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D02")

    label("loc_2B1B")

    PlayBGM("ed7511", 0)
    OP_6F(0x10)

    #C0042
    ChrTalk(
        0x101,
        "#6P#0010Fぐぅっ……！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        (
            "#6P#0108Fこ、この魔獣……\x01",
            "見た目よりもさらに強い……！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#12P#0310F化物どもが……\x01",
            "どんな体力してやがるんだ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#12P#0208F………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(948, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x14)
    Fade(1000)
    OP_82(0x96, 0x64, 0xBB8, 0x320)
    EndChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x1)
    SetCameraDistance(17000, 1000)
    OP_A6(0xA, 0x5, 0x5, 0x3E8, 0x3E8)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    CancelBlur(0)
    OP_0D()
    Sleep(1000)

    #C0046
    ChrTalk(
        0x101,
        (
            "#6P#0010F（まずい、このままじゃ……！）\x02\x03",

            "（何とかこの場を切り抜ける方法は……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D02")

    Sound(530, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0xA, 2, 0, 13)
    StopBGM(0xBB8)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0xA, 2)

    #C0047
    ChrTalk(
        0x101,
        "#6P#0005Fえっ……！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    Fade(500)
    OP_68(-68000, 1500, -2000, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17500, 0)
    OP_68(-71000, 1500, -2000, 500)
    BeginChrThread(0x11, 1, 0, 12)
    SetChrChip(0x0, 0x10, 0x3C, 0x1F4)
    SetChrFlags(0x10, 0x20)

    def lambda_2E28():
        OP_98(0x10, 0x4E20, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2E28)
    OP_0D()
    WaitChrThread(0x10, 1)
    EndChrThread(0x11, 0x1)
    SetChrChip(0x1, 0x10, 0x0, 0x0)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    Fade(500)
    SetChrPos(0x10, -48500, 3500, -2000, 90)
    OP_68(-34500, 1900, -2000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15670, 0)
    BeginChrThread(0xB, 2, 0, 13)
    Sleep(100)
    BeginChrThread(0xC, 2, 0, 13)
    Sleep(100)
    BeginChrThread(0xD, 2, 0, 13)
    OP_98(0x10, 0x2EE0, 0xFFFFF448, 0x0, 0x4E20, 0x0)
    SetChrSubChip(0x10, 0x1)
    Sound(250, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xD, 2)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0048
    ChrTalk(
        0x10,
        "#10A#5P#1407F斬──！\x02",
    )
    #Auto

    CloseMessageWindow()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    SetCameraDistance(20250, 6000)
    SetChrChip(0x0, 0x10, 0x3C, 0x1F4)
    SetChrSubChip(0x10, 0x7)
    PlayEffect(0x4, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_92(0x10, 0xFFFF7842, 0xF3C, 0x3E8)

    def lambda_2FB4():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2FB4)

    def lambda_2FC5():
        OP_96(0x10, 0xFFFF7874, 0x1F4, 0xF46, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2FC5)
    Sleep(200)

    def lambda_2FE2():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2FE2)
    Sound(815, 0, 100, 0)
    Sound(834, 0, 100, 0)
    WaitChrThread(0x10, 2)
    BeginChrThread(0xA, 2, 0, 15)
    WaitChrThread(0x10, 1)
    OP_92(0x10, 0xFFFF85EE, 0xFA, 0x3E8)

    def lambda_301A():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_301A)

    def lambda_302B():
        OP_96(0x10, 0xFFFF85EE, 0x1F4, 0xFA, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_302B)
    Sleep(200)

    def lambda_3048():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3048)
    WaitChrThread(0x10, 2)
    Sound(815, 0, 100, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0xC, 2, 0, 15)
    WaitChrThread(0x10, 1)
    OP_92(0x10, 0xFFFF7C8E, 0xFFFFE188, 0x3E8)

    def lambda_3080():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3080)

    def lambda_3091():
        OP_96(0x10, 0xFFFF7C8E, 0x1F4, 0xFFFFE188, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3091)
    Sleep(200)

    def lambda_30AE():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_30AE)
    WaitChrThread(0x10, 2)
    Sound(815, 0, 100, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0xD, 2, 0, 15)
    WaitChrThread(0x10, 1)
    OP_92(0x10, 0xFFFF716C, 0xFFFFF830, 0x3E8)

    def lambda_30E6():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_30E6)

    def lambda_30F7():
        OP_96(0x10, 0xFFFF716C, 0x1F4, 0xFFFFF830, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_30F7)
    Sleep(200)

    def lambda_3114():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3114)
    WaitChrThread(0x10, 2)
    Sound(815, 0, 100, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0xB, 2, 0, 15)
    SetChrSubChip(0x10, 0x5)
    WaitChrThread(0x10, 1)
    Sleep(500)
    SetChrChip(0x1, 0x10, 0x0, 0x0)
    SetCameraDistance(21250, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x14)
    Fade(500)
    Sound(816, 0, 100, 0)
    Sound(834, 0, 100, 0)
    Sound(502, 0, 100, 0)
    BeginChrThread(0xA, 2, 0, 14)
    Sleep(50)
    BeginChrThread(0xD, 2, 0, 14)
    Sleep(50)
    BeginChrThread(0xC, 2, 0, 14)
    Sleep(50)
    BeginChrThread(0xB, 2, 0, 14)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xD, 2)
    CancelBlur(0)
    OP_68(-38470, 1500, -2170, 2000)
    MoveCamera(46, 16, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(17940, 2000)
    Sleep(500)
    SetChrSubChip(0x10, 0x0)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 70, 0)
    OP_6F(0x79)

    #C0049
    ChrTalk(
        0x101,
        "#6P#0005Fア、アリオスさん……！？\x02",
    )

    CloseMessageWindow()
    Sound(531, 0, 100, 0)
    OP_93(0x10, 0x10E, 0x1F4)
    Sleep(500)

    #C0050
    ChrTalk(
        0x10,
        "#11P#1404F……間に合ったようだな。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(300)

    #C0051
    ChrTalk(
        0x104,
        (
            "#6P#0305Fつ、つーか……\x01",
            "なんでオッサンが\x01",
            "こんなトコにいるんだ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0052
    AnonymousTalk(
        0x10,
        (
            "フ……助けた相手に対して\x01",
            "随分なご挨拶だな。\x02\x03",

            "……ギルドで依頼を確認したら\x01",
            "スコットがこちらに\x01",
            "来ているというのでな。\x02\x03",

            "厄介な場所だから\x01",
            "助太刀が要るだろうと思って\x01",
            "追って来たというわけだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0053
    ChrTalk(
        0x102,
        (
            "#6P#0102F……助かりました。\x01",
            "どうもありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        "#6P#0204F……正直ラッキーでしたね。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        (
            "#6P#0306Fいやいや、流石に\x01",
            "タイミングよすぎだろ！\x02\x03",

            "#0301Fオッサン、まさか\x01",
            "タイミングを計ってたんじゃ\x01",
            "ねぇだろうな～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x10,
        "#11P#1404Fハハ……どうだかな。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x11,
        "おい、みんな無事か？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x11, -50500, 0, -2000, 90)
    SetChrPos(0xE, -51500, 0, -2500, 90)
    SetChrPos(0xF, -51750, 0, -1500, 90)
    ClearChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)
    OP_68(-42000, 1500, -2000, 3000)
    MoveCamera(44, 11, 0, 3000)
    SetCameraDistance(19740, 3000)

    def lambda_3587():
        OP_98(0x11, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3587)
    Sleep(50)

    def lambda_35A4():
        OP_98(0xE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_35A4)
    Sleep(50)

    def lambda_35C1():
        OP_98(0xF, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_35C1)

    def lambda_35DB():
        TurnDirection(0x101, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35DB)

    def lambda_35E8():
        TurnDirection(0x102, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35E8)

    def lambda_35F5():
        TurnDirection(0x103, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_35F5)

    def lambda_3602():
        TurnDirection(0x104, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3602)
    WaitChrThread(0x11, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    OP_6F(0x79)

    #C0058
    ChrTalk(
        0x101,
        (
            "#11P#0000Fスコットさん……\x01",
            "そちらの方も目を覚ましたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x11,
        "#5Pああ、ついさっきな。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xF,
        (
            "#6P皆さん……\x01",
            "どうもありがとうございました！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xF,
        (
            "#6P特に遊撃士の方々には\x01",
            "なんとお礼を言っていいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xE,
        "#6Pうんうん、いいもの見たよ！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xE,
        (
            "#6Pあんな強そうな魔獣を\x01",
            "一撃で倒すなんてな！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xF,
        (
            "#6Pあの、スコットさん……\x01",
            "介抱してもらって嬉しかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xF,
        (
            "#6Pそれに、ライフルの腕も……\x01",
            "すごいんですね……㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xE, 0xF, 500)

    #C0066
    ChrTalk(
        0xE,
        "#12Pちょ、ちょっと……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x110, 0x1F4)

    #C0067
    ChrTalk(
        0x11,
        "#11Pハハ、とにかく無事で何よりだ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x101,
        "#11P#0012Fハ、ハハ……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#11P#0306Fふう、結局いつものパターンに\x01",
            "なっちまったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#11P#0102Fふふ、まあいいじゃない。\x01",
            "観光客は救い出せたんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        "#11P#0204F結果オーライってやつです。\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x11, 0x10, 500)
    OP_64(0x10)
    OP_64(0x11)

    #C0072
    ChrTalk(
        0x11,
        "#5P……アリオスさん？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x10,
        (
            "#11P#1403F……いや、なんでもない。\x02\x03",

            "#1400Fそれより、早く彼らを\x01",
            "アルモリカ村に送ったほうが\x01",
            "いいだろう。\x02\x03",

            "#1404F……特務支援課、\x01",
            "後ろの警戒は頼むぞ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A53():
        TurnDirection(0x101, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A53)
    Sleep(50)

    def lambda_3A63():
        TurnDirection(0x102, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A63)
    Sleep(50)

    def lambda_3A73():
        TurnDirection(0x103, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A73)
    Sleep(50)

    def lambda_3A83():
        TurnDirection(0x104, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A83)
    Sleep(300)

    #C0074
    ChrTalk(
        0x101,
        "#6P#0000Fあ……はい！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CA(0x1, 0xFF, 0x0)
    OP_29(0x1F, 0x1, 0x3)
    NewScene("t0020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_231E end

    def Function_12_3ACE(): pass

    label("Function_12_3ACE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B29")
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x1, 0xFF, 0xFE, 0x80, 0, 1100, 1400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    Sleep(250)
    Jump("Function_12_3ACE")

    label("loc_3B29")

    Return()

    # Function_12_3ACE end

    def Function_13_3B2A(): pass

    label("Function_13_3B2A")

    PlayEffect(0xA, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3B7D():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B7D)
    OP_A6(0xFE, 0xA, 0xA, 0x3E8, 0x9C4)
    SetChrChipByIndex(0xFE, 0x14)
    BeginChrThread(0xFE, 1, 0, 2)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_3B2A end

    def Function_14_3BBB(): pass

    label("Function_14_3BBB")

    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A6(0xFE, 0xA, 0xA, 0x2EE, 0x9C4)
    OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
    Return()

    # Function_14_3BBB end

    def Function_15_3C28(): pass

    label("Function_15_3C28")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_3C28 end

    def Function_16_3C77(): pass

    label("Function_16_3C77")

    TalkBegin(0xFF)
    SetChrName("")

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_16_3C77 end

    SaveToFile()

Try(main)
