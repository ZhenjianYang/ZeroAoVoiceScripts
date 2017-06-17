from ZeroScenarioHelper import *

def main():
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
        "活图腾",                 # 1
        "MapThread",              # 2
        "魔兽",                   # 3
        "魔兽",                   # 4
        "魔兽",                   # 5
        "魔兽",                   # 6
        "游客",                   # 7
        "游客",                   # 8
        "亚里欧斯",               # 9
        "游击士斯克特",           # 10
        "br3000",                 # 11
        "br3000",                 # 12
        "br3000",                 # 13
        "br3000",                 # 14
        "br3000",                 # 15
        "br3000",                 # 16
        "阿尔摩利卡古道方向",     # 17
        "太阳堡垒",               # 18
    ))

    ATBonus("ATBonus_3E0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_3AB9", 8,   16,  0,   10,  5,   3,   0)
    Sepith("Sepith_3AD1", 7,   7,   7,   7,   7,   7,   7)
    Sepith("Sepith_3AF1", 15,  0,   0,   15,  5,   5,   2)

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
        "BattleInfo_638", 0x0000, 25, 6, 60, 10, 1, 20, 0, "br3000", "Sepith_3AB9", 30, 40, 20, 10,
        (
            ("ms69500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_440", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms69500.dat", "ms69500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms69500.dat", "ms63400.dat", "ms69500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_440", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms69500.dat", "ms64100.dat", "ms64100.dat", "ms64100.dat", 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
        )
    )

    BattleInfo(
        "BattleInfo_500", 0x0000, 25, 6, 60, 10, 1, 30, 0, "br3000", "Sepith_3AD1", 30, 40, 20, 10,
        (
            ("ms66800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_440", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms66800.dat", "ms66800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms66800.dat", "ms63400.dat", "ms66800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_440", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
            ("ms66800.dat", "ms63400.dat", "ms66800.dat", "ms63400.dat", 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_4A0", "ed7400", "ed7403", "ATBonus_3E0"),
        )
    )

    BattleInfo(
        "BattleInfo_5C8", 0x0000, 25, 6, 60, 10, 1, 40, 0, "br3000", "Sepith_3AF1", 75, 25, 0, 0,
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

    PlaceName(-94.0, 0.0, -5.0, 0x0000, 0x0000, "阿尔摩利卡古道方向")
    PlaceName(68.0, 0.0, -1.0, 0x0000, 0x0000, "太阳堡垒")

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
        "Function_8_FC8",          # 08, 8
        "Function_9_11C2",         # 09, 9
        "Function_10_1787",        # 0A, 10
        "Function_11_21E2",        # 0B, 11
        "Function_12_38C8",        # 0C, 12
        "Function_13_3924",        # 0D, 13
        "Function_14_39B5",        # 0E, 14
        "Function_15_3A22",        # 0F, 15
        "Function_16_3A71",        # 10, 16
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7F")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('中回复药', 1)"), scpexpr(EXPR_END)), "loc_F11")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x107, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_F7A")

    label("loc_F11")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F7A")

    Jump("loc_FBC")

    label("loc_F7F")

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

    label("loc_FBC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_E92 end

    def Function_8_FC8(): pass

    label("Function_8_FC8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1184")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C1")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1021():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1021)

    def lambda_103B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_103B)
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
    Battle("BattleInfo_700", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_10A2"),
        (2, "loc_10B1"),
        (1, "loc_10BE"),
        (SWITCH_DEFAULT, "loc_10C1"),
    )


    label("loc_10A2")

    SetScenarioFlags(0x75, 5)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_10C1")

    label("loc_10B1")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_10BE")

    OP_B7(0x0)
    Return()

    label("loc_10C1")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('破盾之牙', 1)"), scpexpr(EXPR_END)), "loc_1118")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '破盾之牙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x107, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_117F")

    label("loc_1118")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '破盾之牙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '破盾之牙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_117F")

    Jump("loc_11B6")

    label("loc_1184")

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

    label("loc_11B6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_FC8 end

    def Function_9_11C2(): pass

    label("Function_9_11C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 4)), scpexpr(EXPR_END)), "loc_11CC")
    Return()

    label("loc_11CC")

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
            "大型魔兽正在四处游荡。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【消灭】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1298"),
        (SWITCH_DEFAULT, "loc_12AF"),
    )


    label("loc_1298")

    Sleep(500)
    OP_90(0x0, 45210, 10000, 90260, 270)
    EventEnd(0x5)
    Return()

    label("loc_12AF")

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
        (2, "loc_1371"),
        (1, "loc_1374"),
        (SWITCH_DEFAULT, "loc_1377"),
    )


    label("loc_1371")

    EventEnd(0x5)
    Return()

    label("loc_1374")

    OP_B7(0x0)
    Return()

    label("loc_1377")

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
            "消灭了通缉魔兽！\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '战术书·苍'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber('战术书·苍', 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14BA")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 50320, 10000, 92510, 180)
    SetChrPos(0x102, 52220, 10000, 91130, 252)
    SetChrPos(0x103, 51600, 10000, 88890, 324)
    SetChrPos(0x104, 49140, 10000, 88890, 36)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14A4")
    SetChrPos(0x10A, 48420, 10000, 91130, 108)
    Jump("loc_14B5")

    label("loc_14A4")

    SetChrPos(0x109, 48420, 10000, 91130, 108)

    label("loc_14B5")

    Jump("loc_14FE")

    label("loc_14BA")

    SetChrPos(0x101, 50320, 10000, 92510, 180)
    SetChrPos(0x102, 52320, 10000, 90510, 270)
    SetChrPos(0x103, 50320, 10000, 88510, 0)
    SetChrPos(0x104, 48320, 10000, 90510, 90)

    label("loc_14FE")

    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_154C")

    #C0011
    ChrTalk(
        0x101,
        (
            "#5P#0005F战术书……\x01",
            "好像是本很古老的书籍呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1584")

    label("loc_154C")


    #C0012
    ChrTalk(
        0x101,
        (
            "#5P#0000F战术书……\x01",
            "这好像也是一本很古老的书籍啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1584")


    #C0013
    ChrTalk(
        0x102,
        (
            "#11P#0103F似乎记载了关于组合战技\x01",
            "的使用方法呢。\x02\x03",

            "#0100F兰迪和缇欧的战技\x01",
            "好像和这里写的\x01",
            "很接近吧？\x02",
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
            "#6P#0305F哦哦，好像确实没错啊。\x02\x03",

            "#0300F虽然可能有些难度，不过……\x01",
            "阿缇，我们试一下如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#12P#0202F好的，试试看吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16C3")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_16C3")

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
            "兰迪和缇欧习得了组合战技\x01\x07\x02",

            "『钩刃风暴』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
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

    # Function_9_11C2 end

    def Function_10_1787(): pass

    label("Function_10_1787")

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

    def lambda_194E():
        OP_98(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_194E)
    Sleep(50)

    def lambda_196B():
        OP_98(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_196B)
    Sleep(50)

    def lambda_1988():
        OP_98(0x103, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1988)
    Sleep(50)

    def lambda_19A5():
        OP_98(0x104, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19A5)
    OP_68(-70000, 1500, -2000, 4500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    #N0018
    NpcTalk(
        0xE,
        "男人的声音",
        "#2P#4S谁……谁来救救我～！！\x02",
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
        "#5P#0107F罗伊德，那里！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#6P#0007F嗯！\x02",
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
        "为、为什么我会这么倒霉……！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xE,
        (
            "……来人啊～！！\x01",
            "没人吗～！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B87():
        OP_9B(0x0, 0xA, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1B87)
    SetChrChipByIndex(0xA, 0x15)
    BeginChrThread(0xA, 1, 0, 3)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    def lambda_1BB4():
        OP_9B(0x0, 0xB, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1BB4)
    SetChrChipByIndex(0xB, 0x15)
    BeginChrThread(0xB, 1, 0, 3)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)

    def lambda_1BE1():
        OP_9B(0x0, 0xC, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1BE1)
    SetChrChipByIndex(0xC, 0x15)
    BeginChrThread(0xC, 1, 0, 3)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)

    def lambda_1C0E():
        OP_9B(0x0, 0xD, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1C0E)
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
            "呜、呜咿咿咿……！！\x01",
            "女神，救救我……！！\x02",
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
        "#5P#0007F──慢着！！\x02",
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

    def lambda_1DCB():
        OP_98(0x101, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DCB)
    Sleep(50)

    def lambda_1DE8():
        OP_98(0x102, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DE8)
    Sleep(50)

    def lambda_1E05():
        OP_98(0x103, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E05)
    Sleep(50)

    def lambda_1E22():
        OP_98(0x104, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E22)

    def lambda_1E3C():
        OP_93(0xA, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1E3C)
    Sleep(50)

    def lambda_1E4C():
        OP_93(0xB, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1E4C)
    Sleep(50)

    def lambda_1E5C():
        OP_93(0xC, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1E5C)
    Sleep(50)

    def lambda_1E6C():
        OP_93(0xD, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1E6C)
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
            "#6P#0302F哈哈，看起来……\x01",
            "正好赶上了\x01",
            "最佳时机啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        "#12P#0206F……是最糟时机才对吧。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#6P#0007F我们是克洛斯贝尔警察局的人！\x02\x03",

            "我们来拖住魔兽，\x01",
            "你趁机快逃！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xE,
        "#5P啊，好的……！\x02",
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
            "#6P#0010F呜……！？\x02\x03",

            "怎么回事，这些魔兽……\x01",
            "气势不是一般的强啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#6P#0107F似乎和栖息在这一带的\x01",
            "其它魔兽完全不同……！\x02\x03",

            "莫非是太古时代的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#12P#0303F看样子，似乎不能\x01",
            "小看这些家伙呢。\x02\x03",

            "#0307F哈……有点意思嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        "#12P#0207F……来了！\x02",
    )

    CloseMessageWindow()

    def lambda_2135():
        OP_9B(0x0, 0xA, 0x0, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2135)
    SetChrChipByIndex(0xA, 0x15)
    BeginChrThread(0xA, 1, 0, 3)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)

    def lambda_2162():
        OP_9B(0x0, 0xB, 0x0, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2162)
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

    # Function_10_1787 end

    def Function_11_21E2(): pass

    label("Function_11_21E2")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B3")
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
    Jump("loc_251F")

    label("loc_24B3")

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

    label("loc_251F")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29BD")
    OP_2C(0x1F, 0x3)
    OP_6F(0x10)

    #C0033
    ChrTalk(
        0x101,
        "#6P#0010F成、成功了吗……！？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#6P#0108F这些魔兽……比看上去\x01",
            "更加强大呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#12P#0301F……嘁，真叫人不爽。\x01",
            "到底是什么东西啊……？\x02",
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

    def lambda_2670():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2670)
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
        "#6P#0005F什、什么……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 1)
    Fade(500)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2736():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2736)
    Sleep(100)

    def lambda_2752():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2752)
    Sleep(100)

    def lambda_276E():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_276E)
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
        "#6P#0106F呀！！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        "#12P#0210F……！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#12P#0310F嘁……\x01",
            "这些怪物……！\x02\x03",

            "在这种精疲力尽的状态下，\x01",
            "难道还要再打一场吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#6P#0010F（不妙，这样下去的话……！）\x02\x03",

            "（必须要想个渡过难关的办法……！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B8A")

    label("loc_29BD")

    PlayBGM("ed7511", 0)
    OP_6F(0x10)

    #C0042
    ChrTalk(
        0x101,
        "#6P#0010F呜……！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        (
            "#6P#0108F这、这些魔兽……\x01",
            "比看上去更加难对付……！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#12P#0310F这些怪物……\x01",
            "到底有多少体力啊……！？\x02",
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
            "#6P#0010F（不妙，这样下去的话……！）\x02\x03",

            "（必须要想个渡过难关的办法……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8A")

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
        "#6P#0005F哎……！？\x02",
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

    def lambda_2CAE():
        OP_98(0x10, 0x4E20, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2CAE)
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
        "#10A#5P#1407F斩──！\x02",
    )
    #Auto

    CloseMessageWindow()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    SetCameraDistance(20250, 6000)
    SetChrChip(0x0, 0x10, 0x3C, 0x1F4)
    SetChrSubChip(0x10, 0x7)
    PlayEffect(0x4, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_92(0x10, 0xFFFF7842, 0xF3C, 0x3E8)

    def lambda_2E3A():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2E3A)

    def lambda_2E4B():
        OP_96(0x10, 0xFFFF7874, 0x1F4, 0xF46, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2E4B)
    Sleep(200)

    def lambda_2E68():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2E68)
    Sound(815, 0, 100, 0)
    Sound(834, 0, 100, 0)
    WaitChrThread(0x10, 2)
    BeginChrThread(0xA, 2, 0, 15)
    WaitChrThread(0x10, 1)
    OP_92(0x10, 0xFFFF85EE, 0xFA, 0x3E8)

    def lambda_2EA0():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2EA0)

    def lambda_2EB1():
        OP_96(0x10, 0xFFFF85EE, 0x1F4, 0xFA, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2EB1)
    Sleep(200)

    def lambda_2ECE():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2ECE)
    WaitChrThread(0x10, 2)
    Sound(815, 0, 100, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0xC, 2, 0, 15)
    WaitChrThread(0x10, 1)
    OP_92(0x10, 0xFFFF7C8E, 0xFFFFE188, 0x3E8)

    def lambda_2F06():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2F06)

    def lambda_2F17():
        OP_96(0x10, 0xFFFF7C8E, 0x1F4, 0xFFFFE188, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2F17)
    Sleep(200)

    def lambda_2F34():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2F34)
    WaitChrThread(0x10, 2)
    Sound(815, 0, 100, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0xD, 2, 0, 15)
    WaitChrThread(0x10, 1)
    OP_92(0x10, 0xFFFF716C, 0xFFFFF830, 0x3E8)

    def lambda_2F6C():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2F6C)

    def lambda_2F7D():
        OP_96(0x10, 0xFFFF716C, 0x1F4, 0xFFFFF830, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2F7D)
    Sleep(200)

    def lambda_2F9A():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2F9A)
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
        "#6P#0005F亚、亚里欧斯先生……！？\x02",
    )

    CloseMessageWindow()
    Sound(531, 0, 100, 0)
    OP_93(0x10, 0x10E, 0x1F4)
    Sleep(500)

    #C0050
    ChrTalk(
        0x10,
        "#11P#1404F……看来赶上了啊。\x02",
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
            "#6P#0305F话、话说～……\x01",
            "大叔你怎么会\x01",
            "出现在这种地方啊！？\x02",
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
            "呵……面对出手相救的人，\x01",
            "这种打招呼的方式还真是过分啊。\x02\x03",

            "……我确认了一下协会的委托，\x01",
            "得知斯克特\x01",
            "来了这里。\x02\x03",

            "因为这个地方比较危险，\x01",
            "所以我想他可能会需要帮忙，\x01",
            "就赶了过来。\x02",
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
            "#6P#0102F……得救了，\x01",
            "真的非常感谢您。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        "#6P#0204F……老实说，真是很幸运。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        (
            "#6P#0306F不对不对，我说，\x01",
            "这出现时机未免巧得过头了吧！\x02\x03",

            "#0301F大叔，你该不会是\x01",
            "躲在一边计算时机，\x01",
            "特意等到关键时刻才出来的吧～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x10,
        "#11P#1404F哈哈……随你说吧。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x11,
        "喂，大家都没事吗？\x02",
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

    def lambda_33E5():
        OP_98(0x11, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_33E5)
    Sleep(50)

    def lambda_3402():
        OP_98(0xE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3402)
    Sleep(50)

    def lambda_341F():
        OP_98(0xF, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_341F)

    def lambda_3439():
        TurnDirection(0x101, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3439)

    def lambda_3446():
        TurnDirection(0x102, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3446)

    def lambda_3453():
        TurnDirection(0x103, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3453)

    def lambda_3460():
        TurnDirection(0x104, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3460)
    WaitChrThread(0x11, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    OP_6F(0x79)

    #C0058
    ChrTalk(
        0x101,
        (
            "#11P#0000F斯克特先生……\x01",
            "那位女士也醒了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x11,
        "#5P嗯，刚刚才醒的。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xF,
        (
            "#6P各位……\x01",
            "真是太谢谢你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xF,
        (
            "#6P特别是两位游击士，\x01",
            "真不知该怎么谢你们才好……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xE,
        "#6P嗯嗯，真是让人叹为观止啊！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xE,
        (
            "#6P那么强悍的魔兽，\x01",
            "竟然一击就打倒了！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xF,
        (
            "#6P那个，斯克特先生……\x01",
            "您能照顾我，我好开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xF,
        (
            "#6P而且，您使用来复枪的技巧……\x01",
            "好厉害哦……⊥\x02",
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
        "#12P喂、喂……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x110, 0x1F4)

    #C0067
    ChrTalk(
        0x11,
        "#11P哈哈，总之，平安无事就好啦。\x02",
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
        "#11P#0012F哈、哈哈……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#11P#0306F呼，结果还是变成\x01",
            "一如既往的老套路了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#11P#0102F呵呵，算啦，这不是也很好嘛。\x01",
            "反正也顺利解救了游客。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        "#11P#0204F总算有个好结果。\x02",
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
        "#5P……亚里欧斯先生？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x10,
        (
            "#11P#1403F……不，没什么。\x02\x03",

            "#1400F话说回来，还是尽快\x01",
            "把他们送回阿尔摩利卡村\x01",
            "为好吧。\x02\x03",

            "#1404F……特别任务支援科，\x01",
            "后方警戒工作就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_384F():
        TurnDirection(0x101, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_384F)
    Sleep(50)

    def lambda_385F():
        TurnDirection(0x102, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_385F)
    Sleep(50)

    def lambda_386F():
        TurnDirection(0x103, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_386F)
    Sleep(50)

    def lambda_387F():
        TurnDirection(0x104, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_387F)
    Sleep(300)

    #C0074
    ChrTalk(
        0x101,
        "#6P#0000F啊……是！\x02",
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

    # Function_11_21E2 end

    def Function_12_38C8(): pass

    label("Function_12_38C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3923")
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x1, 0xFF, 0xFE, 0x80, 0, 1100, 1400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    Sleep(250)
    Jump("Function_12_38C8")

    label("loc_3923")

    Return()

    # Function_12_38C8 end

    def Function_13_3924(): pass

    label("Function_13_3924")

    PlayEffect(0xA, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3977():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3977)
    OP_A6(0xFE, 0xA, 0xA, 0x3E8, 0x9C4)
    SetChrChipByIndex(0xFE, 0x14)
    BeginChrThread(0xFE, 1, 0, 2)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_3924 end

    def Function_14_39B5(): pass

    label("Function_14_39B5")

    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A6(0xFE, 0xA, 0xA, 0x2EE, 0x9C4)
    OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
    Return()

    # Function_14_39B5 end

    def Function_15_3A22(): pass

    label("Function_15_3A22")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_3A22 end

    def Function_16_3A71(): pass

    label("Function_16_3A71")

    TalkBegin(0xFF)
    SetChrName("")

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门紧紧关着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_16_3A71 end

    SaveToFile()

Try(main)
