from ZeroScenarioHelper import *

def main():
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
        "柯林",                   # 1
        "ＢＯＳＳ１",             # 2
        "ＢＯＳＳ２",             # 3
        "ＢＯＳＳ３",             # 4
        "ＢＯＳＳ４",             # 5
        "ＢＯＳＳ５",             # 6
        "ＢＯＳＳ６",             # 7
        "卡玛",                   # 8
        "蝴蝶",                   # 9
        "巴士",                   # 10
        "火焰蛇虎鱼",             # 11
        "br1000",                 # 12
        "br1000",                 # 13
        "br1000",                 # 14
        "br1000",                 # 15
        "br1000",                 # 16
        "br1000",                 # 17
        "br1000",                 # 18
        "br1000",                 # 19
        "br1000",                 # 20
        "克洛斯贝尔方向",         # 21
        "贝尔加德门方向",         # 22
    ))

    ATBonus("ATBonus_738", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_5A16", 0,   0,   13,  1,   5,   7,   4)
    Sepith("Sepith_5A1E", 2,   1,   0,   0,   9,   9,   9)
    Sepith("Sepith_5A2E", 4,   4,   10,  2,   0,   5,   5)
    Sepith("Sepith_59F6", 4,   2,   11,  0,   0,   8,   5)
    Sepith("Sepith_59FE", 0,   8,   0,   12,  4,   8,   0)
    Sepith("Sepith_5A3E", 12,  7,   4,   3,   6,   14,  7)

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
        "BattleInfo_920", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_5A16", 30, 40, 20, 10,
        (
            ("ms71300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71300.dat", "ms71300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71300.dat", "ms70400.dat", "ms71300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71300.dat", "ms71300.dat", "ms70400.dat", "ms71300.dat", 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
        )
    )

    BattleInfo(
        "BattleInfo_AB0", 0x0000, 17, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_5A1E", 30, 40, 20, 10,
        (
            ("ms64200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms64200.dat", "ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms64200.dat", "ms66900.dat", "ms64200.dat", "ms66900.dat", 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
        )
    )

    BattleInfo(
        "BattleInfo_9E8", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_5A2E", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms71900.dat", "ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
        )
    )

    BattleInfo(
        "BattleInfo_B78", 0x0000, 17, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_59F6", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
        )
    )

    BattleInfo(
        "BattleInfo_858", 0x0000, 17, 6, 60, 8, 1, 40, 0, "br1000", "Sepith_59FE", 30, 40, 20, 10,
        (
            ("ms70300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms70300.dat", "ms70300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_798", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
            ("ms70300.dat", "ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, "MonsterBattlePostion_778", "MonsterBattlePostion_7F8", "ed7400", "ed7403", "ATBonus_738"),
        )
    )

    BattleInfo(
        "BattleInfo_D0C", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br1000", "Sepith_5A3E", 40, 35, 25, 0,
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

    PlaceName(29.0, 0.0, 19.0, 0x0000, 0x0000, "克洛斯贝尔方向")
    PlaceName(-95.0, 0.0, 84.0, 0x0000, 0x0000, "贝尔加德门方向")
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
        "Function_6_1B56",         # 06, 6
        "Function_7_1C3F",         # 07, 7
        "Function_8_1D75",         # 08, 8
        "Function_9_1D89",         # 09, 9
        "Function_10_1D9D",        # 0A, 10
        "Function_11_1DB1",        # 0B, 11
        "Function_12_2378",        # 0C, 12
        "Function_13_239B",        # 0D, 13
        "Function_14_244A",        # 0E, 14
        "Function_15_256E",        # 0F, 15
        "Function_16_268F",        # 10, 16
        "Function_17_2724",        # 11, 17
        "Function_18_27EC",        # 12, 18
        "Function_19_28DB",        # 13, 19
        "Function_20_2B8E",        # 14, 20
        "Function_21_3C4C",        # 15, 21
        "Function_22_3C72",        # 16, 22
        "Function_23_3C98",        # 17, 23
        "Function_24_3CBE",        # 18, 24
        "Function_25_3CE4",        # 19, 25
        "Function_26_3D0A",        # 1A, 26
        "Function_27_3D26",        # 1B, 27
        "Function_28_3D45",        # 1C, 28
        "Function_29_3DBB",        # 1D, 29
        "Function_30_3E74",        # 1E, 30
        "Function_31_3F21",        # 1F, 31
        "Function_32_3F98",        # 20, 32
        "Function_33_4052",        # 21, 33
        "Function_34_40AD",        # 22, 34
        "Function_35_4A4C",        # 23, 35
        "Function_36_4B01",        # 24, 36
        "Function_37_4B62",        # 25, 37
        "Function_38_4B7E",        # 26, 38
        "Function_39_4C07",        # 27, 39
        "Function_40_4C6B",        # 28, 40
        "Function_41_4D59",        # 29, 41
        "Function_42_4E0B",        # 2A, 42
        "Function_43_4E2A",        # 2B, 43
        "Function_44_4E5F",        # 2C, 44
        "Function_45_4ECA",        # 2D, 45
        "Function_46_4EE9",        # 2E, 46
        "Function_47_4F07",        # 2F, 47
        "Function_48_528E",        # 30, 48
        "Function_49_52DA",        # 31, 49
        "Function_50_591B",        # 32, 50
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B18")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A55")
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
            "出现了魔兽！\x07\x00\x02",
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
        (0, "loc_1A36"),
        (2, "loc_1A45"),
        (1, "loc_1A52"),
        (SWITCH_DEFAULT, "loc_1A55"),
    )


    label("loc_1A36")

    SetScenarioFlags(0x74, 5)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_1A55")

    label("loc_1A45")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1A52")

    OP_B7(0x0)
    Return()

    label("loc_1A55")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('影丸雪踏', 1)"), scpexpr(EXPR_END)), "loc_1AAC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '影丸雪踏'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x118, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1B13")

    label("loc_1AAC")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '影丸雪踏'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '影丸雪踏'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1B13")

    Jump("loc_1B4A")

    label("loc_1B18")

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

    label("loc_1B4A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_195C end

    def Function_6_1B56(): pass

    label("Function_6_1B56")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C10")
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
            "#60I时之耀晶片×６０\x01\x07\x02",

            "#61I空之耀晶片×６０\x01\x07\x02",

            "#62I幻之耀晶片×６０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x119, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1C2D")

    label("loc_1C10")


    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1C2D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1B56 end

    def Function_7_1C3F(): pass

    label("Function_7_1C3F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2C")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('中回复药', 1)"), scpexpr(EXPR_END)), "loc_1CBE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x119, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1D27")

    label("loc_1CBE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D27")

    Jump("loc_1D69")

    label("loc_1D2C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_1D69")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1C3F end

    def Function_8_1D75(): pass

    label("Function_8_1D75")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 7)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1D75 end

    def Function_9_1D89(): pass

    label("Function_9_1D89")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 0)
    OP_65(0x7, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_9_1D89 end

    def Function_10_1D9D(): pass

    label("Function_10_1D9D")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 1)
    OP_65(0x8, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_10_1D9D end

    def Function_11_1DB1(): pass

    label("Function_11_1DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 2)), scpexpr(EXPR_END)), "loc_1DBB")
    Return()

    label("loc_1DBB")

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
            "大型魔兽正在四处游荡。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【消灭】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1E87"),
        (SWITCH_DEFAULT, "loc_1E9E"),
    )


    label("loc_1E87")

    Sleep(500)
    OP_90(0x0, -32290, 0, 1830, 270)
    EventEnd(0x5)
    Return()

    label("loc_1E9E")

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
        (2, "loc_1F60"),
        (1, "loc_1F63"),
        (SWITCH_DEFAULT, "loc_1F66"),
    )


    label("loc_1F60")

    EventEnd(0x5)
    Return()

    label("loc_1F63")

    OP_B7(0x0)
    Return()

    label("loc_1F66")

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
            "消灭了通缉魔兽！\x02",
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
        "#0106F呼，真是强敌啊。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#0300F嗯，意外地难缠啊。\x02\x03",

            "我在警备队时，\x01",
            "也来过这边好几次，\x01",
            "但从没见过这种类型的魔兽啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 2)), scpexpr(EXPR_END)), "loc_2139")

    #C0014
    ChrTalk(
        0x103,
        (
            "#0202F不过，这样的话，\x01",
            "巴士应该就能恢复运行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0000F是啊，\x01",
            "联络市政厅吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EC")

    label("loc_2139")


    #C0016
    ChrTalk(
        0x101,
        (
            "#0008F是吗……\x01",
            "而且竟然在道路的正中，\x01",
            "是有点令人担心啊。\x02\x03",

            "这附近应该\x01",
            "还有巴士站。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#0200F巴士的运行\x01",
            "似乎也会受到影响呢。\x02\x03",

            "还是联络市政厅\x01",
            "比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#0000F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_21EC")

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
            "罗伊德联络市政厅，\x01",
            "传达了已将郊外的魔兽消灭的消息。\x02",
        )
    )

    CloseMessageWindow()

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "巴士似乎马上可以恢复运行了。\x02",
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
            "西克洛斯贝尔街道的巴士恢复了运行。\x07\x00\x02",
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

    # Function_11_1DB1 end

    def Function_12_2378(): pass

    label("Function_12_2378")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_239A")
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)

    label("loc_239A")

    Return()

    # Function_12_2378 end

    def Function_13_239B(): pass

    label("Function_13_239B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0022
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
            "克洛斯贝尔市西出口\x01",      # 0
            "贝尔加德门\x01",              # 1
            "放弃\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2422")
    Call(0, 14)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2442")

    label("loc_2422")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2442")
    Call(0, 15)
    ClearMapFlags(0x8000000)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()

    label("loc_2442")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_239B end

    def Function_14_244A(): pass

    label("Function_14_244A")

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

    def lambda_2525():
        OP_95(0xFE, -43990, 0, 13530, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2525)
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

    # Function_14_244A end

    def Function_15_256E(): pass

    label("Function_15_256E")

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

    def lambda_2649():
        OP_95(0xFE, -39660, 0, 1670, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2649)
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

    # Function_15_256E end

    def Function_16_268F(): pass

    label("Function_16_268F")

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

    # Function_16_268F end

    def Function_17_2724(): pass

    label("Function_17_2724")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0023
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27E7")
    OP_E0(0x2)
    MiniGame(0x6, 0x12, 0xFFFF0D4E, 0x0, 0x8804, 0x0, 0xFFFF0ACE, 0xFFFFFC18, 0x9D94)

    label("loc_27E7")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_17_2724 end

    def Function_18_27EC(): pass

    label("Function_18_27EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_288B")
    TalkBegin(0xFF)

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x02",
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
            "由于接到有凶恶魔兽出没的通报，\x01",
            "现在暂停运行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x95, 2)
    TalkEnd(0xFF)
    Jump("loc_28DA")

    label("loc_288B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28D7")
    TalkBegin(0xFF)

    #C0027
    ChrTalk(
        0x101,
        (
            "#0001F现在不是等巴士的时候……\x01",
            "快去找柯林吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_28DA")

    label("loc_28D7")

    Call(0, 13)

    label("loc_28DA")

    Return()

    # Function_18_27EC end

    def Function_19_28DB(): pass

    label("Function_19_28DB")

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
    SetChrName("小孩子的声音")

    #A0028
    AnonymousTalk(
        0xFF,
        "#2S呀哈哈……！\x02",
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
        "#0005F#11P刚才的是……！？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        "#0108F#11P从、从哪里传来的！？\x02",
    )

    CloseMessageWindow()

    def lambda_2A80():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A80)
    Sleep(50)

    def lambda_2A90():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A90)
    Sleep(50)

    def lambda_2AA0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2AA0)
    Sleep(300)

    #C0031
    ChrTalk(
        0x103,
        "#0202F#5P……是从南边。\x02",
    )

    CloseMessageWindow()

    def lambda_2ACD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ACD)
    Sleep(50)

    def lambda_2ADD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2ADD)
    Sleep(300)

    #C0032
    ChrTalk(
        0x104,
        (
            "#0300F#5P嗯……\x01",
            "是警察学校的方向吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0000F#5P好，赶快去吧……！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x160,
        "#3308F#11P#40W（……似乎平安无事呢。）\x02",
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

    # Function_19_28DB end

    def Function_20_2B8E(): pass

    label("Function_20_2B8E")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CBD")
    SetChrPos(0x101, -38330, -4000, -48020, 180)
    SetChrPos(0x102, -39320, -4000, -47210, 180)
    SetChrPos(0x103, -37450, -4000, -46640, 180)
    SetChrPos(0x104, -37440, -4000, -45160, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)
    Jump("loc_2DF0")

    label("loc_2CBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D25")
    SetChrPos(0x101, -39320, -4000, -47210, 180)
    SetChrPos(0x102, -38330, -4000, -48020, 180)
    SetChrPos(0x103, -37450, -4000, -46640, 180)
    SetChrPos(0x104, -37440, -4000, -45160, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)
    Jump("loc_2DF0")

    label("loc_2D25")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D8D")
    SetChrPos(0x101, -37450, -4000, -46640, 180)
    SetChrPos(0x102, -39320, -4000, -47210, 180)
    SetChrPos(0x103, -38330, -4000, -48020, 180)
    SetChrPos(0x104, -37440, -4000, -45160, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)
    Jump("loc_2DF0")

    label("loc_2D8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF0")
    SetChrPos(0x101, -37440, -4000, -45160, 180)
    SetChrPos(0x102, -39320, -4000, -47210, 180)
    SetChrPos(0x103, -37450, -4000, -46640, 180)
    SetChrPos(0x104, -38330, -4000, -48020, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)

    label("loc_2DF0")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3119")

    #C0035
    ChrTalk(
        0x101,
        "#0002F#5P有了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_31A4")

    label("loc_3119")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3147")

    #C0036
    ChrTalk(
        0x102,
        "#0102F#5P找到了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_31A4")

    label("loc_3147")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_317B")

    #C0037
    ChrTalk(
        0x103,
        "#0202F#5P发现第一目标……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_31A4")

    label("loc_317B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31A4")

    #C0038
    ChrTalk(
        0x104,
        "#0302F#5P找到了……！\x02",
    )

    CloseMessageWindow()

    label("loc_31A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3490")
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
            "#3809F#5P呀哈哈！\x02\x03",

            "#3802F等等，等等啦～！\x02",
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
            "#0012F#11P呼，追着那个，\x01",
            "一直跑到了这里吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        (
            "#0309F#11P哈哈，还真是个\x01",
            "好奇心旺盛的小鬼啊。\x02",
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
            "#0102F#11P呵呵，那么，\x01",
            "赶快把他保护起来吧……\x02",
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
        "#0105F#11P啊……！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#0201F#11P那是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)

    label("loc_3490")

    Fade(500)
    OP_68(-56670, -4900, -65600, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21710, 0)
    SetCameraDistance(20710, 2500)
    SetChrPos(0x8, -49720, -6000, -62980, 270)
    SetChrPos(0x10, -52640, -6000, -64410, 270)

    def lambda_34F3():
        OP_95(0xFE, -56570, -6000, -65650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_34F3)

    def lambda_350D():
        OP_95(0xFE, -56570, -6000, -65650, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_350D)
    WaitChrThread(0x10, 1)

    def lambda_352B():
        OP_95(0xFE, -56810, -6000, -74480, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_352B)
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
        "#3800F#11P哎……？\x02",
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
        "#0007F#11P糟了……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        "#0301F#11P唔……还来得及吗！？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#0110F#11P那种数量的话，要牵制也很困难……！\x02",
    )

    CloseMessageWindow()
    OP_68(-39730, -5300, -62460, 1000)
    OP_6F(0x79)

    #C0050
    ChrTalk(
        0x160,
        "#3307F#11P……唔……！\x02",
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
        "#0011F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#0205F#11P玲……！？\x02",
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
        "#3805F#11P啊哇～……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0054
    ChrTalk(
        0x160,
        "#3307F#4S#1P快退后！！\x02",
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

    def lambda_3AFF():
        OP_95(0xFE, -54950, -6000, -66690, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AFF)
    Sleep(100)

    def lambda_3B1C():
        OP_95(0xFE, -53310, -6000, -64470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B1C)
    Sleep(100)

    def lambda_3B39():
        OP_95(0xFE, -53510, -6000, -66840, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3B39)
    Sleep(100)

    def lambda_3B56():
        OP_95(0xFE, -51780, -6000, -64870, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B56)
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
        "#3308F#12P大哥哥，拜托了……！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#0007F#11P──交给我们吧！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        "#0307F#11P把剩下的收拾掉！\x02",
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

    # Function_20_2B8E end

    def Function_21_3C4C(): pass

    label("Function_21_3C4C")


    def lambda_3C51():
        OP_95(0xFE, -41310, -6000, -59840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C51)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_3C4C end

    def Function_22_3C72(): pass

    label("Function_22_3C72")


    def lambda_3C77():
        OP_95(0xFE, -39470, -6000, -59420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C77)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_22_3C72 end

    def Function_23_3C98(): pass

    label("Function_23_3C98")


    def lambda_3C9D():
        OP_95(0xFE, -42730, -6000, -61720, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C9D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_23_3C98 end

    def Function_24_3CBE(): pass

    label("Function_24_3CBE")


    def lambda_3CC3():
        OP_95(0xFE, -41410, -6000, -61870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CC3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_24_3CBE end

    def Function_25_3CE4(): pass

    label("Function_25_3CE4")


    def lambda_3CE9():
        OP_95(0xFE, -39610, -6000, -61340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CE9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_25_3CE4 end

    def Function_26_3D0A(): pass

    label("Function_26_3D0A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D25")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_26_3D0A")

    label("loc_3D25")

    Return()

    # Function_26_3D0A end

    def Function_27_3D26(): pass

    label("Function_27_3D26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D44")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_27_3D26")

    label("loc_3D44")

    Return()

    # Function_27_3D26 end

    def Function_28_3D45(): pass

    label("Function_28_3D45")

    EndChrThread(0xFE, 0x0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3D8D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D8D)
    WaitChrThread(0xFE, 1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_28_3D45 end

    def Function_29_3DBB(): pass

    label("Function_29_3DBB")

    SetChrPos(0xFE, -72040, -2800, -70380, 135)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_3DE9():
        OP_9D(0xFE, 0xFFFEF8F4, 0xFFFFECDC, 0xFFFEEC9C, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DE9)
    WaitChrThread(0xFE, 1)
    Sound(832, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_3E2C():
        OP_9D(0xFE, 0xFFFF0D26, 0xFFFFE890, 0xFFFEF642, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E2C)
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

    # Function_29_3DBB end

    def Function_30_3E74(): pass

    label("Function_30_3E74")

    SetChrPos(0xFE, -74740, -2800, -62070, 135)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_3EA2():
        OP_9D(0xFE, 0xFFFEF16A, 0xFFFFECDC, 0xFFFF09FC, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EA2)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_3EDF():
        OP_9D(0xFE, 0xFFFF0998, 0xFFFFE890, 0xFFFF0718, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EDF)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_30_3E74 end

    def Function_31_3F21(): pass

    label("Function_31_3F21")

    SetChrPos(0xFE, -69850, -2800, -57770, 90)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_3F4F():
        OP_9D(0xFE, 0xFFFF1BC2, 0xFFFFE890, 0xFFFF13B6, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F4F)
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

    # Function_31_3F21 end

    def Function_32_3F98(): pass

    label("Function_32_3F98")

    SetChrPos(0xFE, -71660, -2900, -73300, 135)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_3FC6():
        OP_9D(0xFE, 0xFFFF03B2, 0xFFFFECDC, 0xFFFEDC98, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FC6)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_4003():
        OP_9D(0xFE, 0xFFFF19CE, 0xFFFFE890, 0xFFFEEB8E, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4003)
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

    # Function_32_3F98 end

    def Function_33_4052(): pass

    label("Function_33_4052")

    SetChrPos(0xFE, -55440, -6000, -76280, 0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 26)

    def lambda_4076():
        OP_95(0xFE, -54700, -6000, -70010, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4076)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_33_4052 end

    def Function_34_40AD(): pass

    label("Function_34_40AD")

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
        "#0006F#11P呼……\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        "#0306F#2P说实话，真是好险啊……\x02",
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
            "#0101F#11P对了……\x01",
            "小玲和柯林呢！？\x02",
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

    def lambda_431D():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_431D)

    def lambda_432A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_432A)
    Sleep(100)

    def lambda_433A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_433A)

    def lambda_4347():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4347)
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

    def lambda_43EC():
        OP_95(0xFE, -55430, -6000, -75010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43EC)

    def lambda_4406():
        OP_95(0xFE, -56590, -6000, -74430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4406)

    def lambda_4420():
        OP_95(0xFE, -55010, -6000, -73390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4420)

    def lambda_443A():
        OP_95(0xFE, -55580, -6000, -72260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_443A)
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
            "#3308F#5P#30W……已经没事了哦。\x02\x03",

            "#3306F大哥哥他们已经把可怕的魔兽\x01",
            "都消灭了……\x02\x03",

            "#3300F所以呢，已经不用害怕啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        "#3810F#60W#12P哎……呜……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x160,
        "#3305F#5P等、等等……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "#3810F#60W#12P呜呜呜呜呜……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0067
    ChrTalk(
        0x8,
        "#3811F#4S#12P呜哇啊啊啊啊啊啊啊啊！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x160, 0x0)
    BeginChrThread(0x160, 0, 0, 46)
    Sleep(500)

    #C0068
    ChrTalk(
        0x160,
        (
            "#3311F#5P#30W为、为什么要哭呀……\x01",
            "都说已经没危险了……\x02\x03",

            "#3308F#40W像你这种人……你这种人……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0069
    ChrTalk(
        0x160,
        (
            "#3310F#5P#4S我本来完全……\x01",
            "……完全没打算要救的啊……！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x160, 0x0)
    SetChrSubChip(0x160, 0xB)

    #C0070
    ChrTalk(
        0x101,
        "#0008F#5P……玲……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        "#0208F#5P小玲……\x02",
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
            "#3310F#5P像傻瓜一样……！\x01",
            "#30W……真的好像傻瓜一样……！\x02\x03",

            "#30W都下定决心只是旁观了……！\x01",
            "都下定决心，绝对不扯上任何关系了……！\x02\x03",

            "#3313F#30W可为什么……为什么玲会……！\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#0108F#5P小玲……\x02",
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

    def lambda_47CC():
        OP_96(0xFE, 0xFFFF2D1A, 0xFFFFE890, 0xFFFED220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47CC)
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
            "#0004F#11P──我不了解你的隐情。\x02\x03",

            "#0000F但是，你刚才一定\x01",
            "守护了你最重要的东西。\x02\x03",

            "不是靠其他人，而是靠你自己。\x02\x03",

            "#0004F那臂弯中感受到的\x01",
            "温暖，就是无可动摇的最佳证据。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x160,
        "#3312F#5P……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#0006F#11P我们很没用，\x01",
            "只是稍微帮了你一把而已。\x02\x03",

            "#0000F但即使如此，也觉得非常荣幸了。\x02\x03",

            "#0002F可以帮助玲──帮助你守护\x01",
            "自己最重要的东西。\x02",
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
        "#3313F#60W#5P呜呜……啊啊……\x02",
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
        "#3310F#4S#5P#70W#25A呜哇啊啊啊啊啊啊啊啊啊！\x02",
    )
    #Auto


    #C0080
    ChrTalk(
        0x8,
        "#3811F#4S#12P#70W#25A呜哇哇哇哇哇哇哇哇哇！\x02",
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

    # Function_34_40AD end

    def Function_35_4A4C(): pass

    label("Function_35_4A4C")


    def lambda_4A51():
        OP_95(0xFE, -39960, -6000, -63090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A51)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(100)

    def lambda_4A83():
        OP_95(0xFE, -42950, -6000, -63260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A83)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xFA, 0x12C)
    Sleep(100)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(100)

    def lambda_4AB5():
        OP_95(0xFE, -45050, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4AB5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(200)

    def lambda_4AE7():
        OP_95(0xFE, -51480, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4AE7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_35_4A4C end

    def Function_36_4B01(): pass

    label("Function_36_4B01")


    def lambda_4B06():
        OP_95(0xFE, -42950, -6000, -63260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B06)
    WaitChrThread(0xFE, 1)
    Sleep(700)

    def lambda_4B27():
        OP_95(0xFE, -45050, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B27)
    WaitChrThread(0xFE, 1)
    Sleep(1100)

    def lambda_4B48():
        OP_95(0xFE, -51480, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B48)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_4B01 end

    def Function_37_4B62(): pass

    label("Function_37_4B62")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B7D")
    OP_A1(0xFE, 0x1388, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_37_4B62")

    label("loc_4B7D")

    Return()

    # Function_37_4B62 end

    def Function_38_4B7E(): pass

    label("Function_38_4B7E")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0x160, 0x2A)
    SetChrSubChip(0x160, 0x4)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_4B9D():
        OP_9D(0xFE, 0xFFFF54B6, 0xFFFFE890, 0xFFFF0178, 0x384, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B9D)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    SetChrSubChip(0x160, 0x0)
    BeginChrThread(0xFE, 0, 0, 37)

    def lambda_4BD1():
        OP_95(0xFE, -53880, -6000, -64819, 15000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BD1)
    Sound(250, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_38_4B7E end

    def Function_39_4C07(): pass

    label("Function_39_4C07")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0x160, 0x2A)
    SetChrSubChip(0x160, 0x0)
    BeginChrThread(0xFE, 0, 0, 37)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_4C2C():
        OP_95(0xFE, -52890, -6000, -63420, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C2C)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_93(0x160, 0xB4, 0x320)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0x160, 0x2B)
    SetChrSubChip(0x160, 0x0)
    Return()

    # Function_39_4C07 end

    def Function_40_4C6B(): pass

    label("Function_40_4C6B")

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

    # Function_40_4C6B end

    def Function_41_4D59(): pass

    label("Function_41_4D59")

    PlayEffect(0x2, 0x1, 0xFE, 0x40, 0, -800, 0, 0, 0, 0, 1750, 1000, 1750, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x800)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0xFE, 0, 0, 42)
    SetChrPos(0xFE, -52890, -6000, -63420, 270)

    def lambda_4DBC():
        OP_96(0xFE, 0xFFFF2644, 0xFFFFE890, 0xFFFED626, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DBC)
    WaitChrThread(0xFE, 1)

    def lambda_4DDA():
        OP_96(0xFE, 0xFFFF3166, 0xFFFFE890, 0xFFFF0844, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DDA)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x800)
    StopEffect(0x1, 0x2)
    Return()

    # Function_41_4D59 end

    def Function_42_4E0B(): pass

    label("Function_42_4E0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E29")
    OP_A1(0xFE, 0x1B58, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_42_4E0B")

    label("loc_4E29")

    Return()

    # Function_42_4E0B end

    def Function_43_4E2A(): pass

    label("Function_43_4E2A")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0x160, 0x2A)
    SetChrSubChip(0x160, 0x0)

    def lambda_4E3C():
        OP_95(0xFE, -57200, -6000, -67220, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E3C)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_43_4E2A end

    def Function_44_4E5F(): pass

    label("Function_44_4E5F")

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

    def lambda_4E9D():
        OP_9D(0xFE, 0xFFFF3576, 0xFFFFE890, 0xFFFEF2BE, 0x2BC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E9D)
    WaitChrThread(0xFE, 1)
    Sound(31, 0, 100, 0)
    Sound(30, 0, 100, 0)
    SetChrSubChip(0xFE, 0x13)
    Return()

    # Function_44_4E5F end

    def Function_45_4ECA(): pass

    label("Function_45_4ECA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4EE8")
    OP_A1(0xFE, 0x3E8, 0x5, 0x8, 0x9, 0xA, 0x9, 0x0)
    Sleep(4000)
    Jump("Function_45_4ECA")

    label("loc_4EE8")

    Return()

    # Function_45_4ECA end

    def Function_46_4EE9(): pass

    label("Function_46_4EE9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F06")
    OP_A1(0xFE, 0x5DC, 0x4, 0xB, 0xC, 0xD, 0xC)
    Sleep(3000)
    Jump("Function_46_4EE9")

    label("loc_4F06")

    Return()

    # Function_46_4EE9 end

    def Function_47_4F07(): pass

    label("Function_47_4F07")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FBC")
    SetChrPos(0x10A, -56130, -6000, -61940, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_4FBC")

    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '特里斯坦号'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('特里斯坦号', 1)

    #C0082
    ChrTalk(
        0x101,
        (
            "#12P#0000F黄色的花……\x01",
            "看来，这一定就是\x01",
            "蕾瓦斯之花了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#5P#0306F不过……\x01",
            "竟然开在这种地方，\x01",
            "市民们很难自己来摘吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        "#12P#0200F就开在警察学校的前面呢。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#6P#0103F这三种颜色的花生长地点\x01",
            "各不相同，想全部凑齐\x01",
            "确实是很不容易的。\x02\x03",

            "#0100F所以风俗现在也已经变了，\x01",
            "在平时扫墓的时候，只要\x01",
            "带上其中的一色就可以了。\x02\x03",

            "只有在举办葬礼的时候\x01",
            "才会使用全部三种颜色的花。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        "#5P#0305F哦，是这样吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51D2")

    #C0087
    ChrTalk(
        0x10A,
        "#11P#0603F这也就是所谓的时代潮流。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5201")

    label("loc_51D2")


    #C0088
    ChrTalk(
        0x103,
        (
            "#12P#0200F传统习俗也渐渐\x01",
            "变得合理化了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5201")


    #C0089
    ChrTalk(
        0x101,
        (
            "#12P#0003F嗯……往往\x01",
            "都是这样的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x9, 0x1)
    OP_29(0x2E, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5257")
    OP_29(0x2E, 0x1, 0x6)

    label("loc_5257")

    ClearMapFlags(0x8000000)
    OP_37()
    Call(0, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_527A")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_527A")

    SetChrPos(0x0, -57910, -6000, -62950, 270)
    EventEnd(0x5)
    Return()

    # Function_47_4F07 end

    def Function_48_528E(): pass

    label("Function_48_528E")

    EventBegin(0x1)

    #C0090
    ChrTalk(
        0x101,
        (
            "#0001F声音不是从这边传来的……\x01",
            "快点去南边吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -32500, 0, 26090, 225)
    EventEnd(0x4)
    Return()

    # Function_48_528E end

    def Function_49_52DA(): pass

    label("Function_49_52DA")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5917")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53F3")
    SetChrPos(0x10A, -51490, -6000, -76540, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_53F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_541E")
    SetChrPos(0x109, -51490, -6000, -76540, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_541E")

    OP_0D()
    OP_68(-50470, -5400, -82530, 6000)
    MoveCamera(134, 26, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(24710, 6000)
    OP_6F(0x79)

    #C0092
    ChrTalk(
        0x102,
        "#0100F前方好像是警察学校呢。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#0204F是罗伊德前辈\x01",
            "以前上学的地方吗？\x02\x03",

            "#0202F听闻是个设备完善的\x01",
            "培训学校。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#0004F嗯，除此之外，\x01",
            "还一并设有公共设施\x01",
            "和警备队的练习场。\x02\x03",

            "#0000F穿过这道门，\x01",
            "就是长长的森林道，\x01",
            "各设施分散建设在其中。\x02\x03",

            "#0012F……话虽如此，但其实\x01",
            "我也没有走过这道门。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_560D")

    def lambda_5585():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5585)
    Sleep(60)

    def lambda_5595():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5595)
    Sleep(60)

    def lambda_55A5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_55A5)
    Sleep(60)

    def lambda_55B5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_55B5)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Jump("loc_56AD")

    label("loc_560D")


    def lambda_5612():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5612)
    Sleep(60)

    def lambda_5622():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5622)
    Sleep(60)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56AA")

    def lambda_568A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_568A)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_56AA")

    Sleep(1000)

    label("loc_56AD")


    #C0095
    ChrTalk(
        0x102,
        "#0105F哎……？\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        "#0305F怎么回事？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0097
    ChrTalk(
        0x101,
        (
            "#0000F#11P我是在车站换乘货物列车，\x01",
            "直接前往警察学校的。\x02\x03",

            "在之后的几个月，\x01",
            "全都是封闭式的宿舍生活。\x02\x03",

            "#0006F为了挑战搜查官考试，\x01",
            "连为数不多的假日也都用来拼命学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        "#0100F是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0301F这算什么啊～？\x01",
            "年纪轻轻的，竟然如此无趣。\x02\x03",

            "#0309F要说度过假日的方法，\x01",
            "去『巴鲁卡』和夜游是基本的吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        (
            "#0206F那只是兰迪前辈\x01",
            "一个人的基本吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#0002F#11P……哈哈………\x02\x03",

            "#0008F（在拿到搜查官资格之前\x01",
            "  绝不回克洛斯贝尔市……）\x02\x03",

            "#0006F（……我的这份执著或许\x01",
            "  太过孩子气了吧……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58E1")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_58E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58FB")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_58FB")

    SetScenarioFlags(0x95, 4)
    SetChrPos(0x0, -52380, -6000, -78750, 180)
    ClearMapFlags(0x8000000)
    OP_37()
    EventEnd(0x5)

    label("loc_5917")

    TalkEnd(0xFF)
    Return()

    # Function_49_52DA end

    def Function_50_591B(): pass

    label("Function_50_591B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0102
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东·克洛斯贝尔市　　　　１３７赛尔矩\x01",
            "北·贝尔加德门　　　　　　６１赛尔矩\x01",
            "南·克洛斯贝尔警察学校　　３１赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_50_591B end

    SaveToFile()

Try(main)
