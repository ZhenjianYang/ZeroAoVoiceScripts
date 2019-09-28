from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r1030.bin",                # FileName
        "r1030",                    # MapName
        "r1030",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("r1030", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x07,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 4, 0, 5],
    )

    BuildStringList((
        "r1030",                  # 0
        "警备队员",               # 1
        "警备队员",               # 2
        "『银螭』特里同",         # 3
        "巴士",                   # 4
        "特别任务支援科的车",     # 5
        "飙车族",                 # 6
        "梅尔卡瓦",               # 7
        "梅尔卡瓦",               # 8
        "火焰蛇虎鱼",             # 9
        "火焰蛇虎鱼",             # 10
        "硬岩龙",                 # 11
        "硬岩龙",                 # 12
        "br1000",                 # 13
        "br1000",                 # 14
        "br1000",                 # 15
        "br1000",                 # 16
        "br1000",                 # 17
        "br1000",                 # 18
        "br1000",                 # 19
        "br1000",                 # 20
        "br1000",                 # 21
        "克洛斯贝尔市方向",       # 22
        "贝尔加德门方向",         # 23
        "警察学校方向",           # 24
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_B4", 0,   0,   7,   0,   2,   2,   2)
    Sepith("Sepith_C4", 2,   2,   0,   0,   3,   3,   3)
    Sepith("Sepith_D4", 2,   1,   5,   0,   0,   3,   2)
    Sepith("Sepith_E4", 0,   3,   0,   5,   2,   3,   0)
    Sepith("Sepith_F4", 2,   1,   4,   1,   0,   2,   2)
    Sepith("Sepith_104", 11,  7,   4,   3,   6,   12,  7)

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

    # monster count: 12

    BattleInfo(
        "BattleInfo_174", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_B4", 30, 40, 20, 10,
        (
            ("ms71300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms71300.dat", "ms71300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms71300.dat", "ms70400.dat", "ms71300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms71300.dat", "ms71300.dat", "ms70400.dat", "ms66900.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_23C", 0x0000, 50, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_C4", 30, 30, 20, 20,
        (
            ("ms64200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms64200.dat", "ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms64200.dat", "ms66900.dat", "ms64200.dat", "ms66900.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_304", 0x0000, 50, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3CC", 0x0000, 50, 6, 60, 8, 1, 40, 0, "br1000", "Sepith_E4", 30, 40, 20, 10,
        (
            ("ms70300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms70300.dat", "ms70300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms70300.dat", "ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_494", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_F4", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms71900.dat", "ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_55C", 0x0000, 84, 6, 45, 6, 1, 30, 0, "br1000", "Sepith_104", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5F8", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72400.dat", "ms72400.dat", "ms72400.dat", "ms72400.dat", "ms72400.dat", "ms72400.dat", 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7451", "ed7453", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_63C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7453", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_680", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7453", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch45700.itc",                   # 00
        "chr/ch31200.itc",                   # 01
        "chr/ch31300.itc",                   # 02
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
        "monster/ch70350.itc",               # 10
        "monster/ch70351.itc",               # 11
        "monster/ch71350.itc",               # 12
        "monster/ch71351.itc",               # 13
        "monster/ch71950.itc",               # 14
        "monster/ch71950.itc",               # 15
        "monster/ch64250.itc",               # 16
        "monster/ch64251.itc",               # 17
        "monster/ch63250.itc",               # 18
        "monster/ch63251.itc",               # 19
        "monster/ch60750.itc",               # 1A
        "monster/ch60750.itc",               # 1B
        "monster/ch72450.itc",               # 1C
        "monster/ch72450.itc",               # 1D
    ))

    DeclNpc(-55560,  -6000,   -78230,  135,  389,  0x0, 0,   1,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-54700,  -6000,   -79209,  315,  389,  0x0, 0,   2,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-59650,  0,       34909,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-39330,  0,       46720,   270,  485,  0x0, 0,   18,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-82230,  -2000,   -27079,  270,  485,  0x0, 0,   18,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-39330,  0,       46720,   270,  485,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(-82230,  -2000,   -27079,  270,  485,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)

    DeclMonster(-17880,  910,     0,       0x1010000,    "BattleInfo_174", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-44410,  -7750,   0,       0x1010000,    "BattleInfo_23C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-16440,  44520,   0,       0x1010000,    "BattleInfo_304", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-39150,  60950,   0,       0x1010000,    "BattleInfo_3CC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-74290,  -25740,  -2000,   0x1010000,    "BattleInfo_304", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-34710,  -42590,  -4000,   0x1010000,    "BattleInfo_174", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-62760,  -62500,  -6000,   0x1010000,    "BattleInfo_494", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-19130,  6440,    0,       0x1010000,    "BattleInfo_55C", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-59570,  -9280,   0,       0x1010000,    "BattleInfo_55C", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-56370,  -76140,  -6000,   0x1010000,    "BattleInfo_55C", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-27490,  31330,   0,       0x1010000,    "BattleInfo_55C", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-23820,  53310,   0,       0x18500B4,    "BattleInfo_5F8", 0,   28,  0xFFFF, 12, 13)

    DeclEvent(0x0000, 0, 28,  -56.0,                 -87.0,                 -7.0,                  2500.0,                [0.05000000074505806,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.799999952316284,     17.399999618530273,    1.399999976158142,     1.0])
    DeclEvent(0x0000, 0, 29,  -32.5,                 1.5,                   -1.0,                  2025.0,                [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666667014360428,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   5.4166669845581055,    -0.10000000894069672,  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 30,  -56.0,                 -80.0,                 -7.0,                  2500.0,                [0.05000000074505806,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.799999952316284,     16.0,                  1.399999976158142,     1.0])
    DeclEvent(0x0040, 0, 22,  -23.81999969482422,    53.310001373291016,    0.0,                   16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   2.9774999618530273,    -6.663750171661377,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 26,  -56.4900016784668,     -86.98999786376953,    -6.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.766000270843506,     28.996665954589844,    1.2000000476837158,    1.0])
    DeclEvent(0x0000, 0, 54,  -34.95000076293945,    23.649999618530273,    0.0,                   900.0,                 [0.035355325788259506, 0.23570235073566437,   -0.0,                  0.0,                   -0.035355351865291595, 0.23570218682289124,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.0718226432800293,    2.663440704345703,     -0.0,                  1.0])
    DeclEvent(0x0000, 0, 55,  -57.27000045776367,    20.360000610351562,    0.0,                   225.0,                 [0.23570218682289124,  0.07071070373058319,   -0.0,                  0.0,                   -0.23570235073566437,  0.07071065157651901,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   18.297563552856445,    2.6099331378936768,    -0.0,                  1.0])

    DeclActor(-37700,  0,       8150,    1200,    -37700,  1000,    8150,    0x007C, 0,  25, 0x0000)
    DeclActor(-12140,  0,       44860,   1200,    -12140,  1000,    44860,   0x007C, 0,  6,  0x0000)
    DeclActor(-41210,  0,       -8039,   1200,    -41210,  1000,    -8039,   0x007C, 0,  7,  0x0000)
    DeclActor(-27210,  -3900,   -44030,  1200,    -27210,  -2900,   -44030,  0x007C, 0,  8,  0x0000)
    DeclActor(-39330,  0,       46720,   1200,    -39330,  0,       46720,   0x007C, 0,  9,  0x0000)
    DeclActor(-82230,  -2000,   -27080,  1200,    -82230,  -2000,   -27080,  0x007C, 0,  10, 0x0000)
    DeclActor(-57830,  0,       35060,   1200,    -58330,  -1000,   41020,   0x007C, 0,  23, 0x0000)
    DeclActor(-36190,  0,       16430,   1200,    -36190,  2000,    16430,   0x007C, 0,  24, 0x0000)
    DeclActor(-60000,  0,       32650,   1200,    -60000,  2000,    32650,   0x007C, 0,  24, 0x0000)
    DeclActor(-49450,  -6000,   -76260,  1200,    -49360,  -3000,   -76640,  0x007C, 0,  57, 0x0000)
    DeclActor(-37790,  0,       10900,   1500,    -37790,  1700,    10900,   0x007C, 0,  58, 0x0000)

    PlaceName(29.0, 0.0, 19.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-95.0, 0.0, 84.0, 0x0000, 0x0000, "贝尔加德门方向")
    PlaceName(-55.0, 0.0, -114.0, 0x0000, 0x0000, "警察学校方向")
    PlaceName(-37.5, 0.0, 8.449999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 12
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 13

    ScpFunction((
        "Function_0_101C",         # 00, 0
        "Function_1_10D4",         # 01, 1
        "Function_2_10F3",         # 02, 2
        "Function_3_1112",         # 03, 3
        "Function_4_117E",         # 04, 4
        "Function_5_17B0",         # 05, 5
        "Function_6_28FB",         # 06, 6
        "Function_7_2A36",         # 07, 7
        "Function_8_2B71",         # 08, 8
        "Function_9_2CAC",         # 09, 9
        "Function_10_2FD0",        # 0A, 10
        "Function_11_32F4",        # 0B, 11
        "Function_12_3317",        # 0C, 12
        "Function_13_331B",        # 0D, 13
        "Function_14_33CF",        # 0E, 14
        "Function_15_3502",        # 0F, 15
        "Function_16_3635",        # 10, 16
        "Function_17_3686",        # 11, 17
        "Function_18_371A",        # 12, 18
        "Function_19_3773",        # 13, 19
        "Function_20_37DD",        # 14, 20
        "Function_21_4302",        # 15, 21
        "Function_22_4652",        # 16, 22
        "Function_23_489E",        # 17, 23
        "Function_24_4B4C",        # 18, 24
        "Function_25_4E79",        # 19, 25
        "Function_26_5113",        # 1A, 26
        "Function_27_5638",        # 1B, 27
        "Function_28_57B7",        # 1C, 28
        "Function_29_612B",        # 1D, 29
        "Function_30_64C9",        # 1E, 30
        "Function_31_6AC5",        # 1F, 31
        "Function_32_708E",        # 20, 32
        "Function_33_70AD",        # 21, 33
        "Function_34_710D",        # 22, 34
        "Function_35_7144",        # 23, 35
        "Function_36_71C4",        # 24, 36
        "Function_37_71E9",        # 25, 37
        "Function_38_724E",        # 26, 38
        "Function_39_7269",        # 27, 39
        "Function_40_72C4",        # 28, 40
        "Function_41_7998",        # 29, 41
        "Function_42_7A0A",        # 2A, 42
        "Function_43_7A6C",        # 2B, 43
        "Function_44_7ACE",        # 2C, 44
        "Function_45_7B3E",        # 2D, 45
        "Function_46_7BD8",        # 2E, 46
        "Function_47_7C10",        # 2F, 47
        "Function_48_7C56",        # 30, 48
        "Function_49_7C8E",        # 31, 49
        "Function_50_7D08",        # 32, 50
        "Function_51_7E94",        # 33, 51
        "Function_52_7EDD",        # 34, 52
        "Function_53_7F14",        # 35, 53
        "Function_54_7F73",        # 36, 54
        "Function_55_8034",        # 37, 55
        "Function_56_8099",        # 38, 56
        "Function_57_8104",        # 39, 57
        "Function_58_816A",        # 3A, 58
    ))


    def Function_0_101C(): pass

    label("Function_0_101C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_105C"),
        (1, "loc_1068"),
        (2, "loc_1074"),
        (3, "loc_1080"),
        (4, "loc_108C"),
        (5, "loc_1098"),
        (6, "loc_10A4"),
        (SWITCH_DEFAULT, "loc_10B0"),
    )


    label("loc_105C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_10BC")

    label("loc_1068")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_10BC")

    label("loc_1074")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_10BC")

    label("loc_1080")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_10BC")

    label("loc_108C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_10BC")

    label("loc_1098")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_10BC")

    label("loc_10A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10BC")

    label("loc_10B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10BC")

    label("loc_10BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10D3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10BC")

    label("loc_10D3")

    Return()

    # Function_0_101C end

    def Function_1_10D4(): pass

    label("Function_1_10D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10F2")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_10D4")

    label("loc_10F2")

    Return()

    # Function_1_10D4 end

    def Function_2_10F3(): pass

    label("Function_2_10F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1111")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_10F3")

    label("loc_1111")

    Return()

    # Function_2_10F3 end

    def Function_3_1112(): pass

    label("Function_3_1112")

    SetMapObjFlags(0x29, 0x2000000)
    SetMapObjFlags(0x2A, 0x2000000)
    SetMapObjFlags(0x28, 0x2000000)
    SetMapObjFlags(0x24, 0x2000000)
    SetMapObjFlags(0x4, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_113F")
    ClearMapObjFlags(0x28, 0x2000000)

    label("loc_113F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1159")
    ClearMapObjFlags(0x29, 0x2000000)
    ClearMapObjFlags(0x2A, 0x2000000)

    label("loc_1159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_116D")
    ClearMapObjFlags(0x24, 0x2000000)

    label("loc_116D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117D")
    ClearMapObjFlags(0x4, 0x2000000)

    label("loc_117D")

    Return()

    # Function_3_1112 end

    def Function_4_117E(): pass

    label("Function_4_117E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_END)), "loc_1198")
    SetChrPos(0xA, -57240, 0, 32830, 95)

    label("loc_1198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11AB")
    SetChrFlags(0xA, 0x80)
    Jump("loc_125E")

    label("loc_11AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_11C2")
    SetChrFlags(0xA, 0x80)

    label("loc_11C2")

    Jump("loc_125E")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11D5")
    Jump("loc_125E")

    label("loc_11D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11F7")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    Jump("loc_125E")

    label("loc_11F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_1205")
    Jump("loc_125E")

    label("loc_1205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1213")
    Jump("loc_125E")

    label("loc_1213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1221")
    Jump("loc_125E")

    label("loc_1221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_122F")
    Jump("loc_125E")

    label("loc_122F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1242")
    SetChrFlags(0xA, 0x10)
    Jump("loc_125E")

    label("loc_1242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1250")
    Jump("loc_125E")

    label("loc_1250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_125E")
    SetChrFlags(0xA, 0x80)

    label("loc_125E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_126D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 40)

    label("loc_126D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_127E")
    Event(0, 31)

    label("loc_127E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1722")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130B")
    SetScenarioFlags(0x38, 0)

    label("loc_130B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1321")
    SetScenarioFlags(0x38, 1)

    label("loc_1321")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1337")
    SetScenarioFlags(0x38, 2)

    label("loc_1337")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_134D")
    SetScenarioFlags(0x38, 3)

    label("loc_134D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1363")
    SetScenarioFlags(0x38, 4)

    label("loc_1363")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1379")
    SetScenarioFlags(0x38, 5)

    label("loc_1379")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_138F")
    SetScenarioFlags(0x38, 6)

    label("loc_138F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A5")
    SetScenarioFlags(0x38, 7)

    label("loc_13A5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13BB")
    SetScenarioFlags(0x39, 0)

    label("loc_13BB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D1")
    SetScenarioFlags(0x39, 1)

    label("loc_13D1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E7")
    SetScenarioFlags(0x39, 2)

    label("loc_13E7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13FD")
    SetScenarioFlags(0x39, 3)

    label("loc_13FD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1413")
    SetScenarioFlags(0x39, 4)

    label("loc_1413")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1429")
    SetScenarioFlags(0x39, 5)

    label("loc_1429")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143F")
    SetScenarioFlags(0x39, 6)

    label("loc_143F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1455")
    SetScenarioFlags(0x39, 7)

    label("loc_1455")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_146B")
    SetScenarioFlags(0x3A, 0)

    label("loc_146B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1481")
    SetScenarioFlags(0x3A, 1)

    label("loc_1481")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1497")
    SetScenarioFlags(0x3A, 2)

    label("loc_1497")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AD")
    SetScenarioFlags(0x3A, 3)

    label("loc_14AD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C3")
    SetScenarioFlags(0x3A, 4)

    label("loc_14C3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D9")
    SetScenarioFlags(0x3A, 5)

    label("loc_14D9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14EF")
    SetScenarioFlags(0x3A, 6)

    label("loc_14EF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1505")
    SetScenarioFlags(0x3A, 7)

    label("loc_1505")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_151B")
    SetScenarioFlags(0x3B, 0)

    label("loc_151B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1531")
    SetScenarioFlags(0x3B, 1)

    label("loc_1531")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1547")
    SetScenarioFlags(0x3B, 2)

    label("loc_1547")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155D")
    SetScenarioFlags(0x3B, 3)

    label("loc_155D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1573")
    SetScenarioFlags(0x3B, 4)

    label("loc_1573")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1589")
    SetScenarioFlags(0x3B, 5)

    label("loc_1589")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159F")
    SetScenarioFlags(0x3B, 6)

    label("loc_159F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B5")
    SetScenarioFlags(0x3B, 7)

    label("loc_15B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15CB")
    SetScenarioFlags(0x3D, 5)

    label("loc_15CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E1")
    SetScenarioFlags(0x3D, 6)

    label("loc_15E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F7")
    SetScenarioFlags(0x3D, 7)

    label("loc_15F7")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1632")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1722")

    label("loc_1632")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1655")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1722")

    label("loc_1655")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1678")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1722")

    label("loc_1678")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169B")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1722")

    label("loc_169B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BE")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1722")

    label("loc_16BE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E1")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1722")

    label("loc_16E1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1704")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1722")

    label("loc_1704")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1722")
    SetScenarioFlags(0x3C, 7)

    label("loc_1722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1738")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176A")
    SetChrPos(0x0, -36420, 0, 17340, 315)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 17)

    label("loc_176A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_179D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179D")
    SetChrPos(0x0, -60000, 0, 32650, 315)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_179D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_17AC")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 16)

    label("loc_17AC")

    Call(0, 11)
    Return()

    # Function_4_117E end

    def Function_5_17B0(): pass

    label("Function_5_17B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_17C2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17C2")

    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17DA")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_17DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17ED")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_17ED")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1805")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1805")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_181D")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_181D")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1835")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1835")

    ModifyEventFlags(0, 5, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_184D")
    ModifyEventFlags(1, 5, 0x80)

    label("loc_184D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1860")
    ModifyEventFlags(1, 5, 0x80)

    label("loc_1860")

    ModifyEventFlags(0, 6, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1878")
    ModifyEventFlags(1, 6, 0x80)

    label("loc_1878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_188B")
    OP_1B(0x1, 0x0, 0x38)

    label("loc_188B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18B1")
    SetMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    OP_70(0x3, 0x0)
    OP_10(0x2, 0x0)
    Jump("loc_18D4")

    label("loc_18B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18CA")
    SetMapObjFlags(0x3, 0x4)
    Jump("loc_18D4")

    label("loc_18CA")

    SetMapObjFlags(0x7, 0x4)
    OP_70(0x3, 0x28)

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1985")
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
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

    label("loc_1985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1993")
    Jump("loc_1A2D")

    label("loc_1993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19C2")
    ClearMapObjFlags(0x24, 0x4)
    SetMapObjFrame(0x24, "light", 0x0, 0x1)
    SetMapObjFrame(0x24, "mark01", 0x0, 0x1)
    Jump("loc_1A2D")

    label("loc_19C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_19D0")
    Jump("loc_1A2D")

    label("loc_19D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_19DE")
    Jump("loc_1A2D")

    label("loc_19DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_19EC")
    Jump("loc_1A2D")

    label("loc_19EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19FA")
    Jump("loc_1A2D")

    label("loc_19FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A08")
    Jump("loc_1A2D")

    label("loc_1A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A16")
    Jump("loc_1A2D")

    label("loc_1A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_1A24")
    Jump("loc_1A2D")

    label("loc_1A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1A2D")

    label("loc_1A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1A54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4F")
    ClearChrFlags(0x1F, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    SetChrFlags(0x1F, 0x8000)

    label("loc_1A4F")

    Jump("loc_1A5E")

    label("loc_1A54")

    SetChrFlags(0x1F, 0x80)
    ModifyEventFlags(0, 3, 0x80)

    label("loc_1A5E")

    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2587")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_2587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_2669")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
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
    Jump("loc_2711")

    label("loc_2669")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
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

    label("loc_2711")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -58330, -1000, 41020, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2775")
    OP_66(0x6, 0x1)

    label("loc_2775")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('初级竿', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小巧射手', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('竹竿', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢竿侵略者', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('水中支配者', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27BA")
    OP_65(0x6, 0x1)

    label("loc_27BA")

    MiniGame(0x2F, 0x7, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xB, 0x80)
    SetMapObjFlags(0x4, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27FA")
    OP_70(0x0, 0x0)
    Jump("loc_27FE")

    label("loc_27FA")

    OP_70(0x0, 0x1E)

    label("loc_27FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2811")
    OP_70(0x1, 0x0)
    Jump("loc_2815")

    label("loc_2811")

    OP_70(0x1, 0x1E)

    label("loc_2815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2828")
    OP_70(0x2, 0x0)
    Jump("loc_282C")

    label("loc_2828")

    OP_70(0x2, 0x1E)

    label("loc_282C")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_288D")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -39330, 0, 46720, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_288D")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28D9")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -82230, -2000, -27080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_28D9")

    OP_1C(0x0, 0x25, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0x26, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0x27, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    Return()

    # Function_5_17B0 end

    def Function_6_28FB(): pass

    label("Function_6_28FB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29ED")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('睡眠之刃', 1)"), scpexpr(EXPR_END)), "loc_297E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E3, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_29E8")

    label("loc_297E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x9D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x9D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_29E8")

    Jump("loc_2A2A")

    label("loc_29ED")

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

    label("loc_2A2A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_28FB end

    def Function_7_2A36(): pass

    label("Function_7_2A36")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B28")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('中回复药', 1)"), scpexpr(EXPR_END)), "loc_2AB9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
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
    SetScenarioFlags(0x1E3, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_2B23")

    label("loc_2AB9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
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

    label("loc_2B23")

    Jump("loc_2B65")

    label("loc_2B28")

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

    label("loc_2B65")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_2A36 end

    def Function_8_2B71(): pass

    label("Function_8_2B71")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C63")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('Ｕ材料', 1)"), scpexpr(EXPR_END)), "loc_2BF4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
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
    SetScenarioFlags(0x1E3, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_2C5E")

    label("loc_2BF4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2C5E")

    Jump("loc_2CA0")

    label("loc_2C63")

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

    label("loc_2CA0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_2B71 end

    def Function_9_2CAC(): pass

    label("Function_9_2CAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E45")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_2E2B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E26")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2E23")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2D4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2D4E)
    TurnDirection(0x10, 0x0, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    PlayEffect(0x7, 0x1, 0x10, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_63C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1E")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E05")
    Call(1, 5)
    Jump("loc_2E1E")

    label("loc_2E05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E1B")
    Call(1, 4)
    Jump("loc_2E1E")

    label("loc_2E1B")

    Call(1, 3)

    label("loc_2E1E")

    Jump("loc_2E26")

    label("loc_2E23")

    Call(1, 1)

    label("loc_2E26")

    Jump("loc_2E41")

    label("loc_2E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2E41")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2E41")

    TalkEnd(0xFF)
    Return()

    label("loc_2E45")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_2FB6")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB1")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2FAE")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2ED9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2ED9)
    TurnDirection(0x12, 0x0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    PlayEffect(0x7, 0x1, 0x12, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_680", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FA9")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F90")
    Call(1, 5)
    Jump("loc_2FA9")

    label("loc_2F90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2FA6")
    Call(1, 4)
    Jump("loc_2FA9")

    label("loc_2FA6")

    Call(1, 3)

    label("loc_2FA9")

    Jump("loc_2FB1")

    label("loc_2FAE")

    Call(1, 1)

    label("loc_2FB1")

    Jump("loc_2FCC")

    label("loc_2FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2FCC")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2FCC")

    TalkEnd(0xFF)
    Return()

    # Function_9_2CAC end

    def Function_10_2FD0(): pass

    label("Function_10_2FD0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3169")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_314F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314A")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_3147")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3072():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3072)
    TurnDirection(0x11, 0x0, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    PlayEffect(0x7, 0x1, 0x11, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_63C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3142")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3129")
    Call(1, 5)
    Jump("loc_3142")

    label("loc_3129")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_313F")
    Call(1, 4)
    Jump("loc_3142")

    label("loc_313F")

    Call(1, 3)

    label("loc_3142")

    Jump("loc_314A")

    label("loc_3147")

    Call(1, 1)

    label("loc_314A")

    Jump("loc_3165")

    label("loc_314F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_3165")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_3165")

    TalkEnd(0xFF)
    Return()

    label("loc_3169")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_32DA")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32D5")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_32D2")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_31FD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_31FD)
    TurnDirection(0x13, 0x0, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    PlayEffect(0x7, 0x1, 0x13, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_680", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CD")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_32B4")
    Call(1, 5)
    Jump("loc_32CD")

    label("loc_32B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_32CA")
    Call(1, 4)
    Jump("loc_32CD")

    label("loc_32CA")

    Call(1, 3)

    label("loc_32CD")

    Jump("loc_32D5")

    label("loc_32D2")

    Call(1, 1)

    label("loc_32D5")

    Jump("loc_32F0")

    label("loc_32DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_32F0")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_32F0")

    TalkEnd(0xFF)
    Return()

    # Function_10_2FD0 end

    def Function_11_32F4(): pass

    label("Function_11_32F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3316")
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)

    label("loc_3316")

    Return()

    # Function_11_32F4 end

    def Function_12_3317(): pass

    label("Function_12_3317")

    Call(1, 6)
    Return()

    # Function_12_3317 end

    def Function_13_331B(): pass

    label("Function_13_331B")

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
            "克洛斯贝尔市西出口\x01",      # 0
            "贝尔加德门\x01",              # 1
            "放弃\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A7")
    Call(0, 14)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_33C7")

    label("loc_33A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C7")
    Call(0, 15)
    ClearMapFlags(0x8000000)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()

    label("loc_33C7")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_13_331B end

    def Function_14_33CF(): pass

    label("Function_14_33CF")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_34FE")
    Fade(500)
    OP_68(-40030, 600, 12630, 0)
    MoveCamera(38, 23, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(24000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -39500, 0, 7300, 270)
    SetChrPos(0x1, -39500, 0, 8500, 270)
    SetChrPos(0x2, -39500, 0, 9700, 270)
    SetChrPos(0x3, -39500, 0, 10900, 270)
    ClearChrFlags(0xB, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    OP_78(0x4, 0xB)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xB, -34810, 0, 22700, 225)
    OP_D5(0xB, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_34B5():
        OP_95(0xFE, -43990, 0, 13530, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_34B5)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xB, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_34FE")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_14_33CF end

    def Function_15_3502(): pass

    label("Function_15_3502")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_3631")
    Fade(500)
    OP_68(-38160, 600, 3480, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -39500, 0, 7300, 180)
    SetChrPos(0x1, -39500, 0, 8500, 180)
    SetChrPos(0x2, -39500, 0, 9700, 180)
    SetChrPos(0x3, -39500, 0, 10900, 180)
    ClearChrFlags(0xB, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    OP_78(0x4, 0xB)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xB, -27200, 0, 1290, 270)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_35E8():
        OP_95(0xFE, -39660, 0, 1670, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_35E8)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xB, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_3631")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_15_3502 end

    def Function_16_3635(): pass

    label("Function_16_3635")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -36870, 0, 7430, 225)
    OP_31(0x1)
    OP_68(-36870, 600, 7430, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    EventEnd(0x5)
    Return()

    # Function_16_3635 end

    def Function_17_3686(): pass

    label("Function_17_3686")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_36E1")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36D6")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_36DC")

    label("loc_36D6")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_36DC")

    Jump("loc_3705")

    label("loc_36E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36FF")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_3705")

    label("loc_36FF")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_3705")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_3686 end

    def Function_18_371A(): pass

    label("Function_18_371A")

    TalkBegin(0xFE)

    #C0019
    ChrTalk(
        0x8,
        (
            "唉，在雨中工作\x01",
            "真是倒霉死了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "已经大致收拾好了，\x01",
            "能不能赶紧收队回去啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_371A end

    def Function_19_3773(): pass

    label("Function_19_3773")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0x9,
        (
            "总算是把那扇\x01",
            "被破坏得不成样子的\x01",
            "大门收拾完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "到底是怎么把它给\x01",
            "破坏成那个样子的啊……？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_3773 end

    def Function_20_37DD(): pass

    label("Function_20_37DD")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37F5")
    SetScenarioFlags(0x0, 1)

    label("loc_37F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_END)), "loc_3801")
    SetScenarioFlags(0x0, 1)

    label("loc_3801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39B9")
    TurnDirection(0xA, 0x101, 0)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0023
    ChrTalk(
        0xA,
        (
            "哦，莫非你是\x01",
            "钓公师团的成员吗?\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00000F是的，我叫罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xA,
        "哈哈，果然啊。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xA,
        (
            "我的名字是特里同，\x01",
            "大家都称我为『银螭』。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        (
            "但老实说，我都觉得自己\x01",
            "未必能配得上这种绰号。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xA,
        (
            "不过，钓师毕竟也需要气势嘛，\x01",
            "所以我也根据俱乐部的方针起了绰号。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#00006F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        (
            "总之，如果想挑战我，\x01",
            "随时都欢迎哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        (
            "但在那之前，\x01",
            "你要先证明自己拥有挑战的资格。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39B9")
    OP_93(0xA, 0x0, 0x0)

    label("loc_39B9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A07")

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
    Jump("loc_3A11")

    label("loc_3A07")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_402F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A3F")
    TurnDirection(0xA, 0x0, 0)

    label("loc_3A3F")

    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3E9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7E")

    #C0032
    ChrTalk(
        0xA,
        (
            "哦哦，那就让我看看\x01",
            "你的钓鱼手册吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0033
    ChrTalk(
        0xA,
        (
            "嘿～很不错嘛，\x01",
            "竟然真的钓到了\x01",
            "这么多种鱼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xA,
        (
            "呵呵，那我们这就开始期待已久的\x01",
            "『爆钓比赛』吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xA,
        (
            "比赛规则是『五局决胜制』——\x01\x07\x02",

            "率先钓到\x01",
            "五种鱼类的\x07\x00",
            "一方获胜。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        "听上去就很有意思吧？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 0)
    Jump("loc_3BDA")

    label("loc_3B7E")


    #C0037
    ChrTalk(
        0xA,
        "嗯？要和我比赛吗？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "比赛规则是『五局决胜制』——\x01\x07\x02",

            "率先钓到\x01",
            "五种鱼类的\x07\x00",
            "一方获胜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BDA")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要以『五局决胜制』的比赛规则\x01",
            "向『银螭』特里同挑战吗？\x07\x00\x02",
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
        (0, "loc_3C69"),
        (1, "loc_3E65"),
        (SWITCH_DEFAULT, "loc_3E99"),
    )


    label("loc_3C69")


    #C0040
    ChrTalk(
        0xA,
        "哈哈，这才对嘛¤\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    ClearMapFlags(0x1)
    OP_68(-58450, 1000, 33710, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x0, -53410, 0, 15290, 226)
    OP_31(0x1)
    SetChrPos(0x101, -57240, 0, 32830, 95)
    OP_93(0xA, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE("apl/ch51012.itc")
    MiniGame(0x7, 0x3, 0xA, 0xFFFF2CDE, 0x0, 0x821E, 0xFFFF1C26, 0xFFFFFC18, 0xA03C)
    SetChrPos(0x0, -53410, 0, 15290, 226)
    OP_31(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D9E")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_68(-60090, 1000, 33250, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -59650, 0, 32659, 0)
    OP_93(0xA, 0xB4, 0x0)
    Sleep(500)
    Call(0, 50)
    Return()

    label("loc_3D9E")

    OP_68(-58660, 1000, 33990, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -57240, 0, 32830, 315)
    TurnDirection(0xA, 0x101, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DFD")
    Call(0, 51)
    Jump("loc_3E24")

    label("loc_3DFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E13")
    Call(0, 53)
    Jump("loc_3E24")

    label("loc_3E13")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E24")
    Call(0, 52)

    label("loc_3E24")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, -57240, 0, 32830, 315)
    OP_31(0x1)
    SetMapFlags(0x1)
    OP_69(0xFF, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_3E99")

    label("loc_3E65")


    #C0041
    ChrTalk(
        0xA,
        "嗯……是吗，真遗憾。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E94")
    OP_93(0xA, 0x0, 0x0)

    label("loc_3E94")

    Jump("loc_3E99")

    label("loc_3E99")

    Jump("loc_402A")

    label("loc_3E9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3F81")

    #C0042
    ChrTalk(
        0xA,
        (
            "哦哦，那就让我看看\x01",
            "你的钓鱼手册吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    #C0043
    ChrTalk(
        0xA,
        "嗯，真可惜，就差一点点了。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "不过，既然都已经取得了如此成果，\x01",
            "早晚会达到目标的。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xA,
        "就差一点点了，继续加油吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F7C")
    OP_93(0xA, 0x0, 0x0)

    label("loc_3F7C")

    Jump("loc_402A")

    label("loc_3F81")


    #C0046
    ChrTalk(
        0xA,
        (
            "哦哦，快让我看看\x01",
            "你的钓鱼手册。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    #C0047
    ChrTalk(
        0xA,
        "嗯～看来你努力得还不够啊。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xA,
        (
            "总之，如果只有这点成绩，\x01",
            "我是不会接受你的挑战的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_402A")
    OP_93(0xA, 0x0, 0x0)

    label("loc_402A")

    Jump("loc_42F9")

    label("loc_402F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4052")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4060")
    Jump("loc_42F9")

    label("loc_4060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_40B3")

    #C0049
    ChrTalk(
        0xA,
        "嗯～最近似乎一直不太平静啊。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xA,
        (
            "这种时候大概\x01",
            "不太适合钓鱼吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F9")

    label("loc_40B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_410A")

    #C0051
    ChrTalk(
        0xA,
        "哎呀～今天下雨呢～～\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xA,
        (
            "被淋成落汤鸡了，真受不了啊。\x01",
            "啊哈哈哈哈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F9")

    label("loc_410A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4153")

    #C0053
    ChrTalk(
        0xA,
        "呼啊～真困呢～\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        (
            "可昨天明明睡了\x01",
            "十二个小时以上啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F9")

    label("loc_4153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_419B")

    #C0055
    ChrTalk(
        0xA,
        "呼～～～呼～～～～～\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        "嗯嗯～今天的空气也很清新～\x02",
    )

    CloseMessageWindow()
    Jump("loc_42F9")

    label("loc_419B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_41E4")

    #C0057
    ChrTalk(
        0xA,
        "呼～完全不上钩啊～～\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "我是不是\x01",
            "该换种鱼饵试试呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F9")

    label("loc_41E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4228")

    #C0059
    ChrTalk(
        0xA,
        "（发呆）～～～～～～～\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        "嗯嗯～真是安静啊～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_42F9")

    label("loc_4228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_42E2")

    #C0061
    ChrTalk(
        0xA,
        "呼～啊～～哈欠～～～\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "………………………………\x01",
            "……好困…………………\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42DD")

    #C0063
    ChrTalk(
        0x101,
        (
            "#00003F（在这里似乎可以钓到鱼……\x01",
            "  不过已经有别人先来了，还是算了吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42DD")

    Jump("loc_42F9")

    label("loc_42E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_42F0")
    Jump("loc_42F9")

    label("loc_42F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_42F9")

    label("loc_42F9")

    Jump("loc_39C3")

    label("loc_42FE")

    TalkEnd(0xFE)
    Return()

    # Function_20_37DD end

    def Function_21_4302(): pass

    label("Function_21_4302")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4327")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4327")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4342")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4342")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_435D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_435D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4378")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4378")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4393")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4393")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43AE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43C9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43E4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43FF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_441A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_441A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4435")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4435")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4450")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4450")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_446B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_446B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4486")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4486")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44A1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_44A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44BC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_44BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44D7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_44D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44F2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_44F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_450D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_450D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4528")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4528")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4543")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4543")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_455E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_455E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4579")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4579")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4594")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4594")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45AF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45CA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45E5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4600")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4600")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_461B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_461B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4636")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4636")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4651")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4651")

    Return()

    # Function_21_4302 end

    def Function_22_4652(): pass

    label("Function_22_4652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 3)), scpexpr(EXPR_END)), "loc_465C")
    Return()

    label("loc_465C")

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

    #A0064
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
        (1, "loc_4728"),
        (SWITCH_DEFAULT, "loc_4741"),
    )


    label("loc_4728")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -24310, 0, 47440, 180)
    EventEnd(0x5)
    Return()

    label("loc_4741")

    Battle("BattleInfo_5F8", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-24310, 1000, 47440, 0)
    OP_90(0x0, -24310, 0, 47440, 180)
    OP_90(0x1, -24310, 0, 47440, 180)
    OP_90(0x2, -24310, 0, 47440, 180)
    OP_90(0x3, -24310, 0, 47440, 180)
    OP_90(0x4, -24310, 0, 47440, 180)
    OP_90(0x5, -24310, 0, 47440, 180)
    OP_90(0x6, -24310, 0, 47440, 180)
    OP_90(0x7, -24310, 0, 47440, 180)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_4803"),
        (1, "loc_4808"),
        (SWITCH_DEFAULT, "loc_480B"),
    )


    label("loc_4803")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_4808")

    OP_B9(0x0)
    Return()

    label("loc_480B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x1F, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0065
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

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x73),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber('琥耀珠', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21D, 3)
    OP_29(0x99, 0x4, 0x2)
    OP_29(0x99, 0x4, 0x10)
    OP_29(0x99, 0x1, 0x0)
    OP_E2(0x2)
    ModifyEventFlags(0, 3, 0x80)
    EventEnd(0x5)
    Return()

    # Function_22_4652 end

    def Function_23_489E(): pass

    label("Function_23_489E")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0067
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(-58890, 1000, 38460, 1500)
    MoveCamera(45, 38, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(21000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0068
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B47")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4978")
    MiniGame(0x6, 0x13, 0xFFFF1E1A, 0x0, 0x88F4, 0x0, 0xFFFF1C26, 0xFFFFFC18, 0xA03C)
    Jump("loc_4B47")

    label("loc_4978")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MiniGame(0x6, 0x14, 0xFFFF1E1A, 0x0, 0x88F4, 0x0, 0xFFFF1C26, 0xFFFFFC18, 0xA03C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B47")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B47")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(-57530, 1000, 35490, 0)
    MoveCamera(42, 31, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17270, 0)
    LoadChrToIndex("apl/ch50160.itc", 0x1E)
    SetChrFlags(0x0, 0x2)
    SetChrChipByIndex(0x0, 0x1E)
    SetChrSubChip(0x0, 0x12)
    SetChrPos(0x0, -57830, 0, 35060, 0)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    #N0069
    NpcTalk(
        0x0,
        "罗伊德",
        (
            "#00011F哦、哦哦……\x01",
            "真是惊人的重量啊。\x02\x03",

            "#00003F而且还这么美丽……\x01",
            "这莫非是一种珍奇\x01",
            "的鱼类吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, -57830, 0, 35060, 0)
    SetChrPos(0x2, -57830, 0, 35060, 0)
    SetChrPos(0x3, -57830, 0, 35060, 0)
    SetChrPos(0x4, -57830, 0, 35060, 0)
    SetChrPos(0x5, -57830, 0, 35060, 0)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D7(0x1E)
    OP_37()
    SetScenarioFlags(0x18B, 5)

    label("loc_4B47")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_23_489E end

    def Function_24_4B4C(): pass

    label("Function_24_4B4C")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B7E")
    SetScenarioFlags(0x31, 2)

    label("loc_4B7E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4BC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_4BBE")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4BB3")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_4BB9")

    label("loc_4BB3")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_4BB9")

    Jump("loc_4BC4")

    label("loc_4BBE")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_4BC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4C35")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4C15"),
        (SWITCH_DEFAULT, "loc_4C26"),
    )


    label("loc_4C15")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4C30")

    label("loc_4C26")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C30")

    Jump("loc_4E66")

    label("loc_4C35")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4C65")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_4C65")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4C8F"),
        (1, "loc_4D93"),
        (2, "loc_4E24"),
        (SWITCH_DEFAULT, "loc_4E5C"),
    )


    label("loc_4C8F")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4CC0")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4CD0")

    label("loc_4CC0")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4CD0")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D26")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D26")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D49")
    Sound(461, 0, 100, 0)

    label("loc_4D49")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4D69")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_4D79")

    label("loc_4D69")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_4D79")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_4BC4")

    label("loc_4D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4E05")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_4DC8")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_4DE0")

    label("loc_4DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4DDB")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_4DE0")

    label("loc_4DDB")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_4DE0")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E1F")

    label("loc_4E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4E15")
    OP_AF(0xFB)
    Jump("loc_4E1F")

    label("loc_4E15")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E1F")

    Jump("loc_4E66")

    label("loc_4E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E3D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E57")

    label("loc_4E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4E4D")
    OP_AF(0xFB)
    Jump("loc_4E57")

    label("loc_4E4D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E57")

    Jump("loc_4E66")

    label("loc_4E5C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E66")

    Jump("loc_4BC4")

    label("loc_4E6B")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_24_4B4C end

    def Function_25_4E79(): pass

    label("Function_25_4E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_506A")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_500E")

    #C0071
    ChrTalk(
        0x105,
        (
            "#10309F嗯，要乘坐巴士\x01",
            "返回克洛斯贝尔市吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00006F都已经走到这里了，怎么可能坐巴士回去。\x02\x03",

            "#00000F路程大概只剩下一半了吧？\x01",
            "我们还是再加把劲，继续步行吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5006")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "随着剧情的进展，\x01",
            "各地的巴士车站\x01",
            "将会开放使用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "乘坐巴士可以便捷往来于各地，\x01",
            "届时请多加利用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 5)

    label("loc_5006")

    SetScenarioFlags(0x0, 2)
    Jump("loc_5067")

    label("loc_500E")


    #C0075
    ChrTalk(
        0x101,
        (
            "#00000F都已经走到这里了，\x01",
            "路程大概只剩下一半了吧？\x01",
            "我们还是再加把劲，继续往前走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5067")

    EventEnd(0x3)
    Return()

    label("loc_506A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50D9")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0077
    ChrTalk(
        0x101,
        (
            "#00001F已经发生了事故，\x01",
            "我们没时间在这里等巴士了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x3)
    Return()

    label("loc_50D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_510F")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0078
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

    label("loc_510F")

    Call(0, 13)
    Return()

    # Function_25_4E79 end

    def Function_26_5113(): pass

    label("Function_26_5113")

    SetMapObjFlags(0x3, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51CC")
    EventBegin(0x1)
    OP_E2(0x3)
    Fade(500)
    MoveCamera(45, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_0D()

    #C0079
    ChrTalk(
        0x101,
        (
            "#00001F这边就是警察学校了……\x02\x03",

            "前方自然也有国防军的士兵在看守。\x01",
            "在被发现之前，还是尽早离开吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -56320, -6000, -83050, 0)
    OP_E2(0x2)
    EventEnd(0x4)
    Jump("loc_5631")

    label("loc_51CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_558A")
    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -55720, -6000, -85510, 180)
    SetChrPos(0x103, -54770, -6000, -85100, 180)
    SetChrPos(0x104, -56880, -6000, -85190, 180)
    SetChrPos(0x105, -55010, -6000, -83820, 180)
    SetChrPos(0x106, -56250, -6000, -83870, 180)
    SetChrPos(0x107, -55490, -6000, -82560, 180)
    SetChrSubChip(0x107, 0x5)
    OP_68(-57100, -1680, -84150, 0)
    MoveCamera(135, 18, 0, 0)
    OP_6E(490, 0)
    SetCameraDistance(17500, 0)
    OP_68(-57100, -4080, -84150, 3000)
    OP_6F(0x79)

    #C0080
    ChrTalk(
        0x101,
        (
            "#00003F#5P这边是警察学校……\x02\x03",

            "#0001F大门紧紧地关着啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        (
            "#00203F#6P……在大门附近\x01",
            "可以感知到微弱的导力波。\x02\x03",

            "#00200F看起来，似乎新装设了\x01",
            "传感器呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00006F#5P嗯，因为我的逃脱，\x01",
            "警备力度又进一步强化了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x105,
        (
            "#10400F#6P嗯，看来我们还是不要\x01",
            "贸然接近为好。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    TurnDirection(0x104, 0x101, 500)

    #C0084
    ChrTalk(
        0x104,
        (
            "#00308F#12P对了，你之前好像说过，\x01",
            "在逃离拘留所的时候，得到了\x01",
            "加尔西亚那个大叔的帮助吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x107,
        (
            "#01200F#3C#6P可我赶到的时候，\x01",
            "只有罗伊德一个人。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00008F#5P嗯，为了掩护我逃脱，\x01",
            "他独自留下牵制国防军……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x106,
        "#10712F#6P那个『杀戮之熊』竟然……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        (
            "#00306F#12P你和那个大叔\x01",
            "也经历了不少事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00003F#5P……虽然很担心\x01",
            "他在那之后的情况如何……\x02\x03",

            "#00001F但如今还是专心考虑\x01",
            "接下来的行动吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 27)
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -56320, -6000, -83050, 0)
    SetScenarioFlags(0x1BC, 6)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_5631")

    label("loc_558A")

    EventBegin(0x1)
    OP_E2(0x3)
    Fade(500)
    MoveCamera(45, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_0D()

    #C0090
    ChrTalk(
        0x103,
        (
            "#00200F大门附近似乎装设了\x01",
            "传感器呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00003F虽然很在意加尔西亚的情况……\x01",
            "但还是不要贸然接近了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -56320, -6000, -83050, 0)
    OP_E2(0x2)
    EventEnd(0x4)

    label("loc_5631")

    ClearMapObjFlags(0x3, 0x1000)
    Return()

    # Function_26_5113 end

    def Function_27_5638(): pass

    label("Function_27_5638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57B6")
    OP_29(0xAF, 0x1, 0xF)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)
    Sleep(500)

    #C0092
    ChrTalk(
        0x101,
        (
            "#00008F#5P话说回来，我们已经到处转过一圈了，\x01",
            "但似乎没有一条路能走得通啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x104,
        (
            "#00303F#12P克洛斯贝尔市自不必说，\x01",
            "贝尔加德门和警察学校\x01",
            "也都不能去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x106,
        "#10706F#6P真是难办啊……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        (
            "#10400F#6P唔，难道就没有其它\x01",
            "的可去之处了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x107,
        (
            "#01200F#3C#6P不如去主路之外的\x01",
            "角落探查一番吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x103,
        (
            "#00203F#5P说的也是……\x01",
            "咱们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57B6")

    Return()

    # Function_27_5638 end

    def Function_28_57B7(): pass

    label("Function_28_57B7")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(-56090, -3600, -86800, 0)
    OP_6E(510, 0)
    MoveCamera(359, 24, 0, 0)
    SetCameraDistance(28520, 0)
    SetChrPos(0x101, -56000, -6000, -78000, 180)
    SetChrPos(0x102, -55200, -6000, -76800, 180)
    SetChrPos(0x109, -56850, -6000, -76650, 180)
    SetChrPos(0x105, -56100, -6000, -75650, 180)
    FadeToBright(1000, 0)
    OP_68(-56030, -3600, -90500, 3000)

    def lambda_589C():
        OP_9B(0x0, 0x101, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_589C)
    Sleep(0)

    def lambda_58B4():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_58B4)
    Sleep(0)

    def lambda_58CC():
        OP_9B(0x0, 0x109, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_58CC)
    Sleep(0)

    def lambda_58E4():
        OP_9B(0x0, 0x105, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_58E4)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0098
    ChrTalk(
        0x101,
        (
            "#00000F#5P嗯，看来已经\x01",
            "帮我们把门打开了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x105,
        "#10306F#5P哎呀呀，总算到了啊。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#00102F#11P前方就是\x01",
            "警察学校了吧？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-56250, -4550, -87530, 0)
    MoveCamera(135, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19650, 0)
    SetChrPos(0x101, -56450, -6000, -88250, 180)
    SetChrPos(0x102, -55350, -6000, -87250, 180)
    SetChrPos(0x109, -57000, -6000, -86650, 180)
    SetChrPos(0x105, -56000, -6000, -86000, 180)
    OP_0D()

    #C0101
    ChrTalk(
        0x101,
        (
            "#00004F#5P嗯，前面是一条\x01",
            "铺修过的林间道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x109,
        (
            "#10100F#6P沿着这条路前进，\x01",
            "很快就能到达警察学校的正门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        "#00100F#5P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x105,
        (
            "#10304F#6P呵，似乎没人来迎接呢，\x01",
            "那我们就继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)
    TurnDirection(0x101, 0x105, 500)
    Sleep(50)

    def lambda_5B77():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5B77)
    Sleep(100)

    def lambda_5B87():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5B87)
    Sleep(100)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    #C0105
    ChrTalk(
        0x101,
        (
            "#00006F#11P……不行，\x01",
            "还是很在意刚才那个男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x109,
        "#10106F#6P是啊，印象太强烈了……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        (
            "#00108F#5P但是，科长交付的任务\x01",
            "也不能置之不顾……\x02\x03",

            "#00101F那我们就兵分两路如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x105,
        (
            "#10303F#6P一组按照原计划前往警察学校，\x01",
            "另一组返回克洛斯贝尔市。\x02\x03",

            "#10300F这主意不错呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0109
    ChrTalk(
        0x101,
        (
            "#00003F#11P不，以我们目前的阵容来说，\x01",
            "分成两队有点草率。\x02\x03",

            "#00001F谨慎起见，\x01",
            "还是先与搜查一科联络一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x102,
        (
            "#00100F#5P原来如此，\x01",
            "这样也好。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(823, 0, 100, 0)
    Sleep(2700)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾玛的声音")

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里是克洛斯贝尔警察局，\x01",
            "搜查一科。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0112
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F艾玛警官，\x01",
            "之前多谢您的关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾玛的声音")

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "班宁斯搜查官。\x02\x03",

            "怎么了？\x01",
            "之前的任务有什么进展了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0114
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F不，有别的事情。\x02\x03",

            "#00001F是这样……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0115
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将遭遇到\x01",
            "独眼壮汉的事情做了说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾玛的声音")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……红发独眼的壮汉，\x01",
            "年龄在四十岁上下吗……\x02\x03",

            "不使用任何交通工具，\x01",
            "徒步行走在市外……\x02\x03",

            "明白了，\x01",
            "我们会多加关注的。\x02\x03",

            "你们就继续处理赛尔盖科长\x01",
            "交付的任务吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0117
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F好，那就拜托您了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(250)
    Sound(813, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0118
    ChrTalk(
        0x105,
        (
            "#10302F#6P呵呵，已经和一科的姐姐\x01",
            "联络过了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(150)

    #C0119
    ChrTalk(
        0x101,
        (
            "#00006F#11P嗯，这样总算是稍微安心了。\x02\x03",

            "#00000F那我们这就进入大门，继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        "#00100F#5P嗯，我们走吧。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x109,
        "#10100F#6P明白。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(19400, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, -56000, -6000, -86000, 180)
    SetScenarioFlags(0x127, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_28_57B7 end

    def Function_29_612B(): pass

    label("Function_29_612B")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    OP_68(-35500, 1000, 1000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -31450, 0, 1050, 270)
    SetChrPos(0x102, -30850, 0, 100, 270)
    SetChrPos(0x103, -29950, 0, 1850, 270)
    SetChrPos(0x104, -28850, 0, 1550, 270)
    SetChrPos(0x109, -29650, 0, 0, 270)
    SetChrPos(0x105, -28050, 0, 750, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(19500, 2500)

    def lambda_620C():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_620C)
    Sleep(20)

    def lambda_6224():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6224)
    Sleep(20)

    def lambda_623C():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_623C)
    Sleep(20)

    def lambda_6254():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6254)
    Sleep(20)

    def lambda_626C():
        OP_9B(0x0, 0x109, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_626C)
    Sleep(20)

    def lambda_6284():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6284)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    Sound(288, 0, 70, 0)
    Sound(876, 0, 50, 0)
    Sleep(200)
    Sound(880, 0, 70, 0)
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6376():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6376)
    Sleep(50)

    def lambda_6386():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6386)
    Sleep(50)

    def lambda_6396():
        OP_93(0x103, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6396)
    Sleep(50)

    def lambda_63A6():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_63A6)
    Sleep(50)

    def lambda_63B6():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_63B6)
    Sleep(50)

    def lambda_63C6():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_63C6)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0122
    ChrTalk(
        0x101,
        "#00007F#5P什么……！\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x109,
        "#10107F#11P这是……爆炸声吗！？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        "#00310F#11P并不是爆炸声吧！？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        "#00207F#5P是南边，快去看看！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(20500, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrPos(0x0, -35500, 0, 1000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    SetScenarioFlags(0x163, 4)
    OP_29(0xA8, 0x1, 0x7)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_29_612B end

    def Function_30_64C9(): pass

    label("Function_30_64C9")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    OP_68(-56000, -5200, -84500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, -56000, -6000, -77000, 180)
    SetChrPos(0x102, -56800, -6000, -75800, 180)
    SetChrPos(0x103, -55250, -6000, -76300, 180)
    SetChrPos(0x104, -55950, -6000, -75050, 180)
    SetChrPos(0x109, -55000, -6000, -74450, 180)
    SetChrPos(0x105, -56500, -6000, -73700, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_6598():
        OP_95(0xFE, -56000, -6000, -83000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6598)

    def lambda_65B2():
        OP_95(0xFE, -56800, -6000, -81800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_65B2)

    def lambda_65CC():
        OP_95(0xFE, -55250, -6000, -82300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_65CC)

    def lambda_65E6():
        OP_95(0xFE, -55950, -6000, -81050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_65E6)

    def lambda_6600():
        OP_95(0xFE, -55000, -6000, -80450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6600)

    def lambda_661A():
        OP_95(0xFE, -56500, -6000, -79700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_661A)
    FadeToBright(1000, 0)
    OP_68(-56000, -5200, -82500, 3000)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    SetChrPos(0x101, -56000, -6000, -79000, 180)
    SetChrPos(0x102, -56800, -6000, -77800, 180)
    SetChrPos(0x103, -55250, -6000, -78300, 180)
    SetChrPos(0x104, -55950, -6000, -77050, 180)
    SetChrPos(0x109, -55000, -6000, -76450, 180)
    SetChrPos(0x105, -56500, -6000, -75700, 180)

    def lambda_6759():
        OP_95(0xFE, -56000, -6000, -91000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6759)

    def lambda_6773():
        OP_95(0xFE, -56800, -6000, -89800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6773)

    def lambda_678D():
        OP_95(0xFE, -55250, -6000, -90300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_678D)

    def lambda_67A7():
        OP_95(0xFE, -55950, -6000, -89050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_67A7)

    def lambda_67C1():
        OP_95(0xFE, -55000, -6000, -88450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_67C1)

    def lambda_67DB():
        OP_95(0xFE, -56500, -6000, -87700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_67DB)
    OP_68(-56740, 500, -88290, 0)
    MoveCamera(163, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18760, 0)
    OP_68(-57070, -800, -87550, 4000)
    MoveCamera(163, 32, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(17690, 4000)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    #C0126
    ChrTalk(
        0x102,
        "#00107F#12P#N这、这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0127
    ChrTalk(
        0x101,
        (
            "#00010F#6P#N这扇大门可是用\x01",
            "特殊合金制造的啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0128
    ChrTalk(
        0x109,
        (
            "#10106F#6P#N简、简直无法相信……\x01",
            "一个魔兽竟能……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0129
    ChrTalk(
        0x104,
        (
            "#00311F#6P#N而且还让列车脱轨了……\x01",
            "究竟是什么样的怪物啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-58390, -800, -83470, 0)
    MoveCamera(162, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(11800, 0)
    OP_0D()
    Sleep(300)

    #C0130
    ChrTalk(
        0x105,
        (
            "#10303F#6P#N……总之，先追上去吧。\x01",
            "应该还没有走远。\x02\x03",

            "#10301F让它逃到森林深处可就麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_69D7():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_69D7)
    Sleep(50)

    def lambda_69E7():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_69E7)
    Sleep(50)

    def lambda_69F7():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_69F7)
    Sleep(50)

    def lambda_6A07():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6A07)
    Sleep(50)

    def lambda_6A17():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6A17)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    #C0131
    ChrTalk(
        0x101,
        (
            "#00001F#11P嗯，没错……（从刚才开始，\x01",
            "瓦吉的神色好像就有些不正常……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -56000, -6000, -84500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x163, 5)
    OP_29(0xA8, 0x1, 0x8)
    ModifyEventFlags(0, 2, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_30_64C9 end

    def Function_31_6AC5(): pass

    label("Function_31_6AC5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch03154.itc", 0x1E)
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(950)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -61160, 0, 28890, 10)
    SetChrPos(0x106, -59710, 0, 27350, 10)
    SetChrPos(0x103, -60010, 0, 28310, 10)
    SetChrPos(0x104, -60900, 0, 27820, 10)
    SetChrPos(0x107, -62090, 0, 27860, 10)
    SetChrPos(0x105, -60370, 0, 30240, 10)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x107, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrChipByIndex(0x105, 0x1E)
    SetChrSubChip(0x105, 0x0)
    BeginChrThread(0x105, 0, 0, 38)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x29, 0xE)
    OP_49()
    SetChrPos(0xE, -60450, 18000, 28100, 0)
    OP_D5(0xE, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x29, 0x4)
    OP_74(0x29, 0x1E)
    OP_71(0x29, 0x1, 0x78, 0x0, 0x20)
    OP_75(0x29, 0x1, 0x0)
    ClearChrFlags(0xF, 0x80)
    OP_78(0x2A, 0xF)
    OP_49()
    SetChrPos(0xF, -60450, 18000, 28100, 0)
    OP_D5(0xF, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x2A, 0x4)
    OP_74(0x2A, 0x1E)
    OP_71(0x2A, 0x65, 0xA0, 0x0, 0x20)
    SetMapObjFlags(0x6, 0x4)
    OP_68(-60450, 15000, 28100, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(36500, 0)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_68(-60450, 0, 28100, 10000)
    MoveCamera(15, 20, 0, 10000)
    BeginChrThread(0xE, 3, 0, 32)
    BeginChrThread(0xF, 3, 0, 33)
    OP_0D()
    StopSound(132, 1000, 100)
    Sleep(4500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xE, 0x3)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0xF, 0x1)
    Sleep(1000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x105, 0x8)
    OP_68(-60250, 5000, 30900, 0)
    MoveCamera(60, 40, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(27000, 0)
    FadeToBright(1000, 0)
    OP_68(-60250, 1000, 30900, 6000)
    MoveCamera(45, 36, 0, 6000)
    SetCameraDistance(20000, 6000)
    BeginChrThread(0x105, 3, 0, 39)
    BeginChrThread(0xE, 3, 0, 34)
    BeginChrThread(0xF, 3, 0, 35)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x105, 3)
    SetMapObjFlags(0x29, 0x4)
    SetChrFlags(0xE, 0x80)
    SetMapObjFlags(0x2A, 0x4)
    SetChrFlags(0xF, 0x80)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x101, -52550, 0, 19530, 135)
    SetChrPos(0x106, -53540, 0, 20610, 135)
    SetChrPos(0x103, -54530, 0, 19160, 135)
    SetChrPos(0x104, -55090, 0, 20060, 135)
    SetChrPos(0x107, -55500, 0, 21740, 135)
    SetChrPos(0x105, -56410, 0, 20640, 135)
    OP_68(-50660, 1000, 16690, 0)
    MoveCamera(90, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13500, 3000)

    def lambda_6E1D():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6E1D)
    Sleep(50)

    def lambda_6E35():
        OP_9B(0x0, 0x106, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6E35)
    Sleep(50)

    def lambda_6E4D():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6E4D)
    Sleep(50)

    def lambda_6E65():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6E65)
    Sleep(50)

    def lambda_6E7D():
        OP_9B(0x0, 0x107, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_6E7D)
    Sleep(50)

    def lambda_6E95():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6E95)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()

    #C0132
    ChrTalk(
        0x104,
        (
            "#00301F#6P向西走的话，很快就能\x01",
            "到达贝尔加德门了吧……\x02\x03",

            "#00306F索妮亚司令应该在那里，\x01",
            "实在是没勇气过去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        "#00206F#6P……的确。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x105,
        (
            "#10403F#6P总之，现在也只能在\x01",
            "可行进范围内探索了。\x02\x03",

            "#10401F道路上有国防军的装甲车通过时，\x01",
            "我们还得注意躲藏一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x106,
        "#10703F#6P说的对……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00008F#6P（索妮亚司令吗……）\x02\x03",

            "#00001F（……要是能想办法\x01",
            "  接触到她就好了……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x2B, 0x4)
    SetMapObjFlags(0x2C, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, -48700, 0, 15700, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 0)
    OP_29(0xAF, 0x1, 0xE)
    OP_24(0x84)
    OP_24(0x1F1)
    OP_24(0x3B6)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_31_6AC5 end

    def Function_32_708E(): pass

    label("Function_32_708E")

    BeginChrThread(0xFE, 0, 0, 36)
    OP_96(0xFE, 0xFFFF13DE, 0xBB8, 0x6DC4, 0x7D0, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_32_708E end

    def Function_33_70AD(): pass

    label("Function_33_70AD")


    def lambda_70B2():
        OP_96(0xFE, 0xFFFF13DE, 0xBB8, 0x6DC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_70B2)
    Sleep(2000)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_74(0x2A, 0x1E)
    OP_71(0x2A, 0x0, 0x32, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 1000, 40)
    Sleep(1000)
    OP_75(0x29, 0x2, 0x0)
    OP_79(0x2A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_33_70AD end

    def Function_34_710D(): pass

    label("Function_34_710D")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_75(0x29, 0x2, 0x0)
    SetChrPos(0xFE, -60450, 6000, 28100, 0)
    OP_96(0xFE, 0xFFFF13DE, 0x4650, 0x6DC4, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_34_710D end

    def Function_35_7144(): pass

    label("Function_35_7144")

    SetChrPos(0xFE, -60450, 6000, 28100, 0)

    def lambda_715A():
        OP_96(0xFE, 0xFFFF13DE, 0x4650, 0x6DC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_715A)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_74(0x2A, 0x1E)
    OP_71(0x2A, 0x33, 0x64, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 1000, 40)
    OP_75(0x29, 0x1, 0x0)
    OP_79(0x2A)
    OP_71(0x2A, 0x65, 0xA0, 0x0, 0x20)
    StopSound(497, 4000, 90)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_35_7144 end

    def Function_36_71C4(): pass

    label("Function_36_71C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_71E8")
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_36_71C4")

    label("loc_71E8")

    Return()

    # Function_36_71C4 end

    def Function_37_71E9(): pass

    label("Function_37_71E9")

    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x28, 0x28, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x1E, 0x1E, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x14, 0x14, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0xA, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Return()

    # Function_37_71E9 end

    def Function_38_724E(): pass

    label("Function_38_724E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7268")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_38_724E")

    label("loc_7268")

    Return()

    # Function_38_724E end

    def Function_39_7269(): pass

    label("Function_39_7269")

    Sleep(1500)
    ClearMapObjFlags(0x2B, 0x4)
    SetMapObjFrame(0x2B, "Null_fream", 0x2, "start")
    Sleep(1500)
    EndChrThread(0x105, 0x0)
    Sound(935, 0, 60, 0)
    SetChrSubChip(0x105, 0x3)
    Sleep(100)
    SetChrSubChip(0x105, 0x4)
    ClearMapObjFlags(0x2C, 0x4)
    SetMapObjFrame(0x2C, "Null_fream", 0x2, "start")
    Sleep(2000)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Return()

    # Function_39_7269 end

    def Function_40_72C4(): pass

    label("Function_40_72C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xC, 0x80)
    OP_78(0x5, 0xC)
    OP_49()
    SetChrPos(0xC, -85890, 2000, 73990, 90)
    OP_D5(0xC, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0xD, 0x80)
    ClearMapObjFlags(0x28, 0x4)
    OP_78(0x28, 0xD)
    SetMapObjFrame(0x28, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xD, -85890, 2000, 73990, 90)
    OP_D5(0xD, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x28, 0x1000)
    OP_74(0x28, 0x1E)
    OP_71(0x28, 0xB5, 0xF0, 0x1, 0x20)
    LoadEffect(0x6, "event\\eva04_00.eff")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x103, 0x80)
    OP_E2(0x3)
    OP_68(-68470, 2600, 62700, 0)
    MoveCamera(82, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(28350, 0)
    OP_68(-66340, 2600, 57390, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(457, 0, 100, 0)
    Sound(493, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 43)
    Sleep(2000)
    BeginChrThread(0xC, 1, 0, 42)
    Sleep(1000)
    Sound(494, 0, 100, 0)
    Sleep(2000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    OP_68(-29120, 2100, 39710, 0)
    MoveCamera(32, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(33680, 0)
    SetChrPos(0xC, -43110, 0, 54200, 90)
    SetChrPos(0xD, -43110, 0, 54200, 0)
    SetCameraDistance(35680, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(486, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 45)
    Sleep(1500)
    BeginChrThread(0xC, 1, 0, 44)
    Sound(493, 0, 100, 0)

    #N0137
    NpcTalk(
        0xD,
        "塞克斯",
        "#6A#40W这些家伙要干什么……！？\x02",
    )
    #Auto

    Sleep(1000)
    OP_68(-48380, 2100, 2970, 4000)
    MoveCamera(32, 26, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(30590, 4000)
    Sound(458, 0, 100, 0)

    #N0138
    NpcTalk(
        0xD,
        "尤利",
        "#6A#40W哈哈，吓吓他们！\x02",
    )
    #Auto

    Sleep(1500)
    Sound(486, 0, 100, 0)
    Sleep(2500)
    Sound(487, 0, 100, 0)
    WaitChrThread(0xD, 1)
    BeginChrThread(0xD, 3, 0, 41)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(500)
    WaitChrThread(0xC, 1)
    OP_71(0x5, 0xB5, 0xB5, 0x0, 0x0)
    OP_71(0x28, 0xB5, 0xB5, 0x0, 0x0)
    FadeToDark(300, 0, 100)

    #N0139
    NpcTalk(
        0xC,
        "罗伊德",
        "#00010F（想故意撞车吗……！！）\x02",
    )

    CloseMessageWindow()
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K紧急指挥\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "急刹车\x01",        # 0
            "绕行回避\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77BF")
    OP_2C(0x8B, 0x1)
    SetScenarioFlags(0x178, 2)

    #N0141
    NpcTalk(
        0xC,
        "罗伊德",
        "#00007F诺艾尔，快刹车！\x02",
    )

    CloseMessageWindow()

    #N0142
    NpcTalk(
        0xC,
        "诺艾尔",
        "#10107F是！\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_0D()
    Sound(487, 0, 100, 0)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    OP_71(0x28, 0xB5, 0xF0, 0x1, 0x20)
    OP_68(-41710, 600, 4300, 2000)
    BeginChrThread(0xC, 1, 0, 46)
    WaitChrThread(0xC, 1)
    Sound(494, 0, 100, 0)
    Sound(493, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 48)
    OP_0D()
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)

    #N0143
    NpcTalk(
        0xD,
        "瑞吉",
        "#8A#30W……什么！\x02",
    )
    #Auto

    Sleep(1200)

    #N0144
    NpcTalk(
        0xC,
        "艾莉",
        "#00105F啊啊……！\x02",
    )

    CloseMessageWindow()

    #N0145
    NpcTalk(
        0xC,
        "兰迪",
        (
            "#00303F啧……\x01",
            "这些家伙竟敢如此乱来。\x02\x03",

            "#00300F只被甩开了这点距离，\x01",
            "应该很快就能赶上吧？\x02",
        )
    )

    CloseMessageWindow()

    #N0146
    NpcTalk(
        0xC,
        "罗伊德",
        (
            "#00000F嗯！\x01",
            "诺艾尔，\x01",
            "继续追击！\x02",
        )
    )

    CloseMessageWindow()

    #N0147
    NpcTalk(
        0xC,
        "诺艾尔",
        "#10101F明白！\x02",
    )

    CloseMessageWindow()
    Sound(494, 0, 100, 0)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    BeginChrThread(0xC, 1, 0, 48)
    OP_29(0x8B, 0x1, 0x2)
    Sleep(3000)
    Jump("loc_798B")

    label("loc_77BF")


    #N0148
    NpcTalk(
        0xC,
        "罗伊德",
        "#00007F暂且绕行吧！\x02",
    )

    CloseMessageWindow()

    #N0149
    NpcTalk(
        0xC,
        "诺艾尔",
        "#10105F是、是的！\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_0D()
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    OP_68(-53830, 2100, -2640, 2000)
    Sound(494, 0, 100, 0)
    Sound(493, 0, 100, 0)
    BeginChrThread(0xC, 1, 0, 47)
    OP_71(0x28, 0xB5, 0xF0, 0x1, 0x20)
    BeginChrThread(0xD, 1, 0, 48)

    #N0150
    NpcTalk(
        0xD,
        "塞克斯",
        "#8A#30W拜拜啦！\x02",
    )
    #Auto

    Sleep(1200)
    Sound(492, 0, 100, 0)
    WaitChrThread(0xC, 1)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)

    #N0151
    NpcTalk(
        0xC,
        "艾莉",
        "#00105F啊啊……！\x02",
    )

    CloseMessageWindow()

    #N0152
    NpcTalk(
        0xC,
        "兰迪",
        (
            "#00303F啧……\x01",
            "这些家伙竟敢如此乱来。\x02\x03",

            "#00308F其实只要\x01",
            "踩一下刹车\x01",
            "就好了啊……\x02",
        )
    )

    CloseMessageWindow()

    #N0153
    NpcTalk(
        0xC,
        "罗伊德",
        (
            "#00006F（选择绕行，\x01",
            "  是我判断失误啊……）\x02\x03",

            "#00001F抱歉，诺艾尔！\x01",
            "麻烦你再次追击吧！\x02",
        )
    )

    CloseMessageWindow()

    #N0154
    NpcTalk(
        0xC,
        "诺艾尔",
        "#10101F明白！\x02",
    )

    CloseMessageWindow()
    OP_68(-48380, 2100, 2970, 2000)
    BeginChrThread(0xC, 1, 0, 49)
    OP_29(0x8B, 0x1, 0x3)
    Sleep(4000)

    label("loc_798B")

    SetScenarioFlags(0x22, 2)
    NewScene("r1020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_72C4 end

    def Function_41_7998(): pass

    label("Function_41_7998")

    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -45630, 0, 13920, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -47650, 0, 1320, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_41_7998 end

    def Function_42_7A0A(): pass

    label("Function_42_7A0A")

    OP_9F(0x0, 0xC)
    OP_9F(0x1, -85890, 2000, 73990)
    OP_9F(0x1, -65760, 2000, 55290)
    OP_9F(0x1, -54460, 2000, 54530)
    OP_9F(0x1, -45720, 0, 54180)
    OP_9F(0x1, -34680, 0, 52700)
    OP_9F(0x1, -28120, 0, 46140)
    OP_9F(0x2, 0xC, 12000, 0x6)
    Return()

    # Function_42_7A0A end

    def Function_43_7A6C(): pass

    label("Function_43_7A6C")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, -85890, 2000, 73990)
    OP_9F(0x1, -65760, 2000, 55290)
    OP_9F(0x1, -54460, 2000, 54530)
    OP_9F(0x1, -45720, 0, 54180)
    OP_9F(0x1, -34680, 0, 52700)
    OP_9F(0x1, -28120, 0, 46140)
    OP_9F(0x2, 0xD, 11000, 0x6)
    Return()

    # Function_43_7A6C end

    def Function_44_7ACE(): pass

    label("Function_44_7ACE")

    OP_9F(0x0, 0xC)
    OP_9F(0x1, -43110, 0, 54200)
    OP_9F(0x1, -32830, 0, 51030)
    OP_9F(0x1, -24400, 0, 40770)
    OP_9F(0x1, -27180, 0, 30110)
    OP_9F(0x1, -37110, 0, 22440)
    OP_9F(0x1, -45630, 0, 13920)
    OP_9F(0x1, -46520, 0, 9080)
    OP_9F(0x2, 0xC, 12000, 0x6)
    Return()

    # Function_44_7ACE end

    def Function_45_7B3E(): pass

    label("Function_45_7B3E")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, -43110, 0, 54200)
    OP_9F(0x1, -32830, 0, 51030)
    OP_9F(0x1, -24400, 0, 40770)
    OP_9F(0x1, -27180, 0, 30110)
    OP_9F(0x1, -37110, 0, 22440)
    OP_9F(0x1, -45630, 0, 13920)
    OP_9F(0x2, 0xD, 11000, 0x6)
    OP_9F(0x0, 0xD)
    OP_9F(0x1, -47650, 0, 1320)
    OP_9F(0x1, -46440, 0, 1320)
    OP_9F(0x2, 0xD, 15000, 0x6)
    OP_9B(0x1, 0xD, 0x5A, 0x3E8, 0x2710, 0x0)
    Return()

    # Function_45_7B3E end

    def Function_46_7BD8(): pass

    label("Function_46_7BD8")

    OP_9F(0x0, 0xC)
    OP_9F(0x1, -46520, 0, 9080)
    OP_9F(0x1, -46890, 0, 7430)
    OP_9F(0x1, -46230, 0, 5680)
    OP_9F(0x2, 0xC, 12000, 0x6)
    Return()

    # Function_46_7BD8 end

    def Function_47_7C10(): pass

    label("Function_47_7C10")

    OP_9F(0x0, 0xC)
    OP_9F(0x1, -46520, 0, 9080)
    OP_9F(0x1, -49690, 0, 3690)
    OP_9F(0x1, -52720, 0, 250)
    OP_9F(0x1, -56430, 0, -3730)
    OP_9F(0x2, 0xC, 15000, 0x6)
    Return()

    # Function_47_7C10 end

    def Function_48_7C56(): pass

    label("Function_48_7C56")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -41760, 0, 1800)
    OP_9F(0x1, -26570, 0, 2310)
    OP_9F(0x1, -20250, 0, 7670)
    OP_9F(0x2, 0xFE, 12000, 0x6)
    Return()

    # Function_48_7C56 end

    def Function_49_7C8E(): pass

    label("Function_49_7C8E")

    Sound(493, 0, 100, 0)
    OP_9B(0x1, 0xC, 0xB4, 0x2710, 0x2710, 0x0)
    OP_9E(0xFE, 0xFFFF277A, 0x1856, 0xFFFFC568, 0x2710, 0x4)
    OP_9B(0x1, 0xC, 0xB4, 0x7D0, 0x2710, 0x0)
    Sleep(300)
    Sound(494, 0, 100, 0)
    OP_9F(0x0, 0xC)
    OP_9F(0x1, -41760, 0, 1800)
    OP_9F(0x1, -26570, 0, 2310)
    OP_9F(0x1, -20250, 0, 7670)
    OP_9F(0x2, 0xC, 12000, 0x6)
    Return()

    # Function_49_7C8E end

    def Function_50_7D08(): pass

    label("Function_50_7D08")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0155
    ChrTalk(
        0xA,
        (
            "没想到我竟然会输……\x01",
            "你小子，干得不错嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xA,
        (
            "既然如此，那就收下击败我\x01",
            "『银螭』的证明吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0157
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('银螭奖牌', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0158
    ChrTalk(
        0x101,
        "#00012F谢、谢谢您。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        (
            "今后你就是本俱乐部认可的\x01",
            "『银螭克星』啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xA,
        (
            "虽说这称号的确是有点土气，\x01",
            "哈哈，不过你就多包涵吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        "#00006F哪、哪里……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C0, 3)
    SetChrPos(0xA, -57240, 0, 32830, 90)
    OP_66(0x6, 0x1)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, -59650, 0, 32659, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_50_7D08 end

    def Function_51_7E94(): pass

    label("Function_51_7E94")


    #C0162
    ChrTalk(
        0xA,
        "这样啊。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "嗯，你这次也许只是\x01",
            "运气欠佳，\x01",
            "以后可以随时来挑战哦。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_51_7E94 end

    def Function_52_7EDD(): pass

    label("Function_52_7EDD")


    #C0164
    ChrTalk(
        0xA,
        "弃权吗……算啦，这也随你。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        "那就下回再战吧。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_52_7EDD end

    def Function_53_7F14(): pass

    label("Function_53_7F14")


    #C0166
    ChrTalk(
        0xA,
        (
            "哈哈，竟然能和我平分秋色，\x01",
            "有点本事嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "也罢，下次再比试时，\x01",
            "我们一定要分个高低哦。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_53_7F14 end

    def Function_54_7F73(): pass

    label("Function_54_7F73")

    EventBegin(0x1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FD3")

    #C0168
    ChrTalk(
        0x101,
        (
            "#00000F这是通向贝尔加德门的方向。\x02\x03",

            "我们还得去警察学校，\x01",
            "就不要绕远路了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_801D")

    #C0169
    ChrTalk(
        0x101,
        (
            "#00001F声音并不是从这个方向传来的，\x01",
            "我们向南边前进吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_801D")

    OP_5A()
    SetChrPos(0x0, -37940, 0, 20690, 225)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_54_7F73 end

    def Function_55_8034(): pass

    label("Function_55_8034")

    EventBegin(0x1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8082")

    #C0170
    ChrTalk(
        0x101,
        (
            "#00001F声音并不是从这个方向传来的，\x01",
            "我们向南边前进吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8082")

    OP_5A()
    SetChrPos(0x0, -53410, 0, 18420, 143)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_55_8034 end

    def Function_56_8099(): pass

    label("Function_56_8099")

    EventBegin(0x1)
    OP_E2(0x3)

    #C0171
    ChrTalk(
        0x101,
        (
            "#00001F这是通向贝尔加德门的方向……\x02\x03",

            "继续前进是很危险的，\x01",
            "还是离开这里吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -70920, 2000, 59620, 135)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_56_8099 end

    def Function_57_8104(): pass

    label("Function_57_8104")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0172
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "      Ｃ．Ｐ．Ｓ．\x01",
            "Crossbell Police School\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_57_8104 end

    def Function_58_816A(): pass

    label("Function_58_816A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东·克洛斯贝尔市　　　　１３７赛尔矩\x01",
            "北·贝尔加德门　　　  　　６１赛尔矩\x01",
            "南·克洛斯贝尔警察学校　　３１赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_58_816A end

    SaveToFile()

Try(main)
