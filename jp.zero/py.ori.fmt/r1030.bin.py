from ZeroScenarioHelper import *

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
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 1000, 9000, 0, 0, 1, 95, 0, 3, 0, 4],
    )

    BuildStringList((
        "r1030",                  # 0
        "コリン",                 # 1
        "ボス１",                 # 2
        "ボス２",                 # 3
        "ボス３",                 # 4
        "ボス４",                 # 5
        "ボス５",                 # 6
        "ボス６",                 # 7
        "カマ",                   # 8
        "チョウ",                 # 9
        "バス",                   # 10
        "カエンギーヌー",         # 11
        "br1000",                 # 12
        "br1000",                 # 13
        "br1000",                 # 14
        "br1000",                 # 15
        "br1000",                 # 16
        "br1000",                 # 17
        "br1000",                 # 18
        "br1000",                 # 19
        "br1000",                 # 20
        "クロスベル市方面",       # 21
        "ベルガード門方面",       # 22
    ))

    ATBonus("ATBonus_738", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_5CC0", 0,   0,   13,  1,   5,   7,   4)
    Sepith("Sepith_5CC8", 2,   1,   0,   0,   9,   9,   9)
    Sepith("Sepith_5CD8", 4,   4,   10,  2,   0,   5,   5)
    Sepith("Sepith_5CA0", 4,   2,   11,  0,   0,   8,   5)
    Sepith("Sepith_5CA8", 0,   8,   0,   12,  4,   8,   0)
    Sepith("Sepith_5CE8", 12,  7,   4,   3,   6,   14,  7)

    MonsterBattlePostion("MonsterBattlePostion_798", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_79C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7AC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_7FC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_800", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_804", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_808", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_80C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_810", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_814", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_778", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_77C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_780", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_784", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_788", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_78C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_790", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_794", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_818", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_81C", 12, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_820", 4, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_824", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_828", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_82C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_830", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_834", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_838", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_83C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_840", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_844", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_848", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_84C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_850", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_854", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_920", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_5CC0", 30, 40, 20, 10,
        (
            ("ms71300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71300.dat", "ms71300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71300.dat", "ms70400.dat", "ms71300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71300.dat", "ms71300.dat", "ms70400.dat", "ms71300.dat", 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
        )
    )

    BattleInfo(
        "BattleInfo_AB0", 0x0000, 17, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_5CC8", 30, 40, 20, 10,
        (
            ("ms64200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms64200.dat", "ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms64200.dat", "ms66900.dat", "ms64200.dat", "ms66900.dat", 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
        )
    )

    BattleInfo(
        "BattleInfo_9E8", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_5CD8", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71900.dat", "ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
        )
    )

    BattleInfo(
        "BattleInfo_B78", 0x0000, 17, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_5CA0", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
        )
    )

    BattleInfo(
        "BattleInfo_858", 0x0000, 17, 6, 60, 8, 1, 40, 0, "br1000", "Sepith_5CA8", 30, 40, 20, 10,
        (
            ("ms70300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms70300.dat", "ms70300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms70300.dat", "ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
        )
    )

    BattleInfo(
        "BattleInfo_D0C", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br1000", "Sepith_5CE8", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C84", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65100.dat", "ms65100.dat", "ms65100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_818", "MonsterBattlePostion_7F8", "ed7401", "ed7403", "ATBonus_738"),
            (),
            (),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_C40", 0x0000, 17, 6, 60, 0, 1, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7401", "ed7403", "ATBonus_738"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_CC8", 0x0002, 26, 6, 0, 0, 1, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62900.dat", "ms62900.dat", "ms62900.dat", "ms62900.dat", 0, 0, 0, 0, "MonsterBattlePostion_838", "MonsterBattlePostion_7F8", "ed7402", "ed7403", "ATBonus_738"),
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
        "monster/ch65150.itc",               # 1A
        "monster/ch65150.itc",               # 1B
        "monster/ch60750.itc",               # 1C
        "monster/ch60750.itc",               # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-59919,  500,     32990,   0,    484,  0x0, 0,   18,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(-17880,  910,     0,       0x1010000,    "BattleInfo_920", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-44410,  -7750,   0,       0x1010000,    "BattleInfo_AB0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-60650,  27380,   0,       0x1010000,    "BattleInfo_9E8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-16440,  44520,   0,       0x1010000,    "BattleInfo_B78", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-39150,  60950,   0,       0x1010000,    "BattleInfo_858", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-74290,  -25740,  -2000,   0x1010000,    "BattleInfo_B78", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-34710,  -42590,  -4000,   0x1010000,    "BattleInfo_920", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-62760,  -62500,  -6000,   0x1010000,    "BattleInfo_9E8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-19130,  6440,    0,       0x1010000,    "BattleInfo_D0C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-59570,  -9280,   0,       0x1010000,    "BattleInfo_D0C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-56370,  -76140,  -6000,   0x1010000,    "BattleInfo_D0C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-27490,  31330,   0,       0x1010000,    "BattleInfo_D0C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-38170,  2140,    1000,    0x185005A,    "BattleInfo_C84", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 19,  -36.0,                 2.0,                   -1.0,                  1406.25,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666666269302368,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   7.200000286102295,     -0.13333332538604736,  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 20,  -38.0,                 -50.0,                 -5.5,                  506.25,                [0.1111111119389534,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.222222328186035,     10.0,                  1.100000023841858,     1.0])
    DeclEvent(0x0000, 0, 11,  -37.56999969482422,    2.0,                   -1.0,                  3600.0,                [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666667014360428,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.696249961853027,     -0.13333334028720856,  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 48,  -28.690000534057617,   29.889999389648438,    -0.5,                  144.0,                 [0.05892554670572281,  0.35355350375175476,   -0.0,                  0.0,                   -0.05892558768391609,  0.35355326533317566,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.451859712600708,     -0.42425668239593506,  0.10000000149011612,   1.0])

    DeclActor(-59920,  0,       32990,   1200,    -59920,  1000,    32990,   0x007C, 0,  5,  0x0000)
    DeclActor(-82750,  -2000,   -27760,  1200,    -82750,  -1000,   -27760,  0x007C, 0,  6,  0x0000)
    DeclActor(-27210,  -3900,   -44030,  1200,    -27210,  -2900,   -44030,  0x007C, 0,  7,  0x0000)
    DeclActor(-37700,  0,       8150,    1200,    -37700,  1000,    8150,    0x007C, 0,  18, 0x0000)
    DeclActor(-62570,  0,       36330,   1200,    -62770,  -1000,   40340,   0x007C, 0,  17, 0x0000)
    DeclActor(-49450,  -6000,   -76260,  1200,    -49360,  -3000,   -76640,  0x007C, 0,  49, 0x0000)
    DeclActor(-12560,  0,       12190,   1200,    -12560,  0,       12190,   0x007C, 0,  8,  0x0000)
    DeclActor(-51750,  0,       -9060,   1200,    -51750,  0,       -9060,   0x007C, 0,  9,  0x0000)
    DeclActor(-23570,  0,       48090,   1200,    -23570,  0,       48090,   0x007C, 0,  10, 0x0000)
    DeclActor(-59500,  -6000,   -63000,  1200,    -59500,  -5000,   -63000,  0x007C, 0,  47, 0x0000)
    DeclActor(-37790,  0,       10900,   1500,    -37790,  1700,    10900,   0x007C, 0,  50, 0x0000)

    PlaceName(29.0, 0.0, 19.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(-95.0, 0.0, 84.0, 0x0000, 0x0000, "ベルガード門方面")
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

    ScpFunction((
        "Function_0_F04",          # 00, 0
        "Function_1_F20",          # 01, 1
        "Function_2_F3F",          # 02, 2
        "Function_3_F5E",          # 03, 3
        "Function_4_F80",          # 04, 4
        "Function_5_195C",         # 05, 5
        "Function_6_1B6F",         # 06, 6
        "Function_7_1C66",         # 07, 7
        "Function_8_1DB3",         # 08, 8
        "Function_9_1DC7",         # 09, 9
        "Function_10_1DDB",        # 0A, 10
        "Function_11_1DEF",        # 0B, 11
        "Function_12_243C",        # 0C, 12
        "Function_13_245F",        # 0D, 13
        "Function_14_2514",        # 0E, 14
        "Function_15_2638",        # 0F, 15
        "Function_16_2759",        # 10, 16
        "Function_17_27EE",        # 11, 17
        "Function_18_28C2",        # 12, 18
        "Function_19_29D5",        # 13, 19
        "Function_20_2C9A",        # 14, 20
        "Function_21_3D8A",        # 15, 21
        "Function_22_3DB0",        # 16, 22
        "Function_23_3DD6",        # 17, 23
        "Function_24_3DFC",        # 18, 24
        "Function_25_3E22",        # 19, 25
        "Function_26_3E48",        # 1A, 26
        "Function_27_3E64",        # 1B, 27
        "Function_28_3E83",        # 1C, 28
        "Function_29_3EF9",        # 1D, 29
        "Function_30_3FB2",        # 1E, 30
        "Function_31_405F",        # 1F, 31
        "Function_32_40D6",        # 20, 32
        "Function_33_4190",        # 21, 33
        "Function_34_41EB",        # 22, 34
        "Function_35_4C0C",        # 23, 35
        "Function_36_4CC1",        # 24, 36
        "Function_37_4D22",        # 25, 37
        "Function_38_4D3E",        # 26, 38
        "Function_39_4DC7",        # 27, 39
        "Function_40_4E2B",        # 28, 40
        "Function_41_4F19",        # 29, 41
        "Function_42_4FCB",        # 2A, 42
        "Function_43_4FEA",        # 2B, 43
        "Function_44_501F",        # 2C, 44
        "Function_45_508A",        # 2D, 45
        "Function_46_50A9",        # 2E, 46
        "Function_47_50C7",        # 2F, 47
        "Function_48_549A",        # 30, 48
        "Function_49_54EE",        # 31, 49
        "Function_50_5BBF",        # 32, 50
    ))


    def Function_0_F04(): pass

    label("Function_0_F04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F1F")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_F04")

    label("loc_F1F")

    Return()

    # Function_0_F04 end

    def Function_1_F20(): pass

    label("Function_1_F20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F3E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_F20")

    label("loc_F3E")

    Return()

    # Function_1_F20 end

    def Function_2_F3F(): pass

    label("Function_2_F3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F5D")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_F3F")

    label("loc_F5D")

    Return()

    # Function_2_F3F end

    def Function_3_F5E(): pass

    label("Function_3_F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_F6D")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 34)

    label("loc_F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_F7C")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 16)

    label("loc_F7C")

    Call(0, 12)
    Return()

    # Function_3_F5E end

    def Function_4_F80(): pass

    label("Function_4_F80")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F9D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FB0")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_FB0")

    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1731")
    SetChrFlags(0x1F, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jump("loc_1745")

    label("loc_1731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1745")
    ClearChrFlags(0x1F, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1745")

    OP_52(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x1F, 0x100)
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x9, 0x1)
    SetMapObjFlags(0x5, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1784")
    OP_66(0x9, 0x1)

    label("loc_1784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1793")
    ClearMapObjFlags(0x5, 0x4)

    label("loc_1793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A6")
    OP_70(0x0, 0x0)
    Jump("loc_17AA")

    label("loc_17A6")

    OP_70(0x0, 0x1E)

    label("loc_17AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BD")
    OP_70(0x1, 0x0)
    Jump("loc_17C1")

    label("loc_17BD")

    OP_70(0x1, 0x1E)

    label("loc_17C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D4")
    OP_70(0x2, 0x0)
    Jump("loc_17D8")

    label("loc_17D4")

    OP_70(0x2, 0x1E)

    label("loc_17D8")

    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 7)), scpexpr(EXPR_END)), "loc_1842")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -12560, 0, 12190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)
    Jump("loc_18F9")

    label("loc_1842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 0)), scpexpr(EXPR_END)), "loc_18A0")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -51750, 0, -9060, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x7, 0x1)
    Jump("loc_18F9")

    label("loc_18A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 1)), scpexpr(EXPR_END)), "loc_18F9")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -23570, 0, 48090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x8, 0x1)

    label("loc_18F9")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -62770, -1000, 40340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_195B")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_195B")

    Return()

    # Function_4_F80 end

    def Function_5_195C(): pass

    label("Function_5_195C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B29")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A57")
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x12, 0x0, 0)
    OP_98(0x12, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_19B5():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_19B5)

    def lambda_19CF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_19CF)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)

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
    WaitChrThread(0x12, 1)
    Battle("BattleInfo_C40", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1A38"),
        (2, "loc_1A47"),
        (1, "loc_1A54"),
        (SWITCH_DEFAULT, "loc_1A57"),
    )


    label("loc_1A38")

    SetScenarioFlags(0x74, 5)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_1A57")

    label("loc_1A47")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1A54")

    OP_B7(0x0)
    Return()

    label("loc_1A57")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x647, 1)"), scpexpr(EXPR_END)), "loc_1AB4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x647),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x118, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1B24")

    label("loc_1AB4")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x647),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x647),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1B24")

    Jump("loc_1B63")

    label("loc_1B29")

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

    label("loc_1B63")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_195C end

    def Function_6_1B6F(): pass

    label("Function_6_1B6F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C2F")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x4, 60)
    AddSepith(0x5, 60)
    AddSepith(0x6, 60)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I時のセピス×６０\x01\x07\x02",

            "#61I空のセピス×６０\x01\x07\x02",

            "#62I幻のセピス×６０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x119, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1C54")

    label("loc_1C2F")


    #A0006
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

    label("loc_1C54")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1B6F end

    def Function_7_1C66(): pass

    label("Function_7_1C66")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D62")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1CEB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
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
    SetScenarioFlags(0x119, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1D5D")

    label("loc_1CEB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D5D")

    Jump("loc_1DA7")

    label("loc_1D62")

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

    label("loc_1DA7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1C66 end

    def Function_8_1DB3(): pass

    label("Function_8_1DB3")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 7)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1DB3 end

    def Function_9_1DC7(): pass

    label("Function_9_1DC7")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 0)
    OP_65(0x7, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_9_1DC7 end

    def Function_10_1DDB(): pass

    label("Function_10_1DDB")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 1)
    OP_65(0x8, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_10_1DDB end

    def Function_11_1DEF(): pass

    label("Function_11_1DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 2)), scpexpr(EXPR_END)), "loc_1DF9")
    Return()

    label("loc_1DF9")

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

    #A0010
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
        (1, "loc_1EDB"),
        (SWITCH_DEFAULT, "loc_1EF2"),
    )


    label("loc_1EDB")

    Sleep(500)
    OP_90(0x0, -32290, 0, 1830, 270)
    EventEnd(0x5)
    Return()

    label("loc_1EF2")

    Battle("BattleInfo_C84", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-32290, 1000, 1830, 0)
    OP_90(0x0, -32290, 0, 1830, 270)
    OP_90(0x1, -32290, 0, 1830, 270)
    OP_90(0x2, -32290, 0, 1830, 270)
    OP_90(0x3, -32290, 0, 1830, 270)
    OP_90(0x4, -32290, 0, 1830, 270)
    OP_90(0x5, -32290, 0, 1830, 270)
    OP_90(0x6, -32290, 0, 1830, 270)
    OP_90(0x7, -32290, 0, 1830, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_1FB4"),
        (1, "loc_1FB7"),
        (SWITCH_DEFAULT, "loc_1FBA"),
    )


    label("loc_1FB4")

    EventEnd(0x5)
    Return()

    label("loc_1FB7")

    OP_B7(0x0)
    Return()

    label("loc_1FBA")

    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(-38360, 600, 1950, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    EventBegin(0x0)
    SetChrFlags(0x1F, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手配魔獣を退治した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrPos(0x101, -38400, 0, 3980, 180)
    SetChrPos(0x102, -36700, 0, 1980, 270)
    SetChrPos(0x103, -38400, 0, -20, 0)
    SetChrPos(0x104, -40400, 0, 1980, 90)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)

    #C0012
    ChrTalk(
        0x102,
        "#0106Fふう、強敵だったわね。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#0300Fああ、妙に手強かったな。\x02\x03",

            "俺も警備隊時代に\x01",
            "この辺りは何度か来てるが、\x01",
            "見た事のないタイプだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 2)), scpexpr(EXPR_END)), "loc_21B5")

    #C0014
    ChrTalk(
        0x103,
        (
            "#0202Fでも、これでバスの運行も\x01",
            "再開できそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0000Fそうだな。\x01",
            "市庁舎に連絡しておこうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2296")

    label("loc_21B5")


    #C0016
    ChrTalk(
        0x101,
        (
            "#0008Fそうか……\x01",
            "それに街道の真ん中にいたとなると\x01",
            "少し心配だな。\x02\x03",

            "すぐ近くに\x01",
            "バス停もあるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#0200Fバスの運行にも\x01",
            "支障が出ていそうですね。\x02\x03",

            "市庁舎に連絡しておいた方が\x01",
            "いいかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#0000Fああ、そうだな。\x02",
    )

    CloseMessageWindow()

    label("loc_2296")

    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは市庁舎を呼び出し、\x01",
            "街道に居た魔獣を倒したことを伝えた。\x02",
        )
    )

    CloseMessageWindow()

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスはすぐに運行を再開するらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_64(0x101)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西クロスベル街道のバスが運行再開しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_37()
    SetScenarioFlags(0x78, 2)
    OP_29(0x10, 0x4, 0x10)
    OP_29(0x10, 0x4, 0x2)
    OP_29(0x10, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_11_1DEF end

    def Function_12_243C(): pass

    label("Function_12_243C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_245E")
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)

    label("loc_245E")

    Return()

    # Function_12_243C end

    def Function_13_245F(): pass

    label("Function_13_245F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0022
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
            "クロスベル市西口\x01",      # 0
            "ベルガード門\x01",          # 1
            "やめる\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24EC")
    Call(0, 14)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_250C")

    label("loc_24EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_250C")
    Call(0, 15)
    ClearMapFlags(0x8000000)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()

    label("loc_250C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_245F end

    def Function_14_2514(): pass

    label("Function_14_2514")

    Fade(1000)
    OP_68(-40030, 600, 12630, 0)
    MoveCamera(38, 23, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(24000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -39500, 0, 7300, 270)
    SetChrPos(0x1, -39500, 0, 8500, 270)
    SetChrPos(0x2, -39500, 0, 9700, 270)
    SetChrPos(0x3, -39500, 0, 10900, 270)
    ClearChrFlags(0x11, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    OP_78(0x4, 0x11)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x11, -27810, 0, 29700, 225)
    OP_D3(0x11, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_25EF():
        OP_95(0xFE, -43990, 0, 13530, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_25EF)
    Sleep(500)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x11, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_14_2514 end

    def Function_15_2638(): pass

    label("Function_15_2638")

    Fade(1000)
    OP_68(-38160, 600, 3480, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -39500, 0, 7300, 180)
    SetChrPos(0x1, -39500, 0, 8500, 180)
    SetChrPos(0x2, -39500, 0, 9700, 180)
    SetChrPos(0x3, -39500, 0, 10900, 180)
    ClearChrFlags(0x11, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    OP_78(0x4, 0x11)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x11, -27200, 0, 1290, 270)
    OP_D3(0x11, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2713():
        OP_95(0xFE, -39660, 0, 1670, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2713)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x11, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_15_2638 end

    def Function_16_2759(): pass

    label("Function_16_2759")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -36870, 0, 7430, 225)
    SetChrPos(0x1, -36870, 0, 7430, 225)
    SetChrPos(0x2, -36870, 0, 7430, 225)
    SetChrPos(0x3, -36870, 0, 7430, 225)
    OP_68(-36870, 600, 7430, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_16_2759 end

    def Function_17_27EE(): pass

    label("Function_17_27EE")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0023
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(-62940, 600, 37620, 1500)
    MoveCamera(45, 45, 0, 1500)
    OP_6E(470, 1500)
    SetCameraDistance(23500, 1500)
    Sleep(1000)
    SetChrName("")

    #A0024
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28BD")
    OP_E0(0x2)
    MiniGame(0x6, 0x12, 0xFFFF0D4E, 0x0, 0x8804, 0x0, 0xFFFF0ACE, 0xFFFFFC18, 0x9D94)

    label("loc_28BD")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_17_27EE end

    def Function_18_28C2(): pass

    label("Function_18_28C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2973")
    TalkBegin(0xFF)

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "凶悪な魔獣出没中との通報を受け、\x01",
            "現在運行を見合わせております。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x95, 2)
    TalkEnd(0xFF)
    Jump("loc_29D4")

    label("loc_2973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29D1")
    TalkBegin(0xFF)

    #C0027
    ChrTalk(
        0x101,
        (
            "#0001Fバスを待っている場合じゃない……\x01",
            "コリン君を探しに行こう！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_29D4")

    label("loc_29D1")

    Call(0, 13)

    label("loc_29D4")

    Return()

    # Function_18_28C2 end

    def Function_19_29D5(): pass

    label("Function_19_29D5")

    EventBegin(0x0)
    OP_E0(0x3)
    Fade(1000)
    OP_68(-37910, 400, 3210, 0)
    MoveCamera(60, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21640, 0)
    SetCameraDistance(20640, 2000)
    SetChrPos(0x101, -40270, 0, 1690, 270)
    SetChrPos(0x102, -39010, 0, 3170, 270)
    SetChrPos(0x103, -39370, 0, 1230, 270)
    SetChrPos(0x104, -37130, 0, 3090, 270)
    SetChrPos(0x160, -36970, 0, 1730, 270)
    SetChrPos(0x8, -46500, -2000, -6500, 0)
    OP_0D()
    SetMessageWindowPos(220, 170, -1, -1)
    SetChrName("子供の声")

    #A0028
    AnonymousTalk(
        0xFF,
        "#2Sきゃはは……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
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
    Sleep(50)
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0029
    ChrTalk(
        0x101,
        "#0005F#11P今のは……！？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        "#0108F#11Pど、どこから聞こえたの！？\x02",
    )

    CloseMessageWindow()

    def lambda_2B7C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B7C)
    Sleep(50)

    def lambda_2B8C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B8C)
    Sleep(50)

    def lambda_2B9C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2B9C)
    Sleep(300)

    #C0031
    ChrTalk(
        0x103,
        "#0202F#5P……南の方からです。\x02",
    )

    CloseMessageWindow()

    def lambda_2BCF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BCF)
    Sleep(50)

    def lambda_2BDF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BDF)
    Sleep(300)

    #C0032
    ChrTalk(
        0x104,
        (
            "#0300F#5Pああ……\x01",
            "警察学校とかがある方向だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0000F#5Pよし、急ごう……！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x160,
        "#3308F#11P#40W（……無事、みたいね。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -41600, 0, 2050, 270)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    SetScenarioFlags(0xA3, 2)
    OP_29(0x46, 0x1, 0xE)
    OP_E0(0x2)
    Call(0, 12)
    EventEnd(0x5)
    Return()

    # Function_19_29D5 end

    def Function_20_2C9A(): pass

    label("Function_20_2C9A")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch07200.itc", 0x26)
    LoadChrToIndex("monster/ch62950.itc", 0x27)
    LoadChrToIndex("monster/ch62951.itc", 0x28)
    LoadChrToIndex("monster/ch62952.itc", 0x29)
    LoadChrToIndex("apl/ch50338.itc", 0x2A)
    LoadChrToIndex("apl/ch50339.itc", 0x2B)
    LoadChrToIndex("apl/ch50340.itc", 0x2C)
    LoadChrToIndex("apl/ch50341.itc", 0x2D)
    LoadChrToIndex("apl/ch50337.itc", 0x2F)
    LoadEffect(0x0, "battle\\ms00001.eff")
    LoadEffect(0x1, "event\\ev312_00.eff")
    LoadEffect(0x2, "event\\ev313_00.eff")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC9")
    SetChrPos(0x101, -38330, -4000, -48020, 180)
    SetChrPos(0x102, -39320, -4000, -47210, 180)
    SetChrPos(0x103, -37450, -4000, -46640, 180)
    SetChrPos(0x104, -37440, -4000, -45160, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)
    Jump("loc_2EFC")

    label("loc_2DC9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E31")
    SetChrPos(0x101, -39320, -4000, -47210, 180)
    SetChrPos(0x102, -38330, -4000, -48020, 180)
    SetChrPos(0x103, -37450, -4000, -46640, 180)
    SetChrPos(0x104, -37440, -4000, -45160, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)
    Jump("loc_2EFC")

    label("loc_2E31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E99")
    SetChrPos(0x101, -37450, -4000, -46640, 180)
    SetChrPos(0x102, -39320, -4000, -47210, 180)
    SetChrPos(0x103, -38330, -4000, -48020, 180)
    SetChrPos(0x104, -37440, -4000, -45160, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)
    Jump("loc_2EFC")

    label("loc_2E99")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EFC")
    SetChrPos(0x101, -37440, -4000, -45160, 180)
    SetChrPos(0x102, -39320, -4000, -47210, 180)
    SetChrPos(0x103, -37450, -4000, -46640, 180)
    SetChrPos(0x104, -38330, -4000, -48020, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)

    label("loc_2EFC")

    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -40040, -6000, -60700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x10, 0x2F)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x1000)
    SetChrPos(0x10, -39960, -6000, -63090, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x1, 0x0, 0x10, 0x140, 0, 700, 0, 0, 0, 0, 1750, 1750, 1750, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x28)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, -56560, -6000, -76920, 0)
    SetChrPos(0xA, -54610, -6000, -78160, 0)
    SetChrPos(0xB, -53190, -6000, -76380, 0)
    SetChrPos(0xC, -58360, -6000, -77640, 0)
    SetChrPos(0xD, -62210, -6000, -69920, 0)
    SetChrPos(0xE, -61950, -6000, -64470, 0)
    ModifyEventFlags(0, 1, 0x80)
    OP_68(-37980, -3400, -45910, 0)
    MoveCamera(51, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19000, 0)
    OP_68(-37980, -3400, -47410, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3225")

    #C0035
    ChrTalk(
        0x101,
        "#0002F#5Pいた……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_3225")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3255")

    #C0036
    ChrTalk(
        0x102,
        "#0102F#5P見つけた……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_3255")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3289")

    #C0037
    ChrTalk(
        0x103,
        "#0202F#5P第一目標発見……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_3289")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B2")

    #C0038
    ChrTalk(
        0x104,
        "#0302F#5Pいたぞ……！\x02",
    )

    CloseMessageWindow()

    label("loc_32B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35C0")
    OP_68(-40310, -5300, -61630, 2500)
    MoveCamera(45, 20, 0, 2500)
    SetCameraDistance(19360, 2500)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0039
    ChrTalk(
        0x8,
        (
            "#3809F#5Pきゃはは！\x02\x03",

            "#3802Fまって、まってよ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-42080, -5300, -61840, 9000)
    BeginChrThread(0x8, 3, 0, 35)
    BeginChrThread(0x10, 3, 0, 36)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x10, 3)
    OP_6F(0x79)
    Fade(500)
    OP_68(-40200, -5300, -60040, 0)
    MoveCamera(30, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21180, 0)
    SetCameraDistance(20180, 3000)
    SetChrPos(0x101, -40200, -6000, -58030, 180)
    SetChrPos(0x102, -38920, -6000, -57280, 180)
    SetChrPos(0x103, -38930, -5770, -55090, 180)
    SetChrPos(0x104, -37290, -5600, -54400, 180)
    SetChrPos(0x160, -37390, -6000, -56350, 180)
    BeginChrThread(0x103, 3, 0, 21)
    BeginChrThread(0x104, 3, 0, 22)
    BeginChrThread(0x101, 3, 0, 23)
    BeginChrThread(0x102, 3, 0, 24)
    BeginChrThread(0x160, 3, 0, 25)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x160, 3)
    OP_6F(0x79)
    OP_0D()

    #C0040
    ChrTalk(
        0x101,
        (
            "#0012F#11Pはあ、あれを追って\x01",
            "ここまで来ちゃったのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        (
            "#0309F#11Pハハ、随分と\x01",
            "好奇心旺盛なガキンチョだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x160,
        "#3308F#11P……………………………\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        (
            "#0102F#11Pふふ、それじゃあ\x01",
            "保護するとしましょうか……\x02",
        )
    )

    CloseMessageWindow()
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
    Sleep(50)
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0044
    ChrTalk(
        0x102,
        "#0105F#11Pあっ……！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#0201F#11Pあれは……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)

    label("loc_35C0")

    Fade(500)
    OP_68(-56670, -4900, -65600, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21710, 0)
    SetCameraDistance(20710, 2500)
    SetChrPos(0x8, -49720, -6000, -62980, 270)
    SetChrPos(0x10, -52640, -6000, -64410, 270)

    def lambda_3623():
        OP_95(0xFE, -56570, -6000, -65650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3623)

    def lambda_363D():
        OP_95(0xFE, -56570, -6000, -65650, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_363D)
    WaitChrThread(0x10, 1)

    def lambda_365B():
        OP_95(0xFE, -56810, -6000, -74480, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_365B)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x12C)
    WaitChrThread(0x10, 1)
    StopEffect(0x0, 0x0)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)
    Sound(836, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-58670, -4900, -65600, 1000)
    SetCameraDistance(23500, 1000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    BeginChrThread(0x9, 3, 0, 29)
    Sleep(150)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    BeginChrThread(0xA, 3, 0, 30)
    Sleep(50)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    BeginChrThread(0xB, 3, 0, 31)
    Sleep(100)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xC, 3, 0, 32)
    Sleep(150)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 3, 0, 33)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x12C)

    #C0046
    ChrTalk(
        0x8,
        "#3800F#11Pふえ……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    Fade(500)
    OP_68(-43050, -5300, -60890, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20080, 0)
    OP_68(-41050, -5300, -60890, 1500)
    SetChrPos(0x101, -42730, -6000, -61720, 270)
    SetChrPos(0x102, -40700, -6000, -59430, 270)
    SetChrPos(0x103, -41600, -6000, -62430, 270)
    SetChrPos(0x104, -39410, -6000, -60380, 270)
    SetChrPos(0x160, -39980, -6000, -62730, 270)
    OP_6F(0x79)
    OP_0D()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()

    #C0047
    ChrTalk(
        0x101,
        "#0007F#11Pまずい……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        "#0301F#11Pクッ……間に合うか！？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#0110F#11Pあの数だと牽制も……！\x02",
    )

    CloseMessageWindow()
    OP_68(-39730, -5300, -62460, 1000)
    OP_6F(0x79)

    #C0050
    ChrTalk(
        0x160,
        "#3307F#11P……っ……！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetCameraDistance(19080, 0)
    SetChrChipByIndex(0x160, 0x2A)
    SetChrSubChip(0x160, 0x0)
    Sound(540, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_68(-43050, -5300, -60890, 3000)
    SetCameraDistance(22080, 3000)
    BeginChrThread(0x160, 3, 0, 38)
    Sleep(1000)
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

    #C0051
    ChrTalk(
        0x101,
        "#0011F#11Pな……！？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#0205F#11Pレンさん……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-57200, -5400, -67220, 0)
    MoveCamera(325, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24800, 0)
    MoveCamera(335, 25, 0, 2000)
    SetCameraDistance(22300, 2000)
    SetChrPos(0x8, -57200, -6000, -67220, 180)
    SetChrPos(0x160, -44270, -6000, -64030, 270)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 0, 0, 27)
    SetChrPos(0x9, -59130, -6000, -62650, 135)
    SetChrPos(0xA, -61560, -6000, -66330, 90)
    SetChrPos(0xB, -60830, -6000, -70180, 45)
    SetChrPos(0xC, -58140, -6000, -72810, 0)
    SetChrPos(0xD, -55020, -6000, -71640, 315)
    SetChrPos(0xE, -53670, -6000, -69290, 315)
    OP_6F(0x79)
    OP_0D()

    #C0053
    ChrTalk(
        0x8,
        "#3805F#11Pはわ～っ……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0054
    ChrTalk(
        0x160,
        "#3307F#4S#1Pさがりなさいッッ！！\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-52990, -5200, -63660, 2000)
    MoveCamera(13, 22, 0, 2000)
    SetCameraDistance(18000, 2000)
    BeginChrThread(0x160, 3, 0, 39)
    WaitChrThread(0x160, 3)
    OP_6F(0x79)
    OP_0D()
    SetChrChipByIndex(0xF, 0x2C)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x160, 3, 0, 40)
    WaitChrThread(0x160, 3)

    #C0055
    ChrTalk(
        0x8,
        "#3805F……………………………\x02",
    )

    CloseMessageWindow()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(-57360, -4800, -67530, 1200)
    MoveCamera(19, 19, 0, 1200)
    OP_6E(510, 1200)
    SetCameraDistance(16309, 1200)
    BeginChrThread(0x160, 3, 0, 43)

    def lambda_3C39():
        OP_95(0xFE, -54950, -6000, -66690, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C39)
    Sleep(100)

    def lambda_3C56():
        OP_95(0xFE, -53310, -6000, -64470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C56)
    Sleep(100)

    def lambda_3C73():
        OP_95(0xFE, -53510, -6000, -66840, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C73)
    Sleep(100)

    def lambda_3C90():
        OP_95(0xFE, -51780, -6000, -64870, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C90)
    WaitChrThread(0x160, 3)
    BeginChrThread(0x160, 3, 0, 44)
    OP_6F(0x79)
    OP_68(-56410, -4800, -67290, 1500)
    SetCameraDistance(20280, 1500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x160, 3)
    OP_6F(0x79)

    #C0056
    ChrTalk(
        0x160,
        "#3308F#12Pお兄さんたち、お願い……！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#0007F#11P──任せろ！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        "#0307F#11P残りは片付けるぜ！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17280, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    SetChrBattleFlags(0x160, 0x8)
    Battle("BattleInfo_CC8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 34)
    Return()

    # Function_20_2C9A end

    def Function_21_3D8A(): pass

    label("Function_21_3D8A")


    def lambda_3D8F():
        OP_95(0xFE, -41310, -6000, -59840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D8F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_3D8A end

    def Function_22_3DB0(): pass

    label("Function_22_3DB0")


    def lambda_3DB5():
        OP_95(0xFE, -39470, -6000, -59420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DB5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_22_3DB0 end

    def Function_23_3DD6(): pass

    label("Function_23_3DD6")


    def lambda_3DDB():
        OP_95(0xFE, -42730, -6000, -61720, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DDB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_23_3DD6 end

    def Function_24_3DFC(): pass

    label("Function_24_3DFC")


    def lambda_3E01():
        OP_95(0xFE, -41410, -6000, -61870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E01)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_24_3DFC end

    def Function_25_3E22(): pass

    label("Function_25_3E22")


    def lambda_3E27():
        OP_95(0xFE, -39610, -6000, -61340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E27)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_25_3E22 end

    def Function_26_3E48(): pass

    label("Function_26_3E48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E63")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_26_3E48")

    label("loc_3E63")

    Return()

    # Function_26_3E48 end

    def Function_27_3E64(): pass

    label("Function_27_3E64")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E82")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_27_3E64")

    label("loc_3E82")

    Return()

    # Function_27_3E64 end

    def Function_28_3E83(): pass

    label("Function_28_3E83")

    EndChrThread(0xFE, 0x0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3ECB():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3ECB)
    WaitChrThread(0xFE, 1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_28_3E83 end

    def Function_29_3EF9(): pass

    label("Function_29_3EF9")

    SetChrPos(0xFE, -72040, -2800, -70380, 135)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_3F27():
        OP_9D(0xFE, 0xFFFEF8F4, 0xFFFFECDC, 0xFFFEEC9C, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F27)
    WaitChrThread(0xFE, 1)
    Sound(832, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_3F6A():
        OP_9D(0xFE, 0xFFFF0D26, 0xFFFFE890, 0xFFFEF642, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F6A)
    WaitChrThread(0xFE, 1)
    Sound(832, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_29_3EF9 end

    def Function_30_3FB2(): pass

    label("Function_30_3FB2")

    SetChrPos(0xFE, -74740, -2800, -62070, 135)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_3FE0():
        OP_9D(0xFE, 0xFFFEF16A, 0xFFFFECDC, 0xFFFF09FC, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FE0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_401D():
        OP_9D(0xFE, 0xFFFF0998, 0xFFFFE890, 0xFFFF0718, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_401D)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_30_3FB2 end

    def Function_31_405F(): pass

    label("Function_31_405F")

    SetChrPos(0xFE, -69850, -2800, -57770, 90)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_408D():
        OP_9D(0xFE, 0xFFFF1BC2, 0xFFFFE890, 0xFFFF13B6, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_408D)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_31_405F end

    def Function_32_40D6(): pass

    label("Function_32_40D6")

    SetChrPos(0xFE, -71660, -2900, -73300, 135)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_4104():
        OP_9D(0xFE, 0xFFFF03B2, 0xFFFFECDC, 0xFFFEDC98, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4104)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_4141():
        OP_9D(0xFE, 0xFFFF19CE, 0xFFFFE890, 0xFFFEEB8E, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4141)
    WaitChrThread(0xFE, 1)
    Sound(832, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0x2D, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_32_40D6 end

    def Function_33_4190(): pass

    label("Function_33_4190")

    SetChrPos(0xFE, -55440, -6000, -76280, 0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 26)

    def lambda_41B4():
        OP_95(0xFE, -54700, -6000, -70010, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41B4)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_33_4190 end

    def Function_34_41EB(): pass

    label("Function_34_41EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch07200.itc", 0x26)
    LoadChrToIndex("apl/ch50341.itc", 0x2D)
    LoadChrToIndex("apl/ch50364.itc", 0x30)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    ClearChrBattleFlags(0x160, 0x8)
    OP_52(0x160, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-54870, -4600, -64980, 0)
    MoveCamera(356, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21020, 0)
    SetChrPos(0x101, -53640, -6000, -65700, 270)
    SetChrPos(0x102, -52260, -6000, -66520, 270)
    SetChrPos(0x103, -51370, -6000, -64550, 270)
    SetChrPos(0x104, -49730, -6000, -65160, 270)
    SetChrPos(0x160, -55310, -6000, -77360, 270)
    SetChrChipByIndex(0x160, 0x2D)
    SetChrSubChip(0x160, 0x0)
    BeginChrThread(0x160, 0, 0, 45)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -55310, -6000, -77360, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(19020, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0059
    ChrTalk(
        0x101,
        "#0006F#11Pふう……\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        "#0306F#2P正直、危なかったぜ……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0061
    ChrTalk(
        0x102,
        (
            "#0101F#11Pそうだ……\x01",
            "レンちゃんとコリン君は！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    def lambda_4469():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4469)

    def lambda_4476():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4476)
    Sleep(100)

    def lambda_4486():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4486)

    def lambda_4493():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4493)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(1000)
    SetChrPos(0x101, -55430, -6000, -70010, 180)
    SetChrPos(0x102, -56590, -6000, -69430, 180)
    SetChrPos(0x103, -55010, -6000, -68390, 180)
    SetChrPos(0x104, -55580, -6000, -67260, 180)
    OP_68(-55580, -4500, -75880, 0)
    MoveCamera(36, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16870, 0)
    OP_68(-55580, -5200, -75880, 3000)

    def lambda_4538():
        OP_95(0xFE, -55430, -6000, -75010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4538)

    def lambda_4552():
        OP_95(0xFE, -56590, -6000, -74430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4552)

    def lambda_456C():
        OP_95(0xFE, -55010, -6000, -73390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_456C)

    def lambda_4586():
        OP_95(0xFE, -55580, -6000, -72260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4586)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_0D()

    #C0062
    ChrTalk(
        0x8,
        "#3805F#12P#40W……………………………\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    #C0063
    ChrTalk(
        0x160,
        (
            "#3308F#5P#30W……もう、大丈夫よ。\x02\x03",

            "#3306Fコワイ魔獣はお兄さんたちが\x01",
            "退治してくれたから……\x02\x03",

            "#3300Fだから、安心してもいいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        "#3810F#60W#12Pふえっ……うくっ……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x160,
        "#3305F#5Pちょ、ちょっと……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "#3810F#60W#12Pうううううっ……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0067
    ChrTalk(
        0x8,
        "#3811F#4S#12Pうわああああああああん！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x160, 0x0)
    BeginChrThread(0x160, 0, 0, 46)
    Sleep(500)

    #C0068
    ChrTalk(
        0x160,
        (
            "#3311F#5P#30Wど、どうして泣くのよ……\x01",
            "もう危なくないって言ってるのに……\x02\x03",

            "#3308F#40Wあなたなんか……あなたなんか……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0069
    ChrTalk(
        0x160,
        (
            "#3310F#5P#4S本当は助けるつもりなんて……\x01",
            "……ゼンゼンなかったのに……！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x160, 0x0)
    SetChrSubChip(0x160, 0xB)

    #C0070
    ChrTalk(
        0x101,
        "#0008F#5P……レン……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        "#0208F#5Pレンさん……\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_A1(0x160, 0x5DC, 0x4, 0x1, 0x2, 0x3, 0x4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0072
    ChrTalk(
        0x160,
        (
            "#3310F#5Pバカみたい……！\x01",
            "#30W……ほんとバカみたい……！\x02\x03",

            "#30W見てるだけって決めたのに……！\x01",
            "絶対に関わらないって決めたのに……！\x02\x03",

            "#3313F#30Wどうして……どうしてレンは……！\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#0108F#5Pレンちゃん……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#0003F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15370, 3000)
    OP_68(-54730, -5200, -76500, 3000)

    def lambda_4972():
        OP_96(0xFE, 0xFFFF2D1A, 0xFFFFE890, 0xFFFED220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4972)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x12C)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x30)
    SetChrSubChip(0x101, 0x5)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0075
    ChrTalk(
        0x101,
        (
            "#0004F#11P──君の事情は知らない。\x02\x03",

            "#0000Fでも、きっと君は\x01",
            "君の大切なものを守ったんだ。\x02\x03",

            "他ならぬ君自身の手で。\x02\x03",

            "#0004Fその腕に感じてる\x01",
            "ぬくもりが何よりの証拠だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x160,
        "#3312F#5Pっ……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#0006F#11P不甲斐ないけど、俺たちは\x01",
            "君の手伝いをしただけだった。\x02\x03",

            "#0000Fでも、それでも光栄に思う。\x02\x03",

            "#0002Fレン──君が君の大切なものを\x01",
            "守る手伝いができて。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x160, 0x708, 0x4, 0x15, 0x16, 0x15, 0x14)
    Sleep(150)
    OP_A1(0x160, 0x4B0, 0x8, 0x15, 0x16, 0x15, 0x14, 0x15, 0x16, 0x15, 0x14)
    Sleep(300)

    #C0078
    ChrTalk(
        0x160,
        "#3313F#60W#5Pううっ……ああっ……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetCameraDistance(20000, 4000)
    Sound(804, 0, 100, 0)
    OP_A1(0x160, 0x7D0, 0x3, 0x5, 0x6, 0x7)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0079
    ChrTalk(
        0x160,
        "#3310F#4S#5P#70W#25Aうわああああああああん！\x02",
    )
    #Auto


    #C0080
    ChrTalk(
        0x8,
        "#3811F#4S#12P#70W#25Aふえええええええんんん！\x02",
    )
    #Auto

    Sleep(1000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_41EB end

    def Function_35_4C0C(): pass

    label("Function_35_4C0C")


    def lambda_4C11():
        OP_95(0xFE, -39960, -6000, -63090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C11)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(100)

    def lambda_4C43():
        OP_95(0xFE, -42950, -6000, -63260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C43)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xFA, 0x12C)
    Sleep(100)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(100)

    def lambda_4C75():
        OP_95(0xFE, -45050, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C75)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(200)

    def lambda_4CA7():
        OP_95(0xFE, -51480, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CA7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_35_4C0C end

    def Function_36_4CC1(): pass

    label("Function_36_4CC1")


    def lambda_4CC6():
        OP_95(0xFE, -42950, -6000, -63260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CC6)
    WaitChrThread(0xFE, 1)
    Sleep(700)

    def lambda_4CE7():
        OP_95(0xFE, -45050, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CE7)
    WaitChrThread(0xFE, 1)
    Sleep(1100)

    def lambda_4D08():
        OP_95(0xFE, -51480, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D08)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_4CC1 end

    def Function_37_4D22(): pass

    label("Function_37_4D22")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D3D")
    OP_A1(0xFE, 0x1388, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_37_4D22")

    label("loc_4D3D")

    Return()

    # Function_37_4D22 end

    def Function_38_4D3E(): pass

    label("Function_38_4D3E")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0x160, 0x2A)
    SetChrSubChip(0x160, 0x4)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_4D5D():
        OP_9D(0xFE, 0xFFFF54B6, 0xFFFFE890, 0xFFFF0178, 0x384, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D5D)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    SetChrSubChip(0x160, 0x0)
    BeginChrThread(0xFE, 0, 0, 37)

    def lambda_4D91():
        OP_95(0xFE, -53880, -6000, -64819, 15000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D91)
    Sound(250, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_38_4D3E end

    def Function_39_4DC7(): pass

    label("Function_39_4DC7")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0x160, 0x2A)
    SetChrSubChip(0x160, 0x0)
    BeginChrThread(0xFE, 0, 0, 37)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_4DEC():
        OP_95(0xFE, -52890, -6000, -63420, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DEC)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_93(0x160, 0xB4, 0x320)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0x160, 0x2B)
    SetChrSubChip(0x160, 0x0)
    Return()

    # Function_39_4DC7 end

    def Function_40_4E2B(): pass

    label("Function_40_4E2B")

    SetChrChipByIndex(0x160, 0x2B)
    SetChrSubChip(0x160, 0x0)
    Sound(540, 0, 100, 0)
    Sound(804, 0, 100, 0)
    SetCameraDistance(15500, 1000)
    OP_A1(0xFE, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    OP_6F(0x79)
    OP_A1(0xFE, 0xFA0, 0x1, 0x3)
    OP_68(-54280, -4700, -69480, 750)
    MoveCamera(13, 18, 0, 750)
    SetCameraDistance(21840, 750)
    Sound(912, 0, 100, 0)
    OP_82(0x96, 0x0, 0x1B58, 0x5DC)
    BeginChrThread(0xF, 3, 0, 41)
    OP_A1(0xFE, 0x7D0, 0x1, 0x4)
    Sleep(400)
    BeginChrThread(0xE, 3, 0, 28)
    Sound(502, 0, 100, 0)
    Sleep(200)
    BeginChrThread(0xD, 3, 0, 28)
    Sound(502, 0, 100, 0)
    Sleep(500)
    OP_6F(0x79)
    OP_68(-52990, -5200, -63660, 2000)
    MoveCamera(13, 22, 0, 2000)
    SetCameraDistance(18000, 2000)
    Sleep(1500)
    OP_A1(0xFE, 0x7D0, 0x3, 0x5, 0x6, 0x7)
    WaitChrThread(0xF, 3)
    OP_82(0x64, 0x0, 0x1B58, 0x12C)
    Fade(250)
    SetChrSubChip(0x160, 0x0)
    OP_0D()
    OP_6F(0x79)
    Return()

    # Function_40_4E2B end

    def Function_41_4F19(): pass

    label("Function_41_4F19")

    PlayEffect(0x2, 0x1, 0xFE, 0x40, 0, -800, 0, 0, 0, 0, 1750, 1000, 1750, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x800)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0xFE, 0, 0, 42)
    SetChrPos(0xFE, -52890, -6000, -63420, 270)

    def lambda_4F7C():
        OP_96(0xFE, 0xFFFF2644, 0xFFFFE890, 0xFFFED626, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F7C)
    WaitChrThread(0xFE, 1)

    def lambda_4F9A():
        OP_96(0xFE, 0xFFFF3166, 0xFFFFE890, 0xFFFF0844, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F9A)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x800)
    StopEffect(0x1, 0x2)
    Return()

    # Function_41_4F19 end

    def Function_42_4FCB(): pass

    label("Function_42_4FCB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FE9")
    OP_A1(0xFE, 0x1B58, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_42_4FCB")

    label("loc_4FE9")

    Return()

    # Function_42_4FCB end

    def Function_43_4FEA(): pass

    label("Function_43_4FEA")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0x160, 0x2A)
    SetChrSubChip(0x160, 0x0)

    def lambda_4FFC():
        OP_95(0xFE, -57200, -6000, -67220, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4FFC)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_43_4FEA end

    def Function_44_501F(): pass

    label("Function_44_501F")

    Fade(250)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x12)
    Sound(804, 0, 100, 0)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_0D()
    Sound(854, 0, 100, 0)

    def lambda_505D():
        OP_9D(0xFE, 0xFFFF3576, 0xFFFFE890, 0xFFFEF2BE, 0x2BC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_505D)
    WaitChrThread(0xFE, 1)
    Sound(31, 0, 100, 0)
    Sound(30, 0, 100, 0)
    SetChrSubChip(0xFE, 0x13)
    Return()

    # Function_44_501F end

    def Function_45_508A(): pass

    label("Function_45_508A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50A8")
    OP_A1(0xFE, 0x3E8, 0x5, 0x8, 0x9, 0xA, 0x9, 0x0)
    Sleep(4000)
    Jump("Function_45_508A")

    label("loc_50A8")

    Return()

    # Function_45_508A end

    def Function_46_50A9(): pass

    label("Function_46_50A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50C6")
    OP_A1(0xFE, 0x5DC, 0x4, 0xB, 0xC, 0xD, 0xC)
    Sleep(3000)
    Jump("Function_46_50A9")

    label("loc_50C6")

    Return()

    # Function_46_50A9 end

    def Function_47_50C7(): pass

    label("Function_47_50C7")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1D, 0x80)
    OP_68(-57720, -5200, -61820, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, -57910, -6000, -62950, 270)
    SetChrPos(0x102, -58320, -6000, -61520, 225)
    SetChrPos(0x103, -57190, -6000, -63960, 270)
    SetChrPos(0x104, -56700, -6000, -61250, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_517C")
    SetChrPos(0x10A, -56130, -6000, -61940, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_517C")

    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x349),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x349, 1)

    #C0082
    ChrTalk(
        0x101,
        (
            "#12P#0000F黄色い花……\x01",
            "これがレヴァスの花で\x01",
            "間違いなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#5P#0306Fしかし……\x01",
            "こんなところに咲いてたら\x01",
            "市民は摘みに来にくいだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        "#12P#0200F警察学校の目の前ですしね。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#6P#0103F群生している場所も\x01",
            "バラバラだから、元々\x01",
            "３色を揃えるのは大変なの。\x02\x03",

            "#0100Fだから普段の墓参りでは\x01",
            "どれか１色でもいいっていう\x01",
            "風潮に変わってきてるの。\x02\x03",

            "３色の花束が使われるのは、\x01",
            "それこそ葬儀の時くらいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        "#5P#0305Fへぇ、そうなのか？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53C6")

    #C0087
    ChrTalk(
        0x10A,
        "#11P#0603F時代の流れ、というものだ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_53FD")

    label("loc_53C6")


    #C0088
    ChrTalk(
        0x103,
        (
            "#12P#0200F伝統も段々\x01",
            "合理的になっているんですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53FD")


    #C0089
    ChrTalk(
        0x101,
        (
            "#12P#0003Fまぁ……得てして\x01",
            "そういうものなのかもな。\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x9, 0x1)
    OP_29(0x2E, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5463")
    OP_29(0x2E, 0x1, 0x6)

    label("loc_5463")

    ClearMapFlags(0x8000000)
    OP_37()
    Call(0, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5486")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_5486")

    SetChrPos(0x0, -57910, -6000, -62950, 270)
    EventEnd(0x5)
    Return()

    # Function_47_50C7 end

    def Function_48_549A(): pass

    label("Function_48_549A")

    EventBegin(0x1)

    #C0090
    ChrTalk(
        0x101,
        (
            "#0001F声がしたのはこっちじゃない……\x01",
            "南の方に急ごう！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -32500, 0, 26090, 225)
    EventEnd(0x4)
    Return()

    # Function_48_549A end

    def Function_49_54EE(): pass

    label("Function_49_54EE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0091
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BBB")
    EventBegin(0x0)
    SetChrFlags(0x1D, 0x80)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    Fade(500)
    OP_68(-49100, -5400, -95960, 0)
    MoveCamera(123, 26, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24710, 0)
    SetChrPos(0x101, -53560, -6000, -80120, 180)
    SetChrPos(0x102, -54580, -6000, -78550, 180)
    SetChrPos(0x103, -51530, -6000, -79120, 180)
    SetChrPos(0x104, -52490, -6000, -77690, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5607")
    SetChrPos(0x10A, -51490, -6000, -76540, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_5607")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5632")
    SetChrPos(0x109, -51490, -6000, -76540, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_5632")

    OP_0D()
    OP_68(-50470, -5400, -82530, 6000)
    MoveCamera(134, 26, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(24710, 6000)
    OP_6F(0x79)

    #C0092
    ChrTalk(
        0x102,
        "#0100Fその先が警察学校みたいね。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#0204Fロイドさんが\x01",
            "在籍していた場所ですか。\x02\x03",

            "#0202Fなかなか設備の充実した\x01",
            "養成学校だと聞いていますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#0004Fああ、それ以外にも\x01",
            "公的施設や警備隊の演習場が\x01",
            "併設されている場所なんだ。\x02\x03",

            "#0000Fこの門を抜けると\x01",
            "長い森林道が続いていて\x01",
            "各施設が点在している。\x02\x03",

            "#0012F……といっても、俺もこの門は\x01",
            "通ったことが無いんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_586B")

    def lambda_57E3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57E3)
    Sleep(60)

    def lambda_57F3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_57F3)
    Sleep(60)

    def lambda_5803():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5803)
    Sleep(60)

    def lambda_5813():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5813)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Jump("loc_590B")

    label("loc_586B")


    def lambda_5870():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5870)
    Sleep(60)

    def lambda_5880():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5880)
    Sleep(60)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5908")

    def lambda_58E8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_58E8)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_5908")

    Sleep(1000)

    label("loc_590B")


    #C0095
    ChrTalk(
        0x102,
        "#0105Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        "#0305Fどういう事だ？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0097
    ChrTalk(
        0x101,
        (
            "#0000F#11P駅で貨物車両に乗り換えて\x01",
            "直接警察学校の方に行ったんだ。\x02\x03",

            "それから数ヶ月、寮暮らしで\x01",
            "カンヅメだったわけさ。\x02\x03",

            "#0006F捜査官試験に挑戦するために\x01",
            "たまの休日も勉強漬けだったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        "#0100Fそうだったの……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0301Fなんだなんだ～？\x01",
            "いい若いモンがけしからんな。\x02\x03",

            "#0309Fやっぱ休日の過ごし方と言えば\x01",
            "カジノに夜遊びが基本だろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        (
            "#0206Fそれはランディさんだけの\x01",
            "基本でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#0002F#11P……はは………\x02\x03",

            "#0008F（捜査官資格を手に入れるまでは\x01",
            "  クロスベル市には戻らない……）\x02\x03",

            "#0006F（……我ながら子供っぽすぎる\x01",
            "  こだわりだったかもな……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B85")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_5B85")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B9F")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_5B9F")

    SetScenarioFlags(0x95, 4)
    SetChrPos(0x0, -52380, -6000, -78750, 180)
    ClearMapFlags(0x8000000)
    OP_37()
    EventEnd(0x5)

    label("loc_5BBB")

    TalkEnd(0xFF)
    Return()

    # Function_49_54EE end

    def Function_50_5BBF(): pass

    label("Function_50_5BBF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0102
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

    # Function_50_5BBF end

    SaveToFile()

Try(main)
