from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0040.bin",                # FileName
        "r0040",                    # MapName
        "r0040",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0040", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x04,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 4, 0, 5],
    )

    BuildStringList((
        "r0040",                  # 0
        "列車",                   # 1
        "パープルシャルロ",       # 2
        "パープルシャルロ",       # 3
        "サベージホーン",         # 4
        "サベージホーン",         # 5
        "ゴールドスタチュー",     # 6
        "幻獣",                   # 7
        "共和国飛行艇",           # 8
        "共和国飛行艇",           # 9
        "共和国戦車",             # 10
        "共和国戦車",             # 11
        "共和国戦車",             # 12
        "共和国戦車",             # 13
        "共和国戦車",             # 14
        "アイオーン２",           # 15
        "共和国戦車",             # 16
        "共和国戦車",             # 17
        "共和国戦車",             # 18
        "共和国戦車",             # 19
        "共和国戦車",             # 20
        "SE制御",                 # 21
        "br0000",                 # 22
        "br0000",                 # 23
        "br0000",                 # 24
        "br0000",                 # 25
        "br0000",                 # 26
        "br0000",                 # 27
        "br0000",                 # 28
        "br0000",                 # 29
        "br0000",                 # 30
        "br0000",                 # 31
        "クロスベル市・アルモリカ村方面",# 32
        "タングラム門方面",       # 33
    ))

    ATBonus("ATBonus_620", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_640", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_400A", 0,   8,   5,   0,   6,   4,   0)
    Sepith("Sepith_4012", 5,   10,  0,   2,   0,   5,   2)
    Sepith("Sepith_3FFA", 3,   4,   11,  0,   3,   4,   0)
    Sepith("Sepith_3FE2", 2,   7,   0,   5,   4,   2,   2)
    Sepith("Sepith_4002", 27,  27,  27,  27,  27,  27,  27)
    Sepith("Sepith_401A", 7,   9,   15,  5,   6,   3,   5)

    MonsterBattlePostion("MonsterBattlePostion_680", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_684", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_688", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_68C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_690", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_694", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_698", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_69C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_6E4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_6E8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_6F4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_6F8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6FC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_660", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_664", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_668", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_66C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_670", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_674", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_678", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_67C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 5, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 2, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_72C", 14, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_730", 5, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_734", 11, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_738", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_73C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_700", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_704", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_708", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_70C", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_710", 14, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_714", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_718", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_71C", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_878", 0x0000, 59, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_400A", 30, 45, 20, 5,
        (
            ("ms66700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms66700.dat", "ms66700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_660", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms66700.dat", "ms69300.dat", "ms66700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms66700.dat", "ms66700.dat", "ms69300.dat", "ms69300.dat", 0, 0, 0, 0, "MonsterBattlePostion_660", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
        )
    )

    BattleInfo(
        "BattleInfo_940", 0x0000, 59, 6, 45, 6, 1, 15, 0, "br0000", "Sepith_4012", 30, 45, 20, 5,
        (
            ("ms69300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms69300.dat", "ms69300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_660", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms69300.dat", "ms66700.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms69300.dat", "ms69300.dat", "ms66700.dat", "ms66700.dat", 0, 0, 0, 0, "MonsterBattlePostion_660", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
        )
    )

    BattleInfo(
        "BattleInfo_740", 0x0000, 60, 6, 45, 6, 1, 50, 0, "br0000", "Sepith_3FFA", 30, 45, 25, 0,
        (
            ("ms64000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms64000.dat", "ms64000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_660", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms64000.dat", "ms64000.dat", "ms64000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7DC", 0x0000, 59, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_3FE2", 30, 45, 25, 0,
        (
            ("ms69900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms69900.dat", "ms69900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_660", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms69900.dat", "ms63000.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AA4", 0x0000, 59, 6, 90, 8, 1, 50, 0, "br0000", "Sepith_4002", 30, 45, 25, 0,
        (
            ("ms66400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms66400.dat", "ms66400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_660", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms66400.dat", "ms66400.dat", "ms66400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A08", 0x0000, 77, 6, 45, 6, 1, 40, 0, "br0000", "Sepith_401A", 40, 35, 25, 0,
        (
            ("ms63701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_660", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7450", "ed7453", "ATBonus_620"),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_C0C", 0x0000, 100, 6, 0, 0, 1, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms74201.dat", "ms74201.dat", "ms74201.dat", "ms74201.dat", "ms74201.dat", "ms74201.dat", 0, 0, "MonsterBattlePostion_720", "MonsterBattlePostion_6E0", "ed7451", "ed7453", "ATBonus_640"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B40", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66700.dat", "ms66700.dat", "ms66700.dat", "ms66700.dat", "ms66700.dat", "ms66700.dat", "ms66700.dat", "ms66700.dat", "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7453", "ed7453", "ATBonus_620"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B84", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "MonsterBattlePostion_680", "MonsterBattlePostion_6E0", "ed7453", "ed7453", "ATBonus_620"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BC8", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88702.dat", "ms88802.dat", "ms88802.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_700", "MonsterBattlePostion_700", "ed7454", "ed7453", "ATBonus_640"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
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
        "monster/ch64050.itc",               # 10
        "monster/ch64051.itc",               # 11
        "monster/ch69950.itc",               # 12
        "monster/ch69950.itc",               # 13
        "monster/ch66750.itc",               # 14
        "monster/ch66750.itc",               # 15
        "monster/ch69350.itc",               # 16
        "monster/ch69351.itc",               # 17
        "monster/ch63750.itc",               # 18
        "monster/ch63751.itc",               # 19
        "monster/ch66450.itc",               # 1A
        "monster/ch66450.itc",               # 1B
        "monster/ch74250.itc",               # 1C
        "monster/ch74250.itc",               # 1D
    ))

    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(121879,  -9000,   -38750,  270,  484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(72540,   -6000,   -54830,  270,  484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(121879,  -9000,   -38750,  270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(72540,   -6000,   -54830,  270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(9739,    500,     -15649,  180,  484,  0x0, 0,   28,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(400,     4090,    0,       0x1010000,    "BattleInfo_878", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(16300,   6830,    0,       0x1010000,    "BattleInfo_878", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(8240,    -13730,  0,       0x1010000,    "BattleInfo_940", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(71150,   -40180,  -6000,   0x1010000,    "BattleInfo_740", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(54700,   -53920,  -6000,   0x1010000,    "BattleInfo_7DC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(84390,   -70870,  -8000,   0x1010000,    "BattleInfo_AA4", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(96330,   -71440,  -9250,   0x1010000,    "BattleInfo_7DC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(145270,  -47320,  -8170,   0x1010000,    "BattleInfo_940", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(97510,   -84120,  -12510,  0x1010000,    "BattleInfo_878", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(131430,  -41690,  -9000,   0x1010000,    "BattleInfo_740", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(10940,   -4140,   0,       0x1010000,    "BattleInfo_A08", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(42050,   -25350,  -2710,   0x1010000,    "BattleInfo_A08", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(127590,  -64060,  -8000,   0x1010000,    "BattleInfo_A08", 0,   24,  0xFFFF, 8,  9)

    DeclEvent(0x0040, 0, 12,  121.26000213623047,    -38.47999954223633,    -10.0,                 16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -15.157500267028809,   4.809999942779541,     2.5,                   1.0])

    DeclActor(9740,    0,       -15650,  1200,    9740,    1000,    -15650,  0x007C, 0,  6,  0x0000)
    DeclActor(141800,  -9000,   -38920,  1200,    141800,  -8000,   -38920,  0x007C, 0,  7,  0x0000)
    DeclActor(121880,  -9000,   -38750,  1200,    121880,  -9000,   -38750,  0x007C, 0,  8,  0x0000)
    DeclActor(72540,   -6000,   -54830,  1200,    72540,   -6000,   -54830,  0x007C, 0,  9,  0x0000)

    PlaceName(-30.0, 0.0, 5.0, 0x0000, 0x0000, "クロスベル市・アルモリカ村方面")
    PlaceName(182.0, 0.0, -64.0, 0x0000, 0x0000, "タングラム門方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 1])                         # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 9
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_D9C",          # 00, 0
        "Function_1_DBB",          # 01, 1
        "Function_2_DDA",          # 02, 2
        "Function_3_DF2",          # 03, 3
        "Function_4_E79",          # 04, 4
        "Function_5_EA0",          # 05, 5
        "Function_6_16D1",         # 06, 6
        "Function_7_198D",         # 07, 7
        "Function_8_1ADE",         # 08, 8
        "Function_9_1E3C",         # 09, 9
        "Function_10_219A",        # 0A, 10
        "Function_11_21CE",        # 0B, 11
        "Function_12_21D2",        # 0C, 12
        "Function_13_224E",        # 0D, 13
        "Function_14_2366",        # 0E, 14
        "Function_15_30CE",        # 0F, 15
        "Function_16_30F1",        # 10, 16
        "Function_17_3117",        # 11, 17
        "Function_18_313D",        # 12, 18
        "Function_19_3163",        # 13, 19
        "Function_20_3189",        # 14, 20
        "Function_21_319D",        # 15, 21
        "Function_22_31B1",        # 16, 22
        "Function_23_324A",        # 17, 23
        "Function_24_32F2",        # 18, 24
        "Function_25_33AE",        # 19, 25
        "Function_26_3431",        # 1A, 26
        "Function_27_34BF",        # 1B, 27
        "Function_28_3550",        # 1C, 28
        "Function_29_35E1",        # 1D, 29
        "Function_30_3666",        # 1E, 30
        "Function_31_36D2",        # 1F, 31
        "Function_32_36FB",        # 20, 32
        "Function_33_3726",        # 21, 33
        "Function_34_3785",        # 22, 34
        "Function_35_37DE",        # 23, 35
        "Function_36_3837",        # 24, 36
        "Function_37_3890",        # 25, 37
        "Function_38_38E9",        # 26, 38
        "Function_39_39FA",        # 27, 39
        "Function_40_3B05",        # 28, 40
        "Function_41_3C10",        # 29, 41
        "Function_42_3D1B",        # 2A, 42
        "Function_43_3E2C",        # 2B, 43
        "Function_44_3E9F",        # 2C, 44
        "Function_45_3F20",        # 2D, 45
        "Function_46_3F39",        # 2E, 46
    ))


    def Function_0_D9C(): pass

    label("Function_0_D9C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DBA")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_D9C")

    label("loc_DBA")

    Return()

    # Function_0_D9C end

    def Function_1_DBB(): pass

    label("Function_1_DBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DD9")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_DBB")

    label("loc_DD9")

    Return()

    # Function_1_DBB end

    def Function_2_DDA(): pass

    label("Function_2_DDA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DF1")
    OP_A1(0xFE, 0x5DC, 0x1, 0x0)
    Jump("Function_2_DDA")

    label("loc_DF1")

    Return()

    # Function_2_DDA end

    def Function_3_DF2(): pass

    label("Function_3_DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E0C")
    SetMapObjFlags(0x2, 0x2000000)
    SetMapObjFlags(0x5, 0x2000000)
    Jump("loc_E78")

    label("loc_E0C")

    SetMapObjFlags(0x6, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)

    label("loc_E78")

    Return()

    # Function_3_DF2 end

    def Function_4_E79(): pass

    label("Function_4_E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E8D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 14)
    Jump("loc_E9C")

    label("loc_E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E9C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)

    label("loc_E9C")

    Call(0, 10)
    Return()

    # Function_4_E79 end

    def Function_5_EA0(): pass

    label("Function_5_EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_EB2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC5")
    OP_1B(0x1, 0x0, 0x2E)

    label("loc_EC5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EEC")
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x5, 0x4)
    Jump("loc_F55")

    label("loc_EEC")

    OP_78(0x5, 0xE)
    ClearMapObjFlags(0x5, 0x4)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x1)
    SetChrPos(0xE, 121260, -9000, -38480, 0)
    OP_93(0xE, 0x0, 0x0)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, 121260, -9000, -38480, 3000, 3000, 90000)

    label("loc_F55")

    OP_52(0x27, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1485")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xF, 0x82, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1531")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xF, 0x82, 0x0)
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
    ClearMapObjFlags(0x24, 0x4)
    ClearMapObjFlags(0x25, 0x4)
    ClearMapObjFlags(0x26, 0x4)
    ClearMapObjFlags(0x27, 0x4)
    ClearMapObjFlags(0x28, 0x4)
    ClearMapObjFlags(0x29, 0x4)
    ClearMapObjFlags(0x2A, 0x4)
    Jump("loc_15A3")

    label("loc_1531")

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
    SetMapObjFlags(0x24, 0x4)
    SetMapObjFlags(0x25, 0x4)
    SetMapObjFlags(0x26, 0x4)
    SetMapObjFlags(0x27, 0x4)
    SetMapObjFlags(0x28, 0x4)
    SetMapObjFlags(0x29, 0x4)
    SetMapObjFlags(0x2A, 0x4)

    label("loc_15A3")

    SetMapObjFlags(0x2, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15C8")
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_15D4")

    label("loc_15C8")

    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)

    label("loc_15D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E7")
    OP_70(0x0, 0x0)
    Jump("loc_15EB")

    label("loc_15E7")

    OP_70(0x0, 0x1E)

    label("loc_15EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15FE")
    OP_70(0x1, 0x0)
    Jump("loc_1602")

    label("loc_15FE")

    OP_70(0x1, 0x1E)

    label("loc_1602")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1663")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 121880, -9000, -38750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_1663")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16AF")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 72540, -6000, -54830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_16AF")

    OP_1C(0x0, 0x2B, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x2C, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x2D, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    Return()

    # Function_5_EA0 end

    def Function_6_16D1(): pass

    label("Function_6_16D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1776")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱の中から強力な魔獣の気配を感じる。\x01",
            "【推定魔獣レベル１００】\x01",
            "宝箱を開きますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1776")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_1776")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1947")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1875")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_17D3():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_17D3)

    def lambda_17ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_17ED)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xD, 1)
    Battle("BattleInfo_C0C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1856"),
        (2, "loc_1865"),
        (1, "loc_1872"),
        (SWITCH_DEFAULT, "loc_1875"),
    )


    label("loc_1856")

    SetScenarioFlags(0x214, 0)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_1875")

    label("loc_1865")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1872")

    OP_B9(0x0)
    Return()

    label("loc_1875")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xAA, 1)"), scpexpr(EXPR_END)), "loc_18D2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E9, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_1942")

    label("loc_18D2")

    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xAA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xAA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1942")

    Jump("loc_1981")

    label("loc_1947")

    FadeToDark(300, 0, 100)

    #A0005
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

    label("loc_1981")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_16D1 end

    def Function_7_198D(): pass

    label("Function_7_198D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8D")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3C, 1)"), scpexpr(EXPR_END)), "loc_1A16")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E9, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1A88")

    label("loc_1A16")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x3C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x3C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A88")

    Jump("loc_1AD2")

    label("loc_1A8D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
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

    label("loc_1AD2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_198D end

    def Function_8_1ADE(): pass

    label("Function_8_1ADE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C96")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_1C77")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0009
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C72")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_1C6F")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1B98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1B98)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0010
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
    Battle("BattleInfo_B40", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C6A")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C51")
    Call(1, 5)
    Jump("loc_1C6A")

    label("loc_1C51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C67")
    Call(1, 4)
    Jump("loc_1C6A")

    label("loc_1C67")

    Call(1, 3)

    label("loc_1C6A")

    Jump("loc_1C72")

    label("loc_1C6F")

    Call(1, 1)

    label("loc_1C72")

    Jump("loc_1C8D")

    label("loc_1C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_1C8D")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1C8D")

    TalkEnd(0xFF)
    Return()

    label("loc_1C96")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_1E21")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0011
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1C")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_1E19")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1D42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1D42)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0012
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
    Battle("BattleInfo_B84", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E14")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1DFB")
    Call(1, 5)
    Jump("loc_1E14")

    label("loc_1DFB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E11")
    Call(1, 4)
    Jump("loc_1E14")

    label("loc_1E11")

    Call(1, 3)

    label("loc_1E14")

    Jump("loc_1E1C")

    label("loc_1E19")

    Call(1, 1)

    label("loc_1E1C")

    Jump("loc_1E37")

    label("loc_1E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_1E37")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1E37")

    TalkEnd(0xFF)
    Return()

    # Function_8_1ADE end

    def Function_9_1E3C(): pass

    label("Function_9_1E3C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FF4")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_1FD5")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0013
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD0")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_1FCD")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1EF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1EF6)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0014
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
    Battle("BattleInfo_B40", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FC8")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1FAF")
    Call(1, 5)
    Jump("loc_1FC8")

    label("loc_1FAF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1FC5")
    Call(1, 4)
    Jump("loc_1FC8")

    label("loc_1FC5")

    Call(1, 3)

    label("loc_1FC8")

    Jump("loc_1FD0")

    label("loc_1FCD")

    Call(1, 1)

    label("loc_1FD0")

    Jump("loc_1FEB")

    label("loc_1FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_1FEB")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1FEB")

    TalkEnd(0xFF)
    Return()

    label("loc_1FF4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_217F")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0015
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_217A")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2177")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_20A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_20A0)
    TurnDirection(0xC, 0x0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    PlayEffect(0x7, 0x1, 0xC, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0016
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
    Battle("BattleInfo_B84", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2172")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2159")
    Call(1, 5)
    Jump("loc_2172")

    label("loc_2159")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_216F")
    Call(1, 4)
    Jump("loc_2172")

    label("loc_216F")

    Call(1, 3)

    label("loc_2172")

    Jump("loc_217A")

    label("loc_2177")

    Call(1, 1)

    label("loc_217A")

    Jump("loc_2195")

    label("loc_217F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2195")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2195")

    TalkEnd(0xFF)
    Return()

    # Function_9_1E3C end

    def Function_10_219A(): pass

    label("Function_10_219A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21B7")
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)

    label("loc_21B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 0)), scpexpr(EXPR_END)), "loc_21C8")
    ClearScenarioFlags(0x3C, 0)
    Jump("loc_21CD")

    label("loc_21C8")

    SetChrFlags(0x22, 0x80)

    label("loc_21CD")

    Return()

    # Function_10_219A end

    def Function_11_21CE(): pass

    label("Function_11_21CE")

    Call(1, 6)
    Return()

    # Function_11_21CE end

    def Function_12_21D2(): pass

    label("Function_12_21D2")

    Battle("BattleInfo_BC8", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2219")
    OP_90(0x0, 124600, -9000, -44230, 180)
    EventEnd(0x5)
    SetChrFlags(0xE, 0x8000)
    Jump("loc_224D")

    label("loc_2219")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_222C")
    Jump("loc_224D")

    label("loc_222C")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x5, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 2)
    EventEnd(0x5)

    label("loc_224D")

    Return()

    # Function_12_21D2 end

    def Function_13_224E(): pass

    label("Function_13_224E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    SetChrPos(0x101, 93000, -13000, -132000, 0)
    SetChrPos(0x109, 93000, -13000, -132000, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xEB, 0x93, 0x6F, 0x28, 0x96, 0x0)
    OP_78(0x2, 0x8)
    OP_49()
    SetChrPos(0x8, 130000, -7150, -108000, 0)
    OP_D5(0x8, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    OP_68(85000, -5150, -100000, 0)
    MoveCamera(15, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    MoveCamera(20, 25, 0, 5000)
    SetCameraDistance(37500, 5000)
    OP_82(0x64, 0x0, 0xBB8, 0x1B58)

    def lambda_2324():
        OP_96(0xFE, 0x0, 0xFFFFE412, 0xFFFE5A20, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2324)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(456, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_224E end

    def Function_14_2366(): pass

    label("Function_14_2366")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadEffect(0x0, "event/ev15060.eff")
    LoadEffect(0x1, "event/ev15058.eff")
    LoadEffect(0x2, "event/ev14002.eff")
    LoadEffect(0x3, "event/ev15102.eff")
    LoadEffect(0x4, "event/ev15056.eff")
    LoadEffect(0x5, "event/ev15057.eff")
    LoadEffect(0x6, "event/ev15059.eff")
    LoadEffect(0x7, "event/ev17022.eff")
    LoadEffect(0x9, "event/eva03_01.eff")
    OP_F3(200000)
    SoundLoad(980)
    SoundLoad(924)
    SoundLoad(868)
    SoundLoad(825)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 0, -17900, 0, 0)
    OP_74(0x6, 0x1E)
    OP_78(0x6, 0x16)
    OP_93(0x16, 0xB4, 0x0)
    SetChrFlags(0x16, 0x1)
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_70(0x6, 0xDD)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x6, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 0, 0, 0, 0)
    OP_78(0x7, 0xF)
    OP_93(0xF, 0x0, 0x0)
    SetMapObjFrame(0x7, "slash", 0x0, 0x1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 0, 0)
    OP_78(0x8, 0x10)
    OP_93(0x10, 0x0, 0x0)
    SetMapObjFrame(0x8, "slash", 0x0, 0x1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, 0, 0, 0)
    OP_74(0x9, 0x1E)
    OP_78(0x9, 0x11)
    OP_93(0x11, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, 0, 0, 0)
    OP_74(0xA, 0x1E)
    OP_78(0xA, 0x12)
    OP_93(0x12, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 0, 0, 0, 0)
    OP_74(0xB, 0x1E)
    OP_78(0xB, 0x13)
    OP_93(0x13, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 0, 0, 0, 0)
    OP_74(0xC, 0x1E)
    OP_78(0xC, 0x14)
    OP_93(0x14, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 0, 0, 0, 0)
    OP_74(0xD, 0x1E)
    OP_78(0xD, 0x15)
    OP_93(0x15, 0x0, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 0, 0, 0, 0)
    OP_74(0xE, 0x1E)
    OP_78(0xE, 0x17)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 0, 0, 0, 0)
    OP_74(0xF, 0x1E)
    OP_78(0xF, 0x18)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 0, 0, 0, 0)
    OP_74(0x10, 0x1E)
    OP_78(0x10, 0x19)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 0, 0, 0, 0)
    OP_74(0x11, 0x1E)
    OP_78(0x11, 0x1A)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 0, 0, 0, 0)
    OP_74(0x12, 0x1E)
    OP_78(0x12, 0x1B)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2B, 0x4)
    SetMapObjFlags(0x2C, 0x4)
    SetMapObjFlags(0x2D, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetChrPos(0x16, 30000, 0, -11000, 0)
    SetChrPos(0xF, 66000, 5000, -53290, 0)
    SetChrPos(0x10, 100540, 5110, -3110, 0)
    SetChrPos(0x11, 75650, -7600, -47820, 0)
    SetChrPos(0x12, 89200, -7950, -54850, 0)
    SetChrPos(0x13, 102800, -7950, -61940, 0)
    SetChrPos(0x14, 117510, -7950, -67760, 0)
    SetChrPos(0x15, 133180, -7950, -62840, 0)
    OP_93(0x16, 0x5A, 0x0)
    OP_93(0xF, 0x13B, 0x0)
    OP_93(0x10, 0x10E, 0x0)
    OP_93(0x11, 0x113, 0x0)
    OP_93(0x12, 0x131, 0x0)
    OP_93(0x13, 0x13B, 0x0)
    OP_93(0x14, 0x145, 0x0)
    OP_93(0x15, 0x116, 0x0)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0xB, 0x1000)
    ClearMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xD, 0x1000)
    OP_68(55930, -6200, -21570, 0)
    MoveCamera(51, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(79580, 0)
    OP_11(0xAB, 0xE3, 0xEB, 0x32, 0x15E, 0x0)
    OP_D5(0xF, 0x4E20, 0x4CE78, 0x0, 0x0)
    OP_D5(0x10, 0x4E20, 0x41EB0, 0x0, 0x0)
    OP_D5(0x11, 0x55F00, 0x43238, 0x0, 0x0)
    OP_93(0x11, 0x13B, 0x0)
    OP_93(0x12, 0x131, 0x0)
    OP_93(0x13, 0x127, 0x0)
    OP_93(0x14, 0x113, 0x0)
    OP_93(0x15, 0x101, 0x0)
    Sound(924, 2, 40, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0x1C, 1, 0, 44)
    FadeToBright(1000, 0)
    BeginChrThread(0xF, 0, 0, 22)
    BeginChrThread(0x10, 0, 0, 23)
    BeginChrThread(0xF, 1, 0, 20)
    BeginChrThread(0x10, 1, 0, 21)
    BeginChrThread(0x11, 0, 0, 24)
    BeginChrThread(0x12, 0, 0, 25)
    OP_68(66630, -6200, -31450, 6000)
    MoveCamera(23, 17, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(79580, 6000)
    OP_0D()
    Sleep(300)
    BlurSwitch(0x1F4, 0x77FFFFFF, 0x0, 0x1, 0xA)
    Sleep(700)
    Sound(990, 0, 100, 0)
    OP_25(0x39C, 0x32)
    CancelBlur(1000)
    Sleep(4000)
    WaitChrThread(0xF, 0)
    WaitChrThread(0x10, 0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    BeginChrThread(0x13, 0, 0, 26)
    BeginChrThread(0x14, 0, 0, 27)
    BeginChrThread(0x15, 0, 0, 28)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0xA, 0x1000)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFlags(0xD, 0x1000)
    OP_68(107050, -6200, -59960, 5000)
    MoveCamera(36, 14, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(47650, 5000)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    StopSound(924, 1000, 50)
    OP_6F(0x79)
    Sleep(200)
    SetChrPos(0x16, 85000, 0, 5000, 0)
    OP_93(0x16, 0x7D, 0x0)
    PlayEffect(0x9, 0x7, 0x16, 0x5, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0xB, 0x1000)
    ClearMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xD, 0x1000)
    OP_70(0x6, 0xDD)
    OP_68(97070, -17200, -39540, 0)
    MoveCamera(90, 29, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(122990, 0)
    OP_11(0xAB, 0xE3, 0xEB, 0x4B, 0x12C, 0x0)
    Fade(500)
    BeginChrThread(0x16, 0, 0, 29)
    BeginChrThread(0x1C, 1, 0, 45)
    OP_68(93660, -17300, -42640, 3000)
    MoveCamera(108, 28, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(110380, 3000)
    OP_0D()
    BlurSwitch(0x1F4, 0x55FFFFFF, 0x0, 0x1, 0xA)
    OP_6F(0x79)
    StopEffect(0x7, 0x0)
    OP_70(0x6, 0xDD)
    SetMapObjFrame(0x9, "head", 0x0, 0x1)
    OP_FD(0x17, 0x11)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFrame(0xA, "head", 0x0, 0x1)
    OP_FD(0x18, 0x12)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFrame(0xB, "head", 0x0, 0x1)
    OP_FD(0x19, 0x13)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFrame(0xC, "head", 0x0, 0x1)
    OP_FD(0x1A, 0x14)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0xD, "head", 0x0, 0x1)
    OP_FD(0x1B, 0x15)
    ClearMapObjFlags(0x12, 0x4)
    SetChrPos(0x16, 13000, 15000, -2000, 0)
    OP_68(105580, -15600, -54960, 0)
    MoveCamera(104, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(67420, 0)
    OP_11(0xAB, 0xE3, 0xEB, 0x32, 0x15E, 0x0)
    CancelBlur(0)
    Fade(500)
    SetCameraDistance(64420, 2500)
    OP_0D()
    Sound(147, 0, 100, 0)
    BeginChrThread(0x17, 1, 0, 15)
    BeginChrThread(0x18, 1, 0, 16)
    BeginChrThread(0x19, 1, 0, 17)
    BeginChrThread(0x1A, 1, 0, 18)
    BeginChrThread(0x1B, 1, 0, 19)
    Sleep(600)
    Sleep(900)
    OP_68(113500, -16300, -47500, 0)
    MoveCamera(88, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(73500, 0)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x18, 0x2)
    EndChrThread(0x19, 0x2)
    EndChrThread(0x1A, 0x2)
    EndChrThread(0x1B, 0x2)
    TurnDirection(0x17, 0x16, 0)
    TurnDirection(0x18, 0x16, 0)
    TurnDirection(0x19, 0x16, 0)
    TurnDirection(0x1A, 0x16, 0)
    TurnDirection(0x1B, 0x16, 0)
    Fade(500)
    BeginChrThread(0x17, 3, 0, 33)
    BeginChrThread(0x18, 3, 0, 34)
    BeginChrThread(0x19, 3, 0, 35)
    BeginChrThread(0x1A, 3, 0, 36)
    BeginChrThread(0x1B, 3, 0, 37)
    OP_0D()
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    Sleep(2500)
    OP_6F(0x79)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    SetChrPos(0x16, 13000, 15000, -2000, 0)
    SetChrFlags(0x16, 0x8000)
    PlayEffect(0x9, 0x6, 0x16, 0x5, 0, 0, 0, 180, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0x7, 0x16, 0x5, 0, 0, 0, 180, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Fade(500)
    OP_68(90640, -18500, -16970, 0)
    MoveCamera(99, 26, 9, 0)
    OP_6E(510, 0)
    SetCameraDistance(115750, 0)
    OP_25(0x3EB, 0x32)
    Sound(980, 2, 70, 0)
    BeginChrThread(0x16, 0, 0, 30)
    OP_68(90630, -16800, -16960, 4000)
    MoveCamera(319, 16, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(102650, 4000)
    OP_0D()
    Sleep(700)
    CancelBlur(700)
    Sleep(2300)
    StopEffect(0x6, 0x2)
    StopEffect(0x7, 0x2)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_6F(0x79)
    WaitChrThread(0x16, 0)
    StopSound(1003, 1000, 40)
    EndChrThread(0x17, 0x3)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1B, 0x3)
    Fade(500)
    OP_68(89470, -14000, -55880, 0)
    MoveCamera(282, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(80220, 0)
    BeginChrThread(0x16, 0, 0, 31)
    BeginChrThread(0x16, 1, 0, 32)
    OP_68(89470, -15000, -55880, 3300)
    MoveCamera(283, 15, 0, 3300)
    OP_6E(510, 3300)
    SetCameraDistance(72940, 3300)
    OP_0D()
    CancelBlur(0)
    Sleep(1500)
    WaitChrThread(0x16, 0)
    WaitChrThread(0x16, 1)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x18, 0x2)
    EndChrThread(0x19, 0x2)
    EndChrThread(0x1A, 0x2)
    EndChrThread(0x1B, 0x2)
    Sleep(500)
    BlurSwitch(0x1F4, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_87(0x4, 0x1, 0x6, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(500)
    Sound(1036, 0, 100, 0)
    Sleep(1000)
    CancelBlur(0)
    Fade(500)
    OP_68(98760, -12900, -52050, 0)
    MoveCamera(299, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(57360, 0)
    Sleep(700)
    BeginChrThread(0x16, 3, 0, 43)
    OP_0D()
    OP_68(63220, -12900, -36880, 4500)
    MoveCamera(327, 24, 0, 4500)
    OP_6E(510, 4500)
    SetCameraDistance(57360, 4500)
    OP_6F(0x79)
    WaitChrThread(0x16, 3)
    OP_68(83000, -4000, -54640, 0)
    MoveCamera(76, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(58360, 0)
    OP_11(0xAB, 0xE3, 0xEB, 0x4B, 0x12C, 0x0)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    Fade(500)
    StopSound(980, 4000, 60)
    OP_68(85560, -4000, -53730, 5000)
    MoveCamera(76, 21, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(81710, 5000)
    OP_0D()
    OP_6F(0x79)
    StopSound(868, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e4210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2366 end

    def Function_15_30CE(): pass

    label("Function_15_30CE")


    def lambda_30D3():

        label("loc_30D3")

        TurnDirection(0xFE, 0x16, 13)
        Yield()
        Jump("loc_30D3")

    QueueWorkItem2(0xFE, 2, lambda_30D3)
    OP_74(0xE, 0xF)
    OP_71(0xE, 0x0, 0x1E, 0x0, 0x0)
    Return()

    # Function_15_30CE end

    def Function_16_30F1(): pass

    label("Function_16_30F1")

    Sleep(150)

    def lambda_30F9():

        label("loc_30F9")

        TurnDirection(0xFE, 0x16, 13)
        Yield()
        Jump("loc_30F9")

    QueueWorkItem2(0xFE, 2, lambda_30F9)
    OP_74(0xF, 0xF)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Return()

    # Function_16_30F1 end

    def Function_17_3117(): pass

    label("Function_17_3117")

    Sleep(300)

    def lambda_311F():

        label("loc_311F")

        TurnDirection(0xFE, 0x16, 13)
        Yield()
        Jump("loc_311F")

    QueueWorkItem2(0xFE, 2, lambda_311F)
    OP_74(0x10, 0xF)
    OP_71(0x10, 0x0, 0x1E, 0x0, 0x0)
    Return()

    # Function_17_3117 end

    def Function_18_313D(): pass

    label("Function_18_313D")

    Sleep(300)

    def lambda_3145():

        label("loc_3145")

        TurnDirection(0xFE, 0x16, 13)
        Yield()
        Jump("loc_3145")

    QueueWorkItem2(0xFE, 2, lambda_3145)
    OP_74(0x11, 0xF)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Return()

    # Function_18_313D end

    def Function_19_3163(): pass

    label("Function_19_3163")

    Sleep(300)

    def lambda_316B():

        label("loc_316B")

        TurnDirection(0xFE, 0x16, 13)
        Yield()
        Jump("loc_316B")

    QueueWorkItem2(0xFE, 2, lambda_316B)
    OP_74(0x12, 0xF)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Return()

    # Function_19_3163 end

    def Function_20_3189(): pass

    label("Function_20_3189")

    Sleep(500)
    OP_74(0x7, 0x4)
    OP_71(0x7, 0x0, 0x3C, 0x0, 0x0)
    Return()

    # Function_20_3189 end

    def Function_21_319D(): pass

    label("Function_21_319D")

    Sleep(2000)
    OP_74(0x8, 0x4)
    OP_71(0x8, 0x0, 0x3C, 0x0, 0x0)
    Return()

    # Function_21_319D end

    def Function_22_31B1(): pass

    label("Function_22_31B1")

    SetChrPos(0xFE, 85090, 10000, -62290, 0)
    OP_87(0x1, 0x0, 0x7, "body", 0x7, 0x1770, 0x0, 0xFFFFE890, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 61090, 2000, -56290)
    OP_9F(0x1, 45000, -6000, -51000)
    OP_9F(0x1, 22000, -12000, -46000)
    OP_9F(0x2, 0xFE, 22000, 0x0)
    OP_82(0x12C, 0x12C, 0x1770, 0x3E8)
    Sound(200, 0, 100, 0)
    Sleep(500)
    Sound(833, 0, 100, 0)
    StopEffect(0x0, 0x2)
    Return()

    # Function_22_31B1 end

    def Function_23_324A(): pass

    label("Function_23_324A")

    Sleep(700)
    SetChrPos(0xFE, 100540, 5110, -3110, 0)
    OP_87(0x1, 0x1, 0x8, "body", 0x7, 0x5DC, 0x0, 0xFFFFFA24, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 90000, 1500, 11000)
    OP_9F(0x1, 80000, -4000, 25000)
    OP_9F(0x1, 75000, -9000, 30000)
    OP_9F(0x2, 0xFE, 8500, 0x0)
    OP_82(0x96, 0x96, 0x1388, 0x1F4)
    Sound(200, 0, 60, 0)
    Sleep(500)
    Sound(833, 0, 60, 0)
    StopEffect(0x1, 0x2)
    StopSound(868, 1000, 90)
    StopSound(825, 1000, 90)
    Return()

    # Function_23_324A end

    def Function_24_32F2(): pass

    label("Function_24_32F2")

    Sleep(2000)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, 87560, -7900, -53490, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 83920, -7900, -50240)
    OP_9F(0x1, 79750, -7850, -48660)
    OP_9F(0x1, 75010, -7600, -48060)
    OP_9F(0x1, 67780, -6000, -47990)
    OP_9F(0x1, 64379, -6000, -46730)
    OP_9F(0x2, 0xFE, 5500, 0x7)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x7D0, 0x1)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Return()

    # Function_24_32F2 end

    def Function_25_33AE(): pass

    label("Function_25_33AE")

    Sleep(5000)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, 89530, -8000, -56000, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 83190, -8000, -49200)
    OP_9F(0x1, 79540, -8000, -48630)
    OP_9F(0x2, 0xFE, 5000, 0x7)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x7D0, 0x1)
    OP_71(0xA, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Return()

    # Function_25_33AE end

    def Function_26_3431(): pass

    label("Function_26_3431")

    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, 104100, -8000, -62830, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 99860, -8000, -60590)
    OP_9F(0x1, 93510, -8000, -59430)
    OP_9F(0x1, 90090, -8000, -56350)
    OP_9F(0x2, 0xFE, 5000, 0x7)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x7D0, 0x1)
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Return()

    # Function_26_3431 end

    def Function_27_34BF(): pass

    label("Function_27_34BF")

    Sleep(1000)
    OP_71(0xC, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, 119230, -8000, -67040, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 112980, -8000, -67120)
    OP_9F(0x1, 107530, -8000, -63290)
    OP_9F(0x1, 104760, -8000, -62000)
    OP_9F(0x2, 0xFE, 5000, 0x7)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x7D0, 0x1)
    OP_71(0xC, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Return()

    # Function_27_34BF end

    def Function_28_3550(): pass

    label("Function_28_3550")

    Sleep(1700)
    OP_71(0xD, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, 133500, -8000, -63480, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 127380, -8000, -64920)
    OP_9F(0x1, 123580, -8000, -67240)
    OP_9F(0x1, 118600, -8000, -67640)
    OP_9F(0x2, 0xFE, 5000, 0x7)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x7D0, 0x1)
    OP_71(0xD, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Return()

    # Function_28_3550 end

    def Function_29_35E1(): pass

    label("Function_29_35E1")

    OP_74(0x6, 0xF)
    OP_71(0x6, 0xF1, 0xF3, 0x0, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 85000, 10000, 5000, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 55000, 12000, -30000)
    OP_9F(0x1, 29000, 15000, -36500)
    OP_9F(0x1, 16000, 17000, -29500)
    OP_9F(0x1, 25000, 19000, -19500)
    OP_9F(0x2, 0xFE, 60000, 0x7)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 65000, 15000, -29500)
    OP_9F(0x2, 0xFE, 60000, 0x7)
    Return()

    # Function_29_35E1 end

    def Function_30_3666(): pass

    label("Function_30_3666")

    SetChrPos(0xFE, 13000, 15000, -2000, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x7D, 0x0)
    OP_9F(0x1, 58500, -1000, -38500)
    OP_9F(0x1, 86500, -1500, -54500)
    OP_9F(0x1, 102500, -2000, -61500)
    OP_9F(0x1, 122500, -4000, -65500)
    OP_9F(0x1, 131500, -1000, -66000)
    OP_9F(0x2, 0xFE, 35000, 0x2)
    Return()

    # Function_30_3666 end

    def Function_31_36D2(): pass

    label("Function_31_36D2")


    def lambda_36D7():
        TurnDirection(0xFE, 0x13, 300)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36D7)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 131500, -7000, -66000)
    OP_9F(0x2, 0xFE, 1800, 0x0)
    Return()

    # Function_31_36D2 end

    def Function_32_36FB(): pass

    label("Function_32_36FB")

    ClearMapObjFlags(0x6, 0x20)
    OP_79(0x6)
    Sound(982, 0, 100, 0)
    OP_74(0x6, 0xF)
    OP_71(0x6, 0x105, 0x118, 0x0, 0x0)
    OP_79(0x6)
    OP_74(0x6, 0xF)
    OP_70(0x6, 0xB)
    Return()

    # Function_32_36FB end

    def Function_33_3726(): pass

    label("Function_33_3726")

    Sleep(200)
    Sound(1003, 2, 80, 0)

    label("loc_372F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3784")
    OP_82(0x82, 0x82, 0xA8C, 0x1F4)
    OP_87(0x0, 0xFF, 0xE, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(820)
    Jump("loc_372F")

    label("loc_3784")

    Return()

    # Function_33_3726 end

    def Function_34_3785(): pass

    label("Function_34_3785")

    Sleep(350)

    label("loc_3788")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37DD")
    OP_82(0x64, 0x64, 0x9C4, 0x1F4)
    OP_87(0x0, 0xFF, 0xF, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(800)
    Jump("loc_3788")

    label("loc_37DD")

    Return()

    # Function_34_3785 end

    def Function_35_37DE(): pass

    label("Function_35_37DE")

    Sleep(500)

    label("loc_37E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3836")
    OP_82(0x50, 0x50, 0x8FC, 0x1F4)
    OP_87(0x0, 0xFF, 0x10, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(840)
    Jump("loc_37E1")

    label("loc_3836")

    Return()

    # Function_35_37DE end

    def Function_36_3837(): pass

    label("Function_36_3837")

    Sleep(650)

    label("loc_383A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_388F")
    OP_82(0x3C, 0x3C, 0x834, 0x1F4)
    OP_87(0x0, 0xFF, 0x11, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(830)
    Jump("loc_383A")

    label("loc_388F")

    Return()

    # Function_36_3837 end

    def Function_37_3890(): pass

    label("Function_37_3890")

    Sleep(800)

    label("loc_3893")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38E8")
    OP_82(0x28, 0x28, 0x76C, 0x1F4)
    OP_87(0x0, 0xFF, 0x12, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(860)
    Jump("loc_3893")

    label("loc_38E8")

    Return()

    # Function_37_3890 end

    def Function_38_38E9(): pass

    label("Function_38_38E9")

    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    OP_78(0x17, 0xFE)
    OP_D5(0xFE, 0x0, 0x497C8, 0x0, 0x0)
    Sound(200, 0, 100, 0)
    Sound(868, 2, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 30, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    OP_87(0x3, 0xFF, 0xD, "body", 0x7, 0x0, 0x3E8, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_38_38E9 end

    def Function_39_39FA(): pass

    label("Function_39_39FA")

    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    OP_78(0x16, 0xFE)
    OP_D5(0xFE, 0x0, 0x4EDB8, 0x0, 0x0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 30, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    OP_87(0x3, 0xFF, 0xC, "body", 0x7, 0x0, 0x3E8, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_39_39FA end

    def Function_40_3B05(): pass

    label("Function_40_3B05")

    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1150)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    OP_78(0x15, 0xFE)
    OP_D5(0xFE, 0x0, 0x4A768, 0x0, 0x0)
    Sound(200, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 30, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    OP_87(0x3, 0xFF, 0xB, "body", 0x7, 0x0, 0x3E8, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_40_3B05 end

    def Function_41_3C10(): pass

    label("Function_41_3C10")

    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1300)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    OP_78(0x14, 0xFE)
    OP_D5(0xFE, 0x0, 0x4A768, 0x0, 0x0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 280, 0, 90, 3, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    OP_87(0x3, 0xFF, 0xA, "body", 0x7, 0x0, 0x3E8, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_41_3C10 end

    def Function_42_3D1B(): pass

    label("Function_42_3D1B")

    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1450)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    OP_78(0x13, 0xFE)
    OP_D5(0xFE, 0x0, 0x4BED8, 0x0, 0x0)
    Sound(200, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(556, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 30, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    OP_87(0x3, 0xFF, 0x9, "body", 0x7, 0x0, 0x3E8, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_42_3D1B end

    def Function_43_3E2C(): pass

    label("Function_43_3E2C")

    SetMapObjFlags(0x13, 0x1000)
    SetMapObjFlags(0x14, 0x1000)
    SetMapObjFlags(0x15, 0x1000)
    SetMapObjFlags(0x16, 0x1000)
    SetMapObjFlags(0x17, 0x1000)
    OP_7D(0xEB, 0xEB, 0xEB, 0x0, 0xBB8)
    BeginChrThread(0x15, 3, 0, 38)
    Sleep(200)
    Sound(1014, 0, 80, 0)
    BeginChrThread(0x14, 3, 0, 39)
    Sleep(200)
    Sound(1014, 0, 80, 0)
    BeginChrThread(0x13, 3, 0, 40)
    Sleep(200)
    Sound(1014, 0, 80, 0)
    BeginChrThread(0x12, 3, 0, 41)
    Sleep(200)
    Sound(1014, 0, 80, 0)
    BeginChrThread(0x11, 3, 0, 42)
    Sleep(200)
    Sound(1014, 0, 80, 0)
    Return()

    # Function_43_3E2C end

    def Function_44_3E9F(): pass

    label("Function_44_3E9F")

    Sound(200, 0, 70, 0)
    Sound(868, 2, 0, 0)
    Sound(825, 2, 0, 0)
    Sleep(50)
    OP_25(0x364, 0xA)
    OP_25(0x339, 0xA)
    Sleep(50)
    OP_25(0x364, 0x14)
    OP_25(0x339, 0x14)
    Sleep(50)
    OP_25(0x364, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(50)
    OP_25(0x364, 0x28)
    OP_25(0x339, 0x28)
    Sleep(50)
    OP_25(0x364, 0x32)
    OP_25(0x339, 0x32)
    Sleep(50)
    OP_25(0x364, 0x3C)
    OP_25(0x339, 0x3C)
    Sleep(50)
    OP_25(0x364, 0x46)
    OP_25(0x339, 0x46)
    Sleep(50)
    OP_25(0x364, 0x50)
    OP_25(0x339, 0x50)
    Sleep(50)
    OP_25(0x364, 0x5A)
    OP_25(0x339, 0x5A)
    Sleep(50)
    OP_25(0x364, 0x64)
    OP_25(0x339, 0x64)
    Return()

    # Function_44_3E9F end

    def Function_45_3F20(): pass

    label("Function_45_3F20")

    Sleep(800)
    Sound(499, 0, 100, 0)
    Sound(999, 0, 100, 0)
    Sleep(800)
    Sound(998, 0, 100, 0)
    Return()

    # Function_45_3F20 end

    def Function_46_3F39(): pass

    label("Function_46_3F39")

    EventBegin(0x1)
    OP_E2(0x3)

    #C0017
    ChrTalk(
        0x101,
        (
            "#00001Fこっちはタングラム門方面か……\x02\x03",

            "これ以上近付くのは危険だな。\x01",
            "大人しく引き返そう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 156770, -8000, -68100, 270)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_46_3F39 end

    SaveToFile()

Try(main)
