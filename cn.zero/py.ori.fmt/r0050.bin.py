from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r0050.bin",                # FileName
        "r0050",                    # MapName
        "r0050",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0050", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 2, 0, 3],
    )

    BuildStringList((
        "r0050",                  # 0
        "紫色布丁花",             # 1
        "寒冰至尊",               # 2
        "br0000",                 # 3
        "br0000",                 # 4
        "br0000",                 # 5
        "br0000",                 # 6
        "br0000",                 # 7
        "br0000",                 # 8
        "br0000",                 # 9
        "克洛斯贝尔市·阿尔摩利卡村方向",# 10
        "唐古拉姆门",             # 11
    ))

    ATBonus("ATBonus_368", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_15EA", 6,   12,  0,   3,   0,   6,   2)
    Sepith("Sepith_15E2", 0,   12,  6,   0,   7,   5,   0)
    Sepith("Sepith_1602", 10,  2,   0,   4,   0,   5,   2)
    Sepith("Sepith_15FA", 4,   0,   1,   10,  5,   3,   0)
    Sepith("Sepith_15F2", 12,  20,  10,  28,  11,  2,   5)

    MonsterBattlePostion("MonsterBattlePostion_3C8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_42C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_430", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_434", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_438", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_43C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_440", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 5, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 0, 0, 180)

    # monster count: 10

    BattleInfo(
        "BattleInfo_6C0", 0x0000, 15, 6, 60, 6, 1, 15, 0, "br0000", "Sepith_15EA", 30, 45, 20, 5,
        (
            ("ms69300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms69300.dat", "ms69300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3A8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms69300.dat", "ms66700.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3C8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms69300.dat", "ms69300.dat", "ms66700.dat", "ms68900.dat", 0, 0, 0, 0, "MonsterBattlePostion_3A8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
        )
    )

    BattleInfo(
        "BattleInfo_5F8", 0x0000, 15, 6, 60, 6, 1, 25, 0, "br0000", "Sepith_15E2", 30, 45, 20, 5,
        (
            ("ms66700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms66700.dat", "ms66700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3A8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms66700.dat", "ms69300.dat", "ms66700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3C8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms66700.dat", "ms66700.dat", "ms69300.dat", "ms68900.dat", 0, 0, 0, 0, "MonsterBattlePostion_3A8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
        )
    )

    BattleInfo(
        "BattleInfo_530", 0x0010, 15, 6, 60, 0, 1, 5, 0, "br0000", "Sepith_1602", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_3C8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_3A8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms77400.dat", "ms77400.dat", "ms65500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_3C8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms68900.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_3A8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
        )
    )

    BattleInfo(
        "BattleInfo_468", 0x0000, 15, 6, 60, 6, 1, 40, 0, "br0000", "Sepith_15FA", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3A8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms65500.dat", "ms69300.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3C8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms65500.dat", "ms65500.dat", "ms69300.dat", "ms68900.dat", 0, 0, 0, 0, "MonsterBattlePostion_3A8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
        )
    )

    BattleInfo(
        "BattleInfo_810", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br0000", "Sepith_15F2", 40, 35, 25, 0,
        (
            ("ms63701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3A8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3C8", "MonsterBattlePostion_428", "ed7400", "ed7403", "ATBonus_368"),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_788", 0x0000, 15, 6, 0, 0, 1, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66700.dat", "ms69300.dat", "ms66700.dat", "ms69300.dat", "ms66700.dat", "ms66700.dat", 0, 0, "MonsterBattlePostion_3A8", "MonsterBattlePostion_428", "ed7401", "ed7403", "ATBonus_368"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7CC", 0x0000, 30, 6, 0, 0, 1, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63100.dat", "ms63100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_448", "MonsterBattlePostion_428", "ed7401", "ed7403", "ATBonus_368"),
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
        "monster/ch65550.itc",               # 10
        "monster/ch65551.itc",               # 11
        "monster/ch77450.itc",               # 12
        "monster/ch77450.itc",               # 13
        "monster/ch66750.itc",               # 14
        "monster/ch66750.itc",               # 15
        "monster/ch69350.itc",               # 16
        "monster/ch69351.itc",               # 17
        "monster/ch63150.itc",               # 18
        "monster/ch63150.itc",               # 19
        "monster/ch63750.itc",               # 1A
        "monster/ch63751.itc",               # 1B
    ))

    DeclNpc(85589,   4500,    20450,   0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(98000,   2750,    11000,   0,    484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(12810,   -14760,  -4000,   0x1010000,    "BattleInfo_6C0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(22410,   32450,   -2000,   0x1010000,    "BattleInfo_5F8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(57420,   -5890,   -2000,   0x1010000,    "BattleInfo_530", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(81820,   8280,    4000,    0x1010000,    "BattleInfo_6C0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(76670,   -19800,  850,     0x1010000,    "BattleInfo_468", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(104220,  -20140,  2009,    0x1010000,    "BattleInfo_5F8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(95910,   800,     2009,    0x1010000,    "BattleInfo_530", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(20360,   21750,   -2000,   0x1010000,    "BattleInfo_810", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(49490,   -11630,  -2000,   0x1010000,    "BattleInfo_810", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(104110,  -1970,   2000,    0x1010000,    "BattleInfo_810", 0,   26,  0xFFFF, 8,  9)

    DeclActor(85590,   4000,    20450,   1200,    85590,   5000,    20450,   0x007C, 0,  4,  0x0000)
    DeclActor(82810,   4000,    20550,   1200,    82810,   5000,    20550,   0x007C, 0,  5,  0x0000)
    DeclActor(98000,   2000,    11000,   1200,    98000,   3000,    11000,   0x007C, 0,  6,  0x0000)
    DeclActor(84940,   4000,    2310,    1200,    84940,   4000,    2310,    0x007C, 0,  7,  0x0000)
    DeclActor(109990,  2009,    -27160,  1500,    109990,  3710,    -27160,  0x007C, 0,  9,  0x0000)

    PlaceName(-15.0, 0.0, -10.0, 0x0000, 0x0000, "克洛斯贝尔市·阿尔摩利卡村方向")
    PlaceName(150.0, 0.0, -27.5, 0x0000, 0x0000, "唐古拉姆门")

    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 1])                         # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 9

    ScpFunction((
        "Function_0_94C",          # 00, 0
        "Function_1_96B",          # 01, 1
        "Function_2_988",          # 02, 2
        "Function_3_C0A",          # 03, 3
        "Function_4_EFF",          # 04, 4
        "Function_5_10F9",         # 05, 5
        "Function_6_124E",         # 06, 6
        "Function_7_14D7",         # 07, 7
        "Function_8_14EB",         # 08, 8
        "Function_9_1509",         # 09, 9
    ))


    def Function_0_94C(): pass

    label("Function_0_94C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96A")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_94C")

    label("loc_96A")

    Return()

    # Function_0_94C end

    def Function_1_96B(): pass

    label("Function_1_96B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_987")
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_96B")

    label("loc_987")

    Return()

    # Function_1_96B end

    def Function_2_988(): pass

    label("Function_2_988")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C06")
    ClearScenarioFlags(0x7A, 0)
    ClearScenarioFlags(0x7A, 1)
    ClearScenarioFlags(0x7A, 2)
    ClearScenarioFlags(0x7A, 3)
    ClearScenarioFlags(0x7A, 4)
    ClearScenarioFlags(0x7A, 5)
    ClearScenarioFlags(0x7A, 6)
    ClearScenarioFlags(0x7A, 7)
    ClearScenarioFlags(0x7B, 0)
    ClearScenarioFlags(0x7B, 1)
    ClearScenarioFlags(0x7B, 2)
    ClearScenarioFlags(0x7B, 3)
    ClearScenarioFlags(0x7B, 4)
    ClearScenarioFlags(0x7B, 5)
    ClearScenarioFlags(0x7B, 6)
    ClearScenarioFlags(0x7B, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E5")
    SetScenarioFlags(0x7A, 0)

    label("loc_9E5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FB")
    SetScenarioFlags(0x7A, 1)

    label("loc_9FB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A11")
    SetScenarioFlags(0x7A, 2)

    label("loc_A11")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A27")
    SetScenarioFlags(0x7A, 3)

    label("loc_A27")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3D")
    SetScenarioFlags(0x7A, 4)

    label("loc_A3D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A53")
    SetScenarioFlags(0x7A, 5)

    label("loc_A53")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A69")
    SetScenarioFlags(0x7A, 6)

    label("loc_A69")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7F")
    SetScenarioFlags(0x7A, 7)

    label("loc_A7F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A95")
    SetScenarioFlags(0x7B, 0)

    label("loc_A95")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAB")
    SetScenarioFlags(0x7B, 1)

    label("loc_AAB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC1")
    SetScenarioFlags(0x7B, 2)

    label("loc_AC1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD7")
    SetScenarioFlags(0x7B, 3)

    label("loc_AD7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AED")
    SetScenarioFlags(0x7B, 4)

    label("loc_AED")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B03")
    SetScenarioFlags(0x7B, 5)

    label("loc_B03")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B19")
    SetScenarioFlags(0x7B, 6)

    label("loc_B19")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2F")
    SetScenarioFlags(0x7B, 7)

    label("loc_B2F")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6A")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_C06")

    label("loc_B6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B81")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_C06")

    label("loc_B81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B98")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_C06")

    label("loc_B98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAF")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_C06")

    label("loc_BAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC6")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_C06")

    label("loc_BC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDD")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_C06")

    label("loc_BDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF4")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_C06")

    label("loc_BF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C06")
    SetScenarioFlags(0x7C, 7)

    label("loc_C06")

    Call(0, 8)
    Return()

    # Function_2_988 end

    def Function_3_C0A(): pass

    label("Function_3_C0A")

    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6F")
    OP_70(0x0, 0x0)
    Jump("loc_E73")

    label("loc_E6F")

    OP_70(0x0, 0x1E)

    label("loc_E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E86")
    OP_70(0x1, 0x0)
    Jump("loc_E8A")

    label("loc_E86")

    OP_70(0x1, 0x1E)

    label("loc_E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9D")
    OP_70(0x2, 0x0)
    Jump("loc_EA1")

    label("loc_E9D")

    OP_70(0x2, 0x1E)

    label("loc_EA1")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 7)), scpexpr(EXPR_END)), "loc_EFE")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 84940, 4000, 2310, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_EFE")

    Return()

    # Function_3_C0A end

    def Function_4_EFF(): pass

    label("Function_4_EFF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BB")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF8")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F58():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F58)

    def lambda_F72():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F72)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0001
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
    Battle("BattleInfo_788", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_FD9"),
        (2, "loc_FE8"),
        (1, "loc_FF5"),
        (SWITCH_DEFAULT, "loc_FF8"),
    )


    label("loc_FD9")

    SetScenarioFlags(0x74, 4)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_FF8")

    label("loc_FE8")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_FF5")

    OP_B7(0x0)
    Return()

    label("loc_FF8")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('冥王铃', 1)"), scpexpr(EXPR_END)), "loc_104F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '冥王铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x101, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_10B6")

    label("loc_104F")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '冥王铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '冥王铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_10B6")

    Jump("loc_10ED")

    label("loc_10BB")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_10ED")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_EFF end

    def Function_5_10F9(): pass

    label("Function_5_10F9")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121F")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 40)
    AddSepith(0x1, 40)
    AddSepith(0x2, 40)
    AddSepith(0x3, 40)
    AddSepith(0x4, 40)
    AddSepith(0x5, 40)
    AddSepith(0x6, 40)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×４０\x01\x07\x02",

            "#57I水之耀晶片×４０\x01\x07\x02",

            "#58I火之耀晶片×４０\x01\x07\x02",

            "#59I风之耀晶片×４０\x01\x07\x02",

            "#60I时之耀晶片×４０\x01\x07\x02",

            "#61I空之耀晶片×４０\x01\x07\x02",

            "#62I幻之耀晶片×４０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x101, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_123C")

    label("loc_121F")


    #A0006
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

    label("loc_123C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_10F9 end

    def Function_6_124E(): pass

    label("Function_6_124E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12DD")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从宝箱中感觉到了高级魔兽的气息。\x01",
            "【推测魔兽等级３０】\x01",
            "要打开宝箱吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12DD")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_12DD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1499")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D6")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1336():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1336)

    def lambda_1350():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1350)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x9, 1)
    Battle("BattleInfo_7CC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_13B7"),
        (2, "loc_13C6"),
        (1, "loc_13D3"),
        (SWITCH_DEFAULT, "loc_13D6"),
    )


    label("loc_13B7")

    SetScenarioFlags(0x72, 0)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_13D6")

    label("loc_13C6")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_13D3")

    OP_B7(0x0)
    Return()

    label("loc_13D6")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('省ＥＰ２', 1)"), scpexpr(EXPR_END)), "loc_142D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x101, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1494")

    label("loc_142D")

    FadeToDark(300, 0, 100)

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1494")

    Jump("loc_14CB")

    label("loc_1499")

    FadeToDark(300, 0, 100)

    #A0011
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

    label("loc_14CB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_124E end

    def Function_7_14D7(): pass

    label("Function_7_14D7")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 7)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_14D7 end

    def Function_8_14EB(): pass

    label("Function_8_14EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1508")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_1508")

    Return()

    # Function_8_14EB end

    def Function_9_1509(): pass

    label("Function_9_1509")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东·唐古拉姆门\x01",
            "西·克洛斯贝尔市　２０６赛尔矩\x01",
            "　　阿尔摩利卡村　２３２赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_1509 end

    SaveToFile()

Try(main)
