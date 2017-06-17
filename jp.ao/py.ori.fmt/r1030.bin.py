from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "警備隊員",               # 1
        "警備隊員",               # 2
        "銀鯱トリトン",           # 3
        "バス",                   # 4
        "特務支援車",             # 5
        "暴走車",                 # 6
        "メルカバ",               # 7
        "メルカバ",               # 8
        "カエンギーヌー",         # 9
        "カエンギーヌー",         # 10
        "ガンテ",                 # 11
        "ガンテ",                 # 12
        "br1000",                 # 13
        "br1000",                 # 14
        "br1000",                 # 15
        "br1000",                 # 16
        "br1000",                 # 17
        "br1000",                 # 18
        "br1000",                 # 19
        "br1000",                 # 20
        "br1000",                 # 21
        "クロスベル市方面",       # 22
        "ベルガード門方面",       # 23
        "警察学校方面",           # 24
    ))

    ATBonus("ATBonus_868", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_888", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_8883", 0,   0,   7,   0,   2,   2,   2)
    Sepith("Sepith_888B", 2,   2,   0,   0,   3,   3,   3)
    Sepith("Sepith_8863", 2,   1,   5,   0,   0,   3,   2)
    Sepith("Sepith_886B", 0,   3,   0,   5,   2,   3,   0)
    Sepith("Sepith_889B", 2,   1,   4,   1,   0,   2,   2)
    Sepith("Sepith_88AB", 11,  7,   4,   3,   6,   12,  7)

    MonsterBattlePostion("MonsterBattlePostion_8C8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_8CC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8DC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_928", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_92C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_930", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_934", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_938", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_93C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_940", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_944", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_8A8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_8AC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8BC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C4", 2, 13, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_A10", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_8883", 30, 40, 20, 10,
        (
            ("ms71300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71300.dat", "ms71300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71300.dat", "ms70400.dat", "ms71300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71300.dat", "ms71300.dat", "ms70400.dat", "ms66900.dat", 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
        )
    )

    BattleInfo(
        "BattleInfo_BA0", 0x0000, 50, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_888B", 30, 30, 20, 20,
        (
            ("ms64200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms64200.dat", "ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms64200.dat", "ms66900.dat", "ms64200.dat", "ms66900.dat", 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
        )
    )

    BattleInfo(
        "BattleInfo_C68", 0x0000, 50, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_8863", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
        )
    )

    BattleInfo(
        "BattleInfo_948", 0x0000, 50, 6, 60, 8, 1, 40, 0, "br1000", "Sepith_886B", 30, 40, 20, 10,
        (
            ("ms70300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms70300.dat", "ms70300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms70300.dat", "ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
        )
    )

    BattleInfo(
        "BattleInfo_AD8", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_889B", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71900.dat", "ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
        )
    )

    BattleInfo(
        "BattleInfo_D30", 0x0000, 84, 6, 45, 6, 1, 30, 0, "br1000", "Sepith_88AB", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E54", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72400.dat", "ms72400.dat", "ms72400.dat", "ms72400.dat", "ms72400.dat", "ms72400.dat", 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7451", "ed7453", "ATBonus_888"),
            (),
            (),
            (),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_DCC", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7453", "ed7453", "ATBonus_868"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E10", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7453", "ed7453", "ATBonus_868"),
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

    DeclMonster(-17880,  910,     0,       0x1010000,    "BattleInfo_A10", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-44410,  -7750,   0,       0x1010000,    "BattleInfo_BA0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-16440,  44520,   0,       0x1010000,    "BattleInfo_C68", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-39150,  60950,   0,       0x1010000,    "BattleInfo_948", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-74290,  -25740,  -2000,   0x1010000,    "BattleInfo_C68", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-34710,  -42590,  -4000,   0x1010000,    "BattleInfo_A10", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-62760,  -62500,  -6000,   0x1010000,    "BattleInfo_AD8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-19130,  6440,    0,       0x1010000,    "BattleInfo_D30", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-59570,  -9280,   0,       0x1010000,    "BattleInfo_D30", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-56370,  -76140,  -6000,   0x1010000,    "BattleInfo_D30", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-27490,  31330,   0,       0x1010000,    "BattleInfo_D30", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-23820,  53310,   0,       0x18500B4,    "BattleInfo_E54", 0,   28,  0xFFFF, 12, 13)

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

    PlaceName(29.0, 0.0, 19.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(-95.0, 0.0, 84.0, 0x0000, 0x0000, "ベルガード門方面")
    PlaceName(-55.0, 0.0, -114.0, 0x0000, 0x0000, "警察学校方面")
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
        "Function_0_102C",         # 00, 0
        "Function_1_10E4",         # 01, 1
        "Function_2_1103",         # 02, 2
        "Function_3_1122",         # 03, 3
        "Function_4_118E",         # 04, 4
        "Function_5_17C0",         # 05, 5
        "Function_6_290B",         # 06, 6
        "Function_7_2A5C",         # 07, 7
        "Function_8_2BAD",         # 08, 8
        "Function_9_2CFE",         # 09, 9
        "Function_10_305C",        # 0A, 10
        "Function_11_33BA",        # 0B, 11
        "Function_12_33DD",        # 0C, 12
        "Function_13_33E1",        # 0D, 13
        "Function_14_349B",        # 0E, 14
        "Function_15_35CE",        # 0F, 15
        "Function_16_3701",        # 10, 16
        "Function_17_3752",        # 11, 17
        "Function_18_37E6",        # 12, 18
        "Function_19_384D",        # 13, 19
        "Function_20_38CD",        # 14, 20
        "Function_21_4538",        # 15, 21
        "Function_22_4888",        # 16, 22
        "Function_23_4AF4",        # 17, 23
        "Function_24_4DA8",        # 18, 24
        "Function_25_50EB",        # 19, 25
        "Function_26_53AD",        # 1A, 26
        "Function_27_5950",        # 1B, 27
        "Function_28_5B0B",        # 1C, 28
        "Function_29_657D",        # 1D, 29
        "Function_30_692D",        # 1E, 30
        "Function_31_6F4F",        # 1F, 31
        "Function_32_7546",        # 20, 32
        "Function_33_7565",        # 21, 33
        "Function_34_75C5",        # 22, 34
        "Function_35_75FC",        # 23, 35
        "Function_36_767C",        # 24, 36
        "Function_37_76A1",        # 25, 37
        "Function_38_7706",        # 26, 38
        "Function_39_7721",        # 27, 39
        "Function_40_777C",        # 28, 40
        "Function_41_7EFE",        # 29, 41
        "Function_42_7F70",        # 2A, 42
        "Function_43_7FD2",        # 2B, 43
        "Function_44_8034",        # 2C, 44
        "Function_45_80A4",        # 2D, 45
        "Function_46_813E",        # 2E, 46
        "Function_47_8176",        # 2F, 47
        "Function_48_81BC",        # 30, 48
        "Function_49_81F4",        # 31, 49
        "Function_50_826E",        # 32, 50
        "Function_51_8450",        # 33, 51
        "Function_52_84BD",        # 34, 52
        "Function_53_84FA",        # 35, 53
        "Function_54_856B",        # 36, 54
        "Function_55_863A",        # 37, 55
        "Function_56_86A3",        # 38, 56
        "Function_57_871C",        # 39, 57
        "Function_58_8782",        # 3A, 58
    ))


    def Function_0_102C(): pass

    label("Function_0_102C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_106C"),
        (1, "loc_1078"),
        (2, "loc_1084"),
        (3, "loc_1090"),
        (4, "loc_109C"),
        (5, "loc_10A8"),
        (6, "loc_10B4"),
        (SWITCH_DEFAULT, "loc_10C0"),
    )


    label("loc_106C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_1078")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_1084")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_1090")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_109C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_10A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_10B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_10C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_10CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_10E3")

    Return()

    # Function_0_102C end

    def Function_1_10E4(): pass

    label("Function_1_10E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1102")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_10E4")

    label("loc_1102")

    Return()

    # Function_1_10E4 end

    def Function_2_1103(): pass

    label("Function_2_1103")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1121")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_1103")

    label("loc_1121")

    Return()

    # Function_2_1103 end

    def Function_3_1122(): pass

    label("Function_3_1122")

    SetMapObjFlags(0x29, 0x2000000)
    SetMapObjFlags(0x2A, 0x2000000)
    SetMapObjFlags(0x28, 0x2000000)
    SetMapObjFlags(0x24, 0x2000000)
    SetMapObjFlags(0x4, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_114F")
    ClearMapObjFlags(0x28, 0x2000000)

    label("loc_114F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1169")
    ClearMapObjFlags(0x29, 0x2000000)
    ClearMapObjFlags(0x2A, 0x2000000)

    label("loc_1169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_117D")
    ClearMapObjFlags(0x24, 0x2000000)

    label("loc_117D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118D")
    ClearMapObjFlags(0x4, 0x2000000)

    label("loc_118D")

    Return()

    # Function_3_1122 end

    def Function_4_118E(): pass

    label("Function_4_118E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_END)), "loc_11A8")
    SetChrPos(0xA, -57240, 0, 32830, 95)

    label("loc_11A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11BB")
    SetChrFlags(0xA, 0x80)
    Jump("loc_126E")

    label("loc_11BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_11D2")
    SetChrFlags(0xA, 0x80)

    label("loc_11D2")

    Jump("loc_126E")

    label("loc_11D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11E5")
    Jump("loc_126E")

    label("loc_11E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1207")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    Jump("loc_126E")

    label("loc_1207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_1215")
    Jump("loc_126E")

    label("loc_1215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1223")
    Jump("loc_126E")

    label("loc_1223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1231")
    Jump("loc_126E")

    label("loc_1231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_123F")
    Jump("loc_126E")

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1252")
    SetChrFlags(0xA, 0x10)
    Jump("loc_126E")

    label("loc_1252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1260")
    Jump("loc_126E")

    label("loc_1260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_126E")
    SetChrFlags(0xA, 0x80)

    label("loc_126E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_127D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 40)

    label("loc_127D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_128E")
    Event(0, 31)

    label("loc_128E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1732")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131B")
    SetScenarioFlags(0x38, 0)

    label("loc_131B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1331")
    SetScenarioFlags(0x38, 1)

    label("loc_1331")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1347")
    SetScenarioFlags(0x38, 2)

    label("loc_1347")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135D")
    SetScenarioFlags(0x38, 3)

    label("loc_135D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    SetScenarioFlags(0x38, 4)

    label("loc_1373")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1389")
    SetScenarioFlags(0x38, 5)

    label("loc_1389")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139F")
    SetScenarioFlags(0x38, 6)

    label("loc_139F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B5")
    SetScenarioFlags(0x38, 7)

    label("loc_13B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CB")
    SetScenarioFlags(0x39, 0)

    label("loc_13CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E1")
    SetScenarioFlags(0x39, 1)

    label("loc_13E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F7")
    SetScenarioFlags(0x39, 2)

    label("loc_13F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140D")
    SetScenarioFlags(0x39, 3)

    label("loc_140D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1423")
    SetScenarioFlags(0x39, 4)

    label("loc_1423")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1439")
    SetScenarioFlags(0x39, 5)

    label("loc_1439")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144F")
    SetScenarioFlags(0x39, 6)

    label("loc_144F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1465")
    SetScenarioFlags(0x39, 7)

    label("loc_1465")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147B")
    SetScenarioFlags(0x3A, 0)

    label("loc_147B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1491")
    SetScenarioFlags(0x3A, 1)

    label("loc_1491")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A7")
    SetScenarioFlags(0x3A, 2)

    label("loc_14A7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BD")
    SetScenarioFlags(0x3A, 3)

    label("loc_14BD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D3")
    SetScenarioFlags(0x3A, 4)

    label("loc_14D3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E9")
    SetScenarioFlags(0x3A, 5)

    label("loc_14E9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FF")
    SetScenarioFlags(0x3A, 6)

    label("loc_14FF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1515")
    SetScenarioFlags(0x3A, 7)

    label("loc_1515")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152B")
    SetScenarioFlags(0x3B, 0)

    label("loc_152B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1541")
    SetScenarioFlags(0x3B, 1)

    label("loc_1541")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1557")
    SetScenarioFlags(0x3B, 2)

    label("loc_1557")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156D")
    SetScenarioFlags(0x3B, 3)

    label("loc_156D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1583")
    SetScenarioFlags(0x3B, 4)

    label("loc_1583")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1599")
    SetScenarioFlags(0x3B, 5)

    label("loc_1599")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AF")
    SetScenarioFlags(0x3B, 6)

    label("loc_15AF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C5")
    SetScenarioFlags(0x3B, 7)

    label("loc_15C5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15DB")
    SetScenarioFlags(0x3D, 5)

    label("loc_15DB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F1")
    SetScenarioFlags(0x3D, 6)

    label("loc_15F1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1607")
    SetScenarioFlags(0x3D, 7)

    label("loc_1607")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1642")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1732")

    label("loc_1642")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1665")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1732")

    label("loc_1665")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1688")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1732")

    label("loc_1688")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16AB")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1732")

    label("loc_16AB")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CE")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1732")

    label("loc_16CE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F1")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1732")

    label("loc_16F1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1714")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1732")

    label("loc_1714")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1732")
    SetScenarioFlags(0x3C, 7)

    label("loc_1732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1748")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_177A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177A")
    SetChrPos(0x0, -36420, 0, 17340, 315)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 17)

    label("loc_177A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_17AD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AD")
    SetChrPos(0x0, -60000, 0, 32650, 315)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_17AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_17BC")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 16)

    label("loc_17BC")

    Call(0, 11)
    Return()

    # Function_4_118E end

    def Function_5_17C0(): pass

    label("Function_5_17C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_17D2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17D2")

    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17EA")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_17EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17FD")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_17FD")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1815")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1815")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_182D")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_182D")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1845")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1845")

    ModifyEventFlags(0, 5, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_185D")
    ModifyEventFlags(1, 5, 0x80)

    label("loc_185D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1870")
    ModifyEventFlags(1, 5, 0x80)

    label("loc_1870")

    ModifyEventFlags(0, 6, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1888")
    ModifyEventFlags(1, 6, 0x80)

    label("loc_1888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_189B")
    OP_1B(0x1, 0x0, 0x38)

    label("loc_189B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18C1")
    SetMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    OP_70(0x3, 0x0)
    OP_10(0x2, 0x0)
    Jump("loc_18E4")

    label("loc_18C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18DA")
    SetMapObjFlags(0x3, 0x4)
    Jump("loc_18E4")

    label("loc_18DA")

    SetMapObjFlags(0x7, 0x4)
    OP_70(0x3, 0x28)

    label("loc_18E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1995")
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

    label("loc_1995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19A3")
    Jump("loc_1A3D")

    label("loc_19A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19D2")
    ClearMapObjFlags(0x24, 0x4)
    SetMapObjFrame(0x24, "light", 0x0, 0x1)
    SetMapObjFrame(0x24, "mark01", 0x0, 0x1)
    Jump("loc_1A3D")

    label("loc_19D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_19E0")
    Jump("loc_1A3D")

    label("loc_19E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_19EE")
    Jump("loc_1A3D")

    label("loc_19EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_19FC")
    Jump("loc_1A3D")

    label("loc_19FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1A0A")
    Jump("loc_1A3D")

    label("loc_1A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A18")
    Jump("loc_1A3D")

    label("loc_1A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A26")
    Jump("loc_1A3D")

    label("loc_1A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_1A34")
    Jump("loc_1A3D")

    label("loc_1A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1A3D")

    label("loc_1A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1A64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5F")
    ClearChrFlags(0x1F, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    SetChrFlags(0x1F, 0x8000)

    label("loc_1A5F")

    Jump("loc_1A6E")

    label("loc_1A64")

    SetChrFlags(0x1F, 0x80)
    ModifyEventFlags(0, 3, 0x80)

    label("loc_1A6E")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2597")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_2597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_2679")
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
    Jump("loc_2721")

    label("loc_2679")

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

    label("loc_2721")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -58330, -1000, 41020, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2785")
    OP_66(0x6, 0x1)

    label("loc_2785")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27CA")
    OP_65(0x6, 0x1)

    label("loc_27CA")

    MiniGame(0x2F, 0x7, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xB, 0x80)
    SetMapObjFlags(0x4, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_280A")
    OP_70(0x0, 0x0)
    Jump("loc_280E")

    label("loc_280A")

    OP_70(0x0, 0x1E)

    label("loc_280E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2821")
    OP_70(0x1, 0x0)
    Jump("loc_2825")

    label("loc_2821")

    OP_70(0x1, 0x1E)

    label("loc_2825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2838")
    OP_70(0x2, 0x0)
    Jump("loc_283C")

    label("loc_2838")

    OP_70(0x2, 0x1E)

    label("loc_283C")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_289D")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -39330, 0, 46720, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_289D")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28E9")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -82230, -2000, -27080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_28E9")

    OP_1C(0x0, 0x25, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0x26, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0x27, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    Return()

    # Function_5_17C0 end

    def Function_6_290B(): pass

    label("Function_6_290B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0B")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x9D, 1)"), scpexpr(EXPR_END)), "loc_2994")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E3, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_2A06")

    label("loc_2994")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x9D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x9D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2A06")

    Jump("loc_2A50")

    label("loc_2A0B")

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

    label("loc_2A50")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_290B end

    def Function_7_2A5C(): pass

    label("Function_7_2A5C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5C")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_2AE5")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E3, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_2B57")

    label("loc_2AE5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2B57")

    Jump("loc_2BA1")

    label("loc_2B5C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_2BA1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_2A5C end

    def Function_8_2BAD(): pass

    label("Function_8_2BAD")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CAD")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x38E, 1)"), scpexpr(EXPR_END)), "loc_2C36")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E3, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_2CA8")

    label("loc_2C36")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2CA8")

    Jump("loc_2CF2")

    label("loc_2CAD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_2CF2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_2BAD end

    def Function_9_2CFE(): pass

    label("Function_9_2CFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EB6")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_2E97")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E92")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2E8F")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2DB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2DB8)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_DCC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E8A")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E71")
    Call(1, 5)
    Jump("loc_2E8A")

    label("loc_2E71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E87")
    Call(1, 4)
    Jump("loc_2E8A")

    label("loc_2E87")

    Call(1, 3)

    label("loc_2E8A")

    Jump("loc_2E92")

    label("loc_2E8F")

    Call(1, 1)

    label("loc_2E92")

    Jump("loc_2EAD")

    label("loc_2E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2EAD")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2EAD")

    TalkEnd(0xFF)
    Return()

    label("loc_2EB6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_3041")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303C")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_3039")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2F62():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2F62)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_E10", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3034")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_301B")
    Call(1, 5)
    Jump("loc_3034")

    label("loc_301B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3031")
    Call(1, 4)
    Jump("loc_3034")

    label("loc_3031")

    Call(1, 3)

    label("loc_3034")

    Jump("loc_303C")

    label("loc_3039")

    Call(1, 1)

    label("loc_303C")

    Jump("loc_3057")

    label("loc_3041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_3057")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_3057")

    TalkEnd(0xFF)
    Return()

    # Function_9_2CFE end

    def Function_10_305C(): pass

    label("Function_10_305C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3214")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_31F5")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31F0")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_31ED")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3116():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3116)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_DCC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31E8")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_31CF")
    Call(1, 5)
    Jump("loc_31E8")

    label("loc_31CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_31E5")
    Call(1, 4)
    Jump("loc_31E8")

    label("loc_31E5")

    Call(1, 3)

    label("loc_31E8")

    Jump("loc_31F0")

    label("loc_31ED")

    Call(1, 1)

    label("loc_31F0")

    Jump("loc_320B")

    label("loc_31F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_320B")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_320B")

    TalkEnd(0xFF)
    Return()

    label("loc_3214")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_339F")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339A")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_3397")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_32C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_32C0)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_E10", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3392")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3379")
    Call(1, 5)
    Jump("loc_3392")

    label("loc_3379")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_338F")
    Call(1, 4)
    Jump("loc_3392")

    label("loc_338F")

    Call(1, 3)

    label("loc_3392")

    Jump("loc_339A")

    label("loc_3397")

    Call(1, 1)

    label("loc_339A")

    Jump("loc_33B5")

    label("loc_339F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_33B5")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_33B5")

    TalkEnd(0xFF)
    Return()

    # Function_10_305C end

    def Function_11_33BA(): pass

    label("Function_11_33BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33DC")
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)

    label("loc_33DC")

    Return()

    # Function_11_33BA end

    def Function_12_33DD(): pass

    label("Function_12_33DD")

    Call(1, 6)
    Return()

    # Function_12_33DD end

    def Function_13_33E1(): pass

    label("Function_13_33E1")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kバス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "クロスベル市西口\x01",      # 0
            "ベルガード門\x01",          # 1
            "やめる\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3473")
    Call(0, 14)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_3493")

    label("loc_3473")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3493")
    Call(0, 15)
    ClearMapFlags(0x8000000)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()

    label("loc_3493")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_13_33E1 end

    def Function_14_349B(): pass

    label("Function_14_349B")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_35CA")
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

    def lambda_3581():
        OP_95(0xFE, -43990, 0, 13530, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3581)
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

    label("loc_35CA")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_14_349B end

    def Function_15_35CE(): pass

    label("Function_15_35CE")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_36FD")
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

    def lambda_36B4():
        OP_95(0xFE, -39660, 0, 1670, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_36B4)
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

    label("loc_36FD")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_15_35CE end

    def Function_16_3701(): pass

    label("Function_16_3701")

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

    # Function_16_3701 end

    def Function_17_3752(): pass

    label("Function_17_3752")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_37AD")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37A2")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_37A8")

    label("loc_37A2")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_37A8")

    Jump("loc_37D1")

    label("loc_37AD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37CB")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_37D1")

    label("loc_37CB")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_37D1")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_3752 end

    def Function_18_37E6(): pass

    label("Function_18_37E6")

    TalkBegin(0xFE)

    #C0019
    ChrTalk(
        0x8,
        (
            "ふう、雨の中作業なんて\x01",
            "ついてないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "一通り片付いたし、\x01",
            "早いところ上がるとするかな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_37E6 end

    def Function_19_384D(): pass

    label("Function_19_384D")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0x9,
        (
            "あの頑強なゲートが\x01",
            "めちゃくちゃだったのを\x01",
            "ようやく片付けてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "なにをどうやったら\x01",
            "あんなことができるんだ……？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_384D end

    def Function_20_38CD(): pass

    label("Function_20_38CD")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38E5")
    SetScenarioFlags(0x0, 1)

    label("loc_38E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_END)), "loc_38F1")
    SetScenarioFlags(0x0, 1)

    label("loc_38F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ADC")
    TurnDirection(0xA, 0x101, 0)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0023
    ChrTalk(
        0xA,
        (
            "おや、もしかすると\x01",
            "君は釣公師団の人？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00000Fはい、ロイドと言います。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xA,
        "はは、やっぱり。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xA,
        (
            "俺の名前はトリトン。\x01",
            "《銀鯱》って渾名で呼ばれてる。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        (
            "まあ、こういうのって正直、\x01",
            "自分でもどうかと思うんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xA,
        (
            "釣師にはハッタリも必要らしくってね。\x01",
            "倶楽部の方針で名乗ってるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#00006Fな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        (
            "ま、勝負を挑みたい時は\x01",
            "いつでも言ってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        (
            "ただし、それなりの\x01",
            "資格は示してもらうけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ADC")
    OP_93(0xA, 0x0, 0x0)

    label("loc_3ADC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4534")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B32")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",            # 0
            "爆釣勝負を挑む\x01",      # 1
            "やめる\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_3B3C")

    label("loc_3B32")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41FF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B6A")
    TurnDirection(0xA, 0x0, 0)

    label("loc_3B6A")

    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4038")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CED")

    #C0032
    ChrTalk(
        0xA,
        (
            "どれどれ、それじゃ釣り手帳を\x01",
            "拝見させてもらうよ。\x02",
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
            "へ～、すごいじゃん。\x01",
            "よくぞこれだけの種類の魚を\x01",
            "釣って来たものだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xA,
        (
            "ふふ、それじゃお待ちかね、\x01",
            "俺との《爆釣勝負》と行こうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xA,
        (
            "種目は『爆釣５目勝負』――\x01\x07\x02",

            "先に５種類の魚を\x01",
            "釣り揃えた方が勝ち\x07\x00",
            "ってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        "なかなか面白そうだろう？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 0)
    Jump("loc_3D5D")

    label("loc_3CED")


    #C0037
    ChrTalk(
        0xA,
        "ん、俺と勝負するかい？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "種目は『爆釣５目勝負』――\x01\x07\x02",

            "先に５種類の魚を\x01",
            "釣り揃えた方が勝ち\x07\x00",
            "ってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D5D")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《銀鯱》トリトンに、\x01",
            "『爆釣５目勝負』を挑みますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "勝負を挑む\x01",      # 0
            "やめておく\x01",      # 1
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
        (0, "loc_3DF6"),
        (1, "loc_3FFF"),
        (SWITCH_DEFAULT, "loc_4033"),
    )


    label("loc_3DF6")


    #C0040
    ChrTalk(
        0xA,
        "はは、そうこなくっちゃ♪\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F38")
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

    label("loc_3F38")

    OP_68(-58660, 1000, 33990, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -57240, 0, 32830, 315)
    TurnDirection(0xA, 0x101, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F97")
    Call(0, 51)
    Jump("loc_3FBE")

    label("loc_3F97")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FAD")
    Call(0, 53)
    Jump("loc_3FBE")

    label("loc_3FAD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FBE")
    Call(0, 52)

    label("loc_3FBE")

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
    Jump("loc_4033")

    label("loc_3FFF")


    #C0041
    ChrTalk(
        0xA,
        "んー、そっか残念だ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_402E")
    OP_93(0xA, 0x0, 0x0)

    label("loc_402E")

    Jump("loc_4033")

    label("loc_4033")

    Jump("loc_41FA")

    label("loc_4038")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_412F")

    #C0042
    ChrTalk(
        0xA,
        (
            "どれどれ、それじゃ釣り手帳を\x01",
            "確認させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    #C0043
    ChrTalk(
        0xA,
        "ん～、惜しいけど後一歩だねー。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "ま、でもここまで来れたんなら\x01",
            "きっと辿り着けるさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xA,
        "あともう一息、頑張って来てよ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_412A")
    OP_93(0xA, 0x0, 0x0)

    label("loc_412A")

    Jump("loc_41FA")

    label("loc_412F")


    #C0046
    ChrTalk(
        0xA,
        (
            "どれどれ、それじゃ釣り手帳を\x01",
            "拝見させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    #C0047
    ChrTalk(
        0xA,
        "ん～、まだまだ努力不足だねー。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xA,
        (
            "とにかく、この程度の釣果じゃ\x01",
            "勝負を受けるわけには行かないな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41FA")
    OP_93(0xA, 0x0, 0x0)

    label("loc_41FA")

    Jump("loc_452F")

    label("loc_41FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_452F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4222")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4230")
    Jump("loc_452F")

    label("loc_4230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4295")

    #C0049
    ChrTalk(
        0xA,
        "ん～、何か最近どうにも物騒だね。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xA,
        (
            "もしかして、\x01",
            "釣りなんかしてる場合じゃない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452F")

    label("loc_4295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_42F0")

    #C0051
    ChrTalk(
        0xA,
        "いや～、今日は雨だね～～。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xA,
        (
            "びしょ濡れで参っちゃうよ。\x01",
            "あはははは。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452F")

    label("loc_42F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4357")

    #C0053
    ChrTalk(
        0xA,
        "くわ～あ～、しっかし眠いな～。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        (
            "これでも昨日は、\x01",
            "１２時間以上寝たんだけどね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452F")

    label("loc_4357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_43B1")

    #C0055
    ChrTalk(
        0xA,
        "す～～～っ、は～～～～～っ。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        "んん～、今日も空気がうんまいねぇ～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_452F")

    label("loc_43B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_440C")

    #C0057
    ChrTalk(
        0xA,
        "ふああ～、かかんないね～～。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "そろそろ、\x01",
            "次のエサ試してみるかな～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452F")

    label("loc_440C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4456")

    #C0059
    ChrTalk(
        0xA,
        "ぼけ～～～～～～～っ。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        "んん～、のどかだねぇ～～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_452F")

    label("loc_4456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4518")

    #C0061
    ChrTalk(
        0xA,
        "ふわ～、あ～～あ～～～っ。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "………………………………\x01",
            "……ん眠い…………………\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4513")

    #C0063
    ChrTalk(
        0x101,
        (
            "#00003F（ここなら何か釣れそうだけど……\x01",
            "  先客がいるなら止めておくか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4513")

    Jump("loc_452F")

    label("loc_4518")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4526")
    Jump("loc_452F")

    label("loc_4526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_452F")

    label("loc_452F")

    Jump("loc_3AE6")

    label("loc_4534")

    TalkEnd(0xFE)
    Return()

    # Function_20_38CD end

    def Function_21_4538(): pass

    label("Function_21_4538")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_455D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_455D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4578")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4578")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4593")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4593")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45AE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45C9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45E4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45FF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_461A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_461A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4635")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4635")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4650")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4650")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_466B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_466B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4686")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4686")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46A1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46BC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46D7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46F2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_470D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_470D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4728")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4728")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4743")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4743")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_475E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_475E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4779")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4779")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4794")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4794")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47AF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47CA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47E5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4800")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4800")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_481B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_481B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4836")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4836")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4851")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4851")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_486C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_486C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4887")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4887")

    Return()

    # Function_21_4538 end

    def Function_22_4888(): pass

    label("Function_22_4888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 3)), scpexpr(EXPR_END)), "loc_4892")
    Return()

    label("loc_4892")

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
        (1, "loc_4974"),
        (SWITCH_DEFAULT, "loc_498D"),
    )


    label("loc_4974")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -24310, 0, 47440, 180)
    EventEnd(0x5)
    Return()

    label("loc_498D")

    Battle("BattleInfo_E54", 0x0, 0x0, 0x100, 0xC, 0xFF)
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
        (2, "loc_4A4F"),
        (1, "loc_4A54"),
        (SWITCH_DEFAULT, "loc_4A57"),
    )


    label("loc_4A4F")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_4A54")

    OP_B9(0x0)
    Return()

    label("loc_4A57")

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
            "手配魔獣を退治した！\x02",
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0x73, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21D, 3)
    OP_29(0x99, 0x4, 0x2)
    OP_29(0x99, 0x4, 0x10)
    OP_29(0x99, 0x1, 0x0)
    OP_E2(0x2)
    ModifyEventFlags(0, 3, 0x80)
    EventEnd(0x5)
    Return()

    # Function_22_4888 end

    def Function_23_4AF4(): pass

    label("Function_23_4AF4")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0067
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DA3")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BDA")
    MiniGame(0x6, 0x13, 0xFFFF1E1A, 0x0, 0x88F4, 0x0, 0xFFFF1C26, 0xFFFFFC18, 0xA03C)
    Jump("loc_4DA3")

    label("loc_4BDA")

    MiniGame(0x6, 0x14, 0xFFFF1E1A, 0x0, 0x88F4, 0x0, 0xFFFF1C26, 0xFFFFFC18, 0xA03C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DA3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DA3")
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
        "ロイド",
        (
            "#00011Fう、うお……\x01",
            "この重量感はとんでもないな。\x02\x03",

            "#00003Fおまけに凄く綺麗だけど……\x01",
            "もしかして特別な魚だったり\x01",
            "するのかな。\x02",
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

    label("loc_4DA3")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_23_4AF4 end

    def Function_24_4DA8(): pass

    label("Function_24_4DA8")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DDA")
    SetScenarioFlags(0x31, 2)

    label("loc_4DDA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_4E1A")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E0F")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_4E15")

    label("loc_4E0F")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_4E15")

    Jump("loc_4E20")

    label("loc_4E1A")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_4E20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4E99")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4E79"),
        (SWITCH_DEFAULT, "loc_4E8A"),
    )


    label("loc_4E79")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4E94")

    label("loc_4E8A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E94")

    Jump("loc_50D8")

    label("loc_4E99")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4ECD")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_4ECD")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F01"),
        (1, "loc_5005"),
        (2, "loc_5096"),
        (SWITCH_DEFAULT, "loc_50CE"),
    )


    label("loc_4F01")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4F32")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4F42")

    label("loc_4F32")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4F42")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F98")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F98")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FBB")
    Sound(461, 0, 100, 0)

    label("loc_4FBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4FDB")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_4FEB")

    label("loc_4FDB")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_4FEB")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_4E20")

    label("loc_5005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_5077")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_503A")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_5052")

    label("loc_503A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_504D")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_5052")

    label("loc_504D")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_5052")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5091")

    label("loc_5077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5087")
    OP_AF(0xFB)
    Jump("loc_5091")

    label("loc_5087")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5091")

    Jump("loc_50D8")

    label("loc_5096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50AF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50C9")

    label("loc_50AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_50BF")
    OP_AF(0xFB)
    Jump("loc_50C9")

    label("loc_50BF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50C9")

    Jump("loc_50D8")

    label("loc_50CE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50D8")

    Jump("loc_4E20")

    label("loc_50DD")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_24_4DA8 end

    def Function_25_50EB(): pass

    label("Function_25_50EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52EE")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A4")

    #C0071
    ChrTalk(
        0x105,
        (
            "#10309Fさてと、バスに乗って\x01",
            "クロスベル市に帰るかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00006Fここまで来てそれはないから。\x02\x03",

            "#00000F道のりはあと半分って所かな？\x01",
            "残りも頑張って歩こう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529C")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ストーリーが進行すると、\x01",
            "各地の停留所からバスを\x01",
            "利用できるようになります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "街道の行き来に便利ですので、\x01",
            "時期が来た後にご活用ください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 5)

    label("loc_529C")

    SetScenarioFlags(0x0, 2)
    Jump("loc_52EB")

    label("loc_52A4")


    #C0075
    ChrTalk(
        0x101,
        (
            "#00000Fここまで来たら\x01",
            "あと半分って所かな？\x01",
            "残りも頑張って歩こう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52EB")

    EventEnd(0x3)
    Return()

    label("loc_52EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5361")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0077
    ChrTalk(
        0x101,
        (
            "#00001F事故のこともあるし、\x01",
            "バスを待ってる時間はないな。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x3)
    Return()

    label("loc_5361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_53A9")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力バスは運行を見合わせているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_53A9")

    Call(0, 13)
    Return()

    # Function_25_50EB end

    def Function_26_53AD(): pass

    label("Function_26_53AD")

    SetMapObjFlags(0x3, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5466")
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
            "#00001Fこっちは警察学校だな……\x02\x03",

            "ここにも当然、国防軍の兵士がいる。\x01",
            "気付かれる前に引き返そう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -56320, -6000, -83050, 0)
    OP_E2(0x2)
    EventEnd(0x4)
    Jump("loc_5949")

    label("loc_5466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5884")
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
            "#00003F#5Pこっちは警察学校方面か……\x02\x03",

            "#0001Fゲートは完全に閉まってるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        (
            "#00203F#6P……ゲート付近から\x01",
            "微量の導力波を感知しました。\x02\x03",

            "#00200Fどうやら新たにセンサーが\x01",
            "取り付けられているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00006F#5Pああ、俺の脱走を受けて\x01",
            "警備が強化されたのかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x105,
        (
            "#10400F#6Pまあ、近づくのは\x01",
            "やめておいた方が良さそうだね。\x02",
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
            "#00308F#12P留置所からの脱出、\x01",
            "ガルシアのおっさんが\x01",
            "手伝ってくれたんだってな？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x107,
        (
            "#01200F#3C#6P私が到着したときには\x01",
            "ロイド、おぬし一人だったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00008F#5Pああ、俺を逃がす為に\x01",
            "国防軍を引きつけてくれて……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x106,
        "#10712F#6Pあの《キリングベア》が……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        (
            "#00306F#12Pあのおっさんにも\x01",
            "色々あったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00003F#5P……あの後どうなったのかは\x01",
            "少し心配だけど……\x02\x03",

            "#00001Fとにかく今は、\x01",
            "先に進む事を考えよう。\x02",
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
    Jump("loc_5949")

    label("loc_5884")

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
            "#00200Fゲート付近にはセンサーが\x01",
            "取り付けられているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00003Fガルシアの事は気になるけど……\x01",
            "近づくのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -56320, -6000, -83050, 0)
    OP_E2(0x2)
    EventEnd(0x4)

    label("loc_5949")

    ClearMapObjFlags(0x3, 0x1000)
    Return()

    # Function_26_53AD end

    def Function_27_5950(): pass

    label("Function_27_5950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B0A")
    OP_29(0xAF, 0x1, 0xF)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)
    Sleep(500)

    #C0092
    ChrTalk(
        0x101,
        (
            "#00008F#5Pとはいえ、一通り回ったけど\x01",
            "今の所は八方ふさがりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x104,
        (
            "#00303F#12Pクロスベル市はもちろん、\x01",
            "ベルガード門にも警察学校方面にも\x01",
            "行けなさそうだしなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x106,
        "#10706F#6P困りましたね……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        (
            "#10400F#6Pふむ、他に行けそうな場所は\x01",
            "なかったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x107,
        (
            "#01200F#3C#6P多少、街道から外れて探してみた方が\x01",
            "いいのかもしれぬな。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x103,
        (
            "#00203F#5Pそうですね……\x01",
            "もう少し探してみましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B0A")

    Return()

    # Function_27_5950 end

    def Function_28_5B0B(): pass

    label("Function_28_5B0B")

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

    def lambda_5BF0():
        OP_9B(0x0, 0x101, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5BF0)
    Sleep(0)

    def lambda_5C08():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5C08)
    Sleep(0)

    def lambda_5C20():
        OP_9B(0x0, 0x109, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5C20)
    Sleep(0)

    def lambda_5C38():
        OP_9B(0x0, 0x105, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5C38)
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
            "#00000F#5Pうん、ちゃんとゲートを\x01",
            "開けてくれたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x105,
        "#10306F#5Pやれやれ、やっと着いたか。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#00102F#11Pここから先が\x01",
            "警察学校でいいのよね？\x02",
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
            "#00004F#5Pああ、この先には舗装された\x01",
            "森林道が続いてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x109,
        (
            "#10100F#6P道なりにしばらく進めば\x01",
            "警察学校の玄関に到着しますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        "#00100F#5Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x105,
        (
            "#10304F#6Pま、迎えも来ないみたいだし、\x01",
            "とっとと行くとしようか。\x02",
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

    def lambda_5F0B():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5F0B)
    Sleep(100)

    def lambda_5F1B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5F1B)
    Sleep(100)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    #C0105
    ChrTalk(
        0x101,
        (
            "#00006F#11P……駄目だ。\x01",
            "どうもさっきの男が気になる。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x109,
        "#10106F#6Pええ、強烈すぎましたからね……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        (
            "#00108F#5Pでも、課長の用事にも\x01",
            "応えないといけないし……\x02\x03",

            "#00101F何だったら２手に分かれる？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x105,
        (
            "#10303F#6Pこのまま警察学校に行く組と、\x01",
            "クロスベル市に戻る組か。\x02\x03",

            "#10300Fそれもアリかもしれないね。\x02",
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
            "#00003F#11Pいや、このメンバーで\x01",
            "２手に分かれるのは早過ぎる。\x02\x03",

            "#00001Fただ念のため、\x01",
            "捜査一課には連絡しておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x102,
        (
            "#00100F#5Pなるほど。\x01",
            "いいかもしれないわね。\x02",
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
    SetChrName("エマの声")

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──クロスベル警察、\x01",
            "捜査一課です。\x02",
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
            "#00000Fエマさん。\x01",
            "先ほどはどうも。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エマの声")

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バニングス捜査官。\x02\x03",

            "どうしました？\x01",
            "先ほどの件について進展が？\x02",
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
            "#00003Fいえ、それとは別件です。\x02\x03",

            "#00001F実は……\x02",
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
            "ロイドは街道で遭遇した\x01",
            "隻眼の大男について説明した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エマの声")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……赤毛で隻眼の偉丈夫#6Rいじょうぶ#、\x01",
            "年齢は４０代くらいですか……\x02\x03",

            "車や鉄道、飛行船を使わずに\x01",
            "徒歩で街道を通ってくるなんて……\x02\x03",

            "──分かりました。\x01",
            "こちらも気を付けておきます。\x02\x03",

            "そちらは、セルゲイ課長の用件を\x01",
            "果たしてくるといいでしょう。\x02",
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
            "#00000Fはい、お願いします。\x02",
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
            "#10302F#6Pフフ、一課のお姉さんに\x01",
            "連絡がついたみたいだね？\x02",
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
            "#00006F#11Pああ、これで少しは安心だろう。\x02\x03",

            "#00000Fそれじゃあゲートを潜ろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        "#00100F#5Pええ、行きましょう。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x109,
        "#10100F#6P了解しました。\x02",
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

    # Function_28_5B0B end

    def Function_29_657D(): pass

    label("Function_29_657D")

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

    def lambda_665E():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_665E)
    Sleep(20)

    def lambda_6676():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6676)
    Sleep(20)

    def lambda_668E():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_668E)
    Sleep(20)

    def lambda_66A6():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_66A6)
    Sleep(20)

    def lambda_66BE():
        OP_9B(0x0, 0x109, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_66BE)
    Sleep(20)

    def lambda_66D6():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_66D6)
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

    def lambda_67C8():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_67C8)
    Sleep(50)

    def lambda_67D8():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_67D8)
    Sleep(50)

    def lambda_67E8():
        OP_93(0x103, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_67E8)
    Sleep(50)

    def lambda_67F8():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_67F8)
    Sleep(50)

    def lambda_6808():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6808)
    Sleep(50)

    def lambda_6818():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6818)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0122
    ChrTalk(
        0x101,
        "#00007F#5Pなんだ……！？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x109,
        "#10107F#11Pこれは……破壊音！？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        "#00310F#11P爆発物の音じゃねえぞ！？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        "#00207F#5P南です、行ってみましょう！\x02",
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

    # Function_29_657D end

    def Function_30_692D(): pass

    label("Function_30_692D")

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

    def lambda_69FC():
        OP_95(0xFE, -56000, -6000, -83000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69FC)

    def lambda_6A16():
        OP_95(0xFE, -56800, -6000, -81800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A16)

    def lambda_6A30():
        OP_95(0xFE, -55250, -6000, -82300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6A30)

    def lambda_6A4A():
        OP_95(0xFE, -55950, -6000, -81050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A4A)

    def lambda_6A64():
        OP_95(0xFE, -55000, -6000, -80450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6A64)

    def lambda_6A7E():
        OP_95(0xFE, -56500, -6000, -79700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6A7E)
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

    def lambda_6BBD():
        OP_95(0xFE, -56000, -6000, -91000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BBD)

    def lambda_6BD7():
        OP_95(0xFE, -56800, -6000, -89800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BD7)

    def lambda_6BF1():
        OP_95(0xFE, -55250, -6000, -90300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BF1)

    def lambda_6C0B():
        OP_95(0xFE, -55950, -6000, -89050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C0B)

    def lambda_6C25():
        OP_95(0xFE, -55000, -6000, -88450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C25)

    def lambda_6C3F():
        OP_95(0xFE, -56500, -6000, -87700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C3F)
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
        "#00107F#12P#Nこ、これは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0127
    ChrTalk(
        0x101,
        (
            "#00010F#6P#Nここのゲートは一応、\x01",
            "特殊合金製だったはずだ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0128
    ChrTalk(
        0x109,
        (
            "#10106F#6P#Nし、信じられません……\x01",
            "ただの魔獣にこんな事が……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0129
    ChrTalk(
        0x104,
        (
            "#00311F#6P#N列車を脱線させた事といい……\x01",
            "どんだけの化物だっつーの。\x02",
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
            "#10303F#6P#N……とにかく追いかけよう。\x01",
            "まだ遠くには行ってないはずだ。\x02\x03",

            "#10301F森の奥に逃げられると厄介だよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E73():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6E73)
    Sleep(50)

    def lambda_6E83():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6E83)
    Sleep(50)

    def lambda_6E93():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6E93)
    Sleep(50)

    def lambda_6EA3():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6EA3)
    Sleep(50)

    def lambda_6EB3():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6EB3)
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
            "#00001F#11Pあ、ああ……\x01",
            "（さっきから様子が変だな？）\x02",
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

    # Function_30_692D end

    def Function_31_6F4F(): pass

    label("Function_31_6F4F")

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

    def lambda_72A7():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_72A7)
    Sleep(50)

    def lambda_72BF():
        OP_9B(0x0, 0x106, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_72BF)
    Sleep(50)

    def lambda_72D7():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_72D7)
    Sleep(50)

    def lambda_72EF():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_72EF)
    Sleep(50)

    def lambda_7307():
        OP_9B(0x0, 0x107, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_7307)
    Sleep(50)

    def lambda_731F():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_731F)
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
            "#00301F#6P西に行けばベルガード門には\x01",
            "すぐに辿り着けるが……\x02\x03",

            "#00306Fソーニャ司令がいるとなると\x01",
            "さすがにその勇気はねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        "#00206F#6P……確かに。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x105,
        (
            "#10403F#6Pとにかく行ける範囲内で\x01",
            "探索してみるしかないね。\x02\x03",

            "#10401F国防軍の装甲車が通ったら\x01",
            "身を隠す必要がありそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x106,
        "#10703F#6Pそうですね……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00008F#6P（ソーニャ司令か……）\x02\x03",

            "#00001F（……何とかコンタクトが\x01",
            "  取れるといいんだけど……）\x02",
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

    # Function_31_6F4F end

    def Function_32_7546(): pass

    label("Function_32_7546")

    BeginChrThread(0xFE, 0, 0, 36)
    OP_96(0xFE, 0xFFFF13DE, 0xBB8, 0x6DC4, 0x7D0, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_32_7546 end

    def Function_33_7565(): pass

    label("Function_33_7565")


    def lambda_756A():
        OP_96(0xFE, 0xFFFF13DE, 0xBB8, 0x6DC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_756A)
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

    # Function_33_7565 end

    def Function_34_75C5(): pass

    label("Function_34_75C5")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_75(0x29, 0x2, 0x0)
    SetChrPos(0xFE, -60450, 6000, 28100, 0)
    OP_96(0xFE, 0xFFFF13DE, 0x4650, 0x6DC4, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_34_75C5 end

    def Function_35_75FC(): pass

    label("Function_35_75FC")

    SetChrPos(0xFE, -60450, 6000, 28100, 0)

    def lambda_7612():
        OP_96(0xFE, 0xFFFF13DE, 0x4650, 0x6DC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7612)
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

    # Function_35_75FC end

    def Function_36_767C(): pass

    label("Function_36_767C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76A0")
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_36_767C")

    label("loc_76A0")

    Return()

    # Function_36_767C end

    def Function_37_76A1(): pass

    label("Function_37_76A1")

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

    # Function_37_76A1 end

    def Function_38_7706(): pass

    label("Function_38_7706")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7720")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_38_7706")

    label("loc_7720")

    Return()

    # Function_38_7706 end

    def Function_39_7721(): pass

    label("Function_39_7721")

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

    # Function_39_7721 end

    def Function_40_777C(): pass

    label("Function_40_777C")

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
        "サイクス",
        "#6A#40Wなんだこいつら……！？\x02",
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
        "ユーリ",
        "#6A#40Wははっ、ビビらしてやんよ！\x02",
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
        "ロイド",
        "#00010F（ぶつけてくる気か……！！）\x02",
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
            "#1K緊急ナビ\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "急ブレーキをかける\x01",        # 0
            "コースを外れて避ける\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CD9")
    OP_2C(0x8B, 0x1)
    SetScenarioFlags(0x178, 2)

    #N0141
    NpcTalk(
        0xC,
        "ロイド",
        "#00007Fノエル、急ブレーキだっ！\x02",
    )

    CloseMessageWindow()

    #N0142
    NpcTalk(
        0xC,
        "ノエル",
        "#10107Fはいっ！\x02",
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
        "レジー",
        "#8A#30W……なーんてなっ！\x02",
    )
    #Auto

    Sleep(1200)

    #N0144
    NpcTalk(
        0xC,
        "エリィ",
        "#00105Fああっ……！？\x02",
    )

    CloseMessageWindow()

    #N0145
    NpcTalk(
        0xC,
        "ランディ",
        (
            "#00303Fチッ……\x01",
            "無茶しやがる奴らだな。\x02\x03",

            "#00300Fだがこの程度なら\x01",
            "すぐに取り返せるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #N0146
    NpcTalk(
        0xC,
        "ロイド",
        (
            "#00000Fああ！\x01",
            "ノエル、引き続き\x01",
            "追跡してくれ！\x02",
        )
    )

    CloseMessageWindow()

    #N0147
    NpcTalk(
        0xC,
        "ノエル",
        "#10101F了解です！\x02",
    )

    CloseMessageWindow()
    Sound(494, 0, 100, 0)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    BeginChrThread(0xC, 1, 0, 48)
    OP_29(0x8B, 0x1, 0x2)
    Sleep(3000)
    Jump("loc_7EF1")

    label("loc_7CD9")


    #N0148
    NpcTalk(
        0xC,
        "ロイド",
        "#00007F一旦コースを外れよう！\x02",
    )

    CloseMessageWindow()

    #N0149
    NpcTalk(
        0xC,
        "ノエル",
        "#10105Fは、はいっ！\x02",
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
        "サイクス",
        "#8A#30Wなーんてなっ！\x02",
    )
    #Auto

    Sleep(1200)
    Sound(492, 0, 100, 0)
    WaitChrThread(0xC, 1)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)

    #N0151
    NpcTalk(
        0xC,
        "エリィ",
        "#00105Fああっ……！？\x02",
    )

    CloseMessageWindow()

    #N0152
    NpcTalk(
        0xC,
        "ランディ",
        (
            "#00303Fチッ……\x01",
            "無茶しやがる奴らだな。\x02\x03",

            "#00308Fブレーキだけで\x01",
            "うまくかわせりゃ\x01",
            "よかったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #N0153
    NpcTalk(
        0xC,
        "ロイド",
        (
            "#00006F（コースを外れたのは\x01",
            "  判断ミスだったな……）\x02\x03",

            "#00001F──すまない、ノエル！\x01",
            "もう一度発進してくれ！\x02",
        )
    )

    CloseMessageWindow()

    #N0154
    NpcTalk(
        0xC,
        "ノエル",
        "#10101F了解です！\x02",
    )

    CloseMessageWindow()
    OP_68(-48380, 2100, 2970, 2000)
    BeginChrThread(0xC, 1, 0, 49)
    OP_29(0x8B, 0x1, 0x3)
    Sleep(4000)

    label("loc_7EF1")

    SetScenarioFlags(0x22, 2)
    NewScene("r1020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_777C end

    def Function_41_7EFE(): pass

    label("Function_41_7EFE")

    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -45630, 0, 13920, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -47650, 0, 1320, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_41_7EFE end

    def Function_42_7F70(): pass

    label("Function_42_7F70")

    OP_9F(0x0, 0xC)
    OP_9F(0x1, -85890, 2000, 73990)
    OP_9F(0x1, -65760, 2000, 55290)
    OP_9F(0x1, -54460, 2000, 54530)
    OP_9F(0x1, -45720, 0, 54180)
    OP_9F(0x1, -34680, 0, 52700)
    OP_9F(0x1, -28120, 0, 46140)
    OP_9F(0x2, 0xC, 12000, 0x6)
    Return()

    # Function_42_7F70 end

    def Function_43_7FD2(): pass

    label("Function_43_7FD2")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, -85890, 2000, 73990)
    OP_9F(0x1, -65760, 2000, 55290)
    OP_9F(0x1, -54460, 2000, 54530)
    OP_9F(0x1, -45720, 0, 54180)
    OP_9F(0x1, -34680, 0, 52700)
    OP_9F(0x1, -28120, 0, 46140)
    OP_9F(0x2, 0xD, 11000, 0x6)
    Return()

    # Function_43_7FD2 end

    def Function_44_8034(): pass

    label("Function_44_8034")

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

    # Function_44_8034 end

    def Function_45_80A4(): pass

    label("Function_45_80A4")

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

    # Function_45_80A4 end

    def Function_46_813E(): pass

    label("Function_46_813E")

    OP_9F(0x0, 0xC)
    OP_9F(0x1, -46520, 0, 9080)
    OP_9F(0x1, -46890, 0, 7430)
    OP_9F(0x1, -46230, 0, 5680)
    OP_9F(0x2, 0xC, 12000, 0x6)
    Return()

    # Function_46_813E end

    def Function_47_8176(): pass

    label("Function_47_8176")

    OP_9F(0x0, 0xC)
    OP_9F(0x1, -46520, 0, 9080)
    OP_9F(0x1, -49690, 0, 3690)
    OP_9F(0x1, -52720, 0, 250)
    OP_9F(0x1, -56430, 0, -3730)
    OP_9F(0x2, 0xC, 15000, 0x6)
    Return()

    # Function_47_8176 end

    def Function_48_81BC(): pass

    label("Function_48_81BC")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -41760, 0, 1800)
    OP_9F(0x1, -26570, 0, 2310)
    OP_9F(0x1, -20250, 0, 7670)
    OP_9F(0x2, 0xFE, 12000, 0x6)
    Return()

    # Function_48_81BC end

    def Function_49_81F4(): pass

    label("Function_49_81F4")

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

    # Function_49_81F4 end

    def Function_50_826E(): pass

    label("Function_50_826E")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0155
    ChrTalk(
        0xA,
        (
            "まさか、この俺が負けるなんて……\x01",
            "君、やるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xA,
        (
            "それじゃ、この俺《銀鯱》を\x01",
            "倒した証を進呈させてもらうよ。\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0158
    ChrTalk(
        0x101,
        "#00012Fど、どうもありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        (
            "さて、これで君も当倶楽部が認める\x01",
            "『銀鯱イーター』ってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xA,
        (
            "はっきり言ってダサイ称号だけど、\x01",
            "ま、その辺はカンベンしてくれな。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        "#00006Fい、いえ……\x02",
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

    # Function_50_826E end

    def Function_51_8450(): pass

    label("Function_51_8450")


    #C0162
    ChrTalk(
        0xA,
        "なるほどね、こんな所か。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "まあ、今回は運が\x01",
            "悪かったのかもしれないし。\x01",
            "またいつでも挑戦してみてよ。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_51_8450 end

    def Function_52_84BD(): pass

    label("Function_52_84BD")


    #C0164
    ChrTalk(
        0xA,
        "棄権、か……まあいいけど。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        "それじゃ、また今度ね。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_52_84BD end

    def Function_53_84FA(): pass

    label("Function_53_84FA")


    #C0166
    ChrTalk(
        0xA,
        (
            "はは、俺と引き分けるなんて\x01",
            "けっこうやるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "まあいいや、次やる時は\x01",
            "決着を付けさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_53_84FA end

    def Function_54_856B(): pass

    label("Function_54_856B")

    EventBegin(0x1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85D5")

    #C0168
    ChrTalk(
        0x101,
        (
            "#00000Fこっちはベルガード門方面だな。\x02\x03",

            "警察学校まで\x01",
            "無用な寄り道はしないでおこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8623")

    #C0169
    ChrTalk(
        0x101,
        (
            "#00001F声が聞こえたのはこっちじゃない。\x01",
            "――南に向かおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8623")

    OP_5A()
    SetChrPos(0x0, -37940, 0, 20690, 225)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_54_856B end

    def Function_55_863A(): pass

    label("Function_55_863A")

    EventBegin(0x1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_868C")

    #C0170
    ChrTalk(
        0x101,
        (
            "#00001F声が聞こえたのはこっちじゃない。\x01",
            "――南に向かおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_868C")

    OP_5A()
    SetChrPos(0x0, -53410, 0, 18420, 143)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_55_863A end

    def Function_56_86A3(): pass

    label("Function_56_86A3")

    EventBegin(0x1)
    OP_E2(0x3)

    #C0171
    ChrTalk(
        0x101,
        (
            "#00001Fこっちはベルガード門方面か……\x02\x03",

            "これ以上近付くのは危険だな。\x01",
            "大人しく引き返そう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -70920, 2000, 59620, 135)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_56_86A3 end

    def Function_57_871C(): pass

    label("Function_57_871C")

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

    # Function_57_871C end

    def Function_58_8782(): pass

    label("Function_58_8782")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東・クロスベル市　　　　１３７セルジュ\x01",
            "北・ベルガード門　　　　　６１セルジュ\x01",
            "南・クロスベル警察学校　　３１セルジュ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_58_8782 end

    SaveToFile()

Try(main)
