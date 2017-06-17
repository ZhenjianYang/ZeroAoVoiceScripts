from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r2010.bin",                # FileName
        "r2010",                    # MapName
        "r2010",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2010", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x12,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 3, 0, 4],
    )

    BuildStringList((
        "r2010",                  # 0
        "『水狂』纳西斯",         # 1
        "岩石鼠",                 # 2
        "岩石鼠",                 # 3
        "钢铁土龙",               # 4
        "钢铁土龙",               # 5
        "幻兽",                   # 6
        "米蕾优三尉",             # 7
        "警备队员",               # 8
        "警备队员",               # 9
        "警备队员",               # 10
        "警备队员",               # 11
        "警备队员",               # 12
        "警备队员",               # 13
        "警备队员",               # 14
        "警备队员",               # 15
        "警备队员",               # 16
        "警备队员",               # 17
        "狼",                     # 18
        "狼",                     # 19
        "狼",                     # 20
        "狼",                     # 21
        "狼",                     # 22
        "猎兵扎克斯",             # 23
        "猎兵",                   # 24
        "猎兵",                   # 25
        "猎兵",                   # 26
        "猎兵",                   # 27
        "猎兵",                   # 28
        "猎兵",                   # 29
        "猎兵",                   # 30
        "狮兽",                   # 31
        "狮兽",                   # 32
        "狮兽",                   # 33
        "SE控制",                 # 34
        "br2000",                 # 35
        "br2000",                 # 36
        "br2000",                 # 37
        "br2000",                 # 38
        "br2000",                 # 39
        "br2000",                 # 40
        "br2000",                 # 41
        "br2000",                 # 42
        "克洛斯贝尔市方向",       # 43
        "矿山镇玛因兹方向",       # 44
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_B4", 6,   0,   0,   3,   2,   4,   0)
    Sepith("Sepith_C4", 3,   0,   1,   5,   3,   2,   0)
    Sepith("Sepith_D4", 6,   0,   8,   0,   1,   0,   6)
    Sepith("Sepith_E4", 0,   7,   2,   0,   1,   0,   4)
    Sepith("Sepith_F4", 11,  3,   6,   4,   6,   10,  8)

    MonsterBattlePostion("MonsterBattlePostion_104", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_128", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_12C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_130", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_134", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_138", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_13C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_144", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_154", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_174", 14, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_178", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_17C", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_180", 0, 0, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_184", 0x0000, 52, 6, 45, 10, 1, 30, 0, "br2000", "Sepith_B4", 40, 30, 20, 0,
        (
            ("ms62500.dat", "ms62500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            ("ms62500.dat", "ms65900.dat", "ms62500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            ("ms62500.dat", "ms62500.dat", "ms65500.dat", "ms62500.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_220", 0x0000, 52, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_C4", 40, 30, 20, 0,
        (
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2BC", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_D4", 40, 30, 20, 0,
        (
            ("ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_358", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_E4", 40, 30, 20, 0,
        (
            ("ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3F4", 0x0000, 82, 6, 45, 6, 1, 30, 0, "br2000", "Sepith_F4", 100, 30, 20, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_490", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62500.dat", "ms62500.dat", "ms62500.dat", "ms62500.dat", "ms62500.dat", "ms62500.dat", 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7453", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4D4", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7453", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_518", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88702.dat", "ms88802.dat", "ms88802.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_164", "MonsterBattlePostion_164", "ed7454", "ed7453", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch45900.itc",                   # 00
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
        "monster/ch62550.itc",               # 10
        "monster/ch62551.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch65550.itc",               # 14
        "monster/ch65551.itc",               # 15
        "monster/ch69450.itc",               # 16
        "monster/ch69450.itc",               # 17
        "monster/ch76050.itc",               # 18
        "monster/ch76051.itc",               # 19
    ))

    DeclNpc(-12130,  5380,    58639,   315,  261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-58250,  0,       33119,   270,  484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(27629,   8000,    38669,   270,  484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-58250,  0,       33119,   270,  484,  0x0, 0,   24,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(27629,   8000,    38669,   270,  484,  0x0, 0,   24,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-31720,  15370,   0,       0x1010000,    "BattleInfo_184", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-64090,  36330,   0,       0x1010000,    "BattleInfo_220", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-41420,  86260,   8000,    0x1010000,    "BattleInfo_2BC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(8029,    99200,   18000,   0x1010000,    "BattleInfo_358", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(27930,   93470,   18000,   0x1010000,    "BattleInfo_184", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(30600,   53520,   8000,    0x1010000,    "BattleInfo_220", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(17410,   30550,   8000,    0x1010000,    "BattleInfo_358", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-52720,  42390,   0,       0x1010000,    "BattleInfo_3F4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(19680,   94830,   18000,   0x1010000,    "BattleInfo_3F4", 0,   24,  0xFFFF, 8,  9)

    DeclEvent(0x0040, 0, 11,  -64.7300033569336,     40.720001220703125,    -1.25,                 16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   8.0912504196167,       -5.090000152587891,    0.3125,                1.0])

    DeclActor(-87000,  0,       35750,   1200,    -87000,  1000,    35750,   0x007C, 0,  5,  0x0000)
    DeclActor(-10830,  5380,    59860,   1200,    -13360,  380,     68320,   0x007C, 0,  12, 0x0000)
    DeclActor(-58250,  0,       33120,   1200,    -58250,  0,       33120,   0x007C, 0,  7,  0x0000)
    DeclActor(27630,   8000,    38670,   1200,    27630,   8000,    38670,   0x007C, 0,  8,  0x0000)

    PlaceName(26.0, 0.0, -28.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(61.0, 18.0, 112.0, 0x0000, 0x0000, "矿山镇玛因兹方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9

    ScpFunction((
        "Function_0_D7C",          # 00, 0
        "Function_1_E34",          # 01, 1
        "Function_2_E53",          # 02, 2
        "Function_3_E72",          # 03, 3
        "Function_4_F68",          # 04, 4
        "Function_5_16BA",         # 05, 5
        "Function_6_17F5",         # 06, 6
        "Function_7_17F9",         # 07, 7
        "Function_8_1B1D",         # 08, 8
        "Function_9_1E41",         # 09, 9
        "Function_10_1E5A",        # 0A, 10
        "Function_11_2947",        # 0B, 11
        "Function_12_29C3",        # 0C, 12
        "Function_13_2C75",        # 0D, 13
        "Function_14_383F",        # 0E, 14
        "Function_15_38EF",        # 0F, 15
        "Function_16_3923",        # 10, 16
        "Function_17_3977",        # 11, 17
        "Function_18_39CB",        # 12, 18
        "Function_19_3A95",        # 13, 19
        "Function_20_3AC7",        # 14, 20
        "Function_21_3AF9",        # 15, 21
        "Function_22_3B32",        # 16, 22
        "Function_23_3B57",        # 17, 23
        "Function_24_3BBA",        # 18, 24
        "Function_25_3C31",        # 19, 25
        "Function_26_3C70",        # 1A, 26
        "Function_27_3CE7",        # 1B, 27
        "Function_28_3D57",        # 1C, 28
        "Function_29_3DCE",        # 1D, 29
        "Function_30_3E07",        # 1E, 30
        "Function_31_3E7E",        # 1F, 31
        "Function_32_3ECB",        # 20, 32
        "Function_33_3F42",        # 21, 33
        "Function_34_3F8F",        # 22, 34
        "Function_35_4006",        # 23, 35
        "Function_36_404C",        # 24, 36
        "Function_37_40C3",        # 25, 37
        "Function_38_410F",        # 26, 38
        "Function_39_4186",        # 27, 39
        "Function_40_41E0",        # 28, 40
        "Function_41_4257",        # 29, 41
        "Function_42_42B4",        # 2A, 42
        "Function_43_432B",        # 2B, 43
        "Function_44_438B",        # 2C, 44
        "Function_45_43E7",        # 2D, 45
        "Function_46_4434",        # 2E, 46
        "Function_47_449A",        # 2F, 47
        "Function_48_44DD",        # 30, 48
        "Function_49_4539",        # 31, 49
        "Function_50_45AF",        # 32, 50
        "Function_51_461F",        # 33, 51
        "Function_52_46E1",        # 34, 52
        "Function_53_4757",        # 35, 53
        "Function_54_47DE",        # 36, 54
        "Function_55_4839",        # 37, 55
        "Function_56_4980",        # 38, 56
        "Function_57_49B5",        # 39, 57
        "Function_58_4A31",        # 3A, 58
        "Function_59_4A66",        # 3B, 59
        "Function_60_4A9F",        # 3C, 60
        "Function_61_4AD4",        # 3D, 61
        "Function_62_4B0D",        # 3E, 62
        "Function_63_4B42",        # 3F, 63
        "Function_64_4B7B",        # 40, 64
        "Function_65_4BD6",        # 41, 65
        "Function_66_4C76",        # 42, 66
        "Function_67_4CD1",        # 43, 67
        "Function_68_4D6B",        # 44, 68
        "Function_69_4DC6",        # 45, 69
        "Function_70_4DF4",        # 46, 70
        "Function_71_4E41",        # 47, 71
        "Function_72_4FF0",        # 48, 72
        "Function_73_503D",        # 49, 73
        "Function_74_506C",        # 4A, 74
        "Function_75_50B9",        # 4B, 75
        "Function_76_50EF",        # 4C, 76
        "Function_77_5109",        # 4D, 77
        "Function_78_513A",        # 4E, 78
        "Function_79_51C4",        # 4F, 79
        "Function_80_536B",        # 50, 80
        "Function_81_53B0",        # 51, 81
        "Function_82_53E8",        # 52, 82
        "Function_83_5437",        # 53, 83
    ))


    def Function_0_D7C(): pass

    label("Function_0_D7C")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_DBC"),
        (1, "loc_DC8"),
        (2, "loc_DD4"),
        (3, "loc_DE0"),
        (4, "loc_DEC"),
        (5, "loc_DF8"),
        (6, "loc_E04"),
        (SWITCH_DEFAULT, "loc_E10"),
    )


    label("loc_DBC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E1C")

    label("loc_DC8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E1C")

    label("loc_DD4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E1C")

    label("loc_DE0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E1C")

    label("loc_DEC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E1C")

    label("loc_DF8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E1C")

    label("loc_E04")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E1C")

    label("loc_E10")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E1C")

    label("loc_E1C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E33")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E1C")

    label("loc_E33")

    Return()

    # Function_0_D7C end

    def Function_1_E34(): pass

    label("Function_1_E34")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E52")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_E34")

    label("loc_E52")

    Return()

    # Function_1_E34 end

    def Function_2_E53(): pass

    label("Function_2_E53")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E71")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_E53")

    label("loc_E71")

    Return()

    # Function_2_E53 end

    def Function_3_E72(): pass

    label("Function_3_E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_END)), "loc_E8C")
    SetChrPos(0x8, -13910, 5380, 56930, 295)

    label("loc_E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E9F")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F3E")

    label("loc_E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_EB6")
    SetChrFlags(0x8, 0x80)

    label("loc_EB6")

    Jump("loc_F3E")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_ECE")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F3E")

    label("loc_ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EDC")
    Jump("loc_F3E")

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_EEA")
    Jump("loc_F3E")

    label("loc_EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_EF8")
    Jump("loc_F3E")

    label("loc_EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F06")
    Jump("loc_F3E")

    label("loc_F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F14")
    Jump("loc_F3E")

    label("loc_F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F22")
    Jump("loc_F3E")

    label("loc_F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F30")
    Jump("loc_F3E")

    label("loc_F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F3E")
    SetChrFlags(0x8, 0x80)

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F55")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 7)
    Event(0, 13)
    Jump("loc_F64")

    label("loc_F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F64")
    ClearScenarioFlags(0x22, 1)
    Event(0, 83)

    label("loc_F64")

    Call(0, 9)
    Return()

    # Function_3_E72 end

    def Function_4_F68(): pass

    label("Function_4_F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_F7A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_F8E")
    OP_24(0x7C)
    ClearScenarioFlags(0x0, 7)
    Jump("loc_FAA")

    label("loc_F8E")

    SoundDistance(0x7C, 0xFFFFCE6E, 0x1504, 0x1205C, 0x7530, 0x249F0, 0x64, 0x0)

    label("loc_FAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FD1")
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0xD, 0x4)
    Jump("loc_103A")

    label("loc_FD1")

    OP_78(0xD, 0xD)
    ClearMapObjFlags(0xD, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x1)
    SetChrPos(0xD, -64730, 250, 40720, 0)
    OP_93(0xD, 0x0, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, -64730, -1250, 40720, 3000, 3000, 90000)

    label("loc_103A")

    OP_52(0x31, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13CE")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)

    label("loc_13CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_144C")
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    Jump("loc_148E")

    label("loc_144C")

    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)

    label("loc_148E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1563")
    OP_11(0x87, 0xAA, 0xFF, 0xA, 0x73, 0x0)
    ClearMapObjFlags(0xE, 0x4)
    OP_74(0xE, 0x1E)
    OP_71(0xE, 0x0, 0x258, 0x0, 0x20)
    OP_C3(0x0, 0x1, 0x3, 0x0, 0x0, 0x1, -13740, -500, 5790, 2000, 2000, 0)
    OP_C3(0x1, 0x1, 0x3, 0x0, 0x0, 0x1, -11950, -500, 7590, 2000, 2000, 0)
    OP_C3(0x2, 0x1, 0x3, 0x0, 0x0, 0x1, -10120, -500, 9350, 2000, 2000, 0)
    OP_C3(0x3, 0x1, 0x3, 0x0, 0x0, 0x1, -8140, -500, 11380, 2000, 2000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg2.eff")
    Jump("loc_1569")

    label("loc_1563")

    SetMapObjFlags(0xE, 0x4)

    label("loc_1569")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -13360, 380, 68320, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15CD")
    OP_66(0x1, 0x1)

    label("loc_15CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15DF")
    OP_65(0x1, 0x1)

    label("loc_15DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F2")
    OP_70(0x0, 0x0)
    Jump("loc_15F6")

    label("loc_15F2")

    OP_70(0x0, 0x1E)

    label("loc_15F6")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1657")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -58250, 0, 33120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_1657")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16A3")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 27630, 8000, 38670, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_16A3")

    OP_1C(0x0, 0xF, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x10, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    Return()

    # Function_4_F68 end

    def Function_5_16BA(): pass

    label("Function_5_16BA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AC")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('夜光眼镜', 1)"), scpexpr(EXPR_END)), "loc_173D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '夜光眼镜'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E6, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_17A7")

    label("loc_173D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '夜光眼镜'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '夜光眼镜'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17A7")

    Jump("loc_17E9")

    label("loc_17AC")

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

    label("loc_17E9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16BA end

    def Function_6_17F5(): pass

    label("Function_6_17F5")

    Call(1, 6)
    Return()

    # Function_6_17F5 end

    def Function_7_17F9(): pass

    label("Function_7_17F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1992")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_1978")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0004
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1973")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_1970")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_189B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_189B)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0005
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
    Battle("BattleInfo_490", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196B")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1952")
    Call(1, 5)
    Jump("loc_196B")

    label("loc_1952")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1968")
    Call(1, 4)
    Jump("loc_196B")

    label("loc_1968")

    Call(1, 3)

    label("loc_196B")

    Jump("loc_1973")

    label("loc_1970")

    Call(1, 1)

    label("loc_1973")

    Jump("loc_198E")

    label("loc_1978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_198E")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_198E")

    TalkEnd(0xFF)
    Return()

    label("loc_1992")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_1B03")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0006
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AFE")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_1AFB")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1A26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1A26)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0007
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
    Battle("BattleInfo_4D4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF6")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1ADD")
    Call(1, 5)
    Jump("loc_1AF6")

    label("loc_1ADD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1AF3")
    Call(1, 4)
    Jump("loc_1AF6")

    label("loc_1AF3")

    Call(1, 3)

    label("loc_1AF6")

    Jump("loc_1AFE")

    label("loc_1AFB")

    Call(1, 1)

    label("loc_1AFE")

    Jump("loc_1B19")

    label("loc_1B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_1B19")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1B19")

    TalkEnd(0xFF)
    Return()

    # Function_7_17F9 end

    def Function_8_1B1D(): pass

    label("Function_8_1B1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1CB6")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_1C9C")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0008
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C97")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1C94")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1BBF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1BBF)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0009
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
    Battle("BattleInfo_490", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C8F")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C76")
    Call(1, 5)
    Jump("loc_1C8F")

    label("loc_1C76")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C8C")
    Call(1, 4)
    Jump("loc_1C8F")

    label("loc_1C8C")

    Call(1, 3)

    label("loc_1C8F")

    Jump("loc_1C97")

    label("loc_1C94")

    Call(1, 1)

    label("loc_1C97")

    Jump("loc_1CB2")

    label("loc_1C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1CB2")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1CB2")

    TalkEnd(0xFF)
    Return()

    label("loc_1CB6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_1E27")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0010
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E22")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1E1F")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1D4A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1D4A)
    TurnDirection(0xC, 0x0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    PlayEffect(0x7, 0x1, 0xC, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0011
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
    Battle("BattleInfo_4D4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1A")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E01")
    Call(1, 5)
    Jump("loc_1E1A")

    label("loc_1E01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E17")
    Call(1, 4)
    Jump("loc_1E1A")

    label("loc_1E17")

    Call(1, 3)

    label("loc_1E1A")

    Jump("loc_1E22")

    label("loc_1E1F")

    Call(1, 1)

    label("loc_1E22")

    Jump("loc_1E3D")

    label("loc_1E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1E3D")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1E3D")

    TalkEnd(0xFF)
    Return()

    # Function_8_1B1D end

    def Function_9_1E41(): pass

    label("Function_9_1E41")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E59")
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)

    label("loc_1E59")

    Return()

    # Function_9_1E41 end

    def Function_10_1E5A(): pass

    label("Function_10_1E5A")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x0, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E72")
    SetScenarioFlags(0x0, 6)

    label("loc_1E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_END)), "loc_1E7E")
    SetScenarioFlags(0x0, 6)

    label("loc_1E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2046")
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0012
    ChrTalk(
        0x8,
        "嗯？你是哪位？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#00003F那个……我是钓公师团\x01",
            "的罗伊德。\x02\x03",

            "#00005F您是钓皇俱乐部的成员吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        "不只是如此。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "我还是钓杰四天王之中\x01",
            "最有品位、最具时尚气息的\x01",
            "『水狂』纳西斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "呵呵，看起来，\x01",
            "你是想向我挑战吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "既然如此，你首先要把\x01",
            "克洛斯贝尔最为华美的鱼\x01",
            "钓上来给我看。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00006F那个……就是指\x01",
            "克洛斯贝尔最漂亮的鱼吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "哈哈哈，你就\x01",
            "好好思考一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "我会在这里耐心\x01",
            "等候你的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 3)

    label("loc_2046")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2050")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2943")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2094")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "进行爆钓比赛\x01",      # 1
            "放弃\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_209E")

    label("loc_2094")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_209E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26AA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_262F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2302")

    #C0021
    ChrTalk(
        0x8,
        (
            "嗯，那就把钓鱼手册\x01",
            "给我看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0022
    ChrTalk(
        0x8,
        (
            "不错，锦鲤——\x01",
            "这正是克洛斯贝尔\x01",
            "最为华美的鱼！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        "#4S干得漂亮！#3S\x02",
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

    #C0024
    ChrTalk(
        0x101,
        "#00012F谢、谢谢夸奖……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        "哈哈，哪里。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "那么，我们的\x01",
            "『爆钓比赛』……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "本想以『美感』来分出胜负……\x01",
            "但似乎没有判定准则呢。\x01",
            "不过，还是要采用一个不同于比大小的规则——\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "我们就以『价值』来决定\x01",
            "比赛胜负吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "垂钓机会只有一次——\x01\x07\x02",

            "谁能钓到价值更高的鱼，\x01",
            "就是比赛的获胜者！\x07\x00",
            "  \x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 4)
    Jump("loc_2375")

    label("loc_2302")


    #C0030
    ChrTalk(
        0x8,
        (
            "要以『比较价值』为规则\x01",
            "向我挑战吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "垂钓机会只有一次——\x01\x07\x02",

            "谁能钓到价值更高的鱼，\x01",
            "就是比赛的获胜者！\x07\x00",
            "  \x02",
        )
    )

    CloseMessageWindow()

    label("loc_2375")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要以『比较价值』为规则\x01",
            "向『水狂』纳西斯挑战吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "挑战爆钓比赛\x01",      # 0
            "放弃\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2406"),
        (1, "loc_260D"),
        (SWITCH_DEFAULT, "loc_262A"),
    )


    label("loc_2406")


    #C0033
    ChrTalk(
        0x8,
        (
            "很好！\x01",
            "那我们就立刻开始吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    ClearMapFlags(0x1)
    OP_68(-15360, 4380, 58540, 0)
    MoveCamera(25, 37, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, -2570, 5380, 47750, 295)
    OP_31(0x1)
    SetChrPos(0x101, -13910, 5380, 56930, 315)
    OP_93(0x8, 0x13B, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE("apl/ch51004.itc")
    MiniGame(0x7, 0x2, 0x8, 0xFFFFC131, 0x140, 0xE5B0, 0xFFFFCCB6, 0x140, 0xFA50)
    SetChrPos(0x0, -2570, 5380, 47750, 295)
    OP_31(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2546")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_68(-9740, 4380, 61600, 0)
    MoveCamera(25, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x101, -11300, 5380, 56730, 340)
    OP_93(0xFE, 0xA0, 0x0)
    Sleep(500)
    Call(0, 79)
    Return()

    label("loc_2546")

    OP_68(-12100, 4380, 60440, 0)
    MoveCamera(25, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, -13910, 5380, 56930, 46)
    OP_93(0xFE, 0xE1, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25A5")
    Call(0, 80)
    Jump("loc_25CC")

    label("loc_25A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25BB")
    Call(0, 82)
    Jump("loc_25CC")

    label("loc_25BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25CC")
    Call(0, 81)

    label("loc_25CC")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_93(0x8, 0x13B, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -13910, 5380, 56930, 46)
    OP_31(0x1)
    SetMapFlags(0x1)
    OP_69(0xFF, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_262A")

    label("loc_260D")


    #C0034
    ChrTalk(
        0x8,
        "是吗……真遗憾啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_262A")

    label("loc_262A")

    Jump("loc_26A5")

    label("loc_262F")


    #C0035
    ChrTalk(
        0x8,
        (
            "嗯，那就把钓鱼手册\x01",
            "给我看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0036
    ChrTalk(
        0x8,
        (
            "不对……\x01",
            "没有那种最为华美的鱼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        "再去想想吧。\x02",
    )

    CloseMessageWindow()

    label("loc_26A5")

    Jump("loc_293E")

    label("loc_26AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_293E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_26DB")
    Jump("loc_293E")

    label("loc_26DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2716")

    #C0038
    ChrTalk(
        0x8,
        (
            "又钓到鱼的我……\x01",
            "嗯～真是非常非常美啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293E")

    label("loc_2716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2724")
    Jump("loc_293E")

    label("loc_2724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2761")

    #C0039
    ChrTalk(
        0x8,
        (
            "沐浴在雨水中的我……\x01",
            "嗯～真是太有魅力啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293E")

    label("loc_2761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_27AD")

    #C0040
    ChrTalk(
        0x8,
        "唔，从刚才开始就一直很吵闹。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "嗯～真是太没有美感了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_293E")

    label("loc_27AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27E8")

    #C0042
    ChrTalk(
        0x8,
        (
            "正在等待鱼儿上钩的我……\x01",
            "真是太迷人了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293E")

    label("loc_27E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_281F")

    #C0043
    ChrTalk(
        0x8,
        (
            "正在准备钓饵的我……\x01",
            "嗯～真完美啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293E")

    label("loc_281F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2856")

    #C0044
    ChrTalk(
        0x8,
        (
            "正在挥舞钓竿的我……\x01",
            "嗯～是最棒的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293E")

    label("loc_2856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2891")

    #C0045
    ChrTalk(
        0x8,
        (
            "矗立在大自然之中的我……\x01",
            "嗯～好迷人啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293E")

    label("loc_2891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2927")

    #C0046
    ChrTalk(
        0x8,
        (
            "正在欣赏水面的我……\x01",
            "嗯～真是太美啦！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2922")

    #C0047
    ChrTalk(
        0x101,
        (
            "#00003F（在这里似乎可以钓到鱼呢……\x01",
            "  但已经有别人先到了，还是算了吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2922")

    Jump("loc_293E")

    label("loc_2927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2935")
    Jump("loc_293E")

    label("loc_2935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_293E")

    label("loc_293E")

    Jump("loc_2050")

    label("loc_2943")

    TalkEnd(0xFE)
    Return()

    # Function_10_1E5A end

    def Function_11_2947(): pass

    label("Function_11_2947")

    Battle("BattleInfo_518", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_298E")
    OP_90(0x0, -62530, 0, 33250, 180)
    EventEnd(0x5)
    SetChrFlags(0xD, 0x8000)
    Jump("loc_29C2")

    label("loc_298E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29A1")
    Jump("loc_29C2")

    label("loc_29A1")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0xD, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x3C, 1)
    EventEnd(0x5)

    label("loc_29C2")

    Return()

    # Function_11_2947 end

    def Function_12_29C3(): pass

    label("Function_12_29C3")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0048
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(-13230, 4370, 66180, 1500)
    MoveCamera(25, 49, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(26000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0049
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C70")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A9D")
    MiniGame(0x6, 0x8, 0xFFFFD5B2, 0x1504, 0xE9D4, 0x14E, 0xFFFFCBD0, 0x17C, 0x10AE0)
    Jump("loc_2C70")

    label("loc_2A9D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MiniGame(0x6, 0x9, 0xFFFFD5B2, 0x1504, 0xE9D4, 0x14E, 0xFFFFCBD0, 0x17C, 0x10AE0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C70")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C70")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(-9450, 4370, 64390, 0)
    MoveCamera(20, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21120, 0)
    LoadChrToIndex("apl/ch50160.itc", 0x1E)
    SetChrFlags(0x0, 0x2)
    SetChrChipByIndex(0x0, 0x1E)
    SetChrSubChip(0x0, 0x12)
    SetChrPos(0x0, -10830, 5380, 59860, 334)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    #N0050
    NpcTalk(
        0x0,
        "罗伊德",
        (
            "#00011F这、这是……\x01",
            "好一条漂亮的大鱼啊。\x02\x03",

            "#00003F和蓝带神仙鱼很相似……\x01",
            "莫非是一种\x01",
            "很特别的鱼吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, -10830, 5380, 59860, 334)
    SetChrPos(0x2, -10830, 5380, 59860, 334)
    SetChrPos(0x3, -10830, 5380, 59860, 334)
    SetChrPos(0x4, -10830, 5380, 59860, 334)
    SetChrPos(0x5, -10830, 5380, 59860, 334)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D7(0x1E)
    OP_37()
    SetScenarioFlags(0x18B, 3)

    label("loc_2C70")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_12_29C3 end

    def Function_13_2C75(): pass

    label("Function_13_2C75")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_D7(0x0)
    OP_D7(0x10)
    OP_D7(0x11)
    OP_D7(0x12)
    OP_D7(0x13)
    OP_D7(0x14)
    OP_D7(0x15)
    OP_D7(0x16)
    OP_D7(0x17)
    OP_D7(0x18)
    OP_D7(0x19)
    LoadChrToIndex("monster/ch86150.itc", 0x1E)
    LoadChrToIndex("monster/ch86151.itc", 0x1F)
    LoadChrToIndex("monster/ch86152.itc", 0x20)
    LoadChrToIndex("monster/ch86153.itc", 0x21)
    LoadChrToIndex("chr/ch41950.itc", 0x23)
    LoadChrToIndex("chr/ch41951.itc", 0x24)
    LoadChrToIndex("chr/ch41952.itc", 0x25)
    LoadChrToIndex("chr/ch42050.itc", 0x28)
    LoadChrToIndex("chr/ch42051.itc", 0x29)
    LoadChrToIndex("chr/ch42052.itc", 0x2A)
    LoadChrToIndex("chr/ch42056.itc", 0x2B)
    LoadChrToIndex("chr/ch31250.itc", 0x2D)
    LoadChrToIndex("chr/ch31251.itc", 0x2E)
    LoadChrToIndex("chr/ch31252.itc", 0x2F)
    LoadChrToIndex("chr/ch31350.itc", 0x32)
    LoadChrToIndex("chr/ch31351.itc", 0x33)
    LoadChrToIndex("chr/ch31352.itc", 0x34)
    LoadChrToIndex("apl/ch50112.itc", 0x3C)
    LoadChrToIndex("apl/ch50118.itc", 0x3D)
    LoadChrToIndex("apl/ch50113.itc", 0x3E)
    LoadChrToIndex("chr/ch32650.itc", 0x37)
    LoadChrToIndex("chr/ch32651.itc", 0x38)
    LoadChrToIndex("chr/ch32654.itc", 0x39)
    LoadChrToIndex("chr/ch32654.itc", 0x3A)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "battle/sp003000.eff")
    SoundLoad(124)
    SoundLoad(860)
    SoundLoad(861)
    SoundLoad(974)
    SoundLoad(1001)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x1F)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    SetChrChipByIndex(0x1F, 0x24)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x24)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x24)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x24)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x29)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x29)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x29)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x1E, 0x29)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0xF, 0x2E)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x2E)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x2E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x2E)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x33)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x33)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x3D)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x3D)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x3D)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x3D)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x3D)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0xE, 0x38)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    OP_90(0xE, -8500, 20000, 88000, 270)
    OP_90(0x14, -6500, 20000, 89250, 270)
    OP_90(0x15, -7000, 20000, 88000, 270)
    OP_90(0x16, -5900, 20000, 86700, 270)
    OP_90(0x17, -4950, 20000, 88700, 270)
    OP_90(0x18, -4300, 20000, 87500, 270)
    OP_90(0xF, -4900, 20000, 90300, 270)
    OP_90(0x10, -3350, 20000, 89550, 270)
    OP_90(0x11, -4750, 20000, 85450, 270)
    OP_90(0x12, -3150, 20000, 86450, 270)
    OP_90(0x13, -2400, 20000, 88300, 270)
    SetChrPos(0x19, -47900, 10000, 95450, 135)
    SetChrPos(0x1A, -45250, 10000, 97850, 180)
    SetChrPos(0x1B, -41600, 10000, 98850, 180)
    SetChrPos(0x1C, -39350, 10000, 97850, 225)
    SetChrPos(0x1D, -38350, 10000, 98400, 225)
    OP_52(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-8500, 18300, 88000, 0)
    MoveCamera(55, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(30000, 0)
    OP_68(-36500, 8600, 86000, 7000)
    MoveCamera(55, 25, 0, 7000)
    OP_6E(510, 7000)
    SetCameraDistance(25000, 7000)
    BeginChrThread(0xE, 1, 0, 23)
    BeginChrThread(0x14, 1, 0, 34)
    BeginChrThread(0x15, 1, 0, 36)
    BeginChrThread(0x16, 1, 0, 38)
    BeginChrThread(0x17, 1, 0, 40)
    BeginChrThread(0x18, 1, 0, 42)
    BeginChrThread(0xF, 1, 0, 24)
    BeginChrThread(0x10, 1, 0, 26)
    BeginChrThread(0x11, 1, 0, 28)
    BeginChrThread(0x12, 1, 0, 30)
    BeginChrThread(0x13, 1, 0, 32)
    Sound(124, 2, 60, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    OP_68(-44000, 8600, 74500, 6000)
    MoveCamera(50, 20, 0, 6000)
    SetCameraDistance(22000, 6000)
    Sleep(2000)
    BeginChrThread(0x29, 1, 0, 76)
    BeginChrThread(0x19, 1, 0, 44)
    Sleep(400)
    BeginChrThread(0x1A, 1, 0, 46)
    Sleep(400)
    BeginChrThread(0x1B, 1, 0, 48)
    Sleep(400)
    BeginChrThread(0x1C, 1, 0, 50)
    Sleep(400)
    BeginChrThread(0x1D, 1, 0, 52)
    WaitChrThread(0xE, 1)
    Sound(531, 0, 80, 0)
    WaitChrThread(0x14, 1)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)
    Sound(805, 0, 80, 0)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x13, 1)
    EndChrThread(0x29, 0x1)
    WaitChrThread(0x19, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1D, 1)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x26, 0x4)
    ClearChrFlags(0x27, 0x4)
    ClearChrFlags(0x28, 0x4)
    ClearChrFlags(0x1F, 0x4)
    ClearChrFlags(0x20, 0x4)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    ClearChrFlags(0x25, 0x4)
    ClearChrFlags(0x1E, 0x4)
    OP_90(0x1E, -40550, 4000, 24100, 315)
    OP_90(0x26, -39100, 4000, 22600, 315)
    OP_90(0x27, -37000, 4000, 23300, 315)
    OP_90(0x28, -39500, 4000, 19900, 315)
    OP_90(0x23, -36850, 4000, 20350, 315)
    OP_90(0x24, -34650, 4000, 20100, 315)
    OP_90(0x25, -35800, 4000, 18000, 315)
    OP_90(0x1F, -32549, 4000, 19950, 315)
    OP_90(0x20, -32700, 4000, 17600, 315)
    OP_90(0x21, -34550, 4000, 16350, 315)
    OP_90(0x22, -36850, 4000, 16350, 315)
    BeginChrThread(0x1E, 1, 0, 54)
    BeginChrThread(0x29, 1, 0, 76)
    BeginChrThread(0x26, 1, 0, 70)
    BeginChrThread(0x27, 1, 0, 72)
    BeginChrThread(0x28, 1, 0, 74)
    BeginChrThread(0x23, 1, 0, 64)
    BeginChrThread(0x24, 1, 0, 66)
    BeginChrThread(0x25, 1, 0, 68)
    BeginChrThread(0x1F, 1, 0, 56)
    BeginChrThread(0x20, 1, 0, 58)
    BeginChrThread(0x21, 1, 0, 60)
    BeginChrThread(0x22, 1, 0, 60)
    OP_68(-38550, 1700, 22050, 0)
    MoveCamera(90, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    OP_68(-52550, 1700, 41050, 4500)
    MoveCamera(50, 10, 0, 4500)
    SetCameraDistance(24500, 4500)
    OP_0D()
    Sleep(2000)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sleep(1000)
    CancelBlur(2000)
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x1F, 0x0)
    EndChrThread(0x20, 0x0)
    EndChrThread(0x21, 0x0)
    EndChrThread(0x22, 0x0)
    EndChrThread(0x23, 0x0)
    EndChrThread(0x24, 0x0)
    EndChrThread(0x25, 0x0)
    EndChrThread(0x1E, 0x0)
    ClearChrFlags(0x1F, 0x20)
    ClearChrFlags(0x20, 0x20)
    ClearChrFlags(0x21, 0x20)
    ClearChrFlags(0x22, 0x20)
    ClearChrFlags(0x23, 0x20)
    ClearChrFlags(0x24, 0x20)
    ClearChrFlags(0x25, 0x20)
    ClearChrFlags(0x1E, 0x20)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x22, 0x1)
    EndChrThread(0x1F, 0x0)
    EndChrThread(0x1F, 0x3)
    EndChrThread(0x20, 0x0)
    EndChrThread(0x20, 0x3)
    EndChrThread(0x21, 0x0)
    EndChrThread(0x21, 0x3)
    EndChrThread(0x22, 0x0)
    EndChrThread(0x22, 0x3)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x29, 0x1)
    EndChrThread(0x26, 0x1)
    EndChrThread(0x27, 0x1)
    EndChrThread(0x28, 0x1)
    OP_68(-44000, 8600, 73000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    SetChrChipByIndex(0xE, 0x39)
    SetChrSubChip(0xE, 0x3)
    OP_0D()

    #C0051
    ChrTalk(
        0xE,
        (
            "#07903F作战开始。\x02\x03",

            "#07901F克洛斯贝尔警备队·独立解放部队，\x01",
            "以及神狼部队……\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7544", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    SetChrSubChip(0xE, 0x4)
    Sound(802, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0052
    ChrTalk(
        0xE,
        "#07907F#4S出动！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(80, 0, -1, -1)
    SetChrName("众警备队员")

    #A0053
    AnonymousTalk(
        0xFF,
        "#5S是！长官！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    BeginChrThread(0x19, 0, 0, 22)
    Sleep(30)
    BeginChrThread(0x1A, 0, 0, 22)
    BeginChrThread(0x1B, 0, 0, 22)
    Sleep(30)
    BeginChrThread(0x1C, 0, 0, 22)
    BeginChrThread(0x1D, 0, 0, 22)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sound(1001, 0, 100, 0)
    SetMessageWindowPos(40, 30, -1, -1)
    SetChrName("狼群")

    #A0054
    AnonymousTalk(
        0xFF,
        "#5S嗷！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopEffect(0x0, 0x2)
    BeginChrThread(0x29, 2, 0, 77)
    OP_82(0x32, 0x32, 0xBB8, 0x4E20)
    BeginChrThread(0x14, 1, 0, 35)
    BeginChrThread(0x15, 1, 0, 37)
    BeginChrThread(0x16, 1, 0, 39)
    BeginChrThread(0x17, 1, 0, 41)
    BeginChrThread(0x18, 1, 0, 43)
    BeginChrThread(0xF, 1, 0, 25)
    BeginChrThread(0x10, 1, 0, 27)
    BeginChrThread(0x11, 1, 0, 29)
    BeginChrThread(0x12, 1, 0, 31)
    BeginChrThread(0x13, 1, 0, 33)
    BeginChrThread(0x19, 1, 0, 45)
    BeginChrThread(0x1A, 1, 0, 47)
    BeginChrThread(0x1B, 1, 0, 49)
    BeginChrThread(0x1C, 1, 0, 51)
    BeginChrThread(0x1D, 1, 0, 53)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sleep(1000)
    Fade(500)
    SetChrPos(0x1E, -44150, 0, 55700, 0)
    SetChrPos(0x23, -43050, 0, 54250, 0)
    SetChrPos(0x24, -45150, 0, 53500, 0)
    SetChrPos(0x25, -44000, 0, 52250, 0)
    SetChrPos(0x26, -46350, 0, 54900, 0)
    SetChrPos(0x27, -41550, 0, 55700, 0)
    SetChrPos(0x28, -42100, 0, 51850, 0)
    SetChrFlags(0x27, 0x800)
    SetChrFlags(0x28, 0x800)
    SetChrPos(0x1F, -41050, 0, 51100, 0)
    SetChrPos(0x20, -42650, 0, 50050, 0)
    SetChrPos(0x21, -44850, 0, 50400, 0)
    SetChrPos(0x22, -46700, 0, 50600, 0)
    OP_68(-44230, 2430, 57830, 0)
    MoveCamera(124, 39, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(15000, 0)
    OP_68(-44360, 6230, 63300, 3000)
    MoveCamera(115, 42, 0, 3000)
    SetCameraDistance(18000, 3000)
    BeginChrThread(0x1E, 1, 0, 55)
    BeginChrThread(0x26, 1, 0, 71)
    BeginChrThread(0x27, 1, 0, 73)
    BeginChrThread(0x28, 1, 0, 75)
    BeginChrThread(0x23, 1, 0, 65)
    BeginChrThread(0x24, 1, 0, 67)
    BeginChrThread(0x25, 1, 0, 69)
    BeginChrThread(0x1F, 1, 0, 57)
    BeginChrThread(0x20, 1, 0, 59)
    BeginChrThread(0x21, 1, 0, 61)
    BeginChrThread(0x22, 1, 0, 61)
    OP_6F(0x79)
    Fade(500)
    OP_68(-44100, 5330, 63070, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(31500, 0)
    MoveCamera(55, 35, 0, 6000)
    SetCameraDistance(31500, 6000)
    Sleep(4000)
    StopSound(860, 1000, 50)
    StopSound(861, 1000, 40)
    BeginChrThread(0x29, 2, 0, 78)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    EndChrThread(0x29, 0x1)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0x22, 2)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2C75 end

    def Function_14_383F(): pass

    label("Function_14_383F")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3877"),
        (1, "loc_3883"),
        (2, "loc_388F"),
        (3, "loc_389B"),
        (4, "loc_38A7"),
        (5, "loc_38B3"),
        (6, "loc_38BF"),
        (SWITCH_DEFAULT, "loc_38CB"),
    )


    label("loc_3877")

    OP_A0(0xFE, 1950, 0x0, 0xFB)
    Jump("loc_38D7")

    label("loc_3883")

    OP_A0(0xFE, 2050, 0x0, 0xFB)
    Jump("loc_38D7")

    label("loc_388F")

    OP_A0(0xFE, 2100, 0x0, 0xFB)
    Jump("loc_38D7")

    label("loc_389B")

    OP_A0(0xFE, 1900, 0x0, 0xFB)
    Jump("loc_38D7")

    label("loc_38A7")

    OP_A0(0xFE, 2150, 0x0, 0xFB)
    Jump("loc_38D7")

    label("loc_38B3")

    OP_A0(0xFE, 1850, 0x0, 0xFB)
    Jump("loc_38D7")

    label("loc_38BF")

    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("loc_38D7")

    label("loc_38CB")

    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("loc_38D7")

    label("loc_38D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38EE")
    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("loc_38D7")

    label("loc_38EE")

    Return()

    # Function_14_383F end

    def Function_15_38EF(): pass

    label("Function_15_38EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3922")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3916")
    OP_4C(0xFE, 0x0)
    Jump("loc_391A")

    label("loc_3916")

    OP_4B(0xFE, 0x0)

    label("loc_391A")

    Sleep(500)
    Jump("Function_15_38EF")

    label("loc_3922")

    Return()

    # Function_15_38EF end

    def Function_16_3923(): pass

    label("Function_16_3923")

    SetChrChipByIndex(0xFE, 0x25)

    label("loc_3927")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3976")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 1050, 1700, 0, -20, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("loc_3927")

    label("loc_3976")

    Return()

    # Function_16_3923 end

    def Function_17_3977(): pass

    label("Function_17_3977")

    SetChrChipByIndex(0xFE, 0x2F)

    label("loc_397B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39CA")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x3)
    Jump("loc_397B")

    label("loc_39CA")

    Return()

    # Function_17_3977 end

    def Function_18_39CB(): pass

    label("Function_18_39CB")

    SetChrChipByIndex(0xFE, 0x1F)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3A1D"),
        (1, "loc_3A29"),
        (2, "loc_3A35"),
        (3, "loc_3A41"),
        (4, "loc_3A4D"),
        (5, "loc_3A59"),
        (6, "loc_3A65"),
        (SWITCH_DEFAULT, "loc_3A71"),
    )


    label("loc_3A1D")

    OP_A0(0xFE, 1200, 0x0, 0x5)
    Jump("loc_3A7D")

    label("loc_3A29")

    OP_A0(0xFE, 1300, 0x0, 0x5)
    Jump("loc_3A7D")

    label("loc_3A35")

    OP_A0(0xFE, 1400, 0x0, 0x5)
    Jump("loc_3A7D")

    label("loc_3A41")

    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3A7D")

    label("loc_3A4D")

    OP_A0(0xFE, 1600, 0x0, 0x5)
    Jump("loc_3A7D")

    label("loc_3A59")

    OP_A0(0xFE, 1700, 0x0, 0x5)
    Jump("loc_3A7D")

    label("loc_3A65")

    OP_A0(0xFE, 1800, 0x0, 0x5)
    Jump("loc_3A7D")

    label("loc_3A71")

    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3A7D")

    label("loc_3A7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A94")
    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3A7D")

    label("loc_3A94")

    Return()

    # Function_18_39CB end

    def Function_19_3A95(): pass

    label("Function_19_3A95")

    SetChrChipByIndex(0xFE, 0x1E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AAF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AC6")
    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3AAF")

    label("loc_3AC6")

    Return()

    # Function_19_3A95 end

    def Function_20_3AC7(): pass

    label("Function_20_3AC7")

    SetChrChipByIndex(0xFE, 0x3D)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AE1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AF8")
    OP_A0(0xFE, 1500, 0x0, 0x4)
    Jump("loc_3AE1")

    label("loc_3AF8")

    Return()

    # Function_20_3AC7 end

    def Function_21_3AF9(): pass

    label("Function_21_3AF9")

    SetChrChipByIndex(0xFE, 0x3C)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B13")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B31")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_3B13")

    label("loc_3B31")

    Return()

    # Function_21_3AF9 end

    def Function_22_3B32(): pass

    label("Function_22_3B32")

    SetChrChipByIndex(0xFE, 0x3E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Return()

    # Function_22_3B32 end

    def Function_23_3B57(): pass

    label("Function_23_3B57")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF3, 0x1388, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF3, 0x1388, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF3, 0x1388, 0x1194, 0x0)
    OP_95(0xFE, -44000, 8000, 73000, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_3B57 end

    def Function_24_3BBA(): pass

    label("Function_24_3BBA")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1194, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1194, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_95(0xFE, -42550, 8000, 80000, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_3BBA end

    def Function_25_3C31(): pass

    label("Function_25_3C31")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2E)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -41350, 7990, 71150, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    Sound(531, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 17)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_25_3C31 end

    def Function_26_3C70(): pass

    label("Function_26_3C70")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x1004, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x1004, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1194, 0x1004, 0x0)
    OP_95(0xFE, -42050, 8000, 77650, 4500, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_3C70 end

    def Function_27_3CE7(): pass

    label("Function_27_3CE7")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2E)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -43900, 7700, 70250, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 17)
    BeginChrThread(0xFE, 3, 0, 15)
    PlayEffect(0x1, 0x0, 0xFF, 0x0, -44050, 2070, 58650, 0, -50, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_27_3CE7 end

    def Function_28_3D57(): pass

    label("Function_28_3D57")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0xFA0, 0xFA0, 0x0)
    OP_95(0xFE, -41350, 8000, 75050, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_3D57 end

    def Function_29_3DCE(): pass

    label("Function_29_3DCE")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2E)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -42600, 8140, 71650, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 17)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_29_3DCE end

    def Function_30_3E07(): pass

    label("Function_30_3E07")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_95(0xFE, -42400, 8000, 76250, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_3E07 end

    def Function_31_3E7E(): pass

    label("Function_31_3E7E")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2E)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -46250, 8000, 72600, 4000, 0x0)
    OP_95(0xFE, -46700, 8050, 70350, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 17)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_31_3E7E end

    def Function_32_3ECB(): pass

    label("Function_32_3ECB")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_95(0xFE, -40850, 8000, 79750, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_3ECB end

    def Function_33_3F42(): pass

    label("Function_33_3F42")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2E)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45100, 8000, 75150, 4000, 0x0)
    OP_95(0xFE, -45350, 8170, 70750, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 17)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_33_3F42 end

    def Function_34_3F8F(): pass

    label("Function_34_3F8F")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1324, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1324, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1324, 0x0)
    OP_95(0xFE, -45200, 8000, 74250, 4100, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_3F8F end

    def Function_35_4006(): pass

    label("Function_35_4006")

    SetChrChipByIndex(0xFE, 0x33)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45650, 8000, 72400, 4000, 0x0)
    OP_95(0xFE, -44000, 6110, 64450, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_4006 end

    def Function_36_404C(): pass

    label("Function_36_404C")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x1194, 0x0)
    OP_95(0xFE, -43300, 8000, 74800, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_404C end

    def Function_37_40C3(): pass

    label("Function_37_40C3")

    SetChrChipByIndex(0xFE, 0x33)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -42350, 8000, 72550, 4000, 0x0)
    OP_95(0xFE, -42500, 6280, 64849, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    Sound(844, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_40C3 end

    def Function_38_410F(): pass

    label("Function_38_410F")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF9, 0x1770, 0x109A, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1004, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF3, 0x157C, 0x1004, 0x0)
    OP_95(0xFE, -44550, 8000, 75850, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_410F end

    def Function_39_4186(): pass

    label("Function_39_4186")

    SetChrChipByIndex(0xFE, 0x33)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45550, 8000, 74000, 4000, 0x0)
    OP_95(0xFE, -45550, 8000, 72400, 4000, 0x0)
    OP_95(0xFE, -45550, 6440, 65200, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_39_4186 end

    def Function_40_41E0(): pass

    label("Function_40_41E0")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5BCC, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1194, 0x0)
    OP_95(0xFE, -45800, 8000, 77000, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_40_41E0 end

    def Function_41_4257(): pass

    label("Function_41_4257")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x33)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45550, 8000, 74000, 4000, 0x0)
    OP_95(0xFE, -45550, 8000, 72400, 4000, 0x0)
    OP_95(0xFE, -44500, 6990, 67000, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_4257 end

    def Function_42_42B4(): pass

    label("Function_42_42B4")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x59D8, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0xFA0, 0x0)
    OP_95(0xFE, -43750, 8000, 77750, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_42B4 end

    def Function_43_432B(): pass

    label("Function_43_432B")

    SetChrChipByIndex(0xFE, 0x33)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -43450, 8000, 74700, 4000, 0x0)
    OP_95(0xFE, -42350, 8000, 72550, 4000, 0x0)
    OP_95(0xFE, -43100, 7030, 67600, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    Sound(844, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_43_432B end

    def Function_44_438B(): pass

    label("Function_44_438B")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF4A5C, 0x1F40, 0x15FF4, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 20)
    OP_95(0xFE, -47800, 8000, 74700, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_44_438B end

    def Function_45_43E7(): pass

    label("Function_45_43E7")

    BeginChrThread(0x29, 1, 0, 76)
    BeginChrThread(0xFE, 0, 0, 20)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -46300, 8000, 72350, 5000, 0x0)
    OP_95(0xFE, -46550, 6010, 64250, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x29, 0x1)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_45_43E7 end

    def Function_46_4434(): pass

    label("Function_46_4434")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF5420, 0x1F40, 0x1653A, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0x29, 1, 0, 76)
    BeginChrThread(0xFE, 0, 0, 20)
    OP_95(0xFE, -47050, 8000, 78600, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x29, 0x1)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_46_4434 end

    def Function_47_449A(): pass

    label("Function_47_449A")

    BeginChrThread(0xFE, 0, 0, 20)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -46300, 8000, 72350, 5000, 0x0)
    OP_95(0xFE, -46300, 7050, 66650, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_47_449A end

    def Function_48_44DD(): pass

    label("Function_48_44DD")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF59FC, 0x1F40, 0x16666, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 20)
    OP_95(0xFE, -45000, 8000, 81250, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_48_44DD end

    def Function_49_4539(): pass

    label("Function_49_4539")

    BeginChrThread(0xFE, 0, 0, 20)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -47350, 8000, 74250, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF42BE, 0x23BE, 0x11684, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_95(0xFE, -48100, 8100, 68250, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_49_4539 end

    def Function_50_45AF(): pass

    label("Function_50_45AF")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF60D2, 0x1F40, 0x16602, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 20)
    OP_95(0xFE, -42400, 8000, 83750, 5000, 0x0)
    OP_95(0xFE, -43400, 8000, 80750, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_50_45AF end

    def Function_51_461F(): pass

    label("Function_51_461F")

    BeginChrThread(0xFE, 0, 0, 20)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -40300, 8000, 76350, 5000, 0x0)
    OP_95(0xFE, -40300, 8000, 73900, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF6582, 0x23F0, 0x11684, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_95(0xFE, -40300, 6600, 64900, 5000, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF5E7A, 0x14C8, 0xF4BA, 0x1F4, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_51_461F end

    def Function_52_46E1(): pass

    label("Function_52_46E1")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(844, 0, 30, 0)
    OP_9D(0xFE, 0xFFFF6906, 0x1F40, 0x16184, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 20)
    OP_95(0xFE, -39600, 8000, 85050, 5000, 0x0)
    OP_95(0xFE, -40600, 8000, 82050, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_52_46E1 end

    def Function_53_4757(): pass

    label("Function_53_4757")

    Sleep(1000)
    BeginChrThread(0xFE, 0, 0, 20)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -40300, 8000, 76350, 5000, 0x0)
    OP_95(0xFE, -40300, 8000, 73900, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF6582, 0x23F0, 0x11684, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_95(0xFE, -40300, 6600, 64900, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_53_4757 end

    def Function_54_47DE(): pass

    label("Function_54_47DE")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x1450, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_54_47DE end

    def Function_55_4839(): pass

    label("Function_55_4839")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -44100, 5070, 62200, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    label("loc_485F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_497F")
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x34)
    SetChrSubChip(0x14, 0x2)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x4)
    OP_9D(0x14, 0xFFFF53BC, 0x11F8, 0xF582, 0x3E8, 0xFA0)
    SetChrFlags(0x14, 0x4)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(532, 0, 60, 0)

    def lambda_48B8():
        OP_A0(0xFE, 1500, 0x3, 0x4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_48B8)
    Sound(540, 0, 60, 0)
    Sound(501, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_48D9():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_48D9)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x4)
    WaitChrThread(0xFE, 3)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Sound(538, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x2B)
    OP_A0(0xFE, 1500, 0x0, 0x1)

    def lambda_492B():
        OP_A0(0xFE, 1000, 0x2, 0x4)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_492B)
    ClearChrFlags(0xFE, 0x4)

    def lambda_493D():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_493D)
    SetChrChipByIndex(0x14, 0x34)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x4)
    OP_9B(0x1, 0x14, 0x0, 0xFFFFFD12, 0x2710, 0x0)
    SetChrFlags(0x14, 0x4)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x4)
    Sleep(1000)
    Jump("loc_485F")

    label("loc_497F")

    Return()

    # Function_55_4839 end

    def Function_56_4980(): pass

    label("Function_56_4980")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_56_4980 end

    def Function_57_49B5(): pass

    label("Function_57_49B5")

    SetChrChipByIndex(0xFE, 0x24)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -44300, 7250, 67800, 0, -30, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Sound(860, 2, 60, 0)
    Sound(861, 2, 50, 0)
    BeginChrThread(0xFE, 0, 0, 16)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_57_49B5 end

    def Function_58_4A31(): pass

    label("Function_58_4A31")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_58_4A31 end

    def Function_59_4A66(): pass

    label("Function_59_4A66")

    SetChrChipByIndex(0xFE, 0x24)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 16)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_59_4A66 end

    def Function_60_4A9F(): pass

    label("Function_60_4A9F")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x6590, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_60_4A9F end

    def Function_61_4AD4(): pass

    label("Function_61_4AD4")

    SetChrChipByIndex(0xFE, 0x24)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 16)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_61_4AD4 end

    def Function_62_4B0D(): pass

    label("Function_62_4B0D")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x6978, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_62_4B0D end

    def Function_63_4B42(): pass

    label("Function_63_4B42")

    SetChrChipByIndex(0xFE, 0x24)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 16)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_63_4B42 end

    def Function_64_4B7B(): pass

    label("Function_64_4B7B")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5208, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x13EC, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x13EC, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x13EC, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_64_4B7B end

    def Function_65_4BD6(): pass

    label("Function_65_4BD6")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -42550, 4800, 63150, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x15, 0x34)

    def lambda_4C05():
        OP_A0(0xFE, 1500, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4C05)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4C17():
        OP_96(0xFE, 0xFFFF59CA, 0x141E, 0xFB2C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4C17)

    def lambda_4C31():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_4C31)
    Sound(538, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4C58():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4C58)
    WaitChrThread(0x15, 1)
    SetChrFlags(0x15, 0x4)
    Return()

    # Function_65_4BD6 end

    def Function_66_4C76(): pass

    label("Function_66_4C76")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_66_4C76 end

    def Function_67_4CD1(): pass

    label("Function_67_4CD1")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45400, 5030, 63600, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x16, 0x34)

    def lambda_4D00():
        OP_A0(0xFE, 1500, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_4D00)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4D12():
        OP_96(0xFE, 0xFFFF4EA8, 0x14F0, 0xFCEE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4D12)

    def lambda_4D2C():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_4D2C)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4D4D():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4D4D)
    WaitChrThread(0x16, 1)
    SetChrFlags(0x16, 0x4)
    Return()

    # Function_67_4CD1 end

    def Function_68_4D6B(): pass

    label("Function_68_4D6B")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x14B4, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xBB8, 0x14B4, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x14B4, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_68_4D6B end

    def Function_69_4DC6(): pass

    label("Function_69_4DC6")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45250, 3920, 59150, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x3E8)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_69_4DC6 end

    def Function_70_4DF4(): pass

    label("Function_70_4DF4")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4844, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x13EC, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x13EC, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x13EC, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_70_4DF4 end

    def Function_71_4E41(): pass

    label("Function_71_4E41")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -46400, 4850, 61800, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 19)
    Sleep(1000)

    label("loc_4E72")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FEF")
    EndChrThread(0x19, 0x0)
    SetChrChipByIndex(0x19, 0x3D)
    SetChrSubChip(0x19, 0x0)
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 60, 0)
    ClearChrFlags(0x19, 0x4)
    OP_9D(0x19, 0xFFFF4A8E, 0x1126, 0xF3F2, 0x3E8, 0xFA0)
    SetChrFlags(0x19, 0x4)
    Sound(657, 0, 50, 0)
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x19, 0, 0, 21)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(501, 0, 60, 0)

    def lambda_4F15():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_4F15)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x4)
    WaitChrThread(0xFE, 0)
    BeginChrThread(0xFE, 0, 0, 19)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A0(0xFE, 1500, 0x0, 0x2)
    Sleep(500)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4F82():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4F82)
    Sound(657, 0, 50, 0)

    def lambda_4F9D():
        OP_A0(0xFE, 1500, 0x3, 0x5)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_4F9D)

    def lambda_4FAA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_4FAA)
    ClearChrFlags(0x19, 0x4)
    OP_9B(0x1, 0x19, 0x0, 0xFFFFFC18, 0x2710, 0x0)
    SetChrFlags(0x19, 0x4)
    WaitChrThread(0xFE, 3)
    WaitChrThread(0xFE, 0)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 19)
    Jump("loc_4E72")

    label("loc_4FEF")

    Return()

    # Function_71_4E41 end

    def Function_72_4FF0(): pass

    label("Function_72_4FF0")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4650, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_72_4FF0 end

    def Function_73_503D(): pass

    label("Function_73_503D")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -41750, 4270, 60750, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 19)
    Return()

    # Function_73_503D end

    def Function_74_506C(): pass

    label("Function_74_506C")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xBB8, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x1450, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_74_506C end

    def Function_75_50B9(): pass

    label("Function_75_50B9")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -43200, 3150, 58750, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 19)
    Return()

    # Function_75_50B9 end

    def Function_76_50EF(): pass

    label("Function_76_50EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5108")
    Sound(845, 0, 50, 0)
    Sleep(500)
    Jump("Function_76_50EF")

    label("loc_5108")

    Return()

    # Function_76_50EF end

    def Function_77_5109(): pass

    label("Function_77_5109")

    Sound(974, 2, 40, 0)
    Sleep(200)
    OP_25(0x3CE, 0x32)
    Sleep(200)
    OP_25(0x3CE, 0x3C)
    Sleep(200)
    OP_25(0x3CE, 0x46)
    Sleep(200)
    OP_25(0x3CE, 0x50)
    Sleep(200)
    OP_25(0x3CE, 0x5A)
    Sleep(200)
    OP_25(0x3CE, 0x64)
    Return()

    # Function_77_5109 end

    def Function_78_513A(): pass

    label("Function_78_513A")

    OP_25(0x3CE, 0x5F)
    Sleep(50)
    OP_25(0x3CE, 0x5A)
    Sleep(50)
    OP_25(0x3CE, 0x55)
    Sleep(50)
    OP_25(0x3CE, 0x50)
    Sleep(50)
    OP_25(0x3CE, 0x4B)
    Sleep(50)
    OP_25(0x3CE, 0x46)
    Sleep(50)
    OP_25(0x3CE, 0x41)
    Sleep(50)
    OP_25(0x3CE, 0x3C)
    Sleep(50)
    OP_25(0x3CE, 0x37)
    Sleep(50)
    OP_25(0x3CE, 0x32)
    Sleep(50)
    OP_25(0x3CE, 0x2D)
    Sleep(50)
    OP_25(0x3CE, 0x28)
    Sleep(50)
    OP_25(0x3CE, 0x23)
    Sleep(50)
    OP_25(0x3CE, 0x1E)
    Sleep(50)
    OP_25(0x3CE, 0x19)
    Sleep(50)
    OP_25(0x3CE, 0x14)
    Sleep(50)
    OP_25(0x3CE, 0xF)
    Sleep(50)
    OP_25(0x3CE, 0xA)
    Sleep(50)
    OP_25(0x3CE, 0x5)
    Sleep(50)
    OP_25(0x3CE, 0x0)
    Return()

    # Function_78_513A end

    def Function_79_51C4(): pass

    label("Function_79_51C4")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0055
    ChrTalk(
        0x8,
        (
            "唔，干得好……\x01",
            "你的确很有实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "那就把这枚奖牌送给你，\x01",
            "作为战胜我的证明吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0057
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '水狂奖牌'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('水狂奖牌', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0058
    ChrTalk(
        0x101,
        "#00012F谢、谢谢……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "呵呵，从今以后，\x01",
            "你就可以自称『水狂猎手』啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "呼，但话说回来，\x01",
            "你只不过是战胜我一场罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "今后也一定要继续\x01",
            "磨练自己的审美观哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#00006F是、是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C0, 5)
    SetChrPos(0x8, -13910, 5380, 56930, 295)
    OP_66(0x1, 0x1)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -11300, 5380, 56730, 250)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_79_51C4 end

    def Function_80_536B(): pass

    label("Function_80_536B")


    #C0063
    ChrTalk(
        0x8,
        (
            "呵呵，\x01",
            "我赢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "不要灰心，重新磨练之后，\x01",
            "再次向我挑战吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_80_536B end

    def Function_81_53B0(): pass

    label("Function_81_53B0")


    #C0065
    ChrTalk(
        0x8,
        (
            "嗯？莫非你想\x01",
            "要退缩吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "……真是没有美感啊。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_81_53B0 end

    def Function_82_53E8(): pass

    label("Function_82_53E8")


    #C0067
    ChrTalk(
        0x8,
        (
            "嗯嗯～真是个\x01",
            "没有美感的结果啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "算啦算啦，\x01",
            "以后有机会时再来挑战吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_82_53E8 end

    def Function_83_5437(): pass

    label("Function_83_5437")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetChrPos(0x0, -1500, 0, 9000, 0)
    SetChrPos(0x1, -1500, 0, 9000, 0)
    SetChrPos(0x2, -1500, 0, 9000, 0)
    SetChrPos(0x3, -1500, 0, 9000, 0)
    SetMapObjFlags(0xE, 0x1000)
    OP_68(-11500, 3000, 8000, 0)
    MoveCamera(77, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25500, 0)
    OP_68(-11500, 2500, 8000, 8000)
    MoveCamera(87, 17, 0, 8000)
    SetCameraDistance(21500, 8000)
    OP_71(0xE, 0x208, 0x2BC, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(700)
    Sound(202, 0, 100, 0)
    Sleep(100)
    Sound(223, 0, 100, 0)
    Sleep(1200)
    FadeToDark(1000, 16777215, -1)
    Sound(181, 0, 100, 0)
    Sleep(1500)
    FadeToBright(1000, 16777215)
    OP_0D()
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_83_5437 end

    SaveToFile()

Try(main)
