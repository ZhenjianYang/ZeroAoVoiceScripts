from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r1530.bin",                # FileName
        "r1530",                    # MapName
        "r1530",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r1530", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x0C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 4800, 0, 35500, 180, 0, 1, 96, 0, 3, 0, 4],
    )

    BuildStringList((
        "r1530",                  # 0
        "雷克罗德Ⅲ世",           # 1
        "彼德",                   # 2
        "克潘",                   # 3
        "巴士",                   # 4
        "绒毛浮游虫",             # 5
        "绒毛浮游虫",             # 6
        "强壮巨骨猩",             # 7
        "强壮巨骨猩",             # 8
        "幻兽",                   # 9
        "纳迪利亚菇",             # 10
        "赛尔丹分部长",           # 11
        "费瑟尔团长",             # 12
        "『银螭』特里同",         # 13
        "『龙宫』辉夜",           # 14
        "『水狂』纳西斯",         # 15
        "『海刃』沙克曼",         # 16
        "br1500",                 # 17
        "br1520",                 # 18
        "br1500",                 # 19
        "br1520",                 # 20
        "br1500",                 # 21
        "br1500",                 # 22
        "br1520",                 # 23
        "br1500",                 # 24
        "br1500",                 # 25
        "br1500",                 # 26
        "克洛斯贝尔市方向",       # 27
        "乌尔斯拉医科大学方向",   # 28
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_B4", 3,   10,  0,   8,   3,   0,   0)
    Sepith("Sepith_C4", 0,   10,  0,   7,   4,   3,   0)
    Sepith("Sepith_D4", 6,   4,   9,   4,   0,   0,   0)
    Sepith("Sepith_E4", 0,   5,   0,   0,   6,   6,   6)
    Sepith("Sepith_F4", 0,   10,  0,   5,   2,   4,   2)
    Sepith("Sepith_104", 5,   3,   0,   8,   0,   4,   3)

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
    MonsterBattlePostion("MonsterBattlePostion_174", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_178", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_17C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_184", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_188", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_18C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_190", 0, 0, 180)

    # monster count: 15

    BattleInfo(
        "BattleInfo_194", 0x0000, 58, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_B4", 30, 40, 20, 10,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_25C", 0x0010, 58, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_C4", 30, 40, 20, 10,
        (
            ("ms63600.dat", 0, 0, 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms63600.dat", "ms63600.dat", 0, 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_324", 0x0000, 58, 6, 45, 10, 1, 50, 0, "br1520", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms65300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65300.dat", "ms65300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65300.dat", "ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3EC", 0x0000, 58, 6, 45, 10, 1, 40, 0, "br1520", "Sepith_E4", 30, 40, 20, 10,
        (
            ("ms65200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_4B4", 0x0000, 58, 6, 45, 10, 1, 30, 0, "br1520", "Sepith_F4", 30, 40, 20, 10,
        (
            ("ms61300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_57C", 0x0000, 58, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_104", 30, 40, 20, 10,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_644", 0x0000, 58, 6, 45, 10, 1, 50, 0, "br1500", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms65300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65300.dat", "ms65300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65300.dat", "ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_70C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7453", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_750", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7453", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_794", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88901.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_174", "MonsterBattlePostion_134", "ed7454", "ed7453", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch45600.itc",                   # 00
        "chr/ch45400.itc",                   # 01
        "apl/ch50165.itc",                   # 02
        "apl/ch50166.itc",                   # 03
        "apl/ch51017.itc",                   # 04
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
        "monster/ch62150.itc",               # 10
        "monster/ch62151.itc",               # 11
        "monster/ch65250.itc",               # 12
        "monster/ch65251.itc",               # 13
        "monster/ch63650.itc",               # 14
        "monster/ch63650.itc",               # 15
        "monster/ch61350.itc",               # 16
        "monster/ch61350.itc",               # 17
        "monster/ch69750.itc",               # 18
        "monster/ch69750.itc",               # 19
        "monster/ch65350.itc",               # 1A
        "monster/ch65351.itc",               # 1B
        "monster/ch70250.itc",               # 1C
        "monster/ch70251.itc",               # 1D
    ))

    DeclNpc(46709,   -6300,   -58759,  95,   389,  0x0, 0,   0,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(47180,   -6289,   -57169,  90,   405,  0x0, 0,   2,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(43380,   -6280,   -62470,  180,  405,  0x0, 0,   3,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(28200,   -5599,   -32259,  270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-17180,  -5500,   -103099, 270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(28200,   -5599,   -32259,  270,  484,  0x0, 0,   28,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(-17180,  -5500,   -103099, 270,  484,  0x0, 0,   28,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4930,    10160,   0,       0x1010000,    "BattleInfo_194", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-33140,  -4930,   0,       0x1010000,    "BattleInfo_25C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-38450,  -31510,  -2800,   0x1010000,    "BattleInfo_25C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-17540,  -38170,  -5600,   0x1010000,    "BattleInfo_324", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-5060,   -13330,  -6300,   0x1010000,    "BattleInfo_3EC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4200,    -20550,  -6300,   0x1010000,    "BattleInfo_4B4", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(2370,    -42510,  -6300,   0x1010000,    "BattleInfo_3EC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(19970,   -49310,  -6300,   0x1010000,    "BattleInfo_4B4", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(33630,   -23560,  -5600,   0x1010000,    "BattleInfo_3EC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(52410,   -28230,  -5600,   0x1010000,    "BattleInfo_4B4", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-38810,  -52060,  -4200,   0x1010000,    "BattleInfo_57C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-21590,  -49910,  -4200,   0x1010000,    "BattleInfo_57C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-30050,  -108200, -4900,   0x1010000,    "BattleInfo_194", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-16070,  -108310, -5770,   0x1010000,    "BattleInfo_644", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-15000,  -92180,  -5770,   0x1010000,    "BattleInfo_644", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 24,  42.25,                 -21.75,                -5.599999904632568,    324.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -14.083333969116211,   1.8125,                1.1200000047683716,    1.0])
    DeclEvent(0x0040, 0, 22,  -38.16999816894531,    -33.31999969482422,    -3.799999952316284,    16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   4.771249771118164,     4.164999961853027,     0.949999988079071,     1.0])

    DeclActor(-24850,  0,       -2920,   1200,    -24850,  1000,    -2920,   0x007C, 0,  21, 0x0000)
    DeclActor(36340,   -5600,   -39750,  1200,    36340,   -4600,   -39750,  0x007C, 0,  5,  0x0000)
    DeclActor(49800,   -5600,   -17450,  1200,    49800,   -4600,   -17450,  0x007C, 0,  6,  0x0000)
    DeclActor(-14500,  -5800,   -88320,  1200,    -14500,  -4800,   -88320,  0x007C, 0,  7,  0x0000)
    DeclActor(28200,   -5600,   -32259,  1200,    28200,   -5600,   -32259,  0x007C, 0,  8,  0x0000)
    DeclActor(-17180,  -5500,   -103100, 1200,    -17180,  -5500,   -103100, 0x007C, 0,  9,  0x0000)
    DeclActor(36400,   -6290,   -67430,  1200,    35830,   -5800,   -74960,  0x007C, 0,  23, 0x0000)
    DeclActor(-18730,  0,       -10,     1200,    -18730,  2000,    -10,     0x007C, 0,  20, 0x0000)

    PlaceName(7.0, 0.0, 52.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-89.0, 0.0, -115.0, 0x0000, 0x0000, "乌尔斯拉医科大学方向")
    PlaceName(-24.700000762939453, 0.0, -2.950000047683716, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5, 6, 7])              # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 11

    ScpFunction((
        "Function_0_F14",          # 00, 0
        "Function_1_FCC",          # 01, 1
        "Function_2_FEB",          # 02, 2
        "Function_3_100A",         # 03, 3
        "Function_4_15C1",         # 04, 4
        "Function_5_1AE9",         # 05, 5
        "Function_6_1C24",         # 06, 6
        "Function_7_1D5F",         # 07, 7
        "Function_8_1E9A",         # 08, 8
        "Function_9_21BE",         # 09, 9
        "Function_10_24E2",        # 0A, 10
        "Function_11_24FB",        # 0B, 11
        "Function_12_24FF",        # 0C, 12
        "Function_13_25BB",        # 0D, 13
        "Function_14_26EE",        # 0E, 14
        "Function_15_2821",        # 0F, 15
        "Function_16_2872",        # 10, 16
        "Function_17_2906",        # 11, 17
        "Function_18_2980",        # 12, 18
        "Function_19_2BB4",        # 13, 19
        "Function_20_2C05",        # 14, 20
        "Function_21_2F32",        # 15, 21
        "Function_22_2F6C",        # 16, 22
        "Function_23_2FE8",        # 17, 23
        "Function_24_3135",        # 18, 24
        "Function_25_3658",        # 19, 25
        "Function_26_39C7",        # 1A, 26
        "Function_27_3A04",        # 1B, 27
        "Function_28_3A44",        # 1C, 28
        "Function_29_403F",        # 1D, 29
    ))


    def Function_0_F14(): pass

    label("Function_0_F14")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_F54"),
        (1, "loc_F60"),
        (2, "loc_F6C"),
        (3, "loc_F78"),
        (4, "loc_F84"),
        (5, "loc_F90"),
        (6, "loc_F9C"),
        (SWITCH_DEFAULT, "loc_FA8"),
    )


    label("loc_F54")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F60")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F6C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F78")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F84")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F90")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F9C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_FA8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_FB4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FCB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_FCB")

    Return()

    # Function_0_F14 end

    def Function_1_FCC(): pass

    label("Function_1_FCC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FEA")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_1_FCC")

    label("loc_FEA")

    Return()

    # Function_1_FCC end

    def Function_2_FEB(): pass

    label("Function_2_FEB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1009")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_2_FEB")

    label("loc_1009")

    Return()

    # Function_2_FEB end

    def Function_3_100A(): pass

    label("Function_3_100A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1022")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_10D8")

    label("loc_1022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1030")
    Jump("loc_10D8")

    label("loc_1030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_104C")
    ClearChrFlags(0x8, 0x80)

    label("loc_104C")

    Jump("loc_10D8")

    label("loc_1051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_105F")
    Jump("loc_10D8")

    label("loc_105F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_106D")
    Jump("loc_10D8")

    label("loc_106D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_107B")
    Jump("loc_10D8")

    label("loc_107B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1089")
    Jump("loc_10D8")

    label("loc_1089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1097")
    Jump("loc_10D8")

    label("loc_1097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10A5")
    Jump("loc_10D8")

    label("loc_10A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_10B3")
    Jump("loc_10D8")

    label("loc_10B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10C1")
    Jump("loc_10D8")

    label("loc_10C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_10CF")
    Jump("loc_10D8")

    label("loc_10CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_10D8")

    label("loc_10D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157C")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1165")
    SetScenarioFlags(0x38, 0)

    label("loc_1165")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117B")
    SetScenarioFlags(0x38, 1)

    label("loc_117B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1191")
    SetScenarioFlags(0x38, 2)

    label("loc_1191")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A7")
    SetScenarioFlags(0x38, 3)

    label("loc_11A7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BD")
    SetScenarioFlags(0x38, 4)

    label("loc_11BD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D3")
    SetScenarioFlags(0x38, 5)

    label("loc_11D3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E9")
    SetScenarioFlags(0x38, 6)

    label("loc_11E9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FF")
    SetScenarioFlags(0x38, 7)

    label("loc_11FF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1215")
    SetScenarioFlags(0x39, 0)

    label("loc_1215")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122B")
    SetScenarioFlags(0x39, 1)

    label("loc_122B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1241")
    SetScenarioFlags(0x39, 2)

    label("loc_1241")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1257")
    SetScenarioFlags(0x39, 3)

    label("loc_1257")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126D")
    SetScenarioFlags(0x39, 4)

    label("loc_126D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1283")
    SetScenarioFlags(0x39, 5)

    label("loc_1283")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1299")
    SetScenarioFlags(0x39, 6)

    label("loc_1299")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AF")
    SetScenarioFlags(0x39, 7)

    label("loc_12AF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C5")
    SetScenarioFlags(0x3A, 0)

    label("loc_12C5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12DB")
    SetScenarioFlags(0x3A, 1)

    label("loc_12DB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F1")
    SetScenarioFlags(0x3A, 2)

    label("loc_12F1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1307")
    SetScenarioFlags(0x3A, 3)

    label("loc_1307")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131D")
    SetScenarioFlags(0x3A, 4)

    label("loc_131D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1333")
    SetScenarioFlags(0x3A, 5)

    label("loc_1333")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1349")
    SetScenarioFlags(0x3A, 6)

    label("loc_1349")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135F")
    SetScenarioFlags(0x3A, 7)

    label("loc_135F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1375")
    SetScenarioFlags(0x3B, 0)

    label("loc_1375")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_138B")
    SetScenarioFlags(0x3B, 1)

    label("loc_138B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A1")
    SetScenarioFlags(0x3B, 2)

    label("loc_13A1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B7")
    SetScenarioFlags(0x3B, 3)

    label("loc_13B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CD")
    SetScenarioFlags(0x3B, 4)

    label("loc_13CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E3")
    SetScenarioFlags(0x3B, 5)

    label("loc_13E3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F9")
    SetScenarioFlags(0x3B, 6)

    label("loc_13F9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140F")
    SetScenarioFlags(0x3B, 7)

    label("loc_140F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1425")
    SetScenarioFlags(0x3D, 5)

    label("loc_1425")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143B")
    SetScenarioFlags(0x3D, 6)

    label("loc_143B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1451")
    SetScenarioFlags(0x3D, 7)

    label("loc_1451")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148C")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_157C")

    label("loc_148C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AF")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_157C")

    label("loc_14AF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D2")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_157C")

    label("loc_14D2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F5")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_157C")

    label("loc_14F5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1518")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_157C")

    label("loc_1518")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_153B")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_157C")

    label("loc_153B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155E")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_157C")

    label("loc_155E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157C")
    SetScenarioFlags(0x3C, 7)

    label("loc_157C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AE")
    SetChrPos(0x0, -18130, 0, -610, 135)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 16)

    label("loc_15AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_15BD")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 15)

    label("loc_15BD")

    Call(0, 10)
    Return()

    # Function_3_100A end

    def Function_4_15C1(): pass

    label("Function_4_15C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_15D3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15D3")

    Sound(136, 1, 50, 0)
    SoundDistance(0x7D, 0x8DF4, 0xFFFFEA20, 0xFA32, 0x15F90, 0x11170, 0x64, 0x0)
    OP_E3(0x3F52, 0xFFFFE976, 0xFFFE520A)
    OP_E3(0xFFFFF10A, 0xFFFFECDC, 0xFFFDF6AC)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1627")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1627")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_164E")
    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16B7")

    label("loc_164E")

    OP_78(0xE, 0x10)
    ClearMapObjFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x1)
    SetChrPos(0x10, -38170, -2800, -33320, 90)
    OP_93(0x10, 0x5A, 0x0)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, -38170, -3800, -33320, 3000, 3000, 90000)

    label("loc_16B7")

    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_189B")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_189B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_18F2")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    Jump("loc_1922")

    label("loc_18F2")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)

    label("loc_1922")

    MiniGame(0x2F, 0x7, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xB, 0x80)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_END)), "loc_196E")
    SetMapObjFrame(0xFF, "stone_off", 0x0, 0x1)
    Jump("loc_198B")

    label("loc_196E")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 56600, -7000, -23650, 6200, 3000, 265000)

    label("loc_198B")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 35830, -5800, -74960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E8")
    OP_70(0x1, 0x0)
    Jump("loc_19EC")

    label("loc_19E8")

    OP_70(0x1, 0x1E)

    label("loc_19EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FF")
    OP_70(0x2, 0x0)
    Jump("loc_1A03")

    label("loc_19FF")

    OP_70(0x2, 0x1E)

    label("loc_1A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A16")
    OP_70(0x3, 0x0)
    Jump("loc_1A1A")

    label("loc_1A16")

    OP_70(0x3, 0x1E)

    label("loc_1A1A")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A7B")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 28200, -5600, -32259, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1A7B")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AC7")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -17180, -5500, -103100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_1AC7")

    OP_1C(0x0, 0xF, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x10, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x11, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    Return()

    # Function_4_15C1 end

    def Function_5_1AE9(): pass

    label("Function_5_1AE9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BDB")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1B6C")
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
    SetScenarioFlags(0x1EC, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1BD6")

    label("loc_1B6C")

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
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1BD6")

    Jump("loc_1C18")

    label("loc_1BDB")

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

    label("loc_1C18")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1AE9 end

    def Function_6_1C24(): pass

    label("Function_6_1C24")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D16")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x97, 1)"), scpexpr(EXPR_END)), "loc_1CA7")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x97),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1D11")

    label("loc_1CA7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x97),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x97),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D11")

    Jump("loc_1D53")

    label("loc_1D16")

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

    label("loc_1D53")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C24 end

    def Function_7_1D5F(): pass

    label("Function_7_1D5F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E51")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_1DE2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1E4C")

    label("loc_1DE2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E4C")

    Jump("loc_1E8E")

    label("loc_1E51")

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

    label("loc_1E8E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1D5F end

    def Function_8_1E9A(): pass

    label("Function_8_1E9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2033")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_2019")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2014")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_2011")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F3C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1F3C)
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
    Battle("BattleInfo_70C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_200C")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1FF3")
    Call(1, 5)
    Jump("loc_200C")

    label("loc_1FF3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2009")
    Call(1, 4)
    Jump("loc_200C")

    label("loc_2009")

    Call(1, 3)

    label("loc_200C")

    Jump("loc_2014")

    label("loc_2011")

    Call(1, 1)

    label("loc_2014")

    Jump("loc_202F")

    label("loc_2019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_202F")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_202F")

    TalkEnd(0xFF)
    Return()

    label("loc_2033")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_21A4")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_219F")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_219C")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_20C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_20C7)
    TurnDirection(0xE, 0x0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    PlayEffect(0x7, 0x1, 0xE, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_750", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2197")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_217E")
    Call(1, 5)
    Jump("loc_2197")

    label("loc_217E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2194")
    Call(1, 4)
    Jump("loc_2197")

    label("loc_2194")

    Call(1, 3)

    label("loc_2197")

    Jump("loc_219F")

    label("loc_219C")

    Call(1, 1)

    label("loc_219F")

    Jump("loc_21BA")

    label("loc_21A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_21BA")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_21BA")

    TalkEnd(0xFF)
    Return()

    # Function_8_1E9A end

    def Function_9_21BE(): pass

    label("Function_9_21BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2357")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_233D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2338")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_2335")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2260():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2260)
    TurnDirection(0xD, 0x0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    PlayEffect(0x7, 0x1, 0xD, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_70C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2330")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2317")
    Call(1, 5)
    Jump("loc_2330")

    label("loc_2317")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_232D")
    Call(1, 4)
    Jump("loc_2330")

    label("loc_232D")

    Call(1, 3)

    label("loc_2330")

    Jump("loc_2338")

    label("loc_2335")

    Call(1, 1)

    label("loc_2338")

    Jump("loc_2353")

    label("loc_233D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_2353")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2353")

    TalkEnd(0xFF)
    Return()

    label("loc_2357")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_24C8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C3")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_24C0")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_23EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_23EB)
    TurnDirection(0xF, 0x0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    PlayEffect(0x7, 0x1, 0xF, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_750", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24BB")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24A2")
    Call(1, 5)
    Jump("loc_24BB")

    label("loc_24A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24B8")
    Call(1, 4)
    Jump("loc_24BB")

    label("loc_24B8")

    Call(1, 3)

    label("loc_24BB")

    Jump("loc_24C3")

    label("loc_24C0")

    Call(1, 1)

    label("loc_24C3")

    Jump("loc_24DE")

    label("loc_24C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_24DE")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_24DE")

    TalkEnd(0xFF)
    Return()

    # Function_9_21BE end

    def Function_10_24E2(): pass

    label("Function_10_24E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24F5")
    Jump("loc_24FA")

    label("loc_24F5")

    SetChrFlags(0x1A, 0x80)

    label("loc_24FA")

    Return()

    # Function_10_24E2 end

    def Function_11_24FB(): pass

    label("Function_11_24FB")

    Call(1, 6)
    Return()

    # Function_11_24FB end

    def Function_12_24FF(): pass

    label("Function_12_24FF")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔市南出口\x01",      # 0
            "圣乌尔斯拉医科大学\x01",      # 1
            "放弃\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2593")
    Call(0, 13)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_25B3")

    label("loc_2593")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B3")
    Call(0, 14)
    ClearMapFlags(0x8000000)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()

    label("loc_25B3")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_12_24FF end

    def Function_13_25BB(): pass

    label("Function_13_25BB")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_26EA")
    Fade(500)
    OP_68(-20430, 600, -680, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -25190, 0, -1760, 180)
    SetChrPos(0x1, -24640, 0, -460, 180)
    SetChrPos(0x2, -23960, 0, 1080, 180)
    SetChrPos(0x3, -23400, 0, 2850, 180)
    ClearChrFlags(0xB, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0xB)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xB, -27960, -10, -14410, 45)
    OP_D5(0xB, 0x0, 0xAFC8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_26A1():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26A1)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xB, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_26EA")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_13_25BB end

    def Function_14_26EE(): pass

    label("Function_14_26EE")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_281D")
    Fade(500)
    OP_68(-22010, 600, -2420, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -25190, 0, -1760, 180)
    SetChrPos(0x1, -24640, 0, -460, 180)
    SetChrPos(0x2, -23960, 0, 1080, 180)
    SetChrPos(0x3, -23400, 0, 2850, 180)
    ClearChrFlags(0xB, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0xB)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xB, -9730, 0, 4220, 225)
    OP_D5(0xB, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_27D4():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_27D4)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xB, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_281D")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_14_26EE end

    def Function_15_2821(): pass

    label("Function_15_2821")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -25540, 0, -2260, 225)
    OP_31(0x1)
    OP_68(-25540, 600, -2260, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    EventEnd(0x5)
    Return()

    # Function_15_2821 end

    def Function_16_2872(): pass

    label("Function_16_2872")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_28CD")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28C2")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_28C8")

    label("loc_28C2")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_28C8")

    Jump("loc_28F1")

    label("loc_28CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28EB")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_28F1")

    label("loc_28EB")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_28F1")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_16_2872 end

    def Function_17_2906(): pass

    label("Function_17_2906")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_291B")
    Call(0, 25)
    Jump("loc_297C")

    label("loc_291B")


    #C0019
    ChrTalk(
        0x8,
        (
            "话说回来，没想到巨骨龙皇鱼\x01",
            "竟然会出现在克洛斯贝尔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        "等着瞧吧……我一定会解决掉它的！\x02",
    )

    CloseMessageWindow()

    label("loc_297C")

    TalkEnd(0xFE)
    Return()

    # Function_17_2906 end

    def Function_18_2980(): pass

    label("Function_18_2980")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF9")

    #C0021
    ChrTalk(
        0x9,
        (
            "虽然那棵巨大的树很令人在意，\x01",
            "但是不垂钓的话，\x01",
            "总觉得静不下心来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "不管是钓鱼还是其它事情，\x01",
            "最重要的都是沉着冷静，\x01",
            "我是这样认为的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2A5E")

    #C0023
    ChrTalk(
        0x9,
        (
            "罗伊德大师，如果有需要，\x01",
            "就请在这里放松一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8F")

    label("loc_2A5E")


    #C0024
    ChrTalk(
        0x9,
        (
            "罗伊德，如果有需要，\x01",
            "就请在这里放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A8F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0025
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x18B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了５个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x18B, 5)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0026
    ChrTalk(
        0x101,
        "#00000F谢、谢谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 1)
    Jump("loc_2BB0")

    label("loc_2AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7B")

    #C0027
    ChrTalk(
        0x9,
        (
            "顺便一提，赛尔丹分部长\x01",
            "去租船小屋\x01",
            "察看情况了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "呵呵，看来分部长\x01",
            "很喜欢那个地方，\x01",
            "至今都还念念不忘呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BB0")

    label("loc_2B7B")


    #C0029
    ChrTalk(
        0x9,
        (
            "好了，今天我要集中精神，\x01",
            "全身心地投入到钓鱼中～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BB0")

    TalkEnd(0xFE)
    Return()

    # Function_18_2980 end

    def Function_19_2BB4(): pass

    label("Function_19_2BB4")

    TalkBegin(0xFE)

    #C0030
    ChrTalk(
        0xA,
        (
            "啊……终于\x01",
            "可以在市外钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        (
            "在大自然之中钓鱼\x01",
            "果然是最棒的说！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_2BB4 end

    def Function_20_2C05(): pass

    label("Function_20_2C05")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C37")
    SetScenarioFlags(0x31, 2)

    label("loc_2C37")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2C77")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C6C")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_2C72")

    label("loc_2C6C")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_2C72")

    Jump("loc_2C7D")

    label("loc_2C77")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_2C7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2CEE")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2CCE"),
        (SWITCH_DEFAULT, "loc_2CDF"),
    )


    label("loc_2CCE")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CE9")

    label("loc_2CDF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CE9")

    Jump("loc_2F1F")

    label("loc_2CEE")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2D1E")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_2D1E")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D48"),
        (1, "loc_2E4C"),
        (2, "loc_2EDD"),
        (SWITCH_DEFAULT, "loc_2F15"),
    )


    label("loc_2D48")

    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_74(0xC, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D79")
    OP_70(0xC, 0x12C)
    OP_71(0xC, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2D89")

    label("loc_2D79")

    OP_70(0xC, 0xF0)
    OP_71(0xC, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2D89")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DDF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DDF")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E02")
    Sound(461, 0, 100, 0)

    label("loc_2E02")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E22")
    OP_70(0xC, 0x14A)
    OP_71(0xC, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2E32")

    label("loc_2E22")

    OP_70(0xC, 0x10E)
    OP_71(0xC, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2E32")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0xC, "light", 0x1, 0x1)
    OP_70(0xC, 0x0)
    Jump("loc_2C7D")

    label("loc_2E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2EBE")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2E81")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_2E99")

    label("loc_2E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2E94")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_2E99")

    label("loc_2E94")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_2E99")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2ED8")

    label("loc_2EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2ECE")
    OP_AF(0xFB)
    Jump("loc_2ED8")

    label("loc_2ECE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2ED8")

    Jump("loc_2F1F")

    label("loc_2EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F10")

    label("loc_2EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2F06")
    OP_AF(0xFB)
    Jump("loc_2F10")

    label("loc_2F06")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F10")

    Jump("loc_2F1F")

    label("loc_2F15")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F1F")

    Jump("loc_2C7D")

    label("loc_2F24")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_2C05 end

    def Function_21_2F32(): pass

    label("Function_21_2F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2F68")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力巴士已经停运了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_2F68")

    Call(0, 12)
    Return()

    # Function_21_2F32 end

    def Function_22_2F6C(): pass

    label("Function_22_2F6C")

    Battle("BattleInfo_794", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB3")
    OP_90(0x0, -30320, -2800, -33510, 90)
    EventEnd(0x5)
    SetChrFlags(0x10, 0x8000)
    Jump("loc_2FE7")

    label("loc_2FB3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC6")
    Jump("loc_2FE7")

    label("loc_2FC6")

    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0xE, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 1)
    EventEnd(0x5)

    label("loc_2FE7")

    Return()

    # Function_22_2F6C end

    def Function_23_2FE8(): pass

    label("Function_23_2FE8")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0033
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(35730, -5700, -72750, 1500)
    MoveCamera(45, 33, 0, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(18000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0034
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3130")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_310E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MiniGame(0x6, 0xD, 0x8E30, 0xFFFFE76E, 0xFFFEF89A, 0xB4, 0x8BF6, 0xFFFFE958, 0xFFFEDB30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3109")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3109")
    Call(0, 29)
    Return()

    label("loc_3109")

    Jump("loc_3130")

    label("loc_310E")

    MiniGame(0x6, 0xC, 0x8E30, 0xFFFFE76E, 0xFFFEF89A, 0xB4, 0x8BF6, 0xFFFFE958, 0xFFFEDB30)

    label("loc_3130")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_23_2FE8 end

    def Function_24_3135(): pass

    label("Function_24_3135")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    OP_68(41000, -4700, -21900, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(43010, -4700, -22040, 1500)
    SetCameraDistance(18000, 1500)
    SetChrPos(0x101, 41600, -5600, -22000, 90)
    SetChrPos(0x102, 41250, -5600, -23250, 90)
    SetChrPos(0x103, 40800, -5600, -21000, 90)
    SetChrPos(0x104, 40150, -5600, -22600, 90)
    SetChrPos(0x109, 40500, -5600, -20200, 90)
    SetChrPos(0x105, 38750, -5600, -21900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)

    def lambda_3227():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3227)
    Sleep(0)

    def lambda_323F():
        OP_9B(0x0, 0x102, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_323F)
    Sleep(0)

    def lambda_3257():
        OP_9B(0x0, 0x103, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3257)
    Sleep(0)

    def lambda_326F():
        OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_326F)
    Sleep(0)

    def lambda_3287():
        OP_9B(0x0, 0x109, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3287)
    Sleep(0)

    def lambda_329F():
        OP_9B(0x0, 0x105, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_329F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_0D()
    OP_6F(0x79)

    #C0035
    ChrTalk(
        0x101,
        "#00005F#5P那是……\x02",
    )

    CloseMessageWindow()
    OP_68(57750, -6200, -24100, 3000)
    MoveCamera(58, 30, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(22000, 3000)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 3)), scpexpr(EXPR_END)), "loc_33E5")

    #C0036
    ChrTalk(
        0x109,
        (
            "#10111F什么时候变成这样了……\x02\x03",

            "#10101F上次来的时候，\x01",
            "那里还没有敞开吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_343A")

    label("loc_33E5")


    #C0037
    ChrTalk(
        0x109,
        (
            "#10111F什么时候变成这样了……\x02\x03",

            "#10108F以前巡逻的时候，\x01",
            "那个地方还没有敞开呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_343A")


    #C0038
    ChrTalk(
        0x104,
        (
            "#00301F可能是某些冲击\x01",
            "将堵死的入口震开了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(42800, -4700, -21900, 0)
    MoveCamera(42, 23, 0, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    TurnDirection(0x105, 0x103, 500)

    #C0039
    ChrTalk(
        0x105,
        (
            "#10304F#6P也就是说，穿过这里，\x01",
            "就是『幻兽』的所在之处了吧？\x02\x03",

            "#10300F有没有『力场异常』的迹象？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_350A():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_350A)

    def lambda_3517():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3517)
    Sleep(50)

    def lambda_3527():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3527)
    Sleep(50)

    def lambda_3537():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3537)
    Sleep(50)

    def lambda_3547():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3547)
    Sleep(50)

    def lambda_3557():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3557)
    Sleep(50)

    def lambda_3567():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3567)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 2)

    #C0040
    ChrTalk(
        0x103,
        (
            "#00203F#5P……目前还没有显著迹象。\x02\x03",

            "#00201F但可以感觉到奇异的气息。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#00108F#12P是吗……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#00001F#11P……总之，\x01",
            "也只能进去看看了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 43500, -5600, -22000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 2)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_24_3135 end

    def Function_25_3658(): pass

    label("Function_25_3658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3709")

    #C0043
    ChrTalk(
        0x8,
        "来了吗……那就马上开始吧。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "你究竟有没有资格挑战\x01",
            "我『钓皇』……\x01",
            "就让我来检验一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "比赛名称是『爆钓必中比赛』——\x01",
            "你究竟能不能跟上我的脚步呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3760")

    label("loc_3709")


    #C0046
    ChrTalk(
        0x8,
        "哼，做好心理准备了吗？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "就在『爆钓必中比赛』中\x01",
            "让我见识一下你的气概和实力吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3760")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要以『爆钓必中』为规则\x01",
            "向雷克罗德Ⅲ世挑战吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "挑战\x01",      # 0
            "放弃\x01",      # 1
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
        (0, "loc_37E7"),
        (1, "loc_3983"),
        (SWITCH_DEFAULT, "loc_39C6"),
    )


    label("loc_37E7")


    #C0049
    ChrTalk(
        0x8,
        "有胆色……那就开始吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E2(0x2)
    ClearMapFlags(0x1)
    OP_68(47160, -5700, -57300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x0, 31550, -5620, -50140, 315)
    OP_31(0x1)
    SetChrPos(0x101, 47200, -6300, -56050, 90)
    OP_93(0xFE, 0x5A, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    MiniGame(0x7, 0x5, 0x8, 0xCD8C, 0xFFFFE764, 0xFFFF24B4, 0xCD6E, 0xFFFFE764, 0xFFFF1352)
    SetChrPos(0x0, 56010, -5600, -3460, 89)
    OP_31(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38BF")
    Call(0, 28)
    Return()

    label("loc_38BF")

    OP_68(45050, -5700, -58570, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 44490, -6270, -58570, 90)
    OP_93(0xFE, 0x10E, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_391E")
    Call(0, 26)
    Jump("loc_3942")

    label("loc_391E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3931")
    Jump("loc_3942")

    label("loc_3931")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3942")
    Call(0, 27)

    label("loc_3942")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 41770, -5950, -58520, 270)
    OP_31(0x1)
    SetMapFlags(0x1)
    OP_69(0xFF, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_39C6")

    label("loc_3983")


    #C0050
    ChrTalk(
        0x8,
        "哼，事到如今，却开始害怕了吗？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "……算了，随便你吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39C6")

    label("loc_39C6")

    Return()

    # Function_25_3658 end

    def Function_26_39C7(): pass

    label("Function_26_39C7")


    #C0052
    ChrTalk(
        0x8,
        (
            "呵呵，\x01",
            "体会到水准的差距了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "实在是\x01",
            "毫无悬念啊。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_26_39C7 end

    def Function_27_3A04(): pass

    label("Function_27_3A04")


    #C0054
    ChrTalk(
        0x8,
        (
            "哼，没想到你会\x01",
            "中途放弃比赛。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "……无聊，真是无聊啊。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_27_3A04 end

    def Function_28_3A44(): pass

    label("Function_28_3A44")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadEffect(0x0, "eff\\mgm03_02.eff")
    LoadEffect(0x1, "eff\\mgm03_01.eff")
    LoadEffect(0x2, "eff\\step04.eff")
    OP_68(49440, -6400, -56150, 0)
    MoveCamera(65, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(24610, 0)
    SetChrPos(0x101, 46750, -6300, -56900, 180)
    TurnDirection(0x8, 0x101, 0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x102, 42000, -5600, -54570, 90)
    SetChrPos(0x104, 41350, -5610, -56000, 90)
    SetChrPos(0x103, 41570, -5600, -53840, 90)
    SetChrPos(0x109, 40430, -5600, -55560, 90)
    SetChrPos(0x105, 40020, -5600, -54360, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0056
    ChrTalk(
        0x8,
        "呵呵呵……哈哈哈哈哈！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "有趣，真是有趣……\x01",
            "没想到你能在『爆钓必中比赛』中\x01",
            "有这等表现。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "好吧，\x01",
            "我承认你的实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "但重点还在于正式决战啊……\x01",
            "嗯，什么样的比赛规则\x01",
            "才与这最终对决相符呢——\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(11, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 60110, -6300, -61610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(11, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, 60110, -6300, -61610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 60110, -6300, -61610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 60110, -6300, -61610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(12, 0, 100, 0)
    Sleep(150)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3D55():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D55)
    Sleep(50)

    def lambda_3D65():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D65)
    Sleep(300)
    StopEffect(0x1, 0x2)

    #C0060
    ChrTalk(
        0x101,
        "#00005F刚、刚才那是……！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "哈哈哈，看来有个\x01",
            "大家伙感应到我们的热情，\x01",
            "闯到这里了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "刚才那条应该是珍珠龙鱼……\x01",
            "但它拥有４亚矩左右的巨大身躯。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "不错，那正是极度稀有的\x01",
            "高级鱼种——巨骨龙皇鱼！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "哈哈哈，真没想到能在\x01",
            "克洛斯贝尔见到它！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#00005F巨、巨骨龙皇鱼……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    #C0066
    ChrTalk(
        0x8,
        (
            "总之，我们这场最终对决\x01",
            "的规则就此决定！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    #C0067
    ChrTalk(
        0x8,
        (
            "先钓起那条\x01",
            "巨骨龙皇鱼的人……\x01",
            "就是这场对决的胜利者。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        "你没有异议吧？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00003F好、好的，\x01",
            "我没有异议……\x02\x03",

            "#00001F（如果能钓起那种庞然大物……\x01",
            "  确实很了不起呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        "呵呵，那就决定了。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "那么，在接下来的比赛中，\x01",
            "时间与回合都无关紧要了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "到底谁能抢先一步，\x01",
            "把它钓起来呢……\x01",
            "比赛从现在开始！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x191, 0)
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 46320, -6300, -56810, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_3A44 end

    def Function_29_403F(): pass

    label("Function_29_403F")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch32200.itc", 0x1E)
    LoadChrToIndex("chr/ch46100.itc", 0x1F)
    LoadChrToIndex("chr/ch45700.itc", 0x20)
    LoadChrToIndex("chr/ch45800.itc", 0x21)
    LoadChrToIndex("chr/ch45900.itc", 0x22)
    LoadChrToIndex("chr/ch46000.itc", 0x23)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "巨骨龙皇鱼又吐出了什么东西。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEF, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40E2")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xEF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    AddItemNumber(0xEF, 1)
    Jump("loc_40F9")

    label("loc_40E2")


    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    AddItemNumber(0x6F, 1)

    label("loc_40F9")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(40790, -6600, -57830, 0)
    MoveCamera(41, 18, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23320, 0)
    SetChrPos(0x101, 37690, -6090, -62260, 0)
    SetChrPos(0x8, 37660, -5910, -60080, 180)
    SetChrPos(0x102, 40850, -5600, -55900, 225)
    SetChrPos(0x103, 39410, -5600, -55320, 225)
    SetChrPos(0x104, 42210, -5640, -55120, 225)
    SetChrPos(0x109, 40880, -5610, -54220, 225)
    SetChrPos(0x105, 39030, -5610, -53880, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0076
    ChrTalk(
        0x8,
        (
            "竟、竟然会这样。\x01",
            "没想到会被你抢先钓到……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "……唔，但输了就是输了，\x01",
            "看来我不得不坦然承认啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        "就把这东西送给你……不，送给阁下吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0079
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0080
    ChrTalk(
        0x8,
        (
            "另外，既然阁下得到了这个证明，\x01",
            "按照钓皇俱乐部的规定，\x01",
            "我在此授予阁下『钓皇杀手』这个称号。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "这是全大陆所有钓师都要肃然起敬的称号，\x01",
            "阁下应该为此感到无比光荣。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        "接下来，关于我们的赛前约定……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 30650, -5880, -57210, 135)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 31220, -5790, -55880, 135)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 34190, -5610, -52480, 225)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 33770, -5600, -52140, 225)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 33620, -5600, -51290, 225)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 32560, -5600, -52360, 225)

    #C0083
    ChrTalk(
        0x15,
        "雷、雷克罗德先生！\x02",
    )

    CloseMessageWindow()

    def lambda_4470():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4470)
    Sleep(50)

    def lambda_4480():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4480)
    OP_68(37270, -5200, -59200, 4000)
    MoveCamera(331, 19, 0, 4000)
    OP_6E(530, 4000)
    SetCameraDistance(19090, 4000)

    def lambda_44BB():
        OP_95(0xFE, 34400, -6070, -60340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_44BB)
    Sleep(50)

    def lambda_44D8():
        OP_95(0xFE, 36920, -5650, -57140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_44D8)
    Sleep(50)

    def lambda_44F5():
        OP_95(0xFE, 34950, -5770, -58800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_44F5)
    Sleep(50)

    def lambda_4512():
        OP_95(0xFE, 37600, -5610, -55680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4512)
    Sleep(50)

    def lambda_452F():
        OP_95(0xFE, 35900, -5610, -55640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_452F)
    Sleep(50)

    def lambda_454C():
        OP_95(0xFE, 35440, -5610, -56920, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_454C)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)

    #C0084
    ChrTalk(
        0x12,
        (
            "呼……呼……\x01",
            "罗伊德团员，难道你……\x02",
        )
    )

    CloseMessageWindow()

    #N0085
    NpcTalk(
        0x13,
        "？？？",
        (
            "#5P唔，看来已经\x01",
            "分出胜负了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x8, 500)

    #C0086
    ChrTalk(
        0x8,
        "你、你是哈巴德……！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        "哈巴德·费瑟尔！！\x02",
    )

    CloseMessageWindow()

    def lambda_45F9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_45F9)
    Sleep(50)

    def lambda_4609():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4609)
    Sleep(50)

    def lambda_4619():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4619)
    Sleep(50)

    def lambda_4629():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4629)
    Sleep(50)

    def lambda_4639():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4639)

    #C0088
    ChrTalk(
        0x13,
        (
            "#5P哦，你是威廉小鬼……\x01",
            "许久不见，都长这么大了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x13,
        (
            "#5P不，现在应该称呼你为\x01",
            "雷克罗德Ⅲ世了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "哼，你这个叛徒！\x01",
            "不要随便直呼我的名字！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "你这家伙……为什么抛弃了钓皇俱乐部！\x01",
            "为什么对我父亲恩将仇报！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x13,
        "#5P唔……那是一场误会。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x13,
        (
            "#5P虽然我与钓皇俱乐部\x01",
            "之间确实有过\x01",
            "一些争执……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x13,
        (
            "#5P但我退出钓皇俱乐部，\x01",
            "成立钓公师团，都在事前\x01",
            "经过你父亲雷克罗德Ⅱ世的许可。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x13,
        (
            "#5P正因如此，\x01",
            "我才会将身在钓皇俱乐部的时期\x01",
            "所拥有的称号——『太公望』沿用至今。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "哼，闭嘴，\x01",
            "不要说些冠冕堂皇的借口！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "按照我原本的打算，\x01",
            "一旦见到你，就要好好教训一顿……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "但我现在心情很郁闷，\x01",
            "就等下次有机会时再说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "在那之前，你就\x01",
            "做好准备等着吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x13,
        "#5P唔……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "还有，赛尔丹。\x01",
            "按照约定，我会把事务所返还给你，\x01",
            "不过你要给我一些整理随身物品的时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "收拾完毕之后，\x01",
            "我们钓皇俱乐部就会\x01",
            "从克洛斯贝尔彻底撤离。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x12,
        "……好，我知道了。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x12,
        (
            "另外，\x01",
            "你当时曾经说过，不管是什么内容，\x01",
            "都会听从我们的一项命令吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        "哼，你已经想好了吗？\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x12,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x101, 500)

    #C0107
    ChrTalk(
        0x12,
        "罗伊德团员，不介意由我来决定吧？\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00001F嗯，那当然。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x8, 500)

    #C0109
    ChrTalk(
        0x12,
        (
            "咳……\x01",
            "那我就下达命令了。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x12,
        (
            "『取消钓皇俱乐部\x01",
            "  从克洛斯贝尔\x01",
            "  撤离的决定』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4BE9():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4BE9)
    Sleep(50)

    def lambda_4BF9():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4BF9)
    Sleep(50)

    def lambda_4C09():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4C09)
    Sleep(50)

    def lambda_4C19():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4C19)
    Sleep(50)

    def lambda_4C29():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4C29)
    Sleep(300)

    #C0111
    ChrTalk(
        0x101,
        "#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x13,
        "#5P哦……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "你、你这家伙……\x01",
            "是在小看我们吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x12,
        "不……正相反。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x12,
        (
            "通过与你们的比试，\x01",
            "我们才认识到自己以前\x01",
            "所处的世界有多么狭窄。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x12,
        (
            "如果今后有机会，\x01",
            "希望还能与你们一起钓鱼……\x01",
            "我只是这样想而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        "#00002F赛尔丹分部长……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x13,
        (
            "#5P嗯，不愧是我\x01",
            "欣赏的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        "一起钓鱼……？\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "我们才不会和你们\x01",
            "这些家伙打成一片——\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x12,
        "那也随你们。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x12,
        (
            "只要不和我们找麻烦，\x01",
            "不管是谁，\x01",
            "我们都很欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x12,
        (
            "只要你们遵守这个原则，\x01",
            "就可以随意使用\x01",
            "我们的租船小屋。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0124
    ChrTalk(
        0x8,
        (
            "谁、谁会使用\x01",
            "那种简陋的小屋啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "不过，既然事先有约，\x01",
            "我会接受你的命令……\x01",
            "但你以后要是再想反悔，我可就恕难从命了。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        "即使如此也没问题吗？\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x12,
        "嗯，没问题。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "哼……\x01",
            "哈巴德也好，你也好，\x01",
            "都是些滥好人。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "啊，还有一件事。\x01",
            "负责接待的塞拉姆……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "原本并不是我们\x01",
            "钓皇俱乐部的成员，\x01",
            "而且她本来是很想加入钓公师团的。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        "今后就拜托你们照顾她了，可以吗？\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x12,
        "嗯，小事一桩。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        "哼，我要说的就这么多。\x02",
    )

    CloseMessageWindow()
    OP_68(37650, -5000, -59390, 3000)
    MoveCamera(4, 23, 0, 3000)
    OP_6E(530, 3000)
    SetCameraDistance(18950, 3000)

    def lambda_5026():
        OP_95(0xFE, 36110, -5730, -58120, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5026)
    Sleep(500)

    def lambda_5043():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x101, 1, lambda_5043)
    Sleep(50)

    def lambda_5058():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x13, 1, lambda_5058)
    Sleep(50)

    def lambda_506D():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x12, 1, lambda_506D)
    Sleep(50)

    def lambda_5082():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x102, 1, lambda_5082)
    Sleep(50)

    def lambda_5097():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x103, 1, lambda_5097)
    Sleep(50)

    def lambda_50AC():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x104, 1, lambda_50AC)
    Sleep(50)

    def lambda_50C1():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x109, 1, lambda_50C1)
    Sleep(50)

    def lambda_50D6():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x105, 1, lambda_50D6)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)

    #C0134
    ChrTalk(
        0x8,
        (
            "好了，各位，\x01",
            "我们赶快收拾好东西，返回本国吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(185, 20, -1, -1)
    SetChrName("钓杰四天王")

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "遵命，老板！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_95(0x8, 34490, -5660, -57880, 2000, 0x0)

    def lambda_516A():
        OP_95(0xFE, 31090, -5670, -51170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_516A)
    Sleep(50)

    def lambda_5187():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5187)
    Sleep(50)

    def lambda_5197():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5197)
    Sleep(50)

    def lambda_51A7():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_51A7)
    Sleep(50)

    def lambda_51B7():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_51B7)
    WaitChrThread(0x15, 1)
    Sleep(1000)

    def lambda_51CB():
        OP_95(0xFE, 33250, -5600, -50050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_51CB)
    Sleep(50)

    def lambda_51E8():
        OP_95(0xFE, 34190, -5610, -52480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_51E8)
    Sleep(50)

    def lambda_5205():
        OP_95(0xFE, 32560, -5600, -52360, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5205)
    Sleep(50)

    def lambda_5222():
        OP_95(0xFE, 33770, -5600, -52140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5222)
    OP_68(37650, -3000, -59390, 3000)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("r0200", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_403F end

    SaveToFile()

Try(main)
