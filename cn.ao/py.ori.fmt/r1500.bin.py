from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r1500.bin",                # FileName
        "r1500",                    # MapName
        "r1500",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r0020", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x09,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 96, 0, 4, 0, 5],
    )

    BuildStringList((
        "r1500",                  # 0
        "比利",                   # 1
        "游客",                   # 2
        "游客",                   # 3
        "游客",                   # 4
        "游客",                   # 5
        "游客",                   # 6
        "游客",                   # 7
        "青年",                   # 8
        "警官",                   # 9
        "警官",                   # 10
        "比利的货车",             # 11
        "费瑟尔",                 # 12
        "巴士",                   # 13
        "国防军士兵",             # 14
        "国防军士兵",             # 15
        "国防军士兵",             # 16
        "国防军士兵",             # 17
        "国防军士兵",             # 18
        "国防军士兵",             # 19
        "电熊",                   # 20
        "电熊",                   # 21
        "强壮巨骨猩",             # 22
        "强壮巨骨猩",             # 23
        "警官",                   # 24
        "警官",                   # 25
        "警官",                   # 26
        "警官",                   # 27
        "警官",                   # 28
        "警车",                   # 29
        "警车",                   # 30
        "车",                     # 31
        "梅尔卡瓦",               # 32
        "梅尔卡瓦",               # 33
        "梅尔卡瓦",               # 34
        "SE控制",                 # 35
        "br1500",                 # 36
        "br1500",                 # 37
        "br1500",                 # 38
        "br1500",                 # 39
        "br1500",                 # 40
        "br1500",                 # 41
        "br1500",                 # 42
        "克洛斯贝尔市方向",       # 43
        "乌尔斯拉医科大学方向",   # 44
        "克洛斯贝尔空港方向",     # 45
    ))

    ATBonus("ATBonus_770", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_5BDF", 5,   3,   0,   8,   0,   4,   3)
    Sepith("Sepith_5BF7", 10,  6,   0,   0,   3,   0,   5)
    Sepith("Sepith_5BEF", 0,   10,  0,   7,   4,   3,   0)
    Sepith("Sepith_5BE7", 9,   0,   6,   3,   0,   0,   5)
    Sepith("Sepith_5C17", 3,   10,  0,   8,   3,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_7D0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_7DC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7EC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_830", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_834", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_838", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_83C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_840", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_844", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_848", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_84C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_7B0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_7BC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7CC", 2, 13, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_850", 0x0000, 58, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_5BDF", 30, 45, 20, 5,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
        )
    )

    BattleInfo(
        "BattleInfo_AA8", 0x0000, 58, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_5BF7", 30, 45, 20, 5,
        (
            ("ms65800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms65800.dat", "ms65800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms65800.dat", "ms63600.dat", "ms65800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms65800.dat", "ms65800.dat", "ms66600.dat", "ms65800.dat", 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
        )
    )

    BattleInfo(
        "BattleInfo_9E0", 0x0010, 58, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_5BEF", 60, 25, 10, 5,
        (
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms63600.dat", "ms66600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "ms63600.dat", 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms63600.dat", "ms63600.dat", "ms62100.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
        )
    )

    BattleInfo(
        "BattleInfo_918", 0x0000, 58, 6, 45, 10, 1, 45, 0, "br1500", "Sepith_5BE7", 30, 45, 20, 5,
        (
            ("ms66600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms66600.dat", "ms66600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms66600.dat", "ms62100.dat", "ms66600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms66600.dat", "ms66600.dat", "ms69700.dat", "ms66600.dat", 0, 0, 0, 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
        )
    )

    BattleInfo(
        "BattleInfo_B70", 0x0000, 58, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_5C17", 30, 45, 20, 5,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
        )
    )

    # event battle count: 4

    BattleInfo(
        "BattleInfo_C38", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62100.dat", "ms62100.dat", "ms62100.dat", "ms62100.dat", "ms62100.dat", "ms62100.dat", "ms62100.dat", "ms62100.dat", "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7453", "ed7453", "ATBonus_770"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C7C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7453", "ed7453", "ATBonus_770"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch23600.itc",                   # 00
        "chr/ch24000.itc",                   # 01
        "chr/ch22300.itc",                   # 02
        "chr/ch21000.itc",                   # 03
        "chr/ch27900.itc",                   # 04
        "chr/ch22800.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch30000.itc",                   # 07
        "chr/ch46100.itc",                   # 08
        "chr/ch20400.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch62150.itc",               # 10
        "monster/ch62151.itc",               # 11
        "monster/ch66650.itc",               # 12
        "monster/ch66651.itc",               # 13
        "monster/ch63650.itc",               # 14
        "monster/ch63650.itc",               # 15
        "monster/ch65850.itc",               # 16
        "monster/ch65851.itc",               # 17
        "monster/ch69750.itc",               # 18
        "monster/ch69750.itc",               # 19
        "monster/ch70250.itc",               # 1A
        "monster/ch70251.itc",               # 1B
    ))

    DeclNpc(14810,   0,       -20889,  315,  389,  0x0, 0,   0,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(5809,    0,       -9000,   135,  389,  0x0, 0,   1,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(6719,    0,       -9920,   315,  389,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(13380,   0,       -16639,  270,  389,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(5809,    0,       -9000,   135,  389,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(5809,    0,       -9000,   135,  389,  0x0, 0,   5,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(6719,    0,       -9920,   315,  389,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(6320,    0,       -21829,  270,  389,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(12579,   0,       -14689,  270,  389,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(13380,   0,       -19639,  270,  389,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(10000,   0,       -10000,  0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(3490,    0,       -8840,   0,    389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-13859,  0,       -95169,  270,  484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(38020,   0,       -116089, 270,  484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-13859,  0,       -95169,  270,  484,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(38020,   0,       -116089, 270,  484,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-18740,  -70990,  0,       0x1010000,    "BattleInfo_850", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-19320,  -73460,  10,      0x1010000,    "BattleInfo_850", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-9910,   -96620,  10,      0x1010000,    "BattleInfo_AA8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-20260,  -97980,  0,       0x1010000,    "BattleInfo_9E0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(16920,   -84000,  10,      0x1010000,    "BattleInfo_AA8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(22580,   -65740,  10,      0x1010000,    "BattleInfo_918", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(32310,   -111280, 0,       0x1010000,    "BattleInfo_B70", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(46440,   -108530, 900,     0x1010000,    "BattleInfo_918", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 26,  0.0,                   -67.0,                 0.0,                   8100.0,                [0.01666666567325592,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333134651184,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333134651184,    0.0,                   -0.0,                  22.333332061767578,    -0.0,                  1.0])

    DeclActor(-10300,  180,     -13000,  1500,    -10300,  1680,    -13000,  0x007C, 0,  28, 0x0000)
    DeclActor(-13860,  0,       -95170,  1200,    -13860,  0,       -95170,  0x007C, 0,  6,  0x0000)
    DeclActor(38020,   0,       -116090, 1200,    38020,   0,       -116090, 0x007C, 0,  7,  0x0000)
    DeclActor(4180,    0,       -25720,  1200,    4180,    2000,    -25720,  0x007C, 0,  27, 0x0000)
    DeclActor(5120,    0,       -26320,  1200,    8000,    2000,    -10000,  0x007C, 0,  27, 0x0000)
    DeclActor(9210,    0,       -24210,  1500,    9210,    1700,    -24210,  0x007C, 0,  47, 0x0000)

    PlaceName(2.0, 0.0, 20.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-27.0, 0.0, -159.0, 0x0000, 0x0000, "乌尔斯拉医科大学方向")
    PlaceName(45.0, 0.0, -24.0, 0x0000, 0x0000, "克洛斯贝尔空港方向")
    PlaceName(-10.649999618530273, 0.0, -11.800000190734863, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5, 6, 7])              # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9

    ScpFunction((
        "Function_0_DF8",          # 00, 0
        "Function_1_EA8",          # 01, 1
        "Function_2_EC7",          # 02, 2
        "Function_3_EE6",          # 03, 3
        "Function_4_FF4",          # 04, 4
        "Function_5_1BB6",         # 05, 5
        "Function_6_2291",         # 06, 6
        "Function_7_25BB",         # 07, 7
        "Function_8_28E5",         # 08, 8
        "Function_9_2931",         # 09, 9
        "Function_10_2959",        # 0A, 10
        "Function_11_2A1B",        # 0B, 11
        "Function_12_2B4D",        # 0C, 12
        "Function_13_2B74",        # 0D, 13
        "Function_14_2C08",        # 0E, 14
        "Function_15_320B",        # 0F, 15
        "Function_16_327B",        # 10, 16
        "Function_17_335F",        # 11, 17
        "Function_18_33B5",        # 12, 18
        "Function_19_345B",        # 13, 19
        "Function_20_3565",        # 14, 20
        "Function_21_35C3",        # 15, 21
        "Function_22_3630",        # 16, 22
        "Function_23_3696",        # 17, 23
        "Function_24_36E1",        # 18, 24
        "Function_25_387D",        # 19, 25
        "Function_26_38CC",        # 1A, 26
        "Function_27_3BE9",        # 1B, 27
        "Function_28_3F16",        # 1C, 28
        "Function_29_3F50",        # 1D, 29
        "Function_30_41A4",        # 1E, 30
        "Function_31_447E",        # 1F, 31
        "Function_32_457E",        # 20, 32
        "Function_33_4FCB",        # 21, 33
        "Function_34_503D",        # 22, 34
        "Function_35_52FA",        # 23, 35
        "Function_36_531F",        # 24, 36
        "Function_37_534D",        # 25, 37
        "Function_38_5385",        # 26, 38
        "Function_39_53AA",        # 27, 39
        "Function_40_544E",        # 28, 40
        "Function_41_54C8",        # 29, 41
        "Function_42_56A2",        # 2A, 42
        "Function_43_587C",        # 2B, 43
        "Function_44_5A56",        # 2C, 44
        "Function_45_5AD0",        # 2D, 45
        "Function_46_5AF1",        # 2E, 46
        "Function_47_5B3A",        # 2F, 47
    ))


    def Function_0_DF8(): pass

    label("Function_0_DF8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_E30"),
        (1, "loc_E3C"),
        (2, "loc_E48"),
        (3, "loc_E54"),
        (4, "loc_E60"),
        (5, "loc_E6C"),
        (6, "loc_E78"),
        (SWITCH_DEFAULT, "loc_E84"),
    )


    label("loc_E30")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E3C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E48")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E54")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E60")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E6C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E78")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E84")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EA7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_EA7")

    Return()

    # Function_0_DF8 end

    def Function_1_EA8(): pass

    label("Function_1_EA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EC6")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_EA8")

    label("loc_EC6")

    Return()

    # Function_1_EA8 end

    def Function_2_EC7(): pass

    label("Function_2_EC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EE5")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_2_EC7")

    label("loc_EE5")

    Return()

    # Function_2_EC7 end

    def Function_3_EE6(): pass

    label("Function_3_EE6")

    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x1E, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    SetMapObjFlags(0x19, 0x2000000)
    SetMapObjFlags(0x1A, 0x2000000)
    SetMapObjFlags(0x1B, 0x2000000)
    SetMapObjFlags(0x1C, 0x2000000)
    SetMapObjFlags(0x1D, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F96")
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)
    ClearMapObjFlags(0x17, 0x2000000)
    ClearMapObjFlags(0x18, 0x2000000)
    ClearMapObjFlags(0x19, 0x2000000)
    ClearMapObjFlags(0x1A, 0x2000000)
    ClearMapObjFlags(0x1B, 0x2000000)
    ClearMapObjFlags(0x1C, 0x2000000)
    ClearMapObjFlags(0x1D, 0x2000000)
    Jump("loc_FF3")

    label("loc_F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_FF3")
    SetMapObjFlags(0x0, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xF, 0x2000000)
    ClearMapObjFlags(0x10, 0x2000000)
    ClearMapObjFlags(0x16, 0x2000000)
    ClearMapObjFlags(0x11, 0x2000000)
    ClearMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)
    ClearMapObjFlags(0x14, 0x2000000)
    ClearMapObjFlags(0x15, 0x2000000)
    ClearMapObjFlags(0x1E, 0x2000000)

    label("loc_FF3")

    Return()

    # Function_3_EE6 end

    def Function_4_FF4(): pass

    label("Function_4_FF4")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1026")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 13380, 0, -16640, 270)
    Jump("loc_116F")

    label("loc_1026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1034")
    Jump("loc_116F")

    label("loc_1034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1042")
    Jump("loc_116F")

    label("loc_1042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1064")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105F")
    ClearChrFlags(0x13, 0x80)

    label("loc_105F")

    Jump("loc_116F")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1072")
    Jump("loc_116F")

    label("loc_1072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1080")
    Jump("loc_116F")

    label("loc_1080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_108E")
    Jump("loc_116F")

    label("loc_108E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10BF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BA")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9610, 0, -14320, 225)

    label("loc_10BA")

    Jump("loc_116F")

    label("loc_10BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10D2")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_116F")

    label("loc_10D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10F9")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_116F")

    label("loc_10F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_112A")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1125")
    ClearChrFlags(0xF, 0x80)

    label("loc_1125")

    Jump("loc_116F")

    label("loc_112A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1158")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9610, 0, -14320, 225)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_116F")

    label("loc_1158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1166")
    Jump("loc_116F")

    label("loc_1166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_116F")

    label("loc_116F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1183")
    ClearScenarioFlags(0x22, 0)
    Event(0, 29)
    Jump("loc_11C8")

    label("loc_1183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1197")
    ClearScenarioFlags(0x22, 1)
    Event(0, 31)
    Jump("loc_11C8")

    label("loc_1197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_11AB")
    ClearScenarioFlags(0x22, 2)
    Event(0, 32)
    Jump("loc_11C8")

    label("loc_11AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_11C8")
    ClearScenarioFlags(0x22, 3)
    SetChrPos(0x0, 12640, 0, -17790, 270)

    label("loc_11C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166C")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1255")
    SetScenarioFlags(0x38, 0)

    label("loc_1255")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126B")
    SetScenarioFlags(0x38, 1)

    label("loc_126B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1281")
    SetScenarioFlags(0x38, 2)

    label("loc_1281")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1297")
    SetScenarioFlags(0x38, 3)

    label("loc_1297")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AD")
    SetScenarioFlags(0x38, 4)

    label("loc_12AD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C3")
    SetScenarioFlags(0x38, 5)

    label("loc_12C3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D9")
    SetScenarioFlags(0x38, 6)

    label("loc_12D9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EF")
    SetScenarioFlags(0x38, 7)

    label("loc_12EF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1305")
    SetScenarioFlags(0x39, 0)

    label("loc_1305")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131B")
    SetScenarioFlags(0x39, 1)

    label("loc_131B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1331")
    SetScenarioFlags(0x39, 2)

    label("loc_1331")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1347")
    SetScenarioFlags(0x39, 3)

    label("loc_1347")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135D")
    SetScenarioFlags(0x39, 4)

    label("loc_135D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    SetScenarioFlags(0x39, 5)

    label("loc_1373")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1389")
    SetScenarioFlags(0x39, 6)

    label("loc_1389")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139F")
    SetScenarioFlags(0x39, 7)

    label("loc_139F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B5")
    SetScenarioFlags(0x3A, 0)

    label("loc_13B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CB")
    SetScenarioFlags(0x3A, 1)

    label("loc_13CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E1")
    SetScenarioFlags(0x3A, 2)

    label("loc_13E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F7")
    SetScenarioFlags(0x3A, 3)

    label("loc_13F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140D")
    SetScenarioFlags(0x3A, 4)

    label("loc_140D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1423")
    SetScenarioFlags(0x3A, 5)

    label("loc_1423")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1439")
    SetScenarioFlags(0x3A, 6)

    label("loc_1439")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144F")
    SetScenarioFlags(0x3A, 7)

    label("loc_144F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1465")
    SetScenarioFlags(0x3B, 0)

    label("loc_1465")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147B")
    SetScenarioFlags(0x3B, 1)

    label("loc_147B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1491")
    SetScenarioFlags(0x3B, 2)

    label("loc_1491")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A7")
    SetScenarioFlags(0x3B, 3)

    label("loc_14A7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BD")
    SetScenarioFlags(0x3B, 4)

    label("loc_14BD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D3")
    SetScenarioFlags(0x3B, 5)

    label("loc_14D3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E9")
    SetScenarioFlags(0x3B, 6)

    label("loc_14E9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FF")
    SetScenarioFlags(0x3B, 7)

    label("loc_14FF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1515")
    SetScenarioFlags(0x3D, 5)

    label("loc_1515")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152B")
    SetScenarioFlags(0x3D, 6)

    label("loc_152B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1541")
    SetScenarioFlags(0x3D, 7)

    label("loc_1541")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157C")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_166C")

    label("loc_157C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159F")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_166C")

    label("loc_159F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C2")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_166C")

    label("loc_15C2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E5")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_166C")

    label("loc_15E5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1608")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_166C")

    label("loc_1608")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162B")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_166C")

    label("loc_162B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164E")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_166C")

    label("loc_164E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166C")
    SetScenarioFlags(0x3C, 7)

    label("loc_166C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1682")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B4")
    SetChrPos(0x0, 2680, 0, -25440, 267)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 13)

    label("loc_16B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_16E7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E7")
    SetChrPos(0x0, 5120, 0, -26320, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_16E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_16F6")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 12)

    label("loc_16F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BB5")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179E")
    SetScenarioFlags(0x38, 0)

    label("loc_179E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B4")
    SetScenarioFlags(0x38, 1)

    label("loc_17B4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CA")
    SetScenarioFlags(0x38, 2)

    label("loc_17CA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E0")
    SetScenarioFlags(0x38, 3)

    label("loc_17E0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F6")
    SetScenarioFlags(0x38, 4)

    label("loc_17F6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180C")
    SetScenarioFlags(0x38, 5)

    label("loc_180C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1822")
    SetScenarioFlags(0x38, 6)

    label("loc_1822")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1838")
    SetScenarioFlags(0x38, 7)

    label("loc_1838")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_184E")
    SetScenarioFlags(0x39, 0)

    label("loc_184E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1864")
    SetScenarioFlags(0x39, 1)

    label("loc_1864")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187A")
    SetScenarioFlags(0x39, 2)

    label("loc_187A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1890")
    SetScenarioFlags(0x39, 3)

    label("loc_1890")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A6")
    SetScenarioFlags(0x39, 4)

    label("loc_18A6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BC")
    SetScenarioFlags(0x39, 5)

    label("loc_18BC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D2")
    SetScenarioFlags(0x39, 6)

    label("loc_18D2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E8")
    SetScenarioFlags(0x39, 7)

    label("loc_18E8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FE")
    SetScenarioFlags(0x3A, 0)

    label("loc_18FE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1914")
    SetScenarioFlags(0x3A, 1)

    label("loc_1914")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192A")
    SetScenarioFlags(0x3A, 2)

    label("loc_192A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1940")
    SetScenarioFlags(0x3A, 3)

    label("loc_1940")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1956")
    SetScenarioFlags(0x3A, 4)

    label("loc_1956")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196C")
    SetScenarioFlags(0x3A, 5)

    label("loc_196C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1982")
    SetScenarioFlags(0x3A, 6)

    label("loc_1982")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1998")
    SetScenarioFlags(0x3A, 7)

    label("loc_1998")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19AE")
    SetScenarioFlags(0x3B, 0)

    label("loc_19AE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C4")
    SetScenarioFlags(0x3B, 1)

    label("loc_19C4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DA")
    SetScenarioFlags(0x3B, 2)

    label("loc_19DA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F0")
    SetScenarioFlags(0x3B, 3)

    label("loc_19F0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A06")
    SetScenarioFlags(0x3B, 4)

    label("loc_1A06")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1C")
    SetScenarioFlags(0x3B, 5)

    label("loc_1A1C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A32")
    SetScenarioFlags(0x3B, 6)

    label("loc_1A32")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A48")
    SetScenarioFlags(0x3B, 7)

    label("loc_1A48")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5E")
    SetScenarioFlags(0x3D, 5)

    label("loc_1A5E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A74")
    SetScenarioFlags(0x3D, 6)

    label("loc_1A74")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8A")
    SetScenarioFlags(0x3D, 7)

    label("loc_1A8A")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC5")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1BB5")

    label("loc_1AC5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE8")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1BB5")

    label("loc_1AE8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0B")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1BB5")

    label("loc_1B0B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B2E")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1BB5")

    label("loc_1B2E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B51")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1BB5")

    label("loc_1B51")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B74")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1BB5")

    label("loc_1B74")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B97")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1BB5")

    label("loc_1B97")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB5")
    SetScenarioFlags(0x3C, 7)

    label("loc_1BB5")

    Return()

    # Function_4_FF4 end

    def Function_5_1BB6(): pass

    label("Function_5_1BB6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BFF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C1F")

    label("loc_1BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1C16")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C1F")

    label("loc_1C16")

    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C62")
    OP_24(0x7D)
    Jump("loc_1CA5")

    label("loc_1C62")

    SoundDistance(0x7D, 0x34C6, 0x0, 0xFFFD8D16, 0x15F90, 0x11170, 0x64, 0x0)
    OP_E3(0x9D4E, 0x118, 0xFFFE0909)
    OP_E3(0xE06A, 0x384, 0xFFFE9238)
    OP_E3(0xFCDA, 0x5A, 0xFFFF282E)

    label("loc_1CA5")

    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E58")
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x35), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000)
    OP_E2(0x1)
    ClearScenarioFlags(0x0, 2)
    Jump("loc_1E75")

    label("loc_1E58")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E75")
    OP_E2(0x0)
    SetScenarioFlags(0x0, 2)

    label("loc_1E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EF9")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x5, 0x12C, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1F50")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x5, 0x12C, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    Jump("loc_1F80")

    label("loc_1F50")

    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)

    label("loc_1F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FEF")
    OP_11(0xA0, 0xC8, 0xFF, 0x0, 0x140, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x0, 0x258, 0x0, 0x20)
    OP_C3(0x0, 0x1, 0x3, 0x0, 0x0, 0x2, -18000, -1000, -64500, 29000, 1000, -66500)
    LoadEffect(0x11, "eff\\\\trapdmg2.eff")
    Jump("loc_1FF5")

    label("loc_1FEF")

    SetMapObjFlags(0xB, 0x4)

    label("loc_1FF5")

    MiniGame(0x2F, 0x3, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x14, 0x80)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2048")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2048")
    Call(0, 9)

    label("loc_2048")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20A9")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -13860, 0, -95170, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x1, 0x1)

    label("loc_20A9")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20F5")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 38020, 0, -116090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_20F5")

    OP_1B(0x4, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2108")
    Jump("loc_21A0")

    label("loc_2108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_211B")
    OP_1B(0x4, 0x0, 0x19)
    Jump("loc_21A0")

    label("loc_211B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_212E")
    OP_1B(0x4, 0x0, 0x19)
    Jump("loc_21A0")

    label("loc_212E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_214B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2146")
    OP_1B(0x4, 0x0, 0x19)

    label("loc_2146")

    Jump("loc_21A0")

    label("loc_214B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2159")
    Jump("loc_21A0")

    label("loc_2159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_216C")
    OP_1B(0x4, 0x0, 0x19)
    Jump("loc_21A0")

    label("loc_216C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_217A")
    Jump("loc_21A0")

    label("loc_217A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2192")
    OP_1B(0x4, 0x0, 0x1E)
    Jump("loc_21A0")

    label("loc_2192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_21A0")
    OP_1B(0x4, 0x0, 0x19)

    label("loc_21A0")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21BD")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_21BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21CE")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_21CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21DC")
    Jump("loc_2290")

    label("loc_21DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_21ED")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_21ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_21FB")
    Jump("loc_2290")

    label("loc_21FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_220C")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_220C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2232")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222A")
    Call(0, 9)
    Jump("loc_222D")

    label("loc_222A")

    Call(0, 8)

    label("loc_222D")

    Jump("loc_2290")

    label("loc_2232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2243")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_2243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2254")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_2254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2265")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_2265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2276")
    Call(0, 9)
    Jump("loc_2290")

    label("loc_2276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2284")
    Jump("loc_2290")

    label("loc_2284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2290")
    Call(0, 8)

    label("loc_2290")

    Return()

    # Function_5_1BB6 end

    def Function_6_2291(): pass

    label("Function_6_2291")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_242F")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_END)), "loc_2410")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0001
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_240B")
    ClearScenarioFlags(0x3A, 0)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_2408")
    ClearScenarioFlags(0x38, 0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2333():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_2333)
    TurnDirection(0x1B, 0x0, 0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    PlayEffect(0x7, 0x1, 0x1B, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0002
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
    Battle("BattleInfo_C38", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2403")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23EA")
    Call(1, 5)
    Jump("loc_2403")

    label("loc_23EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2400")
    Call(1, 4)
    Jump("loc_2403")

    label("loc_2400")

    Call(1, 3)

    label("loc_2403")

    Jump("loc_240B")

    label("loc_2408")

    Call(1, 1)

    label("loc_240B")

    Jump("loc_2426")

    label("loc_2410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_2426")
    ClearScenarioFlags(0x38, 0)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2426")

    TalkEnd(0xFF)
    Return()

    label("loc_242F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_END)), "loc_25A0")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0003
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_259B")
    ClearScenarioFlags(0x3A, 0)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_2598")
    ClearScenarioFlags(0x38, 0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_24C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_24C3)
    TurnDirection(0x1D, 0x0, 0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    PlayEffect(0x7, 0x1, 0x1D, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0004
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
    Battle("BattleInfo_C7C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2593")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_257A")
    Call(1, 5)
    Jump("loc_2593")

    label("loc_257A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2590")
    Call(1, 4)
    Jump("loc_2593")

    label("loc_2590")

    Call(1, 3)

    label("loc_2593")

    Jump("loc_259B")

    label("loc_2598")

    Call(1, 1)

    label("loc_259B")

    Jump("loc_25B6")

    label("loc_25A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_25B6")
    ClearScenarioFlags(0x38, 0)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_25B6")

    TalkEnd(0xFF)
    Return()

    # Function_6_2291 end

    def Function_7_25BB(): pass

    label("Function_7_25BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2759")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_273A")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0005
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2735")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_2732")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_265D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_265D)
    TurnDirection(0x1C, 0x0, 0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    PlayEffect(0x7, 0x1, 0x1C, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0006
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
    Battle("BattleInfo_C38", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1C, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_272D")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2714")
    Call(1, 5)
    Jump("loc_272D")

    label("loc_2714")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_272A")
    Call(1, 4)
    Jump("loc_272D")

    label("loc_272A")

    Call(1, 3)

    label("loc_272D")

    Jump("loc_2735")

    label("loc_2732")

    Call(1, 1)

    label("loc_2735")

    Jump("loc_2750")

    label("loc_273A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_2750")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2750")

    TalkEnd(0xFF)
    Return()

    label("loc_2759")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_28CA")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0007
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C5")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_28C2")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_27ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_27ED)
    TurnDirection(0x1E, 0x0, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    PlayEffect(0x7, 0x1, 0x1E, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0008
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
    Battle("BattleInfo_C7C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1E, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28BD")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_28A4")
    Call(1, 5)
    Jump("loc_28BD")

    label("loc_28A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_28BA")
    Call(1, 4)
    Jump("loc_28BD")

    label("loc_28BA")

    Call(1, 3)

    label("loc_28BD")

    Jump("loc_28C5")

    label("loc_28C2")

    Call(1, 1)

    label("loc_28C5")

    Jump("loc_28E0")

    label("loc_28CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_28E0")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_28E0")

    TalkEnd(0xFF)
    Return()

    # Function_7_25BB end

    def Function_8_28E5(): pass

    label("Function_8_28E5")

    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetMapObjFlags(0xC, 0x1000)
    OP_78(0xC, 0x12)
    SetChrPos(0x12, 2000, 1000, 14000, 0)
    OP_D5(0x12, 0x0, 0x2BF20, 0x0, 0x0)
    Return()

    # Function_8_28E5 end

    def Function_9_2931(): pass

    label("Function_9_2931")

    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetMapObjFlags(0xC, 0x1000)
    OP_78(0xC, 0x12)
    Return()

    # Function_9_2931 end

    def Function_10_2959(): pass

    label("Function_10_2959")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    #A0009
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
            "圣乌尔斯拉医科大学\x01",            # 0
            "岔路口停靠站（河滩附近）\x01",      # 1
            "放弃\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29F3")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2A13")

    label("loc_29F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A13")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_2A13")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_10_2959 end

    def Function_11_2A1B(): pass

    label("Function_11_2A1B")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_2B49")
    Fade(500)
    OP_68(-10500, 780, -11600, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -9800, 180, -11100, 89)
    SetChrPos(0x1, -9800, 180, -10100, 89)
    SetChrPos(0x2, -9800, 180, -9100, 89)
    SetChrPos(0x3, -9800, 180, -8100, 89)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_78(0x0, 0x14)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x14, -6300, 0, -21000, 0)
    OP_D5(0x14, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2B00():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFD314, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2B00)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x14, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_2B49")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_11_2A1B end

    def Function_12_2B4D(): pass

    label("Function_12_2B4D")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -9830, 180, -11430, 90)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_2B4D end

    def Function_13_2B74(): pass

    label("Function_13_2B74")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2BCF")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BC4")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_2BCA")

    label("loc_2BC4")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_2BCA")

    Jump("loc_2BF3")

    label("loc_2BCF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BED")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_2BF3")

    label("loc_2BED")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_2BF3")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_2B74 end

    def Function_14_2C08(): pass

    label("Function_14_2C08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2C19")
    Jump("loc_3207")

    label("loc_2C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2EDD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CEA")

    #C0010
    ChrTalk(
        0xFE,
        (
            "多亏你们，总算把医疗物资\x01",
            "平安送到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "话说回来，诈骗犯吗……\x01",
            "竟然在这种非常时期趁火打劫，\x01",
            "真是个卑劣的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "好在你们已经把他抓住，\x01",
            "总算可以暂时安心了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D42")

    label("loc_2CEA")


    #C0013
    ChrTalk(
        0xFE,
        (
            "诈骗犯吗……\x01",
            "真是个卑劣的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "好在你们已经把他抓住，\x01",
            "总算可以暂时安心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D42")

    Jump("loc_2ED8")

    label("loc_2D47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_2E77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E0C")

    #C0015
    ChrTalk(
        0xFE,
        (
            "可恶，在这种非常时期，\x01",
            "却没能把医疗物资顺利送到……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "……不，事情已经发生了，\x01",
            "再怎么发牢骚也无济于事。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "你们几个也是一样，\x01",
            "赶快转换心情，投入到工作中吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E72")

    label("loc_2E0C")


    #C0018
    ChrTalk(
        0xFE,
        (
            "事情已经发生了，\x01",
            "再怎么发牢骚也无济于事。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "你们几个也是一样，\x01",
            "赶快转换心情，投入到工作中吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E72")

    Jump("loc_2ED8")

    label("loc_2E77")


    #C0020
    ChrTalk(
        0xFE,
        (
            "竟然在这种非常时期趁火打劫，\x01",
            "骗取医疗物资……\x01",
            "绝对不能饶恕他。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "你们一定要\x01",
            "抓到犯人啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED8")

    Jump("loc_3207")

    label("loc_2EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2EEB")
    Jump("loc_3207")

    label("loc_2EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2EF9")
    Jump("loc_3207")

    label("loc_2EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2F07")
    Jump("loc_3207")

    label("loc_2F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3019")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FCC")

    #C0022
    ChrTalk(
        0xFE,
        (
            "唔，竟然会搞混\x01",
            "收货地址……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "虽说是对方的失误，\x01",
            "但我没能及时注意到，也应该担负一部分责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "不过我还有别的货要送，\x01",
            "所以没办法帮他们……\x01",
            "唔，真是不好意思啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3014")

    label("loc_2FCC")


    #C0025
    ChrTalk(
        0xFE,
        (
            "唔，竟然会搞混\x01",
            "收货地址……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "真是对不住卡普亚特急便\x01",
            "的各位啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3014")

    Jump("loc_3207")

    label("loc_3019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3027")
    Jump("loc_3207")

    label("loc_3027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3035")
    Jump("loc_3207")

    label("loc_3035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3043")
    Jump("loc_3207")

    label("loc_3043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_31F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3141")

    #C0027
    ChrTalk(
        0xFE,
        (
            "我们这家运输公司主要\x01",
            "承接从外国寄来的包裹。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "特别是北方的雷米菲利亚公国，\x01",
            "经常会向乌尔斯拉医院寄送\x01",
            "各种医疗物资和器械。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "我既然负责运输那些东西，\x01",
            "就与最尖端的医疗技术存在着间接关系。\x01",
            "所以必须要负起责任，认真运送。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_31EB")

    label("loc_3141")


    #C0030
    ChrTalk(
        0xFE,
        (
            "北方的雷米菲利亚公国\x01",
            "经常会向乌尔斯拉医院寄送\x01",
            "各种医疗物资和器械。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "我既然负责运输那些东西，\x01",
            "就与最尖端的医疗技术存在着间接关系。\x01",
            "所以必须要负起责任，认真运送。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31EB")

    Jump("loc_3207")

    label("loc_31F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_31FE")
    Jump("loc_3207")

    label("loc_31FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3207")

    label("loc_3207")

    TalkEnd(0xFE)
    Return()

    # Function_14_2C08 end

    def Function_15_320B(): pass

    label("Function_15_320B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_321C")
    Jump("loc_3277")

    label("loc_321C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3277")

    #C0032
    ChrTalk(
        0xFE,
        (
            "嗯，好久没有来过\x01",
            "克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "哎呀呀，真是个好地方，\x01",
            "不输给利贝尔呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3277")

    TalkEnd(0xFE)
    Return()

    # Function_15_320B end

    def Function_16_327B(): pass

    label("Function_16_327B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32EE")

    #C0034
    ChrTalk(
        0xFE,
        (
            "之前那起袭击事件\x01",
            "真是太可怕了……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "简直就像做了一场噩梦。\x01",
            "但愿以后别再发生那种事情了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_335B")

    label("loc_32EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_335B")

    #C0036
    ChrTalk(
        0xFE,
        (
            "那艘优美的『埃尔赛尤号』\x01",
            "在空港华丽着陆的场面\x01",
            "真是值得一看啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "呵呵，回去之后可有的讲了。\x02",
    )

    CloseMessageWindow()

    label("loc_335B")

    TalkEnd(0xFE)
    Return()

    # Function_16_327B end

    def Function_17_335F(): pass

    label("Function_17_335F")

    TalkBegin(0xFE)

    #C0038
    ChrTalk(
        0xFE,
        (
            "听说今天要在\x01",
            "港湾区举办咪西\x01",
            "的表演活动～！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "爷爷，\x01",
            "我们赶快去看看吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_335F end

    def Function_18_33B5(): pass

    label("Function_18_33B5")

    TalkBegin(0xFE)

    #C0040
    ChrTalk(
        0xFE,
        (
            "自从克洛斯贝尔发表独立提案之后，\x01",
            "似乎饱受两大国的压力。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "迪塔市长竟然在通商会议现场\x01",
            "发表了那种提案，真是让我大吃一惊。\x01",
            "但那种做法未免过于急进了吧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_33B5 end

    def Function_19_345B(): pass

    label("Function_19_345B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3505")

    #C0042
    ChrTalk(
        0xFE,
        (
            "通商会议明天就要在\x01",
            "这经济枢纽──\x01",
            "克洛斯贝尔正式召开了……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "这场会议想必会对周边诸国\x01",
            "的经济状况也造成很大影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        "……一定要密切关注啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3561")

    label("loc_3505")


    #C0045
    ChrTalk(
        0xFE,
        (
            "明天的通商会议\x01",
            "想必会对周边诸国\x01",
            "的经济状况也造成很大影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        "……一定要密切关注啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3561")

    TalkEnd(0xFE)
    Return()

    # Function_19_345B end

    def Function_20_3565(): pass

    label("Function_20_3565")

    TalkBegin(0xFE)

    #C0047
    ChrTalk(
        0xFE,
        "对、对不起！都是我不好！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "我会带你去百货店随便选购\x01",
            "喜欢的东西，请原谅我吧～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_3565 end

    def Function_21_35C3(): pass

    label("Function_21_35C3")

    TalkBegin(0xFE)

    #C0049
    ChrTalk(
        0xFE,
        (
            "喂，刚才那个职员说米修拉姆\x01",
            "正在停业中，是真的吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "你事先为何不好好确认一下啊，\x01",
            "大笨蛋～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_35C3 end

    def Function_22_3630(): pass

    label("Function_22_3630")

    TalkBegin(0xFE)

    #C0051
    ChrTalk(
        0xFE,
        (
            "唔、唔……\x01",
            "我刚刚旅行\x01",
            "归来……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "但、但肚子突然痛起来了。\x01",
            "是不是应该去医院看看呢……？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_3630 end

    def Function_23_3696(): pass

    label("Function_23_3696")

    TalkBegin(0xFE)

    #C0053
    ChrTalk(
        0xFE,
        (
            "警察正在空港的\x01",
            "飞艇坪调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "请各位不要擅自\x01",
            "进入调查区域。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_3696 end

    def Function_24_36E1(): pass

    label("Function_24_36E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3731")

    #C0055
    ChrTalk(
        0xFE,
        (
            "是特别任务支援科的各位啊，\x01",
            "大家辛苦了！\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "请随意通行！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3879")

    label("loc_3731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3789")

    #C0057
    ChrTalk(
        0xFE,
        (
            "以兰花塔为目标\x01",
            "的恐怖分子吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "总觉得今天将会是\x01",
            "漫长的一天啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3879")

    label("loc_3789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37F7")

    #C0059
    ChrTalk(
        0xFE,
        (
            "揭幕式顺利结束，\x01",
            "真是让人松了口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "虽然通商会议才刚刚开始，\x01",
            "但总算是跨越一道难关了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3879")

    label("loc_37F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3879")

    #C0061
    ChrTalk(
        0xFE,
        (
            "在通商会议召开期间，\x01",
            "将对出入空港的人员\x01",
            "进行严格检查。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "大家一起努力，不要松懈大意，\x01",
            "坚持到通商会议顺利结束吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3879")

    TalkEnd(0xFE)
    Return()

    # Function_24_36E1 end

    def Function_25_387D(): pass

    label("Function_25_387D")

    EventBegin(0x1)

    #C0063
    ChrTalk(
        0x101,
        (
            "#00000F这边是克洛斯贝尔空港，\x01",
            "现在并不需要过去。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11250, 0, -17610, 270)
    EventEnd(0x4)
    Return()

    # Function_25_387D end

    def Function_26_38CC(): pass

    label("Function_26_38CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE8")
    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(14210, 2050, -69500, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(38330, 0)
    SetChrPos(0x101, 1500, 0, -73720, 0)
    SetChrPos(0x107, 2470, 0, -74900, 0)
    SetChrPos(0x105, 870, 0, -75890, 0)
    SetChrSubChip(0x107, 0x5)
    FadeToBright(1000, 0)
    OP_68(-6520, 2050, -69500, 6000)
    OP_6F(0x79)
    Fade(500)
    OP_68(60, 5950, -75080, 0)
    OP_68(60, 2050, -75080, 4000)
    MoveCamera(29, 11, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19360, 0)
    OP_6F(0x79)

    #C0064
    ChrTalk(
        0x101,
        (
            "#00010F#12P这就是笼罩着克洛斯贝尔市的『结界』……\x01",
            "……离近一看，更是觉得无计可施啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x105,
        (
            "#10403F#12P从我在梅尔卡瓦上的观测情况来看，\x01",
            "结界呈半圆状，\x01",
            "笼罩着整个克洛斯贝尔市。\x02\x03",

            "#10408F运送粮食的搬运车、紧急车辆、\x01",
            "国防军、『赤色星座』……\x02\x03",

            "#10401F似乎只有这些得到\x01",
            "总统许可的人或物\x01",
            "才可以自由通行。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x107,
        (
            "#01203F#3C#12P要是没有得到许可，\x01",
            "无论用任何方法都不可能穿越结界。\x02\x03",

            "#01201F在找到使其消失的方法之前，\x01",
            "我们也只能放弃由此进入的想法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00003F#11P……明白了。\x02\x03",

            "#00013F（琪雅，等着我，\x01",
            "  我一定会去找你的……！）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19610, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1AE, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    SetChrPos(0x0, 990, 0, -74180, 180)
    Sleep(500)
    EventEnd(0x5)

    label("loc_3BE8")

    Return()

    # Function_26_38CC end

    def Function_27_3BE9(): pass

    label("Function_27_3BE9")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C1B")
    SetScenarioFlags(0x31, 2)

    label("loc_3C1B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_3C5B")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C50")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_3C56")

    label("loc_3C50")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_3C56")

    Jump("loc_3C61")

    label("loc_3C5B")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_3C61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_3CD2")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3CB2"),
        (SWITCH_DEFAULT, "loc_3CC3"),
    )


    label("loc_3CB2")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3CCD")

    label("loc_3CC3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3CCD")

    Jump("loc_3F03")

    label("loc_3CD2")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3D02")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_3D02")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D2C"),
        (1, "loc_3E30"),
        (2, "loc_3EC1"),
        (SWITCH_DEFAULT, "loc_3EF9"),
    )


    label("loc_3D2C")

    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3D5D")
    OP_70(0x9, 0x12C)
    OP_71(0x9, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_3D6D")

    label("loc_3D5D")

    OP_70(0x9, 0xF0)
    OP_71(0x9, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_3D6D")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DC3")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE6")
    Sound(461, 0, 100, 0)

    label("loc_3DE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3E06")
    OP_70(0x9, 0x14A)
    OP_71(0x9, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_3E16")

    label("loc_3E06")

    OP_70(0x9, 0x10E)
    OP_71(0x9, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_3E16")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x9, "light", 0x1, 0x1)
    OP_70(0x9, 0x0)
    Jump("loc_3C61")

    label("loc_3E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3EA2")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_3E65")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_3E7D")

    label("loc_3E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3E78")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_3E7D")

    label("loc_3E78")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_3E7D")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EBC")

    label("loc_3EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3EB2")
    OP_AF(0xFB)
    Jump("loc_3EBC")

    label("loc_3EB2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EBC")

    Jump("loc_3F03")

    label("loc_3EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EDA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EF4")

    label("loc_3EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3EEA")
    OP_AF(0xFB)
    Jump("loc_3EF4")

    label("loc_3EEA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EF4")

    Jump("loc_3F03")

    label("loc_3EF9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F03")

    Jump("loc_3C61")

    label("loc_3F08")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_27_3BE9 end

    def Function_28_3F16(): pass

    label("Function_28_3F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3F4C")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0068
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

    label("loc_3F4C")

    Call(0, 10)
    Return()

    # Function_28_3F16 end

    def Function_29_3F50(): pass

    label("Function_29_3F50")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    SoundLoad(821)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x1F, 0x7)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    BeginChrThread(0x1F, 0, 0, 0)
    SetChrChipByIndex(0x20, 0x7)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    BeginChrThread(0x20, 0, 0, 0)
    SetChrChipByIndex(0x21, 0x7)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    BeginChrThread(0x21, 0, 0, 0)
    SetChrChipByIndex(0x22, 0x7)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    BeginChrThread(0x22, 0, 0, 0)
    SetChrChipByIndex(0x23, 0x7)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    BeginChrThread(0x23, 0, 0, 0)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    OP_49()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    OP_49()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x1000)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1A, 0x1000)
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1B, 0x1000)
    ClearMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1C, 0x1000)
    ClearMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1D, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x1F, -1400, 0, -13600, 90)
    SetChrPos(0x20, 250, 0, -17400, 45)
    SetChrPos(0x21, 3750, 0, -20300, 45)
    SetChrPos(0x22, 5600, 0, -9350, 225)
    SetChrPos(0x23, 9550, 0, -12400, 180)
    SetChrPos(0x24, -5650, 0, -11000, 0)
    SetChrPos(0x25, 3750, 0, -24250, 270)
    OP_68(2500, 600, -9450, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25500, 0)
    OP_68(17000, 1600, -17500, 10000)
    MoveCamera(45, 20, 0, 10000)
    SetCameraDistance(23500, 10000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(7000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c0180", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_3F50 end

    def Function_30_41A4(): pass

    label("Function_30_41A4")

    EventBegin(0x0)
    Fade(500)
    OP_68(15700, 1000, -17600, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 15700, 0, -17600, 90)
    SetChrPos(0x102, 14300, 0, -18200, 90)
    SetChrPos(0x104, 14300, 0, -17000, 90)
    SetChrPos(0x109, 13200, 0, -17000, 90)
    SetChrPos(0x105, 13200, 0, -18200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00003F（距离傍晚还有一些时间……）\x02\x03",

            "#00001F（虽然似乎有点早，\x01",
            "  要现在就去候船露台等候吗？）\x02",
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
            "【还有其它事情要办】\x01",          # 0
            "【进入空港，去露台等待】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_430A"),
        (1, "loc_432C"),
        (SWITCH_DEFAULT, "loc_447D"),
    )


    label("loc_430A")

    SetChrPos(0x0, 11250, 0, -17610, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Jump("loc_447D")

    label("loc_432C")

    OP_93(0x101, 0x10E, 0x1F4)

    #C0070
    ChrTalk(
        0x101,
        (
            "#11P#00000F好……虽然有些早，\x01",
            "但我们现在就去露台等候吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        "#6P#00102F好、好的……\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        "#5P#00306F做好充分的心理准备吧……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_43C1():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_43C1)
    Sleep(50)

    def lambda_43DE():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_43DE)
    Sleep(50)

    def lambda_43FB():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_43FB)
    Sleep(50)

    def lambda_4418():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4418)
    Sleep(50)

    def lambda_4435():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4435)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    Sleep(500)
    SetScenarioFlags(0x22, 1)
    NewScene("t3510", 0, 0, 0)
    IdleLoop()
    Jump("loc_447D")

    label("loc_447D")

    Return()

    # Function_30_41A4 end

    def Function_31_447E(): pass

    label("Function_31_447E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    OP_68(0, 3000, -64500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20500, 0)
    OP_68(0, 4000, -64500, 8000)
    MoveCamera(40, 27, 0, 8000)
    SetCameraDistance(30500, 8000)
    OP_71(0xB, 0x208, 0x2BC, 0x0, 0x0)
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
    SetScenarioFlags(0x23, 2)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_447E end

    def Function_32_457E(): pass

    label("Function_32_457E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45CA")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_45CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45DE")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_45DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45F2")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_45F2")

    LoadChrToIndex("apl/ch51616.itc", 0x1E)
    LoadChrToIndex("chr/ch41450.itc", 0x1F)
    LoadChrToIndex("chr/ch41451.itc", 0x20)
    LoadChrToIndex("chr/ch41452.itc", 0x21)
    LoadChrToIndex("apl/ch51617.itc", 0x22)
    LoadEffect(0x1, "battle/btgun00.eff")
    LoadEffect(0x2, "event/ev606_00.eff")
    LoadEffect(0x3, "event/eva01_01.eff")
    LoadEffect(0x4, "event/ev17057.eff")
    LoadEffect(0x5, "battle/sc008100.eff")
    LoadEffect(0x6, "event/ev17059.eff")
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(497)
    SoundLoad(825)
    SoundLoad(943)
    SoundLoad(861)
    SoundLoad(865)
    SoundLoad(577)
    SetChrPos(0x0, 8000, 0, 17000, 0)
    SetChrPos(0x1, 8000, 0, 17000, 0)
    SetChrPos(0x2, 8000, 0, 17000, 0)
    SetChrPos(0x3, 8000, 0, 17000, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 300, 0, -76000, 180)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 2900, 0, -76000, 180)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 3100, 0, -72400, 90)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 2600, 0, -67000, 0)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 2600, 0, -65400, 180)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 5300, 0, -65400, 0)
    ClearChrFlags(0x27, 0x80)
    OP_78(0xF, 0x27)
    OP_49()
    SetChrPos(0x27, 0, 19500, -19000, 90)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    OP_74(0xF, 0x1E)
    OP_71(0xF, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x16, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 20000, -19000, 90)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x16, 0x1000)
    OP_74(0x16, 0x1E)
    OP_71(0x16, 0x65, 0xA0, 0x0, 0x20)
    ClearChrFlags(0x29, 0x80)
    OP_78(0x10, 0x29)
    OP_49()
    SetChrPos(0x29, 0, 0, -130000, 0)
    OP_D5(0x29, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    ClearChrFlags(0x24, 0x80)
    OP_78(0x14, 0x24)
    OP_49()
    SetChrPos(0x24, -3700, 0, -71500, 180)
    OP_D5(0x24, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x0)
    SetMapObjFrame(0x14, "light", 0x0, 0x1)
    SetMapObjFrame(0x14, "mark00", 0x0, 0x1)
    SetMapObjFrame(0x14, "mark01", 0x1, 0x1)
    ClearChrFlags(0x25, 0x80)
    OP_78(0x15, 0x25)
    OP_49()
    SetChrPos(0x25, 5300, 0, -71500, 180)
    OP_D5(0x25, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    OP_74(0x15, 0x1E)
    OP_70(0x15, 0x0)
    SetMapObjFrame(0x15, "light", 0x0, 0x1)
    SetMapObjFrame(0x15, "mark00", 0x0, 0x1)
    SetMapObjFrame(0x15, "mark01", 0x1, 0x1)
    ClearChrFlags(0x26, 0x80)
    OP_78(0x1E, 0x26)
    OP_49()
    SetChrPos(0x26, 5300, 0, -62500, 270)
    OP_D5(0x26, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1E, 0x1000)
    OP_74(0x1E, 0x1E)
    OP_70(0x1E, 0x0)
    SetMapObjFrame(0x1E, "light", 0x0, 0x1)
    SetMapObjFrame(0x1E, "mark00", 0x0, 0x1)
    SetMapObjFrame(0x1E, "mark01", 0x1, 0x1)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    SetMapObjFlags(0xC, 0x4)
    OP_68(0, 3000, -25000, 0)
    MoveCamera(30, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25500, 0)
    OP_68(0, 3000, -78000, 10000)
    SetCameraDistance(23000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    BeginChrThread(0x2A, 1, 0, 44)
    Fade(500)
    OP_68(2000, 1000, -76000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    Sleep(1000)
    OP_63(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x19, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_4B56():

        label("loc_4B56")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_4B56")

    QueueWorkItem2(0x15, 2, lambda_4B56)

    def lambda_4B68():

        label("loc_4B68")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_4B68")

    QueueWorkItem2(0x16, 2, lambda_4B68)

    def lambda_4B7A():

        label("loc_4B7A")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_4B7A")

    QueueWorkItem2(0x17, 2, lambda_4B7A)

    def lambda_4B8C():

        label("loc_4B8C")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_4B8C")

    QueueWorkItem2(0x18, 2, lambda_4B8C)

    def lambda_4B9E():

        label("loc_4B9E")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_4B9E")

    QueueWorkItem2(0x19, 2, lambda_4B9E)

    def lambda_4BB0():

        label("loc_4BB0")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_4BB0")

    QueueWorkItem2(0x1A, 2, lambda_4BB0)
    MoveCamera(33, 27, 0, 5000)
    SetCameraDistance(30500, 5000)
    BlurSwitch(0x1388, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_4BE2():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_4BE2)
    Sleep(1500)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x29, 1)
    Fade(500)
    OP_68(0, 6000, -20000, 0)
    MoveCamera(57, 47, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(55000, 0)
    CancelBlur(0)
    SetMapObjFlags(0x1, 0x1000)
    BeginChrThread(0x27, 0, 0, 38)
    BeginChrThread(0x27, 3, 0, 36)
    BeginChrThread(0x29, 3, 0, 37)
    OP_68(0, 4000, -20000, 4000)
    MoveCamera(67, 47, 0, 4000)
    SetCameraDistance(50000, 4000)
    Sleep(1500)
    Sound(942, 0, 100, 0)
    OP_6F(0x79)
    WaitChrThread(0x27, 3)
    EndChrThread(0x27, 0x0)
    SetMapObjFlags(0x1E, 0x4)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    StopSound(825, 2000, 50)
    Fade(500)
    OP_68(0, 2000, -61000, 0)
    MoveCamera(30, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 2000, -56000, 3000)
    MoveCamera(33, 23, 0, 3000)
    SetCameraDistance(20000, 3000)
    SetChrPos(0x24, -4200, 0, -71500, 0)
    OP_D5(0x24, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x25, 4600, 0, -74500, 0)
    OP_D5(0x25, 0x0, 0x0, 0x0, 0x0)
    BeginChrThread(0x24, 3, 0, 39)
    BeginChrThread(0x25, 3, 0, 40)
    BeginChrThread(0x15, 3, 0, 41)
    Sleep(300)
    BeginChrThread(0x16, 3, 0, 42)
    Sleep(300)
    BeginChrThread(0x17, 3, 0, 43)
    StopSound(497, 2000, 70)
    OP_6F(0x79)
    Sleep(2000)
    OP_68(0, 4200, -35000, 1500)
    MoveCamera(27, 21, 0, 1500)
    SetCameraDistance(25000, 1500)
    OP_6F(0x79)
    Sound(920, 0, 100, 0)
    Sound(921, 0, 100, 0)
    Sound(922, 0, 100, 0)
    PlayEffect(0x4, 0x2, 0xFF, 0x0, 0, 4500, -35500, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x27, 0, 0, 34)
    Sleep(3000)
    BeginChrThread(0x2A, 1, 0, 46)
    Fade(500)
    OP_68(0, 1100, -14000, 0)
    MoveCamera(43, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25500, 0)
    SetCameraDistance(23500, 2500)
    EndChrThread(0x27, 0x0)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x3)
    OP_0D()
    Sound(943, 2, 100, 0)
    OP_74(0xF, 0xF)
    OP_71(0xF, 0x137, 0x154, 0x0, 0x0)
    OP_79(0xF)
    OP_24(0x3AF)
    Sound(143, 0, 100, 0)
    OP_6F(0x79)
    OP_68(0, 1100, -7500, 3000)
    MoveCamera(56, 13, 0, 3000)
    SetCameraDistance(21500, 3000)
    BeginChrThread(0x101, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x106, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x2A, 1, 0, 45)
    StopSound(865, 1900, 25)
    StopSound(577, 1900, 20)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x1F1)
    OP_24(0x339)
    OP_24(0x3AF)
    OP_24(0x35D)
    OP_24(0x361)
    OP_24(0x241)
    SetScenarioFlags(0x22, 3)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_457E end

    def Function_33_4FCB(): pass

    label("Function_33_4FCB")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x1)
    Sleep(1)
    SetChrPos(0xFE, 0, 1300, -15500, 0)

    def lambda_4FF8():
        OP_95(0xFE, 0, 0, -8800, 4000, 0x2)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4FF8)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    Sleep(1)

    def lambda_5023():
        OP_97(0xFE, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5023)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_33_4FCB end

    def Function_34_503D(): pass

    label("Function_34_503D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52F9")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 3000, 3500, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -2000, 4200, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1100, 4800, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1500, 5100, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -2700, 3700, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -900, 5000, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 2800, 2900, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -1400, 4500, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 300, 4400, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 2000, 4900, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -3900, 3300, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -500, 3000, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_34_503D")

    label("loc_52F9")

    Return()

    # Function_34_503D end

    def Function_35_52FA(): pass

    label("Function_35_52FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_531E")
    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("Function_35_52FA")

    label("loc_531E")

    Return()

    # Function_35_52FA end

    def Function_36_531F(): pass

    label("Function_36_531F")


    def lambda_5324():
        OP_96(0xFE, 0x0, 0x14B4, 0xFFFFB5C8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5324)
    OP_D5(0xFE, 0x0, 0x2BF20, 0x0, 0x12C0)
    Return()

    # Function_36_531F end

    def Function_37_534D(): pass

    label("Function_37_534D")

    SetChrPos(0x29, 0, 0, -19000, 0)
    OP_D5(0x29, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x29, 0x0, 0x2BF20, 0x0, 0x12C0)
    Return()

    # Function_37_534D end

    def Function_38_5385(): pass

    label("Function_38_5385")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53A9")
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_38_5385")

    label("loc_53A9")

    Return()

    # Function_38_5385 end

    def Function_39_53AA(): pass

    label("Function_39_53AA")

    Sound(486, 0, 100, 0)
    Sound(494, 0, 100, 0)
    OP_71(0x14, 0xB5, 0xF0, 0x0, 0x20)

    def lambda_53C7():
        OP_96(0xFE, 0xFFFFEF98, 0x0, 0xFFFF2540, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53C7)
    WaitChrThread(0xFE, 1)
    Sound(487, 0, 100, 0)
    OP_71(0x14, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x14)
    OP_71(0x14, 0xF1, 0xF3, 0x0, 0x0)
    OP_79(0x14)
    Sound(865, 2, 80, 0)
    Sound(577, 2, 60, 0)
    Sound(861, 2, 60, 0)
    BeginChrThread(0xFE, 0, 0, 35)
    OP_87(0x5, 0x0, 0x14, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Return()

    # Function_39_53AA end

    def Function_40_544E(): pass

    label("Function_40_544E")

    OP_71(0x15, 0xB5, 0xF0, 0x0, 0x20)

    def lambda_545F():
        OP_96(0xFE, 0x11F8, 0x0, 0xFFFF2158, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_545F)
    WaitChrThread(0xFE, 1)
    OP_71(0x15, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x15)
    OP_71(0x15, 0x12C, 0x12A, 0x0, 0x0)
    OP_79(0x15)
    OP_87(0x5, 0x1, 0x15, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Return()

    # Function_40_544E end

    def Function_41_54C8(): pass

    label("Function_41_54C8")

    SetChrPos(0xFE, -800, 0, -70600, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_54E6():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFF26D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_54E6)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)

    label("loc_5511")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56A1")
    SetChrSubChip(0xFE, 0x2)

    def lambda_5525():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5525)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    Jump("loc_5511")

    label("loc_56A1")

    Return()

    # Function_41_54C8 end

    def Function_42_56A2(): pass

    label("Function_42_56A2")

    SetChrPos(0xFE, 1700, 0, -69800, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_56C0():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFF29F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56C0)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)

    label("loc_56EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_587B")
    SetChrSubChip(0xFE, 0x2)

    def lambda_56FF():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_56FF)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    Jump("loc_56EB")

    label("loc_587B")

    Return()

    # Function_42_56A2 end

    def Function_43_587C(): pass

    label("Function_43_587C")

    SetChrPos(0xFE, 200, 0, -71300, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_589A():
        OP_96(0xFE, 0xC8, 0x0, 0xFFFF2414, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_589A)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)

    label("loc_58C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A55")
    SetChrSubChip(0xFE, 0x2)

    def lambda_58D9():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_58D9)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    Jump("loc_58C5")

    label("loc_5A55")

    Return()

    # Function_43_587C end

    def Function_44_5A56(): pass

    label("Function_44_5A56")

    Sound(497, 2, 20, 0)
    Sound(825, 2, 20, 0)
    Sleep(200)
    OP_25(0x1F1, 0x19)
    OP_25(0x339, 0x19)
    Sleep(200)
    OP_25(0x1F1, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(200)
    OP_25(0x1F1, 0x23)
    OP_25(0x339, 0x23)
    Sleep(200)
    OP_25(0x1F1, 0x28)
    OP_25(0x339, 0x28)
    Sleep(200)
    OP_25(0x1F1, 0x2D)
    OP_25(0x339, 0x2D)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    OP_25(0x339, 0x32)
    Sleep(200)
    OP_25(0x1F1, 0x37)
    OP_25(0x339, 0x37)
    Sleep(200)
    OP_25(0x1F1, 0x3C)
    OP_25(0x339, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x41)
    Sleep(200)
    OP_25(0x1F1, 0x46)
    Sleep(200)
    OP_25(0x1F1, 0x4B)
    Return()

    # Function_44_5A56 end

    def Function_45_5AD0(): pass

    label("Function_45_5AD0")

    OP_25(0x35D, 0x14)
    Sleep(300)
    OP_25(0x35D, 0xF)
    Sleep(300)
    OP_25(0x35D, 0xA)
    Sleep(300)
    OP_25(0x35D, 0x5)
    Sleep(300)
    OP_25(0x35D, 0x0)
    Return()

    # Function_45_5AD0 end

    def Function_46_5AF1(): pass

    label("Function_46_5AF1")

    OP_25(0x361, 0x46)
    OP_25(0x241, 0x2D)
    OP_25(0x35D, 0x2D)
    Sleep(250)
    OP_25(0x361, 0x3C)
    OP_25(0x241, 0x28)
    OP_25(0x35D, 0x28)
    Sleep(250)
    OP_25(0x361, 0x32)
    OP_25(0x241, 0x23)
    OP_25(0x35D, 0x23)
    Sleep(250)
    OP_25(0x361, 0x28)
    OP_25(0x241, 0x1E)
    OP_25(0x35D, 0x1E)
    Sleep(250)
    OP_25(0x361, 0x1E)
    OP_25(0x241, 0x19)
    OP_25(0x35D, 0x19)
    Return()

    # Function_46_5AF1 end

    def Function_47_5B3A(): pass

    label("Function_47_5B3A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北·克洛斯贝尔市\x01",
            "东·克洛斯贝尔空港\x01",
            "南·圣乌尔斯拉医科大学　１５３赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_47_5B3A end

    SaveToFile()

Try(main)
