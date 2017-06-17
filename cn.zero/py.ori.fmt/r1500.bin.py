from ZeroScenarioHelper import *

def main():
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
        "搜查官",                 # 8
        "市民",                   # 9
        "市民",                   # 10
        "女孩",                   # 11
        "市民",                   # 12
        "游客",                   # 13
        "市民",                   # 14
        "市民",                   # 15
        "市民",                   # 16
        "市民",                   # 17
        "市民",                   # 18
        "游客",                   # 19
        "记者",                   # 20
        "记者",                   # 21
        "游客",                   # 22
        "游客",                   # 23
        "游客",                   # 24
        "游客",                   # 25
        "游客",                   # 26
        "游客",                   # 27
        "游客",                   # 28
        "游客",                   # 29
        "市民",                   # 30
        "比利",                   # 31
        "交通科的警员",           # 32
        "雷蒙德搜查官",           # 33
        "艾玛搜查官",             # 34
        "多诺邦警督",             # 35
        "巴士",                   # 36
        "巴士站",                 # 37
        "巴士站",                 # 38
        "巴士站",                 # 39
        "巴士站",                 # 40
        "交通科的警员",           # 41
        "蔡特",                   # 42
        "比利的货车",             # 43
        "SE控制",                 # 44
        "br1500",                 # 45
        "br1500",                 # 46
        "br1500",                 # 47
        "br1500",                 # 48
        "br1500",                 # 49
        "克洛斯贝尔市方向",       # 50
        "乌尔斯拉医科大学方向",   # 51
        "克洛斯贝尔空港方向",     # 52
    ))

    ATBonus("ATBonus_8B0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_9077", 4,   2,   0,   8,   0,   3,   2)
    Sepith("Sepith_908F", 8,   2,   0,   0,   3,   0,   5)
    Sepith("Sepith_9087", 0,   8,   0,   4,   4,   2,   0)
    Sepith("Sepith_907F", 8,   0,   5,   2,   0,   0,   4)
    Sepith("Sepith_90AF", 2,   8,   0,   6,   2,   0,   0)

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
        "BattleInfo_990", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_9077", 30, 45, 20, 5,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
        )
    )

    BattleInfo(
        "BattleInfo_BE8", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_908F", 30, 45, 20, 5,
        (
            ("ms65800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms65800.dat", "ms65800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms65800.dat", "ms63600.dat", "ms65800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms65800.dat", "ms65800.dat", "ms66600.dat", "ms65800.dat", 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
        )
    )

    BattleInfo(
        "BattleInfo_B20", 0x0010, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_9087", 60, 25, 10, 5,
        (
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms63600.dat", "ms66600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "ms63600.dat", 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms63600.dat", "ms63600.dat", "ms62100.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
        )
    )

    BattleInfo(
        "BattleInfo_A58", 0x0000, 12, 6, 45, 10, 1, 45, 0, "br1500", "Sepith_907F", 30, 45, 20, 5,
        (
            ("ms66600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms66600.dat", "ms66600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms66600.dat", "ms62100.dat", "ms66600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_910", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
            ("ms66600.dat", "ms66600.dat", "ms69700.dat", "ms66600.dat", 0, 0, 0, 0, "MonsterBattlePostion_8F0", "MonsterBattlePostion_970", "ed7400", "ed7403", "ATBonus_8B0"),
        )
    )

    BattleInfo(
        "BattleInfo_CB0", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_90AF", 30, 45, 20, 5,
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

    PlaceName(2.0, 0.0, 20.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-27.0, 0.0, -159.0, 0x0000, 0x0000, "乌尔斯拉医科大学方向")
    PlaceName(45.0, 0.0, -24.0, 0x0000, 0x0000, "克洛斯贝尔空港方向")
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
        "Function_6_1B17",         # 06, 6
        "Function_7_1C99",         # 07, 7
        "Function_8_1D2E",         # 08, 8
        "Function_9_22B2",         # 09, 9
        "Function_10_23A1",        # 0A, 10
        "Function_11_23AF",        # 0B, 11
        "Function_12_2400",        # 0C, 12
        "Function_13_245C",        # 0D, 13
        "Function_14_24E2",        # 0E, 14
        "Function_15_25D8",        # 0F, 15
        "Function_16_263A",        # 10, 16
        "Function_17_26A0",        # 11, 17
        "Function_18_275A",        # 12, 18
        "Function_19_27DA",        # 13, 19
        "Function_20_2842",        # 14, 20
        "Function_21_28BE",        # 15, 21
        "Function_22_2929",        # 16, 22
        "Function_23_2980",        # 17, 23
        "Function_24_29FC",        # 18, 24
        "Function_25_2A4C",        # 19, 25
        "Function_26_2AC9",        # 1A, 26
        "Function_27_2B0A",        # 1B, 27
        "Function_28_2B45",        # 1C, 28
        "Function_29_2BBE",        # 1D, 29
        "Function_30_2C26",        # 1E, 30
        "Function_31_2C9E",        # 1F, 31
        "Function_32_2EB9",        # 20, 32
        "Function_33_31C2",        # 21, 33
        "Function_34_320B",        # 22, 34
        "Function_35_36F1",        # 23, 35
        "Function_36_371D",        # 24, 36
        "Function_37_375D",        # 25, 37
        "Function_38_3830",        # 26, 38
        "Function_39_38AD",        # 27, 39
        "Function_40_38F8",        # 28, 40
        "Function_41_3950",        # 29, 41
        "Function_42_39B3",        # 2A, 42
        "Function_43_3B4D",        # 2B, 43
        "Function_44_3BFE",        # 2C, 44
        "Function_45_3C4D",        # 2D, 45
        "Function_46_3E17",        # 2E, 46
        "Function_47_4101",        # 2F, 47
        "Function_48_420D",        # 30, 48
        "Function_49_576B",        # 31, 49
        "Function_50_57AF",        # 32, 50
        "Function_51_5DB0",        # 33, 51
        "Function_52_5DCC",        # 34, 52
        "Function_53_5DEB",        # 35, 53
        "Function_54_5DFB",        # 36, 54
        "Function_55_5E17",        # 37, 55
        "Function_56_5E3C",        # 38, 56
        "Function_57_64E8",        # 39, 57
        "Function_58_651D",        # 3A, 58
        "Function_59_652E",        # 3B, 59
        "Function_60_65E2",        # 3C, 60
        "Function_61_662F",        # 3D, 61
        "Function_62_6672",        # 3E, 62
        "Function_63_7CC7",        # 3F, 63
        "Function_64_7D7E",        # 40, 64
        "Function_65_88F7",        # 41, 65
        "Function_66_8BEB",        # 42, 66
        "Function_67_8DB7",        # 43, 67
        "Function_68_8F39",        # 44, 68
        "Function_69_8FD2",        # 45, 69
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
            "有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "圣乌尔斯拉医科大学\x01",          # 0
            "岔口停靠站（河滩附近）\x01",      # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AEF")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1B0F")

    label("loc_1AEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0F")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_1B0F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_1A5C end

    def Function_6_1B17(): pass

    label("Function_6_1B17")

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

    def lambda_1BF1():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_1BF1)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    Sleep(2500)
    Fade(500)
    OP_68(-10500, 780, -11600, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x2B, -6300, 0, -21000, 0)

    def lambda_1C5E():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFD314, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_1C5E)
    WaitChrThread(0x2B, 1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x1)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_6_1B17 end

    def Function_7_1C99(): pass

    label("Function_7_1C99")

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

    # Function_7_1C99 end

    def Function_8_1D2E(): pass

    label("Function_8_1D2E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22AA")

    Menu(
        0,
        32,
        26,
        1,
        (
            "使用警备队车辆进行移动\x01",      # 0
            "在此处休息\x01",                  # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2247")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DD4")
    MenuCmd(1, 1, "★克洛斯贝尔·中央广场")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1DEE")

    label("loc_1DD4")

    MenuCmd(1, 1, "　克洛斯贝尔·中央广场")

    label("loc_1DEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1E")
    MenuCmd(1, 1, "★克洛斯贝尔·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1E36")

    label("loc_1E1E")

    MenuCmd(1, 1, "　克洛斯贝尔·东出口")

    label("loc_1E36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E66")
    MenuCmd(1, 1, "★克洛斯贝尔·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1E7E")

    label("loc_1E66")

    MenuCmd(1, 1, "　克洛斯贝尔·西出口")

    label("loc_1E7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EAE")
    MenuCmd(1, 1, "★克洛斯贝尔·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1EC6")

    label("loc_1EAE")

    MenuCmd(1, 1, "　克洛斯贝尔·南出口")

    label("loc_1EC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF6")
    MenuCmd(1, 1, "★克洛斯贝尔·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1F0E")

    label("loc_1EF6")

    MenuCmd(1, 1, "　克洛斯贝尔·北出口")

    label("loc_1F0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F36")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1F46")

    label("loc_1F36")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_1F46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F6E")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1F7E")

    label("loc_1F6E")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_1F7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FAC")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1FC2")

    label("loc_1FAC")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_1FC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FEC")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1FFE")

    label("loc_1FEC")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_1FFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2028")
    MenuCmd(1, 1, "★玛因兹矿山镇")
    MenuCmd(3, 1, 0x9)
    Jump("loc_203A")

    label("loc_2028")

    MenuCmd(1, 1, "　玛因兹矿山镇")

    label("loc_203A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206A")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_2082")

    label("loc_206A")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_2082")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A8")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_20B6")

    label("loc_20A8")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_20B6")

    MenuCmd(1, 1, "　放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2238")
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
        (0, "loc_218B"),
        (1, "loc_2199"),
        (2, "loc_21A7"),
        (3, "loc_21B5"),
        (4, "loc_21C3"),
        (5, "loc_21D1"),
        (6, "loc_21DF"),
        (7, "loc_21ED"),
        (8, "loc_21FB"),
        (9, "loc_2209"),
        (10, "loc_2217"),
        (11, "loc_2225"),
        (SWITCH_DEFAULT, "loc_2233"),
    )


    label("loc_218B")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_2199")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_21A7")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_21B5")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_21C3")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_21D1")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_21DF")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_21ED")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_21FB")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_2209")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_2217")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_2225")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2233")

    label("loc_2233")

    Jump("loc_2242")

    label("loc_2238")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2242")

    Jump("loc_22A5")

    label("loc_2247")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2292")
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
    Jump("loc_22A5")

    label("loc_2292")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22A5")

    Jump("loc_1D48")

    label("loc_22AA")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1D2E end

    def Function_9_22B2(): pass

    label("Function_9_22B2")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2386")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_238C")

    label("loc_2386")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_238C")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_22B2 end

    def Function_10_23A1(): pass

    label("Function_10_23A1")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)
    Return()

    # Function_10_23A1 end

    def Function_11_23AF(): pass

    label("Function_11_23AF")

    TalkBegin(0xFE)

    #C0002
    ChrTalk(
        0xFE,
        (
            "我喜欢在这里\x01",
            "看飞行船起飞～\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "那么大的船竟然能飞上天，\x01",
            "好厉害哦～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_23AF end

    def Function_12_2400(): pass

    label("Function_12_2400")

    TalkBegin(0xFE)

    #C0004
    ChrTalk(
        0xFE,
        (
            "我正要和孩子\x01",
            "一起去利贝尔旅行。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "听说那边的\x01",
            "饭菜非常好吃呢。\x01",
            "呵呵，好期待。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_2400 end

    def Function_13_245C(): pass

    label("Function_13_245C")

    TalkBegin(0xFE)

    #C0006
    ChrTalk(
        0xFE,
        (
            "因为要从铁路换乘，\x01",
            "便顺便来了克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "这里有铁路、巴士、飞行船……\x01",
            "方便的交通工具应有尽有，\x01",
            "真是个便利的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_245C end

    def Function_14_24E2(): pass

    label("Function_14_24E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2584")

    #C0008
    ChrTalk(
        0xFE,
        (
            "我正打算去\x01",
            "雷米菲利亚。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "说起来，那个国家\x01",
            "好像也有警察机关……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "他们应该比克洛斯贝尔的警察\x01",
            "优秀很多吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#0006F（受打击！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_25D4")

    label("loc_2584")


    #C0012
    ChrTalk(
        0xFE,
        (
            "听说雷米菲利亚\x01",
            "也有警察机关。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "他们应该比克洛斯贝尔的警察\x01",
            "优秀很多吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D4")

    TalkEnd(0xFE)
    Return()

    # Function_14_24E2 end

    def Function_15_25D8(): pass

    label("Function_15_25D8")

    TalkBegin(0xFE)

    #C0014
    ChrTalk(
        0xFE,
        (
            "我刚刚在空港\x01",
            "送走了老公。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "我真是的，\x01",
            "这么大年纪了还挥手道别。\x01",
            "呵呵，好难为情哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_25D8 end

    def Function_16_263A(): pass

    label("Function_16_263A")

    TalkBegin(0xFE)

    #C0016
    ChrTalk(
        0xFE,
        (
            "我和老伴要去\x01",
            "利贝尔旅行。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "听说柏斯市的超市\x01",
            "也十分热闹，不逊于\x01",
            "克洛斯贝尔的百货店呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_263A end

    def Function_17_26A0(): pass

    label("Function_17_26A0")

    TalkBegin(0xFE)

    #C0018
    ChrTalk(
        0xFE,
        (
            "老伴自从两年前\x01",
            "去看过武术大会以后，\x01",
            "就非常喜欢利贝尔的气氛。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "我也受了他的影响，\x01",
            "对利贝尔产生了兴趣，\x01",
            "想去看看那是个怎样的国家呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "呵呵，我们会玩个尽兴的。\x01",
            "呵呵……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_26A0 end

    def Function_18_275A(): pass

    label("Function_18_275A")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "我是个贸易商。\x01",
            "为了准备下个月的纪念庆典，\x01",
            "正打算去进货呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "在庆典开始前都得待在外国，\x01",
            "好好充实一下货物才行啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_275A end

    def Function_19_27DA(): pass

    label("Function_19_27DA")

    TalkBegin(0xFE)

    #C0023
    ChrTalk(
        0xFE,
        (
            "我一直想一个人\x01",
            "到外国旅游一趟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔这里\x01",
            "有着各种传闻，\x01",
            "似乎很刺激，很有趣呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_27DA end

    def Function_20_2842(): pass

    label("Function_20_2842")

    TalkBegin(0xFE)

    #C0025
    ChrTalk(
        0xFE,
        "我是共和国通讯社的人。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "这次是为了报道盛况空前的\x01",
            "克洛斯贝尔创立纪念庆典而来。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "好，鼓足精神去拍照吧～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2842 end

    def Function_21_28BE(): pass

    label("Function_21_28BE")

    TalkBegin(0xFE)

    #C0028
    ChrTalk(
        0xFE,
        (
            "露天店整整齐齐排成一排的画面，\x01",
            "读者应该会很喜欢吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "有没有哪条路的景色\x01",
            "适合拍成好照片呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_28BE end

    def Function_22_2929(): pass

    label("Function_22_2929")

    TalkBegin(0xFE)

    #C0030
    ChrTalk(
        0xFE,
        (
            "为了今天，\x01",
            "我存了好多零用钱呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "要用这些钱带女朋友\x01",
            "玩遍克洛斯贝尔哦！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2929 end

    def Function_23_2980(): pass

    label("Function_23_2980")

    TalkBegin(0xFE)

    #C0032
    ChrTalk(
        0xFE,
        (
            "嗯～我觉得，像我们这个年龄的人，\x01",
            "应该没有足够的米拉\x01",
            "把这里玩遍……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "呵呵，但看他这么起劲，\x01",
            "我就好好期待吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2980 end

    def Function_24_29FC(): pass

    label("Function_24_29FC")

    TalkBegin(0xFE)

    #C0034
    ChrTalk(
        0xFE,
        (
            "每年都是两个女生\x01",
            "一起旅行……也太奇怪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "今年这时期也不对……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_29FC end

    def Function_25_2A4C(): pass

    label("Function_25_2A4C")

    TalkBegin(0xFE)

    #C0036
    ChrTalk(
        0xFE,
        (
            "没、没有那回事～\x01",
            "大家都是这样的，也有两个男人一起旅行的。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "我们两个好朋友难得出来玩，\x01",
            "不要说这种扫兴的话啦～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_2A4C end

    def Function_26_2AC9(): pass

    label("Function_26_2AC9")

    TalkBegin(0xFE)

    #C0038
    ChrTalk(
        0xFE,
        (
            "都到最终日了吗～……\x01",
            "快乐的时间\x01",
            "总是一下就过去了呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_2AC9 end

    def Function_27_2B0A(): pass

    label("Function_27_2B0A")

    TalkBegin(0xFE)

    #C0039
    ChrTalk(
        0xFE,
        (
            "不是挺好的吗，\x01",
            "因此也留下了\x01",
            "很多美好的回忆嘛。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_2B0A end

    def Function_28_2B45(): pass

    label("Function_28_2B45")

    TalkBegin(0xFE)

    #C0040
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "我在米修拉姆住宿的时候\x01",
            "真是倒了大霉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "晚上竟然有军犬到处跑哦！\x01",
            "但这个人竟然\x01",
            "还睡得那么死……！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_2B45 end

    def Function_29_2BBE(): pass

    label("Function_29_2BBE")

    TalkBegin(0xFE)

    #C0042
    ChrTalk(
        0xFE,
        (
            "喂喂，别生气啦。\x01",
            "只是偶尔有\x01",
            "魔兽闯进来了而已吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "所以不要再耍性子，\x01",
            "说什么明年不去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_2BBE end

    def Function_30_2C26(): pass

    label("Function_30_2C26")

    TalkBegin(0xFE)

    #C0044
    ChrTalk(
        0xFE,
        (
            "呼～去雷米菲利亚出差，\x01",
            "而且还是当天往返，\x01",
            "果然够辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "……嗯，老婆还在家等着，\x01",
            "真想早点回去休息啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_2C26 end

    def Function_31_2C9E(): pass

    label("Function_31_2C9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2DAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D47")

    #C0046
    ChrTalk(
        0xFE,
        (
            "空港有飞往利贝尔和雷米菲利亚的\x01",
            "国际定期船。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "今天会有货物从利贝尔那边\x01",
            "送过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "好了～那个什么卡普亚特急便\x01",
            "应该快到了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2DA8")

    label("loc_2D47")


    #C0049
    ChrTalk(
        0xFE,
        (
            "今天会有货物从利贝尔那边\x01",
            "送过来。\x01",
            "我正在这里等呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "那个什么卡普亚特急便\x01",
            "应该快到了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA8")

    TalkEnd(0xFE)
    Return()

    label("loc_2DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E53")

    #C0051
    ChrTalk(
        0xFE,
        (
            "哦……是你们，\x01",
            "又有工作了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "……要不是我疏忽大意，\x01",
            "昨天那个孩子\x01",
            "也就不会遭遇危险了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "今后在工作方面，\x01",
            "我决心加强责任感，\x01",
            "认真处事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2EB5")

    label("loc_2E53")


    #C0054
    ChrTalk(
        0xFE,
        (
            "好了～今天\x01",
            "预计要接收外国\x01",
            "运输公司送来的货物。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "昨天被老爸\x01",
            "教训了，\x01",
            "一定要将功补过才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EB5")

    TalkEnd(0xFE)
    Return()

    # Function_31_2C9E end

    def Function_32_2EB9(): pass

    label("Function_32_2EB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A7")

    #C0056
    ChrTalk(
        0xFE,
        (
            "啊，是你们……\x01",
            "巴士怎么样了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#0000F嗯，果然是出现了\x01",
            "引擎故障……\x02\x03",

            "我们把魔兽赶走，\x01",
            "成功确保了安全。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#0200F至于故障方面，路过的游击士\x01",
            "正在进行处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "哦，这样啊，\x01",
            "那就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "嗯嗯，交给游击士处理的话，\x01",
            "就不会有问题了。\x02",
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
        "#0006F是、是啊。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#0108F艾丝蒂尔和约修亚\x01",
            "也救了我们……\x01",
            "真是无言以对呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        (
            "#0306F风头完全被他们\x01",
            "抢走了呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 0)
    Jump("loc_3164")

    label("loc_30A7")


    #C0064
    ChrTalk(
        0xFE,
        (
            "总之，巴士很快\x01",
            "就会回来了吧？\x01",
            "没出大事就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "也得谢谢你们呢。\x01",
            "偶然路过，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3164")

    #C0066
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，谢谢……\x01",
            "（下次可不能再依赖偶然，\x01",
            "　要更加努力地工作啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_3164")

    Jump("loc_31BE")

    label("loc_3169")


    #C0067
    ChrTalk(
        0xFE,
        (
            "巴士的通讯\x01",
            "好像完全断绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "只要去郊外\x01",
            "看看情况就好了。\x01",
            "总之就拜托你们啦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31BE")

    TalkEnd(0xFE)
    Return()

    # Function_32_2EB9 end

    def Function_33_31C2(): pass

    label("Function_33_31C2")

    TalkBegin(0xFE)

    #C0069
    ChrTalk(
        0xFE,
        "我们打算在车站和空港盯梢。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "唐古拉姆门那边就拜托你们了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_31C2 end

    def Function_34_320B(): pass

    label("Function_34_320B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_36BC")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3388")
    TurnDirection(0xFE, 0x10A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_334A")

    #C0071
    ChrTalk(
        0xFE,
        (
            "呃啊……\x01",
            "一科的达德利搜查官！？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "……嘿嘿，早上好～\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x10A,
        (
            "#0603F都已经快中午了，说什么呢！\x02\x03",

            "#0600F雷蒙德，探听工作\x01",
            "有进展吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "啊，没问题啦。\x01",
            "非常顺利～\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x10A,
        (
            "#0603F………………………………\x01",
            "（所以说，搜查二科还是靠不住啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD9, 2)
    SetScenarioFlags(0x0, 4)
    Jump("loc_337C")

    label("loc_334A")


    #C0076
    ChrTalk(
        0xFE,
        "嘿嘿，要努力探听才行呢。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "工作，工作……\x02",
    )

    CloseMessageWindow()

    label("loc_337C")

    OP_93(0xFE, 0x10E, 0x0)
    Jump("loc_36B7")

    label("loc_3388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3660")

    #C0078
    ChrTalk(
        0xFE,
        "咦～这不是支援科的各位吗？\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "莫非是来帮忙的吗？\x01",
            "喏，就是空港那件事。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F9")
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
        "#0105F空港出什么事了吗……？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "啊～你们还没听说吗～\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "算啦，也许还是不知道为好。\x01",
            "不然会被一科随意使唤到死呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0005F（？？？\x01",
            "  到底发生了什么事呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3658")

    label("loc_34F9")

    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0084
    ChrTalk(
        0x101,
        "#0005F啊，不，倒不是这样……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0300F话说～情况\x01",
            "怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "嗯～虽然不好大声宣扬，\x01",
            "总之，可以说是『尚在搜索』吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "二科也被编入了搜索小组，\x01",
            "我和警督今天\x01",
            "都被使唤得很惨呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#0108F虽然有可能是假情报，\x01",
            "但也得以防万一呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "说得没错。\x01",
            "真是麻烦的事件啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3658")

    SetScenarioFlags(0x0, 4)
    Jump("loc_36B7")

    label("loc_3660")


    #C0090
    ChrTalk(
        0xFE,
        "今天要努力探听情报呢～\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "要在对市民隐瞒实情的同时\x01",
            "进行调查工作，还真是麻烦啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B7")

    Jump("loc_36ED")

    label("loc_36BC")


    #C0092
    ChrTalk(
        0xFE,
        (
            "本来就人手不足了……\x01",
            "唉，也只好尽力而为了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36ED")

    TalkEnd(0xFE)
    Return()

    # Function_34_320B end

    def Function_35_36F1(): pass

    label("Function_35_36F1")

    TalkBegin(0xFE)

    #C0093
    ChrTalk(
        0xFE,
        (
            "巴士还没来吗？\x01",
            "我还有急事呢……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_36F1 end

    def Function_36_371D(): pass

    label("Function_36_371D")

    TalkBegin(0xFE)

    #C0094
    ChrTalk(
        0xFE,
        "我要去探望孙子。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "他住院很久了，\x01",
            "应该很无聊吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_371D end

    def Function_37_375D(): pass

    label("Function_37_375D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_37A9")

    #C0096
    ChrTalk(
        0xFE,
        "咦？巴士怎么还不来啊！\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "不是又出\x01",
            "什么意外了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382C")

    label("loc_37A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3807")

    #C0098
    ChrTalk(
        0xFE,
        (
            "咳咳……\x01",
            "喂，到底要等到什么时候啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "应该早就过了\x01",
            "发车时刻了啊！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_382C")

    label("loc_3807")


    #C0100
    ChrTalk(
        0xFE,
        (
            "我可是感冒了呢。\x01",
            "不能快点来吗！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_382C")

    TalkEnd(0xFE)
    Return()

    # Function_37_375D end

    def Function_38_3830(): pass

    label("Function_38_3830")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3872")

    #C0101
    ChrTalk(
        0xFE,
        "探病探病～⊥\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "我现在要去\x01",
            "探望我男朋友！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A9")

    label("loc_3872")


    #C0103
    ChrTalk(
        0xFE,
        (
            "我们正要\x01",
            "去医院看病……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "到底发生什么事了呢？\x02",
    )

    CloseMessageWindow()

    label("loc_38A9")

    TalkEnd(0xFE)
    Return()

    # Function_38_3830 end

    def Function_39_38AD(): pass

    label("Function_39_38AD")

    TalkBegin(0xFE)

    #C0105
    ChrTalk(
        0xFE,
        "感冒好像恶化了。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "咳咳……\x01",
            "嗯～因为最近经常\x01",
            "熬夜工作吧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_38AD end

    def Function_40_38F8(): pass

    label("Function_40_38F8")

    TalkBegin(0xFE)

    #C0107
    ChrTalk(
        0xFE,
        (
            "我今天要陪公公\x01",
            "去医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "我明明和他说过，\x01",
            "让他早点去医院的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_38F8 end

    def Function_41_3950(): pass

    label("Function_41_3950")

    TalkBegin(0xFE)

    #C0109
    ChrTalk(
        0xFE,
        (
            "真让人头疼啊……\x01",
            "探病时间是到五点半为止。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "这样下去的话，\x01",
            "刚到那里就得直接回头了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_3950 end

    def Function_42_39B3(): pass

    label("Function_42_39B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3A06")

    #N0111
    NpcTalk(
        0xFE,
        "市民",
        "喂～巴士怎么还没个影啊～\x02",
    )

    CloseMessageWindow()

    #N0112
    NpcTalk(
        0xFE,
        "市民",
        "这到底怎么回事啊～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B49")

    label("loc_3A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3B13")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AAE")

    #C0113
    ChrTalk(
        0xFE,
        "达德利搜查官，您辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "自那以来，高层也是一言不发，\x01",
            "我们很难把握情况……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "空港这边的事情就交给我们吧，\x01",
            "日落之前会解决好的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B0E")

    label("loc_3AAE")


    #C0116
    ChrTalk(
        0xFE,
        (
            "……空港现在\x01",
            "被我们搜查一科封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "特别任务支援科，你们不要多管闲事，\x01",
            "拖我们后腿啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B0E")

    Jump("loc_3B49")

    label("loc_3B13")


    #C0118
    ChrTalk(
        0xFE,
        (
            "这里由我们\x01",
            "搜查一科管辖。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        "禁止擅自入内。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 6)

    label("loc_3B49")

    TalkEnd(0xFE)
    Return()

    # Function_42_39B3 end

    def Function_43_3B4D(): pass

    label("Function_43_3B4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B91")

    #C0120
    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "又要去向\x01",
            "市政厅投诉了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BBE")

    label("loc_3B91")


    #C0121
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "今天还是别等了，直接回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BBE")

    Jump("loc_3BFA")

    label("loc_3BC3")


    #C0122
    ChrTalk(
        0xFE,
        (
            "我们是要去\x01",
            "探望一个朋友……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        "发生什么事了呢？\x02",
    )

    CloseMessageWindow()

    label("loc_3BFA")

    TalkEnd(0xFE)
    Return()

    # Function_43_3B4D end

    def Function_44_3BFE(): pass

    label("Function_44_3BFE")

    TalkBegin(0xFE)

    #C0124
    ChrTalk(
        0xFE,
        (
            "警察在问有没有见过\x01",
            "可疑人物……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "但光说什么可疑，\x01",
            "谁会知道啊！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_3BFE end

    def Function_45_3C4D(): pass

    label("Function_45_3C4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D29")

    #C0126
    ChrTalk(
        0xFE,
        (
            "辛苦了，\x01",
            "我们这边正在进行周边排查。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "搜查二科也出动了，\x01",
            "再有三个小时应该就能弄清楚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x10A,
        (
            "#0608F是吗……\x02\x03",

            "#0600F我暂时要单独行动，\x01",
            "艾玛，这边就交给你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "嗯，请放心吧！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3D89")

    label("loc_3D29")


    #C0130
    ChrTalk(
        0xFE,
        (
            "辛苦了，\x01",
            "我们这边正在进行周边排查。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "搜查二科也出动了，\x01",
            "再有三个小时应该就能弄清楚了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D89")

    Jump("loc_3E13")

    label("loc_3D8E")


    #C0132
    ChrTalk(
        0xFE,
        (
            "特别任务支援科，你们\x01",
            "不要太多管闲事。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "你们目前应该处于\x01",
            "达德利长官的指挥之下……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "绝不允许抛下达德利长官，\x01",
            "擅自行动哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E13")

    TalkEnd(0xFE)
    Return()

    # Function_45_3C4D end

    def Function_46_3E17(): pass

    label("Function_46_3E17")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0135
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
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
            "要钓鱼吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40FC")
    OP_E0(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_3EE8")
    MiniGame(0x6, 0xA, 0xCB98, 0x384, 0xFFFE6934, 0x65, 0x105F4, 0xFFFFE8F4, 0xFFFE7898)
    Jump("loc_40FC")

    label("loc_3EE8")

    MiniGame(0x6, 0xB, 0xCB98, 0x384, 0xFFFE6934, 0x65, 0x105F4, 0xFFFFE8F4, 0xFFFE7898)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40FC")
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
        "罗伊德",
        (
            "#0011F呜哇……！！？\x01",
            "这、这、这是什么超级大鱼啊……！？\x02\x03",

            "#0006F还以为鱼竿都要折断了……\x01",
            "这种体积……真的能算是普通的鱼类吗？\x02\x03",

            "#0000F哈哈，算了。\x01",
            "……去跟钓公师团的分部长报告的话，\x01",
            "他一定会很开心的。\x02",
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

    label("loc_40FC")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_46_3E17 end

    def Function_47_4101(): pass

    label("Function_47_4101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_415D")
    TalkBegin(0xFF)
    SetChrName("")

    #A0138
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x02",
        )
    )

    CloseMessageWindow()

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在似乎早已过了\x01",
            "巴士的到达时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_420C")

    label("loc_415D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4183")
    Call(0, 68)
    Jump("loc_420C")

    label("loc_4183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4199")
    Call(0, 48)
    Jump("loc_420C")

    label("loc_4199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41AF")
    Call(0, 56)
    Jump("loc_420C")

    label("loc_41AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_41C0")
    Call(0, 5)
    Jump("loc_420C")

    label("loc_41C0")

    TalkBegin(0xFF)
    SetChrName("")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在早已过了\x01",
            "巴士的到达时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_420C")

    Return()

    # Function_47_4101 end

    def Function_48_420D(): pass

    label("Function_48_420D")

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
            "#0000F#5P下一班车的发车时间是……\x01",
            "十分钟之后吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#0100F#5P在这里稍等一下，\x01",
            "很快就会来了吧。\x02\x03",

            "#0104F乌尔斯拉医院啊……\x01",
            "好久没去那里了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0144
    ChrTalk(
        0x101,
        (
            "#0000F#12P嗯，我也是。\x02\x03",

            "#0006F本来打算回来之后\x01",
            "马上就过去拜访的，\x01",
            "可是每天都很忙呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0145
    ChrTalk(
        0x102,
        "#0105F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x104,
        (
            "#0305F#5P你说要去医院，\x01",
            "难道有哪里不舒服吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#0004F#12P不……\x01",
            "我有熟人在那里工作。\x02\x03",

            "#0002F人家以前很照顾我，\x01",
            "所以回来后一直都想去打个招呼的。\x02\x03",

            "不过我们双方都很忙，\x01",
            "就一直拖了下来。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        "#0100F#5P原来如此，是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        (
            "#0300F#5P在医院工作啊，\x01",
            "是个医生吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(200)

    #C0150
    ChrTalk(
        0x101,
        (
            "#0000F#6P不，是护士。\x02\x03",

            "好像是年轻护士们的带头人，\x01",
            "每天都忙得不可开交。\x02",
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
            "#0305F#5P护士……就是那样的吧？\x02\x03",

            "穿着护士服，\x01",
            "温柔地给人量体温的姐姐？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#0005F#6P哎……\x02\x03",

            "#0000F嗯、嗯，护士服毕竟\x01",
            "是工作装嘛，我想应该会穿的。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        "#0301F#5P那位姐姐，多大了？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        (
            "#0004F#6P比我大五岁，\x01",
            "所以是二十三岁吧……？\x02\x03",

            "#0000F就住在我家的隔壁，\x01",
            "对我而言，就如同亲姐姐一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        "#0301F#5P是美女？\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#0011F#6P嗯、嗯～……\x01",
            "反正我认为她很漂亮。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#0303F#5P大我两岁的姐姐……\x01",
            "而且还穿着护士服吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0158
    ChrTalk(
        0x104,
        (
            "#5P#0307F#4S太好了！\x01",
            "我热血沸腾了！\x02",
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
            "#5P#0309F哎呀～我可真幸福啊！\x02\x03",

            "能够遇到你这样的\x01",
            "挚友！\x02\x03",

            "#0302F所以呢，就麻烦你介绍一下啦☆\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#0006F#6P我说你啊……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0106F#5P唉……\x01",
            "男人就是这样。\x02",
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
            "#0011F#12P喂，不要\x01",
            "把我也算进去啊！\x02",
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
            "#0105F#6P缇欧，你怎么了？\x02\x03",

            "从刚才起，好像就\x01",
            "一直在想什么心事……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4887():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4887)

    def lambda_4894():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4894)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0164
    ChrTalk(
        0x103,
        (
            "#0208F#5P啊……没有……\x01",
            "只是我不太喜欢医院。\x02\x03",

            "#0206F消毒液的气味，\x01",
            "还有打针什么的，有点……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        "#0102F#6P是吗……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#0001F#12P那个，没问题吗？\x02\x03",

            "不然的话，缇欧可以——\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        (
            "#0203F#5P──没有问题。\x02\x03",

            "只是不太喜欢而已，\x01",
            "倒也算不上讨厌。\x02\x03",

            "#0211F要是说我不用去也可以，\x01",
            "我可是会生气的哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0011F#12P我、我不会说的啦。\x02\x03",

            "#0006F（好险好险……\x01",
            "  看来得当心点才行。）\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            "#0204F#5P而且，我也想\x01",
            "见见罗伊德前辈的\x01",
            "那位熟人……\x02\x03",

            "#0202F就是之前和你用通讯器聊天，\x01",
            "聊得很开心的那个人吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0170
    ChrTalk(
        0x101,
        "#0005F#12P你、你怎么会知道……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    def lambda_4AE8():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4AE8)
    Sleep(300)

    #C0171
    ChrTalk(
        0x102,
        (
            "#0104F#5P呵呵，像罗伊德的\x01",
            "姐姐一样的人啊。\x02\x03",

            "#0102F有点期待和她\x01",
            "见面了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        (
            "#0309F#5P噢噢，要说的话，\x01",
            "见姐姐都快变成主要活动了呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x104, 500)
    Sleep(500)

    #C0173
    ChrTalk(
        0x101,
        "#0011F#6P还、还是要以调查为重吧！？\x02",
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
        "#0106F#5P……还没来呢。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x103,
        "#0203F#5P过去三十分钟了……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        (
            "#0306F#5P喂喂，罗伊德。\x02\x03",

            "#0301F不是说十分钟之后\x01",
            "就会来的吗～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0177
    ChrTalk(
        0x101,
        (
            "#0006F#12P……你跟我说也没用啊。\x02\x03",

            "#0008F不过，还真奇怪啊。\x01",
            "确实是有些太迟了……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x30, 0x4)
    SetChrPos(0x30, -1000, 900, 3000, 180)

    #N0178
    NpcTalk(
        0x30,
        "青年的声音",
        (
            "#4P#2S啊……\x01",
            "果然没来啊。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x30, 3, 0, 49)

    def lambda_4DF9():

        label("loc_4DF9")

        TurnDirection(0x101, 0x30, 500)
        Yield()
        Jump("loc_4DF9")

    QueueWorkItem2(0x101, 1, lambda_4DF9)

    def lambda_4E0B():

        label("loc_4E0B")

        TurnDirection(0x102, 0x30, 500)
        Yield()
        Jump("loc_4E0B")

    QueueWorkItem2(0x102, 1, lambda_4E0B)

    def lambda_4E1D():

        label("loc_4E1D")

        TurnDirection(0x103, 0x30, 500)
        Yield()
        Jump("loc_4E1D")

    QueueWorkItem2(0x103, 1, lambda_4E1D)

    def lambda_4E2F():

        label("loc_4E2F")

        TurnDirection(0x104, 0x30, 500)
        Yield()
        Jump("loc_4E2F")

    QueueWorkItem2(0x104, 1, lambda_4E2F)
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
        "事务人员打扮的青年",
        (
            "#5P伤脑筋啊……\x01",
            "这可怎么办才好啊？\x02",
        )
    )

    CloseMessageWindow()

    #N0180
    NpcTalk(
        0x30,
        "事务人员打扮的青年",
        (
            "#5P即使尝试和那边进行导力通讯，\x01",
            "也根本无人应答……\x02",
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
            "#0001F#6P请问……\x01",
            "出什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#0101F#6P巴士好像\x01",
            "迟到很久了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x30, 0x101, 500)
    Sleep(300)

    #N0183
    NpcTalk(
        0x30,
        "事务人员打扮的青年",
        (
            "#11P那个～好像是\x01",
            "出了什么意外了。\x02",
        )
    )

    CloseMessageWindow()

    #N0184
    NpcTalk(
        0x30,
        "事务人员打扮的青年",
        (
            "#11P巴士的司机使用导力通讯\x01",
            "和这边联系过一次……\x02",
        )
    )

    CloseMessageWindow()

    #N0185
    NpcTalk(
        0x30,
        "事务人员打扮的青年",
        (
            "#11P但是中途突然断掉了，\x01",
            "之后就毫无应答了。\x02",
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
        "#0005F#6P这……！？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x103,
        "#0203F#6P……感觉好像有麻烦呢。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x104,
        (
            "#0305F#1P对了……\x01",
            "小哥，你是什么人？\x02",
        )
    )

    CloseMessageWindow()

    #N0189
    NpcTalk(
        0x30,
        "事务人员打扮的青年",
        (
            "#11P啊，我是克洛斯贝尔市\x01",
            "交通科的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x30,
        (
            "#11P负责管理在自治州\x01",
            "运行的巴士……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x30,
        (
            "#11P嗯～联络警备队又有些小题大做，\x01",
            "也只能拜托协会了吧。\x02",
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

    def lambda_52DE():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52DE)

    def lambda_52EB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_52EB)

    def lambda_52F8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_52F8)

    def lambda_5305():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5305)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    #C0192
    ChrTalk(
        0x101,
        "#0001F#11P（……各位，可以吗？）\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        "#0101F#6P（嗯，明白。）\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x103,
        "#0203F#6P（呼……没办法呢。）\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x104,
        "#0300F#1P（哎，这也是机缘巧合吧。）\x02",
    )

    CloseMessageWindow()

    def lambda_53B4():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53B4)

    def lambda_53C1():
        TurnDirection(0xFE, 0x30, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_53C1)

    def lambda_53CE():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_53CE)

    def lambda_53DB():
        TurnDirection(0xFE, 0x30, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_53DB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    #C0196
    ChrTalk(
        0x101,
        (
            "#0000F#6P请问……\x02\x03",

            "这个任务，能不能\x01",
            "交给我们去办？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0197
    ChrTalk(
        0x30,
        "#11P哎？\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x30,
        "#11P你们是……？\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#0000F#6P克洛斯贝尔警察局·特别\x01",
            "任务支援科的人。\x02\x03",

            "我们正准备前往医科大学\x01",
            "执行调查任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x30,
        "#11P哎，你们是警察局的人？\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x30,
        (
            "#11P对了……\x01",
            "我在杂志上看到过。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x30,
        (
            "#11P说警察也像协会一样，\x01",
            "开始为市民服务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#0006F#6P……那个，确切地说，\x01",
            "其实也不太一样。\x02\x03",

            "#0000F不过，去看看巴士的情况\x01",
            "应该还是没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x30,
        (
            "#11P是吗……\x01",
            "那就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x30,
        (
            "#11P要不，我再去委托\x01",
            "游击士协助你们吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        (
            "#0012F#6P不、不用了。\x01",
            "我想应该没问题的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0207
    ChrTalk(
        0x101,
        "#0000F#11P──各位，走吧。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        "#0100F#6P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        "#0302F#1P噢！\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x103,
        "#0202F#6P……明白。\x02",
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

    # Function_48_420D end

    def Function_49_576B(): pass

    label("Function_49_576B")


    def lambda_5770():
        OP_95(0xFE, -1000, 0, -7000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_5770)
    WaitChrThread(0x30, 1)

    def lambda_578E():
        OP_95(0xFE, -7000, 0, -13000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_578E)
    WaitChrThread(0x30, 1)
    OP_93(0x30, 0xB4, 0x1F4)
    Return()

    # Function_49_576B end

    def Function_50_57AF(): pass

    label("Function_50_57AF")

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

    def lambda_59B5():
        OP_95(0xFE, -320, 0, -25730, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_59B5)
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

    def lambda_5A22():
        OP_9D(0xFE, 0xFFFFE188, 0x0, 0xFFFF0344, 0xBB8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_5A22)
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

    def lambda_5A74():
        OP_96(0xFE, 0x3B6, 0x0, 0xFFFF06D2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_5A74)
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

    def lambda_5AD6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_5AD6)
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
    SetChrName("白狼")

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

    def lambda_5C10():
        OP_96(0xFE, 0xFFFFC856, 0x0, 0xFFFEEA94, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_5C10)
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
            "当天晚上……\x01",
            "回到支援科的罗伊德等人\x01",
            "开始整理当天的调查报告。\x02\x03",

            "在将最新查明的事实与证言，\x01",
            "以及更多疑点和目前的推测等情报\x01",
            "进行了简单明了的总结之后……\x02\x03",

            "不知不觉，都已到了第二天，\x01",
            "身心疲惫的罗伊德等人\x01",
            "便回到各自的房间休息去了。\x07\x00\x02",
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

    # Function_50_57AF end

    def Function_51_5DB0(): pass

    label("Function_51_5DB0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DCB")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_51_5DB0")

    label("loc_5DCB")

    Return()

    # Function_51_5DB0 end

    def Function_52_5DCC(): pass

    label("Function_52_5DCC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DEA")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_52_5DCC")

    label("loc_5DEA")

    Return()

    # Function_52_5DCC end

    def Function_53_5DEB(): pass

    label("Function_53_5DEB")

    Sound(465, 0, 100, 0)
    Sleep(4500)
    Sound(471, 0, 100, 0)
    Return()

    # Function_53_5DEB end

    def Function_54_5DFB(): pass

    label("Function_54_5DFB")

    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Return()

    # Function_54_5DFB end

    def Function_55_5E17(): pass

    label("Function_55_5E17")

    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 85, 0)
    Sleep(500)
    Sound(832, 0, 70, 0)
    Sleep(500)
    Sound(832, 0, 55, 0)
    Return()

    # Function_55_5E17 end

    def Function_56_5E3C(): pass

    label("Function_56_5E3C")

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
            "#0000F#5P下一班车的发车时间是……\x01",
            "啊，好像就快来了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_5F70")

    #C0214
    ChrTalk(
        0x102,
        (
            "#0109F#11P呵呵……\x01",
            "时间赶得正好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FC1")

    label("loc_5F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_5F98")

    #C0215
    ChrTalk(
        0x103,
        "#0204F#11P时机正好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FC1")

    label("loc_5F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_5FC1")

    #C0216
    ChrTalk(
        0x104,
        "#0304F#11P时候赶得刚好啊。\x02",
    )

    CloseMessageWindow()

    label("loc_5FC1")

    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x153,
        "#1110F#5P什么来了～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    TurnDirection(0xEF, 0x153, 500)

    #C0218
    ChrTalk(
        0x101,
        (
            "#0004F#12P嗯，就是琪雅\x01",
            "想坐的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x153,
        "#1105F#5P哎～……？\x02",
    )

    CloseMessageWindow()
    Sound(467, 0, 100, 0)
    BeginChrThread(0x33, 1, 0, 60)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6094():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6094)
    Sleep(50)
    OP_93(0xEF, 0xB4, 0x1F4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_60CC")

    #C0220
    ChrTalk(
        0x102,
        "#0102F已经来了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6111")

    label("loc_60CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_60F0")

    #C0221
    ChrTalk(
        0x103,
        "#0202F已经来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6111")

    label("loc_60F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_6111")

    #C0222
    ChrTalk(
        0x104,
        "#0302F已经来了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_6111")

    EndChrThread(0x33, 0x1)
    Fade(500)
    OP_68(2080, 600, -29850, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    ClearMapObjFlags(0x1, 0x4)

    def lambda_6153():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_6153)
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

    def lambda_6221():
        OP_96(0xFE, 0xFFFFEB4C, 0x0, 0xFFFFCD38, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_6221)
    Sleep(1000)
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x2B, 1)

    #C0223
    ChrTalk(
        0x153,
        (
            "#1107F#6P哇啊啊啊啊！？\x01",
            "好大的车哦！\x02",
        )
    )

    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#0002F#6P琪雅，这就叫\x01",
            "巴士哦。\x02",
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
            "#1105F#6P哇哇……\x01",
            "出来了好多人哦！？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#0004F#6P嗯，是去医院的人\x01",
            "回到市里来了。\x02\x03",

            "#0000F我们也要乘坐\x01",
            "这个去医院呢。\x02",
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
            "#1101F#5P琪雅要坐这个吗～！？\x02\x03",

            "罗伊德，你们也一起！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    TurnDirection(0xEF, 0x153, 500)

    #C0228
    ChrTalk(
        0x101,
        "#0002F#12P嗯，当然。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x153,
        (
            "#1109F#5P嘿嘿……\x02\x03",

            "#1110F那个那个，赶快坐上去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_6436")

    #C0230
    ChrTalk(
        0x102,
        (
            "#0109F#5P呵呵……\x01",
            "小心脚下哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6493")

    label("loc_6436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_6466")

    #C0231
    ChrTalk(
        0x103,
        (
            "#0204F#5P呵……\x01",
            "请注意脚下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6493")

    label("loc_6466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_6493")

    #C0232
    ChrTalk(
        0x104,
        (
            "#0309F#5P哈哈……\x01",
            "当心脚下啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6493")

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

    # Function_56_5E3C end

    def Function_57_64E8(): pass

    label("Function_57_64E8")

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

    # Function_57_64E8 end

    def Function_58_651D(): pass

    label("Function_58_651D")

    EndChrThread(0x18, 0x3)
    EndChrThread(0x17, 0x3)
    EndChrThread(0x1E, 0x3)
    EndChrThread(0x11, 0x3)
    Return()

    # Function_58_651D end

    def Function_59_652E(): pass

    label("Function_59_652E")

    SetChrPos(0xFE, -6080, 600, -13010, 270)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_6559():
        OP_95(0xFE, -8730, 180, -12970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6559)

    def lambda_6573():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6573)
    WaitChrThread(0xFE, 1)

    def lambda_6588():
        OP_95(0xFE, -8850, 180, -7610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6588)
    WaitChrThread(0xFE, 1)

    def lambda_65A6():
        OP_95(0xFE, -1260, 0, -7620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65A6)
    WaitChrThread(0xFE, 1)

    def lambda_65C4():
        OP_95(0xFE, -50, 900, 3490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65C4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_59_652E end

    def Function_60_65E2(): pass

    label("Function_60_65E2")

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

    # Function_60_65E2 end

    def Function_61_662F(): pass

    label("Function_61_662F")

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

    # Function_61_662F end

    def Function_62_6672(): pass

    label("Function_62_6672")

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
            "#0005F#11P咦……\x01",
            "排了好长的队啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        "#0100F#11P以这个时间来说，真是少见呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0235
    ChrTalk(
        0x103,
        (
            "#0203F#11P……很奇怪呢。\x02\x03",

            "#0200F五分钟之前应该\x01",
            "刚走了一班车才对……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6835():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6835)
    Sleep(50)

    def lambda_6845():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6845)
    Sleep(50)

    def lambda_6855():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6855)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0236
    ChrTalk(
        0x101,
        "#0001F#6P是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x104,
        "#0301F#5P唔……\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x10E, 0x1F4)
    OP_68(-7200, 1000, -7930, 2500)

    def lambda_68B4():
        OP_95(0xFE, -6860, 0, -8060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_68B4)
    Sleep(300)

    def lambda_68D1():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68D1)
    Sleep(50)

    def lambda_68E1():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68E1)
    Sleep(50)

    def lambda_68F1():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_68F1)
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
            "#0300F#11P哟，这位老兄。\x02\x03",

            "莫非巴士\x01",
            "迟到了吗？\x02",
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
        "#5P嗯，好像是啊。\x02",
    )

    CloseMessageWindow()

    #N0240
    NpcTalk(
        0xE,
        "青年",
        (
            "#5P我已经在这里等了\x01",
            "足足二十分钟了，\x01",
            "但一直没车来呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0241
    NpcTalk(
        0xE,
        "青年",
        (
            "#5P伤脑筋啊……\x01",
            "探病时间都要过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#0301F#11P是吗……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    OP_4C(0xE, 0xFF)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_68(-3580, 1000, -8640, 3000)

    def lambda_6A2E():

        label("loc_6A2E")

        TurnDirection(0x101, 0x104, 500)
        Yield()
        Jump("loc_6A2E")

    QueueWorkItem2(0x101, 1, lambda_6A2E)

    def lambda_6A40():

        label("loc_6A40")

        TurnDirection(0x102, 0x104, 500)
        Yield()
        Jump("loc_6A40")

    QueueWorkItem2(0x102, 1, lambda_6A40)

    def lambda_6A52():

        label("loc_6A52")

        TurnDirection(0x103, 0x104, 500)
        Yield()
        Jump("loc_6A52")

    QueueWorkItem2(0x103, 1, lambda_6A52)

    def lambda_6A64():
        OP_95(0xFE, -3850, 0, -8250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A64)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x102, 500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    OP_6F(0x1)

    #C0243
    ChrTalk(
        0x104,
        "#0306F#5P看来果然迟到了啊。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x102,
        (
            "#0108F#12P难不成……\x01",
            "又是引擎故障吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x103,
        "#0206F#11P有这个可能呢。\x02",
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6B55():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B55)
    Sleep(50)

    def lambda_6B65():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B65)
    Sleep(50)

    def lambda_6B75():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6B75)
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
            "#0001F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性的声音")

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我是达德利，\x01",
            "你们那边的情况如何了？\x02",
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
            "#0005F啊，您辛苦了。\x02\x03",

            "#0000F我们已经顺利取得\x01",
            "游击士协会的协助了。\x02",
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
            "将克洛斯贝尔分部的全体游击士\x01",
            "接受委托，对黑手党及失踪者\x01",
            "进行搜索的情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0250
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哼……\x01",
            "欠了马克莱因一个人情啊。\x02\x03",

            "也罢，凭他们那些人的实力，\x01",
            "应该能取得些什么成果吧。\x02\x03",

            "——至于我们这边，\x01",
            "上层那些人总算开始对\x01",
            "黑手党成员的消失感到不安了。\x02\x03",

            "但是，在正式出动之前，\x01",
            "可能还要花点时间。\x02",
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
            "#0003F明白了。\x02\x03",

            "#0001F对了──\x01",
            "我们现在正在空港附近，\x01",
            "炸弹恐吓事件怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0252
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哼，那个很可能只是\x01",
            "彻头彻尾的假情报。\x02\x03",

            "已经用最新的导力探测器\x01",
            "在空港内查了个遍，\x01",
            "但是什么也没查到。\x02",
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
            "#0013F这件事果然和黑手党的动向\x01",
            "存在什么关系吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0254
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "科里现在也在查这条线。\x02\x03",

            "——慢着，\x01",
            "你们说在空港附近……\x02\x03",

            "难不成，又打算\x01",
            "插手那边的事？\x02",
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
            "#0000F不，其实我们\x01",
            "正准备去乌尔斯拉医院。\x02\x03",

            "关于药物成分调查的联络迟迟未到，\x01",
            "所以我们打算直接过去问问。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0256
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "怎么，还没问来吗？\x02\x03",

            "真是的，所以说新手就是新手。\x01",
            "像这种重要的联络，应该事先定好\x01",
            "确切的时间，迅速了结……\x02",
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
            "#0006F对、对不起。\x01",
            "（确实太过马虎了吗……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0258
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "只要能检明药物的成分，\x01",
            "我这边也就更容易说动上层。\x02\x03",

            "现在一切都寄希望于\x01",
            "那名医生的努力……\x02\x03",

            "……说起来，\x01",
            "那名医生叫什么名字？\x02",
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
            "#0005F啊，我没说过吗？\x02\x03",

            "#0000F他叫做约亚西姆·琼塔，\x01",
            "是负责神经科与药物学的副教授。\x02\x03",

            "虽然才三十多岁，\x01",
            "但据说能力很强，评价很高。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0260
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "唔，那样的话，\x01",
            "可能还有点希望……\x02\x03",

            "——嗯？\x02",
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
            "#0001F嗯？怎么了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0262
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "等一下……\x01",
            "你说约亚西姆·琼塔？\x02\x03",

            "是个戴着眼镜，\x01",
            "感觉有点超然的男子吗？\x02",
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
            "#0005F嗯，没错……\x01",
            "您见过他吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1388)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

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
            "#0001F那个，达德利警官……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……大概是在\x01",
            "两个多月之前见过。\x02\x03",

            "在审问于彩虹剧团的预演中\x01",
            "企图暗杀市长的犯人——\x02\x03",

            "原秘书阿奈斯特\x01",
            "的时候。\x02",
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
            "#0005F哎？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7203", 0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赛尔盖长官可能告诉过你们，\x01",
            "阿奈斯特精神完全错乱了。\x02\x03",

            "无奈之下，就把他以前\x01",
            "经常找的心理咨询师\x01",
            "从乌尔斯拉医院叫来了。\x02\x03",

            "这样一来，总算才能\x01",
            "顺利进行审问……\x02",
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
            "#0011F请、请等一下。\x02\x03",

            "莫非……\x01",
            "约亚西姆医生就是阿奈斯特的……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，就是他的主治医生。\x02\x03",

            "当时觉得不愧是乌尔斯拉医院的\x01",
            "医生，还挺佩服的……\x02\x03",

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

            "#0013F……明白了，\x01",
            "我会不动声色地试探他一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0272
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，你去试试吧。\x02\x03",

            "总之，尽量抓紧时间。\x01",
            "——我会再联系你。\x02",
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
            "#0105F#12P怎、怎么了？\x01",
            "好像说了什么奇怪的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x103,
        (
            "#0205F#11P那个秘书与约亚西姆医生\x01",
            "之间有什么关系吗？\x02",
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
        "#0003F#6P嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将达德利透露的情报转告给了艾莉等人。\x07\x00\x02",
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
        "#0101F#12P这、这……\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        (
            "#0303F#5P感觉一时无法完全理解啊……\x02\x03",

            "#0301F现在回想起来，\x01",
            "那个混蛋秘书当时的态度\x01",
            "与惊人蛮力，不管怎么想都……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x103,
        (
            "#0206F#11P好像与矿工冈兹先生\x01",
            "的情况别无二致呢。\x02\x03",

            "#0208F而且，他的主治医生\x01",
            "居然就是约亚西姆医生……\x02",
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
            "#0101F#12P我、我现在就向医院的\x01",
            "服务台确认一下。\x02\x03",

            "问问约亚西姆医生\x01",
            "在那之后有没有外出——\x02",
        )
    )

    CloseMessageWindow()

    def lambda_79C2():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79C2)

    def lambda_79CF():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_79CF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0282
    ChrTalk(
        0x101,
        "#0001F#6P嗯，拜托了。\x02",
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

            "#0108F……不行，没人接。\x02\x03",

            "好像也没有\x01",
            "占线……\x02",
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
            "#0203F#11P──迟到的巴士加上\x01",
            "联络不上的医院……\x02\x03",

            "#0201F还有最新得知的\x01",
            "意外人际关系吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#0301F#5P……再怎么说，这也很难\x01",
            "用单纯的巧合来解释吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(150)

    #C0286
    ChrTalk(
        0x101,
        (
            "#0003F#6P嗯……\x02\x03",

            "#0013F──天很快就要黑了，\x01",
            "尽快赶往乌尔斯拉医院吧。\x02\x03",

            "要是遇到巴士的话，\x01",
            "就半路拦车乘上去好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x102,
        "#0101F#12P嗯……！\x02",
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

    # Function_62_6672 end

    def Function_63_7CC7(): pass

    label("Function_63_7CC7")

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
            "调查停靠站的告示牌后，\x01",
            "就能乘坐导力巴士。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "进而便可迅速移动至所选目的地，\x01",
            "以更高的效率来往于各处。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 7)
    EventEnd(0x5)
    Return()

    # Function_63_7CC7 end

    def Function_64_7D7E(): pass

    label("Function_64_7D7E")

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
            "#12P#0300F这条大河\x01",
            "就是羽扇河吗？\x02\x03",

            "#0305F浮在正中的\x01",
            "那座建筑是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        "#6P#0003F嗯～我想是某种遗迹吧……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        (
            "#12P#0203F数据库里也没有相关的详细情报呢。\x02\x03",

            "#0200F只是，这里好像被指定为\x01",
            "禁止入内的区域了。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        (
            "#6P#0100F不知道是真是假，\x01",
            "不过，听说向那个遗迹\x01",
            "祈求姻缘很灵验哦。\x02\x03",

            "#0104F据说，只要男方站在这个观景台的左边，\x01",
            "女方站在右边来祈祷，\x01",
            "两人就能一生永不分开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        (
            "#12P#0306F这、这还真是\x01",
            "像模像样的都市传说啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#6P#0000F格蕾丝小姐委托我们拍摄的照片，\x01",
            "在这里似乎能拍到很不错的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85AD")
    TurnDirection(0x101, 0x102, 500)

    #C0296
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么艾莉，\x01",
            "可以拜托你来拍照吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0297
    ChrTalk(
        0x102,
        (
            "#6P#0108F哎，好的。\x01",
            "虽然我没什么自信……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0298
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

    #C0299
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

    #C0300
    ChrTalk(
        0x103,
        (
            "#12P#0200F外行和专家所拍出的照片，\x01",
            "差别可是一目了然的。\x02\x03",

            "#0203F不过，某些粗神经的人\x01",
            "大概无法理解这种细致的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0301
    ChrTalk(
        0x104,
        (
            "#12P#0306F唔……\x01",
            "你在说谁啊，说谁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        (
            "#6P#0000F好啦好啦，\x01",
            "总之就交给艾莉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        (
            "#6P#0100F那么……\x01",
            "我来试试看吧。\x02",
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
            "#6P#0103F……呼，\x01",
            "为了保险起见，我多拍了几张。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        (
            "#6P#0000F看样子，似乎已经拍好了呢。\x02\x03",

            "感觉怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
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

    #C0307
    ChrTalk(
        0x103,
        (
            "#12P#0200F艾莉前辈似乎\x01",
            "找回感觉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#12P#0300F哼……\x01",
            "反正只有我完全搞不懂。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x101,
        (
            "#6P#0000F如果发现了这种风景漂亮的地方，\x01",
            "就再拍些照片吧。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88B7")

    label("loc_85AD")

    TurnDirection(0x101, 0x102, 500)

    #C0310
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么……\x01",
            "艾莉，麻烦你拍照了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x102,
        "#6P#0100F嗯，知道了。\x02",
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
            "#6P#0100F……呼，\x01",
            "大概就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_872F")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_872F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_8746")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_875D")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_875D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_8774")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8774")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_878B")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_878B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_87A2")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_87B9")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_87D0")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_87E7")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8877")

    #C0313
    ChrTalk(
        0x101,
        (
            "#6P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "这样一来，就拍完了格蕾丝小姐\x01",
            "所要求的五张照片了。\x01",
            "现在随时都可以去交付了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88B7")

    label("loc_8877")


    #C0314
    ChrTalk(
        0x101,
        (
            "#6P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88B7")

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

    # Function_64_7D7E end

    def Function_65_88F7(): pass

    label("Function_65_88F7")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A9B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A15")

    #C0315
    ChrTalk(
        0x10A,
        (
            "#0603F……这边的事\x01",
            "交给一科的人就行了……\x02\x03",

            "#0601F若是没有高层那边的问题，\x01",
            "本应集中全部人手去\x01",
            "调查鲁巴彻那边的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x103,
        (
            "#0200F达德利警官\x01",
            "似乎很烦恼。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，一科好像也有\x01",
            "各种麻烦事嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x10A,
        (
            "#0600F……闭嘴，\x01",
            "我们只需做好\x01",
            "自己该做的事！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A96")

    label("loc_8A15")


    #C0319
    ChrTalk(
        0x10A,
        (
            "#0601F……你想去哪里？\x01",
            "空港的事\x01",
            "就交给搜查一科处理！\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        "#0005F说、说得对啊。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        (
            "#0108F（达德利警官好像\x01",
            "  十分焦躁呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A96")

    Jump("loc_8BD4")

    label("loc_8A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B9F")
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B4D")

    #C0322
    ChrTalk(
        0xF,
        "……慢着，特别任务支援科。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xF,
        (
            "克洛斯贝尔空港\x01",
            "正在进行临时设备检查，\x01",
            "禁止入内。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#0005F（临时设备检查……？\x01",
            "  有点古怪啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8B8F")

    label("loc_8B4D")


    #C0325
    ChrTalk(
        0xF,
        (
            "……慢着，特别任务支援科。\x01",
            "克洛斯贝尔空港\x01",
            "现在是禁止入内的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B8F")

    OP_93(0xF, 0x10E, 0x1F4)
    OP_4C(0xF, 0xFF)
    Jump("loc_8BD4")

    label("loc_8B9F")


    #C0326
    ChrTalk(
        0x101,
        (
            "#0000F这边是克洛斯贝尔空港。\x01",
            "……没什么事要去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BD4")

    Sleep(50)
    SetChrPos(0x0, 11250, 0, -17610, 270)
    EventEnd(0x4)
    Return()

    # Function_65_88F7 end

    def Function_66_8BEB(): pass

    label("Function_66_8BEB")

    EventBegin(0x1)
    OP_4B(0x29, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_63(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8C24():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8C24)

    def lambda_8C31():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8C31)

    #C0327
    ChrTalk(
        0x29,
        "达德利长官……\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xF,
        "达德利搜查官，您辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xF,
        (
            "……话说回来，您怎么会和\x01",
            "特别任务支援科在一起……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x10A,
        (
            "#0603F详情稍后再说明……\x02\x03",

            "#0600F对了，你们这边的情况如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x29,
        (
            "嗯，看样子，果然是假情报……\x01",
            "现在刚刚收工。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x10A,
        (
            "#0608F……是吗。\x02\x03",

            "#0600F我很快就会与你们会合的，\x01",
            "在此之前，一科内的事务就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xF,
        "是！\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x29,
        "是！\x02",
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

    # Function_66_8BEB end

    def Function_67_8DB7(): pass

    label("Function_67_8DB7")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E62")

    #C0335
    ChrTalk(
        0x101,
        (
            "#0003F（如此说来，我们的手上还有人偶工房\x01",
            "  交付的箱子呢……）\x02\x03",

            "#0000F（那好像是很昂贵的东西，\x01",
            "  还是先拿去交给伊梅尔达夫人吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F25")

    label("loc_8E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8ED6")

    #C0336
    ChrTalk(
        0x101,
        (
            "#0000F难得有机会，还是坐巴士吧。\x02\x03",

            "去那边的巴士站看看，\x01",
            "应该就能查到下一班巴士的发车时间了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F25")

    label("loc_8ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F25")

    #C0337
    ChrTalk(
        0x101,
        (
            "#0003F可不能带着琪雅\x01",
            "在市外走啊。\x02\x03",

            "#0000F这次还是坐巴士吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F25")

    SetChrPos(0x0, 0, 0, -46000, 0)
    EventEnd(0x4)
    Return()

    # Function_67_8DB7 end

    def Function_68_8F39(): pass

    label("Function_68_8F39")

    TalkBegin(0xFF)

    #C0338
    ChrTalk(
        0x101,
        (
            "#0005F如此说来……\x01",
            "我们的手上还有人偶工房\x01",
            "交付的箱子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#0100F里面的人偶是很昂贵的作品，\x01",
            "在去医院之前，\x01",
            "还是先拿去交给伊梅尔达夫人吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_68_8F39 end

    def Function_69_8FD2(): pass

    label("Function_69_8FD2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北·克洛斯贝尔市\x01",
            "东·克洛斯贝尔空港\x01",
            "南·圣乌尔拉斯医科大学  １５３赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_69_8FD2 end

    SaveToFile()

Try(main)
