from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r2020.bin",                # FileName
        "r2020",                    # MapName
        "r2020",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2020", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x12,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 2, 0, 3],
    )

    BuildStringList((
        "r2020",                  # 0
        "蜂鸟鳄鱼",               # 1
        "蜂鸟鳄鱼",               # 2
        "钢铁土龙",               # 3
        "钢铁土龙",               # 4
        "幻兽",                   # 5
        "车",                     # 6
        "SE控制",                 # 7
        "br2000",                 # 8
        "br2000",                 # 9
        "br2000",                 # 10
        "br2000",                 # 11
        "br2000",                 # 12
        "br2000",                 # 13
        "br2000",                 # 14
        "br2000",                 # 15
        "br2000",                 # 16
        "br2000",                 # 17
        "br0000",                 # 18
        "克洛斯贝尔市方向",       # 19
        "矿山镇玛因兹方向",       # 20
    ))

    ATBonus("ATBonus_664", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_684", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_3237", 3,   0,   1,   5,   3,   2,   0)
    Sepith("Sepith_323F", 0,   7,   2,   0,   1,   0,   4)
    Sepith("Sepith_324F", 5,   2,   0,   3,   0,   3,   2)
    Sepith("Sepith_322F", 6,   0,   0,   3,   2,   4,   0)
    Sepith("Sepith_3247", 6,   0,   8,   0,   1,   0,   6)
    Sepith("Sepith_326F", 29,  29,  29,  29,  29,  29,  29)
    Sepith("Sepith_3277", 11,  3,   6,   4,   6,   10,  8)

    MonsterBattlePostion("MonsterBattlePostion_6C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6CC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_728", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_72C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_730", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_734", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_738", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_73C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_740", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6BC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_744", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_748", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_74C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_750", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_754", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_758", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_75C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_760", 0, 0, 180)

    # monster count: 14

    BattleInfo(
        "BattleInfo_8C8", 0x0000, 52, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_3237", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
        )
    )

    BattleInfo(
        "BattleInfo_82C", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_323F", 40, 30, 20, 0,
        (
            ("ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_990", 0x0010, 52, 6, 90, 0, 1, 5, 0, "br2000", "Sepith_324F", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms77400.dat", "ms77400.dat", "ms65500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms65500.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
        )
    )

    BattleInfo(
        "BattleInfo_764", 0x0000, 52, 6, 45, 10, 1, 30, 0, "br2000", "Sepith_322F", 30, 40, 20, 10,
        (
            ("ms62500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms62500.dat", "ms62500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms62500.dat", "ms65900.dat", "ms62500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms62500.dat", "ms62500.dat", "ms65500.dat", "ms62500.dat", 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
        )
    )

    BattleInfo(
        "BattleInfo_A58", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_3247", 30, 40, 20, 10,
        (
            ("ms69400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
        )
    )

    BattleInfo(
        "BattleInfo_BBC", 0x0000, 52, 6, 90, 8, 1, 50, 0, "br2000", "Sepith_326F", 30, 40, 20, 10,
        (
            ("ms66402.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms66402.dat", "ms66402.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms66402.dat", "ms66402.dat", "ms66402.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms66402.dat", "ms66402.dat", "ms66402.dat", "ms66402.dat", 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
        )
    )

    BattleInfo(
        "BattleInfo_B20", 0x0000, 82, 6, 45, 6, 1, 30, 0, "br2000", "Sepith_3277", 40, 35, 25, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_664"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D0C", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms83200.dat", "ms83200.dat", "ms83200.dat", "ms83200.dat", "ms83200.dat", "ms83200.dat", "ms83200.dat", "ms83200.dat", "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7451", "ed7453", "ATBonus_684"),
            (),
            (),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_C84", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7453", "ed7453", "ATBonus_664"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_CC8", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7453", "ed7453", "ATBonus_664"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D50", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88901.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_744", "MonsterBattlePostion_724", "ed7454", "ed7453", "ATBonus_684"),
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
        "monster/ch62550.itc",               # 10
        "monster/ch62551.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch65550.itc",               # 14
        "monster/ch65551.itc",               # 15
        "monster/ch77450.itc",               # 16
        "monster/ch77450.itc",               # 17
        "monster/ch69450.itc",               # 18
        "monster/ch69450.itc",               # 19
        "monster/ch76050.itc",               # 1A
        "monster/ch76051.itc",               # 1B
        "monster/ch66450.itc",               # 1C
        "monster/ch66450.itc",               # 1D
        "monster/ch83250.itc",               # 1E
        "monster/ch83250.itc",               # 1F
    ))

    DeclNpc(50000,   2000,    -5000,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(32310,   5989,    47240,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(50000,   2000,    -5000,   270,  484,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(32310,   5989,    47240,   270,  484,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(24830,   -5000,   0,       0x1010000,    "BattleInfo_8C8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(53230,   -1940,   2000,    0x1010000,    "BattleInfo_82C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(35920,   6210,    1990,    0x1010000,    "BattleInfo_82C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(52150,   13400,   1990,    0x1010000,    "BattleInfo_82C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(24100,   10020,   1990,    0x1010000,    "BattleInfo_990", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(91270,   -25850,  6180,    0x1010000,    "BattleInfo_764", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(94500,   21310,   11990,   0x1010000,    "BattleInfo_8C8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(46950,   51270,   6000,    0x1010000,    "BattleInfo_A58", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(27720,   28230,   4000,    0x1010000,    "BattleInfo_82C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(49690,   39890,   6000,    0x1010000,    "BattleInfo_BBC", 0,   28,  0xFFFF, 12, 13)
    DeclMonster(44450,   -18520,  1990,    0x1010000,    "BattleInfo_B20", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(108560,  -8460,   10220,   0x1010000,    "BattleInfo_B20", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(59010,   31760,   6000,    0x1010000,    "BattleInfo_B20", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(41090,   15150,   2000,    0x18500B4,    "BattleInfo_D0C", 0,   30,  0xFFFF, 14, 15)

    DeclEvent(0x0000, 0, 11,  104.0,                 -16.5,                 8.5,                   506.25,                [0.04714043438434601,  0.23570235073566437,   -0.0,                  0.0,                   -0.047140467911958694, 0.23570218682289124,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.680422782897949,    -20.623958587646484,   -1.7000000476837158,   1.0])
    DeclEvent(0x0040, 0, 28,  41.09000015258789,     15.149999618530273,    2.0,                   16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -5.136250019073486,    -1.8937499523162842,   -0.5,                  1.0])
    DeclEvent(0x0040, 0, 29,  46.880001068115234,    52.099998474121094,    4.989999771118164,     16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -5.860000133514404,    -6.512499809265137,    -1.247499942779541,    1.0])
    DeclEvent(0x0000, 0, 16,  104.0,                 -16.5,                 8.5,                   506.25,                [0.04714043438434601,  0.23570235073566437,   -0.0,                  0.0,                   -0.047140467911958694, 0.23570218682289124,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.680422782897949,    -20.623958587646484,   -1.7000000476837158,   1.0])
    DeclEvent(0x0000, 0, 17,  79.5,                  -19.5,                 4.0,                   68906.25,              [0.020203042775392532, 0.047140467911958694,  -0.0,                  0.0,                   -0.020203057676553726, 0.04714043438434601,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -2.0001015663146973,   -2.8284287452697754,   -0.7999999523162842,   1.0])

    DeclActor(52570,   2000,    12080,   1200,    52570,   3000,    12080,   0x007C, 0,  4,  0x0000)
    DeclActor(22000,   4000,    26000,   1200,    22000,   5000,    26000,   0x007C, 0,  5,  0x0000)
    DeclActor(24640,   2100,    8840,    1200,    24640,   3100,    8840,    0x007C, 0,  6,  0x0000)
    DeclActor(50000,   2000,    -5000,   1200,    50000,   2000,    -5000,   0x007C, 0,  7,  0x0000)
    DeclActor(32310,   5990,    47240,   1200,    32310,   5990,    47240,   0x007C, 0,  8,  0x0000)

    PlaceName(-17.0, 0.0, -5.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(37.0, 0.0, 94.0, 0x0000, 0x0000, "矿山镇玛因兹方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 11
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 12
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 13
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 14
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 5])                   # 15

    ScpFunction((
        "Function_0_ECC",          # 00, 0
        "Function_1_EEB",          # 01, 1
        "Function_2_F0A",          # 02, 2
        "Function_3_F57",          # 03, 3
        "Function_4_17B6",         # 04, 4
        "Function_5_190F",         # 05, 5
        "Function_6_1A4A",         # 06, 6
        "Function_7_1B85",         # 07, 7
        "Function_8_1EAF",         # 08, 8
        "Function_9_21D9",         # 09, 9
        "Function_10_2217",        # 0A, 10
        "Function_11_221B",        # 0B, 11
        "Function_12_2446",        # 0C, 12
        "Function_13_2476",        # 0D, 13
        "Function_14_24A9",        # 0E, 14
        "Function_15_24DC",        # 0F, 15
        "Function_16_250F",        # 10, 16
        "Function_17_2574",        # 11, 17
        "Function_18_2611",        # 12, 18
        "Function_19_2832",        # 13, 19
        "Function_20_2894",        # 14, 20
        "Function_21_28F6",        # 15, 21
        "Function_22_2958",        # 16, 22
        "Function_23_29BA",        # 17, 23
        "Function_24_29D3",        # 18, 24
        "Function_25_29EC",        # 19, 25
        "Function_26_29FF",        # 1A, 26
        "Function_27_2A12",        # 1B, 27
        "Function_28_2C23",        # 1C, 28
        "Function_29_318B",        # 1D, 29
    ))


    def Function_0_ECC(): pass

    label("Function_0_ECC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EEA")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_ECC")

    label("loc_EEA")

    Return()

    # Function_0_ECC end

    def Function_1_EEB(): pass

    label("Function_1_EEB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F09")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_EEB")

    label("loc_F09")

    Return()

    # Function_1_EEB end

    def Function_2_F0A(): pass

    label("Function_2_F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F1E")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)
    Jump("loc_F2D")

    label("loc_F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F2D")
    ClearScenarioFlags(0x22, 1)
    Event(0, 27)

    label("loc_F2D")

    Call(0, 9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F56")
    SetScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F56")
    ClearScenarioFlags(0x0, 1)

    label("loc_F56")

    Return()

    # Function_2_F0A end

    def Function_3_F57(): pass

    label("Function_3_F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_F69")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F69")

    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FA4")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FD4")
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_FD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FFB")
    ModifyEventFlags(0, 2, 0x80)
    SetMapObjFlags(0xC, 0x4)
    Jump("loc_1064")

    label("loc_FFB")

    OP_78(0xC, 0xC)
    ClearMapObjFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x1)
    SetChrPos(0xC, 46880, 5990, 52100, 225)
    OP_93(0xC, 0xE1, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, 46880, 4990, 52100, 3000, 3000, 90000)

    label("loc_1064")

    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1097")
    ClearChrFlags(0x1C, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    SetChrFlags(0x1C, 0x8000)

    label("loc_1097")

    Jump("loc_10A6")

    label("loc_109C")

    SetChrFlags(0x1C, 0x80)
    ModifyEventFlags(0, 1, 0x80)

    label("loc_10A6")

    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15D1")
    LoadEffect(0x9, "map/mprain00.eff")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15D1")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)
    SetMapObjFrame(0xFF, "model07_shade", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light03", 0x0, 0x1)

    label("loc_15D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1661")
    SetMapObjFrame(0xFF, "model07_shade", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light03", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    Jump("loc_1697")

    label("loc_1661")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)

    label("loc_1697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16AA")
    OP_70(0x0, 0x0)
    Jump("loc_16AE")

    label("loc_16AA")

    OP_70(0x0, 0x1E)

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C1")
    OP_70(0x1, 0x0)
    Jump("loc_16C5")

    label("loc_16C1")

    OP_70(0x1, 0x1E)

    label("loc_16C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D8")
    OP_70(0x2, 0x0)
    Jump("loc_16DC")

    label("loc_16D8")

    OP_70(0x2, 0x1E)

    label("loc_16DC")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_173D")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 50000, 2000, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_173D")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1789")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 32310, 5990, 47240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1789")

    OP_1C(0x0, 0xF, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    OP_1C(0x0, 0x10, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    OP_1C(0x0, 0x11, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    OP_1C(0x0, 0x12, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    Return()

    # Function_3_F57 end

    def Function_4_17B6(): pass

    label("Function_4_17B6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E0")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 40)
    AddSepith(0x1, 40)
    AddSepith(0x2, 40)
    AddSepith(0x3, 40)
    AddSepith(0x4, 40)
    AddSepith(0x5, 40)
    AddSepith(0x6, 40)

    #A0001
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
    SetScenarioFlags(0x1E6, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_18FD")

    label("loc_18E0")


    #A0002
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

    label("loc_18FD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_17B6 end

    def Function_5_190F(): pass

    label("Function_5_190F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A01")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_1992")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
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
    SetScenarioFlags(0x1E6, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_19FC")

    label("loc_1992")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
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

    label("loc_19FC")

    Jump("loc_1A3E")

    label("loc_1A01")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
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

    label("loc_1A3E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_190F end

    def Function_6_1A4A(): pass

    label("Function_6_1A4A")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3C")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x9A, 1)"), scpexpr(EXPR_END)), "loc_1ACD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E6, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1B37")

    label("loc_1ACD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x9A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x9A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1B37")

    Jump("loc_1B79")

    label("loc_1B3C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
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

    label("loc_1B79")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1A4A end

    def Function_7_1B85(): pass

    label("Function_7_1B85")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D23")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_END)), "loc_1D04")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0009
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CFF")
    ClearScenarioFlags(0x3A, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_1CFC")
    ClearScenarioFlags(0x38, 3)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C27():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1C27)
    TurnDirection(0x8, 0x0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    PlayEffect(0x7, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0010
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
    Battle("BattleInfo_C84", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF7")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CDE")
    Call(1, 5)
    Jump("loc_1CF7")

    label("loc_1CDE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CF4")
    Call(1, 4)
    Jump("loc_1CF7")

    label("loc_1CF4")

    Call(1, 3)

    label("loc_1CF7")

    Jump("loc_1CFF")

    label("loc_1CFC")

    Call(1, 1)

    label("loc_1CFF")

    Jump("loc_1D1A")

    label("loc_1D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_1D1A")
    ClearScenarioFlags(0x38, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1D1A")

    TalkEnd(0xFF)
    Return()

    label("loc_1D23")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_END)), "loc_1E94")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0011
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E8F")
    ClearScenarioFlags(0x3A, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_1E8C")
    ClearScenarioFlags(0x38, 3)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1DB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1DB7)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0012
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
    Battle("BattleInfo_CC8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E87")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E6E")
    Call(1, 5)
    Jump("loc_1E87")

    label("loc_1E6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E84")
    Call(1, 4)
    Jump("loc_1E87")

    label("loc_1E84")

    Call(1, 3)

    label("loc_1E87")

    Jump("loc_1E8F")

    label("loc_1E8C")

    Call(1, 1)

    label("loc_1E8F")

    Jump("loc_1EAA")

    label("loc_1E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_1EAA")
    ClearScenarioFlags(0x38, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1EAA")

    TalkEnd(0xFF)
    Return()

    # Function_7_1B85 end

    def Function_8_1EAF(): pass

    label("Function_8_1EAF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_204D")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_202E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2029")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_2026")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1F51)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_C84", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2021")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2008")
    Call(1, 5)
    Jump("loc_2021")

    label("loc_2008")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_201E")
    Call(1, 4)
    Jump("loc_2021")

    label("loc_201E")

    Call(1, 3)

    label("loc_2021")

    Jump("loc_2029")

    label("loc_2026")

    Call(1, 1)

    label("loc_2029")

    Jump("loc_2044")

    label("loc_202E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_2044")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2044")

    TalkEnd(0xFF)
    Return()

    label("loc_204D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_21BE")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B9")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_21B6")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_20E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_20E1)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_CC8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B1")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2198")
    Call(1, 5)
    Jump("loc_21B1")

    label("loc_2198")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_21AE")
    Call(1, 4)
    Jump("loc_21B1")

    label("loc_21AE")

    Call(1, 3)

    label("loc_21B1")

    Jump("loc_21B9")

    label("loc_21B6")

    Call(1, 1)

    label("loc_21B9")

    Jump("loc_21D4")

    label("loc_21BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_21D4")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_21D4")

    TalkEnd(0xFF)
    Return()

    # Function_8_1EAF end

    def Function_9_21D9(): pass

    label("Function_9_21D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21FB")
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    Jump("loc_2200")

    label("loc_21FB")

    SetChrFlags(0x16, 0x80)

    label("loc_2200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 0)), scpexpr(EXPR_END)), "loc_2211")
    ClearScenarioFlags(0x3C, 0)
    Jump("loc_2216")

    label("loc_2211")

    SetChrFlags(0x18, 0x80)

    label("loc_2216")

    Return()

    # Function_9_21D9 end

    def Function_10_2217(): pass

    label("Function_10_2217")

    Call(1, 6)
    Return()

    # Function_10_2217 end

    def Function_11_221B(): pass

    label("Function_11_221B")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    SetChrPos(0x101, 108600, 10120, -10040, 8)
    SetChrPos(0x102, 107040, 10030, -11840, 8)
    SetChrPos(0x109, 109210, 10020, -11670, 8)
    SetChrPos(0x105, 107780, 9990, -14020, 8)
    OP_68(107330, 13510, -11000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_68(105400, 14500, 5340, 9500)
    OP_6E(510, 9500)
    SetCameraDistance(25000, 9500)
    BeginChrThread(0x101, 0, 0, 12)
    BeginChrThread(0x102, 0, 0, 13)
    BeginChrThread(0x109, 0, 0, 14)
    BeginChrThread(0x105, 0, 0, 15)
    FadeToBright(1000, 0)
    OP_0D()
    OP_11(0xA0, 0xDC, 0xDC, 0x1E, 0x64, 0x9C4)
    Sleep(1000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
    MoveCamera(45, 7, 0, 3000)
    Sleep(1000)
    StopEffect(0x7, 0x2)
    StopSound(128, 1000, 100)
    Sleep(1000)
    SetMapObjFrame(0xFF, "light02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light03", 0x1, 0x1)
    Sleep(1000)
    SetMapObjFrame(0xFF, "model07_shade", 0x1, 0x1)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(500)

    #C0017
    ChrTalk(
        0x102,
        "#00102F#5P好漂亮……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x109,
        "#10109F#11P真是绝景……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x105,
        "#10302F#11P嘿，的确值得欣赏。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00004F#5P嗯，天气真晴朗啊。\x02\x03",

            "#00000F芙兰说的\x01",
            "果然没错呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 108500, 11960, 2590, 315)
    SetScenarioFlags(0x129, 0)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)
    ClearScenarioFlags(0x0, 1)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_221B end

    def Function_12_2446(): pass

    label("Function_12_2446")

    OP_95(0xFE, 107850, 11740, -60, 2000, 0x1)
    OP_95(0xFE, 103290, 12000, 6780, 2000, 0x1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_12_2446 end

    def Function_13_2476(): pass

    label("Function_13_2476")

    Sleep(50)
    OP_95(0xFE, 107520, 11440, -1280, 2000, 0x1)
    OP_95(0xFE, 104830, 12000, 5900, 2000, 0x1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_13_2476 end

    def Function_14_24A9(): pass

    label("Function_14_24A9")

    Sleep(100)
    OP_95(0xFE, 109830, 11690, -70, 2000, 0x1)
    OP_95(0xFE, 106090, 12000, 4510, 2000, 0x1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_14_24A9 end

    def Function_15_24DC(): pass

    label("Function_15_24DC")

    Sleep(150)
    OP_95(0xFE, 109230, 11310, -2370, 2000, 0x1)
    OP_95(0xFE, 106780, 12000, 3100, 2000, 0x1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_15_24DC end

    def Function_16_250F(): pass

    label("Function_16_250F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2573")
    ClearScenarioFlags(0x0, 1)
    StopEffect(0x7, 0x2)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
    OP_11(0xA0, 0xDC, 0xDC, 0x1E, 0x64, 0x9C4)
    StopSound(128, 1000, 100)
    Sleep(1000)
    SetMapObjFrame(0xFF, "light02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model07_shade", 0x1, 0x1)

    label("loc_2573")

    Return()

    # Function_16_250F end

    def Function_17_2574(): pass

    label("Function_17_2574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2610")
    SetScenarioFlags(0x0, 1)
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x9C4)
    OP_11(0x95, 0xA0, 0xB5, 0x3, 0x64, 0x9C4)
    Sound(128, 1, 50, 0)
    Sleep(1000)
    SetMapObjFrame(0xFF, "light02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light03", 0x0, 0x1)
    Sleep(1000)
    SetMapObjFrame(0xFF, "model07_shade", 0x0, 0x1)

    label("loc_2610")

    Return()

    # Function_17_2574 end

    def Function_18_2611(): pass

    label("Function_18_2611")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    ClearChrFlags(0xD, 0x80)
    OP_78(0xD, 0xD)
    OP_49()
    SetChrPos(0xD, 23590, 0, -11000, 135)
    OP_D5(0xD, 0x0, 0x20F58, 0x0, 0x0)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x79, 0xB4, 0x0, 0x20)
    OP_93(0xD, 0x87, 0x0)
    BeginChrThread(0xD, 3, 0, 19)
    BeginChrThread(0xE, 1, 0, 25)
    OP_68(38220, 600, -12240, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(38710, 0)
    OP_68(55340, 2100, -8430, 8650)
    MoveCamera(34, 12, 0, 8650)
    OP_6E(510, 8650)
    SetCameraDistance(38620, 8650)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0xD, 97390, 7050, -22730, 8)
    OP_D5(0xD, 0x0, 0x1F40, 0x0, 0x0)
    OP_93(0xD, 0x8, 0x0)
    BeginChrThread(0xD, 3, 0, 21)
    BeginChrThread(0xE, 1, 0, 26)
    OP_68(101000, 14000, -18000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_68(99350, 14500, 10520, 7900)
    OP_6E(510, 7900)
    SetCameraDistance(25000, 7900)
    Fade(500)
    OP_0D()
    OP_11(0xA0, 0xDC, 0xDC, 0x1E, 0x64, 0x7D0)
    Sleep(700)
    MoveCamera(45, 7, 0, 2000)
    Sleep(1000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Sleep(1200)
    StopEffect(0x7, 0x2)
    StopSound(128, 1000, 100)
    Sleep(2000)
    SetMapObjFrame(0xFF, "model07_shade", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light03", 0x1, 0x1)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21420300), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2817")
    SetScenarioFlags(0x22, 1)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Jump("loc_2831")

    label("loc_2817")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21205000), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2831")
    SetScenarioFlags(0x22, 1)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_2831")

    Return()

    # Function_18_2611 end

    def Function_19_2832(): pass

    label("Function_19_2832")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 32280, 300, -18060)
    OP_9F(0x1, 39620, 1720, -20130)
    OP_9F(0x1, 46470, 2020, -17280)
    OP_9F(0x1, 57450, 2000, -9800)
    OP_9F(0x1, 66210, 2140, -11280)
    OP_9F(0x1, 73950, 3490, -15440)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_19_2832 end

    def Function_20_2894(): pass

    label("Function_20_2894")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 32280, 300, -18060)
    OP_9F(0x1, 39620, 1720, -20130)
    OP_9F(0x1, 46470, 2020, -17280)
    OP_9F(0x1, 57450, 2000, -9800)
    OP_9F(0x1, 66210, 2140, -11280)
    OP_9F(0x1, 73950, 3490, -15440)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_20_2894 end

    def Function_21_28F6(): pass

    label("Function_21_28F6")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 105040, 9660, -16580)
    OP_9F(0x1, 108540, 10450, -8730)
    OP_9F(0x1, 106850, 11980, 1640)
    OP_9F(0x1, 97340, 12030, 10490)
    OP_9F(0x1, 94020, 12000, 16660)
    OP_9F(0x1, 89030, 11820, 18970)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_21_28F6 end

    def Function_22_2958(): pass

    label("Function_22_2958")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 105040, 9660, -16580)
    OP_9F(0x1, 108540, 10450, -8730)
    OP_9F(0x1, 106850, 11980, 1640)
    OP_9F(0x1, 97340, 12030, 10490)
    OP_9F(0x1, 94020, 12000, 16660)
    OP_9F(0x1, 89030, 11820, 18970)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_22_2958 end

    def Function_23_29BA(): pass

    label("Function_23_29BA")

    Sound(465, 0, 100, 0)
    Sleep(4000)
    Sound(471, 0, 100, 0)
    Sleep(3000)
    Sound(465, 0, 100, 0)
    Return()

    # Function_23_29BA end

    def Function_24_29D3(): pass

    label("Function_24_29D3")

    Sound(471, 0, 100, 0)
    Sleep(2500)
    Sound(465, 0, 100, 0)
    Sleep(4000)
    Sound(471, 0, 100, 0)
    Return()

    # Function_24_29D3 end

    def Function_25_29EC(): pass

    label("Function_25_29EC")

    Sleep(500)
    Sound(458, 0, 100, 0)
    Sleep(4000)
    Sound(457, 0, 100, 0)
    Return()

    # Function_25_29EC end

    def Function_26_29FF(): pass

    label("Function_26_29FF")

    Sleep(1000)
    Sound(458, 0, 100, 0)
    Sleep(4000)
    Sound(494, 0, 100, 0)
    Return()

    # Function_26_29FF end

    def Function_27_2A12(): pass

    label("Function_27_2A12")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    ClearChrFlags(0xD, 0x80)
    OP_78(0xE, 0xD)
    OP_49()
    SetChrPos(0xD, 23590, 0, -11000, 135)
    OP_D5(0xD, 0x0, 0x20F58, 0x0, 0x0)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    OP_74(0xE, 0x1E)
    OP_71(0xE, 0x79, 0xB4, 0x0, 0x20)
    OP_93(0xD, 0x87, 0x0)
    BeginChrThread(0xD, 3, 0, 20)
    BeginChrThread(0xE, 1, 0, 23)
    OP_68(38220, 600, -12240, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(38710, 0)
    OP_68(55340, 2100, -8430, 11500)
    MoveCamera(34, 12, 0, 11500)
    OP_6E(510, 11500)
    SetCameraDistance(38620, 11500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0xD, 97390, 7050, -22730, 45)
    OP_D5(0xD, 0x0, 0xAFC8, 0x0, 0x0)
    OP_93(0xD, 0x2D, 0x0)
    BeginChrThread(0xD, 3, 0, 22)
    BeginChrThread(0xE, 1, 0, 24)
    OP_68(101000, 14000, -18000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_68(99350, 14500, 10520, 10000)
    OP_6E(510, 10000)
    SetCameraDistance(25000, 10000)
    Fade(500)
    OP_0D()
    OP_11(0xA0, 0xDC, 0xDC, 0x1E, 0x64, 0x960)
    Sleep(850)
    MoveCamera(45, 7, 0, 2400)
    Sleep(1200)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x960)
    Sleep(1500)
    StopEffect(0x7, 0x2)
    StopSound(128, 1000, 100)
    Sleep(2200)
    SetMapObjFrame(0xFF, "model07_shade", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light03", 0x1, 0x1)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_END)), "loc_2C16")
    ClearScenarioFlags(0x25, 1)
    SetScenarioFlags(0x22, 2)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Jump("loc_2C22")

    label("loc_2C16")

    SetScenarioFlags(0x22, 2)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_2C22")

    Return()

    # Function_27_2A12 end

    def Function_28_2C23(): pass

    label("Function_28_2C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 1)), scpexpr(EXPR_END)), "loc_2C2D")
    Return()

    label("loc_2C2D")

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

    #A0021
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
        (1, "loc_2CF9"),
        (SWITCH_DEFAULT, "loc_2D12"),
    )


    label("loc_2CF9")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 39090, 2000, 8870, 180)
    EventEnd(0x5)
    Return()

    label("loc_2D12")

    Battle("BattleInfo_D0C", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(39090, 3000, 8870, 0)
    OP_90(0x0, 39090, 2000, 8870, 180)
    OP_90(0x1, 39090, 2000, 8870, 180)
    OP_90(0x2, 39090, 2000, 8870, 180)
    OP_90(0x3, 39090, 2000, 8870, 180)
    OP_90(0x4, 39090, 2000, 8870, 180)
    OP_90(0x5, 39090, 2000, 8870, 180)
    OP_90(0x6, 39090, 2000, 8870, 180)
    OP_90(0x7, 39090, 2000, 8870, 180)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_2DD4"),
        (1, "loc_2DD9"),
        (SWITCH_DEFAULT, "loc_2DDC"),
    )


    label("loc_2DD4")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_2DD9")

    OP_B9(0x0)
    Return()

    label("loc_2DDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(38540, 2600, 9550, 0)
    MoveCamera(30, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17270, 0)
    SetChrFlags(0x1C, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xB, 1)
    SetChrPos(0x101, 40500, 2000, 12000, 225)
    SetChrPos(0x102, 36500, 2000, 8000, 45)
    SetChrPos(0x105, 36500, 2000, 12000, 140)
    SetChrPos(0x109, 40500, 2000, 8000, 320)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3022")

    #C0024
    ChrTalk(
        0x101,
        "#00003F战术书吗……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        "#00105F#6P相当古旧的书籍呢。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x109,
        (
            "#10100F#12P书中似乎记载着\x01",
            "组合战技的使用方法……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，艾莉和诺艾尔\x01",
            "应该可以掌握这个战技吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0028
    ChrTalk(
        0x102,
        (
            "#00104F#6P是啊……\x01",
            "我认为有一试的价值。\x02\x03",

            "#00100F诺艾尔小姐，我们练习一下如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        "#10102F#12P好，当然没问题！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x21E, 1)
    Jump("loc_30C5")

    label("loc_3022")


    #C0030
    ChrTalk(
        0x101,
        (
            "#00000F战术书……\x01",
            "书中记载着组合战技\x01",
            "的使用方法。\x02\x03",

            "#00004F艾莉和诺艾尔\x01",
            "应该可以掌握这个战技吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#00100F诺艾尔小姐，要试试看吗？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x109,
        "#10102F嗯，当然！\x02",
    )

    CloseMessageWindow()

    label("loc_30C5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x1, 0x18E)
    AddCraft(0x8, 0x18E)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0033
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉和诺艾尔习得组合战技\x01\x07\x02",

            "『南十字星』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    #A0034
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x21C, 1)
    OP_29(0x6D, 0x4, 0x10)
    OP_29(0x6D, 0x4, 0x2)
    OP_29(0x6D, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_E2(0x2)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_28_2C23 end

    def Function_29_318B(): pass

    label("Function_29_318B")

    Battle("BattleInfo_D50", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31D2")
    OP_90(0x0, 39600, 6010, 45150, 225)
    EventEnd(0x5)
    SetChrFlags(0xC, 0x8000)
    Jump("loc_3206")

    label("loc_31D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31E5")
    Jump("loc_3206")

    label("loc_31E5")

    ModifyEventFlags(0, 2, 0x80)
    SetMapObjFlags(0xC, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 2)
    EventEnd(0x5)

    label("loc_3206")

    Return()

    # Function_29_318B end

    SaveToFile()

Try(main)
