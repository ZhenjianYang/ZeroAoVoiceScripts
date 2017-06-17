from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1100.bin",                # FileName
        "c1100",                    # MapName
        "c1100",                    # Location
        0x0016,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c1100", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x06',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 4210, 2500, 8930, 0, 0, 1, 22, 0, 7, 0, 8],
    )

    BuildStringList((
        "c1100",                  # 0
        "库罗玛",                 # 1
        "奥特",                   # 2
        "塔基库",                 # 3
        "弗兰茨巡警",             # 4
        "蔡特",                   # 5
        "游客",                   # 6
        "游客",                   # 7
        "市民",                   # 8
        "男孩",                   # 9
        "市民",                   # 10
        "市民",                   # 11
        "哈斯",                   # 12
        "国防军士兵",             # 13
        "国防军士兵",             # 14
        "市民",                   # 15
        "市民",                   # 16
        "市民",                   # 17
        "市民",                   # 18
        "市民",                   # 19
        "市民",                   # 20
        "警官",                   # 21
        "警官",                   # 22
        "警官",                   # 23
        "市民",                   # 24
        "游客",                   # 25
        "游客",                   # 26
        "小桃",                   # 27
        "隆",                     # 28
        "亨利",                   # 29
        "魔导兵",                 # 30
        "魔导兵",                 # 31
        "游击士斯克特",           # 32
        "游击士温蔡尔",           # 33
        "游击士林",               # 34
        "游击士艾欧莉娅",         # 35
        "剧情用魔兽",             # 36
        "剧情用魔兽",             # 37
        "剧情用魔兽",             # 38
        "凯特巡警",               # 39
        "尤利",                   # 40
        "塞克斯",                 # 41
        "瑞吉",                   # 42
        "警车",                   # 43
        "警车",                   # 44
        "警车",                   # 45
        "警车",                   # 46
        "飙车族",                 # 47
        "车",                     # 48
        "土袋",                   # 49
        "市民１",                 # 50
        "市民２",                 # 51
        "市民３",                 # 52
        "市民４",                 # 53
        "市民５",                 # 54
        "市民６",                 # 55
        "市民７",                 # 56
        "市民８",                 # 57
        "警官",                   # 58
        "警官",                   # 59
        "警官",                   # 60
        "警官",                   # 61
        "警官",                   # 62
        "SE控制",                 # 63
        "bc1100",                 # 64
        "中央广场",               # 65
        "西街",                   # 66
        "行政区",                 # 67
        "住宅街",                 # 68
        "欢乐街",                 # 69
        "东街",                   # 70
        "旧城区",                 # 71
        "港湾区",                 # 72
        "ＩＢＣ",                 # 73
        "站前街道",               # 74
        "后巷",                   # 75
        "乌尔斯拉间道",           # 76
        "东克洛斯贝尔街道",       # 77
        "西克洛斯贝尔街道",       # 78
        "玛因兹山道",             # 79
        "兰花塔",                 # 80
    ))

    ATBonus("ATBonus_BF0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_B017", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_C40", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_C44", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_C48", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C50", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C54", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_C58", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C5C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_CA0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_CA4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_CA8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_CAC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_CB0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_CB4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_CB8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_CBC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_C20", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_C24", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_C28", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_C2C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_C30", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C34", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C38", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C3C", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_CC0", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc1100", "Sepith_B017", 60, 30, 10, 0,
        (
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C40", "MonsterBattlePostion_CA0", "ed7450", "ed7453", "ATBonus_BF0"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C20", "MonsterBattlePostion_CA0", "ed7450", "ed7453", "ATBonus_BF0"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C40", "MonsterBattlePostion_CA0", "ed7450", "ed7453", "ATBonus_BF0"),
            (),
        )
    )

    AddCharChip((
        "chr/ch24900.itc",                   # 00
        "chr/ch20800.itc",                   # 01
        "chr/ch28100.itc",                   # 02
        "chr/ch30000.itc",                   # 03
        "chr/ch02707.itc",                   # 04
        "chr/ch24400.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch21000.itc",                   # 07
        "chr/ch23800.itc",                   # 08
        "chr/ch20400.itc",                   # 09
        "chr/ch21300.itc",                   # 0A
        "chr/ch21002.itc",                   # 0B
        "chr/ch26000.itc",                   # 0C
        "chr/ch41400.itc",                   # 0D
        "chr/ch41500.itc",                   # 0E
        "chr/ch20000.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "chr/ch23300.itc",                   # 12
        "chr/ch21800.itc",                   # 13
        "chr/ch22700.itc",                   # 14
        "chr/ch21400.itc",                   # 15
        "chr/ch49400.itc",                   # 16
        "chr/ch48700.itc",                   # 17
        "chr/ch20700.itc",                   # 18
        "chr/ch20600.itc",                   # 19
        "chr/ch22200.itc",                   # 1A
        "chr/ch32300.itc",                   # 1B
        "chr/ch44200.itc",                   # 1C
    ))

    DeclNpc(6929,    2490,    -6650,   225,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(8369,    2390,    -14850,  90,   257,  0x0, 0,   1,   0,   0,   2,   0,   10,  255,  0)
    DeclNpc(-8739,   2500,    6070,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-15050,  2500,    27399,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(24299,   2500,    -10609,  225,  405,  0x0, 0,   4,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-1340,   2390,    9340,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-2339,   2390,    9340,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-16959,  2500,    -129,    270,  389,  0x0, 0,   7,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-18559,  2500,    -219,    45,   385,  0x0, 0,   8,   0,   0,   4,   0,   29,  255,  0)
    DeclNpc(7389,    2500,    -8180,   135,  389,  0x0, 0,   9,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(8489,    2390,    -8680,   315,  389,  0x0, 0,   10,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(-8390,   2390,    9329,    225,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(14510,   2410,    11399,   270,  389,  0x0, 0,   13,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(14670,   2500,    4420,    270,  389,  0x0, 0,   14,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(13210,   2500,    5900,    90,   389,  0x0, 0,   15,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(12989,   2500,    3599,    45,   389,  0x0, 0,   18,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(12050,   2500,    6840,    90,   389,  0x0, 0,   19,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(11510,   2410,    9470,    180,  389,  0x0, 0,   20,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(9710,    2410,    9939,    90,   389,  0x0, 0,   21,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(1500,    2500,    -3200,   270,  389,  0x0, 0,   23,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(-15050,  2500,    27399,   180,  385,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(21909,   2500,    1659,    180,  385,  0x0, 0,   3,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(21530,   0,       -48659,  0,    385,  0x0, 0,   3,   0,   0,   1,   0,   20,  255,  0)
    DeclNpc(-5150,   2500,    26469,   45,   385,  0x0, 0,   19,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-3839,   2500,    26950,   0,    385,  0x0, 0,   27,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-2960,   2500,    26680,   315,  385,  0x0, 0,   28,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-6159,   2500,    27180,   0,    389,  0x0, 0,   24,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-5750,   2500,    28309,   0,    389,  0x0, 0,   25,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-6900,   2500,    28020,   90,   389,  0x0, 0,   26,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-4789,   2500,    34500,   180,  389,  0x0, 0,   16,  0,   0,   5,   255, 255, 255,  0)
    DeclNpc(-7570,   2500,    34500,   180,  389,  0x0, 0,   16,  0,   0,   5,   255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(8740,    8280,    2490,    0x101010E,    "BattleInfo_CC0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-17560,  9920,    2500,    0x10100E1,    "BattleInfo_CC0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(14710,   -13270,  2390,    0x10100E1,    "BattleInfo_CC0", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0040, 0, 40,  11.420000076293945,    7.010000228881836,     0.0,                   36.0,                  [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.9516667127609253,   -0.5841667056083679,   -0.0,                  1.0])
    DeclEvent(0x0040, 0, 68,  -6.340000152587891,    30.489999771118164,    2.5,                   25.0,                  [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.6340000033378601,    -3.0490000247955322,   -0.5,                  1.0])

    DeclActor(-5540,   2500,    32280,   2000,    -5540,   4000,    32280,   0x007C, 0,  66, 0x0000)
    DeclActor(16550,   2410,    10660,   1200,    16550,   3910,    10660,   0x007C, 0,  69, 0x0000)
    DeclActor(-17980,  2500,    30520,   1200,    -17980,  3700,    30520,   0x007C, 0,  70, 0x0000)

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "中央广场")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "西街")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "行政区")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "住宅街")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "欢乐街")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "东街")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "旧城区")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "港湾区")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "站前街道")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "后巷")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-175.5, 0.0, 26.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-5.0, 0.0, 178.0, 0x0000, 0x0000, "兰花塔")
    PlaceName(-60.130001068115234, 0.0, -126.0999984741211, 0x0000, 0x0051, "")
    PlaceName(9.75, 0.0, -92.30000305175781, 0x0000, 0x0054, "")
    PlaceName(-28.280000686645508, 0.0, -136.5, 0x0000, 0x0057, "")
    PlaceName(-61.099998474121094, 0.0, -88.4000015258789, 0x0000, 0x0053, "")
    PlaceName(-34.45000076293945, 0.0, -57.20000076293945, 0x0000, 0x0053, "")
    PlaceName(-100.43000030517578, 0.0, -94.9000015258789, 0x0000, 0x0053, "")
    PlaceName(-113.0999984741211, 0.0, -67.5999984741211, 0x0000, 0x0053, "")
    PlaceName(-81.9000015258789, 0.0, -26.0, 0x0000, 0x0052, "")
    PlaceName(-75.7300033569336, 0.0, -42.900001525878906, 0x0000, 0x0053, "")
    PlaceName(-64.3499984741211, 0.0, -53.95000076293945, 0x0000, 0x0053, "")
    PlaceName(-27.299999237060547, 0.0, 38.349998474121094, 0x0000, 0x0051, "")
    PlaceName(118.30000305175781, 0.0, -137.8000030517578, 0x0000, 0x0052, "")
    PlaceName(96.19999694824219, 0.0, -255.4499969482422, 0x0000, 0x0053, "")
    PlaceName(79.30000305175781, 0.0, -231.39999389648438, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_E90",          # 00, 0
        "Function_1_F48",          # 01, 1
        "Function_2_F95",          # 02, 2
        "Function_3_106E",         # 03, 3
        "Function_4_1099",         # 04, 4
        "Function_5_10C4",         # 05, 5
        "Function_6_10E3",         # 06, 6
        "Function_7_11C8",         # 07, 7
        "Function_8_193F",         # 08, 8
        "Function_9_21E6",         # 09, 9
        "Function_10_2E74",        # 0A, 10
        "Function_11_3A17",        # 0B, 11
        "Function_12_3BAD",        # 0C, 12
        "Function_13_482B",        # 0D, 13
        "Function_14_4AA3",        # 0E, 14
        "Function_15_4DFE",        # 0F, 15
        "Function_16_4E08",        # 10, 16
        "Function_17_4E12",        # 11, 17
        "Function_18_4E1C",        # 12, 18
        "Function_19_51E1",        # 13, 19
        "Function_20_54CC",        # 14, 20
        "Function_21_564D",        # 15, 21
        "Function_22_570E",        # 16, 22
        "Function_23_57CF",        # 17, 23
        "Function_24_5890",        # 18, 24
        "Function_25_592F",        # 19, 25
        "Function_26_597D",        # 1A, 26
        "Function_27_5A53",        # 1B, 27
        "Function_28_5B1B",        # 1C, 28
        "Function_29_5FDE",        # 1D, 29
        "Function_30_6289",        # 1E, 30
        "Function_31_635F",        # 1F, 31
        "Function_32_640C",        # 20, 32
        "Function_33_645E",        # 21, 33
        "Function_34_64AC",        # 22, 34
        "Function_35_650F",        # 23, 35
        "Function_36_6546",        # 24, 36
        "Function_37_6585",        # 25, 37
        "Function_38_65DA",        # 26, 38
        "Function_39_6600",        # 27, 39
        "Function_40_671C",        # 28, 40
        "Function_41_6EF3",        # 29, 41
        "Function_42_75DB",        # 2A, 42
        "Function_43_793F",        # 2B, 43
        "Function_44_7985",        # 2C, 44
        "Function_45_7DA8",        # 2D, 45
        "Function_46_7E5F",        # 2E, 46
        "Function_47_7EA4",        # 2F, 47
        "Function_48_7EDF",        # 30, 48
        "Function_49_85A9",        # 31, 49
        "Function_50_866C",        # 32, 50
        "Function_51_874B",        # 33, 51
        "Function_52_877A",        # 34, 52
        "Function_53_87A3",        # 35, 53
        "Function_54_88B6",        # 36, 54
        "Function_55_89B2",        # 37, 55
        "Function_56_8AD2",        # 38, 56
        "Function_57_8B37",        # 39, 57
        "Function_58_8B66",        # 3A, 58
        "Function_59_8B8B",        # 3B, 59
        "Function_60_8BFA",        # 3C, 60
        "Function_61_95F6",        # 3D, 61
        "Function_62_9716",        # 3E, 62
        "Function_63_9775",        # 3F, 63
        "Function_64_97A5",        # 40, 64
        "Function_65_97D5",        # 41, 65
        "Function_66_A44B",        # 42, 66
        "Function_67_A4A7",        # 43, 67
        "Function_68_A523",        # 44, 68
        "Function_69_A73C",        # 45, 69
        "Function_70_AEB1",        # 46, 70
    ))


    def Function_0_E90(): pass

    label("Function_0_E90")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_ED0"),
        (1, "loc_EDC"),
        (2, "loc_EE8"),
        (3, "loc_EF4"),
        (4, "loc_F00"),
        (5, "loc_F0C"),
        (6, "loc_F18"),
        (SWITCH_DEFAULT, "loc_F24"),
    )


    label("loc_ED0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_EDC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_EE8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_EF4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F00")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F0C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F18")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F24")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F47")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F47")

    Return()

    # Function_0_E90 end

    def Function_1_F48(): pass

    label("Function_1_F48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F94")
    OP_95(0xFE, 20950, 2490, -3000, 2000, 0x0)
    OP_95(0xFE, 44000, 2490, -2580, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 21530, 0, -48660, 0)
    Jump("Function_1_F48")

    label("loc_F94")

    Return()

    # Function_1_F48 end

    def Function_2_F95(): pass

    label("Function_2_F95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_106D")
    OP_95(0xFE, 17250, 2500, -14850, 1000, 0x0)
    OP_95(0xFE, 17250, 2500, -70, 1000, 0x0)
    OP_95(0xFE, 3810, 2500, 8270, 1000, 0x0)
    OP_95(0xFE, -6210, 2500, 23860, 1000, 0x0)
    OP_95(0xFE, -18440, 2500, 23260, 1000, 0x0)
    OP_95(0xFE, -20840, 2450, 19170, 1000, 0x0)
    OP_95(0xFE, -18240, 2500, 6490, 1000, 0x0)
    OP_95(0xFE, -18430, 2500, -3620, 1000, 0x0)
    OP_95(0xFE, -7420, 2500, -14630, 1000, 0x0)
    OP_95(0xFE, 8370, 2390, -14850, 1000, 0x0)
    Jump("Function_2_F95")

    label("loc_106D")

    Return()

    # Function_2_F95 end

    def Function_3_106E(): pass

    label("Function_3_106E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1098")
    OP_94(0xFE, 0x1F72, 0xFFFFEAD4, 0x109A, 0xFFFFD8AA, 0x7D0)
    Sleep(200)
    Jump("Function_3_106E")

    label("loc_1098")

    Return()

    # Function_3_106E end

    def Function_4_1099(): pass

    label("Function_4_1099")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10C3")
    OP_94(0xFE, 0xFFFFB2BC, 0x8CA, 0xFFFFBAC8, 0xFFFFF204, 0x3E8)
    Sleep(300)
    Jump("Function_4_1099")

    label("loc_10C3")

    Return()

    # Function_4_1099 end

    def Function_5_10C4(): pass

    label("Function_5_10C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10E2")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_5_10C4")

    label("loc_10E2")

    Return()

    # Function_5_10C4 end

    def Function_6_10E3(): pass

    label("Function_6_10E3")

    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    SetMapObjFlags(0x19, 0x2000000)
    SetMapObjFlags(0x1A, 0x2000000)
    SetMapObjFlags(0x1B, 0x2000000)
    SetMapObjFlags(0x1C, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_11A6")
    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0xF, 0x2000000)
    ClearMapObjFlags(0x10, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)
    ClearMapObjFlags(0x14, 0x2000000)
    ClearMapObjFlags(0x15, 0x2000000)
    ClearMapObjFlags(0x16, 0x2000000)
    ClearMapObjFlags(0x17, 0x2000000)
    ClearMapObjFlags(0x18, 0x2000000)
    ClearMapObjFlags(0x19, 0x2000000)
    ClearMapObjFlags(0x1A, 0x2000000)
    ClearMapObjFlags(0x1B, 0x2000000)
    ClearMapObjFlags(0x1C, 0x2000000)

    label("loc_11A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_11C7")
    ClearMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)

    label("loc_11C7")

    Return()

    # Function_6_10E3 end

    def Function_7_11C8(): pass

    label("Function_7_11C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AE")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1293")
    SetChrPos(0x0, 30170, 2500, -90, 270)
    SetChrPos(0x1, 30170, 2500, -90, 270)
    SetChrPos(0x2, 30170, 2500, -90, 270)
    SetChrPos(0x3, 30170, 2500, -90, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1266")
    SetChrPos(0x4, 30170, 2500, -90, 270)
    SetChrPos(0x5, 30170, 2500, -90, 270)
    Jump("loc_1285")

    label("loc_1266")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1285")
    SetChrPos(0x4, 30170, 2500, -90, 270)

    label("loc_1285")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AE")

    label("loc_1293")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1359")
    SetChrPos(0x0, -40390, 0, 24150, 90)
    SetChrPos(0x1, -40390, 0, 24150, 90)
    SetChrPos(0x2, -40390, 0, 24150, 90)
    SetChrPos(0x3, -40390, 0, 24150, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_132C")
    SetChrPos(0x4, -40390, 0, 24150, 90)
    SetChrPos(0x5, -40390, 0, 24150, 90)
    Jump("loc_134B")

    label("loc_132C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_134B")
    SetChrPos(0x4, -40390, 0, 24150, 90)

    label("loc_134B")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AE")

    label("loc_1359")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140D")
    SetChrPos(0x0, -5400, 2500, 35000, 180)
    SetChrPos(0x1, -5400, 2500, 35000, 180)
    SetChrPos(0x2, -5400, 2500, 35000, 180)
    SetChrPos(0x3, -5400, 2500, 35000, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E0")
    SetChrPos(0x4, -5400, 2500, 35000, 180)
    SetChrPos(0x5, -5400, 2500, 35000, 180)
    Jump("loc_13FF")

    label("loc_13E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13FF")
    SetChrPos(0x4, -5400, 2500, 35000, 180)

    label("loc_13FF")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AE")

    label("loc_140D")

    SetChrPos(0x0, 19940, 0, -37920, 0)
    SetChrPos(0x1, 19940, 0, -37920, 0)
    SetChrPos(0x2, 19940, 0, -37920, 0)
    SetChrPos(0x3, 19940, 0, -37920, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1486")
    SetChrPos(0x4, 19940, 0, -37920, 0)
    SetChrPos(0x5, 19940, 0, -37920, 0)
    Jump("loc_14A5")

    label("loc_1486")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14A5")
    SetChrPos(0x4, 19940, 0, -37920, 0)

    label("loc_14A5")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14AE")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_14CF")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_189F")

    label("loc_14CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_14F6")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    Jump("loc_189F")

    label("loc_14F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_15A0")
    SetChrPos(0x9, 9470, 2500, 5580, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 11770, 2500, 4330, 45)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 11440, 2410, 7980, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 9580, 2500, 7830, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 13290, 2410, 9400, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_189F")

    label("loc_15A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15F9")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, -11910, 2490, 8950, 45)
    SetChrPos(0x10, -12830, 2500, 9870, 45)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_189F")

    label("loc_15F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1627")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jump("loc_189F")

    label("loc_1627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_165A")
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x9, 0x16)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1655")
    ClearChrFlags(0xB, 0x80)

    label("loc_1655")

    Jump("loc_189F")

    label("loc_165A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1688")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jump("loc_189F")

    label("loc_1688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16BB")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jump("loc_189F")

    label("loc_16BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16EE")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jump("loc_189F")

    label("loc_16EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1798")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -3560, 2500, 28520, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -9470, 2500, 29190, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x1F, 0x10)
    SetChrFlags(0x20, 0x10)
    SetChrFlags(0x21, 0x10)
    Jump("loc_189F")

    label("loc_1798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1806")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -3560, 2500, 28520, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -9470, 2500, 29190, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_189F")

    label("loc_1806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_184F")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -3560, 2500, 28520, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -9470, 2500, 29190, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_189F")

    label("loc_184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1875")
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x9, 0x16)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_189F")

    label("loc_1875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_189F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189F")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189F")
    SetChrFlags(0xB, 0x10)

    label("loc_189F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18BA")
    Event(0, 41)

    label("loc_18BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E5")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_18E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_18F9")
    ClearScenarioFlags(0x22, 0)
    Event(0, 42)
    Jump("loc_193E")

    label("loc_18F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_190D")
    ClearScenarioFlags(0x22, 1)
    Event(0, 44)
    Jump("loc_193E")

    label("loc_190D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1927")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 3)
    Event(0, 48)
    Jump("loc_193E")

    label("loc_1927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_193E")
    ClearScenarioFlags(0x22, 3)
    SetMapFlags(0x10000000)
    SetScenarioFlags(0x1, 3)
    Event(0, 60)

    label("loc_193E")

    Return()

    # Function_7_11C8 end

    def Function_8_193F(): pass

    label("Function_8_193F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1954")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 2)

    label("loc_1954")

    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1983")
    Jump("loc_1A10")

    label("loc_1983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1991")
    Jump("loc_1A10")

    label("loc_1991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19AB")
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    Jump("loc_1A10")

    label("loc_19AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19C5")
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x2)
    Jump("loc_1A10")

    label("loc_19C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_19D3")
    Jump("loc_1A10")

    label("loc_19D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19ED")
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    Jump("loc_1A10")

    label("loc_19ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_19FB")
    Jump("loc_1A10")

    label("loc_19FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A10")
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)

    label("loc_1A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A3F")
    SetMapObjFrame(0xFF, "ibc_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x1, 0x1)
    Jump("loc_1A60")

    label("loc_1A3F")

    SetMapObjFrame(0xFF, "ibc_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x0, 0x1)

    label("loc_1A60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A79")
    ClearMapObjFlags(0x6, 0x4)
    Jump("loc_1A7F")

    label("loc_1A79")

    SetMapObjFlags(0x6, 0x4)

    label("loc_1A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A97")
    ClearMapFlags(0x2000)
    Jump("loc_1A9E")

    label("loc_1A97")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_1A9E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC0")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ADB")
    OP_1B(0x8, 0x0, 0x3B)

    label("loc_1ADB")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -5540, 2500, 32280, 8000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B0F")
    SetMapObjFlags(0x5, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x0, 0x1)

    label("loc_1B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B22")
    OP_1B(0x8, 0x0, 0x43)

    label("loc_1B22")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B3A")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1B3A")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B56")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_1B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B68")
    OP_65(0x1, 0x1)
    Jump("loc_1BCC")

    label("loc_1B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B7C")
    ClearMapObjFlags(0x12, 0x4)
    Jump("loc_1BCC")

    label("loc_1B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1B8E")
    OP_65(0x1, 0x1)
    Jump("loc_1BCC")

    label("loc_1B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BA2")
    ClearMapObjFlags(0x12, 0x4)
    Jump("loc_1BCC")

    label("loc_1BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1BB4")
    OP_65(0x1, 0x1)
    Jump("loc_1BCC")

    label("loc_1BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1BC8")
    ClearMapObjFlags(0x12, 0x4)
    Jump("loc_1BCC")

    label("loc_1BC8")

    OP_65(0x1, 0x1)

    label("loc_1BCC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BEB")
    OP_10(0x2, 0x0)
    OP_10(0x9, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0xA, 0x1)
    Jump("loc_1BF7")

    label("loc_1BEB")

    OP_10(0x2, 0x1)
    OP_10(0x9, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0xA, 0x0)

    label("loc_1BF7")

    OP_52(0x47, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20A4")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xAF, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_20A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2153")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)

    label("loc_2153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21B5")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x2C, 0xAF, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)

    label("loc_21B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_21C9")
    OP_24(0x7B)
    ClearScenarioFlags(0x1, 3)
    Jump("loc_21E5")

    label("loc_21C9")

    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)

    label("loc_21E5")

    Return()

    # Function_8_193F end

    def Function_9_21E6(): pass

    label("Function_9_21E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_221D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_221D")
    Call(0, 65)
    Return()

    label("loc_221D")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_222A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E70")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_227A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_227A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229A")
    OP_AF(0x80)
    Jump("loc_229C")

    label("loc_229A")

    OP_AF(0x81)

    label("loc_229C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E6B")

    label("loc_22AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22BF")
    Jump("loc_2E6B")

    label("loc_22BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_234C")

    #C0001
    ChrTalk(
        0xFE,
        (
            "唔，看来苦西红柿苏打\x01",
            "还有很大的改良余地。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "为了做出人人爱喝的美味饮料，\x01",
            "我还要继续努力才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6B")

    label("loc_234C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_246B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F2")

    #C0003
    ChrTalk(
        0xFE,
        "各位辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "虽然不是本店原创的饮料，\x01",
            "但在疲劳的时候，\x01",
            "建议饮用『运动汽水Ｘ』！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "喝下之后能补充大量能量，\x01",
            "可以继续努力工作！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2466")

    label("loc_23F2")


    #C0006
    ChrTalk(
        0xFE,
        (
            "刚才接到联络……\x01",
            "在百货店工作的妈妈\x01",
            "平安无事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "来，各位也喝点\x01",
            "『运动汽水Ｘ』，\x01",
            "打起精神来吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2466")

    Jump("loc_2E6B")

    label("loc_246B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2479")
    Jump("loc_2E6B")

    label("loc_2479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_24B6")

    #C0008
    ChrTalk(
        0xFE,
        (
            "各位真是热情高涨啊……\x01",
            "甚至让人有点害怕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6B")

    label("loc_24B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_25DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255C")

    #C0009
    ChrTalk(
        0xFE,
        "各位辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "虽然不是本店原创的饮料，\x01",
            "但在疲劳的时候，\x01",
            "建议饮用『运动汽水Ｘ』！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "喝下之后能补充大量能量，\x01",
            "可以继续努力工作！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25D5")

    label("loc_255C")


    #C0012
    ChrTalk(
        0xFE,
        (
            "虽然不是本店原创的饮料，\x01",
            "但在疲劳的时候，\x01",
            "建议饮用『运动汽水Ｘ』！\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "喝下之后能补充大量能量，\x01",
            "可以继续努力工作！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D5")

    Jump("loc_2E6B")

    label("loc_25DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_270D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2695")

    #C0014
    ChrTalk(
        0xFE,
        (
            "武装集团占领玛因兹的事件\x01",
            "真是好可怕啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "或许是因为发生了这件事，\x01",
            "从今早开始，关于独立的\x01",
            "讨论比以往更加热烈了……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "老实说，我还不知该\x01",
            "如何判断。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2708")

    label("loc_2695")


    #C0017
    ChrTalk(
        0xFE,
        (
            "或许是因为发生了占领事件，\x01",
            "从今早开始，关于独立的\x01",
            "讨论比以往更加热烈了……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "老实说，我还不知该\x01",
            "如何判断。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2708")

    Jump("loc_2E6B")

    label("loc_270D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_271B")
    Jump("loc_2E6B")

    label("loc_271B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2812")

    #C0019
    ChrTalk(
        0xFE,
        (
            "从刚才开始，那些警察\x01",
            "就慌慌张张的。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "莫非又发生\x01",
            "什么事件了吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_280D")

    #C0021
    ChrTalk(
        0x101,
        (
            "#00008F（在这里似乎可以进行\x01",
            "  美食向导的取材……）\x02\x03",

            "#00003F（但现在不是做这种事的时候，\x01",
            "  以后别忘了再过来一趟。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_280D")

    Jump("loc_2E6B")

    label("loc_2812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_295B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28EB")

    #C0022
    ChrTalk(
        0xFE,
        (
            "我在这里开果汁店\x01",
            "差不多有一年了，\x01",
            "多亏大家捧场，生意还算不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "不仅知名度越来越高，\x01",
            "最近采用的『限时供应』\x01",
            "也很有成效。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "呵呵，人总是很难抵挡\x01",
            "限定这类字眼，\x01",
            "我自己也是一样呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2956")

    label("loc_28EB")


    #C0025
    ChrTalk(
        0xFE,
        (
            "把新饮品当作\x01",
            "限时供应品来卖，\x01",
            "是我妈妈的提议……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "妈妈真是个天生的生意人。\x01",
            "她总能教给我很多东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2956")

    Jump("loc_2E6B")

    label("loc_295B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2D")

    #C0027
    ChrTalk(
        0xFE,
        (
            "欢迎光临！\x01",
            "要不要来杯新鲜的果汁～？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "现在还有以热门话题『独立』为主题，\x01",
            "所有原料均采用克洛斯贝尔特产的\x01",
            "限定饮料哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "请一定尝尝这杯\x01",
            "浓缩了克洛斯贝尔\x01",
            "各种美味的终极饮品！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2AB6")

    label("loc_2A2D")


    #C0030
    ChrTalk(
        0xFE,
        (
            "现在还有以热门话题『独立』为主题，\x01",
            "所有原料均采用克洛斯贝尔特产的\x01",
            "限定饮料哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "请一定尝尝这杯浓缩了\x01",
            "自治州各种美味的终极饮品！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB6")

    Jump("loc_2E6B")

    label("loc_2ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2BE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5F")

    #C0032
    ChrTalk(
        0xFE,
        (
            "今天要召开正式会议，\x01",
            "兰花塔那边\x01",
            "好像被封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "我本来还想\x01",
            "去看看呢，\x01",
            "真是遗憾。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "不过，考虑到安全问题，\x01",
            "封锁也是当然的吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BDB")

    label("loc_2B5F")


    #C0035
    ChrTalk(
        0xFE,
        (
            "今天要召开正式会议，\x01",
            "兰花塔那边\x01",
            "好像被封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "考虑到安全问题，\x01",
            "这也是当然的。\x01",
            "但作为一名市民，还是觉得有些遗憾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BDB")

    Jump("loc_2E6B")

    label("loc_2BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C6E")

    #C0037
    ChrTalk(
        0xFE,
        (
            "上午的时候，连这一带\x01",
            "也是人山人海，\x01",
            "现在的人流总算是少些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "呵呵，但多亏如此，\x01",
            "今天的销售额已经\x01",
            "超过往日的平均数了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6B")

    label("loc_2C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2CEB")

    #C0039
    ChrTalk(
        0xFE,
        (
            "欢迎光临！\x01",
            "要不要来杯新鲜的果汁～？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "现在还提供以开始于\x01",
            "明天的通商会议为主题，\x01",
            "专门制作的特别饮品哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6B")

    label("loc_2CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2CF9")
    Jump("loc_2E6B")

    label("loc_2CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2E6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D59")

    #C0041
    ChrTalk(
        0xFE,
        (
            "好、好精彩的\x01",
            "追捕行动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "呵呵，警察们\x01",
            "似乎也都很努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6B")

    label("loc_2D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E11")

    #C0043
    ChrTalk(
        0xFE,
        (
            "欢迎光临！\x01",
            "要不要来杯新鲜的果汁～？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "现在还提供用特殊进口原料\x01",
            "制成的限时饮品哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "如果错过这次机会，以后就\x01",
            "再也品尝不到这种全新风味了，\x01",
            "请一定要尝尝看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E6B")

    label("loc_2E11")


    #C0046
    ChrTalk(
        0xFE,
        (
            "现在还提供用特殊进口原料\x01",
            "制成的限时饮品哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "在销售期结束之前，\x01",
            "请一定要尝尝看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E6B")

    Jump("loc_222A")

    label("loc_2E70")

    TalkEnd(0xFE)
    Return()

    # Function_9_21E6 end

    def Function_10_2E74(): pass

    label("Function_10_2E74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F32")

    #C0048
    ChrTalk(
        0xFE,
        "克洛斯贝尔出现了异常事态……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "咳咳，\x01",
            "在这种时候，更需要\x01",
            "市民们团结一心。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "不要输～克洛斯贝尔！\x01",
            "加油啊～麦克道尔议长！\x01",
            "……来，请各位也一起高呼吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F8A")

    label("loc_2F32")


    #C0051
    ChrTalk(
        0xFE,
        (
            "咳咳……\x01",
            "来，请各位也一起高呼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "不要输～克洛斯贝尔！\x01",
            "加油啊～麦克道尔议长！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8A")

    Jump("loc_3A13")

    label("loc_2F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F9D")
    Jump("loc_3A13")

    label("loc_2F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FE3")

    #C0053
    ChrTalk(
        0xFE,
        "迪塔总统万岁～！！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "绝不原谅帝国和共和国～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A13")

    label("loc_2FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30BD")

    #C0055
    ChrTalk(
        0xFE,
        (
            "当时的惨状，直到如今依然历历在目……\x01",
            "伊莉娅小姐竟然会……！\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "可恶……武装集团真是不可饶恕！\x01",
            "帝国政府也同样不可饶恕！！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "事已至此，我们也只有坚决独立，\x01",
            "抗战到底这一条出路了……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_313B")

    label("loc_30BD")


    #C0058
    ChrTalk(
        0xFE,
        (
            "可恶……武装集团真是不可饶恕！\x01",
            "帝国政府也同样不可饶恕！！\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "事已至此，我们也只有坚决独立，\x01",
            "抗战到底这一条出路了……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313B")

    Jump("loc_3A13")

    label("loc_3140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_321F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31DB")

    #C0060
    ChrTalk(
        0xFE,
        (
            "唔，矿山镇竟然会出事。\x01",
            "这段时期真是令人烦闷啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "……总之，今天是期待已久的\x01",
            "新版舞剧公演日！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "我要尽情享受一番！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_321A")

    label("loc_31DB")


    #C0063
    ChrTalk(
        0xFE,
        (
            "今天是期待已久的\x01",
            "新版舞剧公演日！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "我要尽情享受一番！\x02",
    )

    CloseMessageWindow()

    label("loc_321A")

    Jump("loc_3A13")

    label("loc_321F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_331D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32CD")

    #C0065
    ChrTalk(
        0xFE,
        (
            "终于……终于明天就是\x01",
            "新版舞剧公演了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "兴奋之情真是难以抑制……\x01",
            "……唔，这场雨正适合\x01",
            "给发热的身体降降温啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "总算可以保持冷静了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3318")

    label("loc_32CD")


    #C0068
    ChrTalk(
        0xFE,
        (
            "……唔，这场雨正适合\x01",
            "给发热的身体降降温啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "总算可以保持冷静了。\x02",
    )

    CloseMessageWindow()

    label("loc_3318")

    Jump("loc_3A13")

    label("loc_331D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3440")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F4")

    #C0070
    ChrTalk(
        0xFE,
        (
            "离『金之太阳、银之月』的\x01",
            "新版舞剧公演还有两天……！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "嗯……如果换算成小时，大概是多久呢？\x01",
            "演出时间是傍晚……\x01",
            "看来还有四十八小时以上呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "（坐立不安）……\x01",
            "唔～真是心痒难耐啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_343B")

    label("loc_33F4")


    #C0073
    ChrTalk(
        0xFE,
        (
            "（坐立不安）……\x01",
            "好希望后天早点到来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "唔～真是心痒难耐啊！\x02",
    )

    CloseMessageWindow()

    label("loc_343B")

    Jump("loc_3A13")

    label("loc_3440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34A1")

    #C0075
    ChrTalk(
        0xFE,
        (
            "离『金之太阳、银之月』的\x01",
            "新版舞剧公演还有两天……！\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "唔～真是心痒难耐啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A13")

    label("loc_34A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3540")

    #C0077
    ChrTalk(
        0xFE,
        (
            "离彩虹剧团的\x01",
            "新版舞剧公演\x01",
            "终于只剩三天了！\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "实不相瞒……\x01",
            "这次我还幸运地\x01",
            "弄到了首场公演的票！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        "唔，已经期待得不行了！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35C1")

    label("loc_3540")


    #C0080
    ChrTalk(
        0xFE,
        (
            "话说回来，前几天公布的\x01",
            "新版演员表还真是令人惊讶。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "修利·亚特雷德……\x01",
            "年仅十三岁就能出演那种\x01",
            "重要角色，真是后生可畏啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35C1")

    Jump("loc_3A13")

    label("loc_35C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_36D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3682")

    #C0082
    ChrTalk(
        0xFE,
        (
            "记得是下午开始吧。\x01",
            "终于要在兰花塔召开\x01",
            "正式会议了！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "唔，为了让会议取得更大成功，\x01",
            "我来送上声援吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "#4S迪塔市长……！\x01",
            "我们市民衷心\x01",
            "支持您哦～！！#3S\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_36D1")

    label("loc_3682")


    #C0085
    ChrTalk(
        0xFE,
        "来，再喊一嗓子……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "#4S麦克道尔议长……！\x01",
            "请和市长一起加油吧～！！#3S\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D1")

    Jump("loc_3A13")

    label("loc_36D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3766")

    #C0087
    ChrTalk(
        0xFE,
        (
            "兰花塔……！\x01",
            "多么优雅壮丽啊！！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "我越来越喜欢\x01",
            "这座城市了！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "这样一来，克洛斯贝尔\x01",
            "又多了一座著名建筑！\x01",
            "很好，很好！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A13")

    label("loc_3766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_386E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3815")

    #C0090
    ChrTalk(
        0xFE,
        (
            "唔，各国首脑\x01",
            "明天就要来\x01",
            "克洛斯贝尔了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "而且，明天也是举行\x01",
            "兰花塔揭幕式的日子。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "哎呀呀，一想到这些就好兴奋，\x01",
            "今晚恐怕会睡不着觉了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3869")

    label("loc_3815")


    #C0093
    ChrTalk(
        0xFE,
        (
            "唔，一想到明天的事就好兴奋，\x01",
            "今晚恐怕会\x01",
            "睡不着觉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "不然干脆熬个通宵吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3869")

    Jump("loc_3A13")

    label("loc_386E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_38CF")

    #C0095
    ChrTalk(
        0xFE,
        (
            "早上好，今天下雨呢。\x01",
            "不过，偶尔下点雨也不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "嗯，克洛斯贝尔真是太棒了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A13")

    label("loc_38CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_395F")

    #C0097
    ChrTalk(
        0xFE,
        (
            "你们刚才\x01",
            "堆沙袋的时候，\x01",
            "手脚还挺利索的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "一开始我还在奇怪，\x01",
            "不知你们到底想干什么……\x01",
            "嗯，干得漂亮！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A13")

    label("loc_395F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C0")

    #C0099
    ChrTalk(
        0xFE,
        "早上好，今天也是个好天气啊。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "这种天气最适合散步了。\x01",
            "嗯，很好，很好！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A13")

    label("loc_39C0")


    #C0101
    ChrTalk(
        0xFE,
        "我很喜欢克洛斯贝尔的街景。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "虽然总有令人不安的传闻，\x01",
            "但我还是爱这座城市。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A13")

    TalkEnd(0xFE)
    Return()

    # Function_10_2E74 end

    def Function_11_3A17(): pass

    label("Function_11_3A17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3BA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AA0")

    #C0103
    ChrTalk(
        0xFE,
        (
            "被捕的那些家伙开的车……\x01",
            "好像相当昂贵啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "那是乌尔努公司的最新型吗？\x01",
            "真是受不了那些有钱人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA9")

    label("loc_3AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B1F")

    #C0105
    ChrTalk(
        0xFE,
        (
            "自教团事件以来，\x01",
            "议会也完全变了啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "虽然我们财务科依旧很忙，\x01",
            "但和以前相比，\x01",
            "拥有的权限却宽松多了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BA9")

    label("loc_3B1F")


    #C0107
    ChrTalk(
        0xFE,
        (
            "不管怎么说，那些与帝国、\x01",
            "共和国勾结的议员们都被\x01",
            "肃清了，影响确实很大啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "虽然仍不能无视\x01",
            "两大国的意向……\x01",
            "但起色还是显而易见的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BA9")

    TalkEnd(0xFE)
    Return()

    # Function_11_3A17 end

    def Function_12_3BAD(): pass

    label("Function_12_3BAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3D76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D05")

    #C0109
    ChrTalk(
        0xFE,
        (
            "那棵大树究竟是怎么回事……？\x01",
            "居然还泛着蓝白色的光芒。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "最近这段时间，令人难以置信的事情\x01",
            "接连不断地发生，\x01",
            "而那棵树真是尤为诡异啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "……你们真的准备\x01",
            "冲到那东西里面去？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00003F……嗯，\x01",
            "事到如今，我们没有理由退缩。\x02\x03",

            "#00000F市内就拜托你们了，弗兰茨。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "嗯、嗯，放心吧。\x01",
            "……你们一定要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D71")

    label("loc_3D05")


    #C0114
    ChrTalk(
        0xFE,
        (
            "我们现在只能各尽其职，\x01",
            "做好自己力所能及的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "总之，这里就交给我们吧。\x01",
            "……你们一定要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D71")

    Jump("loc_4827")

    label("loc_3D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3D84")
    Jump("loc_4827")

    label("loc_3D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3D92")
    Jump("loc_4827")

    label("loc_3D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DA0")
    Jump("loc_4827")

    label("loc_3DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3DAE")
    Jump("loc_4827")

    label("loc_3DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E87")

    #C0116
    ChrTalk(
        0xFE,
        (
            "今早竟然就已经完全复原了……\x01",
            "警备队真了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "警备队和警察一样，\x01",
            "最近总是被人看扁，\x01",
            "但他们实际上还是很能干的。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "昨天看到他们在现场努力工作的样子，\x01",
            "我真是大受鼓舞，勇气倍增。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F10")

    label("loc_3E87")


    #C0119
    ChrTalk(
        0xFE,
        (
            "警备队和警察一样，\x01",
            "最近总是被人看扁，\x01",
            "但他们实际上还是很能干的。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "昨天看到他们在现场努力工作的样子，\x01",
            "我真是大受鼓舞，勇气倍增。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F10")

    Jump("loc_4827")

    label("loc_3F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3F23")
    Jump("loc_4827")

    label("loc_3F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3FA8")

    #C0121
    ChrTalk(
        0xFE,
        (
            "最近这段时间，市外各处好像\x01",
            "都出现了所谓的『幻兽』。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "据说打倒以后，\x01",
            "就会呼地一下消失掉……\x01",
            "听起来真是诡异啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4827")

    label("loc_3FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_435D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F0")

    #C0123
    ChrTalk(
        0xFE,
        (
            "通商会议的恐怖袭击骚乱\x01",
            "对克洛斯贝尔警察来说，\x01",
            "真是个很大的打击啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "大家对警察的信赖感刚刚有些改善，\x01",
            "这下又落回了原点……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "我光是像这样站在街上，\x01",
            "都能深刻地感受到\x01",
            "市民们的责难。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "不过，你们特别任务支援科\x01",
            "就另当别论了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#00006F哪里……\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        (
            "#00108F不过，所谓的责难\x01",
            "有那么明显吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "嗯，在巡逻时听到的\x01",
            "责骂明显比以前\x01",
            "更加刺耳了。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "比如『毫无意义地在这里警戒，真是辛苦了』……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "『都是因为你们太无能，我们才会\x01",
            "  被两大国骑在头上』等等。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "虽然无法否认，\x01",
            "但遭到那么过分的攻击，\x01",
            "还是让人很郁闷……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        (
            "#00206F原来如此……\x01",
            "说得确实很刻薄啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#00303F不过，无论别人怎么看，\x01",
            "我们也只能尽力做好自己\x01",
            "力所能及的事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x109,
        (
            "#10101F嗯，就算只是\x01",
            "微薄的力量，有与没有\x01",
            "还是完全不同的。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，所以不必\x01",
            "太在意风评。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "哈哈……确实如各位所说。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "谢谢，\x01",
            "我的心情好多了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 5)
    Jump("loc_4358")

    label("loc_42F0")


    #C0139
    ChrTalk(
        0xFE,
        (
            "你们说的没错，\x01",
            "我们只能做好自己该做的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "悲观失望也无济于事……\x01",
            "还是打起精神，努力工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4358")

    Jump("loc_4827")

    label("loc_435D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_436E")
    Call(0, 13)
    Jump("loc_4827")

    label("loc_436E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_448A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4426")

    #C0141
    ChrTalk(
        0xFE,
        (
            "哦，是罗伊德啊。\x01",
            "广场今天自由开放，\x01",
            "你们可以随意参观哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "呼～就算站在这里观看，\x01",
            "揭幕式也相当壮观。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "人类竟然能建造出\x01",
            "那样的东西，\x01",
            "真是了不起。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4485")

    label("loc_4426")


    #C0144
    ChrTalk(
        0xFE,
        (
            "呼～就算站在这里观看，\x01",
            "揭幕式也相当壮观。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "人类竟然能建造出\x01",
            "那样的东西，\x01",
            "真是了不起。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4485")

    Jump("loc_4827")

    label("loc_448A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4680")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45EF")

    #C0146
    ChrTalk(
        0xFE,
        (
            "哟，罗伊德。\x01",
            "明天就是通商会议了。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "警备人员已经早早进入了戒严状态，\x01",
            "真是让人从现在就开始紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#00006F的确，首脑们\x01",
            "明天就要进入\x01",
            "克洛斯贝尔了。\x02\x03",

            "#00000F再加上兰花塔\x01",
            "也终于要公之于众。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "呼，怎么说呢，\x01",
            "总有些不可思议的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "总之，从明天开始的三天之内，\x01",
            "我们就一起加油，努力工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#00002F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 4)
    Jump("loc_467B")

    label("loc_45EF")


    #C0152
    ChrTalk(
        0xFE,
        (
            "前所未有的大规模国际会议……\x01",
            "越是认真去想这件事，\x01",
            "就越感到紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "呼，总之，\x01",
            "从明天开始的三天之内，\x01",
            "必须要鼓起干劲，努力工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_467B")

    Jump("loc_4827")

    label("loc_4680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4789")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_469B")
    Call(0, 14)
    Jump("loc_4784")

    label("loc_469B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_472C")

    #C0154
    ChrTalk(
        0xFE,
        (
            "虽然我很想成为搜查官……\x01",
            "但以前似乎被自己的\x01",
            "理想所束缚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "我已经想通了，\x01",
            "今后要面对真实的自己，\x01",
            "制定切合实际的目标。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 6)
    Jump("loc_4784")

    label("loc_472C")


    #C0156
    ChrTalk(
        0xFE,
        (
            "虽说只是小雨，\x01",
            "但冒雨警备可不轻松啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "罗伊德，你们也要注意一点，\x01",
            "可别感冒哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4784")

    Jump("loc_4827")

    label("loc_4789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47A4")
    Call(0, 14)
    Jump("loc_4827")

    label("loc_47A4")


    #C0158
    ChrTalk(
        0xFE,
        (
            "虽然我很想成为搜查官……\x01",
            "但以前似乎被自己的\x01",
            "理想所束缚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "我已经想通了，\x01",
            "今后要面对真实的自己，\x01",
            "制定切合实际的目标。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 6)

    label("loc_4827")

    TalkEnd(0xFE)
    Return()

    # Function_12_3BAD end

    def Function_13_482B(): pass

    label("Function_13_482B")

    OP_4B(0xB, 0xFF)
    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)
    OP_4B(0x21, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49AC")

    #C0160
    ChrTalk(
        0xB,
        (
            "实、实在抱歉，\x01",
            "今天要举行正式会议，\x01",
            "所以普通民众就……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x1F,
        "唔，不过，只是去广场看看，应该没问题吧……\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x20,
        (
            "是啊是啊，\x01",
            "我们难得来一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x21,
        (
            "好啦，让我们进去看一会就行了。\x01",
            "十分钟……不，五分钟就够了，好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "不……那个……\x01",
            "问题的重点并不在这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        (
            "#00200F（看来有民众在抗议\x01",
            "  封锁广场呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#00006F（嗯……\x01",
            "  弗兰茨也真不容易啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A92")

    label("loc_49AC")


    #C0167
    ChrTalk(
        0x21,
        (
            "五分钟……不，三分钟\x01",
            "就够了，这总行了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x20,
        (
            "对对，我们只要\x01",
            "稍微看一下就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x1F,
        (
            "嗯，只是去广场看看，\x01",
            "应该没问题吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "那、那个，总之，\x01",
            "不行就是不行……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#00003F（我们要过去的时候，\x01",
            "  还是悄悄从旁边走吧……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A92")

    OP_4C(0xB, 0xFF)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    OP_4C(0x21, 0xFF)
    Return()

    # Function_13_482B end

    def Function_14_4AA3(): pass

    label("Function_14_4AA3")

    RunExpression(0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xB, 0x101, 0)

    #C0172
    ChrTalk(
        0xB,
        (
            "哟，罗伊德，\x01",
            "听说你在搜查一科的研修\x01",
            "终于结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "而且头衔还变成了\x01",
            "高级搜查官……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xB,
        (
            "唉，我们本是警察学校的同期生，\x01",
            "现在却被你越抛越远了。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        (
            "#00012F哪里，没那回事啦。\x02\x03",

            "#00000F对了，弗兰茨，\x01",
            "你的搜查官考试结果如何？\x02\x03",

            "我记得你之前去考了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xB,
        (
            "呼，要是考上了，\x01",
            "肯定会第一个告诉你啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "结果自然是惨败……\x01",
            "老实说，这倒是让我彻底明白了，\x01",
            "自己根本就不适合当搜查官。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#00008F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        "呼，但多亏如此，也使我想通了。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "现在这份公共安全科的工作\x01",
            "也是很有价值的。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xB,
        (
            "我并没必要那么\x01",
            "执著于搜查官……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "我已经决定了，\x01",
            "今后要面对真实的自己，\x01",
            "制定切合实际的目标。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#00005F弗兰茨……\x02\x03",

            "#00002F是吗。\x01",
            "嗯，你能这么想，那真是再好不过了。\x02\x03",

            "既然如此，我们今后就在\x01",
            "各自的道路上努力前进吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xB,
        "嗯，当然！\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x109,
        (
            "#10102F（嗯～这就是\x01",
            "  男人之间的友情吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#00102F（是啊，还真有点羡慕他们。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x13E, 5)
    Return()

    # Function_14_4AA3 end

    def Function_15_4DFE(): pass

    label("Function_15_4DFE")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_15_4DFE end

    def Function_16_4E08(): pass

    label("Function_16_4E08")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_16_4E08 end

    def Function_17_4E12(): pass

    label("Function_17_4E12")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_17_4E12 end

    def Function_18_4E1C(): pass

    label("Function_18_4E1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4E2D")
    Jump("loc_51DD")

    label("loc_4E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE5")

    #C0187
    ChrTalk(
        0xFE,
        "哦，是支援科的各位啊。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        "#00000F嗯，你辛苦啦。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x102,
        "#00100F总部还没有修整完毕吧？\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "嗯，已经大致收拾过一遍了，\x01",
            "但还没有完全恢复……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "入口大厅的受损状况\x01",
            "非常严重。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "要想恢复接待处的职能，\x01",
            "恐怕还需要一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "顺便一说，接待方面的\x01",
            "事务暂时转移到\x01",
            "警察学校了。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "瑞贝卡小姐也在那边，\x01",
            "如果各位在工作中有什么事务\x01",
            "需要处理，可以过去找她。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#00002F原来如此，知道了。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x103,
        "#00200F多谢告知。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 4)
    Jump("loc_5041")

    label("loc_4FE5")


    #C0197
    ChrTalk(
        0xFE,
        (
            "总部还要再过一段时间\x01",
            "才能修整完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "如果各位有什么事务需要处理，\x01",
            "可以去警察学校。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5041")

    Jump("loc_51DD")

    label("loc_5046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_50E2")

    #C0199
    ChrTalk(
        0xFE,
        (
            "今天实施禁行令，\x01",
            "普通民众不得\x01",
            "前往兰花塔一带。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "如你们所见，很多人抗议说\x01",
            "『从没听说过这种事』……\x01",
            "但除了相关人员以外，一律禁止通过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DD")

    label("loc_50E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_514F")

    #C0201
    ChrTalk(
        0xFE,
        (
            "兰花塔前的广场中\x01",
            "有很多市民和游客，\x01",
            "非常热闹。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "揭幕式结束之后，\x01",
            "这里就一直人来人往。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DD")

    label("loc_514F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_51C6")

    #C0203
    ChrTalk(
        0xFE,
        "明天就要举行揭幕式了……\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "自新市政厅大楼开始施工算起，已经\x01",
            "过去了五年，如今终于迎来了这个时刻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DD")

    label("loc_51C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_51D4")
    Jump("loc_51DD")

    label("loc_51D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_51DD")

    label("loc_51DD")

    TalkEnd(0xFE)
    Return()

    # Function_18_4E1C end

    def Function_19_51E1(): pass

    label("Function_19_51E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_52FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A4")

    #C0205
    ChrTalk(
        0xFE,
        (
            "等到下午，首脑们就将\x01",
            "汇集到兰花塔……\x01",
            "正式会议也会随之开始。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "从至今为止的情况来看，\x01",
            "全程风平浪静的可能性\x01",
            "恐怕很低。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "总之，今天也要\x01",
            "打起十二分的精神。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_52F9")

    label("loc_52A4")


    #C0208
    ChrTalk(
        0xFE,
        (
            "老实说，\x01",
            "全程风平浪静的可能性\x01",
            "恐怕很低。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "总之，今天也要\x01",
            "打起十二分的精神。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F9")

    Jump("loc_54C8")

    label("loc_52FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_53A1")

    #C0210
    ChrTalk(
        0xFE,
        (
            "虽说今天人流量比不上纪念庆典的时候，\x01",
            "但也真是够多的。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "恐怖分子有可能会以破坏为目的\x01",
            "而发动突发性的恐怖袭击。\x01",
            "必须要保持警惕，注意监视才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54C8")

    label("loc_53A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_54C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_545C")

    #C0212
    ChrTalk(
        0xFE,
        (
            "各位首脑将在明天\x01",
            "穿过这片街区，\x01",
            "前往新市政厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "这里的视野良好，\x01",
            "是个很适合狙击\x01",
            "的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "在迎接首脑们进入\x01",
            "克洛斯贝尔时，\x01",
            "我们将采取特殊戒严措施。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_54C8")

    label("loc_545C")


    #C0215
    ChrTalk(
        0xFE,
        (
            "这里的视野良好，\x01",
            "是个很适合狙击\x01",
            "的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "在迎接首脑们进入\x01",
            "克洛斯贝尔时，\x01",
            "我们将采取特殊戒严措施。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54C8")

    TalkEnd(0xFE)
    Return()

    # Function_19_51E1 end

    def Function_20_54CC(): pass

    label("Function_20_54CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5546")

    #C0217
    ChrTalk(
        0xFE,
        (
            "竟然同时有\x01",
            "两个恐怖组织要来，\x01",
            "这不是在开玩笑吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "总之……无论如何都要在\x01",
            "混乱发生之前阻止他们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5649")

    label("loc_5546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_55C9")

    #C0219
    ChrTalk(
        0xFE,
        (
            "可恶，如果负责兰花塔那边的\x01",
            "警备工作，就可以亲眼看到\x01",
            "首脑们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "可我却只能看到装设着\x01",
            "防窥视玻璃的高级轿车。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5649")

    label("loc_55C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5649")

    #C0221
    ChrTalk(
        0xFE,
        (
            "周边四国的首脑们\x01",
            "竟然齐聚一堂……\x01",
            "说实话，这规模真是太大了。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "……我还是第一次经历\x01",
            "紧张程度如此高的警备活动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5649")

    TalkEnd(0xFE)
    Return()

    # Function_20_54CC end

    def Function_21_564D(): pass

    label("Function_21_564D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56EF")

    #C0223
    ChrTalk(
        0xC,
        "#01200F咕噜噜……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x109,
        (
            "#10100F蔡特，\x01",
            "你在这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x103,
        (
            "#00202F好像是陪\x01",
            "琪雅来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#00012F话说回来，\x01",
            "你还真是完全融入这个城市了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_570A")

    label("loc_56EF")


    #C0227
    ChrTalk(
        0xC,
        "#01200F咕噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_570A")

    TalkEnd(0xFE)
    Return()

    # Function_21_564D end

    def Function_22_570E(): pass

    label("Function_22_570E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5772")

    #C0228
    ChrTalk(
        0xFE,
        "你好，要来个气球吗～？\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "想要两个或三个也可以，\x01",
            "今天想拿几个就拿几个。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_57CB")

    label("loc_5772")


    #C0230
    ChrTalk(
        0xFE,
        (
            "今天下午的活动\x01",
            "还包括把气球\x01",
            "做成各种样子的教学哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "如果有兴趣，\x01",
            "请一定要参加～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57CB")

    TalkEnd(0xFE)
    Return()

    # Function_22_570E end

    def Function_23_57CF(): pass

    label("Function_23_57CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_588C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_582A")

    #C0232
    ChrTalk(
        0x22,
        (
            "琪雅说她今天\x01",
            "要去图书馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x22,
        "是不是想查什么东西呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_588C")

    label("loc_582A")


    #C0234
    ChrTalk(
        0x22,
        (
            "昨天来找我们一起玩的秦，\x01",
            "好像坐今天的列车回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x22,
        (
            "真有点寂寞……\x01",
            "明明刚刚才成为好朋友。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_588C")

    TalkEnd(0xFE)
    Return()

    # Function_23_57CF end

    def Function_24_5890(): pass

    label("Function_24_5890")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_592B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58FA")

    #C0236
    ChrTalk(
        0x23,
        (
            "可恶，竟然不让进，\x01",
            "真是小气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x23,
        (
            "唉，不然就想些办法，\x01",
            "偷溜进去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_592B")

    label("loc_58FA")


    #C0238
    ChrTalk(
        0x23,
        (
            "啊啊，要是再不快点，\x01",
            "愉快的派对就要开始了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_592B")

    TalkEnd(0xFE)
    Return()

    # Function_24_5890 end

    def Function_25_592F(): pass

    label("Function_25_592F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5979")

    #C0239
    ChrTalk(
        0x24,
        "还是放弃吧，隆～\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x24,
        (
            "通商会议\x01",
            "并不是什么\x01",
            "开心的派对哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5979")

    TalkEnd(0xFE)
    Return()

    # Function_25_592F end

    def Function_26_597D(): pass

    label("Function_26_597D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_59BE")

    #N0241
    NpcTalk(
        0xFE,
        "市民",
        (
            "可恶的帝国和共和国，\x01",
            "尽管放马过来吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A4F")

    label("loc_59BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5A07")

    #C0242
    ChrTalk(
        0xFE,
        (
            "说什么兰花塔前的广场\x01",
            "今天禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        "唉，真无聊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A4F")

    label("loc_5A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5A15")
    Jump("loc_5A4F")

    label("loc_5A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5A4F")

    #C0244
    ChrTalk(
        0xFE,
        (
            "啊，好厉害啊。\x01",
            "就算在这里看，也觉得非常高！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A4F")

    TalkEnd(0xFE)
    Return()

    # Function_26_597D end

    def Function_27_5A53(): pass

    label("Function_27_5A53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5AA4")

    #N0245
    NpcTalk(
        0xFE,
        "市民",
        (
            "亚里欧斯先生担当国防长官的话，\x01",
            "独立之后也可以放心了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B17")

    label("loc_5AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5ADD")

    #C0246
    ChrTalk(
        0xFE,
        (
            "哎，好想像昨天一样，\x01",
            "站在近处仰望啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B17")

    label("loc_5ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5AEB")
    Jump("loc_5B17")

    label("loc_5AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5B17")

    #C0247
    ChrTalk(
        0xFE,
        (
            "是啊。\x01",
            "话说，这会不会太高了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B17")

    TalkEnd(0xFE)
    Return()

    # Function_27_5A53 end

    def Function_28_5B1B(): pass

    label("Function_28_5B1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5B5F")

    #C0248
    ChrTalk(
        0xFE,
        (
            "哈哈，不然我们店也搞个\x01",
            "纪念独立的特卖活动吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FDA")

    label("loc_5B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BD1")

    #C0249
    ChrTalk(
        0xFE,
        (
            "你也听说了吧？\x01",
            "之前那起袭击事件\x01",
            "好像是帝国策动的阴谋。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "我绝对不会\x01",
            "原谅帝国。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5C54")

    label("loc_5BD1")


    #C0251
    ChrTalk(
        0xFE,
        (
            "通过这次的事情，我终于明白了。\x01",
            "就算我们对帝国唯命是从，\x01",
            "他们也丝毫没想过要保护我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "所以我们只能将独立之路\x01",
            "贯彻到底。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C54")

    Jump("loc_5FDA")

    label("loc_5C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5D6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CFC")

    #C0253
    ChrTalk(
        0xFE,
        (
            "没想到……\x01",
            "竟然会发生这种事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "希望警备队能尽力\x01",
            "把事件解决掉……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "但到了万不得已的时候，\x01",
            "我们也只能请求\x01",
            "两大国帮助了吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5D67")

    label("loc_5CFC")


    #C0256
    ChrTalk(
        0xFE,
        (
            "可是，受独立提案的影响，\x01",
            "我们和两大国之间的\x01",
            "关系已经恶化了……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "唔唔……\x01",
            "今后到底会怎么样呢……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D67")

    Jump("loc_5FDA")

    label("loc_5D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5D7A")
    Jump("loc_5FDA")

    label("loc_5D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5DDB")

    #C0258
    ChrTalk(
        0xFE,
        (
            "说起来……明天还要在\x01",
            "市民会馆召开\x01",
            "市民座谈会。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "唔，趁现在\x01",
            "去咨询一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FDA")

    label("loc_5DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5E88")

    #C0260
    ChrTalk(
        0xFE,
        (
            "单从心情来说，\x01",
            "我自然是赞成独立的……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "但如何在两大国的威胁之下\x01",
            "确保安全，才是最大的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "能用交涉来开拓道路固然最好，\x01",
            "但事情可没有那么简单。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FDA")

    label("loc_5E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5EDD")

    #C0263
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔是否应该独立……\x01",
            "唔，无论思考多少次，都很难得出答案啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FDA")

    label("loc_5EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5F64")

    #C0264
    ChrTalk(
        0xFE,
        (
            "只要有迪塔市长和麦克道尔议长\x01",
            "这两人在，本次会议\x01",
            "一定能取得丰厚成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "嗯，克洛斯贝尔未来的\x01",
            "经济形势一片光明啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FDA")

    label("loc_5F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5FDA")

    #C0266
    ChrTalk(
        0xFE,
        (
            "在这里也可以\x01",
            "很清楚地看到揭幕式。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "那座大楼在克洛斯贝尔的\x01",
            "任何地方都能看得见，\x01",
            "真是座庞大的建筑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FDA")

    TalkEnd(0xFE)
    Return()

    # Function_28_5B1B end

    def Function_29_5FDE(): pass

    label("Function_29_5FDE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5FEF")
    Jump("loc_6285")

    label("loc_5FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6032")

    #C0268
    ChrTalk(
        0xFE,
        (
            "对大家做出这么过分的事情……\x01",
            "帝国真是太可恶了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6285")

    label("loc_6032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6087")

    #C0269
    ChrTalk(
        0xFE,
        (
            "爸爸从昨天开始，\x01",
            "就一直很烦恼的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        "希望他能打起精神来……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6285")

    label("loc_6087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6095")
    Jump("loc_6285")

    label("loc_6095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_60F0")

    #C0271
    ChrTalk(
        0xFE,
        (
            "听说明天要在\x01",
            "市民会馆讨论\x01",
            "关于独立的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "嗯，大人们\x01",
            "真是厉害呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6285")

    label("loc_60F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_615F")

    #C0273
    ChrTalk(
        0xFE,
        (
            "嗯～我不是很明白。\x01",
            "既然是邻居，为什么\x01",
            "却不能好好相处呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "这就是那些大人\x01",
            "所说的隐情吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6285")

    label("loc_615F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_61BD")

    #C0275
    ChrTalk(
        0xFE,
        (
            "听大人们说，\x01",
            "独立之后会有好处，\x01",
            "但也有很多坏处。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        "嗯～我是不太明白啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6285")

    label("loc_61BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_621E")

    #C0277
    ChrTalk(
        0xFE,
        "听说今天是举行正式会议的日子。\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "好像是大家聚到一起，\x01",
            "讨论各种事情的活动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6285")

    label("loc_621E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6285")

    #C0279
    ChrTalk(
        0xFE,
        (
            "幕帘『哗』地一下揭开，\x01",
            "然后有烟花一样的东西\x01",
            "『咚咚』地冲上了天……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        "就好像庆典一样！\x02",
    )

    CloseMessageWindow()

    label("loc_6285")

    TalkEnd(0xFE)
    Return()

    # Function_29_5FDE end

    def Function_30_6289(): pass

    label("Function_30_6289")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_62C0")

    #C0281
    ChrTalk(
        0xFE,
        "嘿嘿，今天是个值得庆祝的日子啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_635B")

    label("loc_62C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_635B")

    #C0282
    ChrTalk(
        0xFE,
        (
            "市民会馆内正在\x01",
            "举行慈善宴会，\x01",
            "宴会中有很多有趣的活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "最重要的是，\x01",
            "这种通过娱乐活动使大家重振精神，\x01",
            "从而使城市复兴的创意真是太高明了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_635B")

    TalkEnd(0xFE)
    Return()

    # Function_30_6289 end

    def Function_31_635F(): pass

    label("Function_31_635F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6370")
    Jump("loc_6408")

    label("loc_6370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6408")

    #C0284
    ChrTalk(
        0xFE,
        (
            "这项活动好像是由\x01",
            "克洛斯贝尔市工商协会策划的。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "呵呵，工商协会的各位\x01",
            "真是很懂得如何激发大家的热情，\x01",
            "在每年创立纪念庆典的时候也是如此。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6408")

    TalkEnd(0xFE)
    Return()

    # Function_31_635F end

    def Function_32_640C(): pass

    label("Function_32_640C")

    TalkBegin(0xFE)

    #C0286
    ChrTalk(
        0xFE,
        "市民们的狂热真是惊人……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "或许是因为这正是大家真心\x01",
            "期望的结果吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_640C end

    def Function_33_645E(): pass

    label("Function_33_645E")

    TalkBegin(0xFE)

    #C0288
    ChrTalk(
        0xFE,
        "再这样下去，恐怕会难以收场啊。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "还是趁早把\x01",
            "屏幕车收起来为好。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_645E end

    def Function_34_64AC(): pass

    label("Function_34_64AC")

    TalkBegin(0xFE)

    #C0290
    ChrTalk(
        0xFE,
        (
            "迪塔总统真是下了个\x01",
            "英明的决断啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔生活了这么多年，\x01",
            "从来没这么开心过。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_64AC end

    def Function_35_650F(): pass

    label("Function_35_650F")

    TalkBegin(0xFE)

    #C0292
    ChrTalk(
        0xFE,
        (
            "噢，女神啊，\x01",
            "请您保佑\x01",
            "克洛斯贝尔的未来……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_650F end

    def Function_36_6546(): pass

    label("Function_36_6546")

    TalkBegin(0xFE)

    #C0293
    ChrTalk(
        0xFE,
        "来，你们也一起高呼吧。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        "克洛斯贝尔独立国万岁！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_6546 end

    def Function_37_6585(): pass

    label("Function_37_6585")

    TalkBegin(0xFE)

    #C0295
    ChrTalk(
        0xFE,
        (
            "总统的演讲\x01",
            "真是太精彩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔今后\x01",
            "肯定会成为更加美好的地方！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_6585 end

    def Function_38_65DA(): pass

    label("Function_38_65DA")

    TalkBegin(0xFE)

    #C0297
    ChrTalk(
        0xFE,
        (
            "嘿嘿，大家好像\x01",
            "都很高兴。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_65DA end

    def Function_39_6600(): pass

    label("Function_39_6600")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6696")

    #C0298
    ChrTalk(
        0xFE,
        (
            "在下雨天，\x01",
            "可以听到各种声音，很有趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "水面、雨伞、地面……\x01",
            "雨点打在不同的地方，会有不同的声音，\x01",
            "感觉就像一场交响乐演奏。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6718")

    label("loc_6696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6718")

    #C0300
    ChrTalk(
        0xFE,
        (
            "我的头发很容易翘……\x01",
            "但一到下雨天，\x01",
            "头发就会变得柔顺听话。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "所以我很喜欢下雨……\x01",
            "啊，不好意思，尽说些无聊的话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6718")

    TalkEnd(0xFE)
    Return()

    # Function_39_6600 end

    def Function_40_671C(): pass

    label("Function_40_671C")

    EventBegin(0x0)
    SoundLoad(445)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x16, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)
    OP_68(10760, 4740, 5470, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10000, 0)
    OP_93(0xE, 0x5A, 0x0)
    OP_93(0x19, 0x5A, 0x0)
    SetChrPos(0x101, 5150, 2500, 9860, 90)
    SetChrPos(0x102, 4000, 2500, 11070, 90)
    SetChrPos(0x104, 4740, 2500, 7860, 90)
    SetChrPos(0x103, 3500, 2500, 9070, 90)
    OP_0D()
    Sound(445, 2, 40, 0)

    #C0302
    ChrTalk(
        0x11,
        "好、好震撼的演讲啊……\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x18,
        (
            "#6P没想到竟然会宣布\x01",
            "克洛斯贝尔独立……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x19,
        (
            "#6P而且还把帝国和共和国\x01",
            "说成那样……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x17,
        (
            "#12P说起两大国的『暗斗』……？\x01",
            "莫非以前发生的那起事故也是由于……？\x02",
        )
    )

    CloseMessageWindow()

    #N0306
    NpcTalk(
        0xD,
        "市民",
        "#12P可恶的帝国和共和国……！！\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xF,
        (
            "#6P……迄今为止，可曾有人为克洛斯贝尔\x01",
            "说过那种令人痛快淋漓的话？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x16,
        (
            "克洛斯贝尔的政治家们，\x01",
            "全都是一群被帝国和共和国\x01",
            "豢养的蠢货……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x19,
        (
            "虽然也有像麦克道尔议长\x01",
            "那样的正直者……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x18,
        (
            "#6P但是从没有人\x01",
            "能让我们感受到\x01",
            "如此激情啊……！\x02",
        )
    )

    CloseMessageWindow()

    #N0311
    NpcTalk(
        0xE,
        "市民",
        (
            "#6P而且还任命克洛斯贝尔的守护神\x01",
            "亚里欧斯先生为国防长官！\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x11,
        (
            "#5P这真是再合适不过的人选了。\x01",
            "只要有他一马当先，\x01",
            "率领军队守护克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x17,
        "#12P嘿嘿，我们就天不怕地不怕了！\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x16,
        (
            "克洛斯贝尔的独立\x01",
            "也许并不是痴人说梦……！\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xF,
        (
            "#6P只要把一切都交给迪塔市长……\x01",
            "不，迪塔总统，就没有任何问题了！\x02",
        )
    )

    CloseMessageWindow()
    OP_25(0x1BD, 0x3C)

    #N0316
    NpcTalk(
        0xD,
        "市民",
        (
            "#12P嗯，只要有他在，\x01",
            "帝国和共和国都不足为惧……！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x18,
        "#6P迪塔总统……！\x02",
    )

    CloseMessageWindow()

    #N0318
    NpcTalk(
        0xE,
        "市民",
        "#6P迪塔总统！\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0319
    ChrTalk(
        0x16,
        "#5S迪塔总统万岁！#3S\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("市民们")

    #A0320
    AnonymousTalk(
        0xFF,
        "#5S迪塔总统万岁！！#3S\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_25(0x1BD, 0x50)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0321
    ChrTalk(
        0xF,
        "#5S克洛斯贝尔独立国万岁！#3S\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("市民们")

    #A0322
    AnonymousTalk(
        0xFF,
        "#5S#6P克洛斯贝尔独立国万岁！！#3S\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x14, 0xE1, 0x1F4)
    Sleep(50)
    OP_93(0x15, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x14, 0xB4, 0x1F4)
    Sleep(50)
    OP_93(0x15, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0x14, 0xE1, 0x1F4)
    Sleep(50)
    OP_93(0x15, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x14, 0xB4, 0x1F4)
    Sleep(50)
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(300)
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(50)
    OP_93(0x15, 0x10E, 0x1F4)
    Sleep(100)
    OP_64(0x14)
    OP_64(0x15)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("市民们")

    #A0323
    AnonymousTalk(
        0xFF,
        "#5S迪塔总统万岁！！#3S\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetChrName("市民们")

    #A0324
    AnonymousTalk(
        0xFF,
        "#5S克洛斯贝尔独立国万岁！！#3S\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(3730, 4740, 8080, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10000, 0)
    Fade(500)
    OP_0D()
    OP_25(0x1BD, 0x32)
    Sleep(500)
    OP_25(0x1BD, 0x1E)

    #C0325
    ChrTalk(
        0x101,
        "#6P#00005F……真是惊人的狂热啊。\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        "#6P#00108F嗯……但也可以理解他们的心情。\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x103,
        (
            "#6P#00201F不会因为激动过头\x01",
            "而引起什么骚动吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x104,
        (
            "#12P#00303F没事，有国防军的士兵在，\x01",
            "在闹大之前就会收场的……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        "#6P#00001F……总之，我们快走吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopSound(445, 1000, 30)
    OP_93(0xE, 0x0, 0x0)
    OP_93(0x19, 0xB4, 0x0)
    SetChrPos(0x0, 6520, 2490, 7410, 90)
    OP_4C(0x9, 0xFF)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x16, 0xFF)
    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    OP_4C(0x19, 0xFF)
    OP_4C(0x1A, 0xFF)
    SetScenarioFlags(0x18E, 4)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_40_671C end

    def Function_41_6EF3(): pass

    label("Function_41_6EF3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SoundLoad(803)
    OP_68(-17770, 3700, 27070, 0)
    MoveCamera(33, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -18000, 2500, 27800, 180)
    SetChrPos(0x102, -18000, 2500, 25600, 0)
    SetChrPos(0x109, -19200, 2500, 26700, 90)
    SetChrPos(0x105, -16800, 2500, 26700, 270)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetCameraDistance(17500, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_702B():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_702B)
    Sleep(50)

    def lambda_703B():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_703B)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)

    #C0330
    ChrTalk(
        0x101,
        "#5P#00005F哦，大概是科长吧。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        (
            "#12P#00102F从时间来看，差不多\x01",
            "也该和我们联络了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    #Sound(2084, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0332
    AnonymousTalk(
        0x101,
        (
            "#00000F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0333
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，辛苦了。\x02\x03",

            "早上也和你们说过，\x01",
            "来警察学校一趟。\x02\x03",

            "知道具体位置吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0334
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004F嗯，当然。\x02\x03",

            "#00000F从西克洛斯贝尔街道\x01",
            "途中的大门进去就是了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0335
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，门已经打开了。\x02\x03",

            "另外……\x01",
            "你们已经在市内巡视一圈了吧？\x02\x03",

            "坦率地说，有何感想？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0336
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0337
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F……这个嘛。\x02\x03",

            "#00001F不少地方似乎都散发着火药味，\x01",
            "感觉局势开始变得紧张起来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，今后还要进一步磨练\x01",
            "这种敏锐的直觉。\x02\x03",

            "就这样吧，我在这边等你们。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0339
    AnonymousTalk(
        0x101,
        "#00000F明白了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(813, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sleep(300)

    #C0340
    ChrTalk(
        0x102,
        "#12P#00100F果然是科长啊。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x109,
        (
            "#6P#10105F你们好像谈了些\x01",
            "很令人在意的事情……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(150)

    #C0342
    ChrTalk(
        0x101,
        (
            "#5P#00006F嗯，科长似乎也\x01",
            "觉察到了局势的变化。\x02\x03",

            "#00001F我们最好将黑月和雷克特大尉的\x01",
            "情况也报告给科长一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x102,
        "#12P#00106F是啊……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x105,
        (
            "#11P#10300F那么，我们差不多\x01",
            "也该去警察学校了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        "#5P#00000F嗯，从西出口出去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可以在克洛斯贝尔\x01",
            "市内地图中选择\x01",
            "『西克洛斯贝尔街道』了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -18000, 2500, 27800, 180)
    OP_69(0xFF, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 8370, 2390, -14850, 90)
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    SetScenarioFlags(0x126, 5)
    OP_29(0xA1, 0x1, 0x4)
    OP_24(0x323)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_41_6EF3 end

    def Function_42_75DB(): pass

    label("Function_42_75DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51231.itc", 0x1E)
    SoundLoad(835)
    SoundLoad(821)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x41, 0x1E)
    SetChrSubChip(0x41, 0x0)
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x8000)
    SetChrChipByIndex(0x42, 0x1E)
    SetChrSubChip(0x42, 0x0)
    ClearChrFlags(0x42, 0x80)
    SetChrFlags(0x42, 0x8000)
    SetChrChipByIndex(0x43, 0x1E)
    SetChrSubChip(0x43, 0x0)
    ClearChrFlags(0x43, 0x80)
    SetChrFlags(0x43, 0x8000)
    SetChrChipByIndex(0x44, 0x1E)
    SetChrSubChip(0x44, 0x0)
    ClearChrFlags(0x44, 0x80)
    SetChrFlags(0x44, 0x8000)
    SetChrChipByIndex(0x45, 0x1E)
    SetChrSubChip(0x45, 0x0)
    ClearChrFlags(0x45, 0x80)
    SetChrFlags(0x45, 0x8000)
    ClearChrFlags(0x32, 0x80)
    OP_78(0x7, 0x32)
    OP_49()
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    ClearChrFlags(0x33, 0x80)
    OP_78(0x8, 0x33)
    OP_49()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    ClearChrFlags(0x34, 0x80)
    OP_78(0x9, 0x34)
    OP_49()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    ClearChrFlags(0x35, 0x80)
    OP_78(0xA, 0x35)
    OP_49()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    ClearChrFlags(0x36, 0x80)
    OP_78(0xF, 0x36)
    OP_49()
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetMapObjFrame(0xF, "light", 0x0, 0x1)
    ClearChrFlags(0x37, 0x80)
    OP_78(0x10, 0x37)
    OP_49()
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFrame(0x10, "light", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x41, 10700, 2460, 7850, 225)
    SetChrPos(0x42, 6400, 2500, 10900, 225)
    SetChrPos(0x43, 2950, 2490, 15000, 225)
    SetChrPos(0x44, 1300, 2500, 7350, 45)
    SetChrPos(0x45, 2900, 2500, 5750, 45)
    SetChrPos(0x32, 15000, 2400, 8750, 0)
    OP_D5(0x32, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x33, 4550, 2400, 1400, 315)
    OP_D5(0x33, 0x0, 0x4CE78, 0x0, 0x0)
    SetChrPos(0x34, -2850, 2400, 8850, 315)
    OP_D5(0x34, 0x0, 0x4CE78, 0x0, 0x0)
    SetChrPos(0x35, 22500, 2500, -350, 270)
    OP_D5(0x35, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x36, 32500, 2500, -350, 270)
    OP_D5(0x36, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x37, 45000, 2500, -350, 270)
    OP_D5(0x37, 0x0, 0x41EB0, 0x0, 0x0)
    BeginChrThread(0x35, 1, 0, 43)
    BeginChrThread(0x36, 1, 0, 43)
    BeginChrThread(0x37, 1, 0, 43)
    OP_68(6450, 4000, 6050, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18500, 0)
    OP_68(1350, 4000, 11150, 9000)
    MoveCamera(40, 20, 0, 9000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(458, 0, 100, 0)
    Sleep(4000)
    Sound(494, 0, 60, 0)
    Sleep(2000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_75DB end

    def Function_43_793F(): pass

    label("Function_43_793F")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 17150, 2500, 450)
    OP_9F(0x1, 4400, 2500, 8350)
    OP_9F(0x1, -4000, 2500, 21250)
    OP_9F(0x1, -5850, 2500, 32500)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_43_793F end

    def Function_44_7985(): pass

    label("Function_44_7985")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28000.itc", 0x23)
    LoadChrToIndex("chr/ch27600.itc", 0x24)
    ClearChrFlags(0x32, 0x80)
    OP_78(0xE, 0x32)
    OP_49()
    SetChrPos(0x32, 6200, 2500, 12300, 315)
    OP_D5(0x32, 0x0, 0x4CE78, 0x0, 0x0)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    OP_74(0xE, 0x1E)
    OP_70(0xE, 0x6)
    SetChrPos(0x0, 21600, 2500, 5700, 0)
    SetChrPos(0x1, 21600, 2500, 5700, 0)
    SetChrPos(0x2, 21600, 2500, 5700, 0)
    SetChrPos(0x3, 21600, 2500, 5700, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    OP_4B(0x14, 0xFF)
    SetChrChipByIndex(0x14, 0xD)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -3700, 2500, 16900, 135)
    OP_4B(0x15, 0xFF)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -4000, 2500, 18100, 135)
    SetChrChipByIndex(0x39, 0x0)
    SetChrSubChip(0x39, 0x0)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    SetChrPos(0x39, 4200, 2500, 6700, 45)
    SetChrChipByIndex(0x3A, 0x1)
    SetChrSubChip(0x3A, 0x0)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    SetChrPos(0x3A, 3000, 2500, 6900, 45)
    SetChrChipByIndex(0x3B, 0x2)
    SetChrSubChip(0x3B, 0x0)
    ClearChrFlags(0x3B, 0x80)
    SetChrFlags(0x3B, 0x8000)
    SetChrPos(0x3B, 3000, 2500, 8500, 45)
    SetChrChipByIndex(0x3C, 0x23)
    SetChrSubChip(0x3C, 0x0)
    ClearChrFlags(0x3C, 0x80)
    SetChrFlags(0x3C, 0x8000)
    SetChrPos(0x3C, 2400, 2500, 9200, 45)
    SetChrChipByIndex(0x3D, 0x24)
    SetChrSubChip(0x3D, 0x0)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    SetChrPos(0x3D, 1200, 2500, -2400, 0)
    SetChrChipByIndex(0x3E, 0x9)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    SetChrPos(0x3E, 2900, 2500, -2300, 0)
    SetChrChipByIndex(0x3F, 0xA)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    SetChrPos(0x3F, -7200, 2500, 6400, 90)
    SetChrChipByIndex(0x40, 0xF)
    SetChrSubChip(0x40, 0x0)
    ClearChrFlags(0x40, 0x80)
    SetChrFlags(0x40, 0x8000)
    SetChrPos(0x40, -2400, 2500, 3400, 45)
    OP_68(6700, 4000, 11200, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(5700, 3500, 10200, 10000)
    MoveCamera(45, 17, 0, 10000)
    SetCameraDistance(18000, 10000)
    BeginChrThread(0x32, 3, 0, 45)
    BeginChrThread(0x14, 3, 0, 46)
    BeginChrThread(0x15, 3, 0, 47)
    OP_63(0x39, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, 120, -1, -1)
    SetChrName("麦克道尔议长")

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W当然，对于现状，\x01",
            "每个人都有自己的观点。\x02\x03",

            "但是，当今的政府并不是\x01",
            "通过民主程序而建立的！\x02\x03",

            "所谓的独立宣言，是在众多自治州\x01",
            "议员遭受关押，甚至连我都被软禁\x01",
            "的情况下发表的！\x02\x03",

            "因此，我在此必须指出，\x01",
            "此宣言并未得到议会的承认，\x01",
            "只是个人性质的独裁行为！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_7985 end

    def Function_45_7DA8(): pass

    label("Function_45_7DA8")

    Sleep(2000)

    def lambda_7DB0():
        OP_96(0xFE, 0xAF0, 0x9C4, 0x11F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_7DB0)
    Sleep(500)

    def lambda_7DCD():
        OP_96(0xFE, 0xFFFFFF38, 0x9C4, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_7DCD)
    Sleep(500)

    def lambda_7DEA():
        OP_96(0xFE, 0x384, 0x9C4, 0x1A2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_7DEA)
    Sleep(500)

    def lambda_7E07():
        OP_96(0xFE, 0x1194, 0x9C4, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_7E07)
    WaitChrThread(0x3D, 1)
    OP_63(0x3D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x40, 1)
    OP_63(0x40, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x3E, 1)
    Return()

    # Function_45_7DA8 end

    def Function_46_7E5F(): pass

    label("Function_46_7E5F")

    Sleep(8000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_7E79():
        OP_96(0xFE, 0x8FC, 0x9C4, 0x2AF8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7E79)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_46_7E5F end

    def Function_47_7EA4(): pass

    label("Function_47_7EA4")

    Sleep(8200)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_7EBE():
        OP_96(0xFE, 0x7D0, 0x9C4, 0x2FA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7EBE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_47_7EA4 end

    def Function_48_7EDF(): pass

    label("Function_48_7EDF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadChrToIndex("apl/ch51719.itc", 0x14)
    LoadChrToIndex("apl/ch51718.itc", 0x15)
    LoadChrToIndex("chr/ch32050.itc", 0x16)
    LoadChrToIndex("chr/ch32051.itc", 0x17)
    LoadChrToIndex("chr/ch32056.itc", 0x19)
    LoadChrToIndex("chr/ch32150.itc", 0x1A)
    LoadChrToIndex("chr/ch32151.itc", 0x1B)
    LoadChrToIndex("chr/ch32152.itc", 0x1C)
    LoadChrToIndex("monster/ch85150.itc", 0x1D)
    LoadChrToIndex("monster/ch85151.itc", 0x1E)
    LoadChrToIndex("monster/ch85153.itc", 0x1F)
    LoadEffect(0x0, "event/ev17034.eff")
    LoadEffect(0x1, "event/ev17061.eff")
    LoadEffect(0x2, "battle\\cr313000.eff")
    LoadEffect(0x3, "battle\\ms00001.eff")
    LoadEffect(0x4, "battle\\ms00000.eff")
    LoadEffect(0x5, "event/eva01_01.eff")
    LoadEffect(0x7, "battle\\mg042_00.eff")
    SoundLoad(123)
    SetChrPos(0x0, 21600, 2500, 5700, 0)
    SetChrPos(0x1, 21600, 2500, 5700, 0)
    SetChrPos(0x2, 21600, 2500, 5700, 0)
    SetChrPos(0x3, 21600, 2500, 5700, 0)
    SetChrChipByIndex(0x27, 0x14)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -4500, 2500, 20500, 0)
    SetChrChipByIndex(0x28, 0x15)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, -4800, 2500, 20000, 0)
    SetChrChipByIndex(0x29, 0x16)
    SetChrSubChip(0x29, 0x0)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, -7500, 2500, 20000, 0)
    SetChrChipByIndex(0x2A, 0x1A)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -8000, 2500, 20500, 0)
    SetChrChipByIndex(0x25, 0x1D)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x26, 0x1D)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x32, 0x80)
    OP_78(0x7, 0x32)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x32, 18500, 2500, 700, 295)
    OP_D5(0x32, 0x0, 0x48058, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    ClearChrFlags(0x33, 0x80)
    OP_78(0x11, 0x33)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x33, 10700, 2500, 4300, 300)
    OP_D5(0x33, 0x0, 0x493E0, 0x0, 0x0)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0xB5, 0xF0, 0x0, 0x20)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0348
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K同日，１０：３０──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7573", 0)
    OP_68(8000, 5000, 10500, 0)
    MoveCamera(50, 3, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(40000, 0)
    OP_68(4000, 5000, 10500, 7000)
    MoveCamera(40, 5, 0, 7000)
    SetCameraDistance(43000, 7000)
    Sound(123, 2, 30, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopSound(123, 500, 40)
    Fade(500)
    OP_68(-6100, 4300, 34500, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16500, 0)
    SetCameraDistance(15500, 5000)
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_4B(0x25, 0xFF)
    BeginChrThread(0x25, 3, 0, 55)
    Sleep(400)
    OP_4B(0x26, 0xFF)
    BeginChrThread(0x26, 3, 0, 55)
    BeginChrThread(0x46, 1, 0, 57)
    Sound(825, 2, 40, 0)
    PlayEffect(0x7, 0x0, 0xFF, 0x0, -6100, 2500, 34500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1388)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x0)
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_82E4():
        OP_A6(0xFE, 0x0, 0x64, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_82E4)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8310():
        OP_A6(0xFE, 0x0, 0x64, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_8310)
    Sleep(4500)
    EndChrThread(0x46, 0x1)
    StopSound(825, 1500, 40)
    CancelBlur(500)
    Sleep(500)
    SetChrChipByIndex(0x25, 0x1D)
    SetChrSubChip(0x25, 0x0)
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x26, 0x1D)
    SetChrSubChip(0x26, 0x0)
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Fade(250)
    OP_68(-5500, 3500, 28500, 0)
    MoveCamera(35, 15, 10, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_68(-5500, 3700, 34000, 2000)
    MoveCamera(43, 15, 10, 2000)
    SetCameraDistance(14500, 2000)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x28, 0x80)
    BeginChrThread(0x29, 3, 0, 49)
    Sleep(300)
    BeginChrThread(0x28, 3, 0, 50)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7544", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x29, 3)
    WaitChrThread(0x28, 3)
    WaitChrThread(0x25, 3)
    WaitChrThread(0x26, 3)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x27, 0x80)
    BeginChrThread(0x27, 3, 0, 52)
    Sleep(300)
    BeginChrThread(0x2A, 3, 0, 51)
    WaitChrThread(0x27, 3)
    OP_6F(0x79)

    #C0349
    ChrTalk(
        0x27,
        "扫清！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x2A, 3)
    OP_93(0x2A, 0x87, 0x1F4)

    #C0350
    ChrTalk(
        0x2A,
        "#5P趁现在！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-300, 4000, 13000, 0)
    MoveCamera(100, 31, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0x27, -3500, 2500, 30500, 0)
    SetChrPos(0x28, -3800, 2500, 32000, 0)

    def lambda_8498():

        label("loc_8498")

        TurnDirection(0xFE, 0x33, 500)
        Yield()
        Jump("loc_8498")

    QueueWorkItem2(0x2A, 2, lambda_8498)
    OP_68(-6100, 5000, 33000, 3700)
    MoveCamera(25, 21, 0, 3700)
    SetCameraDistance(15000, 3700)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    BeginChrThread(0x33, 3, 0, 56)
    Sleep(300)
    BeginChrThread(0x32, 3, 0, 56)
    BeginChrThread(0x46, 1, 0, 58)
    WaitChrThread(0x32, 3)
    EndChrThread(0x2A, 0x2)
    ClearChrFlags(0x29, 0x4)
    SetChrChipByIndex(0x29, 0x17)
    SetChrSubChip(0x29, 0x0)

    def lambda_8505():
        OP_95(0xFE, -7500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8505)
    Sleep(50)
    ClearChrFlags(0x28, 0x4)

    def lambda_8527():
        OP_95(0xFE, -4500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8527)
    Sleep(50)
    ClearChrFlags(0x27, 0x4)

    def lambda_8549():
        OP_95(0xFE, -4500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_8549)
    Sleep(50)
    ClearChrFlags(0x2A, 0x4)
    SetChrChipByIndex(0x2A, 0x1B)
    SetChrSubChip(0x2A, 0x0)

    def lambda_8573():
        OP_95(0xFE, -7500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_8573)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    SetScenarioFlags(0x22, 7)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_48_7EDF end

    def Function_49_85A9(): pass

    label("Function_49_85A9")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0x29, 0x17)
    SetChrSubChip(0x29, 0x0)

    def lambda_85C9():
        OP_96(0xFE, 0xFFFFE2B4, 0x9C4, 0x6978, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85C9)

    #C0351
    ChrTalk(
        0x29,
        "#10A喝啊啊啊！\x02",
    )
    #Auto

    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x29, 0x19)
    SetChrSubChip(0x29, 0x2)
    Sound(251, 0, 60, 0)

    def lambda_8607():
        OP_9D(0xFE, 0xFFFFE2B4, 0xDAC, 0x80E8, 0x5DC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8607)
    WaitChrThread(0xFE, 1)
    Sound(815, 0, 100, 0)
    SetChrSubChip(0x29, 0x3)
    BeginChrThread(0x26, 3, 0, 54)
    Sleep(1000)
    SetChrSubChip(0x29, 0x4)

    def lambda_863F():
        OP_9D(0xFE, 0xFFFFE2B4, 0x9C4, 0x7D00, 0xC8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_863F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x29, 0x16)
    SetChrSubChip(0x29, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_49_85A9 end

    def Function_50_866C(): pass

    label("Function_50_866C")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)

    def lambda_8684():
        OP_96(0xFE, 0xFFFFED40, 0x9C4, 0x6D60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8684)
    Sleep(500)

    #C0352
    ChrTalk(
        0x28,
        "#16A哦哦哦哦哦！\x02",
    )
    #Auto

    WaitChrThread(0xFE, 1)
    Sound(844, 0, 70, 0)

    def lambda_86BF():
        OP_9D(0xFE, 0xFFFFED40, 0x9C4, 0x7DC8, 0x384, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86BF)
    Sound(532, 0, 100, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(500)
    Sound(538, 0, 50, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 0, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x7)
    WaitChrThread(0xFE, 1)
    Sound(246, 0, 100, 0)
    Sound(196, 0, 70, 0)
    BeginChrThread(0x25, 3, 0, 53)
    Sleep(1000)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_50_866C end

    def Function_51_874B(): pass

    label("Function_51_874B")

    SetChrChipByIndex(0x2A, 0x1B)
    SetChrSubChip(0x2A, 0x0)

    def lambda_8758():
        OP_96(0xFE, 0xFFFFE0C0, 0x9C4, 0x7724, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8758)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x2A, 0x1A)
    SetChrSubChip(0x2A, 0x0)
    Return()

    # Function_51_874B end

    def Function_52_877A(): pass

    label("Function_52_877A")


    def lambda_877F():
        OP_96(0xFE, 0xFFFFEE6C, 0x9C4, 0x7724, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_877F)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_52_877A end

    def Function_53_87A3(): pass

    label("Function_53_87A3")

    OP_82(0xFA, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_87DD():
        OP_A6(0xFE, 0x0, 0x64, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_87DD)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1700, -500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 1700, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    PlayEffect(0x1, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_88A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_88A2)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_53_87A3 end

    def Function_54_88B6(): pass

    label("Function_54_88B6")

    OP_82(0xFA, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(501, 0, 100, 0)

    def lambda_88F6():
        OP_A6(0xFE, 0x0, 0x64, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_88F6)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 1700, -300, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    MoveCamera(43, 15, 5, 4000)
    SetCameraDistance(16000, 4000)
    Sound(985, 0, 100, 0)
    PlayEffect(0x1, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_899E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_899E)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_54_88B6 end

    def Function_55_89B2(): pass

    label("Function_55_89B2")

    Sound(530, 0, 50, 0)
    Sound(567, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 2850, -15000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0xFA, 0xFA, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8A32():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8A32)
    Sound(501, 0, 50, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 2850, 200, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 2850, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_55_89B2 end

    def Function_56_8AD2(): pass

    label("Function_56_8AD2")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3100, 2500, 10400)
    OP_9F(0x1, -3900, 2500, 20900)
    OP_9F(0x1, -5600, 2500, 35700)
    OP_9F(0x2, 0xFE, 10000, 0x6)

    def lambda_8B0E():
        OP_96(0xFE, 0xFFFFEA20, 0x1D4C, 0xED1C, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8B0E)
    OP_D5(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1F4)
    Return()

    # Function_56_8AD2 end

    def Function_57_8B37(): pass

    label("Function_57_8B37")

    Sleep(500)
    Sound(207, 0, 60, 0)
    Sleep(1000)

    label("loc_8B43")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8B65")
    Sound(246, 0, 70, 0)
    Sleep(300)
    Sound(246, 0, 60, 0)
    Sleep(400)
    Jump("loc_8B43")

    label("loc_8B65")

    Return()

    # Function_57_8B37 end

    def Function_58_8B66(): pass

    label("Function_58_8B66")

    Sound(458, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(2000)
    Sound(487, 0, 100, 0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Return()

    # Function_58_8B66 end

    def Function_59_8B8B(): pass

    label("Function_59_8B8B")

    EventBegin(0x1)

    #C0353
    ChrTalk(
        0x101,
        (
            "#00001F『国防军』的士兵\x01",
            "正在兰花塔一带\x01",
            "森严警备。\x02\x03",

            "#00003F……我们还是不要过去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -5600, 2500, 34230, 180)
    EventEnd(0x4)
    Return()

    # Function_59_8B8B end

    def Function_60_8BFA(): pass

    label("Function_60_8BFA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch44100.itc", 0x14)
    LoadChrToIndex("chr/ch47500.itc", 0x15)
    LoadChrToIndex("chr/ch23600.itc", 0x16)
    LoadChrToIndex("chr/ch30600.itc", 0x17)
    LoadChrToIndex("chr/ch30000.itc", 0x18)
    LoadEffect(0x6, "event\\eva04_00.eff")
    SoundLoad(975)
    SetChrPos(0x101, 18940, 2500, -19860, 180)
    SetChrPos(0x102, 19960, 2500, -18870, 180)
    SetChrPos(0x109, 17860, 2500, -18930, 180)
    SetChrPos(0x105, 19210, 2500, -18160, 180)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0x38, 0x80)
    SetChrFlags(0x38, 0x8000)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    OP_78(0xC, 0x38)
    SetChrPos(0x38, 19670, 2500, -22660, 0)
    OP_D5(0x38, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    OP_49()
    SetChrPos(0x36, 19940, 0, -58340, 0)
    OP_D5(0x36, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x36, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    ClearMapObjFlags(0xB, 0x4)
    OP_74(0xB, 0x1E)
    OP_78(0xB, 0x36)
    OP_71(0xB, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetChrFlags(0x33, 0x8000)
    SetChrFlags(0x34, 0x8000)
    SetChrFlags(0x35, 0x8000)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    OP_78(0x7, 0x32)
    OP_78(0x8, 0x33)
    OP_78(0x9, 0x34)
    OP_78(0xA, 0x35)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x32, 19940, 0, -58340, 0)
    SetChrPos(0x33, 19940, 0, -58340, 0)
    SetChrPos(0x34, 14330, 2500, -18280, 135)
    SetChrPos(0x35, 20420, 2500, -12820, 180)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x33, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_D5(0x32, 0x0, 0x0, 0x0, 0x0)
    OP_D5(0x33, 0x0, 0x0, 0x0, 0x0)
    OP_D5(0x34, 0x0, 0x20F58, 0x0, 0x0)
    OP_D5(0x35, 0x0, 0x2BF20, 0x0, 0x0)
    OP_68(18610, 2750, -45640, 0)
    MoveCamera(46, 34, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(493, 0, 100, 0)
    BeginChrThread(0x36, 1, 0, 62)
    Sleep(800)
    OP_68(19110, 2750, -26510, 1500)
    MoveCamera(46, 28, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(18000, 1500)
    OP_63(0x33, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(487, 0, 100, 0)
    BeginChrThread(0x36, 3, 0, 61)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(500)

    #N0354
    NpcTalk(
        0x36,
        "瑞吉",
        "#10A呜哇！！？？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x36, 1)
    OP_6F(0x79)
    OP_0D()

    #N0355
    NpcTalk(
        0x36,
        "塞克斯",
        (
            "喂喂，刚才通过的时候，\x01",
            "没有这种东西吧！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("尤利")

    #N0356
    NpcTalk(
        0x36,
        "尤利",
        "啧，临时堆砌的路障吗……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(18610, 2750, -45640, 0)
    MoveCamera(46, 34, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    Sound(975, 2, 100, 0)
    Sound(459, 0, 100, 0)

    def lambda_8FFC():
        OP_96(0xFE, 0x4DE4, 0x0, 0xFFFF6BE0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_8FFC)
    Sleep(1000)

    def lambda_9019():
        OP_96(0xFE, 0x4DE4, 0x0, 0xFFFF4CA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_9019)
    OP_68(18540, 2750, -38950, 3000)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x32, 1)
    StopSound(975, 1000, 100)
    Sound(492, 0, 100, 0)
    OP_71(0x8, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x33, 1)
    OP_6F(0x1)
    Sound(462, 0, 100, 0)
    OP_71(0x7, 0x1, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    Fade(500)
    SetChrChipByIndex(0x2E, 0x17)
    SetChrChipByIndex(0xB, 0x18)
    SetChrSubChip(0x2E, 0x0)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0x2E, 17650, 0, -37870, 270)
    Sleep(500)
    Fade(500)
    SetChrPos(0xB, 22130, 0, -37520, 90)
    WaitChrThread(0x2E, 1)
    WaitChrThread(0xB, 1)
    BeginChrThread(0x2E, 1, 0, 63)
    Sleep(500)
    BeginChrThread(0xB, 1, 0, 64)
    OP_68(18370, 2750, -32299, 3000)
    Sleep(1000)
    Sound(461, 0, 100, 0)
    OP_71(0x7, 0x1F, 0x3C, 0x0, 0x0)
    OP_79(0x7)
    WaitChrThread(0x2E, 1)
    WaitChrThread(0xB, 1)
    OP_6F(0x1)
    OP_0D()

    #C0357
    ChrTalk(
        0x105,
        "#N#10302F呵呵，将了一军呢。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#N#00000F嗯，接下来……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x2E,
        "……好了，你们已经走投无路了！\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x2E,
        "乖乖投降吧！\x02",
    )

    CloseMessageWindow()
    SetChrName("塞克斯")

    #N0361
    NpcTalk(
        0x36,
        "塞克斯",
        "……唉，没办法了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(17170, 2750, -33200, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14520, 0)
    SetChrChipByIndex(0x2F, 0x14)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 17930, 230, -31970, 180)
    SetChrChipByIndex(0x30, 0x15)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 17480, 680, -30340, 180)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, 19560, 540, -30840, 180)
    SetChrPos(0x101, 21080, 70, -32549, 270)
    SetChrPos(0x102, 21550, 390, -31400, 270)
    SetChrPos(0x109, 22460, 820, -29860, 225)
    SetChrPos(0x105, 21200, 1010, -29170, 225)
    TurnDirection(0xB, 0x2F, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7518", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0362
    ChrTalk(
        0x31,
        (
            "是是，\x01",
            "我们投降啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x2F,
        (
            "哎呀呀，虽然无能，\x01",
            "但也会动些脑子啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0364
    ChrTalk(
        0x2E,
        (
            "你、你们……\x01",
            "就不能稍微\x01",
            "反省一下吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x2E,
        (
            "你们知道自己的行为\x01",
            "给多少人添了麻烦吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x31,
        (
            "是是，知道啦～\x01",
            "不要那么激动嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x30,
        (
            "过度生气，\x01",
            "可是会增加小细纹的哦，\x01",
            "大～婶。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0368
    ChrTalk(
        0x2E,
        "#4S大、大婶……！？\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x2E,
        (
            "我、我比你们\x01",
            "大不了几岁吧！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x2E, 500)
    Sleep(100)

    #C0370
    ChrTalk(
        0xB,
        "前、前辈，您冷静些……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x2F,
        (
            "好啦，想去哪里都随意，\x01",
            "赶快带我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x2F,
        (
            "反正你们也没有\x01",
            "惩罚我们的权力。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x109,
        "#10105F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x102,
        "#00101F………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x2E, 500)
    Sleep(100)

    #C0375
    ChrTalk(
        0x101,
        (
            "#00000F……凯特前辈。\x01",
            "总之，先把他们\x01",
            "带回总部吧。\x02\x03",

            "导力车也不能\x01",
            "一直停在\x01",
            "这种地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x2E,
        "唉……也是。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0x101, 500)
    Sleep(100)

    #C0377
    ChrTalk(
        0x2E,
        (
            "那么，支援科的各位，\x01",
            "请帮忙把他们带走吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0xB, 500)
    Sleep(100)

    #C0378
    ChrTalk(
        0x2E,
        "弗兰茨，拜托你收拾现场了。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xB,
        "是！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x2F, 500)
    Sleep(100)

    #C0380
    ChrTalk(
        0x101,
        "#00003F…………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c1150", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_60_8BFA end

    def Function_61_95F6(): pass

    label("Function_61_95F6")

    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 19800, 1410, -25000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 19270, 1410, -25000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 19800, 1410, -30710, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 19270, 1410, -30710, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 19420, 1410, -30710, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_61_95F6 end

    def Function_62_9716(): pass

    label("Function_62_9716")

    OP_96(0x36, 0x4D12, 0x0, 0xFFFF7B58, 0x3A98, 0x0)
    OP_9F(0x0, 0x36)
    OP_9F(0x1, 19500, 390, -31390)
    OP_9F(0x1, 19420, 1410, -27710)
    OP_9F(0x1, 19800, 1410, -27710)
    OP_9F(0x2, 0x36, 15000, 0x6)
    OP_D5(0x36, 0xFFFFD8F0, 0xAFC8, 0xFFFFD8F0, 0x0)
    Return()

    # Function_62_9716 end

    def Function_63_9775(): pass

    label("Function_63_9775")

    OP_97(0x2E, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
    OP_95(0x2E, 18560, 10, -34510, 1000, 0x0)
    TurnDirection(0x2E, 0x101, 500)
    Return()

    # Function_63_9775 end

    def Function_64_97A5(): pass

    label("Function_64_97A5")

    OP_97(0xB, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
    OP_95(0xB, 21150, 0, -34360, 1000, 0x0)
    TurnDirection(0xB, 0x101, 500)
    Return()

    # Function_64_97A5 end

    def Function_65_97D5(): pass

    label("Function_65_97D5")

    EventBegin(0x0)
    Fade(500)
    LoadEffect(0x0, "battle/it002_00.eff")
    OP_68(5880, 4740, -10040, 0)
    MoveCamera(7, 27, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(12150, 0)
    SetChrPos(0x101, 5420, 2500, -7460, 45)
    SetChrPos(0x102, 6250, 2500, -8390, 45)
    SetChrPos(0x103, 4250, 2500, -8350, 45)
    SetChrPos(0x104, 5120, 2500, -9330, 45)
    SetChrPos(0x109, 3220, 2500, -9240, 45)
    SetChrPos(0x105, 3990, 2500, -10270, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_0D()

    #C0381
    ChrTalk(
        0x8,
        (
            "欢迎光临，\x01",
            "要不要来杯果汁？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#00000F不好意思，打扰了，\x01",
            "我们是特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0383
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将『美食向导』取材一事的\x01",
            "情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0384
    ChrTalk(
        0x8,
        (
            "啊，是那件事啊，\x01",
            "我听说过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x8,
        (
            "那么，请尝尝这个吧。\x01",
            "这是本店的新饮品，\x01",
            "『苦西红柿苏打』！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9B38")

    #C0386
    ChrTalk(
        0x101,
        (
            "#00005F这、这好像是\x01",
            "麦克道尔议长爱喝的……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x8,
        (
            "嗯，他做了议长之后，\x01",
            "还是一如既往地\x01",
            "喜欢那种饮料……\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x8,
        (
            "这是将那款饮料改良之后\x01",
            "而推出的新饮品。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x8,
        (
            "用苏打缓和了苦味，\x01",
            "就算各位不喜欢苦西红柿的味道，\x01",
            "也可以享受美味，使身体更加健康。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BEA")

    label("loc_9B38")


    #C0390
    ChrTalk(
        0x101,
        "#00005F苦、苦西红柿……就是那种……\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x8,
        (
            "这是将苦西红柿果汁\x01",
            "改良之后而推出的新饮品。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x8,
        (
            "用苏打缓和了苦味，\x01",
            "就算各位不喜欢苦西红柿的味道，\x01",
            "也可以享受美味，使身体更加健康。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BEA")


    #C0393
    ChrTalk(
        0x102,
        "#00109F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x104,
        "#00306F（……喂，罗伊德，真的要喝吗？）\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#00006F（这、这也是工作，没办法……\x01",
            "  努力喝下去吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0396
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人喝下了苦西红柿苏打。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    PlayEffect(0x0, 0x0, 0x101, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x102, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x103, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x104, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0x109, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0x105, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_89(0x5, 0x0)
    Sound(235, 0, 100, 0)
    OP_32(0x0, 0xF7, 0x32)
    OP_32(0x1, 0xF7, 0x32)
    OP_32(0x2, 0xF7, 0x32)
    OP_32(0x3, 0xF7, 0x32)
    OP_32(0x8, 0xF7, 0x32)
    OP_32(0x4, 0xF7, 0x32)
    Sleep(1000)
    SetChrName("")

    #A0397
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全员的ＣＰ提升了５０。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0398
    ChrTalk(
        0x101,
        "#00010F#4S……呜哇……！！\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x109,
        (
            "#10106F咳、咳……！\x01",
            "这、这……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x103,
        (
            "#00206F……不是一般的苦。\x02\x03",

            "#00211F不如说，苏打的刺激口感\x01",
            "反而增强了苦味。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x8,
        "哎，是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x8,
        (
            "嗯……看来还有很大的\x01",
            "改良余地……\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x8,
        (
            "……那么，如果想换换口味，\x01",
            "可以尝尝本店的招牌饮品\x01",
            "『铃铛草莓果汁』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrName("")

    #A0404
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人喝下了铃铛草莓果汁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0405
    ChrTalk(
        0x102,
        (
            "#00102F（咕嘟咕嘟……）\x01",
            "啊，真好喝……\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，刚才的苦味\x01",
            "似乎也起了反衬作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#00012F（在美食向导上介绍的时候，\x01",
            "  还是推荐这种饮品\x01",
            "  比较好……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x172, 4)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A189")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A1A6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_A1B9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A1B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_A1CC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A1CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A1E9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_A1FC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_A219")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_A22C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A22C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A249")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_A25C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_A279")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A279")

    OP_29(0x80, 0x1, 0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A34E")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0408
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在六家饮食店完成了取材！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A345")

    #A0409
    AnonymousTalk(
        0x101,
        (
            "#00003F现在就可以去向\x01",
            "格蕾丝小姐报告了……\x02\x03",

            "#00000F不过，还没有把六个人\x01",
            "喜欢的美食全部找到。\x01",
            "不如再努努力吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A345")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_A34E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A411")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0410
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "找到了特别任务支援科\x01",
            "全体成员各自喜欢的美食。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0411
    AnonymousTalk(
        0x101,
        (
            "#00000F这样一来，已经找到\x01",
            "所有人喜欢的美食了啊。\x02\x03",

            "取材工作已经足够了，\x01",
            "马上去通讯社报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_A411")

    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 5330, 2500, -8020, 56)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_65_97D5 end

    def Function_66_A44B(): pass

    label("Function_66_A44B")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0412
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　  前方为兰花塔  　※\x01",
            "※　无关人员禁止入内　※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_66_A44B end

    def Function_67_A4A7(): pass

    label("Function_67_A4A7")

    EventBegin(0x1)

    #C0413
    ChrTalk(
        0x101,
        (
            "#00000F为了准备明天的会议，\x01",
            "兰花塔那边应该忙得不可开交吧。\x02\x03",

            "既然没什么事，\x01",
            "我们还是不要靠近了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -5600, 2500, 34230, 180)
    EventEnd(0x4)
    Return()

    # Function_67_A4A7 end

    def Function_68_A523(): pass

    label("Function_68_A523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6DC")
    EventBegin(0x0)
    Fade(500)
    OP_68(-4500, 3240, 25730, 0)
    MoveCamera(34, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16420, 0)
    OP_E2(0x3)
    SetChrPos(0x101, -3910, 2500, 21570, 315)
    SetChrPos(0x102, -2680, 2500, 20990, 315)
    SetChrPos(0x103, -5210, 2500, 19950, 315)
    SetChrPos(0x104, -3420, 2500, 19850, 315)
    SetChrPos(0xF4, -4620, 2500, 18200, 315)
    SetChrPos(0xF5, -1960, 2500, 19500, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sleep(500)

    #C0414
    ChrTalk(
        0x102,
        (
            "#12P#00101F……终究不能\x01",
            "随意接近兰花塔前一带啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x104,
        (
            "#12P#00306F是啊，如果被那些家伙发现了，\x01",
            "它们肯定会立刻\x01",
            "呼叫增援的。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        (
            "#12P#00001F……那会对我们的\x01",
            "作战行动造成影响。\x02\x03",

            "#00003F在被发现之前，还是赶快离开吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    SetScenarioFlags(0x1, 4)
    EventEnd(0x5)
    Jump("loc_A73B")

    label("loc_A6DC")

    EventBegin(0x1)
    SetChrName("")

    #A0417
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "兰花塔前有魔导兵在守卫，\x01",
            "还是离开为好。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -7830, 2500, 22590, 21)
    EventEnd(0x4)

    label("loc_A73B")

    Return()

    # Function_68_A523 end

    def Function_69_A73C(): pass

    label("Function_69_A73C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A74D")
    Jump("loc_AEAD")

    label("loc_A74D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A970")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0418
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "慈善宴会\x01",
            " 　『～同心协力，共建复兴之轮～』　　　 \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " 【活动概要】　　　　　　　　　　 \x01",
            " 　·钢琴独奏表演　\x01",
            " 　·克洛斯贝尔职业女性选秀活动\x01",
            " 　·大众美食竞赛\x01",
            " 　·各种才艺教学\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0419
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " 举办场所：克洛斯贝尔市民会馆·多功能大厅\x01",
            " 　　　　会馆前的广场　　\x01",
            " 举办日期：今日　　　　　　　　 \x01",
            " 举办方　：克洛斯贝尔工商协会／克洛斯贝尔市政府\x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " ※参加各种活动的费用\x01",
            " 　将全部以援助资金的形式投入复兴计划。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_AEAD")

    label("loc_A970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AB40")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0420
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " 市民座谈会　　　　　　　　　　　　\x01",
            " 　　『～请认真思考，　　　　 \x01",
            " 　　　　　　　　　探讨独立的利弊～』　　 \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " 【活动概要】　　　　　　　　　　 \x01",
            " 　·有识之士谈论独立问题的利弊　　　　　 \x01",
            " 　·由现役自治州议员参加的公开讨论会　　　 \x01",
            " 举办场所：克洛斯贝尔市民会馆·多功能大厅\x01",
            " 举办日期：今日　　　　　　　　 \x01",
            " 举办方　：克洛斯贝尔市政府／克洛斯贝尔通讯社\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_AEAD")

    label("loc_AB40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AD10")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0421
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " 市民座谈会　　　　　　　　　　　　\x01",
            " 　　『～请认真思考，　　　　 \x01",
            " 　　　　　　　　　探讨独立的利弊～』　　 \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " 【活动概要】　　　　　　　　　　 \x01",
            " 　·有识之士谈论独立问题的利弊　　　　　 \x01",
            " 　·由现役自治州议员参加的公开讨论会　　　 \x01",
            " 举办场所：克洛斯贝尔市民会馆·多功能大厅\x01",
            " 举办日期：明日　　　　　　　　 \x01",
            " 举办方　：克洛斯贝尔市政府／克洛斯贝尔通讯社\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_AEAD")

    label("loc_AD10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AD1E")
    Jump("loc_AEAD")

    label("loc_AD1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_AEA4")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0422
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " 面向入门者的投资家研讨会　　　　　　　　 \x01",
            "  『——如何解读未来的经济发展——』  \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " 举办场所：克洛斯贝尔市民会馆·多功能大厅\x01",
            " 举办日期：今日　　　　　　　　 \x01",
            " 主办者　：贸易商利泽罗　　　　　　　　　　 \x01",
            " ※席位有空余，\x01",
            " 　欢迎各位在本日　　　　　　　　　 \x01",
            " 　随时参加。　　　　　 \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_AEAD")

    label("loc_AEA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_AEAD")

    label("loc_AEAD")

    TalkEnd(0xFF)
    Return()

    # Function_69_A73C end

    def Function_70_AEB1(): pass

    label("Function_70_AEB1")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0423
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门紧紧地锁着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFEB")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF9B")

    #C0424
    ChrTalk(
        0x101,
        (
            "#00003F警察总部……\x01",
            "里面似乎没有人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x10A,
        (
            "#12P#00603F……昨天颁布戒严令以后，\x01",
            "这里就被国防军封锁了。\x02\x03",

            "#00600F总之，现在还是赶快走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        "#00001F嗯……明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFE8")

    label("loc_AF9B")


    #C0427
    ChrTalk(
        0x101,
        (
            "#00003F警察总部……\x01",
            "里面似乎没有人呢。\x02\x03",

            "#00001F总之，现在还是赶快走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFE8")

    SetScenarioFlags(0x1, 5)

    label("loc_AFEB")

    TalkEnd(0xFF)
    Return()

    # Function_70_AEB1 end

    SaveToFile()

Try(main)
