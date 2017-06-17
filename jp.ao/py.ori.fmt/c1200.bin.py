from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1200.bin",                # FileName
        "c1200",                    # MapName
        "c1200",                    # Location
        0x001A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c1200", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x07',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 2000, 0, 0, 0, 0, 1, 26, 0, 8, 0, 9],
    )

    BuildStringList((
        "c1200",                  # 0
        "クーニャ",               # 1
        "オーゼル",               # 2
        "ビショップ",             # 3
        "クワイン老人",           # 4
        "アミサ",                 # 5
        "ニコル",                 # 6
        "セリーヌ",               # 7
        "みっしぃ",               # 8
        "ＭＷＬスタッフ",         # 9
        "ＭＷＬスタッフ",         # 10
        "市民",                   # 11
        "市民",                   # 12
        "市民",                   # 13
        "市民",                   # 14
        "観光客",                 # 15
        "観光客",                 # 16
        "整備員",                 # 17
        "ロイ",                   # 18
        "メイリン",               # 19
        "ツァイト",               # 20
        "キーア",                 # 21
        "シズク",                 # 22
        "観光客",                 # 23
        "男の子",                 # 24
        "市民",                   # 25
        "ジョーリッジ課長",       # 26
        "警官",                   # 27
        "警官",                   # 28
        "水上バスガイド",         # 29
        "パトカー",               # 30
        "ニールセン",             # 31
        "ツァオ",                 # 32
        "ラウ",                   # 33
        "ユーリ",                 # 34
        "サイクス",               # 35
        "レジー",                 # 36
        "暴走車",                 # 37
        "パトカー",               # 38
        "水上バス",               # 39
        "SE制御",                 # 40
        "クライド",               # 41
        "男性",                   # 42
        "車",                     # 43
        "ボート",                 # 44
        "オリビエ",               # 45
        "中央広場",               # 46
        "西通り",                 # 47
        "行政区",                 # 48
        "住宅街",                 # 49
        "歓楽街",                 # 50
        "東通り",                 # 51
        "旧市街",                 # 52
        "港湾区",                 # 53
        "ＩＢＣ",                 # 54
        "駅前通り",               # 55
        "裏通り",                 # 56
        "ウルスラ間道",           # 57
        "東クロスベル街道",       # 58
        "西クロスベル街道",       # 59
        "マインツ山道",           # 60
        "オルキスタワー",         # 61
    ))

    AddCharChip((
        "chr/ch26000.itc",                   # 00
        "chr/ch49600.itc",                   # 01
        "chr/ch49700.itc",                   # 02
        "chr/ch10200.itc",                   # 03
        "chr/ch44500.itc",                   # 04
        "chr/ch44600.itc",                   # 05
        "chr/ch23000.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch20300.itc",                   # 08
        "chr/ch24400.itc",                   # 09
        "chr/ch20500.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch25200.itc",                   # 0C
        "chr/ch26000.itc",                   # 0D
        "apl/ch50168.itc",                   # 0E
        "chr/ch21500.itc",                   # 0F
        "chr/ch28900.itc",                   # 10
        "chr/ch29100.itc",                   # 11
        "chr/ch24000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch21902.itc",                   # 14
        "chr/ch22200.itc",                   # 15
        "chr/ch49500.itc",                   # 16
        "chr/ch49100.itc",                   # 17
        "chr/ch02707.itc",                   # 18
        "chr/ch08200.itc",                   # 19
        "chr/ch08700.itc",                   # 1A
        "chr/ch30100.itc",                   # 1B
        "chr/ch30000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
        "chr/ch00000.itc",                   # 1E
        "chr/ch00000.itc",                   # 1F
        "chr/ch00000.itc",                   # 20
        "chr/ch46500.itc",                   # 21
        "apl/ch51272.itc",                   # 22
        "chr/ch21900.itc",                   # 23
        "chr/ch26600.itc",                   # 24
        "chr/ch45102.itc",                   # 25
    ))

    DeclNpc(-13199,  0,       11500,   90,   257,  0x0, 0,   11,  0,   0,   1,   0,   11,  255,  0)
    DeclNpc(-10470,  0,       13340,   180,  257,  0x0, 0,   12,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-52470,  2000,    21149,   90,   257,  0x0, 0,   13,  0,   0,   2,   0,   13,  255,  0)
    DeclNpc(39669,   -2500,   -19379,  180,  257,  0x0, 0,   18,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(38439,   -2490,   -18079,  135,  257,  0x0, 0,   15,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-18000,  0,       -5750,   90,   385,  0x0, 0,   16,  0,   0,   4,   0,   18,  255,  0)
    DeclNpc(13000,   0,       -10000,  0,    385,  0x0, 0,   17,  0,   0,   5,   0,   19,  255,  0)
    DeclNpc(9479,    -699,    159,     270,  389,  0x0, 0,   3,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(6550,    -699,    -2359,   315,  389,  0x0, 0,   4,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5989,    -699,    2119,    225,  389,  0x0, 0,   5,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4449,    -699,    -810,    90,   389,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4940,    -699,    -2200,   90,   389,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(3809,    -699,    -3369,   45,   389,  0x0, 0,   8,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(39900,   -2500,   3650,    270,  389,  0x0, 0,   11,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(4190,    -699,    1529,    135,  389,  0x0, 0,   9,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(3809,    -699,    250,     90,   389,  0x0, 0,   10,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-90,     -699,    -1649,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(86480,   -2500,   19430,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   31,  255,  0)
    DeclNpc(8659,    -699,    670,     225,  405,  0x0, 0,   24,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(7190,    -699,    379,     90,   389,  0x0, 0,   25,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(8119,    -699,    -730,    0,    389,  0x0, 0,   26,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(7239,    -550,    3190,    180,  389,  0x0, 0,   20,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(7239,    -699,    1580,    0,    385,  0x0, 0,   21,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(47909,   -2500,   16530,   180,  389,  0x0, 0,   23,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(-17799,  0,       13369,   0,    389,  0x0, 0,   27,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(-18000,  0,       -5750,   90,   385,  0x0, 0,   28,  0,   0,   6,   0,   40,  255,  0)
    DeclNpc(-17799,  0,       13369,   180,  389,  0x0, 0,   28,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(42450,   -2500,   2329,    235,  389,  0x0, 0,   36,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(-21239,  0,       14350,   90,   196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(7820,    -400,    3200,    180,  389,  0x0, 0,   37,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   33,  0,   0,   0,   255, 255, 255,  0)

    DeclEvent(0x0000, 0, 65,  -13.5,                 27.5,                  1.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.75,                  -13.75,                -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 66,  5.0,                   33.0,                  1.0,                   324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   -0.4166666865348816,   -11.0,                 -0.1428571492433548,   1.0])
    DeclEvent(0x0000, 0, 67,  -20.0,                 -29.0,                 -0.5,                  324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   1.6666667461395264,    9.666666984558105,     0.0714285746216774,    1.0])
    DeclEvent(0x0000, 0, 68,  -29.0,                 23.329999923706055,    1.0,                   324.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   9.666666984558105,     -1.944166660308838,    -0.1428571492433548,   1.0])
    DeclEvent(0x0000, 0, 78,  -0.23999999463558197,  6.5,                   -0.28999999165534973,  324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   0.019999999552965164,  -2.1666667461395264,   0.0414285734295845,    1.0])
    DeclEvent(0x0000, 0, 79,  -0.09000000357627869,  -6.5,                  -0.20999999344348907,  324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   0.007500000298023224,  2.1666667461395264,    0.030000001192092896,  1.0])
    DeclEvent(0x0000, 0, 93,  33.08000183105469,     0.07999999821186066,   -2.5,                  324.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -11.026667594909668,   -0.006666666828095913, 0.625,                 1.0])

    DeclActor(16750,   -1000,   -15740,  1200,    16750,   0,       -15740,  0x007C, 0,  10, 0x0000)
    DeclActor(82470,   -2500,   15010,   1200,    79890,   -3500,   8810,    0x007C, 0,  46, 0x0000)
    DeclActor(19200,   250,     20500,   2000,    19200,   1250,    20500,   0x007C, 0,  44, 0x0000)
    DeclActor(34000,   -2500,   3400,    1500,    34000,   -1500,   3400,    0x007C, 0,  105, 0x0000)
    DeclActor(7470,    -700,    3250,    1500,    7470,    -550,    3250,    0x007C, 0,  62, 0x0000)
    DeclActor(-7140,   0,       13580,   1500,    -7140,   1250,    13580,   0x007C, 0,  63, 0x0000)
    DeclActor(39300,   -2500,   19050,   1500,    39300,   -1250,   19050,   0x007C, 0,  64, 0x0000)
    DeclActor(-13500,  1000,    27500,   2000,    -13500,  3000,    27500,   0x007C, 0,  45, 0x0000)
    DeclActor(77220,   -2500,   20290,   2000,    77220,   -1000,   20290,   0x007C, 0,  106, 0x0000)

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "中央広場")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "西通り")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "住宅街")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "歓楽街")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "東通り")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "旧市街")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "駅前通り")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "裏通り")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-96.5, 0.0, 203.75, 0x0000, 0x0000, "オルキスタワー")
    PlaceName(-151.9600067138672, 0.0, -103.48999786376953, 0x0000, 0x0051, "")
    PlaceName(-81.55000305175781, 0.0, -69.43000030517578, 0x0000, 0x0054, "")
    PlaceName(-119.87000274658203, 0.0, -113.97000122070312, 0x0000, 0x0057, "")
    PlaceName(-152.94000244140625, 0.0, -65.5, 0x0000, 0x0053, "")
    PlaceName(-126.08999633789062, 0.0, -34.060001373291016, 0x0000, 0x0053, "")
    PlaceName(-192.57000732421875, 0.0, -72.05000305175781, 0x0000, 0x0053, "")
    PlaceName(-205.33999633789062, 0.0, -44.540000915527344, 0x0000, 0x0053, "")
    PlaceName(-173.89999389648438, 0.0, -2.619999885559082, 0x0000, 0x0052, "")
    PlaceName(-167.67999267578125, 0.0, -19.649999618530273, 0x0000, 0x0053, "")
    PlaceName(-156.22000122070312, 0.0, -30.790000915527344, 0x0000, 0x0053, "")
    PlaceName(-118.87999725341797, 0.0, 62.22999954223633, 0x0000, 0x0051, "")
    PlaceName(27.84000015258789, 0.0, -115.27999877929688, 0x0000, 0x0052, "")
    PlaceName(5.570000171661377, 0.0, -233.83999633789062, 0x0000, 0x0053, "")
    PlaceName(-11.460000038146973, 0.0, -209.60000610351562, 0x0000, 0x0053, "")

    ChipFrameInfo(3584, 0)                                       # 0

    ScpFunction((
        "Function_0_E00",          # 00, 0
        "Function_1_EB0",          # 01, 1
        "Function_2_F61",          # 02, 2
        "Function_3_109B",         # 03, 3
        "Function_4_11D5",         # 04, 4
        "Function_5_1286",         # 05, 5
        "Function_6_1337",         # 06, 6
        "Function_7_13E8",         # 07, 7
        "Function_8_14AC",         # 08, 8
        "Function_9_1C86",         # 09, 9
        "Function_10_2092",        # 0A, 10
        "Function_11_21E3",        # 0B, 11
        "Function_12_33A3",        # 0C, 12
        "Function_13_48BB",        # 0D, 13
        "Function_14_5127",        # 0E, 14
        "Function_15_58E9",        # 0F, 15
        "Function_16_5A49",        # 10, 16
        "Function_17_5B92",        # 11, 17
        "Function_18_6005",        # 12, 18
        "Function_19_61ED",        # 13, 19
        "Function_20_62FE",        # 14, 20
        "Function_21_6406",        # 15, 21
        "Function_22_6521",        # 16, 22
        "Function_23_6662",        # 17, 23
        "Function_24_6709",        # 18, 24
        "Function_25_67BF",        # 19, 25
        "Function_26_6882",        # 1A, 26
        "Function_27_68B2",        # 1B, 27
        "Function_28_6A1E",        # 1C, 28
        "Function_29_6B5F",        # 1D, 29
        "Function_30_6B7D",        # 1E, 30
        "Function_31_6BB3",        # 1F, 31
        "Function_32_6BD7",        # 20, 32
        "Function_33_6C42",        # 21, 33
        "Function_34_6D31",        # 22, 34
        "Function_35_6E56",        # 23, 35
        "Function_36_6EF9",        # 24, 36
        "Function_37_7005",        # 25, 37
        "Function_38_70D1",        # 26, 38
        "Function_39_72C0",        # 27, 39
        "Function_40_7455",        # 28, 40
        "Function_41_764E",        # 29, 41
        "Function_42_795D",        # 2A, 42
        "Function_43_7AD8",        # 2B, 43
        "Function_44_7C38",        # 2C, 44
        "Function_45_81A4",        # 2D, 45
        "Function_46_83F7",        # 2E, 46
        "Function_47_84CB",        # 2F, 47
        "Function_48_8D64",        # 30, 48
        "Function_49_8E5E",        # 31, 49
        "Function_50_8E7D",        # 32, 50
        "Function_51_929E",        # 33, 51
        "Function_52_92E9",        # 34, 52
        "Function_53_934A",        # 35, 53
        "Function_54_93AB",        # 36, 54
        "Function_55_93DB",        # 37, 55
        "Function_56_9409",        # 38, 56
        "Function_57_9D2F",        # 39, 57
        "Function_58_9E2F",        # 3A, 58
        "Function_59_9E4D",        # 3B, 59
        "Function_60_9E81",        # 3C, 60
        "Function_61_9EB5",        # 3D, 61
        "Function_62_A4D0",        # 3E, 62
        "Function_63_A511",        # 3F, 63
        "Function_64_A545",        # 40, 64
        "Function_65_A579",        # 41, 65
        "Function_66_A5CA",        # 42, 66
        "Function_67_A638",        # 43, 67
        "Function_68_A6A6",        # 44, 68
        "Function_69_A714",        # 45, 69
        "Function_70_AB39",        # 46, 70
        "Function_71_AD1C",        # 47, 71
        "Function_72_B591",        # 48, 72
        "Function_73_BFEB",        # 49, 73
        "Function_74_C022",        # 4A, 74
        "Function_75_C06D",        # 4B, 75
        "Function_76_D1DD",        # 4C, 76
        "Function_77_D47D",        # 4D, 77
        "Function_78_D4C0",        # 4E, 78
        "Function_79_D570",        # 4F, 79
        "Function_80_D620",        # 50, 80
        "Function_81_E63A",        # 51, 81
        "Function_82_E657",        # 52, 82
        "Function_83_E674",        # 53, 83
        "Function_84_E691",        # 54, 84
        "Function_85_E704",        # 55, 85
        "Function_86_E777",        # 56, 86
        "Function_87_E88B",        # 57, 87
        "Function_88_E99F",        # 58, 88
        "Function_89_E9C4",        # 59, 89
        "Function_90_EA12",        # 5A, 90
        "Function_91_F9A1",        # 5B, 91
        "Function_92_101C5",       # 5C, 92
        "Function_93_1021B",       # 5D, 93
        "Function_94_10561",       # 5E, 94
        "Function_95_10920",       # 5F, 95
        "Function_96_1094E",       # 60, 96
        "Function_97_110E7",       # 61, 97
        "Function_98_11179",       # 62, 98
        "Function_99_111C4",       # 63, 99
        "Function_100_1120F",      # 64, 100
        "Function_101_1125A",      # 65, 101
        "Function_102_112A5",      # 66, 102
        "Function_103_112F0",      # 67, 103
        "Function_104_1133B",      # 68, 104
        "Function_105_11484",      # 69, 105
        "Function_106_115D0",      # 6A, 106
    ))


    def Function_0_E00(): pass

    label("Function_0_E00")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_E38"),
        (1, "loc_E44"),
        (2, "loc_E50"),
        (3, "loc_E5C"),
        (4, "loc_E68"),
        (5, "loc_E74"),
        (6, "loc_E80"),
        (SWITCH_DEFAULT, "loc_E8C"),
    )


    label("loc_E38")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E44")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E50")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E5C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E68")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E74")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E80")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E8C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EAF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_EAF")

    Return()

    # Function_0_E00 end

    def Function_1_EB0(): pass

    label("Function_1_EB0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F60")
    OP_95(0xFE, 14600, 0, 11500, 1000, 0x0)
    OP_95(0xFE, 20200, 0, 8200, 1000, 0x0)
    OP_95(0xFE, 20200, 0, -6200, 1000, 0x0)
    OP_95(0xFE, 14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -20000, 0, -6400, 1000, 0x0)
    OP_95(0xFE, -20000, 0, 6000, 1000, 0x0)
    OP_95(0xFE, -13200, 0, 11500, 1000, 0x0)
    Jump("Function_1_EB0")

    label("loc_F60")

    Return()

    # Function_1_EB0 end

    def Function_2_F61(): pass

    label("Function_2_F61")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_109A")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 5000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, 1760, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, 1760, 5080, 38700, 8000, 0x0)
    Sleep(3000)
    OP_95(0xFE, 1760, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, -13000, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 5000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 5000, 0x0)
    Jump("Function_2_F61")

    label("loc_109A")

    Return()

    # Function_2_F61 end

    def Function_3_109B(): pass

    label("Function_3_109B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11D4")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, 1760, 5080, 38700, 10000, 0x0)
    Sleep(3000)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 8000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 8000, 0x0)
    Jump("Function_3_109B")

    label("loc_11D4")

    Return()

    # Function_3_109B end

    def Function_4_11D5(): pass

    label("Function_4_11D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1285")
    OP_95(0xFE, -13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 18000, 0, -4300, 4000, 0x0)
    OP_95(0xFE, 18000, 0, 7040, 4000, 0x0)
    OP_95(0xFE, 13000, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -12700, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -18000, 0, 5200, 4000, 0x0)
    OP_95(0xFE, -18000, 0, -5750, 4000, 0x0)
    Jump("Function_4_11D5")

    label("loc_1285")

    Return()

    # Function_4_11D5 end

    def Function_5_1286(): pass

    label("Function_5_1286")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1336")
    OP_95(0xFE, 18000, 0, -4300, 4000, 0x0)
    OP_95(0xFE, 18000, 0, 7040, 4000, 0x0)
    OP_95(0xFE, 13000, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -12700, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -18000, 0, 5200, 4000, 0x0)
    OP_95(0xFE, -18000, 0, -5750, 4000, 0x0)
    OP_95(0xFE, -13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 13000, 0, -10000, 4000, 0x0)
    Jump("Function_5_1286")

    label("loc_1336")

    Return()

    # Function_5_1286 end

    def Function_6_1337(): pass

    label("Function_6_1337")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13E7")
    OP_95(0xFE, -13000, 0, -10000, 1000, 0x0)
    OP_95(0xFE, 13000, 0, -10000, 1000, 0x0)
    OP_95(0xFE, 18000, 0, -4300, 1000, 0x0)
    OP_95(0xFE, 18000, 0, 7040, 1000, 0x0)
    OP_95(0xFE, 13000, 0, 10000, 1000, 0x0)
    OP_95(0xFE, -12700, 0, 10000, 1000, 0x0)
    OP_95(0xFE, -18000, 0, 5200, 1000, 0x0)
    OP_95(0xFE, -18000, 0, -5750, 1000, 0x0)
    Jump("Function_6_1337")

    label("loc_13E7")

    Return()

    # Function_6_1337 end

    def Function_7_13E8(): pass

    label("Function_7_13E8")

    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1435")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x7, 0x2000000)

    label("loc_1435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1449")
    ClearMapObjFlags(0xD, 0x2000000)

    label("loc_1449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1458")
    ClearMapObjFlags(0xD, 0x2000000)

    label("loc_1458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1467")
    ClearMapObjFlags(0xA, 0x2000000)

    label("loc_1467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1488")
    ClearMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)

    label("loc_1488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1497")
    ClearMapObjFlags(0xF, 0x2000000)

    label("loc_1497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AB")
    ClearMapObjFlags(0xB, 0x2000000)

    label("loc_14AB")

    Return()

    # Function_7_13E8 end

    def Function_8_14AC(): pass

    label("Function_8_14AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E7")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156E")
    SetChrPos(0x0, 4870, 3350, 31570, 180)
    SetChrPos(0x1, 4870, 3350, 31570, 180)
    SetChrPos(0x2, 4870, 3350, 31570, 180)
    SetChrPos(0x3, 4870, 3350, 31570, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1541")
    SetChrPos(0x4, 4870, 3350, 31570, 180)
    SetChrPos(0x5, 4870, 3350, 31570, 180)
    Jump("loc_1560")

    label("loc_1541")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1560")
    SetChrPos(0x4, 4870, 3350, 31570, 180)

    label("loc_1560")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16E7")

    label("loc_156E")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1646")
    SetChrPos(0x0, -28110, 2000, 23520, 90)
    SetChrPos(0x1, -28110, 2000, 23520, 90)
    SetChrPos(0x2, -28110, 2000, 23520, 90)
    SetChrPos(0x3, -28110, 2000, 23520, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1619")
    SetChrPos(0x4, -28110, 2000, 23520, 90)
    SetChrPos(0x5, -28110, 2000, 23520, 90)
    Jump("loc_1638")

    label("loc_1619")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1638")
    SetChrPos(0x4, -28110, 2000, 23520, 90)

    label("loc_1638")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16E7")

    label("loc_1646")

    SetChrPos(0x0, -19600, 0, -27950, 0)
    SetChrPos(0x1, -19600, 0, -27950, 0)
    SetChrPos(0x2, -19600, 0, -27950, 0)
    SetChrPos(0x3, -19600, 0, -27950, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16BF")
    SetChrPos(0x4, -19600, 0, -27950, 0)
    SetChrPos(0x5, -19600, 0, -27950, 0)
    Jump("loc_16DE")

    label("loc_16BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16DE")
    SetChrPos(0x4, -19600, 0, -27950, 0)

    label("loc_16DE")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16E7")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_16FE")
    Jump("loc_1B60")

    label("loc_16FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_170C")
    Jump("loc_1B60")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 1)), scpexpr(EXPR_END)), "loc_171A")
    Jump("loc_1B60")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1750")
    SetChrPos(0xB, 39670, -2500, -19380, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, 38440, -2490, -18080, 180)
    Jump("loc_1B60")

    label("loc_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1786")
    SetChrFlags(0x8, 0x80)
    BeginChrThread(0xA, 0, 0, 3)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x9, 0x16)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_1B60")

    label("loc_1786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_17AF")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_1B60")

    label("loc_17AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_186B")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x24, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1815")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x16, 40740, -2500, -2330, 180)
    SetChrPos(0x17, 40630, -2500, -3760, 0)
    Jump("loc_1866")

    label("loc_1815")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x15, 0x10)
    SetChrPos(0x16, 38970, -2500, 3640, 90)
    SetChrPos(0x12, 39450, -2500, -2530, 90)
    SetChrPos(0x14, 39750, -2500, -1190, 90)

    label("loc_1866")

    Jump("loc_1B60")

    label("loc_186B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1883")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_1B60")

    label("loc_1883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_190D")
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x10)
    ClearChrFlags(0x26, 0x4)
    SetChrPos(0xB, -7150, 0, 12300, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C1")
    SetChrFlags(0xB, 0x10)

    label("loc_18C1")

    SetChrPos(0xC, -8150, 0, 12300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E1")
    SetChrFlags(0xC, 0x10)

    label("loc_18E1")

    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_93(0x23, 0xB4, 0x0)
    SetChrPos(0x23, -17800, 0, 15000, 180)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_1B60")

    label("loc_190D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A1A")
    BeginChrThread(0xA, 0, 0, 3)
    SetChrPos(0xB, -4350, 0, -8570, 45)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -5350, 0, -8570, 45)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1999")
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_1999")

    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x22, 0x80)
    BeginChrThread(0x22, 0, 0, 0)
    SetChrPos(0x22, -1800, -310, 6250, 135)
    ClearChrFlags(0x23, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A15")
    ClearChrFlags(0x34, 0x80)
    SetChrPos(0x34, 9330, -690, -1000, 270)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 9330, -690, 600, 270)

    label("loc_1A15")

    Jump("loc_1B60")

    label("loc_1A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A7E")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A43")
    SetChrFlags(0xB, 0x10)

    label("loc_1A43")

    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_1A6F")
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x10)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x10)

    label("loc_1A6F")

    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_1B60")

    label("loc_1A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AD4")
    BeginChrThread(0xA, 0, 0, 3)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AC6")
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)

    label("loc_1AC6")

    SetChrChipByIndex(0x9, 0x16)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_1B60")

    label("loc_1AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B60")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFD")
    SetChrFlags(0xB, 0x10)

    label("loc_1AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0C")
    SetChrFlags(0xC, 0x10)

    label("loc_1B0C")

    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_1B4F")
    ClearChrFlags(0x24, 0x80)
    SetChrChipByIndex(0x1E, 0x23)
    SetChrPos(0x1E, 41500, -2500, 160, 90)
    SetChrPos(0x1F, 41500, -2500, -1440, 90)
    Jump("loc_1B60")

    label("loc_1B4F")

    SetChrChipByIndex(0x1E, 0x14)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)

    label("loc_1B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B84")
    SetChrPos(0x18, 42400, -2500, -18000, 270)
    ClearChrFlags(0x18, 0x80)

    label("loc_1B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_END)), "loc_1BB1")
    ClearChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BB1")
    ClearChrFlags(0xC, 0x10)

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1BC5")
    ClearScenarioFlags(0x22, 0)
    Event(0, 50)
    Jump("loc_1C49")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1BD9")
    ClearScenarioFlags(0x22, 1)
    Event(0, 96)
    Jump("loc_1C49")

    label("loc_1BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1BED")
    ClearScenarioFlags(0x22, 2)
    Event(0, 95)
    Jump("loc_1C49")

    label("loc_1BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1C01")
    ClearScenarioFlags(0x22, 3)
    Event(0, 91)
    Jump("loc_1C49")

    label("loc_1C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1C18")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x3, 0)
    Event(0, 56)
    Jump("loc_1C49")

    label("loc_1C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1C2C")
    ClearScenarioFlags(0x22, 5)
    Event(0, 76)
    Jump("loc_1C49")

    label("loc_1C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1C49")
    ClearScenarioFlags(0x22, 6)
    SetChrPos(0x0, 19290, 0, 17220, 180)

    label("loc_1C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C5A")
    Event(0, 75)

    label("loc_1C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C85")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_1C85")

    Return()

    # Function_8_14AC end

    def Function_9_1C86(): pass

    label("Function_9_1C86")

    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x13DE4, 0x0, 0x71E8)
    OP_E3(0x13C54, 0x0, 0xD1B0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D65")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1D65")

    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DB8")
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DB8")
    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x0)
    OP_66(0x2, 0x1)

    label("loc_1DB8")

    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DEF")
    OP_1B(0x2, 0x0, 0x68)
    OP_66(0x7, 0x1)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_1DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E11")
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetMapObjFrame(0xF, "light", 0x0, 0x1)

    label("loc_1E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E65")
    ClearChrFlags(0x25, 0x80)
    OP_78(0xB, 0x25)
    SetChrPos(0x25, -21240, 0, 14350, 90)
    OP_D5(0x25, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)

    label("loc_1E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA6")
    ClearChrFlags(0x33, 0x80)
    OP_78(0xD, 0x33)
    SetChrPos(0x33, 40000, -4000, -22500, 90)
    OP_D5(0x33, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xD, 0x4)

    label("loc_1EA6")

    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x7, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EFC")
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFC")
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xF1, 0x12C, 0x0, 0x20)

    label("loc_1EFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F15")
    ClearMapObjFlags(0x9, 0x4)
    Jump("loc_1F1B")

    label("loc_1F15")

    SetMapObjFlags(0x9, 0x4)

    label("loc_1F1B")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_1F6E")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    OP_66(0x4, 0x1)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)

    label("loc_1F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA6")
    ModifyEventFlags(1, 4, 0x80)
    ModifyEventFlags(1, 5, 0x80)

    label("loc_1FA6")

    ModifyEventFlags(0, 6, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FCA")
    ModifyEventFlags(1, 6, 0x80)

    label("loc_1FCA")

    OP_52(0x1B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2030")
    OP_65(0x1, 0x1)

    label("loc_2030")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 79890, -3500, 8810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208D")
    OP_70(0x8, 0x0)
    Jump("loc_2091")

    label("loc_208D")

    OP_70(0x8, 0x1E)

    label("loc_2091")

    Return()

    # Function_9_1C86 end

    def Function_10_2092(): pass

    label("Function_10_2092")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2192")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1D7, 1)"), scpexpr(EXPR_END)), "loc_211B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_218D")

    label("loc_211B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_218D")

    Jump("loc_21D7")

    label("loc_2192")

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

    label("loc_21D7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_2092 end

    def Function_11_21E3(): pass

    label("Function_11_21E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_239A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2308")

    #C0004
    ChrTalk(
        0xFE,
        (
            "流石に急な展開でビックリしたけど……\x01",
            "このくらい強く出て言わないと、\x01",
            "２大国に舐められるだけなんだよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "だったら私、断固として\x01",
            "ディーター大統領を支持するわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "アリオス長官だっているんだし……\x01",
            "もういつまでも２大国に\x01",
            "勝手なことばかりさせたくないもの！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2395")

    label("loc_2308")


    #C0007
    ChrTalk(
        0xFE,
        (
            "もちろん不安もあるけど……\x01",
            "私は断固として\x01",
            "ディーター大統領を支持するわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "もういつまでも２大国に\x01",
            "勝手なことばかりさせたくないもの！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2395")

    Jump("loc_339F")

    label("loc_239A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2544")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2493")

    #C0009
    ChrTalk(
        0xFE,
        (
            "川沿いの全壊した会社……\x01",
            "共和国政府と関係があったって噂ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "それが判ったから帝国の雇った\x01",
            "猟兵団に襲われたとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "そんな事情はどうでもいいけど……\x01",
            "とにかく、このクロスベルで\x01",
            "余計な事をしないで欲しいわよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_253F")

    label("loc_2493")


    #C0012
    ChrTalk(
        0xFE,
        (
            "こんな事態になっちゃったのは\x01",
            "クロスベルがいつまでも\x01",
            "従属州だから……なんだよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "だったらやっぱり、\x01",
            "私たちは独立の意志をはっきりと\x01",
            "周辺諸国に示すべきだと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253F")

    Jump("loc_339F")

    label("loc_2544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_26DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263D")

    #C0014
    ChrTalk(
        0xFE,
        (
            "武装集団と交戦している警備隊、\x01",
            "かなり苦戦してるんだってね……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "クロスベルが独立すれば\x01",
            "軍備が強化できて、こんな事態にも\x01",
            "わけなく対処できるって噂だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "やっぱり……クロスベルは\x01",
            "独立すべきなのかしら………？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26D8")

    label("loc_263D")


    #C0017
    ChrTalk(
        0xFE,
        (
            "クロスベルが独立すれば\x01",
            "軍備が強化できて、こんな事態にも\x01",
            "わけなく対処できるって噂だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "やっぱり……クロスベルは\x01",
            "独立すべきなのかしら………？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D8")

    Jump("loc_339F")

    label("loc_26DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_26EB")
    Jump("loc_339F")

    label("loc_26EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_288D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2817")

    #C0019
    ChrTalk(
        0xFE,
        (
            "現時点でも、既に独立に\x01",
            "賛成って人の方が多いのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "……う～ん、でも私、\x01",
            "まだ賛成・反対の良し悪しについて\x01",
            "そんなによく分かってないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "そういえば明日、\x01",
            "市民会館で独立をテーマにした\x01",
            "市民フォーラムがあるらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "今からでも問い合わせてみようかしら？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2888")

    label("loc_2817")


    #C0023
    ChrTalk(
        0xFE,
        (
            "明日、市民会館で独立がテーマの\x01",
            "市民フォーラムがあるらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "今からでも問い合わせてみようかしら？\x02",
    )

    CloseMessageWindow()

    label("loc_2888")

    Jump("loc_339F")

    label("loc_288D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2932")

    #C0025
    ChrTalk(
        0xFE,
        (
            "そういえば、独立の是非を問う\x01",
            "住民投票ってあと１週間ちょっとで\x01",
            "行われるんだったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "う～ん、どうしよう。\x01",
            "そろそろ自分の立場を決めないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339F")

    label("loc_2932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F6")

    #C0027
    ChrTalk(
        0xFE,
        (
            "うふふ、アルカンシェルの\x01",
            "リニューアル舞台、\x01",
            "いよいよもうすぐ公開ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "追加キャストの存在なんかも\x01",
            "ついに明らかになったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "これはもう、目が離せないわね！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A6E")

    label("loc_29F6")


    #C0030
    ChrTalk(
        0xFE,
        (
            "追加キャストの女の子、\x01",
            "シュリちゃんって言うのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "まだ日曜学校に通う年齢なのに……\x01",
            "本当に驚かされるわよね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6E")

    Jump("loc_339F")

    label("loc_2A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2BBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B66")

    #C0032
    ChrTalk(
        0xFE,
        (
            "実際に見れてはいないんだけど、\x01",
            "ユリア准佐の凛々しさって\x01",
            "本当に軍人とは思えないわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "別に私、決してそういう趣味が\x01",
            "あるわけじゃないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "ああいう凛々しいお方になら\x01",
            "ギュッて抱きしめられたいわ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BB5")

    label("loc_2B66")


    #C0035
    ChrTalk(
        0xFE,
        (
            "はぁ～、ユリア准佐って\x01",
            "本当に素敵よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "ギュッて抱きしめられたいわ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_2BB5")

    Jump("loc_339F")

    label("loc_2BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C5B")

    #C0037
    ChrTalk(
        0xFE,
        (
            "さっき、東方風の女性が\x01",
            "東通りの方に歩いていったわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "流れるような長い黒髪と\x01",
            "スーツ姿が決まってて、\x01",
            "かっこよかったなあ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A9")

    label("loc_2C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DD6")

    #C0039
    ChrTalk(
        0xFE,
        (
            "今、東方風の女性が\x01",
            "ここを通りかかってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "流れるような長い黒髪と\x01",
            "スーツ姿が決まってて、\x01",
            "かっこよかったなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00005F（東方風の女性で、黒髪……？）\x02\x03",

            "#00001Fあの、その人はどちらへ？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "うん、東通りの方に\x01",
            "歩いていったみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#00003F東通り……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#00101F（“彼女”かどうかは不確かだけど、\x01",
            "  探してみてもいいかもしれないわね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    SetScenarioFlags(0x1C6, 6)
    Jump("loc_31A9")

    label("loc_2DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3131")

    #C0045
    ChrTalk(
        0xFE,
        (
            "リベール王国から来た……\x01",
            "あの……そう、\x01",
            "ユリア・シュバルツ准佐！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "巷に出回っていた\x01",
            "ピンナップ写真を見たんだけど、\x01",
            "私、一目でファンになっちゃった！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "何でもリベールにはファンクラブ\x01",
            "なるものまであるらしいけど……\x01",
            "外国人でも入れるのかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0048
    ChrTalk(
        0x102,
        (
            "#00105Fファ、ファンクラブ\x01",
            "というのは初耳だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        (
            "#10100Fはい、とある雑誌社の\x01",
            "呼びかけで非公式ながらも\x01",
            "最近、結成されたらしいですよ？\x02\x03",

            "#10102Fファンクラブの会員には、\x01",
            "毎月ユリア准佐の公式行事の\x01",
            "予定表や秘蔵写真が届くとか……！\x02\x03",

            "#10106Fただ、残念ながら……\x01",
            "リベールに住んでいないと\x01",
            "入れないらしいんですけどね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0050
    ChrTalk(
        0xFE,
        "えっ、そうなんですか！？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        "#00103Fう～ん、確かにそれは残念ね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x104)
    Sleep(300)

    #C0052
    ChrTalk(
        0x101,
        "#00005F（ノエルもかなり詳しいな。）\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00306F（ああ、なんつうか、\x01",
            "  俺たちが思っている以上かもな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 0)
    Jump("loc_31A9")

    label("loc_3131")


    #C0054
    ChrTalk(
        0xFE,
        (
            "ユリア准佐のファンクラブ、\x01",
            "入りたかったんだけどなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "だ、誰か遠い親戚にでも\x01",
            "リベールの人はいないかしら！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31A9")

    Jump("loc_339F")

    label("loc_31AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3240")

    #C0056
    ChrTalk(
        0xFE,
        "通商会議はいよいよ明日かぁ。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "各国のＶＩＰなんてこれまで\x01",
            "雑誌くらいでしか見た事ないけど、\x01",
            "みんなオーラが違うんだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339F")

    label("loc_3240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_324E")
    Jump("loc_339F")

    label("loc_324E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_339F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3331")

    #C0058
    ChrTalk(
        0xFE,
        (
            "ディーター市長ってホント\x01",
            "非の打ち所のない人物よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "賢くて正義感があって、\x01",
            "行動力とアイデアもあって、\x01",
            "おまけに資産家でハンサムで……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "はあ、何だか言ってて\x01",
            "目が回りそうになっちゃったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_339F")

    label("loc_3331")


    #C0061
    ChrTalk(
        0xFE,
        (
            "ディーター市長ってホント\x01",
            "非の打ち所のない人物よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "政治・経済以外で\x01",
            "何か悩みごとってあるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_339F")

    TalkEnd(0xFE)
    Return()

    # Function_11_21E3 end

    def Function_12_33A3(): pass

    label("Function_12_33A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33DA")
    Call(0, 90)
    Return()

    label("loc_33DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3849")

    #C0063
    ChrTalk(
        0x1A2,
        "クンクン……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x1A2,
        "フム、なかなかイイ匂いがするな！\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    #C0065
    ChrTalk(
        0x9,
        (
            "お、少年！\x01",
            "君にも我が麺の良さが分かるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x1A2,
        "ああ、まあな。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x1A2,
        (
            "Ｂ級グルメにしては、\x01",
            "イイセンいってると思うぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x9,
        "わ、我が麺を指してＢ級だと……！\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "ええい、帰れ帰れ！\x01",
            "価値の分からぬ人間に食わす\x01",
            "麺などないわ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0070
    ChrTalk(
        0x1A2,
        (
            "お姉さん、\x01",
            "ボクなんか悪いこと言いました？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_3687")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3606():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3606)
    Sleep(50)

    def lambda_3616():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3616)
    Sleep(50)

    def lambda_3626():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3626)
    Sleep(300)

    #C0071
    ChrTalk(
        0x102,
        "#00106Fシン君……\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        (
            "#00306Fなんつうか、こういう所は\x01",
            "世間知らずなんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_3687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_3765")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_36E0():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36E0)
    Sleep(50)

    def lambda_36F0():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36F0)
    Sleep(50)

    def lambda_3700():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3700)
    Sleep(300)

    #C0073
    ChrTalk(
        0x102,
        "#00106Fシン君……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x109,
        (
            "#10106Fなんていうか、こういう所は\x01",
            "世間知らずなんですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_3765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_383E")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_37BE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37BE)
    Sleep(50)

    def lambda_37CE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37CE)
    Sleep(50)

    def lambda_37DE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37DE)
    Sleep(300)

    #C0075
    ChrTalk(
        0x102,
        "#00106Fシン君……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、どうやらこういう所は\x01",
            "世間知らずみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_383E")

    TalkEnd(0x9)
    SetScenarioFlags(0x1DC, 1)
    Jump("loc_38B4")

    label("loc_3849")


    #C0077
    ChrTalk(
        0x9,
        "い、言うに事欠いてＢ級とは……！\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "ええい、帰れ帰れ！\x01",
            "価値の分からぬ人間に食わす\x01",
            "麺などないわ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_38B4")

    Return()

    label("loc_38B5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B7")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_391D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_391D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_393D")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48B2")

    label("loc_393D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3951")
    Jump("loc_48B2")

    label("loc_3951")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_3A1F")

    #C0079
    ChrTalk(
        0xFE,
        (
            "フフ、若者の中にも\x01",
            "見込みのある者がいるものだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "渡したレシピを活用し、\x01",
            "是非とも至高の麺を目指すといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "私も君たちを陰ながら\x01",
            "応援させてもらうからな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_3A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A9C")

    #C0082
    ChrTalk(
        0xFE,
        "ふむ、ついにここまで来たか……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "私もそれなりに覚悟はしたつもりだ。\x01",
            "こうなれば最早、突き進むだけだな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_3A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3B5F")

    #C0084
    ChrTalk(
        0xFE,
        (
            "長年、苦楽を共にしてきた屋台が\x01",
            "壊された時は相当ショックだったが……\x01",
            "前を向かないことにはしょうがない！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "この新しく購入した屋台と一緒に\x01",
            "また心機一転、頑張って行くつもりだ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_3B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3BEB")

    #C0086
    ChrTalk(
        0xFE,
        (
            "マインツにとんでもない\x01",
            "大馬鹿者たちが現れたらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "フン、この煮えたぎった熱々の\x01",
            "茹で汁をぶっかけてやりたいわっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_3BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5C")
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0088
    ChrTalk(
        0xFE,
        "……ぶえっくしょん！\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "ふうむ、少し\x01",
            "身体が冷えてきたようだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3CCA")

    label("loc_3C5C")


    #C0090
    ChrTalk(
        0xFE,
        (
            "よしっ、では\x01",
            "自分用に一杯作るとするか！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "麺をすすれば、身も心もポカポカ……\x01",
            "いや、アツアツだからな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CCA")

    Jump("loc_48B2")

    label("loc_3CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3E06")

    #C0092
    ChrTalk(
        0xFE,
        (
            "ん？　どうやら薬味用の\x01",
            "唐辛子粉が大分\x01",
            "減って来ているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "ふむ、どこかで\x01",
            "適当に時間を見つけて\x01",
            "買い出しに行かんとな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E01")

    #C0094
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

    label("loc_3E01")

    Jump("loc_48B2")

    label("loc_3E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E69")

    #C0095
    ChrTalk(
        0xFE,
        "ふむ、今日の麺も最高の出来だ。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "我が渾身の一杯、\x01",
            "存分に味わっていくがいい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_3E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3FC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F65")

    #C0097
    ChrTalk(
        0xFE,
        (
            "国としての独立を提唱するとは、\x01",
            "ディーター市長も\x01",
            "思い切ったことをするものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "だが私は、そんな市長の\x01",
            "姿勢を前向きに評価しているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "そう、つまりは何事においても\x01",
            "活路は大胆な発想の\x01",
            "上にこそ存在するものだからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FBB")

    label("loc_3F65")


    #C0100
    ChrTalk(
        0xFE,
        (
            "挑戦なくして成功なし……\x01",
            "ふむ、政治の世界も麺の世界も\x01",
            "本質は同じというわけだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FBB")

    Jump("loc_48B2")

    label("loc_3FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_408B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4055")

    #C0101
    ChrTalk(
        0xFE,
        "千の客には千のドラマがある。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "客との触れ合いを通して\x01",
            "そんなドラマの一端に触れる……\x01",
            "これもまた屋台の醍醐味だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4086")

    label("loc_4055")


    #C0103
    ChrTalk(
        0xFE,
        (
            "ご老人と孫娘……\x01",
            "仲睦まじくて結構なことだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4086")

    Jump("loc_48B2")

    label("loc_408B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_44DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4134")

    #C0104
    ChrTalk(
        0xFE,
        (
            "先ほど、明るい赤毛をした\x01",
            "スーツ姿の青年が\x01",
            "私の麺を食べていったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "『デザートでも食べに行くか』と\x01",
            "歓楽街の方に向かって行ったぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44D9")

    label("loc_4134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_438F")

    #C0106
    ChrTalk(
        0xFE,
        (
            "先ほど、明るい赤毛をした\x01",
            "スーツ姿の青年が\x01",
            "私の麺を食べていったのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "秘伝のスープのレシピを暴こうと、\x01",
            "屋台の裏にまで入ってきてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "すんでのところで\x01",
            "追い出すことには成功したが……\x01",
            "とんでもない男がいたものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#00005F（明るい赤毛のスーツ姿の青年……）\x02\x03",

            "#00006F（……この行動といい、\x01",
            "  なんだか思い当たる人物が\x01",
            "  知り合いにいた気がするな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x105,
        "#10300Fその人はどこに行ったんだい？\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "ああ、『デザートでも食べに行くか』と\x01",
            "歓楽街の方に向かって行ったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00001F歓楽街……\x02\x03",

            "#00003F（……まだ“彼”だと\x01",
            "  断言はできないけど、\x01",
            "  追ってみようか……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    SetScenarioFlags(0x1C7, 1)
    Jump("loc_44D9")

    label("loc_438F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4446")

    #C0113
    ChrTalk(
        0xFE,
        (
            "ふむ、今日は各国首脳が\x01",
            "クロスベル入りしたとだけあって、\x01",
            "華やかながらも物々しい雰囲気だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "警戒しているのは判るのだが、\x01",
            "警官の視線が気になって仕方ないぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_44D9")

    label("loc_4446")


    #C0115
    ChrTalk(
        0xFE,
        (
            "警官連中は警戒のためか、\x01",
            "ウチの屋台にもチラチラ視線を\x01",
            "送ってくるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "全く、これでは仕事に集中できん。\x01",
            "早く日常に戻って欲しいものだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D9")

    Jump("loc_48B2")

    label("loc_44DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_461A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4599")

    #C0117
    ChrTalk(
        0xFE,
        "麺はコシだ！　そして喉越しだ！\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "言っておくが、うちの麺は\x01",
            "上品に食べる必要など全くないぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "麺は豪快にすすってこそ\x01",
            "その旨みを堪能できるのだからな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4615")

    label("loc_4599")


    #C0120
    ChrTalk(
        0xFE,
        (
            "言っておくが、うちの麺は\x01",
            "上品に食べる必要など全くないぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "麺は豪快にすすってこそ\x01",
            "その旨みを堪能できるのだからな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4615")

    Jump("loc_48B2")

    label("loc_461A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_467E")

    #C0122
    ChrTalk(
        0xFE,
        "ピンクの傘の女の子……？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "いや、こちらには\x01",
            "来ていなかったと思うが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4760")

    label("loc_467E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4706")

    #C0124
    ChrTalk(
        0xFE,
        "麺の道は忍耐だ！\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        "これしきの雨に私は負けんぞっ！\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#00003F（器に雨が入らないか、\x01",
            "  なにげに心配だなぁ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4760")

    label("loc_4706")


    #C0127
    ChrTalk(
        0xFE,
        (
            "さあ、折角来たのだから\x01",
            "ぜひとも一杯食していかないか。\x01",
            "冷えた身体がたちまち暖まるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4760")

    Jump("loc_48B2")

    label("loc_4765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_48B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4858")

    #C0128
    ChrTalk(
        0xFE,
        (
            "麺の道は一日にして成らず……\x01",
            "そしてまた、その道に終わりはない。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "というわけで研究を重ねた上、\x01",
            "この度ついに新作麺を\x01",
            "提供することにあいなった。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "その名も『天上麺≪日輪≫』だ。\x01",
            "ぜひ一度、食していくがいい！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_48B2")

    label("loc_4858")


    #C0131
    ChrTalk(
        0xFE,
        (
            "今度の新作麺には\x01",
            "絶対の自信を持っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "きっと君たちも\x01",
            "満足してくれるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B2")

    Jump("loc_38BF")

    label("loc_48B7")

    TalkEnd(0xFE)
    Return()

    # Function_12_33A3 end

    def Function_13_48BB(): pass

    label("Function_13_48BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4999")

    #C0133
    ChrTalk(
        0xFE,
        (
            "今朝から鉄道便が止まってるせいで、\x01",
            "配達できる数もかなり減っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "……というより、このまま行くと\x01",
            "クロスベルは本当にどうなるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "仕事のことよりそっちが重要だよな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A04")

    label("loc_4999")


    #C0136
    ChrTalk(
        0xFE,
        (
            "ホント、このまま行くと\x01",
            "クロスベルは本当にどうなるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "仕事のことよりそっちが重要だよな……\x02",
    )

    CloseMessageWindow()

    label("loc_4A04")

    Jump("loc_5123")

    label("loc_4A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4A99")

    #C0138
    ChrTalk(
        0xFE,
        (
            "襲撃事件から早くも１週間か……\x01",
            "この辺もやっと落ち着いて来たかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "とにかく、あんな事件は\x01",
            "もう二度と起きて欲しくないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_4A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4B89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B45")

    #C0140
    ChrTalk(
        0xFE,
        (
            "警備隊はマインツの\x01",
            "武装集団を押さえ込むのに、\x01",
            "かなり手こずっているらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "独立して軍隊を所持、か……\x01",
            "やっぱり必要なことなのかもな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4B84")

    label("loc_4B45")


    #C0142
    ChrTalk(
        0xFE,
        (
            "独立して軍隊を所持、か……\x01",
            "やっぱり必要なことなのかもな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B84")

    Jump("loc_5123")

    label("loc_4B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C12")

    #C0143
    ChrTalk(
        0xFE,
        (
            "うおっ！？　雨のせいで\x01",
            "伝票の文字が消えかかってる！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "で、でもまあ、何とか\x01",
            "解読はできそうだな、うん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4C89")

    label("loc_4C12")


    #C0145
    ChrTalk(
        0xFE,
        (
            "配達先の確認にいちいち\x01",
            "本部に戻ってたんじゃ\x01",
            "かなりの時間ロスだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "ふう、しかし\x01",
            "雨の日は色々と大変だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C89")

    Jump("loc_5123")

    label("loc_4C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4CFE")

    #C0147
    ChrTalk(
        0xFE,
        (
            "駅前から西通りの間を\x01",
            "救急車が何台も\x01",
            "往復しているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        "一体、何があったんだろう？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_4CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4D54")

    #C0149
    ChrTalk(
        0xFE,
        "さあて、今日もバリバリ働くぞ～！\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "効率のいいルートは、っと……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_4D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDF")

    #C0151
    ChrTalk(
        0xFE,
        (
            "さてと、あと２件ほど回ったら\x01",
            "昼メシにでもするかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "よ～し、そう考えたら\x01",
            "どことなく力が湧いてきたぞ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4E16")

    label("loc_4DDF")


    #C0153
    ChrTalk(
        0xFE,
        (
            "あと２件回ったらメシ、\x01",
            "あと２件回ったらメシ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E16")

    Jump("loc_5123")

    label("loc_4E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EEB")

    #C0154
    ChrTalk(
        0xFE,
        (
            "通商会議の期間中、\x01",
            "新市庁ビル方面への民間依頼の配達は\x01",
            "警察から一切止められているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "ま、不審物でも紛れ込もうものなら\x01",
            "あらゆる意味で洒落にならないからね。\x01",
            "至極当然の処置だと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_4EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4FC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F99")

    #C0156
    ChrTalk(
        0xFE,
        (
            "午前中はＶＩＰの来訪で\x01",
            "流石に配達どころじゃなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "だがしかしっ、今日も\x01",
            "いつも通りの仕事量でね……\x01",
            "今まさにシワ寄せを食ってる所さ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4FBB")

    label("loc_4F99")


    #C0158
    ChrTalk(
        0xFE,
        "ダッシュダッシュダーッシュ！\x02",
    )

    CloseMessageWindow()

    label("loc_4FBB")

    Jump("loc_5123")

    label("loc_4FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_501C")

    #C0159
    ChrTalk(
        0xFE,
        "巡回の警察官がけっこういるね。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        "……ぶつからないよう気をつけないと。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_501C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_50DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_506A")

    #C0161
    ChrTalk(
        0xFE,
        (
            "悪いけど、今仕事中でさ。\x01",
            "女の子なんて見てないね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50DA")

    label("loc_506A")


    #C0162
    ChrTalk(
        0xFE,
        (
            "へへっ、雨だろうが嵐だろうが、\x01",
            "ドンと来いってんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "……とは言ったものの、\x01",
            "流石に嵐はカンベンだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50DA")

    Jump("loc_5123")

    label("loc_50DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5123")

    #C0164
    ChrTalk(
        0xFE,
        (
            "ふう、忙しい忙しい……\x01",
            "やっぱり配達屋は体力勝負だね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5123")

    TalkEnd(0xFE)
    Return()

    # Function_13_48BB end

    def Function_14_5127(): pass

    label("Function_14_5127")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51ED")

    #C0165
    ChrTalk(
        0xFE,
        (
            "何という愚かな演説じゃ……\x01",
            "世間は騙せても、\x01",
            "このワシは騙されんぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "何が独立国、何が国防軍じゃ！\x01",
            "本当に２大国の脅威から我々を\x01",
            "守り切れるとでも思っておるのか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_525B")

    label("loc_51ED")


    #C0167
    ChrTalk(
        0xFE,
        (
            "女神よ……\x01",
            "ワシのことなど、どうでもいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "じゃから、どうか孫娘を、\x01",
            "アミサのことをお救い下され……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_525B")

    Jump("loc_58E5")

    label("loc_5260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_52DE")

    #C0169
    ChrTalk(
        0xFE,
        (
            "あの時、少しでも逃げ遅れておったら\x01",
            "ワシもアミサも……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "……そう考えると\x01",
            "今でも恐ろしくて仕方ないわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_52DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5350")

    #C0171
    ChrTalk(
        0xFE,
        (
            "まったく、嘆かわしいことじゃわい。\x01",
            "マインツの人たちを苦しめて\x01",
            "一体、何になると言うんじゃ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_5350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_53E5")

    #C0172
    ChrTalk(
        0xFE,
        (
            "ふむ、あの遠くに見えるのが\x01",
            "観覧車というやつじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "……のう、アミサ。\x01",
            "今度おじいちゃんと２人で\x01",
            "テーマパークに行ってみんか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_53E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_543E")

    #C0174
    ChrTalk(
        0xFE,
        (
            "わははははっ、\x01",
            "どうじゃ見たか、アミサ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        "おじいちゃんは凄かろう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_543E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54A1")

    #C0176
    ChrTalk(
        0xFE,
        "待っておれよ、アミサ～！\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "今、おじいちゃんが\x01",
            "大物を釣り上げてやるからのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_54A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54AF")
    Jump("loc_58E5")

    label("loc_54AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_551C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54CA")
    Call(0, 15)
    Jump("loc_5517")

    label("loc_54CA")


    #C0178
    ChrTalk(
        0xFE,
        (
            "アミサは本当に優しい、\x01",
            "いい子じゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "……何だか泣けてきたわい。\x02",
    )

    CloseMessageWindow()

    label("loc_5517")

    Jump("loc_58E5")

    label("loc_551C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_567C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55E7")

    #C0180
    ChrTalk(
        0xFE,
        (
            "通商会議の期間中は\x01",
            "波止場での釣りを控えるよう\x01",
            "警察に言われてしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "じゃが、たまにはこうして\x01",
            "孫娘と街の様子を眺めるのも\x01",
            "楽しいもんじゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xB, 0x2D, 0x0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_561C")

    label("loc_55E7")


    #C0182
    ChrTalk(
        0xFE,
        (
            "ほう、どれどれ。\x01",
            "あれがみっしぃと言うんじゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_561C")

    Jump("loc_5677")

    label("loc_5621")


    #C0183
    ChrTalk(
        0xFE,
        (
            "ふむ、あそこまで\x01",
            "踊れると楽しかろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "若いというのは\x01",
            "ええもんじゃのう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5677")

    Jump("loc_58E5")

    label("loc_567C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5774")

    #C0185
    ChrTalk(
        0xFE,
        (
            "通商会議だか何だか知らんが、\x01",
            "警察どもが街に出張っておって\x01",
            "うっとうしいのう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0186
    ChrTalk(
        0xFE,
        "……はっ、いかんいかん。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "アミサに止められておる\x01",
            "文句をまた言ってしまったぞい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_581B")

    label("loc_5774")


    #C0188
    ChrTalk(
        0xFE,
        (
            "アミサが言うには、わしの文句は\x01",
            "身体によくないんじゃそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "真偽はともかく、アミサの\x01",
            "悲しむ顔は見たくないからのう。\x01",
            "なるべく言わんよう努力してる所じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_581B")

    Jump("loc_58E5")

    label("loc_5820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_582E")
    Jump("loc_58E5")

    label("loc_582E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_58E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5849")
    Call(0, 16)
    Jump("loc_58E5")

    label("loc_5849")


    #C0190
    ChrTalk(
        0xFE,
        (
            "ワシは今の世の中も\x01",
            "病院も大嫌いじゃが……\x01",
            "孫娘のことだけは大好きじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "じゃから、この子の言うことは\x01",
            "なるべく素直に聞いてみることに\x01",
            "したんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58E5")

    TalkEnd(0xFE)
    Return()

    # Function_14_5127 end

    def Function_15_58E9(): pass

    label("Function_15_58E9")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0192
    ChrTalk(
        0xB,
        (
            "ほふっ、ほふっ……\x01",
            "このタンメンというものは\x01",
            "熱くて食べづらいのう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)
    Sleep(500)

    #C0193
    ChrTalk(
        0xC,
        (
            "もう、おじいちゃんったら\x01",
            "慌てて食べるからだよぉ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xC,
        (
            "そうだ、アミサが\x01",
            "フーフーしてあげるから\x01",
            "ちょっと待っててね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)
    Sleep(500)

    #C0195
    ChrTalk(
        0xC,
        (
            "フーフー、フゥー……\x01",
            "はい、どうぞ召し上がれ♪\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "おおっ……\x01",
            "ありがとうのう、アミサ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x0)
    OP_93(0xC, 0x0, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_15_58E9 end

    def Function_16_5A49(): pass

    label("Function_16_5A49")


    #C0197
    ChrTalk(
        0xC,
        (
            "おじいちゃん、\x01",
            "今日もお薬もらって来たからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "ふむ、いつもすまんのう。\x01",
            "では後で飲ませてもらうぞい。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xC,
        (
            "ダ～メ、そう言って\x01",
            "私が目を離すと、まだたまに\x01",
            "飲んでくれないの知ってるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xC,
        (
            "今日もこれからご飯を一緒して、\x01",
            "見届けさせてもらうからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        (
            "そ、そうか……\x01",
            "アミサは何でもお見通しじゃのう。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_16_5A49 end

    def Function_17_5B92(): pass

    label("Function_17_5B92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5C0A")

    #C0202
    ChrTalk(
        0xFE,
        (
            "おじいちゃんが言うみたいに\x01",
            "本当に戦争になっちゃうのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        "……そんなのヤダよ、怖いよ………\x02",
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5C55")

    #C0204
    ChrTalk(
        0xFE,
        (
            "あそこにあった赤い建物……\x01",
            "すっかりなくなっちゃったね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5C96")

    #C0205
    ChrTalk(
        0xFE,
        (
            "おじいちゃん、\x01",
            "イライラは身体に良くないよ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5CEB")

    #C0206
    ChrTalk(
        0xFE,
        (
            "えっ、本当にいいの、\x01",
            "おじいちゃん！？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "わーい！　凄く楽しみ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5D4B")

    #C0208
    ChrTalk(
        0xFE,
        "うんっ！\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "それにさっきのお魚、\x01",
            "ホントにおっきかったね。\x01",
            "晩御飯が楽しみ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5DB7")

    #C0210
    ChrTalk(
        0xFE,
        (
            "おじいちゃん、\x01",
            "今、竿がピクって動いたよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "ドキドキ……\x01",
            "お魚さん、かかってるかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5DC5")
    Jump("loc_6001")

    label("loc_5DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DE0")
    Call(0, 15)
    Jump("loc_5E22")

    label("loc_5DE0")


    #C0212
    ChrTalk(
        0xFE,
        "おじいちゃん、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "何か悲しいことでもあったの？\x02",
    )

    CloseMessageWindow()

    label("loc_5E22")

    Jump("loc_6001")

    label("loc_5E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5F02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E7B")

    #C0214
    ChrTalk(
        0xFE,
        "見て見て、おじいちゃん！\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        "公園にみっしぃがいるよ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EFD")

    label("loc_5E7B")

    OP_4B(0xB, 0xFF)

    #C0216
    ChrTalk(
        0xFE,
        (
            "おじいちゃん、\x01",
            "今度はアミサと一緒に\x01",
            "ダンスに参加しよーよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xB,
        (
            "う、う～む……\x01",
            "さすがにワシには\x01",
            "厳しい気がするのう。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_5EFD")

    Jump("loc_6001")

    label("loc_5F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5F10")
    Jump("loc_6001")

    label("loc_5F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5F1E")
    Jump("loc_6001")

    label("loc_5F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F39")
    Call(0, 16)
    Jump("loc_6001")

    label("loc_5F39")


    #C0218
    ChrTalk(
        0xFE,
        (
            "根気よくお願いしてたら、\x01",
            "頑固なおじいちゃんも最近ようやく\x01",
            "お薬を飲んでくれるようになったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "わたしが見てないと\x01",
            "さぼっちゃう時もあるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "えへへ、諦めずに\x01",
            "お願いを続けて良かったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6001")

    TalkEnd(0xFE)
    Return()

    # Function_17_5B92 end

    def Function_18_6005(): pass

    label("Function_18_6005")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_60CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60AB")

    #C0221
    ChrTalk(
        0xFE,
        "えっほっ……えっほっ……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "明日はいよいよ\x01",
            "リニューアル舞台の公開日なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "雨だからって\x01",
            "落ち着いていられるわけがないよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_60C9")

    label("loc_60AB")


    #C0224
    ChrTalk(
        0xFE,
        "えっほっ……えっほっ……\x02",
    )

    CloseMessageWindow()

    label("loc_60C9")

    Jump("loc_61E9")

    label("loc_60CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6180")

    #C0225
    ChrTalk(
        0xFE,
        "えっほっ……えっほっ……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "休むことも大事だって言っても、\x01",
            "じっとなんかしてられないよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "それに体を動かしてた方が\x01",
            "余計なことを考えずに済むからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_61E9")

    label("loc_6180")


    #C0228
    ChrTalk(
        0xFE,
        "えっほっ……えっほっ……\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "それにしても、最近は外で走ってると\x01",
            "必ずセリーヌ先輩と一緒になるなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61E9")

    TalkEnd(0xFE)
    Return()

    # Function_18_6005 end

    def Function_19_61ED(): pass

    label("Function_19_61ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_62B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_626A")

    #C0230
    ChrTalk(
        0xFE,
        "わ、わたくしだって……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "ニコルにも、そしてシュリにも\x01",
            "負けるつもりはありませんからっ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_62AD")

    label("loc_626A")


    #C0232
    ChrTalk(
        0xFE,
        (
            "ニコルにも、そしてシュリにも\x01",
            "負けるつもりはありませんからっ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62AD")

    Jump("loc_62FA")

    label("loc_62B2")


    #C0233
    ChrTalk(
        0xFE,
        (
            "ニコルめ……\x01",
            "私のことを出し抜こうったって\x01",
            "そうはいきませんからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62FA")

    TalkEnd(0xFE)
    Return()

    # Function_19_61ED end

    def Function_20_62FE(): pass

    label("Function_20_62FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6368")

    #C0234
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みんな～、こんにちは～！\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、今日は\x01",
            "一日楽しもうネ～☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6393")

    label("loc_6368")


    #C0236
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、今日は\x01",
            "一日楽しもうネ～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6393")

    Jump("loc_6402")

    label("loc_6398")


    #C0237
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、\x01",
            "楽しいお兄さんだったネ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "次はワンダーランドで\x01",
            "一緒に踊ってくれたら嬉しいナ～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6402")

    TalkEnd(0xFE)
    Return()

    # Function_20_62FE end

    def Function_21_6406(): pass

    label("Function_21_6406")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_649C")

    #C0239
    ChrTalk(
        0xFE,
        (
            "今日はみっしぃが特別に\x01",
            "ミシュラムからやって来てくれたよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "色々なイベントを用意してるから、\x01",
            "みんなで楽しんでいってね～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_651D")

    label("loc_649C")


    #C0241
    ChrTalk(
        0xFE,
        (
            "いや～、驚きましたよ。\x01",
            "みっしぃのダンスにあそこまで\x01",
            "合わせられるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "せっかくだから\x01",
            "スカウトすればよかったなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_651D")

    TalkEnd(0xFE)
    Return()

    # Function_21_6406 end

    def Function_22_6521(): pass

    label("Function_22_6521")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65D3")

    #C0243
    ChrTalk(
        0xFE,
        (
            "うふふ、もう少ししたら\x01",
            "みっしぃのダンスショーが\x01",
            "始まるからね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "しかも、今日はなんと\x01",
            "みっしぃの隣で踊れる特別イベント！\x01",
            "是非是非参加していってね～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_665E")

    label("loc_65D3")


    #C0245
    ChrTalk(
        0xFE,
        (
            "今の金髪の人、最初は楽器で\x01",
            "みっしぃのダンスのＢＧＭを\x01",
            "奏でてたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "途中で自分でも踊りだしてね。\x01",
            "ふふ、楽しい人だったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665E")

    TalkEnd(0xFE)
    Return()

    # Function_22_6521 end

    def Function_23_6662(): pass

    label("Function_23_6662")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_66AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A6")

    #C0247
    ChrTalk(
        0xFE,
        (
            "ビーチ、ビーチ！\x01",
            "ビーチで泳ぎたい～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66A6")

    Jump("loc_6705")

    label("loc_66AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66DC")

    #C0248
    ChrTalk(
        0xFE,
        "うわ～、本物のみっしぃだ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_6705")

    label("loc_66DC")


    #C0249
    ChrTalk(
        0xFE,
        (
            "今度は僕も\x01",
            "みっしぃと踊りたいな～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6705")

    TalkEnd(0xFE)
    Return()

    # Function_23_6662 end

    def Function_24_6709(): pass

    label("Function_24_6709")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6757")

    #C0250
    ChrTalk(
        0xFE,
        (
            "ドキドキ……\x01",
            "はやくダンスショーが\x01",
            "はじまらないかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67BB")

    label("loc_6757")


    #C0251
    ChrTalk(
        0xFE,
        (
            "あの金髪のお兄ちゃんも\x01",
            "なかなかかっこよかったね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "みっしぃにはかなわないけど！\x01",
            "うふふ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67BB")

    TalkEnd(0xFE)
    Return()

    # Function_24_6709 end

    def Function_25_67BF(): pass

    label("Function_25_67BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6817")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6812")

    #N0253
    NpcTalk(
        0xFE,
        "乗客",
        (
            "私はアーケードにある\x01",
            "ブティックも楽しみだわ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6812")

    Jump("loc_687E")

    label("loc_6817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_684D")

    #C0254
    ChrTalk(
        0xFE,
        (
            "ほらほら、\x01",
            "落ち着いて見なさいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_687E")

    label("loc_684D")


    #C0255
    ChrTalk(
        0xFE,
        (
            "子供たちも随分と\x01",
            "楽しんでくれたみたいだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_687E")

    TalkEnd(0xFE)
    Return()

    # Function_25_67BF end

    def Function_26_6882(): pass

    label("Function_26_6882")

    TalkBegin(0xFE)

    #N0256
    NpcTalk(
        0xFE,
        "乗客",
        "ふふっ、あなたもコドモよね～。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_6882 end

    def Function_27_68B2(): pass

    label("Function_27_68B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_695F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_691A")

    #C0257
    ChrTalk(
        0xFE,
        (
            "彼女もかなり\x01",
            "喜んでくれたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        "やっぱり行ってよかったな～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_695A")

    label("loc_691A")


    #N0259
    NpcTalk(
        0xFE,
        "市民",
        (
            "あ～、楽しみだなあ。\x01",
            "はやくテーマパークで遊びたいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_695A")

    Jump("loc_6A1A")

    label("loc_695F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B7")

    #C0260
    ChrTalk(
        0xFE,
        "これが噂のみっしぃか……\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "このユルい表情が\x01",
            "何ともたまらないね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1A")

    label("loc_69B7")


    #C0262
    ChrTalk(
        0xFE,
        (
            "みっしぃって、\x01",
            "結構華麗なダンスを\x01",
            "踊れるんだなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "ぬいぐるみだと思って\x01",
            "あなどってたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A1A")

    TalkEnd(0xFE)
    Return()

    # Function_27_68B2 end

    def Function_28_6A1E(): pass

    label("Function_28_6A1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A68")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6A63")

    #C0264
    ChrTalk(
        0xFE,
        (
            "うふふ、お土産を\x01",
            "沢山買ってきちゃった☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A63")

    Jump("loc_6B5B")

    label("loc_6A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AF9")

    #C0265
    ChrTalk(
        0xFE,
        (
            "ワンダーランドは休業中なのに、\x01",
            "街で会えるなんて凄くラッキーね。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "私、これをきっかけに\x01",
            "みっしぃのファンになっちゃいそう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5B")

    label("loc_6AF9")


    #C0267
    ChrTalk(
        0xFE,
        (
            "私、すっかりみっしぃの\x01",
            "ファンになっちゃったわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "お土産にグッズを\x01",
            "沢山買って帰ろうっと！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B5B")

    TalkEnd(0xFE)
    Return()

    # Function_28_6A1E end

    def Function_29_6B5F(): pass

    label("Function_29_6B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B76")
    Call(0, 47)
    Return()

    label("loc_6B76")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_29_6B5F end

    def Function_30_6B7D(): pass

    label("Function_30_6B7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BAF")
    Call(0, 61)
    Jump("loc_6BB2")

    label("loc_6BAF")

    Call(0, 69)

    label("loc_6BB2")

    Return()

    # Function_30_6B7D end

    def Function_31_6BB3(): pass

    label("Function_31_6BB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BD6")
    Call(0, 70)

    label("loc_6BD6")

    Return()

    # Function_31_6BB3 end

    def Function_32_6BD7(): pass

    label("Function_32_6BD7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_6C13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BF5")
    Call(0, 34)
    Jump("loc_6C0E")

    label("loc_6BF5")


    #C0269
    ChrTalk(
        0x1B,
        "#01200Fグルルル……\x02",
    )

    CloseMessageWindow()

    label("loc_6C0E")

    Jump("loc_6C3E")

    label("loc_6C13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6C24")
    Jump("loc_6C3E")

    label("loc_6C24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6C35")
    Jump("loc_6C3E")

    label("loc_6C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C3E")

    label("loc_6C3E")

    TalkEnd(0xFE)
    Return()

    # Function_32_6BD7 end

    def Function_33_6C42(): pass

    label("Function_33_6C42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_6D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C60")
    Call(0, 34)
    Jump("loc_6CFD")

    label("loc_6C60")


    #C0270
    ChrTalk(
        0x1C,
        (
            "#01109Fよーしツァイトー、\x01",
            "今度はシズクの上をジャンプ！\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x1B, 0xFF)

    #C0271
    ChrTalk(
        0x1B,
        "#01203Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x1C,
        (
            "#01106F……『危ないからダメ』？\x01",
            "うーん、そっかー。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)

    label("loc_6CFD")

    Jump("loc_6D2D")

    label("loc_6D02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6D13")
    Jump("loc_6D2D")

    label("loc_6D13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6D24")
    Jump("loc_6D2D")

    label("loc_6D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6D2D")

    label("loc_6D2D")

    TalkEnd(0xFE)
    Return()

    # Function_33_6C42 end

    def Function_34_6D31(): pass

    label("Function_34_6D31")

    OP_4B(0x1C, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x1B, 0xFF)

    #C0273
    ChrTalk(
        0x1C,
        (
            "#01100Fよーし、それじゃあ\x01",
            "シズクやってみてー。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x1D,
        (
            "#06005Fうん、えっと……\x02\x03",

            "#06000F……ツァイトさん、お手っ。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x1B,
        "#01200Fウォン。（ぱふっ）\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x1D,
        (
            "#06005Fわあ……やっぱり賢いなぁ。\x02\x03",

            "#06002Fふふっ、それに肉球も\x01",
            "とっても柔らかいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x1C,
        "#01109Fでしょでしょー？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    OP_4C(0x1C, 0xFF)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x1B, 0xFF)
    Return()

    # Function_34_6D31 end

    def Function_35_6E56(): pass

    label("Function_35_6E56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_6ECA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E74")
    Call(0, 34)
    Jump("loc_6EC5")

    label("loc_6E74")


    #C0278
    ChrTalk(
        0x1D,
        (
            "#06002Fふふ、ツァイトさんは\x01",
            "本当に賢いね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x1B, 0xFF)

    #C0279
    ChrTalk(
        0x1B,
        "#01200F……ウォン。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)

    label("loc_6EC5")

    Jump("loc_6EF5")

    label("loc_6ECA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6EDB")
    Jump("loc_6EF5")

    label("loc_6EDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6EEC")
    Jump("loc_6EF5")

    label("loc_6EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6EF5")

    label("loc_6EF5")

    TalkEnd(0xFE)
    Return()

    # Function_35_6E56 end

    def Function_36_6EF9(): pass

    label("Function_36_6EF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_6F7A")

    #C0280
    ChrTalk(
        0xFE,
        (
            "せっかくだからミシュラムを\x01",
            "少し覗いてくることにしたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "ふふ、今からだと\x01",
            "どれだけ見て回れるかしらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7001")

    label("loc_6F7A")


    #C0282
    ChrTalk(
        0xFE,
        (
            "ふふ、クロスベルって\x01",
            "本当に場所によって雰囲気が\x01",
            "ガラリと変わるよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "歓楽街の方は騒がしかったけど、\x01",
            "ここはのんびりできるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7001")

    TalkEnd(0xFE)
    Return()

    # Function_36_6EF9 end

    def Function_37_7005(): pass

    label("Function_37_7005")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_707A")

    #C0284
    ChrTalk(
        0xFE,
        (
            "これからミシュラムに\x01",
            "行くことになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "ボク、かんらん車ってのに\x01",
            "ゼッタイ乗るんだー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70CD")

    label("loc_707A")


    #C0286
    ChrTalk(
        0xFE,
        (
            "ねえ、ママ……\x01",
            "こんな所、つまんないよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        "早くキラキラの所に戻ろうよー。\x02",
    )

    CloseMessageWindow()

    label("loc_70CD")

    TalkEnd(0xFE)
    Return()

    # Function_37_7005 end

    def Function_38_70D1(): pass

    label("Function_38_70D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_71F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_718C")

    #C0288
    ChrTalk(
        0xFE,
        (
            "止まない雨はない……\x01",
            "……そして晴れない空もない。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "……今、良いことを\x01",
            "言おうとしてみたんだけど\x01",
            "うまくまとまらなかったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_71EB")

    label("loc_718C")


    #C0291
    ChrTalk(
        0xFE,
        (
            "止まない雨はない……\x01",
            "……そして減らない腹もない。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        "……って、ますます酷くなったわね。\x02",
    )

    CloseMessageWindow()

    label("loc_71EB")

    Jump("loc_72BC")

    label("loc_71F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_72BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_7263")

    #C0293
    ChrTalk(
        0xFE,
        "傘をさした女の子……\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "そういえば、ついさっき\x01",
            "見かけたような……\x01",
            "そうでないような。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72BC")

    label("loc_7263")


    #C0295
    ChrTalk(
        0xFE,
        (
            "雨粒って一体どんな形を\x01",
            "してるんでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        "……目を凝らしたら見えるかしら？\x02",
    )

    CloseMessageWindow()

    label("loc_72BC")

    TalkEnd(0xFE)
    Return()

    # Function_38_70D1 end

    def Function_39_72C0(): pass

    label("Function_39_72C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73C3")

    #C0297
    ChrTalk(
        0xFE,
        (
            "ミシュラムにいらっしゃる首脳たちが\x01",
            "間もなくこちらに出発するそうだー。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "彼らがタワー入りする間、\x01",
            "ここは再び封鎖体制に入るからなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "ビジネス街方面に用事があれば\x01",
            "速やかに済ましておくようにー。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        "#00000Fはい、分かりました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_7451")

    label("loc_73C3")


    #C0301
    ChrTalk(
        0xFE,
        (
            "首脳たちがミシュラムから到着したら、\x01",
            "ここは再び封鎖体制に入るからなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "ビジネス街方面に用事があれば\x01",
            "速やかに済ましておくようにー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7451")

    TalkEnd(0xFE)
    Return()

    # Function_39_72C0 end

    def Function_40_7455(): pass

    label("Function_40_7455")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_74FD")

    #C0303
    ChrTalk(
        0xFE,
        (
            "テロリストか……\x01",
            "元々想定はしていたとはいえ、\x01",
            "ここへ来て可能性が高まります。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "まあとにかく、しばらくは\x01",
            "本部の指示通りに動くしかありませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_764A")

    label("loc_74FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_75BE")

    #C0305
    ChrTalk(
        0xFE,
        "みっしぃの出張イベントですか……\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "まあ、ちゃんと市の方にも\x01",
            "許可は取っているみたいだし\x01",
            "問題はなさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "しかしまあ、Ｍ・Ｗ・Ｌも\x01",
            "サービス精神旺盛なことですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_764A")

    label("loc_75BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_764A")

    #C0308
    ChrTalk(
        0xFE,
        (
            "『黒月』の動向調査は\x01",
            "広域防犯課の管轄外ですが……\x01",
            "無論警戒は必要です。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "まあ、表立って何かをする\x01",
            "連中とは思えませんがね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_764A")

    TalkEnd(0xFE)
    Return()

    # Function_40_7455 end

    def Function_41_764E(): pass

    label("Function_41_764E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_773E")

    #C0310
    ChrTalk(
        0xFE,
        (
            "黒月の事務所は全壊したが、\x01",
            "１週間でこの辺りも\x01",
            "大分落ち着いたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "近々行われる住民投票の\x01",
            "おかげか、落ち込んでいる市民も\x01",
            "比較的少ないようだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "何かこう、土壇場の人間の\x01",
            "力強さみたいなものを感じるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7959")

    label("loc_773E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_77D5")

    #C0313
    ChrTalk(
        0xFE,
        (
            "既に市内入りした方も\x01",
            "いるらしいが、首脳たちの多くは\x01",
            "まだミシュラム方面にいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        (
            "テロリストの話もあるしな。\x01",
            "警備にも気を遣うぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7959")

    label("loc_77D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_788A")

    #C0315
    ChrTalk(
        0xFE,
        (
            "オズボーン宰相はミシュラムを、\x01",
            "そしてロックスミス大統領はＩＢＣを\x01",
            "訪ねているようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "どちらもそれぞれ周辺警護は磐石だ。\x01",
            "まあ、まず心配はいらないだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7959")

    label("loc_788A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7959")

    #C0317
    ChrTalk(
        0xFE,
        (
            "何かあったらすぐに\x01",
            "パトカーで駆けつけられるよう\x01",
            "ここで待機しているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "警備隊の車両には負けるが、\x01",
            "こいつも防弾仕様で頑丈だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "いざという時には、\x01",
            "盾にもなってくれるってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7959")

    TalkEnd(0xFE)
    Return()

    # Function_41_764E end

    def Function_42_795D(): pass

    label("Function_42_795D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7A49")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_79D8")

    #C0320
    ChrTalk(
        0x24,
        (
            "水上バスのご利用、\x01",
            "ありがとうございました～。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x24,
        (
            "またのご利用を\x01",
            "お待ちしておりま～す！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A44")

    label("loc_79D8")


    #C0322
    ChrTalk(
        0x24,
        (
            "ミシュラム行き水上バス、\x01",
            "間もなく発進いたしま～す。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x24,
        (
            "ご利用のお客様は\x01",
            "早めにご搭乗くださいませ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A44")

    Jump("loc_7AD4")

    label("loc_7A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_7AD4")

    #C0324
    ChrTalk(
        0xFE,
        (
            "ミシュラム行きの水上バスが\x01",
            "ただいま到着いたしましたー。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "これよりご乗船案内を開始しまーす。\x01",
            "並んでお待ちくださいませー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AD4")

    TalkEnd(0xFE)
    Return()

    # Function_42_795D end

    def Function_43_7AD8(): pass

    label("Function_43_7AD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7C34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BB8")

    #C0326
    ChrTalk(
        0xFE,
        (
            "街は警戒態勢ですが……\x01",
            "こうしていると\x01",
            "何とも穏やかなものですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "通商会議の生み出す熱が\x01",
            "一体どんな渦を巻き起こすのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "こうしてここで、のんびり\x01",
            "思案に耽るのも悪くないものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_7C34")

    label("loc_7BB8")


    #C0329
    ChrTalk(
        0xFE,
        (
            "通商会議の生み出す熱が\x01",
            "一体どんな渦を巻き起こすのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "こうしてここで、のんびり\x01",
            "思案に耽るのも悪くないものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C34")

    TalkEnd(0xFE)
    Return()

    # Function_43_7AD8 end

    def Function_44_7C38(): pass

    label("Function_44_7C38")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D34")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D2C")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0331
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっており、\x01",
            "メッセージプレートが付いている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0332
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《黒月貿易公司・クロスベル支社》\x01",
            "※ご用命の方はノックしてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7D2F")

    label("loc_7D2C")

    Call(0, 72)

    label("loc_7D2F")

    Jump("loc_81A0")

    label("loc_7D34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_808D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FC2")
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(20370, 0, 19380, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(20290, 0)
    SetChrPos(0x101, 18600, 0, 17800, 0)
    SetChrPos(0x102, 19700, 0, 17800, 0)
    SetChrPos(0x109, 18600, 0, 16600, 0)
    SetChrPos(0x105, 19700, 0, 16600, 0)
    SetChrPos(0x104, 19100, 0, 15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0333
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっており、\x01",
            "メッセージプレートが付いている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《黒月貿易公司・クロスベル支社》\x01",
            "※ご用命の方はノックしてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0335
    ChrTalk(
        0x101,
        (
            "#00003F……どうやら\x01",
            "時間切れだったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x104,
        (
            "#00306Fま、しゃあねえな。\x01",
            "諦めて他の用事を潰そうぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0337
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【シン少年への市街地案内】\x07\x00",
            "に失敗した……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x73, 0x1, 0xF)
    OP_29(0x73, 0x4, 0x40)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 18910, 0, 13080, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Jump("loc_8088")

    label("loc_7FC2")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっており、\x01",
            "メッセージプレートが付いている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0339
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《黒月貿易公司・クロスベル支社》\x01",
            "※ご用命の方はノックしてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_8088")

    Jump("loc_81A0")

    label("loc_808D")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっており、\x01",
            "メッセージプレートが付いている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0341
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《黒月貿易公司・クロスベル支社》\x01",
            "※ご用命の方はノックしてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81A0")

    #C0342
    ChrTalk(
        0x101,
        (
            "#00003Fこんなところには、\x01",
            "流石に入り込んでないよな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81A0")

    TalkEnd(0xFF)
    Return()

    # Function_44_7C38 end

    def Function_45_81A4(): pass

    label("Function_45_81A4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83A8")

    #C0343
    ChrTalk(
        0x1A2,
        "ふむ、クロスベルタイムズか。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x1A2,
        (
            "……そういえば、同じ港湾区に\x01",
            "本社があったんだったな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8233():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8233)

    def lambda_8240():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8240)

    #C0345
    ChrTalk(
        0x101,
        "#00005F？　何か言いたげだな？\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x1A2,
        "フン、別に……\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x1A2,
        (
            "強いて言うなら、ウチのことを\x01",
            "コソコソかぎ回るような記者連中が\x01",
            "好きになれないってトコロか。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x1A2,
        (
            "ここの経済誌は共和国の\x01",
            "財界人も取り寄せるし、\x01",
            "もちろん評価はしてるけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        "#00003F（う～ん、なんていうか……）\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x102,
        (
            "#00100F（ええ、ホントよくこの歳で\x01",
            "  そんな所まで感じ取れるわね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_83F3")

    label("loc_83A8")


    #C0351
    ChrTalk(
        0x1A2,
        (
            "通信社なんて\x01",
            "入っても追い返されるだけだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x1A2,
        "さっさと次に行くぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_83F3")

    TalkEnd(0xFF)
    Return()

    # Function_45_81A4 end

    def Function_46_83F7(): pass

    label("Function_46_83F7")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0353
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(75920, 0, 7460, 1500)
    MoveCamera(45, 24, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(11500, 1500)
    Sleep(1000)
    SetChrName("")

    #A0354
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84C6")
    OP_E2(0x2)
    MiniGame(0x6, 0x1, 0x14226, 0xFFFFF63C, 0x3AA2, 0xB4, 0x13812, 0xFFFFF254, 0x226A)

    label("loc_84C6")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_46_83F7 end

    def Function_47_84CB(): pass

    label("Function_47_84CB")

    EventBegin(0x0)
    SoundLoad(483)
    Fade(500)
    OP_68(41500, -1500, -18000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 40400, -2500, -18600, 90)
    SetChrPos(0x102, 40200, -2500, -17400, 90)
    SetChrPos(0x103, 39300, -2500, -18600, 90)
    SetChrPos(0x104, 39100, -2500, -17400, 90)
    SetChrPos(0x109, 41400, -2500, -15600, 135)
    SetChrPos(0x105, 40200, -2500, -15600, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x18, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8905")

    #C0355
    ChrTalk(
        0x18,
        "#11Pあ、支援課の方々ッスよね？\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#6P#00000Fはい。\x01",
            "雨の中お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x102,
        (
            "#00104F#6P手配していただいて\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x18,
        (
            "#11Pいやいや、\x01",
            "これが自分の仕事ッスから。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x18,
        "#11Pそうだ、操縦は大丈夫ッスか？\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x18,
        (
            "#11P何だったら\x01",
            "自分が操縦しますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x101,
        "#6P#00008Fそうか、それがあったな……\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x104,
        (
            "#00303F#6Pまあ、車が運転できるなら\x01",
            "難しいモンじゃねえだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x103,
        (
            "#6P#00200Fここはエニグマで\x01",
            "課長に連絡しましょうか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0364
    ChrTalk(
        0x109,
        (
            "#5P#10105Fあ、大丈夫です。\x02\x03",

            "#10100Fこのタイプのボートだったら\x01",
            "操縦の経験はありますから。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_87AA():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_87AA)
    Sleep(50)

    def lambda_87BA():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_87BA)
    Sleep(50)

    def lambda_87CA():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_87CA)
    Sleep(50)

    def lambda_87DA():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_87DA)
    Sleep(50)

    def lambda_87EA():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_87EA)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    #C0365
    ChrTalk(
        0x101,
        "#12P#00002Fへえ、そうなのか。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x104,
        "#6P#00309Fハハ、さすがだな。\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x105,
        (
            "#10302Fやっぱり運転や操縦の類いは\x01",
            "お手のものみたいだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x109,
        (
            "#5P#10112Fふふ、これもソーニャ司令の\x01",
            "仕込みなんだけど……\x02\x03",

            "#10100F──どうします？\x01",
            "早速ボートに乗りますか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x165, 1)
    Jump("loc_894C")

    label("loc_8905")

    TurnDirection(0x109, 0x101, 500)

    #C0369
    ChrTalk(
        0x109,
        (
            "#5P#10100F──どうします？\x01",
            "早速ボートに乗りますか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    label("loc_894C")


    #C0370
    ChrTalk(
        0x101,
        (
            "#12P#00003Fそうだな……\x02\x03",

            "#00008F（目的地で何があるか分からない。\x01",
            "  他にやり残したことは無いかな？）\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0371
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ボートに乗って目的地へ向かうと\x01",
            "この章ではクロスベルの市外に\x01",
            "出られなくなってしまいます。\x02\x03",

            "クエストなどのやり残しなどに\x01",
            "注意してください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ他に用事がある】\x01",                # 0
            "【ボートに乗って湿地帯に向かう】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_8AD9"),
        (0, "loc_8CDA"),
        (SWITCH_DEFAULT, "loc_8D63"),
    )


    label("loc_8AD9")


    #C0372
    ChrTalk(
        0x109,
        "#5P#10102F了解しました！\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x18,
        (
            "#11Pそれじゃあお気をつけて\x01",
            "行ってらっしゃいッス。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51104.itc", 0x28)
    LoadEffect(0x0, "event\\ev315_00.eff")
    SetChrChipByIndex(0x109, 0x28)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 41600, -3700, -22500, 90)
    SetChrPos(0x101, 41200, -3700, -23500, 90)
    SetChrPos(0x102, 40200, -3100, -21700, 90)
    SetChrPos(0x103, 39200, -3100, -23700, 90)
    SetChrPos(0x104, 38400, -3100, -22500, 90)
    SetChrPos(0x105, 38400, -3100, -21500, 90)
    SetChrFlags(0x18, 0x8000)

    def lambda_8BCC():

        label("loc_8BCC")

        TurnDirection(0xFE, 0x33, 500)
        Yield()
        Jump("loc_8BCC")

    QueueWorkItem2(0x18, 2, lambda_8BCC)
    OP_68(40000, -2500, -22500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(17500, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x32, 0x0, 0xBB8, 0x7D0)
    BeginChrThread(0x33, 3, 0, 51)
    BeginChrThread(0x2F, 1, 0, 49)
    Sleep(2000)
    OP_68(50000, -2500, -22500, 5000)
    MoveCamera(70, 10, 0, 5000)
    SetCameraDistance(27500, 5000)
    BeginChrThread(0x33, 0, 0, 48)
    OP_6F(0x79)
    WaitChrThread(0x33, 0)
    StopBGM(0x1B58)
    OP_68(22140, 4000, 20700, 6000)
    MoveCamera(37, 21, 0, 6000)
    SetCameraDistance(26000, 6000)
    OP_6F(0x79)
    Sleep(300)
    SetCameraDistance(22000, 3000)
    Sleep(2000)
    StopSound(126, 1000, 50)
    StopSound(128, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x18, 0x2)
    WaitBGM()
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 0)
    NewScene("c1210", 0, 0, 0)
    IdleLoop()
    Jump("loc_8D63")

    label("loc_8CDA")


    #C0374
    ChrTalk(
        0x109,
        "#5P#10100F分かりました。\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x18,
        (
            "#11Pそれじゃあ準備が済んだら\x01",
            "声を掛けてくださいッス。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 40000, -2500, -18000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x18, 0xFF)
    EventEnd(0x5)
    Jump("loc_8D63")

    label("loc_8D63")

    Return()

    # Function_47_84CB end

    def Function_48_8D64(): pass

    label("Function_48_8D64")

    OP_96(0x33, 0xA410, 0xFFFFF060, 0xFFFFA81C, 0xBB8, 0x0)

    def lambda_8D7D():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8D7D)
    Sleep(1000)

    def lambda_8D9B():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8D9B)
    Sleep(1000)

    def lambda_8DB9():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8DB9)
    Sleep(1000)

    def lambda_8DD7():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8DD7)

    def lambda_8DE4():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8DE4)

    def lambda_8DF1():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8DF1)

    def lambda_8DFE():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8DFE)

    def lambda_8E0B():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8E0B)

    def lambda_8E18():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8E18)

    def lambda_8E25():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8E25)
    Sleep(1000)

    def lambda_8E43():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8E43)
    WaitChrThread(0x33, 1)
    Return()

    # Function_48_8D64 end

    def Function_49_8E5E(): pass

    label("Function_49_8E5E")

    Sound(470, 0, 100, 0)
    Sound(482, 0, 60, 0)
    Sleep(5000)
    Sound(483, 2, 100, 0)
    Sleep(4000)
    StopSound(483, 2000, 90)
    Return()

    # Function_49_8E5E end

    def Function_50_8E7D(): pass

    label("Function_50_8E7D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(483)
    SetMapObjFlags(0x5, 0x4)
    LoadChrToIndex("apl/ch51104.itc", 0x28)
    LoadChrToIndex("chr/ch00001.itc", 0x29)
    LoadChrToIndex("chr/ch00101.itc", 0x2A)
    LoadEffect(0x0, "event\\ev315_00.eff")
    OP_68(39650, -1200, -36850, 0)
    MoveCamera(56, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16610, 0)
    SetChrChipByIndex(0x109, 0x28)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x33, 0x80)
    ClearMapObjFlags(0xD, 0x4)
    OP_78(0xD, 0x33)
    SetChrPos(0x33, 50980, -4000, -30210, 270)
    OP_D5(0x33, 0x0, 0x41EB0, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x18, 0xFF)
    SetChrPos(0x109, 49200, -3700, -30160, 270)
    SetChrPos(0x101, 53730, -3100, -29070, 1)
    SetChrPos(0x102, 51850, -3100, -29370, 270)
    SetChrPos(0x103, 52260, -3100, -30360, 300)
    SetChrPos(0x104, 50980, -3100, -30930, 270)
    SetChrPos(0x105, 53510, -3100, -31010, 280)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 42410, -2500, -18000, 180)
    OP_68(38240, -1200, -24640, 6000)
    MoveCamera(26, 25, 0, 6000)
    OP_6E(600, 5000)
    SetCameraDistance(16610, 5000)
    BeginChrThread(0x33, 0, 0, 54)
    BeginChrThread(0x33, 3, 0, 51)
    BeginChrThread(0x2F, 1, 0, 55)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    TurnDirection(0x104, 0x18, 0)
    Sleep(120)
    TurnDirection(0x102, 0x18, 0)
    Sleep(120)
    TurnDirection(0x105, 0x18, 0)
    Sleep(90)
    TurnDirection(0x103, 0x18, 0)
    Sleep(900)
    OP_93(0x102, 0x1E, 0x0)
    Sleep(300)
    Sleep(300)
    Sleep(150)
    EndChrThread(0x33, 0x3)
    WaitChrThread(0x33, 0)
    Sleep(500)
    BeginChrThread(0x101, 1, 0, 52)
    Sleep(400)
    BeginChrThread(0x102, 1, 0, 53)
    Sleep(300)

    def lambda_9062():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9062)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x18, 0)
    Sleep(120)
    TurnDirection(0x18, 0x101, 0)

    def lambda_908C():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_908C)
    Sleep(100)

    def lambda_90A4():
        OP_9B(0x0, 0xFE, 0x5, 0x258, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_90A4)
    WaitChrThread(0x102, 1)

    def lambda_90BD():
        OP_9B(0x0, 0xFE, 0xF, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_90BD)
    Sleep(800)
    Fade(1000)
    OP_68(38180, 0, -21930, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11490, 0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x101, 41000, -2500, -17960, 91)
    SetChrPos(0x102, 42180, -2500, -14850, 172)
    SetChrPos(0x103, 40190, -2500, -15950, 127)
    SetChrPos(0x104, 37640, -2500, -16670, 127)
    SetChrPos(0x109, 39080, -2500, -19420, 80)
    SetChrPos(0x105, 38110, -2500, -18360, 81)
    TurnDirection(0x18, 0x101, 0)
    OP_0D()
    Sleep(600)
    Sleep(300)
    OP_93(0x101, 0x0, 0x0)
    Sleep(300)
    OP_68(36420, 0, -4160, 6000)
    MoveCamera(39, 25, 0, 8000)
    OP_6E(600, 8000)
    SetCameraDistance(31000, 8000)

    def lambda_91D0():
        OP_95(0xFE, 38490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91D0)
    Sleep(60)

    def lambda_91ED():
        OP_95(0xFE, 37490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_91ED)
    Sleep(30)
    TurnDirection(0x18, 0x101, 500)

    def lambda_9211():
        OP_95(0xFE, 38490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9211)
    Sleep(30)

    def lambda_922E():
        OP_95(0xFE, 37990, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_922E)

    def lambda_9248():
        OP_95(0xFE, 39490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9248)
    Sleep(30)

    def lambda_9265():
        OP_95(0xFE, 38290, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9265)
    Sleep(600)
    Sleep(300)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 2)
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_50_8E7D end

    def Function_51_929E(): pass

    label("Function_51_929E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92E8")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, -500, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("Function_51_929E")

    label("loc_92E8")

    Return()

    # Function_51_929E end

    def Function_52_92E9(): pass

    label("Function_52_92E9")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x2)
    OP_9C(0xFE, 0xFFFFFE0C, 0xFFFFFC18, 0x9C4, 0x3E8, 0x5DC)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_52_92E9 end

    def Function_53_934A(): pass

    label("Function_53_934A")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x2)
    OP_9C(0xFE, 0xFFFFFE0C, 0xFFFFFC18, 0x9C4, 0x3E8, 0x9C4)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(31, 0, 100, 0)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_53_934A end

    def Function_54_93AB(): pass

    label("Function_54_93AB")

    OP_96(0x33, 0x9858, 0xFFFFF060, 0xFFFFA36C, 0x7D0, 0x0)
    TurnDirection(0x18, 0x33, 0)
    OP_96(0x33, 0x96C8, 0xFFFFF060, 0xFFFFA81C, 0x3E8, 0x0)
    Return()

    # Function_54_93AB end

    def Function_55_93DB(): pass

    label("Function_55_93DB")

    Sound(483, 2, 100, 0)
    Sleep(3000)
    StopSound(483, 500, 100)
    Sound(481, 0, 100, 0)
    Sound(477, 0, 50, 0)
    Sleep(1000)
    Sound(484, 0, 70, 0)
    Sleep(4000)
    Sound(478, 0, 50, 0)
    Return()

    # Function_55_93DB end

    def Function_56_9409(): pass

    label("Function_56_9409")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch44100.itc", 0x28)
    LoadChrToIndex("chr/ch47500.itc", 0x29)
    LoadChrToIndex("chr/ch23600.itc", 0x2A)
    SetChrChipByIndex(0x29, 0x28)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 0, 0, 11000, 180)
    SetChrChipByIndex(0x2A, 0x29)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -1000, 0, 9000, 45)
    SetChrChipByIndex(0x2B, 0x2A)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, 1000, 0, 9000, 270)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    OP_78(0xC, 0x2C)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x2C, 4000, 0, 11000, 90)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    OP_78(0xB, 0x2D)
    OP_49()
    SetChrPos(0x2D, -48000, 2000, 23520, 90)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x1, 0x20)
    OP_68(-6940, 5850, 2500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(6780, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    #C0376
    ChrTalk(
        0x2A,
        (
            "いやー、この広い街を\x01",
            "かっ飛ばすのは最高だねえ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(50)

    #C0377
    ChrTalk(
        0x2A,
        (
            "レジー、おまえも運転が\x01",
            "相当上達してきたじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x2B,
        "へへ、だろ？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x29, 500)
    Sleep(50)

    #C0379
    ChrTalk(
        0x2B,
        (
            "まあ、ユーリの用意した\x01",
            "クルマの性能がいいってのも\x01",
            "あるんだろうけどな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x29, 500)
    Sleep(50)

    #C0380
    ChrTalk(
        0x29,
        (
            "フフン、当然だ。\x01",
            "なんと言ってもヴェルヌ社の\x01",
            "最新型だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x29,
        (
            "……それよりレジー。\x01",
            "さっき、道路に立ってた中年に\x01",
            "危うくぶつけそうになっただろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x2B,
        (
            "あ、ああ……\x01",
            "なんとかギリギリでかわしたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x2B,
        (
            "さすがにあれは……\x01",
            "あのおっさんの驚いた顔ときたら……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x29)
    OP_64(0x2A)
    OP_64(0x2B)

    #C0384
    ChrTalk(
        0x29,
        "#4S#1K#1P……傑作だったな！\x02",
    )


    #C0385
    ChrTalk(
        0x2A,
        "#4S#1K#3P傑作だったよなー！！\x02",
    )


    #C0386
    ChrTalk(
        0x2B,
        "#4S#1K#2P傑作だったよな～！！\x02",
    )

    OP_57(0x1)
    OP_5A()
    OP_63(0x29, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x2A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x29)
    OP_64(0x2A)
    OP_64(0x2B)

    #C0387
    ChrTalk(
        0x2A,
        (
            "わははははは！\x01",
            "あのおっさん、マジで\x01",
            "すっげえビビってたし！\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x2A,
        (
            "ひ、ひ、轢かれちゃうよ～！！\x01",
            "たすけてママ～ン、ってか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)
    Sleep(50)

    #C0389
    ChrTalk(
        0x2B,
        (
            "アハハハハ！！\x01",
            "や、やめてくれよサイクス！\x01",
            "腹がよじれる～～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x29,
        (
            "フフ……\x01",
            "まあ、せっかくの長期滞在だし\x01",
            "楽しませてもらおうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x29,
        (
            "俺たちの新しい遊び場……\x01",
            "このクロスベルって街をな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-34730, 5840, 17160, 0)
    MoveCamera(332, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)
    Sound(457, 0, 100, 0)

    def lambda_9A26():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_9A26)
    OP_68(-29600, 5840, 16660, 2000)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_6F(0x1)
    OP_0D()
    Sleep(1200)
    StopSound(457, 1000, 100)
    Fade(500)
    OP_68(-6940, 5850, 2500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(6780, 0)
    OP_93(0x29, 0x13B, 0x0)
    OP_93(0x2A, 0x13B, 0x0)
    OP_93(0x2B, 0x13B, 0x0)
    OP_0D()
    Sleep(50)

    #C0392
    ChrTalk(
        0x29,
        (
            "おっと……\x01",
            "警察のお出ましみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(50)

    #C0393
    ChrTalk(
        0x2A,
        "レジー、クルマ出せ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)
    Sleep(50)

    #C0394
    ChrTalk(
        0x2B,
        (
            "オッケー、あんな奴ら\x01",
            "ちょちょいと振り切ってやんよ！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    BeginChrThread(0x2B, 1, 0, 58)
    Sleep(100)
    BeginChrThread(0x29, 1, 0, 59)
    Sleep(100)
    BeginChrThread(0x2A, 1, 0, 60)
    Sleep(800)
    Sound(485, 0, 100, 0)
    Sleep(50)
    Sound(100, 0, 50, 0)
    OP_71(0xC, 0x1, 0x1E, 0x1, 0x0)
    OP_79(0xA)
    Sleep(500)
    WaitChrThread(0x2B, 1)

    def lambda_9B8C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_9B8C)

    def lambda_9BA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_9BA1)
    WaitChrThread(0x2B, 2)
    Sleep(100)
    WaitChrThread(0x29, 1)

    def lambda_9BBD():
        OP_9B(0x0, 0xFE, 0xB4, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9BBD)

    def lambda_9BD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_9BD2)
    Sleep(100)
    WaitChrThread(0x2A, 1)

    def lambda_9BEA():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9BEA)

    def lambda_9BFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_9BFF)
    Sleep(100)
    WaitChrThread(0x29, 1)
    WaitChrThread(0x29, 2)
    WaitChrThread(0x2A, 1)
    WaitChrThread(0x2A, 2)
    Sound(100, 0, 50, 0)
    OP_71(0xC, 0x1F, 0x3C, 0x1, 0x0)
    Sleep(500)
    Sound(485, 0, 100, 0)
    OP_79(0xA)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1C3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2C, 0x80)
    OP_78(0xC, 0x2C)
    OP_49()
    SetChrPos(0x2C, 4000, 0, 11000, 90)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_74(0xC, 0x1E)
    Sound(470, 0, 50, 0)
    OP_71(0xC, 0x79, 0xB4, 0x1, 0x20)
    OP_0D()
    Sleep(800)
    BeginChrThread(0x2C, 1, 0, 57)
    Sleep(100)
    OP_68(18560, 1210, 10040, 1500)
    SetCameraDistance(30470, 1500)
    OP_6F(0x79)
    Sleep(50)
    OP_68(17250, 1210, -8950, 1200)
    OP_6F(0x1)
    Sleep(50)
    OP_68(-17400, 1210, -12130, 2500)
    OP_6F(0x1)
    WaitChrThread(0x2C, 1)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    OP_0D()
    Sleep(200)
    SetScenarioFlags(0x22, 6)
    NewScene("c1000", 112, 0, 0)
    IdleLoop()
    Return()

    # Function_56_9409 end

    def Function_57_9D2F(): pass

    label("Function_57_9D2F")

    Sound(494, 0, 100, 0)
    OP_98(0x2C, 0x3A98, 0x0, 0x0, 0x2710, 0x0)
    OP_9F(0x0, 0x2C)
    OP_9F(0x1, 19020, 0, 10300)
    OP_9F(0x1, 19750, 0, 6120)
    OP_9F(0x2, 0x2C, 11000, 0x6)
    Sound(458, 0, 100, 0)
    OP_98(0x2C, 0x0, 0x0, 0xFFFFC568, 0x3A98, 0x0)
    Sound(492, 0, 100, 0)
    OP_9F(0x0, 0x2C)
    OP_9F(0x1, 18580, 0, -9470)
    OP_9F(0x1, 14650, 0, -11440)
    OP_9F(0x1, 10980, 0, -11590)
    OP_9F(0x2, 0x2C, 11000, 0x6)
    OP_98(0x2C, 0xFFFF9688, 0x0, 0x0, 0x4E20, 0x0)
    Sound(492, 0, 100, 0)
    OP_9F(0x0, 0x2C)
    OP_9F(0x1, -18160, 0, -11990)
    OP_9F(0x1, -19820, 0, -15120)
    OP_9F(0x1, -19650, 0, -17640)
    OP_9F(0x2, 0x2C, 11000, 0x6)
    OP_98(0x2C, 0x0, 0x0, 0xFFFFB1E0, 0x3A98, 0x0)
    Return()

    # Function_57_9D2F end

    def Function_58_9E2F(): pass

    label("Function_58_9E2F")

    OP_93(0x2B, 0x5A, 0x3E8)
    OP_9B(0x0, 0x2B, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_93(0x2B, 0x0, 0x1F4)
    Return()

    # Function_58_9E2F end

    def Function_59_9E4D(): pass

    label("Function_59_9E4D")

    OP_93(0x29, 0x0, 0x3E8)
    OP_9B(0x0, 0x29, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_93(0x29, 0x5A, 0x3E8)
    OP_9B(0x0, 0x29, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_93(0x29, 0xB4, 0x1F4)
    Return()

    # Function_59_9E4D end

    def Function_60_9E81(): pass

    label("Function_60_9E81")

    OP_93(0x2A, 0x0, 0x3E8)
    OP_9B(0x0, 0x2A, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_93(0x2A, 0x5A, 0x3E8)
    OP_9B(0x0, 0x2A, 0x0, 0x1388, 0xBB8, 0x0)
    OP_93(0x2A, 0xB4, 0x1F4)
    Return()

    # Function_60_9E81 end

    def Function_61_9EB5(): pass

    label("Function_61_9EB5")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1470, 1330, -4340, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12810, 0)
    SetChrPos(0x101, -750, -690, -3500, 0)
    SetChrPos(0x102, 250, -700, -3730, 0)
    SetChrPos(0x109, -750, -480, -5190, 0)
    SetChrPos(0x105, 250, -520, -5100, 0)
    OP_4B(0x19, 0xFF)
    OP_0D()

    #C0395
    ChrTalk(
        0x19,
        (
            "メイリンの奴、\x01",
            "どこにいったんだろ……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#12P#00100Fあの、すみません。\x01",
            "メイリンちゃんのお兄さんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x19, 0xB4, 0x1F4)

    #C0397
    ChrTalk(
        0x19,
        (
            "ん、そうだけど……\x01",
            "何か用かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        (
            "#12P#00000Fえっと、俺たちはクロスベル警察の\x01",
            "特務支援課の者なんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0399
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは\x01",
            "モモの傘探しをしている\x01",
            "事情を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0400
    ChrTalk(
        0x19,
        (
            "……ああ、なるほど。\x01",
            "そういうことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x19,
        (
            "メイリンが違う子の傘を\x01",
            "持っていってたなんて\x01",
            "俺も気づかなかったなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x19,
        (
            "参ったなあ、そういうことなら\x01",
            "すぐにでも返してやりたいんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x109,
        (
            "#12P#10105Fそういえば……\x01",
            "メイリンちゃんはどこに？\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x105,
        (
            "#12P#10300Fキミと一緒に\x01",
            "散歩に出てたんじゃなかったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x19,
        (
            "実を言うと、さっきメイリンと\x01",
            "かくれんぼを始めたところでさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x19,
        (
            "こんな雨の中面倒だったんだけど、\x01",
            "どうしてもやりたいって言うから\x01",
            "付き合ってるんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0x19, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0x19, 0xB4, 0x1F4)
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0407
    ChrTalk(
        0x19,
        (
            "……あいつ、\x01",
            "隠れるの上手いんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x19,
        (
            "俺は探すのへたくそだし、\x01",
            "すぐに見つけられるかどうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        (
            "#12P#00006Fそ、そうですか……\x02\x03",

            "#00000Fでも、そういうことなら……\x01",
            "俺たちもメイリンちゃんを\x01",
            "探してみてもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x19,
        (
            "ああ、それじゃあ\x01",
            "よろしくたのむよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x19,
        (
            "多分、メイリンは\x01",
            "この港湾区のどっかに\x01",
            "隠れているはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x19,
        (
            "かくれんぼだから、\x01",
            "建物の中には入ってないと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x19,
        (
            "難しいかもしれないけど\x01",
            "探してみてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        "#12P#00100Fええ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、それじゃあ\x01",
            "探してみようか。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -330, -700, -3820, 0)
    OP_93(0x19, 0xB4, 0x0)
    OP_4C(0x19, 0xFF)
    ClearChrFlags(0x19, 0x10)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    OP_66(0x4, 0x1)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    ClearChrFlags(0x1A, 0x80)
    SetScenarioFlags(0x133, 4)
    OP_29(0x6B, 0x1, 0x2)
    OP_C9(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_61_9EB5 end

    def Function_62_A4D0(): pass

    label("Function_62_A4D0")

    TalkBegin(0xFF)

    #C0416
    ChrTalk(
        0x101,
        (
            "#00012Fベンチの下には……\x01",
            "いないよな、どう考えても。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_62_A4D0 end

    def Function_63_A511(): pass

    label("Function_63_A511")

    TalkBegin(0xFF)

    #C0417
    ChrTalk(
        0x101,
        "#00000F……屋台の裏にもいないみたいだ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_63_A511 end

    def Function_64_A545(): pass

    label("Function_64_A545")

    TalkBegin(0xFF)

    #C0418
    ChrTalk(
        0x101,
        "#00006Fコンテナの後ろ！　……いないか。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_64_A545 end

    def Function_65_A579(): pass

    label("Function_65_A579")

    EventBegin(0x1)

    #C0419
    ChrTalk(
        0x101,
        (
            "#00000Fかくれんぼだし、\x01",
            "建物の中にはいないはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -14030, 2000, 24980, 180)
    EventEnd(0x4)
    Return()

    # Function_65_A579 end

    def Function_66_A5CA(): pass

    label("Function_66_A5CA")

    EventBegin(0x1)

    #C0420
    ChrTalk(
        0x101,
        (
            "#00000Fメイリンちゃんは\x01",
            "港湾区のどこかにいるはずだ。\x01",
            "……もう少し探してみるか。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 4500, 3050, 30320, 180)
    EventEnd(0x4)
    Return()

    # Function_66_A5CA end

    def Function_67_A638(): pass

    label("Function_67_A638")

    EventBegin(0x1)

    #C0421
    ChrTalk(
        0x101,
        (
            "#00000Fメイリンちゃんは\x01",
            "港湾区のどこかにいるはずだ。\x01",
            "……もう少し探してみるか。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -19940, 0, -25710, 359)
    EventEnd(0x4)
    Return()

    # Function_67_A638 end

    def Function_68_A6A6(): pass

    label("Function_68_A6A6")

    EventBegin(0x1)

    #C0422
    ChrTalk(
        0x101,
        (
            "#00000Fメイリンちゃんは\x01",
            "港湾区のどこかにいるはずだ。\x01",
            "……もう少し探してみるか。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -25570, 2000, 23250, 90)
    EventEnd(0x4)
    Return()

    # Function_68_A6A6 end

    def Function_69_A714(): pass

    label("Function_69_A714")

    TalkBegin(0x19)

    #C0423
    ChrTalk(
        0x19,
        (
            "あんたら、メイリンはまだ\x01",
            "見つかってないみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x19,
        (
            "どうしても見つけられないなら、\x01",
            "ギブアップ宣言すれば\x01",
            "出てきてくれると思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x19,
        "……どうする？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ギブアップする\x01",      # 0
            "やめておく\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA88")
    EventBegin(0x0)
    Fade(500)
    OP_68(-1470, 1330, -4340, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12810, 0)
    SetChrPos(0x101, -750, -690, -3500, 0)
    SetChrPos(0x102, 250, -700, -3730, 0)
    SetChrPos(0x109, -750, -480, -5190, 0)
    SetChrPos(0x105, 250, -520, -5100, 0)
    OP_93(0x19, 0xB4, 0x0)
    OP_4B(0x19, 0xFF)
    OP_0D()

    #C0426
    ChrTalk(
        0x101,
        "#12P#00006F……すみません、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x19,
        "ま、仕方ないよな。\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x19,
        "それじゃあ……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0429
    AnonymousTalk(
        0x19,
        "#4Sメイリ～ン、ギブア～～～ップ！！#3S\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0x19, 0x5A, 0x0)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x109, 0x2D, 0x0)
    OP_93(0x105, 0x2D, 0x0)
    SetChrPos(0x1A, 2590, -700, -2880, 270)
    OP_4B(0x1A, 0xFF)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0430
    ChrTalk(
        0x1A,
        "……えへへ、メイリンの勝ち～♪\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0431
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そうして、ギブアップした\x01",
            "ロイドたちの下にメイリンが現れ…………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0432
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "メイリンがモモの傘を\x01",
            "間違えて持って行ってしまったことを\x01",
            "改めて説明するのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(0, 71)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB35")

    label("loc_AA88")


    #C0433
    ChrTalk(
        0x101,
        "#00000Fいえ、もう少し探してみます。\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x19,
        "そっか、じゃあ頑張ってくれ。\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x19,
        (
            "ちなみに、俺の方はあんまり\x01",
            "期待しないでくれよな。\x01",
            "……多分、日が暮れちまうからさ。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AB35")

    TalkEnd(0x19)
    Return()

    # Function_69_A714 end

    def Function_70_AB39(): pass

    label("Function_70_AB39")

    EventBegin(0x0)
    Fade(500)
    OP_68(87940, -800, 17550, 0)
    MoveCamera(307, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14760, 0)
    SetChrPos(0x101, 86200, -2500, 17950, 37)
    SetChrPos(0x102, 85470, -2500, 16990, 37)
    SetChrPos(0x109, 84630, -2500, 16160, 37)
    SetChrPos(0x105, 83750, -2500, 15320, 37)
    OP_4B(0x1A, 0xFF)
    OP_0D()

    #C0436
    ChrTalk(
        0x101,
        (
            "#00002Fもしかして……\x01",
            "君はメイリンちゃんかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        "#00102Fふふ、見つけたわね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1A, 0x101, 500)
    Sleep(50)

    #C0438
    ChrTalk(
        0x1A,
        "きゃっ、見つかっちゃった～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0439
    ChrTalk(
        0x1A,
        "あれれ……兄たんじゃない～？\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x1A,
        "お兄ちゃんたち、だあれ？\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x109,
        "#10109Fあはは、ようやくですね。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x105,
        (
            "#10300Fそれじゃ、ロイ君のところに\x01",
            "報告しにいくとしようか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Call(0, 71)
    EventEnd(0x5)
    Return()

    # Function_70_AB39 end

    def Function_71_AD1C(): pass

    label("Function_71_AD1C")

    EventBegin(0x0)
    ClearScenarioFlags(0x133, 4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch21500.itc", 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_B1B5")
    OP_2C(0x6B, 0x1)
    SetChrName("")

    #A0443
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうしてロイドたちは、\x01",
            "メイリンを見つけた場所にロイを呼び……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0444
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "メイリンがモモの傘を\x01",
            "間違えて持って行ってしまったことを\x01",
            "改めて説明するのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(67920, -400, 17980, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13970, 0)
    SetChrPos(0x101, 68760, -2500, 19500, 90)
    SetChrPos(0x102, 68760, -2500, 18300, 90)
    SetChrPos(0x109, 67600, -2500, 18300, 90)
    SetChrPos(0x105, 67600, -2500, 19500, 90)
    SetChrPos(0x19, 70770, -2500, 19500, 270)
    SetChrPos(0x1A, 70700, -2500, 18300, 270)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)
    OP_29(0x6B, 0x1, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    #C0445
    ChrTalk(
        0x101,
        "#6P#00000F……というわけなんだ。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x1A,
        (
            "そっか～……\x01",
            "メイリン、間違えちゃったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x19,
        "メイリン、傘を返してやんな。\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x1A,
        "うん、兄たん。\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x1A,
        "はい、これ～。\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x109,
        "#6P#10100Fそれじゃ、交換だね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_9B(0x1, 0x1A, 0x0, 0x320, 0x5DC, 0x0)
    Sleep(1000)
    OP_9B(0x1, 0x1A, 0xB4, 0x320, 0x5DC, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x2)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    SetChrName("")

    #A0451
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "メイリンに傘を渡し、\x01",
            "モモの傘を受け取った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0452
    ChrTalk(
        0x102,
        "#6P#00100Fふふ、ありがとね。\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x1A,
        "ん～ん。\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x1A,
        (
            "それより、あとでちゃんと\x01",
            "モモちゃんって子に\x01",
            "ごめんなさいしなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x105,
        (
            "#6P#10309Fフフ、小さいのに意外と\x01",
            "しっかりしてるじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x19,
        "ふう、そうなんだよな。\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x19,
        (
            "俺もこのくらいしっかりしてりゃ\x01",
            "今頃仕事の一つや二つ……\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x101,
        (
            "#6P#00012Fえ、えっと……とにかく\x01",
            "ありがとうございました。\x02\x03",

            "#00000Fこちらの傘は俺たちが\x01",
            "責任を持って\x01",
            "届けさせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x19,
        "ああ、よろしくたのむぜ。\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x1A,
        "おねがいね～。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Jump("loc_B584")

    label("loc_B1B5")

    OP_68(-1470, 1230, -4340, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12830, 0)
    SetChrPos(0x101, -750, -690, -3500, 0)
    SetChrPos(0x102, 250, -700, -3730, 0)
    SetChrPos(0x109, -750, -480, -5190, 0)
    SetChrPos(0x105, 250, -520, -5100, 0)
    SetChrPos(0x19, 250, -700, -1650, 180)
    SetChrPos(0x1A, -750, -700, -1650, 180)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)
    OP_29(0x6B, 0x1, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    #C0461
    ChrTalk(
        0x101,
        "#12P#00000F……というわけなんだ。\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x1A,
        (
            "そっか～……\x01",
            "メイリン、間違えちゃったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x19,
        "メイリン、傘を返してやんな。\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x1A,
        "うん、兄たん。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x1A,
        "はい、これ～。\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x109,
        "#12P#10100Fそれじゃ、交換だね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_9B(0x1, 0x1A, 0x0, 0x320, 0x5DC, 0x0)
    Sleep(1000)
    OP_9B(0x1, 0x1A, 0xB4, 0x320, 0x5DC, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x2)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    SetChrName("")

    #A0467
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "メイリンに傘を渡し、\x01",
            "モモの傘を手に入れた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0468
    ChrTalk(
        0x102,
        "#12P#00100Fふふ、ありがとね。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x1A,
        "ん～ん。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x1A,
        (
            "それより、あとでちゃんと\x01",
            "モモちゃんって子に\x01",
            "ごめんなさいしなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x105,
        (
            "#12P#10309Fフフ、小さいのに意外と\x01",
            "しっかりしてるじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x19,
        "ふう、そうなんだよな。\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x19,
        (
            "俺もこのくらいしっかりしてりゃ\x01",
            "今頃仕事の一つや二つ……\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x101,
        (
            "#12P#00012Fえ、えっと……とにかく\x01",
            "ありがとうございました。\x02\x03",

            "#00000Fこちらの傘は俺たちが\x01",
            "責任を持って\x01",
            "届けさせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x19,
        "ああ、よろしくたのむぜ。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x1A,
        "おねがいね～。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)

    label("loc_B584")

    SetScenarioFlags(0x22, 0)
    NewScene("c0210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_71_AD1C end

    def Function_72_B591(): pass

    label("Function_72_B591")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch06300.itc", 0x28)
    LoadChrToIndex("chr/ch31400.itc", 0x29)
    OP_68(20370, 0, 19380, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(19230, 0)
    SetChrPos(0x101, 18600, 0, 17800, 0)
    SetChrPos(0x102, 19700, 0, 17800, 0)
    SetChrPos(0x109, 18600, 0, 16600, 0)
    SetChrPos(0x105, 19700, 0, 16600, 0)
    SetChrPos(0x104, 19100, 0, 15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x27, 0x28)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x27, 0x4)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 19100, 0, 21700, 180)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x28, 0x29)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 19100, 0, 21700, 180)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0477
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっており、\x01",
            "メッセージプレートが付いている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0478
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《黒月貿易公司・クロスベル支社》\x01",
            "※ご用命の方はノックしてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0479
    ChrTalk(
        0x109,
        (
            "#6P#10101F『黒月貿易公司』……\x02\x03",

            "#10103Fあの、ツァオという人が\x01",
            "任されている事務所ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x105,
        (
            "#10304Fツァオ・リー。\x01",
            "《白蘭竜》の異名を持つ、\x01",
            "『黒月#4Rヘイユエ#』きっての切れ者だね。\x02\x03",

            "#10300F挨拶がてら寄っていくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x102,
        (
            "#00103Fうーん、といっても\x01",
            "まともに相手をしてくれるとは\x01",
            "限らないでしょうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x104,
        (
            "#12P#00303Fふむ……\x02\x03",

            "#00301Fルバーチェ跡地の一件については\x01",
            "ちょいと聞いておきたかったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#00008Fそういえば、あの跡地は\x01",
            "黒月も狙っていたんだよな……\x02\x03",

            "#00001F結局、《クリムゾン商会》に\x01",
            "出し抜かれた形になったみたいだけど\x01",
            "どう思っているんだろう？\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 0, 100, 0)
    Sleep(500)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)
    Sleep(500)

    #C0484
    ChrTalk(
        0x27,
        (
            "──フフ、どうもこうも、\x01",
            "非常に遺憾に思っていますよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x27, 3, 0, 73)
    Sleep(700)
    BeginChrThread(0x28, 3, 0, 74)
    Sleep(300)

    def lambda_BA95():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BA95)
    Sleep(50)

    def lambda_BAAD():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BAAD)
    Sleep(50)

    def lambda_BAC5():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BAC5)
    Sleep(50)

    def lambda_BADD():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BADD)
    Sleep(50)

    def lambda_BAF5():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BAF5)
    WaitChrThread(0x101, 1)

    #C0485
    ChrTalk(
        0x101,
        "#12P#00005Fツァ、ツァオ支社長……\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x27,
        (
            "#03200Fごきげんよう。\x01",
            "特務支援課の皆さん。\x02\x03",

            "#03209Fいや～、ちょうど良かった。\x02\x03",

            "実は皆さんに少々、\x01",
            "お願いしたい事がありましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        "#12P#00005Fへ……\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x102,
        "#12P#00105Fお願いしたいこと……？\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x27,
        (
            "#03200Fよろしければ中で、\x01",
            "話を聞いていただけませんか？\x02\x03",

            "#03204Fフフ、もちろん\x01",
            "無理にとは言いませんが。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x27, 0x0, 0x1F4)

    def lambda_BC6C():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_BC6C)
    Sleep(500)

    def lambda_BC89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_BC89)
    WaitChrThread(0x27, 1)
    OP_9B(0x1, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)

    #C0490
    ChrTalk(
        0x101,
        "#12P#00005Fちょ、ちょっと……！？\x02",
    )

    CloseMessageWindow()
    OP_97(0x28, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    OP_93(0x28, 0xB4, 0x1F4)
    Sleep(300)

    #C0491
    ChrTalk(
        0x28,
        (
            "……申し訳ありません。\x01",
            "少々困った事になっておりまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x28,
        (
            "もし、お時間があれば\x01",
            "是非ともお力添えをいただけると。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x28,
        (
            "鍵は開けておきますので\x01",
            "遠慮なく中へお入りください。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x1F4)

    def lambda_BDAA():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_BDAA)
    Sleep(500)

    def lambda_BDC7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_BDC7)
    WaitChrThread(0x28, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x104)

    #C0494
    ChrTalk(
        0x105,
        (
            "#12P#10309Fあはは。\x01",
            "本当に人を喰った連中だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x109,
        (
            "#6P#10106Fワジ君は人のこと\x01",
            "全然言えないと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#00101Fでも、どうするの？\x01",
            "罠とかではないと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x104,
        (
            "#12P#00301F何か情報があるかもしれねぇし、\x01",
            "ここは乗ってみるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x101,
        (
            "#00003Fそうだな……\x01",
            "（こっちも忙しいから無理に\x01",
            "  付き合う必要はなさそうだけど。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x153, 4)
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x2, 0x1)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 18600, 0, 17800, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_72_B591 end

    def Function_73_BFEB(): pass

    label("Function_73_BFEB")


    def lambda_BFF0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_BFF0)

    def lambda_C001():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_C001)
    WaitChrThread(0x27, 1)
    OP_93(0x27, 0xB4, 0x1F4)
    Return()

    # Function_73_BFEB end

    def Function_74_C022(): pass

    label("Function_74_C022")


    def lambda_C027():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C027)

    def lambda_C038():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_C038)
    WaitChrThread(0x28, 1)
    OP_95(0x28, 18100, 0, 19500, 2000, 0x0)
    OP_93(0x28, 0xB4, 0x1F4)
    Return()

    # Function_74_C022 end

    def Function_75_C06D(): pass

    label("Function_75_C06D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xF9, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    OP_68(20340, 100, 18050, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(16510, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_C1F0")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x104, 19680, 0, 18250, 180)
    SetChrPos(0x109, 18460, 0, 19360, 180)
    SetChrPos(0x105, 19600, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C148():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C148)

    def lambda_C162():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C162)
    Sleep(100)

    def lambda_C17F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C17F)
    Sleep(50)

    def lambda_C19C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C19C)
    Sleep(100)

    def lambda_C1B9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C1B9)
    Sleep(50)

    def lambda_C1D6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C1D6)
    Jump("loc_C437")

    label("loc_C1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_C316")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x109, 19680, 0, 18250, 180)
    SetChrPos(0x104, 18460, 0, 19360, 180)
    SetChrPos(0x105, 19600, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C26E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C26E)

    def lambda_C288():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C288)
    Sleep(100)

    def lambda_C2A5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C2A5)
    Sleep(50)

    def lambda_C2C2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C2C2)
    Sleep(100)

    def lambda_C2DF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C2DF)
    Sleep(50)

    def lambda_C2FC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C2FC)
    Jump("loc_C437")

    label("loc_C316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_C437")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x105, 19680, 0, 18250, 180)
    SetChrPos(0x104, 19600, 0, 19360, 180)
    SetChrPos(0x109, 18460, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C394():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C394)

    def lambda_C3AE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C3AE)
    Sleep(100)

    def lambda_C3CB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C3CB)
    Sleep(50)

    def lambda_C3E8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C3E8)
    Sleep(100)

    def lambda_C405():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C405)
    Sleep(50)

    def lambda_C422():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C422)

    label("loc_C437")

    OP_68(20080, 600, 15520, 3000)
    MoveCamera(40, 20, 0, 3000)
    OP_6E(560, 3000)
    SetCameraDistance(16390, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_C476():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C476)
    Sleep(50)

    def lambda_C486():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C486)
    Sleep(300)

    #C0499
    ChrTalk(
        0x1A2,
        (
            "#12Pよしっ、それじゃ\x01",
            "さっそく説明を始めるぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        "#00005Fあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x104,
        (
            "#5P#00306F（あの小僧、ちゃっかり\x01",
            "  お嬢を隣りに据えてんのな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x109,
        "#5P#10100F（ええ、それもごく自然に。）\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x105,
        (
            "#5P#10302F（フフ、ほんと\x01",
            "  エリィも気に入られたものだね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0504
    ChrTalk(
        0x1A2,
        "#12Pなんだ、言いたい事でもあるのか？\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        (
            "#00003Fああいや、大丈夫だ。\x02\x03",

            "#00000Fそれよりも\x01",
            "説明の方をお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x1A2,
        "#12Pフフ、なかなかしゅしょーだな。\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x1A2,
        (
            "#12Pさて、さっきも聞いた通り、\x01",
            "これからお前たちに市内を\x01",
            "案内してもらうわけだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x1A2,
        (
            "#12Pこのひろいクロスベルを\x01",
            "目標もなしに歩きまわっても\x01",
            "ただ疲れるだけだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x1A2,
        (
            "#12Pあらかじめ、ボクが決めておいた\x01",
            "ゴール地点をめざしてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x109,
        "#5P#10105Fゴール地点……？\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x1A2,
        (
            "#12Pああ、ズバリ中央広場の\x01",
            "タイムズ百貨店の屋上だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x1A2,
        (
            "#12Pとにかく、最終的にボクを\x01",
            "そこへ連れて行けば、\x01",
            "任務完了ってことにしてやる。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x104,
        "#5P#00300Fなるほど、分かりやすいな。\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x105,
        (
            "#5P#10300Fちなみに、そこへ行くまでの\x01",
            "ルートは自由に決めていいのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x1A2,
        (
            "#12Pいや、興味のないところを\x01",
            "うろつかれてもボクが困るからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x1A2,
        (
            "#12Pここから百貨店までは、\x01",
            "かならず東通りを経由してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x101,
        (
            "#00006Fなんていうか……\x01",
            "随分、段取りが整ってるんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x1A2,
        (
            "#12Pフフン、せっかく\x01",
            "わざわざ出向いたんだ。\x01",
            "そのくらい計画するのは当然だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x1A2,
        (
            "#12Pだけど、そのほかのことに関しては\x01",
            "いっさいノープランだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x1A2,
        (
            "#12Pせいぜい、いろいろ寄り道して\x01",
            "ボクとエリィお姉さんを楽しませてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0521
    ChrTalk(
        0x102,
        "#11P#00109Fいや、私も案内する立場だから……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0522
    ChrTalk(
        0x1A2,
        "#6Pそんな、めっそうもない――\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x1A2,
        (
            "#6Pお姉さんには、この機会に\x01",
            "少しでも骨休めをしていただかないと！\x02",
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

    #C0524
    ChrTalk(
        0x109,
        (
            "#5P#10109Fあはは、なんかもう\x01",
            "ゾッコンって感じですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#00006Fまあ、大体のことは分かったけど……\x02\x03",

            "#00000F今の話だと、割と普通に\x01",
            "街を回る感じになると思うんだが。\x02\x03",

            "シンはそれでよかったのか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CC0C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_CC0C)
    Sleep(50)

    def lambda_CC1C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CC1C)
    Sleep(300)

    #C0526
    ChrTalk(
        0x104,
        (
            "#5P#00305Fああ、なんつうか、\x01",
            "もっとこう他にねえのかよ？\x02\x03",

            "#00300F例えばアルカンシェルに\x01",
            "行ってみてえ、とか。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x105,
        (
            "#5P#10300Fそうそう、それに\x01",
            "ミシュラムのテーマパークとかね。\x02\x03",

            "#10304Fもっとも、今は休業中だけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x1A2,
        (
            "#12P――フン、そんな有名ドコロは\x01",
            "既に当然行ったに決まってるだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x1A2,
        (
            "#12Pたしかにものすごく楽しかったし、\x01",
            "何度行っても楽しいと思うが――\x01",
            "今回の目的はそんなんじゃないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x1A2,
        (
            "#12Pボクにはもっともっと、\x01",
            "クロスベルを知る必要がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x1A2,
        (
            "#12Pそのためには、\x01",
            "観光地としての顔だけじゃなく、\x01",
            "素顔をみないといけないってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x102,
        "#00105Fクロスベルの素顔……\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x101,
        "#00005Fそこまで考えているのか……\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x104,
        (
            "#5P#00306Fやれやれ、\x01",
            "なんつうか末恐ろしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x1A2,
        (
            "#12P――とにかく、\x01",
            "これでモロモロ理解できたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x1A2,
        (
            "#12P時間も惜しいし、\x01",
            "さっさと案内をはじめてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x101,
        "#00000F分かった、さっそく出発しよう。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D014")
    OP_29(0x73, 0x1, 0x1)
    OP_93(0x104, 0x0, 0x1F4)
    Sleep(300)

    #C0538
    ChrTalk(
        0x104,
        (
            "#12P#00300Fそんじゃ、俺たちは先に行くから\x01",
            "後ろの警戒は頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x109,
        "#5P#10100F了解です。\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x105,
        "#5P#10300Fフフ、行ってらっしゃい。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    Jump("loc_D18F")

    label("loc_D014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D0D8")
    OP_29(0x73, 0x1, 0x2)
    OP_93(0x109, 0x0, 0x1F4)
    Sleep(300)

    #C0541
    ChrTalk(
        0x109,
        (
            "#12P#10100Fでは、あたしたちは先に行くので\x01",
            "後ろの警戒はお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x104,
        "#5P#00300Fおうよ、了解だ。\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x105,
        "#5P#10300Fフフ、行ってらっしゃい。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    Jump("loc_D18F")

    label("loc_D0D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D18F")
    OP_29(0x73, 0x1, 0x3)
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(300)

    #C0544
    ChrTalk(
        0x105,
        (
            "#12P#10300Fそれじゃ、僕たちは先に行くから\x01",
            "後ろの警戒は任せたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x109,
        "#5P#10100F了解です。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x104,
        "#5P#00300Fま、せいぜい気を付けてな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)

    label("loc_D18F")

    OP_C9(0x0, 0x1000)
    OP_1B(0x2, 0x0, 0x68)
    SetScenarioFlags(0x153, 5)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 18910, 0, 13080, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_75_C06D end

    def Function_76_D1DD(): pass

    label("Function_76_D1DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31400.itc", 0x28)
    SetChrChipByIndex(0x28, 0x28)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 19190, -10, 14710, 180)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    OP_68(19890, 4500, 11900, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27560, 0)
    SetChrPos(0x1A2, 18620, -10, 3410, 0)
    SetChrPos(0x102, 19450, -10, 3400, 0)
    SetChrPos(0x101, 18970, -10, 1840, 0)
    SetChrPos(0x104, 17790, -10, 610, 0)
    SetChrPos(0x109, 20110, -10, 910, 0)
    SetChrPos(0x105, 19260, -10, -170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x4)
    OP_68(19890, 2500, 11900, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_D30E():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D30E)

    def lambda_D328():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D328)
    Sleep(50)

    def lambda_D345():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D345)
    Sleep(50)

    def lambda_D362():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D362)
    Sleep(50)

    def lambda_D37F():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D37F)
    Sleep(50)

    def lambda_D39C():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D39C)
    WaitChrThread(0x105, 1)
    OP_93(0x28, 0x5A, 0x0)
    OP_9B(0x1, 0x28, 0xB4, 0x3E8, 0x7D0, 0x0)
    BeginChrThread(0x1A2, 3, 0, 77)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 77)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 77)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 77)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 77)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 77)
    Sleep(3000)
    BeginChrThread(0x28, 3, 0, 77)
    WaitChrThread(0x28, 3)
    Sleep(700)
    Sound(104, 0, 80, 0)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    OP_68(19890, 4500, 11900, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c1210", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_76_D1DD end

    def Function_77_D47D(): pass

    label("Function_77_D47D")

    OP_95(0xFE, 19190, -10, 14710, 2000, 0x0)

    def lambda_D496():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D496)
    Sleep(3000)

    def lambda_D4B3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D4B3)
    Return()

    # Function_77_D47D end

    def Function_78_D4C0(): pass

    label("Function_78_D4C0")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, -150, -310, 6250, 135)
    SetChrPos(0x102, -1300, -470, 5330, 135)
    SetChrPos(0x109, -1630, -240, 6620, 135)
    SetChrPos(0x105, -510, -80, 7550, 135)
    SetChrPos(0x104, -2890, -500, 5170, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-330, 1870, 1930, 0)
    MoveCamera(46, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14900, 0)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x34, 0x8000)
    OP_0D()
    SoundLoad(821)
    Call(0, 80)
    Return()

    # Function_78_D4C0 end

    def Function_79_D570(): pass

    label("Function_79_D570")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, -260, -190, -6920, 45)
    SetChrPos(0x102, -1180, -350, -6000, 45)
    SetChrPos(0x109, -1910, -70, -7580, 45)
    SetChrPos(0x105, -720, -10, -8490, 45)
    SetChrPos(0x104, -2890, -260, -6510, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(510, 1150, -6710, 0)
    MoveCamera(25, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14220, 0)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x34, 0x8000)
    OP_0D()
    SoundLoad(821)
    Call(0, 80)
    Return()

    # Function_79_D570 end

    def Function_80_D620(): pass

    label("Function_80_D620")

    Sound(821, 2, 40, 0)

    #C0547
    ChrTalk(
        0x101,
        "#12P#00000F随分にぎやかみたいだな……\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x102,
        (
            "#6P#00100F今日はみっしぃのイベントが\x01",
            "催されているみたいね。\x02\x03",

            "#00104F通商会議の期間中は\x01",
            "ミシュラムが休みだから、\x01",
            "その代わりに開催されているらしいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x109,
        (
            "#6P#10102Fふふ、ティオちゃんがいたら\x01",
            "見たがりそうですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#12P#00002Fはは、ちょうどダンスショーを\x01",
            "やっているみたいだし、\x01",
            "せっかくだから見ていっても……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0551
    ChrTalk(
        0x101,
        "#12P#00005Fって、あれは……！？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(5070, 1800, -2680, 4000)
    MoveCamera(42, 27, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(12260, 4000)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7160", 0)
    SetScenarioFlags(0x2, 3)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0x34, 0x20)
    BeginChrThread(0xF, 1, 0, 86)
    BeginChrThread(0x34, 1, 0, 87)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    #C0552
    ChrTalk(
        0x17,
        "#6P#11Aきゃ～、みっしぃ～！\x02",
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    Sleep(1700)
    ClearScenarioFlags(0x2, 3)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x34, 1)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x34, 0x20)
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x2, 3)
    BeginChrThread(0xF, 0, 0, 81)
    BeginChrThread(0x34, 0, 0, 81)
    BeginChrThread(0x34, 2, 0, 84)
    BeginChrThread(0xF, 2, 0, 85)
    WaitChrThread(0x34, 2)
    WaitChrThread(0xF, 2)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0x34, 0x20)
    ClearScenarioFlags(0x2, 4)
    OP_93(0xF, 0xB4, 0x0)
    OP_93(0x34, 0xB4, 0x0)
    Sleep(200)
    BeginChrThread(0xF, 1, 0, 87)
    BeginChrThread(0x34, 1, 0, 86)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    #C0553
    ChrTalk(
        0x16,
        (
            "#6P#11Aはは、飛び入りの兄さんも\x01",
            "なかなかやるじゃん！\x02",
        )
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    Sleep(1700)
    ClearScenarioFlags(0x2, 3)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x34, 1)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x34, 0x20)
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x2, 3)
    BeginChrThread(0xF, 0, 0, 81)
    BeginChrThread(0x34, 0, 0, 81)
    BeginChrThread(0x34, 2, 0, 85)
    BeginChrThread(0xF, 2, 0, 84)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    Sleep(3200)
    ClearScenarioFlags(0x2, 3)
    SetScenarioFlags(0x2, 3)

    #C0554
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "さー、みんないくヨ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4Sエンジョーイ、みっしぃ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x34, 0x2)
    SetChrFlags(0x34, 0x10)
    SetChrFlags(0x34, 0x20)
    SetChrChipByIndex(0x34, 0x22)
    SetChrSubChip(0x34, 0x0)
    OP_0D()
    ClearScenarioFlags(0x2, 4)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xF, 0, 0, 83)
    BeginChrThread(0xF, 2, 0, 88)
    BeginChrThread(0x34, 2, 0, 89)
    WaitChrThread(0xF, 2)
    WaitChrThread(0x34, 2)
    ClearScenarioFlags(0x2, 3)
    ClearScenarioFlags(0x2, 4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(30, 140, -1, -1)
    SetChrName("観客たち")

    #A0556
    AnonymousTalk(
        0xFF,
        "#4Sエンジョーーーイ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("観客たち")

    #A0557
    AnonymousTalk(
        0xFF,
        "#4Sみっしーーーーぃ☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    Sleep(1200)
    OP_64(0x34)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    Fade(1000)
    OP_68(8000, 1800, -1810, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12910, 0)
    ClearChrFlags(0x34, 0x2)
    ClearChrFlags(0x34, 0x10)
    ClearChrFlags(0x34, 0x20)
    SetChrChipByIndex(0x34, 0x21)
    SetChrSubChip(0x34, 0x0)
    OP_93(0x34, 0x10E, 0x0)
    SetChrPos(0x101, 2520, -700, -410, 90)
    SetChrPos(0x102, 2520, -700, -1650, 90)
    SetChrPos(0x109, 1430, -700, -2270, 90)
    SetChrPos(0x105, 1410, -700, -1020, 90)
    SetChrPos(0x104, 1440, -700, 200, 90)
    OP_0D()
    Sleep(500)

    def lambda_DD0F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_DD0F)
    Sleep(10)

    def lambda_DD1F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_DD1F)
    WaitChrThread(0x34, 1)

    def lambda_DD30():
        OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_DD30)
    Sleep(10)

    def lambda_DD48():
        OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_DD48)
    WaitChrThread(0x34, 1)

    #A0558
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オリビエとみっしぃは\x01",
            "ガッシリと固い握手を交わした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0559
    ChrTalk(
        0x34,
        (
            "#12P#13909Fハッハッハ……\x01",
            "さすがだね、みっしぃ君。\x02\x03",

            "#13902Fキミのダンシング・センス……\x01",
            "はっきり言って脱帽したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、おにーさんも\x01",
            "とっても上手だったヨ～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "どこかでダンスを習ってたの～？\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x34,
        (
            "#12P#13904Fフッ、社交ダンスくらいは\x01",
            "嗜んでいるものでね。\x02\x03",

            "本来ならレディと優雅に\x01",
            "ステップを踏みたいところだが、\x01",
            "キミと踊るのもなかなか楽しかった。\x02\x03",

            "#13902F流石はクロスベル一の\x01",
            "マスコットと言ったところかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、照れちゃうナ～☆\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(1760, 1600, -3500, 0)
    MoveCamera(44, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12200, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0564
    ChrTalk(
        0x101,
        "#6P#00006F（な、何をやってるんだあの人……）\x02",
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x104,
        (
            "#6P#00300F（どうやらステージに\x01",
            "  乱入しちまったみてえだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x109,
        (
            "#6P#10106F（なるべく目立たないようにって\x01",
            "  ミュラーさんに頼まれましたけど、\x01",
            "  これはさすがに無理そうですね……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E12A():
        OP_9B(0x1, 0xFE, 0xB4, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E12A)
    Sleep(10)

    def lambda_E142():
        OP_9B(0x1, 0xFE, 0xB4, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_E142)
    WaitChrThread(0x34, 1)
    OP_93(0x34, 0x10E, 0x1F4)
    Fade(500)
    OP_68(8000, 1800, -1810, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12910, 0)
    OP_0D()

    #C0567
    ChrTalk(
        0x34,
        (
            "#12P#13905Fおや……\x01",
            "どうやら迎えが来てしまったようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x34, 0x0, 0x1F4)
    OP_6F(0x79)

    #C0568
    ChrTalk(
        0x34,
        (
            "#12P#13900Fみっしぃ君、すまないが\x01",
            "ボクはここで退散させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "ありゃりゃ、それはザンネン～。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、今度はゼッタイ\x01",
            "ワンダーランドにも来てよネ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x34,
        (
            "#12P#13902Fフッ、その頼み……\x01",
            "いつか必ず果たさせてもらおう。\x02\x03",

            "#13904Fこの別れはあまりにも辛い。\x01",
            "だからこそボクらの絆は\x01",
            "かけがえの無いものとなるだろう。\x02\x03",

            "#13913F……また会おう#10Rア　デ　ィ　オ　ス#、#2R・#親友#4Rアミーゴ#！\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "ばいばい～☆\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrFlags(0x34, 0x2)
    SetChrFlags(0x34, 0x10)
    SetChrFlags(0x34, 0x20)
    SetChrChipByIndex(0x34, 0x22)
    SetChrSubChip(0x34, 0x0)
    OP_0D()
    BeginChrThread(0x34, 2, 0, 89)
    WaitChrThread(0x34, 2)
    OP_64(0x34)
    Fade(500)
    ClearChrFlags(0x34, 0x2)
    ClearChrFlags(0x34, 0x10)
    ClearChrFlags(0x34, 0x20)
    SetChrFlags(0x34, 0x40)
    SetChrChipByIndex(0x34, 0x21)
    SetChrSubChip(0x34, 0x0)
    OP_93(0x34, 0x0, 0x0)
    OP_0D()

    def lambda_E3D5():

        label("loc_E3D5")

        TurnDirection(0xFE, 0x34, 500)
        Yield()
        Jump("loc_E3D5")

    QueueWorkItem2(0xF, 2, lambda_E3D5)
    OP_68(8890, 1800, 4180, 2000)
    OP_95(0x34, 10730, -700, 580, 4000, 0x0)
    OP_95(0x34, 10620, -700, 3010, 5000, 0x0)
    Sound(809, 0, 70, 0)
    OP_9D(0x34, 0x28DC, 0x0, 0x2440, 0xBB8, 0xBB8)
    Sound(30, 0, 100, 0)
    EndChrThread(0xF, 0x2)
    OP_95(0x34, 4950, 0, 15760, 4000, 0x0)
    SetChrFlags(0x34, 0x80)
    OP_6F(0x1)
    StopBGM(0xFA0)
    OP_93(0x101, 0x0, 0x0)
    OP_93(0x102, 0x0, 0x0)
    OP_93(0x104, 0x0, 0x0)
    OP_93(0x109, 0x0, 0x0)
    OP_93(0x105, 0x0, 0x0)
    Fade(1000)
    OP_68(2820, 1800, -3080, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12910, 0)
    OP_0D()

    #C0573
    ChrTalk(
        0x101,
        (
            "#12P#00011Fああっ……\x01",
            "ま、また逃げられた！\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x105,
        (
            "#6P#10306Fやれやれ、\x01",
            "なんだか場慣れしてるねえ。\x02\x03",

            "#10300Fここまで来たら、\x01",
            "彼が逃げ込みそうな場所も\x01",
            "ある程度絞れてくると思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x102,
        "#12P#00106Fと、とにかく追いかけましょう！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 1570, -700, -240, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    SetScenarioFlags(0x156, 3)
    OP_29(0x76, 0x1, 0x3)
    SetChrPos(0xF, 9480, -700, 160, 270)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xF, 0xFF)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    StopSound(821, 1000, 30)
    EventEnd(0x5)
    Return()

    # Function_80_D620 end

    def Function_81_E63A(): pass

    label("Function_81_E63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_E656")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_81_E63A")

    label("loc_E656")

    Return()

    # Function_81_E63A end

    def Function_82_E657(): pass

    label("Function_82_E657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_E673")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(50)
    Jump("Function_82_E657")

    label("loc_E673")

    Return()

    # Function_82_E657 end

    def Function_83_E674(): pass

    label("Function_83_E674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_E690")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_83_E674")

    label("loc_E690")

    Return()

    # Function_83_E674 end

    def Function_84_E691(): pass

    label("Function_84_E691")

    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFF5D8, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFFC18, 0x7D0, 0x0)
    OP_96(0xFE, 0x1FF4, 0xFFFFFD44, 0xFFFFFF06, 0x7D0, 0x0)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x258, 0x7D0, 0x0)
    Return()

    # Function_84_E691 end

    def Function_85_E704(): pass

    label("Function_85_E704")

    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x834, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x258, 0x7D0, 0x0)
    OP_96(0xFE, 0x28F0, 0xFFFFFD44, 0xFFFFFF06, 0x7D0, 0x0)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFFC18, 0x7D0, 0x0)
    Return()

    # Function_85_E704 end

    def Function_86_E777(): pass

    label("Function_86_E777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_E88A")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    OP_93(0xFE, 0x10E, 0x0)
    Sleep(100)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    Jump("Function_86_E777")

    label("loc_E88A")

    Return()

    # Function_86_E777 end

    def Function_87_E88B(): pass

    label("Function_87_E88B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_E99E")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(100)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    Jump("Function_87_E88B")

    label("loc_E99E")

    Return()

    # Function_87_E88B end

    def Function_88_E99F(): pass

    label("Function_88_E99F")

    Sound(809, 0, 80, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0xBB8)
    OP_93(0xFE, 0x10E, 0x0)
    Return()

    # Function_88_E99F end

    def Function_89_E9C4(): pass

    label("Function_89_E9C4")

    OP_63(0xFE, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(130)
    Sound(822, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(130)
    SetChrSubChip(0xFE, 0x4)
    Sleep(130)
    SetChrSubChip(0xFE, 0x5)
    Sleep(130)
    SetChrSubChip(0xFE, 0x6)
    Sleep(130)
    SetChrSubChip(0xFE, 0x7)
    Return()

    # Function_89_E9C4 end

    def Function_90_EA12(): pass

    label("Function_90_EA12")

    EventBegin(0x0)
    Fade(500)
    OP_68(-12070, 2500, 10460, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(15780, 0)
    SetChrPos(0x101, -9870, 0, 11840, 0)
    SetChrPos(0x102, -11070, 0, 11840, 0)
    SetChrPos(0x103, -9870, 0, 10640, 0)
    SetChrPos(0x104, -11070, 0, 10640, 0)
    SetChrPos(0x109, -11070, 0, 9440, 0)
    SetChrPos(0x105, -9870, 0, 9440, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EAF1")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    Jump("loc_EB05")

    label("loc_EAF1")

    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_EB05")

    OP_0D()

    #C0576
    ChrTalk(
        0x9,
        (
            "よく来たな。\x01",
            "さあ、私の麺を食べていくがいい！\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x101,
        (
            "#00012Fえ、えっと、俺たちは\x01",
            "特務支援課の者なんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0578
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

    #C0579
    ChrTalk(
        0x9,
        (
            "ああ、その件か。\x01",
            "話には聞いているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x9,
        (
            "君たちは運がいい。\x01",
            "この私の至高の麺を\x01",
            "無料で堪能できるのだからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x9,
        (
            "さあ、食したまえ。\x01",
            "これが『天上麺≪日輪≫』だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x105,
        "#10305Fふむ、これはまた……\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x109,
        (
            "#10106F真っ赤なスープが\x01",
            "とっても辛そうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x9,
        "フフ、四の五の言わずに食すといい。\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x9,
        (
            "辛さの先にある味の桃源郷に、\x01",
            "君たちを誘#2Rいざな#ってくれるだろうからな！\x02",
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

    #C0586
    ChrTalk(
        0x101,
        (
            "#00003F（このノリは気になるけど……）\x01",
            "と、とにかく食べてみようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-9560, 2500, 11630, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(15700, 0)
    SetChrPos(0x9, -9810, 0, 13520, 135)
    SetChrPos(0x104, -8390, 0, 12300, 0)
    SetChrPos(0x101, -8250, 0, 11290, 0)
    SetChrPos(0x102, -7150, 0, 12270, 315)
    SetChrPos(0x103, -6100, 0, 12250, 315)
    SetChrPos(0x105, -9920, 0, 11790, 45)
    SetChrPos(0x109, -6860, 0, 11350, 315)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0587
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは天上麺≪日輪≫を食べた。\x07\x00\x02",
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
    Sleep(1000)

    #C0588
    ChrTalk(
        0x101,
        (
            "#00005Fズルズル……\x01",
            "確かに、辛いだけじゃなくて\x01",
            "深みのある味ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x102,
        (
            "#00108Fううん、確かに美味しいけど……\x02\x03",

            "#00106F私たちとしては、\x01",
            "スープが跳ねたりするのは\x01",
            "気になっちゃうわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x109,
        (
            "#10112Fた、確かに……\x01",
            "シミになると大変ですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x9,
        (
            "むむ……女性客は\x01",
            "いつもそんな感想だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x9,
        (
            "スープのハネなど\x01",
            "極上の麺を食せるのならば\x01",
            "さしたる問題ではなかろうに！\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x104,
        "#00303F……ああ、その通りだぜ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0594
    ChrTalk(
        0x103,
        "#00205F……ランディさん？\x02",
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x104,
        (
            "#00303Fこの絶妙な辛さのスープの\x01",
            "奥に広がる濃厚な味わいの世界……\x02\x03",

            "そして、そのスープが絡み付く\x01",
            "コシのあるちぢれ麺……\x01",
            "こいつは男にしか分からねえ良さだ。\x02\x03",

            "#00302Fオッサンの麺への強い想い、\x01",
            "なんだか俺にも分かった気がするぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F38B")

    #C0596
    ChrTalk(
        0x9,
        (
            "おおっ……そうかそうか！\x01",
            "見込みのある若者もいたようだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x9,
        (
            "よし、君には特別にこの麺の\x01",
            "基礎となるレシピを教えよう！\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x9,
        "是非とも精進してくれたまえ！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0599
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ピリ苦坦々麺のレシピ\x07\x00",
            "を教えてもらった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_F460")

    label("loc_F38B")


    #C0600
    ChrTalk(
        0x9,
        (
            "おおっ……そうかそうか！\x01",
            "見込みのある若者もいたようだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x9,
        (
            "よし、君には特別に\x01",
            "もう一杯おごろう！\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x9,
        "是非とも堪能してくれたまえ！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0603
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x190),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x190, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_F460")

    TurnDirection(0x104, 0x9, 500)

    #C0604
    ChrTalk(
        0x104,
        "#00309Fおおっ、あんがとよオッサン！\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0605
    ChrTalk(
        0x101,
        (
            "#00009F（ランディ……\x01",
            "  随分気に入ったみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x105,
        (
            "#10304F（フフ、ここの紹介は\x01",
            "  彼に任せてよさそうだね。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2, 7)
    SetScenarioFlags(0x172, 2)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_F5EC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_F609")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_F61C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F61C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_F62F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_F64C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F64C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_F65F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_F67C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_F68F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_F6AC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F6AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_F6BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F6BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_F6DC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F6DC")

    OP_29(0x80, 0x1, 0x3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F7DF")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0607
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F7D6")

    #A0608
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

    label("loc_F7D6")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_F7DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8B7")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0609
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

    #A0610
    AnonymousTalk(
        0x101,
        (
            "#00004Fこれで６人全員の\x01",
            "お気に入りが見つかった。\x02\x03",

            "#00000F取材はこれで十分だな。\x01",
            "さっそく通信社に報告へ行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_F8B7")

    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F933")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -52470, 2000, 21150, 90)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -18000, 0, -5750, 90)
    BeginChrThread(0xD, 0, 0, 4)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, 13000, 0, -10000, 0)
    BeginChrThread(0xE, 0, 0, 5)
    Jump("loc_F975")

    label("loc_F933")

    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -13200, 0, 11500, 90)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -52470, 2000, 21150, 90)
    BeginChrThread(0xA, 0, 0, 2)

    label("loc_F975")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10470, 0, 11840, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_90_EA12 end

    def Function_91_F9A1(): pass

    label("Function_91_F9A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    LoadChrToIndex("chr/ch47500.itc", 0x28)
    LoadChrToIndex("chr/ch27800.itc", 0x29)
    SoundLoad(462)
    SoundLoad(461)
    SoundLoad(470)
    SoundLoad(457)
    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0xA, 0x4)
    OP_78(0xA, 0x32)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x32, -3570, 2000, 21710, 270)
    OP_D5(0x32, 0x0, 0x41EB0, 0x0, 0x0)
    OP_68(17650, 0, -4330, 0)
    MoveCamera(42, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26020, 0)
    SetChrChipByIndex(0x30, 0x28)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrChipByIndex(0x31, 0x29)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x30, 16050, 0, -6150, 270)
    SetChrPos(0x31, 19620, -10, 4000, 180)
    SetChrPos(0x101, 340, -470, 5300, 315)
    SetChrPos(0x104, 1700, -620, 4480, 315)
    SetChrPos(0x105, 150, -700, 3820, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_FADB():
        OP_9B(0x0, 0x31, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_FADB)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_93(0x30, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0x30, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0x30, 0xB4, 0x1F4)
    Sleep(800)
    OP_93(0x30, 0x10E, 0x1F4)
    WaitChrThread(0x31, 1)
    TurnDirection(0x31, 0x30, 500)

    #C0611
    ChrTalk(
        0x31,
        "クライド君、お待たせしたね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x30, 0x31, 500)
    Sleep(500)
    OP_68(20210, 0, -4730, 2000)
    OP_9B(0x0, 0x30, 0x0, 0x7D0, 0x5DC, 0x0)
    WaitChrThread(0x30, 1)
    OP_6F(0x1)
    Sleep(500)

    #C0612
    ChrTalk(
        0x31,
        "例のものを持ってきたよ。\x02",
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x30, 0x0, 0x1F4, 0x5DC, 0x0)
    WaitChrThread(0x30, 1)
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0613
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クライドはアタッシュケース\x07\x00",
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_9B(0x1, 0x30, 0xB4, 0x1F4, 0x5DC, 0x0)
    WaitChrThread(0x30, 1)

    #C0614
    ChrTalk(
        0x30,
        "どうも、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x31,
        "それで……首尾はどうだね？\x02",
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x30,
        (
            "ええ、彼女のほうも\x01",
            "かなり乗り気みたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x30,
        (
            "この後、《ノイエ＝ブラン》で\x01",
            "バッチリ決めてやりますよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x31,
        "はは、それは結構だ。\x02",
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x31,
        (
            "……おっと、そろそろ\x01",
            "水上バスが出る時間だな。\x01",
            "準備を済ませてくるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x31,
        (
            "それでは、よろしく頼んだよ。\x01",
            "今回の契約さえとりつければ、\x01",
            "君のトップは安泰だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x30,
        "はいっ、任せてくださいっ！！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x31, 1, 0, 92)
    OP_68(22840, 0, -4880, 3000)
    Sleep(1500)

    def lambda_FDE3():
        OP_9B(0x0, 0x30, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_FDE3)
    WaitChrThread(0x30, 1)

    def lambda_FDFC():

        label("loc_FDFC")

        TurnDirection(0xFE, 0x31, 500)
        Yield()
        Jump("loc_FDFC")

    QueueWorkItem2(0x30, 1, lambda_FDFC)
    Sleep(4000)
    EndChrThread(0x30, 0x1)

    #C0622
    ChrTalk(
        0x30,
        "よし……やってやるぞ！\x02",
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x8, 0x9, 0xFA, 0x6)
    Sound(27, 0, 100, 0)

    def lambda_FE49():
        OP_9B(0x0, 0x30, 0x10E, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_FE49)
    Sleep(2000)
    Fade(500)
    OP_68(-2520, 0, 26110, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31670, 0)
    SetChrPos(0x30, 1100, 2000, 23760, 270)
    OP_63(0x30, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)

    def lambda_FEBD():
        OP_9B(0x0, 0x30, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_FEBD)
    WaitChrThread(0x30, 1)

    def lambda_FED6():
        OP_93(0x30, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_FED6)
    WaitChrThread(0x30, 1)
    OP_71(0xA, 0xF1, 0x10E, 0x1, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0xA)
    OP_64(0x30)

    def lambda_FEFF():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_FEFF)

    def lambda_FF14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_FF14)
    WaitChrThread(0x30, 1)
    WaitChrThread(0x30, 2)
    OP_71(0xA, 0x10F, 0x12C, 0x1, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0xA)
    ClearChrFlags(0x32, 0x80)
    OP_78(0xA, 0x32)
    OP_49()
    SetChrPos(0x32, -3570, 2000, 21710, 270)
    OP_D5(0x32, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    OP_0D()
    Sound(470, 0, 100, 0)
    SetCameraDistance(30470, 3000)
    OP_0D()
    Sleep(800)
    Sleep(800)
    OP_68(-15880, 0, 26510, 3000)
    Sound(457, 0, 100, 0)

    def lambda_FFC7():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_FFC7)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    WaitChrThread(0x32, 1)
    OP_6F(0x11)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x32, 0x80)
    ClearChrFlags(0x32, 0x8000)
    ClearMapObjFlags(0xA, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    OP_0D()
    Sleep(500)
    OP_68(2060, 0, 7960, 5000)
    MoveCamera(39, 19, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(27560, 5000)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)

    #C0623
    ChrTalk(
        0x104,
        (
            "#00305Fなんだかゴキゲンで\x01",
            "どっかに行っちまったな。\x02\x03",

            "#00303Fあの副局長の奥さんと\x01",
            "《ノイエ＝ブラン》で\x01",
            "待ち合わせしてるみてえだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、どうするんだい？\x01",
            "流石にこれ以上は\x01",
            "尾行のしようもないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x101,
        (
            "#00003F……エリィたちに連絡して、\x01",
            "一旦警察本部に戻ろう。\x02\x03",

            "#00001Fあのクライドという男の正体……\x01",
            "なんとなく掴めてきた気がする。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c1160", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_91_F9A1 end

    def Function_92_101C5(): pass

    label("Function_92_101C5")

    ClearChrFlags(0x31, 0x4)
    OP_9B(0x0, 0x31, 0x10E, 0xFA0, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x10E, 0x1770, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x10E, 0x1B58, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x5A, 0x1B58, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0x31, 0x4)
    Return()

    # Function_92_101C5 end

    def Function_93_1021B(): pass

    label("Function_93_1021B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(35980, -1400, 370, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17240, 0)
    SetChrPos(0x101, 35590, -2500, 10, 90)
    SetChrPos(0x102, 35400, -2500, 980, 90)
    SetChrPos(0x103, 34850, -2500, -1070, 90)
    SetChrPos(0x104, 34050, -2500, -40, 90)
    SetChrPos(0x109, 33500, -2500, 960, 90)
    SetChrPos(0x105, 33050, -2500, -730, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x24, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1055D")
    SetScenarioFlags(0x176, 2)

    #C0626
    ChrTalk(
        0x24,
        (
            "ミシュラム行き水上バス、\x01",
            "間もなく発進いたしま～す。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x24,
        (
            "ご利用のお客様は\x01",
            "早めにご搭乗くださいませ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそういえば……\x01",
            "テーマパークのほうから\x01",
            "要請がきてたっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x102,
        (
            "#6P#00100Fみっしぃを助けてほしい、\x01",
            "みたいな内容だったわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x109,
        "#6P#10103Fうーん、どんな仕事なんでしょうね？\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x103,
        (
            "#12P#00203F…………………………\x01",
            "とにかく、可及的速やかに\x01",
            "現場に向かうとしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x104,
        (
            "#6P#00309Fハハ、ティオすけ、\x01",
            "すげえやる気だなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、なんだか楽しそうな\x01",
            "予感がしてきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x101,
        (
            "#6P#00003F（一度ミシュラムに渡ったら、\x01",
            "  余程の事情がない限り\x01",
            "  引き受けた方がよさそうだ。）\x02\x03",

            "（このまま向かうか……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1055D")

    Call(0, 94)
    Return()

    # Function_93_1021B end

    def Function_94_10561(): pass

    label("Function_94_10561")

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
            "テーマパークに行く\x01",      # 0
            "やめる\x01",                  # 1
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
        (0, "loc_105CB"),
        (1, "loc_10838"),
        (SWITCH_DEFAULT, "loc_1091F"),
    )


    label("loc_105CB")


    #C0635
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそれじゃあ、\x01",
            "早速向かうとしようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x80)
    SoundLoad(479)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x5, 0x2E)
    OP_49()
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    SetChrPos(0x2E, 51800, -3850, -4000, 0)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_70(0x5, 0x1F)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrPos(0x2E, 126220, -3850, -50690, 315)
    OP_D5(0x2E, 0x0, 0x4CE78, 0x0, 0x0)
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x2E, 51800, -3850, -4000, 0)
    OP_71(0x5, 0x1F, 0x5A, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    Sound(478, 0, 100, 0)
    OP_79(0x9)
    Sound(477, 0, 100, 0)
    Sleep(200)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1075C():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_1075C)
    WaitChrThread(0x2E, 1)

    def lambda_1077A():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_1077A)
    Sleep(2000)
    StopSound(126, 1000, 50)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x2E, 1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x1DF)
    SetChrName("")

    #A0636
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうしてロイドたちは\x01",
            "水上バスでミシュラムに向かい……\x02\x03",

            "依頼者の待つテーマパーク前へと\x01",
            "足を運ぶのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_1091F")

    label("loc_10838")


    #C0637
    ChrTalk(
        0x101,
        "#6P#00003F……ひとまず出直すとするか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0638
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クエストのために\x01",
            "ミシュラムに向かう場合は、\x01",
            "時刻表を調べてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 33190, -2500, 0, 270)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x24, 0xFF)
    ModifyEventFlags(0, 6, 0x80)
    EventEnd(0x5)
    Jump("loc_1091F")

    label("loc_1091F")

    Return()

    # Function_94_10561 end

    def Function_95_10920(): pass

    label("Function_95_10920")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, 38840, -2500, -460, 270)
    OP_69(0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_95_10920 end

    def Function_96_1094E(): pass

    label("Function_96_1094E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(479)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x5, 0x2E)
    OP_49()
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    SetChrPos(0x2E, 51800, -3850, -4000, 0)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetChrPos(0x2E, 126220, -3850, -50690, 315)
    OP_D5(0x2E, 0x0, 0x4CE78, 0x0, 0x0)
    BeginChrThread(0x2F, 1, 0, 97)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x0, 0x1)
    OP_68(59280, 17600, -8870, 0)
    MoveCamera(90, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(51010, 0)
    OP_68(59280, 8000, -8870, 10000)

    def lambda_10A83():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_10A83)
    Sound(475, 0, 100, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x1, 0x1)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x2E, 54800, -3850, -4000, 0)
    Sound(476, 0, 100, 0)
    Sound(477, 0, 100, 0)

    def lambda_10B34():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_10B34)
    WaitChrThread(0x2E, 1)
    OP_82(0x32, 0x0, 0xBB8, 0x1F4)
    Sound(478, 0, 100, 0)
    Sleep(2000)
    Fade(500)
    SetMapObjFlags(0x7, 0x4)
    OP_68(40510, 400, -3870, 0)
    MoveCamera(56, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11290, 0)
    OP_0D()
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x12D, 0x168, 0x0, 0x20)
    OP_71(0x5, 0x1, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0xF1, 0x12C, 0x0, 0x20)
    Sleep(500)
    SetChrPos(0x101, 49180, -2500, -1680, 270)
    SetChrPos(0x102, 49180, -2500, -1680, 270)
    SetChrPos(0x104, 49180, -2500, -1680, 270)
    SetChrPos(0x109, 49180, -2500, -1680, 270)
    SetChrPos(0x105, 49180, -2500, -1680, 270)
    SetChrPos(0x103, 49180, -2500, -1680, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 98)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 99)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 100)
    Sleep(700)
    OP_68(36510, 400, -1860, 5000)
    BeginChrThread(0x109, 3, 0, 101)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 102)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 103)
    WaitChrThread(0x103, 3)
    OP_6F(0x1)

    #C0639
    ChrTalk(
        0x103,
        "#00200F………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_10D11():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10D11)
    Sleep(50)

    def lambda_10D21():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10D21)
    Sleep(50)

    def lambda_10D31():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10D31)
    Sleep(50)

    def lambda_10D41():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10D41)
    Sleep(50)

    def lambda_10D51():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10D51)
    Sleep(300)

    #C0640
    ChrTalk(
        0x104,
        (
            "#00305F……おいロイド。\x01",
            "ティオすけのやつ、\x01",
            "何かあったのか？\x02\x03",

            "合流してから\x01",
            "水上バスの中まで\x01",
            "ずっとあの調子だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x102,
        (
            "#00108Fそうねえ……\x01",
            "どこか遠くを見て\x01",
            "ぼ～っとしてて……\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x105,
        (
            "#10300Fなんだか寂しそうな\x01",
            "雰囲気だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x101,
        (
            "#00000Fう、うーん……\x01",
            "何と言えばいいのやら。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x109,
        (
            "#10105Fあの、ティオちゃん。\x01",
            "どこか具合が悪いの？\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x103,
        (
            "#00203F………………いえ。\x01",
            "わたしなら大丈夫です。\x02\x03",

            "#00202Fちょっと混乱してましたが……\x01",
            "そろそろ整理がつきました。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(1000)

    #C0646
    ChrTalk(
        0x103,
        (
            "#00208F……人はこうして、\x01",
            "大人になっていくんですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0647
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【テーマパークのアルバイト】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x86, 0x1, 0x9)
    OP_29(0x86, 0x1, 0xA)
    OP_29(0x86, 0x4, 0x10)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x3, 0x1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapObjFlags(0x7, 0x4)
    SetChrPos(0x2E, 51800, -3850, -2300, 0)
    SetChrFlags(0x2E, 0x80)
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x16, 40740, -2500, -2330, 180)
    SetChrPos(0x17, 40630, -2500, -3760, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x0, 36990, -2500, 190, 270)
    OP_69(0xFF, 0x0)
    OP_24(0x1DF)
    EventEnd(0x5)
    Return()

    # Function_96_1094E end

    def Function_97_110E7(): pass

    label("Function_97_110E7")

    Sound(479, 2, 0, 0)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    Sleep(8000)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_24(0x1DF)
    Return()

    # Function_97_110E7 end

    def Function_98_11179(): pass

    label("Function_98_11179")


    def lambda_1117E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1117E)

    def lambda_1118F():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1118F)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 37640, -2500, 320, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_98_11179 end

    def Function_99_111C4(): pass

    label("Function_99_111C4")


    def lambda_111C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_111C9)

    def lambda_111DA():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_111DA)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 37640, -2500, -1280, 2000, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Return()

    # Function_99_111C4 end

    def Function_100_1120F(): pass

    label("Function_100_1120F")


    def lambda_11214():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11214)

    def lambda_11225():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11225)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 38890, -2500, 1500, 2000, 0x0)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_100_1120F end

    def Function_101_1125A(): pass

    label("Function_101_1125A")


    def lambda_1125F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1125F)

    def lambda_11270():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11270)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 39690, -2500, -1720, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_101_1125A end

    def Function_102_112A5(): pass

    label("Function_102_112A5")


    def lambda_112AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_112AA)

    def lambda_112BB():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_112BB)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 40640, -2500, 1110, 2000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_102_112A5 end

    def Function_103_112F0(): pass

    label("Function_103_112F0")


    def lambda_112F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_112F5)

    def lambda_11306():
        OP_95(0xFE, 41760, -2500, -1910, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11306)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 41340, -2500, -150, 1500, 0x0)
    OP_93(0x103, 0x10E, 0x1F4)
    Return()

    # Function_103_112F0 end

    def Function_104_1133B(): pass

    label("Function_104_1133B")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11413")

    #C0648
    ChrTalk(
        0x1A2,
        "こっちは東通りか？\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        "#00000Fいや、違うけど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0650
    ChrTalk(
        0x1A2,
        "だよな？\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x1A2,
        (
            "……たしか、ボクは東通りを\x01",
            "経由しろって言ったと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x101,
        "#00006Fそうだな……悪かったよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_11470")

    label("loc_11413")


    #C0653
    ChrTalk(
        0x1A2,
        (
            "おい、寄り道はいいけど\x01",
            "遠回りはカンベンだかんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x1A2,
        "さっさと東通りに連れてってくれ。\x02",
    )

    CloseMessageWindow()

    label("loc_11470")

    SetChrPos(0x0, -28110, 2000, 23520, 90)
    EventEnd(0x4)
    Return()

    # Function_104_1133B end

    def Function_105_11484(): pass

    label("Function_105_11484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1152E")
    EventBegin(0x1)

    #C0655
    ChrTalk(
        0x101,
        (
            "#00003F（一度ミシュラムに渡ったら、\x01",
            "  余程の事情がない限り\x01",
            "  引き受けた方がよさそうだ。）\x02\x03",

            "（このまま向かうか……？）\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 94)
    Jump("loc_115CF")

    label("loc_1152E")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0656
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《ミシュラム》行き水上バス・時刻表\x01\x01",
            "※ミシュラムが誇るテーマパーク\x01",
            "  『ワンダーランド』開園中！\x01",
            "  楽しいひと時をお楽しみ下さい！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)

    label("loc_115CF")

    Return()

    # Function_105_11484 end

    def Function_106_115D0(): pass

    label("Function_106_115D0")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0657
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　《ルピナス川・第一灯台》\x01\x01",
            "関係者以外の立ち入りを禁ずる。\x01",
            "　　　　　～クロスベル市～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_106_115D0 end

    SaveToFile()

Try(main)
