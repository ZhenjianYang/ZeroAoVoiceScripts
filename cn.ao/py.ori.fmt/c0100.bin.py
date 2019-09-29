from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0100.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c0100", "c0100_1", "c1000_1", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x06',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 7, 0, 8],
    )

    BuildStringList((
        "c0100",                  # 0
        "吉娜",                   # 1
        "昆提老人",               # 2
        "亚贝尔",                 # 3
        "米米",                   # 4
        "普鲁娜",                 # 5
        "利娜莉",                 # 6
        "哈斯",                   # 7
        "萨莉",                   # 8
        "柯贝",                   # 9
        "蔡特",                   # 10
        "琪雅",                   # 11
        "凯特巡警",               # 12
        "弗兰茨巡警",             # 13
        "警备队员",               # 14
        "警官",                   # 15
        "国防军士兵",             # 16
        "市民",                   # 17
        "市民",                   # 18
        "车",                     # 19
        "隆",                     # 20
        "亨利",                   # 21
        "琪雅",                   # 22
        "白隼",                   # 23
        "赛尔盖科长",             # 24
        "国防军士兵",             # 25
        "市民１",                 # 26
        "市民２",                 # 27
        "市民３",                 # 28
        "市民４",                 # 29
        "市民５",                 # 30
        "市民６",                 # 31
        "市民７",                 # 32
        "剧情用魔兽",             # 33
        "剧情用魔兽",             # 34
        "剧情用魔兽",             # 35
        "剧情用魔兽",             # 36
        "剧情用魔兽",             # 37
        "车",                     # 38
        "飙车族",                 # 39
        "警车1",                  # 40
        "警车2",                  # 41
        "警车3",                  # 42
        "车",                     # 43
        "车",                     # 44
        "车",                     # 45
        "兰迪",                   # 46
        "诺艾尔",                 # 47
        "瓦吉",                   # 48
        "SE控制",                 # 49
        "警官",                   # 50
        "警官",                   # 51
        "警官",                   # 52
        "警官",                   # 53
        "警官",                   # 54
        "气球摊子",               # 55
        "穆拉",                   # 56
        "奥利维尔",               # 57
        "bc0100",                 # 58
        "bc0100",                 # 59
        "中央广场",               # 60
        "西街",                   # 61
        "行政区",                 # 62
        "住宅街",                 # 63
        "欢乐街",                 # 64
        "东街",                   # 65
        "旧城区",                 # 66
        "港湾区",                 # 67
        "ＩＢＣ",                 # 68
        "站前街道",               # 69
        "后巷",                   # 70
        "乌尔斯拉间道",           # 71
        "东克洛斯贝尔街道",       # 72
        "西克洛斯贝尔街道",       # 73
        "玛因兹山道",             # 74
        "兰花塔",                 # 75
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_B4", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_D8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_DC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_E4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_E8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_EC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_F0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_F4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_F8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_FC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_104", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 0, 0, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_144", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0100", "Sepith_B4", 60, 30, 10, 0,
        (
            ("ms85100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7450", "ed7453", "ATBonus_94"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7450", "ed7453", "ATBonus_94"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_1E0", 0x004A, 3, 6, 45, 3, 3, 30, 0, "bc0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_E4", "ed7544", "ed7453", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch21300.itc",                   # 00
        "chr/ch20002.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20700.itc",                   # 03
        "chr/ch34600.itc",                   # 04
        "chr/ch22100.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch26000.itc",                   # 07
        "chr/ch48500.itc",                   # 08
        "chr/ch48600.itc",                   # 09
        "chr/ch02702.itc",                   # 0A
        "chr/ch30600.itc",                   # 0B
        "chr/ch30000.itc",                   # 0C
        "chr/ch39200.itc",                   # 0D
        "chr/ch08200.itc",                   # 0E
        "chr/ch48700.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "chr/ch02707.itc",                   # 12
        "chr/ch41800.itc",                   # 13
        "chr/ch31200.itc",                   # 14
        "chr/ch22000.itc",                   # 15
        "chr/ch32300.itc",                   # 16
    ))

    DeclNpc(30000,   0,       -1799,   270,  261,  0x0, 0,   0,   0,   0,   2,   1,   0,   255,  0)
    DeclNpc(-6090,   150,     4449,    270,  325,  0x0, 0,   1,   0,   255, 255, 1,   1,   255,  0)
    DeclNpc(-6099,   0,       -9409,   90,   389,  0x0, 0,   2,   0,   0,   0,   1,   2,   255,  0)
    DeclNpc(-289,    0,       -10319,  225,  261,  0x0, 0,   3,   0,   0,   3,   1,   4,   255,  0)
    DeclNpc(850,     0,       17969,   90,   277,  0x0, 0,   6,   0,   0,   0,   1,   7,   255,  0)
    DeclNpc(2539,    0,       17870,   270,  277,  0x0, 0,   5,   0,   0,   0,   1,   9,   255,  0)
    DeclNpc(14130,   0,       340,     270,  261,  0x0, 0,   7,   0,   0,   0,   1,   10,  255,  0)
    DeclNpc(-6099,   0,       -9409,   90,   389,  0x0, 0,   4,   0,   0,   0,   1,   3,   255,  0)
    DeclNpc(-22809,  1299,    -18829,  180,  261,  0x0, 0,   13,  0,   0,   4,   1,   20,  255,  0)
    DeclNpc(-25440,  1299,    -17040,  180,  405,  0x0, 0,   10,  0,   255, 255, 1,   11,  255,  0)
    DeclNpc(-25440,  1299,    -18170,  0,    389,  0x0, 0,   14,  0,   0,   0,   1,   19,  255,  0)
    DeclNpc(-1210,   0,       -2390,   180,  389,  0x0, 0,   11,  0,   0,   0,   1,   12,  255,  0)
    DeclNpc(-1210,   0,       -2390,   180,  389,  0x0, 0,   12,  0,   0,   0,   1,   13,  255,  0)
    DeclNpc(1750,    0,       -1559,   180,  389,  0x0, 0,   20,  0,   0,   0,   1,   14,  255,  0)
    DeclNpc(-18719,  0,       3960,    180,  385,  0x0, 0,   12,  0,   0,   1,   1,   15,  255,  0)
    DeclNpc(-1210,   0,       -2390,   180,  385,  0x0, 0,   19,  0,   0,   0,   1,   16,  255,  0)
    DeclNpc(-8529,   0,       2119,    90,   389,  0x0, 0,   21,  0,   0,   0,   1,   17,  255,  0)
    DeclNpc(-8020,   0,       910,     90,   389,  0x0, 0,   22,  0,   0,   0,   1,   18,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-9070,   13520,   0,       0x10100E1,    "BattleInfo_144", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-4890,   -4070,   0,       0x10100B4,    "BattleInfo_144", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(6530,    -110,    0,       0x10100B4,    "BattleInfo_144", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 11,  0.0,                   -17.0,                 -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  3.4000000953674316,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 105, -20.649999618530273,   -24.65999984741211,    -8.199999809265137,    625.0,                 [0.07071065157651901,  0.14142140746116638,   -0.0,                  0.0,                   -0.07071070373058319,  0.14142130315303802,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   -0.28355100750923157,  6.407801151275635,     4.099999904632568,     1.0])
    DeclEvent(0x0000, 0, 107, 0.12999999523162842,   18.799999237060547,    0.0,                   100.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   -0.012999999336898327, -9.399999618530273,    -0.0,                  1.0])

    DeclActor(0,       0,       -1600,   1000,    0,       2500,    0,       0x007C, 1,  24, 0x0000)
    DeclActor(-6130,   -4200,   -21010,  1000,    -6130,   -3200,   -21010,  0x007C, 1,  25, 0x0000)

    PlaceName(-5.449999809265137, 0.0, -2.7200000286102295, 0x0000, 0x0000, "中央广场")
    PlaceName(-70.54000091552734, 0.0, 1.7300000190734863, 0x0000, 0x0000, "西街")
    PlaceName(21.290000915527344, 0.0, 85.38999938964844, 0x0000, 0x0000, "行政区")
    PlaceName(-130.92999267578125, 0.0, 75.48999786376953, 0x0000, 0x0000, "住宅街")
    PlaceName(-58.65999984741211, 0.0, 67.56999969482422, 0x0000, 0x0000, "欢乐街")
    PlaceName(74.98999786376953, 0.0, -25.489999771118164, 0x0000, 0x0000, "东街")
    PlaceName(110.13999938964844, 0.0, -79.94000244140625, 0x0000, 0x0000, "旧城区")
    PlaceName(102.70999908447266, 0.0, 39.849998474121094, 0x0000, 0x0000, "港湾区")
    PlaceName(76.97000122070312, 0.0, 132.91000366210938, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(5.690000057220459, 0.0, -71.02999877929688, 0x0000, 0x0000, "站前街道")
    PlaceName(-40.84000015258789, 0.0, 31.93000030517578, 0x0000, 0x0000, "后巷")
    PlaceName(2.7200000286102295, 0.0, -101.72000122070312, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(128.4499969482422, 0.0, -11.630000114440918, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-121.02999877929688, 0.0, 0.25, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-115.08999633789062, 0.0, 99.25, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(15.0, 0.0, 216.75, 0x0000, 0x0000, "兰花塔")
    PlaceName(-27.229999542236328, 0.0, -16.579999923706055, 0x0000, 0x0051, "")
    PlaceName(25.989999771118164, 0.0, 9.15999984741211, 0x0000, 0x0054, "")
    PlaceName(-2.9700000286102295, 0.0, -24.5, 0x0000, 0x0057, "")
    PlaceName(-27.969999313354492, 0.0, 12.130000114440918, 0x0000, 0x0053, "")
    PlaceName(-7.670000076293945, 0.0, 35.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-57.91999816894531, 0.0, 7.179999828338623, 0x0000, 0x0053, "")
    PlaceName(-67.56999969482422, 0.0, 27.969999313354492, 0x0000, 0x0053, "")
    PlaceName(-43.810001373291016, 0.0, 59.650001525878906, 0x0000, 0x0052, "")
    PlaceName(-39.11000061035156, 0.0, 46.779998779296875, 0x0000, 0x0053, "")
    PlaceName(-30.440000534057617, 0.0, 38.36000061035156, 0x0000, 0x0053, "")
    PlaceName(-2.2300000190734863, 0.0, 108.6500015258789, 0x0000, 0x0051, "")
    PlaceName(108.6500015258789, 0.0, -25.489999771118164, 0x0000, 0x0052, "")
    PlaceName(91.81999969482422, 0.0, -115.08999633789062, 0x0000, 0x0053, "")
    PlaceName(78.94999694824219, 0.0, -96.7699966430664, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_EBC",          # 00, 0
        "Function_1_F6C",          # 01, 1
        "Function_2_1045",         # 02, 2
        "Function_3_1092",         # 03, 3
        "Function_4_10BD",         # 04, 4
        "Function_5_10E8",         # 05, 5
        "Function_6_1113",         # 06, 6
        "Function_7_125D",         # 07, 7
        "Function_8_2158",         # 08, 8
        "Function_9_2938",         # 09, 9
        "Function_10_2B8A",        # 0A, 10
        "Function_11_2B9A",        # 0B, 11
        "Function_12_3AB5",        # 0C, 12
        "Function_13_3AF2",        # 0D, 13
        "Function_14_3B39",        # 0E, 14
        "Function_15_3B83",        # 0F, 15
        "Function_16_4262",        # 10, 16
        "Function_17_43D9",        # 11, 17
        "Function_18_443E",        # 12, 18
        "Function_19_445A",        # 13, 19
        "Function_20_45B8",        # 14, 20
        "Function_21_4601",        # 15, 21
        "Function_22_4614",        # 16, 22
        "Function_23_4844",        # 17, 23
        "Function_24_4F64",        # 18, 24
        "Function_25_5008",        # 19, 25
        "Function_26_56E3",        # 1A, 26
        "Function_27_5730",        # 1B, 27
        "Function_28_5799",        # 1C, 28
        "Function_29_597F",        # 1D, 29
        "Function_30_5992",        # 1E, 30
        "Function_31_7278",        # 1F, 31
        "Function_32_72A8",        # 20, 32
        "Function_33_72E7",        # 21, 33
        "Function_34_7510",        # 22, 34
        "Function_35_7660",        # 23, 35
        "Function_36_7C83",        # 24, 36
        "Function_37_7CD7",        # 25, 37
        "Function_38_7CF0",        # 26, 38
        "Function_39_7FE2",        # 27, 39
        "Function_40_8029",        # 28, 40
        "Function_41_803C",        # 29, 41
        "Function_42_84AD",        # 2A, 42
        "Function_43_8502",        # 2B, 43
        "Function_44_8557",        # 2C, 44
        "Function_45_85AC",        # 2D, 45
        "Function_46_8601",        # 2E, 46
        "Function_47_8631",        # 2F, 47
        "Function_48_8809",        # 30, 48
        "Function_49_8B9D",        # 31, 49
        "Function_50_941C",        # 32, 50
        "Function_51_9496",        # 33, 51
        "Function_52_991B",        # 34, 52
        "Function_53_9952",        # 35, 53
        "Function_54_9983",        # 36, 54
        "Function_55_99B4",        # 37, 55
        "Function_56_99E5",        # 38, 56
        "Function_57_9A16",        # 39, 57
        "Function_58_9A47",        # 3A, 58
        "Function_59_9A78",        # 3B, 59
        "Function_60_9C5F",        # 3C, 60
        "Function_61_9CA7",        # 3D, 61
        "Function_62_9CC6",        # 3E, 62
        "Function_63_9CE5",        # 3F, 63
        "Function_64_9D19",        # 40, 64
        "Function_65_9D5A",        # 41, 65
        "Function_66_9D9B",        # 42, 66
        "Function_67_9DE4",        # 43, 67
        "Function_68_A6E5",        # 44, 68
        "Function_69_A722",        # 45, 69
        "Function_70_A75F",        # 46, 70
        "Function_71_A79C",        # 47, 71
        "Function_72_A7D9",        # 48, 72
        "Function_73_A816",        # 49, 73
        "Function_74_A853",        # 4A, 74
        "Function_75_A890",        # 4B, 75
        "Function_76_A8AF",        # 4C, 76
        "Function_77_A8CC",        # 4D, 77
        "Function_78_A946",        # 4E, 78
        "Function_79_A999",        # 4F, 79
        "Function_80_A9EC",        # 50, 80
        "Function_81_AA3F",        # 51, 81
        "Function_82_AA92",        # 52, 82
        "Function_83_AAE5",        # 53, 83
        "Function_84_AAFF",        # 54, 84
        "Function_85_BF02",        # 55, 85
        "Function_86_BF3F",        # 56, 86
        "Function_87_C02F",        # 57, 87
        "Function_88_C078",        # 58, 88
        "Function_89_C148",        # 59, 89
        "Function_90_C24F",        # 5A, 90
        "Function_91_C269",        # 5B, 91
        "Function_92_C29B",        # 5C, 92
        "Function_93_C2E2",        # 5D, 93
        "Function_94_C329",        # 5E, 94
        "Function_95_C37E",        # 5F, 95
        "Function_96_C3D3",        # 60, 96
        "Function_97_C428",        # 61, 97
        "Function_98_C653",        # 62, 98
        "Function_99_C74F",        # 63, 99
        "Function_100_C7D3",       # 64, 100
        "Function_101_C8C5",       # 65, 101
        "Function_102_CCDC",       # 66, 102
        "Function_103_D16A",       # 67, 103
        "Function_104_D789",       # 68, 104
        "Function_105_DC25",       # 69, 105
        "Function_106_E310",       # 6A, 106
        "Function_107_E341",       # 6B, 107
        "Function_108_E94A",       # 6C, 108
        "Function_109_EA95",       # 6D, 109
        "Function_110_F486",       # 6E, 110
        "Function_111_F571",       # 6F, 111
        "Function_112_F650",       # 70, 112
        "Function_113_F752",       # 71, 113
    ))


    def Function_0_EBC(): pass

    label("Function_0_EBC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_EF4"),
        (1, "loc_F00"),
        (2, "loc_F0C"),
        (3, "loc_F18"),
        (4, "loc_F24"),
        (5, "loc_F30"),
        (6, "loc_F3C"),
        (SWITCH_DEFAULT, "loc_F48"),
    )


    label("loc_EF4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_F54")

    label("loc_F00")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_F54")

    label("loc_F0C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_F54")

    label("loc_F18")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_F54")

    label("loc_F24")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_F54")

    label("loc_F30")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_F54")

    label("loc_F3C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F54")

    label("loc_F48")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F54")

    label("loc_F54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F6B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F54")

    label("loc_F6B")

    Return()

    # Function_0_EBC end

    def Function_1_F6C(): pass

    label("Function_1_F6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1044")
    OP_95(0xFE, -15910, 0, 1150, 1000, 0x0)
    OP_95(0xFE, -290, 0, 16770, 1000, 0x0)
    OP_95(0xFE, -300, 800, 24250, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xD7, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -290, 0, 16770, 1000, 0x0)
    OP_95(0xFE, -15910, 0, 1150, 1000, 0x0)
    OP_95(0xFE, -18720, 0, 3960, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    Jump("Function_1_F6C")

    label("loc_1044")

    Return()

    # Function_1_F6C end

    def Function_2_1045(): pass

    label("Function_2_1045")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1091")
    OP_95(0xFE, 11850, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 11850, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_2_1045")

    label("loc_1091")

    Return()

    # Function_2_1045 end

    def Function_3_1092(): pass

    label("Function_3_1092")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10BC")
    OP_94(0xFE, 0x366, 0xFFFFE296, 0xFFFFF236, 0xFFFFD166, 0x3E8)
    Sleep(300)
    Jump("Function_3_1092")

    label("loc_10BC")

    Return()

    # Function_3_1092 end

    def Function_4_10BD(): pass

    label("Function_4_10BD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10E7")
    OP_94(0xFE, 0xFFFFA484, 0xFFFFB348, 0xFFFFA722, 0xFFFFB9BA, 0x3E8)
    Sleep(300)
    Jump("Function_4_10BD")

    label("loc_10E7")

    Return()

    # Function_4_10BD end

    def Function_5_10E8(): pass

    label("Function_5_10E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1112")
    OP_94(0xFE, 0xFFFFBE2E, 0x2184, 0xFFFFB38E, 0x1054, 0x3E8)
    Sleep(300)
    Jump("Function_5_10E8")

    label("loc_1112")

    Return()

    # Function_5_10E8 end

    def Function_6_1113(): pass

    label("Function_6_1113")

    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    SetMapObjFlags(0x19, 0x2000000)
    SetMapObjFlags(0x1A, 0x2000000)
    SetMapObjFlags(0x1B, 0x2000000)
    SetMapObjFlags(0x1C, 0x2000000)
    SetMapObjFlags(0x1D, 0x2000000)
    SetMapObjFlags(0x1E, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_115D")
    ClearMapObjFlags(0x13, 0x2000000)
    Jump("loc_125C")

    label("loc_115D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1171")
    ClearMapObjFlags(0x15, 0x2000000)
    Jump("loc_125C")

    label("loc_1171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1185")
    ClearMapObjFlags(0xC, 0x2000000)
    Jump("loc_125C")

    label("loc_1185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_11B1")
    ClearMapObjFlags(0xC, 0x2000000)
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0x1C, 0x2000000)
    ClearMapObjFlags(0x1D, 0x2000000)
    ClearMapObjFlags(0x1E, 0x2000000)
    Jump("loc_125C")

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1225")
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)
    ClearMapObjFlags(0x17, 0x2000000)
    ClearMapObjFlags(0x18, 0x2000000)
    ClearMapObjFlags(0x19, 0x2000000)
    ClearMapObjFlags(0x1A, 0x2000000)
    ClearMapObjFlags(0x1B, 0x2000000)
    ClearMapObjFlags(0x1C, 0x2000000)
    ClearMapObjFlags(0x1D, 0x2000000)
    ClearMapObjFlags(0x1E, 0x2000000)
    Jump("loc_125C")

    label("loc_1225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1239")
    ClearMapObjFlags(0x13, 0x2000000)
    Jump("loc_125C")

    label("loc_1239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_124D")
    ClearMapObjFlags(0x13, 0x2000000)
    Jump("loc_125C")

    label("loc_124D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_125C")
    ClearMapObjFlags(0x13, 0x2000000)

    label("loc_125C")

    Return()

    # Function_6_1113 end

    def Function_7_125D(): pass

    label("Function_7_125D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A22")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131F")
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    SetChrPos(0x1, -26950, -1160, -4340, 90)
    SetChrPos(0x2, -26950, -1160, -4340, 90)
    SetChrPos(0x3, -26950, -1160, -4340, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F2")
    SetChrPos(0x4, -26950, -1160, -4340, 90)
    SetChrPos(0x5, -26950, -1160, -4340, 90)
    Jump("loc_1311")

    label("loc_12F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1311")
    SetChrPos(0x4, -26950, -1160, -4340, 90)

    label("loc_1311")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A22")

    label("loc_131F")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D3")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A6")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_13C5")

    label("loc_13A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C5")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_13C5")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A22")

    label("loc_13D3")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1487")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_145A")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_1479")

    label("loc_145A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1479")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_1479")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A22")

    label("loc_1487")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_153B")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_150E")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_152D")

    label("loc_150E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152D")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_152D")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A22")

    label("loc_153B")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EF")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C2")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_15E1")

    label("loc_15C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E1")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_15E1")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A22")

    label("loc_15EF")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A3")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1676")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_1695")

    label("loc_1676")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1695")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_1695")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A22")

    label("loc_16A3")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1757")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_172A")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_1749")

    label("loc_172A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1749")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_1749")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A22")

    label("loc_1757")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180B")
    SetChrPos(0x0, 4040, 0, -21980, 0)
    SetChrPos(0x1, 4040, 0, -21980, 0)
    SetChrPos(0x2, 4040, 0, -21980, 0)
    SetChrPos(0x3, 4040, 0, -21980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17DE")
    SetChrPos(0x4, 4040, 0, -21980, 0)
    SetChrPos(0x5, 4040, 0, -21980, 0)
    Jump("loc_17FD")

    label("loc_17DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17FD")
    SetChrPos(0x4, 4040, 0, -21980, 0)

    label("loc_17FD")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A22")

    label("loc_180B")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BF")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1892")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_18B1")

    label("loc_1892")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B1")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_18B1")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A22")

    label("loc_18BF")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1973")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1946")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_1965")

    label("loc_1946")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1965")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_1965")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A22")

    label("loc_1973")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A22")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19FA")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_1A19")

    label("loc_19FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A19")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_1A19")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A22")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A8F")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -4510, 0, -8420, 225)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    BeginChrThread(0xB, 0, 0, 0)
    OP_93(0xC, 0x87, 0x0)
    OP_93(0xD, 0x87, 0x0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1EB6")

    label("loc_1A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1AC0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_1EB6")

    label("loc_1AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B06")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -6100, 0, -9410, 90)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -4450, 0, -9880, 270)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_1EB6")

    label("loc_1B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B8A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B3A")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_1B44")

    label("loc_1B3A")

    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_1B44")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -4510, 0, -8420, 180)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_1EB6")

    label("loc_1B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1BA2")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1EB6")

    label("loc_1BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C11")
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x8, 0xF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -6100, 0, -9410, 225)
    SetChrPos(0xB, -6780, 0, -8620, 225)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x8)
    SetChrChipByIndex(0xB, 0x9)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1EB6")

    label("loc_1C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C40")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, -5000, 0, -9410, 270)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1EB6")

    label("loc_1C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1C58")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1EB6")

    label("loc_1C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C87")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C82")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)

    label("loc_1C82")

    Jump("loc_1EB6")

    label("loc_1C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CDC")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -6100, 0, -9410, 0)
    SetChrFlags(0xF, 0x10)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, -9410, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1EB6")

    label("loc_1CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1D2B")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xF, -4240, 0, -7750, 225)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_1EB6")

    label("loc_1D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1DB2")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -6100, 0, -9410, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xB, -5000, 0, -9410, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA3")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -24750, 1300, -16680, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA3")
    SetChrFlags(0x12, 0x10)

    label("loc_1DA3")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1EB6")

    label("loc_1DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E31")
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DEE")
    SetChrChipByIndex(0x11, 0x12)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -26150, -8200, -23200, 180)
    BeginChrThread(0x11, 0, 0, 0)

    label("loc_1DEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E22")
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E22")
    SetChrFlags(0xE, 0x10)

    label("loc_1E22")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1EB6")

    label("loc_1E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1E6E")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x8)
    SetChrChipByIndex(0xB, 0x9)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x8, 0xF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1EB6")

    label("loc_1E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1EB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E8F")
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_1E8F")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -22230, 1300, -20180, 315)
    BeginChrThread(0x11, 0, 0, 0)
    BeginChrThread(0x10, 0, 0, 0)

    label("loc_1EB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1ED8")
    SetChrFlags(0x13, 0x80)

    label("loc_1ED8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EF2")
    Event(0, 30)

    label("loc_1EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F08")
    SetMapFlags(0x10000000)
    Event(0, 35)

    label("loc_1F08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F35")
    SetMapFlags(0x10000000)
    Event(0, 103)

    label("loc_1F35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F78")
    SetChrPos(0xC, 4760, 0, 17660, 90)
    SetChrPos(0xD, 6740, 0, 17590, 270)
    SetChrFlags(0x16, 0x80)

    label("loc_1F78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F93")
    Event(0, 15)

    label("loc_1F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FBE")
    SetMapFlags(0x10000000)
    Event(2, 0)

    label("loc_1FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1FD5")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1, 4)
    Event(0, 9)
    Jump("loc_2157")

    label("loc_1FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1FE9")
    ClearScenarioFlags(0x22, 1)
    Event(0, 16)
    Jump("loc_2157")

    label("loc_1FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1FFD")
    ClearScenarioFlags(0x22, 2)
    Event(0, 19)
    Jump("loc_2157")

    label("loc_1FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_2011")
    ClearScenarioFlags(0x22, 3)
    Event(0, 22)
    Jump("loc_2157")

    label("loc_2011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_2028")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x1, 4)
    Event(0, 23)
    Jump("loc_2157")

    label("loc_2028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_203C")
    ClearScenarioFlags(0x22, 5)
    Event(0, 25)
    Jump("loc_2157")

    label("loc_203C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_2050")
    ClearScenarioFlags(0x22, 6)
    Event(0, 28)
    Jump("loc_2157")

    label("loc_2050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_2067")
    ClearScenarioFlags(0x22, 7)
    SetScenarioFlags(0x1, 4)
    Event(0, 33)
    Jump("loc_2157")

    label("loc_2067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_207B")
    ClearScenarioFlags(0x23, 0)
    Event(0, 34)
    Jump("loc_2157")

    label("loc_207B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_208F")
    ClearScenarioFlags(0x23, 1)
    Event(0, 38)
    Jump("loc_2157")

    label("loc_208F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_20A3")
    ClearScenarioFlags(0x23, 2)
    Event(0, 41)
    Jump("loc_2157")

    label("loc_20A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_20B7")
    ClearScenarioFlags(0x23, 3)
    Event(0, 47)
    Jump("loc_2157")

    label("loc_20B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_20CB")
    ClearScenarioFlags(0x23, 4)
    Event(0, 48)
    Jump("loc_2157")

    label("loc_20CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 5)), scpexpr(EXPR_END)), "loc_20DF")
    ClearScenarioFlags(0x23, 5)
    Event(0, 49)
    Jump("loc_2157")

    label("loc_20DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_20F3")
    ClearScenarioFlags(0x23, 6)
    Event(0, 51)
    Jump("loc_2157")

    label("loc_20F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 7)), scpexpr(EXPR_END)), "loc_2107")
    ClearScenarioFlags(0x23, 7)
    Event(0, 59)
    Jump("loc_2157")

    label("loc_2107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 0)), scpexpr(EXPR_END)), "loc_211B")
    ClearScenarioFlags(0x24, 0)
    Event(0, 67)
    Jump("loc_2157")

    label("loc_211B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 1)), scpexpr(EXPR_END)), "loc_212F")
    ClearScenarioFlags(0x24, 1)
    Event(0, 97)
    Jump("loc_2157")

    label("loc_212F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 2)), scpexpr(EXPR_END)), "loc_2148")
    ClearScenarioFlags(0x24, 2)
    SetMapFlags(0x10000000)
    Event(0, 102)
    Jump("loc_2157")

    label("loc_2148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 3)), scpexpr(EXPR_END)), "loc_2157")
    ClearScenarioFlags(0x24, 3)
    Event(0, 101)

    label("loc_2157")

    Return()

    # Function_7_125D end

    def Function_8_2158(): pass

    label("Function_8_2158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_216D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 4)

    label("loc_216D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2231")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x5A, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_2231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22E0")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x5A, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)

    label("loc_22E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2342")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x26, 0x82, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)

    label("loc_2342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_235A")
    ClearMapFlags(0x2000)
    Jump("loc_2361")

    label("loc_235A")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_2361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23B5")
    ClearMapObjFlags(0xF, 0x4)
    OP_78(0xF, 0x1A)
    SetMapObjFlags(0xF, 0x1000)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -7790, 0, 16480, 90)
    OP_D5(0x1A, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0xF, 0x1E)
    OP_70(0xF, 0x0)
    Jump("loc_241A")

    label("loc_23B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23CD")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_241A")

    label("loc_23CD")

    ClearMapObjFlags(0x13, 0x4)
    OP_78(0x13, 0x1A)
    SetMapObjFlags(0x13, 0x1000)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -8010, 0, 16230, 225)
    OP_D5(0x1A, 0x0, 0x36EE8, 0x0, 0x0)
    OP_74(0x13, 0x1E)
    OP_70(0x13, 0x0)
    SetMapObjFlags(0x13, 0x2)
    SetMapObjFlags(0x13, 0x400)

    label("loc_241A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2434")
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)

    label("loc_2434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24E0")
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    LoadEffect(0xA, "map/mpbell02.eff")
    PlayEffect(0xA, 0x6, 0xFF, 0x0, 0, 3000, 4000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    OP_74(0x14, 0x1E)
    OP_71(0x14, 0x0, 0x1D, 0x0, 0x20)
    SetMapObjFrame(0x14, "bell_add", 0x1, 0x1)
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x1000)
    OP_74(0x16, 0x1E)
    OP_71(0x16, 0x0, 0x258, 0x0, 0x20)

    label("loc_24E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_250F")
    SetMapObjFrame(0xFF, "ibc_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x1, 0x1)
    Jump("loc_2530")

    label("loc_250F")

    SetMapObjFrame(0xFF, "ibc_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x0, 0x1)

    label("loc_2530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_253E")
    Jump("loc_259F")

    label("loc_253E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2552")
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_259F")

    label("loc_2552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2560")
    Jump("loc_259F")

    label("loc_2560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2574")
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_259F")

    label("loc_2574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2582")
    Jump("loc_259F")

    label("loc_2582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2596")
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_259F")

    label("loc_2596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_259F")

    label("loc_259F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B8")
    ClearMapObjFlags(0xA, 0x4)
    Jump("loc_25BE")

    label("loc_25B8")

    SetMapObjFlags(0xA, 0x4)

    label("loc_25BE")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25D6")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_25D6")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2600")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_2600")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_262A")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_262A")

    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28D7")
    OP_10(0x2, 0x0)
    OP_10(0xD, 0x1)
    Jump("loc_28DD")

    label("loc_28D7")

    OP_10(0x2, 0x1)
    OP_10(0xD, 0x0)

    label("loc_28DD")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2923")
    OP_1B(0x0, 0x0, 0x6E)
    OP_1B(0x2, 0x0, 0x6F)
    OP_1B(0x3, 0x0, 0x70)
    OP_1B(0x4, 0x0, 0x71)
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x0)

    label("loc_2923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2937")
    Sound(828, 1, 60, 0)

    label("loc_2937")

    Return()

    # Function_8_2158 end

    def Function_9_2938(): pass

    label("Function_9_2938")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)
    BeginChrThread(0xB, 0, 0, 0)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x13, 0x2D)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_71(0x13, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "阿尔泰尔据点的逮捕行动\x01",
            "过去两天之后──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    SetChrPos(0xB, -4900, 0, -9350, 270)
    SetChrPos(0x2D, 20000, 0, -5000, 270)
    OP_D5(0x2D, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x11, -22250, 1300, -20200, 315)
    BeginChrThread(0x11, 0, 0, 0)
    OP_68(0, 1900, 3650, 0)
    MoveCamera(55, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    MoveCamera(15, 25, 0, 8000)
    OP_6E(700, 8000)
    SetCameraDistance(35000, 8000)
    PlayBGM("ed7150", 0)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(958, 0, 100, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(4450, 1000, -6100, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19000, 0)
    OP_68(-23000, 2200, -19700, 10000)
    MoveCamera(55, 15, 0, 10000)
    SetCameraDistance(15000, 10000)
    BeginChrThread(0x38, 1, 0, 10)

    def lambda_2B59():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2B59)
    OP_0D()
    OP_6F(0x79)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_2938 end

    def Function_10_2B8A(): pass

    label("Function_10_2B8A")

    Sound(458, 0, 100, 0)
    Sleep(4000)
    Sound(494, 0, 50, 0)
    Return()

    # Function_10_2B8A end

    def Function_11_2B9A(): pass

    label("Function_11_2B9A")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis402.itp")
    LoadChrToIndex("chr/ch20600.itc", 0x1E)
    LoadChrToIndex("chr/ch22200.itc", 0x1F)
    SoundLoad(835)
    SetChrPos(0x101, -600, 0, -12000, 0)
    SetChrPos(0x102, -400, 0, -13400, 0)
    SetChrPos(0x109, 600, 0, -12000, 0)
    SetChrPos(0x105, 800, 0, -13400, 0)
    SetChrPos(0x1A5, -1700, 0, -12700, 0)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -12400, 0, -3300, 90)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -13500, 0, -3300, 90)
    SetChrPos(0xB, -5300, 0, -10200, 320)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -6100, 0, -9410, 140)
    OP_68(0, 1100, -11700, 0)
    MoveCamera(47, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)

    def lambda_2CEB():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CEB)
    Sleep(100)

    def lambda_2D08():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D08)
    Sleep(100)

    def lambda_2D25():
        OP_97(0x1A5, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A5, 0, lambda_2D25)
    Sleep(100)

    def lambda_2D42():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D42)
    Sleep(100)

    def lambda_2D5F():
        OP_97(0x105, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2D5F)
    Sound(835, 2, 60, 0)
    OP_68(0, 1100, -7700, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)

    #N0002
    NpcTalk(
        0x1B,
        "男孩的声音",
        "喂！琪雅！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    OP_63(0x1A5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-10700, 1100, -4300, 0)
    MoveCamera(37, 29, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(-2200, 1100, -6700, 3000)
    MoveCamera(357, 19, 0, 3000)
    SetCameraDistance(17000, 3000)
    BeginChrThread(0x1B, 3, 0, 12)
    BeginChrThread(0x1C, 3, 0, 13)

    def lambda_2E8A():

        label("loc_2E8A")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2E8A")

    QueueWorkItem2(0x101, 2, lambda_2E8A)

    def lambda_2E9C():

        label("loc_2E9C")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2E9C")

    QueueWorkItem2(0x102, 2, lambda_2E9C)

    def lambda_2EAE():

        label("loc_2EAE")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2EAE")

    QueueWorkItem2(0x1A5, 2, lambda_2EAE)

    def lambda_2EC0():

        label("loc_2EC0")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2EC0")

    QueueWorkItem2(0x109, 2, lambda_2EC0)

    def lambda_2ED2():

        label("loc_2ED2")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2ED2")

    QueueWorkItem2(0x105, 2, lambda_2ED2)
    WaitChrThread(0x1B, 3)
    WaitChrThread(0x1C, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x1A5, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    #C0003
    ChrTalk(
        0x1A5,
        "#12P#01110F啊，是隆和亨利！\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x1B,
        (
            "#5P你好慢啊，我们不是说好\x01",
            "要在面包店前见面吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x1C,
        "#5P教会的课马上就要开始了哦！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x1A5,
        "#12P#01109F嘿嘿嘿，抱歉抱歉。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00002F隆，亨利，\x01",
            "你们还是这么有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#12P#00109F呵呵，谢谢你们\x01",
            "一直关照琪雅哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0009
    ChrTalk(
        0x1C,
        "#5P啊，好久不见！\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x1B,
        "#5P嘿嘿，好久没见啦。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x1B,
        (
            "#5P我已经听琪雅说了，\x01",
            "支援科又要开始工作了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00004F是啊，托大家的福。\x02\x03",

            "#00000F我们已经磨练得比以前更强了，\x01",
            "请尽管期待吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x1B,
        "#5P嘿嘿，口气不小嘛。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x1B,
        (
            "#5P不过，如今的哥哥姐姐们\x01",
            "的确差不多追上游击士了，\x01",
            "我倒也可以认同你们～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    #C0015
    ChrTalk(
        0x1C,
        "#11P真是的，隆，你的口气太狂妄啦～\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x109,
        "#10109F嘻嘻……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x105,
        (
            "#12P#10304F真不愧是支援科，\x01",
            "连小孩子都这么喜欢你们啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1C, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    def lambda_31EB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_31EB)
    Sleep(1000)

    #C0018
    ChrTalk(
        0x1B,
        "#5P哎，那边的哥哥姐姐是……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x1C,
        "#5P以前从没见过呢。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x1C,
        (
            "#5P仔细一看，缇欧姐姐\x01",
            "和兰迪哥哥都不在呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#12P#00104F他们两个有事外出，\x01",
            "还没回来。\x02\x03",

            "#00100F这两位是诺艾尔小姐和瓦吉先生，\x01",
            "支援科的新成员。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x109,
        "#10102F呵呵，请多指教哦！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x1B,
        "#5P嗯嗯，请多指教！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x1B,
        (
            "#5P……哎？\x01",
            "那个人是男的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x1B,
        (
            "#5P但看脸却\x01",
            "像个女人呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    #C0026
    ChrTalk(
        0x1C,
        "#11P别、别乱说啊，隆！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x105,
        (
            "#12P#10309F呵呵，这个嘛～\x02\x03",

            "#10302F说不定你的第一感觉\x01",
            "就是正确答案呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x1B,
        "#5P？？？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#00006F……真是的，瓦吉，\x01",
            "不要戏弄小孩子啊。\x02\x03",

            "#00000F对了，你们三个\x01",
            "还不快点出发吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1C, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_346F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1A5, 2, lambda_346F)
    Sleep(50)

    def lambda_347F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_347F)
    Sleep(150)

    #C0030
    ChrTalk(
        0x1A5,
        (
            "#6P#01105F啊，都给忘了。\x02\x03",

            "#01109F那就再见啦！\x01",
            "大家要加油工作哦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A5, 500)

    def lambda_34DC():

        label("loc_34DC")

        TurnDirection(0xFE, 0x1A5, 500)
        Yield()
        Jump("loc_34DC")

    QueueWorkItem2(0x101, 2, lambda_34DC)

    #C0031
    ChrTalk(
        0x101,
        "#00009F嗯，琪雅也要加油啊。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        "#12P#00102F路上要小心车哦！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x1A5,
        "#6P#01110F嗯！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x1B,
        (
            "#5P好，那我们\x01",
            "这就去小桃家吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x1C,
        "#5P嗯，赶快出发！\x02",
    )

    CloseMessageWindow()
    OP_68(-5200, 1100, -6700, 4000)
    BeginChrThread(0x1B, 3, 0, 14)
    Sleep(400)
    BeginChrThread(0x1C, 3, 0, 14)
    Sleep(50)
    SetChrFlags(0x1A5, 0x1000)
    BeginChrThread(0x1A5, 3, 0, 14)
    WaitChrThread(0x1B, 3)
    WaitChrThread(0x1C, 3)
    WaitChrThread(0x1A5, 3)
    EndChrThread(0x101, 0x2)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1200, -8000, 0)
    MoveCamera(50, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    #C0036
    ChrTalk(
        0x109,
        (
            "#11P#10109F呵呵……\x01",
            "这些孩子真活泼啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0037
    ChrTalk(
        0x105,
        "#11P#10300F是住在西街的孩子吧？\x02",
    )

    CloseMessageWindow()

    def lambda_3655():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3655)
    Sleep(50)
    TurnDirection(0x102, 0x101, 500)

    #C0038
    ChrTalk(
        0x101,
        (
            "#6P#00002F嗯，一个住在西街，\x01",
            "另一个住在住宅街。\x02\x03",

            "#00004F好，\x01",
            "我们这就开始工作吧。\x02\x03",

            "#00000F首先要去导力商店\x01",
            "和警察总部露个面……\x02\x03",

            "如果可以，\x01",
            "最好在整个城市巡视一圈。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x109,
        (
            "#11P#10100F原来如此，\x01",
            "这就是所谓的巡逻吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#12P#00104F呵呵，倒也不是\x01",
            "那么正式的任务……\x02\x03",

            "#00100F在巡视途中有可能会得到意外的情报，\x01",
            "因此日常巡视也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#6P#00000F再过一段时间，科长应该\x01",
            "会通过艾尼格玛联络我们。\x02\x03",

            "在那之前，我们就在市内巡视，\x01",
            "去想去的地方看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        "#11P#10102F明白了。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        "#11P#10304F呵呵，那就出发吧。\x02",
    )

    CloseMessageWindow()
    StopSound(835, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    Sleep(500)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis302.itp")
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可以使用克洛斯贝尔市内地图了。\x02",
        )
    )

    CloseMessageWindow()

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在市内区域中按下START键，\x01",
            "即可打开市内地图。\x01",
            "（再次按下START键，\x01",
            "  就会切换到自治州地图。）\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，在市内打开地图后，\x01",
            "可以直接移动到\x01",
            "各区域内。\x02",
        )
    )

    CloseMessageWindow()

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请在左边的街区列表中\x01",
            "选择要去的场所。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不过，在某些特殊状况下，\x01",
            "是无法使用市内地图的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0xA, -6100, 0, -9410, 90)
    SetChrPos(0xB, -290, 0, -10320, 225)
    BeginChrThread(0xB, 0, 0, 3)
    OP_D7(0x1E)
    OP_D7(0x1F)
    RemoveParty(0xA4, 0xFF)
    SetChrPos(0x0, -1500, 0, -16820, 90)
    OP_C9(0x1, 0x1000)
    SetScenarioFlags(0x126, 4)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_11_2B9A end

    def Function_12_3AB5(): pass

    label("Function_12_3AB5")


    def lambda_3ABA():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3ABA)
    WaitChrThread(0xFE, 1)

    def lambda_3AD8():
        OP_95(0xFE, -3400, 0, -5700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AD8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_3AB5 end

    def Function_13_3AF2(): pass

    label("Function_13_3AF2")

    Sleep(50)

    def lambda_3AFA():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AFA)
    WaitChrThread(0xFE, 1)

    def lambda_3B18():
        OP_95(0xFE, -2800, 0, -4800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B18)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_13_3AF2 end

    def Function_14_3B39(): pass

    label("Function_14_3B39")

    OP_92(0xFE, 0xFFFFE318, 0xFFFFF31C, 0x1F4)

    def lambda_3B4B():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B4B)
    WaitChrThread(0xFE, 1)

    def lambda_3B69():
        OP_95(0xFE, -17400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B69)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_3B39 end

    def Function_15_3B83(): pass

    label("Function_15_3B83")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SoundLoad(803)
    OP_68(14000, 1200, 6000, 0)
    MoveCamera(57, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 15000, 0, 6000, 270)
    SetChrPos(0x102, 12800, 0, 6000, 90)
    SetChrPos(0x109, 13700, 0, 4700, 0)
    SetChrPos(0x105, 13700, 0, 7300, 180)
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetCameraDistance(18500, 1000)
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

    def lambda_3CB6():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3CB6)
    Sleep(50)

    def lambda_3CC6():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3CC6)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)

    #C0049
    ChrTalk(
        0x101,
        "#11P#00005F哦，大概是科长吧。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#6P#00102F从时间来看，差不多\x01",
            "也该和我们联络了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    #Sound(2084, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0051
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

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，辛苦了。\x02\x03",

            "早上也和你们说过，\x01",
            "来警察学校一趟吧。\x02\x03",

            "知道具体位置吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0053
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

    #A0054
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

    #A0055
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

    #A0056
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

    #A0057
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

    #A0058
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
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0059
    ChrTalk(
        0x102,
        "#6P#00100F果然是科长啊。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x109,
        (
            "#12P#10105F你们好像谈了些\x01",
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

    #C0061
    ChrTalk(
        0x101,
        (
            "#11P#00006F嗯，科长似乎也\x01",
            "觉察到了局势的变化。\x02\x03",

            "#00001F我们最好将黑月和雷克特大尉\x01",
            "的情况也报告给科长一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        "#6P#00106F是啊……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        (
            "#5P#10300F那么，那我们差不多\x01",
            "也该去警察学校了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#11P#00000F嗯，从西出口出去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0065
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
    SetChrPos(0x0, 15000, 0, 6000, 270)
    OP_69(0xFF, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 30000, 0, -1800, 270)
    BeginChrThread(0x8, 0, 0, 2)
    SetScenarioFlags(0x126, 5)
    OP_29(0xA1, 0x1, 0x4)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_15_3B83 end

    def Function_16_4262(): pass

    label("Function_16_4262")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SoundLoad(468)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x8, 0x2D)
    OP_49()
    SetChrPos(0x2D, -35510, -2590, -4520, 90)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4367")
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    EndChrThread(0xA, 0xFF)
    SetChrPos(0xA, -6880, 0, 810, 0)

    def lambda_4333():

        label("loc_4333")

        TurnDirection(0xFE, 0x2D, 500)
        Yield()
        Jump("loc_4333")

    QueueWorkItem2(0xA, 2, lambda_4333)
    SetChrPos(0xB, -6300, 0, -170, 0)
    EndChrThread(0xB, 0xFF)

    def lambda_435A():

        label("loc_435A")

        TurnDirection(0xFE, 0x2D, 500)
        Yield()
        Jump("loc_435A")

    QueueWorkItem2(0xB, 2, lambda_435A)

    label("loc_4367")

    FadeToBright(1000, 0)
    BeginChrThread(0x2D, 3, 0, 17)
    BeginChrThread(0x38, 1, 0, 18)
    OP_68(-17900, 2700, -500, 0)
    MoveCamera(355, 30, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(28000, 0)
    OP_68(-15700, 3700, -300, 7500)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_4262 end

    def Function_17_43D9(): pass

    label("Function_17_43D9")

    SetChrPos(0xFE, -35510, -2590, -4520, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -23860, -640, -4420)
    OP_9F(0x1, -14350, 750, -1880)
    OP_9F(0x1, -11380, 0, 7200)
    OP_9F(0x1, -14250, 0, 13970)
    OP_9F(0x1, -28100, 0, 29400)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_17_43D9 end

    def Function_18_443E(): pass

    label("Function_18_443E")

    Sound(458, 0, 100, 0)
    Sound(468, 2, 100, 0)
    Sleep(5000)
    Sound(494, 0, 60, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_443E end

    def Function_19_445A(): pass

    label("Function_19_445A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0xA, 0x8)
    SetChrChipByIndex(0xB, 0x9)
    SetChrChipByIndex(0x8, 0xF)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x15, 0x2D)
    OP_49()
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    OP_71(0x15, 0x79, 0xB4, 0x0, 0x20)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xC8, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x2D, 11000, 0, 30000, 180)
    OP_D5(0x2D, 0x0, 0x2BF20, 0x0, 0x0)
    BeginChrThread(0x2D, 1, 0, 20)
    BeginChrThread(0x38, 1, 0, 21)
    OP_68(-3500, 4300, -8650, 0)
    MoveCamera(55, -5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15000, 0)
    OP_68(-3500, 2500, -8650, 10000)
    MoveCamera(40, 5, 0, 10000)
    SetCameraDistance(18000, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_445A end

    def Function_20_45B8(): pass

    label("Function_20_45B8")

    Sleep(1500)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 11000, 0, 30000)
    OP_9F(0x1, 8580, 0, 4180)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 4700, 0, -30500)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_20_45B8 end

    def Function_21_4601(): pass

    label("Function_21_4601")

    Sleep(2300)
    Sound(458, 0, 70, 0)
    Sleep(4300)
    Sound(494, 0, 70, 0)
    Return()

    # Function_21_4601 end

    def Function_22_4614(): pass

    label("Function_22_4614")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    SetChrChipByIndex(0xA, 0x2)
    SetChrChipByIndex(0xB, 0x3)
    SetChrChipByIndex(0x8, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    SetChrChipByIndex(0x39, 0xC)
    BeginChrThread(0x39, 0, 0, 0)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    SetChrChipByIndex(0x3A, 0xC)
    BeginChrThread(0x3A, 0, 0, 0)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0xC, 0x2D)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    ClearChrFlags(0x1A, 0x80)
    OP_78(0xF, 0x1A)
    OP_49()
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetChrPos(0x1A, -7800, 0, 16500, 90)
    OP_D5(0x1A, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x13, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x39, 7000, 0, -7700, 270)
    SetChrPos(0x3A, 5750, 0, -7700, 90)
    SetChrPos(0x2D, 8850, 0, -8650, 225)
    OP_D5(0x2D, 0x0, 0x36EE8, 0x0, 0x0)
    OP_68(-15350, 1900, -2500, 0)
    MoveCamera(345, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    OP_68(3000, 1400, -6000, 10000)
    MoveCamera(40, 15, 0, 10000)
    SetCameraDistance(22000, 10000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_4614 end

    def Function_23_4844(): pass

    label("Function_23_4844")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20000.itc", 0x1E)
    LoadChrToIndex("chr/ch24000.itc", 0x1F)
    LoadChrToIndex("chr/ch22300.itc", 0x20)
    LoadChrToIndex("chr/ch21000.itc", 0x21)
    LoadChrToIndex("chr/ch27900.itc", 0x22)
    LoadChrToIndex("chr/ch22800.itc", 0x23)
    LoadChrToIndex("chr/ch20500.itc", 0x24)
    SoundLoad(835)
    SoundLoad(821)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xB, 0x8000)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0x8, 0x8000)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x21, 0x1F)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    BeginChrThread(0x21, 0, 0, 0)
    SetChrChipByIndex(0x22, 0x20)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    BeginChrThread(0x22, 0, 0, 0)
    SetChrChipByIndex(0x23, 0x21)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrChipByIndex(0x24, 0x22)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    BeginChrThread(0x24, 0, 0, 0)
    SetChrChipByIndex(0x25, 0x23)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    BeginChrThread(0x25, 0, 0, 0)
    SetChrChipByIndex(0x26, 0x24)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    BeginChrThread(0x26, 0, 0, 0)
    SetChrChipByIndex(0x39, 0xC)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    BeginChrThread(0x39, 0, 0, 0)
    SetChrChipByIndex(0x3A, 0xC)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    BeginChrThread(0x3A, 0, 0, 0)
    SetChrChipByIndex(0x3B, 0xC)
    ClearChrFlags(0x3B, 0x80)
    SetChrFlags(0x3B, 0x8000)
    BeginChrThread(0x3B, 0, 0, 0)
    SetChrChipByIndex(0x3C, 0xC)
    ClearChrFlags(0x3C, 0x80)
    SetChrFlags(0x3C, 0x8000)
    BeginChrThread(0x3C, 0, 0, 0)
    SetChrChipByIndex(0x3D, 0xC)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    BeginChrThread(0x3D, 0, 0, 0)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0xC, 0x2D)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0xD, 0x2E)
    OP_49()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    ClearChrFlags(0x3E, 0x80)
    OP_78(0x7, 0x3E)
    OP_49()
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1C, 0x1000)
    ClearMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1D, 0x1000)
    ClearMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1E, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W\x01",
            "      七耀历１２０４年──初秋。\x02\x03",

            "由克洛斯贝尔新市长兼ＩＢＣ总裁\x01",
            "迪塔·库罗伊斯提议举办的\x01",
            "『西塞姆里亚通商会议』开始了。\x02\x03",

            "西方大国埃雷波尼亚帝国派出的代表\x01",
            "除了『铁血宰相』吉利亚斯·奥斯本之外，\x01",
            "还有知名的风流雅士奥利维特皇子。\x02\x03",

            "东方大国卡尔瓦德共和国的代表\x01",
            "则是备受支持的庶民派领袖\x01",
            "萨缪尔·洛克史密斯总统。\x02\x03",

            "位于东北部的雷米菲利亚公国\x01",
            "由年轻的领导者阿尔伯特大公出任代表。\x02\x03",

            "位于西南部的利贝尔王国\x01",
            "则由女王代理人科洛蒂娅王太女出席会议。\x02\x03",

            "各方代表均为国宾级重要人士，\x01",
            "如今，众位要人已经汇集至克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    SetChrPos(0x9, 1050, 0, -3100, 90)
    SetChrPos(0x8, 500, 0, -7750, 135)
    SetChrPos(0xA, -1900, 0, -5000, 315)
    SetChrPos(0xF, -3700, 0, -5100, 45)
    SetChrPos(0xB, -2700, 0, -4550, 0)
    SetChrPos(0xE, -2950, 0, -3350, 180)
    SetChrPos(0xC, -1900, 0, -10200, 180)
    SetChrPos(0xD, -1900, 0, -11500, 0)
    SetChrPos(0x39, 15900, 0, 6000, 270)
    SetChrPos(0x3A, 2450, 0, -5250, 90)
    SetChrPos(0x3B, 1150, 0, -9850, 90)
    SetChrPos(0x3C, -5750, 0, -4450, 270)
    SetChrPos(0x3D, 9500, 0, -9350, 315)
    SetChrPos(0x21, -3850, 0, -11600, 135)
    SetChrPos(0x22, 400, 0, -5900, 135)
    SetChrPos(0x23, 0, 0, -5100, 135)
    SetChrPos(0x24, -1650, 0, -7950, 90)
    SetChrPos(0x25, -2050, 0, -13250, 90)
    SetChrPos(0x26, -2700, 0, -7000, 180)
    SetChrPos(0x2D, -6000, 0, -9150, 135)
    OP_D5(0x2D, 0x0, 0x20F58, 0x0, 0x0)
    SetChrPos(0x2E, -7800, 0, 16500, 90)
    OP_D5(0x2E, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x3E, -1700, 0, -2050, 200)
    OP_D5(0x3E, 0x0, 0x1ADB0, 0x0, 0x0)
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    BeginChrThread(0xA, 1, 0, 24)
    BeginChrThread(0xF, 1, 0, 24)
    BeginChrThread(0xC, 1, 0, 24)
    BeginChrThread(0xD, 1, 0, 24)
    BeginChrThread(0x21, 1, 0, 24)
    BeginChrThread(0x22, 1, 0, 24)
    BeginChrThread(0x23, 1, 0, 24)
    BeginChrThread(0x24, 1, 0, 24)
    BeginChrThread(0x25, 1, 0, 24)
    BeginChrThread(0x26, 1, 0, 24)
    OP_68(-12000, 6200, 12900, 0)
    MoveCamera(15, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20750, 0)
    OP_68(-12000, 7200, 12900, 5000)
    MoveCamera(15, -2, 0, 5000)
    SetCameraDistance(22750, 5000)
    PlayBGM("ed7583", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-500, 1000, -6500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(18000, 5000)
    Sleep(4000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0180", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_4844 end

    def Function_24_4F64(): pass

    label("Function_24_4F64")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4F9C"),
        (1, "loc_4FA4"),
        (2, "loc_4FAC"),
        (3, "loc_4FB4"),
        (4, "loc_4FBC"),
        (5, "loc_4FC4"),
        (6, "loc_4FCC"),
        (SWITCH_DEFAULT, "loc_4FD4"),
    )


    label("loc_4F9C")

    Sleep(100)
    Jump("loc_4FDC")

    label("loc_4FA4")

    Sleep(200)
    Jump("loc_4FDC")

    label("loc_4FAC")

    Sleep(300)
    Jump("loc_4FDC")

    label("loc_4FB4")

    Sleep(400)
    Jump("loc_4FDC")

    label("loc_4FBC")

    Sleep(500)
    Jump("loc_4FDC")

    label("loc_4FC4")

    Sleep(600)
    Jump("loc_4FDC")

    label("loc_4FCC")

    Sleep(700)
    Jump("loc_4FDC")

    label("loc_4FD4")

    Sleep(800)
    Jump("loc_4FDC")

    label("loc_4FDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5007")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_4FDC")

    label("loc_5007")

    Return()

    # Function_24_4F64 end

    def Function_25_5008(): pass

    label("Function_25_5008")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20000.itc", 0x1E)
    LoadChrToIndex("chr/ch24000.itc", 0x1F)
    LoadChrToIndex("chr/ch22300.itc", 0x20)
    LoadChrToIndex("chr/ch21000.itc", 0x21)
    LoadChrToIndex("chr/ch27900.itc", 0x22)
    LoadChrToIndex("chr/ch22800.itc", 0x23)
    LoadChrToIndex("chr/ch20500.itc", 0x24)
    SoundLoad(835)
    SoundLoad(821)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xB, 0x8000)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0x8, 0x8000)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x21, 0x1F)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    BeginChrThread(0x21, 0, 0, 0)
    SetChrChipByIndex(0x22, 0x20)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    BeginChrThread(0x22, 0, 0, 0)
    SetChrChipByIndex(0x23, 0x21)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrChipByIndex(0x24, 0x22)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    BeginChrThread(0x24, 0, 0, 0)
    SetChrChipByIndex(0x25, 0x23)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    BeginChrThread(0x25, 0, 0, 0)
    SetChrChipByIndex(0x26, 0x24)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    BeginChrThread(0x26, 0, 0, 0)
    SetChrChipByIndex(0x39, 0xC)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    BeginChrThread(0x39, 0, 0, 0)
    SetChrChipByIndex(0x3A, 0xC)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    BeginChrThread(0x3A, 0, 0, 0)
    SetChrChipByIndex(0x3B, 0xC)
    ClearChrFlags(0x3B, 0x80)
    SetChrFlags(0x3B, 0x8000)
    BeginChrThread(0x3B, 0, 0, 0)
    SetChrChipByIndex(0x3C, 0xC)
    ClearChrFlags(0x3C, 0x80)
    SetChrFlags(0x3C, 0x8000)
    BeginChrThread(0x3C, 0, 0, 0)
    SetChrChipByIndex(0x3D, 0xC)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    BeginChrThread(0x3D, 0, 0, 0)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0xC, 0x2D)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x17, 0x2E)
    OP_49()
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFrame(0x17, "light", 0x0, 0x1)
    ClearChrFlags(0x2F, 0x80)
    OP_78(0xD, 0x2F)
    OP_49()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    ClearChrFlags(0x30, 0x80)
    OP_78(0x18, 0x30)
    OP_49()
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    SetMapObjFrame(0x18, "light", 0x0, 0x1)
    ClearChrFlags(0x31, 0x80)
    OP_78(0x19, 0x31)
    OP_49()
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x1000)
    SetMapObjFrame(0x19, "light", 0x0, 0x1)
    ClearChrFlags(0x32, 0x80)
    OP_78(0x1A, 0x32)
    OP_49()
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1A, 0x1000)
    SetMapObjFrame(0x1A, "light", 0x0, 0x1)
    ClearChrFlags(0x33, 0x80)
    OP_78(0x1B, 0x33)
    OP_49()
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1B, 0x1000)
    SetMapObjFrame(0x1B, "light", 0x0, 0x1)
    ClearChrFlags(0x34, 0x80)
    OP_78(0xE, 0x34)
    OP_49()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    ClearChrFlags(0x3E, 0x80)
    OP_78(0x7, 0x3E)
    OP_49()
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1C, 0x1000)
    ClearMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1D, 0x1000)
    ClearMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1E, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x8, 850, 0, -7200, 135)
    SetChrPos(0x9, 1850, 0, -2700, 90)
    SetChrPos(0xA, -250, 0, -4300, 135)
    SetChrPos(0xF, -500, 0, -5400, 90)
    SetChrPos(0xB, 600, 0, -5700, 90)
    SetChrPos(0xC, -550, 0, -8800, 90)
    SetChrPos(0xD, -700, 0, -9700, 90)
    SetChrPos(0xE, -1600, 0, -3350, 90)
    SetChrPos(0x39, 15900, 0, 6000, 270)
    SetChrPos(0x3A, 2450, 0, -5250, 90)
    SetChrPos(0x3B, 1150, 0, -9850, 90)
    SetChrPos(0x3C, -5750, 0, -4450, 270)
    SetChrPos(0x3D, 9500, 0, -9350, 315)
    SetChrPos(0x21, -2400, 0, -9300, 135)
    SetChrPos(0x22, 150, 0, -2900, 135)
    SetChrPos(0x23, 200, 0, -1900, 135)
    SetChrPos(0x24, -1650, 0, -7950, 90)
    SetChrPos(0x25, -1050, 0, -11000, 90)
    SetChrPos(0x26, -2700, 0, -7000, 135)
    SetChrPos(0x2D, 35000, 0, -4000, 270)
    OP_D5(0x34, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2E, 45000, 0, -4000, 270)
    OP_D5(0x34, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2F, 3700, 0, -20000, 0)
    OP_D5(0x2F, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x30, 3700, 0, -30000, 0)
    OP_D5(0x30, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x31, 3700, 0, -40000, 0)
    OP_D5(0x31, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x32, 3700, 0, -30000, 0)
    OP_D5(0x30, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x33, 3700, 0, -40000, 0)
    OP_D5(0x31, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x34, -6000, 0, -9150, 135)
    OP_D5(0x34, 0x0, 0x20F58, 0x0, 0x0)
    SetChrPos(0x3E, -1700, 0, -2050, 200)
    OP_D5(0x3E, 0x0, 0x1ADB0, 0x0, 0x0)
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    BeginChrThread(0xA, 1, 0, 24)
    BeginChrThread(0xF, 1, 0, 24)
    BeginChrThread(0xC, 1, 0, 24)
    BeginChrThread(0xD, 1, 0, 24)
    BeginChrThread(0x21, 1, 0, 24)
    BeginChrThread(0x22, 1, 0, 24)
    BeginChrThread(0x23, 1, 0, 24)
    BeginChrThread(0x24, 1, 0, 24)
    BeginChrThread(0x25, 1, 0, 24)
    BeginChrThread(0x26, 1, 0, 24)
    BeginChrThread(0x2D, 1, 0, 26)
    BeginChrThread(0x2E, 1, 0, 26)
    OP_68(11000, 600, 800, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29000, 0)
    MoveCamera(47, 10, 0, 25000)
    SetCameraDistance(28000, 25000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(458, 0, 100, 0)
    Sleep(3500)
    Sound(457, 0, 80, 0)
    Sleep(5000)
    Sound(458, 0, 100, 0)
    BeginChrThread(0x2F, 1, 0, 27)
    BeginChrThread(0x30, 1, 0, 27)
    BeginChrThread(0x31, 1, 0, 27)
    Sleep(3500)
    Sound(457, 0, 80, 0)
    Sleep(5000)
    ClearChrFlags(0x2D, 0x80)
    ClearMapObjFlags(0xC, 0x4)
    SetChrPos(0x2D, 3700, 0, -20000, 0)
    OP_D5(0x2D, 0x0, 0x0, 0x0, 0x0)
    Sound(458, 0, 100, 0)
    BeginChrThread(0x2D, 1, 0, 27)
    BeginChrThread(0x32, 1, 0, 27)
    BeginChrThread(0x33, 1, 0, 27)
    Sleep(3000)
    Sound(494, 0, 60, 0)
    Sleep(2000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_5008 end

    def Function_26_56E3(): pass

    label("Function_26_56E3")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 35000, 0, -4000)
    OP_9F(0x1, 11500, 0, 1000)
    OP_9F(0x1, 12000, 0, 30000)
    OP_9F(0x2, 0xFE, 7000, 0x6)

    def lambda_571F():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_571F)
    Return()

    # Function_26_56E3 end

    def Function_27_5730(): pass

    label("Function_27_5730")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3700, 0, -20000)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 10580, 0, 4180)
    OP_9F(0x1, 12000, 0, 10000)
    OP_9F(0x1, 12000, 0, 15000)
    OP_9F(0x2, 0xFE, 7000, 0x6)

    def lambda_5788():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5788)
    Return()

    # Function_27_5730 end

    def Function_28_5799(): pass

    label("Function_28_5799")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x13, 0x2D)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_71(0x13, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0xF, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0xF, -6100, 0, -9410, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, -9410, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0x12, -24750, 1300, -16680, 180)
    SetChrPos(0x2D, 20000, 0, -5000, 270)
    OP_D5(0x2D, 0x0, 0x41EB0, 0x0, 0x0)
    OP_68(-13500, 1900, 4250, 0)
    MoveCamera(25, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    OP_68(750, 1900, -5250, 10000)
    MoveCamera(50, 10, 0, 10000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x38, 1, 0, 29)

    def lambda_5910():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_5910)
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_5799 end

    def Function_29_597F(): pass

    label("Function_29_597F")

    Sleep(500)
    Sound(458, 0, 80, 0)
    Sleep(3600)
    Sound(494, 0, 50, 0)
    Return()

    # Function_29_597F end

    def Function_30_5992(): pass

    label("Function_30_5992")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13800.itc", 0x1E)
    LoadChrToIndex("chr/ch13801.itc", 0x1F)
    LoadChrToIndex("chr/ch13802.itc", 0x20)
    LoadChrToIndex("chr/ch08200.itc", 0x21)
    LoadChrToIndex("chr/ch08201.itc", 0x22)
    LoadChrToIndex("apl/ch50005.itc", 0x23)
    SoundLoad(847)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis244.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu08000.itp")
    OP_68(-28700, -7200, -23400, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x109, -28700, -8200, -21000, 180)
    SetChrPos(0x101, -28700, -8200, -21000, 180)
    SetChrPos(0x102, -28700, -8200, -21000, 180)
    SetChrPos(0x104, -28700, -8200, -21000, 180)
    SetChrPos(0x105, -28700, -8200, -21000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1E, 0x20)
    SetChrPos(0x1E, -28700, -3700, -41000, 0)
    OP_52(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -28700, -8200, -20000, 180)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-28700, -7200, -25400, 5000)
    FadeToBright(2000, 0)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0x105, 3, 0, 42)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 44)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 45)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 46)
    WaitChrThread(0x109, 3)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    Sound(846, 0, 100, 0)
    Sleep(300)
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5C40():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5C40)
    Sleep(50)

    def lambda_5C50():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5C50)
    Sleep(50)

    def lambda_5C60():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5C60)
    Sleep(50)

    def lambda_5C70():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5C70)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    #C0067
    ChrTalk(
        0x101,
        "#5P#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        "#00105F#5P鸟叫声？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7519", 0)
    Fade(250)
    OP_68(-28700, -3900, -33700, 0)
    MoveCamera(43, 23, -11, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_68(-28700, -3900, -29700, 3000)
    MoveCamera(49, 23, -17, 3000)
    SetCameraDistance(14500, 3000)
    OP_52(0x1E, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -27600, -8200, -25400, 180)
    SetChrPos(0x102, -26200, -8200, -25400, 180)
    SetChrPos(0x104, -27700, -8200, -24100, 180)
    SetChrPos(0x109, -26300, -8200, -24100, 180)
    SetChrPos(0x105, -25100, -8200, -25700, 180)
    ClearChrFlags(0x1E, 0x80)

    def lambda_5D9E():

        label("loc_5D9E")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_5D9E")

    QueueWorkItem2(0x1E, 2, lambda_5D9E)

    def lambda_5DB0():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFE9BC, 0xFFFF9A70, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5DB0)
    Sound(847, 2, 70, 0)
    WaitChrThread(0x1E, 1)
    BeginChrThread(0x1E, 3, 0, 31)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5DF2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DF2)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5E1A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5E1A)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5E42():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5E42)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5E6A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5E6A)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5E92():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5E92)
    Sleep(2000)
    Fade(500)
    OP_68(-26800, -5900, -25400, 0)
    MoveCamera(37, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_52(0x1E, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    #C0069
    ChrTalk(
        0x101,
        "#00011F#6P#N什、什么！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0070
    ChrTalk(
        0x109,
        "#10111F#6P#N白、白鹰……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0071
    ChrTalk(
        0x105,
        (
            "#10305F#12P……不，\x01",
            "好像是隼。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        (
            "#00301F#6P喂喂，为何会\x01",
            "出现在城市里……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x1E, 0x3)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x1E, 0x0)
    OP_68(-27800, -6900, -26700, 3000)
    MoveCamera(37, 19, 0, 3000)

    def lambda_5FB0():
        OP_9E(0xFE, 0xFFFF97B4, 0xFFFF9A70, 0x493E0, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5FB0)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1644), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1676), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x16A8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x16DA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x170C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x173E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x17A2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x17D4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1806), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1838), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x189C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x18CE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1932), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1996), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x19C8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x19FA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A2C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A5E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A90), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1AC2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1AF4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B26), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_6151():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6151)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B8A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BBC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BEE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_619A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_619A)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C20), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C52), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C84), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1CB6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_61E3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_61E3)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1CE8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D1A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D7E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1DB0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1DE2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E14), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E46), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E78), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1EAA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1EDC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1F0E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x1E, 1)
    StopSound(847, 700, 60)
    Fade(250)
    EndChrThread(0x1E, 0x2)
    SetChrPos(0x1E, -28000, -7000, -27700, 0)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x1)

    def lambda_62E1():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFE2B4, 0xFFFF93CC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_62E1)
    Sleep(100)
    SetChrSubChip(0x1E, 0x1)
    Sleep(100)
    SetChrSubChip(0x1E, 0x0)
    Sleep(100)
    SetChrSubChip(0x1E, 0x1)
    Sleep(100)
    SetChrSubChip(0x1E, 0x2)
    Sleep(300)
    WaitChrThread(0x1E, 1)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0073
    AnonymousTalk(
        0x1E,
        (
            "啾。\x02\x03",

            "啾、啾、啾。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0074
    ChrTalk(
        0x101,
        (
            "#5P#00001F莫、莫非……\x01",
            "找我们有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#00108F#11P和蔡特找我们说话时\x01",
            "的感觉一样呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#00306F#5P唔，如果阿缇在这里，\x01",
            "就能听懂它在说什么了……\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    ClearChrFlags(0x1D, 0x80)

    def lambda_64E5():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA628, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_64E5)

    def lambda_64FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_64FF)
    WaitChrThread(0x1D, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    #C0077
    ChrTalk(
        0x1D,
        "#01105F#5P哎，怎么了？\x02",
    )

    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    CloseMessageWindow()
    OP_63(0x1D, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1D, 0x22)
    SetChrSubChip(0x1D, 0x0)

    def lambda_656E():
        OP_96(0xFE, 0xFFFF90AC, 0xFFFFDFF8, 0xFFFF9750, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_656E)
    Sleep(300)

    def lambda_658B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_658B)
    Sleep(100)

    def lambda_659B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_659B)
    Sleep(100)

    def lambda_65AB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_65AB)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    OP_93(0x1D, 0x87, 0x1F4)
    #Sound(3029, 255, 100, 0)    #voice#KeA

    #C0078
    ChrTalk(
        0x1D,
        (
            "#6P#01110F哇，白鸟！\x02\x03",

            "#01109F嘴巴尖尖的，\x01",
            "好漂亮啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x13B, 0x1F4)
    Sleep(300)

    #C0079
    ChrTalk(
        0x1E,
        (
            "#11P#08009F啾⊥\x02\x03",

            "#08000F啾、啾、啾¤\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x1D,
        (
            "#6P#01103F嗯，嗯。\x02\x03",

            "#01102F原来如此，是这样啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x101,
        (
            "#5P#00012F（琪雅……\x01",
            "  果然能听懂啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x109,
        "#10112F#5P（好、好厉害啊……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x101, 500)

    def lambda_6747():

        label("loc_6747")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6747")

    QueueWorkItem2(0x1D, 2, lambda_6747)

    #C0083
    ChrTalk(
        0x1D,
        (
            "#6P#01100F那个……这个孩子\x01",
            "的名字是『基库』。\x02\x03",

            "它说有传话要转达给你们，\x01",
            "请你们收下。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#5P#00011F是、是吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x1E, 500)

    #C0085
    ChrTalk(
        0x104,
        (
            "#00305F#5P啊，它的脚上确实\x01",
            "绑着一张纸条呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6807():
        OP_95(0xFE, -27600, -8200, -26600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6807)
    TurnDirection(0x1E, 0x101, 500)
    Sleep(300)

    def lambda_682B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_682B)
    WaitChrThread(0x101, 1)
    EndChrThread(0x1D, 0x2)
    SetChrName("")

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德从白隼的脚上\x01",
            "取下了纸条。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "克洛斯贝尔警察局·特别任务支援科敬启\x02\x03",

            "听闻诸位事迹，\x01",
            "特此冒昧联络。\x02\x03",

            "若时间方便，\x01",
            "望秘密前来会谈。\x02\x03",

            "今日傍晚，于克洛斯贝尔空港的\x01",
            "候船露台静候各位。\x02\x03",

            "另，如各位不便赴邀，\x01",
            "无需另行答复。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)

    #A0088
    AnonymousTalk(
        0x101,
        "#00005F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0089
    AnonymousTalk(
        0x102,
        "#00101F#11P这、这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0090
    AnonymousTalk(
        0x109,
        (
            "#10106F#5P内容奇怪，又没有写明寄信人，\x01",
            "未免也太可疑了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0091
    AnonymousTalk(
        0x105,
        (
            "#10302F#11P不过，字迹相当漂亮，\x01",
            "措辞也十分有礼呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0092
    AnonymousTalk(
        0x104,
        (
            "#00301F#5P更重要的是，字条上印着的\x01",
            "白隼徽章不就是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0093
    AnonymousTalk(
        0x1E,
        (
            "#08000F#12P啾。\x02\x03",

            "啾、啾、啾。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    SetChrSubChip(0x1E, 0x1)
    Sleep(100)
    SetChrSubChip(0x1E, 0x0)
    Sleep(100)
    Sound(847, 2, 70, 0)

    def lambda_6B17():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFE4A8, 0xFFFF93CC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6B17)
    SetChrSubChip(0x1E, 0x1)
    Sleep(100)
    SetChrSubChip(0x1E, 0x0)
    Sleep(100)
    SetChrSubChip(0x1E, 0x1)
    Sleep(100)
    SetChrSubChip(0x1E, 0x0)
    Sleep(100)
    SetChrSubChip(0x1E, 0x1)
    WaitChrThread(0x1E, 1)
    OP_68(-27800, -5900, -30700, 5000)
    MoveCamera(43, 19, 0, 5000)
    SetCameraDistance(16000, 5000)
    Fade(250)
    SetChrPos(0x1E, -28000, -7500, -27700, 0)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x1)

    def lambda_6B9D():

        label("loc_6B9D")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_6B9D")

    QueueWorkItem2(0x1E, 2, lambda_6B9D)
    BeginChrThread(0x1E, 3, 0, 32)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D1A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1CE8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1CB6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C84), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C52), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C20), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BEE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BBC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B8A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B26), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1AF4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1AC2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A90), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A5E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A2C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x19FA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x19C8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1996), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1932), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x18CE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x189C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1838), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1806), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x17D4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x17A2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x173E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x170C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x16DA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x16A8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1676), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1644), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x1E, 3)

    def lambda_6DD2():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFEF98, 0xFFFF64EC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6DD2)
    Sleep(300)

    def lambda_6DEF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_6DEF)
    Sleep(100)

    def lambda_6DFF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6DFF)
    Sleep(100)

    def lambda_6E0F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6E0F)
    Sleep(100)

    def lambda_6E1F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6E1F)
    StopSound(847, 2000, 60)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x1E, 0xFF)
    SetChrFlags(0x1E, 0x80)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)
    OP_6F(0x79)
    Fade(500)
    OP_68(-27800, -6900, -26700, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    TurnDirection(0x101, 0x1D, 500)

    #C0094
    ChrTalk(
        0x101,
        (
            "#11P#00011F那个……\x01",
            "琪雅，它在说什么？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x101, 500)

    #C0095
    ChrTalk(
        0x1D,
        (
            "#6P#01111F嗯……去或不去，\x01",
            "由你们自行决定。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        "#11P#00003F是吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_6F89():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6F89)
    Sleep(50)

    def lambda_6F99():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6F99)
    Sleep(50)

    def lambda_6FA9():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6FA9)
    Sleep(50)

    def lambda_6FB9():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6FB9)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0097
    ChrTalk(
        0x102,
        (
            "#00108F#11P怎、怎么办呢？\x02\x03",

            "#00101F我想应该不可能\x01",
            "是那里的人士……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        "#00306F#5P嗯，确实。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x109,
        (
            "#10108F#5P可是，白隼徽章……\x01",
            "再加上刚才那只白隼……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x105,
        (
            "#10309F#11P啊哈哈，越来越\x01",
            "期待了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(450)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(150)

    #C0101
    ChrTalk(
        0x101,
        (
            "#6P#00003F既然对方特意发来邀请，\x01",
            "我们就接受好了。\x02\x03",

            "#00000F距离傍晚还有一些时间，\x01",
            "把要做的事情做完之后再去也无妨。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        "#00106F#11P知、知道了。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x109,
        "#10106F#5P真、真紧张……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x104,
        (
            "#00309F#5P不过，应该不用\x01",
            "换上正装去吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x105,
        (
            "#10302F#11P呵呵，先把要办的事情办完，\x01",
            "然后就去南出口的克洛斯贝尔空港吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x2D, 0x1F4)
    Sleep(150)

    #C0106
    ChrTalk(
        0x1D,
        (
            "#6P#01110F虽然不知道是怎么回事，\x01",
            "不过大家要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    SetChrFlags(0x1D, 0x80)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, -27700, -8200, -25000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 7)
    OP_29(0xA3, 0x1, 0x11)
    OP_C9(0x1, 0x1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    OP_24(0x34F)
    EventEnd(0x5)
    Return()

    # Function_30_5992 end

    def Function_31_7278(): pass

    label("Function_31_7278")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72A7")

    def lambda_7288():
        OP_9E(0xFE, 0xFFFF99A8, 0xFFFF9A70, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7288)
    WaitChrThread(0x1E, 1)
    Jump("Function_31_7278")

    label("loc_72A7")

    Return()

    # Function_31_7278 end

    def Function_32_72A8(): pass

    label("Function_32_72A8")


    def lambda_72AD():
        OP_9E(0xFE, 0xFFFF9494, 0xFFFF93CC, 0x2BF20, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_72AD)
    WaitChrThread(0x1E, 1)

    def lambda_72CC():
        OP_9E(0xFE, 0xFFFF90AC, 0xFFFF93CC, 0x57E40, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_72CC)
    WaitChrThread(0x1E, 1)
    Return()

    # Function_32_72A8 end

    def Function_33_72E7(): pass

    label("Function_33_72E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x13, 0x2D)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_71(0x13, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K翌日８：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    SetChrPos(0xF, -6100, 0, 9400, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, 9400, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0x2D, -20000, 0, -5000, 90)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(-3650, 1900, 15980, 0)
    MoveCamera(45, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    OP_68(-3650, 1900, 16000, 10000)
    MoveCamera(25, 5, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(40000, 10000)
    PlayBGM("ed7125", 0)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6000)
    Sound(494, 0, 80, 0)

    def lambda_7496():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_7496)
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    MoveCamera(35, 15, 0, 4000)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 6)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_72E7 end

    def Function_34_7510(): pass

    label("Function_34_7510")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, -9400, 270)
    OP_68(-5400, 1900, 7000, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22500, 0)
    OP_68(-1000, 1900, 0, 10000)
    MoveCamera(30, 5, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(27000, 10000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 0)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_7510 end

    def Function_35_7660(): pass

    label("Function_35_7660")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(946)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -16750, 0, 18400, 135)
    SetChrPos(0x102, -17500, 0, 17650, 135)
    SetChrPos(0x103, -18500, 0, 17650, 135)
    SetChrPos(0x104, -16750, 0, 19400, 135)
    SetChrPos(0x109, -17750, 0, 19400, 135)
    SetChrPos(0x105, -18500, 0, 18650, 135)
    ClearChrFlags(0x2F, 0x80)
    OP_78(0x10, 0x2F)
    OP_49()
    OP_D5(0x2F, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFrame(0x10, "light", 0x0, 0x1)
    OP_74(0x10, 0x1E)
    OP_71(0x10, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x30, 0x80)
    OP_78(0x11, 0x30)
    OP_49()
    OP_D5(0x30, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x31, 0x80)
    OP_78(0x12, 0x31)
    OP_49()
    OP_D5(0x31, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0xB5, 0xF0, 0x1, 0x20)
    SetChrPos(0x2F, -27000, -170, -3600, 90)
    SetChrPos(0x30, -35000, -1500, -3600, 90)
    SetChrPos(0x31, -43000, -2830, -3600, 90)
    ClearMapFlags(0x10000000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7846")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)

    def lambda_7815():

        label("loc_7815")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7815")

    QueueWorkItem2(0xA, 2, lambda_7815)

    def lambda_7827():

        label("loc_7827")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7827")

    QueueWorkItem2(0xB, 2, lambda_7827)

    def lambda_7839():

        label("loc_7839")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7839")

    QueueWorkItem2(0x13, 2, lambda_7839)

    label("loc_7846")

    OP_68(-13300, 1500, 14200, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17000, 3000)

    def lambda_788B():
        OP_9B(0x0, 0x101, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_788B)
    Sleep(50)

    def lambda_78A3():
        OP_9B(0x0, 0x102, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_78A3)
    Sleep(50)

    def lambda_78BB():
        OP_9B(0x0, 0x103, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_78BB)
    Sleep(50)

    def lambda_78D3():
        OP_9B(0x0, 0x104, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_78D3)
    Sleep(50)

    def lambda_78EB():
        OP_9B(0x0, 0x105, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_78EB)
    Sleep(50)

    def lambda_7903():
        OP_9B(0x0, 0x109, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7903)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    OP_0D()
    Sound(946, 2, 40, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0108
    ChrTalk(
        0x101,
        "#00005F#5P这声音是……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        "#00201F#5P是警笛声呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_25(0x3B2, 0x3C)
    Fade(1000)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_93(0x109, 0xB4, 0x0)
    OP_93(0x105, 0xB4, 0x0)
    OP_68(-10000, 500, -900, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    OP_68(8150, 500, -19200, 10000)
    MoveCamera(30, 20, 0, 10000)
    BeginChrThread(0x38, 1, 0, 37)
    BeginChrThread(0x2F, 3, 0, 36)
    BeginChrThread(0x30, 3, 0, 36)
    BeginChrThread(0x31, 3, 0, 36)
    WaitChrThread(0x2F, 3)
    WaitChrThread(0x30, 3)
    WaitChrThread(0x31, 3)
    StopSound(946, 3000, 50)
    OP_0D()
    Fade(500)
    OP_93(0x101, 0x87, 0x0)
    OP_93(0x102, 0x87, 0x0)
    OP_93(0x103, 0x87, 0x0)
    OP_93(0x104, 0x87, 0x0)
    OP_93(0x109, 0x87, 0x0)
    OP_93(0x105, 0x87, 0x0)
    OP_68(-13300, 1500, 14200, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    #C0110
    ChrTalk(
        0x109,
        "#10101F#5P出动了三辆急救车……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#00108F#5P应该是在运送\x01",
            "脱轨事故中受伤的乘客吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x105,
        (
            "#10303F#5P嗯，既然在这种时候出车，\x01",
            "应该不会有错。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#00006F#5P……看来塞茜尔姐姐她们\x01",
            "也要开始忙了。\x02\x03",

            "#00001F我们赶快去现场吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        "#00301F#5P嗯。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C55")
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0x13, 0x2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0x13, 0x8000)

    label("loc_7C55")

    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 6)
    OP_24(0x3B2)
    EventEnd(0x5)
    Return()

    # Function_35_7660 end

    def Function_36_7C83(): pass

    label("Function_36_7C83")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13000, 500, -2870)
    OP_9F(0x1, -350, 0, -7080)
    OP_9F(0x1, 4300, 0, -18000)
    OP_9F(0x1, 4500, 0, -30000)
    OP_9F(0x1, 4500, 0, -40000)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_36_7C83 end

    def Function_37_7CD7(): pass

    label("Function_37_7CD7")

    Sound(465, 0, 80, 0)
    Sleep(4000)
    Sound(458, 0, 100, 0)
    Sleep(3000)
    Sound(465, 0, 80, 0)
    Return()

    # Function_37_7CD7 end

    def Function_38_7CF0(): pass

    label("Function_38_7CF0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(946)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x8, 0x2D)
    OP_49()
    SetChrPos(0x2D, -21060, 0, 22140, 135)
    OP_D5(0x2D, 0x0, 0x20F58, 0x0, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x79, 0xB4, 0x1, 0x20)
    ClearChrFlags(0x2F, 0x80)
    OP_78(0x10, 0x2F)
    OP_49()
    OP_D5(0x2F, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFrame(0x10, "light", 0x0, 0x1)
    OP_74(0x10, 0x1E)
    OP_71(0x10, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x30, 0x80)
    OP_78(0x11, 0x30)
    OP_49()
    OP_D5(0x30, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x31, 0x80)
    OP_78(0x12, 0x31)
    OP_49()
    OP_D5(0x31, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0xB5, 0xF0, 0x1, 0x20)
    SetChrPos(0x2F, -27000, -170, -3600, 90)
    SetChrPos(0x30, -35000, -1500, -3600, 90)
    SetChrPos(0x31, -43000, -2830, -3600, 90)
    ClearMapFlags(0x10000000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7ED5")
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0x13, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)

    def lambda_7EA4():

        label("loc_7EA4")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7EA4")

    QueueWorkItem2(0xA, 2, lambda_7EA4)

    def lambda_7EB6():

        label("loc_7EB6")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7EB6")

    QueueWorkItem2(0xB, 2, lambda_7EB6)

    def lambda_7EC8():

        label("loc_7EC8")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7EC8")

    QueueWorkItem2(0x13, 2, lambda_7EC8)

    label("loc_7ED5")

    Sound(946, 2, 60, 0)
    OP_68(-13300, 1500, 14200, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_68(-13580, 1500, 1970, 5000)
    MoveCamera(6, 27, 0, 5000)
    SetCameraDistance(24500, 5000)
    BeginChrThread(0x2D, 3, 0, 39)
    BeginChrThread(0x38, 1, 0, 40)
    WaitChrThread(0x2D, 3)
    OP_6F(0x79)
    OP_0D()
    Sleep(700)
    Fade(1000)
    OP_68(-10000, 500, -900, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    OP_68(8150, 500, -19200, 10000)
    MoveCamera(30, 20, 0, 10000)
    BeginChrThread(0x38, 1, 0, 37)
    BeginChrThread(0x2F, 3, 0, 36)
    BeginChrThread(0x30, 3, 0, 36)
    BeginChrThread(0x31, 3, 0, 36)
    WaitChrThread(0x2F, 3)
    WaitChrThread(0x30, 3)
    StopSound(946, 2000, 50)
    WaitChrThread(0x31, 3)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x3B2)
    SetScenarioFlags(0x22, 6)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_7CF0 end

    def Function_39_7FE2(): pass

    label("Function_39_7FE2")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13630, 0, 14510)
    OP_9F(0x1, -11670, 0, 9100)
    OP_9F(0x1, -12500, 0, 4800)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x8)
    OP_79(0x8)
    Return()

    # Function_39_7FE2 end

    def Function_40_8029(): pass

    label("Function_40_8029")

    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(3000)
    Sound(492, 0, 50, 0)
    Return()

    # Function_40_8029 end

    def Function_41_803C(): pass

    label("Function_41_803C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-28700, -7200, -23400, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x109, -28700, -8200, -21000, 180)
    SetChrPos(0x101, -28700, -8200, -21000, 180)
    SetChrPos(0x102, -28700, -8200, -21000, 180)
    SetChrPos(0x103, -28700, -8200, -21000, 180)
    SetChrPos(0x105, -28700, -8200, -21000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-28700, -7200, -25400, 5000)
    FadeToBright(2000, 0)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0x101, 3, 0, 42)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 44)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 45)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 46)
    WaitChrThread(0x109, 3)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    #C0115
    ChrTalk(
        0x105,
        (
            "#6P#10302F要去的地方，就是欢乐街的巴鲁卡\x01",
            "以及旧城区的两家店吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        (
            "#00003F#11P嗯，虽然其它地方\x01",
            "或许也会有什么线索……\x02\x03",

            "#00001F但我们现在已经\x01",
            "没时间去市外调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#6P#00200F幸好今天早上没有接到\x01",
            "新的支援请求啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#12P#00103F受到昨天那起事件的影响，\x01",
            "总部如今大概也已经混乱不堪了。\x02\x03",

            "#00101F警备队遭受的损伤\x01",
            "好像也相当惨重……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x109,
        "#10108F#5P……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_832E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_832E)

    def lambda_833B():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_833B)
    Sleep(50)

    def lambda_834B():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_834B)
    Sleep(50)

    def lambda_835B():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_835B)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    #C0120
    ChrTalk(
        0x102,
        (
            "#12P#00106F……抱歉。\x02\x03",

            "#00108F没有考虑到\x01",
            "你的心情呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x109,
        (
            "#10112F#5P……不，承受那种危险\x01",
            "也是我们警备队员的份内职责。\x02\x03",

            "#10100F而且，我如今只是\x01",
            "特别任务支援科的一员。\x02\x03",

            "出发吧……\x01",
            "去把兰迪前辈抓回来！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#00002F#11P……嗯！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -28700, -8200, -25000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_29(0xA9, 0x1, 0x7)
    OP_29(0xA9, 0x4, 0x10)
    OP_29(0xAA, 0x4, 0x2)
    OP_29(0xAA, 0x1, 0x0)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    EventEnd(0x5)
    Return()

    # Function_41_803C end

    def Function_42_84AD(): pass

    label("Function_42_84AD")


    def lambda_84B2():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_84B2)

    def lambda_84CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_84CC)
    WaitChrThread(0xFE, 1)

    def lambda_84E1():
        OP_95(0xFE, -27400, -8200, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_84E1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_42_84AD end

    def Function_43_8502(): pass

    label("Function_43_8502")


    def lambda_8507():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8507)

    def lambda_8521():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8521)
    WaitChrThread(0xFE, 1)

    def lambda_8536():
        OP_95(0xFE, -28000, -8200, -26200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8536)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_43_8502 end

    def Function_44_8557(): pass

    label("Function_44_8557")


    def lambda_855C():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_855C)

    def lambda_8576():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8576)
    WaitChrThread(0xFE, 1)

    def lambda_858B():
        OP_95(0xFE, -29400, -8200, -26200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_858B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_44_8557 end

    def Function_45_85AC(): pass

    label("Function_45_85AC")


    def lambda_85B1():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85B1)

    def lambda_85CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_85CB)
    WaitChrThread(0xFE, 1)

    def lambda_85E0():
        OP_95(0xFE, -30000, -8200, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85E0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_45_85AC end

    def Function_46_8601(): pass

    label("Function_46_8601")


    def lambda_8606():
        OP_95(0xFE, -28700, -8200, -23700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8606)

    def lambda_8620():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8620)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_8601 end

    def Function_47_8631(): pass

    label("Function_47_8631")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -4510, 0, -8420, 180)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x13, 0x2D)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_71(0x13, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFrame(0xFF, "ibc_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x1, 0x1)
    SetMapObjFlags(0x7, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x2D, -20000, 0, -5000, 90)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(-5400, 1900, 7000, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22500, 0)
    OP_68(-700, 2500, 3000, 10000)
    MoveCamera(30, 5, 0, 10000)
    SetCameraDistance(27000, 10000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    Sound(457, 0, 80, 0)

    def lambda_87D2():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_87D2)
    Sleep(4000)
    StopSound(835, 1000, 100)
    StopSound(457, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_8631 end

    def Function_48_8809(): pass

    label("Function_48_8809")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41500.itc", 0x1E)
    LoadChrToIndex("chr/ch20000.itc", 0x1F)
    SoundLoad(821)
    SoundLoad(835)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x9, 0x2E)
    OP_49()
    SetChrPos(0x2E, -1000, 0, 18000, 180)
    OP_D5(0x2E, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x3)
    OP_4B(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0x13)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -2500, 0, 16000, 180)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 2400, 0, 16000, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x21, 0x0)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 350, 0, 13000, 0)
    SetChrChipByIndex(0x22, 0x4)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -2800, 0, 11500, 0)
    SetChrChipByIndex(0x23, 0x2)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -1500, 0, 11100, 0)
    SetChrChipByIndex(0x24, 0x3)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 0, 0, 11100, 0)
    SetChrChipByIndex(0x25, 0x6)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 1300, 0, 12000, 0)
    SetChrChipByIndex(0x26, 0x5)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 2300, 0, 11600, 0)
    SetChrChipByIndex(0x27, 0x1F)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -2800, 0, 13100, 0)
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(0, 1700, 13700, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    MoveCamera(30, 25, 0, 15000)
    SetCameraDistance(17000, 15000)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMessageWindowPos(0, 100, -1, -1)
    SetChrName("迪塔总统")

    #A0123
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就在数日前，那邪恶的意志\x01",
            "已将我们克洛斯贝尔击入\x01",
            "恐怖与哀伤的深渊。\x02\x03",

            "我想诸位聪明的市民\x01",
            "早已隐隐察觉到了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_70(0x9, 0x2)
    Sleep(600)
    SetMessageWindowPos(0, 100, -1, -1)
    SetChrName("迪塔总统")

    #A0124
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "但我还是要在这里正式指出\x01",
            "那股势力的名字，并向其发表谴责。\x02\x03",

            "『埃雷波尼亚帝国政府』……\x01",
            "就是那邪恶的意志之一。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x23, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(851, 1500, 60)
    StopSound(835, 1500, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_48_8809 end

    def Function_49_8B9D(): pass

    label("Function_49_8B9D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08201.itc", 0x1F)
    LoadChrToIndex("apl/ch50380.itc", 0x20)
    LoadChrToIndex("apl/ch51080.itc", 0x21)
    SoundLoad(3623)
    SoundLoad(3624)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01104.itp")
    OP_68(-27200, -7200, -23000, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, -27800, -8200, -24700, 90)
    SetChrPos(0x102, -26000, -8200, -24100, 90)
    SetChrPos(0x103, -26600, -8200, -25300, 90)
    SetChrPos(0x104, -27200, -8200, -23500, 90)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -28700, -8200, -20000, 180)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8C97():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8C97)
    Sleep(50)

    def lambda_8CB4():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8CB4)
    Sleep(50)

    def lambda_8CD1():
        OP_97(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8CD1)
    Sleep(50)

    def lambda_8CEE():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8CEE)
    OP_68(-27200, -7200, -24000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    BeginChrThread(0x1D, 3, 0, 50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x101, 0)

    def lambda_8D81():
        TurnDirection(0x101, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8D81)
    Sleep(50)

    def lambda_8D91():
        TurnDirection(0x103, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8D91)
    Sleep(50)

    def lambda_8DA1():
        TurnDirection(0x104, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8DA1)
    Sleep(50)

    def lambda_8DB1():
        TurnDirection(0x102, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8DB1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x1D, 3)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)

    #C0125
    ChrTalk(
        0x101,
        "#00005F#11P琪雅？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0126
    ChrTalk(
        0x1D,
        "#6P#01123F#3623V#30W#15A～～～唔……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_24(0xE27)
    OP_C9(0x1, 0x80000000)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)

    def lambda_8E3B():
        OP_96(0xFE, 0xFFFFA498, 0xFFFFDFF8, 0xFFFF9F84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_8E3B)
    Sleep(300)
    Fade(250)
    OP_68(-24900, -7100, -24000, 0)
    MoveCamera(327, 19, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(13500, 0)
    OP_68(-22900, -7100, -24700, 1000)
    MoveCamera(323, 23, 0, 1000)
    SetCameraDistance(13000, 1000)
    WaitChrThread(0x1D, 1)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)

    def lambda_8EC2():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8EC2)

    def lambda_8EDB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8EDB)

    def lambda_8EE8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8EE8)
    OP_6F(0x79)
    SetCameraDistance(12500, 50000)

    #C0127
    ChrTalk(
        0x101,
        "#11P#00011F哇哇……！\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        "#12P#00205F琪雅……？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        "#00105F怎、怎么了？\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#00302F#11P虽然发生了很多事情，\x01",
            "但琪雅不需要担心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x1D,
        "#5P#01114F#30W………嗯……………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetCameraDistance(12500, 1000)
    Sound(898, 0, 60, 0)
    Fade(250)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x1)
    OP_93(0x101, 0x5A, 0x0)
    OP_0D()
    OP_6F(0x79)

    #C0132
    ChrTalk(
        0x101,
        (
            "#11P#00004F……没关系的，琪雅。\x02\x03",

            "#00008F我们的确猜不到\x01",
            "克洛斯贝尔今后将会\x01",
            "进入怎样的局势……\x02\x03",

            "#00002F但无论到了什么时候，\x01",
            "我们也都会回到琪雅的身边，\x01",
            "这是绝对不会改变的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0x1D,
        "#5P#01105F#30W罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x103,
        (
            "#12P#00204F是啊……\x01",
            "只有这一点是不会改变的。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        (
            "#00302F#11P我们以前外出那么多次，\x01",
            "最后不是也都平安回来了嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x102,
        (
            "#00109F所以琪雅就放心\x01",
            "等着我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x1D,
        "#5P#01121F#40W艾莉、缇欧、兰迪……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1D)
    MoveCamera(326, 23, 0, 1000)
    SetCameraDistance(13000, 1000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x10E, 0x0)

    def lambda_91E4():
        OP_96(0xFE, 0xFFFFA36C, 0xFFFFDFF8, 0xFFFF9F84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_91E4)
    WaitChrThread(0x1D, 1)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0138
    AnonymousTalk(
        0x1D,
        (
            "#3624V#30W嗯……#800W！\x01",
            "#30W大家要小心啊！\x02",
        )
    )

    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE28)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(13500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "瓦吉离开了\x01",
            "队伍。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x8000)
    SetChrPos(0x0, -25340, -8200, -24760, 90)
    OP_69(0xFF, 0x0)
    OP_29(0xAC, 0x4, 0x10)
    OP_29(0xAD, 0x4, 0x2)
    OP_29(0xAD, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9359")
    Jump("loc_935E")

    label("loc_9359")

    OP_29(0x8E, 0x4, 0x40)

    label("loc_935E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_936F")
    Jump("loc_9374")

    label("loc_936F")

    OP_29(0x8F, 0x4, 0x40)

    label("loc_9374")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9385")
    Jump("loc_938A")

    label("loc_9385")

    OP_29(0x90, 0x4, 0x40)

    label("loc_938A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_939B")
    Jump("loc_93A0")

    label("loc_939B")

    OP_29(0x91, 0x4, 0x40)

    label("loc_93A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_93B1")
    Jump("loc_93B6")

    label("loc_93B1")

    OP_29(0x92, 0x4, 0x40)

    label("loc_93B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_93C7")
    Jump("loc_93CC")

    label("loc_93C7")

    OP_29(0x93, 0x4, 0x40)

    label("loc_93CC")

    SubItemNumber(0x328, 10)
    SubItemNumber(0x340, 1)
    SubItemNumber(0x375, 1)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    PlayBGM("ed7151", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7150", "ed7151")
    ReplaceBGM("ed7101", "ed7151")
    ReplaceBGM("ed7116", "ed7151")
    ReplaceBGM("ed7117", "ed7151")
    EventEnd(0x5)
    Return()

    # Function_49_8B9D end

    def Function_50_941C(): pass

    label("Function_50_941C")

    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)

    def lambda_9444():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA240, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9444)

    def lambda_945E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_945E)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    def lambda_948D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_948D)
    Return()

    # Function_50_941C end

    def Function_51_9496(): pass

    label("Function_51_9496")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20000.itc", 0x1E)
    LoadEffect(0x0, "event/ev17033.eff")
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x9, 0x2E)
    OP_49()
    SetChrPos(0x2E, -1000, 0, 18000, 180)
    OP_D5(0x2E, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x5)
    SetChrPos(0x0, 13600, 0, -14000, 0)
    SetChrPos(0x1, 13600, 0, -14000, 0)
    SetChrPos(0x2, 13600, 0, -14000, 0)
    SetChrPos(0x3, 13600, 0, -14000, 0)
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    ClearMapObjFlags(0x14, 0x4)
    OP_70(0x14, 0x0)
    SetMapObjFrame(0x14, "bell_add", 0x0, 0x1)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3000, 4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 3000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x21, 0x0)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 350, 0, 13000, 0)
    SetChrChipByIndex(0x22, 0x4)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -8300, 0, 5000, 0)
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x23, 0x2)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -7000, 0, 4600, 0)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x24, 0x3)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -8000, 0, 4100, 0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x6)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 8800, 0, 5000, 0)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x26, 0x5)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 9800, 0, 4600, 0)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x27, 0x1E)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -13800, 0, 8100, 0)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1600, 8700, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19000, 0)
    BeginChrThread(0x2E, 3, 0, 52)
    OP_68(0, 1600, 13700, 4000)
    SetCameraDistance(16000, 4000)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(250)
    OP_70(0x9, 0x7)
    Sleep(500)
    SetMessageWindowPos(50, 120, -1, -1)
    SetChrName("麦克道尔议长")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W正如各位所知──\x02\x03",

            "不久前，库罗伊斯前市长\x01",
            "发表了『克洛斯贝尔独立国』\x01",
            "正式创立的宣言。\x02\x03",

            "我想，或许有一部分人已经\x01",
            "接受了名为国防军的军事组织，\x01",
            "并习惯了如今的新体制……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_70(0x9, 0x8)
    Sleep(600)
    SetMessageWindowPos(50, 120, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("麦克道尔议长")

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W可是！\x01",
            "请大家再认真思考一次！\x02\x03",

            "如今这样的事态，\x01",
            "真的是我们自己『选择』的吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x2E, 3)
    WaitChrThread(0x22, 3)
    WaitChrThread(0x23, 3)
    WaitChrThread(0x24, 3)
    WaitChrThread(0x25, 3)
    WaitChrThread(0x26, 3)
    WaitChrThread(0x27, 3)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_9496 end

    def Function_52_991B(): pass

    label("Function_52_991B")

    Sleep(3000)
    BeginChrThread(0x25, 3, 0, 56)
    Sleep(100)
    BeginChrThread(0x26, 3, 0, 57)
    Sleep(2000)
    BeginChrThread(0x27, 3, 0, 58)
    Sleep(3000)
    BeginChrThread(0x22, 3, 0, 53)
    Sleep(100)
    BeginChrThread(0x23, 3, 0, 54)
    Sleep(100)
    BeginChrThread(0x24, 3, 0, 55)
    Return()

    # Function_52_991B end

    def Function_53_9952(): pass

    label("Function_53_9952")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_9962():
        OP_95(0xFE, -2800, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9962)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_53_9952 end

    def Function_54_9983(): pass

    label("Function_54_9983")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_9993():
        OP_95(0xFE, -1500, 0, 11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9993)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_54_9983 end

    def Function_55_99B4(): pass

    label("Function_55_99B4")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_99C4():
        OP_95(0xFE, -2500, 0, 10600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99C4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_55_99B4 end

    def Function_56_99E5(): pass

    label("Function_56_99E5")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_99F5():
        OP_95(0xFE, 1300, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99F5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_56_99E5 end

    def Function_57_9A16(): pass

    label("Function_57_9A16")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_9A26():
        OP_95(0xFE, 2300, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A26)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_57_9A16 end

    def Function_58_9A47(): pass

    label("Function_58_9A47")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_9A57():
        OP_95(0xFE, -2800, 0, 13100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A57)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_58_9A47 end

    def Function_59_9A78(): pass

    label("Function_59_9A78")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20000.itc", 0x1E)
    LoadEffect(0x0, "event/ev17033.eff")
    SoundLoad(828)
    SetChrPos(0x0, 13600, 0, -14000, 0)
    SetChrPos(0x1, 13600, 0, -14000, 0)
    SetChrPos(0x2, 13600, 0, -14000, 0)
    SetChrPos(0x3, 13600, 0, -14000, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    OP_70(0x14, 0x0)
    SetMapObjFrame(0x14, "bell_add", 0x0, 0x1)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 3000, 4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 3000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_68(0, 2500, 4000, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(0, 2000, 4000, 10000)
    MoveCamera(50, 29, 0, 10000)
    SetCameraDistance(24000, 10000)
    Sound(828, 2, 80, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x9, 0, 0, 60)
    StopSound(828, 1000, 70)
    StopEffect(0x0, 0x2)
    Sleep(5500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x33C)
    SetScenarioFlags(0x22, 1)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_59_9A78 end

    def Function_60_9C5F(): pass

    label("Function_60_9C5F")

    BeginChrThread(0x9, 3, 0, 66)
    Sleep(300)
    OP_4B(0xE, 0xFF)
    BeginChrThread(0xE, 3, 0, 63)
    Sleep(500)
    OP_4B(0xC, 0xFF)
    BeginChrThread(0xC, 3, 0, 64)
    Sleep(50)
    OP_4B(0xD, 0xFF)
    BeginChrThread(0xD, 3, 0, 65)
    Sleep(500)
    OP_4B(0xB, 0xFF)
    BeginChrThread(0xB, 3, 0, 61)
    Sleep(300)
    OP_4B(0xF, 0xFF)
    BeginChrThread(0xF, 3, 0, 62)
    Return()

    # Function_60_9C5F end

    def Function_61_9CA7(): pass

    label("Function_61_9CA7")


    def lambda_9CAC():
        OP_95(0xFE, -1600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9CAC)
    WaitChrThread(0xB, 1)
    Return()

    # Function_61_9CA7 end

    def Function_62_9CC6(): pass

    label("Function_62_9CC6")


    def lambda_9CCB():
        OP_95(0xFE, -2900, 0, -2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9CCB)
    WaitChrThread(0xF, 1)
    Return()

    # Function_62_9CC6 end

    def Function_63_9CE5(): pass

    label("Function_63_9CE5")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9CFF():
        OP_95(0xFE, 6300, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9CFF)
    WaitChrThread(0xE, 1)
    Return()

    # Function_63_9CE5 end

    def Function_64_9D19(): pass

    label("Function_64_9D19")

    OP_92(0xFE, 0x0, 0xFA0, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9D40():
        OP_95(0xFE, -1100, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9D40)
    WaitChrThread(0xC, 1)
    Return()

    # Function_64_9D19 end

    def Function_65_9D5A(): pass

    label("Function_65_9D5A")

    OP_92(0xFE, 0x0, 0xFA0, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9D81():
        OP_95(0xFE, 400, 0, 12100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9D81)
    WaitChrThread(0xD, 1)
    Return()

    # Function_65_9D5A end

    def Function_66_9D9B(): pass

    label("Function_66_9D9B")

    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -6900, 0, 4200, 270)
    OP_0D()
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_66_9D9B end

    def Function_67_9DE4(): pass

    label("Function_67_9DE4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch03150.itc", 0x23)
    LoadChrToIndex("chr/ch03250.itc", 0x24)
    LoadChrToIndex("monster/ch85152.itc", 0x27)
    LoadEffect(0x0, "event/ev17060.eff")
    SoundLoad(828)
    OP_32(0xFF, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrPos(0x101, 3600, 0, -27000, 0)
    SetChrPos(0x102, 3600, 0, -27000, 0)
    SetChrPos(0x103, 2200, 0, -27000, 0)
    SetChrPos(0x104, 3600, 0, -27000, 0)
    SetChrPos(0x109, 3600, 0, -27000, 0)
    SetChrPos(0x105, 2200, 0, -27000, 0)
    SetChrPos(0x106, 2200, 0, -27000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrChipByIndex(0x28, 0x10)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 5300, 0, -3000, 225)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x28, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x29, 0x10)
    SetChrSubChip(0x29, 0x0)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 4300, 0, -9500, 270)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x29, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2A, 0x10)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -7500, 0, -6600, 105)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x2A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 2500, 4000, 0)
    MoveCamera(57, 5, -20, 0)
    OP_6E(700, 0)
    SetCameraDistance(19000, 0)
    OP_F0(0x0, 0x1)
    Sound(828, 2, 80, 0)
    MoveCamera(23, 10, -15, 9000)
    SetCameraDistance(24000, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(5500)
    BeginChrThread(0x101, 3, 0, 68)
    Sleep(250)
    BeginChrThread(0x103, 3, 0, 70)
    Sleep(250)
    BeginChrThread(0x102, 3, 0, 69)
    Sleep(250)
    BeginChrThread(0x105, 3, 0, 72)
    Sleep(250)
    BeginChrThread(0x104, 3, 0, 71)
    Sleep(250)
    BeginChrThread(0x106, 3, 0, 73)
    Sleep(250)
    BeginChrThread(0x109, 3, 0, 74)
    OP_6F(0x79)
    Fade(500)
    OP_68(2900, 1300, -17000, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    OP_68(-900, 1500, -2000, 5000)
    MoveCamera(43, 13, 0, 5000)
    SetCameraDistance(18000, 5000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)

    #C0142
    ChrTalk(
        0x101,
        "#00013F#12P这是……！\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#00101F#12P和之前笼罩着克洛斯贝尔市的\x01",
            "『结界』似乎相同……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        (
            "#12P#00206F#12P多半是同一物质。\x02\x03",

            "#00201F……另外，这种雾气也许\x01",
            "是由大钟的鸣响而引发的。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        "#00301F#12P喂喂，他们为何要……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x38, 1, 0, 83)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A257():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A257)

    def lambda_A264():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A264)
    Sleep(50)

    def lambda_A274():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A274)

    def lambda_A281():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_A281)
    Sleep(50)

    def lambda_A291():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A291)

    def lambda_A29E():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A29E)
    Sleep(50)

    def lambda_A2AE():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A2AE)
    Sleep(300)

    #C0146
    ChrTalk(
        0x109,
        "#10111F#5P这是……！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x106,
        (
            "#10701F#11P注意，\x01",
            "周围有东西过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x105,
        "#11P#10410F#11P这不就是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x38, 0x1)
    Fade(500)
    OP_68(-7500, 1100, -6600, 0)
    MoveCamera(337, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11000, 0)
    OP_F0(0x0, 0xD)
    SetCameraDistance(12000, 2000)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    BeginChrThread(0x28, 0, 0, 75)
    BeginChrThread(0x29, 0, 0, 75)
    BeginChrThread(0x2A, 0, 0, 75)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x3, 0x2A, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_A3CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_A3CB)
    WaitChrThread(0x2A, 2)
    StopEffect(0x3, 0x2)
    Sleep(300)
    OP_68(-1900, 1300, -7000, 3000)
    MoveCamera(47, 15, 0, 3000)
    SetCameraDistance(14000, 3000)
    PlayEffect(0x0, 0x1, 0x28, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x29, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sound(985, 0, 70, 0)
    Sleep(2000)

    def lambda_A485():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_A485)
    Sleep(300)

    def lambda_A499():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_A499)
    WaitChrThread(0x28, 2)
    StopEffect(0x1, 0x2)
    WaitChrThread(0x29, 2)
    StopEffect(0x2, 0x2)
    OP_6F(0x79)
    OP_F0(0x0, 0xA)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x24)
    SetChrSubChip(0x106, 0x0)
    OP_0D()

    #C0149
    ChrTalk(
        0x102,
        "#6P#00107F出现在『星见之塔』的那种……！？\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#11P#00207F虽然同为魔导智能兵器，\x01",
            "但远比星见之塔中的危险……！\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        "#6P#00307F总之，赶快消灭这些家伙！\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#5P#00007F嗯，解决它们！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x28, 3, 0, 77)
    BeginChrThread(0x29, 3, 0, 77)
    BeginChrThread(0x2A, 3, 0, 77)
    Sleep(260)
    Sound(951, 0, 70, 0)
    Sleep(1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(11500, 500)
    Sleep(500)
    Sound(532, 0, 100, 0)
    EndChrThread(0x28, 0xFF)
    EndChrThread(0x29, 0xFF)
    EndChrThread(0x2A, 0xFF)
    SetChrBattleFlags(0x6, 0x8)
    Battle("BattleInfo_1E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_49()
    ClearChrBattleFlags(0x6, 0x8)
    Call(0, 84)
    Return()

    # Function_67_9DE4 end

    def Function_68_A6E5(): pass

    label("Function_68_A6E5")


    def lambda_A6EA():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A6EA)
    WaitChrThread(0xFE, 1)

    def lambda_A708():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A708)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_A6E5 end

    def Function_69_A722(): pass

    label("Function_69_A722")


    def lambda_A727():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A727)
    WaitChrThread(0xFE, 1)

    def lambda_A745():
        OP_96(0xFE, 0x64, 0x0, 0xFFFFEB4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A745)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_A722 end

    def Function_70_A75F(): pass

    label("Function_70_A75F")


    def lambda_A764():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A764)
    WaitChrThread(0xFE, 1)

    def lambda_A782():
        OP_96(0xFE, 0xFFFFFA88, 0x0, 0xFFFFE9BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A782)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_A75F end

    def Function_71_A79C(): pass

    label("Function_71_A79C")


    def lambda_A7A1():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A7A1)
    WaitChrThread(0xFE, 1)

    def lambda_A7BF():
        OP_96(0xFE, 0x190, 0x0, 0xFFFFE50C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A7BF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_71_A79C end

    def Function_72_A7D9(): pass

    label("Function_72_A7D9")


    def lambda_A7DE():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A7DE)
    WaitChrThread(0xFE, 1)

    def lambda_A7FC():
        OP_96(0xFE, 0xFFFFF4AC, 0x0, 0xFFFFE7C8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A7FC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_72_A7D9 end

    def Function_73_A816(): pass

    label("Function_73_A816")


    def lambda_A81B():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A81B)
    WaitChrThread(0xFE, 1)

    def lambda_A839():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0xFFFFE3E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A839)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_73_A816 end

    def Function_74_A853(): pass

    label("Function_74_A853")


    def lambda_A858():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A858)
    WaitChrThread(0xFE, 1)

    def lambda_A876():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0xFFFFE37C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A876)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_74_A853 end

    def Function_75_A890(): pass

    label("Function_75_A890")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8AE")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_75_A890")

    label("loc_A8AE")

    Return()

    # Function_75_A890 end

    def Function_76_A8AF(): pass

    label("Function_76_A8AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8CB")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_76_A8AF")

    label("loc_A8CB")

    Return()

    # Function_76_A8AF end

    def Function_77_A8CC(): pass

    label("Function_77_A8CC")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_A8FD():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A8FD)
    Sleep(1000)
    SetChrFlags(0xFE, 0x20)

    def lambda_A91E():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFE764, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A91E)
    Sleep(300)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_77_A8CC end

    def Function_78_A946(): pass

    label("Function_78_A946")

    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_A985():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A985)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_78_A946 end

    def Function_79_A999(): pass

    label("Function_79_A999")

    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_A9D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A9D8)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_79_A999 end

    def Function_80_A9EC(): pass

    label("Function_80_A9EC")

    PlayEffect(0x0, 0x3, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_AA2B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AA2B)
    WaitChrThread(0xFE, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_80_A9EC end

    def Function_81_AA3F(): pass

    label("Function_81_AA3F")

    PlayEffect(0x0, 0x4, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_AA7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AA7E)
    WaitChrThread(0xFE, 2)
    StopEffect(0x4, 0x2)
    Return()

    # Function_81_AA3F end

    def Function_82_AA92(): pass

    label("Function_82_AA92")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_AAD1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AAD1)
    WaitChrThread(0xFE, 2)
    StopEffect(0x5, 0x2)
    Return()

    # Function_82_AA92 end

    def Function_83_AAE5(): pass

    label("Function_83_AAE5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AAFE")
    Sound(986, 0, 80, 0)
    Sleep(1000)
    Jump("Function_83_AAE5")

    label("loc_AAFE")

    Return()

    # Function_83_AAE5 end

    def Function_84_AAFF(): pass

    label("Function_84_AAFF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    SoundLoad(3465)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    AddParty(0x9, 0xFF, 0xFF)
    OP_32(0x9, 0x0, 0x5F)
    OP_32(0x9, 0x5, 0xC8)
    OP_42(0x9, 0x467, 0xFF)
    OP_42(0x9, 0x5ED, 0xFF)
    OP_42(0x9, 0x651, 0xFF)
    OP_38(0x9, 0x81, 0x2)
    OP_38(0x9, 0x82, 0x2)
    OP_38(0x9, 0x83, 0x2)
    OP_38(0x9, 0x84, 0x2)
    OP_38(0x9, 0x85, 0x2)
    OP_38(0x9, 0x86, 0x1)
    OP_42(0x9, 0x72, 0x1)
    OP_42(0x9, 0xAD, 0x2)
    OP_42(0x9, 0x93, 0x3)
    OP_42(0x9, 0x8A, 0x4)
    OP_42(0x9, 0x90, 0x5)
    OP_42(0x9, 0x69, 0x6)
    AddCraft(0x9, 0xF8)
    AddCraft(0x9, 0x17A)
    AddCraft(0x9, 0x148)
    SetChrChipPat(0x9, 0x6, 0x145)
    SetChrChipPat(0x9, 0x6, 0x148)
    SetChrChipPat(0x9, 0x6, 0x146)
    LoadChrToIndex("apl/ch50539.itc", 0x0)
    LoadChrToIndex("apl/ch50506.itc", 0x1)
    LoadChrToIndex("apl/ch50509.itc", 0x2)
    LoadChrToIndex("chr/ch00950.itc", 0x3)
    LoadChrToIndex("chr/ch00951.itc", 0x4)
    LoadChrToIndex("chr/ch00952.itc", 0x5)
    LoadChrToIndex("chr/ch00050.itc", 0x6)
    LoadChrToIndex("chr/ch00051.itc", 0x7)
    LoadChrToIndex("chr/ch00150.itc", 0x8)
    LoadChrToIndex("chr/ch00151.itc", 0x9)
    LoadChrToIndex("chr/ch00250.itc", 0xA)
    LoadChrToIndex("chr/ch00251.itc", 0xB)
    LoadChrToIndex("chr/ch00350.itc", 0xC)
    LoadChrToIndex("chr/ch00351.itc", 0xD)
    LoadChrToIndex("chr/ch02950.itc", 0xE)
    LoadChrToIndex("chr/ch02951.itc", 0xF)
    LoadChrToIndex("chr/ch03150.itc", 0x10)
    LoadChrToIndex("chr/ch03151.itc", 0x11)
    LoadChrToIndex("chr/ch03250.itc", 0x12)
    LoadChrToIndex("chr/ch03251.itc", 0x13)
    LoadChrToIndex("monster/ch85150.itc", 0x14)
    LoadChrToIndex("monster/ch85151.itc", 0x15)
    LoadChrToIndex("monster/ch85153.itc", 0x16)
    LoadChrToIndex("monster/ch85152.itc", 0x17)
    LoadEffect(0x0, "event/ev17060.eff")
    LoadEffect(0x1, "event/ev17061.eff")
    LoadEffect(0x2, "battle/btgun00.eff")
    LoadEffect(0x3, "event/ev606_00.eff")
    LoadEffect(0x4, "battle\\ms00001.eff")
    SoundLoad(828)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x101, 0x6)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x8)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xA)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xE)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x10)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x12)
    SetChrSubChip(0x106, 0x0)
    SetChrPos(0x101, -900, 0, -4000, 0)
    SetChrPos(0x102, 100, 0, -5300, 0)
    SetChrPos(0x103, -1400, 0, -5700, 0)
    SetChrPos(0x104, 400, 0, -6900, 0)
    SetChrPos(0x109, -1100, 0, -7300, 0)
    SetChrPos(0x105, -2900, 0, -6200, 0)
    SetChrPos(0x106, -2500, 0, -7200, 0)
    SetChrPos(0x10A, 25500, 0, -3000, 270)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    SetChrChipByIndex(0x28, 0x16)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 5300, 0, -3000, 225)
    OP_52(0x28, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x29, 0x16)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 4300, 0, -9500, 270)
    OP_52(0x29, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2A, 0x16)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -7500, 0, -6600, 105)
    OP_52(0x2A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2B, 0x14)
    SetChrSubChip(0x2B, 0x0)
    SetChrFlags(0x2B, 0x8000)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x2B, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2C, 0x14)
    SetChrSubChip(0x2C, 0x0)
    SetChrFlags(0x2C, 0x8000)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x2C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1F, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 25100, 0, -4300, 270)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AF60():
        TurnDirection(0xFE, 0x28, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AF60)

    def lambda_AF6D():
        TurnDirection(0xFE, 0x28, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AF6D)

    def lambda_AF7A():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AF7A)

    def lambda_AF87():
        TurnDirection(0xFE, 0x29, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AF87)

    def lambda_AF94():
        TurnDirection(0xFE, 0x29, 0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AF94)

    def lambda_AFA1():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AFA1)

    def lambda_AFAE():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_AFAE)
    OP_68(-1900, 1300, -7000, 0)
    MoveCamera(47, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    OP_F0(0x0, 0x1)
    PlayEffect(0x1, 0x1, 0x28, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x29, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x2A, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(828, 2, 80, 0)
    SetCameraDistance(14000, 3000)
    Sound(985, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_B0B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_B0B4)
    Sleep(300)

    def lambda_B0C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_B0C8)
    Sleep(300)

    def lambda_B0DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_B0DC)
    WaitChrThread(0x28, 2)
    StopEffect(0x1, 0x2)
    WaitChrThread(0x29, 2)
    StopEffect(0x2, 0x2)
    WaitChrThread(0x2A, 2)
    StopEffect(0x3, 0x2)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_0D()

    def lambda_B163():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B163)

    def lambda_B170():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B170)
    Sleep(50)

    def lambda_B180():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B180)
    Sleep(50)

    def lambda_B190():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B190)
    Sleep(50)

    def lambda_B1A0():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B1A0)
    Sleep(50)

    def lambda_B1B0():
        TurnDirection(0x106, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_B1B0)
    Sleep(50)

    def lambda_B1C0():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B1C0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)

    #C0153
    ChrTalk(
        0x101,
        (
            "#5P#00010F唔……\x01",
            "那种东西为何会出现在城市里！？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        (
            "#11P#00101F难、难道……\x01",
            "是迪塔叔叔他们放出来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x109,
        (
            "#12P#10107F怎、怎么会……\x01",
            "这绝对不能原谅！\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x105,
        (
            "#6P#10403F不管怎么说，这的确是\x01",
            "可能性最高的答案呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(100)

    #C0157
    ChrTalk(
        0x105,
        (
            "#12P#10408F看样子，魔导兵的出现\x01",
            "与这口『钟』也存在着一定关系……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B341():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B341)

    def lambda_B34E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_B34E)

    #C0158
    ChrTalk(
        0x103,
        "#11P#00201F啊……！\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x106,
        "#6P#10707F……又来了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-1900, 1300, -6700, 3000)
    MoveCamera(40, 25, 0, 3000)
    SetCameraDistance(17500, 3000)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x28, 5300, 0, -3000, 225)
    SetChrPos(0x29, 5300, 0, -8000, 270)
    SetChrPos(0x2A, -7300, 0, -7400, 90)
    SetChrPos(0x2B, -6000, 0, -2400, 135)
    SetChrPos(0x2C, -1500, 0, -12000, 0)
    SetChrChipByIndex(0x28, 0x14)
    SetChrSubChip(0x28, 0x0)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x29, 0x14)
    SetChrSubChip(0x29, 0x0)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2A, 0x14)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2B, 0x14)
    SetChrSubChip(0x2B, 0x0)
    OP_52(0x2B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2C, 0x14)
    SetChrSubChip(0x2C, 0x0)
    OP_52(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x28, 0, 0, 75)
    BeginChrThread(0x29, 0, 0, 75)
    BeginChrThread(0x2A, 0, 0, 75)
    BeginChrThread(0x2B, 0, 0, 75)
    BeginChrThread(0x2C, 0, 0, 75)
    SetChrChipByIndex(0x101, 0x6)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x8)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xA)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xE)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x10)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x12)
    SetChrSubChip(0x106, 0x0)

    def lambda_B590():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B590)

    def lambda_B59D():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B59D)

    def lambda_B5AA():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B5AA)

    def lambda_B5B7():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B5B7)

    def lambda_B5C4():
        TurnDirection(0xFE, 0x2C, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B5C4)

    def lambda_B5D1():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B5D1)

    def lambda_B5DE():
        TurnDirection(0xFE, 0x2C, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_B5DE)
    Sound(985, 0, 100, 0)
    BeginChrThread(0x2A, 3, 0, 80)
    Sleep(300)
    BeginChrThread(0x28, 3, 0, 78)
    Sleep(300)
    BeginChrThread(0x2C, 3, 0, 82)
    Sleep(300)
    Sound(985, 0, 50, 0)
    BeginChrThread(0x29, 3, 0, 79)
    Sleep(300)
    BeginChrThread(0x2B, 3, 0, 81)
    WaitChrThread(0x2B, 3)
    OP_6F(0x79)

    #C0160
    ChrTalk(
        0x101,
        "#11P#00011F……糟糕！\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x104,
        "#5P#00311F啧……不妙啊。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        (
            "#6P#10110F唔……\x01",
            "必须要想办法突围！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 1200)
    BeginChrThread(0x2A, 1, 0, 94)
    BeginChrThread(0x28, 3, 0, 87)
    Sound(951, 0, 80, 0)
    Sleep(200)
    BeginChrThread(0x2B, 1, 0, 95)
    BeginChrThread(0x29, 3, 0, 87)
    Sleep(200)
    BeginChrThread(0x2C, 1, 0, 96)
    Sleep(600)
    Sound(987, 0, 100, 0)
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrChipByIndex(0x28, 0x14)
    SetChrSubChip(0x28, 0x0)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_B6F7():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_B6F7)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x28, 0x1, 1300, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x28, 0x3)
    Sleep(50)
    SetChrChipByIndex(0x29, 0x14)
    SetChrSubChip(0x29, 0x0)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_B772():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_B772)
    Sound(567, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x29, 0x1, 1300, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x29, 0x3)
    EndChrThread(0x2A, 0x0)
    EndChrThread(0x2A, 0x1)
    SetChrChipByIndex(0x2A, 0x14)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2A, 0x20)
    EndChrThread(0x2B, 0x0)
    EndChrThread(0x2B, 0x1)
    SetChrChipByIndex(0x2B, 0x14)
    SetChrSubChip(0x2B, 0x0)
    OP_52(0x2B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2B, 0x20)
    EndChrThread(0x2C, 0x0)
    EndChrThread(0x2C, 0x1)
    SetChrChipByIndex(0x2C, 0x14)
    SetChrSubChip(0x2C, 0x0)
    OP_52(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2C, 0x20)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_B865():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B865)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_B88A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B88A)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_B8B2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B8B2)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_B8D7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B8D7)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_B8FF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B8FF)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_B924():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B924)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_B949():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_B949)
    Sleep(1000)

    def lambda_B959():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_B959)

    def lambda_B966():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_B966)

    def lambda_B973():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_B973)

    def lambda_B980():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_B980)

    def lambda_B98D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_B98D)
    OP_68(14800, 1000, -3800, 2000)
    MoveCamera(45, 17, 0, 2000)
    SetCameraDistance(14000, 2000)
    Sleep(1000)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1F, 0x1)
    SetChrSubChip(0x1F, 0x0)

    def lambda_B9CF():
        OP_96(0xFE, 0x3AFC, 0x0, 0xFFFFEF34, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_B9CF)

    def lambda_B9E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_B9E9)
    Sleep(200)
    SetChrChipByIndex(0x10A, 0x3)
    SetChrSubChip(0x10A, 0x0)

    def lambda_BA05():
        OP_96(0xFE, 0x38A4, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_BA05)

    def lambda_BA1F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_BA1F)
    WaitChrThread(0x1F, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1F, 0x2)
    SetChrSubChip(0x1F, 0x0)
    WaitChrThread(0x10A, 1)
    OP_6F(0x79)

    #C0163
    ChrTalk(
        0x103,
        "#00205F#6P#N科长……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0164
    ChrTalk(
        0x102,
        "#00102F#6P#N还有达德利警官！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0165
    AnonymousTalk(
        0x1F,
        "哼，你们终于来了啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0166
    AnonymousTalk(
        0x10A,
        (
            "#3465V#30W有话稍后再说！\x01",
            "赶快跟上来！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD89)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0167
    ChrTalk(
        0x101,
        "#00002F#6P#N是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0168
    ChrTalk(
        0x104,
        "#00302F#6P#N收到！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, 1000, 0, -4500, 90)
    SetChrPos(0x102, 1000, 0, -4500, 90)
    SetChrPos(0x103, 1000, 0, -6000, 90)
    SetChrPos(0x104, 1000, 0, -6000, 90)
    SetChrPos(0x109, 1000, 0, -6000, 90)
    SetChrPos(0x105, 1000, 0, -4500, 90)
    SetChrPos(0x106, 1000, 0, -4500, 90)
    SetChrPos(0x2A, -300, 0, -7400, 90)
    SetChrPos(0x2B, -1500, 0, -2400, 90)
    SetChrPos(0x2C, -1000, 0, -12000, 90)
    OP_68(9300, 1000, -4800, 2000)
    MoveCamera(41, 15, 0, 2000)
    SetCameraDistance(14500, 2000)
    SetChrChipByIndex(0x10A, 0x5)
    SetChrSubChip(0x10A, 0x0)
    BeginChrThread(0x10A, 0, 0, 88)
    Sleep(100)
    BeginChrThread(0x1F, 0, 0, 89)
    BeginChrThread(0x38, 1, 0, 90)
    BeginChrThread(0x38, 2, 0, 83)
    BeginChrThread(0x28, 0, 0, 86)
    BeginChrThread(0x28, 1, 0, 92)
    Sleep(100)
    BeginChrThread(0x29, 0, 0, 86)
    BeginChrThread(0x29, 1, 0, 93)
    Sleep(100)
    BeginChrThread(0x2A, 0, 0, 86)
    BeginChrThread(0x2A, 1, 0, 92)
    Sleep(100)
    BeginChrThread(0x2B, 0, 0, 86)
    BeginChrThread(0x2B, 1, 0, 93)
    Sleep(100)
    BeginChrThread(0x2C, 0, 0, 86)
    BeginChrThread(0x2C, 1, 0, 93)
    Sleep(1500)
    MoveCamera(46, 20, 5, 12000)
    SetCameraDistance(14000, 12000)
    BeginChrThread(0x103, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 85)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x106, 3, 0, 85)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x104, 3, 0, 85)
    WaitChrThread(0x104, 3)
    EndChrThread(0x10A, 0x0)
    EndChrThread(0x28, 0x0)
    BeginChrThread(0x28, 1, 0, 92)
    EndChrThread(0x2A, 0x0)
    BeginChrThread(0x2A, 1, 0, 92)
    SetChrChipByIndex(0x10A, 0x3)
    SetChrSubChip(0x10A, 0x0)
    OP_93(0x10A, 0x5A, 0x1F4)

    def lambda_BDB8():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_BDB8)
    Sleep(300)
    EndChrThread(0x38, 0x1)
    EndChrThread(0x1F, 0x0)
    EndChrThread(0x29, 0x0)
    BeginChrThread(0x29, 1, 0, 93)
    EndChrThread(0x2B, 0x0)
    BeginChrThread(0x2B, 1, 0, 93)
    EndChrThread(0x2C, 0x0)
    BeginChrThread(0x2C, 1, 0, 93)
    SetChrChipByIndex(0x1F, 0x0)
    SetChrSubChip(0x1F, 0x0)
    OP_93(0x1F, 0x5A, 0x1F4)
    SetChrChipByIndex(0x1F, 0x1)
    SetChrSubChip(0x1F, 0x0)

    def lambda_BE12():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_BE12)
    Sleep(500)
    EndChrThread(0x38, 0x2)
    StopSound(828, 2000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    EndChrThread(0x106, 0xFF)
    EndChrThread(0x10A, 0xFF)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人经由\x01",
            "曲折的小路，终于穿越了\x01",
            "充斥着蓝白色雾气的市区……\x02\x03",

            "并从旧城区的角落\x01",
            "来到了地下空间Ｄ区域。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("m0302", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_84_AAFF end

    def Function_85_BF02(): pass

    label("Function_85_BF02")


    def lambda_BF07():
        OP_95(0xFE, 12000, 0, -6200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF07)
    WaitChrThread(0xFE, 1)

    def lambda_BF25():
        OP_95(0xFE, 26000, 0, -6200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF25)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_85_BF02 end

    def Function_86_BF3F(): pass

    label("Function_86_BF3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C02E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C026")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_4B(0xFE, 0x1)
    OP_4B(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_BF8E():
        OP_A6(0xFE, 0x0, 0x32, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BF8E)
    PlayEffect(0x4, 0xFF, 0xFE, 0x1, 1300, 1500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x2710, 0x0)
    Sleep(900)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 3, 0, 75)
    Sleep(600)
    OP_4C(0xFE, 0x1)
    BeginChrThread(0xFE, 3, 0, 91)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_C026")

    Sleep(300)
    Jump("Function_86_BF3F")

    label("loc_C02E")

    Return()

    # Function_86_BF3F end

    def Function_87_C02F(): pass

    label("Function_87_C02F")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_C060():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C060)
    Sleep(1000)
    Return()

    # Function_87_C02F end

    def Function_88_C078(): pass

    label("Function_88_C078")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1200, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    label("loc_C0C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C147")
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    Sound(567, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1200, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_C0C6")

    label("loc_C147")

    Return()

    # Function_88_C078 end

    def Function_89_C148(): pass

    label("Function_89_C148")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(987, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)

    label("loc_C196")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C24E")
    SetChrSubChip(0x1F, 0x5)
    Sleep(150)
    SetChrSubChip(0x1F, 0x6)
    Sleep(100)
    SetChrSubChip(0x1F, 0x7)
    Sleep(100)
    SetChrSubChip(0x1F, 0x4)
    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrSubChip(0x1F, 0x3)
    Sleep(70)
    SetChrSubChip(0x1F, 0x2)
    Sleep(70)
    SetChrSubChip(0x1F, 0x1)
    Sleep(70)
    SetChrSubChip(0x1F, 0x0)
    Sleep(70)
    SetChrSubChip(0x1F, 0x1)
    Sleep(70)
    SetChrSubChip(0x1F, 0x2)
    Sleep(70)
    SetChrSubChip(0x1F, 0x3)
    Sleep(70)
    SetChrSubChip(0x1F, 0x4)
    Sleep(600)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    Sound(987, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Jump("loc_C196")

    label("loc_C24E")

    Return()

    # Function_89_C148 end

    def Function_90_C24F(): pass

    label("Function_90_C24F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C268")
    Sound(501, 0, 100, 0)
    Sleep(1500)
    Jump("Function_90_C24F")

    label("loc_C268")

    Return()

    # Function_90_C24F end

    def Function_91_C269(): pass

    label("Function_91_C269")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C29A")
    SetChrChipByIndex(0xFE, 0x15)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A0(0xFE, 1000, 0x0, 0x5)
    Jump("Function_91_C269")

    label("loc_C29A")

    Return()

    # Function_91_C269 end

    def Function_92_C29B(): pass

    label("Function_92_C29B")

    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 3, 0, 91)
    OP_99(0xFE, 0x10A, 0x1388, 0x1F4, 0x0)
    EndChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 3, 0, 75)
    Return()

    # Function_92_C29B end

    def Function_93_C2E2(): pass

    label("Function_93_C2E2")

    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 3, 0, 91)
    OP_99(0xFE, 0x1F, 0x1388, 0x1F4, 0x0)
    EndChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 3, 0, 75)
    Return()

    # Function_93_C2E2 end

    def Function_94_C329(): pass

    label("Function_94_C329")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C37D")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 91)
    OP_9B(0x1, 0xFE, 0x0, 0x2EE, 0x3E8, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    Jump("Function_94_C329")

    label("loc_C37D")

    Return()

    # Function_94_C329 end

    def Function_95_C37E(): pass

    label("Function_95_C37E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C3D2")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 91)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    Jump("Function_95_C37E")

    label("loc_C3D2")

    Return()

    # Function_95_C37E end

    def Function_96_C3D3(): pass

    label("Function_96_C3D3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C427")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 91)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    Jump("Function_96_C3D3")

    label("loc_C427")

    Return()

    # Function_96_C3D3 end

    def Function_97_C428(): pass

    label("Function_97_C428")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadChrToIndex("monster/ch85150.itc", 0x1E)
    LoadChrToIndex("monster/ch85151.itc", 0x1F)
    LoadChrToIndex("monster/ch85153.itc", 0x20)
    LoadEffect(0x0, "event/ev17061.eff")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    SetChrPos(0x28, -6800, 0, -600, 90)
    SetChrPos(0x29, -8600, 0, 4700, 270)
    SetChrPos(0x2A, 9900, 0, 700, 0)
    SetChrChipByIndex(0x28, 0x1E)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    OP_52(0x28, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x29, 0x1E)
    SetChrSubChip(0x29, 0x0)
    SetChrFlags(0x29, 0x8000)
    OP_52(0x29, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2A, 0x1E)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x8000)
    OP_52(0x2A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x28, 3, 0, 98)
    BeginChrThread(0x29, 3, 0, 99)
    BeginChrThread(0x2A, 3, 0, 100)
    OP_68(0, 1100, 4000, 0)
    MoveCamera(53, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23000, 0)
    OP_71(0x16, 0x208, 0x2BC, 0x0, 0x0)
    MoveCamera(31, 21, 0, 11000)
    SetCameraDistance(29000, 11000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    Sound(371, 0, 70, 0)
    Sleep(500)
    Fade(500)
    StopSound(828, 2000, 40)
    OP_70(0x14, 0x0)
    SetMapObjFrame(0x14, "bell_add", 0x0, 0x1)
    OP_0D()
    StopEffect(0x6, 0x2)
    Sleep(1000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1770)
    OP_11(0x7B, 0xB4, 0xD5, 0x26, 0x82, 0x1770)
    Sleep(2000)
    StopEffect(0x7, 0x2)
    Sleep(2500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 0)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_97_C428 end

    def Function_98_C653(): pass

    label("Function_98_C653")

    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x28, 0x20)
    BeginChrThread(0xFE, 0, 0, 76)

    def lambda_C681():
        OP_95(0xFE, -3200, 0, -3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_C681)
    WaitChrThread(0x28, 1)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0x28, 0x20)
    SetChrChipByIndex(0x28, 0x1E)
    SetChrSubChip(0x28, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x28, 0xB4, 0x1F4)
    BeginChrThread(0x28, 0, 0, 75)
    Sleep(2500)
    Sound(985, 0, 100, 0)
    Sleep(500)
    EndChrThread(0x28, 0x0)
    PlayEffect(0x0, 0x1, 0x28, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x28, 0x20)
    SetChrSubChip(0x28, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    def lambda_C73B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C73B)
    WaitChrThread(0x28, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_98_C653 end

    def Function_99_C74F(): pass

    label("Function_99_C74F")

    BeginChrThread(0x29, 0, 0, 75)
    Sleep(5000)
    EndChrThread(0x29, 0x0)
    Sound(985, 0, 50, 0)
    PlayEffect(0x0, 0x2, 0x29, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x29, 0x20)
    SetChrSubChip(0x29, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    def lambda_C7BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_C7BF)
    WaitChrThread(0x29, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_99_C74F end

    def Function_100_C7D3(): pass

    label("Function_100_C7D3")

    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2A, 0x20)
    BeginChrThread(0xFE, 0, 0, 76)

    def lambda_C801():
        OP_95(0xFE, 9900, 0, 7700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_C801)
    WaitChrThread(0x2A, 1)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0x2A, 0x20)
    SetChrChipByIndex(0x2A, 0x1E)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x2A, 0, 0, 75)
    Sleep(3000)
    EndChrThread(0x2A, 0x0)
    Sound(985, 0, 50, 0)
    PlayEffect(0x0, 0x3, 0x2A, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x2A, 0x20)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    def lambda_C8B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_C8B1)
    WaitChrThread(0x2A, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_100_C7D3 end

    def Function_101_C8C5(): pass

    label("Function_101_C8C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46500.itc", 0x1E)
    LoadChrToIndex("chr/ch46600.itc", 0x1F)
    OP_68(-13800, 1900, 8170, 0)
    MoveCamera(323, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8940, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x40, 0x80)
    SetChrChipByIndex(0x40, 0x1E)
    SetChrSubChip(0x40, 0x0)
    SetChrPos(0x40, -15530, 0, 9880, 90)
    ClearChrFlags(0x3F, 0x80)
    SetChrChipByIndex(0x3F, 0x1F)
    SetChrSubChip(0x3F, 0x0)
    SetChrPos(0x3F, -14080, 0, 9690, 270)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0170
    ChrTalk(
        0x3F,
        (
            "#12P#12400F真是的，你这家伙……\x01",
            "每次都这么任性妄为。\x02\x03",

            "你又不是不知道\x01",
            "这克洛斯贝尔\x01",
            "是个怎样的地方。\x02\x03",

            "#12406F多少也考虑一下\x01",
            "自己的立场吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x40,
        (
            "#13902F呵，好像让你担心了啊。\x02\x03",

            "#13904F不过，在无法自由行动之前，\x01",
            "我无论如何也想好好观察一下这座城市。\x02\x03",

            "多亏之前的游历，\x01",
            "如今我总算明白这座城市\x01",
            "为何会被称为魔都了。\x02\x03",

            "#13908F……看样子，『他』似乎\x01",
            "也在暗地里行动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x3F,
        (
            "#12P#12400F……嗯，\x01",
            "看来你有所收获啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x40,
        (
            "#13900F呵，托你的福，\x01",
            "我还经历了一场愉快的邂逅呢。\x02\x03",

            "#13905F……哦，对了，\x01",
            "那件事情安排得如何了？\x02\x03",

            "#13904F以你的作风来说，\x01",
            "在我离开的时候，\x01",
            "肯定就已经妥善安排好了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x3F,
        (
            "#12P#12400F嗯，已经和他们联络过了。\x02\x03",

            "#12406F但因为你到处乱跑，\x01",
            "时间安排只能稍作推迟。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x40,
        (
            "#13904F呵呵，那我们就赶快出发吧。\x02\x03",

            "#13900F不能让美丽的女士们\x01",
            "等待太久哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找演奏家】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x76, 0x1, 0x4)
    OP_29(0x76, 0x1, 0x5)
    OP_29(0x76, 0x4, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 6)
    NewScene("c0500", 100, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_101_C8C5 end

    def Function_102_CCDC(): pass

    label("Function_102_CCDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(975)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    OP_78(0xF, 0x2E)
    SetMapObjFrame(0xF, "light", 0x0, 0x1)
    OP_74(0xF, 0x1E)
    OP_71(0xF, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    OP_49()
    SetChrPos(0x2E, 28000, 0, -3910, 270)
    OP_D5(0x2E, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    OP_78(0xC, 0x2F)
    OP_78(0xD, 0x30)
    OP_78(0xE, 0x31)
    OP_49()
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    OP_74(0xC, 0x1E)
    OP_74(0xD, 0x1E)
    OP_74(0xE, 0x1E)
    OP_71(0xC, 0x79, 0xB4, 0x1, 0x20)
    OP_71(0xD, 0x79, 0xB4, 0x1, 0x20)
    OP_71(0xE, 0x79, 0xB4, 0x1, 0x20)
    SetChrFlags(0x2F, 0x8000)
    SetChrFlags(0x30, 0x8000)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x2F, 4040, 0, -21980, 0)
    SetChrPos(0x30, -22270, -380, -4230, 90)
    SetChrPos(0x31, -19750, 0, 20850, 135)
    OP_D5(0x2F, 0x0, 0x0, 0x0, 0x0)
    OP_D5(0x30, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x31, 0x0, 0x20F58, 0x0, 0x0)
    OP_68(16840, 1900, -3910, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18430, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(8180, 1900, -4370, 2000)
    Sound(487, 0, 100, 0)

    def lambda_CEC3():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_CEC3)
    WaitChrThread(0x2E, 1)
    OP_71(0xF, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0xF)
    Sound(975, 2, 100, 0)
    OP_63(0x2E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x1)
    Sleep(200)
    Fade(500)
    OP_68(4140, 1520, -17770, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27440, 0)
    Sound(459, 0, 100, 0)
    Sound(492, 0, 100, 0)

    def lambda_CF55():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_CF55)
    OP_71(0xC, 0x5B, 0x78, 0x0, 0x0)
    OP_68(-17750, 1520, -3100, 4000)
    Sleep(1000)
    Sound(492, 0, 100, 0)
    OP_9F(0x0, 0x30)
    OP_9F(0x1, -22270, -380, -4230)
    OP_9F(0x1, -15910, 0, -4019)
    OP_9F(0x2, 0x30, 5000, 0x6)
    OP_71(0xD, 0x5B, 0x78, 0x0, 0x0)
    MoveCamera(60, 33, 0, 2000)
    Sleep(100)
    OP_68(-11170, 1520, 9140, 3000)

    def lambda_CFE4():
        OP_9B(0x1, 0xFE, 0x0, 0x2EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_CFE4)
    Sleep(1000)
    Sound(492, 0, 100, 0)
    WaitChrThread(0x31, 1)
    OP_71(0xE, 0x5B, 0x78, 0x0, 0x0)
    OP_6F(0x1)
    Sleep(1000)
    Fade(500)
    OP_68(9190, 1900, -2740, 0)
    MoveCamera(36, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18430, 0)

    #N0177
    NpcTalk(
        0x2E,
        "塞克斯",
        "#5P哼，区区杂鱼，竟然如此缠人！\x02",
    )

    CloseMessageWindow()

    #N0178
    NpcTalk(
        0x2E,
        "尤利",
        "#5P瑞吉，甩开他们！\x02",
    )

    CloseMessageWindow()

    #N0179
    NpcTalk(
        0x2E,
        "瑞吉",
        "#5P简单得很！\x02",
    )

    CloseMessageWindow()
    Sound(493, 0, 100, 0)
    OP_71(0xF, 0xB5, 0xF0, 0x1, 0x20)
    OP_9B(0x1, 0x2E, 0x0, 0xFFFFF830, 0x1388, 0x0)
    Sleep(200)
    OP_68(11190, 1900, 12940, 3000)
    MoveCamera(61, 33, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(20320, 3000)
    Sound(486, 0, 100, 0)
    OP_9F(0x0, 0x2E)
    OP_9F(0x1, 14290, 0, -3910)
    OP_9F(0x1, 10690, 0, -310)
    OP_9F(0x1, 10290, 0, 2350)
    OP_9F(0x2, 0x2E, 11000, 0x6)

    def lambda_D13B():
        OP_96(0x2E, 0x2F26, 0x0, 0x88B8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_D13B)
    Sleep(1500)
    StopSound(975, 1000, 100)
    Sleep(1000)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1100", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_102_CCDC end

    def Function_103_D16A(): pass

    label("Function_103_D16A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    OP_68(4270, -700, 10240, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D1C9")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_D208")

    label("loc_D1C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D1EB")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_D208")

    label("loc_D1EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D208")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_D208")

    OP_68(4310, -700, 10200, 3000)
    MoveCamera(39, 20, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(50260, 3000)
    Sound(835, 2, 80, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(9660, 1900, -4450, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12460, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D352")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x104, 15940, 0, -2710, 270)

    def lambda_D2E4():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D2E4)

    def lambda_D2FE():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D2FE)
    Sleep(100)

    def lambda_D31B():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D31B)
    Sleep(50)

    def lambda_D338():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D338)
    Jump("loc_D4F5")

    label("loc_D352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D426")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x109, 15940, 0, -2710, 270)

    def lambda_D3B8():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D3B8)

    def lambda_D3D2():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D3D2)
    Sleep(100)

    def lambda_D3EF():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D3EF)
    Sleep(50)

    def lambda_D40C():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D40C)
    Jump("loc_D4F5")

    label("loc_D426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D4F5")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x105, 15940, 0, -2710, 270)

    def lambda_D48C():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D48C)

    def lambda_D4A6():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D4A6)
    Sleep(100)

    def lambda_D4C3():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D4C3)
    Sleep(50)

    def lambda_D4E0():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D4E0)

    label("loc_D4F5")

    OP_68(9660, 1900, -4450, 3000)
    MoveCamera(47, 27, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(10500, 3000)
    OP_6F(0x79)
    WaitChrThread(0x1A2, 1)

    #C0180
    ChrTalk(
        0x1A2,
        "这里就是中央广场吗？\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x1A2,
        (
            "不愧是繁华街区，\x01",
            "果然很热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，秦要去的\x01",
            "『时代』百货店就在眼前了。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#00000F要直接进去吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0184
    ChrTalk(
        0x1A2,
        (
            "#6P嗯……无所谓，\x01",
            "全都由你们决定吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x1A2,
        (
            "#6P我只要能像现在这样\x01",
            "待在艾莉姐的身边，\x01",
            "就觉得很幸福了！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#00006F呼，真是的，\x01",
            "我们早就知道啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0187
    ChrTalk(
        0x102,
        "#00109F谢谢哦，秦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D6BB")
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    #C0188
    ChrTalk(
        0x104,
        (
            "#00302F好啦，总之我们就\x01",
            "随便转转吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D73A")

    label("loc_D6BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D6FD")
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    #C0189
    ChrTalk(
        0x109,
        (
            "#10102F好啦，那我们就\x01",
            "尽量多逛逛吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D73A")

    label("loc_D6FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D73A")
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    #C0190
    ChrTalk(
        0x105,
        (
            "#10302F好啦，总之我们就\x01",
            "随便逛逛吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D73A")

    StopSound(835, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_1B(0x0, 0x0, 0x6E)
    OP_1B(0x2, 0x0, 0x6F)
    OP_1B(0x3, 0x0, 0x70)
    OP_1B(0x4, 0x0, 0x71)
    ModifyEventFlags(1, 2, 0x80)
    SetScenarioFlags(0x154, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11440, 0, -3410, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_103_D16A end

    def Function_104_D789(): pass

    label("Function_104_D789")

    EventBegin(0x0)
    Fade(500)
    OP_68(-2150, 1900, -5340, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12200, 0)
    SetChrPos(0x101, -1290, 0, -4460, 0)
    SetChrPos(0x102, -2420, 0, -4740, 0)
    SetChrPos(0x104, -1390, 0, -5860, 0)
    SetChrPos(0x103, -220, 0, -4800, 0)
    SetChrPos(0x105, -20, 0, -6070, 0)
    SetChrPos(0x109, -2650, 0, -6050, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_93(0x14, 0xB4, 0x0)
    OP_93(0x15, 0xE1, 0x0)
    OP_0D()

    #C0191
    ChrTalk(
        0x14,
        (
            "啊，罗伊德，\x01",
            "你怎么慌慌张张的？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#00003F我们正在追捕\x01",
            "某个人……\x02\x03",

            "#00001F刚才有莱恩福尔特公司\x01",
            "制造的黑色运输车从这里通过吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x14,
        (
            "黑色运输车……？\x02\x03",

            "哦，听你这么一说……不久之前，\x01",
            "确实有一辆那样的车开了过去。\x02\x03",

            "我记得那辆车\x01",
            "驶向东街方向了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0194
    ChrTalk(
        0x102,
        (
            "#00105F东街吗……？\x02\x03",

            "并不是通往帝国\x01",
            "方向的西街吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x15,
        "嗯，我也看得很清楚。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x104,
        (
            "#00303F唔……如此看来，\x01",
            "他是逃向共和国方向了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x103,
        (
            "#00203F一名帝国人，驾驶着\x01",
            "莱恩福尔特公司制造的运输车……\x02\x03",

            "#00200F如果从常理来推测，自然会\x01",
            "认为他要逃至帝国方向……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x105,
        (
            "#10306F哎呀呀，看来是个\x01",
            "相当狡猾难缠的对手呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#00000F弗兰茨，多谢啦，\x01",
            "你真是帮了大忙。\x02\x03",

            "#00001F……我们最好尽快行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x109,
        (
            "#10103F嗯，如果要追，\x01",
            "还是开导力车\x01",
            "比较好。\x02\x03",

            "#10101F赶快赶往\x01",
            "唐古拉姆门吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x14,
        (
            "虽然不知道是怎么回事，\x01",
            "不过大家要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x15,
        "我在这里祝你们行动顺利！\x02",
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x1)
    SetScenarioFlags(0x19B, 7)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0x14, 0xB4, 0x0)
    OP_93(0x15, 0xB4, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1290, 0, -4460, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_104_D789 end

    def Function_105_DC25(): pass

    label("Function_105_DC25")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E28D")
    Fade(500)
    OP_68(-19610, -6700, -24820, 0)
    MoveCamera(9, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10990, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DD27")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x104, -18650, -8200, -21550, 225)

    def lambda_DCCD():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DCCD)

    def lambda_DCE2():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DCE2)
    Sleep(100)

    def lambda_DCFA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DCFA)
    Sleep(50)

    def lambda_DD12():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DD12)
    Jump("loc_DE7A")

    label("loc_DD27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DDD3")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x109, -18650, -8200, -21550, 225)

    def lambda_DD79():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DD79)

    def lambda_DD8E():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DD8E)
    Sleep(100)

    def lambda_DDA6():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DDA6)
    Sleep(50)

    def lambda_DDBE():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DDBE)
    Jump("loc_DE7A")

    label("loc_DDD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_DE7A")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x105, -18650, -8200, -21550, 225)

    def lambda_DE25():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DE25)

    def lambda_DE3A():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DE3A)
    Sleep(100)

    def lambda_DE52():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DE52)
    Sleep(50)

    def lambda_DE6A():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DE6A)

    label("loc_DE7A")

    OP_0D()
    WaitChrThread(0x101, 1)
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x1A2, 0x10E, 0x1F4)
    Sleep(300)

    #C0203
    ChrTalk(
        0x1A2,
        "#11P怎、怎么回事，那只大狗是……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1A2, 3, 0, 106)
    OP_68(-23520, -6700, -24320, 3000)
    MoveCamera(51, 18, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(13660, 3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DF3E")

    def lambda_DF0E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DF0E)
    Sleep(50)

    def lambda_DF1E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF1E)
    Sleep(50)

    def lambda_DF2E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DF2E)
    Sleep(300)
    Jump("loc_DFB5")

    label("loc_DF3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DF7C")

    def lambda_DF4C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DF4C)
    Sleep(50)

    def lambda_DF5C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF5C)
    Sleep(50)

    def lambda_DF6C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DF6C)
    Sleep(300)
    Jump("loc_DFB5")

    label("loc_DF7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_DFB5")

    def lambda_DF8A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DF8A)
    Sleep(50)

    def lambda_DF9A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF9A)
    Sleep(50)

    def lambda_DFAA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DFAA)
    Sleep(300)

    label("loc_DFB5")

    OP_6F(0x79)

    #C0204
    ChrTalk(
        0x101,
        "#00005F蔡特……待在那种地方啊。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，大概是想呼吸一下\x01",
            "外面的新鲜空气吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-21260, -6700, -23460, 3000)
    OP_9B(0x1, 0x1A2, 0x5A, 0x1F4, 0x3E8, 0x0)
    Sound(812, 0, 100, 0)
    OP_6F(0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0206
    ChrTalk(
        0x102,
        "#6P#00105F秦……你怎么了？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E0B7")
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    #C0207
    ChrTalk(
        0x104,
        (
            "#00309F哈哈～看来你\x01",
            "很害怕蔡特？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E172")

    label("loc_E0B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E133")
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    #C0208
    ChrTalk(
        0x109,
        (
            "#10102F啊哈哈，看来你\x01",
            "有些害怕蔡特啊。\x02\x03",

            "#10104F（其实我以前也很害怕，\x01",
            "  所以很理解他的心情。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E172")

    label("loc_E133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E172")
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    #C0209
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，看样子，\x01",
            "你很害怕蔡特呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E172")


    #C0210
    ChrTalk(
        0x1A2,
        "你、你在说什么……？\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x1A2,
        (
            "我、我可是\x01",
            "什么都、都不怕的！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x1A2, 0x3)
    Sleep(1000)
    OP_93(0x1A2, 0x2D, 0x1F4)
    Sleep(300)

    #C0212
    ChrTalk(
        0x1A2,
        (
            "好了，你们几个，这里已经没什么\x01",
            "可看的了，赶快带我去下一个地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#00000F嗯，知道啦。\x02\x03",

            "#00012F（哈哈，虽然只是在硬撑，\x01",
            "  但这种骨气倒是很值得佩服呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -17980, -8200, -22080, 44)
    SetScenarioFlags(0x1C5, 5)
    OP_29(0x73, 0x1, 0xB)
    Jump("loc_E2F8")

    label("loc_E28D")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    #C0214
    ChrTalk(
        0x1A2,
        (
            "喂、喂……那边已经没什么\x01",
            "可看的了，赶快回广场吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        "#00000F嗯，知道啦。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E2F8")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -17980, -8200, -22080, 44)
    EventEnd(0x4)
    Return()

    # Function_105_DC25 end

    def Function_106_E310(): pass

    label("Function_106_E310")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E340")

    def lambda_E320():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E320)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_106_E310")

    label("loc_E340")

    Return()

    # Function_106_E310 end

    def Function_107_E341(): pass

    label("Function_107_E341")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E6DA")
    OP_68(90, 4400, 25340, 0)
    MoveCamera(359, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16660, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E3F3")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x104, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_E492")

    label("loc_E3F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E445")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x109, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_E492")

    label("loc_E445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E492")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x105, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)

    label("loc_E492")

    OP_68(180, 4350, 26590, 3000)
    MoveCamera(359, 11, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(21260, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_68(10, 400, 21490, 3000)
    MoveCamera(0, 18, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(15710, 3000)
    OP_6F(0x79)

    #C0216
    ChrTalk(
        0x101,
        (
            "#00000F好啦，我们已经\x01",
            "到百货店了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E5B4")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0217
    ChrTalk(
        0x104,
        (
            "#00305F除了这里之外，\x01",
            "还想带这小鬼去其它地方吗？\x02\x03",

            "#00303F进入百货店以后，\x01",
            "大概就没时间\x01",
            "再带他去外面游览了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6AE")

    label("loc_E5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E63B")
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0218
    ChrTalk(
        0x109,
        (
            "#10105F除了这里之外，\x01",
            "还想带秦去别的地方吗？\x02\x03",

            "#10103F进入百货店之后，\x01",
            "应该就没时间\x01",
            "再带他去外边游览了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6AE")

    label("loc_E63B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E6AE")
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0219
    ChrTalk(
        0x105,
        (
            "#10300F除了这里之外，\x01",
            "还要带秦去其它地方吗？\x02\x03",

            "进去以后，\x01",
            "恐怕就没时间\x01",
            "再带他去外面游览了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6AE")


    #C0220
    ChrTalk(
        0x1A2,
        (
            "#6P如何？\x01",
            "全都交给你们决定吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 108)
    Jump("loc_E949")

    label("loc_E6DA")

    OP_68(10, 400, 21490, 0)
    MoveCamera(0, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15710, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E75A")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x104, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_E7F9")

    label("loc_E75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E7AC")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x109, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_E7F9")

    label("loc_E7AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E7F9")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x105, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)

    label("loc_E7F9")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E876")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0221
    ChrTalk(
        0x104,
        (
            "#00300F要进百货店吗？\x02\x03",

            "#00303F进入百货店以后，\x01",
            "大概就没时间\x01",
            "再带他去外面游览了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E944")

    label("loc_E876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E8E8")
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0222
    ChrTalk(
        0x109,
        (
            "#10100F要进入百货店吗？\x02\x03",

            "#10103F进入百货店之后，\x01",
            "应该就没时间\x01",
            "再带他去外边游览了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E944")

    label("loc_E8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E944")
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0223
    ChrTalk(
        0x105,
        (
            "#10300F要进百货店吗？\x02\x03",

            "进去以后，\x01",
            "恐怕就没时间\x01",
            "再带他去外面游览了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E944")

    Call(0, 108)
    EventEnd(0x5)

    label("loc_E949")

    Return()

    # Function_107_E341 end

    def Function_108_E94A(): pass

    label("Function_108_E94A")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "进入百货店\x01",              # 0
            "还要带秦去其它地方\x01",      # 1
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
        (0, "loc_E9B8"),
        (1, "loc_EA0B"),
        (SWITCH_DEFAULT, "loc_EA7D"),
    )


    label("loc_E9B8")

    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0224
    ChrTalk(
        0x101,
        (
            "#00000F这个嘛……\x01",
            "该去的地方应该都去过了，\x01",
            "我们这就进去吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 109)
    Jump("loc_EA7D")

    label("loc_EA0B")

    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0225
    ChrTalk(
        0x101,
        (
            "#00003F这个嘛……也许还有些\x01",
            "值得一去的地方。\x02\x03",

            "#00000F我们还是稍后再进百货店吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C5, 6)
    Jump("loc_EA7D")

    label("loc_EA7D")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -180, 0, 15990, 180)
    EventEnd(0x5)
    Return()

    # Function_108_E94A end

    def Function_109_EA95(): pass

    label("Function_109_EA95")

    LoadChrToIndex("chr/ch00300.itc", 0x1E)
    LoadChrToIndex("chr/ch02900.itc", 0x1F)
    LoadChrToIndex("chr/ch03000.itc", 0x20)

    #C0226
    ChrTalk(
        0x1A2,
        "#6P好，就这么决定了！\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x102,
        (
            "#12P#00100F呵呵，那我们就\x01",
            "赶快进去吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-13670, 1900, 7350, 0)
    MoveCamera(22, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14280, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EBB9")
    SetChrChipByIndex(0x36, 0x1F)
    SetChrChipByIndex(0x37, 0x20)
    SetChrSubChip(0x36, 0x0)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x36, -16070, 0, 6000, 45)
    SetChrPos(0x37, -16550, 0, 7310, 45)
    SetChrPos(0x1A2, -350, 800, 24290, 0)
    SetChrPos(0x102, 500, 800, 24290, 0)
    SetChrPos(0x101, -1000, 800, 25780, 0)
    SetChrPos(0x104, 980, 800, 25780, 0)
    Jump("loc_ECE4")

    label("loc_EBB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EC51")
    SetChrChipByIndex(0x35, 0x1E)
    SetChrChipByIndex(0x37, 0x20)
    SetChrSubChip(0x35, 0x0)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x35, 0x8000)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x35, -16550, 0, 7310, 45)
    SetChrPos(0x37, -16070, 0, 6000, 45)
    SetChrPos(0x1A2, -350, 800, 24290, 0)
    SetChrPos(0x102, 500, 800, 24290, 0)
    SetChrPos(0x101, -1000, 800, 25780, 0)
    SetChrPos(0x109, 980, 800, 25780, 0)
    Jump("loc_ECE4")

    label("loc_EC51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_ECE4")
    SetChrChipByIndex(0x35, 0x1E)
    SetChrChipByIndex(0x36, 0x1F)
    SetChrSubChip(0x35, 0x0)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x35, 0x8000)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x35, -16550, 0, 7310, 45)
    SetChrPos(0x36, -16070, 0, 6000, 45)
    SetChrPos(0x1A2, -350, 800, 24290, 0)
    SetChrPos(0x102, 500, 800, 24290, 0)
    SetChrPos(0x101, -1000, 800, 25780, 0)
    SetChrPos(0x105, 980, 800, 25780, 0)

    label("loc_ECE4")

    OP_0D()
    Sound(100, 0, 40, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EDB5")

    def lambda_ED11():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ED11)
    Sleep(100)

    def lambda_ED29():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ED29)
    Sleep(500)

    def lambda_ED41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ED41)
    Sleep(200)

    def lambda_ED55():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_ED55)

    def lambda_ED66():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_ED66)

    def lambda_ED7B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ED7B)
    Sleep(1000)

    def lambda_ED93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_ED93)

    def lambda_EDA4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EDA4)
    Jump("loc_EF14")

    label("loc_EDB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EE67")

    def lambda_EDC3():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EDC3)
    Sleep(100)

    def lambda_EDDB():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EDDB)
    Sleep(500)

    def lambda_EDF3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EDF3)
    Sleep(200)

    def lambda_EE07():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_EE07)

    def lambda_EE18():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_EE18)

    def lambda_EE2D():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EE2D)
    Sleep(1000)

    def lambda_EE45():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_EE45)

    def lambda_EE56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EE56)
    Jump("loc_EF14")

    label("loc_EE67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EF14")

    def lambda_EE75():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EE75)
    Sleep(100)

    def lambda_EE8D():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EE8D)
    Sleep(500)

    def lambda_EEA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EEA5)
    Sleep(200)

    def lambda_EEB9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_EEB9)

    def lambda_EECA():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_EECA)

    def lambda_EEDF():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EEDF)
    Sleep(1000)

    def lambda_EEF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_EEF7)

    def lambda_EF08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EF08)

    label("loc_EF14")

    WaitChrThread(0x102, 1)
    Sound(100, 0, 40, 0)
    OP_71(0x4, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F0BE")

    #C0228
    ChrTalk(
        0x36,
        (
            "#10100F嗯，看来他们\x01",
            "已经进店了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x37,
        "#10303F………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x36, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x36, 0x37, 500)
    Sleep(300)

    #C0230
    ChrTalk(
        0x36,
        "#11P#10105F怎么了？瓦吉。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x37,
        (
            "#10301F哦，在警戒他们身后时，\x01",
            "似乎感觉到了某种气息。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x36,
        (
            "#11P#10105F气息……\x01",
            "莫非是黑月的人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x37,
        (
            "#10303F嗯，那应该是\x01",
            "最有可能的……\x02\x03",

            "#10300F但具体是什么人，\x01",
            "实在是猜不到呢。\x02\x03",

            "总之，我们稍后\x01",
            "也进入百货店吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x36,
        "#10103F嗯、嗯……知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F46E")

    label("loc_F0BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F2CD")

    #C0235
    ChrTalk(
        0x37,
        (
            "#10300F嗯，看来他们\x01",
            "已经进店了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x35,
        "#00303F………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x37, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x37, 0x35, 500)
    Sleep(300)

    #C0237
    ChrTalk(
        0x37,
        "#11P#10305F怎么了？兰迪。\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x35,
        (
            "#00301F哦，在警戒他们身后时，\x01",
            "似乎感觉到了某种气息。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x37,
        (
            "#11P#10304F呵呵，你也感觉到了啊……\x01",
            "其实我也察觉到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x35,
        (
            "#00303F嗯，恐怕是黑月的人\x01",
            "在跟踪监视吧……\x02\x03",

            "#00301F不过……该怎么说呢，\x01",
            "总觉得似乎没有那么简单呢。\x02\x03",

            "#00306F算了，具体是怎么回事，\x01",
            "谁也猜不到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x37,
        (
            "#11P#10304F呵呵，我的看法和你一样。\x02\x03",

            "#10300F总之，我们现在也只能\x01",
            "继续观望一阵子了。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x35,
        "#00303F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F46E")

    label("loc_F2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F46E")

    #C0243
    ChrTalk(
        0x36,
        (
            "#10100F嗯，看来他们\x01",
            "已经进店了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x35,
        "#00303F………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x36, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x36, 0x35, 500)
    Sleep(300)

    #C0245
    ChrTalk(
        0x36,
        "#11P#10105F怎么了？兰迪前辈。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x35,
        (
            "#00301F哦，在警戒他们身后时，\x01",
            "似乎感觉到了某种气息。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x36,
        (
            "#11P#10101F气息……\x01",
            "莫非是黑月的人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x35,
        (
            "#00303F嗯，那应该是\x01",
            "最有可能的……\x02\x03",

            "#00306F至于具体是什么人，\x01",
            "老实说，实在是猜不到呢。\x02\x03",

            "#00300F总之，再过一会，\x01",
            "我们也进入百货店吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x36,
        "#10101F嗯、嗯……知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_F46E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0170", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_109_EA95 end

    def Function_110_F486(): pass

    label("Function_110_F486")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F52F")

    #C0250
    ChrTalk(
        0x1A2,
        (
            "哎，百货店\x01",
            "是在那边吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#00000F啊，不，\x01",
            "这边是车站……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0252
    ChrTalk(
        0x1A2,
        "那就赶快回去啊。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#00005F啊……嗯……抱歉。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_F55D")

    label("loc_F52F")


    #C0254
    ChrTalk(
        0x101,
        (
            "#00000F没必要去站前街道，\x01",
            "还是回广场吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F55D")

    SetChrPos(0x0, 3740, 0, -19810, 0)
    EventEnd(0x4)
    Return()

    # Function_110_F486 end

    def Function_111_F571(): pass

    label("Function_111_F571")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F61F")
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0255
    ChrTalk(
        0x102,
        (
            "#00105F喂，罗伊德……\x01",
            "往这边走就是行政区了哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0256
    ChrTalk(
        0x101,
        "#00000F是啊，还是回去吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x1A2,
        "百货店不在这边吗？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_F63C")

    label("loc_F61F")


    #C0258
    ChrTalk(
        0x101,
        "#00000F这边是行政区哦。\x02",
    )

    CloseMessageWindow()

    label("loc_F63C")

    SetChrPos(0x0, 13290, 0, 26680, 180)
    EventEnd(0x4)
    Return()

    # Function_111_F571 end

    def Function_112_F650(): pass

    label("Function_112_F650")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F721")
    TurnDirection(0x1A2, 0x0, 500)
    Sleep(300)

    #C0259
    ChrTalk(
        0x1A2,
        "这条街……\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x1A2,
        (
            "莫非前面就是\x01",
            "后巷了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        "#00000F是啊，你竟然连这都知道啊。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x102,
        (
            "#00103F……不过我们\x01",
            "不需要去这边哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x1A2,
        (
            "（嗯……曹他们所说的\x01",
            "  鲁巴彻旧址就在前方……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F73E")

    label("loc_F721")


    #C0264
    ChrTalk(
        0x101,
        "#00000F没必要去后巷哦。\x02",
    )

    CloseMessageWindow()

    label("loc_F73E")

    SetChrPos(0x0, -14110, -10, 14420, 135)
    EventEnd(0x4)
    Return()

    # Function_112_F650 end

    def Function_113_F752(): pass

    label("Function_113_F752")

    EventBegin(0x1)

    #C0265
    ChrTalk(
        0x101,
        (
            "#00000F前方是西街。\x02\x03",

            "#00003F我们的目标是百货店，\x01",
            "不要越走越远，\x01",
            "还是回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)
    Return()

    # Function_113_F752 end

    SaveToFile()

Try(main)
