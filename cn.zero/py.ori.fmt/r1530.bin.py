from ZeroScenarioHelper import *

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
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 3000, 0, 28000, 0, 0, 1, 96, 0, 2, 0, 3],
    )

    BuildStringList((
        "r1530",                  # 0
        "琪露露",                 # 1
        "克潘",                   # 2
        "彼德",                   # 3
        "彼德",                   # 4
        "特级钓师罗伊德",         # 5
        "赛尔丹分部长",           # 6
        "约亚西姆副教授",         # 7
        "巴士",                   # 8
        "后冲鱼",                 # 9
        "br1500",                 # 10
        "br1520",                 # 11
        "br1500",                 # 12
        "br1520",                 # 13
        "br1500",                 # 14
        "br1500",                 # 15
        "br1520",                 # 16
        "br1520",                 # 17
        "br1520",                 # 18
        "克洛斯贝尔市方向",       # 19
        "乌尔斯拉医科大学方向",   # 20
    ))

    ATBonus("ATBonus_630", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_8005", 2,   8,   0,   6,   2,   0,   0)
    Sepith("Sepith_7FDD", 0,   8,   0,   4,   4,   2,   0)
    Sepith("Sepith_7FFD", 7,   3,   5,   3,   0,   0,   0)
    Sepith("Sepith_7FED", 0,   3,   0,   0,   5,   5,   5)
    Sepith("Sepith_7FF5", 0,   8,   0,   2,   2,   4,   2)
    Sepith("Sepith_7FCD", 4,   2,   0,   8,   0,   3,   2)

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
        "BattleInfo_A50", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_8005", 30, 40, 20, 10,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", "ms69800.dat", 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_8C0", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_7FDD", 30, 40, 20, 10,
        (
            ("ms63600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms63600.dat", "ms63600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_BE0", 0x0000, 12, 6, 45, 10, 1, 50, 0, "br1520", "Sepith_7FFD", 30, 40, 20, 10,
        (
            ("ms65300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65300.dat", "ms65300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65300.dat", "ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_7F8", 0x0000, 12, 6, 45, 10, 1, 40, 0, "br1520", "Sepith_7FED", 30, 40, 20, 10,
        (
            ("ms65200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_988", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1520", "Sepith_7FF5", 30, 40, 20, 10,
        (
            ("ms61300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_730", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_7FCD", 30, 40, 20, 10,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_690", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_670", "MonsterBattlePostion_6F0", "ed7400", "ed7403", "ATBonus_630"),
        )
    )

    BattleInfo(
        "BattleInfo_B18", 0x0000, 12, 6, 45, 10, 1, 50, 0, "br1500", "Sepith_7FFD", 30, 40, 20, 10,
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
        "Function_0_E5C",          # 00, 0
        "Function_1_E7B",          # 01, 1
        "Function_2_F33",          # 02, 2
        "Function_3_1091",         # 03, 3
        "Function_4_15F1",         # 04, 4
        "Function_5_17EB",         # 05, 5
        "Function_6_1921",         # 06, 6
        "Function_7_1A57",         # 07, 7
        "Function_8_1A6B",         # 08, 8
        "Function_9_1A7F",         # 09, 9
        "Function_10_1A93",        # 0A, 10
        "Function_11_1B4A",        # 0B, 11
        "Function_12_1C6B",        # 0C, 12
        "Function_13_1D8C",        # 0D, 13
        "Function_14_1E21",        # 0E, 14
        "Function_15_1EF2",        # 0F, 15
        "Function_16_23DF",        # 10, 16
        "Function_17_26ED",        # 11, 17
        "Function_18_281D",        # 12, 18
        "Function_19_2921",        # 13, 19
        "Function_20_29E9",        # 14, 20
        "Function_21_2A9B",        # 15, 21
        "Function_22_306F",        # 16, 22
        "Function_23_32A5",        # 17, 23
        "Function_24_3303",        # 18, 24
        "Function_25_34FC",        # 19, 25
        "Function_26_3B74",        # 1A, 26
        "Function_27_3F99",        # 1B, 27
        "Function_28_408B",        # 1C, 28
        "Function_29_4484",        # 1D, 29
        "Function_30_52D7",        # 1E, 30
        "Function_31_6681",        # 1F, 31
        "Function_32_66AE",        # 20, 32
        "Function_33_66DB",        # 21, 33
        "Function_34_69ED",        # 22, 34
        "Function_35_71BC",        # 23, 35
        "Function_36_79CB",        # 24, 36
        "Function_37_7AA9",        # 25, 37
        "Function_38_7CF7",        # 26, 38
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AD")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16EA")
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
            "出现了魔兽！\x07\x00\x02",
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
        (0, "loc_16CB"),
        (2, "loc_16DA"),
        (1, "loc_16E7"),
        (SWITCH_DEFAULT, "loc_16EA"),
    )


    label("loc_16CB")

    SetScenarioFlags(0x74, 1)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_16EA")

    label("loc_16DA")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_16E7")

    OP_B7(0x0)
    Return()

    label("loc_16EA")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('水珠连衣裙', 1)"), scpexpr(EXPR_END)), "loc_1741")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '水珠连衣裙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_17A8")

    label("loc_1741")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '水珠连衣裙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '水珠连衣裙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17A8")

    Jump("loc_17DF")

    label("loc_17AD")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_17DF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_15F1 end

    def Function_5_17EB(): pass

    label("Function_5_17EB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D8")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('复苏药', 1)"), scpexpr(EXPR_END)), "loc_186A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_18D3")

    label("loc_186A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18D3")

    Jump("loc_1915")

    label("loc_18D8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
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

    label("loc_1915")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_17EB end

    def Function_6_1921(): pass

    label("Function_6_1921")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0E")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('回避３', 1)"), scpexpr(EXPR_END)), "loc_19A0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1A09")

    label("loc_19A0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '回避３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '回避３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A09")

    Jump("loc_1A4B")

    label("loc_1A0E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
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

    label("loc_1A4B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1921 end

    def Function_7_1A57(): pass

    label("Function_7_1A57")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 4)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_1A57 end

    def Function_8_1A6B(): pass

    label("Function_8_1A6B")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1A6B end

    def Function_9_1A7F(): pass

    label("Function_9_1A7F")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 6)
    OP_65(0x7, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_9_1A7F end

    def Function_10_1A93(): pass

    label("Function_10_1A93")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0011
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
            "克洛斯贝尔市南出口\x01",      # 0
            "圣乌尔斯拉医科大学\x01",      # 1
            "放弃\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B22")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1B42")

    label("loc_1B22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B42")
    Call(0, 12)
    ClearMapFlags(0x8000000)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()

    label("loc_1B42")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1A93 end

    def Function_11_1B4A(): pass

    label("Function_11_1B4A")

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

    def lambda_1C25():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C25)
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

    # Function_11_1B4A end

    def Function_12_1C6B(): pass

    label("Function_12_1C6B")

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

    def lambda_1D46():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1D46)
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

    # Function_12_1C6B end

    def Function_13_1D8C(): pass

    label("Function_13_1D8C")

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

    # Function_13_1D8C end

    def Function_14_1E21(): pass

    label("Function_14_1E21")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E90")
    OP_93(0xFE, 0x9F, 0x0)

    #C0012
    ChrTalk(
        0xFE,
        "……水边真令人神清气爽……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "与其待在市里，\x01",
            "果然还是在郊外走走比较好呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EEE")

    label("loc_1E90")

    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0014
    ChrTalk(
        0xFE,
        (
            "你们也是出来散步，\x01",
            "感受大自然的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "不坐巴士，真少见呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1EEE")

    TalkEnd(0xFE)
    Return()

    # Function_14_1E21 end

    def Function_15_1EF2(): pass

    label("Function_15_1EF2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD1")

    #C0016
    ChrTalk(
        0xFE,
        (
            "……昨天有游击士\x01",
            "经过了这里呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "那个双马尾的女孩，\x01",
            "竟然钓起了\x01",
            "２２０里矩的珍珠草哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "然后说自己很忙，下次再来，\x01",
            "就那么回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "……到底是什么来头啊～\x01",
            "垂钓技术相当厉害的说～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_201D")

    label("loc_1FD1")


    #C0020
    ChrTalk(
        0xFE,
        (
            "那个双马尾的女孩\x01",
            "到底是什么来头啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "分部长说不定\x01",
            "知道什么消息呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_201D")

    Jump("loc_23DB")

    label("loc_2022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_20F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A4")

    #C0022
    ChrTalk(
        0xFE,
        (
            "特级钓师罗伊德吗～\x01",
            "原来如此，果然有一手的说～\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "不过，我也是特级钓师呢。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "不会输给他的说～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20EF")

    label("loc_20A4")


    #C0025
    ChrTalk(
        0xFE,
        (
            "虽然在昨天的钓鱼比赛中\x01",
            "以微小的差距输了～\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        "但下次可不会再这样了。\x02",
    )

    CloseMessageWindow()

    label("loc_20EF")

    Jump("loc_23DB")

    label("loc_20F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_23DB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2133")

    #C0027
    ChrTalk(
        0xFE,
        (
            "哦哦……\x01",
            "预感要钓到大鱼的说！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DB")

    label("loc_2133")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2231")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E8")

    #C0028
    ChrTalk(
        0xFE,
        (
            "哎，你在和约亚西姆先生\x01",
            "比赛钓鱼吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "嗯，不要太紧张，好好享受吧。\x01",
            "钓鱼可不是该带着\x01",
            "使命感去做的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "……其实我只是想说点\x01",
            "帅气台词的说。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_222C")

    label("loc_21E8")


    #C0031
    ChrTalk(
        0xFE,
        (
            "嗯，不要太紧张，好好享受吧。\x01",
            "钓鱼可不是该带着\x01",
            "使命感去做的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_222C")

    Jump("loc_23DB")

    label("loc_2231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2334")

    #C0032
    ChrTalk(
        0xFE,
        (
            "啊……这不是\x01",
            "罗伊德警官一行嘛，\x01",
            "各位终于也来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "费瑟尔杯是为了\x01",
            "赞颂钓公师团的名誉会长\x01",
            "费瑟尔男爵而举办的大赛。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "不过，虽说是大赛，\x01",
            "主要目的却不在竞争，\x01",
            "而在于享受垂钓乐趣的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……刚才忘记说明了，\x01",
            "所以一口气说了出来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23DB")

    label("loc_2334")


    #C0036
    ChrTalk(
        0xFE,
        (
            "费瑟尔杯是为了\x01",
            "赞颂钓公师团的名誉会长\x01",
            "费瑟尔男爵而举办的大赛。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "虽说是大赛，主要目的却不在竞争，\x01",
            "而在于享受垂钓乐趣的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "不过，我今天真是斗志十足的说。\x02",
    )

    CloseMessageWindow()

    label("loc_23DB")

    TalkEnd(0xFE)
    Return()

    # Function_15_1EF2 end

    def Function_16_23DF(): pass

    label("Function_16_23DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2554")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2468")

    #C0039
    ChrTalk(
        0xFE,
        "唔～……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "我的水平\x01",
            "果然也只能达到\x01",
            "业余钓师的程度吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "虽然不甘心，但是\x01",
            "完全没有鱼上钩的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_254F")

    label("loc_2468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_24D8")

    #C0042
    ChrTalk(
        0xFE,
        (
            "在这一带应该\x01",
            "可以钓到大鱼的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "唔～……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "总是无法像约亚西姆医生\x01",
            "那样顺利钓到鱼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_254F")

    label("loc_24D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_254F")

    #C0045
    ChrTalk(
        0xFE,
        "你听说了吗？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "约亚西姆团员昨天\x01",
            "在这一带钓到了大鱼哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "呼，我也不能输给他。\x01",
            "必须要再加把劲才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_254F")

    Jump("loc_26E9")

    label("loc_2554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26E9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257B")
    Call(0, 17)
    Jump("loc_25DA")

    label("loc_257B")


    #C0048
    ChrTalk(
        0xFE,
        (
            "……咦，约亚西姆先生\x01",
            "什么时候不见了？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "好奇怪啊，\x01",
            "他明明宣称今天放假，\x01",
            "不用工作的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DA")

    Jump("loc_26E9")

    label("loc_25DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_266E")

    #C0050
    ChrTalk(
        0xFE,
        (
            "约亚西姆医生在钓公师团里\x01",
            "也算是水平相当厉害的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "他身为医生，工作那么忙，\x01",
            "却还能精进到如此地步，\x01",
            "真是令人佩服啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E9")

    label("loc_266E")


    #C0052
    ChrTalk(
        0xFE,
        (
            "呀，好久没在\x01",
            "这个河滩钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "在郊外钓鱼的话，必须要算好时机，\x01",
            "在没有魔兽的时候出来才行，\x01",
            "所以很少有机会能来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E9")

    TalkEnd(0xFE)
    Return()

    # Function_16_23DF end

    def Function_17_26ED(): pass

    label("Function_17_26ED")


    #C0054
    ChrTalk(
        0xFE,
        (
            "约亚西姆医生刚才\x01",
            "塞了本小说给我。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "他的态度过于亲切，\x01",
            "反而让我觉得很可疑……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "结果，好像是偷偷\x01",
            "从我这里拿走了一点钓饵。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#0006F（他到底在干什么啊……）\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "啊，我对书完全没兴趣，\x01",
            "你们要是想看的话，就拿去好了。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '黑市医生格伦　６卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('黑市医生格伦　６卷', 1)
    SetScenarioFlags(0x9C, 5)
    Return()

    # Function_17_26ED end

    def Function_18_281D(): pass

    label("Function_18_281D")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0060
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291C")
    OP_E0(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28FA")
    MiniGame(0x6, 0x10, 0xC526, 0xFFFFE764, 0xFFFF18A2, 0x59, 0xE1AA, 0xFFFFEB4C, 0xFFFF1924)
    Jump("loc_291C")

    label("loc_28FA")

    MiniGame(0x6, 0xC, 0xC526, 0xFFFFE764, 0xFFFF18A2, 0x59, 0xE1AA, 0xFFFFEB4C, 0xFFFF1924)

    label("loc_291C")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_18_281D end

    def Function_19_2921(): pass

    label("Function_19_2921")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0062
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29E4")
    OP_E0(0x2)
    MiniGame(0x6, 0xF, 0x4696, 0xFFFFE764, 0xFFFF2392, 0x10E, 0x37D2, 0xFFFFE764, 0xFFFF2392)

    label("loc_29E4")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_19_2921 end

    def Function_20_29E9(): pass

    label("Function_20_29E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2A41")
    TalkBegin(0xFF)
    SetChrName("")

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x02",
        )
    )

    CloseMessageWindow()

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "巴士的到达时间\x01",
            "似乎早就过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_2A9A")

    label("loc_2A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A52")
    Call(0, 10)
    Jump("loc_2A9A")

    label("loc_2A52")

    TalkBegin(0xFF)
    SetChrName("")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "巴士的到达时间\x01",
            "早就过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2A9A")

    Return()

    # Function_20_29E9 end

    def Function_21_2A9B(): pass

    label("Function_21_2A9B")

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

    def lambda_2B31():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B31)
    Sleep(50)

    def lambda_2B4E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B4E)
    Sleep(60)

    def lambda_2B6B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B6B)
    Sleep(70)

    def lambda_2B88():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B88)
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
        "#0006F#5P呼……\x02",
    )

    CloseMessageWindow()

    def lambda_2BD6():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BD6)

    def lambda_2BE3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BE3)

    def lambda_2BF0():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BF0)

    def lambda_2BFD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BFD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    #C0069
    ChrTalk(
        0x101,
        (
            "#0001F#6P游击士协会的新人，\x01",
            "艾丝蒂尔和约修亚吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#0106F#12P……真让人不由自主地\x01",
            "想叹气啊……\x02\x03",

            "#0101F他们看起来大约和我们同龄，\x01",
            "但好像已经是级别相当高的游击士了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0306F#11P嗯，应该没错吧。\x02\x03",

            "#0301F那种超群的身手和武技……\x01",
            "必然是经历过相当严酷的历练。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        (
            "#0203F#5P是呀……\x01",
            "我们拼尽全力才能勉强应付的魔兽，\x01",
            "被他们转瞬之间就轻松解决了。\x02\x03",

            "#0200F他们两个今后\x01",
            "也会来和我们抢生意吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#0008F#6P是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    #C0074
    ChrTalk(
        0x101,
        (
            "#0004F#6P──消沉也不是办法，\x01",
            "我们只要自己努力就好了。\x02\x03",

            "#0000F而且，与其将他们当作抢生意的，\x01",
            "倒不如将他们当作有力的竞争对手。\x02\x03",

            "这样想也许会更有干劲吧？\x02",
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

    def lambda_2EC3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2EC3)

    def lambda_2ED0():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2ED0)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0075
    ChrTalk(
        0x103,
        (
            "#0211F#5P……如果说是竞争对手，\x01",
            "感觉实力差距也太大了点……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#0304F#11P不过，那也总比\x01",
            "亚里欧斯大叔\x01",
            "要容易追赶一点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        "#0100F#11P嗯～那倒是……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#0004F#6P好啦，大家打起精神来吧。\x02\x03",

            "#0000F难得人家一片好意，\x01",
            "我们就赶快去医院吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        (
            "#0206F#5P虽然又要徒步走去……\x01",
            "唉，但也没办法呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#0102F#11P呵呵，就当是稍微\x01",
            "锻炼一下身体吧。\x02",
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

    # Function_21_2A9B end

    def Function_22_306F(): pass

    label("Function_22_306F")

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

    def lambda_31E4():
        OP_95(0xFE, -28280, 0, -16570, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_31E4)
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

    def lambda_3267():
        OP_95(0xFE, 1980, 0, 15000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3267)
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

    # Function_22_306F end

    def Function_23_32A5(): pass

    label("Function_23_32A5")

    SetChrPos(0xFE, -65379, -4900, -109290, 0)

    def lambda_32BB():
        OP_95(0xFE, -41340, -4900, -109460, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32BB)
    Sound(469, 0, 100, 0)
    Sleep(4000)
    EndChrThread(0xFE, 0x1)

    def lambda_32E2():
        OP_9E(0xFE, 0xFFFF5E84, 0xFFFE8734, 0xFFFEA070, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32E2)
    Sound(458, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_32A5 end

    def Function_24_3303(): pass

    label("Function_24_3303")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x153, 0x80)
    SetChrBattleFlags(0x153, 0x8000)
    SetChrFlags(0xEF, 0x80)
    SetChrBattleFlags(0xEF, 0x8000)
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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3459")
    Sound(471, 0, 100, 0)
    FadeToBright(1000, 0)
    SetChrPos(0xF, -890, 0, 10890, 225)

    def lambda_33EE():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_33EE)
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

    label("loc_3459")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34EF")
    Fade(1000)
    SetChrPos(0xF, -28500, -830, -21530, 0)
    OP_68(-6650, -950, -31510, 0)
    MoveCamera(54, 12, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(37610, 0)
    OP_68(-19030, -950, -31410, 10000)
    OP_0D()
    Sleep(2000)

    def lambda_34C2():
        OP_95(0xFE, -27920, -4200, -50960, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_34C2)
    Sound(458, 0, 100, 0)
    Sleep(4500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xF, 0x1)

    label("loc_34EF")

    SetScenarioFlags(0x5C, 1)
    NewScene("e0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3303 end

    def Function_25_34FC(): pass

    label("Function_25_34FC")

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

    def lambda_35E0():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35E0)
    Sleep(50)

    def lambda_35F8():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35F8)
    Sleep(50)

    def lambda_3610():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3610)
    Sleep(50)

    def lambda_3628():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3628)
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
        "#0007F#11P啊……！\x02",
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

    def lambda_3730():
        OP_95(0xFE, -57800, -4900, -108900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3730)

    def lambda_374A():
        OP_95(0xFE, -58240, -4900, -111000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_374A)

    def lambda_3764():
        OP_95(0xFE, -56460, -4900, -111100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3764)

    def lambda_377E():
        OP_95(0xFE, -56720, -4900, -109480, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_377E)
    WaitChrThread(0x101, 1)

    def lambda_379C():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_379C)
    WaitChrThread(0x102, 1)

    def lambda_37AD():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37AD)
    WaitChrThread(0x103, 1)

    def lambda_37BE():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_37BE)
    WaitChrThread(0x104, 1)

    def lambda_37CF():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_37CF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0082
    ChrTalk(
        0x102,
        (
            "#0105F#12P为、为什么\x01",
            "会在这种地方停车……\x02\x03",

            "#0101F而且……\x01",
            "车里好像一个人都没有？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        "#0301F#12P好像是啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0084
    ChrTalk(
        0x104,
        (
            "#0301F#5P阿缇，\x01",
            "查下周围有什么反应。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_388F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_388F)
    Sleep(50)

    def lambda_389F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_389F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0085
    ChrTalk(
        0x103,
        "#0201F#12P好……\x02",
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
            "#0206F#12P……不行。\x02\x03",

            "#0201F周围１０赛尔矩\x01",
            "之内都没有人类的反应。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#0303F#5P嘁……\x01",
            "就知道是这样。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0088
    ChrTalk(
        0x104,
        (
            "#0301F#11P看起来，也不像是\x01",
            "遭到了魔兽袭击吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#0003F#5P嗯……\x01",
            "车很规矩地停在了路边。\x02\x03",

            "#0008F驾驶员多半是以自己的意志\x01",
            "来靠边停车的吧。\x02\x03",

            "莫非是发生了什么\x01",
            "不得不停车的情况吗……\x02\x03",

            "#0001F总之，调查一下车内吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0090
    ChrTalk(
        0x102,
        "#0101F#6P嗯……！\x02",
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

    # Function_25_34FC end

    def Function_26_3B74(): pass

    label("Function_26_3B74")

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
            "#0003F#5P好的、好的……\x02\x03",

            "#0013F……明白了，\x01",
            "联络工作就交给您了。\x02\x03",

            "我们继续\x01",
            "前往乌尔斯拉医院。\x02\x03",

            "#0003F──是，\x01",
            "我们会多加小心的。\x02",
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
        "#0201F#5P……科长怎么说？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0093
    ChrTalk(
        0x101,
        (
            "#0006F#12P说是要先联络\x01",
            "唐古拉姆门那边。\x02\x03",

            "#0000F好像打算请求\x01",
            "索妮亚副司令的协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#0100F#5P是吗……\x01",
            "那就令人安心多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#0300F#11P嗯，副司令\x01",
            "一定会出手相助的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        (
            "#0200F#5P那么，我们\x01",
            "继续前往医院吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#0003F#12P嗯，从这里到医院\x01",
            "也没多远了。\x02\x03",

            "#0001F说不定，乘客们是走着去医院了，\x01",
            "这种可能性也是存在的。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#0306F#11P嗯，但慰问品都还留在车上，\x01",
            "这就已经说明情况非同寻常了……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#0101F#5P总之，我们尽快吧，\x01",
            "太阳马上就要落山了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#0013F#12P嗯……！\x02",
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

    # Function_26_3B74 end

    def Function_27_3F99(): pass

    label("Function_27_3F99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4087")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4038")

    #C0101
    ChrTalk(
        0x101,
        (
            "#0000F哦……\x02\x03",

            "比赛规则是禁止离开河滩，\x01",
            "去其它地方补给。\x02\x03",

            "为了把约亚西姆医生带回去，\x01",
            "必须要堂堂正正地比一场才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_406B")

    label("loc_4038")


    #C0102
    ChrTalk(
        0x101,
        (
            "#0000F在赢得钓鱼比赛之前，\x01",
            "还不能离开河滩啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_406B")

    Sleep(50)
    SetChrPos(0x0, -17740, -1390, -15870, 156)
    EventEnd(0x4)
    Return()

    label("loc_4087")

    Call(0, 28)
    Return()

    # Function_27_3F99 end

    def Function_28_408B(): pass

    label("Function_28_408B")

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
        "#11P#0005F那是……\x02",
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
        "#5P#0300F哦哦～好像玩得正开心呢。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        (
            "#5P#0106F郊外还有魔兽出没呢，\x01",
            "这些人可真是执著啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x103,
        (
            "#6P#0200F……话说，很不可思议的是，\x01",
            "现在好像并没有魔兽出现呢。\x02\x03",

            "是被钓鱼大赛的\x01",
            "热烈气氛吓跑了吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#12P#0005F那、那应该还不至于吧。\x02\x03",

            "#0003F总而言之……\x01",
            "这里应该就是那个\x01",
            "钓鱼大赛的会场了。\x02\x03",

            "#0000F去找找约亚西姆医生吧。\x02",
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

    # Function_28_408B end

    def Function_29_4484(): pass

    label("Function_29_4484")

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
        "白衣男子",
        (
            "#5P#2400F啦啦啦～……\x02\x03",

            "哎呀，钓鱼果然有趣呢。\x01",
            "光是垂下钓线，\x01",
            "心灵就像被洗涤了一般……\x02\x03",

            "在医院的工作中疲惫不堪的身体\x01",
            "也一下就得到了恢复。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#12P#0003F（蓝发白衣的男性……\x01",
            "  嗯，从背影看应该没错了。）\x02\x03",

            "#0001F请问……\x01",
            "您是约亚西姆医生吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xE,
        (
            "#2400F#5P嗯～……我就是\x01",
            "约亚西姆……\x02\x03",

            "#2403F不好意思，我现在\x01",
            "抽不开身。\x02\x03",

            "#2401F要是有什么事的话……啊！\x02",
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
        "#2405F#5P哦哦，来了……！！\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#12P#0006F#5P完、完全不听人说话。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 1, 0, 32)

    #C0113
    ChrTalk(
        0xE,
        (
            "#2401F#5P我在听，在听啦。\x01",
            "而且还在拉呢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        "#12P#0206F（好冷的笑话……）\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#12P#0006F那、那个！\x02\x03",

            "#0001F是乌尔斯拉医院的塞拉小姐\x01",
            "委托我们\x01",
            "来找医生您的！\x02\x03",

            "因为约亚西姆医生不在，\x01",
            "利顿医生和医院的各位\x01",
            "都在发愁呢！\x02",
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
        "#2400F来啦！！\x02",
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
            "#2405F#5P哦哦～……『云斑蛇头』……\x01",
            "这尺寸还真不小嘛。\x02\x03",

            "#2400F嗯嗯，我每天从医院中\x01",
            "偷跑出来练习，果然有收效呀。\x02",
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
            "#12P#0306F真是太我行我素了……\x02\x03",

            "#0301F看这状态，完全\x01",
            "都没在听人说话啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        (
            "#6P#0106F唉……罗伊德，\x01",
            "看来你还得再向他说明一次才行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#12P#0006F（我、我刚才还特意喊那么大声……）\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(300)

    #C0121
    ChrTalk(
        0xE,
        (
            "#2403F#5P……不，那倒不必。\x02\x03",

            "#2400F乌尔斯拉医院的\x01",
            "大家都在等我回去。\x01",
            "……是这么回事吧？\x02",
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
            "初次见面，幸会。\x01",
            "我是约亚西姆·琼塔。\x02\x03",

            "在乌尔斯拉医院\x01",
            "担任副教授。\x02",
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
            "#2405F#5P咦？\x01",
            "你们几个，好像有点眼熟……\x02\x03",

            "#2403F嗯～这就是所谓的既视感吗？\x01",
            "……那样的话，我就不清楚了，\x01",
            "嗯嗯。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#12P#0006F不，并不是既视感……\x01",
            "（还是赶快做个自我介绍为好吧。）\x02\x03",

            "#0001F嗯……我是\x01",
            "克洛斯贝尔警察局·特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02\x03",

            "#0003F总之，约亚西姆医生您……！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xE,
        (
            "#2409F#5P好了好了，别着急嘛，\x01",
            "事情的情况我已经了解了。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#6P#0100F那么……\x01",
            "您愿意回医院了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xE,
        (
            "#2403F#5P嗯～……你们觉得我该怎么办才好？\x02\x03",

            "#2400F这个费瑟尔杯，\x01",
            "可是我从上上个月开始就一直\x01",
            "热切期待的重大活动呢。\x02\x03",

            "#2406F医院在纪念庆典期间似乎也不会放假，\x01",
            "所以想趁现在好好享受一下啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        "#12P#0211F……您没有身为医生的责任感吗？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xE,
        (
            "#2400F#5P说没有那是骗人的。\x02\x03",

            "#2406F上个月底还写了跟偷懒次数\x01",
            "一样多的检讨书，真是累死人啊。\x02\x03",

            "不过好在有利顿帮我解决了一半，\x01",
            "最后总算都写完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#12P#0006F好像跑题了吧……\x02\x03",

            "#0001F请问，究竟要怎样，\x01",
            "您才愿意回医院呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xE,
        (
            "#2403F#5P这个嘛……\x02\x03",

            "#2400F难得在举办费瑟尔杯……\x01",
            "方便的话，要不要用这个来比一场？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#12P#0005F比钓鱼……？\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xE,
        (
            "#2409F#5P没错。\x02\x03",

            "#2400F如果你们能钓到比我刚才钓的\x01",
            "那条『云斑蛇头』还大的鱼，\x01",
            "我就回医院。\x02\x03",

            "#2409F简单明了，不错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#12P#0303F钓鱼比赛吗……\x01",
            "怎么办，罗伊德？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#12P#0001F……明白了，我接受，\x01",
            "请告诉我详细的规则吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xE,
        (
            "#2409F#5P这就对了。\x02\x03",

            "#2400F待会我会把刚才钓到的\x01",
            "『云斑蛇头』给赛尔丹分部长看。\x02\x03",

            "你们要是钓到鱼的话，\x01",
            "也拿去给赛尔丹分部长看吧。\x02\x03",

            "如果你们钓到的鱼\x01",
            "比『云斑蛇头』还大，\x01",
            "就是你们赢了。\x02\x03",

            "不过要记好……\x01",
            "只能将钓上来的鱼给分部长看一次，\x01",
            "鱼的种类也只限在这个钓鱼点所能钓到的。\x02\x03",

            "而且禁止离开这片河摊，去其它场所补给，\x01",
            "或到其它钓鱼点垂钓。\x02\x03",

            "#2409F……没有异议吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#12P#0001F……明白了，\x01",
            "就按照这规则来比赛吧。\x02\x03",

            "#0003F（……钓饵不知道够不够用呢……\x01",
            "  或许可以向其他团员\x01",
            "  请求帮助吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xE,
        (
            "#2400F#5P那么，立刻就开始吧！\x02\x03",

            "#2409F呵呵，祝你们好运哦。\x02",
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

    # Function_29_4484 end

    def Function_30_52D7(): pass

    label("Function_30_52D7")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6075")

    #C0139
    ChrTalk(
        0xE,
        (
            "#2400F#5P呵呵……\x01",
            "钓到满意的鱼了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#12P#0001F还不清楚……\x01",
            "但我不觉得自己会输。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xE,
        "#2409F#5P呵呵，那可真令人期待。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 300)
    TurnDirection(0x101, 0xD, 300)
    Sleep(300)

    #C0142
    ChrTalk(
        0xE,
        (
            "#2400F#5P那么，赛尔丹分部长，\x01",
            "请您裁定胜负吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xD,
        "#11P唔。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xD,
        (
            "#11P约亚西姆团员钓到的……\x01",
            "是『云斑蛇头』啊。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)

    #C0145
    ChrTalk(
        0xD,
        "#11P我所裁定的结果是……\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)
    Sleep(300)

    #C0146
    ChrTalk(
        0x101,
        "#12P#0001F（紧张……）\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_599D")
    OP_2C(0x16, 0x3)
    OP_29(0x16, 0x1, 0x5)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0147
    ChrTalk(
        0xD,
        "#5S#11P……胜者，罗伊德团员！\x02",
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
            "#2405F#5P您、您说什么？\x01",
            "是不是哪里搞错了？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xD,
        (
            "#11P不……罗伊德钓到的鱼\x01",
            "确实比你那条大得多。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xD,
        "#11P我的眼光是不会有错的！\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xE,
        "#2406F#5P怎、怎么会～\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        "#12P#0109F成功了啊，罗伊德！\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        "#12P#0309F噢噢，真了不起啊！\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        "#12P#0202F一般厉害吧。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#12P#0005F成、成功了吗……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    #C0156
    ChrTalk(
        0xE,
        (
            "#2406F#5P呼……惨败啊。\x02\x03",

            "#2400F哦，对了。\x01",
            "作为胜利的奖品，\x01",
            "这个送给你们吧。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('圣灵药', 1)
    OP_96(0xE, 0x710C, 0xFFFFEA20, 0xFFFF7644, 0x3E8, 0x0)
    Sleep(200)

    #C0158
    ChrTalk(
        0x101,
        (
            "#12P#0005F哎……可以吗？\x01",
            "那我们就心怀感激地收下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xE,
        (
            "#2400F#5P好吧……那我就\x01",
            "按照约定，回医院去吧。\x02",
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
            "#12P#0105F真、真有点意外呢，\x01",
            "还以为您会再稍微耍一会赖的……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xE,
        (
            "#2406F#5P喂喂……\x01",
            "我又不是小孩子。\x02\x03",

            "#2400F无论如何，多亏了这场比赛，\x01",
            "让我充分享受到了钓鱼的乐趣……\x02\x03",

            "#2409F可以说，我这次已经很满足了。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#12P#0005F哎……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6070")

    label("loc_599D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D47")
    OP_29(0x16, 0x1, 0x4)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0163
    ChrTalk(
        0xD,
        "#5S#11P……没有胜者！\x02",
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
        "#2405F#5P你、你说什么？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        "#12P#0005F没有……胜者？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xD,
        (
            "#11P唔，我集中注意力，\x01",
            "仔细量了又量……\x01",
            "不过还真是奇迹，尺寸竟然完全一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xD,
        "#11P嗯，也就是平局啦。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        "#12P#0006F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xE,
        (
            "#2406F#5P竟然是这样……\x01",
            "出现了微妙的结果呢。\x02\x03",

            "既然要比，就要彻底\x01",
            "分出个胜负，这是我的原则呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 300)
    Sleep(300)

    #C0170
    ChrTalk(
        0x101,
        (
            "#12P#0011F嗯、那个～……\x01",
            "但关于刚才的约定……\x02\x03",

            "……在这种情况下，该怎么办呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    #C0171
    ChrTalk(
        0xE,
        (
            "#2406F#5P……嗯，也罢。\x01",
            "我也差不多该回医院了吧。\x02",
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
        "#12P#0005F还、还真爽快啊……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#12P#0105F确实。\x01",
            "还以为会再稍微耍一会赖的……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xE,
        (
            "#2406F#5P喂喂……\x01",
            "我又不是小孩子。\x02\x03",

            "#2400F嗯，虽然是平局，\x01",
            "但我也充分享受到了钓鱼的乐趣……\x01",
            "这就足够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        "#12P#0005F哎……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6070")

    label("loc_5D47")

    OP_29(0x16, 0x1, 0x3)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0176
    ChrTalk(
        0xD,
        "#5S#11P……胜者，约亚西姆团员！\x02",
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
        "#12P#0006F怎、怎么会……！\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xD,
        (
            "#11P……约亚西姆钓到的鱼\x01",
            "确实要大得多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xD,
        "#11P我的眼光是不会有错的！\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#12P#0003F可恶……\x01",
            "是钓鱼方法不对吗……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    #C0181
    ChrTalk(
        0xE,
        (
            "#2409F#5P呵呵……\x01",
            "看来你们还差点火候呢。\x02\x03",

            "#2403F哈，但也不用泄气啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 300)
    Sleep(300)

    #C0182
    ChrTalk(
        0x101,
        (
            "#12P#0005F是、是……\x02\x03",

            "#0006F（任务失败了吗……\x01",
            "  要怎么跟塞拉小姐说明呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xE,
        (
            "#2400F#5P好了，比赛也玩得很开心……\x01",
            "差不多也该回医院了吧。\x02",
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
        "#12P#0005F……哎？\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        (
            "#12P#0105F……那、那个。\x01",
            "不是说，只有我们赢了比赛\x01",
            "您才会……？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xE,
        (
            "#2403F#5P嗯～我说过那种话吗？\x02\x03",

            "#2409F我记得自己好像一次也没有\x01",
            "说过不回医院啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6070")

    Jump("loc_635B")

    label("loc_6075")


    #C0187
    ChrTalk(
        0xE,
        (
            "#2400F#5P呵呵……\x01",
            "钓到满意的鱼了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        "#12P#0006F那个……关于这件事……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xD,
        "#11P其实啊，约亚西姆团员。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xD,
        (
            "#11P他们今天\x01",
            "好像什么都没钓到。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xD,
        (
            "#11P所以打算\x01",
            "放弃这次的比赛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0192
    ChrTalk(
        0xE,
        (
            "#2405F#5P咦，是这样吗？\x02\x03",

            "#2403F嗯、嗯～\x01",
            "总觉得有些扫兴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        (
            "#12P#0006F十、十分抱歉……\x01",
            "今天钓鱼的状态似乎很差。\x02\x03",

            "（任务失败了吗……\x01",
            "  要怎么跟塞拉小姐解释呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xE,
        (
            "#2403F#5P嗯～……\x01",
            "算啦，这种事偶尔也会发生吧。\x02\x03",

            "#2400F也罢也罢。\x01",
            "反正我已经玩够了……\x01",
            "差不多也该回医院了吧。\x02",
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
        "#12P#0005F……哎？\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        (
            "#12P#0105F……那、那个。\x01",
            "不是说，只有我们赢了比赛\x01",
            "您才会……？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xE,
        (
            "#2400F#5P嗯～我说过那种话吗？\x02\x03",

            "#2409F我记得自己好像一次也没有\x01",
            "说过不回医院啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_635B")


    #C0198
    ChrTalk(
        0x104,
        (
            "#12P#0306F这位医生……\x01",
            "其实只是想拖延些时间，\x01",
            "开心地钓鱼吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x103,
        "#12P#0211F……有这种感觉。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xE,
        "#2400F#5P呵呵，我可不明白你们在说什么呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 300)
    Sleep(300)

    #C0201
    ChrTalk(
        0xE,
        (
            "#2403F#5P……赛尔丹分部长，事情就是这样，\x01",
            "我先失陪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xD,
        (
            "#11P是吗，\x01",
            "期待你下次再来参加哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xE,
        "#2409F#5P哈哈，到时请多关照。\x02",
    )

    CloseMessageWindow()
    OP_95(0xD, 34960, -5600, -41280, 2000, 0x0)
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    #C0204
    ChrTalk(
        0xE,
        (
            "#2400F#5P……好了，特别任务支援科的各位，\x01",
            "回医院吧。\x02\x03",

            "这附近应该有巴士站，\x01",
            "我先走了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_64FA():

        label("loc_64FA")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_64FA")

    QueueWorkItem2(0x0, 1, lambda_64FA)

    def lambda_650C():

        label("loc_650C")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_650C")

    QueueWorkItem2(0x0, 1, lambda_650C)

    def lambda_651E():

        label("loc_651E")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_651E")

    QueueWorkItem2(0x0, 1, lambda_651E)

    def lambda_6530():

        label("loc_6530")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_6530")

    QueueWorkItem2(0x0, 1, lambda_6530)
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
            "#12P#0306F怎么说呢……\x01",
            "好像被他耍得团团转啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        "#12P#0106F是呀……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        (
            "#12P#0200F……我们也\x01",
            "赶快过去吧？\x02\x03",

            "#0206F不好好看住的话，\x01",
            "说不定又会让他逃掉了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0208
    ChrTalk(
        0x101,
        (
            "#5P#0000F是、是啊，\x01",
            "和约亚西姆医生坐同一班\x01",
            "巴士回医院吧。\x02",
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

    # Function_30_52D7 end

    def Function_31_6681(): pass

    label("Function_31_6681")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66AD")
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(800)
    Jump("Function_31_6681")

    label("loc_66AD")

    Return()

    # Function_31_6681 end

    def Function_32_66AE(): pass

    label("Function_32_66AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66DA")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(800)
    Jump("Function_32_66AE")

    label("loc_66DA")

    Return()

    # Function_32_66AE end

    def Function_33_66DB(): pass

    label("Function_33_66DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66ED")
    Call(0, 29)
    Return()

    label("loc_66ED")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【对话】\x01",              # 0
            "【确认比赛规则】\x01",      # 1
            "【放弃】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_673F"),
        (1, "loc_68B4"),
        (SWITCH_DEFAULT, "loc_69DC"),
    )


    label("loc_673F")

    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6819")

    #C0209
    ChrTalk(
        0xE,
        (
            "#2400F怎样，钓到了吗？\x02\x03",

            "不过，不必太过在意胜负，\x01",
            "充分享受钓鱼的乐趣吧。\x01",
            "我就在这里等着。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#0001F那可不行。\x02\x03",

            "我一定要赢得比赛，\x01",
            "把约亚西姆医生带回医院才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xE,
        "#2406F罗伊德，好认真啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_68AF")

    label("loc_6819")


    #C0212
    ChrTalk(
        0xE,
        (
            "#2400F说起来……\x01",
            "你是叫罗伊德吧。\x02\x03",

            "#2403F和我尊敬的资深前辈\x01",
            "特级钓师罗伊德先生\x01",
            "同名，真是好巧啊。\x02\x03",

            "#2409F虽然知道是不同的人，\x01",
            "但还是有点紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68AF")

    Jump("loc_69DC")

    label("loc_68B4")

    OP_60(0x0)

    #C0213
    ChrTalk(
        0xE,
        (
            "#2400F你们要是钓到了鱼，\x01",
            "也拿去给赛尔丹分部长看，\x01",
            "让他鉴定大小吧。\x02\x03",

            "#2400F如果你们钓到了比我刚才钓的\x01",
            "那条『云斑蛇头』更大的鱼，\x01",
            "我就回医院。\x02\x03",

            "不过要记好……\x01",
            "只能将钓上来的鱼给分部长看一次，\x01",
            "而且禁止离开这片河摊，去其它场所补给。\x02\x03",

            "……大概就是这样吧。\x01",
            "想确认规则的话，\x01",
            "随时可以问我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69DC")

    label("loc_69DC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_66DB end

    def Function_34_69ED(): pass

    label("Function_34_69ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CC1")
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
        "男子",
        (
            "#12P哎呀，大丰收大丰收，\x01",
            "真是找到一个好钓点呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0215
    NpcTalk(
        0xFE,
        "男子",
        (
            "#12P呀，你是……\x01",
            "钓公师团的团员吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#5P#0003F（姑、姑且算\x01",
            "  是吧……？）\x02\x03",

            "#0000F嗯，我叫罗伊德。\x01",
            "初次见面，请多关照。\x02",
        )
    )

    CloseMessageWindow()

    #N0217
    NpcTalk(
        0xFE,
        "男子",
        (
            "#12P……罗伊德……？\x01",
            "哈哈，这可真是巧啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        "#5P#0005F……哎？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "#12P我的名字也叫罗伊德，\x01",
            "在钓公师团的等级是\x01",
            "特级钓师。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "#12P我作为大赛的嘉宾，\x01",
            "受赛尔丹分部长的邀请，\x01",
            "从利贝尔王国而来。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "#12P在纪念庆典期间，我打算一直待在这边，\x01",
            "请多关照啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#5P#0005F请、请多关照。\x02\x03",

            "#0003F（艾丝蒂尔他们之前说的\x01",
            "  那个罗伊德先生，\x01",
            "  就是这位吗……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0xB7, 3)
    SetChrPos(0x0, 19950, -6300, -47640, 180)
    EventEnd(0x5)
    Jump("loc_71B8")

    label("loc_6CC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6D44")

    #C0223
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "游击士艾丝蒂尔\x01",
            "也来克洛斯贝尔了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "她也相当有一手呢。\x01",
            "我曾经向她提出过挑战，\x01",
            "结果还输了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71B8")

    label("loc_6D44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_713F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_703D")

    #C0225
    ChrTalk(
        0xFE,
        (
            "你们好像在进行钓鱼比赛嘛。\x01",
            "嗯，加油比吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "刚才我稍微瞄了一眼，约亚西姆\x01",
            "钓到的鱼相当大哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "要想赢他的话……如果不钓到\x01",
            "这个湖里最大的『巨鲶』，\x01",
            "恐怕是很难吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        "#0006F（好、好不安……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7035")

    #C0229
    ChrTalk(
        0xFE,
        (
            "哈哈，别摆出那没出息的表情啦，\x01",
            "最重要的还是享受比赛过程本身。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "……对了，机会难得，\x01",
            "我就给你们一点建议吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "与其一开始就以大鱼为目标，\x01",
            "倒不如先钓小鱼，\x01",
            "这才是钓大鱼的诀窍。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "因为蚯蚓之类的钓饵\x01",
            "是吸引不了大鱼的，\x01",
            "所以首先需要拿小鱼来当活饵。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "刚好，这个钓鱼点\x01",
            "好像只有小鱼。\x01",
            "你先用这些鱼饵钓钓看吧。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '虹丸ＥＸ'),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "获得了５个。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0235
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '红虫'),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "获得了５个。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('虹丸ＥＸ', 5)
    AddItemNumber('红虫', 5)

    #C0236
    ChrTalk(
        0x101,
        (
            "#0005F非、非常感谢。\x02\x03",

            "#0003F（……先钓小鱼吗？\x01",
            "  好，机会难得，就试试吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB7, 7)

    label("loc_7035")

    SetScenarioFlags(0x0, 3)
    Jump("loc_713A")

    label("loc_703D")


    #C0237
    ChrTalk(
        0xFE,
        (
            "深处的钓鱼点虽然有\x01",
            "『巨鲶』这种大鱼，\x01",
            "但没有活饵的话，它是不会上钩的。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "与其一开始就以大鱼为目标，\x01",
            "倒不如先钓小鱼，\x01",
            "之后再去深处的钓鱼点。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "刚好，这个钓鱼点\x01",
            "好像只有小鱼。\x01",
            "先钓一些当活饵吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "嗯，加油吧。\x01",
            "最重要的还是享受比赛过程本身。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_713A")

    Jump("loc_71B8")

    label("loc_713F")


    #C0241
    ChrTalk(
        0xFE,
        (
            "我作为大赛的嘉宾，\x01",
            "受赛尔丹分部长的邀请，\x01",
            "从利贝尔王国前来。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，我打算一直待在这边，\x01",
            "请多关照啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71B8")

    TalkEnd(0xFE)
    Return()

    # Function_34_69ED end

    def Function_35_71BC(): pass

    label("Function_35_71BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74B4")

    #C0243
    ChrTalk(
        0xFE,
        (
            "哦，你是罗伊德团员吗？\x01",
            "我早就听说过你的事啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "听说是克潘那家伙\x01",
            "邀请你入团的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "我是钓公师团·克洛斯贝尔分部的\x01",
            "分部长赛尔丹。\x01",
            "今后多关照啊，罗伊德团员！\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#0005F哎？等等……\x02\x03",

            "#0006F那个，我是什么时候……\x01",
            "加入钓公师团的啊？\x02\x03",

            "#0000F以前确实收下过\x01",
            "克潘先生赠送的钓竿，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "哇哈哈，那种小事就不用在意啦！\x01",
            "总之，你已经是\x01",
            "我们的同伴了！\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x101,
        (
            "#0006F（真、真是个强拉硬拽的人啊……）\x02\x03",

            "（算啦，反正大家也有着相同的爱好，\x01",
            " 在钓鱼方面，应该会很聊得来……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7454")

    #C0249
    ChrTalk(
        0xFE,
        (
            "对了，罗伊德团员，\x01",
            "听说你今天要和约亚西姆团员\x01",
            "比赛钓鱼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "虽然与正式钓鱼比赛\x01",
            "的形式不同，但也无伤大雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "想裁定胜负的时候，\x01",
            "就跟我说一声吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74AD")

    label("loc_7454")


    #C0252
    ChrTalk(
        0xFE,
        (
            "罗伊德团员也是来\x01",
            "参加钓鱼大赛的吗？\x01",
            "热烈欢迎啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "随便找个空地方，\x01",
            "自由垂钓吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74AD")

    SetScenarioFlags(0x71, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_74B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7519")

    #C0254
    ChrTalk(
        0xFE,
        (
            "说起来，钓公师团的分部\x01",
            "已经空无一人了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "大赛结束之后，\x01",
            "得赶快回去才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79C7")

    label("loc_7519")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7977")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【对话】\x01",                          # 0
            "【用持有的鱼和约亚西姆比赛】\x01",      # 1
            "【放弃】\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7581"),
        (1, "loc_7688"),
        (SWITCH_DEFAULT, "loc_7965"),
    )


    label("loc_7581")

    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_762D")

    #C0256
    ChrTalk(
        0xFE,
        (
            "我已经听约亚西姆团员说过了……\x01",
            "你们要进行钓鱼比赛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "虽然和正式钓鱼比赛\x01",
            "的形式不同，但也无伤大雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "想裁定胜负的时候，\x01",
            "就跟我说一声吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7683")

    label("loc_762D")


    #C0259
    ChrTalk(
        0xFE,
        (
            "听说你要和约亚西姆团员\x01",
            "进行钓鱼比赛啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "想裁定胜负的时候，\x01",
            "就跟我说一声吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7683")

    Jump("loc_7965")

    label("loc_7688")

    OP_60(0x0)
    Call(0, 36)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77C2")

    #C0261
    ChrTalk(
        0xFE,
        (
            "我已经鉴定过\x01",
            "约亚西姆团员钓到的\x01",
            "『云斑蛇头』的尺寸了。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 37)

    #C0262
    ChrTalk(
        0xFE,
        "要用这条鱼来决胜负吗？\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_7732"),
        (1, "loc_777E"),
        (SWITCH_DEFAULT, "loc_77BD"),
    )


    label("loc_7732")

    OP_60(0x1)

    #C0263
    ChrTalk(
        0xFE,
        "好的！\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "那就把约亚西姆团员叫来吧，\x01",
            "我们在那边裁定胜负。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 30)
    Jump("loc_77BD")

    label("loc_777E")

    OP_60(0x1)

    #C0265
    ChrTalk(
        0xFE,
        "怎么，不比吗？\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "钓到满意的鱼以后\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77BD")

    label("loc_77BD")

    Jump("loc_7960")

    label("loc_77C2")


    #C0267
    ChrTalk(
        0xFE,
        (
            "我已经鉴定过\x01",
            "约亚西姆团员钓到的\x01",
            "『云斑蛇头』的尺寸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        "差不多也该开始比赛了吧？\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "……本以为要比了呢……\x01",
            "可是，在这个钓鱼点能钓到的鱼，\x01",
            "你好像连一条也没有啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        "难道要弃权吗？\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_78BC"),
        (1, "loc_791F"),
        (SWITCH_DEFAULT, "loc_7960"),
    )


    label("loc_78BC")

    OP_60(0x1)

    #C0271
    ChrTalk(
        0xFE,
        (
            "唔，是吗……\x01",
            "那可真遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "那就把约亚西姆团员叫来吧，\x01",
            "得告诉他你弃权的事啊。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 30)
    Jump("loc_7960")

    label("loc_791F")

    OP_60(0x1)

    #C0273
    ChrTalk(
        0xFE,
        "唔，不是要弃权啊。\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "那么钓到鱼以后\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7960")

    label("loc_7960")

    Jump("loc_7965")

    label("loc_7965")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    Jump("loc_79C7")

    label("loc_7977")


    #C0275
    ChrTalk(
        0xFE,
        (
            "哦哦，你们也是来\x01",
            "参加钓鱼大赛的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "随便找个空地方，\x01",
            "自由享受垂钓吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79C7")

    TalkEnd(0xFE)
    Return()

    # Function_35_71BC end

    def Function_36_79CB(): pass

    label("Function_36_79CB")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_79F0")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_79F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A0B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_7A0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A26")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_7A26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A41")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_7A41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A5C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_7A5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A77")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_7A77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A92")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_7A92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7AA8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_7AA8")

    Return()

    # Function_36_79CB end

    def Function_37_7AA9(): pass

    label("Function_37_7AA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AF1")

    #C0277
    ChrTalk(
        0xD,
        (
            "而在你钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『巨鲶』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF6")

    label("loc_7AF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B3D")

    #C0278
    ChrTalk(
        0xD,
        (
            "而在你钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『云斑蛇头』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF6")

    label("loc_7B3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B89")

    #C0279
    ChrTalk(
        0xD,
        (
            "而在你钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『大口鲈鱼』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF6")

    label("loc_7B89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BD1")

    #C0280
    ChrTalk(
        0xD,
        (
            "而在你钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『鲑鱼』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF6")

    label("loc_7BD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C19")

    #C0281
    ChrTalk(
        0xD,
        (
            "而在你钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『黑鲑』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF6")

    label("loc_7C19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C63")

    #C0282
    ChrTalk(
        0xD,
        (
            "而在你钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『银伞鱼』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF6")

    label("loc_7C63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CB1")

    #C0283
    ChrTalk(
        0xD,
        (
            "而在你钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『蓝带神仙鱼』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF6")

    label("loc_7CB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CF6")

    #C0284
    ChrTalk(
        0xD,
        (
            "而在你钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『雪花蟹』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CF6")

    Return()

    # Function_37_7AA9 end

    def Function_38_7CF7(): pass

    label("Function_38_7CF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D4B")

    #C0285
    ChrTalk(
        0xD,
        (
            "#11P而在罗伊德团员钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『巨鲶』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FA4")

    label("loc_7D4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DA3")

    #C0286
    ChrTalk(
        0xD,
        (
            "#11P而在罗伊德团员钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『云斑蛇头』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FA4")

    label("loc_7DA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DFB")

    #C0287
    ChrTalk(
        0xD,
        (
            "#11P而在罗伊德团员钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『大口鲈鱼』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FA4")

    label("loc_7DFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E4F")

    #C0288
    ChrTalk(
        0xD,
        (
            "#11P而在罗伊德团员钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『鲑鱼』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FA4")

    label("loc_7E4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EA3")

    #C0289
    ChrTalk(
        0xD,
        (
            "#11P而在罗伊德团员钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『黑鲑』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FA4")

    label("loc_7EA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF9")

    #C0290
    ChrTalk(
        0xD,
        (
            "#11P而在罗伊德团员钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『银伞鱼』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FA4")

    label("loc_7EF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F53")

    #C0291
    ChrTalk(
        0xD,
        (
            "#11P而在罗伊德团员钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『蓝带神仙鱼』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FA4")

    label("loc_7F53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FA4")

    #C0292
    ChrTalk(
        0xD,
        (
            "#11P而在罗伊德团员钓到的鱼里，\x01",
            "尺寸最大的是……\x01",
            "『雪花蟹』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FA4")

    Return()

    # Function_38_7CF7 end

    SaveToFile()

Try(main)
