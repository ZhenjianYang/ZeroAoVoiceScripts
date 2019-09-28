from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r1010.bin",                # FileName
        "r1010",                    # MapName
        "r1010",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("r1010", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x06,                       # PreInitFunctionIndex
        b'\x00\xff\x04',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 5, 0, 6],
    )

    BuildStringList((
        "r1010",                  # 0
        "弗兰茨巡警",             # 1
        "达利亚队员",             # 2
        "警官",                   # 3
        "警官",                   # 4
        "警官",                   # 5
        "警备队员",               # 6
        "警备队员",               # 7
        "格蕾丝",                 # 8
        "雷因兹",                 # 9
        "车",                     # 10
        "飙车族",                 # 11
        "警车",                   # 12
        "装甲车",                 # 13
        "警车２",                 # 14
        "警车３",                 # 15
        "装甲车２",               # 16
        "尤利",                   # 17
        "塞克斯",                 # 18
        "瑞吉",                   # 19
        "凯特巡警",               # 20
        "米蕾优三尉",             # 21
        "波纹",                   # 22
        "乌黑软体兽",             # 23
        "乌黑软体兽",             # 24
        "硬岩龙",                 # 25
        "硬岩龙",                 # 26
        "黑迟缓虫",               # 27
        "幻兽",                   # 28
        "SE控制",                 # 29
        "br1000",                 # 30
        "br1000",                 # 31
        "br1000",                 # 32
        "br1000",                 # 33
        "br1000",                 # 34
        "br1000",                 # 35
        "br1000",                 # 36
        "br1000",                 # 37
        "br1000",                 # 38
        "br1000",                 # 39
        "克洛斯贝尔市方向",       # 40
        "贝尔加德门方向",         # 41
    ))

    ATBonus("ATBonus_904", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_924", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_98B9", 5,   5,   0,   3,   0,   0,   0)
    Sepith("Sepith_98C1", 2,   1,   4,   1,   0,   2,   2)
    Sepith("Sepith_9889", 2,   1,   5,   0,   0,   3,   2)
    Sepith("Sepith_9881", 2,   0,   3,   4,   0,   0,   3)
    Sepith("Sepith_9879", 4,   2,   3,   0,   3,   0,   0)
    Sepith("Sepith_98D1", 11,  7,   4,   3,   6,   12,  7)

    MonsterBattlePostion("MonsterBattlePostion_964", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_968", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_96C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_970", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_974", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_978", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_97C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_980", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_9C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_9C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_9CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_9D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_9D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_9D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_9DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_9E0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_944", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_948", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_94C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_950", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_954", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_958", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_95C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_960", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_9E4", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_9E8", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_9EC", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_9F0", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_9F4", 14, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_9F8", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_9FC", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_A00", 0, 0, 180)

    # monster count: 14

    BattleInfo(
        "BattleInfo_C5C", 0x0000, 50, 6, 60, 8, 1, 30, 0, "br1000", "Sepith_98B9", 30, 40, 20, 10,
        (
            ("ms71500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71500.dat", "ms71500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71500.dat", "ms71900.dat", "ms71500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71500.dat", "ms71500.dat", "ms71900.dat", "ms71500.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_B94", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_98C1", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_D24", 0x0000, 50, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_9889", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_ACC", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_9881", 30, 40, 20, 10,
        (
            ("ms74800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms74800.dat", "ms74800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms74800.dat", "ms60900.dat", "ms74800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms74800.dat", "ms74800.dat", "ms60900.dat", "ms74800.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_A04", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_9879", 30, 40, 20, 10,
        (
            ("ms60900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60900.dat", "ms60900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60900.dat", "ms74800.dat", "ms60900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60900.dat", "ms60900.dat", "ms74800.dat", "ms60900.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_DEC", 0x0000, 84, 6, 60, 6, 1, 30, 0, "br1000", "Sepith_98D1", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_F10", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7451", "ed7453", "ATBonus_904"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E88", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7453", "ed7453", "ATBonus_904"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_ECC", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7453", "ed7453", "ATBonus_904"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_F54", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88702.dat", "ms88802.dat", "ms88802.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_9E4", "MonsterBattlePostion_9E4", "ed7454", "ed7453", "ATBonus_924"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch30000.itc",                   # 00
        "chr/ch34100.itc",                   # 01
        "chr/ch30000.itc",                   # 02
        "chr/ch31200.itc",                   # 03
        "chr/ch31300.itc",                   # 04
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
        "monster/ch60950.itc",               # 10
        "monster/ch60951.itc",               # 11
        "monster/ch74850.itc",               # 12
        "monster/ch74851.itc",               # 13
        "monster/ch71950.itc",               # 14
        "monster/ch71950.itc",               # 15
        "monster/ch71550.itc",               # 16
        "monster/ch71551.itc",               # 17
        "monster/ch63250.itc",               # 18
        "monster/ch63251.itc",               # 19
        "monster/ch60750.itc",               # 1A
        "monster/ch60750.itc",               # 1B
    ))

    DeclNpc(-44509,  0,       11819,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-50349,  0,       12060,   180,  389,  0x0, 0,   1,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-60919,  -8000,   69760,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-70860,  -8000,   60049,   315,  389,  0x0, 0,   2,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-71940,  -8000,   61029,   135,  389,  0x0, 0,   2,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-67889,  -8000,   74919,   135,  389,  0x0, 0,   3,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-71000,  -8000,   67230,   315,  389,  0x0, 0,   4,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-25579,  0,       -31940,  270,  485,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-83720,  -2000,   610,     270,  485,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-25579,  0,       -31940,  270,  485,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(-83720,  -2000,   610,     270,  485,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(14569,   500,     -37849,  0,    484,  0x0, 0,   16,  0,   0,   3,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(7550,    -1350,   0,       0x1010000,    "BattleInfo_C5C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-16750,  -19710,  0,       0x1010000,    "BattleInfo_B94", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(10290,   -43940,  0,       0x1010000,    "BattleInfo_D24", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-11230,  -38690,  0,       0x1010000,    "BattleInfo_ACC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-36240,  -37350,  -4000,   0x1010000,    "BattleInfo_A04", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-51390,  -4019,   0,       0x1010000,    "BattleInfo_B94", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-47140,  30310,   0,       0x1010000,    "BattleInfo_A04", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-67590,  39710,   -3000,   0x1010000,    "BattleInfo_ACC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-56290,  61040,   -8000,   0x1010000,    "BattleInfo_A04", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-66720,  72450,   -8000,   0x1010000,    "BattleInfo_ACC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-77240,  59790,   -8000,   0x1010000,    "BattleInfo_A04", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-81810,  -13080,  -2000,   0x1010000,    "BattleInfo_C5C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-2090,   -15170,  0,       0x1010000,    "BattleInfo_DEC", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-68650,  -2780,   -2000,   0x1010000,    "BattleInfo_DEC", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 28,  -44.0,                 0.0,                   -1.0,                  2500.0,                [0.14142131805419922,  0.035355351865291595,  -0.0,                  0.0,                   -0.14142140746116638,  0.035355329513549805,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.222537994384766,     1.5556354522705078,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 33,  -54.5,                 60.0,                  -9.0,                  900.0,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   10.90000057220459,     -5.0,                  1.8000000715255737,    1.0])
    DeclEvent(0x0040, 0, 25,  -0.8899999856948853,   -52.72999954223633,    -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   0.11124999821186066,   6.591249942779541,     0.25,                  1.0])
    DeclEvent(0x0000, 0, 26,  3.690000057220459,     25.489999771118164,    2.5,                   576.0,                 [0.04419415816664696,  0.23570235073566437,   -0.0,                  0.0,                   -0.044194187968969345, 0.23570218682289124,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.9634333848953247,    -6.877790451049805,    -0.5,                  1.0])
    DeclEvent(0x0000, 0, 61,  -64.08999633789062,    0.0,                   -3.0,                  1406.25,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666666269302368,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.817999839782715,    -0.0,                  0.6000000238418579,    1.0])

    DeclActor(-80920,  -8000,   60600,   1200,    -80920,  -7000,   60600,   0x007C, 0,  7,  0x0000)
    DeclActor(-72500,  -3000,   40000,   1200,    -72500,  -2000,   40000,   0x007C, 0,  8,  0x0000)
    DeclActor(-38100,  -4000,   -34860,  1200,    -38100,  -3000,   -34860,  0x007C, 0,  9,  0x0000)
    DeclActor(14570,   0,       -37850,  1200,    14570,   1000,    -37850,  0x007C, 0,  10, 0x0000)
    DeclActor(-25580,  0,       -31940,  1200,    -25580,  0,       -31940,  0x007C, 0,  11, 0x0000)
    DeclActor(-83720,  -2000,   610,     1200,    -83720,  -2000,   610,     0x007C, 0,  12, 0x0000)
    DeclActor(-42880,  10,      3570,    1200,    -42880,  2009,    3570,    0x007C, 0,  23, 0x0000)

    PlaceName(17.0, 0.0, 39.25, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-133.0, -2.0, 6.0, 0x0000, 0x0000, "贝尔加德门方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_1120",         # 00, 0
        "Function_1_11D0",         # 01, 1
        "Function_2_11ED",         # 02, 2
        "Function_3_120C",         # 03, 3
        "Function_4_122B",         # 04, 4
        "Function_5_1261",         # 05, 5
        "Function_6_13B8",         # 06, 6
        "Function_7_20FF",         # 07, 7
        "Function_8_223A",         # 08, 8
        "Function_9_2375",         # 09, 9
        "Function_10_24CE",        # 0A, 10
        "Function_11_26CC",        # 0B, 11
        "Function_12_29F6",        # 0C, 12
        "Function_13_2D20",        # 0D, 13
        "Function_14_2D39",        # 0E, 14
        "Function_15_2D3D",        # 0F, 15
        "Function_16_2F69",        # 10, 16
        "Function_17_317A",        # 11, 17
        "Function_18_31E9",        # 12, 18
        "Function_19_326F",        # 13, 19
        "Function_20_32C9",        # 14, 20
        "Function_21_332F",        # 15, 21
        "Function_22_350C",        # 16, 22
        "Function_23_3585",        # 17, 23
        "Function_24_38B2",        # 18, 24
        "Function_25_3946",        # 19, 25
        "Function_26_39C2",        # 1A, 26
        "Function_27_3BF0",        # 1B, 27
        "Function_28_3D64",        # 1C, 28
        "Function_29_4605",        # 1D, 29
        "Function_30_4D54",        # 1E, 30
        "Function_31_4DE4",        # 1F, 31
        "Function_32_4DFD",        # 20, 32
        "Function_33_556C",        # 21, 33
        "Function_34_628B",        # 22, 34
        "Function_35_635C",        # 23, 35
        "Function_36_649E",        # 24, 36
        "Function_37_7090",        # 25, 37
        "Function_38_70D6",        # 26, 38
        "Function_39_711C",        # 27, 39
        "Function_40_719A",        # 28, 40
        "Function_41_71FC",        # 29, 41
        "Function_42_7234",        # 2A, 42
        "Function_43_726C",        # 2B, 43
        "Function_44_72F4",        # 2C, 44
        "Function_45_732C",        # 2D, 45
        "Function_46_7368",        # 2E, 46
        "Function_47_73A4",        # 2F, 47
        "Function_48_73E0",        # 30, 48
        "Function_49_741A",        # 31, 49
        "Function_50_745C",        # 32, 50
        "Function_51_74AA",        # 33, 51
        "Function_52_9633",        # 34, 52
        "Function_53_964A",        # 35, 53
        "Function_54_9661",        # 36, 54
        "Function_55_9678",        # 37, 55
        "Function_56_968F",        # 38, 56
        "Function_57_96A9",        # 39, 57
        "Function_58_9709",        # 3A, 58
        "Function_59_9748",        # 3B, 59
        "Function_60_97A0",        # 3C, 60
        "Function_61_9802",        # 3D, 61
    ))


    def Function_0_1120(): pass

    label("Function_0_1120")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1158"),
        (1, "loc_1164"),
        (2, "loc_1170"),
        (3, "loc_117C"),
        (4, "loc_1188"),
        (5, "loc_1194"),
        (6, "loc_11A0"),
        (SWITCH_DEFAULT, "loc_11AC"),
    )


    label("loc_1158")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_1164")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_1170")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_117C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_1188")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_1194")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_11A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_11AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_11B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_11CF")

    Return()

    # Function_0_1120 end

    def Function_1_11D0(): pass

    label("Function_1_11D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11EC")
    OP_A1(0xFE, 0x1F4, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_11D0")

    label("loc_11EC")

    Return()

    # Function_1_11D0 end

    def Function_2_11ED(): pass

    label("Function_2_11ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_120B")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_11ED")

    label("loc_120B")

    Return()

    # Function_2_11ED end

    def Function_3_120C(): pass

    label("Function_3_120C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_122A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_3_120C")

    label("loc_122A")

    Return()

    # Function_3_120C end

    def Function_4_122B(): pass

    label("Function_4_122B")

    SetMapObjFlags(0x23, 0x2000000)
    SetMapObjFlags(0x24, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1260")
    ClearMapObjFlags(0x23, 0x2000000)
    ClearMapObjFlags(0x24, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)

    label("loc_1260")

    Return()

    # Function_4_122B end

    def Function_5_1261(): pass

    label("Function_5_1261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129C")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)

    label("loc_129C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_12DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B9")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)

    label("loc_12B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12DC")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_12DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_12F0")
    ClearScenarioFlags(0x22, 0)
    Event(0, 29)
    Jump("loc_1382")

    label("loc_12F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1304")
    ClearScenarioFlags(0x22, 1)
    Event(0, 32)
    Jump("loc_1382")

    label("loc_1304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1315")
    ClearScenarioFlags(0x22, 2)
    Jump("loc_1382")

    label("loc_1315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1326")
    ClearScenarioFlags(0x22, 3)
    Jump("loc_1382")

    label("loc_1326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1337")
    ClearScenarioFlags(0x22, 4)
    Jump("loc_1382")

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_134B")
    ClearScenarioFlags(0x22, 5)
    Event(0, 35)
    Jump("loc_1382")

    label("loc_134B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_135F")
    ClearScenarioFlags(0x22, 6)
    Event(0, 36)
    Jump("loc_1382")

    label("loc_135F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_1373")
    ClearScenarioFlags(0x23, 1)
    Event(0, 51)
    Jump("loc_1382")

    label("loc_1373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_1382")
    ClearScenarioFlags(0x23, 2)
    Event(0, 34)

    label("loc_1382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B4")
    SetChrPos(0x0, -43690, 10, 2760, 225)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 24)

    label("loc_13B4")

    Call(0, 13)
    Return()

    # Function_5_1261 end

    def Function_6_13B8(): pass

    label("Function_6_13B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_13CA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13F1")
    ModifyEventFlags(0, 2, 0x80)
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_145A")

    label("loc_13F1")

    OP_78(0x7, 0x23)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x23, 0x8)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x23, 0x1)
    SetChrPos(0x23, -890, 0, -52730, 0)
    OP_93(0x23, 0x0, 0x0)
    OP_52(0x23, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, -890, -1000, -52730, 3000, 3000, 90000)

    label("loc_145A")

    OP_52(0x26, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B8F")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1C47")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
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
    Jump("loc_1CC5")

    label("loc_1C47")

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

    label("loc_1CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D56")
    OP_11(0xAA, 0xC3, 0xFF, 0x0, 0x8C, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x258, 0x0, 0x20)
    OP_C3(0x0, 0x1, 0x3, 0x0, 0x0, 0x1, 7750, 1500, 27600, 2000, 2000, 0)
    OP_C3(0x1, 0x1, 0x3, 0x0, 0x0, 0x1, 5350, 1500, 30010, 2000, 2000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg2.eff")
    Jump("loc_1D5C")

    label("loc_1D56")

    SetMapObjFlags(0x8, 0x4)

    label("loc_1D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EC6")
    ClearChrFlags(0x13, 0x80)
    OP_78(0x22, 0x13)
    ClearMapObjFlags(0x22, 0x4)
    SetChrPos(0x13, -77790, -8000, 64980, 180)
    OP_D5(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFrame(0x22, "light", 0x0, 0x1)
    ClearChrFlags(0x15, 0x80)
    OP_78(0x26, 0x15)
    ClearMapObjFlags(0x26, 0x4)
    SetChrPos(0x15, -74280, -8000, 56340, 315)
    OP_D5(0x15, 0x0, 0x4CE78, 0x0, 0x0)
    SetMapObjFrame(0x26, "light", 0x0, 0x1)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x27, 0x16)
    ClearMapObjFlags(0x27, 0x4)
    SetChrPos(0x16, -56100, -8000, 69080, 251)
    OP_D5(0x16, 0x0, 0x3D478, 0x0, 0x0)
    SetMapObjFrame(0x27, "light", 0x0, 0x1)
    ClearChrFlags(0x14, 0x80)
    OP_78(0x21, 0x14)
    ClearMapObjFlags(0x21, 0x4)
    SetChrPos(0x14, -72640, -8000, 68520, 225)
    OP_D5(0x14, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFrame(0x21, "light", 0x0, 0x1)
    SetMapObjFrame(0x21, "mark01", 0x0, 0x1)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x25, 0x17)
    ClearMapObjFlags(0x25, 0x4)
    SetChrPos(0x17, -65900, -8000, 59320, 260)
    OP_D5(0x17, 0x0, 0x3F7A0, 0x0, 0x0)
    SetMapObjFrame(0x25, "light", 0x0, 0x1)
    SetMapObjFrame(0x25, "mark01", 0x0, 0x1)

    label("loc_1EC6")

    MiniGame(0x2F, 0x6, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFB")
    OP_70(0x0, 0x0)
    Jump("loc_1EFF")

    label("loc_1EFB")

    OP_70(0x0, 0x1E)

    label("loc_1EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F12")
    OP_70(0x1, 0x0)
    Jump("loc_1F16")

    label("loc_1F12")

    OP_70(0x1, 0x1E)

    label("loc_1F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F29")
    OP_70(0x2, 0x0)
    Jump("loc_1F2D")

    label("loc_1F29")

    OP_70(0x2, 0x1E)

    label("loc_1F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F40")
    OP_70(0x3, 0x0)
    Jump("loc_1F44")

    label("loc_1F40")

    OP_70(0x3, 0x1E)

    label("loc_1F44")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FA5")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -25580, 0, -31940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1FA5")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FF1")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -83720, -2000, 610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_1FF1")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2009")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_2009")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2021")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_2021")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_203E")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_203E")

    OP_10(0x2, 0x1)
    OP_10(0x3, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_END)), "loc_2053")
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x1)

    label("loc_2053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2066")
    OP_1B(0x2, 0x0, 0x16)

    label("loc_2066")

    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_207E")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_207E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_209D")
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    Jump("loc_20C3")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_END)), "loc_20B7")
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    Jump("loc_20C3")

    label("loc_20B7")

    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)

    label("loc_20C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20DD")
    ClearMapObjFlags(0x28, 0x4)
    ClearMapObjFlags(0x29, 0x4)

    label("loc_20DD")

    OP_1C(0x0, 0x1E, 0x0, 0x32, 0x0, 0xE, 0x0, 0x0)
    OP_1C(0x0, 0x1F, 0x0, 0x32, 0x0, 0xE, 0x0, 0x0)
    OP_1C(0x0, 0x20, 0x0, 0x32, 0x0, 0xE, 0x0, 0x0)
    Return()

    # Function_6_13B8 end

    def Function_7_20FF(): pass

    label("Function_7_20FF")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F1")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('钢手镯', 1)"), scpexpr(EXPR_END)), "loc_2182")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x44),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_21EC")

    label("loc_2182")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x44),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x44),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_21EC")

    Jump("loc_222E")

    label("loc_21F1")

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

    label("loc_222E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_20FF end

    def Function_8_223A(): pass

    label("Function_8_223A")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_232C")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅰ', 1)"), scpexpr(EXPR_END)), "loc_22BD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
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
    SetScenarioFlags(0x1E2, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_2327")

    label("loc_22BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2327")

    Jump("loc_2369")

    label("loc_232C")

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

    label("loc_2369")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_223A end

    def Function_9_2375(): pass

    label("Function_9_2375")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249F")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x2, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 40)
    AddSepith(0x1, 40)
    AddSepith(0x2, 40)
    AddSepith(0x3, 40)
    AddSepith(0x4, 40)
    AddSepith(0x5, 40)
    AddSepith(0x6, 40)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×４０\x01\x07\x02",

            "#57I水之耀晶片×４０\x01\x07\x02",

            "#58I火之耀晶片×４０\x01\x07\x02",

            "#59I风之耀晶片×４０\x01\x07\x02",

            "#60I时之耀晶片×４０\x01\x07\x02",

            "#61I空之耀晶片×４０\x01\x07\x02",

            "#62I幻之耀晶片×４０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E2, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_24BC")

    label("loc_249F")


    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_24BC")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_2375 end

    def Function_10_24CE(): pass

    label("Function_10_24CE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268E")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25CB")
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x22, 0x0, 0)
    OP_98(0x22, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_252B():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_252B)

    def lambda_2545():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_2545)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x22, 1)
    Battle("BattleInfo_F10", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x22, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_25AC"),
        (2, "loc_25BB"),
        (1, "loc_25C8"),
        (SWITCH_DEFAULT, "loc_25CB"),
    )


    label("loc_25AC")

    SetScenarioFlags(0x216, 1)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_25CB")

    label("loc_25BB")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_25C8")

    OP_B9(0x0)
    Return()

    label("loc_25CB")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ１', 1)"), scpexpr(EXPR_END)), "loc_2622")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_2689")

    label("loc_2622")

    FadeToDark(300, 0, 100)

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2689")

    Jump("loc_26C0")

    label("loc_268E")

    FadeToDark(300, 0, 100)

    #A0012
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

    label("loc_26C0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_24CE end

    def Function_11_26CC(): pass

    label("Function_11_26CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_286A")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_284B")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0013
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2846")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_2843")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_276E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_276E)
    TurnDirection(0x1E, 0x0, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    PlayEffect(0x7, 0x1, 0x1E, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0014
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
    Battle("BattleInfo_E88", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1E, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283E")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2825")
    Call(1, 5)
    Jump("loc_283E")

    label("loc_2825")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_283B")
    Call(1, 4)
    Jump("loc_283E")

    label("loc_283B")

    Call(1, 3)

    label("loc_283E")

    Jump("loc_2846")

    label("loc_2843")

    Call(1, 1)

    label("loc_2846")

    Jump("loc_2861")

    label("loc_284B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_2861")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2861")

    TalkEnd(0xFF)
    Return()

    label("loc_286A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_29DB")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0015
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29D6")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_29D3")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_28FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_28FE)
    TurnDirection(0x20, 0x0, 0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    PlayEffect(0x7, 0x1, 0x20, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0016
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
    Battle("BattleInfo_ECC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x20, 0x80)
    ClearChrFlags(0x20, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29CE")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_29B5")
    Call(1, 5)
    Jump("loc_29CE")

    label("loc_29B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_29CB")
    Call(1, 4)
    Jump("loc_29CE")

    label("loc_29CB")

    Call(1, 3)

    label("loc_29CE")

    Jump("loc_29D6")

    label("loc_29D3")

    Call(1, 1)

    label("loc_29D6")

    Jump("loc_29F1")

    label("loc_29DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_29F1")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_29F1")

    TalkEnd(0xFF)
    Return()

    # Function_11_26CC end

    def Function_12_29F6(): pass

    label("Function_12_29F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B94")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_END)), "loc_2B75")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0017
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B70")
    ClearScenarioFlags(0x3A, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2B6D")
    ClearScenarioFlags(0x38, 3)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2A98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_2A98)
    TurnDirection(0x1F, 0x0, 0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    PlayEffect(0x7, 0x1, 0x1F, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0018
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
    Battle("BattleInfo_E88", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1F, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B68")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B4F")
    Call(1, 5)
    Jump("loc_2B68")

    label("loc_2B4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B65")
    Call(1, 4)
    Jump("loc_2B68")

    label("loc_2B65")

    Call(1, 3)

    label("loc_2B68")

    Jump("loc_2B70")

    label("loc_2B6D")

    Call(1, 1)

    label("loc_2B70")

    Jump("loc_2B8B")

    label("loc_2B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2B8B")
    ClearScenarioFlags(0x38, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2B8B")

    TalkEnd(0xFF)
    Return()

    label("loc_2B94")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_END)), "loc_2D05")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0019
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D00")
    ClearScenarioFlags(0x3A, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2CFD")
    ClearScenarioFlags(0x38, 3)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2C28():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_2C28)
    TurnDirection(0x21, 0x0, 0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    PlayEffect(0x7, 0x1, 0x21, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0020
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
    Battle("BattleInfo_ECC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x21, 0x80)
    ClearChrFlags(0x21, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF8")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2CDF")
    Call(1, 5)
    Jump("loc_2CF8")

    label("loc_2CDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2CF5")
    Call(1, 4)
    Jump("loc_2CF8")

    label("loc_2CF5")

    Call(1, 3)

    label("loc_2CF8")

    Jump("loc_2D00")

    label("loc_2CFD")

    Call(1, 1)

    label("loc_2D00")

    Jump("loc_2D1B")

    label("loc_2D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2D1B")
    ClearScenarioFlags(0x38, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2D1B")

    TalkEnd(0xFF)
    Return()

    # Function_12_29F6 end

    def Function_13_2D20(): pass

    label("Function_13_2D20")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D38")
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)

    label("loc_2D38")

    Return()

    # Function_13_2D20 end

    def Function_14_2D39(): pass

    label("Function_14_2D39")

    Call(1, 6)
    Return()

    # Function_14_2D39 end

    def Function_15_2D3D(): pass

    label("Function_15_2D3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_2E6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E29")

    #C0021
    ChrTalk(
        0xFE,
        (
            "刚、刚才那诡异的\x01",
            "声音是怎么回事！？\x02\x03",

            "简直就像来自地狱的\x01",
            "吼叫一样……！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00003F你冷静点，弗兰茨。\x02\x03",

            "#00001F我们这就去调查，\x01",
            "这里的警备就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "好、好的……我明白了。\x01",
            "罗伊德，你可要小心啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E69")

    label("loc_2E29")


    #C0024
    ChrTalk(
        0xFE,
        (
            "刚、刚才那诡异的\x01",
            "声音是怎么回事！？\x02\x03",

            "你们可要\x01",
            "多加注意啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E69")

    Jump("loc_2F65")

    label("loc_2E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_2F65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F17")

    #C0025
    ChrTalk(
        0xFE,
        (
            "听说那辆事故列车\x01",
            "脱轨得十分夸张。\x02\x03",

            "没有出现遇难者，算是万幸，\x01",
            "但脱轨成那样，估计要花\x01",
            "很长时间来修复。\x02\x03",

            "如果你们要去调查，\x01",
            "可要好好加油。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F65")

    label("loc_2F17")


    #C0026
    ChrTalk(
        0xFE,
        (
            "听说那辆事故列车的\x01",
            "脱轨情况十分夸张。\x02\x03",

            "如果你们要去调查，\x01",
            "可要好好加油。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F65")

    TalkEnd(0xFE)
    Return()

    # Function_15_2D3D end

    def Function_16_2F69(): pass

    label("Function_16_2F69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_30A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302B")

    #C0027
    ChrTalk(
        0xFE,
        (
            "兰迪前辈、诺艾尔上士，\x01",
            "刚、刚才那声吼叫究竟是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#00301F目前还不清楚……\x01",
            "看来还是小心行事为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        "#10101F警备工作就麻烦你了！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "好的，我明白了！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_309F")

    label("loc_302B")


    #C0031
    ChrTalk(
        0xFE,
        (
            "不管刚才那声吼叫到底是怎么回事，\x01",
            "也绝不能让它干扰到这个\x01",
            "正在火速抢修的工作现场。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "这里的警备就交给我们吧！\x02",
    )

    CloseMessageWindow()

    label("loc_309F")

    Jump("loc_3176")

    label("loc_30A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_3176")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312D")

    #C0033
    ChrTalk(
        0xFE,
        (
            "从这里下去，就能\x01",
            "抵达列车事故现场。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "索妮亚司令等人与警方\x01",
            "已经开始取证了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "各位也请前往现场吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3176")

    label("loc_312D")


    #C0036
    ChrTalk(
        0xFE,
        (
            "索妮亚司令等人与警方\x01",
            "都已开始取证。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "各位也请到现场开展调查吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3176")

    TalkEnd(0xFE)
    Return()

    # Function_16_2F69 end

    def Function_17_317A(): pass

    label("Function_17_317A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_31E5")

    #C0038
    ChrTalk(
        0xFE,
        (
            "希望刚才跑进现场的\x01",
            "新闻记者别干扰到\x01",
            "抢修工作的进度。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "算了，她应该也\x01",
            "明白现在的状况。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E5")

    TalkEnd(0xFE)
    Return()

    # Function_17_317A end

    def Function_18_31E9(): pass

    label("Function_18_31E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_326B")

    #C0040
    ChrTalk(
        0xFE,
        (
            "居然能和警备队\x01",
            "协力工作，\x01",
            "这可是相当罕见的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "事故现场触目惊心……\x01",
            "我们警察一定要全力做好\x01",
            "自己能做到的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326B")

    TalkEnd(0xFE)
    Return()

    # Function_18_31E9 end

    def Function_19_326F(): pass

    label("Function_19_326F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_32C5")

    #C0042
    ChrTalk(
        0xFE,
        (
            "警方派搜查二科来\x01",
            "调查事故原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "但目前尚未得出\x01",
            "任何明确的结论。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C5")

    TalkEnd(0xFE)
    Return()

    # Function_19_326F end

    def Function_20_32C9(): pass

    label("Function_20_32C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_332B")

    #C0044
    ChrTalk(
        0xFE,
        (
            "索妮亚司令正在现场\x01",
            "指挥修复工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "如果你们想参加调查，\x01",
            "最好先跟她打声招呼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_332B")

    TalkEnd(0xFE)
    Return()

    # Function_20_32C9 end

    def Function_21_332F(): pass

    label("Function_21_332F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_34AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_340F")

    #C0046
    ChrTalk(
        0xFE,
        (
            "这边是西克洛斯贝尔街道……\x01",
            "刚才听到了一声\x01",
            "诡异的吼叫。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "遵照索妮亚司令的指示，\x01",
            "我们将优先修复铁道。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "不过，首先要尽快把\x01",
            "起重设备运到这里来。\x01",
            "我再重复一遍，要尽快把起重装备……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_34A9")

    label("loc_340F")


    #C0049
    ChrTalk(
        0xFE,
        (
            "那边的问题就交给你们了。\x01",
            "我们将和索妮亚司令一起，\x01",
            "优先进行铁道修复。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "如果我们能迅速完成手头的工作，\x01",
            "就会赶去支援你们。\x01",
            "在那之前，就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A9")

    Jump("loc_3508")

    label("loc_34AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_3508")

    #C0051
    ChrTalk(
        0xFE,
        (
            "在边境持续紧张的状态下，\x01",
            "发生了如此重大的事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "……这真的只是偶然吗？\x02",
    )

    CloseMessageWindow()

    label("loc_3508")

    TalkEnd(0xFE)
    Return()

    # Function_21_332F end

    def Function_22_350C(): pass

    label("Function_22_350C")

    EventBegin(0x1)

    #C0053
    ChrTalk(
        0x101,
        (
            "#00003F修复铁道的工作就交给\x01",
            "索妮亚司令他们吧。\x02\x03",

            "#00001F我们要去确认那声\x01",
            "神秘咆哮的真正来源！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -64870, -8000, 77770, 180)
    EventEnd(0x4)
    Return()

    # Function_22_350C end

    def Function_23_3585(): pass

    label("Function_23_3585")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35B7")
    SetScenarioFlags(0x31, 2)

    label("loc_35B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_35F7")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35EC")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_35F2")

    label("loc_35EC")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_35F2")

    Jump("loc_35FD")

    label("loc_35F7")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_35FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_366E")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_364E"),
        (SWITCH_DEFAULT, "loc_365F"),
    )


    label("loc_364E")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3669")

    label("loc_365F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3669")

    Jump("loc_389F")

    label("loc_366E")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_369E")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_369E")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_36C8"),
        (1, "loc_37CC"),
        (2, "loc_385D"),
        (SWITCH_DEFAULT, "loc_3895"),
    )


    label("loc_36C8")

    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36F9")
    OP_70(0x4, 0x12C)
    OP_71(0x4, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_3709")

    label("loc_36F9")

    OP_70(0x4, 0xF0)
    OP_71(0x4, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_3709")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_375F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_375F")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3782")
    Sound(461, 0, 100, 0)

    label("loc_3782")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37A2")
    OP_70(0x4, 0x14A)
    OP_71(0x4, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_37B2")

    label("loc_37A2")

    OP_70(0x4, 0x10E)
    OP_71(0x4, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_37B2")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x4, "light", 0x1, 0x1)
    OP_70(0x4, 0x0)
    Jump("loc_35FD")

    label("loc_37CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_383E")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_3801")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_3819")

    label("loc_3801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3814")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_3819")

    label("loc_3814")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_3819")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3858")

    label("loc_383E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_384E")
    OP_AF(0xFB)
    Jump("loc_3858")

    label("loc_384E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3858")

    Jump("loc_389F")

    label("loc_385D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3876")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3890")

    label("loc_3876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3886")
    OP_AF(0xFB)
    Jump("loc_3890")

    label("loc_3886")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3890")

    Jump("loc_389F")

    label("loc_3895")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_389F")

    Jump("loc_35FD")

    label("loc_38A4")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_23_3585 end

    def Function_24_38B2(): pass

    label("Function_24_38B2")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_390D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3902")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_3908")

    label("loc_3902")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_3908")

    Jump("loc_3931")

    label("loc_390D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_392B")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_3931")

    label("loc_392B")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_3931")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_24_38B2 end

    def Function_25_3946(): pass

    label("Function_25_3946")

    Battle("BattleInfo_F54", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_398D")
    OP_90(0x0, -7830, 0, -50540, 270)
    EventEnd(0x5)
    SetChrFlags(0x23, 0x8000)
    Jump("loc_39C1")

    label("loc_398D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A0")
    Jump("loc_39C1")

    label("loc_39A0")

    ModifyEventFlags(0, 2, 0x80)
    SetMapObjFlags(0x7, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 1)
    EventEnd(0x5)

    label("loc_39C1")

    Return()

    # Function_25_3946 end

    def Function_26_39C2(): pass

    label("Function_26_39C2")

    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(1860, 9890, 23710, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1680, 2500, 23480, 45)
    SetChrPos(0x103, 2120, 2500, 22540, 45)
    SetChrPos(0x104, 610, 2500, 23840, 45)
    SetChrPos(0x105, 310, 2500, 22140, 45)
    SetChrPos(0x106, -430, 2500, 23430, 45)
    SetChrPos(0x107, 1310, 2490, 21170, 45)
    SetChrSubChip(0x107, 0x5)
    OP_68(1860, 3290, 23710, 4500)
    MoveCamera(45, 23, 0, 4500)
    OP_6E(510, 4500)
    SetCameraDistance(20000, 4500)
    OP_6F(0x79)

    #C0054
    ChrTalk(
        0x101,
        "#00001F笼罩克洛斯贝尔市的『结界』吗……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#00206F唯独这个问题，\x01",
            "目前还是束手无策啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#10400F#6P嗯，现在尚未找到\x01",
            "穿过结界的方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#00301F我们还是去\x01",
            "寻找其它路线为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x106,
        (
            "#10703F#6P而且这里应该是\x01",
            "国防军的巡逻区域……\x01",
            "我们不宜久留。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        "#00003F嗯，是啊……\x02",
    )

    CloseMessageWindow()
    Call(0, 27)
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 2070, 2500, 23540, 225)
    SetScenarioFlags(0x1BD, 0)
    ModifyEventFlags(0, 3, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_26_39C2 end

    def Function_27_3BF0(): pass

    label("Function_27_3BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D63")
    OP_29(0xAF, 0x1, 0xF)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)
    Sleep(500)

    #C0060
    ChrTalk(
        0x101,
        (
            "#00008F话说回来，我们已经到处转过一圈了，\x01",
            "但似乎没有一条路能走得通。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#00306F克洛斯贝尔市自不必说，\x01",
            "贝尔加德门和警察学校\x01",
            "也都不能去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x106,
        "#10706F#6P真是难办啊……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        (
            "#10400F#6P唔，难道就没有其它的\x01",
            "可去之处了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x107,
        (
            "#01200F#3C#12P不如去主路之外的\x01",
            "角落探查一番吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#00203F说的也是……\x01",
            "咱们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D63")

    Return()

    # Function_27_3BF0 end

    def Function_28_3D64(): pass

    label("Function_28_3D64")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -38880, 0, -3420, 315)
    SetChrPos(0x102, -37220, 0, -2870, 315)
    SetChrPos(0x103, -37980, 0, -5050, 315)
    SetChrPos(0x104, -37250, 0, -4040, 315)
    SetChrPos(0x109, -35720, 0, -4900, 315)
    SetChrPos(0x105, -36260, 0, -6090, 315)
    OP_68(-40900, 1200, -650, 0)
    MoveCamera(90, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17500, 2000)

    def lambda_3E4D():
        OP_95(0xFE, -40880, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E4D)
    Sleep(30)

    def lambda_3E6A():
        OP_95(0xFE, -39220, 0, -870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E6A)
    Sleep(30)

    def lambda_3E87():
        OP_95(0xFE, -39980, 0, -3050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E87)
    Sleep(30)

    def lambda_3EA4():
        OP_95(0xFE, -39250, 0, -2040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3EA4)
    Sleep(30)

    def lambda_3EC1():
        OP_95(0xFE, -37720, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3EC1)
    Sleep(30)

    def lambda_3EDE():
        OP_95(0xFE, -38260, 0, -4090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3EDE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-47350, 600, 11150, 4000)
    MoveCamera(45, 23, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(23500, 4000)
    OP_6F(0x79)

    #C0066
    ChrTalk(
        0x101,
        "#00001F#12P#N那是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0067
    ChrTalk(
        0x105,
        (
            "#10300F#12P#N看来那里就是\x01",
            "事故现场了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-47400, 800, 10050, 5000)
    MoveCamera(45, 20, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(18950, 5000)
    SetChrPos(0x101, -41650, 0, 3020, 315)
    SetChrPos(0x102, -41010, 0, 1770, 315)
    SetChrPos(0x103, -42180, 0, 1820, 315)
    SetChrPos(0x104, -40030, 0, 660, 315)
    SetChrPos(0x109, -41520, 0, 250, 315)
    SetChrPos(0x105, -42770, 0, 320, 315)

    def lambda_4094():
        OP_95(0xFE, -47650, 0, 9020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4094)
    Sleep(30)

    def lambda_40B1():
        OP_95(0xFE, -47010, 0, 7770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40B1)
    Sleep(30)

    def lambda_40CE():
        OP_95(0xFE, -48180, 0, 7820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_40CE)
    Sleep(30)

    def lambda_40EB():
        OP_95(0xFE, -46030, 0, 6660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_40EB)
    Sleep(30)

    def lambda_4108():
        OP_95(0xFE, -47520, 0, 6250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4108)
    Sleep(30)

    def lambda_4125():
        OP_95(0xFE, -48770, 0, 6320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4125)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_416C():

        label("loc_416C")

        TurnDirection(0x8, 0x101, 500)
        Yield()
        Jump("loc_416C")

    QueueWorkItem2(0x8, 2, lambda_416C)

    def lambda_417E():

        label("loc_417E")

        TurnDirection(0x9, 0x101, 500)
        Yield()
        Jump("loc_417E")

    QueueWorkItem2(0x9, 2, lambda_417E)
    WaitChrThread(0x101, 1)

    def lambda_4194():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4194)
    WaitChrThread(0x102, 1)

    def lambda_41A5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_41A5)
    WaitChrThread(0x103, 1)

    def lambda_41B6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_41B6)
    WaitChrThread(0x104, 1)

    def lambda_41C7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_41C7)
    WaitChrThread(0x109, 1)

    def lambda_41D8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_41D8)
    WaitChrThread(0x105, 1)

    def lambda_41E9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_41E9)
    WaitChrThread(0x101, 2)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    #C0068
    ChrTalk(
        0x8,
        "#5P哟，罗伊德，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#00000F#12P弗兰茨，辛苦你了。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "#5P兰迪前辈、诺艾尔上士，\x01",
            "各位也辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x109,
        "#10100F#12P你也辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        (
            "#00301F#12P看来前方就是\x01",
            "事故现场了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "#5P是的，索妮亚司令与警方\x01",
            "正在取证。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "#5P二科的多诺邦警督和\x01",
            "雷蒙德搜查官已经到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "#5P不过，听说列车\x01",
            "脱轨得十分夸张。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "#5P要想完全修复，\x01",
            "可得花些时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#00108F#12P请问……\x01",
            "乘客们的情况如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#5P所幸无人遇难，\x01",
            "但有数名乘客受了重伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "#5P急需治疗的伤员刚刚已被\x01",
            "抬上急救车，送往医院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#00006F#12P我们刚才也看见急救车了。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        "#00208F#12P给其他乘客安排了巴士吗？\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "#5P是的，分为两条路线，\x01",
            "一条前往克洛斯贝尔市，\x01",
            "另一条前往阿尔泰尔市。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        "#5P刚才的场面可真是相当混乱啊。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        "#00206F#12P……这是必然的。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x105,
        (
            "#10306F#12P哎呀呀……\x01",
            "真是一起棘手的事故啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00003F#12P总之，我们也去勘察\x01",
            "一下事故现场吧。\x02\x03",

            "#00000F可以让我们进去吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "#5P当然，让你们进去，\x01",
            "谁都不会有意见的。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        "#5P各位请吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -47350, 0, 9050, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, -44510, 0, 11820, 180)
    SetChrPos(0x9, -50350, 0, 12060, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x163, 0)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_28_3D64 end

    def Function_29_4605(): pass

    label("Function_29_4605")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -45010, 0, 2540, 315)
    SetChrPos(0x102, -44060, 0, 3260, 315)
    SetChrPos(0x103, -45070, 0, 1560, 315)
    SetChrPos(0x104, -43100, 0, 2350, 315)
    SetChrPos(0x109, -43180, 0, 1320, 315)
    SetChrPos(0x105, -44250, 0, 510, 315)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x11, 0x80)
    OP_78(0x4, 0x11)
    OP_49()
    SetChrPos(0x11, -28900, 0, -19150, 315)
    OP_D5(0x11, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x1, 0x20)
    VolumeBGM(0x64, 0x3E8)
    FadeToBright(1000, 0)
    OP_68(-38050, 2100, -2550, 0)
    MoveCamera(114, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(30200, 0)
    OP_68(-41150, 1100, 3800, 8000)
    MoveCamera(84, 20, 0, 8000)
    SetCameraDistance(19700, 8000)
    BeginChrThread(0x11, 3, 0, 30)
    BeginChrThread(0x24, 1, 0, 31)
    WaitChrThread(0x11, 3)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Sound(462, 0, 100, 0)
    OP_71(0x4, 0x12D, 0x14A, 0x1, 0x8)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x11, -41260, 0, 4180, 315)
    OP_D5(0x11, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x1000)
    OP_70(0x4, 0x78)
    SetChrFlags(0x11, 0x80)
    OP_68(-44400, 1300, 2600, 0)
    MoveCamera(80, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17200, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17000, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x8, -46510, 0, 9480, 180)
    SetChrPos(0x9, -48380, 0, 8780, 180)
    OP_68(-45400, 1300, 3600, 3000)

    def lambda_48E3():
        OP_95(0xFE, -45600, 0, 4870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_48E3)

    def lambda_48FD():
        OP_95(0xFE, -46440, 0, 4150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_48FD)
    WaitChrThread(0x8, 1)

    def lambda_491B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_491B)
    WaitChrThread(0x9, 1)

    def lambda_492C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_492C)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)

    #C0089
    ChrTalk(
        0x8,
        "#5P哟，罗伊德，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#00000F#11P弗兰茨，你辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "#6P兰迪前辈、诺艾尔上士，\x01",
            "你们也辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        "#10100F#11P你也辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x104,
        (
            "#00301F#11P看来前方就是\x01",
            "事故现场了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "#6P是的，索妮亚司令与警方\x01",
            "正在取证。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "#5P二科的多诺邦警督和\x01",
            "雷蒙德搜查官已经到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "#5P不过，听说列车\x01",
            "脱轨得十分夸张。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "#5P要想完全修复，\x01",
            "可得花些时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00108F#11P请问……\x01",
            "乘客们的情况如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "#6P所幸无人遇难，\x01",
            "但有数名乘客受了重伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "#6P急需治疗的伤员刚刚已被\x01",
            "抬上急救车，送往医院去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#00006F#11P我们刚才也看见急救车了。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        "#00208F#11P给其他乘客安排了巴士吗？\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#5P是的，分为两条路线，\x01",
            "一条前往克洛斯贝尔市，\x01",
            "另一条前往阿尔泰尔市。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        "#5P刚才的场面可真是相当混乱啊。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x103,
        "#00206F#11P……这是必然的。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x105,
        (
            "#10306F#11P哎呀呀……\x01",
            "真是一起棘手的事故啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00003F#11P总之，我们也去勘察\x01",
            "一下事故现场吧。\x02\x03",

            "#00000F可以让我们进去吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "#5P当然，让你们进去，\x01",
            "谁都不会有意见的。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        "#6P各位请吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -47350, 0, 9050, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, -44510, 0, 11820, 180)
    SetChrPos(0x9, -50350, 0, 12060, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x163, 0)
    ModifyEventFlags(0, 0, 0x80)
    ClearMapFlags(0x8000000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_29_4605 end

    def Function_30_4D54(): pass

    label("Function_30_4D54")

    SetChrPos(0xFE, -28900, 0, -19150, 315)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -32900, 0, -12300)
    OP_9F(0x1, -33800, 0, -5850)
    OP_9F(0x1, -34550, 0, -1950)
    OP_9F(0x1, -39400, 0, 3050)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xBB8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_71(0x4, 0x5B, 0x78, 0x1, 0x8)
    Return()

    # Function_30_4D54 end

    def Function_31_4DE4(): pass

    label("Function_31_4DE4")

    Sound(458, 0, 100, 0)
    Sleep(3000)
    Sound(459, 0, 100, 0)
    Sleep(3000)
    Sound(492, 0, 70, 0)
    Return()

    # Function_31_4DE4 end

    def Function_32_4DFD(): pass

    label("Function_32_4DFD")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("chr/ch28100.itc", 0x1F)
    OP_68(-63850, -5700, 68650, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x101, -64849, -8000, 71050, 180)
    SetChrPos(0x102, -65200, -8000, 73050, 180)
    SetChrPos(0x103, -63350, -8000, 71700, 180)
    SetChrPos(0x104, -62850, -8000, 73020, 180)
    SetChrPos(0x109, -64450, -8000, 72300, 180)
    SetChrPos(0x105, -63850, -8000, 73650, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -64569, -8000, 76920, 180)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -63420, -8000, 77430, 180)
    SetMapObjFlags(0x21, 0x1000)

    def lambda_4F1A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F1A)
    Sleep(50)

    def lambda_4F32():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4F32)

    def lambda_4F47():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F47)
    Sleep(50)

    def lambda_4F5F():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F5F)

    def lambda_4F74():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F74)
    Sleep(50)

    def lambda_4F8C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F8C)

    def lambda_4FA1():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4FA1)
    Sleep(50)
    FadeToBright(1000, 0)
    OP_68(-63640, -7200, 68080, 3500)

    def lambda_4FD3():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4FD3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    def lambda_5000():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5000)
    Sleep(50)

    def lambda_5010():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5010)
    Sleep(50)

    def lambda_5020():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5020)
    Sleep(50)

    def lambda_5030():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5030)
    Sleep(50)

    def lambda_5040():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5040)
    Sleep(50)

    def lambda_5050():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5050)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)
    OP_0D()

    #C0110
    ChrTalk(
        0x101,
        "#00006F#12P格蕾丝小姐……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#00101F#6P您该不会是想\x01",
            "跟我们一起去吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xF,
        (
            "#02106F#5P嗯～其实我本想\x01",
            "说『正是如此』。\x02\x03",

            "#02100F可这次好像真的挺危险，\x01",
            "我只好忍耐一下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x10,
        (
            "#5P我们打算先回克洛斯贝尔市，\x01",
            "整理出一份速报。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x10,
        (
            "#5P等其他记者到齐后，\x01",
            "马上就会继续进行取材。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        "#00200F#12P这样最好。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x104,
        (
            "#00303F#12P是啊，不然万一遭到了袭击，\x01",
            "我们可抽不出手来保护你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xF,
        (
            "#02103F#5P目前还不知道是个什么样的魔兽，\x01",
            "但如果真的是它使列车脱轨，\x01",
            "那一定会是非同寻常的对手……\x02\x03",

            "#02101F你们可要多加小心！\x01",
            "事后记得要给我提供情报哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#00000F#12P明白了！\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x109,
        "#10100F#12P您辛苦了！\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x87, 0x1F4)
    OP_68(-61720, -7200, 67040, 4000)
    MoveCamera(54, 18, 0, 4000)
    OP_6E(510, 4000)

    def lambda_52F0():

        label("loc_52F0")

        TurnDirection(0xFE, 0xF, 150)
        Yield()
        Jump("loc_52F0")

    QueueWorkItem2(0x101, 2, lambda_52F0)

    def lambda_5302():

        label("loc_5302")

        TurnDirection(0xFE, 0xF, 100)
        Yield()
        Jump("loc_5302")

    QueueWorkItem2(0x102, 2, lambda_5302)

    def lambda_5314():

        label("loc_5314")

        TurnDirection(0xFE, 0xF, 200)
        Yield()
        Jump("loc_5314")

    QueueWorkItem2(0x103, 2, lambda_5314)

    def lambda_5326():

        label("loc_5326")

        TurnDirection(0xFE, 0xF, 150)
        Yield()
        Jump("loc_5326")

    QueueWorkItem2(0x104, 2, lambda_5326)

    def lambda_5338():

        label("loc_5338")

        TurnDirection(0xFE, 0xF, 100)
        Yield()
        Jump("loc_5338")

    QueueWorkItem2(0x109, 2, lambda_5338)

    def lambda_534A():

        label("loc_534A")

        TurnDirection(0xFE, 0xF, 200)
        Yield()
        Jump("loc_534A")

    QueueWorkItem2(0x105, 2, lambda_534A)

    def lambda_535C():
        OP_95(0xFE, -55190, -8000, 61950, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_535C)
    Sleep(800)
    OP_93(0x10, 0x87, 0x1F4)

    def lambda_5380():
        OP_95(0xFE, -54530, -8000, 62580, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5380)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)
    Sleep(500)
    OP_68(-63110, -7200, 66900, 1000)
    MoveCamera(54, 18, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(18000, 1000)

    def lambda_53F7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_53F7)

    def lambda_5404():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5404)
    Sleep(50)

    def lambda_5414():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5414)
    Sleep(50)

    def lambda_5424():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5424)
    Sleep(50)

    def lambda_5434():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5434)
    Sleep(50)

    def lambda_5444():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5444)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 2)
    OP_6F(0x79)

    #C0120
    ChrTalk(
        0x101,
        (
            "#00003F#12P好了，我们开始追踪吧。\x02\x03",

            "#00013F首先沿着道路\x01",
            "前往正西方向。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x105,
        "#10301F#5P明白。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x104,
        "#00307F#5P无论如何也要把它抓住！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, -65000, -8000, 65000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapObjFlags(0x21, 0x1000)
    SetScenarioFlags(0x163, 2)
    OP_29(0xA8, 0x1, 0x6)
    ModifyEventFlags(0, 4, 0x80)
    OP_C9(0x0, 0x200000)
    OP_1B(0x2, 0x0, 0x16)
    OP_E2(0x2)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    EventEnd(0x5)
    Return()

    # Function_32_4DFD end

    def Function_33_556C(): pass

    label("Function_33_556C")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -57760, -8000, 63610, 0)
    SetChrPos(0x106, -57240, -8000, 62560, 0)
    SetChrPos(0x103, -58560, -8000, 62060, 0)
    SetChrPos(0x104, -57710, -8000, 61210, 0)
    SetChrPos(0x107, -56060, -8000, 61660, 0)
    SetChrPos(0x105, -59860, -8000, 61460, 0)
    OP_68(-57500, -7100, 65300, 0)
    MoveCamera(25, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22500, 0)

    def lambda_563B():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_563B)
    Sleep(50)

    def lambda_5653():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5653)
    Sleep(50)

    def lambda_566B():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_566B)
    Sleep(50)

    def lambda_5683():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5683)
    Sleep(50)

    def lambda_569B():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_569B)
    Sleep(50)

    def lambda_56B3():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_56B3)
    FadeToBright(1000, 0)
    OP_68(-60310, -7100, 69090, 4000)
    SetCameraDistance(24500, 4000)
    MoveCamera(25, 18, 0, 4000)
    Sleep(3500)
    Fade(1000)
    OP_68(-64099, -5100, 77200, 0)
    OP_68(-64099, -7100, 77200, 3500)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x107, 1)
    SetChrSubChip(0x107, 0x5)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_0D()

    #C0123
    ChrTalk(
        0x103,
        (
            "#00205F#6P对了，发生脱轨的那辆列车\x01",
            "已经被运走了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#00000F#11P是啊，就连碎片之类的东西\x01",
            "都清理干净了。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        (
            "#00306F#12P话说回来，那起事故\x01",
            "明明是一起重大事件……\x02\x03",

            "#00301F但最近发生了太多的惊人事件，\x01",
            "相比之下，脱轨事故都没给我留下多少印象呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x105,
        "#10403F#6P……确实如此。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x106,
        (
            "#10703F#12P铁道列车如今已经\x01",
            "完全停运了。\x02\x03",

            "#10708F只有国防军的货运列车会\x01",
            "偶尔从这里通过……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        "#00301F#12P是这样啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0129
    ChrTalk(
        0x101,
        (
            "#00005F#5P……等等。\x02\x03",

            "#00013F如此说来，不就可以到\x01",
            "铁轨上面去了吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrFlags(0x107, 0x20)

    def lambda_59AB():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_59AB)
    Sleep(50)

    def lambda_59BB():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_59BB)
    Sleep(50)

    def lambda_59CB():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_59CB)
    Sleep(50)

    def lambda_59DB():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_59DB)
    Sleep(50)

    def lambda_59EB():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_59EB)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    ClearChrFlags(0x107, 0x20)

    #C0130
    ChrTalk(
        0x106,
        "#10712F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x105,
        (
            "#10402F#6P原来如此……\x01",
            "还有这个办法啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x107,
        (
            "#01203F#3C#11P可是，克洛斯贝尔市周围\x01",
            "目前被『结界』笼罩着。\x02\x03",

            "#01201F在不被察觉的情况下\x01",
            "进入市内是不可能的。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#00004F#5P是啊……我明白。\x02\x03",

            "#00000F但要是往西走呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107, 0xFFFFFDA8, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0134
    ChrTalk(
        0x103,
        "#00205F#6P罗伊德前辈，难道你想……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        (
            "#00307F#12P你打算经由铁道，\x01",
            "潜入贝尔加德门吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00006F#5P……是的。\x02\x03",

            "#00001F我在想，能否和索妮亚司令\x01",
            "当面谈谈呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        "#00301F#12P唔……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#00206F#6P的确，如果她能站在我们这边，\x01",
            "实在是个再可靠不过的后盾……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x105,
        (
            "#10408F#6P但她当时并未反对警备队\x01",
            "重组为国防军这一决定吧？\x02\x03",

            "#10401F考虑到这一点，风险似乎有些高啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x106,
        "#10706F#11P……我也有同感。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#00003F#5P司令自然也有自己的立场，\x01",
            "如果直接前去拜访，我们肯定会被逮捕的。\x02\x03",

            "#00008F但如果想办法潜入大门，\x01",
            "与她取得秘密接触……\x02\x03",

            "#00001F她说不定就会向我们\x01",
            "袒露自己的真正看法。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        "#00200F#6P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x104,
        (
            "#00303F#12P……通过米蕾优他们的态度便不难发现，\x01",
            "国防军内部肯定也有不少人\x01",
            "对目前的体制持怀疑态度。\x02\x03",

            "#00300F像司令那种正义感极强的人，\x01",
            "就更不用说了。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x105,
        (
            "#10406F#6P嗯……既然如此，\x01",
            "我也不反对……\x02\x03",

            "#10401F但如果索妮亚司令在那里的话，\x01",
            "『她』肯定也会在吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0x107, 0x20)

    def lambda_5F33():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5F33)
    Sleep(50)

    def lambda_5F43():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5F43)
    Sleep(50)

    def lambda_5F53():
        TurnDirection(0x106, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5F53)
    Sleep(50)

    def lambda_5F63():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5F63)
    Sleep(50)

    def lambda_5F73():
        TurnDirection(0x107, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_5F73)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x107, 0)
    ClearChrFlags(0x107, 0x20)

    #C0145
    ChrTalk(
        0x103,
        "#00201F#5P啊……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x104,
        "#00306F#11P……还有这个问题啊。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x106,
        "#10708F#11P你是指诺艾尔小姐吧……？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x107,
        (
            "#01200F#3C#11P唔，据你们所说，\x01",
            "她的决心似乎十分坚定。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#00008F#5P……我明白。\x02\x03",

            "#00006F不过，我们的前路\x01",
            "必定困难重重。\x02\x03",

            "#00003F我们与她之间的理念冲突\x01",
            "是迟早要解决的问题。\x02\x03",

            "#00013F为此，哪怕要和她\x01",
            "正面交锋也在所不惜。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x107, 0x20)

    def lambda_60E6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_60E6)
    Sleep(50)

    def lambda_60F6():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_60F6)
    Sleep(50)

    def lambda_6106():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6106)
    Sleep(50)

    def lambda_6116():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_6116)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    ClearChrFlags(0x107, 0x20)

    #C0150
    ChrTalk(
        0x103,
        "#00208F#6P罗伊德前辈……\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#00301F#12P……说的也是，\x01",
            "总不能一直躲躲闪闪的。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x105,
        (
            "#10404F#6P呵呵，既然你已经考虑到了这一层，\x01",
            "那我也没什么可说的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x106,
        (
            "#10710F#11P总之，\x01",
            "我们先把这道门打开吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0154
    ChrTalk(
        0x101,
        "#00000F#5P好……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(113, 0, 50, 0)
    Sound(114, 0, 100, 0)
    Sleep(1000)
    SetChrPos(0x0, -64000, -8000, 75000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetScenarioFlags(0x1A3, 1)
    OP_29(0xAF, 0x1, 0x10)
    ModifyEventFlags(0, 1, 0x80)
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x1)
    ModifyEventFlags(0, 3, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_33_556C end

    def Function_34_628B(): pass

    label("Function_34_628B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFlags(0x8, 0x1000)
    OP_68(5500, 5000, 27500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    OP_68(5500, 5500, 27500, 8000)
    MoveCamera(45, 30, 0, 8000)
    SetCameraDistance(30000, 8000)
    OP_71(0x8, 0x208, 0x2BC, 0x0, 0x0)
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
    NewScene("r2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_628B end

    def Function_35_635C(): pass

    label("Function_35_635C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x11, 0x80)
    OP_78(0x4, 0x11)
    OP_49()
    SetChrPos(0x11, -134100, -2000, 14320, 90)
    OP_D5(0x11, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    ClearChrFlags(0x12, 0x80)
    OP_78(0x23, 0x12)
    OP_49()
    SetChrPos(0x12, -134100, -2000, 14320, 90)
    OP_D5(0x12, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x23, 0x4)
    SetMapObjFlags(0x23, 0x1000)
    SetMapObjFrame(0x23, "light", 0x0, 0x1)
    OP_74(0x23, 0x1E)
    OP_71(0x4, 0xB5, 0xF0, 0x1, 0x20)
    OP_E2(0x3)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x103, 0x80)
    OP_68(-113630, -2100, 10940, 0)
    MoveCamera(25, 29, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(48250, 0)
    Sound(458, 0, 100, 0)
    Sound(493, 0, 100, 0)
    BeginChrThread(0x12, 3, 0, 38)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x11, 3, 0, 37)
    SetCameraDistance(53860, 3000)
    Sleep(1500)
    Sound(494, 0, 100, 0)
    OP_6F(0x10)
    Sleep(500)
    SetScenarioFlags(0x23, 4)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_635C end

    def Function_36_649E(): pass

    label("Function_36_649E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch44100.itc", 0x1E)
    LoadChrToIndex("chr/ch47500.itc", 0x1F)
    LoadChrToIndex("chr/ch23600.itc", 0x20)
    LoadEffect(0x0, "event/ev14100.eff")
    ClearChrFlags(0x11, 0x80)
    OP_78(0x4, 0x11)
    OP_49()
    SetChrPos(0x11, -64480, -2000, -450, 90)
    OP_D5(0x11, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x12, 0x80)
    OP_78(0x23, 0x12)
    OP_49()
    SetChrPos(0x12, -43460, 0, 1050, 90)
    OP_D5(0x12, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x23, 0x4)
    SetMapObjFlags(0x23, 0x1000)
    SetMapObjFrame(0x23, "light", 0x0, 0x1)
    OP_74(0x23, 0x1E)
    OP_71(0x23, 0xB5, 0xF0, 0x1, 0x20)
    OP_68(-40740, 440, -3760, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x3)
    OP_6B(0x12)
    BeginChrThread(0x12, 3, 0, 39)
    BeginChrThread(0x24, 1, 0, 48)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x11, 3, 0, 40)

    #N0155
    NpcTalk(
        0x12,
        "瑞吉",
        (
            "#6A#40W咦、咦咦……\x01",
            "刹、刹车失灵了！？\x02",
        )
    )
    #Auto

    Sleep(1500)

    #N0156
    NpcTalk(
        0x12,
        "塞克斯、尤利",
        "#6A#40W你、你说什么！？\x02",
    )
    #Auto

    Sleep(1500)
    OP_63(0x12, 0x0, 3100, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_6B(0xFF)
    OP_68(-28010, 600, -20980, 2000)
    MoveCamera(59, 23, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(29550, 2000)
    OP_71(0x4, 0xB5, 0xB5, 0x0, 0x0)
    OP_71(0x23, 0xB5, 0xB5, 0x0, 0x0)
    OP_64(0x12)
    FadeToDark(300, 0, 100)
    OP_6F(0x79)

    #N0157
    NpcTalk(
        0x11,
        "罗伊德",
        (
            "#00005F他们的车好像出现\x01",
            "问题了……！\x02\x03",

            "#00003F（怎么办！？\x01",
            "  再这样下去，说不定会演变为\x01",
            "  一起严重事故……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K紧急指令\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "绕到车前使其停下\x01",      # 0
            "撞上车尾使其停下\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_682F")
    SetScenarioFlags(0x178, 6)

    #N0159
    NpcTalk(
        0x11,
        "罗伊德",
        (
            "#00007F诺艾尔！\x01",
            "加快车速！绕到他们前面去！\x02\x03",

            "#00003F虽说这样做会有一定危险……\x01",
            "但我们就用车身来挡住他们吧！\x02",
        )
    )

    CloseMessageWindow()

    #N0160
    NpcTalk(
        0x11,
        "诺艾尔",
        "#10107F……明白了！\x02",
    )

    CloseMessageWindow()
    OP_29(0x8B, 0x1, 0x6)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_68DB")

    label("loc_682F")


    #N0161
    NpcTalk(
        0x11,
        "罗伊德",
        (
            "#00007F诺艾尔！\x01",
            "加快车速！\x01",
            "从后面撞上他们！\x02\x03",

            "#00003F如果能把他们撞到那个池子里，\x01",
            "就能把损害控制在最小程度……！\x02",
        )
    )

    CloseMessageWindow()

    #N0162
    NpcTalk(
        0x11,
        "诺艾尔",
        "#10107F……明白了！\x02",
    )

    CloseMessageWindow()
    OP_29(0x8B, 0x1, 0x7)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_68DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 6)), scpexpr(EXPR_END)), "loc_69E1")
    OP_63(0x12, 0x0, 3100, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x24, 1, 0, 49)
    OP_71(0x4, 0xB5, 0xF0, 0x1, 0x20)
    OP_71(0x23, 0xB5, 0xF0, 0x1, 0x20)
    Fade(500)
    OP_68(-11870, 600, -31810, 0)
    MoveCamera(59, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23270, 0)
    BeginChrThread(0x11, 3, 0, 44)
    BeginChrThread(0x12, 3, 0, 41)
    OP_63(0x12, 0x0, 3100, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()

    #N0163
    NpcTalk(
        0x12,
        "尤利、塞克斯、瑞吉",
        "#5S#8A#30W呜哇哇哇哇哇哇～～～！！\x02",
    )
    #Auto

    Sleep(1200)
    BeginChrThread(0x12, 3, 0, 43)
    OP_0D()
    OP_68(-7500, 600, -37130, 2000)
    MoveCamera(38, 25, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(25520, 2000)
    OP_64(0x12)
    OP_0D()
    Jump("loc_6AFE")

    label("loc_69E1")

    OP_63(0x12, 0x0, 3100, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x24, 1, 0, 50)
    OP_71(0x4, 0xB5, 0xF0, 0x1, 0x20)
    OP_71(0x23, 0xB5, 0xF0, 0x1, 0x20)
    Fade(500)
    OP_68(-11870, 600, -31810, 0)
    MoveCamera(59, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23270, 0)
    BeginChrThread(0x12, 3, 0, 41)
    OP_63(0x12, 0x0, 3100, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()
    BeginChrThread(0x11, 3, 0, 42)

    #N0164
    NpcTalk(
        0x12,
        "尤利、塞克斯、瑞吉",
        "#5S#8A#30W呜哇哇哇哇哇哇～～～！！\x02",
    )
    #Auto

    Sleep(1200)
    OP_82(0x1F4, 0x64, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(500)
    WaitChrThread(0x12, 3)
    BeginChrThread(0x12, 3, 0, 43)
    OP_68(-7500, 600, -37130, 2000)
    MoveCamera(38, 25, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(25520, 2000)
    OP_64(0x12)
    OP_0D()

    label("loc_6AFE")

    ClearMapObjFlags(0x24, 0x4)
    SetMapObjFlags(0x24, 0x1000)
    OP_78(0x24, 0x1D)
    OP_74(0x24, 0x1E)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    OP_49()
    SetChrPos(0x1D, -880, -1000, -42770, 170)
    OP_D5(0x1D, 0x0, 0x29810, 0x0, 0x0)
    OP_71(0x4, 0x5B, 0x78, 0x1, 0x0)
    OP_71(0x23, 0x5B, 0x78, 0x1, 0x0)
    SetChrFlags(0x12, 0x80)
    OP_68(-6410, 600, -43900, 3000)
    MoveCamera(63, 27, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(19600, 3000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -2000, -2000, -43030, 270)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -2000, -2000, -43030, 270)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -2000, -2000, -43030, 270)
    OP_49()

    def lambda_6C0A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_6C0A)

    def lambda_6C1B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_6C1B)

    def lambda_6C2C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_6C2C)
    OP_0D()
    OP_6F(0x79)
    Sleep(2000)
    Sound(485, 0, 100, 0)
    Sleep(50)
    Sound(100, 0, 50, 0)
    OP_71(0x23, 0xF1, 0x10E, 0x0, 0x0)
    Sleep(1500)
    BeginChrThread(0x1A, 3, 0, 47)
    Sleep(1000)
    BeginChrThread(0x19, 3, 0, 46)
    Sleep(1000)
    BeginChrThread(0x18, 3, 0, 45)
    WaitChrThread(0x18, 3)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0165
    ChrTalk(
        0x18,
        "呼……呼……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x19,
        "得、得救了吗……？\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x1A,
        "我、我还以为这次死定了……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-5890, 600, -39990, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25880, 0)
    SetChrPos(0x101, -7160, 0, -37760, 180)
    SetChrPos(0x102, -8730, 0, -37900, 135)
    SetChrPos(0x103, -9140, 0, -39620, 135)
    SetChrPos(0x109, -7560, 0, -35730, 180)
    SetChrPos(0x104, -5260, 0, -35940, 180)
    SetChrPos(0x105, -6310, 0, -35420, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x11, -8550, 0, -30480, 135)
    OP_0D()

    #C0168
    ChrTalk(
        0x102,
        (
            "#00106F呼……\x01",
            "总算没事了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 6)), scpexpr(EXPR_END)), "loc_6F05")
    OP_2C(0x8B, 0x1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0169
    ChrTalk(
        0x101,
        (
            "#00006F这、这都怪我下了\x01",
            "绕到前面的指示……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x109,
        (
            "#10101F哪、哪里的话，\x01",
            "相比发生事故，酿成巨大惨剧，\x01",
            "这种结果要好得多了！\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            "#00203F而且握方向盘的人是\x01",
            "他们自己，这只不过是自作自受罢了。\x02\x03",

            "#00200F不管怎么说，多亏如此，\x01",
            "我们的导力车才能毫发无伤呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FBB")

    label("loc_6F05")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0172
    ChrTalk(
        0x101,
        (
            "#00003F唔、唔……\x01",
            "直接撞上去，\x01",
            "果然还是太过火了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x109,
        (
            "#10106F这、这个嘛……\x01",
            "硬要说的话，\x01",
            "还真是有点呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        "#00203F不过，这也是他们自作自受。\x02",
    )

    CloseMessageWindow()

    label("loc_6FBB")


    #C0175
    ChrTalk(
        0x104,
        (
            "#00309F能够保住性命，\x01",
            "对他们来说就算是赚到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x105,
        "#10304F呵呵，他们这方面的运气还真不错呢。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#00003F唔……\x02\x03",

            "#00000F也罢。\x01",
            "总之，我们赶快联络米蕾优三尉\x01",
            "和公共安全科吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    OP_64(0x18)
    OP_64(0x19)
    OP_64(0x1A)
    SetMapObjFlags(0x24, 0x4)
    ClearScenarioFlags(0x178, 6)
    Call(0, 51)
    Return()

    # Function_36_649E end

    def Function_37_7090(): pass

    label("Function_37_7090")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -134100, -2000, 14320)
    OP_9F(0x1, -108810, -2000, 13590)
    OP_9F(0x1, -100530, -2000, 9110)
    OP_9F(0x1, -85050, -2000, -6880)
    OP_9F(0x2, 0xFE, 15000, 0x6)
    Return()

    # Function_37_7090 end

    def Function_38_70D6(): pass

    label("Function_38_70D6")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -134100, -2000, 14320)
    OP_9F(0x1, -108810, -2000, 13590)
    OP_9F(0x1, -100530, -2000, 9110)
    OP_9F(0x1, -85050, -2000, -6880)
    OP_9F(0x2, 0xFE, 15000, 0x6)
    Return()

    # Function_38_70D6 end

    def Function_39_711C(): pass

    label("Function_39_711C")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -43460, 0, 1050)
    OP_9F(0x1, -40270, 0, -4210)
    OP_9F(0x1, -33620, 0, -5910)
    OP_9F(0x1, -36270, 0, -12500)
    OP_9F(0x1, -30300, 0, -15190)
    OP_9F(0x1, -29950, 0, -23990)
    OP_9F(0x1, -21680, 0, -25620)
    OP_9F(0x1, -14580, 0, -30740)
    OP_9F(0x2, 0xFE, 9000, 0x6)
    Return()

    # Function_39_711C end

    def Function_40_719A(): pass

    label("Function_40_719A")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -62310, -2000, -10)
    OP_9F(0x1, -51780, 0, 500)
    OP_9F(0x1, -40680, 0, -580)
    OP_9F(0x1, -34230, 0, -8310)
    OP_9F(0x1, -32860, 0, -16350)
    OP_9F(0x1, -29710, 0, -21610)
    OP_9F(0x2, 0xFE, 12000, 0x6)
    Return()

    # Function_40_719A end

    def Function_41_71FC(): pass

    label("Function_41_71FC")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -18370, 0, -31800)
    OP_9F(0x1, -13420, 0, -30030)
    OP_9F(0x1, -9100, 0, -32729)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_41_71FC end

    def Function_42_7234(): pass

    label("Function_42_7234")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -21840, 0, -26500)
    OP_9F(0x1, -13400, 0, -26670)
    OP_9F(0x1, -10840, 0, -29640)
    OP_9F(0x2, 0xFE, 18000, 0x6)
    Return()

    # Function_42_7234 end

    def Function_43_726C(): pass

    label("Function_43_726C")

    OP_95(0x12, -5160, 0, -36470, 10000, 0x0)
    OP_95(0x12, -3160, 0, -38680, 10000, 0x0)
    OP_95(0x12, -1500, -2000, -40300, 10000, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -1500, -2000, -40300, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_95(0x12, -880, -2000, -42770, 3000, 0x0)
    Return()

    # Function_43_726C end

    def Function_44_72F4(): pass

    label("Function_44_72F4")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -22220, 0, -26340)
    OP_9F(0x1, -8890, 0, -25820)
    OP_9F(0x1, -6490, 0, -28390)
    OP_9F(0x2, 0xFE, 18000, 0x6)
    Return()

    # Function_44_72F4 end

    def Function_45_732C(): pass

    label("Function_45_732C")


    def lambda_7331():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_7331)
    OP_9B(0x1, 0x18, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_95(0x18, -3500, -2000, -42500, 1000, 0x0)
    OP_93(0x18, 0x10E, 0x1F4)
    Return()

    # Function_45_732C end

    def Function_46_7368(): pass

    label("Function_46_7368")


    def lambda_736D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_736D)
    OP_9B(0x1, 0x19, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_95(0x19, -3500, -2000, -43700, 1000, 0x0)
    OP_93(0x19, 0x10E, 0x1F4)
    Return()

    # Function_46_7368 end

    def Function_47_73A4(): pass

    label("Function_47_73A4")


    def lambda_73A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_73A9)
    OP_9B(0x1, 0x1A, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_95(0x1A, -3500, -2000, -41300, 1000, 0x0)
    OP_93(0x1A, 0x10E, 0x1F4)
    Return()

    # Function_47_73A4 end

    def Function_48_73E0(): pass

    label("Function_48_73E0")

    Sound(486, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(493, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(492, 0, 100, 0)
    Sound(487, 0, 50, 0)
    Return()

    # Function_48_73E0 end

    def Function_49_741A(): pass

    label("Function_49_741A")

    Sound(486, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(492, 0, 100, 0)
    Sleep(1200)
    Sound(976, 0, 100, 0)
    Sound(833, 0, 80, 0)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_49_741A end

    def Function_50_745C(): pass

    label("Function_50_745C")

    Sound(486, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(196, 0, 70, 0)
    Sound(880, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(1200)
    Sound(976, 0, 100, 0)
    Sound(833, 0, 80, 0)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_50_745C end

    def Function_51_74AA(): pass

    label("Function_51_74AA")

    EventBegin(0x0)
    SetChrPos(0x11, -8560, 0, -31050, 135)
    OP_D5(0x11, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x22, 0x1000)
    ClearMapObjFlags(0x22, 0x4)
    OP_78(0x22, 0x13)
    SetMapObjFrame(0x22, "light", 0x0, 0x1)
    OP_74(0x22, 0x1E)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    OP_49()
    SetChrPos(0x13, -13410, 0, -31470, 135)
    OP_D5(0x13, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x21, 0x1000)
    ClearMapObjFlags(0x21, 0x4)
    OP_78(0x21, 0x14)
    SetMapObjFrame(0x21, "light", 0x0, 0x1)
    SetMapObjFrame(0x21, "mark01", 0x0, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    OP_49()
    SetChrPos(0x14, -100, 0, -32439, 180)
    OP_D5(0x14, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(-4280, 600, -28840, 0)
    MoveCamera(49, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26770, 0)
    LoadChrToIndex("chr/ch30600.itc", 0x21)
    LoadChrToIndex("chr/ch32600.itc", 0x22)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -10800, 0, -42330, 90)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -12000, 0, -40540, 45)
    SetChrPos(0x12, -14390, 0, -36830, 180)
    OP_D5(0x12, 0x0, 0x2BF20, 0x0, 0x0)
    OP_71(0x23, 0x1, 0x1E, 0x1, 0x0)
    SetChrPos(0x18, -8910, 0, -42330, 270)
    SetChrPos(0x19, -8910, 0, -41130, 225)
    SetChrPos(0x1A, -8910, 0, -43530, 315)
    SetChrPos(0x101, -9870, 0, -39550, 222)
    SetChrPos(0x102, -9930, 0, -38020, 225)
    SetChrPos(0x103, -14020, 0, -39900, 0)
    SetChrPos(0x109, -11940, 0, -36430, 270)
    SetChrPos(0x104, -7980, 0, -38440, 225)
    SetChrPos(0x105, -8620, 0, -37660, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_E2(0x3)
    OP_68(-10480, 600, -38660, 7000)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-9700, 600, -39930, 0)
    MoveCamera(49, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20920, 0)
    OP_0D()
    Sleep(300)

    #C0178
    ChrTalk(
        0x1B,
        "#2P居住在住宅街的『高贵之血』……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x1B,
        (
            "#2P你们涉嫌超速及其它违法行为，\x01",
            "现在要把你们几个带走。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x18,
        "哼。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x19,
        "啧……\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x1A,
        "可、可恶～！\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#00000F总之，这件事也算告一段落了啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x101, 500)
    Sleep(100)

    #C0184
    ChrTalk(
        0x1C,
        (
            "#07900F这次真是辛苦诸位了。\x01",
            "多亏有你们的帮助，才能成功\x01",
            "抓住这些飙车族。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1C, 500)
    Sleep(100)

    #C0185
    ChrTalk(
        0x1B,
        (
            "#2P米蕾优三尉，\x01",
            "十分感谢您的协助！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)
    Sleep(100)

    #C0186
    ChrTalk(
        0x1B,
        (
            "#2P在边境地带处于紧张局势的\x01",
            "繁忙时期还特意前来协助我们……\x01",
            "实在是感激不尽！\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x1C,
        (
            "#07904F呵呵，彼此彼此。\x02\x03",

            "#07900F对我们来说，这也算是消除了\x01",
            "一个警备方面的不安定要素……\x02\x03",

            "#07902F另外，也要再次\x01",
            "感谢支援科的帮助。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x1C, 500)
    Sleep(100)

    #C0188
    ChrTalk(
        0x104,
        "#00309F哈哈，不用这么客气啦。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)
    Sleep(100)

    #C0189
    ChrTalk(
        0x102,
        (
            "#00105F对了……\x01",
            "缇欧、诺艾尔，\x01",
            "他们的导力车怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-10450, 600, -37570, 2000)
    MoveCamera(38, 21, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(22020, 2000)

    def lambda_79FA():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_79FA)
    Sleep(50)

    def lambda_7A0A():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7A0A)
    Sleep(50)

    def lambda_7A1A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A1A)
    Sleep(50)

    def lambda_7A2A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7A2A)
    Sleep(50)

    def lambda_7A3A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7A3A)
    Sleep(50)

    def lambda_7A4A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7A4A)
    Sleep(50)

    def lambda_7A5A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_7A5A)
    Sleep(50)

    def lambda_7A6A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7A6A)
    Sleep(50)

    def lambda_7A7A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7A7A)
    Sleep(50)

    def lambda_7A8A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_7A8A)
    OP_6F(0x79)
    Sleep(500)

    #C0190
    ChrTalk(
        0x109,
        (
            "#10100F已经查明刹车\x01",
            "失灵的原因了。\x02\x03",

            "#10106F看来只是因为他们对导力车的\x01",
            "维护不够到位而已。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1A, 500)
    Sleep(100)

    #C0191
    ChrTalk(
        0x19,
        (
            "瑞吉，你这家伙……\x01",
            "我不是把维护车辆的事情交给你负责了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x1A,
        (
            "这么一说，我最近好像\x01",
            "是有点偷懒……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x18, 500)
    Sleep(100)

    #C0193
    ChrTalk(
        0x103,
        (
            "#00200F另外，导力引擎也因短路\x01",
            "而彻底损毁了。\x02\x03",

            "#00203F要想修好这辆导力车，\x01",
            "所需花费的修理费用恐怕\x01",
            "都够买一辆新车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x109,
        (
            "#10106F虽然有些浪费……\x01",
            "但也只能把它当作报废车辆来处理了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x103, 500)
    Sleep(100)
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0195
    ChrTalk(
        0x1A,
        "真、真的假的啊……？\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x19,
        (
            "啧，那可是尤利特地准备的\x01",
            "乌尔努公司的最新款啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x18,
        (
            "哼，对我来说，一两辆\x01",
            "导力车根本就不算什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x18,
        (
            "只要到导力商店之类的地方\x01",
            "再买一辆不就好了嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x1A)

    #C0199
    ChrTalk(
        0x1A,
        (
            "哈哈，不愧是尤利！\x01",
            "真是阔绰啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)
    Sleep(100)

    #C0200
    ChrTalk(
        0x19,
        (
            "那我们就赶快去\x01",
            "买新车吧～\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-8540, 600, -39680, 2000)
    MoveCamera(45, 21, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(21910, 2000)

    def lambda_7DCB():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DCB)
    Sleep(50)

    def lambda_7DDB():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7DDB)
    Sleep(50)

    def lambda_7DEB():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7DEB)
    Sleep(50)

    def lambda_7DFB():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7DFB)
    Sleep(50)

    def lambda_7E0B():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E0B)
    Sleep(50)

    def lambda_7E1B():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E1B)
    Sleep(50)

    def lambda_7E2B():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7E2B)
    Sleep(50)

    def lambda_7E3B():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_7E3B)
    OP_6F(0x79)
    Sleep(500)

    #C0201
    ChrTalk(
        0x101,
        (
            "#00007F等、等一下！\x02\x03",

            "#00003F不管怎么说，你们这次的\x01",
            "驾驶明显超速了！\x02\x03",

            "#00001F首先应该虚心接受处罚……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7EB7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7EB7)
    Sleep(50)

    def lambda_7EC7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7EC7)
    Sleep(50)

    def lambda_7ED7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_7ED7)
    Sleep(1000)

    #C0202
    ChrTalk(
        0x18,
        "哼，处罚又能怎样？\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x18,
        (
            "自治州法根本就不能对\x01",
            "我们这些外国人\x01",
            "做出严重处罚。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FEF")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "QS_1105 取缔飙车族１？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【未变更】\x01",      # 0
            "【已完成】\x01",      # 1
            "【未完成】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FDB")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_7FEF")

    label("loc_7FDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FEF")
    OP_29(0x69, 0x3, 0x10)

    label("loc_7FEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8067")

    #C0205
    ChrTalk(
        0x18,
        (
            "和上次一样，只要支付\x01",
            "一点罚金就没事了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x104,
        "#00310F啧……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x105,
        "#10306F哎呀呀，又是这种结局吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_80FE")

    label("loc_8067")


    #C0208
    ChrTalk(
        0x18,
        (
            "反正只要支付\x01",
            "一点罚金就没事了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(100)

    #C0209
    ChrTalk(
        0x104,
        "#00305F真、真的吗？\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x105,
        (
            "#10303F他说得没错，出于各种原因，\x01",
            "现行法律无法对外国人\x01",
            "进行严厉惩处……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80FE")

    TurnDirection(0x104, 0x18, 500)
    Sleep(100)

    #C0211
    ChrTalk(
        0x19,
        "呵呵，就是这样。\x02",
    )

    CloseMessageWindow()

    def lambda_8123():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8123)
    Sleep(50)

    def lambda_8133():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8133)
    Sleep(50)

    def lambda_8143():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8143)
    Sleep(500)

    #C0212
    ChrTalk(
        0x18,
        (
            "我们很忙的，\x01",
            "你们特地把我们带回总部\x01",
            "也很麻烦吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x18,
        (
            "既然如此，我就当场把\x01",
            "罚金付清好了。\x01",
            "这样一来，你们就没什么可抱怨了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x1A,
        "哈哈，尤利真聪明啊～！\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x109,
        "#10107F你、你们几个……！\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x103,
        (
            "#00206F……态度恶劣得让人\x01",
            "无言以对呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x102)
    OP_64(0x1B)

    #C0217
    ChrTalk(
        0x102,
        "#00103F……不，这次可没那么简单了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_82CB():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_82CB)
    Sleep(50)

    def lambda_82DB():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_82DB)
    Sleep(50)

    def lambda_82EB():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_82EB)
    Sleep(500)

    #C0218
    ChrTalk(
        0x19,
        "……啊？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#00100F迪塔叔叔担任市长之后，\x01",
            "一直在致力于改进\x01",
            "克洛斯贝尔自治州法。\x02\x03",

            "#00103F听说，有一部分在不久前\x01",
            "已经修正完毕了。\x02\x03",

            "#00101F依照那些修正条例，\x01",
            "将会加强对外国犯罪者的\x01",
            "处罚力度。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x18,
        "你说什么……！？\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x1B,
        (
            "根据这次的事态，\x01",
            "需要吊销你们的驾照一个月……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x1B,
        "这样处理应该很妥当。\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_8473():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8473)
    Sleep(50)

    def lambda_8483():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8483)
    Sleep(50)

    def lambda_8493():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8493)
    Sleep(500)

    #C0223
    ChrTalk(
        0x19,
        "吊销驾照一个月～！？\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x19,
        (
            "也就是说，\x01",
            "就算买了新导力车，\x01",
            "我们也不能开吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x1A,
        (
            "我、我们这次\x01",
            "说不定真的有点过分了……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x18,
        "……开、开什么玩笑……！\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x18,
        (
            "我凭什么要接受\x01",
            "这种处罚啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x18,
        (
            "#4S只不过是区区自治州的警察而已，\x01",
            "你们真的以为自己\x01",
            "有权处罚我吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#00010F什么……！\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x1B,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x19,
        "……哈、哈哈，就是说啊。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x19,
        (
            "不过是克洛斯贝尔的警察而已，\x01",
            "哪有处罚我们的权力！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x18, 500)
    Sleep(100)

    #C0233
    ChrTalk(
        0x1A,
        (
            "尤、尤利、塞克斯，\x01",
            "可是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1A, 500)
    Sleep(100)

    #C0234
    ChrTalk(
        0x18,
        (
            "瑞吉，你给我闭嘴！\x01",
            "他们可是打算让我们这次的\x01",
            "旅行计划彻底泡汤啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1B, 500)
    Sleep(100)

    #C0235
    ChrTalk(
        0x18,
        (
            "事到如今，\x01",
            "就去让老爸想想办法，\x01",
            "给自治州政府施加压力……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-8700, 600, -39850, 0)
    MoveCamera(41, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18880, 0)
    OP_0D()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0236
    ChrTalk(
        0x1B,
        "#5S……你们给我适可而止吧！\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_884A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_884A)
    Sleep(50)

    def lambda_885A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_885A)
    Sleep(50)

    def lambda_886A():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_886A)
    Sleep(50)

    def lambda_887A():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_887A)
    Sleep(50)

    def lambda_888A():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_888A)
    Sleep(50)

    def lambda_889A():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_889A)
    Sleep(50)

    def lambda_88AA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_88AA)
    Sleep(50)

    def lambda_88BA():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_88BA)
    Sleep(50)

    def lambda_88CA():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_88CA)
    Sleep(1000)

    #C0237
    ChrTalk(
        0x1B,
        (
            "在这起事件中，处罚之类的\x01",
            "问题并不是重点！\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x1B,
        (
            "你们那种野蛮的驾驶方式\x01",
            "给无辜的民众留下了\x01",
            "多少恐怖的回忆……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x1B,
        (
            "你们想过\x01",
            "这个问题吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x19,
        "干、干嘛突然这么凶啊……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x18,
        (
            "哼、哼……！\x01",
            "平民是否会害怕，\x01",
            "关我们什么事。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x18,
        "而且，只不过被导力车——\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x1B,
        (
            "那么……\x01",
            "你们自己就不害怕吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x1B,
        (
            "像这次的事故，\x01",
            "如果不是支援科的各位救了你们，\x01",
            "你们说不定连命都没了吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0245
    ChrTalk(
        0x1A,
        (
            "确、确实，掉进池子的时候，\x01",
            "我还以为这次要完蛋了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x19,
        (
            "……哈、哈哈，胡说什么呢。\x01",
            "我们这么高贵，怎么可能会出那种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x1B,
        "这和你们的身份毫无关系！\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x1B,
        (
            "无辜的人突然\x01",
            "被卷入事故或犯罪事件，\x01",
            "并因此而受伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x1B,
        (
            "我作为一名警察，\x01",
            "至今为止，不知见过多少\x01",
            "类似的案子了！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x1B,
        (
            "你们的危险驾驶也是一样，\x01",
            "给他人造成了\x01",
            "那么可怕的危险！\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x1B,
        (
            "即使如此，你们也敢说\x01",
            "完全不觉得害怕吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x18,
        "…………唔…………\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x1B,
        (
            "丝毫不会为他人着想，\x01",
            "不断给别人造成麻烦……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0254
    ChrTalk(
        0x1B,
        "#4S这只会让你们的高贵血统蒙羞！\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0255
    ChrTalk(
        0x1B,
        "#4S作为一个人，你们难道就不觉得羞耻吗！？\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0256
    ChrTalk(
        0x18,
        "#100W…………唔……唔唔……！！\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x101,
        "#00005F凯特前辈……\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x1B,
        (
            "……总之，我会把\x01",
            "你们几个带回总部。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1B,
        (
            "在吊销驾照的这一个月里，\x01",
            "你们一定要好好反省！！\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x1B,
        (
            "好了，如果听明白了，\x01",
            "就赶快坐到警车里去！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x18, 500)
    Sleep(100)

    #C0261
    ChrTalk(
        0x1A,
        "我、我说啊，尤利、塞克斯……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)
    Sleep(100)

    #C0262
    ChrTalk(
        0x19,
        "嗯，老实说，这次实在是……\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x18,
        "………………啧…………\x02",
    )

    CloseMessageWindow()
    OP_68(-10780, 600, -37980, 3000)
    MoveCamera(37, 28, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(18880, 3000)
    BeginChrThread(0x18, 1, 0, 57)
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 52)
    Sleep(100)
    BeginChrThread(0x102, 1, 0, 53)
    Sleep(100)
    BeginChrThread(0x104, 1, 0, 54)
    Sleep(100)
    BeginChrThread(0x105, 1, 0, 55)
    Sleep(100)

    def lambda_8E81():

        label("loc_8E81")

        TurnDirection(0xFE, 0x18, 0)
        Yield()
        Jump("loc_8E81")

    QueueWorkItem2(0x103, 1, lambda_8E81)
    Sleep(100)
    BeginChrThread(0x109, 1, 0, 56)
    Sleep(100)

    def lambda_8E9F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_8E9F)
    Sleep(50)

    def lambda_8EAF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_8EAF)
    Sleep(2500)

    def lambda_8EBF():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8EBF)
    Sleep(50)

    def lambda_8ECF():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8ECF)
    Sleep(50)

    def lambda_8EDF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_8EDF)
    Sleep(1000)

    def lambda_8EEF():

        label("loc_8EEF")

        TurnDirection(0xFE, 0x18, 0)
        Yield()
        Jump("loc_8EEF")

    QueueWorkItem2(0x109, 1, lambda_8EEF)
    WaitChrThread(0x18, 1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    Sound(462, 0, 100, 0)
    OP_71(0x22, 0x169, 0x186, 0x1, 0x0)
    Sleep(500)
    OP_79(0x23)
    Sleep(300)

    def lambda_8F28():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8F28)

    def lambda_8F3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_8F3D)
    Sleep(300)

    #C0264
    ChrTalk(
        0x19,
        "喂、喂喂，尤利！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x1A,
        "等、等等我们呀～！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x19, 1, 0, 58)
    Sleep(100)
    BeginChrThread(0x1A, 1, 0, 59)
    WaitChrThread(0x19, 1)

    def lambda_8F92():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8F92)

    def lambda_8FA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_8FA7)
    WaitChrThread(0x1A, 1)

    def lambda_8FBC():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8FBC)

    def lambda_8FD1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_8FD1)
    Sleep(500)
    Sound(461, 0, 100, 0)
    OP_71(0x22, 0x187, 0x1A4, 0x1, 0x0)
    Sleep(800)
    OP_79(0x23)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    OP_68(-9990, 600, -38760, 3000)
    OP_6F(0x79)
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    #C0266
    ChrTalk(
        0x101,
        (
            "#00002F（哈哈，看来这番话\x01",
            "  对他们起效了呢。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0267
    ChrTalk(
        0x102,
        (
            "#00104F（是啊……凯特前辈\x01",
            "  刚才可真是气势汹汹。）\x02\x03",

            "#00102F（他们平时肯定没受过什么训斥，\x01",
            "  这次就算是给他们上了一课吧。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x101, 500)
    Sleep(100)

    #C0268
    ChrTalk(
        0x1B,
        (
            "特别任务支援科的各位、米蕾优三尉……\x01",
            "这次真是十分感谢你们的协助！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9138():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9138)
    Sleep(50)

    def lambda_9148():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9148)
    Sleep(50)

    def lambda_9158():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9158)
    Sleep(50)

    def lambda_9168():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9168)
    Sleep(50)

    def lambda_9178():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9178)
    Sleep(50)

    def lambda_9188():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9188)
    Sleep(50)

    def lambda_9198():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9198)
    Sleep(500)

    #C0269
    ChrTalk(
        0x101,
        "#00000F不用客气，您也辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，\x01",
            "这次玩得挺开心呢。\x02\x03",

            "#10304F还体验了一次\x01",
            "车辆追逐战。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x103,
        "#00206F……那可不是值得开心的事。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x1C,
        (
            "#07903F凯特巡警……您的那番话，\x01",
            "也让我感触很深。\x02\x03",

            "#07902F为了守护克洛斯贝尔，\x01",
            "我们今后也要一起努力！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1C, 500)
    Sleep(100)

    #C0273
    ChrTalk(
        0x1B,
        "呵呵，好的！！\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x1B,
        "……那么，我这就告辞了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-2670, 2900, -21660, 0)
    MoveCamera(31, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(27790, 0)
    SetChrPos(0x101, -1680, 0, -23640, 0)
    SetChrPos(0x102, -3300, 0, -25110, 0)
    SetChrPos(0x103, -240, 0, -24520, 0)
    SetChrPos(0x109, -3620, 0, -26890, 0)
    SetChrPos(0x104, -1950, 0, -25950, 0)
    SetChrPos(0x105, -4710, 0, -25570, 0)
    SetChrPos(0x1C, -3020, 0, -22920, 0)
    SetChrPos(0x13, -2650, 0, -18410, 0)
    OP_68(-2670, 600, -21660, 5000)
    BeginChrThread(0x13, 1, 0, 60)
    StopBGM(0xFA0)
    Sound(457, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    OP_68(-2220, 600, -22860, 3000)
    SetCameraDistance(22640, 3000)
    OP_6F(0x79)
    SetChrFlags(0x13, 0x80)
    TurnDirection(0x1C, 0x104, 500)
    Sleep(100)

    #C0275
    ChrTalk(
        0x1C,
        (
            "#07903F接下来，我也去安排一下，\x01",
            "把他们的导力车送到适当的地方吧。\x02\x03",

            "#07900F你们几位要不要一起来呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9461():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9461)
    Sleep(50)

    def lambda_9471():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9471)
    Sleep(50)

    def lambda_9481():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9481)
    Sleep(50)

    def lambda_9491():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9491)
    Sleep(50)

    def lambda_94A1():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_94A1)
    Sleep(50)

    def lambda_94B1():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_94B1)
    Sleep(500)

    #C0276
    ChrTalk(
        0x104,
        "#00304F嗯，反正都帮到这里了。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x109,
        "#10109F就让我们一起去吧！\x02",
    )

    CloseMessageWindow()
    StopSound(128, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0278
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人协助警备队\x01",
            "把飙车族的导力车运走……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0279
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "然后在贝尔加德门重新开始了自己的工作。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0280
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【追赶飙车族】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8B, 0x1, 0x8)
    OP_29(0x8B, 0x1, 0x9)
    OP_29(0x8B, 0x4, 0x10)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x1C, 0x80)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_37()
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("t2000", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_51_74AA end

    def Function_52_9633(): pass

    label("Function_52_9633")

    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_52_9633 end

    def Function_53_964A(): pass

    label("Function_53_964A")

    OP_9B(0x1, 0x102, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x102, 0x10E, 0x1F4)
    Return()

    # Function_53_964A end

    def Function_54_9661(): pass

    label("Function_54_9661")

    OP_9B(0x1, 0x104, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_54_9661 end

    def Function_55_9678(): pass

    label("Function_55_9678")

    OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_55_9678 end

    def Function_56_968F(): pass

    label("Function_56_968F")

    OP_93(0x109, 0x5A, 0x1F4)
    OP_9B(0x1, 0x109, 0xB4, 0x1F4, 0x3E8, 0x0)
    Sleep(2500)
    Return()

    # Function_56_968F end

    def Function_57_96A9(): pass

    label("Function_57_96A9")

    OP_9B(0x1, 0x18, 0x0, 0x320, 0x5DC, 0x0)
    OP_95(0x18, -9870, 0, -39550, 1500, 0x0)

    def lambda_96D1():
        TurnDirection(0x19, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_96D1)
    OP_95(0x18, -12250, 0, -33890, 1500, 0x0)
    OP_95(0x18, -13950, 0, -33830, 1500, 0x0)
    OP_93(0x18, 0x0, 0x1F4)
    Return()

    # Function_57_96A9 end

    def Function_58_9709(): pass

    label("Function_58_9709")

    OP_9B(0x0, 0x19, 0x0, 0x7D0, 0xBB8, 0x0)
    OP_95(0x19, -12250, 0, -33890, 3000, 0x0)
    OP_95(0x19, -13950, 0, -33830, 3000, 0x0)
    OP_93(0x19, 0x0, 0x1F4)
    Return()

    # Function_58_9709 end

    def Function_59_9748(): pass

    label("Function_59_9748")

    OP_95(0x1A, -8910, 0, -41130, 3000, 0x0)
    OP_95(0x1A, -10610, 0, -39800, 3000, 0x0)
    OP_95(0x1A, -12250, 0, -33890, 3000, 0x0)
    OP_95(0x1A, -13950, 0, -33830, 3000, 0x0)
    OP_93(0x1A, 0x0, 0x1F4)
    Return()

    # Function_59_9748 end

    def Function_60_97A0(): pass

    label("Function_60_97A0")

    OP_9F(0x0, 0x13)
    OP_9F(0x1, -2650, 0, -18410)
    OP_9F(0x1, -2370, 0, -5440)
    OP_9F(0x1, 2900, 0, 3350)
    OP_9F(0x1, 610, 640, 12550)
    OP_9F(0x1, 610, 2500, 19990)
    OP_9F(0x1, 2510, 2500, 24560)
    OP_9F(0x2, 0x13, 5500, 0x6)
    Return()

    # Function_60_97A0 end

    def Function_61_9802(): pass

    label("Function_61_9802")

    EventBegin(0x1)
    OP_E2(0x3)

    #C0281
    ChrTalk(
        0x101,
        (
            "#00001F没时间到处乱跑了，\x01",
            "赶快前往事故现场吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -60010, -1990, 470, 89)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_61_9802 end

    SaveToFile()

Try(main)
