from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r0040.bin",                # FileName
        "r0040",                    # MapName
        "r0040",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0040", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x04,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 4, 0, 5],
    )

    BuildStringList((
        "r0040",                  # 0
        "列车",                   # 1
        "紫色布丁花",             # 2
        "紫色布丁花",             # 3
        "凶暴角牛",               # 4
        "凶暴角牛",               # 5
        "黄金雕像",               # 6
        "幻兽",                   # 7
        "共和国飞艇",             # 8
        "共和国飞艇",             # 9
        "共和国战车",             # 10
        "共和国战车",             # 11
        "共和国战车",             # 12
        "共和国战车",             # 13
        "共和国战车",             # 14
        "神机２",                 # 15
        "共和国战车",             # 16
        "共和国战车",             # 17
        "共和国战车",             # 18
        "共和国战车",             # 19
        "共和国战车",             # 20
        "SE控制",                 # 21
        "br0000",                 # 22
        "br0000",                 # 23
        "br0000",                 # 24
        "br0000",                 # 25
        "br0000",                 # 26
        "br0000",                 # 27
        "br0000",                 # 28
        "br0000",                 # 29
        "br0000",                 # 30
        "br0000",                 # 31
        "克洛斯贝尔市·阿尔摩利卡村方向",# 32
        "唐古拉姆门方向",         # 33
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_B4", 0,   8,   5,   0,   6,   4,   0)
    Sepith("Sepith_C4", 5,   10,  0,   2,   0,   5,   2)
    Sepith("Sepith_D4", 3,   4,   11,  0,   3,   4,   0)
    Sepith("Sepith_E4", 2,   7,   0,   5,   4,   2,   2)
    Sepith("Sepith_F4", 27,  27,  27,  27,  27,  27,  27)
    Sepith("Sepith_104", 7,   9,   15,  5,   6,   3,   5)

    MonsterBattlePostion("MonsterBattlePostion_114", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_138", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_13C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_140", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_144", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_148", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_14C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_154", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_174", 5, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_178", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_17C", 2, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 14, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_184", 5, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_188", 11, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_18C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_190", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_194", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_198", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_19C", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_1A0", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_1A4", 14, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_1A8", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_1AC", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_1B0", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_1B4", 0x0000, 59, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms66700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms66700.dat", "ms66700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms66700.dat", "ms69300.dat", "ms66700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms66700.dat", "ms66700.dat", "ms69300.dat", "ms69300.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_27C", 0x0000, 59, 6, 45, 6, 1, 15, 0, "br0000", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms69300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69300.dat", "ms69300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69300.dat", "ms66700.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69300.dat", "ms69300.dat", "ms66700.dat", "ms66700.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_344", 0x0000, 60, 6, 45, 6, 1, 50, 0, "br0000", "Sepith_D4", 30, 45, 25, 0,
        (
            ("ms64000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms64000.dat", "ms64000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms64000.dat", "ms64000.dat", "ms64000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3E0", 0x0000, 59, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_E4", 30, 45, 25, 0,
        (
            ("ms69900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69900.dat", "ms69900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69900.dat", "ms63000.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_47C", 0x0000, 59, 6, 90, 8, 1, 50, 0, "br0000", "Sepith_F4", 30, 45, 25, 0,
        (
            ("ms66400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms66400.dat", "ms66400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms66400.dat", "ms66400.dat", "ms66400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_518", 0x0000, 77, 6, 45, 6, 1, 40, 0, "br0000", "Sepith_104", 40, 35, 25, 0,
        (
            ("ms63701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_5B4", 0x0000, 100, 6, 0, 0, 1, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms74201.dat", "ms74201.dat", "ms74201.dat", "ms74201.dat", "ms74201.dat", "ms74201.dat", 0, 0, "MonsterBattlePostion_174", "MonsterBattlePostion_134", "ed7451", "ed7453", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5F8", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66700.dat", "ms66700.dat", "ms66700.dat", "ms66700.dat", "ms66700.dat", "ms66700.dat", "ms66700.dat", "ms66700.dat", "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7453", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_63C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7453", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_680", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88702.dat", "ms88802.dat", "ms88802.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_194", "MonsterBattlePostion_194", "ed7454", "ed7453", "ATBonus_A4"),
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
        "monster/ch64050.itc",               # 10
        "monster/ch64051.itc",               # 11
        "monster/ch69950.itc",               # 12
        "monster/ch69950.itc",               # 13
        "monster/ch66750.itc",               # 14
        "monster/ch66750.itc",               # 15
        "monster/ch69350.itc",               # 16
        "monster/ch69351.itc",               # 17
        "monster/ch63750.itc",               # 18
        "monster/ch63751.itc",               # 19
        "monster/ch66450.itc",               # 1A
        "monster/ch66450.itc",               # 1B
        "monster/ch74250.itc",               # 1C
        "monster/ch74250.itc",               # 1D
    ))

    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(121879,  -9000,   -38750,  270,  484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(72540,   -6000,   -54830,  270,  484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(121879,  -9000,   -38750,  270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(72540,   -6000,   -54830,  270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(9739,    500,     -15649,  180,  484,  0x0, 0,   28,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(400,     4090,    0,       0x1010000,    "BattleInfo_1B4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(16300,   6830,    0,       0x1010000,    "BattleInfo_1B4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(8240,    -13730,  0,       0x1010000,    "BattleInfo_27C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(71150,   -40180,  -6000,   0x1010000,    "BattleInfo_344", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(54700,   -53920,  -6000,   0x1010000,    "BattleInfo_3E0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(84390,   -70870,  -8000,   0x1010000,    "BattleInfo_47C", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(96330,   -71440,  -9250,   0x1010000,    "BattleInfo_3E0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(145270,  -47320,  -8170,   0x1010000,    "BattleInfo_27C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(97510,   -84120,  -12510,  0x1010000,    "BattleInfo_1B4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(131430,  -41690,  -9000,   0x1010000,    "BattleInfo_344", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(10940,   -4140,   0,       0x1010000,    "BattleInfo_518", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(42050,   -25350,  -2710,   0x1010000,    "BattleInfo_518", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(127590,  -64060,  -8000,   0x1010000,    "BattleInfo_518", 0,   24,  0xFFFF, 8,  9)

    DeclEvent(0x0040, 0, 12,  121.26000213623047,    -38.47999954223633,    -10.0,                 16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -15.157500267028809,   4.809999942779541,     2.5,                   1.0])

    DeclActor(9740,    0,       -15650,  1200,    9740,    1000,    -15650,  0x007C, 0,  6,  0x0000)
    DeclActor(141800,  -9000,   -38920,  1200,    141800,  -8000,   -38920,  0x007C, 0,  7,  0x0000)
    DeclActor(121880,  -9000,   -38750,  1200,    121880,  -9000,   -38750,  0x007C, 0,  8,  0x0000)
    DeclActor(72540,   -6000,   -54830,  1200,    72540,   -6000,   -54830,  0x007C, 0,  9,  0x0000)

    PlaceName(-30.0, 0.0, 5.0, 0x0000, 0x0000, "克洛斯贝尔市·阿尔摩利卡村方向")
    PlaceName(182.0, 0.0, -64.0, 0x0000, 0x0000, "唐古拉姆门方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 1])                         # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 9
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_D8C",          # 00, 0
        "Function_1_DAB",          # 01, 1
        "Function_2_DCA",          # 02, 2
        "Function_3_DE2",          # 03, 3
        "Function_4_E69",          # 04, 4
        "Function_5_E90",          # 05, 5
        "Function_6_16E0",         # 06, 6
        "Function_7_196F",         # 07, 7
        "Function_8_1AAA",         # 08, 8
        "Function_9_1DCE",         # 09, 9
        "Function_10_20F2",        # 0A, 10
        "Function_11_2126",        # 0B, 11
        "Function_12_212A",        # 0C, 12
        "Function_13_21A6",        # 0D, 13
        "Function_14_22BE",        # 0E, 14
        "Function_15_3026",        # 0F, 15
        "Function_16_3049",        # 10, 16
        "Function_17_306F",        # 11, 17
        "Function_18_3095",        # 12, 18
        "Function_19_30BB",        # 13, 19
        "Function_20_30E1",        # 14, 20
        "Function_21_30F5",        # 15, 21
        "Function_22_3109",        # 16, 22
        "Function_23_31A2",        # 17, 23
        "Function_24_324A",        # 18, 24
        "Function_25_3306",        # 19, 25
        "Function_26_3389",        # 1A, 26
        "Function_27_3417",        # 1B, 27
        "Function_28_34A8",        # 1C, 28
        "Function_29_3539",        # 1D, 29
        "Function_30_35BE",        # 1E, 30
        "Function_31_362A",        # 1F, 31
        "Function_32_3653",        # 20, 32
        "Function_33_367E",        # 21, 33
        "Function_34_36DD",        # 22, 34
        "Function_35_3736",        # 23, 35
        "Function_36_378F",        # 24, 36
        "Function_37_37E8",        # 25, 37
        "Function_38_3841",        # 26, 38
        "Function_39_3952",        # 27, 39
        "Function_40_3A5D",        # 28, 40
        "Function_41_3B68",        # 29, 41
        "Function_42_3C73",        # 2A, 42
        "Function_43_3D84",        # 2B, 43
        "Function_44_3DF7",        # 2C, 44
        "Function_45_3E78",        # 2D, 45
        "Function_46_3E91",        # 2E, 46
    ))


    def Function_0_D8C(): pass

    label("Function_0_D8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DAA")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_D8C")

    label("loc_DAA")

    Return()

    # Function_0_D8C end

    def Function_1_DAB(): pass

    label("Function_1_DAB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DC9")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_DAB")

    label("loc_DC9")

    Return()

    # Function_1_DAB end

    def Function_2_DCA(): pass

    label("Function_2_DCA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DE1")
    OP_A1(0xFE, 0x5DC, 0x1, 0x0)
    Jump("Function_2_DCA")

    label("loc_DE1")

    Return()

    # Function_2_DCA end

    def Function_3_DE2(): pass

    label("Function_3_DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_DFC")
    SetMapObjFlags(0x2, 0x2000000)
    SetMapObjFlags(0x5, 0x2000000)
    Jump("loc_E68")

    label("loc_DFC")

    SetMapObjFlags(0x6, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)

    label("loc_E68")

    Return()

    # Function_3_DE2 end

    def Function_4_E69(): pass

    label("Function_4_E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E7D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 14)
    Jump("loc_E8C")

    label("loc_E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E8C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)

    label("loc_E8C")

    Call(0, 10)
    Return()

    # Function_4_E69 end

    def Function_5_E90(): pass

    label("Function_5_E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_EA2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB5")
    OP_1B(0x1, 0x0, 0x2E)

    label("loc_EB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EDC")
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x5, 0x4)
    Jump("loc_F45")

    label("loc_EDC")

    OP_78(0x5, 0xE)
    ClearMapObjFlags(0x5, 0x4)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x1)
    SetChrPos(0xE, 121260, -9000, -38480, 0)
    OP_93(0xE, 0x0, 0x0)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, 121260, -9000, -38480, 3000, 3000, 90000)

    label("loc_F45")

    OP_52(0x27, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1475")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xF, 0x82, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1521")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xF, 0x82, 0x0)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    ClearMapObjFlags(0x1E, 0x4)
    ClearMapObjFlags(0x1F, 0x4)
    ClearMapObjFlags(0x20, 0x4)
    ClearMapObjFlags(0x21, 0x4)
    ClearMapObjFlags(0x22, 0x4)
    ClearMapObjFlags(0x23, 0x4)
    ClearMapObjFlags(0x24, 0x4)
    ClearMapObjFlags(0x25, 0x4)
    ClearMapObjFlags(0x26, 0x4)
    ClearMapObjFlags(0x27, 0x4)
    ClearMapObjFlags(0x28, 0x4)
    ClearMapObjFlags(0x29, 0x4)
    ClearMapObjFlags(0x2A, 0x4)
    Jump("loc_1593")

    label("loc_1521")

    SetMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x20, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetMapObjFlags(0x22, 0x4)
    SetMapObjFlags(0x23, 0x4)
    SetMapObjFlags(0x24, 0x4)
    SetMapObjFlags(0x25, 0x4)
    SetMapObjFlags(0x26, 0x4)
    SetMapObjFlags(0x27, 0x4)
    SetMapObjFlags(0x28, 0x4)
    SetMapObjFlags(0x29, 0x4)
    SetMapObjFlags(0x2A, 0x4)

    label("loc_1593")

    SetMapObjFlags(0x2, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15B8")
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_15E3")

    label("loc_15B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15D7")
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_15E3")

    label("loc_15D7")

    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)

    label("loc_15E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F6")
    OP_70(0x0, 0x0)
    Jump("loc_15FA")

    label("loc_15F6")

    OP_70(0x0, 0x1E)

    label("loc_15FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160D")
    OP_70(0x1, 0x0)
    Jump("loc_1611")

    label("loc_160D")

    OP_70(0x1, 0x1E)

    label("loc_1611")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1672")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 121880, -9000, -38750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_1672")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16BE")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 72540, -6000, -54830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_16BE")

    OP_1C(0x0, 0x2B, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x2C, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x2D, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    Return()

    # Function_5_E90 end

    def Function_6_16E0(): pass

    label("Function_6_16E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1771")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从宝箱中感觉到了强大魔兽的气息。\x01",
            "【推测魔兽等级１００】\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1771")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_1771")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1931")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186E")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_17CE():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_17CE)

    def lambda_17E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_17E8)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    #A0002
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
    Battle("BattleInfo_5B4", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_184F"),
        (2, "loc_185E"),
        (1, "loc_186B"),
        (SWITCH_DEFAULT, "loc_186E"),
    )


    label("loc_184F")

    SetScenarioFlags(0x214, 0)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_186E")

    label("loc_185E")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_186B")

    OP_B9(0x0)
    Return()

    label("loc_186E")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('天王铃', 1)"), scpexpr(EXPR_END)), "loc_18C5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '天王铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E9, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_192C")

    label("loc_18C5")

    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '天王铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '天王铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_192C")

    Jump("loc_1963")

    label("loc_1931")

    FadeToDark(300, 0, 100)

    #A0005
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

    label("loc_1963")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_16E0 end

    def Function_7_196F(): pass

    label("Function_7_196F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A61")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('银胸针', 1)"), scpexpr(EXPR_END)), "loc_19F2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '银胸针'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E9, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1A5C")

    label("loc_19F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '银胸针'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '银胸针'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A5C")

    Jump("loc_1A9E")

    label("loc_1A61")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
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

    label("loc_1A9E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_196F end

    def Function_8_1AAA(): pass

    label("Function_8_1AAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C43")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_1C29")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C24")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_1C21")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1B4C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1B4C)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_5F8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1C")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C03")
    Call(1, 5)
    Jump("loc_1C1C")

    label("loc_1C03")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C19")
    Call(1, 4)
    Jump("loc_1C1C")

    label("loc_1C19")

    Call(1, 3)

    label("loc_1C1C")

    Jump("loc_1C24")

    label("loc_1C21")

    Call(1, 1)

    label("loc_1C24")

    Jump("loc_1C3F")

    label("loc_1C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_1C3F")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1C3F")

    TalkEnd(0xFF)
    Return()

    label("loc_1C43")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_1DB4")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DAF")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_1DAC")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1CD7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1CD7)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_63C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA7")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D8E")
    Call(1, 5)
    Jump("loc_1DA7")

    label("loc_1D8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1DA4")
    Call(1, 4)
    Jump("loc_1DA7")

    label("loc_1DA4")

    Call(1, 3)

    label("loc_1DA7")

    Jump("loc_1DAF")

    label("loc_1DAC")

    Call(1, 1)

    label("loc_1DAF")

    Jump("loc_1DCA")

    label("loc_1DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_1DCA")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1DCA")

    TalkEnd(0xFF)
    Return()

    # Function_8_1AAA end

    def Function_9_1DCE(): pass

    label("Function_9_1DCE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F67")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_1F4D")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F48")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_1F45")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1E70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1E70)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_5F8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F40")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F27")
    Call(1, 5)
    Jump("loc_1F40")

    label("loc_1F27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F3D")
    Call(1, 4)
    Jump("loc_1F40")

    label("loc_1F3D")

    Call(1, 3)

    label("loc_1F40")

    Jump("loc_1F48")

    label("loc_1F45")

    Call(1, 1)

    label("loc_1F48")

    Jump("loc_1F63")

    label("loc_1F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_1F63")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1F63")

    TalkEnd(0xFF)
    Return()

    label("loc_1F67")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_20D8")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D3")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_20D0")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1FFB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1FFB)
    TurnDirection(0xC, 0x0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    PlayEffect(0x7, 0x1, 0xC, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_63C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20CB")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20B2")
    Call(1, 5)
    Jump("loc_20CB")

    label("loc_20B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20C8")
    Call(1, 4)
    Jump("loc_20CB")

    label("loc_20C8")

    Call(1, 3)

    label("loc_20CB")

    Jump("loc_20D3")

    label("loc_20D0")

    Call(1, 1)

    label("loc_20D3")

    Jump("loc_20EE")

    label("loc_20D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_20EE")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_20EE")

    TalkEnd(0xFF)
    Return()

    # Function_9_1DCE end

    def Function_10_20F2(): pass

    label("Function_10_20F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_210F")
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)

    label("loc_210F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 0)), scpexpr(EXPR_END)), "loc_2120")
    ClearScenarioFlags(0x3C, 0)
    Jump("loc_2125")

    label("loc_2120")

    SetChrFlags(0x22, 0x80)

    label("loc_2125")

    Return()

    # Function_10_20F2 end

    def Function_11_2126(): pass

    label("Function_11_2126")

    Call(1, 6)
    Return()

    # Function_11_2126 end

    def Function_12_212A(): pass

    label("Function_12_212A")

    Battle("BattleInfo_680", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2171")
    OP_90(0x0, 124600, -9000, -44230, 180)
    EventEnd(0x5)
    SetChrFlags(0xE, 0x8000)
    Jump("loc_21A5")

    label("loc_2171")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2184")
    Jump("loc_21A5")

    label("loc_2184")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x5, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 2)
    EventEnd(0x5)

    label("loc_21A5")

    Return()

    # Function_12_212A end

    def Function_13_21A6(): pass

    label("Function_13_21A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    SetChrPos(0x101, 93000, -13000, -132000, 0)
    SetChrPos(0x109, 93000, -13000, -132000, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xEB, 0x93, 0x6F, 0x28, 0x96, 0x0)
    OP_78(0x2, 0x8)
    OP_49()
    SetChrPos(0x8, 130000, -7150, -108000, 0)
    OP_D5(0x8, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    OP_68(85000, -5150, -100000, 0)
    MoveCamera(15, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    MoveCamera(20, 25, 0, 5000)
    SetCameraDistance(37500, 5000)
    OP_82(0x64, 0x0, 0xBB8, 0x1B58)

    def lambda_227C():
        OP_96(0xFE, 0x0, 0xFFFFE412, 0xFFFE5A20, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_227C)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(456, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_21A6 end

    def Function_14_22BE(): pass

    label("Function_14_22BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadEffect(0x0, "event/ev15060.eff")
    LoadEffect(0x1, "event/ev15058.eff")
    LoadEffect(0x2, "event/ev14002.eff")
    LoadEffect(0x3, "event/ev15102.eff")
    LoadEffect(0x4, "event/ev15056.eff")
    LoadEffect(0x5, "event/ev15057.eff")
    LoadEffect(0x6, "event/ev15059.eff")
    LoadEffect(0x7, "event/ev17022.eff")
    LoadEffect(0x9, "event/eva03_01.eff")
    OP_F3(200000)
    SoundLoad(980)
    SoundLoad(924)
    SoundLoad(868)
    SoundLoad(825)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 0, -17900, 0, 0)
    OP_74(0x6, 0x1E)
    OP_78(0x6, 0x16)
    OP_93(0x16, 0xB4, 0x0)
    SetChrFlags(0x16, 0x1)
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_70(0x6, 0xDD)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 0, 0, 0, 0)
    OP_78(0x7, 0xF)
    OP_93(0xF, 0x0, 0x0)
    SetMapObjFrame(0x7, "slash", 0x0, 0x1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 0, 0)
    OP_78(0x8, 0x10)
    OP_93(0x10, 0x0, 0x0)
    SetMapObjFrame(0x8, "slash", 0x0, 0x1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, 0, 0, 0)
    OP_74(0x9, 0x1E)
    OP_78(0x9, 0x11)
    OP_93(0x11, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, 0, 0, 0)
    OP_74(0xA, 0x1E)
    OP_78(0xA, 0x12)
    OP_93(0x12, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 0, 0, 0, 0)
    OP_74(0xB, 0x1E)
    OP_78(0xB, 0x13)
    OP_93(0x13, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 0, 0, 0, 0)
    OP_74(0xC, 0x1E)
    OP_78(0xC, 0x14)
    OP_93(0x14, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 0, 0, 0, 0)
    OP_74(0xD, 0x1E)
    OP_78(0xD, 0x15)
    OP_93(0x15, 0x0, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 0, 0, 0, 0)
    OP_74(0xE, 0x1E)
    OP_78(0xE, 0x17)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 0, 0, 0, 0)
    OP_74(0xF, 0x1E)
    OP_78(0xF, 0x18)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 0, 0, 0, 0)
    OP_74(0x10, 0x1E)
    OP_78(0x10, 0x19)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 0, 0, 0, 0)
    OP_74(0x11, 0x1E)
    OP_78(0x11, 0x1A)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 0, 0, 0, 0)
    OP_74(0x12, 0x1E)
    OP_78(0x12, 0x1B)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2B, 0x4)
    SetMapObjFlags(0x2C, 0x4)
    SetMapObjFlags(0x2D, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetChrPos(0x16, 30000, 0, -11000, 0)
    SetChrPos(0xF, 66000, 5000, -53290, 0)
    SetChrPos(0x10, 100540, 5110, -3110, 0)
    SetChrPos(0x11, 75650, -7600, -47820, 0)
    SetChrPos(0x12, 89200, -7950, -54850, 0)
    SetChrPos(0x13, 102800, -7950, -61940, 0)
    SetChrPos(0x14, 117510, -7950, -67760, 0)
    SetChrPos(0x15, 133180, -7950, -62840, 0)
    OP_93(0x16, 0x5A, 0x0)
    OP_93(0xF, 0x13B, 0x0)
    OP_93(0x10, 0x10E, 0x0)
    OP_93(0x11, 0x113, 0x0)
    OP_93(0x12, 0x131, 0x0)
    OP_93(0x13, 0x13B, 0x0)
    OP_93(0x14, 0x145, 0x0)
    OP_93(0x15, 0x116, 0x0)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0xB, 0x1000)
    ClearMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xD, 0x1000)
    OP_68(55930, -6200, -21570, 0)
    MoveCamera(51, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(79580, 0)
    OP_11(0xAB, 0xE3, 0xEB, 0x32, 0x15E, 0x0)
    OP_D5(0xF, 0x4E20, 0x4CE78, 0x0, 0x0)
    OP_D5(0x10, 0x4E20, 0x41EB0, 0x0, 0x0)
    OP_D5(0x11, 0x55F00, 0x43238, 0x0, 0x0)
    OP_93(0x11, 0x13B, 0x0)
    OP_93(0x12, 0x131, 0x0)
    OP_93(0x13, 0x127, 0x0)
    OP_93(0x14, 0x113, 0x0)
    OP_93(0x15, 0x101, 0x0)
    Sound(924, 2, 40, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0x1C, 1, 0, 44)
    FadeToBright(1000, 0)
    BeginChrThread(0xF, 0, 0, 22)
    BeginChrThread(0x10, 0, 0, 23)
    BeginChrThread(0xF, 1, 0, 20)
    BeginChrThread(0x10, 1, 0, 21)
    BeginChrThread(0x11, 0, 0, 24)
    BeginChrThread(0x12, 0, 0, 25)
    OP_68(66630, -6200, -31450, 6000)
    MoveCamera(23, 17, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(79580, 6000)
    OP_0D()
    Sleep(300)
    BlurSwitch(0x1F4, 0x77FFFFFF, 0x0, 0x1, 0xA)
    Sleep(700)
    Sound(990, 0, 100, 0)
    OP_25(0x39C, 0x32)
    CancelBlur(1000)
    Sleep(4000)
    WaitChrThread(0xF, 0)
    WaitChrThread(0x10, 0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    BeginChrThread(0x13, 0, 0, 26)
    BeginChrThread(0x14, 0, 0, 27)
    BeginChrThread(0x15, 0, 0, 28)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0xA, 0x1000)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFlags(0xD, 0x1000)
    OP_68(107050, -6200, -59960, 5000)
    MoveCamera(36, 14, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(47650, 5000)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    StopSound(924, 1000, 50)
    OP_6F(0x79)
    Sleep(200)
    SetChrPos(0x16, 85000, 0, 5000, 0)
    OP_93(0x16, 0x7D, 0x0)
    PlayEffect(0x9, 0x7, 0x16, 0x5, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0xB, 0x1000)
    ClearMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xD, 0x1000)
    OP_70(0x6, 0xDD)
    OP_68(97070, -17200, -39540, 0)
    MoveCamera(90, 29, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(122990, 0)
    OP_11(0xAB, 0xE3, 0xEB, 0x4B, 0x12C, 0x0)
    Fade(500)
    BeginChrThread(0x16, 0, 0, 29)
    BeginChrThread(0x1C, 1, 0, 45)
    OP_68(93660, -17300, -42640, 3000)
    MoveCamera(108, 28, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(110380, 3000)
    OP_0D()
    BlurSwitch(0x1F4, 0x55FFFFFF, 0x0, 0x1, 0xA)
    OP_6F(0x79)
    StopEffect(0x7, 0x0)
    OP_70(0x6, 0xDD)
    SetMapObjFrame(0x9, "head", 0x0, 0x1)
    OP_FD(0x17, 0x11)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFrame(0xA, "head", 0x0, 0x1)
    OP_FD(0x18, 0x12)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFrame(0xB, "head", 0x0, 0x1)
    OP_FD(0x19, 0x13)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFrame(0xC, "head", 0x0, 0x1)
    OP_FD(0x1A, 0x14)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0xD, "head", 0x0, 0x1)
    OP_FD(0x1B, 0x15)
    ClearMapObjFlags(0x12, 0x4)
    SetChrPos(0x16, 13000, 15000, -2000, 0)
    OP_68(105580, -15600, -54960, 0)
    MoveCamera(104, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(67420, 0)
    OP_11(0xAB, 0xE3, 0xEB, 0x32, 0x15E, 0x0)
    CancelBlur(0)
    Fade(500)
    SetCameraDistance(64420, 2500)
    OP_0D()
    Sound(147, 0, 100, 0)
    BeginChrThread(0x17, 1, 0, 15)
    BeginChrThread(0x18, 1, 0, 16)
    BeginChrThread(0x19, 1, 0, 17)
    BeginChrThread(0x1A, 1, 0, 18)
    BeginChrThread(0x1B, 1, 0, 19)
    Sleep(600)
    Sleep(900)
    OP_68(113500, -16300, -47500, 0)
    MoveCamera(88, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(73500, 0)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x18, 0x2)
    EndChrThread(0x19, 0x2)
    EndChrThread(0x1A, 0x2)
    EndChrThread(0x1B, 0x2)
    TurnDirection(0x17, 0x16, 0)
    TurnDirection(0x18, 0x16, 0)
    TurnDirection(0x19, 0x16, 0)
    TurnDirection(0x1A, 0x16, 0)
    TurnDirection(0x1B, 0x16, 0)
    Fade(500)
    BeginChrThread(0x17, 3, 0, 33)
    BeginChrThread(0x18, 3, 0, 34)
    BeginChrThread(0x19, 3, 0, 35)
    BeginChrThread(0x1A, 3, 0, 36)
    BeginChrThread(0x1B, 3, 0, 37)
    OP_0D()
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    Sleep(2500)
    OP_6F(0x79)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    SetChrPos(0x16, 13000, 15000, -2000, 0)
    SetChrFlags(0x16, 0x8000)
    PlayEffect(0x9, 0x6, 0x16, 0x5, 0, 0, 0, 180, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0x7, 0x16, 0x5, 0, 0, 0, 180, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Fade(500)
    OP_68(90640, -18500, -16970, 0)
    MoveCamera(99, 26, 9, 0)
    OP_6E(510, 0)
    SetCameraDistance(115750, 0)
    OP_25(0x3EB, 0x32)
    Sound(980, 2, 70, 0)
    BeginChrThread(0x16, 0, 0, 30)
    OP_68(90630, -16800, -16960, 4000)
    MoveCamera(319, 16, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(102650, 4000)
    OP_0D()
    Sleep(700)
    CancelBlur(700)
    Sleep(2300)
    StopEffect(0x6, 0x2)
    StopEffect(0x7, 0x2)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_6F(0x79)
    WaitChrThread(0x16, 0)
    StopSound(1003, 1000, 40)
    EndChrThread(0x17, 0x3)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1B, 0x3)
    Fade(500)
    OP_68(89470, -14000, -55880, 0)
    MoveCamera(282, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(80220, 0)
    BeginChrThread(0x16, 0, 0, 31)
    BeginChrThread(0x16, 1, 0, 32)
    OP_68(89470, -15000, -55880, 3300)
    MoveCamera(283, 15, 0, 3300)
    OP_6E(510, 3300)
    SetCameraDistance(72940, 3300)
    OP_0D()
    CancelBlur(0)
    Sleep(1500)
    WaitChrThread(0x16, 0)
    WaitChrThread(0x16, 1)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x18, 0x2)
    EndChrThread(0x19, 0x2)
    EndChrThread(0x1A, 0x2)
    EndChrThread(0x1B, 0x2)
    Sleep(500)
    BlurSwitch(0x1F4, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_87(0x4, 0x1, 0x6, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(500)
    Sound(1036, 0, 100, 0)
    Sleep(1000)
    CancelBlur(0)
    Fade(500)
    OP_68(98760, -12900, -52050, 0)
    MoveCamera(299, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(57360, 0)
    Sleep(700)
    BeginChrThread(0x16, 3, 0, 43)
    OP_0D()
    OP_68(63220, -12900, -36880, 4500)
    MoveCamera(327, 24, 0, 4500)
    OP_6E(510, 4500)
    SetCameraDistance(57360, 4500)
    OP_6F(0x79)
    WaitChrThread(0x16, 3)
    OP_68(83000, -4000, -54640, 0)
    MoveCamera(76, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(58360, 0)
    OP_11(0xAB, 0xE3, 0xEB, 0x4B, 0x12C, 0x0)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    Fade(500)
    StopSound(980, 4000, 60)
    OP_68(85560, -4000, -53730, 5000)
    MoveCamera(76, 21, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(81710, 5000)
    OP_0D()
    OP_6F(0x79)
    StopSound(868, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e4210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_22BE end

    def Function_15_3026(): pass

    label("Function_15_3026")


    def lambda_302B():
        TurnDirection(0xFE, 0x16, 13)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0xFE, 2, lambda_302B)
    OP_74(0xE, 0xF)
    OP_71(0xE, 0x0, 0x1E, 0x0, 0x0)
    Return()

    # Function_15_3026 end

    def Function_16_3049(): pass

    label("Function_16_3049")

    Sleep(150)

    def lambda_3051():
        TurnDirection(0xFE, 0x16, 13)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0xFE, 2, lambda_3051)
    OP_74(0xF, 0xF)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Return()

    # Function_16_3049 end

    def Function_17_306F(): pass

    label("Function_17_306F")

    Sleep(300)

    def lambda_3077():
        TurnDirection(0xFE, 0x16, 13)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0xFE, 2, lambda_3077)
    OP_74(0x10, 0xF)
    OP_71(0x10, 0x0, 0x1E, 0x0, 0x0)
    Return()

    # Function_17_306F end

    def Function_18_3095(): pass

    label("Function_18_3095")

    Sleep(300)

    def lambda_309D():
        TurnDirection(0xFE, 0x16, 13)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0xFE, 2, lambda_309D)
    OP_74(0x11, 0xF)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Return()

    # Function_18_3095 end

    def Function_19_30BB(): pass

    label("Function_19_30BB")

    Sleep(300)

    def lambda_30C3():
        TurnDirection(0xFE, 0x16, 13)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0xFE, 2, lambda_30C3)
    OP_74(0x12, 0xF)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Return()

    # Function_19_30BB end

    def Function_20_30E1(): pass

    label("Function_20_30E1")

    Sleep(500)
    OP_74(0x7, 0x4)
    OP_71(0x7, 0x0, 0x3C, 0x0, 0x0)
    Return()

    # Function_20_30E1 end

    def Function_21_30F5(): pass

    label("Function_21_30F5")

    Sleep(2000)
    OP_74(0x8, 0x4)
    OP_71(0x8, 0x0, 0x3C, 0x0, 0x0)
    Return()

    # Function_21_30F5 end

    def Function_22_3109(): pass

    label("Function_22_3109")

    SetChrPos(0xFE, 85090, 10000, -62290, 0)
    OP_87(0x1, 0x0, 0x7, "body", 0x7, 0x1770, 0x0, 0xFFFFE890, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 61090, 2000, -56290)
    OP_9F(0x1, 45000, -6000, -51000)
    OP_9F(0x1, 22000, -12000, -46000)
    OP_9F(0x2, 0xFE, 22000, 0x0)
    OP_82(0x12C, 0x12C, 0x1770, 0x3E8)
    Sound(200, 0, 100, 0)
    Sleep(500)
    Sound(833, 0, 100, 0)
    StopEffect(0x0, 0x2)
    Return()

    # Function_22_3109 end

    def Function_23_31A2(): pass

    label("Function_23_31A2")

    Sleep(700)
    SetChrPos(0xFE, 100540, 5110, -3110, 0)
    OP_87(0x1, 0x1, 0x8, "body", 0x7, 0x5DC, 0x0, 0xFFFFFA24, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 90000, 1500, 11000)
    OP_9F(0x1, 80000, -4000, 25000)
    OP_9F(0x1, 75000, -9000, 30000)
    OP_9F(0x2, 0xFE, 8500, 0x0)
    OP_82(0x96, 0x96, 0x1388, 0x1F4)
    Sound(200, 0, 60, 0)
    Sleep(500)
    Sound(833, 0, 60, 0)
    StopEffect(0x1, 0x2)
    StopSound(868, 1000, 90)
    StopSound(825, 1000, 90)
    Return()

    # Function_23_31A2 end

    def Function_24_324A(): pass

    label("Function_24_324A")

    Sleep(2000)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, 87560, -7900, -53490, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 83920, -7900, -50240)
    OP_9F(0x1, 79750, -7850, -48660)
    OP_9F(0x1, 75010, -7600, -48060)
    OP_9F(0x1, 67780, -6000, -47990)
    OP_9F(0x1, 64379, -6000, -46730)
    OP_9F(0x2, 0xFE, 5500, 0x7)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x7D0, 0x1)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Return()

    # Function_24_324A end

    def Function_25_3306(): pass

    label("Function_25_3306")

    Sleep(5000)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, 89530, -8000, -56000, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 83190, -8000, -49200)
    OP_9F(0x1, 79540, -8000, -48630)
    OP_9F(0x2, 0xFE, 5000, 0x7)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x7D0, 0x1)
    OP_71(0xA, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Return()

    # Function_25_3306 end

    def Function_26_3389(): pass

    label("Function_26_3389")

    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, 104100, -8000, -62830, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 99860, -8000, -60590)
    OP_9F(0x1, 93510, -8000, -59430)
    OP_9F(0x1, 90090, -8000, -56350)
    OP_9F(0x2, 0xFE, 5000, 0x7)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x7D0, 0x1)
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Return()

    # Function_26_3389 end

    def Function_27_3417(): pass

    label("Function_27_3417")

    Sleep(1000)
    OP_71(0xC, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, 119230, -8000, -67040, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 112980, -8000, -67120)
    OP_9F(0x1, 107530, -8000, -63290)
    OP_9F(0x1, 104760, -8000, -62000)
    OP_9F(0x2, 0xFE, 5000, 0x7)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x7D0, 0x1)
    OP_71(0xC, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Return()

    # Function_27_3417 end

    def Function_28_34A8(): pass

    label("Function_28_34A8")

    Sleep(1700)
    OP_71(0xD, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, 133500, -8000, -63480, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 127380, -8000, -64920)
    OP_9F(0x1, 123580, -8000, -67240)
    OP_9F(0x1, 118600, -8000, -67640)
    OP_9F(0x2, 0xFE, 5000, 0x7)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x7D0, 0x1)
    OP_71(0xD, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Return()

    # Function_28_34A8 end

    def Function_29_3539(): pass

    label("Function_29_3539")

    OP_74(0x6, 0xF)
    OP_71(0x6, 0xF1, 0xF3, 0x0, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 85000, 10000, 5000, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 55000, 12000, -30000)
    OP_9F(0x1, 29000, 15000, -36500)
    OP_9F(0x1, 16000, 17000, -29500)
    OP_9F(0x1, 25000, 19000, -19500)
    OP_9F(0x2, 0xFE, 60000, 0x7)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 65000, 15000, -29500)
    OP_9F(0x2, 0xFE, 60000, 0x7)
    Return()

    # Function_29_3539 end

    def Function_30_35BE(): pass

    label("Function_30_35BE")

    SetChrPos(0xFE, 13000, 15000, -2000, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x7D, 0x0)
    OP_9F(0x1, 58500, -1000, -38500)
    OP_9F(0x1, 86500, -1500, -54500)
    OP_9F(0x1, 102500, -2000, -61500)
    OP_9F(0x1, 122500, -4000, -65500)
    OP_9F(0x1, 131500, -1000, -66000)
    OP_9F(0x2, 0xFE, 35000, 0x2)
    Return()

    # Function_30_35BE end

    def Function_31_362A(): pass

    label("Function_31_362A")


    def lambda_362F():
        TurnDirection(0xFE, 0x13, 300)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_362F)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 131500, -7000, -66000)
    OP_9F(0x2, 0xFE, 1800, 0x0)
    Return()

    # Function_31_362A end

    def Function_32_3653(): pass

    label("Function_32_3653")

    ClearMapObjFlags(0x6, 0x20)
    OP_79(0x6)
    Sound(982, 0, 100, 0)
    OP_74(0x6, 0xF)
    OP_71(0x6, 0x105, 0x118, 0x0, 0x0)
    OP_79(0x6)
    OP_74(0x6, 0xF)
    OP_70(0x6, 0xB)
    Return()

    # Function_32_3653 end

    def Function_33_367E(): pass

    label("Function_33_367E")

    Sleep(200)
    Sound(1003, 2, 80, 0)

    label("loc_3687")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36DC")
    OP_82(0x82, 0x82, 0xA8C, 0x1F4)
    OP_87(0x0, 0xFF, 0xE, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(820)
    Jump("loc_3687")

    label("loc_36DC")

    Return()

    # Function_33_367E end

    def Function_34_36DD(): pass

    label("Function_34_36DD")

    Sleep(350)

    label("loc_36E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3735")
    OP_82(0x64, 0x64, 0x9C4, 0x1F4)
    OP_87(0x0, 0xFF, 0xF, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(800)
    Jump("loc_36E0")

    label("loc_3735")

    Return()

    # Function_34_36DD end

    def Function_35_3736(): pass

    label("Function_35_3736")

    Sleep(500)

    label("loc_3739")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_378E")
    OP_82(0x50, 0x50, 0x8FC, 0x1F4)
    OP_87(0x0, 0xFF, 0x10, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(840)
    Jump("loc_3739")

    label("loc_378E")

    Return()

    # Function_35_3736 end

    def Function_36_378F(): pass

    label("Function_36_378F")

    Sleep(650)

    label("loc_3792")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37E7")
    OP_82(0x3C, 0x3C, 0x834, 0x1F4)
    OP_87(0x0, 0xFF, 0x11, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(830)
    Jump("loc_3792")

    label("loc_37E7")

    Return()

    # Function_36_378F end

    def Function_37_37E8(): pass

    label("Function_37_37E8")

    Sleep(800)

    label("loc_37EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3840")
    OP_82(0x28, 0x28, 0x76C, 0x1F4)
    OP_87(0x0, 0xFF, 0x12, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(860)
    Jump("loc_37EB")

    label("loc_3840")

    Return()

    # Function_37_37E8 end

    def Function_38_3841(): pass

    label("Function_38_3841")

    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    OP_78(0x17, 0xFE)
    OP_D5(0xFE, 0x0, 0x497C8, 0x0, 0x0)
    Sound(200, 0, 100, 0)
    Sound(868, 2, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 30, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    OP_87(0x3, 0xFF, 0xD, "body", 0x7, 0x0, 0x3E8, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_38_3841 end

    def Function_39_3952(): pass

    label("Function_39_3952")

    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    OP_78(0x16, 0xFE)
    OP_D5(0xFE, 0x0, 0x4EDB8, 0x0, 0x0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 30, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    OP_87(0x3, 0xFF, 0xC, "body", 0x7, 0x0, 0x3E8, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_39_3952 end

    def Function_40_3A5D(): pass

    label("Function_40_3A5D")

    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1150)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    OP_78(0x15, 0xFE)
    OP_D5(0xFE, 0x0, 0x4A768, 0x0, 0x0)
    Sound(200, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 30, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    OP_87(0x3, 0xFF, 0xB, "body", 0x7, 0x0, 0x3E8, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_40_3A5D end

    def Function_41_3B68(): pass

    label("Function_41_3B68")

    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1300)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    OP_78(0x14, 0xFE)
    OP_D5(0xFE, 0x0, 0x4A768, 0x0, 0x0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 280, 0, 90, 3, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    OP_87(0x3, 0xFF, 0xA, "body", 0x7, 0x0, 0x3E8, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_41_3B68 end

    def Function_42_3C73(): pass

    label("Function_42_3C73")

    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1450)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    OP_78(0x13, 0xFE)
    OP_D5(0xFE, 0x0, 0x4BED8, 0x0, 0x0)
    Sound(200, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(556, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 30, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    OP_87(0x3, 0xFF, 0x9, "body", 0x7, 0x0, 0x3E8, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_42_3C73 end

    def Function_43_3D84(): pass

    label("Function_43_3D84")

    SetMapObjFlags(0x13, 0x1000)
    SetMapObjFlags(0x14, 0x1000)
    SetMapObjFlags(0x15, 0x1000)
    SetMapObjFlags(0x16, 0x1000)
    SetMapObjFlags(0x17, 0x1000)
    OP_7D(0xEB, 0xEB, 0xEB, 0x0, 0xBB8)
    BeginChrThread(0x15, 3, 0, 38)
    Sleep(200)
    Sound(1014, 0, 80, 0)
    BeginChrThread(0x14, 3, 0, 39)
    Sleep(200)
    Sound(1014, 0, 80, 0)
    BeginChrThread(0x13, 3, 0, 40)
    Sleep(200)
    Sound(1014, 0, 80, 0)
    BeginChrThread(0x12, 3, 0, 41)
    Sleep(200)
    Sound(1014, 0, 80, 0)
    BeginChrThread(0x11, 3, 0, 42)
    Sleep(200)
    Sound(1014, 0, 80, 0)
    Return()

    # Function_43_3D84 end

    def Function_44_3DF7(): pass

    label("Function_44_3DF7")

    Sound(200, 0, 70, 0)
    Sound(868, 2, 0, 0)
    Sound(825, 2, 0, 0)
    Sleep(50)
    OP_25(0x364, 0xA)
    OP_25(0x339, 0xA)
    Sleep(50)
    OP_25(0x364, 0x14)
    OP_25(0x339, 0x14)
    Sleep(50)
    OP_25(0x364, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(50)
    OP_25(0x364, 0x28)
    OP_25(0x339, 0x28)
    Sleep(50)
    OP_25(0x364, 0x32)
    OP_25(0x339, 0x32)
    Sleep(50)
    OP_25(0x364, 0x3C)
    OP_25(0x339, 0x3C)
    Sleep(50)
    OP_25(0x364, 0x46)
    OP_25(0x339, 0x46)
    Sleep(50)
    OP_25(0x364, 0x50)
    OP_25(0x339, 0x50)
    Sleep(50)
    OP_25(0x364, 0x5A)
    OP_25(0x339, 0x5A)
    Sleep(50)
    OP_25(0x364, 0x64)
    OP_25(0x339, 0x64)
    Return()

    # Function_44_3DF7 end

    def Function_45_3E78(): pass

    label("Function_45_3E78")

    Sleep(800)
    Sound(499, 0, 100, 0)
    Sound(999, 0, 100, 0)
    Sleep(800)
    Sound(998, 0, 100, 0)
    Return()

    # Function_45_3E78 end

    def Function_46_3E91(): pass

    label("Function_46_3E91")

    EventBegin(0x1)
    OP_E2(0x3)

    #C0017
    ChrTalk(
        0x101,
        (
            "#00001F这边是唐古拉姆门方向……\x02\x03",

            "继续前进是很危险的，\x01",
            "还是回去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 156770, -8000, -68100, 270)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_46_3E91 end

    SaveToFile()

Try(main)
