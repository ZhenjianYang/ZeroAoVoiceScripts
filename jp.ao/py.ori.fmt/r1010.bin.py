from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "フランツ巡査",           # 1
        "ダリア隊員",             # 2
        "警官",                   # 3
        "警官",                   # 4
        "警官",                   # 5
        "警備隊員",               # 6
        "警備隊員",               # 7
        "グレイス",               # 8
        "レインズ",               # 9
        "車",                     # 10
        "暴走車",                 # 11
        "パトカー",               # 12
        "装甲車",                 # 13
        "パトカー２",             # 14
        "パトカー３",             # 15
        "装甲車２",               # 16
        "ユーリ",                 # 17
        "サイクス",               # 18
        "レジー",                 # 19
        "ケイト巡査",             # 20
        "ミレイユ三尉",           # 21
        "波紋",                   # 22
        "エボニードローメ",       # 23
        "エボニードローメ",       # 24
        "ガンテ",                 # 25
        "ガンテ",                 # 26
        "クロベルガ蟲",           # 27
        "幻獣",                   # 28
        "SE制御",                 # 29
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
        "クロスベル市方面",       # 40
        "ベルガード門方面",       # 41
    ))

    ATBonus("ATBonus_904", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_924", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_A267", 5,   5,   0,   3,   0,   0,   0)
    Sepith("Sepith_A26F", 2,   1,   4,   1,   0,   2,   2)
    Sepith("Sepith_A237", 2,   1,   5,   0,   0,   3,   2)
    Sepith("Sepith_A22F", 2,   0,   3,   4,   0,   0,   3)
    Sepith("Sepith_A227", 4,   2,   3,   0,   3,   0,   0)
    Sepith("Sepith_A27F", 11,  7,   4,   3,   6,   12,  7)

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
        "BattleInfo_C5C", 0x0000, 50, 6, 60, 8, 1, 30, 0, "br1000", "Sepith_A267", 30, 40, 20, 10,
        (
            ("ms71500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71500.dat", "ms71500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71500.dat", "ms71900.dat", "ms71500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71500.dat", "ms71500.dat", "ms71900.dat", "ms71500.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_B94", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_A26F", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_D24", 0x0000, 50, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_A237", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_ACC", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_A22F", 30, 40, 20, 10,
        (
            ("ms74800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms74800.dat", "ms74800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms74800.dat", "ms60900.dat", "ms74800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms74800.dat", "ms74800.dat", "ms60900.dat", "ms74800.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_A04", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_A227", 30, 40, 20, 10,
        (
            ("ms60900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60900.dat", "ms60900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60900.dat", "ms74800.dat", "ms60900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60900.dat", "ms60900.dat", "ms74800.dat", "ms60900.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_DEC", 0x0000, 84, 6, 60, 6, 1, 30, 0, "br1000", "Sepith_A27F", 40, 35, 25, 0,
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

    PlaceName(17.0, 0.0, 39.25, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(-133.0, -2.0, 6.0, 0x0000, 0x0000, "ベルガード門方面")

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
        "Function_8_2250",         # 08, 8
        "Function_9_23A1",         # 09, 9
        "Function_10_2508",        # 0A, 10
        "Function_11_271F",        # 0B, 11
        "Function_12_2A7D",        # 0C, 12
        "Function_13_2DDB",        # 0D, 13
        "Function_14_2DF4",        # 0E, 14
        "Function_15_2DF8",        # 0F, 15
        "Function_16_308C",        # 10, 16
        "Function_17_32F1",        # 11, 17
        "Function_18_3384",        # 12, 18
        "Function_19_341C",        # 13, 19
        "Function_20_34AC",        # 14, 20
        "Function_21_352A",        # 15, 21
        "Function_22_375B",        # 16, 22
        "Function_23_37E6",        # 17, 23
        "Function_24_3B29",        # 18, 24
        "Function_25_3BBD",        # 19, 25
        "Function_26_3C39",        # 1A, 26
        "Function_27_3EA1",        # 1B, 27
        "Function_28_4053",        # 1C, 28
        "Function_29_49C2",        # 1D, 29
        "Function_30_51CF",        # 1E, 30
        "Function_31_525F",        # 1F, 31
        "Function_32_5278",        # 20, 32
        "Function_33_5A42",        # 21, 33
        "Function_34_686D",        # 22, 34
        "Function_35_693E",        # 23, 35
        "Function_36_6A80",        # 24, 36
        "Function_37_76CA",        # 25, 37
        "Function_38_7710",        # 26, 38
        "Function_39_7756",        # 27, 39
        "Function_40_77D4",        # 28, 40
        "Function_41_7836",        # 29, 41
        "Function_42_786E",        # 2A, 42
        "Function_43_78A6",        # 2B, 43
        "Function_44_792E",        # 2C, 44
        "Function_45_7966",        # 2D, 45
        "Function_46_79A2",        # 2E, 46
        "Function_47_79DE",        # 2F, 47
        "Function_48_7A1A",        # 30, 48
        "Function_49_7A54",        # 31, 49
        "Function_50_7A96",        # 32, 50
        "Function_51_7AE4",        # 33, 51
        "Function_52_9FD1",        # 34, 52
        "Function_53_9FE8",        # 35, 53
        "Function_54_9FFF",        # 36, 54
        "Function_55_A016",        # 37, 55
        "Function_56_A02D",        # 38, 56
        "Function_57_A047",        # 39, 57
        "Function_58_A0A7",        # 3A, 58
        "Function_59_A0E6",        # 3B, 59
        "Function_60_A13E",        # 3C, 60
        "Function_61_A1A0",        # 3D, 61
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FF")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x44, 1)"), scpexpr(EXPR_END)), "loc_2188")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_21FA")

    label("loc_2188")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x44),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x44),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_21FA")

    Jump("loc_2244")

    label("loc_21FF")

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

    label("loc_2244")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_20FF end

    def Function_8_2250(): pass

    label("Function_8_2250")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2350")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_22D9")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_234B")

    label("loc_22D9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_234B")

    Jump("loc_2395")

    label("loc_2350")

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

    label("loc_2395")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_2250 end

    def Function_9_23A1(): pass

    label("Function_9_23A1")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D1")
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
            "#56I地のセピス×４０\x01\x07\x02",

            "#57I水のセピス×４０\x01\x07\x02",

            "#58I火のセピス×４０\x01\x07\x02",

            "#59I風のセピス×４０\x01\x07\x02",

            "#60I時のセピス×４０\x01\x07\x02",

            "#61I空のセピス×４０\x01\x07\x02",

            "#62I幻のセピス×４０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E2, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_24F6")

    label("loc_24D1")


    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_24F6")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_23A1 end

    def Function_10_2508(): pass

    label("Function_10_2508")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D9")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2607")
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x22, 0x0, 0)
    OP_98(0x22, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2565():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2565)

    def lambda_257F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_257F)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_25E8"),
        (2, "loc_25F7"),
        (1, "loc_2604"),
        (SWITCH_DEFAULT, "loc_2607"),
    )


    label("loc_25E8")

    SetScenarioFlags(0x216, 1)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_2607")

    label("loc_25F7")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2604")

    OP_B9(0x0)
    Return()

    label("loc_2607")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x68, 1)"), scpexpr(EXPR_END)), "loc_2664")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_26D4")

    label("loc_2664")

    FadeToDark(300, 0, 100)

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_26D4")

    Jump("loc_2713")

    label("loc_26D9")

    FadeToDark(300, 0, 100)

    #A0012
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

    label("loc_2713")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_2508 end

    def Function_11_271F(): pass

    label("Function_11_271F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28D7")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_28B8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B3")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_28B0")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_27D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_27D9)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_E88", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1E, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28AB")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2892")
    Call(1, 5)
    Jump("loc_28AB")

    label("loc_2892")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_28A8")
    Call(1, 4)
    Jump("loc_28AB")

    label("loc_28A8")

    Call(1, 3)

    label("loc_28AB")

    Jump("loc_28B3")

    label("loc_28B0")

    Call(1, 1)

    label("loc_28B3")

    Jump("loc_28CE")

    label("loc_28B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_28CE")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_28CE")

    TalkEnd(0xFF)
    Return()

    label("loc_28D7")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_2A62")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A5D")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_2A5A")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2983():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_2983)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_ECC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x20, 0x80)
    ClearChrFlags(0x20, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A55")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A3C")
    Call(1, 5)
    Jump("loc_2A55")

    label("loc_2A3C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A52")
    Call(1, 4)
    Jump("loc_2A55")

    label("loc_2A52")

    Call(1, 3)

    label("loc_2A55")

    Jump("loc_2A5D")

    label("loc_2A5A")

    Call(1, 1)

    label("loc_2A5D")

    Jump("loc_2A78")

    label("loc_2A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_2A78")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2A78")

    TalkEnd(0xFF)
    Return()

    # Function_11_271F end

    def Function_12_2A7D(): pass

    label("Function_12_2A7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C35")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_END)), "loc_2C16")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0017
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C11")
    ClearScenarioFlags(0x3A, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2C0E")
    ClearScenarioFlags(0x38, 3)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2B37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_2B37)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_E88", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1F, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C09")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2BF0")
    Call(1, 5)
    Jump("loc_2C09")

    label("loc_2BF0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2C06")
    Call(1, 4)
    Jump("loc_2C09")

    label("loc_2C06")

    Call(1, 3)

    label("loc_2C09")

    Jump("loc_2C11")

    label("loc_2C0E")

    Call(1, 1)

    label("loc_2C11")

    Jump("loc_2C2C")

    label("loc_2C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2C2C")
    ClearScenarioFlags(0x38, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2C2C")

    TalkEnd(0xFF)
    Return()

    label("loc_2C35")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_END)), "loc_2DC0")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0019
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DBB")
    ClearScenarioFlags(0x3A, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2DB8")
    ClearScenarioFlags(0x38, 3)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2CE1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_2CE1)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_ECC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x21, 0x80)
    ClearChrFlags(0x21, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB3")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2D9A")
    Call(1, 5)
    Jump("loc_2DB3")

    label("loc_2D9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2DB0")
    Call(1, 4)
    Jump("loc_2DB3")

    label("loc_2DB0")

    Call(1, 3)

    label("loc_2DB3")

    Jump("loc_2DBB")

    label("loc_2DB8")

    Call(1, 1)

    label("loc_2DBB")

    Jump("loc_2DD6")

    label("loc_2DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2DD6")
    ClearScenarioFlags(0x38, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2DD6")

    TalkEnd(0xFF)
    Return()

    # Function_12_2A7D end

    def Function_13_2DDB(): pass

    label("Function_13_2DDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2DF3")
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)

    label("loc_2DF3")

    Return()

    # Function_13_2DDB end

    def Function_14_2DF4(): pass

    label("Function_14_2DF4")

    Call(1, 6)
    Return()

    # Function_14_2DF4 end

    def Function_15_2DF8(): pass

    label("Function_15_2DF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_2F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F02")

    #C0021
    ChrTalk(
        0xFE,
        (
            "な、なんなんだ、\x01",
            "今の不気味な声は！？\x02\x03",

            "まるで地獄からの\x01",
            "呼び声みたいな……！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00003F落ち着いてくれ、フランツ。\x02\x03",

            "#00001F今から俺たちが調べてくる。\x01",
            "ここはよろしく頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "あ、ああ……分かった。\x01",
            "ロイド、気をつけてくれよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F54")

    label("loc_2F02")


    #C0024
    ChrTalk(
        0xFE,
        (
            "な、何だったんだ、\x01",
            "今の不気味な声は……\x02\x03",

            "お前たち、\x01",
            "十分に気をつけてくれよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F54")

    Jump("loc_3088")

    label("loc_2F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_3088")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3026")

    #C0025
    ChrTalk(
        0xFE,
        (
            "列車は見事なまでに\x01",
            "脱線しちゃってるみたいだ。\x02\x03",

            "死者が出なかったのは幸いだけど\x01",
            "ありゃあ、復旧までに\x01",
            "ちょっと掛かりそうだなぁ。\x02\x03",

            "お前たちも捜査するなら、\x01",
            "がんばってくれよな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3088")

    label("loc_3026")


    #C0026
    ChrTalk(
        0xFE,
        (
            "列車は見事なまでに\x01",
            "脱線しちゃってるみたいだ。\x02\x03",

            "お前たちも捜査するなら、\x01",
            "がんばってくれよな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3088")

    TalkEnd(0xFE)
    Return()

    # Function_15_2DF8 end

    def Function_16_308C(): pass

    label("Function_16_308C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_31E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315C")

    #C0027
    ChrTalk(
        0xFE,
        (
            "ランディ先輩、ノエルさん。\x01",
            "い、今聞こえた叫び声は……？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#00301F分からねえが……\x01",
            "気をつけた方がよさそうだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        "#10101F警戒をお願いします！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "はっ、了解しました！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31DC")

    label("loc_315C")


    #C0031
    ChrTalk(
        0xFE,
        (
            "先ほどの叫び声が何であれ、\x01",
            "復旧作業を急ぐこの現場に\x01",
            "横槍を入れさせる訳には行きません。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "こちらの警戒はお任せください！\x02",
    )

    CloseMessageWindow()

    label("loc_31DC")

    Jump("loc_32ED")

    label("loc_31E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_32ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328C")

    #C0033
    ChrTalk(
        0xFE,
        (
            "列車事故の現場は、\x01",
            "ここを降りてすぐです。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "すでにソーニャ司令たちと\x01",
            "警察の方が検証に入っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "皆さん、どうぞお通りください。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32ED")

    label("loc_328C")


    #C0036
    ChrTalk(
        0xFE,
        (
            "すでにソーニャ司令たちと\x01",
            "警察の方が検証に入っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "皆さん、どうぞお通りください。\x02",
    )

    CloseMessageWindow()

    label("loc_32ED")

    TalkEnd(0xFE)
    Return()

    # Function_16_308C end

    def Function_17_32F1(): pass

    label("Function_17_32F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_3380")

    #C0038
    ChrTalk(
        0xFE,
        (
            "先ほど入ったマスコミの人が、\x01",
            "復旧作業の邪魔を\x01",
            "しなければいいんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "まあ、そのあたりは\x01",
            "弁えている人なんでしょうがね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3380")

    TalkEnd(0xFE)
    Return()

    # Function_17_32F1 end

    def Function_18_3384(): pass

    label("Function_18_3384")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_3418")

    #C0040
    ChrTalk(
        0xFE,
        (
            "警備隊と協力して\x01",
            "作業に当たるってのも\x01",
            "なかなか珍しいよなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "現場はひどい有様だし……\x01",
            "俺たち警察もできることを\x01",
            "やらないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3418")

    TalkEnd(0xFE)
    Return()

    # Function_18_3384 end

    def Function_19_341C(): pass

    label("Function_19_341C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_34A8")

    #C0042
    ChrTalk(
        0xFE,
        (
            "警察からは捜査二課の人たちが\x01",
            "原因の調査に駆り出されたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "だが、今のところは明確なことは\x01",
            "判明していないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A8")

    TalkEnd(0xFE)
    Return()

    # Function_19_341C end

    def Function_20_34AC(): pass

    label("Function_20_34AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_3526")

    #C0044
    ChrTalk(
        0xFE,
        (
            "現場ではソーニャ司令が\x01",
            "復旧の指揮に当たっているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "調査に入るつもりなら、\x01",
            "一言挨拶しておくんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3526")

    TalkEnd(0xFE)
    Return()

    # Function_20_34AC end

    def Function_21_352A(): pass

    label("Function_21_352A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_36E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3632")

    #C0046
    ChrTalk(
        0xFE,
        (
            "こちら西クロスベル街道……\x01",
            "先ほど、正体不明の存在の\x01",
            "雄叫びを確認した。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "ソーニャ司令の指示により、\x01",
            "我々は鉄道の復旧作業を優先する。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "ただし、重機の移送を出来る限り\x01",
            "急がせるようにとのこと。\x01",
            "繰り返す、重機の移送を……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_36DC")

    label("loc_3632")


    #C0049
    ChrTalk(
        0xFE,
        (
            "そちらは君たちに任せる。\x01",
            "我々はソーニャ司令とともに\x01",
            "鉄道の復旧作業を優先しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "迅速に終われば応援に\x01",
            "駆けつけることも可能だろう。\x01",
            "それまではよろしく頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36DC")

    Jump("loc_3757")

    label("loc_36E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_3757")

    #C0051
    ChrTalk(
        0xFE,
        (
            "国境の緊張状態が続くこの状況で、\x01",
            "厄介な事故が起こってしまったものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "……本当に偶然なのだろうか。\x02",
    )

    CloseMessageWindow()

    label("loc_3757")

    TalkEnd(0xFE)
    Return()

    # Function_21_352A end

    def Function_22_375B(): pass

    label("Function_22_375B")

    EventBegin(0x1)

    #C0053
    ChrTalk(
        0x101,
        (
            "#00003F鉄道の復旧作業は一旦、\x01",
            "ソーニャ司令たちに任せよう。\x02\x03",

            "#00001F俺たちは、あの謎の咆哮の\x01",
            "正体を確かめるぞ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -64870, -8000, 77770, 180)
    EventEnd(0x4)
    Return()

    # Function_22_375B end

    def Function_23_37E6(): pass

    label("Function_23_37E6")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3818")
    SetScenarioFlags(0x31, 2)

    label("loc_3818")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_385E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_3858")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_384D")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_3853")

    label("loc_384D")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_3853")

    Jump("loc_385E")

    label("loc_3858")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_385E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_38D7")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_38B7"),
        (SWITCH_DEFAULT, "loc_38C8"),
    )


    label("loc_38B7")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_38D2")

    label("loc_38C8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38D2")

    Jump("loc_3B16")

    label("loc_38D7")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_390B")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_390B")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_393F"),
        (1, "loc_3A43"),
        (2, "loc_3AD4"),
        (SWITCH_DEFAULT, "loc_3B0C"),
    )


    label("loc_393F")

    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3970")
    OP_70(0x4, 0x12C)
    OP_71(0x4, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_3980")

    label("loc_3970")

    OP_70(0x4, 0xF0)
    OP_71(0x4, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_3980")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39D6")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F9")
    Sound(461, 0, 100, 0)

    label("loc_39F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A19")
    OP_70(0x4, 0x14A)
    OP_71(0x4, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_3A29")

    label("loc_3A19")

    OP_70(0x4, 0x10E)
    OP_71(0x4, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_3A29")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x4, "light", 0x1, 0x1)
    OP_70(0x4, 0x0)
    Jump("loc_385E")

    label("loc_3A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3AB5")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_3A78")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_3A90")

    label("loc_3A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3A8B")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_3A90")

    label("loc_3A8B")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_3A90")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3ACF")

    label("loc_3AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3AC5")
    OP_AF(0xFB)
    Jump("loc_3ACF")

    label("loc_3AC5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3ACF")

    Jump("loc_3B16")

    label("loc_3AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AED")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B07")

    label("loc_3AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3AFD")
    OP_AF(0xFB)
    Jump("loc_3B07")

    label("loc_3AFD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B07")

    Jump("loc_3B16")

    label("loc_3B0C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B16")

    Jump("loc_385E")

    label("loc_3B1B")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_23_37E6 end

    def Function_24_3B29(): pass

    label("Function_24_3B29")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_3B84")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B79")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_3B7F")

    label("loc_3B79")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_3B7F")

    Jump("loc_3BA8")

    label("loc_3B84")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BA2")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_3BA8")

    label("loc_3BA2")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_3BA8")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_24_3B29 end

    def Function_25_3BBD(): pass

    label("Function_25_3BBD")

    Battle("BattleInfo_F54", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C04")
    OP_90(0x0, -7830, 0, -50540, 270)
    EventEnd(0x5)
    SetChrFlags(0x23, 0x8000)
    Jump("loc_3C38")

    label("loc_3C04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C17")
    Jump("loc_3C38")

    label("loc_3C17")

    ModifyEventFlags(0, 2, 0x80)
    SetMapObjFlags(0x7, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 1)
    EventEnd(0x5)

    label("loc_3C38")

    Return()

    # Function_25_3BBD end

    def Function_26_3C39(): pass

    label("Function_26_3C39")

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
        "#00001Fクロスベル市には《結界》か……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#00206Fこればかりは、今のところ\x01",
            "どうしようもありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#10400F#6Pまあ、入る方法も\x01",
            "見つかってないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#00301Fああ、他のルートを\x01",
            "探した方が賢明だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x106,
        (
            "#10703F#6P国防軍の巡回地点でも\x01",
            "あると思いますし、\x01",
            "長居はしない方がよさそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        "#00003Fああ、そうだな……\x02",
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

    # Function_26_3C39 end

    def Function_27_3EA1(): pass

    label("Function_27_3EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4052")
    OP_29(0xAF, 0x1, 0xF)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)
    Sleep(500)

    #C0060
    ChrTalk(
        0x101,
        (
            "#00008Fとはいえ、一通り回ったけど\x01",
            "今の所は八方ふさがりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#00306Fクロスベル市はもちろん、\x01",
            "ベルガード門にも警察学校方面にも\x01",
            "行けなさそうだしなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x106,
        "#10706F#6P困りましたね……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        (
            "#10400F#6Pふむ、他に行けそうな場所は\x01",
            "なかったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x107,
        (
            "#01200F#3C#12P多少、街道から外れて探してみた方が\x01",
            "いいのかもしれぬな。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#00203Fそうですね……\x01",
            "もう少し探してみましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4052")

    Return()

    # Function_27_3EA1 end

    def Function_28_4053(): pass

    label("Function_28_4053")

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

    def lambda_413C():
        OP_95(0xFE, -40880, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_413C)
    Sleep(30)

    def lambda_4159():
        OP_95(0xFE, -39220, 0, -870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4159)
    Sleep(30)

    def lambda_4176():
        OP_95(0xFE, -39980, 0, -3050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4176)
    Sleep(30)

    def lambda_4193():
        OP_95(0xFE, -39250, 0, -2040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4193)
    Sleep(30)

    def lambda_41B0():
        OP_95(0xFE, -37720, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41B0)
    Sleep(30)

    def lambda_41CD():
        OP_95(0xFE, -38260, 0, -4090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_41CD)
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
        "#00001F#12P#Nあれは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0067
    ChrTalk(
        0x105,
        (
            "#10300F#12P#Nどうやらあそこが\x01",
            "事故現場みたいだね。\x02",
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

    def lambda_4391():
        OP_95(0xFE, -47650, 0, 9020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4391)
    Sleep(30)

    def lambda_43AE():
        OP_95(0xFE, -47010, 0, 7770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43AE)
    Sleep(30)

    def lambda_43CB():
        OP_95(0xFE, -48180, 0, 7820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43CB)
    Sleep(30)

    def lambda_43E8():
        OP_95(0xFE, -46030, 0, 6660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43E8)
    Sleep(30)

    def lambda_4405():
        OP_95(0xFE, -47520, 0, 6250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4405)
    Sleep(30)

    def lambda_4422():
        OP_95(0xFE, -48770, 0, 6320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4422)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4469():

        label("loc_4469")

        TurnDirection(0x8, 0x101, 500)
        Yield()
        Jump("loc_4469")

    QueueWorkItem2(0x8, 2, lambda_4469)

    def lambda_447B():

        label("loc_447B")

        TurnDirection(0x9, 0x101, 500)
        Yield()
        Jump("loc_447B")

    QueueWorkItem2(0x9, 2, lambda_447B)
    WaitChrThread(0x101, 1)

    def lambda_4491():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4491)
    WaitChrThread(0x102, 1)

    def lambda_44A2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_44A2)
    WaitChrThread(0x103, 1)

    def lambda_44B3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_44B3)
    WaitChrThread(0x104, 1)

    def lambda_44C4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_44C4)
    WaitChrThread(0x109, 1)

    def lambda_44D5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_44D5)
    WaitChrThread(0x105, 1)

    def lambda_44E6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_44E6)
    WaitChrThread(0x101, 2)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    #C0068
    ChrTalk(
        0x8,
        "#5Pやあ、ロイドたちか。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#00000F#12Pフランツ、お疲れ。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "#5Pランディ先輩、ノエルさんも。\x01",
            "お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x109,
        "#10100F#12Pそちらこそお疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        (
            "#00301F#12Pどうやら事故現場ってのは\x01",
            "その先で間違いないみてぇだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "#5Pはい、既にソーニャ司令と\x01",
            "警察の方が検証に入っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "#5P二課のドノバン警部と\x01",
            "レイモンドさんが来てるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "#5Pしかしまあ、見事なまでに\x01",
            "脱線しちゃってるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "#5Pありゃあ、復旧までに\x01",
            "ちょっと掛かりそうだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#00108F#12Pその……\x01",
            "乗客の人たちの被害は？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#5P幸い、死者は出なかったようですが\x01",
            "何人か重傷者が出たみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "#5P治療の必要がありそうな方は\x01",
            "先ほど救急車で搬送されました。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#00006F#12Pああ、さっき見たよ。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        "#00208F#12P他の乗客は、一通りバスで？\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "#5Pああ、市内に行くのと\x01",
            "アルタイル市まで行くのの\x01",
            "２手に分かれるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        "#5Pさっきまで大混乱だったよ。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        "#00206F#12P……無理もないかと。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x105,
        (
            "#10306F#12Pやれやれ。\x01",
            "厄介な事故が起きたもんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00003F#12Pとにかく俺たちも\x01",
            "事故現場を見てみよう。\x02\x03",

            "#00000F通してもらってもいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "#5Pああ、お前たちなら\x01",
            "誰も文句は言わないだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        "#5Pどうぞお通りください！\x02",
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

    # Function_28_4053 end

    def Function_29_49C2(): pass

    label("Function_29_49C2")

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

    def lambda_4CA0():
        OP_95(0xFE, -45600, 0, 4870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4CA0)

    def lambda_4CBA():
        OP_95(0xFE, -46440, 0, 4150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4CBA)
    WaitChrThread(0x8, 1)

    def lambda_4CD8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4CD8)
    WaitChrThread(0x9, 1)

    def lambda_4CE9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4CE9)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)

    #C0089
    ChrTalk(
        0x8,
        "#5Pやあ、ロイドたちか。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#00000F#11Pフランツ、お疲れ。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "#6Pランディ先輩、ノエルさんも。\x01",
            "お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        "#10100F#11Pそちらこそお疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x104,
        (
            "#00301F#11Pどうやら事故現場ってのは\x01",
            "その先で間違いないみてぇだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "#6Pはい、既にソーニャ司令と\x01",
            "警察の方が検証に入っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "#5P二課のドノバン警部と\x01",
            "レイモンドさんが来てるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "#5Pしかしまあ、見事なまでに\x01",
            "脱線しちゃってるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "#5Pありゃあ、復旧までに\x01",
            "ちょっと掛かりそうだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00108F#11Pその……\x01",
            "乗客の人たちの被害は？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "#6P幸い、死者は出なかったようですが\x01",
            "何人か重傷者が出たみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "#6P治療の必要がありそうな方は\x01",
            "先ほど救急車で搬送されました。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#00006F#11Pああ、さっき見たよ。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        "#00208F#11P他の乗客は、一通りバスで？\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#5Pああ、市内に行くのと\x01",
            "アルタイル市まで行くのの\x01",
            "２手に分かれるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        "#5Pさっきまで大混乱だったよ。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x103,
        "#00206F#11P……無理もないかと。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x105,
        (
            "#10306F#11Pやれやれ。\x01",
            "厄介な事故が起きたもんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00003F#11Pとにかく俺たちも\x01",
            "事故現場を見てみよう。\x02\x03",

            "#00000F通してもらってもいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "#5Pああ、お前たちなら\x01",
            "誰も文句は言わないだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        "#6Pどうぞお通りください！\x02",
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

    # Function_29_49C2 end

    def Function_30_51CF(): pass

    label("Function_30_51CF")

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

    # Function_30_51CF end

    def Function_31_525F(): pass

    label("Function_31_525F")

    Sound(458, 0, 100, 0)
    Sleep(3000)
    Sound(459, 0, 100, 0)
    Sleep(3000)
    Sound(492, 0, 70, 0)
    Return()

    # Function_31_525F end

    def Function_32_5278(): pass

    label("Function_32_5278")

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

    def lambda_5395():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5395)
    Sleep(50)

    def lambda_53AD():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_53AD)

    def lambda_53C2():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53C2)
    Sleep(50)

    def lambda_53DA():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_53DA)

    def lambda_53EF():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_53EF)
    Sleep(50)

    def lambda_5407():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5407)

    def lambda_541C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_541C)
    Sleep(50)
    FadeToBright(1000, 0)
    OP_68(-63640, -7200, 68080, 3500)

    def lambda_544E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_544E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    def lambda_547B():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_547B)
    Sleep(50)

    def lambda_548B():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_548B)
    Sleep(50)

    def lambda_549B():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_549B)
    Sleep(50)

    def lambda_54AB():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_54AB)
    Sleep(50)

    def lambda_54BB():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_54BB)
    Sleep(50)

    def lambda_54CB():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_54CB)
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
        "#00006F#12Pグレイスさん……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#00101F#6Pさすがに付いて来るとか\x01",
            "言いませんよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xF,
        (
            "#02106F#5Pえ～、いいじゃないって\x01",
            "言いたいところだけど。\x02\x03",

            "#02100Fさすがに危険そうだし\x01",
            "ここは我慢しておくわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x10,
        (
            "#5Pいったんクロスベル市に戻って\x01",
            "速報をまとめるつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x10,
        (
            "#5P他の記者が集まり次第、\x01",
            "すぐにでも取材を再開しますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        "#00200F#12Pそれが無難かと。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x104,
        (
            "#00303F#12Pま、さすがに襲われても\x01",
            "フォローしきれねぇしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xF,
        (
            "#02103F#5Pどんな魔獣か知らないけど\x01",
            "本当に列車を脱線させたのなら\x01",
            "尋常な相手じゃないわ……\x02\x03",

            "#02101Fくれぐれも気をつけて！\x01",
            "後でネタを提供してちょうだい！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#00000F#12P了解しました！\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x109,
        "#10100F#12Pお疲れ様です！\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x87, 0x1F4)
    OP_68(-61720, -7200, 67040, 4000)
    MoveCamera(54, 18, 0, 4000)
    OP_6E(510, 4000)

    def lambda_57A9():

        label("loc_57A9")

        TurnDirection(0xFE, 0xF, 150)
        Yield()
        Jump("loc_57A9")

    QueueWorkItem2(0x101, 2, lambda_57A9)

    def lambda_57BB():

        label("loc_57BB")

        TurnDirection(0xFE, 0xF, 100)
        Yield()
        Jump("loc_57BB")

    QueueWorkItem2(0x102, 2, lambda_57BB)

    def lambda_57CD():

        label("loc_57CD")

        TurnDirection(0xFE, 0xF, 200)
        Yield()
        Jump("loc_57CD")

    QueueWorkItem2(0x103, 2, lambda_57CD)

    def lambda_57DF():

        label("loc_57DF")

        TurnDirection(0xFE, 0xF, 150)
        Yield()
        Jump("loc_57DF")

    QueueWorkItem2(0x104, 2, lambda_57DF)

    def lambda_57F1():

        label("loc_57F1")

        TurnDirection(0xFE, 0xF, 100)
        Yield()
        Jump("loc_57F1")

    QueueWorkItem2(0x109, 2, lambda_57F1)

    def lambda_5803():

        label("loc_5803")

        TurnDirection(0xFE, 0xF, 200)
        Yield()
        Jump("loc_5803")

    QueueWorkItem2(0x105, 2, lambda_5803)

    def lambda_5815():
        OP_95(0xFE, -55190, -8000, 61950, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5815)
    Sleep(800)
    OP_93(0x10, 0x87, 0x1F4)

    def lambda_5839():
        OP_95(0xFE, -54530, -8000, 62580, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5839)
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

    def lambda_58B0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_58B0)

    def lambda_58BD():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_58BD)
    Sleep(50)

    def lambda_58CD():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_58CD)
    Sleep(50)

    def lambda_58DD():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_58DD)
    Sleep(50)

    def lambda_58ED():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_58ED)
    Sleep(50)

    def lambda_58FD():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_58FD)
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
            "#00003F#12P──よし、追跡を始めよう。\x02\x03",

            "#00013Fまずは街道をまっすぐ\x01",
            "西の方に向かうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x105,
        "#10301F#5Pｊａ#4Rヤ ー#。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x104,
        "#00307F#5P何としても捕まえねぇとな！\x02",
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

    # Function_32_5278 end

    def Function_33_5A42(): pass

    label("Function_33_5A42")

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

    def lambda_5B11():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B11)
    Sleep(50)

    def lambda_5B29():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5B29)
    Sleep(50)

    def lambda_5B41():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B41)
    Sleep(50)

    def lambda_5B59():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B59)
    Sleep(50)

    def lambda_5B71():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5B71)
    Sleep(50)

    def lambda_5B89():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B89)
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
            "#00205F#6Pそういえば、脱線事故の車輌は\x01",
            "完全に撤去されたんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#00000F#11Pああ、破片とかの類いも\x01",
            "一通り片付けられたはずさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        (
            "#00306F#12Pしっかし、あの事故も\x01",
            "かなり大事#4Rおおごと#だったハズだが……\x02\x03",

            "#00301F強烈な事ばかり起きたせいか、\x01",
            "イマイチ印象が薄いよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x105,
        "#10403F#6P……確かにね。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x106,
        (
            "#10703F#12P大陸横断鉄道も現在は\x01",
            "完全に運行を休止しています。\x02\x03",

            "#10708Fたまに国防軍の貨物列車が\x01",
            "通るくらいみたいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        "#00301F#12Pなるほどな。\x02",
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
            "#00005F#5P……待てよ。\x02\x03",

            "#00013Fという事は、線路に出て\x01",
            "行き来できるかもしれない……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrFlags(0x107, 0x20)

    def lambda_5ECB():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5ECB)
    Sleep(50)

    def lambda_5EDB():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5EDB)
    Sleep(50)

    def lambda_5EEB():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5EEB)
    Sleep(50)

    def lambda_5EFB():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5EFB)
    Sleep(50)

    def lambda_5F0B():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_5F0B)
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
        "#10712F#11Pあ……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x105,
        (
            "#10402F#6Pなるほど……\x01",
            "その手があったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x107,
        (
            "#01203F#3C#11Pだが、クロスベル市方面は\x01",
            "《結界》に包まれている状態だ。\x02\x03",

            "#01201F気付かれずに\x01",
            "都市に入るのは不可能だぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#00004F#5Pああ……判っている。\x02\x03",

            "#00000Fだが、西の方ならどうだ？\x02",
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
        "#00205F#6Pロイドさん、もしかして……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        (
            "#00307F#12P線路からベルガード門に\x01",
            "潜入するつもりかよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00006F#5P……ああ、考えたんだけど。\x02\x03",

            "#00001F一度、ソーニャ司令と\x01",
            "直接話せないかと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        "#00301F#12Pむう……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#00206F#6P確かに味方になってもらえたら\x01",
            "この上なく頼もしい人ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x105,
        (
            "#10408F#6Pでも、国防軍への移行については\x01",
            "反対はしなかったんだよね？\x02\x03",

            "#10401Fさすがにリスクが高そうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x106,
        "#10706F#11P……私も同感です。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#00003F#5P勿論、立場もあるだろうから\x01",
            "正面から訪ねても捕まるだけだろう。\x02\x03",

            "#00008Fだが、何とか門に潜入して\x01",
            "秘密裏にコンタクトが取れれば……\x02\x03",

            "#00001Fひょっとしたら本音を\x01",
            "語ってくれるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        "#00200F#6Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x104,
        (
            "#00303F#12P……ミレイユたちを見ても\x01",
            "国防軍内で疑問を持ってる人間が\x01",
            "少なくないのは確かだろう。\x02\x03",

            "#00300Fあれだけ正義感が強い人なら\x01",
            "尚更かもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x105,
        (
            "#10406F#6Pうーん、そういう事なら\x01",
            "僕も反対はしないけど……\x02\x03",

            "#10401Fソーニャ司令がいるとしたら\x01",
            "“彼女”もいるんじゃないの？\x02",
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

    def lambda_64C9():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_64C9)
    Sleep(50)

    def lambda_64D9():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_64D9)
    Sleep(50)

    def lambda_64E9():
        TurnDirection(0x106, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_64E9)
    Sleep(50)

    def lambda_64F9():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_64F9)
    Sleep(50)

    def lambda_6509():
        TurnDirection(0x107, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_6509)
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
        "#00201F#5Pあ……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x104,
        "#00306F#11P……それがあったか。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x106,
        "#10708F#11Pノエルさん……ですね。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x107,
        (
            "#01200F#3C#11Pふむ、話を聞く限り\x01",
            "彼女の決意は固そうだが？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#00008F#5P……判ってる。\x02\x03",

            "#00006Fだが、俺たちの進む道が\x01",
            "恐ろしく困難なのは確かだ。\x02\x03",

            "#00003F彼女との行き違いにしても……\x01",
            "いずれ乗り越える必要がある。\x02\x03",

            "#00013F──それが直接、\x01",
            "やり合う形になったとしても。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x107, 0x20)

    def lambda_66A8():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_66A8)
    Sleep(50)

    def lambda_66B8():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_66B8)
    Sleep(50)

    def lambda_66C8():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_66C8)
    Sleep(50)

    def lambda_66D8():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_66D8)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    ClearChrFlags(0x107, 0x20)

    #C0150
    ChrTalk(
        0x103,
        "#00208F#6Pロイドさん……\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#00301F#12P……確かに。\x01",
            "避けてばかりはいられねぇか。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x105,
        (
            "#10404F#6Pフフ、そこまで考えてるなら\x01",
            "これ以上は言わないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x106,
        (
            "#10710F#11Pとりあえず、フェンスを外して\x01",
            "線路に出られるようにしましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0154
    ChrTalk(
        0x101,
        "#00000F#5Pああ……！\x02",
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

    # Function_33_5A42 end

    def Function_34_686D(): pass

    label("Function_34_686D")

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

    # Function_34_686D end

    def Function_35_693E(): pass

    label("Function_35_693E")

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

    # Function_35_693E end

    def Function_36_6A80(): pass

    label("Function_36_6A80")

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
        "レジー",
        (
            "#6A#40Wあ、あれ……\x01",
            "ブ、ブレーキがきかねえ！？\x02",
        )
    )
    #Auto

    Sleep(1500)

    #N0156
    NpcTalk(
        0x12,
        "サイクス・ユーリ",
        "#6A#40Wな、なにいい！？\x02",
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
        "ロイド",
        (
            "#00005F何かトラブルが\x01",
            "あったらしい……！\x02\x03",

            "#00003F（どうする！？\x01",
            "  このままじゃ大事故に\x01",
            "  なるかもしれない……！）\x02",
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
            "#1K緊急ナビ\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "前に回りこんで止める\x01",        # 0
            "後ろからぶつけて止める\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E23")
    SetScenarioFlags(0x178, 6)

    #N0159
    NpcTalk(
        0x11,
        "ロイド",
        (
            "#00007Fノエル！\x01",
            "スピードを上げて回り込むんだ！\x02\x03",

            "#00003F多少危険だけど……\x01",
            "車体を壁にして止めよう！\x02",
        )
    )

    CloseMessageWindow()

    #N0160
    NpcTalk(
        0x11,
        "ノエル",
        "#10107F……了解！\x02",
    )

    CloseMessageWindow()
    OP_29(0x8B, 0x1, 0x6)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_6ECF")

    label("loc_6E23")


    #N0161
    NpcTalk(
        0x11,
        "ロイド",
        (
            "#00007Fノエル！\x01",
            "スピードを上げて\x01",
            "後ろからぶつけるんだ！\x02\x03",

            "#00003Fあの池に落とせば、\x01",
            "被害を最小限にできるかも……！\x02",
        )
    )

    CloseMessageWindow()

    #N0162
    NpcTalk(
        0x11,
        "ノエル",
        "#10107F……了解！\x02",
    )

    CloseMessageWindow()
    OP_29(0x8B, 0x1, 0x7)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 6)), scpexpr(EXPR_END)), "loc_6FDB")
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
        "ユーリ・サイクス・レジー",
        "#5S#8A#30Wうわあああああ～～～！！\x02",
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
    Jump("loc_70FE")

    label("loc_6FDB")

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
        "ユーリ・サイクス・レジー",
        "#5S#8A#30Wうわあああああ～～～！！\x02",
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

    label("loc_70FE")

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

    def lambda_720A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_720A)

    def lambda_721B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_721B)

    def lambda_722C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_722C)
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
        "はあっ、はあっ……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x19,
        "た、助かったのか……？\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x1A,
        "し、死ぬかと思った……\x02",
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
            "#00106Fふぅ……\x01",
            "なんとか無事みたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 6)), scpexpr(EXPR_END)), "loc_7521")
    OP_2C(0x8B, 0x1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0169
    ChrTalk(
        0x101,
        (
            "#00006Fお、俺が前に回りこませた\x01",
            "せいかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x109,
        (
            "#10101Fい、いえ。\x01",
            "事故になって大惨事になるより\x01",
            "絶対に良かったはずですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            "#00203Fそもそもハンドルを切ったのは\x01",
            "彼らですし、自業自得かと。\x02\x03",

            "#00200Fまあ、おかげでわたしたちの車が\x01",
            "傷つかずにすみましたけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75E9")

    label("loc_7521")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0172
    ChrTalk(
        0x101,
        (
            "#00003Fう、うーん……\x01",
            "さすがにブツけるのは\x01",
            "やりすぎだったかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x109,
        (
            "#10106Fそ、そうですね……\x01",
            "強引といえば\x01",
            "強引だったかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        "#00203Fまあ、彼らの自業自得かと。\x02",
    )

    CloseMessageWindow()

    label("loc_75E9")


    #C0175
    ChrTalk(
        0x104,
        (
            "#00309F命が助かっただけでも\x01",
            "儲けモンだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x105,
        "#10304Fフフ、彼らも悪運が強いよねぇ。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#00003Fう～ん……\x02\x03",

            "#00000Fま、まあいいか。\x01",
            "とりあえず、ミレイユ三尉と\x01",
            "広域防犯課に連絡しよう。\x02",
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

    # Function_36_6A80 end

    def Function_37_76CA(): pass

    label("Function_37_76CA")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -134100, -2000, 14320)
    OP_9F(0x1, -108810, -2000, 13590)
    OP_9F(0x1, -100530, -2000, 9110)
    OP_9F(0x1, -85050, -2000, -6880)
    OP_9F(0x2, 0xFE, 15000, 0x6)
    Return()

    # Function_37_76CA end

    def Function_38_7710(): pass

    label("Function_38_7710")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -134100, -2000, 14320)
    OP_9F(0x1, -108810, -2000, 13590)
    OP_9F(0x1, -100530, -2000, 9110)
    OP_9F(0x1, -85050, -2000, -6880)
    OP_9F(0x2, 0xFE, 15000, 0x6)
    Return()

    # Function_38_7710 end

    def Function_39_7756(): pass

    label("Function_39_7756")

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

    # Function_39_7756 end

    def Function_40_77D4(): pass

    label("Function_40_77D4")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -62310, -2000, -10)
    OP_9F(0x1, -51780, 0, 500)
    OP_9F(0x1, -40680, 0, -580)
    OP_9F(0x1, -34230, 0, -8310)
    OP_9F(0x1, -32860, 0, -16350)
    OP_9F(0x1, -29710, 0, -21610)
    OP_9F(0x2, 0xFE, 12000, 0x6)
    Return()

    # Function_40_77D4 end

    def Function_41_7836(): pass

    label("Function_41_7836")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -18370, 0, -31800)
    OP_9F(0x1, -13420, 0, -30030)
    OP_9F(0x1, -9100, 0, -32729)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_41_7836 end

    def Function_42_786E(): pass

    label("Function_42_786E")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -21840, 0, -26500)
    OP_9F(0x1, -13400, 0, -26670)
    OP_9F(0x1, -10840, 0, -29640)
    OP_9F(0x2, 0xFE, 18000, 0x6)
    Return()

    # Function_42_786E end

    def Function_43_78A6(): pass

    label("Function_43_78A6")

    OP_95(0x12, -5160, 0, -36470, 10000, 0x0)
    OP_95(0x12, -3160, 0, -38680, 10000, 0x0)
    OP_95(0x12, -1500, -2000, -40300, 10000, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -1500, -2000, -40300, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_95(0x12, -880, -2000, -42770, 3000, 0x0)
    Return()

    # Function_43_78A6 end

    def Function_44_792E(): pass

    label("Function_44_792E")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -22220, 0, -26340)
    OP_9F(0x1, -8890, 0, -25820)
    OP_9F(0x1, -6490, 0, -28390)
    OP_9F(0x2, 0xFE, 18000, 0x6)
    Return()

    # Function_44_792E end

    def Function_45_7966(): pass

    label("Function_45_7966")


    def lambda_796B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_796B)
    OP_9B(0x1, 0x18, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_95(0x18, -3500, -2000, -42500, 1000, 0x0)
    OP_93(0x18, 0x10E, 0x1F4)
    Return()

    # Function_45_7966 end

    def Function_46_79A2(): pass

    label("Function_46_79A2")


    def lambda_79A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_79A7)
    OP_9B(0x1, 0x19, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_95(0x19, -3500, -2000, -43700, 1000, 0x0)
    OP_93(0x19, 0x10E, 0x1F4)
    Return()

    # Function_46_79A2 end

    def Function_47_79DE(): pass

    label("Function_47_79DE")


    def lambda_79E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_79E3)
    OP_9B(0x1, 0x1A, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_95(0x1A, -3500, -2000, -41300, 1000, 0x0)
    OP_93(0x1A, 0x10E, 0x1F4)
    Return()

    # Function_47_79DE end

    def Function_48_7A1A(): pass

    label("Function_48_7A1A")

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

    # Function_48_7A1A end

    def Function_49_7A54(): pass

    label("Function_49_7A54")

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

    # Function_49_7A54 end

    def Function_50_7A96(): pass

    label("Function_50_7A96")

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

    # Function_50_7A96 end

    def Function_51_7AE4(): pass

    label("Function_51_7AE4")

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
        "#2P住宅街在住、《ハイブラッズ》……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x1B,
        (
            "#2Pスピード違反、その他諸々の容疑で\x01",
            "あなた達を連行させて頂くわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x18,
        "フン。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x19,
        "チッ……\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x1A,
        "ヘ、ヘックション！！\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#00000Fとりあえず、これで一見落着ですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x101, 500)
    Sleep(100)

    #C0184
    ChrTalk(
        0x1C,
        (
            "#07900Fあなた達、ご苦労様。\x01",
            "おかげで暴走車を\x01",
            "捕まえることができたわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1C, 500)
    Sleep(100)

    #C0185
    ChrTalk(
        0x1B,
        (
            "#2Pミレイユ三尉、\x01",
            "ご協力ありがとうございました！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)
    Sleep(100)

    #C0186
    ChrTalk(
        0x1B,
        (
            "#2P国境の緊張状態で\x01",
            "お忙しい時だと思いますが……\x01",
            "感謝させていただきます！\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x1C,
        (
            "#07904Fふふ、それはお互い様です。\x02\x03",

            "#07900Fこちらとしても、警備の不安要素が\x01",
            "一つ減らせたことになりますし……\x02\x03",

            "#07902F支援課にも、改めてお礼を\x01",
            "しなくちゃならないわね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x1C, 500)
    Sleep(100)

    #C0188
    ChrTalk(
        0x104,
        "#00309Fハハ、いいってことよ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)
    Sleep(100)

    #C0189
    ChrTalk(
        0x102,
        (
            "#00105Fところで……\x01",
            "ティオちゃん、ノエルさん。\x01",
            "彼らのクルマの方はどう？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-10450, 600, -37570, 2000)
    MoveCamera(38, 21, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(22020, 2000)

    def lambda_8090():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8090)
    Sleep(50)

    def lambda_80A0():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_80A0)
    Sleep(50)

    def lambda_80B0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80B0)
    Sleep(50)

    def lambda_80C0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_80C0)
    Sleep(50)

    def lambda_80D0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_80D0)
    Sleep(50)

    def lambda_80E0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_80E0)
    Sleep(50)

    def lambda_80F0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_80F0)
    Sleep(50)

    def lambda_8100():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8100)
    Sleep(50)

    def lambda_8110():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8110)
    Sleep(50)

    def lambda_8120():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8120)
    OP_6F(0x79)
    Sleep(500)

    #C0190
    ChrTalk(
        0x109,
        (
            "#10100F一応、ブレーキが壊れた\x01",
            "原因が特定できました。\x02\x03",

            "#10106Fどうやら、単にメンテナンスが\x01",
            "甘かったみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1A, 500)
    Sleep(100)

    #C0191
    ChrTalk(
        0x19,
        (
            "レジー、お前なあ……\x01",
            "メンテは任せてたじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x1A,
        (
            "そういえば最近ちょっと\x01",
            "サボり気味だったかも……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x18, 500)
    Sleep(100)

    #C0193
    ChrTalk(
        0x103,
        (
            "#00200Fあと、導力エンジンが完全に\x01",
            "ショートしているようです。\x02\x03",

            "#00203F修理するとなると、\x01",
            "新品を買うくらいの修理費が\x01",
            "かかってしまうかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x109,
        (
            "#10106Fもったいないけど……\x01",
            "廃車にしてしまう他ないと思います。\x02",
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
        "マ、マジかよ……\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x19,
        (
            "チッ、せっかくユーリが用意した\x01",
            "ヴェルヌの最新型だったのによ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x18,
        (
            "フン、クルマの１台や２台は\x01",
            "俺にとっちゃ安いもんさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x18,
        (
            "オーバルストアあたりで\x01",
            "また調達すればいいだろう。\x02",
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
            "ははっ、さっすがユーリ！\x01",
            "太っ腹だなあ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)
    Sleep(100)

    #C0200
    ChrTalk(
        0x19,
        (
            "んじゃ、さっさと\x01",
            "買いにいくとしようぜ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-8540, 600, -39680, 2000)
    MoveCamera(45, 21, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(21910, 2000)

    def lambda_84C3():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84C3)
    Sleep(50)

    def lambda_84D3():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_84D3)
    Sleep(50)

    def lambda_84E3():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_84E3)
    Sleep(50)

    def lambda_84F3():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_84F3)
    Sleep(50)

    def lambda_8503():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8503)
    Sleep(50)

    def lambda_8513():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8513)
    Sleep(50)

    def lambda_8523():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_8523)
    Sleep(50)

    def lambda_8533():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_8533)
    OP_6F(0x79)
    Sleep(500)

    #C0201
    ChrTalk(
        0x101,
        (
            "#00007Fま、待て！\x02\x03",

            "#00003Fその前に、今回の運転は\x01",
            "明らかなスピード違反だ！\x02\x03",

            "#00001Fまずはきちんと罰則を受けて……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_85BB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_85BB)
    Sleep(50)

    def lambda_85CB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_85CB)
    Sleep(50)

    def lambda_85DB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_85DB)
    Sleep(1000)

    #C0202
    ChrTalk(
        0x18,
        "フン、罰則がどうした？\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x18,
        (
            "俺たち外国人に対して、\x01",
            "自治州法では大した罰則を\x01",
            "与える事はできないはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8731")
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
            "QS_1105 暴走車の取り締まり１を？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",            # 0
            "【クリアしている】\x01",        # 1
            "【クリアしていない】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_871D")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_8731")

    label("loc_871D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8731")
    OP_29(0x69, 0x3, 0x10)

    label("loc_8731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_87C1")

    #C0205
    ChrTalk(
        0x18,
        (
            "この間のように、せいぜい\x01",
            "罰金を払えば済む話なんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x104,
        "#00310Fチッ……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x105,
        "#10306Fやれやれ、またこういうオチかい？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8876")

    label("loc_87C1")


    #C0208
    ChrTalk(
        0x18,
        (
            "どうせ、せいぜい\x01",
            "罰金を払えば済む話なんだろう？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(100)

    #C0209
    ChrTalk(
        0x104,
        "#00305Fそ、そうなのかよ？\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x105,
        (
            "#10303Fまあ確かに、現行法じゃ\x01",
            "外国人に対して強く出れない\x01",
            "事情はありそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8876")

    TurnDirection(0x104, 0x18, 500)
    Sleep(100)

    #C0211
    ChrTalk(
        0x19,
        "フフ、そういうこったな。\x02",
    )

    CloseMessageWindow()

    def lambda_88A3():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_88A3)
    Sleep(50)

    def lambda_88B3():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_88B3)
    Sleep(50)

    def lambda_88C3():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_88C3)
    Sleep(500)

    #C0212
    ChrTalk(
        0x18,
        (
            "俺たちも忙しいし、\x01",
            "あんたらもわざわざ本部に\x01",
            "連行していくのは面倒だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x18,
        (
            "なんだったら、罰金なんかは\x01",
            "ここで支払ってやろう。\x01",
            "それで文句はないはずだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x1A,
        "ハハッ、ユーリあったまいいー！\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x109,
        "#10107Fあ、あなた達……！\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x103,
        (
            "#00206F……感心してしまうほどの\x01",
            "最低ぶりですね。\x02",
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
        "#00103F……いえ、そうはいかないわ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8A7D():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8A7D)
    Sleep(50)

    def lambda_8A8D():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8A8D)
    Sleep(50)

    def lambda_8A9D():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8A9D)
    Sleep(500)

    #C0218
    ChrTalk(
        0x19,
        "……はあ？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#00100Fおじさまが市長になってから、\x01",
            "クロスベルの自治州法は\x01",
            "常に変革を続けているの。\x02\x03",

            "#00103F先日も、自治州法が\x01",
            "一部改正されたと聞いたわ。\x02\x03",

            "#00101Fそれによって、外国人の\x01",
            "犯罪行為に関しての罰則が\x01",
            "強化されることになったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x18,
        "なんだと……！？\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x1B,
        (
            "今回の場合だと、\x01",
            "１ヶ月の免許停止処分……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x1B,
        "このあたりが妥当でしょうね。\x02",
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

    def lambda_8C57():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8C57)
    Sleep(50)

    def lambda_8C67():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8C67)
    Sleep(50)

    def lambda_8C77():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8C77)
    Sleep(500)

    #C0223
    ChrTalk(
        0x19,
        "い、１ヶ月の免許停止～！？\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x19,
        (
            "っつーことは、\x01",
            "新しいクルマを買ったとしても\x01",
            "運転しちゃダメってことかよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x1A,
        (
            "さ、さすがに\x01",
            "やりすぎたってことかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x18,
        "……ふ、ふざけるなよ……！\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x18,
        (
            "何故俺がそんな罰則などを\x01",
            "受けなくちゃならない！？\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x18,
        (
            "#4Sお前ら自治州の警察ごときに、\x01",
            "この俺を裁く権利が\x01",
            "あるとでも思っているのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#00010Fなっ……！\x02",
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
        "……は、はは、そうだよな。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x19,
        (
            "クロスベルの警察なんかが\x01",
            "俺たちを裁いていい訳がねえよな！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x18, 500)
    Sleep(100)

    #C0233
    ChrTalk(
        0x1A,
        (
            "ユ、ユーリ、サイクス。\x01",
            "だけどさあ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1A, 500)
    Sleep(100)

    #C0234
    ChrTalk(
        0x18,
        (
            "黙っていろ、レジー！\x01",
            "俺たちの旅行が台無しに\x01",
            "されようとしてるんだぞ！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1B, 500)
    Sleep(100)

    #C0235
    ChrTalk(
        0x18,
        (
            "こうなったら、\x01",
            "親父に手を回してもらって\x01",
            "自治州政府に圧力をかけ──\x02",
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
        "#5S……いい加減にしなさいっ！\x02",
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

    def lambda_9098():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9098)
    Sleep(50)

    def lambda_90A8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_90A8)
    Sleep(50)

    def lambda_90B8():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_90B8)
    Sleep(50)

    def lambda_90C8():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_90C8)
    Sleep(50)

    def lambda_90D8():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_90D8)
    Sleep(50)

    def lambda_90E8():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_90E8)
    Sleep(50)

    def lambda_90F8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_90F8)
    Sleep(50)

    def lambda_9108():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9108)
    Sleep(50)

    def lambda_9118():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_9118)
    Sleep(1000)

    #C0237
    ChrTalk(
        0x1B,
        (
            "この際、罰則云々は\x01",
            "大した問題じゃないのよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x1B,
        (
            "あなた達の乱暴な運転で、\x01",
            "罪もない人たちがどれだけ\x01",
            "怖い思いをしているか……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x1B,
        (
            "あなた達は、\x01",
            "考えたことがあるのっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x19,
        "な、なんだよ急に……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x18,
        (
            "フ、フン……\x01",
            "庶民がどれだけ怖がろうが\x01",
            "俺たちの知ったことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x18,
        "それに、たかが導力車くらいで──\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x1B,
        (
            "だったら……\x01",
            "あなた達自身は怖くなかったの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x1B,
        (
            "今回の事故だって、\x01",
            "支援課が助けてくれなかったら\x01",
            "命を落としていたかもしれないのよ！？\x02",
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
            "た、確かに池に突っ込んだ時は\x01",
            "もうダメかと思ったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x19,
        (
            "……は、はは、何言ってんだ。\x01",
            "俺たちがそんな事になるわけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x1B,
        "誰だろうと関係ないわ！\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x1B,
        (
            "突然、事故や犯罪に巻き込まれて\x01",
            "何の関係もない人が\x01",
            "傷つくことだってある……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x1B,
        (
            "私は警察官として、\x01",
            "そういったケースを\x01",
            "何度だって見てきたわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x1B,
        (
            "あなた達の危険運転は、\x01",
            "そこまでの恐怖を\x01",
            "他人に与えているのっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x1B,
        (
            "それでも、あなた達は\x01",
            "怖くなかったというの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x18,
        "…………っ…………\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x1B,
        (
            "そんな他人の気持ちを考えもしないで\x01",
            "迷惑をかけ続けるなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0254
    ChrTalk(
        0x1B,
        "#4Sハイブラッズ#12R高 貴 な る 血 #が聞いて呆れるわ！！\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0255
    ChrTalk(
        0x1B,
        "#4S人として、恥ずかしいと思わないのっ！？\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0256
    ChrTalk(
        0x18,
        "#100W…………ぐ……ぐッ……！！\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x101,
        "#00005Fケイト先輩……\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x1B,
        (
            "……とにかく、貴方たちを\x01",
            "本部まで連行させてもらうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1B,
        (
            "１ヶ月の免許停止の間に、\x01",
            "しっかりと反省すること！！\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x1B,
        (
            "さあ、分かったら\x01",
            "パトカーに乗った乗った！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x18, 500)
    Sleep(100)

    #C0261
    ChrTalk(
        0x1A,
        "な、なあユーリ、サイクス……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)
    Sleep(100)

    #C0262
    ChrTalk(
        0x19,
        "ああ、正直今回ばかりは……\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x18,
        "………………チッ…………\x02",
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

    def lambda_9783():

        label("loc_9783")

        TurnDirection(0xFE, 0x18, 0)
        Yield()
        Jump("loc_9783")

    QueueWorkItem2(0x103, 1, lambda_9783)
    Sleep(100)
    BeginChrThread(0x109, 1, 0, 56)
    Sleep(100)

    def lambda_97A1():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_97A1)
    Sleep(50)

    def lambda_97B1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_97B1)
    Sleep(2500)

    def lambda_97C1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97C1)
    Sleep(50)

    def lambda_97D1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_97D1)
    Sleep(50)

    def lambda_97E1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_97E1)
    Sleep(1000)

    def lambda_97F1():

        label("loc_97F1")

        TurnDirection(0xFE, 0x18, 0)
        Yield()
        Jump("loc_97F1")

    QueueWorkItem2(0x109, 1, lambda_97F1)
    WaitChrThread(0x18, 1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    Sound(462, 0, 100, 0)
    OP_71(0x22, 0x169, 0x186, 0x1, 0x0)
    Sleep(500)
    OP_79(0x23)
    Sleep(300)

    def lambda_982A():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_982A)

    def lambda_983F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_983F)
    Sleep(300)

    #C0264
    ChrTalk(
        0x19,
        "お、おいユーリ！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x1A,
        "ま、待ってくれよ～！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x19, 1, 0, 58)
    Sleep(100)
    BeginChrThread(0x1A, 1, 0, 59)
    WaitChrThread(0x19, 1)

    def lambda_9896():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9896)

    def lambda_98AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_98AB)
    WaitChrThread(0x1A, 1)

    def lambda_98C0():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_98C0)

    def lambda_98D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_98D5)
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
            "#00002F（はは、彼らも結構\x01",
            "  こたえてるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0267
    ChrTalk(
        0x102,
        (
            "#00104F（ええ……ケイトさん、\x01",
            "  ものすごい剣幕だったもの。）\x02\x03",

            "#00102F（普段、怒られ慣れていないでしょうし\x01",
            "  いい薬になったんじゃないかしら。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x101, 500)
    Sleep(100)

    #C0268
    ChrTalk(
        0x1B,
        (
            "特務支援課の皆さん、ミレイユ三尉……\x01",
            "改めて、ご協力ありがとうございます！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A5E():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A5E)
    Sleep(50)

    def lambda_9A6E():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A6E)
    Sleep(50)

    def lambda_9A7E():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9A7E)
    Sleep(50)

    def lambda_9A8E():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9A8E)
    Sleep(50)

    def lambda_9A9E():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9A9E)
    Sleep(50)

    def lambda_9AAE():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9AAE)
    Sleep(50)

    def lambda_9ABE():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9ABE)
    Sleep(500)

    #C0269
    ChrTalk(
        0x101,
        "#00000Fはい、お疲れ様です！\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x105,
        (
            "#10309Fフフ、おかげさまで\x01",
            "なかなか楽しかったよ。\x02\x03",

            "#10304Fカーチェイスなんかも\x01",
            "体験できたしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x103,
        "#00206F……楽しむことではないかと。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x1C,
        (
            "#07903Fケイト巡査……あなたの言葉は、\x01",
            "私の胸にも響くものがあったわ。\x02\x03",

            "#07902Fクロスベルを守るために、\x01",
            "お互いがんばっていきましょう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1C, 500)
    Sleep(100)

    #C0273
    ChrTalk(
        0x1B,
        "ふふっ、はい！！\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x1B,
        "……それでは、失礼します！\x02",
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
            "#07903Fそれじゃあ、私も彼らの導力車を\x01",
            "然るべき所に引渡しに行くとしましょう。\x02\x03",

            "#07900Fあなた達、同行してもらえるかしら。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9DDD():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DDD)
    Sleep(50)

    def lambda_9DED():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9DED)
    Sleep(50)

    def lambda_9DFD():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9DFD)
    Sleep(50)

    def lambda_9E0D():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E0D)
    Sleep(50)

    def lambda_9E1D():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9E1D)
    Sleep(50)

    def lambda_9E2D():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E2D)
    Sleep(500)

    #C0276
    ChrTalk(
        0x104,
        "#00304Fまあ、ここまで付き合ったしな。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x109,
        "#10109Fお供させて頂きます！\x02",
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
            "その後、ロイドたちは警備隊による\x01",
            "暴走車の牽引作業を手伝い……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0279
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ベルガード門にて活動を再開するのだった。\x07\x00\x02",
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
            "クエスト【暴走車の追跡】\x07\x00",
            "を達成した！\x02",
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

    # Function_51_7AE4 end

    def Function_52_9FD1(): pass

    label("Function_52_9FD1")

    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_52_9FD1 end

    def Function_53_9FE8(): pass

    label("Function_53_9FE8")

    OP_9B(0x1, 0x102, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x102, 0x10E, 0x1F4)
    Return()

    # Function_53_9FE8 end

    def Function_54_9FFF(): pass

    label("Function_54_9FFF")

    OP_9B(0x1, 0x104, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_54_9FFF end

    def Function_55_A016(): pass

    label("Function_55_A016")

    OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_55_A016 end

    def Function_56_A02D(): pass

    label("Function_56_A02D")

    OP_93(0x109, 0x5A, 0x1F4)
    OP_9B(0x1, 0x109, 0xB4, 0x1F4, 0x3E8, 0x0)
    Sleep(2500)
    Return()

    # Function_56_A02D end

    def Function_57_A047(): pass

    label("Function_57_A047")

    OP_9B(0x1, 0x18, 0x0, 0x320, 0x5DC, 0x0)
    OP_95(0x18, -9870, 0, -39550, 1500, 0x0)

    def lambda_A06F():
        TurnDirection(0x19, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_A06F)
    OP_95(0x18, -12250, 0, -33890, 1500, 0x0)
    OP_95(0x18, -13950, 0, -33830, 1500, 0x0)
    OP_93(0x18, 0x0, 0x1F4)
    Return()

    # Function_57_A047 end

    def Function_58_A0A7(): pass

    label("Function_58_A0A7")

    OP_9B(0x0, 0x19, 0x0, 0x7D0, 0xBB8, 0x0)
    OP_95(0x19, -12250, 0, -33890, 3000, 0x0)
    OP_95(0x19, -13950, 0, -33830, 3000, 0x0)
    OP_93(0x19, 0x0, 0x1F4)
    Return()

    # Function_58_A0A7 end

    def Function_59_A0E6(): pass

    label("Function_59_A0E6")

    OP_95(0x1A, -8910, 0, -41130, 3000, 0x0)
    OP_95(0x1A, -10610, 0, -39800, 3000, 0x0)
    OP_95(0x1A, -12250, 0, -33890, 3000, 0x0)
    OP_95(0x1A, -13950, 0, -33830, 3000, 0x0)
    OP_93(0x1A, 0x0, 0x1F4)
    Return()

    # Function_59_A0E6 end

    def Function_60_A13E(): pass

    label("Function_60_A13E")

    OP_9F(0x0, 0x13)
    OP_9F(0x1, -2650, 0, -18410)
    OP_9F(0x1, -2370, 0, -5440)
    OP_9F(0x1, 2900, 0, 3350)
    OP_9F(0x1, 610, 640, 12550)
    OP_9F(0x1, 610, 2500, 19990)
    OP_9F(0x1, 2510, 2500, 24560)
    OP_9F(0x2, 0x13, 5500, 0x6)
    Return()

    # Function_60_A13E end

    def Function_61_A1A0(): pass

    label("Function_61_A1A0")

    EventBegin(0x1)
    OP_E2(0x3)

    #C0281
    ChrTalk(
        0x101,
        (
            "#00001F寄り道はしていられないな。\x01",
            "とにかく事故現場に向かおう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -60010, -1990, 470, 89)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_61_A1A0 end

    SaveToFile()

Try(main)
