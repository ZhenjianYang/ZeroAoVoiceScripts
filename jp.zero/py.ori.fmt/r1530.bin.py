from ZeroScenarioHelper import *

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
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 3000, 0, 28000, 0, 0, 1, 96, 0, 2, 0, 3],
    )

    BuildStringList((
        "r1530",                  # 0
        "チルル",                 # 1
        "コパン",                 # 2
        "ペーター",               # 3
        "ペーター",               # 4
        "特級釣師ロイド",         # 5
        "セルダン支部長",         # 6
        "ヨアヒム准教授",         # 7
        "バス",                   # 8
        "バックラッシュ",         # 9
        "br1500",                 # 10
        "br1520",                 # 11
        "br1500",                 # 12
        "br1520",                 # 13
        "br1500",                 # 14
        "br1500",                 # 15
        "br1520",                 # 16
        "br1520",                 # 17
        "br1520",                 # 18
        "クロスベル市方面",       # 19
        "ウルスラ医科大学方面",   # 20
    ))

    ATBonus("ATBonus_630", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_8DD3", 2,   8,   0,   6,   2,   0,   0)
    Sepith("Sepith_8DAB", 0,   8,   0,   4,   4,   2,   0)
    Sepith("Sepith_8DCB", 7,   3,   5,   3,   0,   0,   0)
    Sepith("Sepith_8DBB", 0,   3,   0,   0,   5,   5,   5)
    Sepith("Sepith_8DC3", 0,   8,   0,   2,   2,   4,   2)
    Sepith("Sepith_8D9B", 4,   2,   0,   8,   0,   3,   2)

    MonsterBattlePostion("MonsterBattlePostion_690", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_694", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_698", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_69C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_6F4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_6F8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_6FC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_700", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_704", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_708", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_70C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_670", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_674", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_678", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_67C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_680", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_684", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_688", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_68C", 2, 13, 180)

    # monster count: 15

    BattleInfo(
        "BattleInfo_A50", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_8DD3", 30, 40, 20, 10,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", "ms69800.dat", 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_8C0", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_8DAB", 30, 40, 20, 10,
        (
            ("ms63600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms63600.dat", "ms63600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_BE0", 0x0000, 12, 6, 45, 10, 1, 50, 0, "br1520", "Sepith_8DCB", 30, 40, 20, 10,
        (
            ("ms65300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65300.dat", "ms65300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65300.dat", "ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_7F8", 0x0000, 12, 6, 45, 10, 1, 40, 0, "br1520", "Sepith_8DBB", 30, 40, 20, 10,
        (
            ("ms65200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_988", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1520", "Sepith_8DC3", 30, 40, 20, 10,
        (
            ("ms61300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_730", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_8D9B", 30, 40, 20, 10,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_B18", 0x0000, 12, 6, 45, 10, 1, 50, 0, "br1500", "Sepith_8DCB", 30, 40, 20, 10,
        (
            ("ms65300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65300.dat", "ms65300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65300.dat", "ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_CA8", 0x0000, 12, 6, 45, 0, 1, 0, 0, "br1520", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65300.dat", "ms65300.dat", "ms65300.dat", "ms65300.dat", "ms65300.dat", "ms65300.dat", "ms65300.dat", "ms65300.dat", "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7401", "ed7403", "ATBonus_630"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch20500.itc",                   # 00
        "apl/ch50166.itc",                   # 01
        "apl/ch50165.itc",                   # 02
        "chr/ch24200.itc",                   # 03
        "apl/ch50169.itc",                   # 04
        "apl/ch50164.itc",                   # 05
        "apl/ch50377.itc",                   # 06
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
    ))

    DeclNpc(-13489,  -6010,   -41110,  159,  385,  0x0, 0,   0,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(39619,   -6300,   -65120,  180,  405,  0x0, 0,   1,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(29520,   -6289,   -65250,  270,  405,  0x0, 0,   2,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-19620,  0,       -10680,  135,  389,  0x0, 0,   3,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(20459,   -6300,   -50159,  270,  405,  0x0, 0,   4,   0,   255, 255, 0,   34,  255,  0)
    DeclNpc(28489,   -6170,   -59029,  180,  405,  0x0, 0,   5,   0,   255, 255, 0,   35,  255,  0)
    DeclNpc(44099,   -5610,   -18569,  0,    439,  0x0, 0,   6,   0,   255, 255, 0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(38689,   -4500,   -53729,  0,    484,  0x0, 0,   26,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(4930,    10160,   0,       0x1010000,    "BattleInfo_A50", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-33140,  -4930,   0,       0x1010000,    "BattleInfo_8C0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-38450,  -31510,  -2800,   0x1010000,    "BattleInfo_8C0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-17540,  -38170,  -5600,   0x1010000,    "BattleInfo_BE0", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-5060,   -13330,  -6300,   0x1010000,    "BattleInfo_7F8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4200,    -20550,  -6300,   0x1010000,    "BattleInfo_988", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(2370,    -42510,  -6300,   0x1010000,    "BattleInfo_7F8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(19970,   -49310,  -6300,   0x1010000,    "BattleInfo_988", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(33630,   -23560,  -5600,   0x1010000,    "BattleInfo_7F8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(52410,   -28230,  -5600,   0x1010000,    "BattleInfo_988", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-38810,  -52060,  -4200,   0x1010000,    "BattleInfo_730", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-21590,  -49910,  -4200,   0x1010000,    "BattleInfo_730", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-30050,  -108200, -4900,   0x1010000,    "BattleInfo_A50", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-16070,  -108310, -5770,   0x1010000,    "BattleInfo_B18", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-15000,  -92180,  -5770,   0x1010000,    "BattleInfo_B18", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 25,  -37.0,                 -108.5,                -5.900000095367432,    225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.333333969116211,    10.850000381469727,    1.1800000667572021,    1.0])
    DeclEvent(0x0040, 0, 27,  -18.100000381469727,   -10.199999809265137,   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.262500047683716,     1.274999976158142,     0.20000000298023224,   1.0])

    DeclActor(38690,   -5500,   -53730,  1200,    38690,   -4500,   -53730,  0x007C, 0,  4,  0x0000)
    DeclActor(49800,   -5600,   -17450,  1200,    49800,   -4600,   -17450,  0x007C, 0,  5,  0x0000)
    DeclActor(-14500,  -5800,   -88320,  1200,    -14500,  -4800,   -88320,  0x007C, 0,  6,  0x0000)
    DeclActor(-24850,  0,       -2920,   1200,    -24850,  1000,    -2920,   0x007C, 0,  20, 0x0000)
    DeclActor(51410,   -6300,   -59200,  1200,    57770,   -5300,   -59100,  0x007C, 0,  18, 0x0000)
    DeclActor(-5450,   0,       11740,   1200,    -5450,   0,       11740,   0x007C, 0,  7,  0x0000)
    DeclActor(-37940,  -4200,   -50580,  1200,    -37940,  -4200,   -50580,  0x007C, 0,  8,  0x0000)
    DeclActor(-50120,  -4900,   -118170, 1200,    -50120,  -4900,   -118170, 0x007C, 0,  9,  0x0000)
    DeclActor(18070,   -6300,   -56430,  1200,    14290,   -6300,   -56430,  0x007C, 0,  19, 0x0000)

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
        "Function_0_E5C",          # 00, 0
        "Function_1_E7B",          # 01, 1
        "Function_2_F33",          # 02, 2
        "Function_3_1091",         # 03, 3
        "Function_4_15F1",         # 04, 4
        "Function_5_1804",         # 05, 5
        "Function_6_1951",         # 06, 6
        "Function_7_1A9E",         # 07, 7
        "Function_8_1AB2",         # 08, 8
        "Function_9_1AC6",         # 09, 9
        "Function_10_1ADA",        # 0A, 10
        "Function_11_1B95",        # 0B, 11
        "Function_12_1CB6",        # 0C, 12
        "Function_13_1DD7",        # 0D, 13
        "Function_14_1E6C",        # 0E, 14
        "Function_15_1F47",        # 0F, 15
        "Function_16_2528",        # 10, 16
        "Function_17_28DE",        # 11, 17
        "Function_18_2A3E",        # 12, 18
        "Function_19_2B4E",        # 13, 19
        "Function_20_2C22",        # 14, 20
        "Function_21_2CEE",        # 15, 21
        "Function_22_3352",        # 16, 22
        "Function_23_3588",        # 17, 23
        "Function_24_35E6",        # 18, 24
        "Function_25_37C1",        # 19, 25
        "Function_26_3E9B",        # 1A, 26
        "Function_27_4348",        # 1B, 27
        "Function_28_445C",        # 1C, 28
        "Function_29_4879",        # 1D, 29
        "Function_30_58FC",        # 1E, 30
        "Function_31_6F4A",        # 1F, 31
        "Function_32_6F77",        # 20, 32
        "Function_33_6FA4",        # 21, 33
        "Function_34_7352",        # 22, 34
        "Function_35_7CE9",        # 23, 35
        "Function_36_864D",        # 24, 36
        "Function_37_872B",        # 25, 37
        "Function_38_8A27",        # 26, 38
    ))


    def Function_0_E5C(): pass

    label("Function_0_E5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E7A")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_E5C")

    label("loc_E7A")

    Return()

    # Function_0_E5C end

    def Function_1_E7B(): pass

    label("Function_1_E7B")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_EBB"),
        (1, "loc_EC7"),
        (2, "loc_ED3"),
        (3, "loc_EDF"),
        (4, "loc_EEB"),
        (5, "loc_EF7"),
        (6, "loc_F03"),
        (SWITCH_DEFAULT, "loc_F0F"),
    )


    label("loc_EBB")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_F1B")

    label("loc_EC7")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_F1B")

    label("loc_ED3")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_F1B")

    label("loc_EDF")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_F1B")

    label("loc_EEB")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_F1B")

    label("loc_EF7")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_F1B")

    label("loc_F03")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F1B")

    label("loc_F0F")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F1B")

    label("loc_F1B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F32")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F1B")

    label("loc_F32")

    Return()

    # Function_1_E7B end

    def Function_2_F33(): pass

    label("Function_2_F33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE7")
    SetChrPos(0x9, 3350, -6300, -18380, 0)
    SetChrPos(0xA, 2660, -6300, -42330, 160)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8D")
    ClearChrFlags(0xE, 0x80)

    label("loc_F8D")

    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)

    label("loc_FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FFF")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    label("loc_FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_101C")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)

    label("loc_101C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1039")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)

    label("loc_1039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_104A")
    Event(0, 21)

    label("loc_104A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_105E")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 22)
    Jump("loc_1081")

    label("loc_105E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1072")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 24)
    Jump("loc_1081")

    label("loc_1072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_1081")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 26)

    label("loc_1081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_1090")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 13)

    label("loc_1090")

    Return()

    # Function_2_F33 end

    def Function_3_1091(): pass

    label("Function_3_1091")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A9")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_10A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1153")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xF1, 0xC2, 0xB1, 0x0, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x2)
    SetMapObjFlags(0x0, 0x400)
    SetMapObjFlags(0x0, 0x1000)
    OP_78(0x0, 0xF)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    SetChrPos(0xF, -58400, -4900, -105400, 285)
    OP_D3(0xF, 0x0, 0x45948, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x1E)

    label("loc_1153")

    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1175")
    Jump("loc_1194")

    label("loc_1175")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_118F")
    Jump("loc_1194")

    label("loc_118F")

    ModifyEventFlags(0, 1, 0x80)

    label("loc_1194")

    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B7")
    OP_70(0x1, 0x0)
    Jump("loc_13BB")

    label("loc_13B7")

    OP_70(0x1, 0x1E)

    label("loc_13BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13CE")
    OP_70(0x2, 0x0)
    Jump("loc_13D2")

    label("loc_13CE")

    OP_70(0x2, 0x1E)

    label("loc_13D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E5")
    OP_70(0x3, 0x0)
    Jump("loc_13E9")

    label("loc_13E5")

    OP_70(0x3, 0x1E)

    label("loc_13E9")

    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 4)), scpexpr(EXPR_END)), "loc_1453")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 25130, 2000, -11040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)
    Jump("loc_150A")

    label("loc_1453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 5)), scpexpr(EXPR_END)), "loc_14B1")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 25130, 2000, -11040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)
    Jump("loc_150A")

    label("loc_14B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 6)), scpexpr(EXPR_END)), "loc_150A")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 25130, 2000, -11040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x7, 0x1)

    label("loc_150A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_151C")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_151C")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 57770, -5300, -59100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15BA")
    OP_66(0x8, 0x1)
    PlayEffect(0x8, 0x7, 0xFF, 0x0, 14290, -6300, -56430, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_15BA")

    SoundDistance(0x7D, 0x8DF4, 0xFFFFEA20, 0xFA32, 0x15F90, 0x11170, 0x64, 0x0)
    OP_E1(0x3F52, 0xFFFFE976, 0xFFFE520A)
    OP_E1(0xFFFFF10A, 0xFFFFECDC, 0xFFFDF6AC)
    Return()

    # Function_3_1091 end

    def Function_4_15F1(): pass

    label("Function_4_15F1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BE")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16EC")
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x10, 0x0, 0)
    OP_98(0x10, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_164A():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_164A)

    def lambda_1664():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1664)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x10, 1)
    Battle("BattleInfo_CA8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_16CD"),
        (2, "loc_16DC"),
        (1, "loc_16E9"),
        (SWITCH_DEFAULT, "loc_16EC"),
    )


    label("loc_16CD")

    SetScenarioFlags(0x74, 1)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_16EC")

    label("loc_16DC")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_16E9")

    OP_B7(0x0)
    Return()

    label("loc_16EC")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E0, 1)"), scpexpr(EXPR_END)), "loc_1749")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_17B9")

    label("loc_1749")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5E0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5E0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17B9")

    Jump("loc_17F8")

    label("loc_17BE")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_17F8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_15F1 end

    def Function_5_1804(): pass

    label("Function_5_1804")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1900")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_1889")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_18FB")

    label("loc_1889")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18FB")

    Jump("loc_1945")

    label("loc_1900")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
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

    label("loc_1945")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1804 end

    def Function_6_1951(): pass

    label("Function_6_1951")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4D")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x82, 1)"), scpexpr(EXPR_END)), "loc_19D6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1A48")

    label("loc_19D6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A48")

    Jump("loc_1A92")

    label("loc_1A4D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
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

    label("loc_1A92")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1951 end

    def Function_7_1A9E(): pass

    label("Function_7_1A9E")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 4)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_1A9E end

    def Function_8_1AB2(): pass

    label("Function_8_1AB2")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1AB2 end

    def Function_9_1AC6(): pass

    label("Function_9_1AC6")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 6)
    OP_65(0x7, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_9_1AC6 end

    def Function_10_1ADA(): pass

    label("Function_10_1ADA")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0011
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
            "クロスベル市南口\x01",        # 0
            "聖ウルスラ医科大学\x01",      # 1
            "やめる\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6D")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1B8D")

    label("loc_1B6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8D")
    Call(0, 12)
    ClearMapFlags(0x8000000)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()

    label("loc_1B8D")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1ADA end

    def Function_11_1B95(): pass

    label("Function_11_1B95")

    Fade(1000)
    OP_68(-20430, 600, -680, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -25190, 0, -1760, 180)
    SetChrPos(0x1, -24640, 0, -460, 180)
    SetChrPos(0x2, -23960, 0, 1080, 180)
    SetChrPos(0x3, -23400, 0, 2850, 180)
    ClearChrFlags(0xF, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0xF)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xF, -29550, -10, -16070, 45)
    OP_D3(0xF, 0x0, 0xAFC8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1C70():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C70)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xF, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_11_1B95 end

    def Function_12_1CB6(): pass

    label("Function_12_1CB6")

    Fade(1000)
    OP_68(-22010, 600, -2420, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -25190, 0, -1760, 180)
    SetChrPos(0x1, -24640, 0, -460, 180)
    SetChrPos(0x2, -23960, 0, 1080, 180)
    SetChrPos(0x3, -23400, 0, 2850, 180)
    ClearChrFlags(0xF, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0xF)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xF, -6730, 0, 7220, 225)
    OP_D3(0xF, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1D91():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1D91)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xF, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_12_1CB6 end

    def Function_13_1DD7(): pass

    label("Function_13_1DD7")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -25540, 0, -2260, 225)
    SetChrPos(0x1, -25540, 0, -2260, 225)
    SetChrPos(0x2, -25540, 0, -2260, 225)
    SetChrPos(0x3, -25540, 0, -2260, 225)
    OP_68(-25540, 600, -2260, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_13_1DD7 end

    def Function_14_1E6C(): pass

    label("Function_14_1E6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED7")
    OP_93(0xFE, 0x9F, 0x0)

    #C0012
    ChrTalk(
        0xFE,
        "……水が気持ちいい……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "やっぱり街にいるより\x01",
            "街道を歩く方がいいね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F43")

    label("loc_1ED7")

    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0014
    ChrTalk(
        0xFE,
        (
            "あなたたちも\x01",
            "自然を求めて散策にきたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "バス使わないなんて、珍しいね。\x02",
    )

    CloseMessageWindow()

    label("loc_1F43")

    TalkEnd(0xFE)
    Return()

    # Function_14_1E6C end

    def Function_15_1F47(): pass

    label("Function_15_1F47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_20C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205C")

    #C0016
    ChrTalk(
        0xFE,
        (
            "……昨日遊撃士の人が\x01",
            "通りかかったんすよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "あのツインテールの女、\x01",
            "２２０リジュのパールグラスを\x01",
            "釣っていきやがってぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "忙しいからまた今度、\x01",
            "とか言って帰っていったんすよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "……何だったんすかねー。\x01",
            "相当の腕前だったっすけどー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20C2")

    label("loc_205C")


    #C0020
    ChrTalk(
        0xFE,
        (
            "あのツインテールの女、\x01",
            "何だったんすかねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "支部長なら何か知ってるかも\x01",
            "しれないっすけどー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C2")

    Jump("loc_2524")

    label("loc_20C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215B")

    #C0022
    ChrTalk(
        0xFE,
        (
            "特級釣師ロイドかー、\x01",
            "なるほど、中々やるっすねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "でも、オレも特級釣師っすから。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "負けてられないっすねー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21A8")

    label("loc_215B")


    #C0025
    ChrTalk(
        0xFE,
        (
            "昨日の釣り勝負は\x01",
            "接戦で負けたけどー。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        "次はこうはいかないっすから。\x02",
    )

    CloseMessageWindow()

    label("loc_21A8")

    Jump("loc_2524")

    label("loc_21AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2524")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_21EC")

    #C0027
    ChrTalk(
        0xFE,
        (
            "おっとぉ……\x01",
            "大物の予感っす！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2524")

    label("loc_21EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2324")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CB")

    #C0028
    ChrTalk(
        0xFE,
        (
            "え、ヨアヒムさんと\x01",
            "釣り勝負してるんっすか？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "まぁ、気を張らずに楽しむことっす。\x01",
            "釣りは使命感でやるもんじゃ\x01",
            "ないっすからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "……ちょっとかっこいい事を\x01",
            "言ってみたかっただけっす。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_231F")

    label("loc_22CB")


    #C0031
    ChrTalk(
        0xFE,
        (
            "まぁ、気を張らずに楽しむことっす。\x01",
            "釣りは使命感でやるもんじゃ\x01",
            "ないっすからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231F")

    Jump("loc_2524")

    label("loc_2324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2461")

    #C0032
    ChrTalk(
        0xFE,
        (
            "あ……警察の\x01",
            "ロイドさん達じゃないっすか。\x01",
            "ようやく皆さんも来たんすね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "フィッシャー杯とは、\x01",
            "釣公師団の名誉会長である\x01",
            "フィッシャー男爵を讃える大会っす。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "ただ大会と言っても、\x01",
            "競争というよりは\x01",
            "釣りを楽しむことが目的っすけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……さっき説明しそびれたから\x01",
            "一気に説明してみたっす。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2524")

    label("loc_2461")


    #C0036
    ChrTalk(
        0xFE,
        (
            "フィッシャー杯とは、\x01",
            "釣公師団の名誉会長である\x01",
            "フィッシャー男爵を讃える大会っす。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "大会と言っても、競争よりは\x01",
            "釣りを楽しむことが目的っすけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "でも今日だけは、オレもやる気っすよ。\x02",
    )

    CloseMessageWindow()

    label("loc_2524")

    TalkEnd(0xFE)
    Return()

    # Function_15_1F47 end

    def Function_16_2528(): pass

    label("Function_16_2528")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_26F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_25CF")

    #C0039
    ChrTalk(
        0xFE,
        "うーむ……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "やはり私の腕前は\x01",
            "道楽釣り師程度、という\x01",
            "ことでしょうかねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "悔しいですが、ぴくりとも\x01",
            "掛かる気配がありませんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26F2")

    label("loc_25CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2651")

    #C0042
    ChrTalk(
        0xFE,
        (
            "この辺りで大物が\x01",
            "釣れるはずなですがねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "うーむ……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "中々ヨアヒム師のように\x01",
            "うまくは行きませんねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26F2")

    label("loc_2651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_26F2")

    #C0045
    ChrTalk(
        0xFE,
        "お聞きになりました？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "昨日ヨアヒム団員が\x01",
            "この辺りで大物を釣り上げたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "ふう、私も負けていられません。\x01",
            "少しでも努力しませんとねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F2")

    Jump("loc_28DA")

    label("loc_26F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_28DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_27A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271E")
    Call(0, 17)
    Jump("loc_279F")

    label("loc_271E")


    #C0048
    ChrTalk(
        0xFE,
        (
            "……あれっ、いつのまにか\x01",
            "ヨアヒムさんがいなくなってる？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "おっかしいなぁ、\x01",
            "今日は仕事が休みだって\x01",
            "言いふらしてたのに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279F")

    Jump("loc_28DA")

    label("loc_27A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2841")

    #C0050
    ChrTalk(
        0xFE,
        (
            "ヨアヒムさんは釣公師団でも\x01",
            "なかなかの腕前でしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "医者という忙しい仕事の傍ら、\x01",
            "よく精進されているなあと\x01",
            "感心しているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DA")

    label("loc_2841")


    #C0052
    ChrTalk(
        0xFE,
        (
            "いやぁ、この中州で釣りをするのも\x01",
            "久しぶりだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "街道の釣りは魔獣のいないときを\x01",
            "見計らっていかないといけないから\x01",
            "なかなか出来ないんですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DA")

    TalkEnd(0xFE)
    Return()

    # Function_16_2528 end

    def Function_17_28DE(): pass

    label("Function_17_28DE")


    #C0054
    ChrTalk(
        0xFE,
        (
            "さっきヨアヒムさんに\x01",
            "小説を押し付けられたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "あまりに白々しいから\x01",
            "怪しいと思ってたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "どうもこっそりと\x01",
            "釣餌をくすねられてたみたいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#0006F（何してんだあの人は……）\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "あ、本には全然興味ないんで\x01",
            "よかったらコレ、もらってください。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2CB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2CB, 1)
    SetScenarioFlags(0x9C, 5)
    Return()

    # Function_17_28DE end

    def Function_18_2A3E(): pass

    label("Function_18_2A3E")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0060
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(54040, -5700, -57590, 1500)
    MoveCamera(45, 32, 0, 1500)
    OP_6E(430, 1500)
    SetCameraDistance(23500, 1500)
    Sleep(1000)
    SetChrName("")

    #A0061
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B49")
    OP_E0(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B27")
    MiniGame(0x6, 0x10, 0xC526, 0xFFFFE764, 0xFFFF18A2, 0x59, 0xE1AA, 0xFFFFEB4C, 0xFFFF1924)
    Jump("loc_2B49")

    label("loc_2B27")

    MiniGame(0x6, 0xC, 0xC526, 0xFFFFE764, 0xFFFF18A2, 0x59, 0xE1AA, 0xFFFFEB4C, 0xFFFF1924)

    label("loc_2B49")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_18_2A3E end

    def Function_19_2B4E(): pass

    label("Function_19_2B4E")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0062
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(13960, -5700, -56570, 1500)
    MoveCamera(45, 30, 0, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(19950, 1500)
    Sleep(1000)
    SetChrName("")

    #A0063
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C1D")
    OP_E0(0x2)
    MiniGame(0x6, 0xF, 0x4696, 0xFFFFE764, 0xFFFF2392, 0x10E, 0x37D2, 0xFFFFE764, 0xFFFF2392)

    label("loc_2C1D")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_19_2B4E end

    def Function_20_2C22(): pass

    label("Function_20_2C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2C88")
    TalkBegin(0xFF)
    SetChrName("")

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x02",
        )
    )

    CloseMessageWindow()

    #A0065
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
    Jump("loc_2CED")

    label("loc_2C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2C99")
    Call(0, 10)
    Jump("loc_2CED")

    label("loc_2C99")

    TalkBegin(0xFF)
    SetChrName("")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0067
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

    label("loc_2CED")

    Return()

    # Function_20_2C22 end

    def Function_21_2CEE(): pass

    label("Function_21_2CEE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(4900, 900, 29270, 0)
    MoveCamera(24, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(17800, 0)
    SetChrPos(0x101, 4050, 0, 29300, 180)
    SetChrPos(0x102, 5250, 0, 29300, 180)
    SetChrPos(0x103, 4050, 0, 30800, 180)
    SetChrPos(0x104, 5250, 0, 30800, 180)
    OP_68(4610, 900, 27270, 2500)

    def lambda_2D84():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D84)
    Sleep(50)

    def lambda_2DA1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2DA1)
    Sleep(60)

    def lambda_2DBE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2DBE)
    Sleep(70)

    def lambda_2DDB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2DDB)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    #C0068
    ChrTalk(
        0x101,
        "#0006F#5Pふう……\x02",
    )

    CloseMessageWindow()

    def lambda_2E2B():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E2B)

    def lambda_2E38():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E38)

    def lambda_2E45():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2E45)

    def lambda_2E52():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2E52)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    #C0069
    ChrTalk(
        0x101,
        (
            "#0001F#6P遊撃士協会の新顔#4Rニューフェイス#、\x01",
            "エステルとヨシュアか……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#0106F#12P……なんだか思わず\x01",
            "溜息が出てしまうわね……\x02\x03",

            "#0101F私たちと同い年くらいだけど\x01",
            "相当、高位の遊撃士なのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0306F#11Pああ、間違いねぇだろ。\x02\x03",

            "#0301Fあの身のこなしと技のキレ……\x01",
            "かなりの修羅場をくぐってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        (
            "#0203F#5Pそうですね……\x01",
            "わたしたちが苦労した魔獣を\x01",
            "あっという間でしたし。\x02\x03",

            "#0200F今後はあの人たちも\x01",
            "商売敵になるわけですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#0008F#6Pそうだな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    #C0074
    ChrTalk(
        0x101,
        (
            "#0004F#6P──落ち込んでも仕方ない。\x01",
            "俺たちは俺たちで頑張ればいいさ。\x02\x03",

            "#0000Fそれに商売敵というより\x01",
            "いいライバルって考えておこう。\x02\x03",

            "その方がやる気が出てこないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_314C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_314C)

    def lambda_3159():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3159)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0075
    ChrTalk(
        0x103,
        (
            "#0211F#5P……ライバルというには\x01",
            "実力差がありすぎる気が……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#0304F#11Pま、それでもあの\x01",
            "アリオスってオッサンよりは\x01",
            "まだ追いつけそうではあるかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        "#0100F#11Pうーん、それは確かに……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#0004F#6Pまあ、気の持ちようってことさ。\x02\x03",

            "#0000Fせっかくの彼らの好意だ。\x01",
            "このまま病院まで行かせてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        (
            "#0206F#5Pまた徒歩ですけど……\x01",
            "まあ、仕方ない展開ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#0102F#11Pふふ、せいぜい少しでも\x01",
            "身体を鍛えておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18300, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5000, 0, 29400, 180)
    SetScenarioFlags(0x61, 5)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_21_2CEE end

    def Function_22_3352(): pass

    label("Function_22_3352")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xF)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xF, -28200, -4900, -102400, 0)
    OP_D3(0xF, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xF1, 0xC2, 0xB1, 0x0, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")
    ClearChrFlags(0xF, 0x4)
    FadeToBright(1000, 0)
    OP_68(-39300, -8300, -105090, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(42630, 0)
    OP_68(-26300, -5300, -94050, 12000)
    BeginChrThread(0xF, 3, 0, 23)
    OP_0D()
    Sleep(6300)
    Fade(1000)
    EndChrThread(0xF, 0x3)
    EndChrThread(0xF, 0x2)
    EndChrThread(0xF, 0x1)
    OP_68(-13410, -4300, -29940, 0)
    MoveCamera(62, 14, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(44090, 0)
    OP_68(-13410, -1300, -29940, 6000)
    SetCameraDistance(34090, 6000)
    Sleep(1000)
    SetChrPos(0xF, -28420, -4200, -50490, 0)

    def lambda_34C7():
        OP_95(0xFE, -28280, 0, -16570, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_34C7)
    Sound(465, 0, 100, 0)
    OP_0D()
    Sleep(5000)
    Fade(1000)
    EndChrThread(0xF, 0x1)
    OP_68(-11620, -4300, -8150, 0)
    MoveCamera(31, 23, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(57130, 0)
    OP_68(-11620, -1600, -8150, 5000)
    Sound(471, 0, 100, 0)
    SetChrPos(0xF, -23750, 0, -9730, 0)

    def lambda_354A():
        OP_95(0xFE, 1980, 0, 15000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_354A)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xF, 0x1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("e0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_3352 end

    def Function_23_3588(): pass

    label("Function_23_3588")

    SetChrPos(0xFE, -65379, -4900, -109290, 0)

    def lambda_359E():
        OP_95(0xFE, -41340, -4900, -109460, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_359E)
    Sound(469, 0, 100, 0)
    Sleep(4000)
    EndChrThread(0xFE, 0x1)

    def lambda_35C5():
        OP_9E(0xFE, 0xFFFF5E84, 0xFFFE8734, 0xFFFEA070, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_35C5)
    Sound(458, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_3588 end

    def Function_24_35E6(): pass

    label("Function_24_35E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-28200, 600, -14200, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xF)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xF, -28200, 0, -14200, 180)
    OP_D3(0xF, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_371E")
    Sound(471, 0, 100, 0)
    FadeToBright(1000, 0)
    SetChrPos(0xF, -890, 0, 10890, 225)

    def lambda_36B3():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_36B3)
    OP_68(-5600, -350, 2290, 0)
    MoveCamera(33, 11, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(52930, 0)
    OP_68(-5600, -2850, 2290, 6000)
    OP_0D()
    Sleep(1000)
    Sound(465, 0, 100, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xF, 0x1)

    label("loc_371E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37B4")
    Fade(1000)
    SetChrPos(0xF, -28500, -830, -21530, 0)
    OP_68(-6650, -950, -31510, 0)
    MoveCamera(54, 12, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(37610, 0)
    OP_68(-19030, -950, -31410, 10000)
    OP_0D()
    Sleep(2000)

    def lambda_3787():
        OP_95(0xFE, -27920, -4200, -50960, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3787)
    Sound(458, 0, 100, 0)
    Sleep(4500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xF, 0x1)

    label("loc_37B4")

    SetScenarioFlags(0x5C, 1)
    NewScene("e0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_35E6 end

    def Function_25_37C1(): pass

    label("Function_25_37C1")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(-38620, -4300, -107290, 0)
    MoveCamera(31, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20160, 0)
    SetChrPos(0x101, -36290, -4900, -108440, 270)
    SetChrPos(0x102, -35800, -4900, -109620, 270)
    SetChrPos(0x103, -34460, -4900, -107100, 270)
    SetChrPos(0x104, -33640, -4900, -108220, 270)
    FadeToBright(1000, 0)
    SetCameraDistance(19160, 2000)

    def lambda_38A5():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38A5)
    Sleep(50)

    def lambda_38BD():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38BD)
    Sleep(50)

    def lambda_38D5():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_38D5)
    Sleep(50)

    def lambda_38ED():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_38ED)
    WaitChrThread(0x101, 1)
    OP_0D()
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

    #C0081
    ChrTalk(
        0x101,
        "#0007F#11Pあ……！\x02",
    )

    CloseMessageWindow()
    OP_68(-57020, -4100, -107490, 3500)
    SetCameraDistance(19000, 3500)
    Sleep(3500)
    SetChrPos(0x101, -48030, -4900, -109440, 270)
    SetChrPos(0x102, -48470, -4900, -111260, 270)
    SetChrPos(0x103, -46230, -4900, -111130, 270)
    SetChrPos(0x104, -46260, -4900, -109630, 270)
    SetCameraDistance(20000, 2000)

    def lambda_39F5():
        OP_95(0xFE, -57800, -4900, -108900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39F5)

    def lambda_3A0F():
        OP_95(0xFE, -58240, -4900, -111000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A0F)

    def lambda_3A29():
        OP_95(0xFE, -56460, -4900, -111100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A29)

    def lambda_3A43():
        OP_95(0xFE, -56720, -4900, -109480, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A43)
    WaitChrThread(0x101, 1)

    def lambda_3A61():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A61)
    WaitChrThread(0x102, 1)

    def lambda_3A72():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A72)
    WaitChrThread(0x103, 1)

    def lambda_3A83():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A83)
    WaitChrThread(0x104, 1)

    def lambda_3A94():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A94)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0082
    ChrTalk(
        0x102,
        (
            "#0105F#12Pど、どうして\x01",
            "こんな場所に停車を……\x02\x03",

            "#0101Fそれに……\x01",
            "誰も乗っていないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        "#0301F#12Pそうみてぇだな……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0084
    ChrTalk(
        0x104,
        (
            "#0301F#5Pティオすけ、\x01",
            "周囲の反応はどうだ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B64():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B64)
    Sleep(50)

    def lambda_3B74():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B74)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0085
    ChrTalk(
        0x103,
        "#0201F#12Pはい……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)
    Sound(1278, 255, 100, 0)    #voice#Tio
    Sleep(800)
    VolumeBGM(0x3C, 0x3E8)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Fade(250)
    OP_24(0x348)
    Sound(820, 0, 100, 0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)

    #C0086
    ChrTalk(
        0x103,
        (
            "#0206F#12P……ダメです。\x02\x03",

            "#0201F周囲１０セルジュに\x01",
            "人の反応はありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#0303F#5Pチッ……\x01",
            "だろうと思ったぜ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0088
    ChrTalk(
        0x104,
        (
            "#0301F#11Pどうやら魔獣に襲われたって\x01",
            "雰囲気でも無さそうだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#0003F#5Pああ……\x01",
            "ちゃんと路肩に停車している。\x02\x03",

            "#0008F多分、運転手が自分の意志で\x01",
            "こちらに寄せて停車したんだろう。\x02\x03",

            "もしくは停車せざるを得ない\x01",
            "何らかの事態が発生したのか……\x02\x03",

            "#0001Fこのまま中も調べてみよう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0090
    ChrTalk(
        0x102,
        "#0101F#6Pええ……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x348)
    SetScenarioFlags(0x5C, 2)
    NewScene("e0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_37C1 end

    def Function_26_3E9B(): pass

    label("Function_26_3E9B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    OP_68(-56490, -3100, -107870, 0)
    MoveCamera(31, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19160, 0)
    SetChrPos(0x101, -56790, -4900, -110680, 180)
    SetChrPos(0x102, -58500, -4900, -109250, 180)
    SetChrPos(0x103, -56840, -4900, -108730, 180)
    SetChrPos(0x104, -55360, -4900, -108810, 180)
    TurnDirection(0x102, 0x101, 0)
    TurnDirection(0x103, 0x101, 0)
    TurnDirection(0x104, 0x101, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x7)
    FadeToBright(1000, 0)
    OP_68(-56490, -4100, -107870, 3000)
    OP_6F(0x79)
    OP_0D()

    #C0091
    ChrTalk(
        0x101,
        (
            "#0003F#5Pはい、はい……\x02\x03",

            "#0013F……分かりました。\x01",
            "連絡の方はお願いします。\x02\x03",

            "こちらはこのまま\x01",
            "ウルスラ病院に向かいます。\x02\x03",

            "#0003F──はい。\x01",
            "くれぐれも気をつけます。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(807, 0, 100, 0)
    SetChrSubChip(0x101, 0x6)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0092
    ChrTalk(
        0x103,
        "#0201F#5P……課長はなんと？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0093
    ChrTalk(
        0x101,
        (
            "#0006F#12Pとりあえずタングラム門に\x01",
            "連絡をしてくれるみたいだ。\x02\x03",

            "#0000Fソーニャ副司令に\x01",
            "協力を要請してみるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#0100F#5Pそう……\x01",
            "ちょっと助かるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#0300F#11Pああ、副司令だったら\x01",
            "必ず力になってくれんだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        (
            "#0200F#5Pとりあえずわたしたちは\x01",
            "このまま病院ですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#0003F#12Pああ、ここから病院まで\x01",
            "もうそんなに離れていない。\x02\x03",

            "#0001Fひょっとしたら乗客が歩いて\x01",
            "病院に向かった可能性もある。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#0306F#11Pま、見舞いの品を置いてる時点で\x01",
            "タダ事じゃなさそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#0101F#5Pとにかく急ぎましょう。\x01",
            "すぐに日が落ちてしまうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#0013F#12Pああ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()
    OP_D5(0x1E)
    OP_37()
    OP_68(-58000, -4300, -108800, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, -58000, -4900, -108800, 270)
    SetChrPos(0x1, -58000, -4900, -108800, 270)
    SetChrPos(0x2, -58000, -4900, -108800, 270)
    SetChrPos(0x3, -58000, -4900, -108800, 270)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE0, 2)
    OP_29(0x4D, 0x1, 0x2)
    Sleep(500)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_26_3E9B end

    def Function_27_4348(): pass

    label("Function_27_4348")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4458")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F9")

    #C0101
    ChrTalk(
        0x101,
        (
            "#0000F……おっと。\x02\x03",

            "補給のために中州から出るのは\x01",
            "禁止ってルールだったな。\x02\x03",

            "ヨアヒム先生を連れ戻すためにも\x01",
            "正々堂々、勝負しないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_443C")

    label("loc_43F9")


    #C0102
    ChrTalk(
        0x101,
        (
            "#0000F釣り勝負に勝つまでは\x01",
            "中州を出て行くわけには行かないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_443C")

    Sleep(50)
    SetChrPos(0x0, -17740, -1390, -15870, 156)
    EventEnd(0x4)
    Return()

    label("loc_4458")

    Call(0, 28)
    Return()

    # Function_27_4348 end

    def Function_28_445C(): pass

    label("Function_28_445C")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    OP_E0(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-18840, 600, -8900, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(21100, 0)
    SetChrPos(0x101, -18810, 0, -10540, 180)
    SetChrPos(0x102, -18810, 0, -9120, 180)
    SetChrPos(0x103, -20390, 0, -10540, 180)
    SetChrPos(0x104, -20390, 0, -9120, 180)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0103
    ChrTalk(
        0x101,
        "#11P#0005Fあれは……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(800)
    OP_68(6610, -5700, -12400, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(21000, 0)
    OP_68(3620, -5700, -17770, 3000)
    MoveCamera(34, 21, 0, 3000)
    Sleep(4000)
    Fade(800)
    OP_68(3180, -5430, -35010, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    OP_68(3460, -5430, -41130, 2600)
    MoveCamera(21, 23, 0, 2600)
    Sleep(3600)
    Fade(800)
    OP_68(21620, -5700, -48780, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(24500, 0)
    SetCameraDistance(19500, 2600)
    Sleep(3600)
    Fade(800)
    OP_68(44800, -5000, -18700, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(27000, 0)
    SetCameraDistance(26000, 2800)
    OP_63(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(3600)
    Fade(800)
    OP_68(-18200, 600, -10810, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(21100, 0)
    OP_0D()

    #C0104
    ChrTalk(
        0x104,
        "#5P#0300Fおーおー、楽しんでるねぇ。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        (
            "#5P#0106F街道には魔獣も出るでしょうに、\x01",
            "たくましい人達ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x103,
        (
            "#6P#0200F……今は不思議と\x01",
            "魔獣はいないようですが。\x02\x03",

            "釣り大会の熱気で\x01",
            "逃げてしまったとか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#12P#0005Fさ、さすがにそれはないと思うけど。\x02\x03",

            "#0003Fとにかく……\x01",
            "ここが例の釣り大会の会場なのは\x01",
            "間違いなさそうだ。\x02\x03",

            "#0000Fヨアヒム先生を探してみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xBD, 3)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_28_445C end

    def Function_29_4879(): pass

    label("Function_29_4879")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    OP_E0(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(45080, -5000, -18980, 0)
    MoveCamera(43, 16, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 44540, -5600, -20590, 0)
    SetChrPos(0x102, 43130, -5600, -20590, 0)
    SetChrPos(0x103, 43130, -5600, -22300, 0)
    SetChrPos(0x104, 44540, -5600, -22300, 0)
    LoadChrToIndex("chr/ch07100.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02400.itp")
    FadeToBright(1000, 0)
    OP_0D()

    #N0108
    NpcTalk(
        0xE,
        "白衣の男",
        (
            "#5P#2400Fフンフフーン……\x02\x03",

            "いやぁ、やっぱり釣りはいいね。\x01",
            "糸を垂らしているだけで\x01",
            "心が洗われるというか……\x02\x03",

            "病院勤めで疲れた体も\x01",
            "リフレッシュするというものだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#12P#0003F（青い髪で白衣の男性……\x01",
            "  うん、後姿から見ても間違いないな。）\x02\x03",

            "#0001Fあの……\x01",
            "ヨアヒム先生、ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xE,
        (
            "#2400F#5Pん～……いかにも僕は\x01",
            "ヨアヒムという者だが……\x02\x03",

            "#2403F悪いけど、今ちょっと\x01",
            "手が離せないんだ。\x02\x03",

            "#2401F用件はなにか……なっと！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 1, 0, 31)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0111
    ChrTalk(
        0xE,
        "#2405F#5Pおお、来た……！！\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#12P#0006F#5Pま、まるで聞いちゃいないな。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 1, 0, 32)

    #C0113
    ChrTalk(
        0xE,
        (
            "#2401F#5P聞いてる、聞いているよ。\x01",
            "そして、引いているよっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        "#12P#0206F（寒い……）\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#12P#0006Fえ、えっとですね！\x02\x03",

            "#0001Fウルスラ病院のセラさんから\x01",
            "依頼を受けて、\x01",
            "先生を探していたんです！\x02\x03",

            "ヨアヒム先生がいなくて、\x01",
            "リットンさんや病院の皆さんが\x01",
            "困っているんですよ！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0xE, 0x1)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0116
    ChrTalk(
        0xE,
        "#2400F来たぁ！！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x2)
    Sleep(200)
    SetChrSubChip(0xE, 0x3)
    Sleep(200)
    Sound(11, 0, 100, 0)
    SetChrSubChip(0xE, 0x4)
    Sleep(200)
    SetChrSubChip(0xE, 0x5)
    Sleep(150)
    SetChrSubChip(0xE, 0x6)
    Sleep(150)
    SetChrSubChip(0xE, 0x7)
    Sleep(1000)

    #C0117
    ChrTalk(
        0xE,
        (
            "#2405F#5Pおお～……『バイパーヘッド』……\x01",
            "まずまずのサイズじゃないか。\x02\x03",

            "#2400Fうんうん、日々病院を抜けて\x01",
            "練習に励んでいる甲斐があったなぁ。\x02",
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
    Sleep(1200)

    #C0118
    ChrTalk(
        0x104,
        (
            "#12P#0306Fなんつぅマイペースな……\x02\x03",

            "#0301Fつかもう、話なんか\x01",
            "完全に聞いてねぇだろこれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        (
            "#6P#0106Fはぁ……ロイド。\x01",
            "もう一度説明しなきゃだめみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#12P#0006F（せ、せっかく大声出したのに……）\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(300)

    #C0121
    ChrTalk(
        0xE,
        (
            "#2403F#5P……いや、それには及ばないよ。\x02\x03",

            "#2400Fウルスラ病院で\x01",
            "皆が僕の帰りを待っている。\x01",
            "……そういう話だろう？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0xE, 0x2)
    ClearChrFlags(0xE, 0x20)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    OP_64(0xE)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_93(0xE, 0xB4, 0x190)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0122
    AnonymousTalk(
        0xE,
        (
            "どうも初めまして。\x01",
            "僕の名前はヨアヒム・ギュンター。\x02\x03",

            "ウルスラ病院で\x01",
            "准教授なんかをやってる者さ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0123
    ChrTalk(
        0xE,
        (
            "#2405F#5Pってあれ？\x01",
            "君たちどこかで見たことが……\x02\x03",

            "#2403Fうーん、これはデジャヴ？\x01",
            "……だとすれば僕の知る所ではないね、\x01",
            "うんうん。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#12P#0006Fいえ、デジャヴではなく……\x01",
            "（もう自己紹介した方が早いかな。）\x02\x03",

            "#0001Fえっと……自分は\x01",
            "クロスベル警察・特務支援課の\x01",
            "ロイド・バニングスです。\x02\x03",

            "#0003Fとにかくヨアヒム先生には……！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xE,
        (
            "#2409F#5Pまぁまぁ、良いじゃないか。\x01",
            "とりあえず事情は理解したからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#6P#0100Fそれじゃあ……\x01",
            "病院に戻っていただけるんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xE,
        (
            "#2403F#5Pん～……どうしたらいいと思うね？\x02\x03",

            "#2400F僕としてはこのフィッシャー杯は、\x01",
            "先々月あたりから楽しみにしていた\x01",
            "一大イベントでね。\x02\x03",

            "#2406F記念祭中に休みもなさそうだし、\x01",
            "今のうちに楽しみたいんだがねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        "#12P#0211F……医者の責任感とか無いんですか？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xE,
        (
            "#2400F#5P無いといえば嘘になるな。\x02\x03",

            "#2406F先月末も抜け出した回数分の\x01",
            "始末書を書かされて大変だったんだ。\x02\x03",

            "半分はリットン君が持ってくれたので\x01",
            "なんとか終わったんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#12P#0006F話がズレてきてるし……\x02\x03",

            "#0001Fあの、じゃあどうしたら\x01",
            "病院に戻ってくれますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xE,
        (
            "#2403F#5Pそうだなぁ……\x02\x03",

            "#2400Fせっかくのフィッシャー杯……\x01",
            "よければコイツで勝負してみないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#12P#0005F魚釣り……？\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xE,
        (
            "#2409F#5Pその通り。\x02\x03",

            "#2400Fもし君たちが、さっき僕が釣り上げた\x01",
            "『バイパーヘッド』よりも大物を\x01",
            "釣り上げたなら、僕は病院へ戻ろう。\x02\x03",

            "#2409Fシンプルでいいだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#12P#0303F釣り勝負ってやつか……\x01",
            "どうするんだ、ロイド？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#12P#0001F……分かりました、受けて立ちます。\x01",
            "詳しいルールを教えてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xE,
        (
            "#2409F#5Pそうこなくっちゃ。\x02\x03",

            "#2400Fあとで僕は、セルダン支部長に\x01",
            "先程の『バイパーヘッド』を見てもらう。\x02\x03",

            "君たちも魚を釣ったら、\x01",
            "セルダン支部長に見せてみてくれ。\x02\x03",

            "その魚が僕の釣り上げた\x01",
            "『バイパーヘッド』より大物なら、\x01",
            "君たちの勝ちだ。\x02\x03",

            "ただし……\x01",
            "支部長に見せられるのは一回限り。\x01",
            "魚の種類はこの釣り場で釣れるもののみ。\x02\x03",

            "補給や、他所の釣り場に行くために\x01",
            "中州から出るのは禁止とする。\x02\x03",

            "#2409F……そんなところでどうかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#12P#0001F……了解しました。\x01",
            "そのルールで勝負しましょう。\x02\x03",

            "#0003F（……エサ、足りるかな……\x01",
            "  他の団員を頼ってみるのも\x01",
            "  ありかもしれない。）\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xE,
        (
            "#2400F#5Pでは、早速始めるとしよう！\x02\x03",

            "#2409Fふふ、まぁ健闘を祈るよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(43950, -5000, -20620, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, 43950, -5600, -20620, 0)
    SetChrPos(0x1, 43950, -5600, -20620, 0)
    SetChrPos(0x2, 43950, -5600, -20620, 0)
    SetChrPos(0x3, 43950, -5600, -20620, 0)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xE, 0x20)
    OP_93(0xE, 0x0, 0x0)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    ClearScenarioFlags(0x0, 1)
    ModifyEventFlags(1, 1, 0x80)
    OP_29(0x16, 0x1, 0x2)
    Sleep(500)
    OP_37()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_29_4879 end

    def Function_30_58FC(): pass

    label("Function_30_58FC")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    OP_E0(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_68(30260, -4900, -35640, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(710, 0)
    SetCameraDistance(14090, 0)
    SetChrPos(0x101, 30680, -5600, -37020, 315)
    SetChrPos(0xE, 28940, -5600, -35260, 135)
    SetChrPos(0xD, 31010, -5600, -34670, 225)
    SetChrPos(0x102, 32000, -5600, -39360, 0)
    SetChrPos(0x103, 30860, -5600, -39370, 0)
    SetChrPos(0x104, 29730, -5600, -39380, 0)
    LoadChrToIndex("chr/ch07100.itc", 0x1E)
    LoadChrToIndex("chr/ch32200.itc", 0x1F)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x2)
    ClearChrFlags(0xE, 0x20)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6838")

    #C0139
    ChrTalk(
        0xE,
        (
            "#2400F#5Pフッフッフ……\x01",
            "満足のいく魚が釣れたかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#12P#0001Fまだ分かりませんが……\x01",
            "負けたつもりはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xE,
        "#2409F#5Pほほう、それは楽しみだ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 300)
    TurnDirection(0x101, 0xD, 300)
    Sleep(300)

    #C0142
    ChrTalk(
        0xE,
        (
            "#2400F#5Pそれでは、セルダン支部長。\x01",
            "判定をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xD,
        "#11Pうむ。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xD,
        (
            "#11Pヨアヒム団員の釣り上げたのは……\x01",
            "『バイパーヘッド』だったな。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)

    #C0145
    ChrTalk(
        0xD,
        "#11P判定の結果は……\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)
    Sleep(300)

    #C0146
    ChrTalk(
        0x101,
        "#12P#0001F（ゴクリ……）\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_607A")
    OP_2C(0x16, 0x3)
    OP_29(0x16, 0x1, 0x5)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0147
    ChrTalk(
        0xD,
        "#5S#11P……勝者、ロイド団員！\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0148
    ChrTalk(
        0xE,
        (
            "#2405F#5Pな、なんだって？\x01",
            "何かの間違いでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xD,
        (
            "#11Pいや……確かにロイド君の\x01",
            "釣った魚のほうが、はるかに大物だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xD,
        "#11Pこの俺の目に間違いはない！\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xE,
        "#2406F#5Pそ、そんな～。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        "#12P#0109Fやったわね、ロイド！\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        "#12P#0309Fおお、大したもんだぜ！\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        "#12P#0202F普通にすごいです。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#12P#0005Fや、やった……のか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    #C0156
    ChrTalk(
        0xE,
        (
            "#2406F#5Pふぅ……完敗か。\x02\x03",

            "#2400Fおっと、そうだ。\x01",
            "勝利を讃えて、君たちには\x01",
            "これをプレゼントしよう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 300)
    OP_95(0xE, 29970, -5600, -36340, 1000, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1FC, 1)
    OP_96(0xE, 0x710C, 0xFFFFEA20, 0xFFFF7644, 0x3E8, 0x0)
    Sleep(200)

    #C0158
    ChrTalk(
        0x101,
        (
            "#12P#0005Fえっ……いいんですか？\x01",
            "じゃあ、ありがたく貰っておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xE,
        (
            "#2400F#5Pさて……それじゃあ僕は\x01",
            "約束どおり病院に戻るとするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0160
    ChrTalk(
        0x102,
        (
            "#12P#0105Fな、なんだか意外ですね。\x01",
            "もう少し駄々をこねるのかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xE,
        (
            "#2406F#5Pおいおい……\x01",
            "子どもじゃないんだからさ。\x02\x03",

            "#2400Fま、勝負を持ちかけたおかげで\x01",
            "充分に釣りを楽しめたし……\x02\x03",

            "#2409F今回は大満足と言えるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#12P#0005Fえっ……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6833")

    label("loc_607A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_649C")
    OP_29(0x16, 0x1, 0x4)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0163
    ChrTalk(
        0xD,
        "#5S#11P……勝者、なし！\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0164
    ChrTalk(
        0xE,
        "#2405F#5Pな、なんですって？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        "#12P#0005F勝者……なし？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xD,
        (
            "#11Pうむ、俺も目を凝らして\x01",
            "丁寧に丁寧に計ったのだが……\x01",
            "奇跡的に、全く同じサイズだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xD,
        "#11Pまぁ、要するに引き分けだ。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        "#12P#0006Fそ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xE,
        (
            "#2406F#5Pなんともはや……\x01",
            "微妙な結果に落ち着いたものだね。\x02\x03",

            "やるからには勝敗を\x01",
            "きっちり決める主義なんだが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 300)
    Sleep(300)

    #C0170
    ChrTalk(
        0x101,
        (
            "#12P#0011Fえ、えーっと……\x01",
            "さっきの約束の件なんですけど。\x02\x03",

            "……この場合、どうしましょう？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    #C0171
    ChrTalk(
        0xE,
        (
            "#2406F#5P……ま、いいだろう。\x01",
            "そろそろ病院に戻るとしようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0172
    ChrTalk(
        0x101,
        "#12P#0005Fや、やけにあっさりしてますね……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#12P#0105Fほんと。\x01",
            "もう少し駄々をこねるのかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xE,
        (
            "#2406F#5Pおいおい……\x01",
            "子どもじゃないんだからさ。\x02\x03",

            "#2400Fま、引き分けにはなったが\x01",
            "充分に釣りを楽しめたし……\x01",
            "いいってことさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        "#12P#0005Fえっ……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6833")

    label("loc_649C")

    OP_29(0x16, 0x1, 0x3)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0176
    ChrTalk(
        0xD,
        "#5S#11P……勝者、ヨアヒム団員！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0177
    ChrTalk(
        0x101,
        "#12P#0006Fそ、そんな……！\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xD,
        (
            "#11P……確かにヨアヒム君の\x01",
            "釣った魚のほうが、はるかに大物だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xD,
        "#11Pこの俺の目に間違いはない！\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#12P#0003Fくそっ……\x01",
            "釣り方が悪かったのか……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    #C0181
    ChrTalk(
        0xE,
        (
            "#2409F#5Pフッフッフ……\x01",
            "今一歩届かなかったようだね。\x02\x03",

            "#2403Fまぁ、気を落とさないことだよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 300)
    Sleep(300)

    #C0182
    ChrTalk(
        0x101,
        (
            "#12P#0005Fは、はぁ……\x02\x03",

            "#0006F（任務失敗か……\x01",
            "  セラさんになんて説明すれば……）\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xE,
        (
            "#2400F#5Pさぁて、勝負も楽しんだことだし……\x01",
            "そろそろ病院に戻るとするかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0184
    ChrTalk(
        0x101,
        "#12P#0005F……へっ？\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        (
            "#12P#0105F……あ、あの。\x01",
            "私たちが勝負に勝ったらという\x01",
            "話だったのでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xE,
        (
            "#2403F#5Pん～、そんなこと言ったかね？\x02\x03",

            "#2409F僕は病院に戻らないなんて\x01",
            "一度も言ってないと思うけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6833")

    Jump("loc_6BAC")

    label("loc_6838")


    #C0187
    ChrTalk(
        0xE,
        (
            "#2400F#5Pフッフッフ……\x01",
            "満足のいく魚が釣れたかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        "#12P#0006Fあの……それなんですけど……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xD,
        "#11P実はな、ヨアヒム団員。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xD,
        (
            "#11P彼らはどうやら今日、\x01",
            "全くの坊主だったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xD,
        (
            "#11Pだから今回の勝負は\x01",
            "ギブアップしたいそうなのだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0192
    ChrTalk(
        0xE,
        (
            "#2405F#5Pええっ、そうなのかい？\x02\x03",

            "#2403Fう、うーん。\x01",
            "なんだか拍子抜けしちゃったなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        (
            "#12P#0006Fす、すみません……\x01",
            "どうも釣りの調子が悪くて。\x02\x03",

            "（任務失敗か……\x01",
            "  セラさんになんて説明すれば……）\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xE,
        (
            "#2403F#5Pふーん……\x01",
            "ま、そういう時もあるか。\x02\x03",

            "#2400Fまぁいいや。\x01",
            "充分楽しんだことだし……\x01",
            "そろそろ病院に戻るとするかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0195
    ChrTalk(
        0x101,
        "#12P#0005F……へっ？\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        (
            "#12P#0105F……あ、あの。\x01",
            "私たちが勝負に勝ったらという\x01",
            "話だったのでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xE,
        (
            "#2400F#5Pん～、そんなこと言ったかね？\x02\x03",

            "#2409F僕は病院に戻らないなんて\x01",
            "一度も言ってないと思うけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BAC")


    #C0198
    ChrTalk(
        0x104,
        (
            "#12P#0306Fこの先生……\x01",
            "単に楽しく釣りをする時間を\x01",
            "稼いでただけなんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x103,
        "#12P#0211F……そんな気がします。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xE,
        "#2400F#5Pフフ、何の事やら分かりかねるよ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 300)
    Sleep(300)

    #C0201
    ChrTalk(
        0xE,
        (
            "#2403F#5P……セルダン支部長、そういうわけで。\x01",
            "僕はこれで失礼します。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xD,
        (
            "#11Pそうか。\x01",
            "次回の参加も待っているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xE,
        "#2409F#5Pはは、よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    OP_95(0xD, 34960, -5600, -41280, 2000, 0x0)
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    #C0204
    ChrTalk(
        0xE,
        (
            "#2400F#5P……さ、特務支援課の皆さん。\x01",
            "病院に帰ろうじゃないか。\x02\x03",

            "近くにバス停があったはずだから\x01",
            "先に行ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D9B():

        label("loc_6D9B")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_6D9B")

    QueueWorkItem2(0x0, 1, lambda_6D9B)

    def lambda_6DAD():

        label("loc_6DAD")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_6DAD")

    QueueWorkItem2(0x0, 1, lambda_6DAD)

    def lambda_6DBF():

        label("loc_6DBF")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_6DBF")

    QueueWorkItem2(0x0, 1, lambda_6DBF)

    def lambda_6DD1():

        label("loc_6DD1")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_6DD1")

    QueueWorkItem2(0x0, 1, lambda_6DD1)
    OP_95(0xE, 25590, -5600, -32140, 2000, 0x0)
    OP_95(0xE, 19610, -5600, -32180, 2000, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    #C0205
    ChrTalk(
        0x104,
        (
            "#12P#0306Fなんつーか……\x01",
            "散々振り回された感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        "#12P#0106Fそうね……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        (
            "#12P#0200F……わたしたちも急いだ方が\x01",
            "良いのでは？\x02\x03",

            "#0206F目を離すとまた\x01",
            "逃げられるかもしれませんし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0208
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそ、そうだな。\x01",
            "ヨアヒム先生と同じバスで\x01",
            "病院に戻るとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    ClearMapFlags(0x8000000)
    SetScenarioFlags(0x5C, 1)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_58FC end

    def Function_31_6F4A(): pass

    label("Function_31_6F4A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F76")
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(800)
    Jump("Function_31_6F4A")

    label("loc_6F76")

    Return()

    # Function_31_6F4A end

    def Function_32_6F77(): pass

    label("Function_32_6F77")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FA3")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(800)
    Jump("Function_32_6F77")

    label("loc_6FA3")

    Return()

    # Function_32_6F77 end

    def Function_33_6FA4(): pass

    label("Function_33_6FA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FB6")
    Call(0, 29)
    Return()

    label("loc_6FB6")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【話す】\x01",                        # 0
            "【勝負のルールを確認する】\x01",      # 1
            "【やめる】\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7014"),
        (1, "loc_71DD"),
        (SWITCH_DEFAULT, "loc_7341"),
    )


    label("loc_7014")

    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7120")

    #C0209
    ChrTalk(
        0xE,
        (
            "#2400Fどう、釣れてるかい？\x02\x03",

            "ま、勝敗なんて気にせず\x01",
            "存分に釣りを楽しんでいきたまえ。\x01",
            "僕はここで待ってるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#0001Fそういうわけには行きません。\x02\x03",

            "必ず勝って、ヨアヒム先生を\x01",
            "病院に連れ戻しますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xE,
        "#2406Fロイド君、マジメだねぇ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_71D8")

    label("loc_7120")


    #C0212
    ChrTalk(
        0xE,
        (
            "#2400Fそういえば……\x01",
            "君、ロイド君って言うんだねぇ。\x02\x03",

            "#2403F尊敬する大先輩、\x01",
            "特級釣師のロイドさんと\x01",
            "同じ名前なんてすごい偶然だな。\x02\x03",

            "#2409F別人と分かっていても\x01",
            "身が締まる思いだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71D8")

    Jump("loc_7341")

    label("loc_71DD")

    OP_60(0x0)

    #C0213
    ChrTalk(
        0xE,
        (
            "#2400F君たちも魚を釣ったら、\x01",
            "セルダン支部長に見せて\x01",
            "サイズを判定してみてくれ。\x02\x03",

            "#2400Fもし君たちが、さっき僕が釣り上げた\x01",
            "『バイパーヘッド』よりも大物を\x01",
            "釣り上げたなら、僕は病院へ戻ろう。\x02\x03",

            "ただし……\x01",
            "支部長に見せられるのは１回限り。\x01",
            "補給の為に中州から出るのは禁止とする。\x02\x03",

            "……そんなところかな。\x01",
            "ルールを確認したくなったら\x01",
            "いつでも聞いてくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7341")

    label("loc_7341")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_6FA4 end

    def Function_34_7352(): pass

    label("Function_34_7352")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_769A")
    EventBegin(0x0)
    SetMapFlags(0x8000000)
    OP_E0(0x2)
    Fade(500)
    OP_68(21800, -5700, -48170, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, 19950, -6300, -47640, 180)
    SetChrPos(0x102, 21740, -6300, -46700, 180)
    SetChrPos(0x103, 22920, -6300, -47470, 225)
    SetChrPos(0x104, 23350, -6300, -48580, 225)
    OP_0D()

    #N0214
    NpcTalk(
        0xFE,
        "男性",
        (
            "#12Pいやぁ、大漁大漁。\x01",
            "なかなかいいポイントを見つけたよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0215
    NpcTalk(
        0xFE,
        "男性",
        (
            "#12Pおや、君は……\x01",
            "釣公師団の団員かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#5P#0003F（い、一応そういうことに\x01",
            "  なるのかな……？）\x02\x03",

            "#0000Fえっと、ロイドと言います。\x01",
            "どうも初めまして。\x02",
        )
    )

    CloseMessageWindow()

    #N0217
    NpcTalk(
        0xFE,
        "男性",
        (
            "#12P……ロイド……？\x01",
            "はは、何たる偶然だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        "#5P#0005F……え。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "#12P私の名前もロイドというんだ。\x01",
            "釣公師団では特級釣師として\x01",
            "名を連ねているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "#12P大会のゲストとして\x01",
            "セルダン支部長に呼ばれて\x01",
            "リベール王国からやって来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "#12P記念祭の間は滞在するつもりだから\x01",
            "どうかよろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#5P#0005Fよ、よろしくお願いします。\x02\x03",

            "#0003F（前にエステルたちが言ってた\x01",
            "  ロイドさんって、\x01",
            "  この人のことかな……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0xB7, 3)
    SetChrPos(0x0, 19950, -6300, -47640, 180)
    EventEnd(0x5)
    Jump("loc_7CE5")

    label("loc_769A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7749")

    #C0223
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "遊撃士のエステル君も\x01",
            "クロスベルにきているんだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "彼女もなかなかの腕前でね。\x01",
            "僕は一度勝負を仕掛けて\x01",
            "負かされたこともあるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CE5")

    label("loc_7749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AFC")

    #C0225
    ChrTalk(
        0xFE,
        (
            "君たち、釣り勝負をしているらしいな。\x01",
            "うむ、存分に戦いたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "さっき覗き見たが、ヨアヒム君の\x01",
            "釣った魚は相当の大物だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "あれに勝つには……この湖で最大の\x01",
            "『タイタン』という種類の魚を\x01",
            "釣り上げなければ厳しいだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        "#0006F（ふ、不安だ……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AF4")

    #C0229
    ChrTalk(
        0xFE,
        (
            "はは、情けない顔をするもんじゃない。\x01",
            "第一に優先すべきは楽しむことだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "……そうだな、折角だからこの私が\x01",
            "アドバイスしてあげよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "いきなり大物を狙うより、\x01",
            "まずは、小物を釣ること。\x01",
            "これが大物を釣り上げるコツだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "大物はミミズみたいなエサじゃ\x01",
            "近寄ってすらくれないからね。\x01",
            "まずは生餌となる小物が必要なのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "ちょうど、このポイントは\x01",
            "小魚しかいないようだ。\x01",
            "まずはこのエサで釣ってみるといい。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0234
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x18B),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "を５個手に入れた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0235
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x188),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "を５個手に入れた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x18B, 5)
    AddItemNumber(0x188, 5)

    #C0236
    ChrTalk(
        0x101,
        (
            "#0005Fあ、ありがとうございます。\x02\x03",

            "#0003F（……まずは小物、か。\x01",
            "  よし、せっかくだし試してみるか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB7, 7)

    label("loc_7AF4")

    SetScenarioFlags(0x0, 3)
    Jump("loc_7C47")

    label("loc_7AFC")


    #C0237
    ChrTalk(
        0xFE,
        (
            "奥のポイントには大物の\x01",
            "『タイタン』という魚がいるが、\x01",
            "生餌がない限り見向きもされないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "いきなり大物を狙うより、\x01",
            "まずは、小物を釣ること。\x01",
            "奥のポイントに行くのはその後だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "ちょうど、このポイントは\x01",
            "小魚しかいないようだ。\x01",
            "まずは生餌を確保するといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "まぁ、がんばりたまえ。\x01",
            "第一に優先すべきは楽しむことだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C47")

    Jump("loc_7CE5")

    label("loc_7C4C")


    #C0241
    ChrTalk(
        0xFE,
        (
            "私は大会のゲストとして\x01",
            "セルダン支部長に呼ばれて\x01",
            "リベール王国からやって来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "記念祭の間は滞在するつもりだから\x01",
            "どうかよろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CE5")

    TalkEnd(0xFE)
    Return()

    # Function_34_7352 end

    def Function_35_7CE9(): pass

    label("Function_35_7CE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8056")

    #C0243
    ChrTalk(
        0xFE,
        (
            "お、君がロイド団員か？\x01",
            "かねがね話は聞いているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "コパンのやつに誘われて\x01",
            "ウチに入団したそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "俺は釣公師団・クロスベル支部の\x01",
            "支部長を務めるセルダンだ。\x01",
            "以後宜しくな、ロイド団員！\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#0005Fえ？　ええと……\x02\x03",

            "#0006Fあの、自分は釣公師団……に\x01",
            "入団した事になってるんですか？\x02\x03",

            "#0000F確かに以前\x01",
            "釣竿を受け取りましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "ふはは、細かい事は気にするな！\x01",
            "君はもはや\x01",
            "俺たちの同志も同然だぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x101,
        (
            "#0006F（ご、強引な人だな……）\x02\x03",

            "（まあ同じ趣味を持ってる人たちみたいだ、\x01",
            "  釣りの話なんかは合いそうだけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7FDC")

    #C0249
    ChrTalk(
        0xFE,
        (
            "ところでロイド団員、\x01",
            "今日はヨアヒム団員と\x01",
            "釣り勝負をするんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "公式の釣り勝負の形式とは\x01",
            "外れているが、まあいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "勝敗を判定したくなったら\x01",
            "俺に声をかけてくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_804F")

    label("loc_7FDC")


    #C0252
    ChrTalk(
        0xFE,
        (
            "ロイド団員も釣り大会に\x01",
            "参加しに来たのかね？\x01",
            "なら大歓迎だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "空いている場所を使って\x01",
            "自由に楽しむがいい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_804F")

    SetScenarioFlags(0x71, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_8056")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_80C9")

    #C0254
    ChrTalk(
        0xFE,
        (
            "そういえば、釣公師団の支部を\x01",
            "あけっぱなしだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "大会が終わり次第\x01",
            "早く帰ってやらねば。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8649")

    label("loc_80C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_85E5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【話す】\x01",                            # 0
            "【手持ちの魚でヨアヒムと勝負】\x01",      # 1
            "【やめる】\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8135"),
        (1, "loc_8268"),
        (SWITCH_DEFAULT, "loc_85D3"),
    )


    label("loc_8135")

    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81FD")

    #C0256
    ChrTalk(
        0xFE,
        (
            "ヨアヒム団員から話は聞いている……\x01",
            "釣り勝負をするんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "公式の釣り勝負の形式とは\x01",
            "外れているが、まあいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "勝敗を判定したくなったら\x01",
            "俺に声をかけてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8263")

    label("loc_81FD")


    #C0259
    ChrTalk(
        0xFE,
        (
            "ヨアヒム団員と釣り勝負を\x01",
            "しているんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "勝敗を判定したくなったら\x01",
            "俺に声をかけてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8263")

    Jump("loc_85D3")

    label("loc_8268")

    OP_60(0x0)
    Call(0, 36)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83E4")

    #C0261
    ChrTalk(
        0xFE,
        (
            "ヨアヒム団員の釣った\x01",
            "『バイパーヘッド』は、\x01",
            "すでにサイズを計算しているぞ。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 37)

    #C0262
    ChrTalk(
        0xFE,
        "この魚で勝負するのか？\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【はい】\x01",        # 0
            "【いいえ】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_832C"),
        (1, "loc_8384"),
        (SWITCH_DEFAULT, "loc_83DF"),
    )


    label("loc_832C")

    OP_60(0x1)

    #C0263
    ChrTalk(
        0xFE,
        "よし来た！\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "ではヨアヒム団員を呼んで来よう。\x01",
            "判定はそこで行なうぞ。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 30)
    Jump("loc_83DF")

    label("loc_8384")

    OP_60(0x1)

    #C0265
    ChrTalk(
        0xFE,
        "なんだ、勝負しないのか？\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "満足のいく魚が釣れたら\x01",
            "もう一度声をかけてくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83DF")

    label("loc_83DF")

    Jump("loc_85CE")

    label("loc_83E4")


    #C0267
    ChrTalk(
        0xFE,
        (
            "ヨアヒム団員の釣った\x01",
            "『バイパーヘッド』は、\x01",
            "すでにサイズを計算しているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        "そろそろ勝負を始めるか？\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "……と思ったら……\x01",
            "この釣り場で釣れる魚を\x01",
            "一匹も持っていないじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        "まさか、ギブアップするのか？\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【はい】\x01",        # 0
            "【いいえ】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_8502"),
        (1, "loc_857D"),
        (SWITCH_DEFAULT, "loc_85CE"),
    )


    label("loc_8502")

    OP_60(0x1)

    #C0271
    ChrTalk(
        0xFE,
        (
            "ふむ、そうか……\x01",
            "それは残念だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "ではヨアヒム団員を呼んで来よう。\x01",
            "ギブアップする旨を伝えなければな。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 30)
    Jump("loc_85CE")

    label("loc_857D")

    OP_60(0x1)

    #C0273
    ChrTalk(
        0xFE,
        "うむ、そうでなくてはな。\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "魚が釣れたら\x01",
            "もう一度声をかけてくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85CE")

    label("loc_85CE")

    Jump("loc_85D3")

    label("loc_85D3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    Jump("loc_8649")

    label("loc_85E5")


    #C0275
    ChrTalk(
        0xFE,
        (
            "おお、君たちも釣り大会に\x01",
            "参加しに来たのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "空いている場所を使って\x01",
            "自由に楽しむがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8649")

    TalkEnd(0xFE)
    Return()

    # Function_35_7CE9 end

    def Function_36_864D(): pass

    label("Function_36_864D")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_8672")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_8672")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_868D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_868D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_86A8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_86A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_86C3")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_86C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_86DE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_86DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_86F9")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_86F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_8714")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_8714")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_872A")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_872A")

    Return()

    # Function_36_864D end

    def Function_37_872B(): pass

    label("Function_37_872B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8789")

    #C0277
    ChrTalk(
        0xD,
        (
            "対して、君の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『タイタン』だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A26")

    label("loc_8789")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87ED")

    #C0278
    ChrTalk(
        0xD,
        (
            "対して、君の釣った魚で\x01",
            "最もサイズが大きいものも……\x01",
            "『バイパーヘッド』だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A26")

    label("loc_87ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_884F")

    #C0279
    ChrTalk(
        0xD,
        (
            "対して、君の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『グラトンバス』だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A26")

    label("loc_884F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88AD")

    #C0280
    ChrTalk(
        0xD,
        (
            "対して、君の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『サモーナ』だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A26")

    label("loc_88AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_890B")

    #C0281
    ChrTalk(
        0xD,
        (
            "対して、君の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『トラード』だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A26")

    label("loc_890B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8969")

    #C0282
    ChrTalk(
        0xD,
        (
            "対して、君の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『カサギン』だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A26")

    label("loc_8969")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C7")

    #C0283
    ChrTalk(
        0xD,
        (
            "対して、君の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『エーゼル』だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A26")

    label("loc_89C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A26")

    #C0284
    ChrTalk(
        0xD,
        (
            "対して、君の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『スノーシュラブ』だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A26")

    Return()

    # Function_37_872B end

    def Function_38_8A27(): pass

    label("Function_38_8A27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A8F")

    #C0285
    ChrTalk(
        0xD,
        (
            "#11Pそして、ロイド団員の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『タイタン』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D72")

    label("loc_8A8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AFD")

    #C0286
    ChrTalk(
        0xD,
        (
            "#11Pそして、ロイド団員の釣った魚で\x01",
            "最もサイズが大きいものも……\x01",
            "『バイパーヘッド』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D72")

    label("loc_8AFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B69")

    #C0287
    ChrTalk(
        0xD,
        (
            "#11Pそして、ロイド団員の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『グラトンバス』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D72")

    label("loc_8B69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BD1")

    #C0288
    ChrTalk(
        0xD,
        (
            "#11Pそして、ロイド団員の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『サモーナ』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D72")

    label("loc_8BD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C39")

    #C0289
    ChrTalk(
        0xD,
        (
            "#11Pそして、ロイド団員の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『トラード』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D72")

    label("loc_8C39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CA1")

    #C0290
    ChrTalk(
        0xD,
        (
            "#11Pそして、ロイド団員の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『カサギン』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D72")

    label("loc_8CA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D09")

    #C0291
    ChrTalk(
        0xD,
        (
            "#11Pそして、ロイド団員の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『エーゼル』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D72")

    label("loc_8D09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D72")

    #C0292
    ChrTalk(
        0xD,
        (
            "#11Pそして、ロイド団員の釣った魚で\x01",
            "最もサイズが大きいものは……\x01",
            "『スノーシュラブ』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D72")

    Return()

    # Function_38_8A27 end

    SaveToFile()

Try(main)
