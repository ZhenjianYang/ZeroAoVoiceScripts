from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ジーナ",                 # 1
        "コンテ老人",             # 2
        "アベル",                 # 3
        "ミミ",                   # 4
        "プルーナ",               # 5
        "リナリー",               # 6
        "ハース",                 # 7
        "サリー",                 # 8
        "コッペ",                 # 9
        "ツァイト",               # 10
        "キーア",                 # 11
        "ケイト巡査",             # 12
        "フランツ巡査",           # 13
        "警備隊員",               # 14
        "警官",                   # 15
        "国防軍兵士",             # 16
        "市民",                   # 17
        "市民",                   # 18
        "車",                     # 19
        "リュウ",                 # 20
        "アンリ",                 # 21
        "キーア",                 # 22
        "白ハヤブサ",             # 23
        "セルゲイ課長",           # 24
        "国防軍兵士",             # 25
        "市民１",                 # 26
        "市民２",                 # 27
        "市民３",                 # 28
        "市民４",                 # 29
        "市民５",                 # 30
        "市民６",                 # 31
        "市民７",                 # 32
        "イベント用モンスター",   # 33
        "イベント用モンスター",   # 34
        "イベント用モンスター",   # 35
        "イベント用モンスター",   # 36
        "イベント用モンスター",   # 37
        "車",                     # 38
        "暴走車",                 # 39
        "パトカー1",              # 40
        "パトカー2",              # 41
        "パトカー3",              # 42
        "車",                     # 43
        "車",                     # 44
        "車",                     # 45
        "ランディ",               # 46
        "ノエル",                 # 47
        "ワジ",                   # 48
        "SE制御",                 # 49
        "警官",                   # 50
        "警官",                   # 51
        "警官",                   # 52
        "警官",                   # 53
        "警官",                   # 54
        "風船屋",                 # 55
        "ミュラー",               # 56
        "オリビエ",               # 57
        "bc0100",                 # 58
        "bc0100",                 # 59
        "中央広場",               # 60
        "西通り",                 # 61
        "行政区",                 # 62
        "住宅街",                 # 63
        "歓楽街",                 # 64
        "東通り",                 # 65
        "旧市街",                 # 66
        "港湾区",                 # 67
        "ＩＢＣ",                 # 68
        "駅前通り",               # 69
        "裏通り",                 # 70
        "ウルスラ間道",           # 71
        "東クロスベル街道",       # 72
        "西クロスベル街道",       # 73
        "マインツ山道",           # 74
        "オルキスタワー",         # 75
    ))

    ATBonus("ATBonus_B6C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_B7C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_10368", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_BBC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_BCC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_BD0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_BD4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_BD8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C1C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_C20", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_C24", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_C28", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_C2C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_C30", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_C34", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C38", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_B9C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_BA0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_BA4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_BA8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_BAC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_BB0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_BB4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_BB8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_C3C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C40", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_C44", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_C48", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C50", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C54", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C58", 0, 0, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_C5C", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0100", "Sepith_10368", 60, 30, 10, 0,
        (
            ("ms85100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_BBC", "MonsterBattlePostion_C1C", "ed7450", "ed7453", "ATBonus_B6C"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_B9C", "MonsterBattlePostion_C1C", "ed7450", "ed7453", "ATBonus_B6C"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_BBC", "MonsterBattlePostion_C1C", "ed7450", "ed7453", "ATBonus_B6C"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_CF8", 0x004A, 3, 6, 45, 3, 3, 30, 0, "bc0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C3C", "MonsterBattlePostion_C1C", "ed7544", "ed7453", "ATBonus_B7C"),
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

    DeclMonster(-9070,   13520,   0,       0x10100E1,    "BattleInfo_C5C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-4890,   -4070,   0,       0x10100B4,    "BattleInfo_C5C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(6530,    -110,    0,       0x10100B4,    "BattleInfo_C5C", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 11,  0.0,                   -17.0,                 -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  3.4000000953674316,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 105, -20.649999618530273,   -24.65999984741211,    -8.199999809265137,    625.0,                 [0.07071065157651901,  0.14142140746116638,   -0.0,                  0.0,                   -0.07071070373058319,  0.14142130315303802,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   -0.28355100750923157,  6.407801151275635,     4.099999904632568,     1.0])
    DeclEvent(0x0000, 0, 107, 0.12999999523162842,   18.799999237060547,    0.0,                   100.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   -0.012999999336898327, -9.399999618530273,    -0.0,                  1.0])

    DeclActor(0,       0,       -1600,   1000,    0,       2500,    0,       0x007C, 1,  24, 0x0000)
    DeclActor(-6130,   -4200,   -21010,  1000,    -6130,   -3200,   -21010,  0x007C, 1,  25, 0x0000)

    PlaceName(-5.449999809265137, 0.0, -2.7200000286102295, 0x0000, 0x0000, "中央広場")
    PlaceName(-70.54000091552734, 0.0, 1.7300000190734863, 0x0000, 0x0000, "西通り")
    PlaceName(21.290000915527344, 0.0, 85.38999938964844, 0x0000, 0x0000, "行政区")
    PlaceName(-130.92999267578125, 0.0, 75.48999786376953, 0x0000, 0x0000, "住宅街")
    PlaceName(-58.65999984741211, 0.0, 67.56999969482422, 0x0000, 0x0000, "歓楽街")
    PlaceName(74.98999786376953, 0.0, -25.489999771118164, 0x0000, 0x0000, "東通り")
    PlaceName(110.13999938964844, 0.0, -79.94000244140625, 0x0000, 0x0000, "旧市街")
    PlaceName(102.70999908447266, 0.0, 39.849998474121094, 0x0000, 0x0000, "港湾区")
    PlaceName(76.97000122070312, 0.0, 132.91000366210938, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(5.690000057220459, 0.0, -71.02999877929688, 0x0000, 0x0000, "駅前通り")
    PlaceName(-40.84000015258789, 0.0, 31.93000030517578, 0x0000, 0x0000, "裏通り")
    PlaceName(2.7200000286102295, 0.0, -101.72000122070312, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(128.4499969482422, 0.0, -11.630000114440918, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-121.02999877929688, 0.0, 0.25, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-115.08999633789062, 0.0, 99.25, 0x0000, 0x0000, "マインツ山道")
    PlaceName(15.0, 0.0, 216.75, 0x0000, 0x0000, "オルキスタワー")
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
        "Function_0_F1C",          # 00, 0
        "Function_1_FCC",          # 01, 1
        "Function_2_10A5",         # 02, 2
        "Function_3_10F2",         # 03, 3
        "Function_4_111D",         # 04, 4
        "Function_5_1148",         # 05, 5
        "Function_6_1173",         # 06, 6
        "Function_7_12BD",         # 07, 7
        "Function_8_2196",         # 08, 8
        "Function_9_2976",         # 09, 9
        "Function_10_2BD0",        # 0A, 10
        "Function_11_2BE0",        # 0B, 11
        "Function_12_3CCF",        # 0C, 12
        "Function_13_3D0C",        # 0D, 13
        "Function_14_3D53",        # 0E, 14
        "Function_15_3D9D",        # 0F, 15
        "Function_16_44F4",        # 10, 16
        "Function_17_466B",        # 11, 17
        "Function_18_46D0",        # 12, 18
        "Function_19_46EC",        # 13, 19
        "Function_20_484A",        # 14, 20
        "Function_21_4893",        # 15, 21
        "Function_22_48A6",        # 16, 22
        "Function_23_4AD6",        # 17, 23
        "Function_24_523A",        # 18, 24
        "Function_25_52DE",        # 19, 25
        "Function_26_59B9",        # 1A, 26
        "Function_27_5A06",        # 1B, 27
        "Function_28_5A6F",        # 1C, 28
        "Function_29_5C55",        # 1D, 29
        "Function_30_5C68",        # 1E, 30
        "Function_31_7758",        # 1F, 31
        "Function_32_7788",        # 20, 32
        "Function_33_77C7",        # 21, 33
        "Function_34_79F2",        # 22, 34
        "Function_35_7B42",        # 23, 35
        "Function_36_818F",        # 24, 36
        "Function_37_81E3",        # 25, 37
        "Function_38_81FC",        # 26, 38
        "Function_39_84EE",        # 27, 39
        "Function_40_8535",        # 28, 40
        "Function_41_8548",        # 29, 41
        "Function_42_8A19",        # 2A, 42
        "Function_43_8A6E",        # 2B, 43
        "Function_44_8AC3",        # 2C, 44
        "Function_45_8B18",        # 2D, 45
        "Function_46_8B6D",        # 2E, 46
        "Function_47_8B9D",        # 2F, 47
        "Function_48_8D75",        # 30, 48
        "Function_49_9147",        # 31, 49
        "Function_50_9A2C",        # 32, 50
        "Function_51_9AA6",        # 33, 51
        "Function_52_9F67",        # 34, 52
        "Function_53_9F9E",        # 35, 53
        "Function_54_9FCF",        # 36, 54
        "Function_55_A000",        # 37, 55
        "Function_56_A031",        # 38, 56
        "Function_57_A062",        # 39, 57
        "Function_58_A093",        # 3A, 58
        "Function_59_A0C4",        # 3B, 59
        "Function_60_A2AB",        # 3C, 60
        "Function_61_A2F3",        # 3D, 61
        "Function_62_A312",        # 3E, 62
        "Function_63_A331",        # 3F, 63
        "Function_64_A365",        # 40, 64
        "Function_65_A3A6",        # 41, 65
        "Function_66_A3E7",        # 42, 66
        "Function_67_A430",        # 43, 67
        "Function_68_AD47",        # 44, 68
        "Function_69_AD84",        # 45, 69
        "Function_70_ADC1",        # 46, 70
        "Function_71_ADFE",        # 47, 71
        "Function_72_AE3B",        # 48, 72
        "Function_73_AE78",        # 49, 73
        "Function_74_AEB5",        # 4A, 74
        "Function_75_AEF2",        # 4B, 75
        "Function_76_AF11",        # 4C, 76
        "Function_77_AF2E",        # 4D, 77
        "Function_78_AFA8",        # 4E, 78
        "Function_79_AFFB",        # 4F, 79
        "Function_80_B04E",        # 50, 80
        "Function_81_B0A1",        # 51, 81
        "Function_82_B0F4",        # 52, 82
        "Function_83_B147",        # 53, 83
        "Function_84_B161",        # 54, 84
        "Function_85_C598",        # 55, 85
        "Function_86_C5D5",        # 56, 86
        "Function_87_C6C5",        # 57, 87
        "Function_88_C70E",        # 58, 88
        "Function_89_C7DE",        # 59, 89
        "Function_90_C8E5",        # 5A, 90
        "Function_91_C8FF",        # 5B, 91
        "Function_92_C931",        # 5C, 92
        "Function_93_C978",        # 5D, 93
        "Function_94_C9BF",        # 5E, 94
        "Function_95_CA14",        # 5F, 95
        "Function_96_CA69",        # 60, 96
        "Function_97_CABE",        # 61, 97
        "Function_98_CCE9",        # 62, 98
        "Function_99_CDE5",        # 63, 99
        "Function_100_CE69",       # 64, 100
        "Function_101_CF5B",       # 65, 101
        "Function_102_D424",       # 66, 102
        "Function_103_D8C4",       # 67, 103
        "Function_104_DF69",       # 68, 104
        "Function_105_E4A5",       # 69, 105
        "Function_106_EBD0",       # 6A, 106
        "Function_107_EC01",       # 6B, 107
        "Function_108_F316",       # 6C, 108
        "Function_109_F473",       # 6D, 109
        "Function_110_FF6C",       # 6E, 110
        "Function_111_10093",      # 6F, 111
        "Function_112_10190",      # 70, 112
        "Function_113_102C6",      # 71, 113
    ))


    def Function_0_F1C(): pass

    label("Function_0_F1C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_F54"),
        (1, "loc_F60"),
        (2, "loc_F6C"),
        (3, "loc_F78"),
        (4, "loc_F84"),
        (5, "loc_F90"),
        (6, "loc_F9C"),
        (SWITCH_DEFAULT, "loc_FA8"),
    )


    label("loc_F54")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F60")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F6C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F78")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F84")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F90")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F9C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_FA8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_FB4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FCB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_FCB")

    Return()

    # Function_0_F1C end

    def Function_1_FCC(): pass

    label("Function_1_FCC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10A4")
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
    Jump("Function_1_FCC")

    label("loc_10A4")

    Return()

    # Function_1_FCC end

    def Function_2_10A5(): pass

    label("Function_2_10A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10F1")
    OP_95(0xFE, 11850, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 11850, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_2_10A5")

    label("loc_10F1")

    Return()

    # Function_2_10A5 end

    def Function_3_10F2(): pass

    label("Function_3_10F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_111C")
    OP_94(0xFE, 0x366, 0xFFFFE296, 0xFFFFF236, 0xFFFFD166, 0x3E8)
    Sleep(300)
    Jump("Function_3_10F2")

    label("loc_111C")

    Return()

    # Function_3_10F2 end

    def Function_4_111D(): pass

    label("Function_4_111D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1147")
    OP_94(0xFE, 0xFFFFA484, 0xFFFFB348, 0xFFFFA722, 0xFFFFB9BA, 0x3E8)
    Sleep(300)
    Jump("Function_4_111D")

    label("loc_1147")

    Return()

    # Function_4_111D end

    def Function_5_1148(): pass

    label("Function_5_1148")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1172")
    OP_94(0xFE, 0xFFFFBE2E, 0x2184, 0xFFFFB38E, 0x1054, 0x3E8)
    Sleep(300)
    Jump("Function_5_1148")

    label("loc_1172")

    Return()

    # Function_5_1148 end

    def Function_6_1173(): pass

    label("Function_6_1173")

    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    SetMapObjFlags(0x19, 0x2000000)
    SetMapObjFlags(0x1A, 0x2000000)
    SetMapObjFlags(0x1B, 0x2000000)
    SetMapObjFlags(0x1C, 0x2000000)
    SetMapObjFlags(0x1D, 0x2000000)
    SetMapObjFlags(0x1E, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_11BD")
    ClearMapObjFlags(0x13, 0x2000000)
    Jump("loc_12BC")

    label("loc_11BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_11D1")
    ClearMapObjFlags(0x15, 0x2000000)
    Jump("loc_12BC")

    label("loc_11D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_11E5")
    ClearMapObjFlags(0xC, 0x2000000)
    Jump("loc_12BC")

    label("loc_11E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1211")
    ClearMapObjFlags(0xC, 0x2000000)
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0x1C, 0x2000000)
    ClearMapObjFlags(0x1D, 0x2000000)
    ClearMapObjFlags(0x1E, 0x2000000)
    Jump("loc_12BC")

    label("loc_1211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1285")
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
    Jump("loc_12BC")

    label("loc_1285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1299")
    ClearMapObjFlags(0x13, 0x2000000)
    Jump("loc_12BC")

    label("loc_1299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_12AD")
    ClearMapObjFlags(0x13, 0x2000000)
    Jump("loc_12BC")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_12BC")
    ClearMapObjFlags(0x13, 0x2000000)

    label("loc_12BC")

    Return()

    # Function_6_1173 end

    def Function_7_12BD(): pass

    label("Function_7_12BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A82")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137F")
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    SetChrPos(0x1, -26950, -1160, -4340, 90)
    SetChrPos(0x2, -26950, -1160, -4340, 90)
    SetChrPos(0x3, -26950, -1160, -4340, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1352")
    SetChrPos(0x4, -26950, -1160, -4340, 90)
    SetChrPos(0x5, -26950, -1160, -4340, 90)
    Jump("loc_1371")

    label("loc_1352")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1371")
    SetChrPos(0x4, -26950, -1160, -4340, 90)

    label("loc_1371")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_137F")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1433")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1406")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_1425")

    label("loc_1406")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1425")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_1425")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_1433")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E7")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14BA")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_14D9")

    label("loc_14BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D9")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_14D9")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_14E7")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159B")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156E")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_158D")

    label("loc_156E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158D")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_158D")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_159B")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164F")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1622")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_1641")

    label("loc_1622")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1641")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_1641")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_164F")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1703")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D6")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_16F5")

    label("loc_16D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F5")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_16F5")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_1703")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B7")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_178A")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_17A9")

    label("loc_178A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17A9")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_17A9")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_17B7")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186B")
    SetChrPos(0x0, 4040, 0, -21980, 0)
    SetChrPos(0x1, 4040, 0, -21980, 0)
    SetChrPos(0x2, 4040, 0, -21980, 0)
    SetChrPos(0x3, 4040, 0, -21980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_183E")
    SetChrPos(0x4, 4040, 0, -21980, 0)
    SetChrPos(0x5, 4040, 0, -21980, 0)
    Jump("loc_185D")

    label("loc_183E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185D")
    SetChrPos(0x4, 4040, 0, -21980, 0)

    label("loc_185D")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_186B")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_191F")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18F2")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_1911")

    label("loc_18F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1911")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_1911")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_191F")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D3")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A6")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_19C5")

    label("loc_19A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C5")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_19C5")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_19D3")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A82")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A5A")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_1A79")

    label("loc_1A5A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A79")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_1A79")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A82")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1AEF")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -4510, 0, -8420, 225)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    BeginChrThread(0xB, 0, 0, 0)
    OP_93(0xC, 0x87, 0x0)
    OP_93(0xD, 0x87, 0x0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1B20")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_1F16")

    label("loc_1B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B66")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -6100, 0, -9410, 90)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -4450, 0, -9880, 270)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_1F16")

    label("loc_1B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B9A")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_1BA4")

    label("loc_1B9A")

    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_1BA4")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -4510, 0, -8420, 180)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_1F16")

    label("loc_1BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C02")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C71")
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
    Jump("loc_1F16")

    label("loc_1C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1CA0")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, -5000, 0, -9410, 270)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CB8")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CE7")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CE2")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)

    label("loc_1CE2")

    Jump("loc_1F16")

    label("loc_1CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D3C")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -6100, 0, -9410, 0)
    SetChrFlags(0xF, 0x10)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, -9410, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1D8B")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xF, -4240, 0, -7750, 225)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_1F16")

    label("loc_1D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E12")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -6100, 0, -9410, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xB, -5000, 0, -9410, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E03")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -24750, 1300, -16680, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E03")
    SetChrFlags(0x12, 0x10)

    label("loc_1E03")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E91")
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4E")
    SetChrChipByIndex(0x11, 0x12)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -26150, -8200, -23200, 180)
    BeginChrThread(0x11, 0, 0, 0)

    label("loc_1E4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E82")
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E82")
    SetChrFlags(0xE, 0x10)

    label("loc_1E82")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1ECE")
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
    Jump("loc_1F16")

    label("loc_1ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EEF")
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_1EEF")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -22230, 1300, -20180, 315)
    BeginChrThread(0x11, 0, 0, 0)
    BeginChrThread(0x10, 0, 0, 0)

    label("loc_1F16")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F30")
    Event(0, 30)

    label("loc_1F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F46")
    SetMapFlags(0x10000000)
    Event(0, 35)

    label("loc_1F46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F73")
    SetMapFlags(0x10000000)
    Event(0, 103)

    label("loc_1F73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FB6")
    SetChrPos(0xC, 4760, 0, 17660, 90)
    SetChrPos(0xD, 6740, 0, 17590, 270)
    SetChrFlags(0x16, 0x80)

    label("loc_1FB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FD1")
    Event(0, 15)

    label("loc_1FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FFC")
    SetMapFlags(0x10000000)
    Event(2, 0)

    label("loc_1FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2013")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1, 4)
    Event(0, 9)
    Jump("loc_2195")

    label("loc_2013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_2027")
    ClearScenarioFlags(0x22, 1)
    Event(0, 16)
    Jump("loc_2195")

    label("loc_2027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_203B")
    ClearScenarioFlags(0x22, 2)
    Event(0, 19)
    Jump("loc_2195")

    label("loc_203B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_204F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 22)
    Jump("loc_2195")

    label("loc_204F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_2066")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x1, 4)
    Event(0, 23)
    Jump("loc_2195")

    label("loc_2066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_207A")
    ClearScenarioFlags(0x22, 5)
    Event(0, 25)
    Jump("loc_2195")

    label("loc_207A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_208E")
    ClearScenarioFlags(0x22, 6)
    Event(0, 28)
    Jump("loc_2195")

    label("loc_208E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_20A5")
    ClearScenarioFlags(0x22, 7)
    SetScenarioFlags(0x1, 4)
    Event(0, 33)
    Jump("loc_2195")

    label("loc_20A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_20B9")
    ClearScenarioFlags(0x23, 0)
    Event(0, 34)
    Jump("loc_2195")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_20CD")
    ClearScenarioFlags(0x23, 1)
    Event(0, 38)
    Jump("loc_2195")

    label("loc_20CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_20E1")
    ClearScenarioFlags(0x23, 2)
    Event(0, 41)
    Jump("loc_2195")

    label("loc_20E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_20F5")
    ClearScenarioFlags(0x23, 3)
    Event(0, 47)
    Jump("loc_2195")

    label("loc_20F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_2109")
    ClearScenarioFlags(0x23, 4)
    Event(0, 48)
    Jump("loc_2195")

    label("loc_2109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 5)), scpexpr(EXPR_END)), "loc_211D")
    ClearScenarioFlags(0x23, 5)
    Event(0, 49)
    Jump("loc_2195")

    label("loc_211D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_2131")
    ClearScenarioFlags(0x23, 6)
    Event(0, 51)
    Jump("loc_2195")

    label("loc_2131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 7)), scpexpr(EXPR_END)), "loc_2145")
    ClearScenarioFlags(0x23, 7)
    Event(0, 59)
    Jump("loc_2195")

    label("loc_2145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 0)), scpexpr(EXPR_END)), "loc_2159")
    ClearScenarioFlags(0x24, 0)
    Event(0, 67)
    Jump("loc_2195")

    label("loc_2159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 1)), scpexpr(EXPR_END)), "loc_216D")
    ClearScenarioFlags(0x24, 1)
    Event(0, 97)
    Jump("loc_2195")

    label("loc_216D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 2)), scpexpr(EXPR_END)), "loc_2186")
    ClearScenarioFlags(0x24, 2)
    SetMapFlags(0x10000000)
    Event(0, 102)
    Jump("loc_2195")

    label("loc_2186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 3)), scpexpr(EXPR_END)), "loc_2195")
    ClearScenarioFlags(0x24, 3)
    Event(0, 101)

    label("loc_2195")

    Return()

    # Function_7_12BD end

    def Function_8_2196(): pass

    label("Function_8_2196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_21AB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 4)

    label("loc_21AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_226F")
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

    label("loc_226F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_231E")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x5A, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)

    label("loc_231E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2380")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x26, 0x82, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)

    label("loc_2380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2398")
    ClearMapFlags(0x2000)
    Jump("loc_239F")

    label("loc_2398")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23F3")
    ClearMapObjFlags(0xF, 0x4)
    OP_78(0xF, 0x1A)
    SetMapObjFlags(0xF, 0x1000)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -7790, 0, 16480, 90)
    OP_D5(0x1A, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0xF, 0x1E)
    OP_70(0xF, 0x0)
    Jump("loc_2458")

    label("loc_23F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_240B")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_2458")

    label("loc_240B")

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

    label("loc_2458")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2472")
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)

    label("loc_2472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_251E")
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

    label("loc_251E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_254D")
    SetMapObjFrame(0xFF, "ibc_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x1, 0x1)
    Jump("loc_256E")

    label("loc_254D")

    SetMapObjFrame(0xFF, "ibc_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x0, 0x1)

    label("loc_256E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_257C")
    Jump("loc_25DD")

    label("loc_257C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2590")
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_25DD")

    label("loc_2590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_259E")
    Jump("loc_25DD")

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25B2")
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_25DD")

    label("loc_25B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_25C0")
    Jump("loc_25DD")

    label("loc_25C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_25D4")
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_25DD")

    label("loc_25D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_25DD")

    label("loc_25DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F6")
    ClearMapObjFlags(0xA, 0x4)
    Jump("loc_25FC")

    label("loc_25F6")

    SetMapObjFlags(0xA, 0x4)

    label("loc_25FC")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2614")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_2614")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_263E")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_263E")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2668")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_2668")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2915")
    OP_10(0x2, 0x0)
    OP_10(0xD, 0x1)
    Jump("loc_291B")

    label("loc_2915")

    OP_10(0x2, 0x1)
    OP_10(0xD, 0x0)

    label("loc_291B")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2961")
    OP_1B(0x0, 0x0, 0x6E)
    OP_1B(0x2, 0x0, 0x6F)
    OP_1B(0x3, 0x0, 0x70)
    OP_1B(0x4, 0x0, 0x71)
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x0)

    label("loc_2961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2975")
    Sound(828, 1, 60, 0)

    label("loc_2975")

    Return()

    # Function_8_2196 end

    def Function_9_2976(): pass

    label("Function_9_2976")

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
            "アルタイル・ロッジにおける\x01",
            "逮捕劇から２日後──\x02",
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

    def lambda_2B9F():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2B9F)
    OP_0D()
    OP_6F(0x79)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_2976 end

    def Function_10_2BD0(): pass

    label("Function_10_2BD0")

    Sound(458, 0, 100, 0)
    Sleep(4000)
    Sound(494, 0, 50, 0)
    Return()

    # Function_10_2BD0 end

    def Function_11_2BE0(): pass

    label("Function_11_2BE0")

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

    def lambda_2D31():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D31)
    Sleep(100)

    def lambda_2D4E():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D4E)
    Sleep(100)

    def lambda_2D6B():
        OP_97(0x1A5, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A5, 0, lambda_2D6B)
    Sleep(100)

    def lambda_2D88():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D88)
    Sleep(100)

    def lambda_2DA5():
        OP_97(0x105, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2DA5)
    Sound(835, 2, 60, 0)
    OP_68(0, 1100, -7700, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)

    #N0002
    NpcTalk(
        0x1B,
        "男の子の声",
        "おーい、キーア！\x02",
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

    def lambda_2ED6():

        label("loc_2ED6")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2ED6")

    QueueWorkItem2(0x101, 2, lambda_2ED6)

    def lambda_2EE8():

        label("loc_2EE8")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2EE8")

    QueueWorkItem2(0x102, 2, lambda_2EE8)

    def lambda_2EFA():

        label("loc_2EFA")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2EFA")

    QueueWorkItem2(0x1A5, 2, lambda_2EFA)

    def lambda_2F0C():

        label("loc_2F0C")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2F0C")

    QueueWorkItem2(0x109, 2, lambda_2F0C)

    def lambda_2F1E():

        label("loc_2F1E")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2F1E")

    QueueWorkItem2(0x105, 2, lambda_2F1E)
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
        "#12P#01110Fあ、リュウにアンリ！\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x1B,
        (
            "#5Pおっせーよ、パン屋の前で\x01",
            "待ち合わせだったろー！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x1C,
        "#5Pそろそろ授業が始まるよ？\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x1A5,
        "#12P#01109Fえへへ、ゴメンゴメン。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00002Fやあ、リュウにアンリ。\x01",
            "相変わらず元気だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#12P#00109Fふふ、いつもキーアちゃんと\x01",
            "仲良くしてくれてありがとう。\x02",
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
        "#5Pあ、おひさしぶりです！\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x1B,
        "#5Pへへ、久しぶりじゃん。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x1B,
        (
            "#5Pキーアから聞いたけど\x01",
            "支援課、また始めんだってな？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00004Fああ、おかげさまでね。\x02\x03",

            "#00000F色々パワーアップしているから\x01",
            "楽しみにしててくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x1B,
        "#5Pへへ、言うじゃんか。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x1B,
        (
            "#5Pま、今の兄ちゃんたちだったら\x01",
            "遊撃士と同じくらいは\x01",
            "認めてやってもいいかな～。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    #C0015
    ChrTalk(
        0x1C,
        "#11Pだからリュウ、偉そうだってば～。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x109,
        "#10109Fクスクス……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x105,
        (
            "#12P#10304Fさすが支援課。\x01",
            "子供にも大人気みたいだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1C, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    def lambda_3291():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_3291)
    Sleep(1000)

    #C0018
    ChrTalk(
        0x1B,
        "#5Pあれ、そっちの姉ちゃんたちは……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x1C,
        "#5P見かけない顔、ですね。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x1C,
        (
            "#5Pそういえばティオさんに\x01",
            "ランディさんもいないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#12P#00104F２人は用事があって\x01",
            "まだ戻ってきていないの。\x02\x03",

            "#00100Fこちらは、ノエルさんにワジ君。\x01",
            "支援課の新人さんたちなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x109,
        "#10102Fふふっ、よろしくね！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x1B,
        "#5Pおお、よろしく！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x1B,
        (
            "#5P……って、あれ。\x01",
            "そっちはオトコなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x1B,
        (
            "#5Pなんかオンナみたいな\x01",
            "カオしてるけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    #C0026
    ChrTalk(
        0x1C,
        "#11Pちょ、ちょっとリュウ！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x105,
        (
            "#12P#10309Fフフ、どうだろうね？\x02\x03",

            "#10302F君が女だと思うんだったら\x01",
            "その通りかもしれないよ？\x02",
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
            "#00006F……だからワジ。\x01",
            "子供を惑わすんじゃない。\x02\x03",

            "#00000Fそれより３人とも\x01",
            "急がなくていいのか？\x02",
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

    def lambda_3585():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1A5, 2, lambda_3585)
    Sleep(50)

    def lambda_3595():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_3595)
    Sleep(150)

    #C0030
    ChrTalk(
        0x1A5,
        (
            "#6P#01105Fあ、そーだった。\x02\x03",

            "#01109Fそれじゃあみんな！\x01",
            "お仕事がんばってねー！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A5, 500)

    def lambda_35FE():

        label("loc_35FE")

        TurnDirection(0xFE, 0x1A5, 500)
        Yield()
        Jump("loc_35FE")

    QueueWorkItem2(0x101, 2, lambda_35FE)

    #C0031
    ChrTalk(
        0x101,
        "#00009Fああ、キーアも頑張れよ。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        "#12P#00102F車には気を付けてね？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x1A5,
        "#6P#01110Fうんっ！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x1B,
        (
            "#5Pよーし、そんじゃ\x01",
            "モモん家に寄ってくか。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x1C,
        "#5Pうん、急ごう！\x02",
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
            "#11P#10109Fふふっ……\x01",
            "元気な子たちですね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0037
    ChrTalk(
        0x105,
        "#11P#10300F西通りに住んでる子かい？\x02",
    )

    CloseMessageWindow()

    def lambda_3797():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3797)
    Sleep(50)
    TurnDirection(0x102, 0x101, 500)

    #C0038
    ChrTalk(
        0x101,
        (
            "#6P#00002Fああ、もう一人は\x01",
            "住宅街に住んでるんだけどね。\x02\x03",

            "#00004F──さてと。\x01",
            "俺たちも仕事を始めよう。\x02\x03",

            "#00000Fとりあえず、そこのオーバルストアと\x01",
            "警察本部には寄るとして……\x02\x03",

            "できれば市内も一通り\x01",
            "回ってみた方がいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x109,
        (
            "#11P#10100Fなるほど。\x01",
            "パトロールというわけですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#12P#00104Fふふ、そこまで\x01",
            "大げさなものじゃないけど……\x02\x03",

            "#00100F意外な情報が入ってきたりするから\x01",
            "巡回も大事だったりするのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#6P#00000Fしばらくしたら課長から\x01",
            "エニグマに連絡が入るだろう。\x02\x03",

            "それまでに市内で\x01",
            "気になる場所に行っておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        "#11P#10102F了解しました。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        "#11P#10304Fフフ、それじゃあ行こうか。\x02",
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
            "クロスベル市内の地図が利用可能になりました。\x02",
        )
    )

    CloseMessageWindow()

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "市内のフィールド上でSTARTボタンを押すと\x01",
            "街の全体マップを開くことができます。\x01",
            "（もう一度STARTボタンを押すと\x01",
            "  自治州の地図を表示します。）\x02",
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
            "また、市内では地図を利用して\x01",
            "エリア単位でショートカット移動を\x01",
            "することが可能です。\x02",
        )
    )

    CloseMessageWindow()

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "左側の街区リストから\x01",
            "行きたいエリアを選択してください。\x02",
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
            "ただし、状況によっては\x01",
            "市街地図が使えない場合もあります。\x02",
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

    # Function_11_2BE0 end

    def Function_12_3CCF(): pass

    label("Function_12_3CCF")


    def lambda_3CD4():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CD4)
    WaitChrThread(0xFE, 1)

    def lambda_3CF2():
        OP_95(0xFE, -3400, 0, -5700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CF2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_3CCF end

    def Function_13_3D0C(): pass

    label("Function_13_3D0C")

    Sleep(50)

    def lambda_3D14():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D14)
    WaitChrThread(0xFE, 1)

    def lambda_3D32():
        OP_95(0xFE, -2800, 0, -4800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D32)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_13_3D0C end

    def Function_14_3D53(): pass

    label("Function_14_3D53")

    OP_92(0xFE, 0xFFFFE318, 0xFFFFF31C, 0x1F4)

    def lambda_3D65():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D65)
    WaitChrThread(0xFE, 1)

    def lambda_3D83():
        OP_95(0xFE, -17400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D83)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_3D53 end

    def Function_15_3D9D(): pass

    label("Function_15_3D9D")

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

    def lambda_3ED0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3ED0)
    Sleep(50)

    def lambda_3EE0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3EE0)
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
        "#11P#00005Fあっと、課長かな？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#6P#00102Fそろそろ掛かってきても\x01",
            "おかしくない時間ね。\x02",
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
            "#00000Fはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0052
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

    #A0053
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

    #A0054
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

    #A0055
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

    #A0056
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

    #A0057
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

    #A0058
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
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0059
    ChrTalk(
        0x102,
        "#6P#00100Fやっぱり課長だったみたいね。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x109,
        (
            "#12P#10105F何か気になることを\x01",
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

    #C0061
    ChrTalk(
        0x101,
        (
            "#11P#00006Fああ、課長も色々と\x01",
            "状況の変化を感じているらしい。\x02\x03",

            "#00001F黒月やレクター大尉のことも\x01",
            "報告した方が良さそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        "#6P#00106Fそうね……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        (
            "#5P#10300Fで、そろそろ\x01",
            "警察学校に行くのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#11P#00000Fああ、西口から街道に出よう。\x02",
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

    # Function_15_3D9D end

    def Function_16_44F4(): pass

    label("Function_16_44F4")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45F9")
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    EndChrThread(0xA, 0xFF)
    SetChrPos(0xA, -6880, 0, 810, 0)

    def lambda_45C5():

        label("loc_45C5")

        TurnDirection(0xFE, 0x2D, 500)
        Yield()
        Jump("loc_45C5")

    QueueWorkItem2(0xA, 2, lambda_45C5)
    SetChrPos(0xB, -6300, 0, -170, 0)
    EndChrThread(0xB, 0xFF)

    def lambda_45EC():

        label("loc_45EC")

        TurnDirection(0xFE, 0x2D, 500)
        Yield()
        Jump("loc_45EC")

    QueueWorkItem2(0xB, 2, lambda_45EC)

    label("loc_45F9")

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

    # Function_16_44F4 end

    def Function_17_466B(): pass

    label("Function_17_466B")

    SetChrPos(0xFE, -35510, -2590, -4520, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -23860, -640, -4420)
    OP_9F(0x1, -14350, 750, -1880)
    OP_9F(0x1, -11380, 0, 7200)
    OP_9F(0x1, -14250, 0, 13970)
    OP_9F(0x1, -28100, 0, 29400)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_17_466B end

    def Function_18_46D0(): pass

    label("Function_18_46D0")

    Sound(458, 0, 100, 0)
    Sound(468, 2, 100, 0)
    Sleep(5000)
    Sound(494, 0, 60, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_46D0 end

    def Function_19_46EC(): pass

    label("Function_19_46EC")

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

    # Function_19_46EC end

    def Function_20_484A(): pass

    label("Function_20_484A")

    Sleep(1500)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 11000, 0, 30000)
    OP_9F(0x1, 8580, 0, 4180)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 4700, 0, -30500)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_20_484A end

    def Function_21_4893(): pass

    label("Function_21_4893")

    Sleep(2300)
    Sound(458, 0, 70, 0)
    Sleep(4300)
    Sound(494, 0, 70, 0)
    Return()

    # Function_21_4893 end

    def Function_22_48A6(): pass

    label("Function_22_48A6")

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

    # Function_22_48A6 end

    def Function_23_4AD6(): pass

    label("Function_23_4AD6")

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
            "      七耀暦１２０４年──初秋。\x02\x03",

            "新クロスベル市長にして、ＩＢＣ総裁、\x01",
            "ディーター・クロイスが提唱した\x01",
            "『西ゼムリア通商会議』が始まった。\x02\x03",

            "西の大国、エレボニア帝国からは\x01",
            "《鉄血宰相》ギリアス・オズボーンに加え、\x01",
            "粋人#4Rすいじん#として知られるオリヴァルト皇子──\x02\x03",

            "東の大国、カルバード共和国からは\x01",
            "庶民派として支持を集めている\x01",
            "サミュエル・ロックスミス大統領──\x02\x03",

            "北東にあるレミフェリア公国からは\x01",
            "若くして国を治めるアルバート大公──\x02\x03",

            "南西にあるリベール王国からは\x01",
            "女王代理としてクローディア王太女──\x02\x03",

            "いずれも国賓クラスのＶＩＰたちが\x01",
            "今まさにクロスベルに集まりつつあった。\x02",
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

    # Function_23_4AD6 end

    def Function_24_523A(): pass

    label("Function_24_523A")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5272"),
        (1, "loc_527A"),
        (2, "loc_5282"),
        (3, "loc_528A"),
        (4, "loc_5292"),
        (5, "loc_529A"),
        (6, "loc_52A2"),
        (SWITCH_DEFAULT, "loc_52AA"),
    )


    label("loc_5272")

    Sleep(100)
    Jump("loc_52B2")

    label("loc_527A")

    Sleep(200)
    Jump("loc_52B2")

    label("loc_5282")

    Sleep(300)
    Jump("loc_52B2")

    label("loc_528A")

    Sleep(400)
    Jump("loc_52B2")

    label("loc_5292")

    Sleep(500)
    Jump("loc_52B2")

    label("loc_529A")

    Sleep(600)
    Jump("loc_52B2")

    label("loc_52A2")

    Sleep(700)
    Jump("loc_52B2")

    label("loc_52AA")

    Sleep(800)
    Jump("loc_52B2")

    label("loc_52B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52DD")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_52B2")

    label("loc_52DD")

    Return()

    # Function_24_523A end

    def Function_25_52DE(): pass

    label("Function_25_52DE")

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

    # Function_25_52DE end

    def Function_26_59B9(): pass

    label("Function_26_59B9")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 35000, 0, -4000)
    OP_9F(0x1, 11500, 0, 1000)
    OP_9F(0x1, 12000, 0, 30000)
    OP_9F(0x2, 0xFE, 7000, 0x6)

    def lambda_59F5():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_59F5)
    Return()

    # Function_26_59B9 end

    def Function_27_5A06(): pass

    label("Function_27_5A06")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3700, 0, -20000)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 10580, 0, 4180)
    OP_9F(0x1, 12000, 0, 10000)
    OP_9F(0x1, 12000, 0, 15000)
    OP_9F(0x2, 0xFE, 7000, 0x6)

    def lambda_5A5E():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5A5E)
    Return()

    # Function_27_5A06 end

    def Function_28_5A6F(): pass

    label("Function_28_5A6F")

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

    def lambda_5BE6():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_5BE6)
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

    # Function_28_5A6F end

    def Function_29_5C55(): pass

    label("Function_29_5C55")

    Sleep(500)
    Sound(458, 0, 80, 0)
    Sleep(3600)
    Sound(494, 0, 50, 0)
    Return()

    # Function_29_5C55 end

    def Function_30_5C68(): pass

    label("Function_30_5C68")

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

    def lambda_5F16():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5F16)
    Sleep(50)

    def lambda_5F26():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5F26)
    Sleep(50)

    def lambda_5F36():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5F36)
    Sleep(50)

    def lambda_5F46():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5F46)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    #C0067
    ChrTalk(
        0x101,
        "#5P#00005Fあれ……？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        "#00105F#5P鳥の鳴き声？\x02",
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

    def lambda_607A():

        label("loc_607A")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_607A")

    QueueWorkItem2(0x1E, 2, lambda_607A)

    def lambda_608C():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFE9BC, 0xFFFF9A70, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_608C)
    Sound(847, 2, 70, 0)
    WaitChrThread(0x1E, 1)
    BeginChrThread(0x1E, 3, 0, 31)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_60CE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_60CE)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_60F6():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_60F6)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_611E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_611E)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6146():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6146)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_616E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_616E)
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
        "#00011F#6P#Nな、なんだ！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0070
    ChrTalk(
        0x109,
        "#10111F#6P#Nし、白いタカ……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0071
    ChrTalk(
        0x105,
        (
            "#10305F#12P……いや\x01",
            "ハヤブサみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        (
            "#00301F#6Pおいおい、何だって\x01",
            "こんな街のど真ん中に……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x1E, 0x3)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x1E, 0x0)
    OP_68(-27800, -6900, -26700, 3000)
    MoveCamera(37, 19, 0, 3000)

    def lambda_62AA():
        OP_9E(0xFE, 0xFFFF97B4, 0xFFFF9A70, 0x493E0, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_62AA)
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

    def lambda_644B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_644B)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B8A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BBC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BEE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_6494():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6494)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C20), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C52), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C84), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1CB6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_64DD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_64DD)
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

    def lambda_65DB():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFE2B4, 0xFFFF93CC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_65DB)
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
            "ピューイ。\x02\x03",

            "ピュイ、ピュイ、ピューイ。\x02",
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
            "#5P#00001Fも、もしかして……\x01",
            "俺たちに何か用があるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#00108F#11Pツァイトが話しかける時と\x01",
            "同じような感じだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#00306F#5Pうーん、ティオすけがいたら\x01",
            "何喋ってんのか判りそうだが……\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    ClearChrFlags(0x1D, 0x80)

    def lambda_681B():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA628, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_681B)

    def lambda_6835():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_6835)
    WaitChrThread(0x1D, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    #C0077
    ChrTalk(
        0x1D,
        "#01105F#5Pあれー、どうしたのー？\x02",
    )

    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    CloseMessageWindow()
    OP_63(0x1D, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1D, 0x22)
    SetChrSubChip(0x1D, 0x0)

    def lambda_68AE():
        OP_96(0xFE, 0xFFFF90AC, 0xFFFFDFF8, 0xFFFF9750, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_68AE)
    Sleep(300)

    def lambda_68CB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_68CB)
    Sleep(100)

    def lambda_68DB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_68DB)
    Sleep(100)

    def lambda_68EB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_68EB)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    OP_93(0x1D, 0x87, 0x1F4)
    #Sound(3029, 255, 100, 0)    #voice#KeA

    #C0078
    ChrTalk(
        0x1D,
        (
            "#6P#01110Fわぁ、白いトリだぁ！\x02\x03",

            "#01109Fクチバシも尖ってて\x01",
            "カッコイイー！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x13B, 0x1F4)
    Sleep(300)

    #C0079
    ChrTalk(
        0x1E,
        (
            "#11P#08009Fピューイ㈱\x02\x03",

            "#08000Fピュイイ、ピュイ、ピュイ♪\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x1D,
        (
            "#6P#01103Fふむ、ふむ。\x02\x03",

            "#01102Fなるほど、そうなんだー。\x02",
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
            "#5P#00012F（キーア……\x01",
            "  やっぱり判るのかな？）\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x109,
        "#10112F#5P（ス、スゴイですね……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x101, 500)

    def lambda_6AC3():

        label("loc_6AC3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6AC3")

    QueueWorkItem2(0x1D, 2, lambda_6AC3)

    #C0083
    ChrTalk(
        0x1D,
        (
            "#6P#01100Fえっとね、この子、\x01",
            "『ジーク』っていうんだってー。\x02\x03",

            "ロイドたちに伝言があるから\x01",
            "受け取ってって言ってるよー？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#5P#00011Fそ、そうなのか……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x1E, 500)

    #C0085
    ChrTalk(
        0x104,
        (
            "#00305F#5Pお、確かに脚のところに\x01",
            "メモが括りつけてあるな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6BB7():
        OP_95(0xFE, -27600, -8200, -26600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BB7)
    TurnDirection(0x1E, 0x101, 500)
    Sleep(300)

    def lambda_6BDB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6BDB)
    WaitChrThread(0x101, 1)
    EndChrThread(0x1D, 0x2)
    SetChrName("")

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは白ハヤブサの脚に\x01",
            "括りつけてあったメモを取った。\x07\x00\x02",
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
            "拝啓　クロスベル警察、特務支援課様\x02\x03",

            "皆様の評判を耳にして\x01",
            "不躾#4Rぶしつけ#ですが連絡させていただきました。\x02\x03",

            "もしお時間があれば内密に\x01",
            "相談に乗っていただけないでしょうか。\x02\x03",

            "本日夕刻、クロスベル空港、\x01",
            "待合いテラスにてお待ちしております。\x02\x03",

            "追伸　もしご都合がつかない場合も\x01",
            "ご返答は頂かなくて結構です。\x07\x00\x02",
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
        "#00101F#11Pこ、これって……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0090
    AnonymousTalk(
        0x109,
        (
            "#10106F#5P内容といい、差出人不明といい\x01",
            "怪しすぎますけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0091
    AnonymousTalk(
        0x105,
        (
            "#10302F#11Pでも、綺麗な筆跡だし、\x01",
            "文章も丁寧な感じだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0092
    AnonymousTalk(
        0x104,
        (
            "#00301F#5P何よりも、メモに押されてる\x01",
            "その白ハヤブサの紋章は……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0093
    AnonymousTalk(
        0x1E,
        (
            "#08000F#12Pピューイ。\x02\x03",

            "ピュイ、ピュイ、ピューイ。\x02",
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

    def lambda_6F79():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFE4A8, 0xFFFF93CC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6F79)
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

    def lambda_6FFF():

        label("loc_6FFF")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_6FFF")

    QueueWorkItem2(0x1E, 2, lambda_6FFF)
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

    def lambda_7234():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFEF98, 0xFFFF64EC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7234)
    Sleep(300)

    def lambda_7251():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_7251)
    Sleep(100)

    def lambda_7261():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7261)
    Sleep(100)

    def lambda_7271():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7271)
    Sleep(100)

    def lambda_7281():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7281)
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
            "#11P#00011Fえっと……\x01",
            "キーア、彼はなんて？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x101, 500)

    #C0095
    ChrTalk(
        0x1D,
        (
            "#6P#01111Fんー、行くか行かないかは\x01",
            "ロイドたち次第だってー。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        "#11P#00003Fそうか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_7401():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7401)
    Sleep(50)

    def lambda_7411():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7411)
    Sleep(50)

    def lambda_7421():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7421)
    Sleep(50)

    def lambda_7431():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7431)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0097
    ChrTalk(
        0x102,
        (
            "#00108F#11Pど、どうするの？\x02\x03",

            "#00101Fまさかそんな訳は\x01",
            "無いとは思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        "#00306F#5Pああ、さすがになぁ。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x109,
        (
            "#10108F#5Pでも、白ハヤブサの紋章って……\x01",
            "今の子もそうだったみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x105,
        (
            "#10309F#11Pあはは、いやが上にも\x01",
            "期待しちゃうよねぇ。\x02",
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
            "#6P#00003F──せっかくのお誘いだ。\x01",
            "ここはお受けしておこう。\x02\x03",

            "#00000Fまだ夕方まで時間はあるから\x01",
            "用事を済ませてからでもいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        "#00106F#11Pわ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x109,
        "#10106F#5Pき、緊張してきました……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x104,
        (
            "#00309F#5Pまあ、さすがに正装して\x01",
            "行く必要はないだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x105,
        (
            "#10302F#11Pフフ、それじゃあ用が済んだら\x01",
            "南口のクロスベル空港に行こうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x2D, 0x1F4)
    Sleep(150)

    #C0106
    ChrTalk(
        0x1D,
        (
            "#6P#01110Fよく分からないけど\x01",
            "みんな、がんばってねー。\x02",
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

    # Function_30_5C68 end

    def Function_31_7758(): pass

    label("Function_31_7758")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7787")

    def lambda_7768():
        OP_9E(0xFE, 0xFFFF99A8, 0xFFFF9A70, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7768)
    WaitChrThread(0x1E, 1)
    Jump("Function_31_7758")

    label("loc_7787")

    Return()

    # Function_31_7758 end

    def Function_32_7788(): pass

    label("Function_32_7788")


    def lambda_778D():
        OP_9E(0xFE, 0xFFFF9494, 0xFFFF93CC, 0x2BF20, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_778D)
    WaitChrThread(0x1E, 1)

    def lambda_77AC():
        OP_9E(0xFE, 0xFFFF90AC, 0xFFFF93CC, 0x57E40, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_77AC)
    WaitChrThread(0x1E, 1)
    Return()

    # Function_32_7788 end

    def Function_33_77C7(): pass

    label("Function_33_77C7")

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
            "#1K翌日、８：００──\x02",
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

    def lambda_7978():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_7978)
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

    # Function_33_77C7 end

    def Function_34_79F2(): pass

    label("Function_34_79F2")

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

    # Function_34_79F2 end

    def Function_35_7B42(): pass

    label("Function_35_7B42")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D28")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)

    def lambda_7CF7():

        label("loc_7CF7")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7CF7")

    QueueWorkItem2(0xA, 2, lambda_7CF7)

    def lambda_7D09():

        label("loc_7D09")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7D09")

    QueueWorkItem2(0xB, 2, lambda_7D09)

    def lambda_7D1B():

        label("loc_7D1B")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7D1B")

    QueueWorkItem2(0x13, 2, lambda_7D1B)

    label("loc_7D28")

    OP_68(-13300, 1500, 14200, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17000, 3000)

    def lambda_7D6D():
        OP_9B(0x0, 0x101, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7D6D)
    Sleep(50)

    def lambda_7D85():
        OP_9B(0x0, 0x102, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7D85)
    Sleep(50)

    def lambda_7D9D():
        OP_9B(0x0, 0x103, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7D9D)
    Sleep(50)

    def lambda_7DB5():
        OP_9B(0x0, 0x104, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7DB5)
    Sleep(50)

    def lambda_7DCD():
        OP_9B(0x0, 0x105, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7DCD)
    Sleep(50)

    def lambda_7DE5():
        OP_9B(0x0, 0x109, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7DE5)
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
        "#00005F#5Pこの音は……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        "#00201F#5Pサイレンの音、ですね。\x02",
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
        "#10101F#5P救急車が３台も……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#00108F#5Pやっぱり脱線事故の怪我人を\x01",
            "搬送しているのかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x105,
        (
            "#10303F#5Pま、このタイミングだし\x01",
            "間違いないんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#00006F#5P……セシル姉たちも\x01",
            "忙しい事になりそうだな。\x02\x03",

            "#00001F俺たちも現場へ急ごう。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        "#00301F#5Pおお。\x02",
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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8161")
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

    label("loc_8161")

    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 6)
    OP_24(0x3B2)
    EventEnd(0x5)
    Return()

    # Function_35_7B42 end

    def Function_36_818F(): pass

    label("Function_36_818F")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13000, 500, -2870)
    OP_9F(0x1, -350, 0, -7080)
    OP_9F(0x1, 4300, 0, -18000)
    OP_9F(0x1, 4500, 0, -30000)
    OP_9F(0x1, 4500, 0, -40000)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_36_818F end

    def Function_37_81E3(): pass

    label("Function_37_81E3")

    Sound(465, 0, 80, 0)
    Sleep(4000)
    Sound(458, 0, 100, 0)
    Sleep(3000)
    Sound(465, 0, 80, 0)
    Return()

    # Function_37_81E3 end

    def Function_38_81FC(): pass

    label("Function_38_81FC")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_83E1")
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0x13, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)

    def lambda_83B0():

        label("loc_83B0")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_83B0")

    QueueWorkItem2(0xA, 2, lambda_83B0)

    def lambda_83C2():

        label("loc_83C2")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_83C2")

    QueueWorkItem2(0xB, 2, lambda_83C2)

    def lambda_83D4():

        label("loc_83D4")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_83D4")

    QueueWorkItem2(0x13, 2, lambda_83D4)

    label("loc_83E1")

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

    # Function_38_81FC end

    def Function_39_84EE(): pass

    label("Function_39_84EE")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13630, 0, 14510)
    OP_9F(0x1, -11670, 0, 9100)
    OP_9F(0x1, -12500, 0, 4800)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x8)
    OP_79(0x8)
    Return()

    # Function_39_84EE end

    def Function_40_8535(): pass

    label("Function_40_8535")

    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(3000)
    Sound(492, 0, 50, 0)
    Return()

    # Function_40_8535 end

    def Function_41_8548(): pass

    label("Function_41_8548")

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
            "#6P#10302Fさてと、歓楽街のカジノに\x01",
            "旧市街の２軒だったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        (
            "#00003F#11Pああ、他の場所にも手がかりが\x01",
            "あるかもしれないけど……\x02\x03",

            "#00001Fとりあえず市外に\x01",
            "出ている暇はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#6P#00200F幸い、今朝は新たな支援要請が\x01",
            "来てなかったみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#12P#00103F多分、昨日の事件の影響で\x01",
            "本部も混乱してるんでしょうね。\x02\x03",

            "#00101F警備隊もかなりの\x01",
            "被害を受けたみたいだし……\x02",
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

    def lambda_8864():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8864)

    def lambda_8871():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8871)
    Sleep(50)

    def lambda_8881():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8881)
    Sleep(50)

    def lambda_8891():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8891)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    #C0120
    ChrTalk(
        0x102,
        (
            "#12P#00106F……ごめんなさい。\x02\x03",

            "#00108F貴女の立場からしたら\x01",
            "他人事じゃないわよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x109,
        (
            "#10112F#5P……いえ、そうした危険も\x01",
            "警備隊#6Rあたしたち#の職分ですから。\x02\x03",

            "#10100Fそれに今はあくまで\x01",
            "特務支援課の一員です。\x02\x03",

            "行きましょう……\x01",
            "ランディ先輩を捕まえに！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#00002F#11P……ああ！\x02",
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

    # Function_41_8548 end

    def Function_42_8A19(): pass

    label("Function_42_8A19")


    def lambda_8A1E():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8A1E)

    def lambda_8A38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8A38)
    WaitChrThread(0xFE, 1)

    def lambda_8A4D():
        OP_95(0xFE, -27400, -8200, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8A4D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_42_8A19 end

    def Function_43_8A6E(): pass

    label("Function_43_8A6E")


    def lambda_8A73():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8A73)

    def lambda_8A8D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8A8D)
    WaitChrThread(0xFE, 1)

    def lambda_8AA2():
        OP_95(0xFE, -28000, -8200, -26200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8AA2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_43_8A6E end

    def Function_44_8AC3(): pass

    label("Function_44_8AC3")


    def lambda_8AC8():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8AC8)

    def lambda_8AE2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8AE2)
    WaitChrThread(0xFE, 1)

    def lambda_8AF7():
        OP_95(0xFE, -29400, -8200, -26200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8AF7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_44_8AC3 end

    def Function_45_8B18(): pass

    label("Function_45_8B18")


    def lambda_8B1D():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8B1D)

    def lambda_8B37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8B37)
    WaitChrThread(0xFE, 1)

    def lambda_8B4C():
        OP_95(0xFE, -30000, -8200, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8B4C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_45_8B18 end

    def Function_46_8B6D(): pass

    label("Function_46_8B6D")


    def lambda_8B72():
        OP_95(0xFE, -28700, -8200, -23700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8B72)

    def lambda_8B8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8B8C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_8B6D end

    def Function_47_8B9D(): pass

    label("Function_47_8B9D")

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

    def lambda_8D3E():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8D3E)
    Sleep(4000)
    StopSound(835, 1000, 100)
    StopSound(457, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_8B9D end

    def Function_48_8D75(): pass

    label("Function_48_8D75")

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
    SetChrName("ディーター大統領")

    #A0123
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その意志は、つい先日も、\x01",
            "このクロスベルを恐怖と哀しみの\x01",
            "どん底に叩き落としました。\x02\x03",

            "聡明な市民諸君ならば薄々、\x01",
            "気付かれていると思いますが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_70(0x9, 0x2)
    Sleep(600)
    SetMessageWindowPos(0, 100, -1, -1)
    SetChrName("ディーター大統領")

    #A0124
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "私はあえて、今日この場で\x01",
            "その勢力を名指しで弾劾しましょう。\x02\x03",

            "『エレボニア帝国政府』……\x01",
            "それがその邪悪な意志の一つです。\x02",
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

    # Function_48_8D75 end

    def Function_49_9147(): pass

    label("Function_49_9147")

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

    def lambda_9241():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9241)
    Sleep(50)

    def lambda_925E():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_925E)
    Sleep(50)

    def lambda_927B():
        OP_97(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_927B)
    Sleep(50)

    def lambda_9298():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9298)
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

    def lambda_932B():
        TurnDirection(0x101, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_932B)
    Sleep(50)

    def lambda_933B():
        TurnDirection(0x103, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_933B)
    Sleep(50)

    def lambda_934B():
        TurnDirection(0x104, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_934B)
    Sleep(50)

    def lambda_935B():
        TurnDirection(0x102, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_935B)
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
        "#00005F#11Pキーア？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0126
    ChrTalk(
        0x1D,
        "#6P#01123F#3623V#30W#15A～～～っ～～～……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_24(0xE27)
    OP_C9(0x1, 0x80000000)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)

    def lambda_93ED():
        OP_96(0xFE, 0xFFFFA498, 0xFFFFDFF8, 0xFFFF9F84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_93ED)
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

    def lambda_9474():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9474)

    def lambda_948D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_948D)

    def lambda_949A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_949A)
    OP_6F(0x79)
    SetCameraDistance(12500, 50000)

    #C0127
    ChrTalk(
        0x101,
        "#11P#00011Fわわっ……！\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        "#12P#00205Fキーア……？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        "#00105Fど、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#00302F#11P確かに色々起きてるが\x01",
            "心配することはねえんだぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x1D,
        "#5P#01114F#30W………うん……………\x02",
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
            "#11P#00004F……大丈夫だ、キーア。\x02\x03",

            "#00008F確かにこの先、\x01",
            "クロスベルがどうなるか\x01",
            "分からない状況だけど……\x02\x03",

            "#00002F俺たちがいつだって\x01",
            "キーアの元に帰ってくるのは\x01",
            "絶対に変わらないからさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0x1D,
        "#5P#01105F#30Wロイド……\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x103,
        (
            "#12P#00204Fそうですね……\x01",
            "それだけは確かです。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        (
            "#00302F#11P前に俺たちが出かけた時も\x01",
            "ちゃんと帰って来ただろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x102,
        (
            "#00109Fだからキーアちゃん。\x01",
            "安心して待っててちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x1D,
        "#5P#01121F#40Wエリィ、ティオ、ランディ……\x02",
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

    def lambda_97D4():
        OP_96(0xFE, 0xFFFFA36C, 0xFFFFDFF8, 0xFFFF9F84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_97D4)
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
            "#3624V#30Wうん……#800W！\x01",
            "#30Wみんな、気を付けてね！\x02",
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
            "ワジがパーティメンバーから\x01",
            "外れました。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9969")
    Jump("loc_996E")

    label("loc_9969")

    OP_29(0x8E, 0x4, 0x40)

    label("loc_996E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_997F")
    Jump("loc_9984")

    label("loc_997F")

    OP_29(0x8F, 0x4, 0x40)

    label("loc_9984")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9995")
    Jump("loc_999A")

    label("loc_9995")

    OP_29(0x90, 0x4, 0x40)

    label("loc_999A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_99AB")
    Jump("loc_99B0")

    label("loc_99AB")

    OP_29(0x91, 0x4, 0x40)

    label("loc_99B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_99C1")
    Jump("loc_99C6")

    label("loc_99C1")

    OP_29(0x92, 0x4, 0x40)

    label("loc_99C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_99D7")
    Jump("loc_99DC")

    label("loc_99D7")

    OP_29(0x93, 0x4, 0x40)

    label("loc_99DC")

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

    # Function_49_9147 end

    def Function_50_9A2C(): pass

    label("Function_50_9A2C")

    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)

    def lambda_9A54():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA240, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9A54)

    def lambda_9A6E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9A6E)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    def lambda_9A9D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9A9D)
    Return()

    # Function_50_9A2C end

    def Function_51_9AA6(): pass

    label("Function_51_9AA6")

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
    SetChrName("マクダエル議長")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W皆さんもご存知の通り──\x02\x03",

            "先日、前クロイス市長により\x01",
            "『クロスベル独立国』の創立が\x01",
            "宣言されました。\x02\x03",

            "国防軍という軍事組織も設立され、\x01",
            "新たな体制に慣れつつある人も\x01",
            "いるかとは思いますが……\x02",
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
    SetChrName("マクダエル議長")

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W──ですが皆さん！\x01",
            "今一度、考えて頂きたいのです！\x02\x03",

            "果たして我々は、この事態を\x01",
            "真に“選択”したかということを！\x07\x00\x02",
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

    # Function_51_9AA6 end

    def Function_52_9F67(): pass

    label("Function_52_9F67")

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

    # Function_52_9F67 end

    def Function_53_9F9E(): pass

    label("Function_53_9F9E")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_9FAE():
        OP_95(0xFE, -2800, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FAE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_53_9F9E end

    def Function_54_9FCF(): pass

    label("Function_54_9FCF")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_9FDF():
        OP_95(0xFE, -1500, 0, 11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FDF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_54_9FCF end

    def Function_55_A000(): pass

    label("Function_55_A000")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A010():
        OP_95(0xFE, -2500, 0, 10600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A010)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_55_A000 end

    def Function_56_A031(): pass

    label("Function_56_A031")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A041():
        OP_95(0xFE, 1300, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A041)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_56_A031 end

    def Function_57_A062(): pass

    label("Function_57_A062")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A072():
        OP_95(0xFE, 2300, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A072)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_57_A062 end

    def Function_58_A093(): pass

    label("Function_58_A093")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A0A3():
        OP_95(0xFE, -2800, 0, 13100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A0A3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_58_A093 end

    def Function_59_A0C4(): pass

    label("Function_59_A0C4")

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

    # Function_59_A0C4 end

    def Function_60_A2AB(): pass

    label("Function_60_A2AB")

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

    # Function_60_A2AB end

    def Function_61_A2F3(): pass

    label("Function_61_A2F3")


    def lambda_A2F8():
        OP_95(0xFE, -1600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A2F8)
    WaitChrThread(0xB, 1)
    Return()

    # Function_61_A2F3 end

    def Function_62_A312(): pass

    label("Function_62_A312")


    def lambda_A317():
        OP_95(0xFE, -2900, 0, -2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A317)
    WaitChrThread(0xF, 1)
    Return()

    # Function_62_A312 end

    def Function_63_A331(): pass

    label("Function_63_A331")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A34B():
        OP_95(0xFE, 6300, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A34B)
    WaitChrThread(0xE, 1)
    Return()

    # Function_63_A331 end

    def Function_64_A365(): pass

    label("Function_64_A365")

    OP_92(0xFE, 0x0, 0xFA0, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A38C():
        OP_95(0xFE, -1100, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A38C)
    WaitChrThread(0xC, 1)
    Return()

    # Function_64_A365 end

    def Function_65_A3A6(): pass

    label("Function_65_A3A6")

    OP_92(0xFE, 0x0, 0xFA0, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A3CD():
        OP_95(0xFE, 400, 0, 12100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A3CD)
    WaitChrThread(0xD, 1)
    Return()

    # Function_65_A3A6 end

    def Function_66_A3E7(): pass

    label("Function_66_A3E7")

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

    # Function_66_A3E7 end

    def Function_67_A430(): pass

    label("Function_67_A430")

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
        "#00013F#12Pこれは……！\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#00101F#12Pクロスベル市を包んでいた\x01",
            "《結界》と同じような……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        (
            "#12P#00206F#12P多分、同質のものです。\x02\x03",

            "#00201F……そして鐘の共鳴が\x01",
            "このモヤを発生しているのかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        "#00301F#12Pおいおい、何のために──\x02",
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

    def lambda_A8B5():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A8B5)

    def lambda_A8C2():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A8C2)
    Sleep(50)

    def lambda_A8D2():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A8D2)

    def lambda_A8DF():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_A8DF)
    Sleep(50)

    def lambda_A8EF():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A8EF)

    def lambda_A8FC():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A8FC)
    Sleep(50)

    def lambda_A90C():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A90C)
    Sleep(300)

    #C0146
    ChrTalk(
        0x109,
        "#10111F#5Pこれは……！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x106,
        (
            "#10701F#11P──気をつけて。\x01",
            "周囲から来ます。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x105,
        "#11P#10410F#11Pしかもこれは……\x02",
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

    def lambda_AA37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_AA37)
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

    def lambda_AAF1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_AAF1)
    Sleep(300)

    def lambda_AB05():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_AB05)
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
        "#6P#00107F《星見の塔》にいた……！？\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#11P#00207F同じ魔導のゴーレムですが\x01",
            "遥かに危険そうです……！\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        "#6P#00307Fとにかくブッ倒すぞ！\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#5P#00007Fああ、撃破する！\x02",
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
    Battle("BattleInfo_CF8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_49()
    ClearChrBattleFlags(0x6, 0x8)
    Call(0, 84)
    Return()

    # Function_67_A430 end

    def Function_68_AD47(): pass

    label("Function_68_AD47")


    def lambda_AD4C():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD4C)
    WaitChrThread(0xFE, 1)

    def lambda_AD6A():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD6A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_AD47 end

    def Function_69_AD84(): pass

    label("Function_69_AD84")


    def lambda_AD89():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD89)
    WaitChrThread(0xFE, 1)

    def lambda_ADA7():
        OP_96(0xFE, 0x64, 0x0, 0xFFFFEB4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADA7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_AD84 end

    def Function_70_ADC1(): pass

    label("Function_70_ADC1")


    def lambda_ADC6():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADC6)
    WaitChrThread(0xFE, 1)

    def lambda_ADE4():
        OP_96(0xFE, 0xFFFFFA88, 0x0, 0xFFFFE9BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADE4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_ADC1 end

    def Function_71_ADFE(): pass

    label("Function_71_ADFE")


    def lambda_AE03():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE03)
    WaitChrThread(0xFE, 1)

    def lambda_AE21():
        OP_96(0xFE, 0x190, 0x0, 0xFFFFE50C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE21)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_71_ADFE end

    def Function_72_AE3B(): pass

    label("Function_72_AE3B")


    def lambda_AE40():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE40)
    WaitChrThread(0xFE, 1)

    def lambda_AE5E():
        OP_96(0xFE, 0xFFFFF4AC, 0x0, 0xFFFFE7C8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE5E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_72_AE3B end

    def Function_73_AE78(): pass

    label("Function_73_AE78")


    def lambda_AE7D():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE7D)
    WaitChrThread(0xFE, 1)

    def lambda_AE9B():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0xFFFFE3E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE9B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_73_AE78 end

    def Function_74_AEB5(): pass

    label("Function_74_AEB5")


    def lambda_AEBA():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEBA)
    WaitChrThread(0xFE, 1)

    def lambda_AED8():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0xFFFFE37C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AED8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_74_AEB5 end

    def Function_75_AEF2(): pass

    label("Function_75_AEF2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AF10")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_75_AEF2")

    label("loc_AF10")

    Return()

    # Function_75_AEF2 end

    def Function_76_AF11(): pass

    label("Function_76_AF11")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AF2D")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_76_AF11")

    label("loc_AF2D")

    Return()

    # Function_76_AF11 end

    def Function_77_AF2E(): pass

    label("Function_77_AF2E")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_AF5F():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AF5F)
    Sleep(1000)
    SetChrFlags(0xFE, 0x20)

    def lambda_AF80():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFE764, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF80)
    Sleep(300)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_77_AF2E end

    def Function_78_AFA8(): pass

    label("Function_78_AFA8")

    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_AFE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AFE7)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_78_AFA8 end

    def Function_79_AFFB(): pass

    label("Function_79_AFFB")

    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B03A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B03A)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_79_AFFB end

    def Function_80_B04E(): pass

    label("Function_80_B04E")

    PlayEffect(0x0, 0x3, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B08D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B08D)
    WaitChrThread(0xFE, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_80_B04E end

    def Function_81_B0A1(): pass

    label("Function_81_B0A1")

    PlayEffect(0x0, 0x4, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B0E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B0E0)
    WaitChrThread(0xFE, 2)
    StopEffect(0x4, 0x2)
    Return()

    # Function_81_B0A1 end

    def Function_82_B0F4(): pass

    label("Function_82_B0F4")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B133():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B133)
    WaitChrThread(0xFE, 2)
    StopEffect(0x5, 0x2)
    Return()

    # Function_82_B0F4 end

    def Function_83_B147(): pass

    label("Function_83_B147")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B160")
    Sound(986, 0, 80, 0)
    Sleep(1000)
    Jump("Function_83_B147")

    label("loc_B160")

    Return()

    # Function_83_B147 end

    def Function_84_B161(): pass

    label("Function_84_B161")

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

    def lambda_B5C2():
        TurnDirection(0xFE, 0x28, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B5C2)

    def lambda_B5CF():
        TurnDirection(0xFE, 0x28, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B5CF)

    def lambda_B5DC():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B5DC)

    def lambda_B5E9():
        TurnDirection(0xFE, 0x29, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B5E9)

    def lambda_B5F6():
        TurnDirection(0xFE, 0x29, 0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B5F6)

    def lambda_B603():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B603)

    def lambda_B610():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_B610)
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

    def lambda_B716():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_B716)
    Sleep(300)

    def lambda_B72A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_B72A)
    Sleep(300)

    def lambda_B73E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_B73E)
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

    def lambda_B7C5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B7C5)

    def lambda_B7D2():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B7D2)
    Sleep(50)

    def lambda_B7E2():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B7E2)
    Sleep(50)

    def lambda_B7F2():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B7F2)
    Sleep(50)

    def lambda_B802():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B802)
    Sleep(50)

    def lambda_B812():
        TurnDirection(0x106, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_B812)
    Sleep(50)

    def lambda_B822():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B822)
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
            "#5P#00010Fくっ……\x01",
            "どうしてあんなのが街中に！？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        (
            "#11P#00101Fま、まさか……\x01",
            "おじさまたちが放ったとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x109,
        (
            "#12P#10107Fそ、そんな……\x01",
            "絶対に許されないです！\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x105,
        (
            "#6P#10403Fでも、可能性としては\x01",
            "それが一番ありそうだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(100)

    #C0157
    ChrTalk(
        0x105,
        (
            "#12P#10408Fどうやらこの《鐘》も\x01",
            "関係していそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B9A7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B9A7)

    def lambda_B9B4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_B9B4)

    #C0158
    ChrTalk(
        0x103,
        "#11P#00201Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x106,
        "#6P#10707F……また来ます！\x02",
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

    def lambda_BBFA():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BBFA)

    def lambda_BC07():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BC07)

    def lambda_BC14():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BC14)

    def lambda_BC21():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BC21)

    def lambda_BC2E():
        TurnDirection(0xFE, 0x2C, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BC2E)

    def lambda_BC3B():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BC3B)

    def lambda_BC48():
        TurnDirection(0xFE, 0x2C, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_BC48)
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
        "#11P#00011F……しまった！\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x104,
        "#5P#00311Fチッ……ヤバイな。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        (
            "#6P#10110Fくっ……\x01",
            "何とか突破しないと！\x02",
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

    def lambda_BD6D():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_BD6D)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x28, 0x1, 1300, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x28, 0x3)
    Sleep(50)
    SetChrChipByIndex(0x29, 0x14)
    SetChrSubChip(0x29, 0x0)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_BDE8():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_BDE8)
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

    def lambda_BEDB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BEDB)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BF00():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BF00)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BF28():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BF28)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BF4D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BF4D)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BF75():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BF75)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BF9A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BF9A)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BFBF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_BFBF)
    Sleep(1000)

    def lambda_BFCF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_BFCF)

    def lambda_BFDC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_BFDC)

    def lambda_BFE9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_BFE9)

    def lambda_BFF6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_BFF6)

    def lambda_C003():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_C003)
    OP_68(14800, 1000, -3800, 2000)
    MoveCamera(45, 17, 0, 2000)
    SetCameraDistance(14000, 2000)
    Sleep(1000)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1F, 0x1)
    SetChrSubChip(0x1F, 0x0)

    def lambda_C045():
        OP_96(0xFE, 0x3AFC, 0x0, 0xFFFFEF34, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_C045)

    def lambda_C05F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_C05F)
    Sleep(200)
    SetChrChipByIndex(0x10A, 0x3)
    SetChrSubChip(0x10A, 0x0)

    def lambda_C07B():
        OP_96(0xFE, 0x38A4, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C07B)

    def lambda_C095():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_C095)
    WaitChrThread(0x1F, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1F, 0x2)
    SetChrSubChip(0x1F, 0x0)
    WaitChrThread(0x10A, 1)
    OP_6F(0x79)

    #C0163
    ChrTalk(
        0x103,
        "#00205F#6P#N課長……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0164
    ChrTalk(
        0x102,
        "#00102F#6P#Nダドリーさんも！\x02",
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
        "フッ、やっと来たか。\x02",
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
            "#3465V#30W話は後だ！\x01",
            "こちらに付いて来い！\x02",
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
        "#00002F#6P#Nはいっ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0168
    ChrTalk(
        0x104,
        "#00302F#6P#N合点承知だぜ！\x02",
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

    def lambda_C43E():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C43E)
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

    def lambda_C498():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_C498)
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
            "その後、ロイドたちは\x01",
            "青白いモヤの出ている市街地を\x01",
            "複雑なルートで走り抜け……\x02\x03",

            "旧市街の一角から\x01",
            "ジオフロントＤ区画に辿り着いた。\x07\x00\x02",
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

    # Function_84_B161 end

    def Function_85_C598(): pass

    label("Function_85_C598")


    def lambda_C59D():
        OP_95(0xFE, 12000, 0, -6200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C59D)
    WaitChrThread(0xFE, 1)

    def lambda_C5BB():
        OP_95(0xFE, 26000, 0, -6200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C5BB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_85_C598 end

    def Function_86_C5D5(): pass

    label("Function_86_C5D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C6C4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C6BC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_4B(0xFE, 0x1)
    OP_4B(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C624():
        OP_A6(0xFE, 0x0, 0x32, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C624)
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

    label("loc_C6BC")

    Sleep(300)
    Jump("Function_86_C5D5")

    label("loc_C6C4")

    Return()

    # Function_86_C5D5 end

    def Function_87_C6C5(): pass

    label("Function_87_C6C5")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_C6F6():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C6F6)
    Sleep(1000)
    Return()

    # Function_87_C6C5 end

    def Function_88_C70E(): pass

    label("Function_88_C70E")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1200, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    label("loc_C75C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C7DD")
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
    Jump("loc_C75C")

    label("loc_C7DD")

    Return()

    # Function_88_C70E end

    def Function_89_C7DE(): pass

    label("Function_89_C7DE")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(987, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)

    label("loc_C82C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C8E4")
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
    Jump("loc_C82C")

    label("loc_C8E4")

    Return()

    # Function_89_C7DE end

    def Function_90_C8E5(): pass

    label("Function_90_C8E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C8FE")
    Sound(501, 0, 100, 0)
    Sleep(1500)
    Jump("Function_90_C8E5")

    label("loc_C8FE")

    Return()

    # Function_90_C8E5 end

    def Function_91_C8FF(): pass

    label("Function_91_C8FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C930")
    SetChrChipByIndex(0xFE, 0x15)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A0(0xFE, 1000, 0x0, 0x5)
    Jump("Function_91_C8FF")

    label("loc_C930")

    Return()

    # Function_91_C8FF end

    def Function_92_C931(): pass

    label("Function_92_C931")

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

    # Function_92_C931 end

    def Function_93_C978(): pass

    label("Function_93_C978")

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

    # Function_93_C978 end

    def Function_94_C9BF(): pass

    label("Function_94_C9BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CA13")
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
    Jump("Function_94_C9BF")

    label("loc_CA13")

    Return()

    # Function_94_C9BF end

    def Function_95_CA14(): pass

    label("Function_95_CA14")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CA68")
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
    Jump("Function_95_CA14")

    label("loc_CA68")

    Return()

    # Function_95_CA14 end

    def Function_96_CA69(): pass

    label("Function_96_CA69")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CABD")
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
    Jump("Function_96_CA69")

    label("loc_CABD")

    Return()

    # Function_96_CA69 end

    def Function_97_CABE(): pass

    label("Function_97_CABE")

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

    # Function_97_CABE end

    def Function_98_CCE9(): pass

    label("Function_98_CCE9")

    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x28, 0x20)
    BeginChrThread(0xFE, 0, 0, 76)

    def lambda_CD17():
        OP_95(0xFE, -3200, 0, -3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_CD17)
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

    def lambda_CDD1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_CDD1)
    WaitChrThread(0x28, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_98_CCE9 end

    def Function_99_CDE5(): pass

    label("Function_99_CDE5")

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

    def lambda_CE55():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_CE55)
    WaitChrThread(0x29, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_99_CDE5 end

    def Function_100_CE69(): pass

    label("Function_100_CE69")

    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2A, 0x20)
    BeginChrThread(0xFE, 0, 0, 76)

    def lambda_CE97():
        OP_95(0xFE, 9900, 0, 7700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_CE97)
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

    def lambda_CF47():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_CF47)
    WaitChrThread(0x2A, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_100_CE69 end

    def Function_101_CF5B(): pass

    label("Function_101_CF5B")

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
            "#12P#12400Fまったく、お前という奴は……\x01",
            "いつもいつも好き勝手しおって。\x02\x03",

            "このクロスベルが\x01",
            "どういった場所なのか\x01",
            "知らないわけでもあるまい。\x02\x03",

            "#12406F少しは自分の立場というものを\x01",
            "弁えてほしいものだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x40,
        (
            "#13902Fフッ、心配をかけてしまったかな。\x02\x03",

            "#13904Fただ、身動きが取れなくなる前に\x01",
            "どうしてもこの街を見ておきたくてね。\x02\x03",

            "おかげでここが\x01",
            "魔都と呼ばれる所以が\x01",
            "何となく分かった気がする。\x02\x03",

            "#13908F……なにやら“彼”も、\x01",
            "水面下で動いているようだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x3F,
        (
            "#12P#12400F……ふむ。\x01",
            "収穫はあったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x40,
        (
            "#13900Fフッ、ミュラーのおかげで\x01",
            "楽しい出会いもあったしね。\x02\x03",

            "#13905F……ああ、そういえば\x01",
            "そっちの段取りはどうだい？\x02\x03",

            "#13904Fキミのことだから、\x01",
            "ボクのいない間にも手際よく\x01",
            "進めておいてくれたんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x3F,
        (
            "#12P#12400Fああ、すでに連絡は済ませた。\x02\x03",

            "#12406Fお前のせいでスケジュールには\x01",
            "若干遅れが出てしまったがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x40,
        (
            "#13904Fフッ、だったら急ぐとしよう。\x02\x03",

            "#13900F麗しのレディたちを\x01",
            "待たせるものではないしね。\x02",
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
            "クエスト【演奏家の捜索】\x07\x00",
            "を達成した！\x02",
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

    # Function_101_CF5B end

    def Function_102_D424(): pass

    label("Function_102_D424")

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

    def lambda_D60B():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_D60B)
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

    def lambda_D69D():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_D69D)
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

    def lambda_D72C():
        OP_9B(0x1, 0xFE, 0x0, 0x2EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_D72C)
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
        "サイクス",
        "#5Pあー、ザコの癖にうっぜ！\x02",
    )

    CloseMessageWindow()

    #N0178
    NpcTalk(
        0x2E,
        "ユーリ",
        "#5Pレジー、振り切ってやれ！\x02",
    )

    CloseMessageWindow()

    #N0179
    NpcTalk(
        0x2E,
        "レジー",
        "#5Pちょろいっつーの！\x02",
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

    def lambda_D895():
        OP_96(0x2E, 0x2F26, 0x0, 0x88B8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_D895)
    Sleep(1500)
    StopSound(975, 1000, 100)
    Sleep(1000)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1100", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_102_D424 end

    def Function_103_D8C4(): pass

    label("Function_103_D8C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    OP_68(4270, -700, 10240, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D923")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_D962")

    label("loc_D923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D945")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_D962")

    label("loc_D945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D962")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_D962")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DAAC")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x104, 15940, 0, -2710, 270)

    def lambda_DA3E():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DA3E)

    def lambda_DA58():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DA58)
    Sleep(100)

    def lambda_DA75():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA75)
    Sleep(50)

    def lambda_DA92():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DA92)
    Jump("loc_DC4F")

    label("loc_DAAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DB80")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x109, 15940, 0, -2710, 270)

    def lambda_DB12():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DB12)

    def lambda_DB2C():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB2C)
    Sleep(100)

    def lambda_DB49():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB49)
    Sleep(50)

    def lambda_DB66():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DB66)
    Jump("loc_DC4F")

    label("loc_DB80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_DC4F")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x105, 15940, 0, -2710, 270)

    def lambda_DBE6():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DBE6)

    def lambda_DC00():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DC00)
    Sleep(100)

    def lambda_DC1D():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DC1D)
    Sleep(50)

    def lambda_DC3A():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DC3A)

    label("loc_DC4F")

    OP_68(9660, 1900, -4450, 3000)
    MoveCamera(47, 27, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(10500, 3000)
    OP_6F(0x79)
    WaitChrThread(0x1A2, 1)

    #C0180
    ChrTalk(
        0x1A2,
        "ここが中央広場か。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x1A2,
        (
            "さすがに目抜き通りとだけあって\x01",
            "なかなか活気があるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、シン君の言っていた\x01",
            "タイムズ百貨店も目と鼻の先よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#00000Fすぐに向かった方がいいか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0184
    ChrTalk(
        0x1A2,
        (
            "#6Pんー、まあもう\x01",
            "すべてお前たちに任せるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x1A2,
        (
            "#6Pとにかく、ボクはこうして\x01",
            "エリィお姉さんのそばにいるだけで\x01",
            "幸せなんだからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#00006Fああ、もう\x01",
            "それは十分わかったよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0187
    ChrTalk(
        0x102,
        "#00109Fありがとね、シン君。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DE7B")
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    #C0188
    ChrTalk(
        0x104,
        (
            "#00302Fま、とにかく。\x01",
            "適当にブラブラ回るとすっか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF1A")

    label("loc_DE7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DED1")
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    #C0189
    ChrTalk(
        0x109,
        (
            "#10102Fまあとにかく、なるべく\x01",
            "色々と回ってみましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF1A")

    label("loc_DED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_DF1A")
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    #C0190
    ChrTalk(
        0x105,
        (
            "#10302Fまあとにかく。\x01",
            "適当に色々回るとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF1A")

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

    # Function_103_D8C4 end

    def Function_104_DF69(): pass

    label("Function_104_DF69")

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
            "やあ、ロイド。\x01",
            "そんなにあわててどうした？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#00003F今、ある人物を追いかけている\x01",
            "所なんだけど……\x02\x03",

            "#00001Fさっきここをラインフォルト社製の\x01",
            "黒い運搬車が通らなかったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x14,
        (
            "黒い運搬車……？\x02\x03",

            "ああ、そういえば少し前に\x01",
            "そんな車が通った気がするな。\x02\x03",

            "確か、東通りのほうへ\x01",
            "抜けて行った気がするけど。\x02",
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
            "#00105F東通り……ですか？\x02\x03",

            "帝国方面に向かう\x01",
            "西通りの方ではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x15,
        "ええ、私も確かに見かけました。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x104,
        (
            "#00303Fふむ……どうやら行き先は\x01",
            "共和国方面だったみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x103,
        (
            "#00203Fラインフォルト社製の運搬車を\x01",
            "運転する帝国人……\x02\x03",

            "#00200F逃走するとしたら帝国方面だろうと\x01",
            "思っていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x105,
        (
            "#10306Fやれやれ、なかなか一筋縄では\x01",
            "いかない相手みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#00000Fともかく、ありがとう。\x01",
            "助かったよフランツ。\x02\x03",

            "#00001F……急いだほうがよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x109,
        (
            "#10103Fええ、追いかけるなら\x01",
            "導力車を使った方が\x01",
            "いいかもしれません。\x02\x03",

            "#10101F急いでタングラム門に\x01",
            "向かいましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x14,
        (
            "なんだかよく分からないが、\x01",
            "頑張ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x15,
        "健闘をお祈りします！\x02",
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

    # Function_104_DF69 end

    def Function_105_E4A5(): pass

    label("Function_105_E4A5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB4D")
    Fade(500)
    OP_68(-19610, -6700, -24820, 0)
    MoveCamera(9, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10990, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E5A7")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x104, -18650, -8200, -21550, 225)

    def lambda_E54D():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E54D)

    def lambda_E562():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E562)
    Sleep(100)

    def lambda_E57A():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E57A)
    Sleep(50)

    def lambda_E592():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E592)
    Jump("loc_E6FA")

    label("loc_E5A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E653")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x109, -18650, -8200, -21550, 225)

    def lambda_E5F9():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E5F9)

    def lambda_E60E():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E60E)
    Sleep(100)

    def lambda_E626():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E626)
    Sleep(50)

    def lambda_E63E():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E63E)
    Jump("loc_E6FA")

    label("loc_E653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E6FA")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x105, -18650, -8200, -21550, 225)

    def lambda_E6A5():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E6A5)

    def lambda_E6BA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E6BA)
    Sleep(100)

    def lambda_E6D2():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E6D2)
    Sleep(50)

    def lambda_E6EA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E6EA)

    label("loc_E6FA")

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
        "#11Pな、なんだ、あのデカイ犬は……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1A2, 3, 0, 106)
    OP_68(-23520, -6700, -24320, 3000)
    MoveCamera(51, 18, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(13660, 3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E7C0")

    def lambda_E790():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E790)
    Sleep(50)

    def lambda_E7A0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E7A0)
    Sleep(50)

    def lambda_E7B0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E7B0)
    Sleep(300)
    Jump("loc_E837")

    label("loc_E7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E7FE")

    def lambda_E7CE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E7CE)
    Sleep(50)

    def lambda_E7DE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E7DE)
    Sleep(50)

    def lambda_E7EE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E7EE)
    Sleep(300)
    Jump("loc_E837")

    label("loc_E7FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E837")

    def lambda_E80C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E80C)
    Sleep(50)

    def lambda_E81C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E81C)
    Sleep(50)

    def lambda_E82C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E82C)
    Sleep(300)

    label("loc_E837")

    OP_6F(0x79)

    #C0204
    ChrTalk(
        0x101,
        "#00005Fツァイト……あんな所で。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、外の空気が\x01",
            "吸いたかったのかしらね。\x02",
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
        "#6P#00105Fシン君……どうかしたの？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E94F")
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    #C0207
    ChrTalk(
        0x104,
        (
            "#00309Fはは～ん、さては\x01",
            "ツァイトが怖えんだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA2C")

    label("loc_E94F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E9E3")
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    #C0208
    ChrTalk(
        0x109,
        (
            "#10102Fあはは、どうやら\x01",
            "ツァイト君が怖いみたいですね。\x02\x03",

            "#10104F（あたしも最初は苦手だったから\x01",
            "  気持ちは分かるけど。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA2C")

    label("loc_E9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EA2C")
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    #C0209
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、どうやら\x01",
            "ツァイトが怖いと見えるね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA2C")


    #C0210
    ChrTalk(
        0x1A2,
        "な、なんのことだ……？\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x1A2,
        (
            "ボクにこ、怖いモノなんか\x01",
            "ないんだから、な。\x02",
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
            "さぁて、お前たち。\x01",
            "こっちはいいから次の場所に行くぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#00000Fああ、了解だ。\x02\x03",

            "#00012F（はは、見るからにやせ我慢だけど\x01",
            "  見上げた根性だな。）\x02",
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
    Jump("loc_EBB8")

    label("loc_EB4D")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    #C0214
    ChrTalk(
        0x1A2,
        (
            "お、おい……\x01",
            "そっちはいいから広場の方に戻るぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        "#00000Fああ、了解だ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EBB8")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -17980, -8200, -22080, 44)
    EventEnd(0x4)
    Return()

    # Function_105_E4A5 end

    def Function_106_EBD0(): pass

    label("Function_106_EBD0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EC00")

    def lambda_EBE0():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EBE0)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_106_EBD0")

    label("loc_EC00")

    Return()

    # Function_106_EBD0 end

    def Function_107_EC01(): pass

    label("Function_107_EC01")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F02A")
    OP_68(90, 4400, 25340, 0)
    MoveCamera(359, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16660, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_ECB3")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x104, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_ED52")

    label("loc_ECB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_ED05")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x109, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_ED52")

    label("loc_ED05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_ED52")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x105, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)

    label("loc_ED52")

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
            "#00000Fさてと、百貨店に\x01",
            "到着したわけだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EE9C")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0217
    ChrTalk(
        0x104,
        (
            "#00305Fまだ他に、小僧を\x01",
            "連れて行きてえ場所はねえのか？\x02\x03",

            "#00303Fいったん中に入ったら、\x01",
            "もう外を案内している時間は\x01",
            "なくなっちまいそうだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFF0")

    label("loc_EE9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EF51")
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0218
    ChrTalk(
        0x109,
        (
            "#10105Fまだ他に、シン君を連れて\x01",
            "行きたい場所はありませんかね？\x02\x03",

            "#10103Fいったん中に入ったら、\x01",
            "もう外を案内している時間は\x01",
            "なくなってしまいそうですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFF0")

    label("loc_EF51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EFF0")
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0219
    ChrTalk(
        0x105,
        (
            "#10300Fまだ他に、シンを連れて\x01",
            "行きたい場所はないのかい？\x02\x03",

            "いったん中に入ったら、\x01",
            "もう外を案内している時間は\x01",
            "なくなっちゃいそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFF0")


    #C0220
    ChrTalk(
        0x1A2,
        (
            "#6Pどうするんだ？\x01",
            "すべてお前たちに任せるぞ。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 108)
    Jump("loc_F315")

    label("loc_F02A")

    OP_68(10, 400, 21490, 0)
    MoveCamera(0, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15710, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F0AA")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x104, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F149")

    label("loc_F0AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F0FC")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x109, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F149")

    label("loc_F0FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F149")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x105, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)

    label("loc_F149")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F1EA")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0221
    ChrTalk(
        0x104,
        (
            "#00300Fそろそろ、百貨店に入るか？\x02\x03",

            "#00303Fいったん中に入ったら、\x01",
            "もう外を案内している時間は\x01",
            "なくなっちまいそうだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F310")

    label("loc_F1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F286")
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0222
    ChrTalk(
        0x109,
        (
            "#10100Fそろそろ、百貨店に入りますか？\x02\x03",

            "#10103Fいったん中に入ったら、\x01",
            "もう外を案内している時間は\x01",
            "なくなってしまいそうですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F310")

    label("loc_F286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F310")
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0223
    ChrTalk(
        0x105,
        (
            "#10300Fそろそろ、百貨店に入るかい？\x02\x03",

            "いったん中に入ったら、\x01",
            "もう外を案内している時間は\x01",
            "なくなっちゃいそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F310")

    Call(0, 108)
    EventEnd(0x5)

    label("loc_F315")

    Return()

    # Function_107_EC01 end

    def Function_108_F316(): pass

    label("Function_108_F316")

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
            "百貨店に入る\x01",                # 0
            "まだ他の場所を案内する\x01",      # 1
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
        (0, "loc_F38A"),
        (1, "loc_F3DB"),
        (SWITCH_DEFAULT, "loc_F45B"),
    )


    label("loc_F38A")

    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0224
    ChrTalk(
        0x101,
        (
            "#00000Fそうだな、\x01",
            "一通り案内できたと思うし\x01",
            "中に入ろうか。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 109)
    Jump("loc_F45B")

    label("loc_F3DB")

    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0225
    ChrTalk(
        0x101,
        (
            "#00003Fそうだな、まだ案内したい\x01",
            "場所もあるかもしれないし。\x02\x03",

            "#00000F入るのは、後回しにしよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C5, 6)
    Jump("loc_F45B")

    label("loc_F45B")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -180, 0, 15990, 180)
    EventEnd(0x5)
    Return()

    # Function_108_F316 end

    def Function_109_F473(): pass

    label("Function_109_F473")

    LoadChrToIndex("chr/ch00300.itc", 0x1E)
    LoadChrToIndex("chr/ch02900.itc", 0x1F)
    LoadChrToIndex("chr/ch03000.itc", 0x20)

    #C0226
    ChrTalk(
        0x1A2,
        "#6Pよし、決まったな！\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x102,
        (
            "#12P#00100Fふふ、それじゃ\x01",
            "さっそく入りましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-13670, 1900, 7350, 0)
    MoveCamera(22, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14280, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F5A3")
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
    Jump("loc_F6CE")

    label("loc_F5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F63B")
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
    Jump("loc_F6CE")

    label("loc_F63B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F6CE")
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

    label("loc_F6CE")

    OP_0D()
    Sound(100, 0, 40, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F79F")

    def lambda_F6FB():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F6FB)
    Sleep(100)

    def lambda_F713():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F713)
    Sleep(500)

    def lambda_F72B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F72B)
    Sleep(200)

    def lambda_F73F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F73F)

    def lambda_F750():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F750)

    def lambda_F765():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F765)
    Sleep(1000)

    def lambda_F77D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F77D)

    def lambda_F78E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F78E)
    Jump("loc_F8FE")

    label("loc_F79F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F851")

    def lambda_F7AD():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F7AD)
    Sleep(100)

    def lambda_F7C5():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F7C5)
    Sleep(500)

    def lambda_F7DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F7DD)
    Sleep(200)

    def lambda_F7F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F7F1)

    def lambda_F802():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F802)

    def lambda_F817():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F817)
    Sleep(1000)

    def lambda_F82F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F82F)

    def lambda_F840():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F840)
    Jump("loc_F8FE")

    label("loc_F851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F8FE")

    def lambda_F85F():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F85F)
    Sleep(100)

    def lambda_F877():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F877)
    Sleep(500)

    def lambda_F88F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F88F)
    Sleep(200)

    def lambda_F8A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F8A3)

    def lambda_F8B4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F8B4)

    def lambda_F8C9():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F8C9)
    Sleep(1000)

    def lambda_F8E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F8E1)

    def lambda_F8F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F8F2)

    label("loc_F8FE")

    WaitChrThread(0x102, 1)
    Sound(100, 0, 40, 0)
    OP_71(0x4, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FAF8")

    #C0228
    ChrTalk(
        0x36,
        (
            "#10100Fうん、どうやら\x01",
            "お店の中に入ったみたいだね。\x02",
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
        "#11P#10105Fどうかした、ワジ君？\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x37,
        (
            "#10301Fああ、背後を警戒している間、\x01",
            "何か気配を感じた気がしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x36,
        (
            "#11P#10105F気配……\x01",
            "それって、黒月の人たちかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x37,
        (
            "#10303Fああ、それも当然\x01",
            "考えられるだろうけど……\x02\x03",

            "#10300Fまあ、ただ具体的なことは\x01",
            "さっぱりだね。\x02\x03",

            "とりあえず、僕たちも\x01",
            "少ししたら百貨店に入ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x36,
        "#10103Fう、うん……了解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF54")

    label("loc_FAF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FD65")

    #C0235
    ChrTalk(
        0x37,
        (
            "#10300Fふむ、どうやら\x01",
            "店の中に入ったみたいだね。\x02",
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
        "#11P#10305Fどうかしたかい、ランディ？\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x35,
        (
            "#00301Fああ、背後を警戒してる時に\x01",
            "何やら気配を感じた気がしてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x37,
        (
            "#11P#10304Fフフ、君もか……\x01",
            "僕も何となく感じてはいたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x35,
        (
            "#00303Fああ、おそらく黒月の連中が\x01",
            "監視を付けているんだろうが……\x02\x03",

            "#00301Fなんつうか、どうにも\x01",
            "それだけじゃない感じがしてな。\x02\x03",

            "#00306Fま、もっとも具体的なことは\x01",
            "何も分からねえんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x37,
        (
            "#11P#10304Fフフ、僕も同じ見解だよ。\x02\x03",

            "#10300Fとにかく、今はまだ\x01",
            "様子を見るしかなさそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x35,
        "#00303Fああ、そうだな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF54")

    label("loc_FD65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FF54")

    #C0243
    ChrTalk(
        0x36,
        (
            "#10100Fうん、どうやら\x01",
            "お店の中に入ったみたいですね。\x02",
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
        "#11P#10105Fどうかしました、ランディ先輩？\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x35,
        (
            "#00301Fああ、背後を警戒してる時に\x01",
            "何やら気配を感じた気がしてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x36,
        (
            "#11P#10101F気配……\x01",
            "それって、黒月の人たちですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x35,
        (
            "#00303Fああ、当然それも\x01",
            "考えられるだろうが……\x02\x03",

            "#00306Fただ、正直\x01",
            "具体的なことはさっぱりだ。\x02\x03",

            "#00300Fとりあえず、俺たちも\x01",
            "あと少ししたら百貨店に入ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x36,
        "#10101Fえ、ええ……了解です。\x02",
    )

    CloseMessageWindow()

    label("loc_FF54")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0170", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_109_F473 end

    def Function_110_FF6C(): pass

    label("Function_110_FF6C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10043")

    #C0250
    ChrTalk(
        0x1A2,
        (
            "えっと、百貨店は\x01",
            "そっち側にあるのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#00000Fああいや、\x01",
            "こっちは駅の方だけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0252
    ChrTalk(
        0x1A2,
        "なら、さっさと戻って来いっての。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#00005Fあ、ああ……すまない。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_1007F")

    label("loc_10043")


    #C0254
    ChrTalk(
        0x101,
        (
            "#00000F駅前通りに出る必要はないな。\x01",
            "広場の方に戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1007F")

    SetChrPos(0x0, 3740, 0, -19810, 0)
    EventEnd(0x4)
    Return()

    # Function_110_FF6C end

    def Function_111_10093(): pass

    label("Function_111_10093")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10157")
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0255
    ChrTalk(
        0x102,
        (
            "#00105Fねえ、ロイド……\x01",
            "こっちに行くと行政区よね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0256
    ChrTalk(
        0x101,
        "#00000Fそうだな、引き返そう。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x1A2,
        "百貨店、こっちじゃなかったのか？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_1017C")

    label("loc_10157")


    #C0258
    ChrTalk(
        0x101,
        "#00000Fこっちは行政区方面だな。\x02",
    )

    CloseMessageWindow()

    label("loc_1017C")

    SetChrPos(0x0, 13290, 0, 26680, 180)
    EventEnd(0x4)
    Return()

    # Function_111_10093 end

    def Function_112_10190(): pass

    label("Function_112_10190")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10291")
    TurnDirection(0x1A2, 0x0, 500)
    Sleep(300)

    #C0259
    ChrTalk(
        0x1A2,
        "このアーケードは……\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x1A2,
        (
            "もしかして、\x01",
            "ここから裏通りに入れるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        "#00000Fああ、よく知ってるな。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x102,
        (
            "#00103F……とりあえず、\x01",
            "こっちに用事はないわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x1A2,
        (
            "（ふむ、ツァオたちの言ってた\x01",
            "  ルバーチェ跡がここに……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_102B2")

    label("loc_10291")


    #C0264
    ChrTalk(
        0x101,
        "#00000F裏通りに用はないな。\x02",
    )

    CloseMessageWindow()

    label("loc_102B2")

    SetChrPos(0x0, -14110, -10, 14420, 135)
    EventEnd(0x4)
    Return()

    # Function_112_10190 end

    def Function_113_102C6(): pass

    label("Function_113_102C6")

    EventBegin(0x1)

    #C0265
    ChrTalk(
        0x101,
        (
            "#00000Fこの先は西通りだな。\x02\x03",

            "#00003Fあまり百貨店から\x01",
            "遠ざかるわけにもいかないし、\x01",
            "引き返そう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)
    Return()

    # Function_113_102C6 end

    SaveToFile()

Try(main)
