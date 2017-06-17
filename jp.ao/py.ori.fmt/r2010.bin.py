from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "水狂ナルセス",           # 1
        "ロックラッタ",           # 2
        "ロックラッタ",           # 3
        "鉄鋼ドリュー",           # 4
        "鉄鋼ドリュー",           # 5
        "幻獣",                   # 6
        "ミレイユ三尉",           # 7
        "警備隊員",               # 8
        "警備隊員",               # 9
        "警備隊員",               # 10
        "警備隊員",               # 11
        "警備隊員",               # 12
        "警備隊員",               # 13
        "警備隊員",               # 14
        "警備隊員",               # 15
        "警備隊員",               # 16
        "警備隊員",               # 17
        "狼",                     # 18
        "狼",                     # 19
        "狼",                     # 20
        "狼",                     # 21
        "狼",                     # 22
        "猟兵ザックス",           # 23
        "猟兵",                   # 24
        "猟兵",                   # 25
        "猟兵",                   # 26
        "猟兵",                   # 27
        "猟兵",                   # 28
        "猟兵",                   # 29
        "猟兵",                   # 30
        "クーガー",               # 31
        "クーガー",               # 32
        "クーガー",               # 33
        "SE制御",                 # 34
        "br2000",                 # 35
        "br2000",                 # 36
        "br2000",                 # 37
        "br2000",                 # 38
        "br2000",                 # 39
        "br2000",                 # 40
        "br2000",                 # 41
        "br2000",                 # 42
        "クロスベル市方面",       # 43
        "鉱山町マインツ方面",     # 44
    ))

    ATBonus("ATBonus_6FC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_71C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_592D", 6,   0,   0,   3,   2,   4,   0)
    Sepith("Sepith_5935", 3,   0,   1,   5,   3,   2,   0)
    Sepith("Sepith_5945", 6,   0,   8,   0,   1,   0,   6)
    Sepith("Sepith_593D", 0,   7,   2,   0,   1,   0,   4)
    Sepith("Sepith_5975", 11,  3,   6,   4,   6,   10,  8)

    MonsterBattlePostion("MonsterBattlePostion_73C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_740", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_744", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_748", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_74C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_750", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_754", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_758", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_7BC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_7C0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_7C4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_7C8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_7CC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_7D0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_7D4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_75C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_760", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_764", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_768", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_76C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_770", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_774", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_778", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7DC", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E0", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E4", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E8", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_7EC", 14, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_7F0", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_7F4", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_7F8", 0, 0, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_7FC", 0x0000, 52, 6, 45, 10, 1, 30, 0, "br2000", "Sepith_592D", 40, 30, 20, 0,
        (
            ("ms62500.dat", "ms62500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms62500.dat", "ms65900.dat", "ms62500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms62500.dat", "ms62500.dat", "ms65500.dat", "ms62500.dat", 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_934", 0x0000, 52, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_5935", 40, 30, 20, 0,
        (
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9D0", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_5945", 40, 30, 20, 0,
        (
            ("ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_898", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_593D", 40, 30, 20, 0,
        (
            ("ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A6C", 0x0000, 82, 6, 45, 6, 1, 30, 0, "br2000", "Sepith_5975", 100, 30, 20, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            (),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_B08", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62500.dat", "ms62500.dat", "ms62500.dat", "ms62500.dat", "ms62500.dat", "ms62500.dat", 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7453", "ed7453", "ATBonus_6FC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B4C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7453", "ed7453", "ATBonus_6FC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B90", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88702.dat", "ms88802.dat", "ms88802.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_7DC", "MonsterBattlePostion_7DC", "ed7454", "ed7453", "ATBonus_71C"),
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

    DeclMonster(-31720,  15370,   0,       0x1010000,    "BattleInfo_7FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-64090,  36330,   0,       0x1010000,    "BattleInfo_934", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-41420,  86260,   8000,    0x1010000,    "BattleInfo_9D0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(8029,    99200,   18000,   0x1010000,    "BattleInfo_898", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(27930,   93470,   18000,   0x1010000,    "BattleInfo_7FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(30600,   53520,   8000,    0x1010000,    "BattleInfo_934", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(17410,   30550,   8000,    0x1010000,    "BattleInfo_898", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-52720,  42390,   0,       0x1010000,    "BattleInfo_A6C", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(19680,   94830,   18000,   0x1010000,    "BattleInfo_A6C", 0,   24,  0xFFFF, 8,  9)

    DeclEvent(0x0040, 0, 11,  -64.7300033569336,     40.720001220703125,    -1.25,                 16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   8.0912504196167,       -5.090000152587891,    0.3125,                1.0])

    DeclActor(-87000,  0,       35750,   1200,    -87000,  1000,    35750,   0x007C, 0,  5,  0x0000)
    DeclActor(-10830,  5380,    59860,   1200,    -13360,  380,     68320,   0x007C, 0,  12, 0x0000)
    DeclActor(-58250,  0,       33120,   1200,    -58250,  0,       33120,   0x007C, 0,  7,  0x0000)
    DeclActor(27630,   8000,    38670,   1200,    27630,   8000,    38670,   0x007C, 0,  8,  0x0000)

    PlaceName(26.0, 0.0, -28.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(61.0, 18.0, 112.0, 0x0000, 0x0000, "鉱山町マインツ方面")

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
        "Function_0_D9C",          # 00, 0
        "Function_1_E54",          # 01, 1
        "Function_2_E73",          # 02, 2
        "Function_3_E92",          # 03, 3
        "Function_4_F88",          # 04, 4
        "Function_5_16DA",         # 05, 5
        "Function_6_182B",         # 06, 6
        "Function_7_182F",         # 07, 7
        "Function_8_1B8D",         # 08, 8
        "Function_9_1EEB",         # 09, 9
        "Function_10_1F04",        # 0A, 10
        "Function_11_2C02",        # 0B, 11
        "Function_12_2C7E",        # 0C, 12
        "Function_13_2F30",        # 0D, 13
        "Function_14_3B32",        # 0E, 14
        "Function_15_3BE2",        # 0F, 15
        "Function_16_3C16",        # 10, 16
        "Function_17_3C6A",        # 11, 17
        "Function_18_3CBE",        # 12, 18
        "Function_19_3D88",        # 13, 19
        "Function_20_3DBA",        # 14, 20
        "Function_21_3DEC",        # 15, 21
        "Function_22_3E25",        # 16, 22
        "Function_23_3E4A",        # 17, 23
        "Function_24_3EAD",        # 18, 24
        "Function_25_3F24",        # 19, 25
        "Function_26_3F63",        # 1A, 26
        "Function_27_3FDA",        # 1B, 27
        "Function_28_404A",        # 1C, 28
        "Function_29_40C1",        # 1D, 29
        "Function_30_40FA",        # 1E, 30
        "Function_31_4171",        # 1F, 31
        "Function_32_41BE",        # 20, 32
        "Function_33_4235",        # 21, 33
        "Function_34_4282",        # 22, 34
        "Function_35_42F9",        # 23, 35
        "Function_36_433F",        # 24, 36
        "Function_37_43B6",        # 25, 37
        "Function_38_4402",        # 26, 38
        "Function_39_4479",        # 27, 39
        "Function_40_44D3",        # 28, 40
        "Function_41_454A",        # 29, 41
        "Function_42_45A7",        # 2A, 42
        "Function_43_461E",        # 2B, 43
        "Function_44_467E",        # 2C, 44
        "Function_45_46DA",        # 2D, 45
        "Function_46_4727",        # 2E, 46
        "Function_47_478D",        # 2F, 47
        "Function_48_47D0",        # 30, 48
        "Function_49_482C",        # 31, 49
        "Function_50_48A2",        # 32, 50
        "Function_51_4912",        # 33, 51
        "Function_52_49D4",        # 34, 52
        "Function_53_4A4A",        # 35, 53
        "Function_54_4AD1",        # 36, 54
        "Function_55_4B2C",        # 37, 55
        "Function_56_4C73",        # 38, 56
        "Function_57_4CA8",        # 39, 57
        "Function_58_4D24",        # 3A, 58
        "Function_59_4D59",        # 3B, 59
        "Function_60_4D92",        # 3C, 60
        "Function_61_4DC7",        # 3D, 61
        "Function_62_4E00",        # 3E, 62
        "Function_63_4E35",        # 3F, 63
        "Function_64_4E6E",        # 40, 64
        "Function_65_4EC9",        # 41, 65
        "Function_66_4F69",        # 42, 66
        "Function_67_4FC4",        # 43, 67
        "Function_68_505E",        # 44, 68
        "Function_69_50B9",        # 45, 69
        "Function_70_50E7",        # 46, 70
        "Function_71_5134",        # 47, 71
        "Function_72_52E3",        # 48, 72
        "Function_73_5330",        # 49, 73
        "Function_74_535F",        # 4A, 74
        "Function_75_53AC",        # 4B, 75
        "Function_76_53E2",        # 4C, 76
        "Function_77_53FC",        # 4D, 77
        "Function_78_542D",        # 4E, 78
        "Function_79_54B7",        # 4F, 79
        "Function_80_56BA",        # 50, 80
        "Function_81_5733",        # 51, 81
        "Function_82_5785",        # 52, 82
        "Function_83_57F0",        # 53, 83
    ))


    def Function_0_D9C(): pass

    label("Function_0_D9C")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_DDC"),
        (1, "loc_DE8"),
        (2, "loc_DF4"),
        (3, "loc_E00"),
        (4, "loc_E0C"),
        (5, "loc_E18"),
        (6, "loc_E24"),
        (SWITCH_DEFAULT, "loc_E30"),
    )


    label("loc_DDC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_DE8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_DF4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E00")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E0C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E18")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E24")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E30")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E3C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E53")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E53")

    Return()

    # Function_0_D9C end

    def Function_1_E54(): pass

    label("Function_1_E54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E72")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_E54")

    label("loc_E72")

    Return()

    # Function_1_E54 end

    def Function_2_E73(): pass

    label("Function_2_E73")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E91")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_E73")

    label("loc_E91")

    Return()

    # Function_2_E73 end

    def Function_3_E92(): pass

    label("Function_3_E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_END)), "loc_EAC")
    SetChrPos(0x8, -13910, 5380, 56930, 295)

    label("loc_EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_EBF")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F5E")

    label("loc_EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_EDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_ED6")
    SetChrFlags(0x8, 0x80)

    label("loc_ED6")

    Jump("loc_F5E")

    label("loc_EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_EEE")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F5E")

    label("loc_EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EFC")
    Jump("loc_F5E")

    label("loc_EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F0A")
    Jump("loc_F5E")

    label("loc_F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F18")
    Jump("loc_F5E")

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F26")
    Jump("loc_F5E")

    label("loc_F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F34")
    Jump("loc_F5E")

    label("loc_F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F42")
    Jump("loc_F5E")

    label("loc_F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F50")
    Jump("loc_F5E")

    label("loc_F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F5E")
    SetChrFlags(0x8, 0x80)

    label("loc_F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F75")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 7)
    Event(0, 13)
    Jump("loc_F84")

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F84")
    ClearScenarioFlags(0x22, 1)
    Event(0, 83)

    label("loc_F84")

    Call(0, 9)
    Return()

    # Function_3_E92 end

    def Function_4_F88(): pass

    label("Function_4_F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_F9A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_FAE")
    OP_24(0x7C)
    ClearScenarioFlags(0x0, 7)
    Jump("loc_FCA")

    label("loc_FAE")

    SoundDistance(0x7C, 0xFFFFCE6E, 0x1504, 0x1205C, 0x7530, 0x249F0, 0x64, 0x0)

    label("loc_FCA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FF1")
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0xD, 0x4)
    Jump("loc_105A")

    label("loc_FF1")

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

    label("loc_105A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13EE")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)

    label("loc_13EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_146C")
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
    Jump("loc_14AE")

    label("loc_146C")

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

    label("loc_14AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1583")
    OP_11(0x87, 0xAA, 0xFF, 0xA, 0x73, 0x0)
    ClearMapObjFlags(0xE, 0x4)
    OP_74(0xE, 0x1E)
    OP_71(0xE, 0x0, 0x258, 0x0, 0x20)
    OP_C3(0x0, 0x1, 0x3, 0x0, 0x0, 0x1, -13740, -500, 5790, 2000, 2000, 0)
    OP_C3(0x1, 0x1, 0x3, 0x0, 0x0, 0x1, -11950, -500, 7590, 2000, 2000, 0)
    OP_C3(0x2, 0x1, 0x3, 0x0, 0x0, 0x1, -10120, -500, 9350, 2000, 2000, 0)
    OP_C3(0x3, 0x1, 0x3, 0x0, 0x0, 0x1, -8140, -500, 11380, 2000, 2000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg2.eff")
    Jump("loc_1589")

    label("loc_1583")

    SetMapObjFlags(0xE, 0x4)

    label("loc_1589")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -13360, 380, 68320, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15ED")
    OP_66(0x1, 0x1)

    label("loc_15ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15FF")
    OP_65(0x1, 0x1)

    label("loc_15FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1612")
    OP_70(0x0, 0x0)
    Jump("loc_1616")

    label("loc_1612")

    OP_70(0x0, 0x1E)

    label("loc_1616")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1677")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -58250, 0, 33120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_1677")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16C3")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 27630, 8000, 38670, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_16C3")

    OP_1C(0x0, 0xF, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x10, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    Return()

    # Function_4_F88 end

    def Function_5_16DA(): pass

    label("Function_5_16DA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DA")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3F, 1)"), scpexpr(EXPR_END)), "loc_1763")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E6, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_17D5")

    label("loc_1763")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x3F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x3F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17D5")

    Jump("loc_181F")

    label("loc_17DA")

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

    label("loc_181F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16DA end

    def Function_6_182B(): pass

    label("Function_6_182B")

    Call(1, 6)
    Return()

    # Function_6_182B end

    def Function_7_182F(): pass

    label("Function_7_182F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19E7")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_19C8")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0004
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C3")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_19C0")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_18E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_18E9)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_B08", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BB")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_19A2")
    Call(1, 5)
    Jump("loc_19BB")

    label("loc_19A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_19B8")
    Call(1, 4)
    Jump("loc_19BB")

    label("loc_19B8")

    Call(1, 3)

    label("loc_19BB")

    Jump("loc_19C3")

    label("loc_19C0")

    Call(1, 1)

    label("loc_19C3")

    Jump("loc_19DE")

    label("loc_19C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_19DE")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_19DE")

    TalkEnd(0xFF)
    Return()

    label("loc_19E7")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_1B72")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0006
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6D")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_1B6A")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1A93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1A93)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_B4C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B65")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B4C")
    Call(1, 5)
    Jump("loc_1B65")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B62")
    Call(1, 4)
    Jump("loc_1B65")

    label("loc_1B62")

    Call(1, 3)

    label("loc_1B65")

    Jump("loc_1B6D")

    label("loc_1B6A")

    Call(1, 1)

    label("loc_1B6D")

    Jump("loc_1B88")

    label("loc_1B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_1B88")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1B88")

    TalkEnd(0xFF)
    Return()

    # Function_7_182F end

    def Function_8_1B8D(): pass

    label("Function_8_1B8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D45")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_1D26")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0008
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D21")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1D1E")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C47():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1C47)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_B08", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D19")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D00")
    Call(1, 5)
    Jump("loc_1D19")

    label("loc_1D00")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D16")
    Call(1, 4)
    Jump("loc_1D19")

    label("loc_1D16")

    Call(1, 3)

    label("loc_1D19")

    Jump("loc_1D21")

    label("loc_1D1E")

    Call(1, 1)

    label("loc_1D21")

    Jump("loc_1D3C")

    label("loc_1D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1D3C")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1D3C")

    TalkEnd(0xFF)
    Return()

    label("loc_1D45")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_1ED0")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ECB")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1EC8")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1DF1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1DF1)
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
    Battle("BattleInfo_B4C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC3")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EAA")
    Call(1, 5)
    Jump("loc_1EC3")

    label("loc_1EAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EC0")
    Call(1, 4)
    Jump("loc_1EC3")

    label("loc_1EC0")

    Call(1, 3)

    label("loc_1EC3")

    Jump("loc_1ECB")

    label("loc_1EC8")

    Call(1, 1)

    label("loc_1ECB")

    Jump("loc_1EE6")

    label("loc_1ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1EE6")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1EE6")

    TalkEnd(0xFF)
    Return()

    # Function_8_1B8D end

    def Function_9_1EEB(): pass

    label("Function_9_1EEB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F03")
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)

    label("loc_1F03")

    Return()

    # Function_9_1EEB end

    def Function_10_1F04(): pass

    label("Function_10_1F04")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x0, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F1C")
    SetScenarioFlags(0x0, 6)

    label("loc_1F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_END)), "loc_1F28")
    SetScenarioFlags(0x0, 6)

    label("loc_1F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2176")
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0012
    ChrTalk(
        0x8,
        "フゥム、キミは誰だい？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#00003Fえっと、釣公師団の\x01",
            "ロイドと言います。\x02\x03",

            "#00005F釣皇倶楽部の方……ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        "オフコース。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "いかにもボクは釣傑四天王の\x01",
            "エレガント＆スタイリッシュガイ、\x01",
            "《水狂》ナルセスさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "フフ、何でもキミたち、\x01",
            "ボクにチャレンジするんだってね？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "ならまずは、ここクロスベルの\x01",
            "モストビュリホーフィッシュを\x01",
            "フィッシングしてみせたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00006Fええっと、クロスベルで\x01",
            "最も美しい魚、ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "ハッハー、まあじっくり\x01",
            "シンキングしてみることだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "ボクはここでじっくり\x01",
            "ウェイティングさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 3)

    label("loc_2176")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2180")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21CC")

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
    Jump("loc_21D6")

    label("loc_21CC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28BF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A0")

    #C0021
    ChrTalk(
        0x8,
        (
            "フム、ではフィッシングノートを\x01",
            "チェックさせてもらうよ？\x02",
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
            "そう、ノーブルカルプ――\x01",
            "これこそがクロスベルの\x01",
            "モストビュリホーフィッシュさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        "#4Sグレイト＆ビュリホーーッ！#3S\x02",
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
        "#00012Fど、どうも……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        "ハッハー、どういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "それではボクとの\x01",
            "《爆釣ファイト》だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "美しさ勝負……\x01",
            "では優劣を付けられないからね。\x01",
            "ただしサイズとは違う基準――\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "『爆釣プライスファイト』で\x01",
            "ウィナーを決めることにしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "チャンスはワンタイム――\x01\x07\x02",

            "釣った魚の値段が\x01",
            "高かった方がウィナー\x07\x00",
            "さ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 4)
    Jump("loc_2527")

    label("loc_24A0")


    #C0030
    ChrTalk(
        0x8,
        (
            "『爆釣プライスファイト』で\x01",
            "ボクにチャレンジするかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "チャンスはワンタイム――\x01\x07\x02",

            "釣った魚の値段が\x01",
            "高かった方がウィナー\x07\x00",
            "さ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2527")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《水狂》ナルセスに、\x01",
            "『爆釣プライスファイト』を挑みますか？\x07\x00\x02",
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
        (0, "loc_25C8"),
        (1, "loc_27E4"),
        (SWITCH_DEFAULT, "loc_280D"),
    )


    label("loc_25C8")


    #C0033
    ChrTalk(
        0x8,
        (
            "ゲレイトッ！\x01",
            "ではさっそくファイティングだ。\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271D")
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

    label("loc_271D")

    OP_68(-12100, 4380, 60440, 0)
    MoveCamera(25, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, -13910, 5380, 56930, 46)
    OP_93(0xFE, 0xE1, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_277C")
    Call(0, 80)
    Jump("loc_27A3")

    label("loc_277C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2792")
    Call(0, 82)
    Jump("loc_27A3")

    label("loc_2792")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A3")
    Call(0, 81)

    label("loc_27A3")

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
    Jump("loc_280D")

    label("loc_27E4")


    #C0034
    ChrTalk(
        0x8,
        "ナット・グレイト……残念だよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_280D")

    label("loc_280D")

    Jump("loc_28BA")

    label("loc_2812")


    #C0035
    ChrTalk(
        0x8,
        (
            "フム、ではフィッシングノートを\x01",
            "チェックさせてもらうよ？\x02",
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
            "ノーグッド……\x01",
            "ナット・ビュリホーだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        "シンキングアゲインしてきたまえ。\x02",
    )

    CloseMessageWindow()

    label("loc_28BA")

    Jump("loc_2BF9")

    label("loc_28BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_28F0")
    Jump("loc_2BF9")

    label("loc_28F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2949")

    #C0038
    ChrTalk(
        0x8,
        (
            "フィッシュをキャッチするボク……\x01",
            "ン～～、ヴェリヴェリビュリホーーッ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF9")

    label("loc_2949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2957")
    Jump("loc_2BF9")

    label("loc_2957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_29A0")

    #C0039
    ChrTalk(
        0x8,
        (
            "レインにさらされるボク……\x01",
            "ン～～、コーケティッシュ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF9")

    label("loc_29A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2A00")

    #C0040
    ChrTalk(
        0x8,
        "ムゥ、さっきから何かノイジーだね。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "ン～～、ナット・ビュリホーーーーッ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BF9")

    label("loc_2A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A53")

    #C0042
    ChrTalk(
        0x8,
        (
            "フィッシュをステアするボク……\x01",
            "ン～～、ソフィスティケイテッド！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF9")

    label("loc_2A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2AA2")

    #C0043
    ChrTalk(
        0x8,
        (
            "釣りエサをセットするボク……\x01",
            "ン～～、ワンダホウーーーーッ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF9")

    label("loc_2AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2AEB")

    #C0044
    ChrTalk(
        0x8,
        (
            "ロッドをスイングするボク……\x01",
            "ン～～、マーヴェラスッ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF9")

    label("loc_2AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B36")

    #C0045
    ChrTalk(
        0x8,
        (
            "大自然にスタンドするボク……\x01",
            "ン～～、エクセレントゥッ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF9")

    label("loc_2B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2BE2")

    #C0046
    ChrTalk(
        0x8,
        (
            "水面にリファインドするボク……\x01",
            "ン～～、ビュリホーーーーッ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BDD")

    #C0047
    ChrTalk(
        0x101,
        (
            "#00003F（ここなら何か釣れそうだけど……\x01",
            "  先客がいるなら止めておくか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BDD")

    Jump("loc_2BF9")

    label("loc_2BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2BF0")
    Jump("loc_2BF9")

    label("loc_2BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2BF9")

    label("loc_2BF9")

    Jump("loc_2180")

    label("loc_2BFE")

    TalkEnd(0xFE)
    Return()

    # Function_10_1F04 end

    def Function_11_2C02(): pass

    label("Function_11_2C02")

    Battle("BattleInfo_B90", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C49")
    OP_90(0x0, -62530, 0, 33250, 180)
    EventEnd(0x5)
    SetChrFlags(0xD, 0x8000)
    Jump("loc_2C7D")

    label("loc_2C49")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5C")
    Jump("loc_2C7D")

    label("loc_2C5C")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0xD, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x3C, 1)
    EventEnd(0x5)

    label("loc_2C7D")

    Return()

    # Function_11_2C02 end

    def Function_12_2C7E(): pass

    label("Function_12_2C7E")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0048
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2B")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D64")
    MiniGame(0x6, 0x8, 0xFFFFD5B2, 0x1504, 0xE9D4, 0x14E, 0xFFFFCBD0, 0x17C, 0x10AE0)
    Jump("loc_2F2B")

    label("loc_2D64")

    MiniGame(0x6, 0x9, 0xFFFFD5B2, 0x1504, 0xE9D4, 0x14E, 0xFFFFCBD0, 0x17C, 0x10AE0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F2B")
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
        "ロイド",
        (
            "#00011Fこ、これは……\x01",
            "またすごく綺麗な大物だな。\x02\x03",

            "#00003Fエーゼルに似てるけど……\x01",
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

    label("loc_2F2B")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_12_2C7E end

    def Function_13_2F30(): pass

    label("Function_13_2F30")

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
            "#07903F──作戦を開始する。\x02\x03",

            "#07901Fクロスベル警備隊所属、\x01",
            "独立解放部隊、および神狼部隊……\x02",
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
        "#07907F#4S戦闘開始#8Rオープン・コンバット#！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(80, 0, -1, -1)
    SetChrName("警備隊員たち")

    #A0053
    AnonymousTalk(
        0xFF,
        "#5Sイエス・マム！\x02",
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
    SetChrName("狼たち")

    #A0054
    AnonymousTalk(
        0xFF,
        "#5Sウォン！\x02",
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

    # Function_13_2F30 end

    def Function_14_3B32(): pass

    label("Function_14_3B32")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3B6A"),
        (1, "loc_3B76"),
        (2, "loc_3B82"),
        (3, "loc_3B8E"),
        (4, "loc_3B9A"),
        (5, "loc_3BA6"),
        (6, "loc_3BB2"),
        (SWITCH_DEFAULT, "loc_3BBE"),
    )


    label("loc_3B6A")

    OP_A0(0xFE, 1950, 0x0, 0xFB)
    Jump("loc_3BCA")

    label("loc_3B76")

    OP_A0(0xFE, 2050, 0x0, 0xFB)
    Jump("loc_3BCA")

    label("loc_3B82")

    OP_A0(0xFE, 2100, 0x0, 0xFB)
    Jump("loc_3BCA")

    label("loc_3B8E")

    OP_A0(0xFE, 1900, 0x0, 0xFB)
    Jump("loc_3BCA")

    label("loc_3B9A")

    OP_A0(0xFE, 2150, 0x0, 0xFB)
    Jump("loc_3BCA")

    label("loc_3BA6")

    OP_A0(0xFE, 1850, 0x0, 0xFB)
    Jump("loc_3BCA")

    label("loc_3BB2")

    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("loc_3BCA")

    label("loc_3BBE")

    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("loc_3BCA")

    label("loc_3BCA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BE1")
    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("loc_3BCA")

    label("loc_3BE1")

    Return()

    # Function_14_3B32 end

    def Function_15_3BE2(): pass

    label("Function_15_3BE2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C15")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C09")
    OP_4C(0xFE, 0x0)
    Jump("loc_3C0D")

    label("loc_3C09")

    OP_4B(0xFE, 0x0)

    label("loc_3C0D")

    Sleep(500)
    Jump("Function_15_3BE2")

    label("loc_3C15")

    Return()

    # Function_15_3BE2 end

    def Function_16_3C16(): pass

    label("Function_16_3C16")

    SetChrChipByIndex(0xFE, 0x25)

    label("loc_3C1A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C69")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 1050, 1700, 0, -20, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("loc_3C1A")

    label("loc_3C69")

    Return()

    # Function_16_3C16 end

    def Function_17_3C6A(): pass

    label("Function_17_3C6A")

    SetChrChipByIndex(0xFE, 0x2F)

    label("loc_3C6E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CBD")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x3)
    Jump("loc_3C6E")

    label("loc_3CBD")

    Return()

    # Function_17_3C6A end

    def Function_18_3CBE(): pass

    label("Function_18_3CBE")

    SetChrChipByIndex(0xFE, 0x1F)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3D10"),
        (1, "loc_3D1C"),
        (2, "loc_3D28"),
        (3, "loc_3D34"),
        (4, "loc_3D40"),
        (5, "loc_3D4C"),
        (6, "loc_3D58"),
        (SWITCH_DEFAULT, "loc_3D64"),
    )


    label("loc_3D10")

    OP_A0(0xFE, 1200, 0x0, 0x5)
    Jump("loc_3D70")

    label("loc_3D1C")

    OP_A0(0xFE, 1300, 0x0, 0x5)
    Jump("loc_3D70")

    label("loc_3D28")

    OP_A0(0xFE, 1400, 0x0, 0x5)
    Jump("loc_3D70")

    label("loc_3D34")

    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3D70")

    label("loc_3D40")

    OP_A0(0xFE, 1600, 0x0, 0x5)
    Jump("loc_3D70")

    label("loc_3D4C")

    OP_A0(0xFE, 1700, 0x0, 0x5)
    Jump("loc_3D70")

    label("loc_3D58")

    OP_A0(0xFE, 1800, 0x0, 0x5)
    Jump("loc_3D70")

    label("loc_3D64")

    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3D70")

    label("loc_3D70")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D87")
    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3D70")

    label("loc_3D87")

    Return()

    # Function_18_3CBE end

    def Function_19_3D88(): pass

    label("Function_19_3D88")

    SetChrChipByIndex(0xFE, 0x1E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DA2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DB9")
    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3DA2")

    label("loc_3DB9")

    Return()

    # Function_19_3D88 end

    def Function_20_3DBA(): pass

    label("Function_20_3DBA")

    SetChrChipByIndex(0xFE, 0x3D)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DD4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DEB")
    OP_A0(0xFE, 1500, 0x0, 0x4)
    Jump("loc_3DD4")

    label("loc_3DEB")

    Return()

    # Function_20_3DBA end

    def Function_21_3DEC(): pass

    label("Function_21_3DEC")

    SetChrChipByIndex(0xFE, 0x3C)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E06")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E24")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_3E06")

    label("loc_3E24")

    Return()

    # Function_21_3DEC end

    def Function_22_3E25(): pass

    label("Function_22_3E25")

    SetChrChipByIndex(0xFE, 0x3E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Return()

    # Function_22_3E25 end

    def Function_23_3E4A(): pass

    label("Function_23_3E4A")

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

    # Function_23_3E4A end

    def Function_24_3EAD(): pass

    label("Function_24_3EAD")

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

    # Function_24_3EAD end

    def Function_25_3F24(): pass

    label("Function_25_3F24")

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

    # Function_25_3F24 end

    def Function_26_3F63(): pass

    label("Function_26_3F63")

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

    # Function_26_3F63 end

    def Function_27_3FDA(): pass

    label("Function_27_3FDA")

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

    # Function_27_3FDA end

    def Function_28_404A(): pass

    label("Function_28_404A")

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

    # Function_28_404A end

    def Function_29_40C1(): pass

    label("Function_29_40C1")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2E)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -42600, 8140, 71650, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 17)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_29_40C1 end

    def Function_30_40FA(): pass

    label("Function_30_40FA")

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

    # Function_30_40FA end

    def Function_31_4171(): pass

    label("Function_31_4171")

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

    # Function_31_4171 end

    def Function_32_41BE(): pass

    label("Function_32_41BE")

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

    # Function_32_41BE end

    def Function_33_4235(): pass

    label("Function_33_4235")

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

    # Function_33_4235 end

    def Function_34_4282(): pass

    label("Function_34_4282")

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

    # Function_34_4282 end

    def Function_35_42F9(): pass

    label("Function_35_42F9")

    SetChrChipByIndex(0xFE, 0x33)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45650, 8000, 72400, 4000, 0x0)
    OP_95(0xFE, -44000, 6110, 64450, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_42F9 end

    def Function_36_433F(): pass

    label("Function_36_433F")

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

    # Function_36_433F end

    def Function_37_43B6(): pass

    label("Function_37_43B6")

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

    # Function_37_43B6 end

    def Function_38_4402(): pass

    label("Function_38_4402")

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

    # Function_38_4402 end

    def Function_39_4479(): pass

    label("Function_39_4479")

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

    # Function_39_4479 end

    def Function_40_44D3(): pass

    label("Function_40_44D3")

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

    # Function_40_44D3 end

    def Function_41_454A(): pass

    label("Function_41_454A")

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

    # Function_41_454A end

    def Function_42_45A7(): pass

    label("Function_42_45A7")

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

    # Function_42_45A7 end

    def Function_43_461E(): pass

    label("Function_43_461E")

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

    # Function_43_461E end

    def Function_44_467E(): pass

    label("Function_44_467E")

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

    # Function_44_467E end

    def Function_45_46DA(): pass

    label("Function_45_46DA")

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

    # Function_45_46DA end

    def Function_46_4727(): pass

    label("Function_46_4727")

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

    # Function_46_4727 end

    def Function_47_478D(): pass

    label("Function_47_478D")

    BeginChrThread(0xFE, 0, 0, 20)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -46300, 8000, 72350, 5000, 0x0)
    OP_95(0xFE, -46300, 7050, 66650, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_47_478D end

    def Function_48_47D0(): pass

    label("Function_48_47D0")

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

    # Function_48_47D0 end

    def Function_49_482C(): pass

    label("Function_49_482C")

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

    # Function_49_482C end

    def Function_50_48A2(): pass

    label("Function_50_48A2")

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

    # Function_50_48A2 end

    def Function_51_4912(): pass

    label("Function_51_4912")

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

    # Function_51_4912 end

    def Function_52_49D4(): pass

    label("Function_52_49D4")

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

    # Function_52_49D4 end

    def Function_53_4A4A(): pass

    label("Function_53_4A4A")

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

    # Function_53_4A4A end

    def Function_54_4AD1(): pass

    label("Function_54_4AD1")

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

    # Function_54_4AD1 end

    def Function_55_4B2C(): pass

    label("Function_55_4B2C")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -44100, 5070, 62200, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    label("loc_4B52")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C72")
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x34)
    SetChrSubChip(0x14, 0x2)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x4)
    OP_9D(0x14, 0xFFFF53BC, 0x11F8, 0xF582, 0x3E8, 0xFA0)
    SetChrFlags(0x14, 0x4)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(532, 0, 60, 0)

    def lambda_4BAB():
        OP_A0(0xFE, 1500, 0x3, 0x4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4BAB)
    Sound(540, 0, 60, 0)
    Sound(501, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4BCC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4BCC)
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

    def lambda_4C1E():
        OP_A0(0xFE, 1000, 0x2, 0x4)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_4C1E)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4C30():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C30)
    SetChrChipByIndex(0x14, 0x34)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x4)
    OP_9B(0x1, 0x14, 0x0, 0xFFFFFD12, 0x2710, 0x0)
    SetChrFlags(0x14, 0x4)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x4)
    Sleep(1000)
    Jump("loc_4B52")

    label("loc_4C72")

    Return()

    # Function_55_4B2C end

    def Function_56_4C73(): pass

    label("Function_56_4C73")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_56_4C73 end

    def Function_57_4CA8(): pass

    label("Function_57_4CA8")

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

    # Function_57_4CA8 end

    def Function_58_4D24(): pass

    label("Function_58_4D24")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_58_4D24 end

    def Function_59_4D59(): pass

    label("Function_59_4D59")

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

    # Function_59_4D59 end

    def Function_60_4D92(): pass

    label("Function_60_4D92")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x6590, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_60_4D92 end

    def Function_61_4DC7(): pass

    label("Function_61_4DC7")

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

    # Function_61_4DC7 end

    def Function_62_4E00(): pass

    label("Function_62_4E00")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x6978, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_62_4E00 end

    def Function_63_4E35(): pass

    label("Function_63_4E35")

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

    # Function_63_4E35 end

    def Function_64_4E6E(): pass

    label("Function_64_4E6E")

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

    # Function_64_4E6E end

    def Function_65_4EC9(): pass

    label("Function_65_4EC9")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -42550, 4800, 63150, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x15, 0x34)

    def lambda_4EF8():
        OP_A0(0xFE, 1500, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4EF8)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4F0A():
        OP_96(0xFE, 0xFFFF59CA, 0x141E, 0xFB2C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4F0A)

    def lambda_4F24():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_4F24)
    Sound(538, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4F4B():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4F4B)
    WaitChrThread(0x15, 1)
    SetChrFlags(0x15, 0x4)
    Return()

    # Function_65_4EC9 end

    def Function_66_4F69(): pass

    label("Function_66_4F69")

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

    # Function_66_4F69 end

    def Function_67_4FC4(): pass

    label("Function_67_4FC4")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45400, 5030, 63600, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x16, 0x34)

    def lambda_4FF3():
        OP_A0(0xFE, 1500, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_4FF3)
    ClearChrFlags(0xFE, 0x4)

    def lambda_5005():
        OP_96(0xFE, 0xFFFF4EA8, 0x14F0, 0xFCEE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5005)

    def lambda_501F():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_501F)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5040():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5040)
    WaitChrThread(0x16, 1)
    SetChrFlags(0x16, 0x4)
    Return()

    # Function_67_4FC4 end

    def Function_68_505E(): pass

    label("Function_68_505E")

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

    # Function_68_505E end

    def Function_69_50B9(): pass

    label("Function_69_50B9")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45250, 3920, 59150, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x3E8)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_69_50B9 end

    def Function_70_50E7(): pass

    label("Function_70_50E7")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4844, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x13EC, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x13EC, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x13EC, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_70_50E7 end

    def Function_71_5134(): pass

    label("Function_71_5134")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -46400, 4850, 61800, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 19)
    Sleep(1000)

    label("loc_5165")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52E2")
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

    def lambda_5208():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_5208)
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

    def lambda_5275():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5275)
    Sound(657, 0, 50, 0)

    def lambda_5290():
        OP_A0(0xFE, 1500, 0x3, 0x5)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_5290)

    def lambda_529D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_529D)
    ClearChrFlags(0x19, 0x4)
    OP_9B(0x1, 0x19, 0x0, 0xFFFFFC18, 0x2710, 0x0)
    SetChrFlags(0x19, 0x4)
    WaitChrThread(0xFE, 3)
    WaitChrThread(0xFE, 0)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 19)
    Jump("loc_5165")

    label("loc_52E2")

    Return()

    # Function_71_5134 end

    def Function_72_52E3(): pass

    label("Function_72_52E3")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4650, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_72_52E3 end

    def Function_73_5330(): pass

    label("Function_73_5330")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -41750, 4270, 60750, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 19)
    Return()

    # Function_73_5330 end

    def Function_74_535F(): pass

    label("Function_74_535F")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xBB8, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x1450, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_74_535F end

    def Function_75_53AC(): pass

    label("Function_75_53AC")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -43200, 3150, 58750, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 19)
    Return()

    # Function_75_53AC end

    def Function_76_53E2(): pass

    label("Function_76_53E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53FB")
    Sound(845, 0, 50, 0)
    Sleep(500)
    Jump("Function_76_53E2")

    label("loc_53FB")

    Return()

    # Function_76_53E2 end

    def Function_77_53FC(): pass

    label("Function_77_53FC")

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

    # Function_77_53FC end

    def Function_78_542D(): pass

    label("Function_78_542D")

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

    # Function_78_542D end

    def Function_79_54B7(): pass

    label("Function_79_54B7")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0055
    ChrTalk(
        0x8,
        (
            "フゥム、やるじゃないか……\x01",
            "キミ、なかなかビュリホーだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "それじゃ、ボクに勝った証として\x01",
            "ディス・メダルをプレゼントだ。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x29),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x29, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0058
    ChrTalk(
        0x101,
        "#00012Fど、どうも……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "フフ、ではこれよりキミは\x01",
            "『水狂ハンター』を名乗りたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "ま、といってもボクに\x01",
            "勝ったのは、ただのワンタイム。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "これからもビューティーを\x01",
            "ポリッシュするのを忘れずにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#00006Fは、はあ……\x02",
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

    # Function_79_54B7 end

    def Function_80_56BA(): pass

    label("Function_80_56BA")


    #C0063
    ChrTalk(
        0x8,
        (
            "フフ、というわけで\x01",
            "バトルはボクのヴィクトリーだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "ま、せいぜいフェイスでも\x01",
            "ウォッシュして出直してくるんだね。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_80_56BA end

    def Function_81_5733(): pass

    label("Function_81_5733")


    #C0065
    ChrTalk(
        0x8,
        (
            "フゥム、もしかして\x01",
            "トイレットタイムかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "……ナット・ビュリホーだね。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_81_5733 end

    def Function_82_5785(): pass

    label("Function_82_5785")


    #C0067
    ChrTalk(
        0x8,
        (
            "ンン～、ナット・\x01",
            "ビュリホーな結果だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "まあまた、エブリタイム\x01",
            "ファイティングしようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_82_5785 end

    def Function_83_57F0(): pass

    label("Function_83_57F0")

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

    # Function_83_57F0 end

    SaveToFile()

Try(main)
