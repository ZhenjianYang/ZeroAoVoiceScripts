from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "クロマ",                 # 1
        "オットー",               # 2
        "タジク",                 # 3
        "フランツ巡査",           # 4
        "ツァイト",               # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "市民",                   # 8
        "男の子",                 # 9
        "市民",                   # 10
        "市民",                   # 11
        "ハース",                 # 12
        "国防軍兵士",             # 13
        "国防軍兵士",             # 14
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
        "観光客",                 # 25
        "観光客",                 # 26
        "モモ",                   # 27
        "リュウ",                 # 28
        "アンリ",                 # 29
        "魔導兵",                 # 30
        "魔導兵",                 # 31
        "遊撃士スコット",         # 32
        "遊撃士ヴェンツェル",     # 33
        "遊撃士リン",             # 34
        "遊撃士エオリア",         # 35
        "イベント用モンスター",   # 36
        "イベント用モンスター",   # 37
        "イベント用モンスター",   # 38
        "ケイト巡査",             # 39
        "ユーリ",                 # 40
        "サイクス",               # 41
        "レジー",                 # 42
        "パトカー",               # 43
        "パトカー",               # 44
        "パトカー",               # 45
        "パトカー",               # 46
        "暴走車",                 # 47
        "車",                     # 48
        "土嚢",                   # 49
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
        "SE制御",                 # 63
        "bc1100",                 # 64
        "中央広場",               # 65
        "西通り",                 # 66
        "行政区",                 # 67
        "住宅街",                 # 68
        "歓楽街",                 # 69
        "東通り",                 # 70
        "旧市街",                 # 71
        "港湾区",                 # 72
        "ＩＢＣ",                 # 73
        "駅前通り",               # 74
        "裏通り",                 # 75
        "ウルスラ間道",           # 76
        "東クロスベル街道",       # 77
        "西クロスベル街道",       # 78
        "マインツ山道",           # 79
        "オルキスタワー",         # 80
    ))

    ATBonus("ATBonus_BF0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_C52E", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_CC0", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc1100", "Sepith_C52E", 60, 30, 10, 0,
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

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "中央広場")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "西通り")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "行政区")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "住宅街")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "歓楽街")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "東通り")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "旧市街")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "港湾区")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "駅前通り")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "裏通り")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-175.5, 0.0, 26.0, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-5.0, 0.0, 178.0, 0x0000, 0x0000, "オルキスタワー")
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
        "Function_10_31C0",        # 0A, 10
        "Function_11_3FFB",        # 0B, 11
        "Function_12_41FD",        # 0C, 12
        "Function_13_50A5",        # 0D, 13
        "Function_14_5375",        # 0E, 14
        "Function_15_578E",        # 0F, 15
        "Function_16_5798",        # 10, 16
        "Function_17_57A2",        # 11, 17
        "Function_18_57AC",        # 12, 18
        "Function_19_5C35",        # 13, 19
        "Function_20_5FFA",        # 14, 20
        "Function_21_61DF",        # 15, 21
        "Function_22_62CA",        # 16, 22
        "Function_23_63BD",        # 17, 23
        "Function_24_64B4",        # 18, 24
        "Function_25_657B",        # 19, 25
        "Function_26_65EB",        # 1A, 26
        "Function_27_66F5",        # 1B, 27
        "Function_28_67D1",        # 1C, 28
        "Function_29_6D94",        # 1D, 29
        "Function_30_70FF",        # 1E, 30
        "Function_31_71F3",        # 1F, 31
        "Function_32_72A4",        # 20, 32
        "Function_33_730A",        # 21, 33
        "Function_34_736C",        # 22, 34
        "Function_35_73E9",        # 23, 35
        "Function_36_7436",        # 24, 36
        "Function_37_747B",        # 25, 37
        "Function_38_74F0",        # 26, 38
        "Function_39_7526",        # 27, 39
        "Function_40_7678",        # 28, 40
        "Function_41_7F23",        # 29, 41
        "Function_42_8687",        # 2A, 42
        "Function_43_89EB",        # 2B, 43
        "Function_44_8A31",        # 2C, 44
        "Function_45_8E9E",        # 2D, 45
        "Function_46_8F55",        # 2E, 46
        "Function_47_8F9A",        # 2F, 47
        "Function_48_8FD5",        # 30, 48
        "Function_49_969F",        # 31, 49
        "Function_50_9764",        # 32, 50
        "Function_51_9845",        # 33, 51
        "Function_52_9874",        # 34, 52
        "Function_53_989D",        # 35, 53
        "Function_54_99B0",        # 36, 54
        "Function_55_9AAC",        # 37, 55
        "Function_56_9BCC",        # 38, 56
        "Function_57_9C31",        # 39, 57
        "Function_58_9C60",        # 3A, 58
        "Function_59_9C85",        # 3B, 59
        "Function_60_9D0A",        # 3C, 60
        "Function_61_A818",        # 3D, 61
        "Function_62_A938",        # 3E, 62
        "Function_63_A997",        # 3F, 63
        "Function_64_A9C7",        # 40, 64
        "Function_65_A9F7",        # 41, 65
        "Function_66_B7B1",        # 42, 66
        "Function_67_B819",        # 43, 67
        "Function_68_B891",        # 44, 68
        "Function_69_BAE2",        # 45, 69
        "Function_70_C38A",        # 46, 70
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31BC")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2288")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2288")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A8")
    OP_AF(0x80)
    Jump("loc_22AA")

    label("loc_22A8")

    OP_AF(0x81)

    label("loc_22AA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31B7")

    label("loc_22B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22CD")
    Jump("loc_31B7")

    label("loc_22CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31B7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2380")

    #C0001
    ChrTalk(
        0xFE,
        (
            "うーん、にがトマトソーダには\x01",
            "まだまだ改良の余地がありそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "万人が楽しめる美味しいジュースを\x01",
            "作るためにも、頑張りませんと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B7")

    label("loc_2380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2450")

    #C0003
    ChrTalk(
        0xFE,
        "皆さん、お疲れ様でーす！\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "当店のオリジナルではありませんが、\x01",
            "疲れた身体には、『スポリタンＸ』が\x01",
            "オススメですよー！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "エネルギーをばっちり充填して\x01",
            "頑張っていきましょー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24DE")

    label("loc_2450")


    #C0006
    ChrTalk(
        0xFE,
        (
            "さっき連絡があって……\x01",
            "百貨店のお母さんも\x01",
            "無事みたいでよかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "さあ、みなさんも\x01",
            "スポリタンパワーで\x01",
            "元気を出していきましょう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24DE")

    Jump("loc_31B7")

    label("loc_24E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_24F1")
    Jump("loc_31B7")

    label("loc_24F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2544")

    #C0008
    ChrTalk(
        0xFE,
        (
            "皆さん、凄い熱気ですね……\x01",
            "何だか少し怖いくらいかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B7")

    label("loc_2544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_26B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2614")

    #C0009
    ChrTalk(
        0xFE,
        "皆さん、お疲れ様でーす！\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "当店のオリジナルではありませんが、\x01",
            "疲れた身体には、『スポリタンＸ』が\x01",
            "オススメですよー！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "エネルギーをばっちり充填して\x01",
            "頑張っていきましょー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26AB")

    label("loc_2614")


    #C0012
    ChrTalk(
        0xFE,
        (
            "当店のオリジナルではありませんが、\x01",
            "疲れた身体には、『スポリタンＸ』が\x01",
            "オススメですよー！\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "エネルギーをばっちり充填して\x01",
            "頑張っていきましょー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26AB")

    Jump("loc_31B7")

    label("loc_26B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_281D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278B")

    #C0014
    ChrTalk(
        0xFE,
        (
            "マインツの占拠事件、\x01",
            "本当に恐ろしい話ですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "それを受けてか、\x01",
            "今朝から独立の議論も活発に\x01",
            "なっているみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "正直、どう判断すればいいのか\x01",
            "私にはまだ判らないです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2818")

    label("loc_278B")


    #C0017
    ChrTalk(
        0xFE,
        (
            "占拠事件を受けてか、\x01",
            "今朝から独立の議論も活発に\x01",
            "なっているみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "正直、どう判断すればいいのか\x01",
            "私にはまだ判らないです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2818")

    Jump("loc_31B7")

    label("loc_281D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_282B")
    Jump("loc_31B7")

    label("loc_282B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_294C")

    #C0019
    ChrTalk(
        0xFE,
        (
            "さっきから警察の人たちが\x01",
            "慌しくしているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "また何か事件でも\x01",
            "起こったのでしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2947")

    #C0021
    ChrTalk(
        0x101,
        (
            "#00008F（ここでグルメガイドの取材が\x01",
            "  出来そうだけど……）\x02\x03",

            "#00003F（今はそれどころじゃない。\x01",
            "  後で忘れずに来るとしよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2947")

    Jump("loc_31B7")

    label("loc_294C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A79")

    #C0022
    ChrTalk(
        0xFE,
        (
            "ジュース屋を始めて\x01",
            "そろそろ１年くらい経つんですが、\x01",
            "おかげ様で売り上げが順調なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "徐々に認知を頂いているのと、\x01",
            "最近は“期間限定”を取り入れたのが\x01",
            "特に功を奏したみたいでして。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "ふふ、私もそうですけど、\x01",
            "どうして人って限定と名の付く物に\x01",
            "弱いんでしょうかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2B02")

    label("loc_2A79")


    #C0025
    ChrTalk(
        0xFE,
        (
            "新メニューを\x01",
            "期間限定で売り出すのは、\x01",
            "母の提案だったんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "母は根っからの商売人ですね。\x01",
            "いつも勉強させられてばかりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B02")

    Jump("loc_31B7")

    label("loc_2B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C11")

    #C0027
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませー！\x01",
            "新鮮なジュースはいかがですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "今なら、話題の国家独立をテーマに\x01",
            "クロスベルの特産品のみを使用した\x01",
            "限定メニューもございまーす。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "クロスベルの旨みが\x01",
            "凝縮された究極の一杯を\x01",
            "ぜひ一度、ご賞味くださいませー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CBA")

    label("loc_2C11")


    #C0030
    ChrTalk(
        0xFE,
        (
            "今なら、話題の国家独立をテーマに\x01",
            "クロスベルの特産品のみを使用した\x01",
            "限定メニューもございまーす。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "自治州の旨みが凝縮された一杯を\x01",
            "ぜひ一度、ご賞味くださいませー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CBA")

    Jump("loc_31B7")

    label("loc_2CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DAB")

    #C0032
    ChrTalk(
        0xFE,
        (
            "今日は本会議とだけあって、\x01",
            "オルキスタワー方面は\x01",
            "封鎖されているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "私もちょっと\x01",
            "様子を見に行こうと\x01",
            "思っていたので残念です。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "でもまあ、安全のことを考えると\x01",
            "当たり前なんでしょうけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E4F")

    label("loc_2DAB")


    #C0035
    ChrTalk(
        0xFE,
        (
            "今日は本会議とだけあって、\x01",
            "オルキスタワー方面は\x01",
            "封鎖されているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "安全のことを考えると\x01",
            "当たり前なんでしょうけど、\x01",
            "一市民としては少し残念です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E4F")

    Jump("loc_31B7")

    label("loc_2E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F12")

    #C0037
    ChrTalk(
        0xFE,
        (
            "午前中は流石にこの辺りも\x01",
            "人でごった返しでしたけど、\x01",
            "ようやく落ち着いてきましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "ふふ、でもおかげ様で\x01",
            "今日は既に、いつもの売り上げの\x01",
            "平均を超えさせてもらいました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B7")

    label("loc_2F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2FAD")

    #C0039
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませー！\x01",
            "新鮮なジュースはいかがですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "今なら、明日からの\x01",
            "通商会議をイメージした\x01",
            "特別メニューもご提供できますよー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B7")

    label("loc_2FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FBB")
    Jump("loc_31B7")

    label("loc_2FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_31B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3037")

    #C0041
    ChrTalk(
        0xFE,
        (
            "な、なんだか\x01",
            "すごい捕り物でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "ふふ、警察のみなさんも\x01",
            "がんばってるみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B7")

    label("loc_3037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312F")

    #C0043
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませー！\x01",
            "新鮮なジュースはいかがですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "今なら、変り種の輸入食材を使用した\x01",
            "期間限定メニューもございまーす。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "このチャンスを逃すと後には\x01",
            "味わえない、新感覚のフレーバーを\x01",
            "ぜひ一度、ご賞味くださいませー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_31B7")

    label("loc_312F")


    #C0046
    ChrTalk(
        0xFE,
        (
            "今なら、変り種の輸入食材を使用した\x01",
            "期間限定メニューもございまーす。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "販売が終了してしまう前に\x01",
            "ぜひ一度、ご賞味くださいませー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B7")

    Jump("loc_222A")

    label("loc_31BC")

    TalkEnd(0xFE)
    Return()

    # Function_9_21E6 end

    def Function_10_31C0(): pass

    label("Function_10_31C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3309")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_329E")

    #C0048
    ChrTalk(
        0xFE,
        "クロスベルに訪れた異常事態……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "うぉっほん、\x01",
            "こういう時こそ市民の心を\x01",
            "一つにしなければならんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "負けるな～、クロスベル！\x01",
            "ガンバレ～、マクダエル議長！\x01",
            "……さあ、諸君もご一緒に。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3304")

    label("loc_329E")


    #C0051
    ChrTalk(
        0xFE,
        (
            "うぉっほん……\x01",
            "さあ、諸君もご一緒に。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "負けるな～、クロスベル！\x01",
            "ガンバレ～、マクダエル議長！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3304")

    Jump("loc_3FF7")

    label("loc_3309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3317")
    Jump("loc_3FF7")

    label("loc_3317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3373")

    #C0053
    ChrTalk(
        0xFE,
        "ディーター大統領、バンザ～イ！！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "帝国を、そして共和国を許すな～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FF7")

    label("loc_3373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3461")

    #C0055
    ChrTalk(
        0xFE,
        (
            "今も目に焼きついて離れん……\x01",
            "まさか、イリア様があのような形で……！\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "うむむ……許すまじ武装集団っ！\x01",
            "そして許すまじ、帝国政府っっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "こうなれば、我々は断固独立して\x01",
            "徹底抗戦するしかあるまいっ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34EB")

    label("loc_3461")


    #C0058
    ChrTalk(
        0xFE,
        (
            "うむむ……許すまじ武装集団っ！\x01",
            "そして許すまじ、帝国政府っっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "こうなれば、我々は断固独立して\x01",
            "徹底抗戦するしかあるまいっ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34EB")

    Jump("loc_3FF7")

    label("loc_34F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B9")

    #C0060
    ChrTalk(
        0xFE,
        (
            "ふむ、鉱山町で事件とな。\x01",
            "こんな時に全くイヤになるね……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "……とにかく、今日は待ちに待った\x01",
            "リニューアル舞台の公開日なんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "目一杯、楽しませてもらうつもりだよ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_361C")

    label("loc_35B9")


    #C0063
    ChrTalk(
        0xFE,
        (
            "今日は待ちに待った\x01",
            "リニューアル舞台の公開日なんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "目一杯、楽しませてもらうつもりだよ！\x02",
    )

    CloseMessageWindow()

    label("loc_361C")

    Jump("loc_3FF7")

    label("loc_3621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3737")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36DD")

    #C0065
    ChrTalk(
        0xFE,
        (
            "ついに、ついに明日には\x01",
            "リニューアル公演が……！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "興奮を抑えきれんが……\x01",
            "……ふむ、この雨は\x01",
            "火照った身体にちょうどいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "何とか冷静を保てそうだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3732")

    label("loc_36DD")


    #C0068
    ChrTalk(
        0xFE,
        (
            "……ふむ、この雨は\x01",
            "火照った身体にちょうどいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "何とか冷静を保てそうだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_3732")

    Jump("loc_3FF7")

    label("loc_3737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_387C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381E")

    #C0070
    ChrTalk(
        0xFE,
        (
            "『金の太陽、銀の月』の\x01",
            "リニューアル公演まであと２日……！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "えーっと、時間にするとどのくらいだ。\x01",
            "当日は夕方公演だから……\x01",
            "確実に４８時間以上はあるのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "そわそわ……\x01",
            "う～む、辛抱たまらんっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3877")

    label("loc_381E")


    #C0073
    ChrTalk(
        0xFE,
        (
            "そわそわ……\x01",
            "一刻も早く明後日になって欲しいものだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "う～む、辛抱たまらんっ！\x02",
    )

    CloseMessageWindow()

    label("loc_3877")

    Jump("loc_3FF7")

    label("loc_387C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_38E7")

    #C0075
    ChrTalk(
        0xFE,
        (
            "『金の太陽、銀の月』の\x01",
            "リニューアル公演まであと２日……！\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "ふむ、辛抱たまらんぞ！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FF7")

    label("loc_38E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39BC")

    #C0077
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの\x01",
            "リニューアル公演が\x01",
            "いよいよ３日後に迫ったな！\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "そして実はなんと……\x01",
            "今回は運良く初回公演のチケットが\x01",
            "手に入ったんだっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        "ふむ、楽しみ過ぎて仕方がないぞ！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A4D")

    label("loc_39BC")


    #C0080
    ChrTalk(
        0xFE,
        (
            "それにしても先日の配役の\x01",
            "追加発表には驚かされたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "シュリ・アトレイド……\x01",
            "弱冠１３歳にして、早くも大役を\x01",
            "演じるなんて全く恐れ入るよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A4D")

    Jump("loc_3FF7")

    label("loc_3A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B5A")

    #C0082
    ChrTalk(
        0xFE,
        (
            "確か午後からだったか。\x01",
            "いよいよ、オルキスタワーで\x01",
            "本会議が開かれるわけだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "ふむ、よりよい会議になるために\x01",
            "声援でも送るとしようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "#4Sディーター市長～……っ！\x01",
            "我々市民はあなたを\x01",
            "心より応援していますぞ～っ！！#3S\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BB9")

    label("loc_3B5A")


    #C0085
    ChrTalk(
        0xFE,
        "どれ、もう一つ……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "#4Sマクダエル議長～……っ！\x01",
            "市長と共に頑張ってくだされ～っ！！#3S\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB9")

    Jump("loc_3FF7")

    label("loc_3BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C86")

    #C0087
    ChrTalk(
        0xFE,
        (
            "オルキスタワー……！\x01",
            "何て優美で壮大なんだ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "この街のことが\x01",
            "ますます好きになってしまうな！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "これでまた１つ、このクロスベルに\x01",
            "新たな名所が加わったわけだな！\x01",
            "結構、結構！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FF7")

    label("loc_3C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3DF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7B")

    #C0090
    ChrTalk(
        0xFE,
        (
            "ふむ、各国の首脳たちが\x01",
            "このクロスベルにやって来るのは\x01",
            "いよいよ明日というわけだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "それに明日はオルキスタワーの\x01",
            "除幕式が行われる日でもある。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "いやはや、そんなことを考えると\x01",
            "興奮して今夜は眠れなさそうだ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3DED")

    label("loc_3D7B")


    #C0093
    ChrTalk(
        0xFE,
        (
            "ふむ、明日のことを考えると\x01",
            "興奮して今夜は\x01",
            "眠れなさそうな気がするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "いっそのこと、徹夜してしまおうか。\x02",
    )

    CloseMessageWindow()

    label("loc_3DED")

    Jump("loc_3FF7")

    label("loc_3DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3E6D")

    #C0095
    ChrTalk(
        0xFE,
        (
            "おはよう、今日はあいにく雨だが\x01",
            "たまにはこんな日があってもいいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "ふむ、クロスベルはやはり最高だ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FF7")

    label("loc_3E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F17")

    #C0097
    ChrTalk(
        0xFE,
        (
            "君たち、さっきの\x01",
            "土嚢を組んだ手際は\x01",
            "なかなか良かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "最初は何をしているのかと\x01",
            "首を傾げたものだったが……\x01",
            "ウム、アッパレだ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FF7")

    label("loc_3F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F86")

    #C0099
    ChrTalk(
        0xFE,
        "おはよう、今日も素晴らしい天気だね。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "まさに最高の散歩日和だよ。\x01",
            "いや、結構、結構！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FF7")

    label("loc_3F86")


    #C0101
    ChrTalk(
        0xFE,
        "私はクロスベルの街並みが大好きだ。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "物騒な話を聞くこともよくあるが、\x01",
            "それでも私はこの街を愛しているよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF7")

    TalkEnd(0xFE)
    Return()

    # Function_10_31C0 end

    def Function_11_3FFB(): pass

    label("Function_11_3FFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_41F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_408A")

    #C0103
    ChrTalk(
        0xFE,
        (
            "捕まったヤツの車……\x01",
            "やたらと高そうだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "ありゃ、ヴェルヌの最新型か？\x01",
            "これだから金持ちはよ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F9")

    label("loc_408A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4143")

    #C0105
    ChrTalk(
        0xFE,
        (
            "教団事件ってのが起こって以来、\x01",
            "議会もすっかり変わったよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "オレたち財務課が忙しいのは\x01",
            "相変わらずだが、以前に比べると\x01",
            "のびのび仕事をやらしてもらってるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_41F9")

    label("loc_4143")


    #C0107
    ChrTalk(
        0xFE,
        (
            "何より、帝国と共和国に\x01",
            "どっぷり浸かってた議員連中が\x01",
            "一掃されたのが大きいよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "かといって、両国の意向を\x01",
            "無視できるってわけでもないが……\x01",
            "この差には歴然たるものがあるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F9")

    TalkEnd(0xFE)
    Return()

    # Function_11_3FFB end

    def Function_12_41FD(): pass

    label("Function_12_41FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4404")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4385")

    #C0109
    ChrTalk(
        0xFE,
        (
            "あの大きな樹は一体何なんだ……？\x01",
            "何やら青白く光ってるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "ここ最近信じられない事が\x01",
            "何度も続いてたけど、\x01",
            "あれは輪を掛けて不気味だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "……お前ら、ホントにあんなのに\x01",
            "飛び込んでいくつもりなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00003F……ああ。\x01",
            "今更引くわけにもいかないからな。\x02\x03",

            "#00000F市内は頼んだぞ、フランツ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "あ、ああ、任せてくれ。\x01",
            "……お前らも気をつけてな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43FF")

    label("loc_4385")


    #C0114
    ChrTalk(
        0xFE,
        (
            "今は各人が自分のできることを\x01",
            "やっていかないと、だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "とにかく、ここは任せてくれ。\x01",
            "……お前らも気をつけてな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43FF")

    Jump("loc_50A1")

    label("loc_4404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4412")
    Jump("loc_50A1")

    label("loc_4412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4420")
    Jump("loc_50A1")

    label("loc_4420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_442E")
    Jump("loc_50A1")

    label("loc_442E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_443C")
    Jump("loc_50A1")

    label("loc_443C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_45B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_451D")

    #C0116
    ChrTalk(
        0xFE,
        (
            "今朝には完全復旧とは……\x01",
            "警備隊もやるよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "警察と同じで警備隊も最近は\x01",
            "過小評価されがちだけど、\x01",
            "実際はかなり大したもんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "昨日、現場で働く姿を見ていて\x01",
            "マジで勇気をもらったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45B0")

    label("loc_451D")


    #C0119
    ChrTalk(
        0xFE,
        (
            "警察と同じで警備隊も最近は\x01",
            "過小評価されがちだけど、\x01",
            "実際はかなり大したもんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "昨日、現場で働く姿を見ていて\x01",
            "マジで勇気をもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B0")

    Jump("loc_50A1")

    label("loc_45B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_45C3")
    Jump("loc_50A1")

    label("loc_45C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4658")

    #C0121
    ChrTalk(
        0xFE,
        (
            "何か最近、市外のあちこちに\x01",
            "《幻獣》ってのが現れるらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "倒すとフッと\x01",
            "消えちまうなんて聞いたが……\x01",
            "気味の悪いの話だよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50A1")

    label("loc_4658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A56")

    #C0123
    ChrTalk(
        0xFE,
        (
            "通商会議のテロ騒動は、\x01",
            "クロスベル警察にとって\x01",
            "本当に散々だったよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "最近少しは改善が見られていた\x01",
            "警察全体の信頼も元通り失墜……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "こうやって街中に立ってるとさ、\x01",
            "ほんと風当たりが\x01",
            "強くなったことを実感するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "もっとも、ロイドたち\x01",
            "特務支援課は別だけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#00006Fああいや……\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        (
            "#00108Fけど、風当たりって、\x01",
            "そんなに顕著なんですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "とりあえず、巡回中とかに\x01",
            "浴びせられる罵声のトーンは\x01",
            "明らかに以前以上かな。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "『意味のない警戒ご苦労さん』とか。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "『お前らが無能だから\x01",
            "  ２大国が付け上がるんだ』とか。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "決して否定はできないんだが、\x01",
            "必要以上に叩かれるのも\x01",
            "何かやるせないっていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        (
            "#00206Fなるほど……\x01",
            "確かになかなか辛辣ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#00303Fまあ、だがどう思われようと\x01",
            "俺たちは俺たちにやれることを\x01",
            "やるしかねえだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x109,
        (
            "#10101Fええ、それに\x01",
            "たとえちっぽけな力でも\x01",
            "あるのとないのとじゃ大違いですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x105,
        (
            "#10302Fふふ、だからあんまり風評を\x01",
            "気にすることはないんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "はは……確かにそうかもね。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "ありがとう。\x01",
            "何かちょっとスッキリしたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 5)
    Jump("loc_4AD8")

    label("loc_4A56")


    #C0139
    ChrTalk(
        0xFE,
        (
            "俺たちは俺たちにやれることを\x01",
            "やるしかない、確かにそうだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "腐ってても仕方ないし……\x01",
            "また気合い入れて頑張らないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD8")

    Jump("loc_50A1")

    label("loc_4ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4AEE")
    Call(0, 13)
    Jump("loc_50A1")

    label("loc_4AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD6")

    #C0141
    ChrTalk(
        0xFE,
        (
            "お、ロイドか。\x01",
            "今日は広場は自由に開放してるから\x01",
            "遠慮なく通ってくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "いや～、しかし除幕式は\x01",
            "ここから見ても十分すごかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "何ていうか、人間が\x01",
            "あんなものを造れるってのも\x01",
            "すごい話だよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C57")

    label("loc_4BD6")


    #C0144
    ChrTalk(
        0xFE,
        (
            "いや～、しかし除幕式は\x01",
            "ここから見ても十分すごかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "何ていうか、人間が\x01",
            "あんなものを造れるってのも\x01",
            "すごい話だよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C57")

    Jump("loc_50A1")

    label("loc_4C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DF1")

    #C0146
    ChrTalk(
        0xFE,
        (
            "よう、ロイド。\x01",
            "いよいよ明日から通商会議だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "警備の方もさっそく厳戒モードで\x01",
            "早くも緊張してきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#00006F確かに、明日には\x01",
            "首脳たちがクロスベル入り\x01",
            "するわけだからな。\x02\x03",

            "#00000F加えてオルキスタワーも\x01",
            "いよいよお披露目だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "ふぅ、何ていうか\x01",
            "色々とあり得ない感じだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "とにかく、明日から３日間、\x01",
            "お互い気を引き締めていこうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#00002Fああ、了解だ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 4)
    Jump("loc_4E8B")

    label("loc_4DF1")


    #C0152
    ChrTalk(
        0xFE,
        (
            "かつてない規模の国際会議……\x01",
            "改めて考えれば考えるほど、\x01",
            "どんどん緊張してくるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "ま、とにかく、\x01",
            "明日からの３日間は\x01",
            "気を引き締めていかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E8B")

    Jump("loc_50A1")

    label("loc_4E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4FD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAB")
    Call(0, 14)
    Jump("loc_4FD0")

    label("loc_4EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4F6A")

    #C0154
    ChrTalk(
        0xFE,
        (
            "確かに捜査官は憧れだけど……\x01",
            "何だか俺、理想にとらわれていた\x01",
            "気がするんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "何ていうか、これからはもっと\x01",
            "等身大の自分ってヤツと\x01",
            "向かい合ってみることに決めたぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 6)
    Jump("loc_4FD0")

    label("loc_4F6A")


    #C0156
    ChrTalk(
        0xFE,
        (
            "小雨とはいえ、\x01",
            "雨の日の警備は楽じゃないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "ロイドたちも、風邪を\x01",
            "引かないよう気を付けろよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD0")

    Jump("loc_50A1")

    label("loc_4FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_50A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF0")
    Call(0, 14)
    Jump("loc_50A1")

    label("loc_4FF0")


    #C0158
    ChrTalk(
        0xFE,
        (
            "確かに捜査官は憧れだけど……\x01",
            "何だか俺、理想にとらわれていた\x01",
            "気がするんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "何ていうか、これからはもっと\x01",
            "等身大の自分ってヤツと\x01",
            "向かい合ってみることに決めたぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 6)

    label("loc_50A1")

    TalkEnd(0xFE)
    Return()

    # Function_12_41FD end

    def Function_13_50A5(): pass

    label("Function_13_50A5")

    OP_4B(0xB, 0xFF)
    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)
    OP_4B(0x21, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5260")

    #C0160
    ChrTalk(
        0xB,
        (
            "も、申し訳ありません。\x01",
            "今日は本会議が行われる関係で\x01",
            "一般の方は――\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x1F,
        "ふむ、でも広場は関係ないだろう？\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x20,
        (
            "そうだよそうだよ、\x01",
            "僕らもせっかく来たんだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x21,
        (
            "ね、少しだけならいいでしょ？\x01",
            "１０分、いや５分でいいから、ね？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "いや、えっと、\x01",
            "そういう問題ではなくですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        (
            "#00200F（どうやら、広場の封鎖に対して\x01",
            "  抗議を行っているようですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#00006F（ああ。\x01",
            "  ……フランツも大変だな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5364")

    label("loc_5260")


    #C0167
    ChrTalk(
        0x21,
        (
            "５分、いや３分で\x01",
            "いいからお願い、ね？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x20,
        (
            "そうそう、僕らは\x01",
            "ちょっとだけでいいから。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x1F,
        (
            "いや、そもそも広場は\x01",
            "通しても問題ないはずだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "え、えっと、とにかく\x01",
            "駄目なものは駄目でして……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#00003F（俺たちが通る時は、\x01",
            "  脇をさりげなく通ろう……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5364")

    OP_4C(0xB, 0xFF)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    OP_4C(0x21, 0xFF)
    Return()

    # Function_13_50A5 end

    def Function_14_5375(): pass

    label("Function_14_5375")

    RunExpression(0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xB, 0x101, 0)

    #C0172
    ChrTalk(
        0xB,
        (
            "よう、ロイド。\x01",
            "捜査一課の研修もようやく\x01",
            "終わったんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "そしてロイドの肩書きも\x01",
            "とうとう上級捜査官に……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xB,
        (
            "はぁ、警察学校の同期だってのに\x01",
            "遠い所に行っちまったもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        (
            "#00012Fいや、別にそんなことないから。\x02\x03",

            "#00000Fそういえば、フランツの方は\x01",
            "捜査官試験の結果はどうだったんだ？\x02\x03",

            "確か、ちょっと前に受けたんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xB,
        (
            "ふっ、受かってたら\x01",
            "真っ先にロイドに報告してるさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "結果は惨敗……\x01",
            "はっきり言って俺には捜査官は\x01",
            "向いてないって思い知らされたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#00008Fそ、そうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        "まあでも、おかげで吹っ切れたよ。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "今の広域防犯課の仕事だって、\x01",
            "やりがいは十分過ぎるほどあるしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xB,
        (
            "別にそこまで捜査官に\x01",
            "拘る必要はなかったって言うか……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "これからはもっと、\x01",
            "等身大の自分ってヤツと\x01",
            "向かい合ってみることにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#00005Fフランツ……\x02\x03",

            "#00002Fそうか。\x01",
            "うん、そう思えるのは何よりだ。\x02\x03",

            "なら、これからもお互いに\x01",
            "それぞれの道を頑張って行こうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xB,
        "ああ、もちろんだ！\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x109,
        (
            "#10102F（う～ん、なんか\x01",
            "  男の友情って感じですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#00102F（ええ、ちょっと羨ましいわね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x13E, 5)
    Return()

    # Function_14_5375 end

    def Function_15_578E(): pass

    label("Function_15_578E")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_15_578E end

    def Function_16_5798(): pass

    label("Function_16_5798")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_16_5798 end

    def Function_17_57A2(): pass

    label("Function_17_57A2")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_17_57A2 end

    def Function_18_57AC(): pass

    label("Function_18_57AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_57BD")
    Jump("loc_5C31")

    label("loc_57BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5A5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59EB")

    #C0187
    ChrTalk(
        0xFE,
        "おや、支援課の皆さんですね。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        "#00000Fええ、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x102,
        "#00100F本部はまだ復旧中なんですね？\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "ええ、とりあえず一通り\x01",
            "片付けた状態ではありますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "とにかく、エントランスの\x01",
            "被害がひどい状況でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "受付の機能を回復させるには、\x01",
            "まだしばらく時間がかかります。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "ちなみに、受付に関する\x01",
            "事務作業は一時的に警察学校で\x01",
            "行うことになりまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "レベッカさんもいるし、\x01",
            "何か仕事関連の事務処理があれば\x01",
            "そちらで対応できるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#00002Fなるほど、了解です。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x103,
        "#00200Fどうも、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 4)
    Jump("loc_5A59")

    label("loc_59EB")


    #C0197
    ChrTalk(
        0xFE,
        (
            "本部が復旧するまで\x01",
            "まだしばらくかかります。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "何か事務処理があれば、\x01",
            "警察学校の方へ行くといいですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A59")

    Jump("loc_5C31")

    label("loc_5A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B28")

    #C0199
    ChrTalk(
        0xFE,
        (
            "今日は一般の方の\x01",
            "オルキスタワー方面への立ち入りを\x01",
            "制限させてもらっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "ご覧の通り『そんなの聞いてない』と\x01",
            "抗議してくる方も多いのですが……\x01",
            "とにかく関係者以外は通しません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C31")

    label("loc_5B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BA7")

    #C0201
    ChrTalk(
        0xFE,
        (
            "タワー前の広場は、\x01",
            "多くの市民や\x01",
            "観光客で賑わっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "除幕式の直後から、\x01",
            "往来もひっきりなしですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C31")

    label("loc_5BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5C1A")

    #C0203
    ChrTalk(
        0xFE,
        "明日はいよいよ除幕式……\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "新市庁ビルの工事が始まって５年、\x01",
            "ついにようやくという感じですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C31")

    label("loc_5C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5C28")
    Jump("loc_5C31")

    label("loc_5C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5C31")

    label("loc_5C31")

    TalkEnd(0xFE)
    Return()

    # Function_18_57AC end

    def Function_19_5C35(): pass

    label("Function_19_5C35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2E")

    #C0205
    ChrTalk(
        0xFE,
        (
            "午後になれば首脳たちも\x01",
            "オルキスタワーに集まり……\x01",
            "そして本会議が始まるわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "ここまでの状況からして、\x01",
            "何も起こらない可能性ってのは\x01",
            "かなり低いだろうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "とにかく、今日も\x01",
            "気合いを高めていくとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5DAD")

    label("loc_5D2E")


    #C0208
    ChrTalk(
        0xFE,
        (
            "はっきり言って、\x01",
            "何も起こらない可能性ってのは\x01",
            "かなり低いだろうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "とにかく、今日も\x01",
            "気合いを高めていくとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DAD")

    Jump("loc_5FF6")

    label("loc_5DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5E57")

    #C0210
    ChrTalk(
        0xFE,
        (
            "記念祭の時とまではいかないが、\x01",
            "流石に今日は人出が多いようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "撹乱目的で突発的に\x01",
            "テロ行為が発生する可能性もある。\x01",
            "注意深く監視しないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FF6")

    label("loc_5E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F5A")

    #C0212
    ChrTalk(
        0xFE,
        (
            "明日はどの首脳も、\x01",
            "この街区を抜けて新市庁の方に\x01",
            "向かわれることになる。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "この場所は見通しもよく、\x01",
            "狙撃などの犯行を実行しやすい\x01",
            "場所だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "クロスベル入りする\x01",
            "首脳たちを迎える時は、\x01",
            "特に厳戒な体制が敷かれる予定だぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5FF6")

    label("loc_5F5A")


    #C0215
    ChrTalk(
        0xFE,
        (
            "この場所は見通しもよく、\x01",
            "狙撃などの犯行を実行しやすい\x01",
            "場所だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "クロスベル入りする\x01",
            "首脳たちを迎える時は、\x01",
            "特に厳戒な体制が敷かれる予定だぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FF6")

    TalkEnd(0xFE)
    Return()

    # Function_19_5C35 end

    def Function_20_5FFA(): pass

    label("Function_20_5FFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_609A")

    #C0217
    ChrTalk(
        0xFE,
        (
            "テロリスト集団が同時に\x01",
            "２組もやって来るだなんて\x01",
            "まったく冗談じゃないよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "とにかく……何が何でも混乱が\x01",
            "起きる前に食い止めなきゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61DB")

    label("loc_609A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6141")

    #C0219
    ChrTalk(
        0xFE,
        (
            "くそー、オルキスタワー方面の\x01",
            "警備担当だったら首脳たちを\x01",
            "実際にこの目で見れたのにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "俺が見れたのはスモークガラスで\x01",
            "守られたリムジンだけだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61DB")

    label("loc_6141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_61DB")

    #C0221
    ChrTalk(
        0xFE,
        (
            "周辺４ヶ国の首脳たちが\x01",
            "一同に会するなんて……\x01",
            "正直、規模が凄まじ過ぎるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "……ここまで緊張感のある\x01",
            "警戒活動は初めてかもしれないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61DB")

    TalkEnd(0xFE)
    Return()

    # Function_20_5FFA end

    def Function_21_61DF(): pass

    label("Function_21_61DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62A7")

    #C0223
    ChrTalk(
        0xC,
        "#01200Fグルル……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x109,
        (
            "#10100Fツァイト君、\x01",
            "こんな所にいたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x103,
        (
            "#00202Fキーアの付き添いで\x01",
            "来てるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#00012Fそれにしても、\x01",
            "すっかり街に馴染んでるなあ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_62C6")

    label("loc_62A7")


    #C0227
    ChrTalk(
        0xC,
        "#01200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_62C6")

    TalkEnd(0xFE)
    Return()

    # Function_21_61DF end

    def Function_22_62CA(): pass

    label("Function_22_62CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6346")

    #C0228
    ChrTalk(
        0xFE,
        "さあさあ、風船はいかが～？\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "１個でも２個でも３個でも、\x01",
            "今日はいくらでも持って行ってくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_63B9")

    label("loc_6346")


    #C0230
    ChrTalk(
        0xFE,
        (
            "午後からは\x01",
            "バルーンアート教室ってのも\x01",
            "開催予定で～す。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "興味のある方はぜひぜひ\x01",
            "ふるってご参加くださ～い。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63B9")

    TalkEnd(0xFE)
    Return()

    # Function_22_62CA end

    def Function_23_63BD(): pass

    label("Function_23_63BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_64B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6438")

    #C0232
    ChrTalk(
        0x22,
        (
            "キーアちゃん、今日は\x01",
            "図書館に行くって言ってたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x22,
        "何か探しものでもあったのかな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_64B0")

    label("loc_6438")


    #C0234
    ChrTalk(
        0x22,
        (
            "昨日来てたシンくんも、\x01",
            "今日の列車で帰っちゃうらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x22,
        (
            "ちょっと寂しいな……\x01",
            "いいお友達になれそうだったのに。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64B0")

    TalkEnd(0xFE)
    Return()

    # Function_23_63BD end

    def Function_24_64B4(): pass

    label("Function_24_64B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_653E")

    #C0236
    ChrTalk(
        0x23,
        (
            "くっそー、入ったらダメだなんて\x01",
            "ケチくさいこと言いやがって。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x23,
        (
            "あーあ、なんとか\x01",
            "潜り込めねーかなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6577")

    label("loc_653E")


    #C0238
    ChrTalk(
        0x23,
        (
            "あー、早くしないと\x01",
            "楽しいパーティが始まっちまうぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6577")

    TalkEnd(0xFE)
    Return()

    # Function_24_64B4 end

    def Function_25_657B(): pass

    label("Function_25_657B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_65E7")

    #C0239
    ChrTalk(
        0x24,
        "もう、諦めようよリュウ～。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x24,
        (
            "通商会議って、\x01",
            "別に楽しいパーティとかじゃ\x01",
            "ないんだからね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E7")

    TalkEnd(0xFE)
    Return()

    # Function_25_657B end

    def Function_26_65EB(): pass

    label("Function_26_65EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_663E")

    #N0241
    NpcTalk(
        0xFE,
        "市民",
        (
            "帝国と共和国め、どこからでも\x01",
            "かかってきやがれってんだ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66F1")

    label("loc_663E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_669F")

    #C0242
    ChrTalk(
        0xFE,
        (
            "なんか今日はタワー前の\x01",
            "広場には入れないんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        "はぁ、つまんねーの。\x02",
    )

    CloseMessageWindow()
    Jump("loc_66F1")

    label("loc_669F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_66AD")
    Jump("loc_66F1")

    label("loc_66AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_66F1")

    #C0244
    ChrTalk(
        0xFE,
        (
            "はー、すっげーなー。\x01",
            "こっから見ても十分デケーじゃん！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F1")

    TalkEnd(0xFE)
    Return()

    # Function_26_65EB end

    def Function_27_66F5(): pass

    label("Function_27_66F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6746")

    #N0245
    NpcTalk(
        0xFE,
        "市民",
        (
            "アリオスさんが国防長官なら、\x01",
            "独立後も安心できるわね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67CD")

    label("loc_6746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_678D")

    #C0246
    ChrTalk(
        0xFE,
        (
            "あーん、また昨日みたいに\x01",
            "近くで見上げたかったなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67CD")

    label("loc_678D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_679B")
    Jump("loc_67CD")

    label("loc_679B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_67CD")

    #C0247
    ChrTalk(
        0xFE,
        (
            "だねー。\x01",
            "ってか、デカすぎじゃない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67CD")

    TalkEnd(0xFE)
    Return()

    # Function_27_66F5 end

    def Function_28_67D1(): pass

    label("Function_28_67D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_681F")

    #C0248
    ChrTalk(
        0xFE,
        (
            "はは、こんどウチの店でも\x01",
            "独立記念セールをやろうかなあ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D90")

    label("loc_681F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6957")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68B1")

    #C0249
    ChrTalk(
        0xFE,
        (
            "君も聞いたかい？\x01",
            "どうやらこの間の襲撃事件は\x01",
            "帝国の陰謀だったらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "僕は本当に\x01",
            "帝国という国が許せないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6952")

    label("loc_68B1")


    #C0251
    ChrTalk(
        0xFE,
        (
            "でも今回のことでよく分かったよ。\x01",
            "例え帝国に従った所で彼らは\x01",
            "僕らを守るつもりなんて毛頭ない……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "だからこそ、僕らは独立の意志を\x01",
            "押し通すしかないってね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6952")

    Jump("loc_6D90")

    label("loc_6957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A22")

    #C0253
    ChrTalk(
        0xFE,
        (
            "まさか……\x01",
            "こんな事件が起こるなんてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "警備隊が何とかしてくれると\x01",
            "いいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "いよいよとなれば、\x01",
            "それこそ２大国の力を借りないと\x01",
            "いけないんじゃないだろうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6A95")

    label("loc_6A22")


    #C0256
    ChrTalk(
        0xFE,
        (
            "だが、独立提唱の影響で\x01",
            "２大国との関係は\x01",
            "悪化しているというし……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "ううむ……\x01",
            "一体この先どうなるんだ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A95")

    Jump("loc_6D90")

    label("loc_6A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6AA8")
    Jump("loc_6D90")

    label("loc_6AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6B2F")

    #C0258
    ChrTalk(
        0xFE,
        (
            "そういえば……明日は\x01",
            "市民会館で市民フォーラムが\x01",
            "行われるんだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "ふむ、今からでも\x01",
            "問い合わせてみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D90")

    label("loc_6B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6C00")

    #C0260
    ChrTalk(
        0xFE,
        (
            "心情的なことだけで言うと、\x01",
            "独立にはもちろん賛成なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "とにかく、２大国の脅威から\x01",
            "どう安全を保つかが問題だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "対話で道が開けるといいんだが、\x01",
            "そう単純な話でもないからねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D90")

    label("loc_6C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6C59")

    #C0263
    ChrTalk(
        0xFE,
        (
            "クロスベルが独立するべきか否か……\x01",
            "ふむ、何度考えても難しい問題だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D90")

    label("loc_6C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6D02")

    #C0264
    ChrTalk(
        0xFE,
        (
            "ディーター市長とマクダエル議長、\x01",
            "この２人がいれば本会議は\x01",
            "必ず実り豊かなものになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "ふむ、クロスベル経済の\x01",
            "未来はますますもって明るいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D90")

    label("loc_6D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6D90")

    #C0266
    ChrTalk(
        0xFE,
        (
            "除幕式はこの場所からでも\x01",
            "十分に楽しめたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "クロスベルのどこからでも\x01",
            "見られるなんて、本当に凄まじい\x01",
            "スケールの建物だよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D90")

    TalkEnd(0xFE)
    Return()

    # Function_28_67D1 end

    def Function_29_6D94(): pass

    label("Function_29_6D94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6DA5")
    Jump("loc_70FB")

    label("loc_6DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6DF4")

    #C0268
    ChrTalk(
        0xFE,
        (
            "みんなにひどいことをして……\x01",
            "ていこくってわるいヤツだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_6DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6E59")

    #C0269
    ChrTalk(
        0xFE,
        (
            "パパ、昨日からずっと\x01",
            "こんなかんじでなやんでるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        "ゲンキ出してほしいな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_6E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6E67")
    Jump("loc_70FB")

    label("loc_6E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6EEE")

    #C0271
    ChrTalk(
        0xFE,
        (
            "明日、しみんかいかんで\x01",
            "ドクリツについてみんなで\x01",
            "お話するんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "うーん、なんか\x01",
            "オトナってカッコイイよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_6EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F83")

    #C0273
    ChrTalk(
        0xFE,
        (
            "う～ん、よくわからないけど\x01",
            "なんでおとなりさん同士で\x01",
            "なかよくできないんだろうね？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "これも、オトナの\x01",
            "じじょーってヤツなのかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_6F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7003")

    #C0275
    ChrTalk(
        0xFE,
        (
            "ドクリツすると、\x01",
            "良いこともあるけど悪いことも\x01",
            "いっぱいなんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        "う～ん、ボクにはよく分かんないや。\x02",
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_7003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7078")

    #C0277
    ChrTalk(
        0xFE,
        "今日はほんかいぎの日なんだって。\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "なんか、みんなで集まって\x01",
            "いろんなことをお話しするらしいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_7078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_70FB")

    #C0279
    ChrTalk(
        0xFE,
        (
            "カーテンがしゃーってなって、\x01",
            "それからハナビみたいなのが\x01",
            "ドドーンって上がって……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        "なんか、お祭りみたいだったよ！\x02",
    )

    CloseMessageWindow()

    label("loc_70FB")

    TalkEnd(0xFE)
    Return()

    # Function_29_6D94 end

    def Function_30_70FF(): pass

    label("Function_30_70FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_713A")

    #C0281
    ChrTalk(
        0xFE,
        "へへっ、今日はめでたい日になったな！\x02",
    )

    CloseMessageWindow()
    Jump("loc_71EF")

    label("loc_713A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_71EF")

    #C0282
    ChrTalk(
        0xFE,
        (
            "今、市民会館でやってる\x01",
            "チャリティイベントだけど、\x01",
            "ほんと色んな催しがあって楽しいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "それに何より、こうやって\x01",
            "楽しむことが復興につながるって\x01",
            "発想が素晴らしいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71EF")

    TalkEnd(0xFE)
    Return()

    # Function_30_70FF end

    def Function_31_71F3(): pass

    label("Function_31_71F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7204")
    Jump("loc_72A0")

    label("loc_7204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_72A0")

    #C0284
    ChrTalk(
        0xFE,
        (
            "このイベントの企画者は\x01",
            "クロスベル商工会なんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "ふふ、毎年記念祭の時にも\x01",
            "思うけど、商工会の人たちって\x01",
            "盛り上げ上手でパワフルよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72A0")

    TalkEnd(0xFE)
    Return()

    # Function_31_71F3 end

    def Function_32_72A4(): pass

    label("Function_32_72A4")

    TalkBegin(0xFE)

    #C0286
    ChrTalk(
        0xFE,
        "市民たちの熱狂ぶりはすさまじい……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "誰もが心の底で望んでいた\x01",
            "展開だったのかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_72A4 end

    def Function_33_730A(): pass

    label("Function_33_730A")

    TalkBegin(0xFE)

    #C0288
    ChrTalk(
        0xFE,
        "このままでは収拾がつかないな。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "早いところスクリーン車を\x01",
            "撤収した方がよさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_730A end

    def Function_34_736C(): pass

    label("Function_34_736C")

    TalkBegin(0xFE)

    #C0290
    ChrTalk(
        0xFE,
        (
            "ディーター大統領は\x01",
            "素晴らしい決断をして下さった。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "長年クロスベルで生きてきて、\x01",
            "これほど嬉しい事はないぞい。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_736C end

    def Function_35_73E9(): pass

    label("Function_35_73E9")

    TalkBegin(0xFE)

    #C0292
    ChrTalk(
        0xFE,
        (
            "おお、女神様。\x01",
            "どうかクロスベルの未来を\x01",
            "見守っていてください……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_73E9 end

    def Function_36_7436(): pass

    label("Function_36_7436")

    TalkBegin(0xFE)

    #C0293
    ChrTalk(
        0xFE,
        "さあ、あんたたちも一緒に。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        "クロスベル独立国、万歳！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_7436 end

    def Function_37_747B(): pass

    label("Function_37_747B")

    TalkBegin(0xFE)

    #C0295
    ChrTalk(
        0xFE,
        (
            "大統領さんの演説は\x01",
            "とっても素晴らしかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "クロスベルは、これからもっと\x01",
            "素敵な場所になるわよね！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_747B end

    def Function_38_74F0(): pass

    label("Function_38_74F0")

    TalkBegin(0xFE)

    #C0297
    ChrTalk(
        0xFE,
        (
            "えへへ、なんだかみんな\x01",
            "うれしそうだねー。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_74F0 end

    def Function_39_7526(): pass

    label("Function_39_7526")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_75C8")

    #C0298
    ChrTalk(
        0xFE,
        (
            "雨の日って、\x01",
            "色んな音が聞けて楽しいですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "水面や傘や地面……\x01",
            "当たる場所によって音が変わって\x01",
            "ちょっとしたオーケストラって感じです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7674")

    label("loc_75C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7674")

    #C0300
    ChrTalk(
        0xFE,
        (
            "私ってクセッ毛なんですけど……\x01",
            "雨の日は何だかイイ感じに\x01",
            "髪がまとまってくれるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "だから私、雨の日が好きで……\x01",
            "って、どうでもいい話をしてすみません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7674")

    TalkEnd(0xFE)
    Return()

    # Function_39_7526 end

    def Function_40_7678(): pass

    label("Function_40_7678")

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
        "す、すごい演説だったな……\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x18,
        (
            "#6Pまさかクロスベルの\x01",
            "独立を宣言するなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x19,
        (
            "#6Pそれも、帝国と共和国を\x01",
            "あんな風に言ってしまうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x17,
        (
            "#12P２大国の“暗闘”とか言ってたけど……\x01",
            "もしかして昔起きたあの事故も……？\x02",
        )
    )

    CloseMessageWindow()

    #N0306
    NpcTalk(
        0xD,
        "市民",
        "#12P帝国と共和国め……！！\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xF,
        (
            "#6P……今まで、クロスベルの為に\x01",
            "あそこまで言ってくれる人がいたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x16,
        (
            "クロスベルの政治家たちは、\x01",
            "帝国と共和国に飼いならされた\x01",
            "うつけどもばかりじゃった……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x19,
        (
            "マクダエル議長みたいな\x01",
            "立派な人はいたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x18,
        (
            "#6Pここまでのパワーを\x01",
            "感じさせてくれる人は\x01",
            "確かにいなかったよな……！\x02",
        )
    )

    CloseMessageWindow()

    #N0311
    NpcTalk(
        0xE,
        "市民",
        (
            "#6Pしかも、クロスベルの守護神\x01",
            "アリオスさんが国防長官ですって！\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x11,
        (
            "#5Pこれ以上ない人選だよな。\x01",
            "あの人が先頭に立って\x01",
            "クロスベルを守ってくれるなら……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x17,
        "#12Pええ、怖いものなんて何もないわ！\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x16,
        (
            "クロスベルの独立も、\x01",
            "夢物語じゃないのかもしれん……！\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xF,
        (
            "#6Pディーター市長、いや大統領……\x01",
            "彼に任せておけばきっと大丈夫だ！\x02",
        )
    )

    CloseMessageWindow()
    OP_25(0x1BD, 0x3C)

    #N0316
    NpcTalk(
        0xD,
        "市民",
        (
            "#12Pおお、彼さえいれば\x01",
            "帝国や共和国なんて怖くない……！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x18,
        "#6Pディーター大統領……！\x02",
    )

    CloseMessageWindow()

    #N0318
    NpcTalk(
        0xE,
        "市民",
        "#6Pディーター大統領っ！\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0319
    ChrTalk(
        0x16,
        "#5Sディーター大統領、万歳！#3S\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("市民たち")

    #A0320
    AnonymousTalk(
        0xFF,
        "#5Sディーター大統領、万歳！！#3S\x02",
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
        "#5Sクロスベル独立国、万歳！#3S\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("市民たち")

    #A0322
    AnonymousTalk(
        0xFF,
        "#5S#6Pクロスベル独立国、万歳！！#3S\x02",
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
    SetChrName("市民たち")

    #A0323
    AnonymousTalk(
        0xFF,
        "#5Sディーター大統領、万歳！！#3S\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetChrName("市民たち")

    #A0324
    AnonymousTalk(
        0xFF,
        "#5Sクロスベル独立国、万歳！！#3S\x02",
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
        "#6P#00005F……もの凄い熱狂ぶりだな。\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        "#6P#00108Fええ……気持ちは分かるけれど。\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x103,
        (
            "#6P#00201F熱くなりすぎて\x01",
            "トラブルが起きないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x104,
        (
            "#12P#00303Fまあ、国防軍の兵士もいるし\x01",
            "そのうち収まるだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        "#6P#00001F……とにかく、行くとしよう。\x02",
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

    # Function_40_7678 end

    def Function_41_7F23(): pass

    label("Function_41_7F23")

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

    def lambda_805B():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_805B)
    Sleep(50)

    def lambda_806B():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_806B)
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
        "#5P#00005Fあっと、課長かな？\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        (
            "#12P#00102Fそろそろ掛かってきても\x01",
            "おかしくない時間ね。\x02",
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
            "#00000Fはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0333
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おう、ご苦労。\x02\x03",

            "朝言った通り、そろそろ\x01",
            "警察学校に来てもらうぞ。\x02\x03",

            "場所は分かるな？\x02",
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
            "#00004Fええ、もちろん。\x02\x03",

            "#00000F西クロスベル街道の途中から\x01",
            "ゲートに入ったところですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0335
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、ゲートは開けておく。\x02\x03",

            "ところで……\x01",
            "一通り街を回ったはずだな。\x02\x03",

            "率直に言ってどうだった？\x02",
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
            "#00011Fあ……\x02",
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
            "#00003F……そうですね。\x02\x03",

            "#00001F色々とキナ臭い状況に\x01",
            "なり始めている気がします。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その嗅覚、今まで以上に\x01",
            "研ぎ澄ませておくといい。\x02\x03",

            "それじゃあ待ってるぞ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0339
    AnonymousTalk(
        0x101,
        "#00000F了解しました。\x02",
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
        "#12P#00100Fやっぱり課長だったみたいね。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x109,
        (
            "#6P#10105F何か気になることを\x01",
            "言ってたみたいですけど……？\x02",
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
            "#5P#00006Fああ、課長も色々と\x01",
            "状況の変化を感じているらしい。\x02\x03",

            "#00001F黒月やレクター大尉のことも\x01",
            "報告した方が良さそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x102,
        "#12P#00106Fそうね……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x105,
        (
            "#11P#10300Fで、そろそろ\x01",
            "警察学校に行くのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        "#5P#00000Fああ、西口から街道に出よう。\x02",
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
            "クロスベルの市街地図から\x01",
            "『西クロスベル街道』が\x01",
            "選択できるようになりました。\x07\x00\x02",
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

    # Function_41_7F23 end

    def Function_42_8687(): pass

    label("Function_42_8687")

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

    # Function_42_8687 end

    def Function_43_89EB(): pass

    label("Function_43_89EB")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 17150, 2500, 450)
    OP_9F(0x1, 4400, 2500, 8350)
    OP_9F(0x1, -4000, 2500, 21250)
    OP_9F(0x1, -5850, 2500, 32500)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_43_89EB end

    def Function_44_8A31(): pass

    label("Function_44_8A31")

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
    SetChrName("マクダエル議長")

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W──無論、現状についての是非は\x01",
            "人それぞれあるでしょう！\x02\x03",

            "ですが現政府は、真に民主的な\x01",
            "手続きによっては成立していません！\x02\x03",

            "自治州議員の多くが拘束され、\x01",
            "私自身、監禁された状態で、\x01",
            "クロスベルの独立は宣言されました！\x02\x03",

            "この宣言が、議会の承認を経ずに\x01",
            "個人の独断で行われたものである事は\x01",
            "改めて指摘しておきたいと思います。\x07\x00\x02",
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

    # Function_44_8A31 end

    def Function_45_8E9E(): pass

    label("Function_45_8E9E")

    Sleep(2000)

    def lambda_8EA6():
        OP_96(0xFE, 0xAF0, 0x9C4, 0x11F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_8EA6)
    Sleep(500)

    def lambda_8EC3():
        OP_96(0xFE, 0xFFFFFF38, 0x9C4, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_8EC3)
    Sleep(500)

    def lambda_8EE0():
        OP_96(0xFE, 0x384, 0x9C4, 0x1A2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_8EE0)
    Sleep(500)

    def lambda_8EFD():
        OP_96(0xFE, 0x1194, 0x9C4, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_8EFD)
    WaitChrThread(0x3D, 1)
    OP_63(0x3D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x40, 1)
    OP_63(0x40, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x3E, 1)
    Return()

    # Function_45_8E9E end

    def Function_46_8F55(): pass

    label("Function_46_8F55")

    Sleep(8000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_8F6F():
        OP_96(0xFE, 0x8FC, 0x9C4, 0x2AF8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F6F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_46_8F55 end

    def Function_47_8F9A(): pass

    label("Function_47_8F9A")

    Sleep(8200)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_8FB4():
        OP_96(0xFE, 0x7D0, 0x9C4, 0x2FA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FB4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_47_8F9A end

    def Function_48_8FD5(): pass

    label("Function_48_8FD5")

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
            "#1K同日、１０：３０──\x02",
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

    def lambda_93DA():
        OP_A6(0xFE, 0x0, 0x64, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_93DA)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_9406():
        OP_A6(0xFE, 0x0, 0x64, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_9406)
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
        "クリア！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x2A, 3)
    OP_93(0x2A, 0x87, 0x1F4)

    #C0350
    ChrTalk(
        0x2A,
        "#5P今よ！\x02",
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

    def lambda_958E():

        label("loc_958E")

        TurnDirection(0xFE, 0x33, 500)
        Yield()
        Jump("loc_958E")

    QueueWorkItem2(0x2A, 2, lambda_958E)
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

    def lambda_95FB():
        OP_95(0xFE, -7500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_95FB)
    Sleep(50)
    ClearChrFlags(0x28, 0x4)

    def lambda_961D():
        OP_95(0xFE, -4500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_961D)
    Sleep(50)
    ClearChrFlags(0x27, 0x4)

    def lambda_963F():
        OP_95(0xFE, -4500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_963F)
    Sleep(50)
    ClearChrFlags(0x2A, 0x4)
    SetChrChipByIndex(0x2A, 0x1B)
    SetChrSubChip(0x2A, 0x0)

    def lambda_9669():
        OP_95(0xFE, -7500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9669)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    SetScenarioFlags(0x22, 7)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_48_8FD5 end

    def Function_49_969F(): pass

    label("Function_49_969F")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0x29, 0x17)
    SetChrSubChip(0x29, 0x0)

    def lambda_96BF():
        OP_96(0xFE, 0xFFFFE2B4, 0x9C4, 0x6978, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_96BF)

    #C0351
    ChrTalk(
        0x29,
        "#10Aはあああっ！\x02",
    )
    #Auto

    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x29, 0x19)
    SetChrSubChip(0x29, 0x2)
    Sound(251, 0, 60, 0)

    def lambda_96FF():
        OP_9D(0xFE, 0xFFFFE2B4, 0xDAC, 0x80E8, 0x5DC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_96FF)
    WaitChrThread(0xFE, 1)
    Sound(815, 0, 100, 0)
    SetChrSubChip(0x29, 0x3)
    BeginChrThread(0x26, 3, 0, 54)
    Sleep(1000)
    SetChrSubChip(0x29, 0x4)

    def lambda_9737():
        OP_9D(0xFE, 0xFFFFE2B4, 0x9C4, 0x7D00, 0xC8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9737)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x29, 0x16)
    SetChrSubChip(0x29, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_49_969F end

    def Function_50_9764(): pass

    label("Function_50_9764")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)

    def lambda_977C():
        OP_96(0xFE, 0xFFFFED40, 0x9C4, 0x6D60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_977C)
    Sleep(500)

    #C0352
    ChrTalk(
        0x28,
        "#16Aおおおおおっ！\x02",
    )
    #Auto

    WaitChrThread(0xFE, 1)
    Sound(844, 0, 70, 0)

    def lambda_97B9():
        OP_9D(0xFE, 0xFFFFED40, 0x9C4, 0x7DC8, 0x384, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_97B9)
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

    # Function_50_9764 end

    def Function_51_9845(): pass

    label("Function_51_9845")

    SetChrChipByIndex(0x2A, 0x1B)
    SetChrSubChip(0x2A, 0x0)

    def lambda_9852():
        OP_96(0xFE, 0xFFFFE0C0, 0x9C4, 0x7724, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9852)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x2A, 0x1A)
    SetChrSubChip(0x2A, 0x0)
    Return()

    # Function_51_9845 end

    def Function_52_9874(): pass

    label("Function_52_9874")


    def lambda_9879():
        OP_96(0xFE, 0xFFFFEE6C, 0x9C4, 0x7724, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9879)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_52_9874 end

    def Function_53_989D(): pass

    label("Function_53_989D")

    OP_82(0xFA, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_98D7():
        OP_A6(0xFE, 0x0, 0x64, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_98D7)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1700, -500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 1700, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    PlayEffect(0x1, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_999C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_999C)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_53_989D end

    def Function_54_99B0(): pass

    label("Function_54_99B0")

    OP_82(0xFA, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(501, 0, 100, 0)

    def lambda_99F0():
        OP_A6(0xFE, 0x0, 0x64, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_99F0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 1700, -300, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    MoveCamera(43, 15, 5, 4000)
    SetCameraDistance(16000, 4000)
    Sound(985, 0, 100, 0)
    PlayEffect(0x1, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_9A98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9A98)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_54_99B0 end

    def Function_55_9AAC(): pass

    label("Function_55_9AAC")

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

    def lambda_9B2C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9B2C)
    Sound(501, 0, 50, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 2850, 200, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 2850, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_55_9AAC end

    def Function_56_9BCC(): pass

    label("Function_56_9BCC")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3100, 2500, 10400)
    OP_9F(0x1, -3900, 2500, 20900)
    OP_9F(0x1, -5600, 2500, 35700)
    OP_9F(0x2, 0xFE, 10000, 0x6)

    def lambda_9C08():
        OP_96(0xFE, 0xFFFFEA20, 0x1D4C, 0xED1C, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C08)
    OP_D5(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1F4)
    Return()

    # Function_56_9BCC end

    def Function_57_9C31(): pass

    label("Function_57_9C31")

    Sleep(500)
    Sound(207, 0, 60, 0)
    Sleep(1000)

    label("loc_9C3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C5F")
    Sound(246, 0, 70, 0)
    Sleep(300)
    Sound(246, 0, 60, 0)
    Sleep(400)
    Jump("loc_9C3D")

    label("loc_9C5F")

    Return()

    # Function_57_9C31 end

    def Function_58_9C60(): pass

    label("Function_58_9C60")

    Sound(458, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(2000)
    Sound(487, 0, 100, 0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Return()

    # Function_58_9C60 end

    def Function_59_9C85(): pass

    label("Function_59_9C85")

    EventBegin(0x1)

    #C0353
    ChrTalk(
        0x101,
        (
            "#00001Fオルキスタワー方面は\x01",
            "『国防軍』が厳しく\x01",
            "警備しているみたいだ。\x02\x03",

            "#00003F……行くのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -5600, 2500, 34230, 180)
    EventEnd(0x4)
    Return()

    # Function_59_9C85 end

    def Function_60_9D0A(): pass

    label("Function_60_9D0A")

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
        "レジー",
        "#10Aうわっ！！？？\x02",
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
        "サイクス",
        (
            "おいおい、さっき通った時は\x01",
            "こんなの無かったぞ！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("ユーリ")

    #N0356
    NpcTalk(
        0x36,
        "ユーリ",
        "チッ、即席のバリケードか……\x02",
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

    def lambda_A122():
        OP_96(0xFE, 0x4DE4, 0x0, 0xFFFF6BE0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_A122)
    Sleep(1000)

    def lambda_A13F():
        OP_96(0xFE, 0x4DE4, 0x0, 0xFFFF4CA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_A13F)
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
        "#N#10302Fフフ、チェックメイトだね。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#N#00000Fああ、後は……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x2E,
        "……さぁ、いよいよ追い詰めたわよ！\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x2E,
        "おとなしく投降しなさい！\x02",
    )

    CloseMessageWindow()
    SetChrName("サイクス")

    #N0361
    NpcTalk(
        0x36,
        "サイクス",
        "……まあ、しゃーねえか。\x02",
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
            "へいへい、\x01",
            "トーコーしますよっと～。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x2F,
        (
            "やれやれ、無能は無能なりに\x01",
            "頭を使ったというわけか。\x02",
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
            "あ、あなたたちね……\x01",
            "少しは反省の色を\x01",
            "見せたらどうなの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x2E,
        (
            "自分たちがどれだけの人に\x01",
            "迷惑をかけてるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x31,
        (
            "はいはい、分かりましたよ～。\x01",
            "そう興奮するなっつの。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x30,
        (
            "あんまり怒ると\x01",
            "コジワが増えちまうぜ、\x01",
            "オ・バ・サ・ン。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0368
    ChrTalk(
        0x2E,
        "#4Sお、おばっ……！？\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x2E,
        (
            "あ、あなたたちと\x01",
            "そんなに変わらないでしょ！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x2E, 500)
    Sleep(100)

    #C0370
    ChrTalk(
        0xB,
        "せ、先輩、落ちついて……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x2F,
        (
            "ほら、さっさとどこにでも\x01",
            "連行していったらどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x2F,
        (
            "ま、俺たちに罰則を与えるなんて\x01",
            "お前らには出来ないだろうがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x109,
        "#10105Fえっ……！？\x02",
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
            "#00000F……ケイト先輩。\x01",
            "とにかく今は彼らを\x01",
            "本部に連行しましょう。\x02\x03",

            "いつまでもここに\x01",
            "車を停めておくわけにも\x01",
            "いきませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x2E,
        "くっ……そうね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0x101, 500)
    Sleep(100)

    #C0377
    ChrTalk(
        0x2E,
        (
            "それじゃあ支援課のみんなは、\x01",
            "その子らの連行を手伝って頂戴。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0xB, 500)
    Sleep(100)

    #C0378
    ChrTalk(
        0x2E,
        "フランツ君は撤収の準備をよろしく。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xB,
        "はッ！\x02",
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

    # Function_60_9D0A end

    def Function_61_A818(): pass

    label("Function_61_A818")

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

    # Function_61_A818 end

    def Function_62_A938(): pass

    label("Function_62_A938")

    OP_96(0x36, 0x4D12, 0x0, 0xFFFF7B58, 0x3A98, 0x0)
    OP_9F(0x0, 0x36)
    OP_9F(0x1, 19500, 390, -31390)
    OP_9F(0x1, 19420, 1410, -27710)
    OP_9F(0x1, 19800, 1410, -27710)
    OP_9F(0x2, 0x36, 15000, 0x6)
    OP_D5(0x36, 0xFFFFD8F0, 0xAFC8, 0xFFFFD8F0, 0x0)
    Return()

    # Function_62_A938 end

    def Function_63_A997(): pass

    label("Function_63_A997")

    OP_97(0x2E, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
    OP_95(0x2E, 18560, 10, -34510, 1000, 0x0)
    TurnDirection(0x2E, 0x101, 500)
    Return()

    # Function_63_A997 end

    def Function_64_A9C7(): pass

    label("Function_64_A9C7")

    OP_97(0xB, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
    OP_95(0xB, 21150, 0, -34360, 1000, 0x0)
    TurnDirection(0xB, 0x101, 500)
    Return()

    # Function_64_A9C7 end

    def Function_65_A9F7(): pass

    label("Function_65_A9F7")

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
            "いらっしゃいませ。\x01",
            "ジュースはいかがですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#00000Fすみません、\x01",
            "特務支援課の者なんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0383
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『一押しグルメ』の取材で\x01",
            "来たことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0384
    ChrTalk(
        0x8,
        (
            "ああ、その件でしたか。\x01",
            "話は伺っていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x8,
        (
            "それでは、こちらをどうぞ。\x01",
            "ジューススタンドの新商品、\x01",
            "『にがトマトソーダ』です！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_ADB4")

    #C0386
    ChrTalk(
        0x101,
        (
            "#00005Fこ、これは確か、\x01",
            "マクダエル議長御用達の……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x8,
        (
            "ええ、議長になられてからも\x01",
            "変わりなくご愛飲\x01",
            "いただいていますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x8,
        (
            "これは、あのドリンクを\x01",
            "改良した新商品なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x8,
        (
            "ソーダで苦味を和らげていますから、\x01",
            "にがトマトが苦手な皆様も\x01",
            "美味しく健康になれるはずです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE7C")

    label("loc_ADB4")


    #C0390
    ChrTalk(
        0x101,
        "#00005Fに、にがトマトって……あの？\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x8,
        (
            "これは、にがトマトのジュースを\x01",
            "改良した新商品なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x8,
        (
            "ソーダで苦味を和らげていますから、\x01",
            "にがトマトが苦手な皆様も\x01",
            "美味しく健康になれるはずです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE7C")


    #C0393
    ChrTalk(
        0x102,
        "#00109Fな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x104,
        "#00306F（……おいロイド、マジで飲むのか？）\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#00006F（し、仕事だし仕方ない……\x01",
            "  頑張って飲んでみよう。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0396
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちはにがトマトソーダを飲んだ。\x07\x00\x02",
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
            "全員のＣＰが５０回復した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0398
    ChrTalk(
        0x101,
        "#00010F#4S……ぶはっ……！！\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x109,
        (
            "#10106Fごほっ、ごほっ……！\x01",
            "こ、これは……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x103,
        (
            "#00206F……がっつり苦いです。\x02\x03",

            "#00211Fというか、ソーダのシュワシュワが\x01",
            "それをパワーアップさせているかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x8,
        "ええっ、そうですか？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x8,
        (
            "うーん、まだまだ改良の余地が\x01",
            "ありそうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x8,
        (
            "……とにかく、お口直しなら\x01",
            "こちらの定番ドリンク、\x01",
            "『ベルベリージュース』をどうぞ。\x02",
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
            "ロイドたちはベルベリージュースを飲んだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0405
    ChrTalk(
        0x102,
        (
            "#00102F（こくこく……）\x01",
            "あっ、すごくおいしい……\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、さっきの苦さの反動も\x01",
            "ありそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#00012F（ガイドで紹介するときは、\x01",
            "  こっちをオススメしたほうが\x01",
            "  いいかもしれないなあ……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x172, 4)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_B4B3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_B4D0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_B4E3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_B4F6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_B513")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_B526")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_B543")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_B556")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_B573")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_B586")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_B5A3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B5A3")

    OP_29(0x80, 0x1, 0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6A6")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0408
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "飲食店６ヶ所の取材を終えた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B69D")

    #A0409
    AnonymousTalk(
        0x101,
        (
            "#00003Fすぐにでもグレイスさんに\x01",
            "報告に行く事はできそうだけど……\x02\x03",

            "#00000Fまだ６人全員のお気に入りが\x01",
            "見つかったわけじゃない。\x01",
            "もう少し頑張ってみるかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B69D")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_B6A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B777")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0410
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特務支援課メンバー全員の\x01",
            "お気に入りを見つけた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0411
    AnonymousTalk(
        0x101,
        (
            "#00000Fこれで６人全員の\x01",
            "お気に入りが見つかった。\x02\x03",

            "取材はこれで十分だな。\x01",
            "さっそく通信社に報告へ行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_B777")

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

    # Function_65_A9F7 end

    def Function_66_B7B1(): pass

    label("Function_66_B7B1")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0412
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　 この先オルキスタワー 　※\x01",
            "※　関係者以外立ち入り禁止　※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_66_B7B1 end

    def Function_67_B819(): pass

    label("Function_67_B819")

    EventBegin(0x1)

    #C0413
    ChrTalk(
        0x101,
        (
            "#00000F今は明日の準備で\x01",
            "タワー方面も大忙しだろう。\x02\x03",

            "用事もないのに\x01",
            "近付くのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -5600, 2500, 34230, 180)
    EventEnd(0x4)
    Return()

    # Function_67_B819 end

    def Function_68_B891(): pass

    label("Function_68_B891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA68")
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
            "#12P#00101F……流石にタワー前には\x01",
            "近づけそうにないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x104,
        (
            "#12P#00306Fだな、あそこにいるヤツに\x01",
            "見つかったらあっという間に\x01",
            "増援を呼ばれそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        (
            "#12P#00001F……そうなると\x01",
            "作戦への影響も避けられない。\x02\x03",

            "#00003F気付かれない内に引き返そう。\x02",
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
    Jump("loc_BAE1")

    label("loc_BA68")

    EventBegin(0x1)
    SetChrName("")

    #A0417
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "タワー前は魔導兵によって守られている。\x01",
            "引き返した方がよさそうだ。\x07\x00\x02",
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

    label("loc_BAE1")

    Return()

    # Function_68_B891 end

    def Function_69_BAE2(): pass

    label("Function_69_BAE2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BAF3")
    Jump("loc_C386")

    label("loc_BAF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BDC5")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0418
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " チャリティイベント　　　　　　　　　　　 \x01",
            " 　『～みんなで広げよう復興の輪～』　　　 \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " 【プログラム概要】　　　　　　　　　　　 \x01",
            " 　・ソロピアノコンサート　　　　　　　　 \x01",
            " 　・ミス・クロスベルコンテスト　　　　　 \x01",
            " 　・大衆グルメコンテスト　　　　　　　　 \x01",
            " 　・各種アートワーク教室　　　　　　　　 \x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0419
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "  場所 ：クロスベル市民会館・多目的ホール \x01",
            " 　　　　会館前広場　　　　　　　　　　　 \x01",
            " 開催日：本日　　　　　　　　　　　　　　 \x01",
            " 主催者：クロスベル商工会／クロスベル市　 \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " ※各種イベントの参加費用は、　　　　　　 \x01",
            " 　全て復興支援の資金に充てられます。　　 \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_C386")

    label("loc_BDC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BFB6")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0420
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " 市民フォーラム　　　　　　　　　　　　　 \x01",
            " 　　『～今こそ真剣に考えよう、　　　　　 \x01",
            " 　　　　　　　　　国家独立の是非～』　　 \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " 【プログラム概要】　　　　　　　　　　　 \x01",
            " 　・有識者が語る国家独立の是非　　　　　 \x01",
            " 　・現役自治州議員による公開討論会　　　 \x01",
            "  場所 ：クロスベル市民会館・多目的ホール \x01",
            " 開催日：本日　　　　　　　　　　　　　　 \x01",
            " 主催者：クロスベル市／クロスベル通信社　 \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_C386")

    label("loc_BFB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C1A9")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0421
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " 市民フォーラム　　　　　　　　　　　　　 \x01",
            " 　　『～今こそ真剣に考えよう、　　　　　　 \x01",
            " 　　　　　　　　　国家独立の是非～』　　 \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " 【プログラム概要】　　　　　　　　　　　 \x01",
            " 　・有識者が語る国家独立の是非　　　　　 \x01",
            " 　・現役自治州議員による公開討論会　　　 \x01",
            "  場所 ：クロスベル市民会館・多目的ホール \x01",
            " 開催日：明日　　　　　　　　　　　　　　 \x01",
            " 主催者：クロスベル市／クロスベル通信社　 \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_C386")

    label("loc_C1A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C1B7")
    Jump("loc_C386")

    label("loc_C1B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C37D")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0422
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " 初心者向け投資家セミナー　　　　　　　　 \x01",
            "  『――明日の経済を読み解くために――』  \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            "  場所 ：クロスベル市民会館・多目的ホール \x01",
            " 開催日：本日　　　　　　　　　　　　　　 \x01",
            " 主催者：貿易商リゼロ　　　　　　　　　　 \x01",
            " ※なお席には余裕がございますので、　　　 \x01",
            " 　当日の飛び入り参加も　　　　　　　　　 \x01",
            " 　ぜひぜひお待ちしております。　　　　　 \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_C386")

    label("loc_C37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C386")

    label("loc_C386")

    TalkEnd(0xFF)
    Return()

    # Function_69_BAE2 end

    def Function_70_C38A(): pass

    label("Function_70_C38A")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0423
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には固く鍵が掛けられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C502")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C4A6")

    #C0424
    ChrTalk(
        0x101,
        (
            "#00003F警察本部……\x01",
            "中には誰もいないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x10A,
        (
            "#12P#00603F……昨日の戒厳令以降、ここは\x01",
            "国防軍によって封鎖された状態だ。\x02\x03",

            "#00600F――とにかく、今は先を急ぐぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        "#00001Fええ……了解です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C4FF")

    label("loc_C4A6")


    #C0427
    ChrTalk(
        0x101,
        (
            "#00003F警察本部……\x01",
            "中には誰もいないみたいだな。\x02\x03",

            "#00001Fとにかく、今は先を急ごう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4FF")

    SetScenarioFlags(0x1, 5)

    label("loc_C502")

    TalkEnd(0xFF)
    Return()

    # Function_70_C38A end

    SaveToFile()

Try(main)
