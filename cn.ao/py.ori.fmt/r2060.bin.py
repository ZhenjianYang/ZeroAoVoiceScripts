from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r2060.bin",                # FileName
        "r2060",                    # MapName
        "r2060",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r0020", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x16,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 3, 0, 4],
    )

    BuildStringList((
        "r2060",                  # 0
        "矿工冈兹",               # 1
        "飞鱼",                   # 2
        "飞鱼",                   # 3
        "钢铁土龙",               # 4
        "钢铁土龙",               # 5
        "警备队员",               # 6
        "警备队员",               # 7
        "警备队员",               # 8
        "警备队员",               # 9
        "警备队员",               # 10
        "警备队员",               # 11
        "警备队员",               # 12
        "警备队员",               # 13
        "猎兵",                   # 14
        "猎兵",                   # 15
        "猎兵",                   # 16
        "猎兵",                   # 17
        "猎兵",                   # 18
        "猎兵",                   # 19
        "猎兵",                   # 20
        "兰迪",                   # 21
        "谢莉",                   # 22
        "米蕾优三尉",             # 23
        "格蕾丝",                 # 24
        "猎兵加雷斯",             # 25
        "狮兽",                   # 26
        "狮兽",                   # 27
        "狮兽",                   # 28
        "狮兽",                   # 29
        "狮兽",                   # 30
        "狮兽",                   # 31
        "狼",                     # 32
        "狼",                     # 33
        "狼",                     # 34
        "狼",                     # 35
        "狼",                     # 36
        "车",                     # 37
        "装甲车",                 # 38
        "装甲车",                 # 39
        "新型装甲车",             # 40
        "武器",                   # 41
        "武器",                   # 42
        "SE控制",                 # 43
        "br2060",                 # 44
        "br2060",                 # 45
        "br2060",                 # 46
        "br2060",                 # 47
        "br2060",                 # 48
        "br2060",                 # 49
        "br2060",                 # 50
        "br2061",                 # 51
        "克洛斯贝尔市方向",       # 52
        "矿山镇玛因兹方向",       # 53
    ))

    ATBonus("ATBonus_A34", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A54", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_126A5", 0,   6,   2,   1,   3,   3,   0)
    Sepith("Sepith_126CD", 0,   0,   0,   5,   5,   5,   3)
    Sepith("Sepith_1268D", 0,   7,   2,   0,   1,   0,   4)
    Sepith("Sepith_126C5", 11,  3,   6,   4,   6,   10,  8)

    MonsterBattlePostion("MonsterBattlePostion_A94", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_A98", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_A9C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AA0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_AA4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_AA8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_AAC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_AB0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_AF4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_AF8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_AFC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_B00", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_B04", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_B08", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_B0C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B10", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_A74", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_A78", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A7C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_A80", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_A84", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_A88", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_A90", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B14", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B18", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B1C", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B20", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B24", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B28", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B2C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B30", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B34", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B38", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_B3C", 9, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_B40", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B44", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B48", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4C", 7, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_B50", 9, 10, 180)

    # monster count: 14

    BattleInfo(
        "BattleInfo_CE4", 0x0000, 53, 6, 45, 10, 1, 50, 0, "br2060", "Sepith_126A5", 30, 40, 20, 10,
        (
            ("ms64400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
        )
    )

    BattleInfo(
        "BattleInfo_B54", 0x0000, 53, 6, 45, 10, 1, 30, 0, "br2060", "Sepith_126CD", 30, 40, 20, 10,
        (
            ("ms71700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms71700.dat", "ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
        )
    )

    BattleInfo(
        "BattleInfo_C1C", 0x0000, 53, 6, 45, 10, 1, 25, 0, "br2060", "Sepith_1268D", 30, 40, 20, 10,
        (
            ("ms65900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
        )
    )

    BattleInfo(
        "BattleInfo_DAC", 0x0000, 81, 6, 45, 6, 1, 30, 0, "br2060", "Sepith_126C5", 40, 35, 25, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_E48", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7453", "ed7453", "ATBonus_A34"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E8C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7453", "ed7453", "ATBonus_A34"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_ED0", 0x00DA, 3, 6, 45, 3, 3, 30, 0, "br2060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03400.dat", "ms41900.dat", "ms41900.dat", "ms82000.dat", 0, 0, "ms81800.dat", 0, "MonsterBattlePostion_B14", "MonsterBattlePostion_A94", "ed7455", "ed7453", "ATBonus_A54"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_F14", 0x0042, 0, 6, 0, 0, 3, 0, 0, "br2061", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42100.dat", "ms82001.dat", "ms82001.dat", "ms82001.dat", "ms82001.dat", "ms82001.dat", "ms82001.dat", 0, "MonsterBattlePostion_B34", "MonsterBattlePostion_B34", "ed7455", "ed7453", "ATBonus_A54"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch30700.itc",                   # 00
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
        "monster/ch71750.itc",               # 10
        "monster/ch71751.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch64450.itc",               # 14
        "monster/ch64450.itc",               # 15
        "monster/ch76050.itc",               # 16
        "monster/ch76051.itc",               # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(3630,    0,       25250,   270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(14050,   10000,   160259,  270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(3630,    0,       25250,   270,  484,  0x0, 0,   22,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(14050,   10000,   160259,  270,  484,  0x0, 0,   22,  0,   0,   2,   255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(690,     27940,   0,       0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-39910,  61380,   0,       0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-42170,  79460,   0,       0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(350,     141340,  0,       0x1010000,    "BattleInfo_B54", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(5600,    124460,  0,       0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(23790,   135160,  0,       0x1010000,    "BattleInfo_C1C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-7650,   149400,  4000,    0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(15210,   144180,  6000,    0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(12090,   156500,  10000,   0x1010000,    "BattleInfo_B54", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(6050,    159680,  10000,   0x1010000,    "BattleInfo_B54", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-13710,  39330,   0,       0x1010000,    "BattleInfo_DAC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-32470,  88800,   0,       0x1010000,    "BattleInfo_DAC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-20640,  138730,  0,       0x1010000,    "BattleInfo_DAC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(14120,   125230,  0,       0x1010000,    "BattleInfo_DAC", 0,   22,  0xFFFF, 6,  7)

    DeclEvent(0x0040, 0, 12,  -24.0,                 196.0,                 7.0,                   42.25,                 [0.07692307978868484,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.07692307978868484,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.846153974533081,     -15.076923370361328,   -1.399999976158142,    1.0])
    DeclEvent(0x0000, 0, 99,  -20.0,                 152.0,                 2.0,                   900.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.6666667461395264,    -30.399999618530273,   -0.4000000059604645,   1.0])
    DeclEvent(0x0000, 0, 100, -8.0,                  135.5,                 -1.0,                  2500.0,                [0.18793852627277374,  0.017101014032959938,  -0.0,                  0.0,                   -0.06840405613183975,  0.046984631568193436,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   10.772257804870605,    -6.229609489440918,    0.20000001788139343,   1.0])
    DeclEvent(0x0000, 0, 14,  -25.84000015258789,    198.6999969482422,     7.0,                   441.0,                 [0.05050760880112648,  0.23570233583450317,   -0.0,                  0.0,                   -0.050507642328739166, 0.23570218682289124,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   11.340985298156738,    -40.74347686767578,    -1.3999998569488525,   1.0])

    DeclActor(18120,   10000,   151900,  1200,    18120,   11000,   151900,  0x007C, 0,  5,  0x0000)
    DeclActor(-42340,  8000,    197150,  1200,    -42340,  9000,    197150,  0x007C, 0,  6,  0x0000)
    DeclActor(21780,   6050,    139350,  1200,    21780,   7050,    139350,  0x007C, 0,  7,  0x0000)
    DeclActor(3630,    0,       25250,   1200,    3630,    0,       25250,   0x007C, 0,  8,  0x0000)
    DeclActor(14050,   10000,   160260,  1200,    14050,   10000,   160260,  0x007C, 0,  9,  0x0000)
    DeclActor(-20040,  8000,    199730,  1200,    -20040,  9500,    199730,  0x007C, 0,  142, 0x0000)
    DeclActor(-22660,  8000,    197420,  1200,    -22660,  9500,    197420,  0x007C, 0,  142, 0x0000)

    PlaceName(-3.0, 0.0, -15.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(87.0, 6.0, 122.0, 0x0000, 0x0000, "矿山镇玛因兹方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_11F4",         # 00, 0
        "Function_1_12A4",         # 01, 1
        "Function_2_12C3",         # 02, 2
        "Function_3_12E2",         # 03, 3
        "Function_4_188B",         # 04, 4
        "Function_5_2121",         # 05, 5
        "Function_6_225C",         # 06, 6
        "Function_7_2397",         # 07, 7
        "Function_8_24D2",         # 08, 8
        "Function_9_27FC",         # 09, 9
        "Function_10_2B26",        # 0A, 10
        "Function_11_2B49",        # 0B, 11
        "Function_12_2C8D",        # 0C, 12
        "Function_13_32AF",        # 0D, 13
        "Function_14_32D7",        # 0E, 14
        "Function_15_3599",        # 0F, 15
        "Function_16_35B0",        # 10, 16
        "Function_17_37EE",        # 11, 17
        "Function_18_3854",        # 12, 18
        "Function_19_385F",        # 13, 19
        "Function_20_38BD",        # 14, 20
        "Function_21_394B",        # 15, 21
        "Function_22_3A5F",        # 16, 22
        "Function_23_3ACF",        # 17, 23
        "Function_24_3C4C",        # 18, 24
        "Function_25_3CBF",        # 19, 25
        "Function_26_3CD4",        # 1A, 26
        "Function_27_3DF1",        # 1B, 27
        "Function_28_3E53",        # 1C, 28
        "Function_29_5152",        # 1D, 29
        "Function_30_5268",        # 1E, 30
        "Function_31_5385",        # 1F, 31
        "Function_32_53D1",        # 20, 32
        "Function_33_542B",        # 21, 33
        "Function_34_5471",        # 22, 34
        "Function_35_54BD",        # 23, 35
        "Function_36_5510",        # 24, 36
        "Function_37_555D",        # 25, 37
        "Function_38_55AA",        # 26, 38
        "Function_39_55FD",        # 27, 39
        "Function_40_563C",        # 28, 40
        "Function_41_908D",        # 29, 41
        "Function_42_90B5",        # 2A, 42
        "Function_43_90DD",        # 2B, 43
        "Function_44_9105",        # 2C, 44
        "Function_45_912D",        # 2D, 45
        "Function_46_9155",        # 2E, 46
        "Function_47_9191",        # 2F, 47
        "Function_48_91CD",        # 30, 48
        "Function_49_91F5",        # 31, 49
        "Function_50_9229",        # 32, 50
        "Function_51_9279",        # 33, 51
        "Function_52_92C9",        # 34, 52
        "Function_53_9319",        # 35, 53
        "Function_54_9374",        # 36, 54
        "Function_55_93BF",        # 37, 55
        "Function_56_941B",        # 38, 56
        "Function_57_944D",        # 39, 57
        "Function_58_947F",        # 3A, 58
        "Function_59_94E4",        # 3B, 59
        "Function_60_9546",        # 3C, 60
        "Function_61_9593",        # 3D, 61
        "Function_62_95E4",        # 3E, 62
        "Function_63_9682",        # 3F, 63
        "Function_64_969B",        # 40, 64
        "Function_65_96B4",        # 41, 65
        "Function_66_96CD",        # 42, 66
        "Function_67_96E5",        # 43, 67
        "Function_68_9750",        # 44, 68
        "Function_69_97F9",        # 45, 69
        "Function_70_9809",        # 46, 70
        "Function_71_981F",        # 47, 71
        "Function_72_9839",        # 48, 72
        "Function_73_C8DE",        # 49, 73
        "Function_74_C90C",        # 4A, 74
        "Function_75_C940",        # 4B, 75
        "Function_76_CA36",        # 4C, 76
        "Function_77_CA6A",        # 4D, 77
        "Function_78_CAEF",        # 4E, 78
        "Function_79_CB45",        # 4F, 79
        "Function_80_CC06",        # 50, 80
        "Function_81_CC5C",        # 51, 81
        "Function_82_CCE3",        # 52, 82
        "Function_83_CD4D",        # 53, 83
        "Function_84_CE29",        # 54, 84
        "Function_85_CE93",        # 55, 85
        "Function_86_CF35",        # 56, 86
        "Function_87_CFB3",        # 57, 87
        "Function_88_D037",        # 58, 88
        "Function_89_D087",        # 59, 89
        "Function_90_D14C",        # 5A, 90
        "Function_91_D1CF",        # 5B, 91
        "Function_92_D24C",        # 5C, 92
        "Function_93_D2B5",        # 5D, 93
        "Function_94_D31E",        # 5E, 94
        "Function_95_D373",        # 5F, 95
        "Function_96_D3CE",        # 60, 96
        "Function_97_D3F3",        # 61, 97
        "Function_98_D418",        # 62, 98
        "Function_99_D7DA",        # 63, 99
        "Function_100_D951",       # 64, 100
        "Function_101_E6FE",       # 65, 101
        "Function_102_E777",       # 66, 102
        "Function_103_E7F0",       # 67, 103
        "Function_104_10EDC",      # 68, 104
        "Function_105_10EF8",      # 69, 105
        "Function_106_10F14",      # 6A, 106
        "Function_107_10F30",      # 6B, 107
        "Function_108_10F4C",      # 6C, 108
        "Function_109_10F6C",      # 6D, 109
        "Function_110_11071",      # 6E, 110
        "Function_111_110E6",      # 6F, 111
        "Function_112_111C1",      # 70, 112
        "Function_113_11251",      # 71, 113
        "Function_114_11356",      # 72, 114
        "Function_115_113EC",      # 73, 115
        "Function_116_114A1",      # 74, 116
        "Function_117_11516",      # 75, 117
        "Function_118_115B9",      # 76, 118
        "Function_119_1162E",      # 77, 119
        "Function_120_116D7",      # 78, 120
        "Function_121_1174C",      # 79, 121
        "Function_122_11810",      # 7A, 122
        "Function_123_118D0",      # 7B, 123
        "Function_124_1194E",      # 7C, 124
        "Function_125_119FC",      # 7D, 125
        "Function_126_11A5E",      # 7E, 126
        "Function_127_11AAE",      # 7F, 127
        "Function_128_11B4D",      # 80, 128
        "Function_129_11BEC",      # 81, 129
        "Function_130_11C5C",      # 82, 130
        "Function_131_11DA3",      # 83, 131
        "Function_132_11E40",      # 84, 132
        "Function_133_11F68",      # 85, 133
        "Function_134_11F9A",      # 86, 134
        "Function_135_11FD3",      # 87, 135
        "Function_136_12086",      # 88, 136
        "Function_137_12140",      # 89, 137
        "Function_138_121FA",      # 8A, 138
        "Function_139_122C4",      # 8B, 139
        "Function_140_1232E",      # 8C, 140
        "Function_141_1238D",      # 8D, 141
        "Function_142_123BE",      # 8E, 142
    ))


    def Function_0_11F4(): pass

    label("Function_0_11F4")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_122C"),
        (1, "loc_1238"),
        (2, "loc_1244"),
        (3, "loc_1250"),
        (4, "loc_125C"),
        (5, "loc_1268"),
        (6, "loc_1274"),
        (SWITCH_DEFAULT, "loc_1280"),
    )


    label("loc_122C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1238")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1244")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1250")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_125C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1268")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1274")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1280")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_128C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_12A3")

    Return()

    # Function_0_11F4 end

    def Function_1_12A4(): pass

    label("Function_1_12A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12C2")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_12A4")

    label("loc_12C2")

    Return()

    # Function_1_12A4 end

    def Function_2_12C3(): pass

    label("Function_2_12C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12E1")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_12C3")

    label("loc_12E1")

    Return()

    # Function_2_12C3 end

    def Function_3_12E2(): pass

    label("Function_3_12E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1306")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -24500, 8000, 193000, 270)

    label("loc_1306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1321")
    SetMapFlags(0x10000000)
    Event(0, 40)
    Jump("loc_1337")

    label("loc_1321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1337")
    SetMapFlags(0x10000000)
    Event(0, 98)

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_134E")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 16)
    Jump("loc_13CA")

    label("loc_134E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1362")
    ClearScenarioFlags(0x22, 1)
    Event(0, 21)
    Jump("loc_13CA")

    label("loc_1362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1376")
    ClearScenarioFlags(0x22, 2)
    Event(0, 23)
    Jump("loc_13CA")

    label("loc_1376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_138A")
    ClearScenarioFlags(0x22, 3)
    Event(0, 26)
    Jump("loc_13CA")

    label("loc_138A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_13A1")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x0, 0)
    Event(0, 28)
    Jump("loc_13CA")

    label("loc_13A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_13B5")
    ClearScenarioFlags(0x22, 5)
    Event(0, 72)
    Jump("loc_13CA")

    label("loc_13B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_13CA")
    ClearScenarioFlags(0x22, 6)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 103)

    label("loc_13CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1877")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1460")
    SetScenarioFlags(0x38, 0)

    label("loc_1460")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1476")
    SetScenarioFlags(0x38, 1)

    label("loc_1476")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148C")
    SetScenarioFlags(0x38, 2)

    label("loc_148C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A2")
    SetScenarioFlags(0x38, 3)

    label("loc_14A2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B8")
    SetScenarioFlags(0x38, 4)

    label("loc_14B8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14CE")
    SetScenarioFlags(0x38, 5)

    label("loc_14CE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E4")
    SetScenarioFlags(0x38, 6)

    label("loc_14E4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FA")
    SetScenarioFlags(0x38, 7)

    label("loc_14FA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1510")
    SetScenarioFlags(0x39, 0)

    label("loc_1510")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1526")
    SetScenarioFlags(0x39, 1)

    label("loc_1526")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_153C")
    SetScenarioFlags(0x39, 2)

    label("loc_153C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1552")
    SetScenarioFlags(0x39, 3)

    label("loc_1552")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1568")
    SetScenarioFlags(0x39, 4)

    label("loc_1568")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157E")
    SetScenarioFlags(0x39, 5)

    label("loc_157E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1594")
    SetScenarioFlags(0x39, 6)

    label("loc_1594")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AA")
    SetScenarioFlags(0x39, 7)

    label("loc_15AA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C0")
    SetScenarioFlags(0x3A, 0)

    label("loc_15C0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D6")
    SetScenarioFlags(0x3A, 1)

    label("loc_15D6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EC")
    SetScenarioFlags(0x3A, 2)

    label("loc_15EC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1602")
    SetScenarioFlags(0x3A, 3)

    label("loc_1602")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1618")
    SetScenarioFlags(0x3A, 4)

    label("loc_1618")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162E")
    SetScenarioFlags(0x3A, 5)

    label("loc_162E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1644")
    SetScenarioFlags(0x3A, 6)

    label("loc_1644")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165A")
    SetScenarioFlags(0x3A, 7)

    label("loc_165A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1670")
    SetScenarioFlags(0x3B, 0)

    label("loc_1670")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1686")
    SetScenarioFlags(0x3B, 1)

    label("loc_1686")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169C")
    SetScenarioFlags(0x3B, 2)

    label("loc_169C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B2")
    SetScenarioFlags(0x3B, 3)

    label("loc_16B2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C8")
    SetScenarioFlags(0x3B, 4)

    label("loc_16C8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16DE")
    SetScenarioFlags(0x3B, 5)

    label("loc_16DE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F4")
    SetScenarioFlags(0x3B, 6)

    label("loc_16F4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170A")
    SetScenarioFlags(0x3B, 7)

    label("loc_170A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1720")
    SetScenarioFlags(0x3D, 5)

    label("loc_1720")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1736")
    SetScenarioFlags(0x3D, 6)

    label("loc_1736")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174C")
    SetScenarioFlags(0x3D, 7)

    label("loc_174C")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1787")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1877")

    label("loc_1787")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AA")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1877")

    label("loc_17AA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CD")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1877")

    label("loc_17CD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F0")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1877")

    label("loc_17F0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1813")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1877")

    label("loc_1813")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1836")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1877")

    label("loc_1836")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1859")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1877")

    label("loc_1859")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1877")
    SetScenarioFlags(0x3C, 7)

    label("loc_1877")

    Call(0, 10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_188A")
    OP_E2(0x1)

    label("loc_188A")

    Return()

    # Function_3_12E2 end

    def Function_4_188B(): pass

    label("Function_4_188B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18A5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_18B7")

    label("loc_18A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_18B7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18B7")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18CF")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_18CF")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E7")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_18E7")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1904")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1904")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_191C")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_191C")

    OP_52(0x3D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x3D, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E0B")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1E32")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_1E32")

    label("loc_1E32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E94")
    LoadEffect(0x9, "event/ev11006.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 1)), scpexpr(EXPR_END)), "loc_1E94")
    PlayEffect(0x9, 0x0, 0xFF, 0x0, -16500, 10100, 203350, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_1E94")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EEE")
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    SetBarrier(0x0, 0x1, 0x1, 0x0, -23440, 8000, 175460, 10000, 5000, 150000)
    Jump("loc_1F0E")

    label("loc_1EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F0E")
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)

    label("loc_1F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1E")
    SetMapObjFlags(0x5, 0x4)

    label("loc_1F1E")

    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F79")
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetBarrier(0x0, 0x0, 0x1, 0x0, -19610, 3500, 152140, 8000, 5000, 0)

    label("loc_1F79")

    SetMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F92")
    OP_70(0x0, 0x0)
    Jump("loc_1F96")

    label("loc_1F92")

    OP_70(0x0, 0x1E)

    label("loc_1F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA9")
    OP_70(0x1, 0x0)
    Jump("loc_1FAD")

    label("loc_1FA9")

    OP_70(0x1, 0x1E)

    label("loc_1FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC0")
    OP_70(0x2, 0x0)
    Jump("loc_1FC4")

    label("loc_1FC0")

    OP_70(0x2, 0x1E)

    label("loc_1FC4")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2025")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 3630, 0, 25250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_2025")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2071")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 14050, 10000, 160260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_2071")

    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_209D")
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x10)
    Jump("loc_20D5")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B0")
    OP_66(0x5, 0x1)
    Jump("loc_20D5")

    label("loc_20B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BF")
    Jump("loc_20D5")

    label("loc_20BF")

    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x10)
    OP_66(0x6, 0x1)

    label("loc_20D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_20E9")
    OP_24(0x6E)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_2120")

    label("loc_20E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2120")
    SoundDistance(0x6E, 0xFFFFE976, 0x1F40, 0x2F472, 0x186A0, 0x186A0, 0x5A, 0x0)
    OP_E3(0xAFC8, 0x0, 0xDEEE)

    label("loc_2120")

    Return()

    # Function_4_188B end

    def Function_5_2121(): pass

    label("Function_5_2121")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2213")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('Ｕ材料', 1)"), scpexpr(EXPR_END)), "loc_21A4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_220E")

    label("loc_21A4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_220E")

    Jump("loc_2250")

    label("loc_2213")

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

    label("loc_2250")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_2121 end

    def Function_6_225C(): pass

    label("Function_6_225C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234E")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('安全头盔', 1)"), scpexpr(EXPR_END)), "loc_22DF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_2349")

    label("loc_22DF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x5B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x5B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2349")

    Jump("loc_238B")

    label("loc_234E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_238B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_225C end

    def Function_7_2397(): pass

    label("Function_7_2397")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2489")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅰ', 1)"), scpexpr(EXPR_END)), "loc_241A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_2484")

    label("loc_241A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2484")

    Jump("loc_24C6")

    label("loc_2489")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_24C6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_2397 end

    def Function_8_24D2(): pass

    label("Function_8_24D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2670")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_2651")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_264C")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_2649")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2574():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2574)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_E48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2644")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_262B")
    Call(1, 5)
    Jump("loc_2644")

    label("loc_262B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2641")
    Call(1, 4)
    Jump("loc_2644")

    label("loc_2641")

    Call(1, 3)

    label("loc_2644")

    Jump("loc_264C")

    label("loc_2649")

    Call(1, 1)

    label("loc_264C")

    Jump("loc_2667")

    label("loc_2651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_2667")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2667")

    TalkEnd(0xFF)
    Return()

    label("loc_2670")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_27E1")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0012
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27DC")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_27D9")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2704():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2704)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0013
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
    Battle("BattleInfo_E8C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D4")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27BB")
    Call(1, 5)
    Jump("loc_27D4")

    label("loc_27BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27D1")
    Call(1, 4)
    Jump("loc_27D4")

    label("loc_27D1")

    Call(1, 3)

    label("loc_27D4")

    Jump("loc_27DC")

    label("loc_27D9")

    Call(1, 1)

    label("loc_27DC")

    Jump("loc_27F7")

    label("loc_27E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_27F7")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_27F7")

    TalkEnd(0xFF)
    Return()

    # Function_8_24D2 end

    def Function_9_27FC(): pass

    label("Function_9_27FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_299A")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_297B")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0014
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2976")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2973")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_289E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_289E)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0015
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
    Battle("BattleInfo_E48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296E")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2955")
    Call(1, 5)
    Jump("loc_296E")

    label("loc_2955")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_296B")
    Call(1, 4)
    Jump("loc_296E")

    label("loc_296B")

    Call(1, 3)

    label("loc_296E")

    Jump("loc_2976")

    label("loc_2973")

    Call(1, 1)

    label("loc_2976")

    Jump("loc_2991")

    label("loc_297B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2991")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2991")

    TalkEnd(0xFF)
    Return()

    label("loc_299A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_2B0B")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0016
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B06")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2B03")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2A2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2A2E)
    TurnDirection(0xC, 0x0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    PlayEffect(0x7, 0x1, 0xC, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0017
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
    Battle("BattleInfo_E8C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AFE")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2AE5")
    Call(1, 5)
    Jump("loc_2AFE")

    label("loc_2AE5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2AFB")
    Call(1, 4)
    Jump("loc_2AFE")

    label("loc_2AFB")

    Call(1, 3)

    label("loc_2AFE")

    Jump("loc_2B06")

    label("loc_2B03")

    Call(1, 1)

    label("loc_2B06")

    Jump("loc_2B21")

    label("loc_2B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2B21")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2B21")

    TalkEnd(0xFF)
    Return()

    # Function_9_27FC end

    def Function_10_2B26(): pass

    label("Function_10_2B26")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B48")
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x40, 0x80)

    label("loc_2B48")

    Return()

    # Function_10_2B26 end

    def Function_11_2B49(): pass

    label("Function_11_2B49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C44")

    #C0018
    ChrTalk(
        0xFE,
        (
            "这里就是旧矿山的入口，如果已经\x01",
            "准备好了，就拜托各位进去调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "……话说回来，竟然能把\x01",
            "这么坚固的大门破坏……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "就算是平时一直从事体力劳动\x01",
            "的我们也不可能做得到。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "到底是什么人干的啊……\x01",
            "你们进去以后一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C89")

    label("loc_2C44")


    #C0022
    ChrTalk(
        0xFE,
        (
            "这里就是旧矿山的入口，如果已经\x01",
            "准备好了，就拜托各位进去调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C89")

    TalkEnd(0xFE)
    Return()

    # Function_11_2B49 end

    def Function_12_2C8D(): pass

    label("Function_12_2C8D")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -24500, 8000, 193000, 225)
    OP_68(-26610, 8600, 194070, 0)
    MoveCamera(18, 12, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22780, 0)
    SetChrPos(0x101, -30700, 8000, 190200, 45)
    SetChrPos(0x102, -29700, 8000, 189200, 45)
    SetChrPos(0x109, -31700, 8000, 189200, 45)
    SetChrPos(0x105, -30700, 8000, 188200, 45)
    SetCameraDistance(21780, 2000)

    def lambda_2D42():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D42)
    Sleep(50)

    def lambda_2D5A():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D5A)
    Sleep(50)

    def lambda_2D72():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2D72)
    Sleep(50)
    FadeToBright(1000, 0)

    def lambda_2D93():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2D93)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0023
    ChrTalk(
        0x8,
        "#11P哟，你们来了啊。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00000F#6P嗯，就是这里吧？\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_68(-27470, 9000, 194940, 1500)
    MoveCamera(6, 20, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(16800, 1500)
    Sleep(200)

    def lambda_2E28():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E28)
    Sleep(100)

    def lambda_2E38():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2E38)
    Sleep(100)

    def lambda_2E48():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2E48)
    Sleep(100)

    def lambda_2E58():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2E58)
    OP_6F(0x79)
    Sleep(300)

    #C0025
    ChrTalk(
        0x101,
        "#00001F#6P#N这就是那扇被破坏的门吗……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0026
    ChrTalk(
        0x102,
        (
            "#00101F#12P#N……好像是被\x01",
            "某种武器斩开的呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0027
    ChrTalk(
        0x8,
        (
            "#11P嗯，老实说，很难相信\x01",
            "这是凭人类之力做到的……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "#11P总之，这里就是旧矿山的入口。\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x9, 0x0, 0xFF, 0x0, -16500, 10100, 203350, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x32, 1, 0, 13)
    Sleep(200)

    def lambda_2F67():
        OP_93(0xFE, 0x2C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2F67)
    Sleep(300)
    OP_68(-25180, 9700, 194680, 2000)
    MoveCamera(45, 4, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(14520, 2000)

    def lambda_2FA5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2FA5)
    Sleep(100)

    def lambda_2FB5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2FB5)
    Sleep(150)

    def lambda_2FC5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2FC5)
    Sleep(100)

    def lambda_2FD5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2FD5)
    Sleep(600)
    OP_6F(0x79)
    Sleep(500)

    #C0029
    ChrTalk(
        0x109,
        "#10105F#6P#N这、这光芒是……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0030
    ChrTalk(
        0x105,
        (
            "#10304F#12P#N呵呵，\x01",
            "相当妖异的气氛啊。\x02\x03",

            "#10300F里面似乎徘徊着\x01",
            "很危险的魔兽。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0031
    ChrTalk(
        0x101,
        "#00003F#6P#N嗯……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopSound(828, 1000, 40)
    Sleep(500)
    Sleep(100)
    OP_68(-27900, 9400, 191850, 1500)
    MoveCamera(45, 20, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(17520, 1500)
    Sleep(1000)

    def lambda_30B6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_30B6)
    Sleep(100)

    def lambda_30C6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_30C6)
    OP_6F(0x79)

    #C0032
    ChrTalk(
        0x102,
        (
            "#00108F#11P……罗伊德，怎么办？\x02\x03",

            "#00101F如果情势需要，\x01",
            "不妨与警备队联络……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x109,
        (
            "#10106F#6P有道理……\x01",
            "那样可以增加调查人手。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3157():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3157)
    Sleep(50)

    def lambda_3167():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3167)
    Sleep(50)

    def lambda_3177():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3177)
    Sleep(200)

    #C0034
    ChrTalk(
        0x101,
        (
            "#00003F#5P……不，还是先由\x01",
            "我们几个去调查内部的情况吧。\x02\x03",

            "#00001F如果凭我们的能力无法应付，\x01",
            "再请求警备队的支援也不迟。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        "#00100F#11P明白了。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x109,
        "#10101F#6P知道了！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x105,
        (
            "#10302F#12P既然如此，我们最好\x01",
            "准备万全之后再进去啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x8, -24500, 8000, 193000, 270)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -28770, 8000, 190930, 45)
    SetScenarioFlags(0x12A, 1)
    OP_29(0xA2, 0x1, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    EventEnd(0x5)
    Return()

    # Function_12_2C8D end

    def Function_13_32AF(): pass

    label("Function_13_32AF")

    Sleep(2300)
    Sound(929, 0, 30, 0)
    Sound(828, 2, 50, 0)
    Sleep(2200)
    Sound(831, 0, 40, 0)
    Sleep(1500)
    Sound(948, 0, 30, 0)
    Sound(830, 0, 30, 0)
    Return()

    # Function_13_32AF end

    def Function_14_32D7(): pass

    label("Function_14_32D7")

    EventBegin(0x0)
    Fade(500)
    OP_68(-25500, 8600, 194000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -26580, 8000, 194320, 45)
    SetChrPos(0x102, -25580, 8000, 193320, 45)
    SetChrPos(0x109, -27580, 8000, 193320, 45)
    SetChrPos(0x105, -26580, 8000, 192320, 45)
    OP_0D()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00008F#5P（一旦开始调查此地，\x01",
            "  恐怕就无暇处理其它事情了。）\x02\x03",

            "#00001F（……要怎么办？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还有其它事情】\x01",      # 0
            "【进入旧矿山】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_340F"),
        (1, "loc_3427"),
        (SWITCH_DEFAULT, "loc_3598"),
    )


    label("loc_340F")

    SetChrPos(0x0, -27820, 8000, 192000, 225)
    EventEnd(0x5)
    Jump("loc_3598")

    label("loc_3427")

    OP_4B(0x8, 0xFF)
    Sleep(100)

    def lambda_3433():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3433)
    Sleep(50)

    def lambda_3443():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3443)
    Sleep(50)

    def lambda_3453():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3453)
    Sleep(50)

    def lambda_3463():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3463)
    Sleep(300)

    #C0039
    ChrTalk(
        0x101,
        (
            "#00000F#6P冈兹先生。\x02\x03",

            "我们这就进去调查一下，\x01",
            "请您在这里等我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        "#11P嗯，要小心啊。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "#11P如果觉得情况危险，\x01",
            "一定要赶快出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-23660, 8600, 196120, 2500)
    MoveCamera(44, 15, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(21380, 2500)

    def lambda_352B():

        label("loc_352B")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_352B")

    QueueWorkItem2(0x8, 2, lambda_352B)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 15)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 15)
    Sleep(100)
    BeginChrThread(0x109, 3, 0, 15)
    Sleep(200)
    BeginChrThread(0x105, 3, 0, 15)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    Sleep(500)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    OP_4C(0x8, 0xFF)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("m4100", 0, 0, 0)
    IdleLoop()
    Jump("loc_3598")

    label("loc_3598")

    Return()

    # Function_14_32D7 end

    def Function_15_3599(): pass

    label("Function_15_3599")

    OP_93(0xFE, 0x2D, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    Return()

    # Function_15_3599 end

    def Function_16_35B0(): pass

    label("Function_16_35B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    StopEffect(0x0, 0x0)
    LoadEffect(0x1, "event/ev11008.eff")
    ClearMapObjFlags(0x6, 0x4)
    SoundLoad(996)
    OP_68(-26540, 9100, 195770, 0)
    MoveCamera(30, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x8, -25500, 8000, 194000, 225)
    OP_93(0x8, 0xE1, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(996, 2, 30, 0)
    FadeToBright(1000, 0)
    Sound(833, 0, 40, 0)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, -22000, 8500, 197270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()
    StopSound(996, 4000, 20)
    BeginChrThread(0x8, 3, 0, 17)
    Sleep(1000)

    #C0042
    ChrTalk(
        0x8,
        "#5P什、什么！？\x02",
    )

    WaitChrThread(0x8, 3)
    CloseMessageWindow()
    OP_64(0x8)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 19)
    WaitChrThread(0x8, 3)

    #C0043
    ChrTalk(
        0x8,
        "#5P这、这到底是……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0044
    ChrTalk(
        0x8,
        (
            "#4S#5P喂——！\x01",
            "你们没事吧！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0045
    ChrTalk(
        0x8,
        "#4S#5P如果听得到就回答我！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(300)

    #C0046
    ChrTalk(
        0x8,
        (
            "#5P不、不行……\x01",
            "声音好像传不过去……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "#5P必、必须要赶快通知大家！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x8, 3, 0, 20)
    WaitChrThread(0x8, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x8)
    SetScenarioFlags(0x22, 1)
    NewScene("m4100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_35B0 end

    def Function_17_37EE(): pass

    label("Function_17_37EE")

    OP_9B(0x0, 0xFE, 0xF, 0x7D0, 0x1388, 0x1)
    BeginChrThread(0xFE, 2, 0, 18)
    OP_9B(0x1, 0xFE, 0x1E, 0x7D0, 0x1388, 0x1)
    OP_9C(0xFE, 0xFFFFFA24, 0x0, 0x0, 0xFA, 0x3E8)
    OP_9C(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x32, 0x3E8)
    WaitChrThread(0xFE, 2)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    Return()

    # Function_17_37EE end

    def Function_18_3854(): pass

    label("Function_18_3854")

    Sleep(50)
    OP_93(0xFE, 0x5A, 0x3E8)
    Return()

    # Function_18_3854 end

    def Function_19_385F(): pass

    label("Function_19_385F")

    OP_9B(0x0, 0xFE, 0x159, 0x7D0, 0xFA0, 0x1)
    OP_68(-21150, 8600, 198420, 1000)
    MoveCamera(45, 8, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(24670, 1000)
    OP_9B(0x0, 0xFE, 0xF, 0xBB8, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x1F4, 0x7D0, 0x0)
    OP_6F(0x1)
    Return()

    # Function_19_385F end

    def Function_20_38BD(): pass

    label("Function_20_38BD")

    OP_9B(0x0, 0xFE, 0x87, 0x7D0, 0x1388, 0x1)
    OP_9C(0xFE, 0x1F4, 0x0, 0xFFFFFC18, 0xC8, 0x514)
    OP_9F(0x0, 0xFE)
    OP_68(-17810, 8600, 176550, 1800)
    MoveCamera(103, 14, 0, 1800)
    OP_6E(570, 1800)
    SetCameraDistance(24170, 1800)
    OP_9F(0x1, -24060, 8000, 179360)
    OP_9F(0x1, -18830, 8000, 172310)
    OP_9F(0x1, -19580, 6190, 164770)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    OP_6F(0x1)
    Return()

    # Function_20_38BD end

    def Function_21_394B(): pass

    label("Function_21_394B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    Call(0, 25)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(71000, 6600, 117380, 0)
    MoveCamera(43, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(44310, 0)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0xB, 0x2C)
    OP_49()
    SetChrPos(0x2C, 96000, 6100, 116000, 270)
    OP_D5(0x2C, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_93(0x2C, 0x10E, 0x0)
    BeginChrThread(0x2C, 3, 0, 22)
    OP_68(54840, 6400, 109190, 6000)
    MoveCamera(12, 10, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(34290, 6000)
    Sound(458, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_394B end

    def Function_22_3A5F(): pass

    label("Function_22_3A5F")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 68060, 6100, 116000)
    OP_9F(0x1, 63850, 5100, 116200)
    OP_9F(0x1, 59920, 3400, 116450)
    OP_9F(0x1, 57920, 2800, 116670)
    OP_9F(0x1, 54050, 2300, 116670)
    OP_9F(0x1, 42060, 1800, 116840)
    OP_9F(0x1, 37880, 900, 117530)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_22_3A5F end

    def Function_23_3ACF(): pass

    label("Function_23_3ACF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    Call(0, 25)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(-26280, 9500, 189200, 0)
    MoveCamera(12, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(32439, 0)
    OP_68(-24060, 9100, 174650, 3000)
    MoveCamera(4, 10, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(32439, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(-24020, 3700, 131610, 0)
    MoveCamera(34, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(28620, 0)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0xB, 0x2C)
    OP_49()
    SetChrPos(0x2C, 2100, 100, 132550, 295)
    OP_D5(0x2C, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x1, 0x20)
    OP_93(0x2C, 0x127, 0x0)
    BeginChrThread(0x2C, 3, 0, 24)
    Fade(500)
    OP_0D()
    OP_6F(0x79)
    OP_68(-28890, 5300, 118180, 5500)
    MoveCamera(41, 22, 0, 5500)
    OP_6E(510, 5500)
    SetCameraDistance(45260, 5500)
    Sleep(1000)
    Sound(458, 0, 100, 0)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_3ACF end

    def Function_24_3C4C(): pass

    label("Function_24_3C4C")

    Sleep(1500)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -7160, 100, 136270)
    OP_9F(0x1, -17940, 100, 135920)
    OP_9F(0x1, -24640, 100, 131910)
    OP_9F(0x1, -31160, 100, 124060)
    OP_9F(0x1, -32000, -200, 115650)
    OP_9F(0x1, -32000, -800, 112000)
    OP_9F(0x1, -32000, -800, 100000)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_24_3C4C end

    def Function_25_3CBF(): pass

    label("Function_25_3CBF")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Return()

    # Function_25_3CBF end

    def Function_26_3CD4(): pass

    label("Function_26_3CD4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    Call(0, 25)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(480, 600, 7510, 0)
    MoveCamera(19, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(34550, 0)
    OP_68(1970, 600, -2920, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(33700, 5000)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0xB, 0x2C)
    OP_49()
    SetChrPos(0x2C, -13140, 200, 38660, 135)
    OP_D5(0x2C, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x1, 0x20)
    OP_93(0x2C, 0x87, 0x0)
    BeginChrThread(0x2C, 3, 0, 27)
    Sound(458, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    MoveCamera(60, 24, 0, 4000)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_3CD4 end

    def Function_27_3DF1(): pass

    label("Function_27_3DF1")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13140, 200, 38660)
    OP_9F(0x1, -6650, 200, 32140)
    OP_9F(0x1, -1380, 200, 24520)
    OP_9F(0x1, -390, 200, 17010)
    OP_9F(0x1, -500, 200, -6130)
    OP_9F(0x1, -550, 400, -19760)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_27_3DF1 end

    def Function_28_3E53(): pass

    label("Function_28_3E53")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    LoadChrToIndex("chr/ch31251.itc", 0x23)
    LoadChrToIndex("chr/ch31252.itc", 0x24)
    LoadChrToIndex("chr/ch31253.itc", 0x25)
    LoadChrToIndex("apl/ch50515.itc", 0x26)
    LoadChrToIndex("chr/ch41950.itc", 0x32)
    LoadChrToIndex("chr/ch42057.itc", 0x33)
    LoadChrToIndex("chr/ch03450.itc", 0x28)
    LoadEffect(0x0, "battle\\sc008002.eff")
    LoadEffect(0x1, "event\\ev14014.eff")
    LoadEffect(0x2, "battle\\sp003000.eff")
    LoadEffect(0x3, "battle\\sc008100.eff")
    LoadEffect(0x4, "battle/cr414000.eff")
    LoadEffect(0x5, "event/ev14001.eff")
    LoadEffect(0x6, "event/ev14002.eff")
    SoundLoad(469)
    SoundLoad(868)
    SoundLoad(577)
    SoundLoad(586)
    SoundLoad(861)
    SoundLoad(865)
    SoundLoad(866)
    SoundLoad(869)
    SoundLoad(3953)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x32)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x32)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x1)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x33)
    SetChrSubChip(0x19, 0x1)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0xC, 0x2D)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetMapObjFrame(0xC, "mark01", 0x0, 0x1)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0xD, 0x2E)
    OP_49()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "mark01", 0x0, 0x1)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0x2F, 0x80)
    OP_78(0xE, 0x2F)
    OP_49()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    SetMapObjFrame(0xE, "mark01", 0x0, 0x1)
    OP_74(0xE, 0x1E)
    OP_71(0xE, 0x79, 0xB4, 0x0, 0x20)
    OP_F3(100000)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x18, 2350, 5250, 147800, 225)
    SetChrPos(0x19, 10550, 6000, 145050, 225)
    SetChrPos(0x2D, 0, 250, -10000, 0)
    SetChrPos(0x2E, 0, 250, -20000, 0)
    SetChrPos(0x2F, 0, 250, -30000, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K一小时前──",
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(500)
    OP_68(-410, 1500, -5380, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(28000, 0)
    OP_68(-10670, 1500, 35200, 16000)
    MoveCamera(5, 14, 0, 16000)
    SetCameraDistance(36000, 16000)
    BeginChrThread(0x2D, 3, 0, 29)
    BeginChrThread(0x2E, 3, 0, 29)
    BeginChrThread(0x2F, 3, 0, 29)
    PlayBGM("ed7566", 0)
    Sound(465, 0, 100, 0)
    BeginChrThread(0x32, 1, 0, 39)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(867, 0, 100, 0)
    SetMessageWindowPos(270, 140, -1, -1)
    SetChrName("通讯联络的声音")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里是司令部……\x01",
            "通知第三中队。\x05\x02",
        )
    )

    Sleep(6500)
    Sound(471, 0, 100, 0)
    SetChrName("通讯联络的声音")

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "武装集团的规模不明。\x05\x02",
        )
    )

    Sleep(6000)
    OP_57(0x0)
    OP_5A()
    Sound(457, 0, 100, 0)
    Fade(500)
    OP_68(-22250, 1500, 48650, 0)
    MoveCamera(95, 15, 0, 0)
    SetCameraDistance(34000, 0)
    OP_68(-36150, 1500, 70550, 10000)
    MoveCamera(35, 15, 0, 15500)
    SetCameraDistance(35000, 15500)
    OP_0D()
    SetChrName("通讯联络的声音")

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "很可能是之前一直潜伏在\x01",
            "市内的『赤色星座』。\x05\x02",
        )
    )

    Sleep(6750)
    SetChrName("通讯联络的声音")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请尽最大努力确保\x01",
            "玛因兹居民的安全。\x07\x00\x05\x02",
        )
    )

    Sleep(6750)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(471, 0, 100, 0)
    Fade(500)
    OP_68(-32700, 400, 104650, 0)
    MoveCamera(30, 22, 0, 0)
    SetCameraDistance(22000, 0)
    OP_6B(0x2D)
    MoveCamera(45, 26, 0, 12000)
    SetCameraDistance(30000, 12000)
    OP_0D()
    Sleep(1500)
    SetMessageWindowPos(30, 30, -1, -1)
    SetChrName("通讯联络的声音")

    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第三中队收到。\x05\x02",
        )
    )

    Sleep(7000)

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "即将对武装集团展开……\x07\x00\x05\x02",
        )
    )

    WaitChrThread(0x2D, 3)
    OP_71(0xC, 0x79, 0x79, 0x0, 0x0)
    EndChrThread(0x2E, 0x3)

    def lambda_4434():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_4434)

    def lambda_4449():
        OP_D5(0xFE, 0x0, 0x1ADB0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_4449)
    OP_74(0xD, 0xF)
    OP_71(0xD, 0x5B, 0x78, 0x0, 0x8)
    EndChrThread(0x2F, 0x3)

    def lambda_4476():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_4476)
    OP_74(0xE, 0xF)
    OP_71(0xE, 0x5B, 0x78, 0x0, 0x8)
    OP_6B(0xFF)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    StopSound(469, 500, 100)
    OP_78(0xF, 0x2D)
    OP_49()
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    OP_74(0xF, 0x1E)
    StopBGM(0x0)
    Sound(200, 0, 70, 0)
    Sound(196, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0x2D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x3E8, 0x0, 0xBB8, 0x3E8)
    OP_71(0xF, 0x1, 0x3C, 0x0, 0x8)
    OP_79(0xF)
    Sound(868, 2, 100, 0)
    OP_71(0xF, 0x3D, 0x78, 0x0, 0x20)
    Sleep(1000)
    OP_0D()
    PlayBGM("ed7586", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x24A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(-11650, 1100, 136550, 0)
    MoveCamera(45, 29, 0, 0)
    SetCameraDistance(30000, 0)
    SetCameraDistance(25000, 500)
    OP_0D()
    OP_74(0xD, 0x1E)
    OP_74(0xE, 0x1E)
    SetMessageWindowPos(40, 20, -1, -1)
    SetChrName("通讯联络的声音")

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力地雷……！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("通讯联络的声音")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3A不好，整体作战部署……\x07\x00\x02",
        )
    )
    #Auto

    BeginChrThread(0x2E, 3, 0, 30)
    Sleep(1000)
    Fade(250)
    OP_78(0x10, 0x2E)
    OP_49()
    OP_D5(0x2E, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    OP_74(0x10, 0x1E)
    OP_71(0x10, 0x1, 0x3C, 0x0, 0x8)
    OP_79(0x10)
    OP_71(0x10, 0x3D, 0x78, 0x0, 0x20)
    WaitChrThread(0x2E, 3)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    MoveCamera(45, 32, 0, 3000)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xD, -11800, 600, 135700, 180)
    SetChrPos(0xE, -11800, 600, 135700, 180)
    SetChrPos(0xF, -11800, 600, 135700, 180)
    SetChrPos(0x10, -11800, 600, 135700, 180)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0xD, 3, 0, 31)
    Sleep(300)
    BeginChrThread(0xE, 3, 0, 32)
    Sleep(300)
    BeginChrThread(0xF, 3, 0, 33)
    Sleep(300)
    BeginChrThread(0x10, 3, 0, 34)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    Sound(865, 2, 90, 0)
    Sound(861, 2, 90, 0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, -12000, 0, 134900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x1, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x3, 0xF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x3E8, 0x0, 0xBB8, 0x5DC)
    Sleep(200)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    Sleep(1300)
    Sound(871, 0, 80, 0)
    StopSound(865, 500, 90)
    StopSound(861, 500, 90)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    Sleep(500)
    Fade(250)
    Sound(514, 0, 100, 0)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x26)
    SetChrSubChip(0x10, 0x0)
    OP_0D()
    Sleep(500)
    Fade(500)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x11, -23450, 750, 134000, 250)
    SetChrPos(0x12, -23450, 750, 134000, 250)
    SetChrPos(0x13, -23450, 750, 134000, 250)
    SetChrPos(0x14, -23450, 750, 134000, 250)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, 4720, 6000, 147900, 225)
    SetChrPos(0x16, 6820, 6000, 145170, 225)
    SetChrPos(0x17, 8210, 6000, 144440, 225)
    SetChrPos(0x1D, 5120, 6000, 144550, 225)
    OP_68(-21010, 1700, 135220, 0)
    MoveCamera(25, 25, -2, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    SetCameraDistance(25000, 1500)
    Sound(586, 2, 70, 0)
    Sound(577, 2, 80, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1388)
    PlayEffect(0x2, 0x1, 0xFF, 0x0, -23450, 0, 134000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_87(0x3, 0x0, 0xE, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sound(464, 0, 100, 0)
    OP_71(0xE, 0x0, 0x14, 0x0, 0x0)
    OP_79(0xE)
    BeginChrThread(0x11, 3, 0, 35)
    Sleep(300)
    BeginChrThread(0x12, 3, 0, 36)
    Sleep(300)
    StopEffect(0x1, 0x2)
    BeginChrThread(0x13, 3, 0, 37)
    Sleep(300)
    BeginChrThread(0x14, 3, 0, 38)
    Sleep(500)
    Sound(463, 0, 100, 0)
    OP_71(0xE, 0x1E, 0x32, 0x0, 0x0)
    OP_79(0xE)
    OP_74(0xE, 0x2)
    OP_71(0xE, 0x12C, 0x12A, 0x0, 0x0)
    OP_79(0xE)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    StopEffect(0x0, 0x2)
    StopSound(586, 500, 70)
    StopSound(577, 500, 80)
    Sound(866, 0, 100, 0)
    Sleep(500)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    OP_0D()
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    #N0057
    NpcTalk(
        0x1D,
        "女孩的声音",
        (
            "#35A#3953V#30W啊哈哈……\x01",
            "反应不错嘛。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_68(5200, 6900, 144650, 2000)
    MoveCamera(20, 12, 0, 2000)
    SetCameraDistance(18500, 2000)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0058
    AnonymousTalk(
        0x1D,
        (
            "呵呵……\x01",
            "好像已经有三个月没实战了呢～\x02\x03",

            "终于可以让『赤颅』\x01",
            "得到满足了¤\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0059
    ChrTalk(
        0xD,
        "呜……\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xE,
        "这、这些家伙是……！？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x1D,
        (
            "#04602F#11P扫荡作战开始，\x01",
            "首先压制到隧道一带。\x02\x03",

            "#04612F如果有人反抗，全部杀掉就好了⊥\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(290, 30, -1, -1)
    SetChrName("众猎兵")
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #A0062
    AnonymousTalk(
        0xFF,
        "#4S明白！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_25(0x364, 0x5A)
    Sleep(200)
    OP_25(0x364, 0x50)
    Sleep(200)
    OP_25(0x364, 0x46)
    Sleep(200)
    OP_25(0x364, 0x3C)
    Sleep(200)
    Sleep(200)
    Sleep(1500)
    OP_71(0xF, 0x79, 0xF0, 0x0, 0x20)
    OP_71(0x10, 0x79, 0xF0, 0x0, 0x20)
    OP_78(0x11, 0x2F)
    OP_49()
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0x79, 0xF0, 0x0, 0x20)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    PlayEffect(0x5, 0x0, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x10, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x2, 0x14, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-21010, 1000, 135220, 0)
    MoveCamera(40, 23, -5, 0)
    SetCameraDistance(24000, 0)
    OP_6E(500, 0)
    MoveCamera(45, 25, -5, 3000)
    SetCameraDistance(29000, 3000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x96, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrPos(0x2D, -35750, 0, 65550, 315)
    SetChrPos(0xD, -36550, 0, 70200, 0)
    SetChrPos(0xE, -35400, 0, 59650, 135)
    PlayEffect(0x5, 0x0, 0xD, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-36760, 1000, 70070, 0)
    MoveCamera(50, 14, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(15200, 0)
    OP_68(-36450, 1300, 65180, 6000)
    MoveCamera(58, 19, -5, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(18000, 6000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x2F, 250, 0, 2000, 70)
    SetChrPos(0xD, -1750, 0, 5650, 0)
    SetChrPos(0xE, 1500, 0, -2550, 315)
    PlayEffect(0x5, 0x0, 0xD, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-600, 1750, 8400, 0)
    MoveCamera(40, 7, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(16600, 0)
    OP_68(-500, 1750, -5000, 6000)
    MoveCamera(50, 25, -5, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(18100, 6000)
    Sleep(5000)
    StopSound(868, 1000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D5)
    OP_24(0x364)
    OP_24(0x241)
    OP_24(0x24A)
    OP_24(0x35D)
    OP_24(0x361)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_3E53 end

    def Function_29_5152(): pass

    label("Function_29_5152")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -330, 0, 18450)
    OP_9F(0x1, -1340, 0, 24860)
    OP_9F(0x1, -10950, 0, 37180)
    OP_9F(0x1, -23380, 0, 49190)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -27790, 0, 53200)
    OP_9F(0x1, -34120, 0, 61210)
    OP_9F(0x1, -34850, 0, 65540)
    OP_9F(0x1, -36260, 0, 80660)
    OP_9F(0x1, -32229, 0, 91050)
    OP_9F(0x1, -32229, -1000, 105220)
    OP_9F(0x1, -32229, -1000, 108220)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -32229, -1000, 110120)
    OP_9F(0x1, -32229, 0, 120970)
    OP_9F(0x1, -29470, 0, 127710)
    OP_9F(0x1, -20460, 0, 135510)
    OP_9F(0x1, -10260, 0, 136910)
    OP_9F(0x1, -1960, 0, 134520)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_29_5152 end

    def Function_30_5268(): pass

    label("Function_30_5268")

    Sound(869, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2E, 0x0, -500, 0, -20000, 30, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2E, 0x0, 1000, 0, -19000, 30, 40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    OP_82(0x3E8, 0x0, 0xBB8, 0x1F4)
    Sound(200, 0, 70, 0)
    Sound(196, 0, 80, 0)
    PlayEffect(0x6, 0xFF, 0x2E, 0x0, -500, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x3E8, 0x0, 0xBB8, 0x3E8)
    PlayEffect(0x6, 0xFF, 0x2E, 0x0, 1000, 0, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Return()

    # Function_30_5268 end

    def Function_31_5385(): pass

    label("Function_31_5385")


    def lambda_538A():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_538A)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0xD, 1)
    OP_95(0xD, -8350, 0, 134700, 4000, 0x0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_31_5385 end

    def Function_32_53D1(): pass

    label("Function_32_53D1")


    def lambda_53D6():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_53D6)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0xE, 1)
    OP_95(0xE, -14150, 0, 135000, 4000, 0x0)
    OP_95(0xE, -15650, 0, 137600, 4000, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x2)
    Return()

    # Function_32_53D1 end

    def Function_33_542B(): pass

    label("Function_33_542B")


    def lambda_5430():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5430)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0xF, 1)
    OP_95(0xF, -8000, 0, 133000, 4000, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x2)
    Return()

    # Function_33_542B end

    def Function_34_5471(): pass

    label("Function_34_5471")


    def lambda_5476():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5476)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x10, 1)
    OP_95(0x10, -15400, 0, 134000, 4000, 0x0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x2)
    Return()

    # Function_34_5471 end

    def Function_35_54BD(): pass

    label("Function_35_54BD")


    def lambda_54C2():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_54C2)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x11, 1)
    OP_95(0x11, -20920, 0, 132340, 4000, 0x0)
    OP_93(0x11, 0x46, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x2)
    Return()

    # Function_35_54BD end

    def Function_36_5510(): pass

    label("Function_36_5510")


    def lambda_5515():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5515)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x12, 1)
    OP_95(0x12, -25270, 0, 136260, 4000, 0x0)
    OP_93(0x12, 0x46, 0x1F4)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x2)
    Return()

    # Function_36_5510 end

    def Function_37_555D(): pass

    label("Function_37_555D")


    def lambda_5562():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5562)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x13, 1)
    OP_95(0x13, -24450, 0, 131530, 4000, 0x0)
    OP_93(0x13, 0x46, 0x1F4)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x2)
    Return()

    # Function_37_555D end

    def Function_38_55AA(): pass

    label("Function_38_55AA")


    def lambda_55AF():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_55AF)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x14, 1)
    OP_95(0x14, -26170, 0, 133270, 4000, 0x0)
    OP_93(0x14, 0x46, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x2)
    Return()

    # Function_38_55AA end

    def Function_39_55FD(): pass

    label("Function_39_55FD")

    Sound(469, 2, 20, 0)
    Sleep(100)
    OP_25(0x1D5, 0x1E)
    Sleep(100)
    OP_25(0x1D5, 0x28)
    Sleep(100)
    OP_25(0x1D5, 0x32)
    Sleep(100)
    OP_25(0x1D5, 0x3C)
    Sleep(100)
    OP_25(0x1D5, 0x46)
    Sleep(100)
    OP_25(0x1D5, 0x50)
    Sleep(100)
    OP_25(0x1D5, 0x5A)
    Sleep(100)
    OP_25(0x1D5, 0x64)
    Return()

    # Function_39_55FD end

    def Function_40_563C(): pass

    label("Function_40_563C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("monster/ch82053.itc", 0x20)
    LoadChrToIndex("apl/ch51428.itc", 0x46)
    LoadChrToIndex("apl/ch51429.itc", 0x47)
    LoadChrToIndex("chr/ch0035E.itc", 0x48)
    LoadChrToIndex("apl/ch51430.itc", 0x49)
    LoadChrToIndex("chr/ch41950.itc", 0x32)
    LoadChrToIndex("chr/ch41951.itc", 0x33)
    LoadChrToIndex("chr/ch41952.itc", 0x34)
    LoadChrToIndex("chr/ch41953.itc", 0x35)
    LoadChrToIndex("chr/ch41954.itc", 0x36)
    LoadEffect(0x0, "event/ev14020.eff")
    LoadEffect(0x1, "battle/sp003000.eff")
    LoadEffect(0x2, "battle/ms00000.eff")
    LoadEffect(0x3, "battle/btgun00.eff")
    LoadEffect(0x4, "event/ev14021.eff")
    SoundLoad(3320)
    SoundLoad(2761)
    SoundLoad(2762)
    SoundLoad(2763)
    SoundLoad(2764)
    SoundLoad(3954)
    SoundLoad(3955)
    SoundLoad(3956)
    SoundLoad(3933)
    SoundLoad(580)
    SoundLoad(291)
    SoundLoad(861)
    SoundLoad(865)
    OP_32(0xFF, 0xFF, 0x0)
    SetChrPos(0x101, -27840, 8000, 191100, 180)
    SetChrPos(0x102, -26070, 8000, 191780, 180)
    SetChrPos(0x103, -28370, 8000, 192020, 180)
    SetChrPos(0x109, -29440, 8000, 192310, 180)
    SetChrPos(0x105, -26390, 8000, 193520, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x1C, 0x46)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x15, 0x33)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x33)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x33)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x33)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x33)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x21, 0x20)
    SetChrChipByIndex(0x22, 0x1F)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x22, 0x20)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x23, 0x20)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x20)
    OP_F3(100000)
    SetChrPos(0x1C, -20150, 5250, 161000, 135)
    ClearChrFlags(0x1C, 0x4)

    def lambda_5891():
        OP_95(0x1C, -10150, 4000, 151000, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5891)
    BeginChrThread(0x1C, 3, 0, 53)
    OP_68(-20150, 5850, 161000, 0)
    MoveCamera(15, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_6B(0x1C)
    MoveCamera(10, 25, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(16000, 2000)
    OP_82(0x64, 0x0, 0xBB8, 0x7D0)
    Sound(291, 2, 80, 0)
    Sound(580, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x1C, 1)
    EndChrThread(0x1C, 0x3)
    SetChrFlags(0x1C, 0x4)
    Fade(500)
    OP_6B(0xFF)
    OP_68(-3950, 600, 134100, 0)
    MoveCamera(40, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    OP_68(-1000, 600, 134250, 1500)
    MoveCamera(45, 22, 0, 1500)
    SetCameraDistance(19750, 500)
    SetChrPos(0x15, -850, 0, 134500, 90)
    SetChrPos(0x16, -2850, 0, 134750, 90)
    SetChrPos(0x17, -2850, 0, 133250, 90)
    SetChrPos(0x18, -4850, 0, 134750, 90)
    SetChrPos(0x19, -4850, 0, 133250, 90)
    SetChrPos(0x1A, -6850, 0, 134750, 90)
    SetChrPos(0x1B, -6850, 0, 133250, 90)

    def lambda_5A05():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5A05)

    def lambda_5A1A():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5A1A)

    def lambda_5A2F():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5A2F)

    def lambda_5A44():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5A44)

    def lambda_5A59():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5A59)

    def lambda_5A6E():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5A6E)

    def lambda_5A83():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5A83)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    PlayEffect(0x1, 0x0, 0x1A, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(861, 2, 80, 0)
    WaitChrThread(0x1A, 1)
    SetChrChipByIndex(0x1A, 0x35)
    BeginChrThread(0x1A, 3, 0, 62)

    #C0063
    ChrTalk(
        0x1A,
        "#10A#5P啊……！\x02",
    )
    #Auto

    WaitChrThread(0x1B, 1)
    SetChrChipByIndex(0x1B, 0x35)
    BeginChrThread(0x1B, 3, 0, 62)

    #C0064
    ChrTalk(
        0x1B,
        "#10A#6P唔……！？\x02",
    )
    #Auto

    StopEffect(0x0, 0x2)
    OP_24(0x35D)
    StopSound(291, 500, 80)
    StopSound(580, 500, 50)
    WaitChrThread(0x15, 1)

    def lambda_5B42():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5B42)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x32)
    SetChrSubChip(0x17, 0x0)
    WaitChrThread(0x18, 1)
    SetChrChipByIndex(0x18, 0x32)
    SetChrSubChip(0x18, 0x0)
    WaitChrThread(0x19, 1)
    SetChrChipByIndex(0x19, 0x32)
    SetChrSubChip(0x19, 0x0)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5B97():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5B97)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5BBF():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_5BBF)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5BE4():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_5BE4)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5C0C():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_5C0C)
    Sleep(50)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5C34():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_5C34)
    Sleep(1000)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x16, 2)
    WaitChrThread(0x17, 2)
    WaitChrThread(0x18, 2)
    WaitChrThread(0x19, 2)

    #C0065
    ChrTalk(
        0x16,
        "#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x19,
        (
            "#4P难道……！\x01",
            "是兰道夫队长吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    #C0067
    ChrTalk(
        0x15,
        (
            "#2P散开！\x01",
            "不要聚在一起！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-3700, 600, 134450, 1500)
    MoveCamera(45, 25, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(22000, 1500)
    BeginChrThread(0x18, 3, 0, 46)
    Sleep(50)
    BeginChrThread(0x19, 3, 0, 47)
    Sleep(50)
    BeginChrThread(0x16, 3, 0, 43)
    Sleep(50)
    BeginChrThread(0x17, 3, 0, 44)
    Sleep(50)
    BeginChrThread(0x15, 3, 0, 41)
    WaitChrThread(0x15, 3)
    Sound(865, 2, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    BeginChrThread(0x15, 0, 0, 49)
    BeginChrThread(0x15, 3, 0, 50)
    WaitChrThread(0x16, 3)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x16, 3, 0, 50)
    WaitChrThread(0x18, 3)
    BeginChrThread(0x18, 0, 0, 49)
    BeginChrThread(0x18, 3, 0, 50)
    WaitChrThread(0x17, 3)
    BeginChrThread(0x17, 0, 0, 49)
    BeginChrThread(0x17, 3, 0, 50)
    WaitChrThread(0x19, 3)
    BeginChrThread(0x19, 0, 0, 49)
    BeginChrThread(0x19, 3, 0, 50)
    OP_6F(0x79)
    Sleep(1000)
    OP_25(0x361, 0x28)
    Sound(861, 2, 60, 0)
    Fade(500)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x19, 0x3)
    OP_68(-10150, 4600, 151000, 0)
    MoveCamera(45, 30, 5, 0)
    SetCameraDistance(22000, 0)
    OP_6B(0x1C)
    MoveCamera(90, 30, 0, 3000)
    SetCameraDistance(18000, 3000)
    PlayEffect(0x0, 0x0, 0x1C, 0x5, 3000, 3000, -8000, 90, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    SetChrFlags(0x1C, 0x800)
    ClearChrFlags(0x1C, 0x4)
    OP_95(0x1C, -430, 4000, 148540, 7000, 0x0)
    OP_95(0x1C, 5180, 6000, 148550, 7000, 0x0)
    StopEffect(0x0, 0x2)
    StopSound(865, 1000, 30)
    StopSound(861, 1000, 50)
    OP_95(0x1C, 9820, 6000, 144350, 7000, 0x0)
    OP_93(0x1C, 0xE1, 0x1F4)
    SetChrFlags(0x1C, 0x4)
    Sound(358, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(150)
    OP_C9(0x0, 0x80000000)

    #C0068
    ChrTalk(
        0x1C,
        "#00314F#2761V#5P#10A#30W太迟钝了……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Fade(250)
    SetChrChipByIndex(0x1C, 0x47)
    SetChrFlags(0x1C, 0x2)
    SetChrSubChip(0x1C, 0x0)
    OP_0D()
    Sound(318, 0, 100, 0)
    Sound(859, 0, 50, 0)
    OP_A1(0x1C, 0x5DC, 0x2, 0x0, 0x6)
    Sleep(100)
    OP_A0(0x1C, 1500, 0x1, 0x2)
    SetChrSubChip(0x1C, 0x3)
    PlayEffect(0x4, 0x1, 0x1C, 0x3, 0, -6500, 10500, 5, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x4, 0x2, 0x1C, 0x3, 0, -6500, 10500, -5, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    Sleep(500)
    OP_A0(0x1C, 1500, 0x4, 0x5)
    Fade(250)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x2)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    BeginChrThread(0x1C, 3, 0, 51)
    Sound(291, 2, 80, 0)
    Sound(580, 2, 50, 0)
    Sleep(1000)
    EndChrThread(0x1C, 0x3)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    Fade(500)
    ClearChrFlags(0x1C, 0x800)
    OP_6B(0xFF)
    OP_68(-3700, 600, 134450, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    TurnDirection(0x15, 0x1C, 0)
    TurnDirection(0x16, 0x1C, 0)
    TurnDirection(0x17, 0x1C, 0)
    TurnDirection(0x18, 0x1C, 0)
    TurnDirection(0x19, 0x1C, 0)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 50, 0)
    BeginChrThread(0x15, 0, 0, 49)
    BeginChrThread(0x15, 3, 0, 50)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x16, 3, 0, 50)
    BeginChrThread(0x17, 0, 0, 49)
    BeginChrThread(0x17, 3, 0, 50)
    BeginChrThread(0x18, 0, 0, 49)
    BeginChrThread(0x18, 3, 0, 50)
    BeginChrThread(0x19, 0, 0, 49)
    BeginChrThread(0x19, 3, 0, 50)
    PlayEffect(0x4, 0x0, 0xFF, 0x0, -1000, 0, 135500, 225, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 700)
    PlayEffect(0x4, 0x1, 0xFF, 0x0, -4400, 0, 138500, 225, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 400)
    OP_0D()
    OP_25(0x123, 0x14)
    OP_25(0x244, 0x14)
    OP_4B(0x15, 0x0)
    OP_4B(0x15, 0x3)
    SetChrFlags(0x15, 0x20)

    def lambda_610D():
        OP_96(0xFE, 0xFFFFFF06, 0x0, 0x2049A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_610D)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    SetChrFlags(0x16, 0x20)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x1)

    def lambda_613C():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0x21F8E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_613C)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    Sound(200, 0, 100, 0)
    Sound(833, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0x16, 0x34)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x16, 3, 0, 50)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x18, 0x3)
    SetChrFlags(0x18, 0x20)
    SetChrChipByIndex(0x18, 0x35)
    SetChrSubChip(0x18, 0x0)

    def lambda_619B():
        OP_96(0xFE, 0xFFFFE638, 0x0, 0x2130E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_619B)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    Sound(196, 0, 100, 0)
    Sleep(500)
    SetChrChipByIndex(0x18, 0x34)
    BeginChrThread(0x18, 0, 0, 49)
    BeginChrThread(0x18, 3, 0, 50)
    ClearChrFlags(0x15, 0x20)
    OP_4C(0x15, 0x0)
    OP_4C(0x15, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    PlayEffect(0x1, 0x2, 0xFF, 0x0, -3750, 0, 137850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    SetChrChipByIndex(0x16, 0x35)
    BeginChrThread(0x16, 3, 0, 62)

    #C0069
    ChrTalk(
        0x16,
        "#10A#6P哇啊啊！？\x02",
    )
    #Auto

    Sleep(1500)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x18, 0x3)
    SetChrChipByIndex(0x18, 0x35)
    BeginChrThread(0x18, 3, 0, 62)
    WaitChrThread(0x18, 3)
    OP_25(0x361, 0x32)
    OP_25(0x35D, 0x28)

    #C0070
    ChrTalk(
        0x18,
        "#6P不愧是队长……！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    TurnDirection(0x15, 0x19, 500)

    #C0071
    ChrTalk(
        0x15,
        (
            "可恶！\x01",
            "放狮兽对付他！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x19, 0x0)
    EndChrThread(0x19, 0x3)
    Sleep(300)
    OP_93(0x19, 0x5A, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x19, 0x36)
    SetChrSubChip(0x19, 0x0)
    OP_0D()
    Sound(947, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    StopEffect(0x2, 0x0)
    StopSound(865, 490, 40)
    StopSound(861, 490, 40)
    OP_24(0x123)
    OP_24(0x244)
    Sound(948, 0, 100, 0)
    Fade(500)
    OP_68(9820, 6600, 144350, 0)
    MoveCamera(80, 15, 5, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x21, 21700, 10000, 144400, 270)
    SetChrPos(0x22, -3450, 4000, 149200, 90)
    SetChrPos(0x23, 5640, 10000, 153370, 134)
    SetChrPos(0x24, 9200, 10000, 153110, 180)
    BeginChrThread(0x21, 3, 0, 58)
    BeginChrThread(0x22, 3, 0, 59)
    BeginChrThread(0x23, 3, 0, 60)
    BeginChrThread(0x24, 3, 0, 61)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    BeginChrThread(0x1C, 3, 0, 51)
    Sound(291, 2, 80, 0)
    Sound(580, 2, 50, 0)
    Sleep(500)
    StopSound(291, 500, 80)
    StopSound(580, 500, 50)
    EndChrThread(0x1C, 0x3)

    def lambda_63DF():

        label("loc_63DF")

        TurnDirection(0xFE, 0x21, 1000)
        Yield()
        Jump("loc_63DF")

    QueueWorkItem2(0x1C, 2, lambda_63DF)
    WaitChrThread(0x21, 3)
    OP_68(8450, 6600, 145850, 500)
    MoveCamera(60, 30, -5, 500)
    OP_6E(500, 500)
    SetCameraDistance(20000, 500)
    Sound(844, 0, 50, 0)
    SetChrChipByIndex(0x1C, 0x49)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0x21FC, 0x1770, 0x23F32, 0x3E8, 0x1770)
    SetChrSubChip(0x1C, 0x0)
    Sound(62, 0, 100, 0)

    def lambda_6452():

        label("loc_6452")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_6452")

    QueueWorkItem2(0x21, 2, lambda_6452)
    BeginChrThread(0x21, 0, 0, 57)
    EndChrThread(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)

    def lambda_6476():

        label("loc_6476")

        TurnDirection(0xFE, 0x22, 1000)
        Yield()
        Jump("loc_6476")

    QueueWorkItem2(0x1C, 2, lambda_6476)
    WaitChrThread(0x22, 3)
    OP_68(11050, 6600, 145550, 500)
    MoveCamera(355, 28, -5, 500)
    OP_6E(500, 500)
    SetCameraDistance(20000, 500)
    Sound(844, 0, 70, 0)
    SetChrChipByIndex(0x1C, 0x49)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0x2D82, 0x186A, 0x241F8, 0x3E8, 0x1770)
    SetChrSubChip(0x1C, 0x0)
    Sound(63, 0, 100, 0)

    def lambda_64E9():

        label("loc_64E9")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_64E9")

    QueueWorkItem2(0x22, 2, lambda_64E9)
    BeginChrThread(0x22, 0, 0, 57)
    EndChrThread(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)

    def lambda_650D():

        label("loc_650D")

        TurnDirection(0xFE, 0x23, 1000)
        Yield()
        Jump("loc_650D")

    QueueWorkItem2(0x1C, 2, lambda_650D)
    WaitChrThread(0x23, 3)
    OP_68(10400, 7500, 146150, 500)
    MoveCamera(60, 28, 10, 500)
    OP_6E(500, 500)
    SetCameraDistance(20000, 500)
    Sound(844, 0, 70, 0)
    SetChrChipByIndex(0x1C, 0x49)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0x30A2, 0x1770, 0x23988, 0x3E8, 0x1770)
    SetChrSubChip(0x1C, 0x0)
    Sound(62, 0, 100, 0)

    def lambda_6580():

        label("loc_6580")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_6580")

    QueueWorkItem2(0x23, 2, lambda_6580)
    BeginChrThread(0x23, 0, 0, 57)
    EndChrThread(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)

    def lambda_65A4():

        label("loc_65A4")

        TurnDirection(0xFE, 0x24, 1000)
        Yield()
        Jump("loc_65A4")

    QueueWorkItem2(0x1C, 2, lambda_65A4)
    WaitChrThread(0x24, 3)
    OP_68(14150, 6600, 145450, 500)
    MoveCamera(335, 21, -5, 500)
    OP_6E(500, 500)
    SetCameraDistance(19000, 500)
    Sound(844, 0, 70, 0)
    SetChrChipByIndex(0x1C, 0x49)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0x413C, 0x1770, 0x233DE, 0x3E8, 0x1770)
    SetChrSubChip(0x1C, 0x0)
    Sound(63, 0, 100, 0)

    def lambda_6617():

        label("loc_6617")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_6617")

    QueueWorkItem2(0x24, 2, lambda_6617)
    BeginChrThread(0x24, 0, 0, 57)
    Sleep(150)
    OP_C9(0x0, 0x80000000)

    #C0072
    ChrTalk(
        0x1C,
        "#00312F#2762V#12P#22A#30W哈……这有什么用。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    EndChrThread(0x1C, 0x2)
    EndChrThread(0x21, 0x2)
    EndChrThread(0x22, 0x2)
    EndChrThread(0x23, 0x2)
    EndChrThread(0x24, 0x2)
    SetCameraDistance(16000, 100)
    Sound(358, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrFlags(0x1C, 0x20)
    SetChrSubChip(0x1C, 0x1)

    def lambda_66A4():
        OP_96(0xFE, 0x3746, 0x1770, 0x236FE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_66A4)
    Sleep(100)
    EndChrThread(0x1C, 0x1)
    ClearChrFlags(0x1C, 0x20)
    EndChrThread(0x21, 0x0)
    EndChrThread(0x22, 0x0)
    EndChrThread(0x23, 0x0)
    EndChrThread(0x24, 0x0)
    OP_24(0x244)
    OP_24(0x123)
    OP_24(0x35D)
    OP_24(0x361)
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xFFFFFFFF, 0x30200020, "", 0x30000300, 0x0, 0x0, 0x0, 0x30082000, 0x30082000, 0x30082000, 0x30082000, 0x0, 0x0, 0x0, 0x0, 0x24A, 0x8)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04602.itp")
    OP_D7(0x0)
    OP_D7(0x10)
    OP_D7(0x11)
    OP_D7(0x12)
    OP_D7(0x13)
    OP_D7(0x14)
    OP_D7(0x15)
    OP_D7(0x16)
    OP_D7(0x17)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("monster/ch82053.itc", 0x20)
    LoadChrToIndex("apl/ch51428.itc", 0x46)
    LoadChrToIndex("chr/ch0035E.itc", 0x47)
    LoadChrToIndex("chr/ch0035C.itc", 0x48)
    LoadChrToIndex("apl/ch51431.itc", 0x49)
    LoadChrToIndex("apl/ch51437.itc", 0x4A)
    LoadChrToIndex("apl/ch51430.itc", 0x4B)
    LoadChrToIndex("apl/ch51432.itc", 0x4C)
    LoadChrToIndex("chr/ch03450.itc", 0x28)
    LoadChrToIndex("chr/ch03451.itc", 0x29)
    LoadChrToIndex("chr/ch03452.itc", 0x2A)
    LoadChrToIndex("chr/ch0345F.itc", 0x2B)
    LoadChrToIndex("apl/ch51442.itc", 0x2C)
    LoadChrToIndex("apl/ch51433.itc", 0x2D)
    LoadChrToIndex("chr/ch41950.itc", 0x32)
    LoadChrToIndex("chr/ch41951.itc", 0x33)
    LoadChrToIndex("chr/ch41952.itc", 0x34)
    LoadChrToIndex("chr/ch41953.itc", 0x35)
    LoadChrToIndex("chr/ch00050.itc", 0x37)
    LoadChrToIndex("chr/ch00051.itc", 0x38)
    LoadChrToIndex("chr/ch00052.itc", 0x39)
    LoadChrToIndex("chr/ch00150.itc", 0x3C)
    LoadChrToIndex("chr/ch00151.itc", 0x3D)
    LoadChrToIndex("chr/ch00152.itc", 0x3E)
    LoadChrToIndex("chr/ch00250.itc", 0x41)
    LoadChrToIndex("chr/ch00251.itc", 0x42)
    LoadChrToIndex("chr/ch00254.itc", 0x43)
    LoadChrToIndex("chr/ch02950.itc", 0x50)
    LoadChrToIndex("chr/ch02951.itc", 0x51)
    LoadChrToIndex("chr/ch02952.itc", 0x52)
    LoadChrToIndex("chr/ch03050.itc", 0x55)
    LoadChrToIndex("chr/ch03051.itc", 0x56)
    LoadChrToIndex("apl/ch51436.itc", 0x57)
    LoadEffect(0x0, "battle/mg040_00.eff")
    LoadEffect(0x1, "battle/sp003000.eff")
    LoadEffect(0x2, "battle/ms00000.eff")
    LoadEffect(0x3, "battle/btgun00.eff")
    LoadEffect(0x4, "event/ev14021.eff")
    LoadEffect(0x5, "event/ev14020.eff")
    LoadEffect(0x6, "battle/mgaria0.eff")
    LoadEffect(0x7, "battle/mgaria1.eff")
    LoadEffect(0x8, "battle/sc003200.eff")
    LoadEffect(0x9, "event/eva01_01.eff")
    LoadEffect(0xA, "event/ev606_00.eff")
    LoadEffect(0xF, "battle/sc003203.eff")
    SoundLoad(580)
    SoundLoad(291)
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(870)
    SoundLoad(875)
    SoundLoad(863)
    SoundLoad(196)
    SoundLoad(566)
    SetMapObjFlags(0x5, 0x1000)
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x30)
    SetChrChipByIndex(0x15, 0x32)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x3)
    SetChrChipByIndex(0x17, 0x32)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x35)
    SetChrSubChip(0x18, 0x3)
    SetChrChipByIndex(0x19, 0x32)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x35)
    SetChrSubChip(0x1A, 0x3)
    SetChrChipByIndex(0x1B, 0x35)
    SetChrSubChip(0x1B, 0x3)
    SetChrChipByIndex(0x1D, 0x29)
    SetChrSubChip(0x1D, 0x1)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x21, 0x20)
    SetChrSubChip(0x21, 0x1)
    SetChrChipByIndex(0x22, 0x20)
    SetChrSubChip(0x22, 0x1)
    SetChrChipByIndex(0x23, 0x20)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0x0)
    SetChrChipByIndex(0x30, 0x4C)
    SetChrSubChip(0x30, 0x0)
    SetChrFlags(0x30, 0x20)
    SetChrFlags(0x30, 0x2)
    SetChrFlags(0x30, 0x8000)
    ClearChrFlags(0x30, 0x1)
    SetChrPos(0x30, -21250, -200, 135950, 0)
    SetChrChipByIndex(0x31, 0x4C)
    SetChrSubChip(0x31, 0x0)
    SetChrFlags(0x31, 0x20)
    SetChrFlags(0x31, 0x2)
    SetChrFlags(0x31, 0x8000)
    ClearChrFlags(0x31, 0x1)
    SetChrPos(0x31, -20000, 1000, 137600, 0)
    OP_52(0x31, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F3(100000)
    SetChrPos(0x1C, 8100, 6000, 147450, 300)

    def lambda_6A78():
        OP_96(0xFE, 0x14B4, 0x1770, 0x24252, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6A78)
    OP_68(9000, 6600, 147400, 0)
    MoveCamera(55, 15, 5, 0)
    OP_6E(600, 0)
    SetCameraDistance(14300, 0)
    SetCameraDistance(16300, 500)
    Sound(251, 0, 100, 0)
    FadeToBright(500, 16777215)
    OP_0D()
    WaitChrThread(0x1C, 1)
    Sound(358, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_A0(0x1C, 2000, 0x31, 0x37)
    Sleep(300)
    Sound(288, 0, 100, 0)
    Sound(540, 0, 80, 0)
    OP_A0(0x1C, 6000, 0x38, 0x3C)
    Sound(948, 0, 100, 0)
    PlayEffect(0x8, 0x0, 0x21, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x1, 0x22, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x2, 0x23, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x3, 0x24, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(289, 0, 100, 0)
    Sound(514, 0, 100, 0)
    Sound(833, 0, 70, 0)
    Sleep(500)

    def lambda_6BFD():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_6BFD)

    def lambda_6C0E():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 3, lambda_6C0E)

    def lambda_6C1F():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_6C1F)

    def lambda_6C30():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_6C30)
    WaitChrThread(0x21, 3)
    WaitChrThread(0x22, 3)
    WaitChrThread(0x23, 3)
    WaitChrThread(0x24, 3)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    Sleep(1000)
    Fade(500)
    TurnDirection(0x15, 0x1C, 0)
    TurnDirection(0x17, 0x1C, 0)
    TurnDirection(0x19, 0x1C, 0)
    OP_68(-3700, 600, 134450, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    #C0073
    ChrTalk(
        0x17,
        "#11P哦哦……！\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x19,
        "#5P赤、赤色死神……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x19, 500)

    #C0075
    ChrTalk(
        0x15,
        (
            "不要被他压倒！\x01",
            "发动连续攻击干掉他！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x0, 0x1F4)
    SetChrChipByIndex(0x15, 0x34)
    BeginChrThread(0x15, 3, 0, 50)
    Sound(865, 2, 60, 0)
    OP_68(-7750, 600, 136150, 2000)
    MoveCamera(45, 25, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(20000, 2000)
    SetChrChipByIndex(0x19, 0x33)

    def lambda_6D57():
        OP_95(0xFE, -14850, 0, 140200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6D57)
    Sleep(100)
    SetChrChipByIndex(0x17, 0x33)

    def lambda_6D78():
        OP_95(0xFE, -14850, 10, 139000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6D78)
    OP_6F(0x79)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x19, 0x1)
    Fade(500)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    StopSound(865, 500, 60)
    SetChrPos(0x17, -11400, 0, 137850, 275)
    SetChrPos(0x19, -13600, 0, 137850, 275)
    SetChrPos(0x15, -10600, 0, 135600, 275)
    OP_68(-20000, 5000, 152050, 0)
    MoveCamera(55, 30, -5, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(-19450, 2000, 145100, 4000)
    MoveCamera(60, 30, -10, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(20750, 4000)
    ClearChrFlags(0x1C, 0x20)
    ClearChrFlags(0x1C, 0x2)
    SetChrPos(0x1C, -15900, 4040, 156150, 230)
    SetChrChipByIndex(0x1C, 0x46)
    OP_95(0x1C, -20000, 4000, 152050, 7000, 0x0)
    OP_93(0x1C, 0xB4, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x1388)
    SetChrChipByIndex(0x1C, 0x47)
    BeginChrThread(0x1C, 3, 0, 51)
    Sound(291, 2, 80, 0)
    Sound(580, 2, 50, 0)
    Sound(861, 2, 50, 0)
    PlayEffect(0x1, 0x0, 0x17, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x19, 3, 0, 48)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 45)
    Sleep(500)
    BeginChrThread(0x15, 3, 0, 42)
    WaitChrThread(0x19, 3)
    SetChrChipByIndex(0x19, 0x34)
    BeginChrThread(0x19, 0, 0, 49)
    BeginChrThread(0x19, 3, 0, 50)
    WaitChrThread(0x17, 3)
    SetChrChipByIndex(0x17, 0x34)
    BeginChrThread(0x17, 0, 0, 49)
    BeginChrThread(0x17, 3, 0, 50)
    WaitChrThread(0x15, 3)
    SetChrChipByIndex(0x15, 0x34)
    BeginChrThread(0x15, 0, 0, 49)
    BeginChrThread(0x15, 3, 0, 50)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x19, 0x3)
    SetChrChipByIndex(0x19, 0x35)
    BeginChrThread(0x19, 3, 0, 62)
    Sleep(500)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    SetChrChipByIndex(0x17, 0x35)
    BeginChrThread(0x17, 3, 0, 62)
    OP_6F(0x79)
    Sleep(1000)
    OP_82(0x0, 0x0, 0xBB8, 0x0)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    SetChrChipByIndex(0x15, 0x35)
    SetChrSubChip(0x15, 0x3)
    StopSound(291, 300, 80)
    StopSound(580, 300, 50)
    OP_24(0x35D)
    EndChrThread(0x1C, 0x3)
    StopEffect(0x0, 0x0)
    Fade(500)
    SetChrPos(0x101, -28250, 8000, 190850, 180)
    SetChrPos(0x102, -29000, 8000, 191650, 180)
    SetChrPos(0x103, -26500, 8000, 191250, 180)
    SetChrPos(0x109, -26600, 8000, 192950, 180)
    SetChrPos(0x105, -27900, 8000, 193650, 180)
    OP_68(-27850, 8600, 188350, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    OP_68(-27000, 8600, 192650, 3000)
    MoveCamera(50, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(19500, 3000)
    OP_0D()
    Sound(863, 2, 80, 0)
    OP_6F(0x79)

    #C0076
    ChrTalk(
        0x101,
        "#00011F#5P好、好厉害……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        "#00108F#5P压、压倒性的优势啊……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x103,
        "#00206F#5P太惊人了……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x109,
        (
            "#10111F#5P那才是兰迪前辈\x01",
            "真正的战斗能力吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x105,
        (
            "#10306F#5P哎呀呀，看样子，\x01",
            "似乎不需要我们帮忙了呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x105,
        (
            "#10301F#5P不，\x01",
            "好像有点危险了。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00007F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    StopSound(863, 1000, 80)
    Fade(500)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    OP_68(-20000, 4600, 152050, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(-20000, 4600, 152050, 1000)
    MoveCamera(50, 30, 0, 1000)
    OP_6E(500, 1000)
    SetCameraDistance(14750, 1000)
    SetChrPos(0x1D, 4540, 10000, 165890, 225)
    Sound(291, 2, 100, 0)
    Sound(580, 2, 50, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    SetChrChipByIndex(0x1C, 0x47)
    BeginChrThread(0x1C, 3, 0, 51)
    OP_0D()
    OP_6F(0x79)
    StopSound(291, 700, 100)
    StopSound(580, 700, 50)
    EndChrThread(0x1C, 0x3)
    OP_C9(0x0, 0x80000000)

    #N0083
    NpcTalk(
        0x1D,
        "女孩的声音",
        (
            "#3954V#6P#25A#30W啊哈哈！\x01",
            "你状态绝佳嘛，兰迪哥！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1C, 0x1D, 500)

    #C0084
    ChrTalk(
        0x1C,
        "#00311F#2763V#6P#15A#30W……谢莉吗！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_6B(0x1C)
    MoveCamera(40, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15750, 3000)
    ClearChrFlags(0x1C, 0x4)
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x4, 0x0, 0xFF, 0x0, -18400, 4000, 154350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1100)
    Sleep(100)
    Sound(200, 0, 80, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    SetChrChipByIndex(0x1C, 0x4B)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0xFFFFAAA6, 0x9A6, 0x245C2, 0x3E8, 0x1B58)
    SetChrSubChip(0x1C, 0x0)
    PlayEffect(0x4, 0x1, 0xFF, 0x0, -21750, 3000, 149950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1100)
    Sleep(100)
    Sound(196, 0, 80, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    OP_93(0x1C, 0x13B, 0x3E8)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0xFFFFB758, 0x5D2, 0x23EB0, 0x3E8, 0x1B58)
    SetChrSubChip(0x1C, 0x0)
    Sound(580, 2, 70, 0)
    Sound(291, 2, 70, 0)
    Sound(861, 2, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    PlayEffect(0x1, 0x2, 0x1C, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x1C, 0x46)
    OP_95(0x1C, -19500, 0, 137600, 7000, 0x0)
    WaitChrThread(0x1C, 1)
    SetChrFlags(0x1C, 0x4)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopSound(580, 700, 80)
    StopSound(291, 700, 60)
    OP_24(0x35D)
    OP_82(0x0, 0x0, 0xBB8, 0x0)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x1C, 0x47)
    TurnDirection(0x1C, 0x1D, 500)
    OP_6B(0xFF)
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(-16100, 7300, 151850, 0)
    MoveCamera(30, 20, -5, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(15500, 1000)
    OP_93(0x1C, 0xA, 0x0)
    SetChrPos(0x1D, -16100, 10700, 151850, 210)
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1D, 0x2B)
    SetChrSubChip(0x1D, 0x1)
    Sound(844, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFC11C, 0x1A2C, 0x2512A, 0x3E8, 0x2710)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    Sound(326, 0, 100, 0)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    OP_0D()
    OP_6F(0x79)

    #C0085
    ChrTalk(
        0x1D,
        (
            "#04612F#5P嗯嗯，兰迪哥\x01",
            "就是要这样才对！\x02\x03",

            "#04602F虽然不是谢莉喜欢的类型，\x01",
            "但真是很帅呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-19500, 1000, 137600, 1500)
    MoveCamera(65, 20, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(16000, 1500)
    OP_6F(0x79)

    #C0086
    ChrTalk(
        0x1C,
        (
            "#00311F#12P闭嘴……小丫头。\x02\x03",

            "我可不想被你这种\x01",
            "食人猛虎喜欢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1D,
        (
            "#04612F#6P呵呵，好无情啊！\x02\x03",

            "#04602F不过，机会难得，\x01",
            "就让我再开心一下吧！\x02",
        )
    )

    CloseMessageWindow()
    Sound(291, 2, 100, 0)
    Sound(580, 2, 70, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    SetChrChipByIndex(0x1C, 0x47)
    BeginChrThread(0x1C, 3, 0, 52)

    def lambda_76B2():

        label("loc_76B2")

        TurnDirection(0xFE, 0x1D, 300)
        Yield()
        Jump("loc_76B2")

    QueueWorkItem2(0x1C, 2, lambda_76B2)
    Sleep(1000)
    Fade(500)
    EndChrThread(0x1C, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    OP_68(-16100, 7300, 151850, 0)
    MoveCamera(60, 30, -5, 0)
    OP_6E(500, 0)
    SetCameraDistance(15700, 0)
    OP_6B(0x1D)
    MoveCamera(70, 30, -5, 3000)
    SetChrFlags(0x1D, 0x800)
    PlayEffect(0x5, 0x0, 0x1D, 0x5, 3000, 3000, -8000, 90, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x1D, 0x29)
    OP_95(0x1D, -15400, 6700, 148050, 10000, 0x0)
    OP_95(0x1D, -14000, 6700, 145400, 10000, 0x0)
    OP_82(0x0, 0x0, 0xBB8, 0x0)
    SetChrChipByIndex(0x1D, 0x2B)
    SetChrSubChip(0x1D, 0x1)
    Sound(844, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFD954, 0xFA0, 0x230BE, 0x3E8, 0x2710)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    StopSound(291, 700, 80)
    StopSound(580, 700, 40)
    StopEffect(0x0, 0x2)
    OP_6B(0xFF)
    OP_68(-16980, 1100, 137980, 750)
    MoveCamera(25, 26, 0, 750)
    SetCameraDistance(18000, 750)
    SetChrFlags(0x1D, 0x2)
    SetChrSubChip(0x1D, 0xE)
    Sound(844, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFC68A, 0x0, 0x21BCE, 0x3E8, 0x1388)
    SetChrSubChip(0x1D, 0x6)
    Sleep(100)
    ClearChrFlags(0x1D, 0x2)
    Sound(326, 0, 100, 0)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    TurnDirection(0x1D, 0x1C, 0)
    ClearChrFlags(0x1D, 0x800)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x1C, 0x2)
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x1D, 0x2A)
    SetChrSubChip(0x1D, 0x0)
    Sleep(50)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x32, 1, 0, 69)
    BeginChrThread(0x1D, 3, 0, 63)
    Sleep(100)
    EndChrThread(0x1D, 0x3)
    SetChrSubChip(0x1D, 0x3)
    OP_68(-18900, 1190, 137700, 500)
    SetCameraDistance(14670, 500)
    Sound(250, 0, 100, 0)
    SetChrFlags(0x1D, 0x20)
    OP_9A(0x1D, 0x1C, 0x6A4, 0x4E20, 0x0)
    ClearChrFlags(0x1D, 0x20)
    Sound(875, 2, 90, 0)
    OP_25(0x366, 0x50)
    SetChrChipByIndex(0x1D, 0x2C)
    BeginChrThread(0x1D, 2, 0, 65)
    Fade(250)
    Sound(566, 0, 80, 0)
    Sound(372, 0, 80, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0xFA)
    SetChrChipByIndex(0x1C, 0x49)
    SetChrFlags(0x1C, 0x2)
    OP_A0(0x1C, 2000, 0x0, 0x1)
    BeginChrThread(0x1C, 2, 0, 54)

    def lambda_7909():

        label("loc_7909")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_7909")

    QueueWorkItem2(0x1C, 3, lambda_7909)
    Sleep(50)

    def lambda_792A():

        label("loc_792A")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_792A")

    QueueWorkItem2(0x1D, 3, lambda_792A)
    OP_0D()

    #C0088
    ChrTalk(
        0x1C,
        "#00310F#6P唔……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x1D,
        (
            "#04604F#11P呵呵……\x01",
            "果然还是有点生锈了啊。\x02\x03",

            "#04611F差不多也快到极限了吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x1C,
        (
            "#00307F#6P『赤颅』……\x01",
            "你已经可以完全掌控了吗……唔！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x1D,
        (
            "#04609F#11P嘻嘻，我早已不是当年\x01",
            "受兰迪哥指导的谢莉啦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0092
    ChrTalk(
        0x1D,
        "#04602F#11P#23A#4S如果还不明白，就亲身体会吧！\x02",
    )
    #Auto

    CloseMessageWindow()
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1D, 0x20)
    OP_68(-19300, 1190, 137780, 1500)

    def lambda_7A8A():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7A8A)

    def lambda_7A9F():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7A9F)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1D, 1)
    Sleep(500)
    OP_68(-19700, 1190, 137860, 1500)

    def lambda_7AD0():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7AD0)

    def lambda_7AE5():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7AE5)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1D, 1)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    #Sound(3920, 255, 90, 0)    #voice#Shirley
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    #C0093
    ChrTalk(
        0x1D,
        (
            "#04612F#5S#11P#26A啊哈哈！\x01",
            "断掉吧！！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1D, 0x3)
    SetChrFlags(0x1C, 0x800)
    SetChrFlags(0x1D, 0x800)
    Sound(874, 0, 100, 0)

    def lambda_7B65():
        OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7B65)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1C, 0x2)
    SetChrChipByIndex(0x1D, 0x2A)
    OP_A0(0x1D, 3000, 0x0, 0x3)
    BeginChrThread(0x1D, 3, 0, 64)
    StopSound(870, 500, 80)
    StopSound(875, 500, 90)
    Sound(873, 0, 100, 0)
    OP_68(-19830, 1190, 136740, 300)
    SetCameraDistance(16000, 300)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    OP_68(-21240, 1200, 136720, 500)
    MoveCamera(63, 24, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(14000, 500)
    Sleep(100)

    def lambda_7C01():
        OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7C01)
    EndChrThread(0x1D, 0x3)
    SetChrFlags(0x1D, 0x2)
    SetChrChipByIndex(0x1D, 0x2D)
    Sound(815, 0, 100, 0)
    OP_A1(0x1D, 0xDAC, 0x2, 0x0, 0x1)
    #Sound(2764, 255, 100, 1)    #voice#Randy

    #C0094
    ChrTalk(
        0x1C,
        "#00313F#6P#10A#N呜啊……！\x02",
    )
    #Auto


    def lambda_7C56():
        OP_A0(0xFE, 2000, 0x3, 0x4)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_7C56)

    def lambda_7C63():
        OP_9D(0xFE, 0xFFFFA740, 0x0, 0x214BC, 0x2EE, 0x2710)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7C63)

    def lambda_7C80():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_7C80)
    Sound(880, 0, 80, 0)
    Sound(566, 0, 50, 0)
    ClearChrFlags(0x31, 0x80)

    def lambda_7CAA():
        OP_9D(0xFE, 0xFFFFA7B8, 0xFFFFFF38, 0x20E5E, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_7CAA)
    BeginChrThread(0x31, 3, 0, 66)
    WaitChrThread(0x1C, 1)
    Sound(811, 0, 100, 0)
    Sound(862, 0, 100, 0)
    SetChrChipByIndex(0x1C, 0x4A)
    SetChrSubChip(0x1C, 0x2)
    ClearChrFlags(0x30, 0x80)
    WaitChrThread(0x1D, 1)
    OP_C9(0x1, 0x80000000)
    WaitChrThread(0x31, 1)
    EndChrThread(0x31, 0x3)
    SetChrSubChip(0x31, 0x1)
    Sound(288, 0, 70, 0)
    OP_6F(0x79)
    ClearChrFlags(0x1D, 0x20)
    ClearChrFlags(0x1C, 0x20)
    Sleep(1000)
    Fade(250)
    SetCameraDistance(13500, 2000)
    OP_A1(0x1D, 0xDAC, 0x2, 0x2, 0x3)
    OP_0D()
    Sleep(500)

    #C0095
    ChrTalk(
        0x1D,
        (
            "#04606F#11P唔……现在的兰迪哥\x01",
            "果然无法让我满足啊。\x02\x03",

            "#04611F算啦，\x01",
            "反正我已经找到一个\x01",
            "最棒的好对手了⊥\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x1C, 0x3)
    OP_0D()
    Sleep(300)

    #C0096
    ChrTalk(
        0x1C,
        "#00311F#6P#N你……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0097
    ChrTalk(
        0x1D,
        (
            "#04604F#11P呵呵，兰迪哥\x01",
            "还是回爸爸那里\x01",
            "重新锻炼一下吧。\x02\x03",

            "#04602F只要你能恢复状态，\x01",
            "马上就可以继承『斗神』之位了。\x02\x03",

            "#04609F至于这次嘛……\x01",
            "暂且就取下你一条手臂如何？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x2)
    SetChrChipByIndex(0x1D, 0x2A)
    SetChrSubChip(0x1D, 0x0)
    Sound(358, 0, 100, 0)
    Sleep(50)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x1D, 3, 0, 63)
    BeginChrThread(0x32, 1, 0, 69)
    Sleep(500)

    #C0098
    ChrTalk(
        0x1C,
        "#00310F#6P#N呜……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    #N0099
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "#3320V#4S#10A兰迪——！！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    StopSound(870, 500, 100)
    Sound(873, 0, 100, 0)
    EndChrThread(0x1D, 0x3)
    Sound(530, 0, 100, 0)
    PlayEffect(0xA, 0xFF, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1D, 0x2B)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFBB40, 0x0, 0x21B10, 0x1F4, 0xFA0)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    OP_93(0x1D, 0x168, 0x0)
    Sound(530, 0, 100, 0)
    PlayEffect(0xA, 0xFF, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFBDCA, 0x0, 0x2146C, 0x1F4, 0xFA0)
    SetChrSubChip(0x1D, 0x0)
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0x1D, 0x28)

    #C0100
    ChrTalk(
        0x1D,
        "#04605F#12P啊。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x1C,
        "#00305F#12P#N……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    ClearChrFlags(0x1C, 0x800)
    ClearChrFlags(0x1D, 0x800)
    OP_68(-21250, 8600, 172900, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(18000, 3000)
    SetChrChipByIndex(0x101, 0x37)
    SetChrChipByIndex(0x102, 0x3E)
    SetChrChipByIndex(0x103, 0x43)
    SetChrChipByIndex(0x109, 0x50)
    SetChrPos(0x101, -21400, 7650, 170850, 180)
    SetChrPos(0x102, -22000, 8000, 172800, 180)
    SetChrPos(0x103, -20300, 8000, 173230, 180)
    SetChrPos(0x109, -20850, 7850, 171700, 180)
    BeginChrThread(0x102, 3, 0, 67)
    BeginChrThread(0x103, 3, 0, 68)
    Sleep(100)

    def lambda_80DB():
        OP_9B(0x1, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80DB)
    Sleep(50)

    def lambda_80F3():
        OP_9B(0x1, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_80F3)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x103, 3)
    EndChrThread(0x102, 0x3)
    Fade(500)
    OP_68(-16950, 600, 136300, 0)
    MoveCamera(30, 28, 0, 0)
    SetCameraDistance(17000, 0)
    OP_6B(0x1D)
    SetCameraDistance(16000, 2000)
    MoveCamera(70, 30, 0, 2000)
    OP_0D()
    OP_93(0x1D, 0x13B, 0x320)
    Sound(530, 0, 100, 0)
    PlayEffect(0xA, 0xFF, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x1D, 0x2B)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFC3D8, 0x0, 0x20DC8, 0x1F4, 0x1770)
    SetChrSubChip(0x1D, 0x0)
    OP_93(0x1D, 0x2D, 0x320)
    Sound(530, 0, 100, 0)
    PlayEffect(0xA, 0xFF, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x1D, 0x1)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFCA4A, 0x0, 0x212AA, 0x1F4, 0x1770)
    SetChrSubChip(0x1D, 0x0)
    OP_93(0x1D, 0x13B, 0x320)
    Sound(530, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFD21A, 0x0, 0x20F8A, 0x1F4, 0x1770)
    OP_93(0x1D, 0x12C, 0x320)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x1D, 0x28)
    OP_6F(0x79)

    #C0102
    ChrTalk(
        0x1D,
        (
            "#04612F#11P啊哈哈，干得不错嘛！\x02\x03",

            "#04602F很好，那就先\x01",
            "让我换换口味……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    PlayEffect(0x1, 0x0, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(865, 2, 30, 0)
    Sound(861, 2, 60, 0)
    Sound(539, 0, 100, 0)
    Sleep(420)
    Sound(539, 0, 100, 0)
    Sleep(420)
    Sound(539, 0, 100, 0)
    Sleep(160)
    StopEffect(0x0, 0x2)
    StopSound(861, 500, 60)
    StopSound(865, 500, 40)
    Fade(500)
    SetChrPos(0x101, -19400, 0, 142000, 120)
    SetChrPos(0x109, -17400, 0, 141450, 135)
    SetChrPos(0x105, -8700, 0, 133000, 295)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x109, 0x52)
    SetChrSubChip(0x109, 0x4)
    OP_6B(0xFF)
    OP_68(-19400, 1600, 142000, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(-12200, 1000, 135050, 1500)
    MoveCamera(70, 30, -5, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(15000, 1500)

    def lambda_8437():
        OP_95(0xFE, -16000, 0, 138600, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8437)
    OP_0D()
    #Sound(2014, 255, 100, 0)    #voice#Lloyd
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    #C0103
    ChrTalk(
        0x101,
        "#00007F#4S#18A#5P喔噢噢噢噢噢噢噢！\x02",
    )
    #Auto

    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x39)
    SetChrSubChip(0x101, 0x4)
    Sound(251, 0, 100, 0)

    def lambda_84A3():
        OP_9D(0xFE, 0xFFFFCE96, 0x0, 0x21214, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84A3)
    WaitChrThread(0x101, 1)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x1D, 0x2C)
    SetChrSubChip(0x1D, 0x0)
    PlayEffect(0x9, 0xFF, 0x101, 0x3, -300, 800, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(566, 0, 70, 0)
    Sound(815, 0, 100, 0)
    Sound(862, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    def lambda_852A():

        label("loc_852A")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_852A")

    QueueWorkItem2(0x101, 3, lambda_852A)
    Sleep(50)

    def lambda_854B():

        label("loc_854B")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_854B")

    QueueWorkItem2(0x1D, 3, lambda_854B)
    Sleep(500)
    Sleep(1000)

    #C0104
    ChrTalk(
        0x1C,
        "#00307F#5P罗伊德……！\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x1D,
        (
            "#04604F#11P呼……啊哈哈！\x02\x03",

            "#04602F小哥，真是没看出来，\x01",
            "你倒也挺有狠劲的嘛。\x02\x03",

            "面对谢莉这样的小姑娘，\x01",
            "居然不知羞耻地以多打一！\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#00010F#6P因为我明白你绝不是\x01",
            "可以手下留情的对手……\x02\x03",

            "#00007F我会把你当作危险度\x01",
            "为Ｓ级的通缉魔兽来对待！\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x1D,
        "#04609F#11P哈哈！这就对了！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 2, 0, 55)
    BeginChrThread(0x1D, 2, 0, 65)
    BeginChrThread(0x32, 1, 0, 70)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)

    #C0108
    ChrTalk(
        0x1C,
        (
            "#00310F#5P唔……不行！快退开！\x02\x03",

            "就算是你的旋棍，\x01",
            "也不可能防住那……\x02",
        )
    )

    CloseMessageWindow()

    #N0109
    NpcTalk(
        0x105,
        "声音",
        "#11P#N嗯，那是肯定的。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    OP_68(-8700, 600, 133000, 400)
    MoveCamera(85, 30, -10, 400)
    SetCameraDistance(15000, 400)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x1D, 0x3)
    EndChrThread(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x37)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0x55)
    SetChrSubChip(0x105, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_6F(0x79)
    SetChrChip(0x0, 0x105, 0x1E, 0xC8)
    OP_99(0x105, 0x1D, 0x5DC, 0x4E20, 0x0)
    SetChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x105, 0x1000)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x57)
    SetChrSubChip(0x105, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(500)
    PlayEffect(0xF, 0x0, 0x105, 0x3, 0, 500, -400, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(253, 0, 100, 0)

    def lambda_883E():
        OP_96(0xFE, 0xFFFFD21A, 0xFFFFFE70, 0x20F8A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_883E)
    Sound(3091, 255, 100, 0)    #voice#Lazy
    OP_68(-11000, 900, 135050, 500)
    MoveCamera(68, 25, 5, 500)
    OP_6E(500, 500)
    SetCameraDistance(18250, 500)
    Sound(873, 0, 100, 0)
    StopSound(870, 500, 100)
    StopSound(875, 500, 100)
    EndChrThread(0x1D, 0x2)
    SetChrFlags(0x1D, 0x20)
    SetChrChipByIndex(0x1D, 0x2B)
    SetChrSubChip(0x1D, 0x0)
    OP_93(0x1D, 0x13B, 0x0)
    OP_96(0x1D, 0xFFFFDDA0, 0x0, 0x20D96, 0x2710, 0x0)

    def lambda_88CA():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_88CA)
    ClearChrFlags(0x1D, 0x20)
    OP_6F(0x79)
    StopEffect(0x0, 0x2)
    SetChrChip(0x1, 0x105, 0x0, 0x0)

    #C0110
    ChrTalk(
        0x1D,
        "#04605F#11P#6A哇！？\x02",
    )
    #Auto

    CloseMessageWindow()
    SetChrChipByIndex(0x105, 0x55)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x105, 0x20)
    ClearChrFlags(0x105, 0x1000)
    SetChrPos(0x105, -11750, 0, 135050, 295)

    def lambda_893C():

        label("loc_893C")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_893C")

    QueueWorkItem2(0x105, 3, lambda_893C)
    OP_68(-8600, 1000, 135100, 1000)
    MoveCamera(50, 25, 0, 1000)
    OP_6E(500, 1000)
    SetCameraDistance(18700, 1000)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFE34A, 0x0, 0x20882, 0x1F4, 0x1B58)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFEB24, 0x0, 0x20CCE, 0x1F4, 0x1B58)
    SetChrSubChip(0x1D, 0x0)
    TurnDirection(0x1D, 0x101, 1000)
    SetChrChipByIndex(0x1D, 0x28)
    EndChrThread(0x105, 0x3)
    OP_6F(0x79)

    #C0111
    ChrTalk(
        0x105,
        (
            "#10306F#6P……哎呀呀，靠刚才那一击，\x01",
            "还是不能扭转局面啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x15, 0x33)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x20)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x20)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x15, 10600, 0, 135200, 275)
    SetChrPos(0x16, 10100, 0, 132750, 275)
    SetChrPos(0x21, 13100, 0, 133700, 275)

    #C0112
    ChrTalk(
        0x15,
        "队长！\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x16,
        "谢莉队长！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, -7850, 0, 136800, 270)
    SetChrPos(0x15, 4350, 0, 137800, 270)
    SetChrPos(0x16, 3850, 0, 135800, 270)
    SetChrPos(0x21, 6350, 0, 136800, 270)
    SetChrPos(0x101, -14350, 0, 136800, 90)
    SetChrPos(0x105, -13050, 0, 138200, 270)
    OP_68(0, 600, 136800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(-6950, 600, 136800, 2000)
    MoveCamera(45, 30, 5, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(16000, 2000)

    def lambda_8B73():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8B73)
    Sleep(50)

    def lambda_8B8B():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8B8B)
    Sleep(50)

    def lambda_8BA3():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8BA3)
    BeginChrThread(0x21, 3, 0, 56)
    BeginChrThread(0x32, 1, 0, 71)
    OP_0D()
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x1)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x34)
    SetChrSubChip(0x16, 0x1)
    WaitChrThread(0x21, 1)
    EndChrThread(0x21, 0x3)
    EndChrThread(0x32, 0x1)
    SetChrChipByIndex(0x21, 0x1E)
    SetChrSubChip(0x21, 0x0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-19050, 600, 137050, 0)
    MoveCamera(90, 22, -5, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(17000, 1500)
    SetChrChipByIndex(0x101, 0x37)
    SetChrChipByIndex(0x102, 0x3C)
    SetChrChipByIndex(0x103, 0x41)
    SetChrChipByIndex(0x109, 0x50)
    SetChrChipByIndex(0x105, 0x55)
    SetChrPos(0x102, -17850, 0, 141950, 180)
    SetChrPos(0x103, -18750, 0, 143300, 178)
    SetChrPos(0x109, -17000, 0, 140850, 180)

    def lambda_8C7F():
        OP_95(0xFE, -15250, 0, 138150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8C7F)

    def lambda_8C99():
        OP_95(0xFE, -15200, 0, 135450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8C99)

    def lambda_8CB3():
        OP_95(0xFE, -16800, 0, 136150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8CB3)

    def lambda_8CCD():
        OP_95(0xFE, -16700, 0, 137700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8CCD)
    WaitChrThread(0x105, 1)

    def lambda_8CEB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8CEB)
    WaitChrThread(0x109, 1)
    Sound(531, 0, 100, 0)

    def lambda_8D02():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8D02)
    WaitChrThread(0x102, 1)

    def lambda_8D13():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8D13)
    WaitChrThread(0x103, 1)
    Sound(805, 0, 100, 0)

    def lambda_8D2A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8D2A)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0114
    ChrTalk(
        0x1C,
        "#00306F#6P#N你们……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_68(-12400, 1150, 136830, 2000)
    MoveCamera(87, 10, -5, 2000)
    OP_6E(450, 2000)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    #C0115
    ChrTalk(
        0x1D,
        (
            "#04604F#3955V#11P#40W呵呵，ＯＫ，ＯＫ。\x02\x03",

            "#3956V既然那么想和谢莉玩，\x01",
            "我就做你们的对手吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF74)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7455", 0)

    #A0116
    AnonymousTalk(
        0x1D,
        (
            "#3933V#40W啊哈哈哈哈#1200W！#40W尽量让我#1000W\x01",
            "#4S#30W开心些吧！\x02",
        )
    )

    Sleep(2800)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    CloseMessageWindow()
    OP_24(0xF5D)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(10, 50, -1, -1)

    #A0117
    AnonymousTalk(
        0x101,
        "#00007F来了！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 150, -1, -1)

    #A0118
    AnonymousTalk(
        0x109,
        "#10107F全力迎击！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)

    def lambda_8F1E():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F1E)

    def lambda_8F33():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8F33)

    def lambda_8F48():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8F48)

    def lambda_8F5D():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8F5D)

    def lambda_8F72():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8F72)
    SetChrChipByIndex(0x1D, 0x29)
    SetChrChipByIndex(0x15, 0x33)
    SetChrChipByIndex(0x16, 0x33)
    SetChrChipByIndex(0x21, 0x1F)

    def lambda_8F97():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_8F97)

    def lambda_8FAC():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8FAC)

    def lambda_8FC1():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8FC1)

    def lambda_8FD6():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8FD6)
    BeginChrThread(0x21, 3, 0, 56)
    OP_24(0x244)
    OP_24(0x123)
    OP_24(0x361)
    OP_24(0x35D)
    OP_24(0x366)
    OP_24(0x36B)
    OP_24(0x35F)
    SetCameraDistance(17000, 150)
    Sleep(150)
    Battle("BattleInfo_ED0", 0x0, 0x0, 0x100, 0x3D, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x21, 0x3)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    AddParty(0x3, 0xFF, 0xFF)
    ClearMapFlags(0x10000000)
    Call(0, 72)
    Return()

    # Function_40_563C end

    def Function_41_908D(): pass

    label("Function_41_908D")

    SetChrChipByIndex(0x15, 0x33)
    OP_95(0x15, -50, 0, 133650, 6000, 0x0)
    OP_93(0x15, 0x0, 0x1F4)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x1)
    Return()

    # Function_41_908D end

    def Function_42_90B5(): pass

    label("Function_42_90B5")

    SetChrChipByIndex(0x15, 0x33)
    OP_95(0x15, -18850, 0, 137000, 6000, 0x0)
    OP_93(0x15, 0x0, 0x1F4)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x1)
    Return()

    # Function_42_90B5 end

    def Function_43_90DD(): pass

    label("Function_43_90DD")

    SetChrChipByIndex(0x16, 0x33)
    OP_95(0x16, -2050, 0, 137900, 6000, 0x0)
    OP_93(0x16, 0x0, 0x1F4)
    SetChrChipByIndex(0x16, 0x34)
    SetChrSubChip(0x16, 0x1)
    Return()

    # Function_43_90DD end

    def Function_44_9105(): pass

    label("Function_44_9105")

    SetChrChipByIndex(0x17, 0x33)
    OP_95(0x17, -4500, 0, 131150, 6000, 0x0)
    OP_93(0x17, 0x0, 0x1F4)
    SetChrChipByIndex(0x17, 0x34)
    SetChrSubChip(0x17, 0x1)
    Return()

    # Function_44_9105 end

    def Function_45_912D(): pass

    label("Function_45_912D")

    SetChrChipByIndex(0x17, 0x33)
    OP_95(0x17, -17500, 0, 139450, 6000, 0x0)
    OP_93(0x17, 0x0, 0x1F4)
    SetChrChipByIndex(0x17, 0x34)
    SetChrSubChip(0x17, 0x1)
    Return()

    # Function_45_912D end

    def Function_46_9155(): pass

    label("Function_46_9155")

    SetChrChipByIndex(0x18, 0x33)
    OP_95(0x18, -3950, 0, 136900, 6000, 0x0)
    OP_95(0x18, -5300, 0, 137700, 6000, 0x0)
    OP_93(0x18, 0x0, 0x1F4)
    SetChrChipByIndex(0x18, 0x34)
    SetChrSubChip(0x18, 0x1)
    Return()

    # Function_46_9155 end

    def Function_47_9191(): pass

    label("Function_47_9191")

    SetChrChipByIndex(0x19, 0x33)
    OP_95(0x19, -4500, 0, 131150, 6000, 0x0)
    OP_95(0x19, -7550, 0, 133100, 6000, 0x0)
    OP_93(0x19, 0x0, 0x1F4)
    SetChrChipByIndex(0x19, 0x34)
    SetChrSubChip(0x19, 0x1)
    Return()

    # Function_47_9191 end

    def Function_48_91CD(): pass

    label("Function_48_91CD")

    SetChrChipByIndex(0x19, 0x33)
    OP_95(0x19, -20150, 0, 140400, 6000, 0x0)
    OP_93(0x19, 0x0, 0x1F4)
    SetChrChipByIndex(0x19, 0x34)
    SetChrSubChip(0x19, 0x1)
    Return()

    # Function_48_91CD end

    def Function_49_91F5(): pass

    label("Function_49_91F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9228")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_921C")
    OP_4C(0xFE, 0x3)
    Jump("loc_9220")

    label("loc_921C")

    OP_4B(0xFE, 0x3)

    label("loc_9220")

    Sleep(500)
    Jump("Function_49_91F5")

    label("loc_9228")

    Return()

    # Function_49_91F5 end

    def Function_50_9229(): pass

    label("Function_50_9229")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9278")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("Function_50_9229")

    label("loc_9278")

    Return()

    # Function_50_9229 end

    def Function_51_9279(): pass

    label("Function_51_9279")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92C8")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("Function_51_9279")

    label("loc_92C8")

    Return()

    # Function_51_9279 end

    def Function_52_92C9(): pass

    label("Function_52_92C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9318")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, -150, 1250, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("Function_52_92C9")

    label("loc_9318")

    Return()

    # Function_52_92C9 end

    def Function_53_9319(): pass

    label("Function_53_9319")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9373")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 0, 1100, 2600, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x14, 0x32, 0xBB8)
    Jump("Function_53_9319")

    label("loc_9373")

    Return()

    # Function_53_9319 end

    def Function_54_9374(): pass

    label("Function_54_9374")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93BE")
    PlayEffect(0x9, 0xFF, 0xFE, 0x3, -200, 1550, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_54_9374")

    label("loc_93BE")

    Return()

    # Function_54_9374 end

    def Function_55_93BF(): pass

    label("Function_55_93BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_941A")
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    PlayEffect(0x9, 0xFF, 0xFE, 0x3, -300, 800, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_55_93BF")

    label("loc_941A")

    Return()

    # Function_55_93BF end

    def Function_56_941B(): pass

    label("Function_56_941B")

    SetChrChipByIndex(0xFE, 0x1F)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9435")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_944C")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_9435")

    label("loc_944C")

    Return()

    # Function_56_941B end

    def Function_57_944D(): pass

    label("Function_57_944D")

    SetChrChipByIndex(0xFE, 0x1E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9467")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_947E")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_9467")

    label("loc_947E")

    Return()

    # Function_57_944D end

    def Function_58_947F(): pass

    label("Function_58_947F")

    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x5)
    Sound(809, 0, 100, 0)
    OP_9D(0x21, 0x3B60, 0x1770, 0x23410, 0x3E8, 0x1770)
    BeginChrThread(0x21, 0, 0, 56)
    OP_95(0x21, 12700, 6000, 144400, 6000, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrSubChip(0x21, 0x5)

    def lambda_94CB():
        OP_9D(0xFE, 0x265C, 0x1770, 0x233DE, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_94CB)
    Return()

    # Function_58_947F end

    def Function_59_94E4(): pass

    label("Function_59_94E4")

    Sleep(100)
    SetChrChipByIndex(0x22, 0x1F)
    BeginChrThread(0x22, 0, 0, 56)
    OP_95(0x22, -320, 4000, 149170, 6000, 0x0)
    OP_95(0x22, 5060, 6000, 148610, 6000, 0x0)
    EndChrThread(0x22, 0x0)
    TurnDirection(0x22, 0x1C, 500)
    SetChrSubChip(0x22, 0x5)

    def lambda_952D():
        OP_9D(0xFE, 0x21FC, 0x1770, 0x23F32, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_952D)
    Return()

    # Function_59_94E4 end

    def Function_60_9546(): pass

    label("Function_60_9546")

    Sleep(1600)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x5)
    Sound(809, 0, 100, 0)
    OP_9D(0x23, 0x238C, 0x1770, 0x24784, 0x3E8, 0x1770)
    TurnDirection(0x23, 0x1C, 500)

    def lambda_957A():
        OP_9D(0xFE, 0x2D82, 0x186A, 0x241F8, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_957A)
    Return()

    # Function_60_9546 end

    def Function_61_9593(): pass

    label("Function_61_9593")

    Sleep(2000)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x5)
    Sound(809, 0, 100, 0)
    OP_9D(0x24, 0x285A, 0x1770, 0x24572, 0x3E8, 0x1770)
    TurnDirection(0x24, 0x1C, 500)
    SetChrSubChip(0x24, 0x5)

    def lambda_95CB():
        OP_9D(0xFE, 0x30A2, 0x1770, 0x23988, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_95CB)
    Return()

    # Function_61_9593 end

    def Function_62_95E4(): pass

    label("Function_62_95E4")

    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 60, 0)

    def lambda_962F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_962F)

    def lambda_9648():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9648)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE70, 0x7D0, 0x0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sound(514, 0, 75, 0)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_62_95E4 end

    def Function_63_9682(): pass

    label("Function_63_9682")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_969A")
    OP_A1(0xFE, 0xDAC, 0x2, 0x1, 0x2)
    Jump("Function_63_9682")

    label("loc_969A")

    Return()

    # Function_63_9682 end

    def Function_64_969B(): pass

    label("Function_64_969B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96B3")
    OP_A1(0xFE, 0xDAC, 0x2, 0x4, 0x5)
    Jump("Function_64_969B")

    label("loc_96B3")

    Return()

    # Function_64_969B end

    def Function_65_96B4(): pass

    label("Function_65_96B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96CC")
    OP_A1(0xFE, 0xDAC, 0x2, 0x0, 0x1)
    Jump("Function_65_96B4")

    label("loc_96CC")

    Return()

    # Function_65_96B4 end

    def Function_66_96CD(): pass

    label("Function_66_96CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96E4")
    OP_A0(0xFE, 5000, 0x1, 0x6)
    Jump("Function_66_96CD")

    label("loc_96E4")

    Return()

    # Function_66_96CD end

    def Function_67_96E5(): pass

    label("Function_67_96E5")

    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_96ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_974F")
    SetChrSubChip(0xFE, 0x2)
    Sleep(850)
    SetChrSubChip(0xFE, 0x3)
    Sound(530, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x5, 0, 1200, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(80)
    SetChrSubChip(0xFE, 0x4)
    Sleep(80)
    Jump("loc_96ED")

    label("loc_974F")

    Return()

    # Function_67_96E5 end

    def Function_68_9750(): pass

    label("Function_68_9750")

    SetChrSubChip(0xFE, 0x0)
    Sound(357, 0, 100, 0)
    PlayEffect(0x6, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    Sound(280, 0, 80, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_68_9750 end

    def Function_69_97F9(): pass

    label("Function_69_97F9")

    Sound(872, 0, 100, 0)
    Sleep(400)
    Sound(870, 2, 100, 0)
    Return()

    # Function_69_97F9 end

    def Function_70_9809(): pass

    label("Function_70_9809")

    Sound(872, 0, 100, 0)
    Sleep(400)
    Sound(870, 2, 100, 0)
    Sound(875, 2, 100, 0)
    Return()

    # Function_70_9809 end

    def Function_71_981F(): pass

    label("Function_71_981F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9838")
    Sound(845, 0, 100, 0)
    Sleep(400)
    Jump("Function_71_981F")

    label("loc_9838")

    Return()

    # Function_71_981F end

    def Function_72_9839(): pass

    label("Function_72_9839")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x37)
    LoadChrToIndex("chr/ch00150.itc", 0x3C)
    LoadChrToIndex("chr/ch00250.itc", 0x41)
    LoadChrToIndex("apl/ch51439.itc", 0x47)
    LoadChrToIndex("chr/ch02950.itc", 0x50)
    LoadChrToIndex("chr/ch03050.itc", 0x55)
    LoadChrToIndex("chr/ch32650.itc", 0x1E)
    LoadChrToIndex("chr/ch32651.itc", 0x1F)
    LoadChrToIndex("chr/ch32654.itc", 0x21)
    LoadChrToIndex("chr/ch31251.itc", 0x23)
    LoadChrToIndex("chr/ch31252.itc", 0x24)
    LoadChrToIndex("chr/ch03450.itc", 0x28)
    LoadChrToIndex("chr/ch03451.itc", 0x29)
    LoadChrToIndex("chr/ch0345F.itc", 0x2A)
    LoadChrToIndex("chr/ch41951.itc", 0x32)
    LoadChrToIndex("chr/ch41952.itc", 0x33)
    LoadChrToIndex("chr/ch41953.itc", 0x34)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis266.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis267.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis268.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    LoadEffect(0x0, "battle/sp003000.eff")
    LoadEffect(0x1, "event/ev12002.eff")
    LoadEffect(0x3, "battle/btgun00.eff")
    SoundLoad(860)
    SoundLoad(861)
    SoundLoad(865)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x2)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x2)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x3)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x20)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x34)
    SetChrSubChip(0x16, 0x3)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x33)
    SetChrSubChip(0x17, 0x2)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x2)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x33)
    SetChrSubChip(0x19, 0x2)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x33)
    SetChrSubChip(0x1A, 0x2)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x101, 0x37)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x3C)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x41)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x47)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x50)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x55)
    SetChrSubChip(0x105, 0x0)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0x28)
    SetMapObjFlags(0x5, 0x1000)
    OP_F3(100000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AEA")
    OP_2C(0xAA, 0x1)

    label("loc_9AEA")

    SetChrPos(0x101, -25100, 0, 133850, 215)
    SetChrPos(0x102, -23800, 0, 136100, 215)
    SetChrPos(0x103, -22350, 0, 135550, 215)
    SetChrPos(0x109, -23050, 0, 134100, 215)
    SetChrPos(0x105, -25200, 0, 135200, 215)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x104, -20800, 0, 138300, 215)
    SetChrPos(0x1D, -27600, 0, 129250, 45)
    SetChrPos(0x15, -29400, 0, 127550, 45)
    SetChrPos(0x16, -27750, 0, 127050, 45)
    OP_68(-26000, 1200, 132500, 0)
    MoveCamera(75, 20, 3, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0119
    ChrTalk(
        0x101,
        "#00010F#5P唔，呼……呼……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x105,
        (
            "#10310F#5P这就是最强级别的\x01",
            "猎兵团的实力吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x109,
        (
            "#10108F#5P唔……要论平日的训练，\x01",
            "我们应该不输对方才对！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1D,
        (
            "#04606F#12P嗯……倒也不差，\x01",
            "不过就到此为止好了。\x02\x03",

            "#04611F在品尝至尊美味之前，\x01",
            "没必要吃太多餐前甜点。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        "#00105F#5P哎……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x131, 0x1F4)

    #C0124
    ChrTalk(
        0x103,
        "#00202F#11P啊……！\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0x1F4)
    Sound(860, 2, 80, 0)
    Sound(861, 2, 50, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    StopSound(860, 1000, 70)
    StopSound(861, 1000, 40)
    Sleep(500)
    Fade(500)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x1E, -26100, 8000, 175800, 180)
    SetChrPos(0xD, -27300, 8000, 176550, 180)
    SetChrPos(0xE, -25250, 8000, 174750, 180)
    SetChrPos(0xF, -25240, 8000, 180620, 182)
    SetChrPos(0x10, -27270, 8000, 183470, 137)
    SetChrPos(0x11, -27530, 8000, 187170, 182)
    SetChrPos(0x12, -27170, 8000, 190850, 225)
    SetChrPos(0x13, -25790, 8000, 194970, 225)
    SetChrPos(0x14, -22670, 8000, 198030, 225)
    OP_68(-28100, 10150, 182100, 0)
    MoveCamera(30, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21450, 0)
    OP_68(-26100, 8600, 175800, 7000)
    MoveCamera(45, 25, 0, 7000)
    SetCameraDistance(20000, 7000)
    PlayEffect(0x1, 0x0, 0xD, 0x3, 100, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xE, 0x3, 100, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xF, 1, 0, 78)
    BeginChrThread(0x10, 1, 0, 80)
    BeginChrThread(0x11, 1, 0, 82)
    BeginChrThread(0x12, 1, 0, 84)
    BeginChrThread(0x13, 1, 0, 86)
    BeginChrThread(0x14, 1, 0, 87)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0x1E, -17250, 6300, 165100, 180)
    SetChrPos(0xD, -18000, 6650, 166580, 180)
    SetChrPos(0xE, -16050, 6880, 167530, 180)
    OP_68(-18150, 6000, 161050, 0)
    MoveCamera(15, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    OP_68(-20000, 4900, 152450, 3000)
    MoveCamera(15, 25, -5, 3000)
    SetCameraDistance(20000, 3000)
    BeginChrThread(0x1E, 1, 0, 73)
    BeginChrThread(0xD, 1, 0, 74)
    BeginChrThread(0xE, 1, 0, 76)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x1E, 1)

    #C0125
    ChrTalk(
        0x101,
        "#00002F#6P#N米蕾优三尉……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0126
    ChrTalk(
        0x109,
        "#10109F#12P#N来、来支援我们了吗……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0127
    ChrTalk(
        0x1E,
        (
            "#07904F#5P嗯，司令接到了\x01",
            "你们科长发来的联络。\x02\x03",

            "#07907F确认敌方部队！\x01",
            "开始扫荡作战！\x02\x03",

            "以夺回玛因兹与\x01",
            "确保居民安全为最优先事项！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("众警备队员")

    #A0128
    AnonymousTalk(
        0xFF,
        "#4S是！长官！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_82(0x0, 0x64, 0xBB8, 0x2710)
    Sound(860, 2, 80, 0)
    Sound(861, 2, 50, 0)
    BeginChrThread(0xD, 0, 0, 49)
    BeginChrThread(0xD, 3, 0, 88)
    BeginChrThread(0xE, 0, 0, 49)
    BeginChrThread(0xE, 3, 0, 88)
    BeginChrThread(0x13, 0, 0, 49)
    BeginChrThread(0x13, 3, 0, 88)
    BeginChrThread(0x14, 0, 0, 49)
    BeginChrThread(0x14, 3, 0, 88)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x10, 0x23)

    def lambda_A1D3():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A1D3)
    Sleep(50)
    SetChrChipByIndex(0xF, 0x23)

    def lambda_A1EF():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A1EF)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x23)

    def lambda_A20B():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A20B)
    Sleep(300)
    SetChrChipByIndex(0x12, 0x23)

    def lambda_A227():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A227)
    Sleep(1000)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    OP_25(0x35C, 0x32)
    OP_25(0x35D, 0x3C)
    Fade(500)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x3)
    SetChrChipByIndex(0xD, 0x23)
    SetChrChipByIndex(0xE, 0x23)
    SetChrPos(0x101, -23100, 0, 133850, 215)
    SetChrPos(0x102, -21800, 0, 136100, 215)
    SetChrPos(0x103, -20250, 0, 135550, 215)
    SetChrPos(0x109, -21050, 0, 134100, 215)
    SetChrPos(0x105, -23200, 0, 135200, 215)
    SetChrSubChip(0x104, 0x26)
    SetChrPos(0x15, -29350, 0, 128850, 45)
    SetChrPos(0x16, -27650, 0, 127400, 45)
    SetChrPos(0xD, -18850, 0, 142850, 225)
    SetChrPos(0xE, -18850, 0, 142850, 225)
    SetChrPos(0xF, -18850, 0, 142850, 225)
    SetChrPos(0x10, -14750, 0, 138850, 225)
    SetChrPos(0x11, -13750, 0, 139150, 225)
    SetChrPos(0x12, -14750, 0, 138850, 225)
    SetChrChipByIndex(0x15, 0x33)
    SetChrChipByIndex(0x16, 0x33)
    Sound(865, 2, 60, 0)
    BeginChrThread(0x15, 0, 0, 49)
    BeginChrThread(0x15, 3, 0, 50)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x16, 3, 0, 50)
    OP_68(-26250, 1000, 130699, 0)
    MoveCamera(45, 30, -2, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(21500, 1000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -29900, 0, 126800, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 1, 0, 96)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    Sleep(300)
    SetChrChipByIndex(0x15, 0x32)
    OP_93(0x15, 0xE1, 0x2EE)

    def lambda_A42C():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A42C)
    StopSound(865, 300, 50)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    Sleep(300)
    SetChrChipByIndex(0x16, 0x32)
    OP_93(0x16, 0xE1, 0x2EE)

    def lambda_A45D():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A45D)

    #C0129
    ChrTalk(
        0x1D,
        (
            "#04612F#6P呵呵，那就再见吧～！\x02\x03",

            "#04602F不过我感觉\x01",
            "很快就会再见面的！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1D, 0x29)
    OP_93(0x1D, 0xE1, 0x2EE)

    def lambda_A4C7():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A4C7)
    OP_68(-29200, 1000, 127750, 5000)

    def lambda_A4ED():
        OP_9B(0x0, 0xFE, 0xFFFD, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A4ED)
    Sleep(50)

    def lambda_A505():
        OP_9B(0x0, 0xFE, 0x3, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A505)
    Sleep(300)

    def lambda_A51D():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A51D)
    Sleep(50)

    def lambda_A535():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A535)
    Sleep(300)

    def lambda_A54D():
        OP_9B(0x0, 0xFE, 0xFFFA, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A54D)
    Sleep(50)

    def lambda_A565():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A565)
    Sleep(1000)
    WaitChrThread(0x1D, 1)
    Fade(500)
    BeginChrThread(0x101, 1, 0, 97)
    StopEffect(0x0, 0x0)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1D, -32049, -1000, 105900, 180)
    SetChrPos(0x15, -33400, -1000, 103250, 0)
    SetChrPos(0x16, -30900, -1000, 103850, 0)
    SetChrPos(0x17, -32500, -1000, 100400, 0)
    SetChrPos(0x18, -31150, -770, 98800, 0)
    SetChrPos(0x19, -30900, 0, 90450, 0)
    SetChrPos(0x1A, -34100, 0, 91050, 0)
    SetChrPos(0xD, -32750, -870, 112700, 180)
    SetChrPos(0xE, -31350, -980, 112150, 180)
    SetChrPos(0xF, -30000, -560, 114350, 180)
    SetChrPos(0x10, -33850, -600, 114150, 180)
    SetChrPos(0x11, -33050, -310, 115700, 180)
    SetChrPos(0x12, -30500, -290, 115800, 180)
    BeginChrThread(0xD, 1, 0, 75)
    BeginChrThread(0xE, 1, 0, 77)
    BeginChrThread(0xF, 1, 0, 79)
    BeginChrThread(0x10, 1, 0, 81)
    BeginChrThread(0x11, 1, 0, 83)
    BeginChrThread(0x12, 1, 0, 85)
    BeginChrThread(0x1D, 1, 0, 89)
    BeginChrThread(0x15, 1, 0, 90)
    BeginChrThread(0x16, 1, 0, 91)
    BeginChrThread(0x17, 1, 0, 92)
    BeginChrThread(0x18, 1, 0, 93)
    BeginChrThread(0x19, 1, 0, 94)
    BeginChrThread(0x1A, 1, 0, 95)
    OP_68(-32159, -400, 105000, 0)
    MoveCamera(35, 25, 5, 0)
    OP_6E(500, 0)
    SetCameraDistance(25600, 0)
    OP_68(-35290, 600, 84430, 7000)
    MoveCamera(45, 25, 10, 7000)
    OP_6F(0x79)
    WaitChrThread(0x1D, 1)
    Sleep(1500)
    StopSound(860, 1000, 40)
    StopSound(861, 1000, 50)
    Fade(500)
    EndChrThread(0x101, 0x1)
    OP_82(0xA, 0xA, 0xBB8, 0x0)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x0)
    EndChrThread(0x10, 0x3)
    EndChrThread(0x11, 0x0)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x12, 0x3)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1A, 0x1)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x104, 0x2)
    SetChrPos(0x101, -19900, 0, 137400, 270)
    SetChrPos(0x102, -18800, 0, 135450, 335)
    SetChrPos(0x103, -17850, 0, 136550, 270)
    SetChrPos(0x109, -19750, 0, 135350, 270)
    SetChrPos(0x105, -18200, 0, 138000, 270)
    SetChrPos(0x1E, -20000, 0, 143700, 225)
    SetChrPos(0xD, -22200, 0, 141350, 225)
    SetChrPos(0xE, -21750, 0, 139600, 225)
    SetChrChipByIndex(0xD, 0x23)
    SetChrChipByIndex(0xE, 0x23)

    def lambda_A8C6():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A8C6)

    def lambda_A8DB():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A8DB)
    SetChrChipByIndex(0x1E, 0x1F)

    def lambda_A8F4():
        OP_95(0xFE, -22150, 0, 139350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A8F4)
    OP_68(-20950, 1200, 137200, 0)
    MoveCamera(13, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(20000, 2000)
    WaitChrThread(0x1E, 1)

    def lambda_A949():

        label("loc_A949")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_A949")

    QueueWorkItem2(0x101, 2, lambda_A949)

    def lambda_A95B():

        label("loc_A95B")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_A95B")

    QueueWorkItem2(0x104, 2, lambda_A95B)

    def lambda_A96D():
        TurnDirection(0x1E, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_A96D)
    Sleep(50)

    def lambda_A97D():

        label("loc_A97D")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_A97D")

    QueueWorkItem2(0x102, 2, lambda_A97D)

    def lambda_A98F():

        label("loc_A98F")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_A98F")

    QueueWorkItem2(0x103, 2, lambda_A98F)
    Sleep(50)

    def lambda_A9A4():

        label("loc_A9A4")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_A9A4")

    QueueWorkItem2(0x109, 2, lambda_A9A4)

    def lambda_A9B6():

        label("loc_A9B6")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_A9B6")

    QueueWorkItem2(0x105, 2, lambda_A9B6)
    WaitChrThread(0x1E, 2)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    OP_0D()
    OP_6F(0x79)

    #C0130
    ChrTalk(
        0x104,
        "#00308F#12P米蕾优……\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    #C0131
    ChrTalk(
        0x1E,
        (
            "#07906F#5P真是的，你总是\x01",
            "这么乱来……\x02\x03",

            "#07902F那些家伙就\x01",
            "交给我们来对付吧。\x02\x03",

            "……你们几位，\x01",
            "请把兰迪看好，\x01",
            "不要再让他如此莽撞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#00000F#12P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        "#00204F#12P放心吧。\x02",
    )

    CloseMessageWindow()
    OP_68(-23820, 1000, 133320, 2000)
    MoveCamera(25, 25, 0, 2000)
    SetCameraDistance(18500, 2000)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x1E, 0x1F)
    OP_95(0x1E, -28500, 0, 128750, 5000, 0x0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x1E, 0x80)
    Sleep(500)
    Fade(500)
    OP_93(0x101, 0xC8, 0x0)
    OP_93(0x102, 0xC8, 0x0)
    OP_93(0x103, 0xC8, 0x0)
    OP_93(0x109, 0xC8, 0x0)
    OP_93(0x105, 0xC8, 0x0)
    OP_68(-19800, 1000, 137300, 0)
    MoveCamera(20, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    OP_0D()
    Sleep(300)

    #C0134
    ChrTalk(
        0x101,
        "#00006F#5P呼，哎呀呀……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        (
            "#00102F#11P总之……\x01",
            "暂且算是告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        "#00314F#5P#40W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(-20300, 1000, 137800, 1500)

    def lambda_AC5F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AC5F)
    Sleep(50)

    def lambda_AC6F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AC6F)

    def lambda_AC7C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AC7C)
    Sleep(50)

    def lambda_AC8C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AC8C)

    def lambda_AC99():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AC99)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    #C0137
    ChrTalk(
        0x101,
        "#00005F#12P兰迪……？\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x109,
        (
            "#10108F#12P你、你没事吧？\x01",
            "是不是什么地方受了伤……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0139
    ChrTalk(
        0x104,
        (
            "#00303F#30W#5P……罗伊德，\x01",
            "你给我解释一下……\x02\x03",

            "#00312F你到底在想些什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        "#00011F#12P哎……\x02",
    )

    CloseMessageWindow()

    def lambda_AD7E():

        label("loc_AD7E")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_AD7E")

    QueueWorkItem2(0x102, 2, lambda_AD7E)

    def lambda_AD90():

        label("loc_AD90")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_AD90")

    QueueWorkItem2(0x103, 2, lambda_AD90)

    def lambda_ADA2():

        label("loc_ADA2")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_ADA2")

    QueueWorkItem2(0x109, 2, lambda_ADA2)

    def lambda_ADB4():

        label("loc_ADB4")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_ADB4")

    QueueWorkItem2(0x105, 2, lambda_ADB4)
    OP_68(-20000, 1000, 137800, 1000)
    OP_9A(0x104, 0x101, 0x190, 0x3E8, 0x0)
    Fade(250)
    SetCameraDistance(20000, 250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x47)
    SetChrSubChip(0x101, 0x29)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0x47)
    SetChrSubChip(0x104, 0x2)

    def lambda_AE27():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AE27)
    OP_0D()
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)

    #C0141
    ChrTalk(
        0x101,
        "#00011F#12P唔……！\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        "#00105F#12P兰迪！？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        "#00205F#11P兰迪前辈……！？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    SetCameraDistance(18000, 50000)
    Sleep(500)

    #C0144
    ChrTalk(
        0x104,
        (
            "#00311F#30W#5P你难道不明白吗……\x01",
            "你们踏入的地方\x01",
            "可是『战场』啊……！\x02\x03",

            "#30W你们这些既不是军人也不是\x01",
            "猎兵的非专业战斗人士\x01",
            "竟然来到这种地方……\x02\x03",

            "#30W这究竟有多么危险，\x01",
            "你真的明白吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#00013F#12P……兰迪………\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x104,
        (
            "#00303F#30W#5P……我对大小姐和阿缇\x01",
            "有不少话想说……\x02\x03",

            "……也想问问诺艾尔和瓦吉，\x01",
            "为什么明知危险，\x01",
            "也不阻止大家……\x02\x03",

            "#00311F但是，最关键的还是你罗伊德！\x01",
            "你可是队长啊……！\x02\x03",

            "在这种时候，你怎能感情用事，\x01",
            "把同伴置于险境……？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        "#00003F#12P#30W…………开什么玩笑。\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetCameraDistance(20000, 100)

    def lambda_B0C4():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B0C4)
    Sound(811, 0, 60, 0)

    def lambda_B0DF():
        OP_A0(0xFE, 2000, 0x29, 0x2B)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B0DF)

    def lambda_B0EC():
        OP_A0(0xFE, 2000, 0x2, 0x4)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_B0EC)

    def lambda_B0F9():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B0F9)

    def lambda_B10E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B10E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x104, 1)
    Sleep(500)
    OP_68(-20350, 1000, 137900, 500)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_99(0x101, 0x104, 0x190, 0x3E8, 0x0)
    OP_6F(0x79)
    SetCameraDistance(18000, 120000)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x47)
    SetChrSubChip(0x101, 0x2C)
    SetChrSubChip(0x104, 0x5)

    def lambda_B1A6():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B1A6)
    OP_0D()

    #C0148
    ChrTalk(
        0x104,
        "#00305F#5P唔……！\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x102,
        "#00101F#12P罗伊德……！\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        "#00208F#12P罗伊德前辈……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0151
    ChrTalk(
        0x101,
        (
            "#00010F#12P我们正是因为不能把同伴置于险境，\x01",
            "所以才会来到这里的啊！\x02\x03",

            "#00006F什么叫『就这样，再见』……？\x02\x03",

            "#00007F……只留下一张那样的\x01",
            "字条就不辞而别……\x01",
            "你真的觉得我们能接受吗！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A0(0x104, 1000, 0x20, 0x21)
    Sleep(500)

    #C0152
    ChrTalk(
        0x104,
        (
            "#00313F#5P#30W呜……\x02\x03",

            "……我果然……\x02\x03",

            "#40W我果然……从一开始\x01",
            "就不应该和你们在一起……\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_CB(0x2, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)

    #C0153
    ChrTalk(
        0x104,
        (
            "#00313F#30W#5P……我的双手染满鲜血……\x02\x03",

            "不仅是在战场上杀死士兵……\x02\x03",

            "为了诱骗棘手的敌方部队，\x01",
            "也曾利用过毫无牵连的村子……\x02\x03",

            "因此害那无辜的家伙……\x02\x03",

            "……害那个目光和你一样\x01",
            "的年轻人白白牺牲了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        "#00005F#12P……！\x02",
    )

    CloseMessageWindow()
    OP_68(-20000, 1000, 137750, 500)
    SetChrSubChip(0x101, 0x2D)

    def lambda_B505():
        OP_9B(0x1, 0xFE, 0xFFF6, 0xFFFFFDA8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B505)

    def lambda_B51A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B51A)
    Sound(811, 0, 60, 0)

    def lambda_B539():
        OP_A0(0xFE, 1500, 0x6, 0x7)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_B539)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    Sleep(500)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0155
    ChrTalk(
        0x104,
        (
            "#00307F#5P站在你们面前的人就是\x01",
            "一个如此无药可救的混蛋！\x02\x03",

            "#00306F别再……继续管我了！\x02\x03",

            "别再带着小狗一样的目光靠近我，\x01",
            "别再把我当成可以依靠的兄长了……！\x02\x03",

            "#00308F如果一直这样下去……我……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0156
    ChrTalk(
        0x104,
        (
            "#00313F#4S#5P#40W……我恐怕就会……\x01",
            "恐怕就会渐渐原谅自己了！！\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        "#00108F#12P#30W……兰迪……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x103,
        "#00206F#11P#30W兰迪前辈……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x109,
        "#10108F#12P#30W………前辈……………\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x105,
        "#10303F#11P#30W………原来是这样啊…………\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        "#00008F#12P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_A0(0x101, 1000, 0x2D, 0x30)

    #C0162
    ChrTalk(
        0x101,
        (
            "#00004F#12P#30W………哈哈……………\x02\x03",

            "太好了……我总算放心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x12C, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_A0(0x104, 1500, 0x7, 0xA)
    Sleep(150)

    #C0163
    ChrTalk(
        0x104,
        "#00305F#40W#5P………哎……………\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x102,
        "#00105F#12P罗、罗伊德……？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        "#00205F#11P罗伊德前辈……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0x101, 1000, 0x2F, 0x2D)
    Sleep(300)

    #C0166
    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W……如果你仍像平时一样，摆出一副\x01",
            "漫不经心的轻松表情，企图开几句玩笑来蒙混过去，\x01",
            "我还真不知该如何应对呢……\x02\x03",

            "#00002F不过……\x01",
            "你总算向我们袒露出真实感情了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x104, 0x7D0, 0x4, 0x1D, 0x1E, 0x1D, 0xA)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0167
    ChrTalk(
        0x104,
        "#00305F#5P！！\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x102,
        "#00102F#12P#30W……啊………\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x109,
        "#10102F#12P#30W……罗伊德警官……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W仔细想想，其实兰迪和我们一样，\x01",
            "也是个涉世未深的年轻人……\x02\x03",

            "#00008F……大家都知道你背负着\x01",
            "沉重的过去，但一直都在刻意回避，\x01",
            "不去触及相关的话题……\x02\x03",

            "我们总是依靠你的帮助，\x01",
            "却从没帮你分担过一点点……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        "#00206F#11P#30W……是的……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        "#00103F#12P#30W………是啊………\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        (
            "#00306F#5P#30W……喂……喂………\x02\x03",

            "#00301F我不是都说过了吗，\x01",
            "我没有资格接受……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W兰迪的过去与罪恶感\x01",
            "都是属于兰迪自己的东西。\x02\x03",

            "#00003F我想，那是需要兰迪在自己心中\x01",
            "解决的问题。\x02\x03",

            "#00001F而解决结果也许是\x01",
            "永远不能原谅自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x104,
        "#00308F#5P#30W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#00003F#12P#30W不过，就算别人\x01",
            "无法原谅兰迪……\x02\x03",

            "就算连兰迪自己\x01",
            "都无法原谅自己……\x02\x03",

            "#00002F……我们也会\x01",
            "原谅兰迪的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0xC8, 0x0, 0xBB8, 0xC8)

    #C0177
    ChrTalk(
        0x104,
        "#00305F#5P#4S！！？\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        (
            "#00104F#12P#30W……是啊。\x02\x03",

            "#00102F只有相互体谅，相互包容，\x01",
            "才能算是真正的『同伴』……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#00204F#11P#30W就像大家在当时\x01",
            "接受了我的过去一样……\x02\x03",

            "#00202F我也会接受兰迪前辈的过去，\x01",
            "还有喜好搭讪的性格\x01",
            "和不检点的作风。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x109,
        (
            "#10103F#12P#30W……我也接受。\x02\x03",

            "#10100F同为军人……\x01",
            "我知道有些事情是无法避免的。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x105,
        (
            "#10302F#11P#30W哎呀呀，其实我\x01",
            "很不擅长说这样的话呢。\x02\x03",

            "#10304F……人类活在这个世界上，\x01",
            "本身便背负着某种罪孽。\x02\x03",

            "#10300F这么说或许有点不妥……不过，\x01",
            "在女神面前，大家其实并没有多大区别哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A0(0x104, 1500, 0xA, 0xD)
    Sleep(500)

    #C0182
    ChrTalk(
        0x104,
        "#00314F#40W#5P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W我们既没有生活在过去，\x01",
            "也没有生活在未知的明天……\x02\x03",

            "我们只能生活在今天，\x01",
            "只能把握住眼前的一瞬间。\x02\x03",

            "#00008F而在如今这一瞬间……\x01",
            "我们大家共处在同一场所。\x02\x03",

            "如果这个事实能让你感受到\x01",
            "哪怕是一点点的开心……\x02\x03",

            "#00000F就请像我们接受你一样，\x01",
            "接受我们吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_BFEB():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BFEB)
    WaitChrThread(0x104, 2)
    Sleep(500)

    def lambda_C00B():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C00B)
    WaitChrThread(0x104, 2)
    Sleep(500)
    OP_A0(0x104, 1500, 0xE, 0x10)
    Sleep(300)

    #C0184
    ChrTalk(
        0x104,
        (
            "#00313F#40W#5P…………………………………\x02\x03",

            "……真是的……你们总是这么……\x02\x03",

            "#40W为什么我……非要当众接受\x01",
            "这么煽情的劝慰啊……\x02\x03",

            "#40W……实在是太丢脸了……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        (
            "#00204F#11P好啦，我以前不是也\x01",
            "有过同样经历吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        (
            "#00104F#12P呵呵，就像你当时说的一样……\x02\x03",

            "#00102F从选择留在支援科的那一刻开始，\x01",
            "我们就都成了\x01",
            "某人的受害者啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0187
    ChrTalk(
        0x101,
        "#00011F#11P为、为什么非要说我是加害者……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x109,
        (
            "#10112F#12P呵呵……\x01",
            "确实很有说服力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x105,
        (
            "#10309F#11P啊哈哈，连我都抵抗不了\x01",
            "这种一本正经的纯真型呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        "#00314F#40W#5P…………………………………\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    Sleep(150)
    OP_A0(0x104, 1200, 0x10, 0x13)
    Sleep(500)
    Sound(2374, 255, 80, 0)    #voice#Randy
    OP_A0(0x104, 1200, 0x13, 0x16)
    Sleep(800)

    #C0191
    ChrTalk(
        0x104,
        (
            "#00306F#5P#30W……呼。\x02\x03",

            "#00303F我杀过人……\x01",
            "而且是个游手好闲的废物。\x02\x03",

            "自以为很有实力，\x01",
            "却差点就被那个\x01",
            "怪物一样的小丫头取了性命。\x02\x03",

            "#00308F今后或许还会\x01",
            "像这次一样狼狈，\x01",
            "给你们添各种麻烦……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    OP_A0(0x104, 1300, 0x16, 0x19)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7569", 0)

    #A0192
    AnonymousTalk(
        0x104,
        "#5P#30W即使如此也没问题吗？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0193
    ChrTalk(
        0x101,
        "#00014F#12P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x102,
        "#00109F#12P嗯，当然。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x103,
        "#00214F#11P没问题。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x109,
        (
            "#10109F#12P今后也请\x01",
            "继续指教了！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x105,
        (
            "#10302F#11P呵呵……\x01",
            "大雨过后，就该出现什么来的？\x02",
        )
    )

    CloseMessageWindow()
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x32, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sleep(500)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    OP_68(-19000, 1000, 137650, 1000)

    def lambda_C503():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C503)
    Sleep(500)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    #C0198
    ChrTalk(
        0x104,
        (
            "#00310F#5P瓦吉，你小子……\x02\x03",

            "明明答应过我要保密的，\x01",
            "结果却到处乱说！？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x105,
        (
            "#10305F#11P哪有，你误会了。\x02\x03",

            "#10306F我遵照约定，什么都没说，\x01",
            "是罗伊德他们自己非要\x01",
            "调查你的去处。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C5CA():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C5CA)
    Sleep(50)

    def lambda_C5DA():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C5DA)

    def lambda_C5E7():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C5E7)
    Sleep(50)

    def lambda_C5F7():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C5F7)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)

    #C0200
    ChrTalk(
        0x109,
        (
            "#10105F#6P等、等一下，瓦吉……\x02\x03",

            "#10101F你……之前就知道\x01",
            "兰迪前辈要离开吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        "#00013F#6P瓦吉，你可真是……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x103,
        "#00211F#12P瓦吉先生……\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#00106F#12P呼，这可真是\x01",
            "有点过分啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x105,
        (
            "#10305F#11P其实我并没有\x01",
            "连具体目的地都问到的……\x02\x03",

            "#10306F哎呀呀……\x01",
            "看样子，我好像变成坏人了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x109,
        "#10106F#6P真是的……\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x103,
        (
            "#00203F#12P瓦吉先生偶尔也该\x01",
            "反省一下呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x104,
        "#00309F#5P哈哈……\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x9B, 0x1F4)
    Sleep(300)

    #C0208
    ChrTalk(
        0x104,
        (
            "#00304F#5P好了，\x01",
            "我总算能动弹了。\x02\x03",

            "#00300F虽然有些迟，不过先去\x01",
            "看看米蕾优他们那里的状况如何？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C804():
        OP_93(0xFE, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C804)
    Sleep(50)

    def lambda_C814():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C814)

    def lambda_C821():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C821)
    Sleep(50)

    def lambda_C831():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C831)

    def lambda_C83E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C83E)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)

    #C0209
    ChrTalk(
        0x101,
        "#00000F#12P是啊……\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x102,
        (
            "#00106F#12P但愿\x01",
            "『赤色星座』\x01",
            "已经撤退了。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    ReplaceBGM(-1, -1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 3)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_72_9839 end

    def Function_73_C8DE(): pass

    label("Function_73_C8DE")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -20000, 4000, 152450, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_73_C8DE end

    def Function_74_C90C(): pass

    label("Function_74_C90C")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -20000, 4000, 155150, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_74_C90C end

    def Function_75_C940(): pass

    label("Function_75_C940")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -32000, -1000, 102300, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    StopEffect(0x0, 0x2)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -34000, -1000, 107960, 4000, 0x0)
    OP_95(0xFE, -34000, 0, 89150, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -37350, 0, 76050, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_75_C940 end

    def Function_76_CA36(): pass

    label("Function_76_CA36")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -18750, 4000, 155600, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_76_CA36 end

    def Function_77_CA6A(): pass

    label("Function_77_CA6A")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    Sleep(1500)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -29680, -1000, 108290, 4000, 0x0)
    OP_95(0xFE, -32800, 0, 88200, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    Return()

    # Function_77_CA6A end

    def Function_78_CAEF(): pass

    label("Function_78_CAEF")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -21500, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -21500, 4000, 152550, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_78_CAEF end

    def Function_79_CB45(): pass

    label("Function_79_CB45")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -30450, -1000, 108500, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, -32100, 0, 93750, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    StopEffect(0x1, 0x2)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -31360, 0, 87960, 4000, 0x0)
    OP_95(0xFE, -33960, 0, 81120, 4000, 0x0)
    OP_95(0xFE, -34760, 0, 71820, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_79_CB45 end

    def Function_80_CC06(): pass

    label("Function_80_CC06")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -18800, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -18800, 4000, 152400, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_80_CC06 end

    def Function_81_CC5C(): pass

    label("Function_81_CC5C")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -33250, -1000, 107600, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    Sleep(2000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -34390, 0, 90290, 4000, 0x0)
    OP_95(0xFE, -39800, 0, 82050, 4000, 0x0)
    OP_95(0xFE, -38250, 0, 70760, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_81_CC5C end

    def Function_82_CCE3(): pass

    label("Function_82_CCE3")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -27250, 8000, 183450, 5000, 0x0)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -18150, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -18150, 4000, 154150, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_82_CCE3 end

    def Function_83_CD4D(): pass

    label("Function_83_CD4D")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -34000, -1000, 107960, 4000, 0x0)
    OP_95(0xFE, -32500, -1000, 103650, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, -32750, 0, 90700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(2500)
    StopEffect(0x2, 0x2)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -34390, 0, 90290, 4000, 0x0)
    OP_95(0xFE, -39800, 0, 82050, 4000, 0x0)
    OP_95(0xFE, -38250, 0, 70760, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_83_CD4D end

    def Function_84_CE29(): pass

    label("Function_84_CE29")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -27250, 8000, 183450, 5000, 0x0)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -20900, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -20900, 4000, 154150, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_84_CE29 end

    def Function_85_CE93(): pass

    label("Function_85_CE93")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -29800, -1000, 107850, 4000, 0x0)
    OP_95(0xFE, -31150, -1000, 101100, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    Sleep(2500)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -31360, 0, 87960, 4000, 0x0)
    OP_95(0xFE, -33960, 0, 81120, 4000, 0x0)
    OP_95(0xFE, -34760, 0, 71820, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_85_CE93 end

    def Function_86_CF35(): pass

    label("Function_86_CF35")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -27170, 8000, 190850, 5000, 0x0)
    OP_95(0xFE, -27250, 8000, 183450, 5000, 0x0)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -15550, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -17550, 4000, 152900, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_86_CF35 end

    def Function_87_CFB3(): pass

    label("Function_87_CFB3")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -27170, 8000, 190850, 5000, 0x0)
    OP_95(0xFE, -27250, 8000, 183450, 5000, 0x0)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -22250, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -22250, 4000, 153950, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_87_CFB3 end

    def Function_88_D037(): pass

    label("Function_88_D037")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D086")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 950, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x3, 0x2)
    Jump("Function_88_D037")

    label("loc_D086")

    Return()

    # Function_88_D037 end

    def Function_89_D087(): pass

    label("Function_89_D087")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -32650, 0, 89540, 6000, 0x0)
    OP_95(0xFE, -37240, 0, 83770, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xFE, 0x10E, 0x3E8)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF6276, 0xA28, 0x14776, 0xBB8, 0x1770)
    Sound(326, 0, 100, 0)
    OP_95(0xFE, -43910, 2600, 80620, 6000, 0x0)
    OP_93(0xFE, 0x87, 0x3E8)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF5FD8, 0x14B4, 0x130B0, 0xBB8, 0x1770)
    Sound(326, 0, 100, 0)
    OP_95(0xFE, -38420, 5300, 70130, 6000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_89_D087 end

    def Function_90_D14C(): pass

    label("Function_90_D14C")

    Sound(865, 2, 60, 0)
    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(1000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -33500, -1000, 100150, 5000, 0x0)
    OP_95(0xFE, -32900, 0, 91150, 5000, 0x0)
    OP_95(0xFE, -36550, 0, 84250, 5000, 0x0)
    OP_95(0xFE, -36950, 0, 67700, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_90_D14C end

    def Function_91_D1CF(): pass

    label("Function_91_D1CF")

    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(1300)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -30050, -810, 99000, 5000, 0x0)
    OP_95(0xFE, -32049, 0, 90500, 5000, 0x0)
    OP_95(0xFE, -35650, 0, 79100, 5000, 0x0)
    OP_95(0xFE, -34860, 0, 68450, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_91_D1CF end

    def Function_92_D24C(): pass

    label("Function_92_D24C")

    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(2500)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -32900, 0, 91150, 5000, 0x0)
    OP_95(0xFE, -36550, 0, 84250, 5000, 0x0)
    OP_95(0xFE, -36950, 0, 67700, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_92_D24C end

    def Function_93_D2B5(): pass

    label("Function_93_D2B5")

    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(2800)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -32049, 0, 90500, 5000, 0x0)
    OP_95(0xFE, -35650, 0, 79100, 5000, 0x0)
    OP_95(0xFE, -34860, 0, 68450, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_93_D2B5 end

    def Function_94_D31E(): pass

    label("Function_94_D31E")

    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(5000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -35650, 0, 79100, 5000, 0x0)
    OP_95(0xFE, -34860, 0, 68450, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_94_D31E end

    def Function_95_D373(): pass

    label("Function_95_D373")

    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(5000)
    StopSound(865, 500, 50)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -36550, 0, 84250, 5000, 0x0)
    OP_95(0xFE, -36950, 0, 67700, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_95_D373 end

    def Function_96_D3CE(): pass

    label("Function_96_D3CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D3F2")
    OP_82(0xA, 0xA, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_96_D3CE")

    label("loc_D3F2")

    Return()

    # Function_96_D3CE end

    def Function_97_D3F3(): pass

    label("Function_97_D3F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D417")
    OP_82(0x28, 0x28, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_97_D3F3")

    label("loc_D417")

    Return()

    # Function_97_D3F3 end

    def Function_98_D418(): pass

    label("Function_98_D418")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_E2(0x1)
    SetChrPos(0x101, -250, 0, -750, 0)
    SetChrPos(0x106, 750, 0, -1500, 0)
    SetChrPos(0x103, -1250, 0, -2500, 0)
    SetChrPos(0x107, -2250, 0, -2750, 0)
    SetChrPos(0x105, -250, 0, -3500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(0, 600, -2000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    OP_68(140, 600, 1460, 2000)
    MoveCamera(45, 25, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(20500, 2000)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)

    def lambda_D4F6():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D4F6)
    Sleep(0)

    def lambda_D50E():
        OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D50E)
    Sleep(0)

    def lambda_D526():
        OP_9B(0x0, 0x106, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_D526)
    Sleep(0)

    def lambda_D53E():
        OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D53E)
    Sleep(0)

    def lambda_D556():
        OP_9B(0x0, 0x107, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_D556)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    OP_0D()
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0211
    ChrTalk(
        0x101,
        "#00007F#11P是战斗的声音……！\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        (
            "#00201F#12P西北方向，距离约１０赛尔矩！\x02\x03",

            "恐怕是在山道外围的\x01",
            "山岳地带展开了战斗……！\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7586", 0)
    ReplaceBGM("ed7251", "ed7586")

    #C0213
    ChrTalk(
        0x101,
        "#00010F#11P呜……山岳地带吗……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x105,
        (
            "#10401F#12P我们恐怕很难\x01",
            "登上那里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x106,
        (
            "#10707F#11P不……\x01",
            "还是先去看看吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x107,
        (
            "#01201F#12P#3C嗯，万一情况紧急，\x01",
            "我们两个可以跃到崖上介入。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#00007F#11P明白了！\x01",
            "如果形势需要，就拜托你们二位了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 1500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x1A2, 5)
    OP_29(0xAF, 0x1, 0xC)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetBarrier(0x0, 0x0, 0x1, 0x0, -19610, 3500, 152140, 8000, 5000, 0)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    Return()

    # Function_98_D418 end

    def Function_99_D7DA(): pass

    label("Function_99_D7DA")

    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    OP_68(-19600, 4400, 152850, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25650, 0)
    SetChrPos(0x101, -19600, 3800, 151650, 0)
    SetChrPos(0x106, -19000, 3350, 150700, 0)
    SetChrPos(0x103, -21000, 3550, 151100, 0)
    SetChrPos(0x107, -21900, 3350, 150700, 0)
    SetChrPos(0x105, -20450, 3100, 150150, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x107, 0x5)
    OP_0D()

    #C0218
    ChrTalk(
        0x101,
        "#00010F#11P啧，这是什么！？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x105,
        (
            "#10408F#12P为了封锁战场而\x01",
            "围设的带刺铁线……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#00201F#12P战斗似乎发生在\x01",
            "我们上方。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#00007F#11P没办法……\x01",
            "迂回前进，寻找其它道路吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -19790, 3280, 150550, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x1A2, 6)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_99_D7DA end

    def Function_100_D951(): pass

    label("Function_100_D951")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x1)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("apl/ch51708.itc", 0x32)
    LoadChrToIndex("apl/ch51709.itc", 0x33)
    LoadChrToIndex("apl/ch51775.itc", 0x34)
    LoadChrToIndex("chr/ch00050.itc", 0x37)
    LoadChrToIndex("chr/ch00250.itc", 0x41)
    LoadChrToIndex("chr/ch03150.itc", 0x55)
    LoadChrToIndex("chr/ch02750.itc", 0x50)
    LoadChrToIndex("chr/ch03250.itc", 0x3C)
    LoadChrToIndex("chr/ch0325A.itc", 0x3D)
    LoadChrToIndex("chr/ch03257.itc", 0x3E)
    LoadEffect(0x0, "event/ev17048.eff")
    LoadEffect(0x1, "event/eva01_01.eff")
    SoundLoad(863)
    SoundLoad(864)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 0x32)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x1F)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    StopEffect(0x9, 0x0)
    StopEffect(0xA, 0x0)
    OP_F3(100000)
    ClearScenarioFlags(0x0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 0)), scpexpr(EXPR_END)), "loc_DA6F")
    SetScenarioFlags(0x0, 4)

    label("loc_DA6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 1)), scpexpr(EXPR_END)), "loc_DA7B")
    SetScenarioFlags(0x0, 4)

    label("loc_DA7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 2)), scpexpr(EXPR_END)), "loc_DA87")
    SetScenarioFlags(0x0, 4)

    label("loc_DA87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 3)), scpexpr(EXPR_END)), "loc_DA93")
    SetScenarioFlags(0x0, 4)

    label("loc_DA93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 4)), scpexpr(EXPR_END)), "loc_DA9F")
    SetScenarioFlags(0x0, 4)

    label("loc_DA9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 5)), scpexpr(EXPR_END)), "loc_DAAB")
    SetScenarioFlags(0x0, 4)

    label("loc_DAAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 6)), scpexpr(EXPR_END)), "loc_DAB7")
    SetScenarioFlags(0x0, 4)

    label("loc_DAB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 7)), scpexpr(EXPR_END)), "loc_DAC3")
    SetScenarioFlags(0x0, 4)

    label("loc_DAC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 0)), scpexpr(EXPR_END)), "loc_DACF")
    SetScenarioFlags(0x0, 4)

    label("loc_DACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 1)), scpexpr(EXPR_END)), "loc_DADB")
    SetScenarioFlags(0x0, 4)

    label("loc_DADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 2)), scpexpr(EXPR_END)), "loc_DAE7")
    SetScenarioFlags(0x0, 4)

    label("loc_DAE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 3)), scpexpr(EXPR_END)), "loc_DAF3")
    SetScenarioFlags(0x0, 4)

    label("loc_DAF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB02")
    OP_2C(0xAF, 0x1)

    label("loc_DB02")

    SetChrPos(0x101, 3800, 0, 134250, 95)
    SetChrPos(0x106, 2800, 0, 135300, 95)
    SetChrPos(0x103, 1650, 0, 133250, 95)
    SetChrPos(0x107, 900, 0, 131850, 95)
    SetChrPos(0x105, 750, 0, 134500, 95)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_52(0x107, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x20, 10700, 10000, 152000, 180)
    SetChrPos(0x21, 22750, 14000, 155150, 225)
    SetChrPos(0x22, 7000, 15000, 165350, 180)
    SetChrPos(0x23, -6000, 0, 129500, 95)
    SetChrPos(0x24, -5350, 0, 142650, 140)
    SetChrPos(0x25, 15250, 0, 123500, 320)
    SetChrPos(0x26, 18500, 0, 131500, 275)
    OP_68(3000, 1000, 134200, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(6250, 1000, 133850, 2500)
    MoveCamera(50, 25, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(22000, 2500)
    FadeToBright(1000, 0)

    def lambda_DC63():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DC63)
    Sleep(10)

    def lambda_DC7B():
        OP_9B(0x0, 0x106, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_DC7B)
    Sleep(10)

    def lambda_DC93():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DC93)
    Sleep(10)

    def lambda_DCAB():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DCAB)
    Sleep(10)

    def lambda_DCC3():
        OP_9B(0x0, 0x107, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_DCC3)
    Sleep(10)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0222
    ChrTalk(
        0x101,
        "#00005F#5P……？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0223
    ChrTalk(
        0x106,
        "#10707F#6P#4S罗伊德警官！\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    ReplaceBGM(-1, -1)
    Sound(567, 0, 100, 0)
    OP_68(7950, 1000, 135000, 300)
    MoveCamera(50, 20, 0, 300)
    OP_6E(510, 300)
    SetCameraDistance(24000, 300)
    SetChrFlags(0x106, 0x20)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x106, 0x3D)
    SetChrSubChip(0x106, 0x1)
    Sound(251, 0, 100, 0)
    OP_96(0x106, 0x1F40, 0x0, 0x20F26, 0x2710, 0x0)

    def lambda_DDBC():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DDBC)
    SetChrChipByIndex(0x106, 0x3C)
    SetChrSubChip(0x106, 0x0)
    OP_93(0x106, 0x5, 0x3E8)
    SetChrChipByIndex(0x106, 0x3E)
    SetChrSubChip(0x106, 0x0)
    PlayEffect(0x0, 0xFF, 0x106, 0x5, 0, 800, -1200, 180, 45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x106, 0x5, 0, 1200, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetCameraDistance(20530, 500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(361, 0, 100, 0)
    Sound(566, 0, 60, 0)
    OP_A6(0x106, 0x0, 0x14, 0x1F4, 0xBB8)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sleep(300)
    CancelBlur(0)

    def lambda_DE9B():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DE9B)
    Sleep(50)

    def lambda_DEAB():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DEAB)
    Sleep(50)

    def lambda_DEBB():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DEBB)
    Sleep(50)

    def lambda_DECB():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_DECB)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)

    #C0224
    ChrTalk(
        0x105,
        "#10410F#6P狙击吗……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5, 0x1F4)

    #C0225
    ChrTalk(
        0x103,
        "#00207F#12P在那里！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    Fade(500)
    OP_68(9000, 4400, 147650, 0)
    MoveCamera(35, -8, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_68(9860, 10000, 150940, 4000)
    MoveCamera(40, 4, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(18000, 4000)
    SetChrFlags(0x20, 0x800)
    OP_6F(0x79)

    #C0226
    ChrTalk(
        0x20,
        (
            "#5P不愧是『银』，\x01",
            "竟然能察觉到我。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#00010F#11P啧……\x01",
            "早有埋伏吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x20,
        (
            "#5P你们从隧道穿行时，\x01",
            "我们就已经发觉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x20,
        (
            "#5P话说回来，在这种戒严状态下，\x01",
            "你们居然还能出没于自治州各地。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x20,
        (
            "#5P想必是乘坐了那位骑士的\x01",
            "作战艇——梅尔卡瓦吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x105,
        (
            "#10402F#11P……哎，\x01",
            "已经掌握到我的身份了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x20,
        (
            "#5P你们特意来此，\x01",
            "多半是想与反抗军联手吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x20,
        (
            "#5P可惜你们来迟了一步，\x01",
            "扫荡作战已经开始了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(11210, 11800, 153420, 2000)
    MoveCamera(23, 4, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(20580, 2000)
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x20, 0x33)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x2)
    OP_0D()
    OP_6F(0x79)
    Sound(863, 2, 100, 0)
    Sound(864, 2, 80, 0)

    #C0234
    ChrTalk(
        0x20,
        (
            "#5P虽然多少会花点力气，\x01",
            "但相信用不了多久就能镇压完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x20,
        (
            "#5P不好意思，你们就在那里\x01",
            "边咬手指边看好戏吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        "#00007F#11P啧……岂能如你所愿！\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x106,
        (
            "#10707F#11P还是由我和蔡特\x01",
            "发起突破……！\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x20,
        "#5P休想得逞。\x02",
    )

    CloseMessageWindow()
    StopSound(864, 1000, 100)
    StopSound(863, 1000, 80)
    Fade(250)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 0x34)
    OP_A0(0x20, 1500, 0x0, 0x1)
    Sound(947, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0x101, 0x37)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x5F, 0x0)
    SetChrChipByIndex(0x103, 0x41)
    SetChrSubChip(0x103, 0x0)
    OP_93(0x103, 0x8C, 0x0)
    SetChrChipByIndex(0x105, 0x55)
    SetChrSubChip(0x105, 0x0)
    OP_93(0x105, 0x140, 0x0)
    SetChrChipByIndex(0x107, 0x50)
    SetChrSubChip(0x107, 0x0)
    OP_93(0x107, 0x113, 0x0)
    SetChrChipByIndex(0x106, 0x3C)
    SetChrSubChip(0x106, 0x0)
    SetChrPos(0x106, 6780, 0, 134950, 5)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    OP_68(6250, 1000, 133850, 5000)
    MoveCamera(50, 30, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(23000, 5000)
    BeginChrThread(0x21, 1, 0, 101)
    BeginChrThread(0x22, 1, 0, 102)
    StopBGM(0xFA0)
    Sleep(3000)
    BeginChrThread(0x32, 1, 0, 71)
    BeginChrThread(0x23, 3, 0, 56)

    def lambda_E342():
        OP_95(0xFE, 1300, 0, 131450, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_E342)
    Sleep(100)
    BeginChrThread(0x24, 3, 0, 56)

    def lambda_E365():
        OP_95(0xFE, 1750, 0, 136900, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_E365)
    Sleep(100)
    BeginChrThread(0x25, 3, 0, 56)

    def lambda_E388():
        OP_95(0xFE, 8390, 0, 129310, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_E388)
    Sleep(100)
    BeginChrThread(0x26, 3, 0, 56)

    def lambda_E3AB():
        OP_95(0xFE, 11450, 0, 133150, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_E3AB)
    WaitChrThread(0x23, 1)
    BeginChrThread(0x23, 3, 0, 57)
    WaitChrThread(0x24, 1)
    BeginChrThread(0x24, 3, 0, 57)
    WaitChrThread(0x25, 1)
    BeginChrThread(0x25, 3, 0, 57)
    WaitChrThread(0x26, 1)
    EndChrThread(0x32, 0x1)
    BeginChrThread(0x26, 3, 0, 57)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x22, 1)
    OP_6F(0x79)

    #C0239
    ChrTalk(
        0x106,
        "#10701F#11P……！\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x107,
        "#01201F#11P#3C唔，被包围了啊。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x105,
        "#10408F#12P真是有点不妙呢……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7455", 0)
    Fade(500)
    SetChrChipByIndex(0x20, 0x33)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x2)
    OP_68(10700, 10600, 152000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18000, 800)
    OP_0D()
    OP_6F(0x79)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 100, 0)
    OP_A1(0x20, 0x5DC, 0x2, 0x1, 0x2)
    Sleep(300)

    #C0242
    ChrTalk(
        0x20,
        (
            "#5P罗伊德·班宁斯\x01",
            "及其党羽……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x20,
        (
            "#5P『赤色星座』的连队长\x01",
            "『闪击』加雷斯来当你们的对手。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(6250, 1000, 133850, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22000, 0)
    OP_0D()

    #C0244
    ChrTalk(
        0x101,
        (
            "#00007F#5P唔……\x01",
            "各位，准备迎击！\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x103,
        (
            "#00207F#5P一定要随时注意\x01",
            "山崖上方的狙击！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    EndChrThread(0x21, 0x3)
    EndChrThread(0x22, 0x3)
    EndChrThread(0x23, 0x3)
    EndChrThread(0x24, 0x3)
    EndChrThread(0x25, 0x3)
    EndChrThread(0x26, 0x3)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x6)
    SetChrChipByIndex(0x22, 0x1F)
    SetChrSubChip(0x22, 0x6)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x6)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x6)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x6)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x6)

    def lambda_E5FC():
        OP_9D(0xFE, 0x1C52, 0x0, 0x20ADA, 0x1F4, 0x88B8)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_E5FC)

    def lambda_E619():
        OP_9D(0xFE, 0x1482, 0x0, 0x20ADA, 0x1F4, 0x88B8)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_E619)

    def lambda_E636():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_E636)

    def lambda_E653():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_E653)

    def lambda_E670():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_E670)

    def lambda_E68D():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_E68D)
    OP_24(0x35F)
    OP_24(0x360)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(20000, 200)
    Sleep(200)
    CancelBlur(200)
    Battle("BattleInfo_F14", 0x30200011, 0x0, 0x100, 0x17, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x22, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    EndChrThread(0x26, 0x1)
    Call(0, 103)
    Return()

    # Function_100_D951 end

    def Function_101_E6FE(): pass

    label("Function_101_E6FE")

    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    SetChrSubChip(0xFE, 0x6)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x4812, 0x2710, 0x24E3C, 0x3E8, 0x1770)
    BeginChrThread(0xFE, 3, 0, 56)
    OP_96(0xFE, 0x4268, 0x2710, 0x248C4, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x3C28, 0x1770, 0x22E66, 0x3E8, 0x1770)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 3, 0, 57)
    Return()

    # Function_101_E6FE end

    def Function_102_E777(): pass

    label("Function_102_E777")

    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    SetChrSubChip(0xFE, 0x6)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x1C52, 0x2710, 0x273BC, 0x3E8, 0x1770)
    BeginChrThread(0xFE, 3, 0, 56)
    OP_96(0xFE, 0x1FD6, 0x2710, 0x2576A, 0x1770, 0x0)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x1E14, 0x1770, 0x23668, 0x3E8, 0x1770)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 3, 0, 57)
    Return()

    # Function_102_E777 end

    def Function_103_E7F0(): pass

    label("Function_103_E7F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    SoundLoad(2768)
    SoundLoad(2769)
    SoundLoad(2770)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07900.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02100.itp")
    AddParty(0x3, 0xFF, 0xFF)
    OP_32(0x3, 0x0, 0x54)
    OP_32(0x3, 0x5, 0x64)
    OP_42(0x3, 0x42D, 0xFF)
    OP_42(0x3, 0x5ED, 0xFF)
    OP_42(0x3, 0x651, 0xFF)
    OP_38(0x3, 0x81, 0x2)
    OP_38(0x3, 0x83, 0x2)
    OP_38(0x3, 0x84, 0x2)
    OP_38(0x3, 0x85, 0x2)
    OP_42(0x3, 0x8D, 0x1)
    OP_42(0x3, 0x9F, 0x3)
    OP_42(0x3, 0x6E, 0x4)
    OP_42(0x3, 0x7E, 0x5)
    AddCraft(0x3, 0xB9)
    AddCraft(0x3, 0xBA)
    AddCraft(0x3, 0x12A)
    OP_D7(0x0)
    OP_D7(0x10)
    OP_D7(0x11)
    OP_D7(0x12)
    OP_D7(0x13)
    OP_D7(0x14)
    OP_D7(0x15)
    OP_D7(0x16)
    OP_D7(0x17)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("apl/ch51709.itc", 0x32)
    LoadChrToIndex("apl/ch51710.itc", 0x33)
    LoadChrToIndex("chr/ch41951.itc", 0x34)
    LoadChrToIndex("chr/ch41952.itc", 0x35)
    LoadChrToIndex("chr/ch42051.itc", 0x5A)
    LoadChrToIndex("chr/ch42050.itc", 0x5B)
    LoadChrToIndex("chr/ch42052.itc", 0x5C)
    LoadChrToIndex("chr/ch42056.itc", 0x5D)
    LoadChrToIndex("chr/ch31251.itc", 0x23)
    LoadChrToIndex("chr/ch31252.itc", 0x24)
    LoadChrToIndex("chr/ch31351.itc", 0x5F)
    LoadChrToIndex("chr/ch31350.itc", 0x60)
    LoadChrToIndex("chr/ch31352.itc", 0x61)
    LoadChrToIndex("apl/ch50112.itc", 0x64)
    LoadChrToIndex("apl/ch50118.itc", 0x65)
    LoadChrToIndex("apl/ch50113.itc", 0x66)
    LoadChrToIndex("chr/ch00050.itc", 0x37)
    LoadChrToIndex("chr/ch00250.itc", 0x41)
    LoadChrToIndex("chr/ch03150.itc", 0x55)
    LoadChrToIndex("chr/ch02750.itc", 0x50)
    LoadChrToIndex("chr/ch03250.itc", 0x3C)
    LoadChrToIndex("chr/ch00352.itc", 0x46)
    LoadChrToIndex("chr/ch0035E.itc", 0x47)
    LoadChrToIndex("chr/ch32650.itc", 0x25)
    LoadChrToIndex("chr/ch32651.itc", 0x26)
    LoadChrToIndex("chr/ch32654.itc", 0x27)
    LoadChrToIndex("chr/ch06000.itc", 0x21)
    LoadChrToIndex("apl/ch50010.itc", 0x22)
    LoadEffect(0x0, "event/ev14020.eff")
    LoadEffect(0x1, "battle/sp003000.eff")
    LoadEffect(0x2, "battle/ms00000.eff")
    LoadEffect(0x3, "battle/btgun00.eff")
    LoadEffect(0x4, "event/eva01_01.eff")
    LoadEffect(0x8, "event/eva02_00.eff")
    SoundLoad(110)
    SoundLoad(974)
    SoundLoad(865)
    SoundLoad(863)
    SoundLoad(861)
    SetChrChipByIndex(0x101, 0x37)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x41)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0x55)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x50)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x106, 0x3C)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0x20, 0x32)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x1E)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    SetChrChipByIndex(0x22, 0x1E)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    ClearChrFlags(0x24, 0x80)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    ClearChrFlags(0x25, 0x80)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    ClearChrFlags(0x26, 0x80)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x34)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x34)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x5A)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x5A)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x5A)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x11, 0x5F)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x5F)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x5F)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x27, 0x65)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x65)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    SetChrChipByIndex(0x29, 0x65)
    SetChrSubChip(0x29, 0x0)
    SetChrFlags(0x29, 0x8000)
    SetChrChipByIndex(0x2A, 0x65)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2B, 0x65)
    SetChrSubChip(0x2B, 0x0)
    SetChrFlags(0x2B, 0x8000)
    SetChrChipByIndex(0x1E, 0x25)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    StopEffect(0x9, 0x0)
    StopEffect(0xA, 0x0)
    OP_52(0x107, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 7780, 0, 133900, 95)
    SetChrPos(0x106, 6780, 0, 134950, 5)
    SetChrPos(0x103, 5630, 0, 132900, 140)
    SetChrPos(0x107, 4880, 0, 131500, 275)
    SetChrPos(0x105, 4730, 0, 134150, 320)
    SetChrPos(0x104, 21900, 14000, 153900, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x20, 10700, 10000, 152000, 180)
    SetChrPos(0x21, 9800, 0, 137600, 220)
    SetChrPos(0x22, 5200, 0, 138500, 180)
    SetChrPos(0x23, 1300, 0, 131450, 75)
    SetChrPos(0x24, 1750, 0, 136900, 130)
    SetChrPos(0x25, 8390, 0, 129310, 310)
    SetChrPos(0x26, 11450, 0, 133150, 280)
    BeginChrThread(0x21, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x22, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x23, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x24, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x25, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x26, 3, 0, 57)
    OP_68(6250, 1000, 133850, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(23000, 2000)
    PlayBGM("ed7582", 0)
    Sound(110, 2, 30, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0246
    ChrTalk(
        0x101,
        (
            "#00010F#5P……呜……\x01",
            "不愧是『赤色星座』……！\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x105,
        (
            "#10410F#12P从高处发动的狙击\x01",
            "竟有这么强的威胁性……！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    EndChrThread(0x21, 0x3)
    EndChrThread(0x22, 0x3)
    EndChrThread(0x23, 0x3)
    EndChrThread(0x24, 0x3)
    EndChrThread(0x25, 0x3)
    EndChrThread(0x26, 0x3)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    OP_68(10700, 10600, 152000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(300)

    #C0248
    ChrTalk(
        0x20,
        (
            "#5P不愧是少爷的同事，很不错\x01",
            "的反应。      \x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x20,
        (
            "#5P但从战术角度来说，\x01",
            "被狙击兵占据高地\x01",
            "便意味着绝对的失败。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x20,
        "#5P你们还是老老实实地投——\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    StopSound(110, 4000, 20)
    Sound(973, 0, 100, 0)
    Sleep(800)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x20, 0x13B, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0251
    ChrTalk(
        0x20,
        "#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        "#00005F#11P刚才那是……！\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        "#00202F#11P莫、莫非……\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x107,
        "#01203F#11P#3C嗯，看来赶上了。\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    OP_68(8700, 10600, 153000, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x15, 15600, 21000, 37950, 195)
    SetChrPos(0x16, 13450, 21000, 42250, 195)
    SetChrPos(0x17, 10650, 21000, 43650, 195)
    SetChrPos(0x18, 15600, 21000, 37950, 195)
    SetChrPos(0x19, 13450, 21000, 42250, 195)
    SetChrPos(0x1A, 10650, 21000, 43650, 195)
    SetChrPos(0x23, 16900, 21000, 40050, 235)
    SetChrPos(0x24, 5550, 21000, 43750, 145)
    SetChrPos(0x27, 17200, 21000, 40500, 180)
    SetChrPos(0x28, 11150, 21000, 43950, 180)
    SetChrPos(0x29, 14600, 21000, 42050, 180)
    SetChrPos(0x2A, 15450, 21000, 40850, 180)
    SetChrPos(0x2B, 14150, 21000, 42150, 180)
    SetChrPos(0xD, 18850, 21000, 37900, 225)
    SetChrPos(0xE, 10000, 21000, 43900, 180)
    SetChrPos(0xF, 16350, 21000, 40850, 180)
    SetChrPos(0x11, 18850, 21000, 37400, 180)
    SetChrPos(0x12, 15600, 21000, 37950, 180)
    SetChrPos(0x13, 18600, 21000, 39500, 180)
    SetChrPos(0x1E, 12200, 21000, 42800, 180)
    OP_68(14320, 15500, 34850, 0)
    MoveCamera(55, 5, -5, 0)
    SetCameraDistance(21000, 0)
    OP_68(12250, 15900, 33850, 8000)
    MoveCamera(65, 25, -5, 8000)
    SetCameraDistance(23500, 8000)
    OP_11(0xFF, 0xFF, 0xFF, 0x1E, 0x1F4, 0x0)
    BeginChrThread(0x32, 1, 0, 141)
    FadeToBright(1000, 0)
    BeginChrThread(0x24, 1, 0, 122)
    BeginChrThread(0x23, 1, 0, 121)
    BeginChrThread(0x17, 1, 0, 113)
    BeginChrThread(0x1A, 1, 0, 119)
    BeginChrThread(0x16, 1, 0, 111)
    BeginChrThread(0x18, 1, 0, 115)
    BeginChrThread(0x15, 1, 0, 109)
    BeginChrThread(0x19, 1, 0, 117)
    BeginChrThread(0x27, 1, 0, 135)
    BeginChrThread(0x28, 1, 0, 136)
    BeginChrThread(0x29, 1, 0, 137)
    BeginChrThread(0x1E, 1, 0, 125)
    BeginChrThread(0xD, 1, 0, 127)
    BeginChrThread(0xE, 1, 0, 128)
    BeginChrThread(0xF, 1, 0, 129)
    BeginChrThread(0x11, 1, 0, 130)
    BeginChrThread(0x12, 1, 0, 131)
    BeginChrThread(0x13, 1, 0, 132)
    BeginChrThread(0x2A, 1, 0, 138)
    BeginChrThread(0x2B, 1, 0, 139)
    Sleep(8000)
    Fade(500)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x19, 0x1)
    Sound(865, 2, 50, 0)
    Sound(861, 2, 50, 0)
    SetChrChipByIndex(0x15, 0x35)
    BeginChrThread(0x15, 0, 0, 49)
    BeginChrThread(0x15, 3, 0, 50)
    SetChrChipByIndex(0x16, 0x35)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x16, 3, 0, 50)
    SetChrChipByIndex(0x17, 0x35)
    BeginChrThread(0x17, 0, 0, 49)
    BeginChrThread(0x17, 3, 0, 50)
    SetChrChipByIndex(0x18, 0x5B)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x5B)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x5B)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x23, 0x1E)
    BeginChrThread(0x23, 3, 0, 57)
    SetChrChipByIndex(0x24, 0x1E)
    BeginChrThread(0x24, 3, 0, 57)
    SetChrPos(0x15, 11300, 8000, 21350, 0)
    SetChrPos(0x16, 22150, 12000, 20940, 315)
    SetChrPos(0x17, 19200, 12000, 19100, 0)
    SetChrPos(0x18, 15050, 8000, 23450, 0)
    SetChrPos(0x19, 16850, 8000, 23000, 0)
    SetChrPos(0x1A, 8300, 8000, 19300, 45)
    SetChrPos(0x23, 13500, 8000, 25150, 0)
    SetChrPos(0x24, 14450, 12000, 18100, 0)
    OP_68(17990, 13000, 30170, 0)
    MoveCamera(125, 35, -10, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(30000, 4000)
    OP_82(0x0, 0x64, 0xBB8, 0xFA0)
    Sleep(4000)
    Fade(500)
    OP_68(14600, 12800, 29330, 0)
    MoveCamera(62, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(33000, 0)
    SetCameraDistance(37000, 4000)
    OP_82(0x0, 0x64, 0xBB8, 0xFA0)
    Sleep(2000)
    StopSound(865, 900, 40)
    StopSound(861, 900, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x64, 0xBB8, 0x0)
    StopSound(974, 1000, 50)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x11, 0x1)
    ClearChrFlags(0x18, 0x20)
    ClearChrFlags(0x11, 0x20)
    EndChrThread(0x23, 0x3)
    EndChrThread(0x24, 0x3)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    OP_11(0xFF, 0xFF, 0xFF, 0x1E, 0x96, 0x0)
    SetChrPos(0x20, 11400, 10000, 153550, 315)
    OP_68(9400, 10600, 154550, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(11400, 10600, 153550, 2000)
    Sound(863, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0255
    ChrTalk(
        0x20,
        "#11P啧……是狼！？\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x103,
        "#00214F#11P是蔡特的部下们……！\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x101,
        (
            "#00002F#11P还有……\x01",
            "那是米蕾优他们！？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x20,
        (
            "#11P唔……\x01",
            "不过是群野兽而已！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x20,
        (
            "#11P好！\x01",
            "我们就来两面夹击……\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    #N0260
    NpcTalk(
        0x104,
        "青年的声音",
        "#2768V#15A#30W哪有那么容易，加雷斯。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x20, 0x5A, 0x1F4)
    Fade(500)
    OP_68(21900, 15000, 153900, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(14500, 0)
    SetChrChipByIndex(0x104, 0x46)
    SetChrSubChip(0x104, 0x5)
    OP_0D()
    OP_68(10700, 11200, 153480, 1000)
    MoveCamera(37, 26, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(17100, 1000)
    SetChrSubChip(0x104, 0x1)
    Sound(2293, 255, 100, 0)    #voice#Randy
    Sound(844, 0, 100, 0)
    OP_9D(0x104, 0x31CE, 0x2710, 0x25706, 0x3E8, 0x1388)
    Fade(100)
    Sound(532, 0, 100, 0)
    SetChrChipByIndex(0x20, 0x33)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x2)
    SetChrSubChip(0x104, 0x2)
    OP_0D()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    PlayEffect(0x4, 0xFF, 0x20, 0x5, 0, 1200, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(372, 0, 60, 0)
    Sound(566, 0, 70, 0)
    SetChrSubChip(0x104, 0x3)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x1000)
    OP_9B(0x1, 0x20, 0x0, 0xFFFFF63C, 0x2710, 0x0)
    ClearChrFlags(0x20, 0x20)
    ClearChrFlags(0x20, 0x1000)

    #C0261
    ChrTalk(
        0x20,
        "#5P噢！？\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        "#00202F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x107,
        "#01200F#11P#3C呵……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        "#00005F#11P兰、兰迪！？\x02",
    )

    CloseMessageWindow()
    MoveCamera(27, 26, 0, 20000)
    OP_A1(0x104, 0x5DC, 0x2, 0x4, 0x5)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0265
    ChrTalk(
        0x104,
        (
            "#00304F#2769V#11P嘿，好久不见啦。\x02\x03",

            "#00302F#2770V想说的话实在是堆积如山，\x01",
            "但还是稍后再聊吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xAD2)
    OP_C9(0x1, 0x80000000)
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x20, 0x32)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x2)
    OP_0D()
    Sleep(300)

    #C0266
    ChrTalk(
        0x20,
        "#5P少爷……果然厉害啊。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x20,
        (
            "#5P竟然能绕到\x01",
            "我这狙击兵的身后。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x104,
        (
            "#00306F#11P呼，但如果没有那些狼帮忙，\x01",
            "情况恐怕会很危险呢。\x02\x03",

            "#00301F另外，你的注意力完全集中\x01",
            "在了罗伊德他们身上，这可是严重失误。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x20,
        "#5P说的没错。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x20,
        (
            "#5P……话说回来，少爷，\x01",
            "你还在用那种武器啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x20,
        (
            "#5P在手中没有来复枪的情况下，\x01",
            "你觉得能战胜我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x104,
        (
            "#00305F#11P嗯？我并没说\x01",
            "不用这东西啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x47)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(300)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0273
    ChrTalk(
        0x104,
        (
            "#00300F#11P之前已经请基约姆大叔\x01",
            "帮我修理好了。\x02\x03",

            "#00306F另外，无论多么强劲，\x01",
            "如果机关部位受到损伤，\x01",
            "手感也会有所下降的。\x02\x03",

            "#00302F所以我只在关键时刻才会使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x20,
        "#5P……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x20,
        (
            "#5P的确，在经受刚才那一击之后，\x01",
            "我这把来复枪的精准度已经降低了。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x20,
        "#5P看来现在的形势对我们相当不利呢。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        (
            "#00303F#11P嗯，赶快撤退吧。\x02\x03",

            "#00307F另外，替我转告叔叔……\x01",
            "我一定会打倒他！\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x20,
        "#5P明白了。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x20,
        (
            "#5P少爷，和前段时间相比，\x01",
            "你真是大有长进了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(8380, 11000, 154390, 1000)
    OP_93(0x20, 0x13B, 0x1F4)
    OP_6F(0x1)
    Sound(947, 0, 100, 0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0280
    ChrTalk(
        0x20,
        (
            "#11P#4S作战中断！\x01",
            "撤退至地点Ｄ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("众猎兵")

    #A0281
    AnonymousTalk(
        0xFF,
        "#4S是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x32, 1, 0, 141)
    StopSound(863, 1000, 40)
    Fade(500)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x2)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x2)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x2)
    SetChrChipByIndex(0x11, 0x60)
    SetChrSubChip(0x11, 0x1)
    SetChrChipByIndex(0x12, 0x60)
    SetChrSubChip(0x12, 0x1)
    SetChrChipByIndex(0x13, 0x60)
    SetChrSubChip(0x13, 0x1)
    SetChrChipByIndex(0x1E, 0x25)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x15, 11300, 8000, 21350, 0)
    SetChrPos(0x16, 22150, 12000, 20940, 315)
    SetChrPos(0x17, 19200, 12000, 19100, 0)
    SetChrPos(0x18, 13500, 8000, 23700, 315)
    SetChrPos(0x19, 16850, 8000, 23000, 315)
    SetChrPos(0x1A, 8300, 8000, 19300, 45)
    SetChrPos(0x25, 13500, 8000, 25150, 315)
    SetChrPos(0x26, 14450, 12000, 18100, 0)
    SetChrPos(0x27, 17600, 12000, 30300, 180)
    SetChrPos(0x28, 13900, 12000, 33350, 225)
    SetChrPos(0x29, 8950, 12000, 36650, 180)
    SetChrPos(0x2A, 13650, 8000, 28530, 180)
    SetChrPos(0x2B, 14150, 16000, 38400, 180)
    SetChrPos(0xD, 14050, 12000, 31950, 225)
    SetChrPos(0xE, 11100, 12000, 35250, 180)
    SetChrPos(0xF, 17700, 16000, 36750, 225)
    SetChrPos(0x11, 15950, 8000, 26850, 225)
    SetChrPos(0x12, 16050, 12000, 30400, 180)
    SetChrPos(0x13, 18250, 8000, 24600, 270)
    SetChrPos(0x1E, 12100, 16000, 39450, 180)
    OP_11(0xFF, 0xFF, 0xFF, 0x1E, 0x1F4, 0x0)
    OP_68(13500, 16950, 33900, 0)
    MoveCamera(66, 20, 5, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    OP_68(13500, 14950, 33900, 5000)
    SetCameraDistance(22000, 5000)
    OP_0D()
    Sound(973, 0, 70, 0)
    BeginChrThread(0x27, 1, 0, 140)
    BeginChrThread(0x28, 1, 0, 140)
    BeginChrThread(0x29, 1, 0, 140)
    BeginChrThread(0x2A, 1, 0, 140)
    BeginChrThread(0x2B, 1, 0, 140)
    Sleep(4000)
    Fade(500)
    BeginChrThread(0x25, 1, 0, 123)
    BeginChrThread(0x18, 1, 0, 116)
    BeginChrThread(0x15, 1, 0, 110)
    BeginChrThread(0x19, 1, 0, 118)
    BeginChrThread(0x1A, 1, 0, 120)
    BeginChrThread(0x16, 1, 0, 112)
    BeginChrThread(0x17, 1, 0, 114)
    BeginChrThread(0x26, 1, 0, 124)
    OP_68(12380, 9100, 24480, 0)
    MoveCamera(75, 15, 0, 0)
    SetCameraDistance(20000, 0)
    OP_68(15030, 8500, 24830, 8000)
    MoveCamera(65, 20, 5, 8000)
    SetCameraDistance(35000, 8000)
    Sound(973, 0, 60, 0)
    Sleep(6000)
    StopSound(974, 2000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x25, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x26, 0x1)
    EndChrThread(0x27, 0x1)
    EndChrThread(0x28, 0x1)
    EndChrThread(0x29, 0x1)
    EndChrThread(0x2A, 0x1)
    EndChrThread(0x2B, 0x1)
    OP_11(0xFF, 0xFF, 0xFF, 0x1E, 0x96, 0x0)
    StopBGM(0x1770)
    WaitBGM()
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    SetChrPos(0x101, -13100, 0, 138500, 270)
    SetChrPos(0x103, -12250, 0, 137300, 270)
    SetChrPos(0x104, -19350, 4000, 152500, 180)
    SetChrPos(0x105, -13100, 0, 138500, 270)
    SetChrPos(0x106, -12250, 0, 137300, 270)
    SetChrPos(0x107, -11100, 0, 138500, 270)
    SetChrPos(0x1E, -26650, 0, 131150, 45)
    SetChrPos(0x1F, -19350, 4000, 152500, 180)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7569", 0)
    OP_68(-19350, 5000, 152500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_68(-20250, 1000, 142000, 5000)
    MoveCamera(45, 25, 0, 5000)
    SetCameraDistance(19000, 5000)

    def lambda_1016F():
        OP_95(0xFE, -20250, 0, 142650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1016F)
    FadeToBright(1000, 0)
    Sleep(3000)
    BeginChrThread(0x101, 1, 0, 104)
    Sleep(200)
    BeginChrThread(0x103, 1, 0, 105)
    Sleep(500)
    BeginChrThread(0x105, 1, 0, 106)
    Sleep(300)
    BeginChrThread(0x106, 1, 0, 107)
    Sleep(300)
    BeginChrThread(0x107, 1, 0, 108)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0282
    ChrTalk(
        0x101,
        "#00014F#12P兰迪……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0283
    ChrTalk(
        0x103,
        "#00214F#11P……兰迪前辈！\x02",
    )

    WaitChrThread(0x106, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)
    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    #Sound(2364, 255, 100, 0)    #voice#Randy

    #A0284
    AnonymousTalk(
        0x104,
        (
            "哟，大家辛苦了。\x02\x03",

            "没想到你们竟然会\x01",
            "跑到这里啊……\x02\x03",

            "罗伊德，阿缇，\x01",
            "你们没事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0285
    ChrTalk(
        0x101,
        "#00002F#12P嗯，彼此彼此……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x103,
        "#00202F#11P你也……顺利逃脱了啊？\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x104,
        (
            "#00304F#5P嗯，费了一番工夫，总算是独力\x01",
            "逃了出来，之后就和米蕾优他们会合了。\x02\x03",

            "#00301F这段时间，我们一直在\x01",
            "这一带展开反抗作战……\x02\x03",

            "#00306F这次本以为\x01",
            "彻底完蛋了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        (
            "#00012F#12P是吗……\x01",
            "最终大家都没事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x103,
        (
            "#00204F#11P这多亏蔡特的\x01",
            "部下们帮忙啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x107, 500)
    Sleep(100)

    #C0290
    ChrTalk(
        0x104,
        (
            "#00304F#6P嗯，就在我们陷入危机的时候，\x01",
            "它们突然赶来支援。\x02\x03",

            "#00302F莫非是你\x01",
            "把它们叫来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x107,
        (
            "#01203F#11P#3C嗯，出于保险。\x02\x03",

            "#01200F我之前就叮嘱过它们，\x01",
            "让它们多注意猎兵们的行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x104,
        "#00309F#6P嘿，原来如此……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0293
    ChrTalk(
        0x104,
        (
            "#00307F#6P#4S嗯……哎哎！？\x02\x03",

            "#4S你……你为什么会说话！？\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        "#00012F#12P哈哈……\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x103,
        "#00202F#11P很吃惊吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    TurnDirection(0x104, 0x105, 500)
    Sleep(500)
    TurnDirection(0x104, 0x106, 500)

    #C0296
    ChrTalk(
        0x104,
        (
            "#00305F#5P嗯？仔细一看，\x01",
            "瓦吉还打扮得那么奇怪……\x02\x03",

            "#00307F而且连莉夏也在！？\x01",
            "你怎么会和罗伊德他们在一起！？\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        "#10404F#6P哎呀呀。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x106,
        "#10709F#12P嘻嘻……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1E, 0x80)

    #N0299
    NpcTalk(
        0x1E,
        "女性的声音",
        "#5P兰迪！\x02",
    )

    OP_64(0x104)
    CloseMessageWindow()
    Fade(500)
    OP_68(-26650, 1000, 131150, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(-21000, 1000, 141150, 2000)
    MoveCamera(40, 20, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(21000, 2000)
    SetChrPos(0x107, -18250, 0, 142700, 0)
    SetChrChipByIndex(0x1E, 0x26)

    def lambda_1073C():
        OP_96(0x1E, 0xFFFFA84E, 0x0, 0x22024, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1073C)

    def lambda_10756():
        OP_92(0x101, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10756)
    Sleep(0)

    def lambda_1076C():
        OP_92(0x103, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1076C)
    Sleep(0)

    def lambda_10782():
        OP_92(0x104, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10782)
    Sleep(0)

    def lambda_10798():
        OP_92(0x105, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10798)
    Sleep(0)

    def lambda_107AE():
        OP_92(0x106, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_107AE)
    Sleep(0)

    def lambda_107C4():
        OP_92(0x107, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_107C4)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    WaitChrThread(0x1E, 1)
    SetChrChipByIndex(0x1E, 0x25)
    SetChrSubChip(0x1E, 0x0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0300
    AnonymousTalk(
        0x1E,
        (
            "确认完毕，敌方部队已经撤退了。\x02\x03",

            "如此一来，\x01",
            "我们又可以坚持一段时间了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0301
    ChrTalk(
        0x104,
        "#00302F#5P是吗……\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        "#00002F#5P米蕾优小姐，好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x103,
        "#00204F#11P你平安无事，真是太好了。\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x1E,
        (
            "#07904F#6P你们也一样……\x01",
            "大家都平安无事真好。\x02\x03",

            "#07902F……话说回来，你们的队伍成员\x01",
            "还真奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        "#00202F#11P嗯，事情的经过比较复杂。\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x105,
        (
            "#10402F#5P总之，我们先稍微休息一下，\x01",
            "然后就开始交换情报吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x80)
    FadeToDark(0, 16777215, -1)
    Sound(810, 0, 100, 0)
    OP_0D()
    Sleep(100)
    FadeToBright(650, 16777215)
    OP_0D()

    #N0307
    NpcTalk(
        0x1F,
        "女性的声音",
        "#4P嗯！非常赞成！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-21250, 1800, 140800, 3000)
    MoveCamera(35, 20, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(22000, 3000)

    def lambda_10AD8():
        OP_95(0xFE, -19850, 450, 144900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_10AD8)

    def lambda_10AF2():
        OP_92(0x101, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10AF2)
    Sleep(50)

    def lambda_10B08():
        OP_92(0x103, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10B08)
    Sleep(50)

    def lambda_10B1E():
        OP_92(0x104, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10B1E)
    Sleep(50)

    def lambda_10B34():
        OP_92(0x105, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10B34)
    Sleep(50)

    def lambda_10B4A():
        OP_92(0x106, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_10B4A)
    Sleep(50)

    def lambda_10B60():
        OP_92(0x107, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_10B60)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    WaitChrThread(0x1F, 1)
    OP_6F(0x79)

    #C0308
    ChrTalk(
        0x101,
        "#00011F#12P格、格蕾丝小姐！？\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x103,
        "#00205F#12P您怎么会在这里……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 4000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    OP_96(0x1F, 0xFFFFB65E, 0x1C2, 0x23604, 0x7D0, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    Sleep(50)
    Sound(810, 0, 100, 0)
    PlayEffect(0x8, 0xFF, 0x1F, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    OP_96(0x1F, 0xFFFFAE8E, 0x1C2, 0x23604, 0x7D0, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    Sleep(50)
    Sound(810, 0, 100, 0)
    PlayEffect(0x8, 0xFF, 0x1F, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    OP_96(0x1F, 0xFFFFB276, 0x1C2, 0x23604, 0x7D0, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    Sleep(50)
    Sound(810, 0, 100, 0)
    PlayEffect(0x8, 0xFF, 0x1F, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0310
    AnonymousTalk(
        0x1F,
        (
            "这个嘛～因为稍微出了点问题，\x01",
            "在克洛斯贝尔市已经待不下去了。\x02\x03",

            "所以我就以从军记者兼摄影师的身份\x01",
            "加入到兰迪他们这里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0311
    ChrTalk(
        0x1E,
        (
            "#07906F#6P#N呼……但我实在\x01",
            "不是很欢迎呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0312
    ChrTalk(
        0x104,
        (
            "#00309F#5P哈哈，情况就是这样。\x02\x03",

            "#00300F总之，我们似乎有必要\x01",
            "交流一下至今为止经历的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19370, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x6E)
    OP_24(0x3CE)
    OP_24(0x361)
    OP_24(0x35F)
    OP_24(0x35D)
    SetScenarioFlags(0x22, 4)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_103_E7F0 end

    def Function_104_10EDC(): pass

    label("Function_104_10EDC")

    OP_95(0xFE, -20250, 0, 141150, 5000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_104_10EDC end

    def Function_105_10EF8(): pass

    label("Function_105_10EF8")

    OP_95(0xFE, -18900, 0, 141140, 5000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_105_10EF8 end

    def Function_106_10F14(): pass

    label("Function_106_10F14")

    OP_95(0xFE, -22600, 0, 140700, 3000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_106_10F14 end

    def Function_107_10F30(): pass

    label("Function_107_10F30")

    OP_95(0xFE, -20400, 0, 139200, 3000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_107_10F30 end

    def Function_108_10F4C(): pass

    label("Function_108_10F4C")

    OP_95(0xFE, -17750, 0, 142700, 3000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_108_10F4C end

    def Function_109_10F6C(): pass

    label("Function_109_10F6C")

    Sleep(3000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x3CF0, 0x3E80, 0x943E, 0x1F4, 0x1388)
    Sound(326, 0, 50, 0)
    OP_95(0xFE, 17500, 16000, 35950, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x4556, 0x2EE0, 0x7D31, 0x1F4, 0x1388)
    Sound(326, 0, 50, 0)
    OP_95(0xFE, 18350, 12000, 28550, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_82(0x0, 0x64, 0xBB8, 0x3E8)
    SetChrChipByIndex(0xFE, 0x35)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(1000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    StopSound(865, 500, 40)
    StopSound(861, 500, 40)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 50, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_109_10F6C end

    def Function_110_11071(): pass

    label("Function_110_11071")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sleep(2000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    OP_95(0xFE, 11800, 8000, 25000, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 50, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_110_11071 end

    def Function_111_110E6(): pass

    label("Function_111_110E6")

    Sleep(2000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x348A, 0x3E80, 0xA50A, 0x1F4, 0x1388)
    OP_95(0xFE, 14000, 16000, 38300, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x3BF6, 0x2EE0, 0x83D6, 0x1F4, 0x1388)
    OP_95(0xFE, 16250, 12000, 30050, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_82(0x0, 0x64, 0xBB8, 0x7D0)
    SetChrChipByIndex(0xFE, 0x35)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(2000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_111_110E6 end

    def Function_112_111C1(): pass

    label("Function_112_111C1")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sleep(6000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x4BFA, 0x1F40, 0x59D8, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 12400, 8000, 26250, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_112_111C1 end

    def Function_113_11251(): pass

    label("Function_113_11251")

    Sleep(1000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x299A, 0x3E80, 0xAA82, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 10950, 16000, 40000, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x3070, 0x2EE0, 0x8CA0, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 13850, 12000, 32100, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sound(865, 2, 50, 0)
    Sound(861, 2, 50, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x7D0)
    SetChrChipByIndex(0xFE, 0x35)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(2000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_113_11251 end

    def Function_114_11356(): pass

    label("Function_114_11356")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sleep(7000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x474A, 0x1F40, 0x574E, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 11800, 8000, 25000, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_114_11356 end

    def Function_115_113EC(): pass

    label("Function_115_113EC")

    Sleep(2500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x3CF0, 0x3E80, 0x943E, 0x1F4, 0x1388)
    OP_95(0xFE, 17500, 16000, 35950, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x4556, 0x2EE0, 0x7D31, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 17350, 12000, 29450, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_115_113EC end

    def Function_116_114A1(): pass

    label("Function_116_114A1")

    SetChrChipByIndex(0xFE, 0x5B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    OP_95(0xFE, 11800, 8000, 25000, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_116_114A1 end

    def Function_117_11516(): pass

    label("Function_117_11516")

    Sleep(3500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x348A, 0x3E80, 0xA50A, 0x1F4, 0x1388)
    OP_95(0xFE, 12850, 16000, 39150, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x3BF6, 0x2EE0, 0x83D6, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 17350, 12000, 29450, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_117_11516 end

    def Function_118_115B9(): pass

    label("Function_118_115B9")

    SetChrChipByIndex(0xFE, 0x5B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(3000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    OP_95(0xFE, 12400, 8000, 26250, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_118_115B9 end

    def Function_119_1162E(): pass

    label("Function_119_1162E")

    Sleep(1500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x299A, 0x3E80, 0xAA82, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 9000, 16000, 40400, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x3070, 0x2EE0, 0x8CA0, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 17350, 12000, 29450, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_119_1162E end

    def Function_120_116D7(): pass

    label("Function_120_116D7")

    SetChrChipByIndex(0xFE, 0x5B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(4000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    OP_95(0xFE, 11800, 8000, 25000, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_120_116D7 end

    def Function_121_1174C(): pass

    label("Function_121_1174C")

    Sleep(500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x6)
    OP_9D(0xFE, 0x4204, 0x3E80, 0x9C72, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 14650, 16000, 38300, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrSubChip(0xFE, 0x6)
    OP_9D(0xFE, 0x4556, 0x2EE0, 0x7D31, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 17350, 12000, 29450, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_121_1174C end

    def Function_122_11810(): pass

    label("Function_122_11810")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x6)
    OP_9D(0xFE, 0x15AE, 0x3E80, 0xAAE6, 0x1F4, 0x1388)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 7700, 16000, 40750, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 70, 0)
    OP_9D(0xFE, 0x27A6, 0x2EE0, 0x8D68, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 12250, 12000, 33250, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(809, 0, 60, 0)
    OP_9D(0xFE, 0x34EE, 0x1F40, 0x7116, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_122_11810 end

    def Function_123_118D0(): pass

    label("Function_123_118D0")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1F)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 12400, 8000, 26250, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 60, 0)
    OP_9D(0xFE, 0x2486, 0xFA0, 0x70E4, 0x1F4, 0xFA0)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 3350, 4000, 34900, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_123_118D0 end

    def Function_124_1194E(): pass

    label("Function_124_1194E")

    Sleep(5000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1F)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 14450, 12000, 19000, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x6)
    OP_9D(0xFE, 0x37AA, 0x1F40, 0x587A, 0x1F4, 0xFA0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 11800, 8000, 25000, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x6)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_124_1194E end

    def Function_125_119FC(): pass

    label("Function_125_119FC")

    Sleep(6500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x2FA8, 0x3E80, 0xA730, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 12100, 16000, 39450, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    SetChrSubChip(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_125_119FC end

    def Function_126_11A5E(): pass

    label("Function_126_11A5E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11AAD")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x3)
    Jump("Function_126_11A5E")

    label("loc_11AAD")

    Return()

    # Function_126_11A5E end

    def Function_127_11AAE(): pass

    label("Function_127_11AAE")

    Sleep(7000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x4)
    Sound(809, 0, 40, 0)
    OP_9D(0xFE, 0x49A2, 0x3E80, 0x940C, 0x1F4, 0x1388)
    OP_95(0xFE, 17250, 16000, 36300, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x3B92, 0x2EE0, 0x8340, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 14050, 12000, 31950, 5000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 126)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_127_11AAE end

    def Function_128_11B4D(): pass

    label("Function_128_11B4D")

    Sleep(7500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 40, 0)
    OP_9D(0xFE, 0x2710, 0x3E80, 0xAB7C, 0x1F4, 0x1388)
    OP_95(0xFE, 10450, 16000, 39900, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x2A94, 0x2EE0, 0x90BA, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 11100, 12000, 35250, 5000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 126)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_128_11B4D end

    def Function_129_11BEC(): pass

    label("Function_129_11BEC")

    Sleep(8500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 40, 0)
    OP_9D(0xFE, 0x3FDE, 0x3E80, 0x9F92, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 17700, 16000, 36750, 5000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 126)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_129_11BEC end

    def Function_130_11C5C(): pass

    label("Function_130_11C5C")

    Sleep(9000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5F)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x49A2, 0x4E20, 0x9218, 0x1F4, 0x1388)
    Sound(326, 0, 10, 0)
    OP_95(0xFE, 18850, 16000, 36250, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x44C0, 0x2EE0, 0x82DC, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 16600, 12000, 29850, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    TurnDirection(0xFE, 0x18, 500)
    SetChrChipByIndex(0xFE, 0x60)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x18, 0xFE, 500)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0xFE, 0x20)

    label("loc_11D24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11DA2")

    def lambda_11D34():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_11D34)
    SetChrChipByIndex(0x18, 0x5D)

    def lambda_11D4D():
        OP_A0(0xFE, 2000, 0x0, 0x3)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_11D4D)
    OP_9A(0x18, 0xFE, 0x3E8, 0x2710, 0x0)
    Sleep(1000)

    def lambda_11D6B():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_11D6B)
    SetChrChipByIndex(0xFE, 0x61)

    def lambda_11D84():
        OP_A0(0xFE, 2000, 0x0, 0x4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_11D84)
    OP_9A(0xFE, 0x18, 0x3E8, 0x2710, 0x0)
    Sleep(1000)
    Jump("loc_11D24")

    label("loc_11DA2")

    Return()

    # Function_130_11C5C end

    def Function_131_11DA3(): pass

    label("Function_131_11DA3")

    Sleep(9500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5F)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x3CF0, 0x3E80, 0x943E, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 17500, 16000, 35950, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x4556, 0x2EE0, 0x7D31, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 16050, 12000, 30400, 5000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x60)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_131_11DA3 end

    def Function_132_11E40(): pass

    label("Function_132_11E40")

    Sleep(10000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5F)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x48A8, 0x3E80, 0x9A4C, 0x1F4, 0x1388)
    OP_95(0xFE, 18850, 16000, 36250, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x44C0, 0x2EE0, 0x82DC, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 18750, 12000, 28900, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x474A, 0x1F40, 0x6018, 0x1F4, 0x1388)
    TurnDirection(0xFE, 0x19, 500)
    SetChrChipByIndex(0xFE, 0x60)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x19, 0xFE, 500)
    SetChrChipByIndex(0xFE, 0x61)

    def lambda_11F07():
        OP_A0(0xFE, 2000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_11F07)
    SetChrFlags(0xFE, 0x20)
    OP_9A(0xFE, 0x19, 0x3E8, 0x2710, 0x0)
    Sound(566, 0, 20, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x19, 0x5C)
    SetChrSubChip(0x19, 0x0)

    def lambda_11F3A():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_11F3A)

    def lambda_11F53():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_11F53)
    Return()

    # Function_132_11E40 end

    def Function_133_11F68(): pass

    label("Function_133_11F68")

    SetChrChipByIndex(0xFE, 0x65)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11F82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11F99")
    OP_A0(0xFE, 1500, 0x0, 0x4)
    Jump("loc_11F82")

    label("loc_11F99")

    Return()

    # Function_133_11F68 end

    def Function_134_11F9A(): pass

    label("Function_134_11F9A")

    SetChrChipByIndex(0xFE, 0x64)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11FB4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11FD2")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_11FB4")

    label("loc_11FD2")

    Return()

    # Function_134_11F9A end

    def Function_135_11FD3(): pass

    label("Function_135_11FD3")

    Sleep(4500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x4330, 0x3E80, 0x9E34, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 17050, 16000, 36600, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 134)
    Sleep(1000)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x4556, 0x2EE0, 0x7D31, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 17600, 12000, 30300, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 134)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_135_11FD3 end

    def Function_136_12086(): pass

    label("Function_136_12086")

    Sleep(5000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x2B8E, 0x3E80, 0xABAE, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 11400, 16000, 39700, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 134)
    Sleep(1000)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x3BF6, 0x2EE0, 0x83D6, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 13900, 12000, 33350, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 134)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_136_12086 end

    def Function_137_12140(): pass

    label("Function_137_12140")

    Sleep(5500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 40, 0)
    OP_9D(0xFE, 0x3908, 0x3E80, 0xA442, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 14500, 16000, 38100, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 134)
    Sleep(1000)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x3070, 0x2EE0, 0x8CA0, 0x1F4, 0x1388)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 8950, 12000, 36650, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 134)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_137_12140 end

    def Function_138_121FA(): pass

    label("Function_138_121FA")

    Sleep(6000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 40, 0)
    OP_9D(0xFE, 0x3C5A, 0x3E80, 0x9F92, 0x1F4, 0x1388)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 15750, 16000, 36400, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x3E3A, 0x2EE0, 0x7EC2, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 15100, 12000, 31250, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x3552, 0x1F40, 0x6F72, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    OP_93(0xFE, 0xB4, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 134)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_138_121FA end

    def Function_139_122C4(): pass

    label("Function_139_122C4")

    Sleep(6500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x3746, 0x3E80, 0xA4A6, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 14150, 16000, 38400, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 134)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_139_122C4 end

    def Function_140_1232E(): pass

    label("Function_140_1232E")

    BeginChrThread(0xFE, 0, 0, 134)

    label("loc_12334")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1238C")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12384")
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x66)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x2, 0x3, 0x2, 0x3)
    Return()

    label("loc_12384")

    Sleep(1000)
    Jump("loc_12334")

    label("loc_1238C")

    Return()

    # Function_140_1232E end

    def Function_141_1238D(): pass

    label("Function_141_1238D")

    Sound(974, 2, 20, 0)
    Sleep(200)
    OP_25(0x3CE, 0x1E)
    Sleep(200)
    OP_25(0x3CE, 0x28)
    Sleep(200)
    OP_25(0x3CE, 0x32)
    Sleep(200)
    OP_25(0x3CE, 0x3C)
    Sleep(200)
    OP_25(0x3CE, 0x46)
    Sleep(200)
    OP_25(0x3CE, 0x46)
    Return()

    # Function_141_1238D end

    def Function_142_123BE(): pass

    label("Function_142_123BE")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('旧矿山的钥匙', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1257B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1250E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1247F")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0313
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旧矿山的大门紧紧关闭着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0314
    ChrTalk(
        0x101,
        (
            "#00000F我们虽然接到了\x01",
            "驱赶旧矿山通缉魔兽的委托……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        (
            "#00100F但还是先去和\x01",
            "镇长谈谈为好啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_12509")

    label("loc_1247F")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0316
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旧矿山的大门紧紧关闭着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0317
    ChrTalk(
        0x101,
        (
            "#00000F虽然接到了驱赶\x01",
            "通缉魔兽的委托……\x01",
            "但我们手里并没有钥匙。\x02\x03",

            "还是先去和镇长谈谈吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12509")

    Jump("loc_12576")

    label("loc_1250E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_12549")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0318
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旧矿山的大门紧紧关闭着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_12576")

    label("loc_12549")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0319
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旧矿山的大门紧紧关闭着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_12576")

    Jump("loc_12651")

    label("loc_1257B")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0320
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旧矿山的大门紧紧关闭着。\x02\x03",

            "如果使用向镇长借来的备用钥匙，\x01",
            "应该可以将锁打开。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "使用钥匙\x01",      # 0
            "不使用\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12651")
    Sound(806, 0, 100, 0)
    SetChrName("")

    #A0321
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁打开了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x14F, 4)
    SetMapObjFlags(0x5, 0x10)
    OP_65(0x6, 0x1)
    Jump("loc_12651")

    label("loc_12651")

    TalkEnd(0xFF)
    Return()

    # Function_142_123BE end

    SaveToFile()

Try(main)
