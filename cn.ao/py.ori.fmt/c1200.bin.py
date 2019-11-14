from ScenarioHelper import *

def main():
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
        "库妮娅",                 # 1
        "奥赛尔",                 # 2
        "毕肖普",                 # 3
        "奎因老人",               # 4
        "亚米萨",                 # 5
        "尼克鲁",                 # 6
        "塞利娜",                 # 7
        "咪西",                   # 8
        "奇幻乐园工作人员",       # 9
        "奇幻乐园工作人员",       # 10
        "市民",                   # 11
        "市民",                   # 12
        "市民",                   # 13
        "市民",                   # 14
        "游客",                   # 15
        "游客",                   # 16
        "维修员",                 # 17
        "洛依",                   # 18
        "梅琳",                   # 19
        "蔡特",                   # 20
        "琪雅",                   # 21
        "滴",                     # 22
        "游客",                   # 23
        "男孩",                   # 24
        "市民",                   # 25
        "乔里基科长",             # 26
        "警官",                   # 27
        "警官",                   # 28
        "水上巴士向导",           # 29
        "警车",                   # 30
        "尼尔森",                 # 31
        "曹",                     # 32
        "刘",                     # 33
        "尤利",                   # 34
        "塞克斯",                 # 35
        "瑞吉",                   # 36
        "飙车族",                 # 37
        "警车",                   # 38
        "水上巴士",               # 39
        "SE控制",                 # 40
        "克莱德",                 # 41
        "男人",                   # 42
        "车",                     # 43
        "小船",                   # 44
        "奥利维尔",               # 45
        "中央广场",               # 46
        "西街",                   # 47
        "行政区",                 # 48
        "住宅街",                 # 49
        "欢乐街",                 # 50
        "东街",                   # 51
        "旧城区",                 # 52
        "港湾区",                 # 53
        "ＩＢＣ",                 # 54
        "站前街道",               # 55
        "后巷",                   # 56
        "乌尔斯拉间道",           # 57
        "东克洛斯贝尔街道",       # 58
        "西克洛斯贝尔街道",       # 59
        "玛因兹山道",             # 60
        "兰花塔",                 # 61
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

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "中央广场")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "西街")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "住宅街")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "欢乐街")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "东街")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "旧城区")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "站前街道")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "后巷")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-96.5, 0.0, 203.75, 0x0000, 0x0000, "兰花塔")
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
        "Function_11_21CD",        # 0B, 11
        "Function_12_3073",        # 0C, 12
        "Function_13_42D9",        # 0D, 13
        "Function_14_49EF",        # 0E, 14
        "Function_15_507B",        # 0F, 15
        "Function_16_5185",        # 10, 16
        "Function_17_5286",        # 11, 17
        "Function_18_5621",        # 12, 18
        "Function_19_57D9",        # 13, 19
        "Function_20_5892",        # 14, 20
        "Function_21_5972",        # 15, 21
        "Function_22_5A59",        # 16, 22
        "Function_23_5B68",        # 17, 23
        "Function_24_5C05",        # 18, 24
        "Function_25_5C8F",        # 19, 25
        "Function_26_5D2C",        # 1A, 26
        "Function_27_5D54",        # 1B, 27
        "Function_28_5E8A",        # 1C, 28
        "Function_29_5F99",        # 1D, 29
        "Function_30_5FB7",        # 1E, 30
        "Function_31_5FED",        # 1F, 31
        "Function_32_6011",        # 20, 32
        "Function_33_607C",        # 21, 33
        "Function_34_6155",        # 22, 34
        "Function_35_624A",        # 23, 35
        "Function_36_62DD",        # 24, 36
        "Function_37_63BD",        # 25, 37
        "Function_38_644B",        # 26, 38
        "Function_39_65F6",        # 27, 39
        "Function_40_6739",        # 28, 40
        "Function_41_6908",        # 29, 41
        "Function_42_6BCB",        # 2A, 42
        "Function_43_6CCE",        # 2B, 43
        "Function_44_6DDC",        # 2C, 44
        "Function_45_72A2",        # 2D, 45
        "Function_46_74D7",        # 2E, 46
        "Function_47_759F",        # 2F, 47
        "Function_48_7D34",        # 30, 48
        "Function_49_7E2E",        # 31, 49
        "Function_50_7E4D",        # 32, 50
        "Function_51_826E",        # 33, 51
        "Function_52_82B9",        # 34, 52
        "Function_53_831A",        # 35, 53
        "Function_54_837B",        # 36, 54
        "Function_55_83AB",        # 37, 55
        "Function_56_83D9",        # 38, 56
        "Function_57_8C4D",        # 39, 57
        "Function_58_8D4D",        # 3A, 58
        "Function_59_8D6B",        # 3B, 59
        "Function_60_8D9F",        # 3C, 60
        "Function_61_8DD3",        # 3D, 61
        "Function_62_92A6",        # 3E, 62
        "Function_63_92E7",        # 3F, 63
        "Function_64_930D",        # 40, 64
        "Function_65_9335",        # 41, 65
        "Function_66_937E",        # 42, 66
        "Function_67_93D8",        # 43, 67
        "Function_68_9432",        # 44, 68
        "Function_69_948C",        # 45, 69
        "Function_70_9805",        # 46, 70
        "Function_71_99A6",        # 47, 71
        "Function_72_A0B3",        # 48, 72
        "Function_73_A9A7",        # 49, 73
        "Function_74_A9DE",        # 4A, 74
        "Function_75_AA29",        # 4B, 75
        "Function_76_B95F",        # 4C, 76
        "Function_77_BBFF",        # 4D, 77
        "Function_78_BC42",        # 4E, 78
        "Function_79_BCF2",        # 4F, 79
        "Function_80_BDA2",        # 50, 80
        "Function_81_CBF7",        # 51, 81
        "Function_82_CC14",        # 52, 82
        "Function_83_CC31",        # 53, 83
        "Function_84_CC4E",        # 54, 84
        "Function_85_CCC1",        # 55, 85
        "Function_86_CD34",        # 56, 86
        "Function_87_CE48",        # 57, 87
        "Function_88_CF5C",        # 58, 88
        "Function_89_CF81",        # 59, 89
        "Function_90_CFCF",        # 5A, 90
        "Function_91_DDF2",        # 5B, 91
        "Function_92_E552",        # 5C, 92
        "Function_93_E5A8",        # 5D, 93
        "Function_94_E85E",        # 5E, 94
        "Function_95_EBD9",        # 5F, 95
        "Function_96_EC07",        # 60, 96
        "Function_97_F330",        # 61, 97
        "Function_98_F3C2",        # 62, 98
        "Function_99_F40D",        # 63, 99
        "Function_100_F458",       # 64, 100
        "Function_101_F4A3",       # 65, 101
        "Function_102_F4EE",       # 66, 102
        "Function_103_F539",       # 67, 103
        "Function_104_F584",       # 68, 104
        "Function_105_F68D",       # 69, 105
        "Function_106_F7B5",       # 6A, 106
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2184")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1D7, 1)"), scpexpr(EXPR_END)), "loc_2115")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_217F")

    label("loc_2115")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_217F")

    Jump("loc_21C1")

    label("loc_2184")

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

    label("loc_21C1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_2092 end

    def Function_11_21CD(): pass

    label("Function_11_21CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A4")

    #C0004
    ChrTalk(
        0xFE,
        (
            "事情的发展太过突然，我自然有些吃惊……\x01",
            "但态度如果不强硬些，\x01",
            "肯定会被两大国小看。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "所以我坚决支持\x01",
            "迪塔总统！\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "再加上还有亚里欧斯长官在……\x01",
            "总不能永远都任由\x01",
            "两大国为所欲为！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2301")

    label("loc_22A4")


    #C0007
    ChrTalk(
        0xFE,
        (
            "虽然肯定有些不安……\x01",
            "但我坚决支持\x01",
            "迪塔总统！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "我可不希望永远都任由\x01",
            "两大国为所欲为！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2301")

    Jump("loc_306F")

    label("loc_2306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_247E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23EF")

    #C0009
    ChrTalk(
        0xFE,
        (
            "沿岸那个被彻底破坏的公司……\x01",
            "据说和共和国政府存在关联。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "既然如此，应该就是得知了此事的帝国\x01",
            "雇佣猎兵团发动了袭击吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "那种事情随便怎样都好……\x01",
            "总之，我可不希望克洛斯贝尔\x01",
            "再被卷进这种事情了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2479")

    label("loc_23EF")


    #C0012
    ChrTalk(
        0xFE,
        (
            "之所以会发生如此事态，\x01",
            "主要还是因为克洛斯贝尔\x01",
            "一直都是从属州吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "既然如此，我们显然\x01",
            "还是应该向周边诸国\x01",
            "明确表达独立的意志。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2479")

    Jump("loc_306F")

    label("loc_247E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_25D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_254D")

    #C0014
    ChrTalk(
        0xFE,
        (
            "与武装集团交战中的警备队\x01",
            "似乎陷入严峻苦战了……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "我听说，只要克洛斯贝尔独立，\x01",
            "就能使军备得到强化，\x01",
            "从而轻易应对这种事态……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔……果然还是\x01",
            "应该独立吧………？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25CC")

    label("loc_254D")


    #C0017
    ChrTalk(
        0xFE,
        (
            "我听说，只要克洛斯贝尔独立，\x01",
            "就能使军备得到强化，\x01",
            "从而轻易应对这种事态……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔……果然还是\x01",
            "应该独立吧………？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25CC")

    Jump("loc_306F")

    label("loc_25D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25DF")
    Jump("loc_306F")

    label("loc_25DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_271F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C5")

    #C0019
    ChrTalk(
        0xFE,
        (
            "目前来说，赞成独立的人\x01",
            "占了多数。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "……唔～但我不是很明白\x01",
            "赞成和反对分别有哪些利弊，\x01",
            "还拿不定主意。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "说起来，明天好像\x01",
            "要在市民会馆召开\x01",
            "以独立为主题的市民座谈会……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "不如去咨询一下好了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_271A")

    label("loc_26C5")


    #C0023
    ChrTalk(
        0xFE,
        (
            "明天好像要在市民会馆召开\x01",
            "以独立为主题的市民座谈会……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "不如去咨询一下好了。\x02",
    )

    CloseMessageWindow()

    label("loc_271A")

    Jump("loc_306F")

    label("loc_271F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27A0")

    #C0025
    ChrTalk(
        0xFE,
        (
            "话说回来，调查独立意向的\x01",
            "居民投票在一周后\x01",
            "就要开始了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "唔～该怎么决定呢？\x01",
            "必须要尽快确定自己的立场了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306F")

    label("loc_27A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2834")

    #C0027
    ChrTalk(
        0xFE,
        (
            "呵呵呵，彩虹剧团的\x01",
            "新版舞剧\x01",
            "很快就要公演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "而且还确定要\x01",
            "增加新角色……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "接下来可绝对不能错过任何消息啊！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_289E")

    label("loc_2834")


    #C0030
    ChrTalk(
        0xFE,
        (
            "扮演新增角色的那个女孩\x01",
            "好像是叫修利。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "以她的年龄来说，还应该在主日学校上课……\x01",
            "真是让人吃惊呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_289E")

    Jump("loc_306F")

    label("loc_28A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_29AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2968")

    #C0032
    ChrTalk(
        0xFE,
        (
            "虽然没有见过本人，\x01",
            "但尤莉亚准校的容貌如此清秀，\x01",
            "真想象不出她会是一名军人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "我并没有那方面的\x01",
            "特殊喜好啦……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "但看到那么清秀端庄的美人，\x01",
            "好想紧紧抱在怀里⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_29A5")

    label("loc_2968")


    #C0035
    ChrTalk(
        0xFE,
        (
            "呼～尤莉亚准校\x01",
            "真是潇洒啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "好想把她紧紧抱在怀里⊥\x02",
    )

    CloseMessageWindow()

    label("loc_29A5")

    Jump("loc_306F")

    label("loc_29AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A37")

    #C0037
    ChrTalk(
        0xFE,
        (
            "刚才有个东方打扮的女性\x01",
            "往东街那边走去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "那流水一般的乌黑长发，\x01",
            "还有潇洒的西装打扮……\x01",
            "真是太美了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC1")

    label("loc_2A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B7E")

    #C0039
    ChrTalk(
        0xFE,
        (
            "刚才有个东方打扮的女性\x01",
            "从这里经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "那流水一般的乌黑长发，\x01",
            "还有潇洒的西装打扮……\x01",
            "真是太美了……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00005F（东方打扮的黑发女性……？）\x02\x03",

            "#00001F请问那个人去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "唔，好像是去了\x01",
            "东街方向。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#00003F东街……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#00101F（虽然还不能确定是不是『她』，\x01",
            "  但似乎应该去一探究竟呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    SetScenarioFlags(0x1C6, 6)
    Jump("loc_2EC1")

    label("loc_2B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E63")

    #C0045
    ChrTalk(
        0xFE,
        (
            "来自利贝尔王国……\x01",
            "嗯……哦，想起来了！\x01",
            "是尤莉亚·舒华兹准校！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "我自从在街上看到\x01",
            "她的照片之后，\x01",
            "就彻底迷上她了！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "而且，听说在利贝尔还成立了\x01",
            "她的后援会……\x01",
            "不知道外国人能不能加入呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0048
    ChrTalk(
        0x102,
        (
            "#00105F准、准校的后援会吗……\x01",
            "我还是第一次听说呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        (
            "#10100F好像是在某个\x01",
            "杂志社的提议之下，\x01",
            "最近刚刚成立的非官方俱乐部。\x02\x03",

            "#10102F听说俱乐部的会员每个月\x01",
            "都能收到准校的官方行程表\x01",
            "和珍藏照片呢……！\x02\x03",

            "#10106F但遗憾的是……\x01",
            "似乎只有居住在利贝尔的人\x01",
            "才能加入呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0050
    ChrTalk(
        0xFE,
        "哎！是这样吗！？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        "#00103F嗯～的确很遗憾呢。\x02",
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
        "#00005F（诺艾尔好像对此很熟悉啊。）\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00306F（是啊，该怎么说呢……\x01",
            "  痴迷程度好像比我们想象中的还要强呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 0)
    Jump("loc_2EC1")

    label("loc_2E63")


    #C0054
    ChrTalk(
        0xFE,
        (
            "我好想加入尤莉亚准校的\x01",
            "后援会啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "不、不知道能不能找出一个\x01",
            "住在利贝尔的远亲呢！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC1")

    Jump("loc_306F")

    label("loc_2EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F44")

    #C0056
    ChrTalk(
        0xFE,
        "通商会议终于要在明天正式召开了啊。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "至今为止，我只在杂志上见过\x01",
            "各国的首脑要人，\x01",
            "他们想必都气度非凡吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306F")

    label("loc_2F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2F52")
    Jump("loc_306F")

    label("loc_2F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_306F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300B")

    #C0058
    ChrTalk(
        0xFE,
        (
            "迪塔市长真的是个\x01",
            "完美无缺的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "既有头脑又充满正义感，\x01",
            "兼具行动力与创新意识，\x01",
            "而且还是个英俊的资产家……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "呼，总觉得说着说着\x01",
            "就要迷上他了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_306F")

    label("loc_300B")


    #C0061
    ChrTalk(
        0xFE,
        (
            "迪塔市长真的是个\x01",
            "完美无缺的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "除了政治和经济之外，\x01",
            "应该就没有什么事情能让他烦恼了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306F")

    TalkEnd(0xFE)
    Return()

    # Function_11_21CD end

    def Function_12_3073(): pass

    label("Function_12_3073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30AA")
    Call(0, 90)
    Return()

    label("loc_30AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3521")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C5")

    #C0063
    ChrTalk(
        0x1A2,
        "（仔细嗅）……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x1A2,
        "嗯，好香的味道啊！\x02",
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
            "嘿，少年！\x01",
            "你也能明白我的面有多好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x1A2,
        "哦，算是吧。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x1A2,
        (
            "如果是Ｂ级美食家，\x01",
            "应该会较为满意吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x9,
        "竟、竟敢说我的面是Ｂ级……！\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "可恶！回去回去！\x01",
            "我的面不会让不懂其价值\x01",
            "的人吃！\x02",
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
            "大姐姐，\x01",
            "我说了什么不对的话吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_331B")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_32A0():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32A0)
    Sleep(50)

    def lambda_32B0():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32B0)
    Sleep(50)

    def lambda_32C0():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_32C0)
    Sleep(300)

    #C0071
    ChrTalk(
        0x102,
        "#00106F秦……\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        (
            "#00306F该怎么说呢，在这方面\x01",
            "好像不太通人情事故呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BA")

    label("loc_331B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_33EF")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3374():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3374)
    Sleep(50)

    def lambda_3384():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3384)
    Sleep(50)

    def lambda_3394():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3394)
    Sleep(300)

    #C0073
    ChrTalk(
        0x102,
        "#00106F秦……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x109,
        (
            "#10106F该怎么说呢，在这方面\x01",
            "好像不太通人情事故呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BA")

    label("loc_33EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_34BA")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3448():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3448)
    Sleep(50)

    def lambda_3458():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3458)
    Sleep(50)

    def lambda_3468():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3468)
    Sleep(300)

    #C0075
    ChrTalk(
        0x102,
        "#00106F秦……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，看来他在这方面\x01",
            "不太通人情世故呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34BA")

    TalkEnd(0x9)
    SetScenarioFlags(0x1DC, 1)
    Jump("loc_3520")

    label("loc_34C5")


    #C0077
    ChrTalk(
        0x9,
        "竟、竟敢说我的面是Ｂ级……！\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "可恶！回去回去！\x01",
            "我的面不会让不懂其价值\x01",
            "的人吃！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3520")

    Return()

    label("loc_3521")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_352B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D5")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_357B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_357B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_359B")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_42D0")

    label("loc_359B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35AF")
    Jump("loc_42D0")

    label("loc_35AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_365F")

    #C0079
    ChrTalk(
        0xFE,
        (
            "呵呵，年轻人之中，\x01",
            "也有一些可造之材啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "一定要好好活用我给你们的食谱，\x01",
            "努力做出最顶级的面条。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "我也会在背后\x01",
            "为你们加油的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42D0")

    label("loc_365F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_36CC")

    #C0082
    ChrTalk(
        0xFE,
        "唔，终于到此地步了吗……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "我也要拿出相应的觉悟。\x01",
            "事到如今，唯一能做的就只有勇敢前进！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42D0")

    label("loc_36CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_378B")

    #C0084
    ChrTalk(
        0xFE,
        (
            "多年来一直与我同甘共苦的摊子\x01",
            "被毁坏时，真是受了相当大的打击……\x01",
            "但无论在什么时候，也必须要积极向前看！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "趁着这次弃旧换新，我也得重新振奋精神，\x01",
            "今后要和新摊子一起加油！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42D0")

    label("loc_378B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_37FD")

    #C0086
    ChrTalk(
        0xFE,
        (
            "玛因兹好像出现了一群\x01",
            "非常惊人的可恶家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "哼，真想把这些刚煮好的滚烫汤汁\x01",
            "泼到他们的脸上。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42D0")

    label("loc_37FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_38C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3858")
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0088
    ChrTalk(
        0xFE,
        "……啊嚏！\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "唔，身体好像有点\x01",
            "发冷啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_38BE")

    label("loc_3858")


    #C0090
    ChrTalk(
        0xFE,
        (
            "好，那就给自己\x01",
            "做碗热面吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "只要吃下一碗面，身心都会温暖无比……\x01",
            "哈，因为是热腾腾的面条啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38BE")

    Jump("loc_42D0")

    label("loc_38C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_39C6")

    #C0092
    ChrTalk(
        0xFE,
        (
            "嗯？调味用的\x01",
            "辣椒粉好像\x01",
            "已经所剩无几了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "唔，得找个\x01",
            "合适的时间\x01",
            "去买一些了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39C1")

    #C0094
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

    label("loc_39C1")

    Jump("loc_42D0")

    label("loc_39C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A17")

    #C0095
    ChrTalk(
        0xFE,
        "嗯，今天的面也是最棒的。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "来尽情品尝我全心\x01",
            "制作的面条吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42D0")

    label("loc_3A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC5")

    #C0097
    ChrTalk(
        0xFE,
        (
            "竟然会提议独立，\x01",
            "迪塔市长真是\x01",
            "相当大胆啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "不过，我对市长这种积极的\x01",
            "做法持肯定态度。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "无论做任何事情，\x01",
            "若想成功，\x01",
            "都需要大胆的设想。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B11")

    label("loc_3AC5")


    #C0100
    ChrTalk(
        0xFE,
        (
            "不经挑战，便不可能获得成功……\x01",
            "唔……政治与做面条\x01",
            "的本质其实是一样的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B11")

    Jump("loc_42D0")

    label("loc_3B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9D")

    #C0101
    ChrTalk(
        0xFE,
        "一千位客人，就有一千种人生。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "通过与客人的接触，\x01",
            "了解到对方人生的一角……\x01",
            "这也是开店的乐趣之一啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BD4")

    label("loc_3B9D")


    #C0103
    ChrTalk(
        0xFE,
        (
            "那位老人和孙女的关系融洽起来了……\x01",
            "真是可喜可贺。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD4")

    Jump("loc_42D0")

    label("loc_3BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C64")

    #C0104
    ChrTalk(
        0xFE,
        (
            "刚才有个穿着西装\x01",
            "的红发青年\x01",
            "来吃了我的面。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "他一边说着『去吃些餐后甜点吧』，\x01",
            "一边往欢乐街那边走去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F73")

    label("loc_3C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E5B")

    #C0106
    ChrTalk(
        0xFE,
        (
            "刚才有个穿着西装\x01",
            "的红发青年\x01",
            "来吃了我的面……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "但他跑到了摊子里侧，\x01",
            "想偷看我的秘传汤料配方。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "在千钧一发之际，\x01",
            "我终于成功把他赶走了……\x01",
            "真是个奇怪的男人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#00005F（穿西装的红发青年……）\x02\x03",

            "#00006F（……而且，这种行为方式\x01",
            "  似乎和我们认识的\x01",
            "  某个人很相符呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x105,
        "#10300F那个人去哪里了？\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "哦，他一边说着『去吃些餐后甜点吧』，\x01",
            "一边往欢乐街那边走去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00001F欢乐街……\x02\x03",

            "#00003F（……虽然还无法断言\x01",
            "  那个人就是『他』，\x01",
            "  但还是追去看看如何……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    SetScenarioFlags(0x1C7, 1)
    Jump("loc_3F73")

    label("loc_3E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EEE")

    #C0113
    ChrTalk(
        0xFE,
        (
            "嗯，各国的首脑今天\x01",
            "都来到了克洛斯贝尔，\x01",
            "市里的气氛真是隆重森严。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "我也明白警戒工作是必要的，\x01",
            "但还是非常介意警察的视线。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3F73")

    label("loc_3EEE")


    #C0115
    ChrTalk(
        0xFE,
        (
            "因为那些警察在警戒，\x01",
            "我在这里摆摊子都能\x01",
            "隐隐感觉到射来的视线。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "真是的，都不能集中精神工作了。\x01",
            "希望能早点恢复平常的生活啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F73")

    Jump("loc_42D0")

    label("loc_3F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402D")

    #C0117
    ChrTalk(
        0xFE,
        "面条就得筋道！而且还要爽口！\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "话说在先，吃我做的面条，\x01",
            "完全不需要注意什么仪态吃相！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "就得狼吞虎咽，吃得嗒嗒有声，\x01",
            "才能充分品味到面条的味道！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_40A5")

    label("loc_402D")


    #C0120
    ChrTalk(
        0xFE,
        (
            "话说在先，吃我做的面条，\x01",
            "完全不需要注意什么仪态吃相！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "就得狼吞虎咽，吃得嗒嗒有声，\x01",
            "才能充分品味到面条的味道！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40A5")

    Jump("loc_42D0")

    label("loc_40AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_41D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_40FA")

    #C0122
    ChrTalk(
        0xFE,
        "撑粉色雨伞的女孩……？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "没见过，没来过\x01",
            "我这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41CE")

    label("loc_40FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417A")

    #C0124
    ChrTalk(
        0xFE,
        "做面之道就是忍耐！\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        "我是不会败给这点小雨的！\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#00003F（雨不会溅到餐具上吗？\x01",
            "  有些让人担心呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_41CE")

    label("loc_417A")


    #C0127
    ChrTalk(
        0xFE,
        (
            "来吧，难得过来一趟，\x01",
            "一定要尝一碗我做的面啊。\x01",
            "吃了它，能让冰冷的身体瞬间温暖。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41CE")

    Jump("loc_42D0")

    label("loc_41D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_42D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_428A")

    #C0128
    ChrTalk(
        0xFE,
        (
            "做面之道，非一朝一夕之功……\x01",
            "而且这条道路永远都没有终点。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "经过反复研究，\x01",
            "我终于做出了\x01",
            "新品面条。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "它的名字是天上面『日轮』。\x01",
            "请一定要尝尝看！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_42D0")

    label("loc_428A")


    #C0131
    ChrTalk(
        0xFE,
        (
            "我对这次的新品面条\x01",
            "有着绝对的自信。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "相信一定能让\x01",
            "你们满足。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42D0")

    Jump("loc_352B")

    label("loc_42D5")

    TalkEnd(0xFE)
    Return()

    # Function_12_3073 end

    def Function_13_42D9(): pass

    label("Function_13_42D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43A1")

    #C0133
    ChrTalk(
        0xFE,
        (
            "从今天早上开始，铁路货运就停运了，\x01",
            "送货数量一下减了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "……话说回来，如果再这么下去，\x01",
            "克洛斯贝尔究竟会变得怎样呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "和工作相比，还是这个问题更重要啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4404")

    label("loc_43A1")


    #C0136
    ChrTalk(
        0xFE,
        (
            "说起来，如果再这么下去\x01",
            "克洛斯贝尔究竟会变得怎样呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "和工作相比，还是这个问题更重要啊……\x02",
    )

    CloseMessageWindow()

    label("loc_4404")

    Jump("loc_49EB")

    label("loc_4409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4481")

    #C0138
    ChrTalk(
        0xFE,
        (
            "袭击事件已经过去一周了……\x01",
            "这一带也终于恢复平静了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "总之，真希望那样的事件\x01",
            "别再发生第二次了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49EB")

    label("loc_4481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_454F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4513")

    #C0140
    ChrTalk(
        0xFE,
        (
            "警备队在镇压\x01",
            "玛因兹的武装集团时，\x01",
            "好像花费了相当一番工夫。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "作为国家独立，然后建立军队……\x01",
            "果然还是必要的吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_454A")

    label("loc_4513")


    #C0142
    ChrTalk(
        0xFE,
        (
            "作为国家独立，然后建立军队……\x01",
            "果然还是必要的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_454A")

    Jump("loc_49EB")

    label("loc_454F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_462C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45CA")

    #C0143
    ChrTalk(
        0xFE,
        (
            "哇！？被雨淋了之后，\x01",
            "送货单上的文字都消失了！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "不、不过，总会有办法\x01",
            "识别出来的……嗯。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4627")

    label("loc_45CA")


    #C0145
    ChrTalk(
        0xFE,
        (
            "如果回总部逐一确认\x01",
            "送货地点，\x01",
            "会浪费掉大量时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "呼，在下雨天送货，\x01",
            "真是很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4627")

    Jump("loc_49EB")

    label("loc_462C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4686")

    #C0147
    ChrTalk(
        0xFE,
        (
            "有很多辆急救车\x01",
            "往返于站前街道\x01",
            "到西街的路线呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        "究竟发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_49EB")

    label("loc_4686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46CC")

    #C0149
    ChrTalk(
        0xFE,
        "好，今天也要努力工作～！\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "效率最佳的路线是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_49EB")

    label("loc_46CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4773")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_473F")

    #C0151
    ChrTalk(
        0xFE,
        (
            "嗯，再送两件，\x01",
            "然后就去吃午饭了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "好～只要这么一想，\x01",
            "就觉得涌现出不少力量了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_476E")

    label("loc_473F")


    #C0153
    ChrTalk(
        0xFE,
        (
            "再送两件就去吃饭，\x01",
            "再送两件就去吃饭……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_476E")

    Jump("loc_49EB")

    label("loc_4773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4815")

    #C0154
    ChrTalk(
        0xFE,
        (
            "在通商会议期间，\x01",
            "警察禁止我们向市政厅大楼\x01",
            "配送任何发自民间的包裹。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "要是混进了可疑物品，\x01",
            "可就再也笑不出来了。\x01",
            "所以我认为这是很合理的规定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49EB")

    label("loc_4815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_48B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_489F")

    #C0156
    ChrTalk(
        0xFE,
        (
            "上午有各国要人前来，\x01",
            "实在没法送货。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "不过，今天的工作量\x01",
            "还是和平时一样多……\x01",
            "这正是要拿出干劲的时候！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_48B3")

    label("loc_489F")


    #C0158
    ChrTalk(
        0xFE,
        "冲啊冲啊冲啊！\x02",
    )

    CloseMessageWindow()

    label("loc_48B3")

    Jump("loc_49EB")

    label("loc_48B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4904")

    #C0159
    ChrTalk(
        0xFE,
        "巡逻的警察真是不少呢。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        "……得小心些，免得撞上他们。\x02",
    )

    CloseMessageWindow()
    Jump("loc_49EB")

    label("loc_4904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_49AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_494A")

    #C0161
    ChrTalk(
        0xFE,
        (
            "不好意思，我正在工作，\x01",
            "没见过什么女孩哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49A6")

    label("loc_494A")


    #C0162
    ChrTalk(
        0xFE,
        (
            "嘿嘿，刮风也好，暴雨也好，\x01",
            "我都不会退缩的！\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "……话虽如此，\x01",
            "但最好还是别下暴雨啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A6")

    Jump("loc_49EB")

    label("loc_49AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_49EB")

    #C0164
    ChrTalk(
        0xFE,
        (
            "呼，好忙好忙……\x01",
            "送货果然是个靠体力吃饭的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49EB")

    TalkEnd(0xFE)
    Return()

    # Function_13_42D9 end

    def Function_14_49EF(): pass

    label("Function_14_49EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4B10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AAD")

    #C0165
    ChrTalk(
        0xFE,
        (
            "真是愚蠢透顶的演说啊……\x01",
            "就算能欺骗所有人，\x01",
            "也别想欺骗老头子我！\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "什么独立国！什么国防军！\x01",
            "他们真的以为自己能在两大国的\x01",
            "威胁之下，保证我们的安全吗！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B0B")

    label("loc_4AAD")


    #C0167
    ChrTalk(
        0xFE,
        (
            "女神啊……\x01",
            "无论让我遭遇到什么事情都无所谓。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "但无论如何也请\x01",
            "救救我的孙女亚米萨……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B0B")

    Jump("loc_5077")

    label("loc_4B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B7E")

    #C0169
    ChrTalk(
        0xFE,
        (
            "当时如果逃得稍微慢些的话，\x01",
            "我和亚米萨恐怕就都……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "……如今回想起来，\x01",
            "仍然无比后怕呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5077")

    label("loc_4B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4BD0")

    #C0171
    ChrTalk(
        0xFE,
        (
            "真是可叹啊。\x01",
            "竟然如此折磨玛因兹的居民，\x01",
            "这究竟是要做什么……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5077")

    label("loc_4BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C51")

    #C0172
    ChrTalk(
        0xFE,
        (
            "唔，远远望去能看到的那个，应该就是\x01",
            "叫做观览车的东西吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "……喂，亚米萨，\x01",
            "下次和爷爷一起去\x01",
            "主题公园玩吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5077")

    label("loc_4C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4CA0")

    #C0174
    ChrTalk(
        0xFE,
        (
            "哇哈哈哈哈！\x01",
            "怎么样，看到了吗？亚米萨。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        "爷爷很厉害吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5077")

    label("loc_4CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4CE9")

    #C0176
    ChrTalk(
        0xFE,
        "看着吧，亚米萨～！\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "爷爷马上就会\x01",
            "钓起一条大鱼了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5077")

    label("loc_4CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4CF7")
    Jump("loc_5077")

    label("loc_4CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D12")
    Call(0, 15)
    Jump("loc_4D5B")

    label("loc_4D12")


    #C0178
    ChrTalk(
        0xFE,
        (
            "亚米萨真是个温柔善良\x01",
            "的好孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "……太感动了，感觉要哭出来了。\x02",
    )

    CloseMessageWindow()

    label("loc_4D5B")

    Jump("loc_5077")

    label("loc_4D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E09")

    #C0180
    ChrTalk(
        0xFE,
        (
            "警察对我说，\x01",
            "在通商会议的召开期间，\x01",
            "禁止在码头钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "不过，偶尔和孙女一起\x01",
            "欣赏欣赏城市的风景，\x01",
            "倒也挺愉快的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xB, 0x2D, 0x0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_4E2A")

    label("loc_4E09")


    #C0182
    ChrTalk(
        0xFE,
        (
            "哦，我看看，\x01",
            "那就是咪西啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E2A")

    Jump("loc_4E63")

    label("loc_4E2F")


    #C0183
    ChrTalk(
        0xFE,
        (
            "唔，跳得好像\x01",
            "很快乐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "年轻就是\x01",
            "好啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E63")

    Jump("loc_5077")

    label("loc_4E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4FDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F52")

    #C0185
    ChrTalk(
        0xFE,
        (
            "我可懒得管什么通商会议，\x01",
            "一群警察在街上转来转去，\x01",
            "真是让人心烦。\x02",
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
        "……啊，不好不好。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "亚米萨说过，让我不要总是抱怨，\x01",
            "结果一不小心又没管住自己。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_4FD9")

    label("loc_4F52")


    #C0188
    ChrTalk(
        0xFE,
        (
            "亚米萨说，我总是抱怨连连，\x01",
            "对自己的身体很不好。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "虽然不知道她说的对不对，\x01",
            "但我可不想看到她伤心的样子。\x01",
            "尽量照着她说的努力吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD9")

    Jump("loc_5077")

    label("loc_4FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4FEC")
    Jump("loc_5077")

    label("loc_4FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5007")
    Call(0, 16)
    Jump("loc_5077")

    label("loc_5007")


    #C0190
    ChrTalk(
        0xFE,
        (
            "在这个世界上，\x01",
            "我最讨厌的就是医院……\x01",
            "不过我最疼爱孙女了。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "所以，只要是那\x01",
            "孩子说的，我都\x01",
            "会尽量接受。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5077")

    TalkEnd(0xFE)
    Return()

    # Function_14_49EF end

    def Function_15_507B(): pass

    label("Function_15_507B")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0192
    ChrTalk(
        0xB,
        (
            "呼啊、呼啊……\x01",
            "这汤面太烫了，\x01",
            "真是难以入口啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)
    Sleep(500)

    #C0193
    ChrTalk(
        0xC,
        (
            "真是的，都是因为爷爷\x01",
            "吃得那么急。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xC,
        (
            "对了，我来帮您\x01",
            "吹吹吧，\x01",
            "稍等一下哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)
    Sleep(500)

    #C0195
    ChrTalk(
        0xC,
        (
            "（吹气）……\x01",
            "好啦，可以吃了¤\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "哦哦……\x01",
            "谢谢啦，亚米萨。\x02",
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

    # Function_15_507B end

    def Function_16_5185(): pass

    label("Function_16_5185")


    #C0197
    ChrTalk(
        0xC,
        (
            "爷爷，我今天\x01",
            "也给您带药来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "嗯，总是麻烦你呢，\x01",
            "我过一会就吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xC,
        (
            "不行～只要我没在一边看着，\x01",
            "您有时候就会不吃药。\x01",
            "我都知道的。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xC,
        (
            "今天我也会在旁边监督的，\x01",
            "不但要吃药，也要好好吃饭哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        (
            "是、是吗……\x01",
            "真是什么都瞒不过你啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_16_5185 end

    def Function_17_5286(): pass

    label("Function_17_5286")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_52E0")

    #C0202
    ChrTalk(
        0xFE,
        (
            "真的会像爷爷说的一样，\x01",
            "爆发战争吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        "……不要啊，好可怕………\x02",
    )

    CloseMessageWindow()
    Jump("loc_561D")

    label("loc_52E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5323")

    #C0204
    ChrTalk(
        0xFE,
        (
            "那边那座红色的建筑物……\x01",
            "完全变成一堆废墟了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_561D")

    label("loc_5323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5358")

    #C0205
    ChrTalk(
        0xFE,
        (
            "爷爷，心情烦躁\x01",
            "对身体很不好哦……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_561D")

    label("loc_5358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5399")

    #C0206
    ChrTalk(
        0xFE,
        (
            "哎，真的可以吗！？\x01",
            "爷爷！\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "哇！好期待啊¤\x02",
    )

    CloseMessageWindow()
    Jump("loc_561D")

    label("loc_5399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_53E1")

    #C0208
    ChrTalk(
        0xFE,
        "嗯！\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "刚才那条鱼\x01",
            "真的好大哦。\x01",
            "好期待今天的晚饭¤\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_561D")

    label("loc_53E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_542F")

    #C0210
    ChrTalk(
        0xFE,
        (
            "爷爷，\x01",
            "鱼竿刚才动了一下呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "（紧张）……\x01",
            "鱼上钩了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_561D")

    label("loc_542F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_543D")
    Jump("loc_561D")

    label("loc_543D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_548B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5458")
    Call(0, 15)
    Jump("loc_5486")

    label("loc_5458")


    #C0212
    ChrTalk(
        0xFE,
        "爷爷，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "有什么难过的事情吗？\x02",
    )

    CloseMessageWindow()

    label("loc_5486")

    Jump("loc_561D")

    label("loc_548B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54CD")

    #C0214
    ChrTalk(
        0xFE,
        "看啊看啊！爷爷！\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        "咪西来公园了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_552B")

    label("loc_54CD")

    OP_4B(0xB, 0xFF)

    #C0216
    ChrTalk(
        0xFE,
        (
            "爷爷，\x01",
            "下次和亚米萨\x01",
            "一起去跳舞吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xB,
        (
            "唔～唔……\x01",
            "对我来说，是个\x01",
            "严峻的考验啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_552B")

    Jump("loc_561D")

    label("loc_5530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_553E")
    Jump("loc_561D")

    label("loc_553E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_554C")
    Jump("loc_561D")

    label("loc_554C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_561D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5567")
    Call(0, 16)
    Jump("loc_561D")

    label("loc_5567")


    #C0218
    ChrTalk(
        0xFE,
        (
            "因为我坚持不懈，一直恳求，\x01",
            "性格顽固的爷爷最近\x01",
            "终于开始吃药了。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "虽然在我不盯着的时候，\x01",
            "他偶尔还是会偷偷不吃……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，一直没有放弃，\x01",
            "终于成功说服了爷爷，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_561D")

    TalkEnd(0xFE)
    Return()

    # Function_17_5286 end

    def Function_18_5621(): pass

    label("Function_18_5621")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_56D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56AD")

    #C0221
    ChrTalk(
        0xFE,
        "（喘气）……（喘气）……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "新版舞剧\x01",
            "终于要在明天公演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "虽然下着雨，\x01",
            "但我的心情还是无法平静啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_56CB")

    label("loc_56AD")


    #C0224
    ChrTalk(
        0xFE,
        "（喘气）……（喘气）……\x02",
    )

    CloseMessageWindow()

    label("loc_56CB")

    Jump("loc_57D5")

    label("loc_56D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5768")

    #C0225
    ChrTalk(
        0xFE,
        "（喘气）……（喘气）……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "虽说休息也是很重要的，\x01",
            "但我还是不能什么都不做啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "活动一下身体，\x01",
            "至少可以让自己不再胡思乱想。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_57D5")

    label("loc_5768")


    #C0228
    ChrTalk(
        0xFE,
        "（喘气）……（喘气）……\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "话说回来，最近这段时间，只要我在外面\x01",
            "跑步，塞利娜前辈就一定会和我一起跑。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57D5")

    TalkEnd(0xFE)
    Return()

    # Function_18_5621 end

    def Function_19_57D9(): pass

    label("Function_19_57D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5828")

    #C0230
    ChrTalk(
        0xFE,
        "我、我……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "我可不想输给\x01",
            "尼克鲁和修利。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_584B")

    label("loc_5828")


    #C0232
    ChrTalk(
        0xFE,
        (
            "我可不想输给尼克鲁\x01",
            "和修利啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_584B")

    Jump("loc_588E")

    label("loc_5850")


    #C0233
    ChrTalk(
        0xFE,
        (
            "尼克鲁那家伙……\x01",
            "竟想一鼓作气超越我。\x01",
            "才不会让他如愿呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_588E")

    TalkEnd(0xFE)
    Return()

    # Function_19_57D9 end

    def Function_20_5892(): pass

    label("Function_20_5892")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5916")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58EA")

    #C0234
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "大家好～！\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，\x01",
            "要度过愉快的一天哦～☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5911")

    label("loc_58EA")


    #C0236
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，\x01",
            "要度过愉快的一天哦～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5911")

    Jump("loc_596E")

    label("loc_5916")


    #C0237
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，\x01",
            "真是位有趣的小哥～\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "要是下次他能和我一起在\x01",
            "主题公园跳舞就好了～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_596E")

    TalkEnd(0xFE)
    Return()

    # Function_20_5892 end

    def Function_21_5972(): pass

    label("Function_21_5972")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E4")

    #C0239
    ChrTalk(
        0xFE,
        (
            "咪西今天是特意\x01",
            "从米修拉姆过来的哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "我们准备了各式各样的节目，\x01",
            "大家一起来参加吧～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A55")

    label("loc_59E4")


    #C0241
    ChrTalk(
        0xFE,
        (
            "哎呀～真是让人吃惊啊。\x01",
            "竟然能完美配合\x01",
            "咪西的舞步……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "难得遇到这么厉害的人，\x01",
            "要是能把他招揽过来就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A55")

    TalkEnd(0xFE)
    Return()

    # Function_21_5972 end

    def Function_22_5A59(): pass

    label("Function_22_5A59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AE9")

    #C0243
    ChrTalk(
        0xFE,
        (
            "呵呵呵，\x01",
            "咪西的舞蹈表演\x01",
            "很快就要开始啦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "另外，今天还有特别活动，\x01",
            "可以过去和咪西一起跳舞！\x01",
            "请一定要踊跃参加啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B64")

    label("loc_5AE9")


    #C0245
    ChrTalk(
        0xFE,
        (
            "那个金发的人\x01",
            "先是弹奏乐器，\x01",
            "为咪西的舞蹈提供伴奏音乐……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "弹着弹着，自己也跑去一起跳了。\x01",
            "呵呵，真是个有趣的人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B64")

    TalkEnd(0xFE)
    Return()

    # Function_22_5A59 end

    def Function_23_5B68(): pass

    label("Function_23_5B68")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5BB9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BB4")

    #C0247
    ChrTalk(
        0xFE,
        (
            "湖水浴场！湖水浴场！\x01",
            "好想去湖水浴场游泳啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BB4")

    Jump("loc_5C01")

    label("loc_5BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE2")

    #C0248
    ChrTalk(
        0xFE,
        "哇～是真正的咪西～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C01")

    label("loc_5BE2")


    #C0249
    ChrTalk(
        0xFE,
        (
            "我也想和咪西\x01",
            "一起跳舞～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C01")

    TalkEnd(0xFE)
    Return()

    # Function_23_5B68 end

    def Function_24_5C05(): pass

    label("Function_24_5C05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C47")

    #C0250
    ChrTalk(
        0xFE,
        (
            "（心跳加快）……\x01",
            "舞蹈表演还不\x01",
            "快点开始吗～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C8B")

    label("loc_5C47")


    #C0251
    ChrTalk(
        0xFE,
        (
            "那个金发的哥哥\x01",
            "真帅啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "虽然还是不能和咪西相比！\x01",
            "呵呵呵。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C8B")

    TalkEnd(0xFE)
    Return()

    # Function_24_5C05 end

    def Function_25_5C8F(): pass

    label("Function_25_5C8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5CDB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD6")

    #N0253
    NpcTalk(
        0xFE,
        "乘客",
        (
            "我对商店街的精品时装店\x01",
            "很有兴趣呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CD6")

    Jump("loc_5D28")

    label("loc_5CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D07")

    #C0254
    ChrTalk(
        0xFE,
        (
            "好了好了，\x01",
            "不要着急嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D28")

    label("loc_5D07")


    #C0255
    ChrTalk(
        0xFE,
        (
            "小孩们好像也看得\x01",
            "很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D28")

    TalkEnd(0xFE)
    Return()

    # Function_25_5C8F end

    def Function_26_5D2C(): pass

    label("Function_26_5D2C")

    TalkBegin(0xFE)

    #N0256
    NpcTalk(
        0xFE,
        "乘客",
        "呵呵，你真是孩子气啊～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_5D2C end

    def Function_27_5D54(): pass

    label("Function_27_5D54")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5DD7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5DA2")

    #C0257
    ChrTalk(
        0xFE,
        (
            "我女朋友好像\x01",
            "非常开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        "果然去对了～\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DD2")

    label("loc_5DA2")


    #N0259
    NpcTalk(
        0xFE,
        "市民",
        (
            "啊～好期待啊。\x01",
            "真想快点去主题公园玩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD2")

    Jump("loc_5E86")

    label("loc_5DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E2D")

    #C0260
    ChrTalk(
        0xFE,
        "这就是传说中的咪西吗……\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "那不知忧愁的表情\x01",
            "真是让人越看越爱！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E86")

    label("loc_5E2D")


    #C0262
    ChrTalk(
        0xFE,
        (
            "咪西的\x01",
            "舞蹈表演\x01",
            "真是很华丽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "本以为只是个普通玩偶而已，\x01",
            "看来真是太小看它了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E86")

    TalkEnd(0xFE)
    Return()

    # Function_27_5D54 end

    def Function_28_5E8A(): pass

    label("Function_28_5E8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5EC8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5EC3")

    #C0264
    ChrTalk(
        0xFE,
        (
            "呵呵呵，我买了\x01",
            "很多特产呢☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EC3")

    Jump("loc_5F95")

    label("loc_5EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F45")

    #C0265
    ChrTalk(
        0xFE,
        (
            "虽然主题公园暂时停业，\x01",
            "但能在市里见到咪西真是超幸运啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "经过这次的相遇，\x01",
            "我已经成为咪西的支持者了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F95")

    label("loc_5F45")


    #C0267
    ChrTalk(
        0xFE,
        (
            "我已经完全成为\x01",
            "咪西的支持者了！\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "我要买很多咪西的周边，\x01",
            "带回去做纪念！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F95")

    TalkEnd(0xFE)
    Return()

    # Function_28_5E8A end

    def Function_29_5F99(): pass

    label("Function_29_5F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FB0")
    Call(0, 47)
    Return()

    label("loc_5FB0")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_29_5F99 end

    def Function_30_5FB7(): pass

    label("Function_30_5FB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FE9")
    Call(0, 61)
    Jump("loc_5FEC")

    label("loc_5FE9")

    Call(0, 69)

    label("loc_5FEC")

    Return()

    # Function_30_5FB7 end

    def Function_31_5FED(): pass

    label("Function_31_5FED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6010")
    Call(0, 70)

    label("loc_6010")

    Return()

    # Function_31_5FED end

    def Function_32_6011(): pass

    label("Function_32_6011")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_604D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_602F")
    Call(0, 34)
    Jump("loc_6048")

    label("loc_602F")


    #C0269
    ChrTalk(
        0x1B,
        "#01200F咕呜呜呜……\x02",
    )

    CloseMessageWindow()

    label("loc_6048")

    Jump("loc_6078")

    label("loc_604D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_605E")
    Jump("loc_6078")

    label("loc_605E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_606F")
    Jump("loc_6078")

    label("loc_606F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6078")

    label("loc_6078")

    TalkEnd(0xFE)
    Return()

    # Function_32_6011 end

    def Function_33_607C(): pass

    label("Function_33_607C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_6126")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_609A")
    Call(0, 34)
    Jump("loc_6121")

    label("loc_609A")


    #C0270
    ChrTalk(
        0x1C,
        (
            "#01109F好，蔡特，\x01",
            "从小滴的头上跳过去吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x1B, 0xFF)

    #C0271
    ChrTalk(
        0x1B,
        "#01203F咕呜呜呜……嗷。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x1C,
        (
            "#01106F……『太危险了，不行』？\x01",
            "嗯……是吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)

    label("loc_6121")

    Jump("loc_6151")

    label("loc_6126")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6137")
    Jump("loc_6151")

    label("loc_6137")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6148")
    Jump("loc_6151")

    label("loc_6148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6151")

    label("loc_6151")

    TalkEnd(0xFE)
    Return()

    # Function_33_607C end

    def Function_34_6155(): pass

    label("Function_34_6155")

    OP_4B(0x1C, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x1B, 0xFF)

    #C0273
    ChrTalk(
        0x1C,
        (
            "#01100F好，那就让\x01",
            "小滴来试试吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x1D,
        (
            "#06005F嗯，那个……\x02\x03",

            "#06000F……蔡特，请把手伸出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x1B,
        "#01200F嗷。（啪）\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x1D,
        (
            "#06005F哇……果然聪明啊。\x02\x03",

            "#06002F呵呵，而且它爪子上的肉球\x01",
            "好柔软呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x1C,
        "#01109F对吧对吧～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    OP_4C(0x1C, 0xFF)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x1B, 0xFF)
    Return()

    # Function_34_6155 end

    def Function_35_624A(): pass

    label("Function_35_624A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_62AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6268")
    Call(0, 34)
    Jump("loc_62A9")

    label("loc_6268")


    #C0278
    ChrTalk(
        0x1D,
        (
            "#06002F呵呵，蔡特果然\x01",
            "聪明啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x1B, 0xFF)

    #C0279
    ChrTalk(
        0x1B,
        "#01200F……嗷。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)

    label("loc_62A9")

    Jump("loc_62D9")

    label("loc_62AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_62BF")
    Jump("loc_62D9")

    label("loc_62BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_62D0")
    Jump("loc_62D9")

    label("loc_62D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_62D9")

    label("loc_62D9")

    TalkEnd(0xFE)
    Return()

    # Function_35_624A end

    def Function_36_62DD(): pass

    label("Function_36_62DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_634A")

    #C0280
    ChrTalk(
        0xFE,
        (
            "难得来一次，\x01",
            "不然就去米修拉姆看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "呵呵，现在才去，\x01",
            "不知道时间还够去多少地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63B9")

    label("loc_634A")


    #C0282
    ChrTalk(
        0xFE,
        (
            "呵呵，克洛斯贝尔这个地方，\x01",
            "不同街区的环境\x01",
            "真是有很大差异呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "欢乐街一带喧嚣无比，\x01",
            "而这里却如此宁静。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63B9")

    TalkEnd(0xFE)
    Return()

    # Function_36_62DD end

    def Function_37_63BD(): pass

    label("Function_37_63BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_6404")

    #C0284
    ChrTalk(
        0xFE,
        (
            "我要去\x01",
            "米修拉姆了。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "一定要去坐\x01",
            "那个观览车！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6447")

    label("loc_6404")


    #C0286
    ChrTalk(
        0xFE,
        (
            "妈妈……\x01",
            "这里好无聊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        "我们赶快回那个闪闪发亮的地方吧。\x02",
    )

    CloseMessageWindow()

    label("loc_6447")

    TalkEnd(0xFE)
    Return()

    # Function_37_63BD end

    def Function_38_644B(): pass

    label("Function_38_644B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6550")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64F4")

    #C0288
    ChrTalk(
        0xFE,
        (
            "没有永远不止的雨……\x01",
            "……也没有永不晴朗的天空。\x02",
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
            "……我刚才好像说出了\x01",
            "两句很帅气的话，\x01",
            "可惜接不下去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_654B")

    label("loc_64F4")


    #C0291
    ChrTalk(
        0xFE,
        (
            "没有永远不止的雨……\x01",
            "……也没有永远不会饿的肚子。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        "……呃，越来越不像样了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_654B")

    Jump("loc_65F2")

    label("loc_6550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_65F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_65AD")

    #C0293
    ChrTalk(
        0xFE,
        "撑伞的女孩……\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "如此说来，刚才好像\x01",
            "见到过……\x01",
            "也好像没见过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65F2")

    label("loc_65AD")


    #C0295
    ChrTalk(
        0xFE,
        (
            "雨滴到底是\x01",
            "什么形状的呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        "……如果凝神注视，能看清楚吗？\x02",
    )

    CloseMessageWindow()

    label("loc_65F2")

    TalkEnd(0xFE)
    Return()

    # Function_38_644B end

    def Function_39_65F6(): pass

    label("Function_39_65F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66CB")

    #C0297
    ChrTalk(
        0xFE,
        (
            "不久之后，各国首脑就要从米修拉姆\x01",
            "回到这里，并出发前往兰花塔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "在他们进去兰花塔之前，\x01",
            "这里将会再次封锁戒严。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "如果有事要去金融街，\x01",
            "就抓紧时间办完吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        "#00000F好的，明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6735")

    label("loc_66CB")


    #C0301
    ChrTalk(
        0xFE,
        (
            "各国首脑从米修拉姆回到这里之后，\x01",
            "这里将会再次封锁戒严。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "如果有事要去金融街，\x01",
            "就抓紧时间办完吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6735")

    TalkEnd(0xFE)
    Return()

    # Function_39_65F6 end

    def Function_40_6739(): pass

    label("Function_40_6739")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_67DB")

    #C0303
    ChrTalk(
        0xFE,
        (
            "恐怖分子吗……\x01",
            "虽然原本就有所准备，但现在看来，\x01",
            "他们来这里的可能性进一步提高了。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "算了，不管怎么说，\x01",
            "暂时也只有遵照总部的指示来行动了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6904")

    label("loc_67DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6878")

    #C0305
    ChrTalk(
        0xFE,
        "咪西的外出表演活动吗……\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "好像已经得到了市里的\x01",
            "正式许可，\x01",
            "应该没什么问题吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "话说回来，米修拉姆奇幻乐园的\x01",
            "服务精神也真是旺盛呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6904")

    label("loc_6878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6904")

    #C0308
    ChrTalk(
        0xFE,
        (
            "调查『黑月』动向的工作\x01",
            "并不在公共安全科的职责范围内……\x01",
            "但警戒还是有必要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "不过，我想那些家伙\x01",
            "应该不会有什么公开举动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6904")

    TalkEnd(0xFE)
    Return()

    # Function_40_6739 end

    def Function_41_6908(): pass

    label("Function_41_6908")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_69F2")

    #C0310
    ChrTalk(
        0xFE,
        (
            "虽然黑月的事务所遭到彻底破坏，\x01",
            "但经过这一周时间的沉淀，\x01",
            "这一带的气氛好像已经平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "也许是因为即将召开\x01",
            "居民投票活动，\x01",
            "情绪消沉的市民似乎并不多……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "这让人充分感受到了大家在\x01",
            "处于危难时刻的强韧信念。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BC7")

    label("loc_69F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A7D")

    #C0313
    ChrTalk(
        0xFE,
        (
            "虽然有部分首脑已经返回市内，\x01",
            "不过多数首脑人物\x01",
            "还留在米修拉姆。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        (
            "毕竟有关于恐怖分子的情报，\x01",
            "警备工作一定要认真执行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BC7")

    label("loc_6A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6B12")

    #C0315
    ChrTalk(
        0xFE,
        (
            "听说奥斯本宰相去米修拉姆访问了，\x01",
            "而洛克史密斯总统\x01",
            "好像去ＩＢＣ访问了……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "两地周边的警卫工作都坚如磐石。\x01",
            "应该没什么可担心的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BC7")

    label("loc_6B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6BC7")

    #C0317
    ChrTalk(
        0xFE,
        (
            "我正在这里待命，\x01",
            "如果发生什么情况，\x01",
            "马上就会开警车赶往现场。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "虽然比不上警备队的装甲车，\x01",
            "但这警车也可以防弹，十分结实。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "如果遇到特殊情况，\x01",
            "完全可以当作护盾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BC7")

    TalkEnd(0xFE)
    Return()

    # Function_41_6908 end

    def Function_42_6BCB(): pass

    label("Function_42_6BCB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6C71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6C22")

    #C0320
    ChrTalk(
        0x24,
        (
            "多谢各位乘坐\x01",
            "水上巴士～\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x24,
        (
            "期待您\x01",
            "下次再来乘坐～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C6C")

    label("loc_6C22")


    #C0322
    ChrTalk(
        0x24,
        (
            "前往米修拉姆的水上巴士\x01",
            "即将出发～\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x24,
        (
            "需要搭乘的客人\x01",
            "请尽早上船～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C6C")

    Jump("loc_6CCA")

    label("loc_6C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_6CCA")

    #C0324
    ChrTalk(
        0xFE,
        (
            "前往米修拉姆的水上巴士\x01",
            "已经到达。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "稍后即将安排大家登船，\x01",
            "请排队等待。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CCA")

    TalkEnd(0xFE)
    Return()

    # Function_42_6BCB end

    def Function_43_6CCE(): pass

    label("Function_43_6CCE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6DD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D82")

    #C0326
    ChrTalk(
        0xFE,
        (
            "市内进入戒严状态了……\x01",
            "但这样一来，\x01",
            "反而觉得气氛很安稳呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "通商会议的热度\x01",
            "究竟会引发一场怎样的热潮呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "在这里静心思索一番\x01",
            "也不坏啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6DD8")

    label("loc_6D82")


    #C0329
    ChrTalk(
        0xFE,
        (
            "通商会议的热度\x01",
            "究竟会引发一场怎样的热潮呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "在这里静心思索一番\x01",
            "也不坏啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DD8")

    TalkEnd(0xFE)
    Return()

    # Function_43_6CCE end

    def Function_44_6DDC(): pass

    label("Function_44_6DDC")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EB2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EAA")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0331
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁，\x01",
            "门上挂着告示板。\x07\x00\x02",
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
            "『黑月贸易公司·克洛斯贝尔分公司』\x01",
            "※如有事情，敬请敲门。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_6EAD")

    label("loc_6EAA")

    Call(0, 72)

    label("loc_6EAD")

    Jump("loc_729E")

    label("loc_6EB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7114")
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
            "大门上着锁，\x01",
            "门上挂着告示板。\x07\x00\x02",
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
            "『黑月贸易公司·克洛斯贝尔分公司』\x01",
            "※如有事情，敬请敲门。\x07\x00\x02",
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
            "#00003F……看样子，\x01",
            "已经由别人陪秦少爷去游览了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x104,
        (
            "#00306F算了，这也没办法。\x01",
            "放弃任务，去处理其它事情吧。\x02",
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
            "任务【带领少年秦游览市区】\x07\x00",
            "失败了……\x02",
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
    Jump("loc_71B4")

    label("loc_7114")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁，\x01",
            "门上挂着告示板。\x07\x00\x02",
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
            "『黑月贸易公司·克洛斯贝尔分公司』\x01",
            "※如有事情，敬请敲门。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_71B4")

    Jump("loc_729E")

    label("loc_71B9")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁，\x01",
            "门上挂着告示板。\x07\x00\x02",
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
            "『黑月贸易公司·克洛斯贝尔分公司』\x01",
            "※如有事情，敬请敲门。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_729E")

    #C0342
    ChrTalk(
        0x101,
        (
            "#00003F再怎么说，应该也不会\x01",
            "进入这种地方吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_729E")

    TalkEnd(0xFF)
    Return()

    # Function_44_6DDC end

    def Function_45_72A2(): pass

    label("Function_45_72A2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_747C")

    #C0343
    ChrTalk(
        0x1A2,
        "唔，克洛斯贝尔通讯社啊。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x1A2,
        (
            "……我想起来了，他们的通讯社\x01",
            "就在这港湾区。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7323():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7323)

    def lambda_7330():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7330)

    #C0345
    ChrTalk(
        0x101,
        "#00005F嗯？你有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x1A2,
        "哼，也没什么……\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x1A2,
        (
            "硬要说的话，\x01",
            "就是不太喜欢那些整天鬼鬼祟祟\x01",
            "围着我们转的记者。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x1A2,
        (
            "不过，共和国的经济界人士\x01",
            "也都在订阅他们的经济杂志，\x01",
            "因此还是可以给予正面评价。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        "#00003F（呼～真不知该怎么形容他呢……）\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x102,
        (
            "#00100F（嗯，这个年龄就能说出这样的话，\x01",
            "  真让人难以相信呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_74D3")

    label("loc_747C")


    #C0351
    ChrTalk(
        0x1A2,
        (
            "通讯社这种地方……\x01",
            "我们就算进去，也会被立刻请出去吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x1A2,
        "还是赶快去别的地方吧。\x02",
    )

    CloseMessageWindow()

    label("loc_74D3")

    TalkEnd(0xFF)
    Return()

    # Function_45_72A2 end

    def Function_46_74D7(): pass

    label("Function_46_74D7")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0353
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759A")
    OP_E2(0x2)
    MiniGame(0x6, 0x1, 0x14226, 0xFFFFF63C, 0x3AA2, 0xB4, 0x13812, 0xFFFFF254, 0x226A)

    label("loc_759A")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_46_74D7 end

    def Function_47_759F(): pass

    label("Function_47_759F")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7959")

    #C0355
    ChrTalk(
        0x18,
        "#11P啊，是支援科的各位吧？\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#6P#00000F是的，下雨天还麻烦您，\x01",
            "真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x102,
        (
            "#00104F#6P多谢您帮我们\x01",
            "准备船只。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x18,
        (
            "#11P哪里哪里，\x01",
            "这是我分内的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x18,
        "#11P对了，你们会驾驶吗？\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x18,
        (
            "#11P如果有需要，\x01",
            "我可以为你们驾驶。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x101,
        "#6P#00008F对了，这也是个问题呢……\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x104,
        (
            "#00303F#6P如果会开车的话，\x01",
            "开船应该也不算太难吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x103,
        (
            "#6P#00200F科长会驾驶船只，\x01",
            "要用艾尼格玛联络他吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0364
    ChrTalk(
        0x109,
        (
            "#5P#10105F啊，不必了。\x02\x03",

            "#10100F我驾驶过\x01",
            "这种类型的船。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_782A():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_782A)
    Sleep(50)

    def lambda_783A():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_783A)
    Sleep(50)

    def lambda_784A():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_784A)
    Sleep(50)

    def lambda_785A():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_785A)
    Sleep(50)

    def lambda_786A():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_786A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    #C0365
    ChrTalk(
        0x101,
        "#12P#00002F哎，是吗？\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x104,
        "#6P#00309F哈哈，果然有一套啊。\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x105,
        (
            "#10302F看来你的确很擅长\x01",
            "驾驶、操作类的技术呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x109,
        (
            "#5P#10112F呵呵，这都是被索尼娅司令\x01",
            "锻炼出来的……\x02\x03",

            "#10100F如何？\x01",
            "要立刻乘船吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x165, 1)
    Jump("loc_798C")

    label("loc_7959")

    TurnDirection(0x109, 0x101, 500)

    #C0369
    ChrTalk(
        0x109,
        (
            "#5P#10100F如何？\x01",
            "要立刻乘船吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    label("loc_798C")


    #C0370
    ChrTalk(
        0x101,
        (
            "#12P#00003F这个嘛……\x02\x03",

            "#00008F（到了目的地之后，不知将会发生什么。\x01",
            "  还有没有其它的事情没做完呢？）\x02",
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
            "一旦乘船前往目的地，\x01",
            "在本章之内，就无法再前往\x01",
            "克洛斯贝尔市外了。\x02\x03",

            "请注意是否还有\x01",
            "未完成的任务。\x07\x00\x02",
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
            "【还有其它事情】\x01",      # 0
            "【乘船前往湿地】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_7AD9"),
        (0, "loc_7CBE"),
        (SWITCH_DEFAULT, "loc_7D33"),
    )


    label("loc_7AD9")


    #C0372
    ChrTalk(
        0x109,
        "#5P#10102F明白了！\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x18,
        (
            "#11P那好，各位\x01",
            "一路小心啊。\x02",
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

    def lambda_7BB0():

        label("loc_7BB0")

        TurnDirection(0xFE, 0x33, 500)
        Yield()
        Jump("loc_7BB0")

    QueueWorkItem2(0x18, 2, lambda_7BB0)
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
    Jump("loc_7D33")

    label("loc_7CBE")


    #C0374
    ChrTalk(
        0x109,
        "#5P#10100F明白了。\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x18,
        (
            "#11P那好，你们准备完毕之后\x01",
            "再来找我吧。\x02",
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
    Jump("loc_7D33")

    label("loc_7D33")

    Return()

    # Function_47_759F end

    def Function_48_7D34(): pass

    label("Function_48_7D34")

    OP_96(0x33, 0xA410, 0xFFFFF060, 0xFFFFA81C, 0xBB8, 0x0)

    def lambda_7D4D():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7D4D)
    Sleep(1000)

    def lambda_7D6B():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7D6B)
    Sleep(1000)

    def lambda_7D89():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7D89)
    Sleep(1000)

    def lambda_7DA7():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7DA7)

    def lambda_7DB4():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7DB4)

    def lambda_7DC1():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7DC1)

    def lambda_7DCE():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7DCE)

    def lambda_7DDB():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7DDB)

    def lambda_7DE8():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7DE8)

    def lambda_7DF5():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7DF5)
    Sleep(1000)

    def lambda_7E13():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7E13)
    WaitChrThread(0x33, 1)
    Return()

    # Function_48_7D34 end

    def Function_49_7E2E(): pass

    label("Function_49_7E2E")

    Sound(470, 0, 100, 0)
    Sound(482, 0, 60, 0)
    Sleep(5000)
    Sound(483, 2, 100, 0)
    Sleep(4000)
    StopSound(483, 2000, 90)
    Return()

    # Function_49_7E2E end

    def Function_50_7E4D(): pass

    label("Function_50_7E4D")

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

    def lambda_8032():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8032)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x18, 0)
    Sleep(120)
    TurnDirection(0x18, 0x101, 0)

    def lambda_805C():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_805C)
    Sleep(100)

    def lambda_8074():
        OP_9B(0x0, 0xFE, 0x5, 0x258, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8074)
    WaitChrThread(0x102, 1)

    def lambda_808D():
        OP_9B(0x0, 0xFE, 0xF, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_808D)
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

    def lambda_81A0():
        OP_95(0xFE, 38490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81A0)
    Sleep(60)

    def lambda_81BD():
        OP_95(0xFE, 37490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_81BD)
    Sleep(30)
    TurnDirection(0x18, 0x101, 500)

    def lambda_81E1():
        OP_95(0xFE, 38490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_81E1)
    Sleep(30)

    def lambda_81FE():
        OP_95(0xFE, 37990, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_81FE)

    def lambda_8218():
        OP_95(0xFE, 39490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8218)
    Sleep(30)

    def lambda_8235():
        OP_95(0xFE, 38290, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8235)
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

    # Function_50_7E4D end

    def Function_51_826E(): pass

    label("Function_51_826E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_82B8")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, -500, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("Function_51_826E")

    label("loc_82B8")

    Return()

    # Function_51_826E end

    def Function_52_82B9(): pass

    label("Function_52_82B9")

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

    # Function_52_82B9 end

    def Function_53_831A(): pass

    label("Function_53_831A")

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

    # Function_53_831A end

    def Function_54_837B(): pass

    label("Function_54_837B")

    OP_96(0x33, 0x9858, 0xFFFFF060, 0xFFFFA36C, 0x7D0, 0x0)
    TurnDirection(0x18, 0x33, 0)
    OP_96(0x33, 0x96C8, 0xFFFFF060, 0xFFFFA81C, 0x3E8, 0x0)
    Return()

    # Function_54_837B end

    def Function_55_83AB(): pass

    label("Function_55_83AB")

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

    # Function_55_83AB end

    def Function_56_83D9(): pass

    label("Function_56_83D9")

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
            "哎呀呀，在这大城市里兜风\x01",
            "真是太爽了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(50)

    #C0377
    ChrTalk(
        0x2A,
        (
            "瑞吉，你的驾驶技术\x01",
            "越来越了不起了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x2B,
        "嘿嘿，是吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x29, 500)
    Sleep(50)

    #C0379
    ChrTalk(
        0x2B,
        (
            "不过这也是因为\x01",
            "尤利准备的导力车\x01",
            "性能超群。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x29, 500)
    Sleep(50)

    #C0380
    ChrTalk(
        0x29,
        (
            "哼哼，那当然。\x01",
            "这可是乌尔努公司\x01",
            "的最新型车辆啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x29,
        (
            "……对了，瑞吉，\x01",
            "我们刚才差点就撞到了\x01",
            "那个站在路上的中年人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x2B,
        (
            "啊，嗯……\x01",
            "贴身而过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x2B,
        (
            "想想那个大叔\x01",
            "当时的吃惊表情……\x02",
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
        "#4S#1K#1P……真是太搞笑了！\x02",
    )


    #C0385
    ChrTalk(
        0x2A,
        "#4S#1K#3P真是太搞笑了！！\x02",
    )


    #C0386
    ChrTalk(
        0x2B,
        "#4S#1K#2P真是太搞笑了～！！\x02",
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
            "哇哈哈哈哈！\x01",
            "那个大叔当时真是被吓得\x01",
            "屁滚尿流啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x2A,
        (
            "我、我、我要被轧死啦～！！\x01",
            "救救我呀！妈妈～他心里一定是这么想的吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)
    Sleep(50)

    #C0389
    ChrTalk(
        0x2B,
        (
            "啊哈哈哈哈哈！！\x01",
            "别、别再说了，塞克斯！\x01",
            "我的肚子都笑疼了～～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x29,
        (
            "呵呵……\x01",
            "难得决定要长期居住在此，\x01",
            "总要找些乐子嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x29,
        (
            "这座名叫克洛斯贝尔的城市……\x01",
            "就是我们的新游戏场了。\x02",
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

    def lambda_8962():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8962)
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
            "哦……\x01",
            "警察好像要过来了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(50)

    #C0393
    ChrTalk(
        0x2A,
        "瑞吉，开车出发！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)
    Sleep(50)

    #C0394
    ChrTalk(
        0x2B,
        (
            "OK，不费吹灰之力\x01",
            "就能甩开那些家伙！\x02",
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

    def lambda_8AAA():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8AAA)

    def lambda_8ABF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_8ABF)
    WaitChrThread(0x2B, 2)
    Sleep(100)
    WaitChrThread(0x29, 1)

    def lambda_8ADB():
        OP_9B(0x0, 0xFE, 0xB4, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8ADB)

    def lambda_8AF0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_8AF0)
    Sleep(100)
    WaitChrThread(0x2A, 1)

    def lambda_8B08():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_8B08)

    def lambda_8B1D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_8B1D)
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

    # Function_56_83D9 end

    def Function_57_8C4D(): pass

    label("Function_57_8C4D")

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

    # Function_57_8C4D end

    def Function_58_8D4D(): pass

    label("Function_58_8D4D")

    OP_93(0x2B, 0x5A, 0x3E8)
    OP_9B(0x0, 0x2B, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_93(0x2B, 0x0, 0x1F4)
    Return()

    # Function_58_8D4D end

    def Function_59_8D6B(): pass

    label("Function_59_8D6B")

    OP_93(0x29, 0x0, 0x3E8)
    OP_9B(0x0, 0x29, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_93(0x29, 0x5A, 0x3E8)
    OP_9B(0x0, 0x29, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_93(0x29, 0xB4, 0x1F4)
    Return()

    # Function_59_8D6B end

    def Function_60_8D9F(): pass

    label("Function_60_8D9F")

    OP_93(0x2A, 0x0, 0x3E8)
    OP_9B(0x0, 0x2A, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_93(0x2A, 0x5A, 0x3E8)
    OP_9B(0x0, 0x2A, 0x0, 0x1388, 0xBB8, 0x0)
    OP_93(0x2A, 0xB4, 0x1F4)
    Return()

    # Function_60_8D9F end

    def Function_61_8DD3(): pass

    label("Function_61_8DD3")

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
            "梅琳那家伙\x01",
            "到底藏到哪里去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#12P#00100F那个……打扰一下，\x01",
            "请问您是梅琳的哥哥吗？\x02",
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
            "嗯？是啊……\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        (
            "#12P#00000F哦，我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0399
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将\x01",
            "帮小桃寻找雨伞\x01",
            "一事做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0400
    ChrTalk(
        0x19,
        (
            "……哦，\x01",
            "是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x19,
        (
            "梅琳竟然错拿了\x01",
            "别的孩子的伞，\x01",
            "我都没注意到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x19,
        (
            "真糟糕，既然如此，\x01",
            "本应马上物归原主才对……\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x109,
        (
            "#12P#10105F说起来……\x01",
            "梅琳去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x105,
        (
            "#12P#10300F她不是和你\x01",
            "一起出来散步吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x19,
        (
            "其实我刚刚开始和梅琳\x01",
            "玩捉迷藏。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x19,
        (
            "虽然在下雨天玩这个很麻烦，\x01",
            "但她坚持要玩，\x01",
            "我就迁就她了……\x02",
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
            "……她很擅长\x01",
            "躲藏的。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x19,
        (
            "而我又不太会找人，\x01",
            "恐怕很难立刻发现她……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        (
            "#12P#00006F是、是这样啊……\x02\x03",

            "#00000F既然如此……\x01",
            "我们可以一起\x01",
            "找梅琳吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x19,
        (
            "哦，当然，\x01",
            "那就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x19,
        (
            "梅琳应该就\x01",
            "藏在这港湾区\x01",
            "中的某个地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x19,
        (
            "既然是捉迷藏，\x01",
            "我想应该不会进入室内的。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x19,
        (
            "总之难度不小，\x01",
            "请各位加油找吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        "#12P#00100F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，那我们就\x01",
            "开始找吧。\x02",
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

    # Function_61_8DD3 end

    def Function_62_92A6(): pass

    label("Function_62_92A6")

    TalkBegin(0xFF)

    #C0416
    ChrTalk(
        0x101,
        (
            "#00012F长椅下面……没有呢。\x01",
            "想想也知道不会在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_62_92A6 end

    def Function_63_92E7(): pass

    label("Function_63_92E7")

    TalkBegin(0xFF)

    #C0417
    ChrTalk(
        0x101,
        "#00000F……不在摊子后面。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_63_92E7 end

    def Function_64_930D(): pass

    label("Function_64_930D")

    TalkBegin(0xFF)

    #C0418
    ChrTalk(
        0x101,
        "#00006F箱子后面……没有啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_64_930D end

    def Function_65_9335(): pass

    label("Function_65_9335")

    EventBegin(0x1)

    #C0419
    ChrTalk(
        0x101,
        (
            "#00000F既然是捉迷藏，\x01",
            "应该不会进入室内的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -14030, 2000, 24980, 180)
    EventEnd(0x4)
    Return()

    # Function_65_9335 end

    def Function_66_937E(): pass

    label("Function_66_937E")

    EventBegin(0x1)

    #C0420
    ChrTalk(
        0x101,
        (
            "#00000F梅琳应该就在\x01",
            "这港湾区中的某个地方。\x01",
            "……再找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 4500, 3050, 30320, 180)
    EventEnd(0x4)
    Return()

    # Function_66_937E end

    def Function_67_93D8(): pass

    label("Function_67_93D8")

    EventBegin(0x1)

    #C0421
    ChrTalk(
        0x101,
        (
            "#00000F梅琳应该就在\x01",
            "这港湾区中的某个地方。\x01",
            "……再找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -19940, 0, -25710, 359)
    EventEnd(0x4)
    Return()

    # Function_67_93D8 end

    def Function_68_9432(): pass

    label("Function_68_9432")

    EventBegin(0x1)

    #C0422
    ChrTalk(
        0x101,
        (
            "#00000F梅琳应该就在\x01",
            "这港湾区中的某个地方。\x01",
            "……再找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -25570, 2000, 23250, 90)
    EventEnd(0x4)
    Return()

    # Function_68_9432 end

    def Function_69_948C(): pass

    label("Function_69_948C")

    TalkBegin(0x19)

    #C0423
    ChrTalk(
        0x19,
        (
            "你们好像还没\x01",
            "找到梅琳吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x19,
        (
            "如果实在找不到，\x01",
            "只要宣布认输，\x01",
            "她应该就会出来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x19,
        "……如何？\x02",
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
            "认输\x01",          # 0
            "继续寻找\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9778")
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
        "#12P#00006F……抱歉，那就认输吧。\x02",
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x19,
        "呼，这也没办法。\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x19,
        "那么……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0429
    AnonymousTalk(
        0x19,
        "#4S梅琳～！我认输啦～～～！！#3S\x02",
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
        "……嘿嘿嘿，梅琳赢了～¤\x02",
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
            "就这样，罗伊德等人认输之后，\x01",
            "梅琳出现在众人的眼前…………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0432
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将梅琳错拿了\x01",
            "小桃雨伞的事情\x01",
            "再次做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(0, 71)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9801")

    label("loc_9778")


    #C0433
    ChrTalk(
        0x101,
        "#00000F不，我们再找找吧。\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x19,
        "是吗，那就加油吧。\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x19,
        (
            "顺便一说，请不要对我\x01",
            "抱有太高期待哦。\x01",
            "……我恐怕找到天黑都找不到。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9801")

    TalkEnd(0x19)
    Return()

    # Function_69_948C end

    def Function_70_9805(): pass

    label("Function_70_9805")

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
            "#00002F你就是……\x01",
            "梅琳吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        "#00102F呵呵，找到你了哦。\x02",
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
        "哇，被发现了～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0439
    ChrTalk(
        0x1A,
        "哎哎……不是哥哥啊～？\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x1A,
        "大哥哥，大姐姐，你们是谁？\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x109,
        "#10109F啊哈哈，总算找到了。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x105,
        (
            "#10300F那我们就回洛依\x01",
            "那里报告吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Call(0, 71)
    EventEnd(0x5)
    Return()

    # Function_70_9805 end

    def Function_71_99A6(): pass

    label("Function_71_99A6")

    EventBegin(0x0)
    ClearScenarioFlags(0x133, 4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch21500.itc", 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_9D75")
    OP_2C(0x6B, 0x1)
    SetChrName("")

    #A0443
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，罗伊德等人\x01",
            "把洛依叫到了梅琳藏身的地方……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0444
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将梅琳错拿了\x01",
            "小桃雨伞的事情\x01",
            "再次做了说明。\x07\x00\x02",
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
        "#6P#00000F……事情就是这样。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x1A,
        (
            "是这样啊～\x01",
            "原来是我拿错了伞。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x19,
        "梅琳，把伞还给人家吧。\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x1A,
        "嗯，哥哥。\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x1A,
        "就是这把～\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x109,
        "#6P#10100F好，交换。\x02",
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
            "把手中的伞交给了梅琳，\x01",
            "并收下了小桃的伞。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0452
    ChrTalk(
        0x102,
        "#6P#00100F呵呵，谢谢你啦。\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x1A,
        "不用～\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x1A,
        (
            "以后有机会，\x01",
            "我一定要向那个\x01",
            "叫小桃的小朋友道歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x105,
        (
            "#6P#10309F呵呵，小小年纪\x01",
            "就这么懂事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x19,
        "呼，是啊。\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x19,
        (
            "要是我也成熟些的话，\x01",
            "现在就能找到个工作了……\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x101,
        (
            "#6P#00012F那、那个……总之，\x01",
            "谢谢二位的帮忙。\x02\x03",

            "#00000F我们会把\x01",
            "雨伞交还给\x01",
            "对方的。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x19,
        "嗯，那就麻烦你们了。\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x1A,
        "拜托啦～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Jump("loc_A0A6")

    label("loc_9D75")

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
        "#12P#00000F……事情就是这样。\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x1A,
        (
            "是这样啊～\x01",
            "原来是我拿错了伞。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x19,
        "梅琳，把伞还给人家吧。\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x1A,
        "嗯，哥哥。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x1A,
        "就是这把～\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x109,
        "#12P#10100F好，交换。\x02",
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
            "把手中的伞交给了梅琳，\x01",
            "并收下了小桃的伞。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0468
    ChrTalk(
        0x102,
        "#12P#00100F呵呵，谢谢你啦。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x1A,
        "哪里～\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x1A,
        (
            "以后有机会，\x01",
            "我一定要向那个\x01",
            "叫小桃的小朋友道歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x105,
        (
            "#12P#10309F呵呵，小小年纪\x01",
            "就这么懂事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x19,
        "呼，是啊。\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x19,
        (
            "要是我也成熟些的话，\x01",
            "现在就能找到个工作了……\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x101,
        (
            "#12P#00012F那、那个……总之，\x01",
            "谢谢二位的帮忙。\x02\x03",

            "#00000F我们会把\x01",
            "雨伞交还给\x01",
            "对方的。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x19,
        "嗯，那就麻烦你们了。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x1A,
        "拜托啦～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)

    label("loc_A0A6")

    SetScenarioFlags(0x22, 0)
    NewScene("c0210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_71_99A6 end

    def Function_72_A0B3(): pass

    label("Function_72_A0B3")

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
            "大门上着锁，\x01",
            "门上挂着告示板。\x07\x00\x02",
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
            "『黑月贸易公司·克洛斯贝尔分公司』\x01",
            "※如有事情，敬请敲门。\x07\x00\x02",
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
            "#6P#10101F『黑月贸易公司』……\x02\x03",

            "#10103F就是那个名叫曹的人\x01",
            "负责管理的事务所吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x105,
        (
            "#10304F曹·李。\x01",
            "有着『白兰龙』之称号，\x01",
            "『黑月』组织中的精英干部。\x02\x03",

            "#10300F进去打个招呼如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x102,
        (
            "#00103F唔……\x01",
            "但对方未必愿意\x01",
            "接待我们吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x104,
        (
            "#12P#00303F唔……\x02\x03",

            "#00301F关于鲁巴彻旧址的事情，\x01",
            "本来还想询问他们一下呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#00008F说起来，黑月之前也想\x01",
            "争取到那片地呢……\x02\x03",

            "#00001F但最后却落入\x01",
            "『深红商会』之手了，\x01",
            "不知他们有什么想法。\x02",
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
            "呵呵，关于此事，\x01",
            "我们当然是深感遗憾啊。\x02",
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

    def lambda_A4FD():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4FD)
    Sleep(50)

    def lambda_A515():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A515)
    Sleep(50)

    def lambda_A52D():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A52D)
    Sleep(50)

    def lambda_A545():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A545)
    Sleep(50)

    def lambda_A55D():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A55D)
    WaitChrThread(0x101, 1)

    #C0485
    ChrTalk(
        0x101,
        "#12P#00005F曹先生……\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x27,
        (
            "#03200F你们好，\x01",
            "特别任务支援科的各位。\x02\x03",

            "#03209F呀～你们来得正好。\x02\x03",

            "其实我有点事情\x01",
            "希望各位帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        "#12P#00005F哎……\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x102,
        "#12P#00105F有事要我们帮忙……？\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x27,
        (
            "#03200F如果方便，\x01",
            "可以进来说话吗？\x02\x03",

            "#03204F呵呵，我当然\x01",
            "没有强迫的意思。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x27, 0x0, 0x1F4)

    def lambda_A68A():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_A68A)
    Sleep(500)

    def lambda_A6A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_A6A7)
    WaitChrThread(0x27, 1)
    OP_9B(0x1, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)

    #C0490
    ChrTalk(
        0x101,
        "#12P#00005F等、等一下……！？\x02",
    )

    CloseMessageWindow()
    OP_97(0x28, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    OP_93(0x28, 0xB4, 0x1F4)
    Sleep(300)

    #C0491
    ChrTalk(
        0x28,
        (
            "……不好意思，\x01",
            "我们遇到点麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x28,
        (
            "如果各位有时间，\x01",
            "还请不吝相助。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x28,
        (
            "门没上锁，不必客气，\x01",
            "请直接进来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x1F4)

    def lambda_A786():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_A786)
    Sleep(500)

    def lambda_A7A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_A7A3)
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
            "#12P#10309F啊哈哈，\x01",
            "这些家伙可真会强人所难啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x109,
        (
            "#6P#10106F我认为瓦吉\x01",
            "完全没资格说别人……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#00101F话说回来，该怎么办呢？\x01",
            "这有可能是个陷阱……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x104,
        (
            "#12P#00301F也许能从他们那里得到什么情报呢，\x01",
            "不然就进去看看吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x101,
        (
            "#00003F说的也对……\x01",
            "（不过我们也很忙，\x01",
            "  没必要勉强自己协助他们。）\x02",
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

    # Function_72_A0B3 end

    def Function_73_A9A7(): pass

    label("Function_73_A9A7")


    def lambda_A9AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_A9AC)

    def lambda_A9BD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_A9BD)
    WaitChrThread(0x27, 1)
    OP_93(0x27, 0xB4, 0x1F4)
    Return()

    # Function_73_A9A7 end

    def Function_74_A9DE(): pass

    label("Function_74_A9DE")


    def lambda_A9E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_A9E3)

    def lambda_A9F4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_A9F4)
    WaitChrThread(0x28, 1)
    OP_95(0x28, 18100, 0, 19500, 2000, 0x0)
    OP_93(0x28, 0xB4, 0x1F4)
    Return()

    # Function_74_A9DE end

    def Function_75_AA29(): pass

    label("Function_75_AA29")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_ABAC")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x104, 19680, 0, 18250, 180)
    SetChrPos(0x109, 18460, 0, 19360, 180)
    SetChrPos(0x105, 19600, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_AB04():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_AB04)

    def lambda_AB1E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB1E)
    Sleep(100)

    def lambda_AB3B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB3B)
    Sleep(50)

    def lambda_AB58():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AB58)
    Sleep(100)

    def lambda_AB75():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AB75)
    Sleep(50)

    def lambda_AB92():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AB92)
    Jump("loc_ADF3")

    label("loc_ABAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_ACD2")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x109, 19680, 0, 18250, 180)
    SetChrPos(0x104, 18460, 0, 19360, 180)
    SetChrPos(0x105, 19600, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_AC2A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_AC2A)

    def lambda_AC44():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AC44)
    Sleep(100)

    def lambda_AC61():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC61)
    Sleep(50)

    def lambda_AC7E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AC7E)
    Sleep(100)

    def lambda_AC9B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC9B)
    Sleep(50)

    def lambda_ACB8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ACB8)
    Jump("loc_ADF3")

    label("loc_ACD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_ADF3")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x105, 19680, 0, 18250, 180)
    SetChrPos(0x104, 19600, 0, 19360, 180)
    SetChrPos(0x109, 18460, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_AD50():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_AD50)

    def lambda_AD6A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD6A)
    Sleep(100)

    def lambda_AD87():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD87)
    Sleep(50)

    def lambda_ADA4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ADA4)
    Sleep(100)

    def lambda_ADC1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ADC1)
    Sleep(50)

    def lambda_ADDE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ADDE)

    label("loc_ADF3")

    OP_68(20080, 600, 15520, 3000)
    MoveCamera(40, 20, 0, 3000)
    OP_6E(560, 3000)
    SetCameraDistance(16390, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_AE32():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_AE32)
    Sleep(50)

    def lambda_AE42():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE42)
    Sleep(300)

    #C0499
    ChrTalk(
        0x1A2,
        (
            "#12P好，那我现在就\x01",
            "开始说明！\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        "#00005F啊……嗯……\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x104,
        (
            "#5P#00306F（那小鬼真会见缝插针啊，\x01",
            "  趁机站到大小姐身边了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x109,
        "#5P#10100F（嗯，而且行动那么自然。）\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x105,
        (
            "#5P#10302F（呵呵，看来他真的\x01",
            "  很喜欢艾莉呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0504
    ChrTalk(
        0x1A2,
        "#12P怎么？你们有什么话想说吗？\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        (
            "#00003F啊，不不，没有的。\x02\x03",

            "#00000F还是请你来\x01",
            "做个说明吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x1A2,
        "#12P呵呵，你真明白事理。\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x1A2,
        (
            "#12P那么，就如刚才所说，\x01",
            "接下来由你们带领我\x01",
            "参观市内各地……\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x1A2,
        (
            "#12P但克洛斯贝尔太过广阔，\x01",
            "如果漫无目的地四处乱逛，\x01",
            "很快就会走累的。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x1A2,
        (
            "#12P因此，我已经事先决定好了\x01",
            "此行的终点。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x109,
        "#5P#10105F终点……？\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x1A2,
        (
            "#12P嗯，那就是\x01",
            "『时代』百货店的楼顶。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x1A2,
        (
            "#12P总之，你们最后只要\x01",
            "把我带到那里，\x01",
            "就算是完成任务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x104,
        "#5P#00300F原来如此，说得真是简单易懂啊。\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x105,
        (
            "#5P#10300F顺便一问，前往百货店的路线\x01",
            "由我们随意决定吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x1A2,
        (
            "#12P不，我可不想在不感兴趣\x01",
            "的地方浪费时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x1A2,
        (
            "#12P从这里出发之后，一定要经由东街，\x01",
            "最终到达百货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x101,
        (
            "#00006F该怎么说呢……\x01",
            "计划制定得真是很完善啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x1A2,
        (
            "#12P呵呵，难得\x01",
            "来此一趟，\x01",
            "自然要制定好基本计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x1A2,
        (
            "#12P不过，除此之外\x01",
            "也没有其它要求了。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x1A2,
        (
            "#12P你们就尽量多带我四处逛逛，\x01",
            "让我和艾莉姐一路上开心点吧。\x02",
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
        "#11P#00109F这个，我也是你的向导啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0522
    ChrTalk(
        0x1A2,
        "#6P才不是！\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x1A2,
        (
            "#6P艾莉姐，请一定要趁此机会，\x01",
            "让自己休息一下哦。\x02",
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
            "#5P#10109F啊哈哈，他好像已经\x01",
            "痴迷得无法自拔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#00006F好，我已经基本明白了……\x02\x03",

            "#00000F按照你的意思，\x01",
            "就只是在街上随便逛一逛嘛。\x02\x03",

            "这样就可以满足了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B46C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_B46C)
    Sleep(50)

    def lambda_B47C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B47C)
    Sleep(300)

    #C0526
    ChrTalk(
        0x104,
        (
            "#5P#00305F就是啊，你难道没有\x01",
            "其它特别想去的地方吗？\x02\x03",

            "#00300F比如说，去看彩虹剧团\x01",
            "的表演……之类的。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x105,
        (
            "#5P#10300F对啊对啊，再比如说\x01",
            "米修拉姆的主题公园。\x02\x03",

            "#10304F不过那里现在正在停业呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x1A2,
        (
            "#12P哼，那种有名的地方，\x01",
            "我当然已经去过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x1A2,
        (
            "#12P在那里的确玩得很开心，\x01",
            "不管再去多少次应该都不会腻，\x01",
            "但我此行的目的并不是游玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x1A2,
        (
            "#12P我必须要对克洛斯贝尔\x01",
            "有更加深刻的了解。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x1A2,
        (
            "#12P因此，不光要了解\x01",
            "那些观光地，也必须要感受到\x01",
            "克洛斯贝尔的真实面貌。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x102,
        "#00105F克洛斯贝尔的真实面貌……\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x101,
        "#00005F竟然考虑得如此深远……\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x104,
        (
            "#5P#00306F哎呀呀，\x01",
            "真是后生可畏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x1A2,
        (
            "#12P总之，你们已经\x01",
            "完全理解了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x1A2,
        (
            "#12P时间宝贵，\x01",
            "立刻出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x101,
        "#00000F明白了，我们赶快出发吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_B7CC")
    OP_29(0x73, 0x1, 0x1)
    OP_93(0x104, 0x0, 0x1F4)
    Sleep(300)

    #C0538
    ChrTalk(
        0x104,
        (
            "#12P#00300F那我们就走在前面，\x01",
            "后方警戒就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x109,
        "#5P#10100F知道了。\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x105,
        "#5P#10300F呵呵，慢走。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    Jump("loc_B911")

    label("loc_B7CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B874")
    OP_29(0x73, 0x1, 0x2)
    OP_93(0x109, 0x0, 0x1F4)
    Sleep(300)

    #C0541
    ChrTalk(
        0x109,
        (
            "#12P#10100F那么，我们就走在前面，\x01",
            "后方警戒就拜托二位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x104,
        "#5P#00300F哦，知道啦。\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x105,
        "#5P#10300F呵呵，慢走。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    Jump("loc_B911")

    label("loc_B874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B911")
    OP_29(0x73, 0x1, 0x3)
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(300)

    #C0544
    ChrTalk(
        0x105,
        (
            "#12P#10300F那我们就先走一步，\x01",
            "后方警戒就交给你们啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x109,
        "#5P#10100F明白。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x104,
        "#5P#00300F嗯，路上小心啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)

    label("loc_B911")

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

    # Function_75_AA29 end

    def Function_76_B95F(): pass

    label("Function_76_B95F")

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

    def lambda_BA90():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_BA90)

    def lambda_BAAA():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BAAA)
    Sleep(50)

    def lambda_BAC7():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BAC7)
    Sleep(50)

    def lambda_BAE4():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BAE4)
    Sleep(50)

    def lambda_BB01():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BB01)
    Sleep(50)

    def lambda_BB1E():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BB1E)
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

    # Function_76_B95F end

    def Function_77_BBFF(): pass

    label("Function_77_BBFF")

    OP_95(0xFE, 19190, -10, 14710, 2000, 0x0)

    def lambda_BC18():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC18)
    Sleep(3000)

    def lambda_BC35():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BC35)
    Return()

    # Function_77_BBFF end

    def Function_78_BC42(): pass

    label("Function_78_BC42")

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

    # Function_78_BC42 end

    def Function_79_BCF2(): pass

    label("Function_79_BCF2")

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

    # Function_79_BCF2 end

    def Function_80_BDA2(): pass

    label("Function_80_BDA2")

    Sound(821, 2, 40, 0)

    #C0547
    ChrTalk(
        0x101,
        "#12P#00000F真是相当热闹啊……\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x102,
        (
            "#6P#00100F据说今天有咪西的\x01",
            "外出表演活动呢。\x02\x03",

            "#00104F在通商会议的召开期间，\x01",
            "米修拉姆暂时停业。\x01",
            "作为弥补，就举办了这种活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x109,
        (
            "#6P#10102F呵呵，缇欧要是在这里，\x01",
            "一定会很感兴趣吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#12P#00002F哈哈，好像正好赶上\x01",
            "咪西的舞蹈表演呢。\x01",
            "机会难得，我们就看看……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0551
    ChrTalk(
        0x101,
        "#12P#00005F哎，那是……！？\x02",
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
        "#6P#11A哇～咪西～！\x02",
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
            "#6P#11A哈哈，那个和咪西一起跳舞的\x01",
            "小哥也很有一套嘛！\x02",
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
            "好，大家一起来吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SＥＮＪＯＹ——咪西☆\x07\x00\x02",
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
    SetChrName("观众们")

    #A0556
    AnonymousTalk(
        0xFF,
        "#4SＥＮＪＯＹ——！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("观众们")

    #A0557
    AnonymousTalk(
        0xFF,
        "#4S咪西————☆\x02",
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

    def lambda_C435():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_C435)
    Sleep(10)

    def lambda_C445():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_C445)
    WaitChrThread(0x34, 1)

    def lambda_C456():
        OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_C456)
    Sleep(10)

    def lambda_C46E():
        OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_C46E)
    WaitChrThread(0x34, 1)

    #A0558
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "奥利维尔与咪西的手\x01",
            "紧紧地握在了一起。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0559
    ChrTalk(
        0x34,
        (
            "#12P#13909F哈哈哈……\x01",
            "名不虚传啊，咪西。\x02\x03",

            "#13902F你的舞蹈很有美感……\x01",
            "真是让人深感敬佩。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，小哥你也\x01",
            "很厉害呀～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "以前学过舞蹈吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x34,
        (
            "#12P#13904F呵呵，社交舞\x01",
            "正是我的兴趣。\x02\x03",

            "我原本只喜欢与\x01",
            "优雅的淑女共舞，\x01",
            "不过和你跳舞也很开心。\x02\x03",

            "#13902F真不愧是克洛斯贝尔的\x01",
            "著名吉祥物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，说得人家都不好意思啦～☆\x02",
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
        "#6P#00006F（他、他到底在干什么……）\x02",
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x104,
        (
            "#6P#00300F（看样子，好像是在\x01",
            "  中途凑过去的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x109,
        (
            "#6P#10106F（穆拉先生还特意交代过，\x01",
            "  希望尽量不要引人注目，\x01",
            "  但实在是不可能了啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C79C():
        OP_9B(0x1, 0xFE, 0xB4, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_C79C)
    Sleep(10)

    def lambda_C7B4():
        OP_9B(0x1, 0xFE, 0xB4, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_C7B4)
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
            "#12P#13905F哦……\x01",
            "似乎有人来迎接我了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x34, 0x0, 0x1F4)
    OP_6F(0x79)

    #C0568
    ChrTalk(
        0x34,
        (
            "#12P#13900F咪西，不好意思，\x01",
            "我这就要告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "哎呀，那真是遗憾～\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，下次一定\x01",
            "要来主题公园玩哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x34,
        (
            "#12P#13902F呵，这个邀请……\x01",
            "我有朝一日定会回应。\x02\x03",

            "#13904F离别让人无比痛苦。\x01",
            "但正因如此，我们之间的羁绊\x01",
            "才会成为无可替代的可贵存在。\x02\x03",

            "#13913F……再见了，好友！\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "拜拜～☆\x02",
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

    def lambda_C9C0():

        label("loc_C9C0")

        TurnDirection(0xFE, 0x34, 500)
        Yield()
        Jump("loc_C9C0")

    QueueWorkItem2(0xF, 2, lambda_C9C0)
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
            "#12P#00011F啊啊……\x01",
            "又、又让他逃掉了！\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x105,
        (
            "#6P#10306F哎呀呀，\x01",
            "他好像很习惯逃跑啊。\x02\x03",

            "#10300F到此地步，\x01",
            "他可能逃去的地点\x01",
            "范围已经越来越小了……\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x102,
        "#12P#00106F总、总之，继续追吧！\x02",
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

    # Function_80_BDA2 end

    def Function_81_CBF7(): pass

    label("Function_81_CBF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_CC13")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_81_CBF7")

    label("loc_CC13")

    Return()

    # Function_81_CBF7 end

    def Function_82_CC14(): pass

    label("Function_82_CC14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_CC30")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(50)
    Jump("Function_82_CC14")

    label("loc_CC30")

    Return()

    # Function_82_CC14 end

    def Function_83_CC31(): pass

    label("Function_83_CC31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_CC4D")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_83_CC31")

    label("loc_CC4D")

    Return()

    # Function_83_CC31 end

    def Function_84_CC4E(): pass

    label("Function_84_CC4E")

    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFF5D8, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFFC18, 0x7D0, 0x0)
    OP_96(0xFE, 0x1FF4, 0xFFFFFD44, 0xFFFFFF06, 0x7D0, 0x0)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x258, 0x7D0, 0x0)
    Return()

    # Function_84_CC4E end

    def Function_85_CCC1(): pass

    label("Function_85_CCC1")

    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x834, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x258, 0x7D0, 0x0)
    OP_96(0xFE, 0x28F0, 0xFFFFFD44, 0xFFFFFF06, 0x7D0, 0x0)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFFC18, 0x7D0, 0x0)
    Return()

    # Function_85_CCC1 end

    def Function_86_CD34(): pass

    label("Function_86_CD34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_CE47")
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
    Jump("Function_86_CD34")

    label("loc_CE47")

    Return()

    # Function_86_CD34 end

    def Function_87_CE48(): pass

    label("Function_87_CE48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_CF5B")
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
    Jump("Function_87_CE48")

    label("loc_CF5B")

    Return()

    # Function_87_CE48 end

    def Function_88_CF5C(): pass

    label("Function_88_CF5C")

    Sound(809, 0, 80, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0xBB8)
    OP_93(0xFE, 0x10E, 0x0)
    Return()

    # Function_88_CF5C end

    def Function_89_CF81(): pass

    label("Function_89_CF81")

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

    # Function_89_CF81 end

    def Function_90_CFCF(): pass

    label("Function_90_CFCF")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D0AE")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    Jump("loc_D0C2")

    label("loc_D0AE")

    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_D0C2")

    OP_0D()

    #C0576
    ChrTalk(
        0x9,
        (
            "来得好，\x01",
            "快来尝尝我做的面吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x101,
        (
            "#00012F那、那个……我们是\x01",
            "特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0578
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

    #C0579
    ChrTalk(
        0x9,
        (
            "哦，是那个啊，\x01",
            "我听说过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x9,
        (
            "你们的运气真好，\x01",
            "可以免费品尝到\x01",
            "我的顶级面条！\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x9,
        (
            "来，吃吧。\x01",
            "这就是天上面『日轮』！\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x105,
        "#10305F唔，这真是……\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x109,
        (
            "#10106F汤的颜色鲜红，\x01",
            "看起来似乎非常辣。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x9,
        "呵呵，别管那么多，先吃了再说吧。\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x9,
        (
            "越过辛辣之后，等待着你们的是\x01",
            "世外桃源般的美味诱惑！\x02",
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
            "#00003F（这态度让人有些不安呢……）\x01",
            "总、总之，还是尝尝看吧。\x02",
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
            "罗伊德等人品尝了天上面『日轮』。\x07\x00\x02",
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
            "#00005F（喝汤）……\x01",
            "的确，并不是一味的辣，\x01",
            "味道相当浓厚呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x102,
        (
            "#00108F嗯，确实很美味……\x02\x03",

            "#00106F不过吃面的时候\x01",
            "总是担心汤会\x01",
            "溅出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x109,
        (
            "#10112F的、的确……\x01",
            "要是把衣服弄脏，可就糟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x9,
        (
            "嗯嗯……女性客人\x01",
            "一般都会有这种感想。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x9,
        (
            "其实，只要能吃到\x01",
            "美味的面条，\x01",
            "溅点汤根本不算什么大问题！\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x104,
        "#00303F……嗯，正是如此。\x02",
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
        "#00205F……兰迪前辈？\x02",
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x104,
        (
            "#00303F在这味道绝妙的鲜辣汤汁的深处，\x01",
            "可以感受到极其浓厚的深邃味道……\x02\x03",

            "还有这沾满浓香汤料，\x01",
            "筋道又卷曲的面条……\x01",
            "只有男人才能体会到其中的妙处。\x02\x03",

            "#00302F不知为何，我好像可以感受到\x01",
            "大叔在面条中倾注的强烈热情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D858")

    #C0596
    ChrTalk(
        0x9,
        (
            "噢噢……是吗！是吗！\x01",
            "看来年轻人之中也有可造之材啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x9,
        (
            "好！就破例把这道面料理的\x01",
            "基础食谱教给你吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x9,
        "一定要努力练习啊！\x02",
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
            "微苦担担面的做法\x07\x00",
            "被教授了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D907")

    label("loc_D858")


    #C0600
    ChrTalk(
        0x9,
        (
            "噢噢……是吗！是吗！\x01",
            "看来年轻人之中也有可造之材啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x9,
        (
            "好，那就再\x01",
            "送你一碗吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x9,
        "请尽情品尝！\x02",
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x190, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_D907")

    TurnDirection(0x104, 0x9, 500)

    #C0604
    ChrTalk(
        0x104,
        "#00309F哦哦，谢啦，大叔！\x02",
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
            "#00009F（兰迪……\x01",
            "  好像很喜欢这道料理呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x105,
        (
            "#10304F（呵呵，那这篇介绍文\x01",
            "  就交给他来写吧。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2, 7)
    SetScenarioFlags(0x172, 2)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_DA79")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DA79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_DA96")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DA96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_DAA9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DAA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_DABC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_DAD9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DAD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_DAEC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DAEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_DB09")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DB09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_DB1C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DB1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_DB39")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DB39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_DB4C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DB4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_DB69")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DB69")

    OP_29(0x80, 0x1, 0x3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC3E")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0607
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DC35")

    #A0608
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

    label("loc_DC35")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_DC3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD08")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0609
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

    #A0610
    AnonymousTalk(
        0x101,
        (
            "#00004F这样一来，已经找到\x01",
            "所有人喜欢的美食了啊。\x02\x03",

            "#00000F取材工作已经足够了，\x01",
            "马上去通讯社报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_DD08")

    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DD84")
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
    Jump("loc_DDC6")

    label("loc_DD84")

    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -13200, 0, 11500, 90)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -52470, 2000, 21150, 90)
    BeginChrThread(0xA, 0, 0, 2)

    label("loc_DDC6")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10470, 0, 11840, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_90_CFCF end

    def Function_91_DDF2(): pass

    label("Function_91_DDF2")

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

    def lambda_DF2C():
        OP_9B(0x0, 0x31, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_DF2C)
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
        "克莱德，让你久等啦。\x02",
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
        "我已经把东西带来了。\x02",
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
            "公文包\x07\x00",
            "交给了克莱德。\x02",
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
        "谢谢，您辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x31,
        "那么……情况如何了？\x02",
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x30,
        (
            "嗯，她似乎\x01",
            "很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x30,
        (
            "接下来，就要在\x01",
            "『诺艾·布朗』彻底搞定！\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x31,
        "哈哈，不错嘛。\x02",
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x31,
        (
            "……哦，水上巴士\x01",
            "马上就要来了啊。\x01",
            "我得赶快去做好准备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x31,
        (
            "总之，接下来就看你的了。\x01",
            "只要签了这次的合同，\x01",
            "你首席的地位就彻底稳固了。\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x30,
        "是的，交给我吧！！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x31, 1, 0, 92)
    OP_68(22840, 0, -4880, 3000)
    Sleep(1500)

    def lambda_E1BA():
        OP_9B(0x0, 0x30, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_E1BA)
    WaitChrThread(0x30, 1)

    def lambda_E1D3():

        label("loc_E1D3")

        TurnDirection(0xFE, 0x31, 500)
        Yield()
        Jump("loc_E1D3")

    QueueWorkItem2(0x30, 1, lambda_E1D3)
    Sleep(4000)
    EndChrThread(0x30, 0x1)

    #C0622
    ChrTalk(
        0x30,
        "好……加油吧！\x02",
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x8, 0x9, 0xFA, 0x6)
    Sound(27, 0, 100, 0)

    def lambda_E218():
        OP_9B(0x0, 0x30, 0x10E, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_E218)
    Sleep(2000)
    Fade(500)
    OP_68(-2520, 0, 26110, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31670, 0)
    SetChrPos(0x30, 1100, 2000, 23760, 270)
    OP_63(0x30, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)

    def lambda_E28C():
        OP_9B(0x0, 0x30, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_E28C)
    WaitChrThread(0x30, 1)

    def lambda_E2A5():
        OP_93(0x30, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_E2A5)
    WaitChrThread(0x30, 1)
    OP_71(0xA, 0xF1, 0x10E, 0x1, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0xA)
    OP_64(0x30)

    def lambda_E2CE():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_E2CE)

    def lambda_E2E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_E2E3)
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

    def lambda_E396():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_E396)
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
            "#00305F兴致勃勃地\x01",
            "走了啊。\x02\x03",

            "#00303F他似乎和副局长的夫人\x01",
            "相约在『诺艾·布朗』\x01",
            "见面……\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，要怎么办呢？\x01",
            "再怎么说，也不能\x01",
            "继续跟踪他们了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x101,
        (
            "#00003F……和艾莉她们联络一下，\x01",
            "暂时返回警察总部吧。\x02\x03",

            "#00001F那个名叫克莱德的男人……\x01",
            "我想我已经知道他的真实身份了。\x02",
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

    # Function_91_DDF2 end

    def Function_92_E552(): pass

    label("Function_92_E552")

    ClearChrFlags(0x31, 0x4)
    OP_9B(0x0, 0x31, 0x10E, 0xFA0, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x10E, 0x1770, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x10E, 0x1B58, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x5A, 0x1B58, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0x31, 0x4)
    Return()

    # Function_92_E552 end

    def Function_93_E5A8(): pass

    label("Function_93_E5A8")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E85A")
    SetScenarioFlags(0x176, 2)

    #C0626
    ChrTalk(
        0x24,
        (
            "前往米修拉姆的水上巴士\x01",
            "即将出发～\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x24,
        (
            "需要搭乘的客人\x01",
            "请尽早上船～！\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x101,
        (
            "#6P#00000F对了……\x01",
            "主题公园那边\x01",
            "还有支援请求呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x102,
        (
            "#6P#00100F具体内容好像是\x01",
            "帮助咪西。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x109,
        "#6P#10103F嗯……到底是什么工作呢？\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x103,
        (
            "#12P#00203F…………………………\x01",
            "总之，以最快速度\x01",
            "赶往现场吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x104,
        (
            "#6P#00309F哈哈，阿缇可真是\x01",
            "干劲十足啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，总有种\x01",
            "这个任务会很有趣的预感呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x101,
        (
            "#6P#00003F（前往米修拉姆之后，\x01",
            "  如果没有什么意外情况，\x01",
            "  我们就要接受委托了。）\x02\x03",

            "（要出发吗……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E85A")

    Call(0, 94)
    Return()

    # Function_93_E5A8 end

    def Function_94_E85E(): pass

    label("Function_94_E85E")

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
            "前往主题公园\x01",      # 0
            "放弃\x01",              # 1
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
        (0, "loc_E8C0"),
        (1, "loc_EB05"),
        (SWITCH_DEFAULT, "loc_EBD8"),
    )


    label("loc_E8C0")


    #C0635
    ChrTalk(
        0x101,
        (
            "#6P#00000F那我们就\x01",
            "赶快上船吧。\x02",
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

    def lambda_EA43():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_EA43)
    WaitChrThread(0x2E, 1)

    def lambda_EA61():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_EA61)
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
            "罗伊德等人乘坐水上巴士\x01",
            "前往米修拉姆……\x02\x03",

            "来到了主题公园的门前，\x01",
            "与委托人会面。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_EBD8")

    label("loc_EB05")


    #C0637
    ChrTalk(
        0x101,
        "#6P#00003F……还是稍后再过去吧。\x02",
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
            "准备前往米修拉姆\x01",
            "接受委托时，\x01",
            "请调查水上巴士的时刻表。\x07\x00\x02",
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
    Jump("loc_EBD8")

    label("loc_EBD8")

    Return()

    # Function_94_E85E end

    def Function_95_EBD9(): pass

    label("Function_95_EBD9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, 38840, -2500, -460, 270)
    OP_69(0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_95_EBD9 end

    def Function_96_EC07(): pass

    label("Function_96_EC07")

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

    def lambda_ED3C():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_ED3C)
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

    def lambda_EDED():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_EDED)
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

    def lambda_EFCA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EFCA)
    Sleep(50)

    def lambda_EFDA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EFDA)
    Sleep(50)

    def lambda_EFEA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EFEA)
    Sleep(50)

    def lambda_EFFA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EFFA)
    Sleep(50)

    def lambda_F00A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F00A)
    Sleep(300)

    #C0640
    ChrTalk(
        0x104,
        (
            "#00305F……喂，罗伊德。\x01",
            "阿缇到底\x01",
            "怎么了？\x02\x03",

            "从我们会合开始，\x01",
            "到乘坐水上巴士的这一路，\x01",
            "她一直都是那种样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x102,
        (
            "#00108F是啊……\x01",
            "一直在默默发呆，\x01",
            "茫然眺望着远方……\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x105,
        (
            "#10300F心情似乎\x01",
            "很失落呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x101,
        (
            "#00000F唔、唔……\x01",
            "该怎么说才好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x109,
        (
            "#10105F那个……缇欧，\x01",
            "你是不是哪里不舒服？\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x103,
        (
            "#00203F………………不。\x01",
            "我没事。\x02\x03",

            "#00202F只是脑子里有点乱……\x01",
            "需要平复一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(1000)

    #C0646
    ChrTalk(
        0x103,
        (
            "#00208F……人就是这样\x01",
            "慢慢长大的啊……\x02",
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
            "任务【主题公园的兼职】\x07\x00",
            "完成！\x02",
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

    # Function_96_EC07 end

    def Function_97_F330(): pass

    label("Function_97_F330")

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

    # Function_97_F330 end

    def Function_98_F3C2(): pass

    label("Function_98_F3C2")


    def lambda_F3C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F3C7)

    def lambda_F3D8():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F3D8)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 37640, -2500, 320, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_98_F3C2 end

    def Function_99_F40D(): pass

    label("Function_99_F40D")


    def lambda_F412():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F412)

    def lambda_F423():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F423)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 37640, -2500, -1280, 2000, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Return()

    # Function_99_F40D end

    def Function_100_F458(): pass

    label("Function_100_F458")


    def lambda_F45D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F45D)

    def lambda_F46E():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F46E)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 38890, -2500, 1500, 2000, 0x0)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_100_F458 end

    def Function_101_F4A3(): pass

    label("Function_101_F4A3")


    def lambda_F4A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F4A8)

    def lambda_F4B9():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F4B9)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 39690, -2500, -1720, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_101_F4A3 end

    def Function_102_F4EE(): pass

    label("Function_102_F4EE")


    def lambda_F4F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F4F3)

    def lambda_F504():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F504)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 40640, -2500, 1110, 2000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_102_F4EE end

    def Function_103_F539(): pass

    label("Function_103_F539")


    def lambda_F53E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F53E)

    def lambda_F54F():
        OP_95(0xFE, 41760, -2500, -1910, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F54F)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 41340, -2500, -150, 1500, 0x0)
    OP_93(0x103, 0x10E, 0x1F4)
    Return()

    # Function_103_F539 end

    def Function_104_F584(): pass

    label("Function_104_F584")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F638")

    #C0648
    ChrTalk(
        0x1A2,
        "这边是东街吗？\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        "#00000F不、不是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0650
    ChrTalk(
        0x1A2,
        "所以啊。\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x1A2,
        (
            "……我之前不是说过吗，\x01",
            "要经过东街前进。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x101,
        "#00006F是的……真抱歉。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_F679")

    label("loc_F638")


    #C0653
    ChrTalk(
        0x1A2,
        (
            "喂，不要到处乱转，\x01",
            "我可不想绕远路。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x1A2,
        "赶快带我往东街走。\x02",
    )

    CloseMessageWindow()

    label("loc_F679")

    SetChrPos(0x0, -28110, 2000, 23520, 90)
    EventEnd(0x4)
    Return()

    # Function_104_F584 end

    def Function_105_F68D(): pass

    label("Function_105_F68D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F723")
    EventBegin(0x1)

    #C0655
    ChrTalk(
        0x101,
        (
            "#00003F（前往米修拉姆之后，\x01",
            "  如果没有什么意外情况，\x01",
            "  我们就要接受委托了。）\x02\x03",

            "（要出发吗……？）\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 94)
    Jump("loc_F7B4")

    label("loc_F723")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0656
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "前往『米修拉姆』的水上巴士的时刻表\x01\x01",
            "※米修拉姆引以为傲的主题公园\x01",
            "  『奇幻乐园』开园中！\x01",
            "  请尽情享受快乐的时光！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)

    label("loc_F7B4")

    Return()

    # Function_105_F68D end

    def Function_106_F7B5(): pass

    label("Function_106_F7B5")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0657
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　『羽扇河·第一灯塔』\x01\x01",
            "无关人员禁止入内。\x01",
            "　　　　　～克洛斯贝尔市～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_106_F7B5 end

    SaveToFile()

Try(main)
