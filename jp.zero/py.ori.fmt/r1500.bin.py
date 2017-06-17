from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1500.bin",                # FileName
        "r1500",                    # MapName
        "r1500",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r1500", "r0000_1", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, -65000, 0, 0, 1, 96, 0, 1, 0, 2],
    )

    BuildStringList((
        "r1500",                  # 0
        "市民",                   # 1
        "市民",                   # 2
        "市民",                   # 3
        "市民",                   # 4
        "市民",                   # 5
        "市民",                   # 6
        "市民",                   # 7
        "捜査官",                 # 8
        "市民",                   # 9
        "市民",                   # 10
        "女の子",                 # 11
        "市民",                   # 12
        "観光客",                 # 13
        "市民",                   # 14
        "市民",                   # 15
        "市民",                   # 16
        "市民",                   # 17
        "市民",                   # 18
        "観光客",                 # 19
        "記者",                   # 20
        "記者",                   # 21
        "観光客",                 # 22
        "観光客",                 # 23
        "観光客",                 # 24
        "観光客",                 # 25
        "観光客",                 # 26
        "観光客",                 # 27
        "観光客",                 # 28
        "観光客",                 # 29
        "市民",                   # 30
        "ビリー",                 # 31
        "交通課の職員",           # 32
        "レイモンド捜査官",       # 33
        "エマ捜査官",             # 34
        "ドノバン警部",           # 35
        "バス",                   # 36
        "バス待ち",               # 37
        "バス待ち",               # 38
        "バス待ち",               # 39
        "バス待ち",               # 40
        "交通課の職員",           # 41
        "ツァイト",               # 42
        "ビリーのバン",           # 43
        "SE制御",                 # 44
        "br1500",                 # 45
        "br1500",                 # 46
        "br1500",                 # 47
        "br1500",                 # 48
        "br1500",                 # 49
        "クロスベル市方面",       # 50
        "ウルスラ医科大学方面",   # 51
        "クロスベル空港方面",     # 52
    ))

    ATBonus("ATBonus_8B0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_9F1A", 4,   2,   0,   8,   0,   3,   2)
    Sepith("Sepith_9F32", 8,   2,   0,   0,   3,   0,   5)
    Sepith("Sepith_9F2A", 0,   8,   0,   4,   4,   2,   0)
    Sepith("Sepith_9F22", 8,   0,   5,   2,   0,   0,   4)
    Sepith("Sepith_9F52", 2,   8,   0,   6,   2,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_910", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_914", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_918", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_91C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_920", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_924", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_928", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_92C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_970", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_974", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_978", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_97C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_980", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_984", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_988", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_98C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_8F0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_8FC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_900", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_904", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_908", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_90C", 2, 13, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_990", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_9F1A", 30, 45, 20, 5,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
        )
    )

    BattleInfo(
        "BattleInfo_BE8", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_9F32", 30, 45, 20, 5,
        (
            ("ms65800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms65800.dat", "ms65800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms65800.dat", "ms63600.dat", "ms65800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms65800.dat", "ms65800.dat", "ms66600.dat", "ms65800.dat", 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
        )
    )

    BattleInfo(
        "BattleInfo_B20", 0x0010, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_9F2A", 60, 25, 10, 5,
        (
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms63600.dat", "ms66600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "ms63600.dat", 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms63600.dat", "ms63600.dat", "ms62100.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
        )
    )

    BattleInfo(
        "BattleInfo_A58", 0x0000, 12, 6, 45, 10, 1, 45, 0, "br1500", "Sepith_9F22", 30, 45, 20, 5,
        (
            ("ms66600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms66600.dat", "ms66600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms66600.dat", "ms62100.dat", "ms66600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms66600.dat", "ms66600.dat", "ms69700.dat", "ms66600.dat", 0, 0, 0, 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
        )
    )

    BattleInfo(
        "BattleInfo_CB0", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_9F52", 30, 45, 20, 5,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", "ms69800.dat", 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
        )
    )

    AddCharChip((
        "chr/ch28100.itc",                   # 00
        "chr/ch21900.itc",                   # 01
        "chr/ch20800.itc",                   # 02
        "chr/ch24400.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch21600.itc",                   # 05
        "chr/ch21100.itc",                   # 06
        "chr/ch23600.itc",                   # 07
        "chr/ch21200.itc",                   # 08
        "chr/ch21300.itc",                   # 09
        "chr/ch21000.itc",                   # 0A
        "chr/ch20700.itc",                   # 0B
        "chr/ch20300.itc",                   # 0C
        "chr/ch21800.itc",                   # 0D
        "chr/ch20000.itc",                   # 0E
        "chr/ch20100.itc",                   # 0F
        "chr/ch20200.itc",                   # 10
        "chr/ch20400.itc",                   # 11
        "chr/ch23700.itc",                   # 12
        "chr/ch24500.itc",                   # 13
        "chr/ch27800.itc",                   # 14
        "chr/ch28100.itc",                   # 15
        "chr/ch30200.itc",                   # 16
        "chr/ch30500.itc",                   # 17
        "chr/ch30300.itc",                   # 18
        "chr/ch26800.itc",                   # 19
        "chr/ch22100.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
        "monster/ch62150.itc",               # 1E
        "monster/ch62151.itc",               # 1F
        "monster/ch66650.itc",               # 20
        "monster/ch66651.itc",               # 21
        "monster/ch63650.itc",               # 22
        "monster/ch63650.itc",               # 23
        "monster/ch65850.itc",               # 24
        "monster/ch65851.itc",               # 25
        "monster/ch69750.itc",               # 26
        "monster/ch69750.itc",               # 27
    ))

    DeclNpc(-9779,   180,     -10890,  135,  389,  0x0, 0,   1,   0,   0,   0,   0,   35,  255,  0)
    DeclNpc(-9560,   180,     -8470,   135,  389,  0x0, 0,   2,   0,   0,   0,   0,   36,  255,  0)
    DeclNpc(-9479,   180,     -7039,   315,  389,  0x0, 0,   3,   0,   0,   0,   0,   37,  255,  0)
    DeclNpc(-9409,   180,     -5860,   225,  389,  0x0, 0,   4,   0,   0,   0,   0,   38,  255,  0)
    DeclNpc(-8899,   180,     -4000,   90,   389,  0x0, 0,   5,   0,   0,   0,   0,   39,  255,  0)
    DeclNpc(-7699,   180,     -4000,   270,  389,  0x0, 0,   6,   0,   0,   0,   0,   40,  255,  0)
    DeclNpc(-10020,  180,     -9489,   180,  389,  0x0, 0,   7,   0,   0,   0,   0,   41,  255,  0)
    DeclNpc(12989,   0,       -17559,  270,  389,  0x0, 0,   20,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(-9810,   180,     -9920,   180,  389,  0x0, 0,   9,   0,   0,   0,   0,   43,  255,  0)
    DeclNpc(-7010,   180,     -4260,   90,   389,  0x0, 0,   10,  0,   0,   0,   0,   44,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   11,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   12,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10609,   0,       -14939,  270,  389,  0x0, 0,   13,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(10609,   0,       -14939,  270,  389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(10609,   0,       -14939,  270,  389,  0x0, 0,   1,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   14,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   15,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(10609,   0,       -14939,  90,   389,  0x0, 0,   16,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(10609,   0,       -14939,  270,  389,  0x0, 0,   25,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   3,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   19,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   18,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   26,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(5340,    0,       -20360,  0,    389,  0x0, 0,   19,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(5340,    0,       -19159,  180,  389,  0x0, 0,   3,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   1,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   13,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(10609,   0,       -14939,  270,  389,  0x0, 0,   20,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(4980,    0,       -12670,  270,  389,  0x0, 0,   7,   0,   0,   0,   0,   31,  255,  0)
    DeclNpc(2210,    0,       -34220,  270,  389,  0x0, 0,   21,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(-5639,   180,     -4260,   270,  389,  0x0, 0,   22,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(13060,   0,       -16149,  180,  389,  0x0, 0,   23,  0,   0,   0,   0,   45,  255,  0)
    DeclNpc(11449,   0,       -15000,  180,  389,  0x0, 0,   24,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-18740,  -70990,  0,       0x1010000,    "BattleInfo_990", 0,   30,  0xFFFF, 0,  1)
    DeclMonster(-19320,  -73460,  10,      0x1010000,    "BattleInfo_990", 0,   30,  0xFFFF, 0,  1)
    DeclMonster(-9910,   -96620,  10,      0x1010000,    "BattleInfo_BE8", 0,   36,  0xFFFF, 6,  7)
    DeclMonster(-20260,  -97980,  0,       0x1010000,    "BattleInfo_B20", 0,   34,  0xFFFF, 4,  5)
    DeclMonster(16920,   -84000,  10,      0x1010000,    "BattleInfo_BE8", 0,   36,  0xFFFF, 6,  7)
    DeclMonster(22580,   -65740,  10,      0x1010000,    "BattleInfo_A58", 0,   32,  0xFFFF, 2,  3)
    DeclMonster(32310,   -111280, 0,       0x1010000,    "BattleInfo_CB0", 0,   38,  0xFFFF, 8,  9)
    DeclMonster(46440,   -108530, 900,     0x1010000,    "BattleInfo_A58", 0,   32,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 66,  14.0,                  -17.5,                 -0.5,                  100.0,                 [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.09999999403953552,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -7.0,                  1.7499998807907104,    0.09999999403953552,   1.0])

    DeclActor(-10300,  180,     -13000,  1500,    -10300,  1680,    -13000,  0x007C, 0,  47, 0x0000)
    DeclActor(53350,   900,     -104390, 1200,    67060,   -5900,   -100200, 0x007C, 0,  46, 0x0000)
    DeclActor(22470,   0,       -63690,  1200,    22470,   0,       -63690,  0x007C, 0,  3,  0x0000)
    DeclActor(8160,    0,       -11670,  1200,    8160,    2000,    -11670,  0x007C, 0,  10, 0x0000)
    DeclActor(44690,   900,     -108690, 7500,    44690,   900,     -108690, 0x007C, 0,  64, 0x0000)
    DeclActor(9210,    0,       -24210,  1500,    9210,    1700,    -24210,  0x007C, 0,  69, 0x0000)

    PlaceName(2.0, 0.0, 20.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(-27.0, 0.0, -159.0, 0x0000, 0x0000, "ウルスラ医科大学方面")
    PlaceName(45.0, 0.0, -24.0, 0x0000, 0x0000, "クロスベル空港方面")
    PlaceName(-10.649999618530273, 0.0, -11.800000190734863, 0x0000, 0x0055, "")
    PlaceName(8.25, 0.0, -10.0, 0x0000, 0x0056, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5, 6, 7])              # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9

    ScpFunction((
        "Function_0_F08",          # 00, 0
        "Function_1_FC0",          # 01, 1
        "Function_2_15D1",         # 02, 2
        "Function_3_19FB",         # 03, 3
        "Function_4_1A0F",         # 04, 4
        "Function_5_1A5C",         # 05, 5
        "Function_6_1B1D",         # 06, 6
        "Function_7_1C9F",         # 07, 7
        "Function_8_1D34",         # 08, 8
        "Function_9_22E6",         # 09, 9
        "Function_10_23D5",        # 0A, 10
        "Function_11_23E3",        # 0B, 11
        "Function_12_2450",        # 0C, 12
        "Function_13_24CC",        # 0D, 13
        "Function_14_2564",        # 0E, 14
        "Function_15_2698",        # 0F, 15
        "Function_16_2718",        # 10, 16
        "Function_17_27A2",        # 11, 17
        "Function_18_2880",        # 12, 18
        "Function_19_2908",        # 13, 19
        "Function_20_2986",        # 14, 20
        "Function_21_2A12",        # 15, 21
        "Function_22_2A8F",        # 16, 22
        "Function_23_2B04",        # 17, 23
        "Function_24_2B90",        # 18, 24
        "Function_25_2BEE",        # 19, 25
        "Function_26_2C79",        # 1A, 26
        "Function_27_2CC0",        # 1B, 27
        "Function_28_2D09",        # 1C, 28
        "Function_29_2DA8",        # 1D, 29
        "Function_30_2E40",        # 1E, 30
        "Function_31_2EC8",        # 1F, 31
        "Function_32_3189",        # 20, 32
        "Function_33_3579",        # 21, 33
        "Function_34_35D2",        # 22, 34
        "Function_35_3B78",        # 23, 35
        "Function_36_3BB8",        # 24, 36
        "Function_37_3C0E",        # 25, 37
        "Function_38_3D17",        # 26, 38
        "Function_39_3DBA",        # 27, 39
        "Function_40_3E29",        # 28, 40
        "Function_41_3E95",        # 29, 41
        "Function_42_3EF8",        # 2A, 42
        "Function_43_40D6",        # 2B, 43
        "Function_44_41B1",        # 2C, 44
        "Function_45_4220",        # 2D, 45
        "Function_46_445E",        # 2E, 46
        "Function_47_4752",        # 2F, 47
        "Function_48_4870",        # 30, 48
        "Function_49_602E",        # 31, 49
        "Function_50_6072",        # 32, 50
        "Function_51_669D",        # 33, 51
        "Function_52_66B9",        # 34, 52
        "Function_53_66D8",        # 35, 53
        "Function_54_66E8",        # 36, 54
        "Function_55_6704",        # 37, 55
        "Function_56_6729",        # 38, 56
        "Function_57_6E9D",        # 39, 57
        "Function_58_6ED2",        # 3A, 58
        "Function_59_6EE3",        # 3B, 59
        "Function_60_6F97",        # 3C, 60
        "Function_61_6FE4",        # 3D, 61
        "Function_62_7027",        # 3E, 62
        "Function_63_896A",        # 3F, 63
        "Function_64_8A45",        # 40, 64
        "Function_65_970C",        # 41, 65
        "Function_66_9A58",        # 42, 66
        "Function_67_9C34",        # 43, 67
        "Function_68_9DD4",        # 44, 68
        "Function_69_9E73",        # 45, 69
    ))


    def Function_0_F08(): pass

    label("Function_0_F08")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_F48"),
        (1, "loc_F54"),
        (2, "loc_F60"),
        (3, "loc_F6C"),
        (4, "loc_F78"),
        (5, "loc_F84"),
        (6, "loc_F90"),
        (SWITCH_DEFAULT, "loc_F9C"),
    )


    label("loc_F48")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_FA8")

    label("loc_F54")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_FA8")

    label("loc_F60")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_FA8")

    label("loc_F6C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_FA8")

    label("loc_F78")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_FA8")

    label("loc_F84")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_FA8")

    label("loc_F90")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FA8")

    label("loc_F9C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FA8")

    label("loc_FA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FBF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FA8")

    label("loc_FBF")

    Return()

    # Function_0_F08 end

    def Function_1_FC0(): pass

    label("Function_1_FC0")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xF9, 5)
    SetScenarioFlags(0xFB, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE5")
    SetMapFlags(0x10000000)
    Event(0, 62)

    label("loc_FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_FF4")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 50)

    label("loc_FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1070")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, -10010, 180, -11740, 180)
    SetChrPos(0xB, -10010, 180, -10540, 180)
    SetChrPos(0xE, -10010, 180, -9240, 180)
    SetChrPos(0xF, -10010, 180, -8039, 180)
    SetChrPos(0x10, -10010, 180, -6840, 180)
    Jump("loc_1158")

    label("loc_1070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_10B4")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0xF, 15000, 0, -16570, 0)
    SetChrPos(0x29, 15000, 0, -15170, 180)
    Jump("loc_1158")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_10D1")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x28, 0x80)
    Jump("loc_1158")

    label("loc_10D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 4)), scpexpr(EXPR_END)), "loc_10DF")
    Jump("loc_1158")

    label("loc_10DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_10F7")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_1158")

    label("loc_10F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_END)), "loc_1105")
    Jump("loc_1158")

    label("loc_1105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1131")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x27, 0x80)
    Jump("loc_1158")

    label("loc_1131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_1158")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x27, 0x80)

    label("loc_1158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1166")
    Jump("loc_12E5")

    label("loc_1166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1174")
    Jump("loc_12E5")

    label("loc_1174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1187")
    ClearChrFlags(0x25, 0x80)
    Jump("loc_12E5")

    label("loc_1187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1195")
    Jump("loc_12E5")

    label("loc_1195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_11B2")
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x10)
    Jump("loc_12E5")

    label("loc_11B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_11D9")
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x21, 0x10)
    Jump("loc_12E5")

    label("loc_11D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_11FB")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x10)
    SetChrFlags(0x1F, 0x10)
    Jump("loc_12E5")

    label("loc_11FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1213")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_12E5")

    label("loc_1213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_125B")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1256")
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, 11450, 0, -16500, 0)
    ClearChrFlags(0x2A, 0x80)

    label("loc_1256")

    Jump("loc_12E5")

    label("loc_125B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_126E")
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_12E5")

    label("loc_126E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1281")
    ClearChrFlags(0x19, 0x80)
    Jump("loc_12E5")

    label("loc_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1299")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_12E5")

    label("loc_1299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_12AC")
    ClearChrFlags(0x16, 0x80)
    Jump("loc_12E5")

    label("loc_12AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_12BF")
    ClearChrFlags(0x15, 0x80)
    Jump("loc_12E5")

    label("loc_12BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_12D2")
    ClearChrFlags(0x14, 0x80)
    Jump("loc_12E5")

    label("loc_12D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_12E5")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)

    label("loc_12E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12F3")
    Jump("loc_1303")

    label("loc_12F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1303")
    Event(0, 4)

    label("loc_1303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1319")
    Event(0, 63)

    label("loc_1319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_1328")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 7)

    label("loc_1328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_1340")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)

    label("loc_1340")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15D0")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AF")
    SetScenarioFlags(0x7A, 0)

    label("loc_13AF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C5")
    SetScenarioFlags(0x7A, 1)

    label("loc_13C5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13DB")
    SetScenarioFlags(0x7A, 2)

    label("loc_13DB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F1")
    SetScenarioFlags(0x7A, 3)

    label("loc_13F1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1407")
    SetScenarioFlags(0x7A, 4)

    label("loc_1407")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141D")
    SetScenarioFlags(0x7A, 5)

    label("loc_141D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1433")
    SetScenarioFlags(0x7A, 6)

    label("loc_1433")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1449")
    SetScenarioFlags(0x7A, 7)

    label("loc_1449")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145F")
    SetScenarioFlags(0x7B, 0)

    label("loc_145F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1475")
    SetScenarioFlags(0x7B, 1)

    label("loc_1475")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148B")
    SetScenarioFlags(0x7B, 2)

    label("loc_148B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A1")
    SetScenarioFlags(0x7B, 3)

    label("loc_14A1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B7")
    SetScenarioFlags(0x7B, 4)

    label("loc_14B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14CD")
    SetScenarioFlags(0x7B, 5)

    label("loc_14CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E3")
    SetScenarioFlags(0x7B, 6)

    label("loc_14E3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F9")
    SetScenarioFlags(0x7B, 7)

    label("loc_14F9")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1534")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_15D0")

    label("loc_1534")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154B")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_15D0")

    label("loc_154B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1562")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_15D0")

    label("loc_1562")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1579")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_15D0")

    label("loc_1579")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1590")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_15D0")

    label("loc_1590")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A7")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_15D0")

    label("loc_15A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15BE")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_15D0")

    label("loc_15BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D0")
    SetScenarioFlags(0x7C, 7)

    label("loc_15D0")

    Return()

    # Function_1_FC0 end

    def Function_2_15D1(): pass

    label("Function_2_15D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1629")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_161B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1624")

    label("loc_161B")

    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1624")

    Jump("loc_167B")

    label("loc_1629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_167B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1672")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_167B")

    label("loc_1672")

    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_167B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1694")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    Jump("loc_169A")

    label("loc_1694")

    OP_10(0x0, 0x1)
    OP_10(0x5, 0x0)

    label("loc_169A")

    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16E7")
    SetMapFlags(0x2000)
    OP_E0(0x1)
    ClearScenarioFlags(0x1, 0)
    Jump("loc_16FB")

    label("loc_16E7")

    ClearMapFlags(0x2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FB")
    OP_E0(0x0)
    SetScenarioFlags(0x1, 0)

    label("loc_16FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1709")
    Jump("loc_172B")

    label("loc_1709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_172B")
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetMapObjFlags(0x2, 0x2)

    label("loc_172B")

    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_177C")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD2, 0xAE, 0x9B, 0x5, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")

    label("loc_177C")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_178E")
    Jump("loc_17CF")

    label("loc_178E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_17CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_17A8")
    Jump("loc_17CF")

    label("loc_17A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_17BA")
    Jump("loc_17CF")

    label("loc_17BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_17CF")
    OP_66(0x4, 0x1)
    OP_65(0x1, 0x1)

    label("loc_17CF")

    SetMapObjFlags(0x3, 0x4)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_180C")
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    ClearMapObjFlags(0x3, 0x4)
    OP_66(0x3, 0x1)
    Jump("loc_1811")

    label("loc_180C")

    OP_16(0x3, 0x4, 0x1, 0x0)

    label("loc_1811")

    OP_1B(0x4, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1837")
    OP_1B(0x4, 0x0, 0x41)

    label("loc_1837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1853")
    OP_1B(0x4, 0x0, 0x41)

    label("loc_1853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1866")
    OP_1B(0x4, 0x0, 0x41)

    label("loc_1866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1888")
    OP_1B(0x4, 0x0, 0x41)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1888")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1888")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18B0")
    OP_1B(0x2, 0x0, 0x43)

    label("loc_18B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18C3")
    OP_1B(0x2, 0x0, 0x43)

    label("loc_18C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18D6")
    OP_1B(0x2, 0x0, 0x43)

    label("loc_18D6")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 0)), scpexpr(EXPR_END)), "loc_1933")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 22470, 0, -63690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_1933")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 67060, -5900, -100200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19B7")
    OP_24(0x7D)
    Jump("loc_19FA")

    label("loc_19B7")

    SoundDistance(0x7D, 0x34C6, 0x0, 0xFFFD8D16, 0x15F90, 0x11170, 0x64, 0x0)
    OP_E1(0x9D4E, 0x118, 0xFFFE0909)
    OP_E1(0xE06A, 0x384, 0xFFFE9238)
    OP_E1(0xFCDA, 0x5A, 0xFFFF282E)

    label("loc_19FA")

    Return()

    # Function_2_15D1 end

    def Function_3_19FB(): pass

    label("Function_3_19FB")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 0)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_3_19FB end

    def Function_4_1A0F(): pass

    label("Function_4_1A0F")

    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetMapObjFlags(0x2, 0x1000)
    OP_78(0x2, 0x32)
    OP_49()
    SetChrPos(0x32, 2000, 1000, 14000, 0)
    OP_D3(0x32, 0x0, 0x2BF20, 0x0, 0x0)
    Return()

    # Function_4_1A0F end

    def Function_5_1A5C(): pass

    label("Function_5_1A5C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "聖ウルスラ医科大学\x01",          # 0
            "分岐停留所（中州付近）\x01",      # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF5")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1B15")

    label("loc_1AF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B15")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_1B15")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_1A5C end

    def Function_6_1B1D(): pass

    label("Function_6_1B1D")

    Fade(1000)
    OP_68(0, 600, -32000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -9800, 180, -11100, 89)
    SetChrPos(0x1, -9800, 180, -10100, 89)
    SetChrPos(0x2, -9800, 180, -9100, 89)
    SetChrPos(0x3, -9800, 180, -8100, 89)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_78(0x1, 0x2B)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x2B, 0, 0, -40000, 0)
    OP_D3(0x2B, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1BF7():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_1BF7)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    Sleep(2500)
    Fade(500)
    OP_68(-10500, 780, -11600, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x2B, -6300, 0, -21000, 0)

    def lambda_1C64():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFD314, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_1C64)
    WaitChrThread(0x2B, 1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x1)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_6_1B1D end

    def Function_7_1C9F(): pass

    label("Function_7_1C9F")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -9830, 180, -11430, 90)
    SetChrPos(0x1, -9830, 180, -11430, 90)
    SetChrPos(0x2, -9830, 180, -11430, 90)
    SetChrPos(0x3, -9830, 180, -11430, 90)
    OP_68(-9830, 780, -11430, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_7_1C9F end

    def Function_8_1D34(): pass

    label("Function_8_1D34")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22DE")

    Menu(
        0,
        32,
        26,
        1,
        (
            "警備隊車両で移動をする\x01",      # 0
            "ここで休憩をする\x01",            # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_227B")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DE4")
    MenuCmd(1, 1, "★クロスベル市・中央広場")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1E00")

    label("loc_1DE4")

    MenuCmd(1, 1, "　クロスベル市・中央広場")

    label("loc_1E00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E32")
    MenuCmd(1, 1, "★クロスベル市・東出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1E4C")

    label("loc_1E32")

    MenuCmd(1, 1, "　クロスベル市・東出口")

    label("loc_1E4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E7E")
    MenuCmd(1, 1, "★クロスベル市・西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1E98")

    label("loc_1E7E")

    MenuCmd(1, 1, "　クロスベル市・西出口")

    label("loc_1E98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ECA")
    MenuCmd(1, 1, "★クロスベル市・南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1EE4")

    label("loc_1ECA")

    MenuCmd(1, 1, "　クロスベル市・南出口")

    label("loc_1EE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F16")
    MenuCmd(1, 1, "★クロスベル市・北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1F30")

    label("loc_1F16")

    MenuCmd(1, 1, "　クロスベル市・北出口")

    label("loc_1F30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F5A")
    MenuCmd(1, 1, "★タングラム門")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1F6C")

    label("loc_1F5A")

    MenuCmd(1, 1, "　タングラム門")

    label("loc_1F6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F96")
    MenuCmd(1, 1, "★ベルガード門")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1FA8")

    label("loc_1F96")

    MenuCmd(1, 1, "　ベルガード門")

    label("loc_1FA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD6")
    MenuCmd(1, 1, "★ウルスラ医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1FEC")

    label("loc_1FD6")

    MenuCmd(1, 1, "　ウルスラ医科大学")

    label("loc_1FEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2016")
    MenuCmd(1, 1, "★アルモリカ村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_2028")

    label("loc_2016")

    MenuCmd(1, 1, "　アルモリカ村")

    label("loc_2028")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2054")
    MenuCmd(1, 1, "★マインツ鉱山町")
    MenuCmd(3, 1, 0x9)
    Jump("loc_2068")

    label("loc_2054")

    MenuCmd(1, 1, "　マインツ鉱山町")

    label("loc_2068")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_209A")
    MenuCmd(1, 1, "★マインツ山道・隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_20B4")

    label("loc_209A")

    MenuCmd(1, 1, "　マインツ山道・隧道内")

    label("loc_20B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DA")
    MenuCmd(1, 1, "★星見の塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_20E8")

    label("loc_20DA")

    MenuCmd(1, 1, "　星見の塔")

    label("loc_20E8")

    MenuCmd(1, 1, "　やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_226C")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x3)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21BF"),
        (1, "loc_21CD"),
        (2, "loc_21DB"),
        (3, "loc_21E9"),
        (4, "loc_21F7"),
        (5, "loc_2205"),
        (6, "loc_2213"),
        (7, "loc_2221"),
        (8, "loc_222F"),
        (9, "loc_223D"),
        (10, "loc_224B"),
        (11, "loc_2259"),
        (SWITCH_DEFAULT, "loc_2267"),
    )


    label("loc_21BF")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_21CD")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_21DB")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_21E9")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_21F7")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_2205")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_2213")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_2221")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_222F")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_223D")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_224B")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_2259")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2267")

    label("loc_2267")

    Jump("loc_2276")

    label("loc_226C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2276")

    Jump("loc_22D9")

    label("loc_227B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C6")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_22D9")

    label("loc_22C6")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22D9")

    Jump("loc_1D4E")

    label("loc_22DE")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1D34 end

    def Function_9_22E6(): pass

    label("Function_9_22E6")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 8280, 0, -13050, 180)
    SetChrPos(0x1, 8280, 0, -13050, 180)
    SetChrPos(0x2, 8280, 0, -13050, 180)
    SetChrPos(0x3, 8280, 0, -13050, 180)
    SetChrPos(0x4, 8280, 0, -13050, 180)
    SetChrPos(0x5, 8280, 0, -13050, 180)
    Sleep(1)
    OP_68(8280, 600, -13050, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23BA")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_23C0")

    label("loc_23BA")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_23C0")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_22E6 end

    def Function_10_23D5(): pass

    label("Function_10_23D5")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)
    Return()

    # Function_10_23D5 end

    def Function_11_23E3(): pass

    label("Function_11_23E3")

    TalkBegin(0xFE)

    #C0002
    ChrTalk(
        0xFE,
        (
            "ここから飛行船が\x01",
            "飛び立つのを見るのがすきなのー。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "あんなのが飛んじゃうなんて\x01",
            "すごいよね～。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_23E3 end

    def Function_12_2450(): pass

    label("Function_12_2450")

    TalkBegin(0xFE)

    #C0004
    ChrTalk(
        0xFE,
        (
            "今から子供と一緒に\x01",
            "リベールのほうに旅行なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "あっちはごはんが\x01",
            "とってもおいしいらしいわ。\x01",
            "うふふ、楽しみ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_2450 end

    def Function_13_24CC(): pass

    label("Function_13_24CC")

    TalkBegin(0xFE)

    #C0006
    ChrTalk(
        0xFE,
        (
            "鉄道からの乗り継ぎで\x01",
            "クロスベルに立ち寄ったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "この国には鉄道、バス、飛行船……\x01",
            "便利な足が見事に揃っている。\x01",
            "とても便利な場所だよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_24CC end

    def Function_14_2564(): pass

    label("Function_14_2564")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262C")

    #C0008
    ChrTalk(
        0xFE,
        (
            "今からレミフェリアのほうに\x01",
            "行く予定なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "そういえばあの国にも\x01",
            "警察機関があるんだっけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "クロスベルの警察よりは\x01",
            "さぞ優秀なんでしょうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#0006F（ぐさっ！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2694")

    label("loc_262C")


    #C0012
    ChrTalk(
        0xFE,
        (
            "レミフェリアにも\x01",
            "警察機関があるんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "クロスベルの警察よりは\x01",
            "さぞ優秀なんでしょうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2694")

    TalkEnd(0xFE)
    Return()

    # Function_14_2564 end

    def Function_15_2698(): pass

    label("Function_15_2698")

    TalkBegin(0xFE)

    #C0014
    ChrTalk(
        0xFE,
        (
            "今、旦那を空港に\x01",
            "見送ったところなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "わたしったら、\x01",
            "年甲斐もなく手を振っちゃったわ。\x01",
            "ふふ、恥ずかしいわね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_2698 end

    def Function_16_2718(): pass

    label("Function_16_2718")

    TalkBegin(0xFE)

    #C0016
    ChrTalk(
        0xFE,
        (
            "婆さんとリベールへ\x01",
            "旅行に行くのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "ボース市のマーケットは、\x01",
            "クロスベル市のデパートに\x01",
            "負けないほど活気があるらしいぞ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_2718 end

    def Function_17_27A2(): pass

    label("Function_17_27A2")

    TalkBegin(0xFE)

    #C0018
    ChrTalk(
        0xFE,
        (
            "爺さんは２年前の武道大会を\x01",
            "見に行ってから、リベールの空気を\x01",
            "いたく気に入ったそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "私も爺さんに毒されて\x01",
            "リベールがどんな国か\x01",
            "気になってしまってねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "まぁ、せいぜい楽しんでくるさ。\x01",
            "おっほっほ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_27A2 end

    def Function_18_2880(): pass

    label("Function_18_2880")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "私は貿易商でね。\x01",
            "来月の記念祭に向けて、\x01",
            "今から仕入れに向かうところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "直前まで外国で粘って、\x01",
            "品物を充実させないとな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2880 end

    def Function_19_2908(): pass

    label("Function_19_2908")

    TalkBegin(0xFE)

    #C0023
    ChrTalk(
        0xFE,
        (
            "一度、一人で外国旅行に\x01",
            "来てみたかったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "クロスベルは\x01",
            "色々と噂がある場所だけど、\x01",
            "刺激的で楽しそうだわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_2908 end

    def Function_20_2986(): pass

    label("Function_20_2986")

    TalkBegin(0xFE)

    #C0025
    ChrTalk(
        0xFE,
        "俺は共和国の通信社の者でね。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "大盛況のクロスベル創立記念祭を\x01",
            "取材にやってきたのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "さ、景気よく写真をとっていくぞー！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2986 end

    def Function_21_2A12(): pass

    label("Function_21_2A12")

    TalkBegin(0xFE)

    #C0028
    ChrTalk(
        0xFE,
        (
            "出店がズラっと並んでる画#2Rえ#なんか、\x01",
            "読者ウケしそうですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "いい写真が撮れそうな\x01",
            "通りとかってないです？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2A12 end

    def Function_22_2A8F(): pass

    label("Function_22_2A8F")

    TalkBegin(0xFE)

    #C0030
    ChrTalk(
        0xFE,
        (
            "今日のために小遣いを\x01",
            "たっぷり溜めてきたんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "こいつで彼女と一緒に\x01",
            "クロスベルを遊びつくしてやるぜ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2A8F end

    def Function_23_2B04(): pass

    label("Function_23_2B04")

    TalkBegin(0xFE)

    #C0032
    ChrTalk(
        0xFE,
        (
            "うーん、私たちくらいの歳じゃ\x01",
            "遊びつくすほどのミラは\x01",
            "持ってないと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "ふふ、まぁ張り切ってるし\x01",
            "期待しちゃおうかな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2B04 end

    def Function_24_2B90(): pass

    label("Function_24_2B90")

    TalkBegin(0xFE)

    #C0034
    ChrTalk(
        0xFE,
        (
            "毎年毎年、\x01",
            "女２人で旅行ってのも……ないよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "今年は時期も外しちゃったし……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_2B90 end

    def Function_25_2BEE(): pass

    label("Function_25_2BEE")

    TalkBegin(0xFE)

    #C0036
    ChrTalk(
        0xFE,
        (
            "そ、そんなことないよー。\x01",
            "みんなやってるって、男２人とか。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "せっかく友達２人なんだし、\x01",
            "テンション下がること言わないでよー。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_2BEE end

    def Function_26_2C79(): pass

    label("Function_26_2C79")

    TalkBegin(0xFE)

    #C0038
    ChrTalk(
        0xFE,
        (
            "もう最終日かー……\x01",
            "楽しい時間って\x01",
            "すぐ終わっちゃうのよね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_2C79 end

    def Function_27_2CC0(): pass

    label("Function_27_2CC0")

    TalkBegin(0xFE)

    #C0039
    ChrTalk(
        0xFE,
        (
            "いいじゃないか、\x01",
            "おかげでいい思い出が\x01",
            "沢山できたんだからさ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_2CC0 end

    def Function_28_2D09(): pass

    label("Function_28_2D09")

    TalkBegin(0xFE)

    #C0040
    ChrTalk(
        0xFE,
        (
            "はぁ……\x01",
            "ミシュラムに宿泊していたら\x01",
            "本当に酷い目にあったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "夜中に軍用犬が走り回ってるのよ？\x01",
            "なのにこの人ときたら\x01",
            "ぐっすり眠っちゃって……！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_2D09 end

    def Function_29_2DA8(): pass

    label("Function_29_2DA8")

    TalkBegin(0xFE)

    #C0042
    ChrTalk(
        0xFE,
        (
            "おいおい、機嫌を直せよ。\x01",
            "たまたまどこかから\x01",
            "魔獣が入り込んだだけだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "だから、来年はもう行かないなんて\x01",
            "ワガママを言わないでくれよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_2DA8 end

    def Function_30_2E40(): pass

    label("Function_30_2E40")

    TalkBegin(0xFE)

    #C0044
    ChrTalk(
        0xFE,
        (
            "ふー、日帰りで\x01",
            "レミフェリアまで出張は\x01",
            "やっぱり大変だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "……さ、奥さんが家で待ってる。\x01",
            "はやく帰ってゆっくりしたいな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_2E40 end

    def Function_31_2EC8(): pass

    label("Function_31_2EC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_3030")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA7")

    #C0046
    ChrTalk(
        0xFE,
        (
            "空港からはリベール・レミフェリア行きの\x01",
            "国際定期便が出ていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "今日は、リベールの方から\x01",
            "荷物が届く事になってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "さーて、カプア特急便とやらは\x01",
            "そろそろ到着した頃かねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_302C")

    label("loc_2FA7")


    #C0049
    ChrTalk(
        0xFE,
        (
            "今日は、リベールの方から\x01",
            "荷物が届く事になっててね。\x01",
            "ここで待ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "カプア特急便とやらは\x01",
            "そろそろ到着したころかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_302C")

    TalkEnd(0xFE)
    Return()

    label("loc_3030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3101")

    #C0051
    ChrTalk(
        0xFE,
        (
            "お……あんた達、\x01",
            "さっそく仕事かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "……俺が確認を怠らなきゃ、\x01",
            "昨日、あの子を危ない目に\x01",
            "遭わせずに済んだんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "これから仕事やる以上は、\x01",
            "ちゃんと責任感を持って\x01",
            "やろうと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3185")

    label("loc_3101")


    #C0054
    ChrTalk(
        0xFE,
        (
            "さーて、今日は\x01",
            "外国の運送会社の荷物を\x01",
            "受け取る予定なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "昨日はオヤジに\x01",
            "ゲンコ貰っちまったし、\x01",
            "汚名返上といかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3185")

    TalkEnd(0xFE)
    Return()

    # Function_31_2EC8 end

    def Function_32_3189(): pass

    label("Function_32_3189")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_34F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33FD")

    #C0056
    ChrTalk(
        0xFE,
        (
            "ああ、君たち……\x01",
            "バスの方はどうだったんだい！？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#0000Fはい、やはりエンジントラブルを\x01",
            "起こしていたみたいで……\x02\x03",

            "一応魔獣は追い払って\x01",
            "安全を確保しておきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#0200F今は通りがかった遊撃士が\x01",
            "対応してくれています。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "ほっ、そうか。\x01",
            "それなら良かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "うんうん、遊撃士なら\x01",
            "対応を誤るはずもないよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x101,
        "#0006Fそ、そうですね。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#0108Fエステルさんとヨシュアさんには\x01",
            "助けられてしまったし……\x01",
            "返す言葉もないわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        (
            "#0306F完璧に美味しい所を\x01",
            "持って行かれちまったなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 0)
    Jump("loc_34F1")

    label("loc_33FD")


    #C0064
    ChrTalk(
        0xFE,
        (
            "ともかく、もうすぐバスが\x01",
            "戻ってくるんだね？\x01",
            "大事がなくてよかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "君たちにもお礼を言わなくちゃな。\x01",
            "偶然居合わせてくれて、\x01",
            "本当に助かったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F1")

    #C0066
    ChrTalk(
        0x101,
        (
            "#0000Fはは、どうも……\x01",
            "（今度からは偶然に頼らずに\x01",
            " 仕事をしないとな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_34F1")

    Jump("loc_3575")

    label("loc_34F6")


    #C0067
    ChrTalk(
        0xFE,
        (
            "バスからの通信は\x01",
            "完全に途切れているらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "街道の様子を\x01",
            "見てくるだけでも構わないから。\x01",
            "どうかよろしく頼んだよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3575")

    TalkEnd(0xFE)
    Return()

    # Function_32_3189 end

    def Function_33_3579(): pass

    label("Function_33_3579")

    TalkBegin(0xFE)

    #C0069
    ChrTalk(
        0xFE,
        "俺たちは駅と空港で張り込むつもりだ。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "お前らはタングラム門の方を頼むぞ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_3579 end

    def Function_34_35D2(): pass

    label("Function_34_35D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3B39")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3791")
    TurnDirection(0xFE, 0x10A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3743")

    #C0071
    ChrTalk(
        0xFE,
        (
            "げげっ……\x01",
            "一課のダドリー捜査官！？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "……えへ、おはようございマ～ス。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x10A,
        (
            "#0603F昼近くになって何を言っている？\x02\x03",

            "#0600Fレイモンド君、聞き込みの方は\x01",
            "進んでいるんだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "あ、大丈夫ですよ。\x01",
            "スゴク順調です～。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x10A,
        (
            "#0603F………………………………\x01",
            "（これだから捜査二課は……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD9, 2)
    SetScenarioFlags(0x0, 4)
    Jump("loc_3785")

    label("loc_3743")


    #C0076
    ChrTalk(
        0xFE,
        "えへ、聞き込み頑張らなくっちゃ。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "お仕事、お仕事っと……\x02",
    )

    CloseMessageWindow()

    label("loc_3785")

    OP_93(0xFE, 0x10E, 0x0)
    Jump("loc_3B34")

    label("loc_3791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ADF")

    #C0078
    ChrTalk(
        0xFE,
        "あれ～、支援課のみんなじゃん。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "もしかして応援かい？\x01",
            "ほら、空港の件のさぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3922")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0080
    ChrTalk(
        0x102,
        "#0105F空港がどうかしたんですか……？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "あー、まだ聞いてないんだ～。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "まあ知らない方がいいかもね。\x01",
            "一課にすごいこき使われちゃうしね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0005F（？？？\x01",
            "  何かあったのかな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD7")

    label("loc_3922")

    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0084
    ChrTalk(
        0x101,
        "#0005Fあ、いえ、そういうわけでは……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0300Fつーか状況は\x01",
            "どうなってるんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "ん～、あんまり大声じゃ言えないけど\x01",
            "まだ“捜索中”って感じかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "二課も体制に組み込まれちゃってさ、\x01",
            "俺も警部も今日は\x01",
            "バリバリこき使われてるんだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#0108Fフェイクかもしれないけど\x01",
            "万が一という事もありますものね……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "そゆこと。\x01",
            "まったく面倒な事件だよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD7")

    SetScenarioFlags(0x0, 4)
    Jump("loc_3B34")

    label("loc_3ADF")


    #C0090
    ChrTalk(
        0xFE,
        "今日はバリバリ聞き込みだよ～。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "市民に伏せながら\x01",
            "捜査ってのも面倒だよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B34")

    Jump("loc_3B74")

    label("loc_3B39")


    #C0092
    ChrTalk(
        0xFE,
        (
            "ただでさえ人手不足だけど……\x01",
            "まぁ、やるしかないよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B74")

    TalkEnd(0xFE)
    Return()

    # Function_34_35D2 end

    def Function_35_3B78(): pass

    label("Function_35_3B78")

    TalkBegin(0xFE)

    #C0093
    ChrTalk(
        0xFE,
        (
            "バス、まだ来ないのかしら。\x01",
            "こっちは急いでるのに……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_3B78 end

    def Function_36_3BB8(): pass

    label("Function_36_3BB8")

    TalkBegin(0xFE)

    #C0094
    ChrTalk(
        0xFE,
        "孫の見舞いに行くんじゃよ。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "入院も長いと\x01",
            "退屈しておるじゃろうからの。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_3BB8 end

    def Function_37_3C0E(): pass

    label("Function_37_3C0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3C6A")

    #C0096
    ChrTalk(
        0xFE,
        "うり？　バス来ないんだけど。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "またトラブルでも\x01",
            "あったのかなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D13")

    label("loc_3C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD8")

    #C0098
    ChrTalk(
        0xFE,
        (
            "ごほごほ……\x01",
            "おい、いつまで待たせるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "もうとっくに\x01",
            "時刻は過ぎてるはずだぜ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3D13")

    label("loc_3CD8")


    #C0100
    ChrTalk(
        0xFE,
        (
            "こっちは風邪引いてるんだよ。\x01",
            "早くしてほしいもんだね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D13")

    TalkEnd(0xFE)
    Return()

    # Function_37_3C0E end

    def Function_38_3D17(): pass

    label("Function_38_3D17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3D69")

    #C0101
    ChrTalk(
        0xFE,
        "お見舞いお見舞い～㈱\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "これから彼氏の\x01",
            "お見舞いに行くの！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DB6")

    label("loc_3D69")


    #C0103
    ChrTalk(
        0xFE,
        (
            "私たち、これから\x01",
            "病院で診てもらうんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "何かあったのかしら。\x02",
    )

    CloseMessageWindow()

    label("loc_3DB6")

    TalkEnd(0xFE)
    Return()

    # Function_38_3D17 end

    def Function_39_3DBA(): pass

    label("Function_39_3DBA")

    TalkBegin(0xFE)

    #C0105
    ChrTalk(
        0xFE,
        "どうも風邪をこじらせたようだ。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "ごほごほ……\x01",
            "うーん、最近仕事で夜遅くまで\x01",
            "働いてたからなぁ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_3DBA end

    def Function_40_3E29(): pass

    label("Function_40_3E29")

    TalkBegin(0xFE)

    #C0107
    ChrTalk(
        0xFE,
        (
            "今日はお義父さんの\x01",
            "付き添いなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "もう……だから早く\x01",
            "病院に行って下さいって\x01",
            "言ったのに。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_3E29 end

    def Function_41_3E95(): pass

    label("Function_41_3E95")

    TalkBegin(0xFE)

    #C0109
    ChrTalk(
        0xFE,
        (
            "困ったな……\x01",
            "面会時間は５時半までなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "このままじゃ\x01",
            "着いた途端にＵターンたぜ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_3E95 end

    def Function_42_3EF8(): pass

    label("Function_42_3EF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3F55")

    #N0111
    NpcTalk(
        0xFE,
        "市民",
        "おーい、ちっともバス来ねえぞ～。\x02",
    )

    CloseMessageWindow()

    #N0112
    NpcTalk(
        0xFE,
        "市民",
        "どうなってんだこれー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_40D2")

    label("loc_3F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4088")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4015")

    #C0113
    ChrTalk(
        0xFE,
        "ダドリー捜査官、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "上層部もあれ以来だんまりですし、\x01",
            "状況が把握しづらいのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "空港の件はお任せ下さい。\x01",
            "日暮れまでには片付けますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4083")

    label("loc_4015")


    #C0116
    ChrTalk(
        0xFE,
        (
            "……空港は現在\x01",
            "我々捜査一課が封鎖している。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "特務支援課、余計な真似をして\x01",
            "足を引っ張るんじゃないぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4083")

    Jump("loc_40D2")

    label("loc_4088")


    #C0118
    ChrTalk(
        0xFE,
        (
            "ここは我々\x01",
            "捜査一課が仕切っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        "勝手な立ち入りは許さん。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 6)

    label("loc_40D2")

    TalkEnd(0xFE)
    Return()

    # Function_42_3EF8 end

    def Function_43_40D6(): pass

    label("Function_43_40D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_415C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_412A")

    #C0120
    ChrTalk(
        0xFE,
        (
            "まったくね。\x01",
            "また市庁に\x01",
            "文句言ってやらなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4157")

    label("loc_412A")


    #C0121
    ChrTalk(
        0xFE,
        (
            "まったく……\x01",
            "今日は諦めて帰ろうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4157")

    Jump("loc_41AD")

    label("loc_415C")


    #C0122
    ChrTalk(
        0xFE,
        (
            "私たちは知り合いの\x01",
            "見舞いに行くとこなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        "何かあったのかしら。\x02",
    )

    CloseMessageWindow()

    label("loc_41AD")

    TalkEnd(0xFE)
    Return()

    # Function_43_40D6 end

    def Function_44_41B1(): pass

    label("Function_44_41B1")

    TalkBegin(0xFE)

    #C0124
    ChrTalk(
        0xFE,
        (
            "警察の人に不審人物を\x01",
            "見なかったかと聞かれたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "一口に不審と言われても\x01",
            "よく分からんよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_41B1 end

    def Function_45_4220(): pass

    label("Function_45_4220")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_432E")

    #C0126
    ChrTalk(
        0xFE,
        (
            "お疲れ様です。\x01",
            "こちらは周辺の洗い出しに入った所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "捜査二課も使っていますし\x01",
            "３時間もあれば、はっきりするかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x10A,
        (
            "#0608Fそうか……\x02\x03",

            "#0600F私はしばらく単独行動をとる。\x01",
            "エマ君、こちらは頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "ええ、お任せ下さい！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_43AA")

    label("loc_432E")


    #C0130
    ChrTalk(
        0xFE,
        (
            "お疲れ様です。\x01",
            "こちらは周辺の洗い出しに入った所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "捜査二課も使っていますし\x01",
            "３時間もあれば、はっきりするかと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43AA")

    Jump("loc_445A")

    label("loc_43AF")


    #C0132
    ChrTalk(
        0xFE,
        (
            "特務支援課、あまり\x01",
            "出しゃばりすぎないように。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "現在あなたたちは\x01",
            "ダドリーさんの指揮下にあるはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "ダドリーさんを差し置いた\x01",
            "勝手な行動は、断固許しませんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_445A")

    TalkEnd(0xFE)
    Return()

    # Function_45_4220 end

    def Function_46_445E(): pass

    label("Function_46_445E")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0135
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(52890, 2860, -105330, 1500)
    MoveCamera(57, 25, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(16000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_474D")
    OP_E0(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_453B")
    MiniGame(0x6, 0xA, 0xCB98, 0x384, 0xFFFE6934, 0x65, 0x105F4, 0xFFFFE8F4, 0xFFFE7898)
    Jump("loc_474D")

    label("loc_453B")

    MiniGame(0x6, 0xB, 0xCB98, 0x384, 0xFFFE6934, 0x65, 0x105F4, 0xFFFFE8F4, 0xFFFE7898)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_474D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_474D")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(53380, 2860, -106080, 0)
    MoveCamera(58, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(13540, 0)
    LoadChrToIndex("apl/ch50161.itc", 0x28)
    SetChrChipByIndex(0x0, 0x28)
    SetChrSubChip(0x0, 0x12)
    SetChrFlags(0x0, 0x2)
    SetChrPos(0x0, 52120, 900, -104140, 101)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    #N0137
    NpcTalk(
        0x0,
        "ロイド",
        (
            "#0011Fうわッ……！！？\x01",
            "な、な、何だこの超大物は……！？\x02\x03",

            "#0006F竿が折れるかと思った……\x01",
            "このサイズ、本当に魚なのか？\x02\x03",

            "#0000Fハハ、まあいいや。\x01",
            "……釣公師団の支部長に報告したら\x01",
            "喜びそうな話だけど。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, 52120, 900, -104140, 101)
    SetChrPos(0x2, 52120, 900, -104140, 101)
    SetChrPos(0x3, 52120, 900, -104140, 101)
    SetChrPos(0x4, 52120, 900, -104140, 101)
    SetChrPos(0x5, 52120, 900, -104140, 101)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D5(0x28)
    OP_37()
    SetScenarioFlags(0x69, 4)

    label("loc_474D")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_46_445E end

    def Function_47_4752(): pass

    label("Function_47_4752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_47B8")
    TalkBegin(0xFF)
    SetChrName("")

    #A0138
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x02",
        )
    )

    CloseMessageWindow()

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの到着時刻は\x01",
            "とうに過ぎているようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_486F")

    label("loc_47B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47DE")
    Call(0, 68)
    Jump("loc_486F")

    label("loc_47DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47F4")
    Call(0, 48)
    Jump("loc_486F")

    label("loc_47F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_480A")
    Call(0, 56)
    Jump("loc_486F")

    label("loc_480A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_481B")
    Call(0, 5)
    Jump("loc_486F")

    label("loc_481B")

    TalkBegin(0xFF)
    SetChrName("")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの到着時刻は\x01",
            "とうに過ぎている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_486F")

    Return()

    # Function_47_4752 end

    def Function_48_4870(): pass

    label("Function_48_4870")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_68(-10000, 1300, -10900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -10300, 180, -11500, 180)
    SetChrPos(0x102, -10300, 180, -10000, 180)
    SetChrPos(0x104, -8500, 180, -9400, 225)
    SetChrPos(0x103, -9800, 180, -8300, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0142
    ChrTalk(
        0x101,
        (
            "#0000F#5P次の発車時刻は……\x01",
            "１０分後ってところか。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#0100F#5P待っていれば\x01",
            "すぐに来るわね。\x02\x03",

            "#0104Fウルスラ病院か……\x01",
            "行くのは久しぶりだわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0144
    ChrTalk(
        0x101,
        (
            "#0000F#12Pああ、俺もそうだよ。\x02\x03",

            "#0006F本当ならすぐにでも\x01",
            "訪ねるつもりだったんだけど\x01",
            "毎日忙しかったからなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0145
    ChrTalk(
        0x102,
        "#0105F#5Pあら……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x104,
        (
            "#0305F#5P病院に行くって、\x01",
            "どこか具合でも悪いのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#0004F#12Pいや……\x01",
            "知り合いが勤めているんだ。\x02\x03",

            "#0002Fずいぶん世話になった人でさ。\x01",
            "戻った挨拶をしたかったんだけど。\x02\x03",

            "お互い忙しかったから\x01",
            "先延ばしになってたんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        "#0100F#5Pなるほど、そうだったの。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        (
            "#0300F#5P勤めてるってことは\x01",
            "医者かなんかか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(200)

    #C0150
    ChrTalk(
        0x101,
        (
            "#0000F#6Pいや、看護師をしてる人だよ。\x02\x03",

            "若手のまとめ役みたいで\x01",
            "毎日とんでもなく忙しいみたいだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x104,
        (
            "#0305F#5P看護師ってことは……アレか？\x02\x03",

            "もしかして、ナース服着て\x01",
            "優しく検温してくれるお姉さん？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#0005F#6Pへ……\x02\x03",

            "#0000Fま、まあナース服は\x01",
            "仕事着だから着てると思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        "#0301F#5Pそのお姉さん、幾つ？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        (
            "#0004F#6P俺より５歳上だから\x01",
            "２３歳になったかな……？\x02\x03",

            "#0000Fうちの隣に住んでた人で\x01",
            "姉さんみたいな人だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        "#0301F#5P美人？\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#0011F#6Pう、うーん……\x01",
            "綺麗な人であるとは思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#0303F#5P２歳年上のお姉さん……\x01",
            "しかもナース服と来たか……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0158
    ChrTalk(
        0x104,
        (
            "#5P#0307F#4Sストライクど真ん中！\x01",
            "おーし、みなぎって来たぜぇ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    #C0159
    ChrTalk(
        0x104,
        (
            "#5P#0309Fいや～、俺は幸せだなぁ！\x02\x03",

            "お前みたいな親友#4Rマブダチ#と\x01",
            "巡り合うことが出来て！\x02\x03",

            "#0302Fというわけで紹介ヨロシクね☆\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#0006F#6Pあのな……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0106F#5Pはぁ……\x01",
            "男子っていうのはこれだから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0162
    ChrTalk(
        0x101,
        (
            "#0011F#12Pちょ、そこで\x01",
            "俺も入れないでくれよ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x103, 500)

    #C0163
    ChrTalk(
        0x102,
        (
            "#0105F#6Pティオちゃん、どうしたの？\x02\x03",

            "さっきから考え事を\x01",
            "してるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FEC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FEC)

    def lambda_4FF9():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4FF9)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0164
    ChrTalk(
        0x103,
        (
            "#0208F#5Pあ……いえ。\x01",
            "少々、病院とかは苦手で。\x02\x03",

            "#0206F消毒液の匂いとか\x01",
            "注射とかがちょっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        "#0102F#6Pそっか……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#0001F#12Pえっと、大丈夫か？\x02\x03",

            "何だったらティオは──\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        (
            "#0203F#5P──問題ありません。\x02\x03",

            "ちょっと苦手というだけで\x01",
            "嫌いというほどではないです。\x02\x03",

            "#0211F来なくてもいいとか\x01",
            "言ったら怒りますよ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0011F#12Pい、言わないって。\x02\x03",

            "#0006F（危ない危ない……\x01",
            "  少し気をつけなくちゃな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            "#0204F#5Pそれに、わたしも\x01",
            "ロイドさんのお知り合いには\x01",
            "会ってみたいですし……\x02\x03",

            "#0202Fこの前、通信器で\x01",
            "嬉しそうに話していた人ですよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0170
    ChrTalk(
        0x101,
        "#0005F#12Pど、どうしてそれを……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    def lambda_528F():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_528F)
    Sleep(300)

    #C0171
    ChrTalk(
        0x102,
        (
            "#0104F#5Pふふ、ロイドの\x01",
            "お姉さんみたいな人か。\x02\x03",

            "#0102Fちょっと会うのが\x01",
            "楽しみになってきたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        (
            "#0309F#5Pおお、どっちかって言うと\x01",
            "メインイベントになりそうだぜ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x104, 500)
    Sleep(500)

    #C0173
    ChrTalk(
        0x101,
        "#0011F#6Pあ、あくまで捜査優先だからな！？\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrPos(0x101, -10000, 180, -11500, 180)
    SetChrPos(0x102, -10000, 180, -8900, 180)
    SetChrPos(0x104, -10000, 180, -10200, 180)
    SetChrPos(0x103, -10000, 180, -7600, 180)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x2C, -10000, 180, -6300, 180)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2D, -10000, 180, -5000, 180)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x2E, -8700, 180, -5000, 270)
    ClearChrFlags(0x2F, 0x80)
    SetChrPos(0x2F, -7400, 180, -5000, 270)
    Sleep(1000)
    OP_68(-10000, 1800, -10900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(-10000, 1400, -10900, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0174
    ChrTalk(
        0x102,
        "#0106F#5P……来ないわね。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x103,
        "#0203F#5P３０分経過です……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        (
            "#0306F#5Pおいおい、ロイド。\x02\x03",

            "#0301F１０分後に来るんじゃ\x01",
            "なかったのかよ～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0177
    ChrTalk(
        0x101,
        (
            "#0006F#12P……俺に言われても。\x02\x03",

            "#0008Fしかし妙だな。\x01",
            "さすがに遅すぎる気が……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x30, 0x4)
    SetChrPos(0x30, -1000, 900, 3000, 180)

    #N0178
    NpcTalk(
        0x30,
        "青年の声",
        (
            "#4P#2Sああ……\x01",
            "やっぱり来てないよなぁ。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x30, 3, 0, 49)

    def lambda_55DE():

        label("loc_55DE")

        TurnDirection(0x101, 0x30, 500)
        Yield()
        Jump("loc_55DE")

    QueueWorkItem2(0x101, 1, lambda_55DE)

    def lambda_55F0():

        label("loc_55F0")

        TurnDirection(0x102, 0x30, 500)
        Yield()
        Jump("loc_55F0")

    QueueWorkItem2(0x102, 1, lambda_55F0)

    def lambda_5602():

        label("loc_5602")

        TurnDirection(0x103, 0x30, 500)
        Yield()
        Jump("loc_5602")

    QueueWorkItem2(0x103, 1, lambda_5602)

    def lambda_5614():

        label("loc_5614")

        TurnDirection(0x104, 0x30, 500)
        Yield()
        Jump("loc_5614")

    QueueWorkItem2(0x104, 1, lambda_5614)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-8590, 1000, -11890, 6000)
    OP_6F(0x1)
    WaitChrThread(0x30, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)

    #N0179
    NpcTalk(
        0x30,
        "事務姿の青年",
        (
            "#5P困ったなぁ……\x01",
            "本当にどうしたんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #N0180
    NpcTalk(
        0x30,
        "事務姿の青年",
        (
            "#5Pこっちから通信入れても\x01",
            "何の返事もないし……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-8910, 1000, -11110, 0)
    MoveCamera(61, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -9780, 180, -11560, 90)
    SetChrPos(0x104, -9650, 180, -10110, 135)
    SetChrPos(0x102, -10840, 180, -10750, 90)
    SetChrPos(0x103, -10640, 180, -9430, 135)
    SetChrPos(0x2C, -10080, 180, -7470, 135)
    SetChrPos(0x2D, -8550, 180, -5520, 180)
    SetChrPos(0x2E, -9820, 180, -5930, 135)
    SetChrPos(0x2F, -7450, 180, -5520, 180)
    OP_0D()

    #C0181
    ChrTalk(
        0x101,
        (
            "#0001F#6Pあの……\x01",
            "どうかしたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#0101F#6P随分バスが\x01",
            "遅れてるみたいですけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x30, 0x101, 500)
    Sleep(300)

    #N0183
    NpcTalk(
        0x30,
        "事務姿の青年",
        (
            "#11Pいや～、何かトラブルが\x01",
            "起こったみたいでして。\x02",
        )
    )

    CloseMessageWindow()

    #N0184
    NpcTalk(
        0x30,
        "事務姿の青年",
        (
            "#11P一度、バスの運転手から\x01",
            "通信があったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #N0185
    NpcTalk(
        0x30,
        "事務姿の青年",
        (
            "#11P途中でプツリと切れてしまって\x01",
            "応答が無くなってしまったんです。\x02",
        )
    )

    CloseMessageWindow()
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

    #C0186
    ChrTalk(
        0x101,
        "#0005F#6Pそれって……！？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x103,
        "#0203F#6P……トラブルの匂いがしますね。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x104,
        (
            "#0305F#1Pところで……\x01",
            "兄さん、どこの人なんだ？\x02",
        )
    )

    CloseMessageWindow()

    #N0189
    NpcTalk(
        0x30,
        "事務姿の青年",
        (
            "#11Pああ、僕はクロスベル市、\x01",
            "交通課の者です。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x30,
        (
            "#11P一応、自治州で運行している\x01",
            "バスの管理をしてるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x30,
        (
            "#11Pうーん、警備隊に連絡するのもなんだし\x01",
            "やっぱりギルドに頼るしかないかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    def lambda_5B35():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B35)

    def lambda_5B42():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B42)

    def lambda_5B4F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B4F)

    def lambda_5B5C():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B5C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    #C0192
    ChrTalk(
        0x101,
        "#0001F#11P（……みんな、いいか？）\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        "#0101F#6P（ええ、分かってる。）\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x103,
        "#0203F#6P（ふう……仕方ないですね。）\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x104,
        "#0300F#1P（ま、これも巡り合わせだろ。）\x02",
    )

    CloseMessageWindow()

    def lambda_5C21():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C21)

    def lambda_5C2E():
        TurnDirection(0xFE, 0x30, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C2E)

    def lambda_5C3B():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C3B)

    def lambda_5C48():
        TurnDirection(0xFE, 0x30, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C48)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    #C0196
    ChrTalk(
        0x101,
        (
            "#0000F#6Pあの……\x02\x03",

            "その役目、自分たちに\x01",
            "任せてくれませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0197
    ChrTalk(
        0x30,
        "#11Pえ。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x30,
        "#11P君たちは……？\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#0000F#6Pクロスベル警察、\x01",
            "特務支援課の者です。\x02\x03",

            "これから捜査任務で\x01",
            "医科大学に向かう所でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x30,
        "#11Pえ、君たち、警察の人？\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x30,
        (
            "#11Pそっか……\x01",
            "雑誌で読んだことがあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x30,
        (
            "#11P警察がギルドみたいな\x01",
            "市民サービスを始めたって。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#0006F#6P……その、厳密には\x01",
            "同じではないんですけど。\x02\x03",

            "#0000Fバスの様子を見に行くくらい\x01",
            "問題なく出来るかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x30,
        (
            "#11Pそうか……\x01",
            "それならよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x30,
        (
            "#11P何だったら、遊撃士の\x01",
            "応援でも頼んでおくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        (
            "#0012F#6Pい、いや。\x01",
            "多分大丈夫だと思います。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0207
    ChrTalk(
        0x101,
        "#0000F#11P──みんな、行こう。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        "#0100F#6Pええ……！\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        "#0302F#1Pおうよ！\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x103,
        "#0202F#6P……了解です。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x30, 0x80)
    SetChrBattleFlags(0x30, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    SetChrFlags(0x2E, 0x80)
    SetChrBattleFlags(0x2E, 0x8000)
    SetChrFlags(0x2F, 0x80)
    SetChrBattleFlags(0x2F, 0x8000)
    SetChrPos(0x0, -5110, 0, -13100, 180)
    SetScenarioFlags(0x61, 2)
    OP_29(0x3F, 0x1, 0x6)
    OP_1B(0x2, 0xFF, 0xFFFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x8, -9780, 180, -10890, 180)
    SetChrPos(0x9, -9560, 180, -8470, 180)
    SetChrPos(0xA, -9480, 180, -7040, 180)
    SetChrPos(0xB, -9410, 180, -5860, 180)
    SetChrPos(0x10, -9810, 180, -9920, 180)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_48_4870 end

    def Function_49_602E(): pass

    label("Function_49_602E")


    def lambda_6033():
        OP_95(0xFE, -1000, 0, -7000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_6033)
    WaitChrThread(0x30, 1)

    def lambda_6051():
        OP_95(0xFE, -7000, 0, -13000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_6051)
    WaitChrThread(0x30, 1)
    OP_93(0x30, 0xB4, 0x1F4)
    Return()

    # Function_49_602E end

    def Function_50_6072(): pass

    label("Function_50_6072")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch02600.itc", 0x28)
    LoadChrToIndex("chr/ch02651.itc", 0x29)
    LoadChrToIndex("chr/ch02602.itc", 0x2A)
    SetChrPos(0x0, 0, 0, -80000, 0)
    SetChrPos(0x1, 0, 0, -80000, 0)
    SetChrPos(0x2, 0, 0, -80000, 0)
    SetChrPos(0x3, 0, 0, -80000, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrChipByIndex(0x31, 0x29)
    SetChrSubChip(0x31, 0x0)
    SetChrPos(0x2B, 1850, 0, -99380, 0)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    OP_78(0x1, 0x2B)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x31, -15190, 0, -65690, 90)
    OP_D3(0x2B, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD2, 0xAE, 0x9B, 0x5, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01200.itp")
    BeginChrThread(0x33, 1, 0, 53)
    FadeToBright(1000, 0)
    OP_68(4940, 600, -80110, 0)
    MoveCamera(46, 11, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(34420, 0)
    OP_68(3390, 600, -61360, 8000)

    def lambda_6278():
        OP_95(0xFE, -320, 0, -25730, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_6278)
    OP_6F(0x1)
    OP_0D()
    Sleep(2000)
    StopBGM(0x1770)
    WaitChrThread(0x2B, 1)
    OP_52(0x31, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x31, 0x29)
    SetChrSubChip(0x31, 0x0)
    OP_52(0x31, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x31, 0x1)

    def lambda_62E5():
        OP_9D(0xFE, 0xFFFFE188, 0x0, 0xFFFF0344, 0xBB8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_62E5)
    WaitChrThread(0x31, 1)
    SetChrFlags(0x31, 0x1)
    Sound(46, 0, 100, 0)
    SetChrSubChip(0x31, 0x1)
    Sleep(50)
    SetChrSubChip(0x31, 0x2)
    Sleep(50)
    SetChrSubChip(0x31, 0x3)
    Sleep(50)
    SetChrFlags(0x31, 0x20)
    BeginChrThread(0x31, 3, 0, 51)
    BeginChrThread(0x33, 1, 0, 54)

    def lambda_6337():
        OP_96(0xFE, 0x3B6, 0x0, 0xFFFF06D2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_6337)
    Sleep(1000)
    Fade(500)
    OP_68(2880, 600, -60120, 0)
    MoveCamera(41, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24800, 0)
    OP_0D()
    WaitChrThread(0x31, 1)
    EndChrThread(0x31, 0x3)
    EndChrThread(0x33, 0x1)
    ClearChrFlags(0x31, 0x20)

    def lambda_6399():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_6399)
    WaitChrThread(0x31, 1)
    SetChrChipByIndex(0x31, 0x2A)
    SetChrSubChip(0x31, 0x0)
    OP_52(0x31, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x31, 0x20)
    BeginChrThread(0x31, 3, 0, 52)
    Sleep(800)
    Sound(2053, 255, 80, 0)    #voice#Zeit
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)
    SetChrName("白い狼")

    #A0211
    AnonymousTalk(
        0xFF,
        "…………………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(300)
    EndChrThread(0x31, 0x3)
    ClearChrFlags(0x31, 0x20)
    OP_93(0x31, 0x10E, 0x1F4)
    SetChrChipByIndex(0x31, 0x29)
    SetChrSubChip(0x31, 0x0)
    OP_52(0x31, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x31, 0x20)
    BeginChrThread(0x31, 3, 0, 51)
    BeginChrThread(0x33, 1, 0, 55)
    SetCameraDistance(30800, 3000)
    OP_68(1020, 600, -61950, 3000)

    def lambda_64D5():
        OP_96(0xFE, 0xFFFFC856, 0x0, 0xFFFEEA94, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_64D5)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x31, 1)
    EndChrThread(0x31, 0x3)
    EndChrThread(0x33, 0x1)
    ClearChrFlags(0x31, 0x20)
    OP_0D()
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x33, 0x1)
    Sleep(2000)
    SetChrName("")

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その夜……\x01",
            "支援課に戻ったロイドたちは\x01",
            "その日の分の調書をまとめ始めた。\x02\x03",

            "新たに判明した事実や証言、\x01",
            "さらに不審点や現時点での推測などを\x01",
            "分かりやすくまとめていくうちに……\x02\x03",

            "いつの間にか日付が変わり、\x01",
            "心身共に疲れきったロイドたちは\x01",
            "それぞれの部屋に戻って休むのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x64, 0)
    SetScenarioFlags(0x5C, 4)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_50_6072 end

    def Function_51_669D(): pass

    label("Function_51_669D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66B8")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_51_669D")

    label("loc_66B8")

    Return()

    # Function_51_669D end

    def Function_52_66B9(): pass

    label("Function_52_66B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66D7")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_52_66B9")

    label("loc_66D7")

    Return()

    # Function_52_66B9 end

    def Function_53_66D8(): pass

    label("Function_53_66D8")

    Sound(465, 0, 100, 0)
    Sleep(4500)
    Sound(471, 0, 100, 0)
    Return()

    # Function_53_66D8 end

    def Function_54_66E8(): pass

    label("Function_54_66E8")

    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Return()

    # Function_54_66E8 end

    def Function_55_6704(): pass

    label("Function_55_6704")

    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 85, 0)
    Sleep(500)
    Sound(832, 0, 70, 0)
    Sleep(500)
    Sound(832, 0, 55, 0)
    Return()

    # Function_55_6704 end

    def Function_56_6729(): pass

    label("Function_56_6729")

    EventBegin(0x0)
    SoundLoad(468)
    Fade(1000)
    OP_68(-9140, 780, -11210, 0)
    MoveCamera(55, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25710, 0)
    SetChrPos(0x101, -10500, 180, -11600, 180)
    SetChrPos(0x153, -9630, 180, -10060, 180)
    SetChrPos(0xEF, -9220, 180, -11310, 225)
    ClearChrFlags(0x2B, 0x80)
    SetMapObjFlags(0x1, 0x2)
    SetMapObjFlags(0x1, 0x1000)
    OP_78(0x1, 0x2B)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x2B, 0, 0, -40000, 0)
    OP_D3(0x2B, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    OP_0D()

    #C0213
    ChrTalk(
        0x101,
        (
            "#0000F#5P次の発車時刻は……\x01",
            "おっと、もう来るみたいだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_6869")

    #C0214
    ChrTalk(
        0x102,
        (
            "#0109F#11Pふふ……\x01",
            "タイミングが良かったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68D2")

    label("loc_6869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_68A1")

    #C0215
    ChrTalk(
        0x103,
        "#0204F#11Pタイミングが良かったです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_68D2")

    label("loc_68A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_68D2")

    #C0216
    ChrTalk(
        0x104,
        "#0304F#11Pタイミングが良かったな。\x02",
    )

    CloseMessageWindow()

    label("loc_68D2")

    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x153,
        "#1110F#5P来るってなにがー？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    TurnDirection(0xEF, 0x153, 500)

    #C0218
    ChrTalk(
        0x101,
        (
            "#0004F#12Pああ、キーアが\x01",
            "乗りたがってたものだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x153,
        "#1105F#5Pふぇ～……？\x02",
    )

    CloseMessageWindow()
    Sound(467, 0, 100, 0)
    BeginChrThread(0x33, 1, 0, 60)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_69BB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69BB)
    Sleep(50)
    OP_93(0xEF, 0xB4, 0x1F4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_69FB")

    #C0220
    ChrTalk(
        0x102,
        "#0102F早速、来たみたいね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A54")

    label("loc_69FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_6A2B")

    #C0221
    ChrTalk(
        0x103,
        "#0202F早速、来たみたいです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A54")

    label("loc_6A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_6A54")

    #C0222
    ChrTalk(
        0x104,
        "#0302F早速、来やがったな。\x02",
    )

    CloseMessageWindow()

    label("loc_6A54")

    EndChrThread(0x33, 0x1)
    Fade(500)
    OP_68(2080, 600, -29850, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    ClearMapObjFlags(0x1, 0x4)

    def lambda_6A96():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_6A96)
    Sound(466, 0, 100, 0)
    BeginChrThread(0x33, 1, 0, 61)
    Sleep(3000)
    EndChrThread(0x33, 0x1)
    Fade(500)
    OP_68(-8650, 780, -10720, 0)
    MoveCamera(55, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18760, 0)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrPos(0x101, -11000, 180, -11600, 90)
    SetChrPos(0x153, -11000, 180, -10400, 90)
    SetChrPos(0xEF, -11000, 180, -9200, 90)
    SetChrPos(0xC, -11000, 180, -8000, 180)
    SetChrPos(0xD, -11000, 180, -6800, 180)
    SetChrPos(0x2B, -5300, 0, -21000, 0)

    def lambda_6B64():
        OP_96(0xFE, 0xFFFFEB4C, 0x0, 0xFFFFCD38, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_6B64)
    Sleep(1000)
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x2B, 1)

    #C0223
    ChrTalk(
        0x153,
        (
            "#1107F#6Pわああああっ！？\x01",
            "おっきなクルマだぁ！\x02",
        )
    )

    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#0002F#6Pキーア、これが\x01",
            "バスって言うんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_71(0x1, 0x1, 0x1E, 0x1, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x1)
    BeginChrThread(0xC, 3, 0, 57)
    Sleep(3000)

    #C0225
    ChrTalk(
        0x153,
        (
            "#1105F#6Pわわっ……\x01",
            "いっぱい出てきたよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#0004F#6Pああ、病院に行ってた人が\x01",
            "街に戻ってきたんだ。\x02\x03",

            "#0000Fこれに乗って俺たちも\x01",
            "病院って所に行くわけさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x153, 0x101, 500)

    #C0227
    ChrTalk(
        0x153,
        (
            "#1101F#5Pキーア、これに乗るのー！？\x02\x03",

            "ロイドたちもいっしょに！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    TurnDirection(0xEF, 0x153, 500)

    #C0228
    ChrTalk(
        0x101,
        "#0002F#12Pああ、もちろん。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x153,
        (
            "#1109F#5Pえへへ……\x02\x03",

            "#1110Fねえねえ、はやく乗ろうよ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_6DD3")

    #C0230
    ChrTalk(
        0x102,
        (
            "#0109F#5Pふふ……\x01",
            "足元に気をつけてね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E48")

    label("loc_6DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_6E13")

    #C0231
    ChrTalk(
        0x103,
        (
            "#0204F#5Pくす……\x01",
            "足元に気をつけてください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E48")

    label("loc_6E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_6E48")

    #C0232
    ChrTalk(
        0x104,
        (
            "#0309F#5Pハハ……\x01",
            "足元に気をつけろよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E48")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xC, 0x3)
    Call(0, 58)
    SetChrPos(0xC, -8900, 180, -4000, 90)
    SetChrPos(0xD, -7700, 180, -4000, 270)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1D4)
    SetScenarioFlags(0x5C, 1)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_56_6729 end

    def Function_57_6E9D(): pass

    label("Function_57_6E9D")

    BeginChrThread(0x18, 3, 0, 59)
    Sleep(1000)
    BeginChrThread(0x17, 3, 0, 59)
    Sleep(1000)
    BeginChrThread(0x1E, 3, 0, 59)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 59)
    Sleep(1000)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x1E, 3)
    WaitChrThread(0x11, 3)
    Return()

    # Function_57_6E9D end

    def Function_58_6ED2(): pass

    label("Function_58_6ED2")

    EndChrThread(0x18, 0x3)
    EndChrThread(0x17, 0x3)
    EndChrThread(0x1E, 0x3)
    EndChrThread(0x11, 0x3)
    Return()

    # Function_58_6ED2 end

    def Function_59_6EE3(): pass

    label("Function_59_6EE3")

    SetChrPos(0xFE, -6080, 600, -13010, 270)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_6F0E():
        OP_95(0xFE, -8730, 180, -12970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F0E)

    def lambda_6F28():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6F28)
    WaitChrThread(0xFE, 1)

    def lambda_6F3D():
        OP_95(0xFE, -8850, 180, -7610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F3D)
    WaitChrThread(0xFE, 1)

    def lambda_6F5B():
        OP_95(0xFE, -1260, 0, -7620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F5B)
    WaitChrThread(0xFE, 1)

    def lambda_6F79():
        OP_95(0xFE, -50, 900, 3490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F79)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_59_6EE3 end

    def Function_60_6F97(): pass

    label("Function_60_6F97")

    Sound(468, 2, 0, 0)
    Sleep(100)
    OP_25(0x1D4, 0xA)
    Sleep(100)
    OP_25(0x1D4, 0x14)
    Sleep(100)
    OP_25(0x1D4, 0x1E)
    Sleep(100)
    OP_25(0x1D4, 0x28)
    Sleep(100)
    OP_25(0x1D4, 0x32)
    Sleep(100)
    OP_25(0x1D4, 0x3C)
    Sleep(100)
    OP_25(0x1D4, 0x46)
    Sleep(100)
    OP_25(0x1D4, 0x50)
    Sleep(100)
    OP_25(0x1D4, 0x5A)
    Sleep(100)
    OP_25(0x1D4, 0x64)
    Return()

    # Function_60_6F97 end

    def Function_61_6FE4(): pass

    label("Function_61_6FE4")

    OP_25(0x1D4, 0x5A)
    Sleep(100)
    OP_25(0x1D4, 0x50)
    Sleep(100)
    OP_25(0x1D4, 0x46)
    Sleep(100)
    OP_25(0x1D4, 0x3C)
    Sleep(100)
    OP_25(0x1D4, 0x32)
    Sleep(100)
    OP_25(0x1D4, 0x28)
    Sleep(100)
    OP_25(0x1D4, 0x1E)
    Sleep(100)
    OP_25(0x1D4, 0x14)
    Sleep(100)
    OP_25(0x1D4, 0xA)
    Sleep(100)
    OP_24(0x1D4)
    Return()

    # Function_61_6FE4 end

    def Function_62_7027(): pass

    label("Function_62_7027")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    LoadChrToIndex("apl/ch50111.itc", 0x29)
    SoundLoad(806)
    SoundLoad(891)
    OP_68(-5810, 1000, -9380, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24150, 0)
    SetChrPos(0x101, -5570, 0, -9390, 270)
    SetChrPos(0x102, -4760, 0, -10050, 270)
    SetChrPos(0x103, -3220, 0, -9280, 270)
    SetChrPos(0x104, -3850, 0, -8250, 270)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    SetCameraDistance(23150, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0233
    ChrTalk(
        0x101,
        (
            "#0005F#11Pあれ……\x01",
            "けっこう並んでるな？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        "#0100F#11Pこの時間にしては珍しいわね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0235
    ChrTalk(
        0x103,
        (
            "#0203F#11P……おかしいですね。\x02\x03",

            "#0200Fちょうど５分前に前の便が\x01",
            "出たばかりのはずですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7206():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7206)
    Sleep(50)

    def lambda_7216():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7216)
    Sleep(50)

    def lambda_7226():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7226)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0236
    ChrTalk(
        0x101,
        "#0001F#6Pそうなのか？\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x104,
        "#0301F#5Pふむ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x10E, 0x1F4)
    OP_68(-7200, 1000, -7930, 2500)

    def lambda_7289():
        OP_95(0xFE, -6860, 0, -8060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7289)
    Sleep(300)

    def lambda_72A6():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72A6)
    Sleep(50)

    def lambda_72B6():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_72B6)
    Sleep(50)

    def lambda_72C6():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_72C6)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    TurnDirection(0x104, 0xE, 500)
    OP_6F(0x79)

    #C0238
    ChrTalk(
        0x104,
        (
            "#0300F#11Pよう、そこの兄さん。\x02\x03",

            "ひょっとして\x01",
            "バスが遅れてんのかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xE, 0xFF)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x104, 500)

    #N0239
    NpcTalk(
        0xE,
        "青年",
        "#5Pああ、そうみたいだな。\x02",
    )

    CloseMessageWindow()

    #N0240
    NpcTalk(
        0xE,
        "青年",
        (
            "#5P俺も２０分くらい前から\x01",
            "待ってるんだが\x01",
            "なかなか来なくってさ。\x02",
        )
    )

    CloseMessageWindow()

    #N0241
    NpcTalk(
        0xE,
        "青年",
        (
            "#5P困ったな……\x01",
            "面会時刻を過ぎちまうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#0301F#11Pそっか……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    OP_4C(0xE, 0xFF)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_68(-3580, 1000, -8640, 3000)

    def lambda_7433():

        label("loc_7433")

        TurnDirection(0x101, 0x104, 500)
        Yield()
        Jump("loc_7433")

    QueueWorkItem2(0x101, 1, lambda_7433)

    def lambda_7445():

        label("loc_7445")

        TurnDirection(0x102, 0x104, 500)
        Yield()
        Jump("loc_7445")

    QueueWorkItem2(0x102, 1, lambda_7445)

    def lambda_7457():

        label("loc_7457")

        TurnDirection(0x103, 0x104, 500)
        Yield()
        Jump("loc_7457")

    QueueWorkItem2(0x103, 1, lambda_7457)

    def lambda_7469():
        OP_95(0xFE, -3850, 0, -8250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7469)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x102, 500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    OP_6F(0x1)

    #C0243
    ChrTalk(
        0x104,
        "#0306F#5Pやっぱ遅れてるみてぇだな。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x102,
        (
            "#0108F#12Pひょっとして……\x01",
            "またエンジントラブルかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x103,
        "#0206F#11Pその可能性はありそうですね。\x02",
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7582():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7582)
    Sleep(50)

    def lambda_7592():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7592)
    Sleep(50)

    def lambda_75A2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75A2)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(150)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    SetChrSubChip(0x101, 0x5)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0246
    AnonymousTalk(
        0x101,
        (
            "#0001Fはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男の声")

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダドリーだ。\x01",
            "そちらの状況はどうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0248
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fああ、お疲れさまです。\x02\x03",

            "#0000F遊撃士協会の協力は無事、\x01",
            "取り付ける事ができました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0249
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル支部の遊撃士全員が\x01",
            "マフィアと行方不明者たちの捜索を\x01",
            "引き受けてくれた事を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0250
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フン……\x01",
            "マクレインに借りを作ったか。\x02\x03",

            "まあいい、連中ならば\x01",
            "何らかの成果は挙げるだろう。\x02\x03",

            "──こちらはようやく、\x01",
            "マフィアどもの姿が消えた事実に\x01",
            "上の連中が騒ぎ始めたところだ。\x02\x03",

            "だが、まともに動けるには\x01",
            "もう少し時間がかかるかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0251
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F了解しました。\x02\x03",

            "#0001Fそういえば──\x01",
            "今、空港近くにいるんですが\x01",
            "爆破予告の方はどうなりました？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0252
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フン、そちらは完全に\x01",
            "ガセだった可能性が高いな。\x02\x03",

            "最新の導力探知器で\x01",
            "空港内をくまなく調べたが\x01",
            "何も出てこなかった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0253
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0013Fやはりマフィアの動向と\x01",
            "何らかの関係が……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0254
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今、その線も探っている。\x02\x03",

            "──ちょっと待て。\x01",
            "空港の近くにいるそうだが……\x02\x03",

            "まさかそちらの方にまで\x01",
            "首を突っ込むつもりなのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0255
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fいえ、実はこれから\x01",
            "ウルスラ病院に向かうんです。\x02\x03",

            "成分調査の連絡が遅れているので\x01",
            "直接訪ねてみようかと。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0256
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なんだ、まだ聞いていないのか？\x02\x03",

            "まったく、これだから新米は。\x01",
            "その手の連絡は、正確な時間を\x01",
            "決めて迅速にだな……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0257
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006Fす、すみません。\x01",
            "（確かにアバウト過ぎたか……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0258
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "薬の成分が明らかになれば\x01",
            "こちらも上を動かしやすくなる。\x02\x03",

            "その医師とやらの働きには\x01",
            "期待したいところだが……\x02\x03",

            "……そういえば、\x01",
            "何という名前の医師なんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0259
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fああ、言ってませんでしたか。\x02\x03",

            "#0000Fヨアヒム・ギュンターといって\x01",
            "神経科と薬学担当の准教授です。\x02\x03",

            "３０台半ばくらいですけど\x01",
            "かなり有能という評判ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0260
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふむ、それなら少しは\x01",
            "期待できるかもしれんが……\x02\x03",

            "──ん？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0261
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F？　どうしました？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0262
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ちょっと待て……\x01",
            "ヨアヒム・ギュンターと言ったか？\x02\x03",

            "それは眼鏡をかけた\x01",
            "わりと飄々とした感じの男か？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0263
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fええ、そうですけど……\x01",
            "会った事があるんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1388)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0264
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#40W…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0265
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001Fあの、ダドリーさん……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……会ったのは\x01",
            "２ヶ月ほど前のことだ。\x02\x03",

            "アルカンシェルのプレ公演で\x01",
            "市長を暗殺しようとした犯人──\x02\x03",

            "アーネスト元秘書の\x01",
            "取調べをしている最中にな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0267
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fえ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7203", 0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルゲイさんから聞いたかもしれんが、\x01",
            "アーネストは完全に錯乱していた。\x02\x03",

            "そこで仕方なく、彼が以前から\x01",
            "相談していたというカウンセラーを\x01",
            "ウルスラ病院から呼び寄せたんだ。\x02\x03",

            "それでようやく、まともに事情聴取が\x01",
            "出来るようになったんだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0269
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011Fちょ、ちょっと待ってください。\x02\x03",

            "ひょっとして……\x01",
            "ヨアヒム先生がアーネストの？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、主治医という訳だ。\x02\x03",

            "その時は、さすがウルスラ病院の\x01",
            "医師だと感心したものだったが……\x02\x03",

            "………………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0271
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F……………………………………\x02\x03",

            "#0013F……分かりました。\x01",
            "本人にそれとなく当たってみます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0272
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、そうしてみろ。\x02\x03",

            "とにかく時間は有効に使え。\x01",
            "──またこちらから連絡する。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(825, 0, 100, 0)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0273
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0008F#30W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0274
    ChrTalk(
        0x102,
        (
            "#0105F#12Pど、どうしたの？\x01",
            "変な話をしてたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x103,
        (
            "#0205F#11Pあの秘書の人とヨアヒム先生が\x01",
            "何か関係あるんですか？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0276
    ChrTalk(
        0x101,
        "#0003F#6Pああ……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダドリーからの情報をエリィたちに伝えた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    #C0278
    ChrTalk(
        0x102,
        "#0101F#12Pそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        (
            "#0303F#5Pちょっと待てって感じだな……\x02\x03",

            "#0301F考えてみりゃあ、\x01",
            "あの時の秘書野郎の態度と\x01",
            "馬鹿力はどう考えても……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x103,
        (
            "#0206F#11P鉱員のガンツさんのケースと\x01",
            "そっくりかもしれませんね。\x02\x03",

            "#0208Fしかもその主治医だった人が\x01",
            "ヨアヒム先生というのは……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0281
    ChrTalk(
        0x102,
        (
            "#0101F#12Pちょ、ちょっと病院の\x01",
            "受付に確認してみるわね。\x02\x03",

            "あれからヨアヒム先生が\x01",
            "どこかに出かけていないか──\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8617():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8617)

    def lambda_8624():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8624)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0282
    ChrTalk(
        0x101,
        "#0001F#6Pああ、頼む。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x190)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x10)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(200)
    Sound(807, 0, 100, 0)
    Sleep(800)
    Sound(891, 2, 100, 0)
    Sleep(2500)

    #C0283
    ChrTalk(
        0x102,
        (
            "#0103F#5P…………………………………\x02\x03",

            "#0108F……駄目、出ないわ。\x02\x03",

            "話し中というわけでも\x01",
            "無さそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x37B)
    Sound(807, 0, 100, 0)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x102, 0x10)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x102, 0x0, 0x190)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0284
    ChrTalk(
        0x103,
        (
            "#0203F#11P──遅れているバスに\x01",
            "連絡が付かない病院……\x02\x03",

            "#0201Fそして新たに判明した\x01",
            "意外な人間関係ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#0301F#5P……さすがにちょいとばかり\x01",
            "お膳立てが整いすぎてねぇか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(150)

    #C0286
    ChrTalk(
        0x101,
        (
            "#0003F#6Pああ……\x02\x03",

            "#0013F──じきに日も暮れる。\x01",
            "急いでウルスラ病院に向かおう。\x02\x03",

            "バスとすれ違ったら呼び止めて\x01",
            "そのまま乗せてもらえばいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x102,
        "#0101F#12Pええ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(21650, 2500)
    OP_6F(0x79)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x28)
    OP_D5(0x29)
    SetChrPos(0x0, -4680, 0, -11060, 180)
    SetScenarioFlags(0xE0, 1)
    OP_29(0x4D, 0x1, 0x1)
    ReplaceBGM("ed7000", "ed7000")
    ReplaceBGM("ed7200", "ed7203")
    ReplaceBGM("ed7202", "ed7203")
    ReplaceBGM("ed7100", "ed7203")
    ReplaceBGM("ed7101", "ed7203")
    ReplaceBGM("ed7111", "ed7203")
    ReplaceBGM("ed7116", "ed7203")
    ReplaceBGM("ed7117", "ed7203")
    ReplaceBGM("ed7124", "ed7203")
    OP_24(0x326)
    OP_24(0x37B)
    EventEnd(0x5)
    Return()

    # Function_62_7027 end

    def Function_63_896A(): pass

    label("Function_63_896A")

    EventBegin(0x0)
    Sleep(1000)
    OP_68(-9260, 1500, -12230, 3000)
    MoveCamera(45, 21, 0, 3000)
    OP_6E(510, 5000)
    SetCameraDistance(23500, 5000)
    OP_6F(0x79)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "停留所の看板を調べると、\x01",
            "導力バスに乗ることができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "選択した行き先へ素早く移動することができ、\x01",
            "各地を効率的に回ることが可能です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 7)
    EventEnd(0x5)
    Return()

    # Function_63_896A end

    def Function_64_8A45(): pass

    label("Function_64_8A45")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x3B, 0x80)
    OP_68(50680, 2860, -111330, 0)
    MoveCamera(55, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17280, 0)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, 49980, 900, -106970, 102)
    SetChrPos(0x102, 52090, 900, -107470, 102)
    SetChrPos(0x103, 50300, 900, -109260, 102)
    SetChrPos(0x104, 51400, 900, -110070, 102)
    FadeToBright(500, 0)
    OP_0D()

    #C0290
    ChrTalk(
        0x104,
        (
            "#12P#0300Fこのでけぇ川は\x01",
            "ルピナス川だったっけか。\x02\x03",

            "#0305F真ん中に浮かんでいる\x01",
            "あの建物は何なんだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        "#6P#0003Fうーん、何かの遺跡だと思うけど……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        (
            "#12P#0203Fデータベースにも詳細はありませんね。\x02\x03",

            "#0200Fただ立入禁止区画には\x01",
            "指定されているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        (
            "#6P#0100F本当かどうかは知らないけど、\x01",
            "縁結びのご利益がある遺跡だとか\x01",
            "言われているみたいよ。\x02\x03",

            "#0104Fこの見晴らし台の左側に男の人、\x01",
            "右側に女の人が立ってお祈りをすると、\x01",
            "２人は一生離ればなれにならないとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        (
            "#12P#0306Fそ、そりゃまた\x01",
            "都市伝説らしい都市伝説だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#6P#0000Fグレイスさんに依頼された写真、\x01",
            "ここならいいものが撮れそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9380")
    TurnDirection(0x101, 0x102, 500)

    #C0296
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれじゃあエリィ、\x01",
            "撮影をお願いできるかな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0297
    ChrTalk(
        0x102,
        (
            "#6P#0108Fえ、ええ。\x01",
            "ちょっと自信はないけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0298
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

    #C0299
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

    #C0300
    ChrTalk(
        0x103,
        (
            "#12P#0200F素人とプロの写真を見比べると\x01",
            "一目で違いが分かりますからね。\x02\x03",

            "#0203F粗雑な人には、その繊細さが\x01",
            "理解できないかも知れませんが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0301
    ChrTalk(
        0x104,
        (
            "#12P#0306Fぐっ……\x01",
            "誰のことを言ってんだ、誰の。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        (
            "#6P#0000Fま、まぁまぁ。\x01",
            "ここはエリィに任せてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        (
            "#6P#0100Fそれじゃあ……\x01",
            "やってみるわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x66, 0x1F4)
    OP_93(0x101, 0x66, 0x1F4)
    OP_93(0x103, 0x66, 0x1F4)
    OP_93(0x104, 0x66, 0x1F4)
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

    #C0304
    ChrTalk(
        0x102,
        (
            "#6P#0103F……ふぅ。\x01",
            "念のため何枚か撮っておいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        (
            "#6P#0000Fどうやら撮れたみたいだな。\x02\x03",

            "出来栄えはどんな感じだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
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

    #C0307
    ChrTalk(
        0x103,
        (
            "#12P#0200Fエリィさんも\x01",
            "カンを取り戻せたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#12P#0300Fふーん……\x01",
            "俺にはさっぱりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x101,
        (
            "#6P#0000Fまたこういう場所を見つけたら\x01",
            "写真に収めていこう。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96CC")

    label("loc_9380")

    TurnDirection(0x101, 0x102, 500)

    #C0310
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれじゃあ……\x01",
            "エリィ、撮影を頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x102,
        "#6P#0100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x66, 0x1F4)
    OP_93(0x101, 0x66, 0x1F4)
    OP_93(0x103, 0x66, 0x1F4)
    OP_93(0x104, 0x66, 0x1F4)
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

    #C0312
    ChrTalk(
        0x102,
        (
            "#6P#0100F……ふぅ。\x01",
            "こんなところかしら。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_9516")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9516")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_952D")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_952D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_9544")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9544")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_955B")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_955B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_9572")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9572")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_9589")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9589")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_95A0")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_95B7")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_95CE")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9678")

    #C0313
    ChrTalk(
        0x101,
        (
            "#6P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "これでグレイスさんに提示された\x01",
            "５枚ってノルマは達成できた。\x01",
            "これでいつでも提出できそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96CC")

    label("loc_9678")


    #C0314
    ChrTalk(
        0x101,
        (
            "#6P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96CC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 52100, 900, -107040, 102)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x4)
    Sleep(500)
    ClearMapFlags(0x8000000)
    OP_37()
    OP_65(0x4, 0x1)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_64_8A45 end

    def Function_65_970C(): pass

    label("Function_65_970C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98F0")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_984A")

    #C0315
    ChrTalk(
        0x10A,
        (
            "#0603F……こちらの事は\x01",
            "一課の面々に任せておけばいい……\x02\x03",

            "#0601F上層部の一件がなければ\x01",
            "ルバーチェの方に\x01",
            "人員を集める所だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x103,
        (
            "#0200Fダドリーさんは\x01",
            "お悩み中みたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x104,
        (
            "#0300Fハハ、一課も色々\x01",
            "あるみたいだしなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x10A,
        (
            "#0600F……黙れ。\x01",
            "我々は我々の\x01",
            "やるべき事をするぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98EB")

    label("loc_984A")


    #C0319
    ChrTalk(
        0x10A,
        (
            "#0601F……どこへ行くつもりだ？\x01",
            "空港の件なら\x01",
            "捜査一課に任せておけ！\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        "#0005Fそ、そうですね。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        (
            "#0108F（ダドリーさん、何だか\x01",
            "  カリカリしているわね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98EB")

    Jump("loc_9A41")

    label("loc_98F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A06")
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99B4")

    #C0322
    ChrTalk(
        0xF,
        "……待て、特務支援課。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xF,
        (
            "クロスベル空港は\x01",
            "臨時の設備検査を行っている。\x01",
            "立ち入りはできないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#0005F（臨時の設備検査……？\x01",
            "  何か妙だな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_99F6")

    label("loc_99B4")


    #C0325
    ChrTalk(
        0xF,
        (
            "……待て、特務支援課。\x01",
            "クロスベル空港は\x01",
            "現在立ち入り禁止だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99F6")

    OP_93(0xF, 0x10E, 0x1F4)
    OP_4C(0xF, 0xFF)
    Jump("loc_9A41")

    label("loc_9A06")


    #C0326
    ChrTalk(
        0x101,
        (
            "#0000Fこっちはクロスベル空港だ。\x01",
            "……特に用はないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A41")

    Sleep(50)
    SetChrPos(0x0, 11250, 0, -17610, 270)
    EventEnd(0x4)
    Return()

    # Function_65_970C end

    def Function_66_9A58(): pass

    label("Function_66_9A58")

    EventBegin(0x1)
    OP_4B(0x29, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_63(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9A91():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9A91)

    def lambda_9A9E():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9A9E)

    #C0327
    ChrTalk(
        0x29,
        "ダドリーさん……\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xF,
        "ダドリー捜査官、お疲れ様です！\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xF,
        (
            "……しかし、何故\x01",
            "特務支援課などと……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x10A,
        (
            "#0603F詳しい説明は後でする……\x02\x03",

            "#0600Fそれより、こちらの状況はどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x29,
        (
            "ええ、やはりフェイクかと……\x01",
            "今アシを洗っている所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x10A,
        (
            "#0608F……そうか。\x02\x03",

            "#0600F私もじきに合流する。\x01",
            "それまで一課内の事は頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xF,
        "はっ！\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x29,
        "はい！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xC9, 3)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(50)
    OP_93(0x29, 0xB4, 0x0)
    OP_93(0xF, 0x0, 0x0)
    SetChrPos(0x0, 11250, 0, -17610, 270)
    OP_4C(0x29, 0xFF)
    OP_4C(0xF, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_66_9A58 end

    def Function_67_9C34(): pass

    label("Function_67_9C34")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CEB")

    #C0335
    ChrTalk(
        0x101,
        (
            "#0003F（そういえば、人形工房から\x01",
            "  預かったトランクがあったな……）\x02\x03",

            "#0000F（かなり高価なものみたいだし\x01",
            "  先にイメルダさんに渡しておこう。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DC0")

    label("loc_9CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D55")

    #C0336
    ChrTalk(
        0x101,
        (
            "#0000F折角だしバスを使おう。\x02\x03",

            "そこのバス停を見れば\x01",
            "次のバスの時刻が分かるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DC0")

    label("loc_9D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DC0")

    #C0337
    ChrTalk(
        0x101,
        (
            "#0003Fキーアを連れて\x01",
            "街道を歩くわけにはいかないな。\x02\x03",

            "#0000Fここはやっぱりバスを使おう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DC0")

    SetChrPos(0x0, 0, 0, -46000, 0)
    EventEnd(0x4)
    Return()

    # Function_67_9C34 end

    def Function_68_9DD4(): pass

    label("Function_68_9DD4")

    TalkBegin(0xFF)

    #C0338
    ChrTalk(
        0x101,
        (
            "#0005Fそういえば……\x01",
            "人形工房から預かった\x01",
            "トランクがあったっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#0100Fとても高価な作品だし、\x01",
            "病院に向かう前に、\x01",
            "イメルダさんに渡しましょう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_68_9DD4 end

    def Function_69_9E73(): pass

    label("Function_69_9E73")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北・クロスベル市\x01",
            "東・クロスベル空港\x01",
            "南・聖ウルスラ医科大学　１５３セルジュ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_69_9E73 end

    SaveToFile()

Try(main)
