from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "レイクロードⅢ世",       # 1
        "ペーター",               # 2
        "コパン",                 # 3
        "バス",                   # 4
        "ケサラン",               # 5
        "ケサラン",               # 6
        "ゴーディ・オッサー",     # 7
        "ゴーディ・オッサー",     # 8
        "幻獣",                   # 9
        "ナデリア茸",             # 10
        "セルダン支部長",         # 11
        "フィッシャー団長",       # 12
        "銀鯱トリトン",           # 13
        "竜宮カグヤ",             # 14
        "水狂ナルセス",           # 15
        "海刃シャークマン",       # 16
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
        "クロスベル市方面",       # 27
        "ウルスラ医科大学方面",   # 28
    ))

    ATBonus("ATBonus_6D8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_6F8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_56D6", 3,   10,  0,   8,   3,   0,   0)
    Sepith("Sepith_56AE", 0,   10,  0,   7,   4,   3,   0)
    Sepith("Sepith_56CE", 6,   4,   9,   4,   0,   0,   0)
    Sepith("Sepith_56BE", 0,   5,   0,   0,   6,   6,   6)
    Sepith("Sepith_56C6", 0,   10,  0,   5,   2,   4,   2)
    Sepith("Sepith_569E", 5,   3,   0,   8,   0,   4,   3)

    MonsterBattlePostion("MonsterBattlePostion_738", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_73C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_740", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_744", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_748", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_74C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_750", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_754", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_798", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_79C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_7A0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_7A4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_7A8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_7AC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_7B0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_718", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_72C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_730", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_734", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D4", 0, 0, 180)

    # monster count: 15

    BattleInfo(
        "BattleInfo_AF8", 0x0000, 58, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_56D6", 30, 40, 20, 10,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_968", 0x0010, 58, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_56AE", 30, 40, 20, 10,
        (
            ("ms63600.dat", 0, 0, 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms63600.dat", "ms63600.dat", 0, 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_C88", 0x0000, 58, 6, 45, 10, 1, 50, 0, "br1520", "Sepith_56CE", 30, 40, 20, 10,
        (
            ("ms65300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_8A0", 0x0000, 58, 6, 45, 10, 1, 40, 0, "br1520", "Sepith_56BE", 30, 40, 20, 10,
        (
            ("ms65200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_A30", 0x0000, 58, 6, 45, 10, 1, 30, 0, "br1520", "Sepith_56C6", 30, 40, 20, 10,
        (
            ("ms61300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_7D8", 0x0000, 58, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_569E", 30, 40, 20, 10,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_BC0", 0x0000, 58, 6, 45, 10, 1, 50, 0, "br1500", "Sepith_56CE", 30, 40, 20, 10,
        (
            ("ms65300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_D50", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7453", "ed7453", "ATBonus_6D8"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D94", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7453", "ed7453", "ATBonus_6D8"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_DD8", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88901.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7B8", "MonsterBattlePostion_798", "ed7454", "ed7453", "ATBonus_6F8"),
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

    DeclMonster(4930,    10160,   0,       0x1010000,    "BattleInfo_AF8", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-33140,  -4930,   0,       0x1010000,    "BattleInfo_968", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-38450,  -31510,  -2800,   0x1010000,    "BattleInfo_968", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-17540,  -38170,  -5600,   0x1010000,    "BattleInfo_C88", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-5060,   -13330,  -6300,   0x1010000,    "BattleInfo_8A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4200,    -20550,  -6300,   0x1010000,    "BattleInfo_A30", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(2370,    -42510,  -6300,   0x1010000,    "BattleInfo_8A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(19970,   -49310,  -6300,   0x1010000,    "BattleInfo_A30", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(33630,   -23560,  -5600,   0x1010000,    "BattleInfo_8A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(52410,   -28230,  -5600,   0x1010000,    "BattleInfo_A30", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-38810,  -52060,  -4200,   0x1010000,    "BattleInfo_7D8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-21590,  -49910,  -4200,   0x1010000,    "BattleInfo_7D8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-30050,  -108200, -4900,   0x1010000,    "BattleInfo_AF8", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-16070,  -108310, -5770,   0x1010000,    "BattleInfo_BC0", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-15000,  -92180,  -5770,   0x1010000,    "BattleInfo_BC0", 0,   26,  0xFFFF, 10, 11)

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

    PlaceName(7.0, 0.0, 52.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(-89.0, 0.0, -115.0, 0x0000, 0x0000, "ウルスラ医科大学方面")
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
        "Function_0_F24",          # 00, 0
        "Function_1_FDC",          # 01, 1
        "Function_2_FFB",          # 02, 2
        "Function_3_101A",         # 03, 3
        "Function_4_15D1",         # 04, 4
        "Function_5_1AF9",         # 05, 5
        "Function_6_1C4A",         # 06, 6
        "Function_7_1D9B",         # 07, 7
        "Function_8_1EEC",         # 08, 8
        "Function_9_224A",         # 09, 9
        "Function_10_25A8",        # 0A, 10
        "Function_11_25C1",        # 0B, 11
        "Function_12_25C5",        # 0C, 12
        "Function_13_2685",        # 0D, 13
        "Function_14_27B8",        # 0E, 14
        "Function_15_28EB",        # 0F, 15
        "Function_16_293C",        # 10, 16
        "Function_17_29D0",        # 11, 17
        "Function_18_2A4C",        # 12, 18
        "Function_19_2CFA",        # 13, 19
        "Function_20_2D61",        # 14, 20
        "Function_21_30A4",        # 15, 21
        "Function_22_30F0",        # 16, 22
        "Function_23_316C",        # 17, 23
        "Function_24_329B",        # 18, 24
        "Function_25_37EA",        # 19, 25
        "Function_26_3B7E",        # 1A, 26
        "Function_27_3BD3",        # 1B, 27
        "Function_28_3C27",        # 1C, 28
        "Function_29_428A",        # 1D, 29
    ))


    def Function_0_F24(): pass

    label("Function_0_F24")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_F64"),
        (1, "loc_F70"),
        (2, "loc_F7C"),
        (3, "loc_F88"),
        (4, "loc_F94"),
        (5, "loc_FA0"),
        (6, "loc_FAC"),
        (SWITCH_DEFAULT, "loc_FB8"),
    )


    label("loc_F64")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_F70")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_F7C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_F88")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_F94")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_FA0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_FAC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_FB8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_FC4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FDB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_FDB")

    Return()

    # Function_0_F24 end

    def Function_1_FDC(): pass

    label("Function_1_FDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FFA")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_1_FDC")

    label("loc_FFA")

    Return()

    # Function_1_FDC end

    def Function_2_FFB(): pass

    label("Function_2_FFB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1019")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_2_FFB")

    label("loc_1019")

    Return()

    # Function_2_FFB end

    def Function_3_101A(): pass

    label("Function_3_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1032")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_10E8")

    label("loc_1032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1040")
    Jump("loc_10E8")

    label("loc_1040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_105C")
    ClearChrFlags(0x8, 0x80)

    label("loc_105C")

    Jump("loc_10E8")

    label("loc_1061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_106F")
    Jump("loc_10E8")

    label("loc_106F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_107D")
    Jump("loc_10E8")

    label("loc_107D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_108B")
    Jump("loc_10E8")

    label("loc_108B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1099")
    Jump("loc_10E8")

    label("loc_1099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10A7")
    Jump("loc_10E8")

    label("loc_10A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10B5")
    Jump("loc_10E8")

    label("loc_10B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_10C3")
    Jump("loc_10E8")

    label("loc_10C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10D1")
    Jump("loc_10E8")

    label("loc_10D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_10DF")
    Jump("loc_10E8")

    label("loc_10DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_10E8")

    label("loc_10E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158C")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1175")
    SetScenarioFlags(0x38, 0)

    label("loc_1175")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118B")
    SetScenarioFlags(0x38, 1)

    label("loc_118B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A1")
    SetScenarioFlags(0x38, 2)

    label("loc_11A1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B7")
    SetScenarioFlags(0x38, 3)

    label("loc_11B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CD")
    SetScenarioFlags(0x38, 4)

    label("loc_11CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E3")
    SetScenarioFlags(0x38, 5)

    label("loc_11E3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F9")
    SetScenarioFlags(0x38, 6)

    label("loc_11F9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120F")
    SetScenarioFlags(0x38, 7)

    label("loc_120F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1225")
    SetScenarioFlags(0x39, 0)

    label("loc_1225")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123B")
    SetScenarioFlags(0x39, 1)

    label("loc_123B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1251")
    SetScenarioFlags(0x39, 2)

    label("loc_1251")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1267")
    SetScenarioFlags(0x39, 3)

    label("loc_1267")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_127D")
    SetScenarioFlags(0x39, 4)

    label("loc_127D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1293")
    SetScenarioFlags(0x39, 5)

    label("loc_1293")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A9")
    SetScenarioFlags(0x39, 6)

    label("loc_12A9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BF")
    SetScenarioFlags(0x39, 7)

    label("loc_12BF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D5")
    SetScenarioFlags(0x3A, 0)

    label("loc_12D5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EB")
    SetScenarioFlags(0x3A, 1)

    label("loc_12EB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1301")
    SetScenarioFlags(0x3A, 2)

    label("loc_1301")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1317")
    SetScenarioFlags(0x3A, 3)

    label("loc_1317")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132D")
    SetScenarioFlags(0x3A, 4)

    label("loc_132D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1343")
    SetScenarioFlags(0x3A, 5)

    label("loc_1343")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1359")
    SetScenarioFlags(0x3A, 6)

    label("loc_1359")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136F")
    SetScenarioFlags(0x3A, 7)

    label("loc_136F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1385")
    SetScenarioFlags(0x3B, 0)

    label("loc_1385")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139B")
    SetScenarioFlags(0x3B, 1)

    label("loc_139B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B1")
    SetScenarioFlags(0x3B, 2)

    label("loc_13B1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C7")
    SetScenarioFlags(0x3B, 3)

    label("loc_13C7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13DD")
    SetScenarioFlags(0x3B, 4)

    label("loc_13DD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F3")
    SetScenarioFlags(0x3B, 5)

    label("loc_13F3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1409")
    SetScenarioFlags(0x3B, 6)

    label("loc_1409")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141F")
    SetScenarioFlags(0x3B, 7)

    label("loc_141F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1435")
    SetScenarioFlags(0x3D, 5)

    label("loc_1435")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144B")
    SetScenarioFlags(0x3D, 6)

    label("loc_144B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1461")
    SetScenarioFlags(0x3D, 7)

    label("loc_1461")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149C")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_158C")

    label("loc_149C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BF")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_158C")

    label("loc_14BF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E2")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_158C")

    label("loc_14E2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1505")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_158C")

    label("loc_1505")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1528")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_158C")

    label("loc_1528")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154B")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_158C")

    label("loc_154B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156E")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_158C")

    label("loc_156E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158C")
    SetScenarioFlags(0x3C, 7)

    label("loc_158C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15BE")
    SetChrPos(0x0, -18130, 0, -610, 135)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 16)

    label("loc_15BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_15CD")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 15)

    label("loc_15CD")

    Call(0, 10)
    Return()

    # Function_3_101A end

    def Function_4_15D1(): pass

    label("Function_4_15D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_15E3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15E3")

    Sound(136, 1, 50, 0)
    SoundDistance(0x7D, 0x8DF4, 0xFFFFEA20, 0xFA32, 0x15F90, 0x11170, 0x64, 0x0)
    OP_E3(0x3F52, 0xFFFFE976, 0xFFFE520A)
    OP_E3(0xFFFFF10A, 0xFFFFECDC, 0xFFFDF6AC)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1637")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1637")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_165E")
    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16C7")

    label("loc_165E")

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

    label("loc_16C7")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18AB")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_18AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1902")
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
    Jump("loc_1932")

    label("loc_1902")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)

    label("loc_1932")

    MiniGame(0x2F, 0x7, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xB, 0x80)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_END)), "loc_197E")
    SetMapObjFrame(0xFF, "stone_off", 0x0, 0x1)
    Jump("loc_199B")

    label("loc_197E")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 56600, -7000, -23650, 6200, 3000, 265000)

    label("loc_199B")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 35830, -5800, -74960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F8")
    OP_70(0x1, 0x0)
    Jump("loc_19FC")

    label("loc_19F8")

    OP_70(0x1, 0x1E)

    label("loc_19FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0F")
    OP_70(0x2, 0x0)
    Jump("loc_1A13")

    label("loc_1A0F")

    OP_70(0x2, 0x1E)

    label("loc_1A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A26")
    OP_70(0x3, 0x0)
    Jump("loc_1A2A")

    label("loc_1A26")

    OP_70(0x3, 0x1E)

    label("loc_1A2A")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A8B")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 28200, -5600, -32259, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1A8B")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AD7")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -17180, -5500, -103100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_1AD7")

    OP_1C(0x0, 0xF, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x10, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x11, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    Return()

    # Function_4_15D1 end

    def Function_5_1AF9(): pass

    label("Function_5_1AF9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF9")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1B82")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1BF4")

    label("loc_1B82")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
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

    label("loc_1BF4")

    Jump("loc_1C3E")

    label("loc_1BF9")

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

    label("loc_1C3E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1AF9 end

    def Function_6_1C4A(): pass

    label("Function_6_1C4A")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4A")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x97, 1)"), scpexpr(EXPR_END)), "loc_1CD3")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1D45")

    label("loc_1CD3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x97),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x97),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D45")

    Jump("loc_1D8F")

    label("loc_1D4A")

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

    label("loc_1D8F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C4A end

    def Function_7_1D9B(): pass

    label("Function_7_1D9B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9B")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_1E24")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1E96")

    label("loc_1E24")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E96")

    Jump("loc_1EE0")

    label("loc_1E9B")

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

    label("loc_1EE0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1D9B end

    def Function_8_1EEC(): pass

    label("Function_8_1EEC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_20A4")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_2085")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2080")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_207D")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1FA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1FA6)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_D50", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2078")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_205F")
    Call(1, 5)
    Jump("loc_2078")

    label("loc_205F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2075")
    Call(1, 4)
    Jump("loc_2078")

    label("loc_2075")

    Call(1, 3)

    label("loc_2078")

    Jump("loc_2080")

    label("loc_207D")

    Call(1, 1)

    label("loc_2080")

    Jump("loc_209B")

    label("loc_2085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_209B")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_209B")

    TalkEnd(0xFF)
    Return()

    label("loc_20A4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_222F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_222A")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_2227")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2150():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2150)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_D94", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2222")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2209")
    Call(1, 5)
    Jump("loc_2222")

    label("loc_2209")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_221F")
    Call(1, 4)
    Jump("loc_2222")

    label("loc_221F")

    Call(1, 3)

    label("loc_2222")

    Jump("loc_222A")

    label("loc_2227")

    Call(1, 1)

    label("loc_222A")

    Jump("loc_2245")

    label("loc_222F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_2245")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2245")

    TalkEnd(0xFF)
    Return()

    # Function_8_1EEC end

    def Function_9_224A(): pass

    label("Function_9_224A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2402")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_23E3")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23DE")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_23DB")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2304():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2304)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_D50", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23D6")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23BD")
    Call(1, 5)
    Jump("loc_23D6")

    label("loc_23BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23D3")
    Call(1, 4)
    Jump("loc_23D6")

    label("loc_23D3")

    Call(1, 3)

    label("loc_23D6")

    Jump("loc_23DE")

    label("loc_23DB")

    Call(1, 1)

    label("loc_23DE")

    Jump("loc_23F9")

    label("loc_23E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_23F9")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_23F9")

    TalkEnd(0xFF)
    Return()

    label("loc_2402")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_258D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2588")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_2585")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_24AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_24AE)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_D94", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2580")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2567")
    Call(1, 5)
    Jump("loc_2580")

    label("loc_2567")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_257D")
    Call(1, 4)
    Jump("loc_2580")

    label("loc_257D")

    Call(1, 3)

    label("loc_2580")

    Jump("loc_2588")

    label("loc_2585")

    Call(1, 1)

    label("loc_2588")

    Jump("loc_25A3")

    label("loc_258D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_25A3")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_25A3")

    TalkEnd(0xFF)
    Return()

    # Function_9_224A end

    def Function_10_25A8(): pass

    label("Function_10_25A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25BB")
    Jump("loc_25C0")

    label("loc_25BB")

    SetChrFlags(0x1A, 0x80)

    label("loc_25C0")

    Return()

    # Function_10_25A8 end

    def Function_11_25C1(): pass

    label("Function_11_25C1")

    Call(1, 6)
    Return()

    # Function_11_25C1 end

    def Function_12_25C5(): pass

    label("Function_12_25C5")

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
            "クロスベル市南口\x01",        # 0
            "聖ウルスラ医科大学\x01",      # 1
            "やめる\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_265D")
    Call(0, 13)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_267D")

    label("loc_265D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267D")
    Call(0, 14)
    ClearMapFlags(0x8000000)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()

    label("loc_267D")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_12_25C5 end

    def Function_13_2685(): pass

    label("Function_13_2685")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_27B4")
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

    def lambda_276B():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_276B)
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

    label("loc_27B4")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_13_2685 end

    def Function_14_27B8(): pass

    label("Function_14_27B8")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_28E7")
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

    def lambda_289E():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_289E)
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

    label("loc_28E7")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_14_27B8 end

    def Function_15_28EB(): pass

    label("Function_15_28EB")

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

    # Function_15_28EB end

    def Function_16_293C(): pass

    label("Function_16_293C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2997")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_298C")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_2992")

    label("loc_298C")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_2992")

    Jump("loc_29BB")

    label("loc_2997")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29B5")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_29BB")

    label("loc_29B5")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_29BB")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_16_293C end

    def Function_17_29D0(): pass

    label("Function_17_29D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E5")
    Call(0, 25)
    Jump("loc_2A48")

    label("loc_29E5")


    #C0019
    ChrTalk(
        0x8,
        (
            "それにしても、ギガルークが\x01",
            "このクロスベルに現れるとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        "見てろ……必ず仕留めてくれる！\x02",
    )

    CloseMessageWindow()

    label("loc_2A48")

    TalkEnd(0xFE)
    Return()

    # Function_17_29D0 end

    def Function_18_2A4C(): pass

    label("Function_18_2A4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C17")

    #C0021
    ChrTalk(
        0x9,
        (
            "あの巨大な樹は気になりますが、\x01",
            "とにかく釣り糸を垂らさない事には\x01",
            "心が落ち着きませんからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "釣りでも何でも、とにかく\x01",
            "ドンと構えていることが重要だと\x01",
            "私は思うんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2B58")

    #C0023
    ChrTalk(
        0x9,
        (
            "というわけで、ロイド師も\x01",
            "よければこれで息抜きして下さい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B97")

    label("loc_2B58")


    #C0024
    ChrTalk(
        0x9,
        (
            "というわけで、ロイド君も\x01",
            "よければこれで息抜きして下さい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B97")

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
            "を５個受け取った。\x02",
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
        "#00000Fあ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 1)
    Jump("loc_2CF6")

    label("loc_2C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB9")

    #C0027
    ChrTalk(
        0x9,
        (
            "ちなみにセルダン支部長は\x01",
            "ボート小屋の\x01",
            "様子を見に行きましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "ふふ、どうやら支部長は\x01",
            "あの場所が気に入って\x01",
            "忘れられないみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CF6")

    label("loc_2CB9")


    #C0029
    ChrTalk(
        0x9,
        (
            "さて、今日は心ゆくまで\x01",
            "釣りに集中させてもらいますよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF6")

    TalkEnd(0xFE)
    Return()

    # Function_18_2A4C end

    def Function_19_2CFA(): pass

    label("Function_19_2CFA")

    TalkBegin(0xFE)

    #C0030
    ChrTalk(
        0xA,
        (
            "ああ……ようやく\x01",
            "市外で釣りが出来るッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        (
            "大自然の中でする釣りは、\x01",
            "やっぱ最高ッスね！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_2CFA end

    def Function_20_2D61(): pass

    label("Function_20_2D61")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D93")
    SetScenarioFlags(0x31, 2)

    label("loc_2D93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2DD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2DD3")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2DC8")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_2DCE")

    label("loc_2DC8")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_2DCE")

    Jump("loc_2DD9")

    label("loc_2DD3")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_2DD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3096")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2E52")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E32"),
        (SWITCH_DEFAULT, "loc_2E43"),
    )


    label("loc_2E32")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2E4D")

    label("loc_2E43")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E4D")

    Jump("loc_3091")

    label("loc_2E52")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2E86")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_2E86")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EBA"),
        (1, "loc_2FBE"),
        (2, "loc_304F"),
        (SWITCH_DEFAULT, "loc_3087"),
    )


    label("loc_2EBA")

    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_74(0xC, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EEB")
    OP_70(0xC, 0x12C)
    OP_71(0xC, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2EFB")

    label("loc_2EEB")

    OP_70(0xC, 0xF0)
    OP_71(0xC, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2EFB")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F51")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F51")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F74")
    Sound(461, 0, 100, 0)

    label("loc_2F74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F94")
    OP_70(0xC, 0x14A)
    OP_71(0xC, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2FA4")

    label("loc_2F94")

    OP_70(0xC, 0x10E)
    OP_71(0xC, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2FA4")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0xC, "light", 0x1, 0x1)
    OP_70(0xC, 0x0)
    Jump("loc_2DD9")

    label("loc_2FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3030")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2FF3")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_300B")

    label("loc_2FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3006")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_300B")

    label("loc_3006")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_300B")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_304A")

    label("loc_3030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3040")
    OP_AF(0xFB)
    Jump("loc_304A")

    label("loc_3040")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_304A")

    Jump("loc_3091")

    label("loc_304F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3068")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3082")

    label("loc_3068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3078")
    OP_AF(0xFB)
    Jump("loc_3082")

    label("loc_3078")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3082")

    Jump("loc_3091")

    label("loc_3087")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3091")

    Jump("loc_2DD9")

    label("loc_3096")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_2D61 end

    def Function_21_30A4(): pass

    label("Function_21_30A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_30EC")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0032
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

    label("loc_30EC")

    Call(0, 12)
    Return()

    # Function_21_30A4 end

    def Function_22_30F0(): pass

    label("Function_22_30F0")

    Battle("BattleInfo_DD8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3137")
    OP_90(0x0, -30320, -2800, -33510, 90)
    EventEnd(0x5)
    SetChrFlags(0x10, 0x8000)
    Jump("loc_316B")

    label("loc_3137")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314A")
    Jump("loc_316B")

    label("loc_314A")

    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0xE, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 1)
    EventEnd(0x5)

    label("loc_316B")

    Return()

    # Function_22_30F0 end

    def Function_23_316C(): pass

    label("Function_23_316C")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0033
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3296")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3274")
    MiniGame(0x6, 0xD, 0x8E30, 0xFFFFE76E, 0xFFFEF89A, 0xB4, 0x8BF6, 0xFFFFE958, 0xFFFEDB30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_326F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_END)), "loc_326F")
    Call(0, 29)
    Return()

    label("loc_326F")

    Jump("loc_3296")

    label("loc_3274")

    MiniGame(0x6, 0xC, 0x8E30, 0xFFFFE76E, 0xFFFEF89A, 0xB4, 0x8BF6, 0xFFFFE958, 0xFFFEDB30)

    label("loc_3296")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_23_316C end

    def Function_24_329B(): pass

    label("Function_24_329B")

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

    def lambda_338D():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_338D)
    Sleep(0)

    def lambda_33A5():
        OP_9B(0x0, 0x102, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_33A5)
    Sleep(0)

    def lambda_33BD():
        OP_9B(0x0, 0x103, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_33BD)
    Sleep(0)

    def lambda_33D5():
        OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_33D5)
    Sleep(0)

    def lambda_33ED():
        OP_9B(0x0, 0x109, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_33ED)
    Sleep(0)

    def lambda_3405():
        OP_9B(0x0, 0x105, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3405)
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
        "#00005F#5Pあれは……\x02",
    )

    CloseMessageWindow()
    OP_68(57750, -6200, -24100, 3000)
    MoveCamera(58, 30, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(22000, 3000)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 3)), scpexpr(EXPR_END)), "loc_3551")

    #C0036
    ChrTalk(
        0x109,
        (
            "#10111Fいつの間にこんな……\x02\x03",

            "#10101F前に来た時は\x01",
            "開いていませんでしたよね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35A6")

    label("loc_3551")


    #C0037
    ChrTalk(
        0x109,
        (
            "#10111Fいつの間にこんな……\x02\x03",

            "#10108F昔、巡回した時には\x01",
            "開いていなかったのに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A6")


    #C0038
    ChrTalk(
        0x104,
        (
            "#00301F何かの弾みで、埋まってた入口が\x01",
            "開けちまったのかもしれねぇな。\x02",
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
            "#10304F#6Pで、ここを抜けた先に\x01",
            "《幻獣》がいるわけだね？\x02\x03",

            "#10300F“場の異常”の気配はどうだい？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_368E():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_368E)

    def lambda_369B():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_369B)
    Sleep(50)

    def lambda_36AB():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_36AB)
    Sleep(50)

    def lambda_36BB():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_36BB)
    Sleep(50)

    def lambda_36CB():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_36CB)
    Sleep(50)

    def lambda_36DB():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_36DB)
    Sleep(50)

    def lambda_36EB():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_36EB)
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
            "#00203F#5P……今の所、はっきりとは。\x02\x03",

            "#00201Fただ、妙な気配は感じます。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#00108F#12Pそう……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#00001F#11P……とにかく\x01",
            "入ってみるしかないだろう。\x02",
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

    # Function_24_329B end

    def Function_25_37EA(): pass

    label("Function_25_37EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A7")

    #C0043
    ChrTalk(
        0x8,
        "来たか……さっそく始めるぞ。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "まずはこの《釣皇》に\x01",
            "挑む資格が本当にあるのか……\x01",
            "それを試してやる。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "その名も『爆釣必中勝負』――\x01",
            "果たして付いて来られるかな？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3900")

    label("loc_38A7")


    #C0046
    ChrTalk(
        0x8,
        "フン、心の準備はできたか？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "『爆釣必中勝負』……\x01",
            "貴様の気概と実力を見せてみろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3900")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レイクロードⅢ世に、\x01",
            "『爆釣必中勝負』を挑みますか？\x07\x00\x02",
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
        (0, "loc_3999"),
        (1, "loc_3B3A"),
        (SWITCH_DEFAULT, "loc_3B7D"),
    )


    label("loc_3999")


    #C0049
    ChrTalk(
        0x8,
        "いい覚悟だ……行くぞ！\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A76")
    Call(0, 28)
    Return()

    label("loc_3A76")

    OP_68(45050, -5700, -58570, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 44490, -6270, -58570, 90)
    OP_93(0xFE, 0x10E, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD5")
    Call(0, 26)
    Jump("loc_3AF9")

    label("loc_3AD5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE8")
    Jump("loc_3AF9")

    label("loc_3AE8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF9")
    Call(0, 27)

    label("loc_3AF9")

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
    Jump("loc_3B7D")

    label("loc_3B3A")


    #C0050
    ChrTalk(
        0x8,
        "フン、今更怖気づいたか？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "……まあいい、勝手にしろ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B7D")

    label("loc_3B7D")

    Return()

    # Function_25_37EA end

    def Function_26_3B7E(): pass

    label("Function_26_3B7E")


    #C0052
    ChrTalk(
        0x8,
        (
            "フハハッ、\x01",
            "格の違いを思い知ったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "他愛もないとは、\x01",
            "まさにこのことだな。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_26_3B7E end

    def Function_27_3BD3(): pass

    label("Function_27_3BD3")


    #C0054
    ChrTalk(
        0x8,
        (
            "フンッ、まさか\x01",
            "勝負を途中で投げるとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "……くだらん、実にくだらんぞ。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_27_3BD3 end

    def Function_28_3C27(): pass

    label("Function_28_3C27")

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
        "フフフ……フハハハハッ！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "面白い、実に面白い……\x01",
            "よくぞまあ『爆釣必中勝負』で\x01",
            "ここまで付いて来れたものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "良かろう、\x01",
            "貴様のことを認めてやるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "だが問題は決着か……\x01",
            "さて、フィナーレに相応しい\x01",
            "勝負はどうしたものか――\x02",
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

    def lambda_3F5A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F5A)
    Sleep(50)

    def lambda_3F6A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3F6A)
    Sleep(300)
    StopEffect(0x1, 0x2)

    #C0060
    ChrTalk(
        0x101,
        "#00005Fい、今のは……！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "フハハ、どうやら我らの\x01",
            "熱に当てられてとんだ大物が\x01",
            "迷い込んだようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "今のは確かにパルルクだったが……\x01",
            "４アージュ級の巨体を誇っていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "そう、あれはまさしく\x01",
            "超希少上位種・ギガルーク！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "フハハッ、まさかクロスベルで\x01",
            "出会えるとは思わなかったぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#00005Fギ、ギガルーク……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    #C0066
    ChrTalk(
        0x8,
        (
            "ともかく、我らの\x01",
            "最終勝負はこれで決まりだ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    #C0067
    ChrTalk(
        0x8,
        (
            "あのギガルークを\x01",
            "先に釣り上げた者……\x01",
            "それがこの対決の勝者とする。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        "――異論はないな？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00003Fえ、ええ。\x01",
            "それは構いませんが……\x02\x03",

            "#00001F（あんな超大物……\x01",
            "  確かに釣れたら凄いよな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        "フフ、決まりだな。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "では、ここからは\x01",
            "時間もターンも関係ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "一体どちらが先に\x01",
            "ヤツを釣り上げられるか……\x01",
            "さっそく勝負開始だ！\x02",
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

    # Function_28_3C27 end

    def Function_29_428A(): pass

    label("Function_29_428A")

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
            "ギガルークはさらに何かを吐き出した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEF, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_433B")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xEF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0xEF, 1)
    Jump("loc_4358")

    label("loc_433B")


    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x6F, 1)

    label("loc_4358")

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
            "な、なんということだ。\x01",
            "この俺が先を越されるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "……ふむ、だが負けは負け。\x01",
            "素直に認めざるを得ないようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        "貴様……いや貴公にはこれを贈ろう。\x02",
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
            "を受け取った。\x02",
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
            "そしてこの証を得た貴公には\x01",
            "釣皇倶楽部の規約により、\x01",
            "『釣皇スレイヤー』の称号が与えられる。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "大陸中の釣師が一目置く称号だ。\x01",
            "光栄に思うがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        "あとは、勝負の取り決めについてだが……\x02",
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
        "レ、レイクロード様！\x02",
    )

    CloseMessageWindow()

    def lambda_46E1():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46E1)
    Sleep(50)

    def lambda_46F1():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_46F1)
    OP_68(37270, -5200, -59200, 4000)
    MoveCamera(331, 19, 0, 4000)
    OP_6E(530, 4000)
    SetCameraDistance(19090, 4000)

    def lambda_472C():
        OP_95(0xFE, 34400, -6070, -60340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_472C)
    Sleep(50)

    def lambda_4749():
        OP_95(0xFE, 36920, -5650, -57140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4749)
    Sleep(50)

    def lambda_4766():
        OP_95(0xFE, 34950, -5770, -58800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4766)
    Sleep(50)

    def lambda_4783():
        OP_95(0xFE, 37600, -5610, -55680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4783)
    Sleep(50)

    def lambda_47A0():
        OP_95(0xFE, 35900, -5610, -55640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_47A0)
    Sleep(50)

    def lambda_47BD():
        OP_95(0xFE, 35440, -5610, -56920, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_47BD)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)

    #C0084
    ChrTalk(
        0x12,
        (
            "はあはあ……\x01",
            "ロイド団員、君はまさか……\x02",
        )
    )

    CloseMessageWindow()

    #N0085
    NpcTalk(
        0x13,
        "？？？",
        (
            "#5Pふむ、どうやら既に\x01",
            "決着は付いていたようであるな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x8, 500)

    #C0086
    ChrTalk(
        0x8,
        "き、貴様はハーバード……！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        "ハーバード・フィッシャー！！\x02",
    )

    CloseMessageWindow()

    def lambda_4894():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4894)
    Sleep(50)

    def lambda_48A4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_48A4)
    Sleep(50)

    def lambda_48B4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_48B4)
    Sleep(50)

    def lambda_48C4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_48C4)
    Sleep(50)

    def lambda_48D4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_48D4)

    #C0088
    ChrTalk(
        0x13,
        (
            "#5Pそういう君はウィリアム坊……\x01",
            "見ない内に大きくなったものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x13,
        (
            "#5Pいや、今はレイクロードⅢ世と\x01",
            "呼ぶべきだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "フンッ、この裏切り者が！\x01",
            "気安く俺の名前を呼ぶんじゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "貴様……なぜ釣皇倶楽部を捨てた！\x01",
            "なぜ父に対し、恩を仇で返した！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x13,
        "#5Pふむ……それは誤解なのである。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x13,
        (
            "#5P確かに我輩と釣皇倶楽部との間に\x01",
            "少なからず確執があったことは\x01",
            "事実であるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x13,
        (
            "#5P我輩が釣皇倶楽部を脱退し、\x01",
            "釣公師団を設立したことは君の父君\x01",
            "レイクロードⅡ世も承知の上だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x13,
        (
            "#5Pだからこそ我輩は、\x01",
            "釣皇倶楽部時代に名乗っていた\x01",
            "《太公望》の称号を今も――\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "ええい、うるさい。\x01",
            "偉そうに御託を並べるんじゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "とにかく、貴様が出るのであれば\x01",
            "引導を渡してやろうと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "正直、今は腹が一杯なのでな。\x01",
            "またの機会に取っておいてやる。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "それまで、せいぜい\x01",
            "首を洗って待っていることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x13,
        "#5Pふむ……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "そして、セルダン。\x01",
            "約束通り事務所は返還するが、\x01",
            "少々荷物整理の時間はもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "それが済んだら、\x01",
            "俺たち釣皇倶楽部は\x01",
            "クロスベルから完全撤退だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x12,
        "……ああ、了解だ。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x12,
        (
            "あとは――\x01",
            "何でも１つだけ命令を\x01",
            "聞いてくれるんだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        "フン、もう決まっているのか？\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x12,
        "ああ、そういうことだ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x101, 500)

    #C0107
    ChrTalk(
        0x12,
        "ロイド団員、構わないか？\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00001Fええ、もちろんです。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x8, 500)

    #C0109
    ChrTalk(
        0x12,
        (
            "コホン……\x01",
            "では命令させてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x12,
        (
            "『釣皇倶楽部の\x01",
            "  クロスベルからの撤退を\x01",
            "  取り消してもらう』。\x02",
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

    def lambda_4F46():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4F46)
    Sleep(50)

    def lambda_4F56():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4F56)
    Sleep(50)

    def lambda_4F66():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4F66)
    Sleep(50)

    def lambda_4F76():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4F76)
    Sleep(50)

    def lambda_4F86():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4F86)
    Sleep(300)

    #C0111
    ChrTalk(
        0x101,
        "#00005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x13,
        "#5Pほう……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "き、貴様……\x01",
            "俺たちを舐めているのか！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x12,
        "いや……むしろその逆だ。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x12,
        (
            "アンタらと戦って、\x01",
            "俺たちは自分たちの世界が\x01",
            "いかに狭いかを知った。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x12,
        (
            "機会があれば、\x01",
            "また一緒に釣りをしたい……\x01",
            "単純にそう思っただけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        "#00002Fセルダン支部長……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x13,
        (
            "#5Pふむ、さすが我輩が\x01",
            "見込んだ男なのである。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        "一緒に釣り、だと……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "貴様らと馴れ合うことなど\x01",
            "できるわけが――\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x12,
        "それならそれで構わない。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x12,
        (
            "俺たちはそもそも、\x01",
            "邪魔さえされなければ\x01",
            "誰でも大歓迎なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x12,
        (
            "それさえ守ってくれるなら、\x01",
            "俺たちのボート小屋を自由に\x01",
            "使ってくれても構わないしな。\x02",
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
            "だ、誰があのような\x01",
            "粗末な小屋を使うと言うのだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "とにかく、ルールは\x01",
            "ルールとして受け入れるが……\x01",
            "後からの変更は受け付けんぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        "それでもいいと言うのだな？\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x12,
        "ああ、問題ない。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "フン……\x01",
            "ハーバートといい貴様といい\x01",
            "どこまでもお目出度い連中だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "ああ、それと\x01",
            "受付のセイラームだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "あいつは元々、\x01",
            "釣皇倶楽部の人間ではない上に、\x01",
            "釣公師団に入りたがっていたからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        "貴様らが面倒を見てやれ、いいな。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x12,
        "ああ、そのくらいお安い御用だ。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        "フンッ、話は以上だ。\x02",
    )

    CloseMessageWindow()
    OP_68(37650, -5000, -59390, 3000)
    MoveCamera(4, 23, 0, 3000)
    OP_6E(530, 3000)
    SetCameraDistance(18950, 3000)

    def lambda_5433():
        OP_95(0xFE, 36110, -5730, -58120, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5433)
    Sleep(500)

    def lambda_5450():

        label("loc_5450")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5450")

    QueueWorkItem2(0x101, 1, lambda_5450)
    Sleep(50)

    def lambda_5465():

        label("loc_5465")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5465")

    QueueWorkItem2(0x13, 1, lambda_5465)
    Sleep(50)

    def lambda_547A():

        label("loc_547A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_547A")

    QueueWorkItem2(0x12, 1, lambda_547A)
    Sleep(50)

    def lambda_548F():

        label("loc_548F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_548F")

    QueueWorkItem2(0x102, 1, lambda_548F)
    Sleep(50)

    def lambda_54A4():

        label("loc_54A4")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_54A4")

    QueueWorkItem2(0x103, 1, lambda_54A4)
    Sleep(50)

    def lambda_54B9():

        label("loc_54B9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_54B9")

    QueueWorkItem2(0x104, 1, lambda_54B9)
    Sleep(50)

    def lambda_54CE():

        label("loc_54CE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_54CE")

    QueueWorkItem2(0x109, 1, lambda_54CE)
    Sleep(50)

    def lambda_54E3():

        label("loc_54E3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_54E3")

    QueueWorkItem2(0x105, 1, lambda_54E3)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)

    #C0134
    ChrTalk(
        0x8,
        (
            "さあ、皆の者。\x01",
            "さっさと片付けて本国へ帰るぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(185, 20, -1, -1)
    SetChrName("釣傑四天王")

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "――イエス・ボス！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_95(0x8, 34490, -5660, -57880, 2000, 0x0)

    def lambda_557D():
        OP_95(0xFE, 31090, -5670, -51170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_557D)
    Sleep(50)

    def lambda_559A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_559A)
    Sleep(50)

    def lambda_55AA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_55AA)
    Sleep(50)

    def lambda_55BA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_55BA)
    Sleep(50)

    def lambda_55CA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_55CA)
    WaitChrThread(0x15, 1)
    Sleep(1000)

    def lambda_55DE():
        OP_95(0xFE, 33250, -5600, -50050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_55DE)
    Sleep(50)

    def lambda_55FB():
        OP_95(0xFE, 34190, -5610, -52480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_55FB)
    Sleep(50)

    def lambda_5618():
        OP_95(0xFE, 32560, -5600, -52360, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5618)
    Sleep(50)

    def lambda_5635():
        OP_95(0xFE, 33770, -5600, -52140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5635)
    OP_68(37650, -3000, -59390, 3000)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("r0200", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_428A end

    SaveToFile()

Try(main)
