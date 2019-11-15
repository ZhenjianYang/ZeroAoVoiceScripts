from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1200.bin",                # FileName
        "c1200",                    # MapName
        "c1200",                    # Location
        0x001A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 26, 0, 10, 0, 11],
    )

    BuildStringList((
        "c1200",                  # 0
        "库妮娅",                 # 1
        "奥赛尔",                 # 2
        "毕肖普",                 # 3
        "奎因老人",               # 4
        "亚米萨",                 # 5
        "游客",                   # 6
        "游客",                   # 7
        "游客",                   # 8
        "游客",                   # 9
        "游客",                   # 10
        "游客",                   # 11
        "市民",                   # 12
        "市民",                   # 13
        "市民",                   # 14
        "市民",                   # 15
        "市民",                   # 16
        "水上巴士向导",           # 17
        "黑月成员",               # 18
        "格蕾丝",                 # 19
        "雷因兹",                 # 20
        "罗伯兹主任",             # 21
        "游击士斯克特",           # 22
        "帕尔",                   # 23
        "尼克鲁",                 # 24
        "塞利娜",                 # 25
        "弗兰茨巡警",             # 26
        "黑月成员",               # 27
        "黑月成员",               # 28
        "刘",                     # 29
        "达德利搜查官",           # 30
        "银",                     # 31
        "达德利的车",             # 32
        "中央广场",               # 33
        "西街",                   # 34
        "行政区",                 # 35
        "住宅街",                 # 36
        "欢乐街",                 # 37
        "东街",                   # 38
        "旧城区",                 # 39
        "港湾区",                 # 40
        "ＩＢＣ",                 # 41
        "站前街道",               # 42
        "后巷",                   # 43
        "乌尔斯拉间道",           # 44
        "东克洛斯贝尔街道",       # 45
        "西克洛斯贝尔街道",       # 46
        "玛因兹山道",             # 47
    ))

    AddCharChip((
        "chr/ch22100.itc",                   # 00
        "chr/ch25200.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "apl/ch50168.itc",                   # 03
        "chr/ch21500.itc",                   # 04
        "chr/ch29300.itc",                   # 05
        "chr/ch31500.itc",                   # 06
        "chr/ch28100.itc",                   # 07
        "chr/ch06000.itc",                   # 08
        "chr/ch30000.itc",                   # 09
        "chr/ch21102.itc",                   # 0A
        "chr/ch20600.itc",                   # 0B
        "chr/ch20400.itc",                   # 0C
        "chr/ch21900.itc",                   # 0D
        "chr/ch20700.itc",                   # 0E
        "chr/ch20800.itc",                   # 0F
        "chr/ch26600.itc",                   # 10
        "chr/ch27200.itc",                   # 11
        "chr/ch26600.itc",                   # 12
        "chr/ch28900.itc",                   # 13
        "chr/ch29100.itc",                   # 14
        "chr/ch31400.itc",                   # 15
        "chr/ch24000.itc",                   # 16
        "chr/ch21300.itc",                   # 17
        "chr/ch24400.itc",                   # 18
        "chr/ch34200.itc",                   # 19
        "chr/ch21100.itc",                   # 1A
    ))

    DeclNpc(-13199,  0,       11500,   90,   257,  0x0, 0,   0,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(-10470,  0,       13340,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-52470,  2000,    21149,   90,   257,  0x0, 0,   2,   0,   0,   2,   0,   15,  255,  0)
    DeclNpc(39669,   -2500,   -19379,  180,  277,  0x0, 0,   3,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(38439,   -2490,   -18079,  135,  261,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(7469,    -699,    3029,    180,  453,  0x0, 0,   10,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(9489,    -699,    129,     64,   389,  0x0, 0,   11,  0,   0,   9,   0,   25,  255,  0)
    DeclNpc(42000,   -2500,   0,       90,   389,  0x0, 0,   12,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(40000,   -2500,   0,       180,  389,  0x0, 0,   13,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(40000,   -2500,   -1250,   90,   389,  0x0, 0,   14,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(38000,   -2500,   0,       90,   389,  0x0, 0,   15,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(17629,   0,       -2130,   0,    389,  0x0, 0,   23,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(9409,    0,       13489,   90,   389,  0x0, 0,   12,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(22500,   0,       1019,    0,    389,  0x0, 0,   24,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(2900,    0,       9310,    90,   405,  0x0, 0,   25,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(3730,    0,       8510,    45,   389,  0x0, 0,   26,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(42450,   -2500,   2329,    235,  389,  0x0, 0,   16,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(18989,   9,       19649,   180,  389,  0x0, 0,   6,   0,   0,   0,   0,   35,  255,  0)
    DeclNpc(3069,    -699,    1110,    180,  389,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(21620,   0,       14909,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-9189,   -9,      12270,   315,  389,  0x0, 0,   5,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(3259,    -699,    1440,    90,   405,  0x0, 0,   17,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(5159,    -699,    1639,    270,  405,  0x0, 0,   18,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-18000,  0,       -5750,   90,   389,  0x0, 0,   19,  0,   0,   3,   0,   38,  255,  0)
    DeclNpc(-16979,  0,       -13449,  45,   389,  0x0, 0,   20,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(19100,   0,       16600,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   37,  255,  0)
    DeclNpc(22399,   0,       19500,   0,    453,  0x0, 0,   6,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(24000,   0,       17899,   45,   453,  0x0, 0,   6,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(19879,   0,       19629,   225,  389,  0x0, 0,   21,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 54,  21.0,                  5.5,                   -1.5,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.4000000953674316,   -1.8333333730697632,   0.30000001192092896,   1.0])
    DeclEvent(0x0000, 0, 54,  13.5,                  11.5,                  -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -4.5,                  -1.149999976158142,    0.20000000298023224,   1.0])

    DeclActor(19200,   250,     20500,   2000,    19200,   1250,    20500,   0x007C, 0,  42, 0x0000)
    DeclActor(68620,   -2500,   15400,   1200,    68040,   -3500,   11820,   0x007C, 0,  41, 0x0000)
    DeclActor(34000,   -2500,   3400,    1500,    34000,   -1500,   3400,    0x007C, 0,  57, 0x0000)
    DeclActor(77440,   -2500,   19770,   1200,    77440,   -1000,   19770,   0x007C, 0,  58, 0x0000)

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
    PlaceName(-108.4000015258789, 0.0, -100.87000274658203, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_914",          # 00, 0
        "Function_1_9CC",          # 01, 1
        "Function_2_A7D",          # 02, 2
        "Function_3_BB7",          # 03, 3
        "Function_4_C68",          # 04, 4
        "Function_5_C93",          # 05, 5
        "Function_6_CBE",          # 06, 6
        "Function_7_CFE",          # 07, 7
        "Function_8_D3E",          # 08, 8
        "Function_9_D69",          # 09, 9
        "Function_10_D94",         # 0A, 10
        "Function_11_129E",        # 0B, 11
        "Function_12_1570",        # 0C, 12
        "Function_13_2205",        # 0D, 13
        "Function_14_3766",        # 0E, 14
        "Function_15_3849",        # 0F, 15
        "Function_16_3EB3",        # 10, 16
        "Function_17_489C",        # 11, 17
        "Function_18_4D8D",        # 12, 18
        "Function_19_4E48",        # 13, 19
        "Function_20_4F1A",        # 14, 20
        "Function_21_51AA",        # 15, 21
        "Function_22_55BF",        # 16, 22
        "Function_23_582F",        # 17, 23
        "Function_24_5886",        # 18, 24
        "Function_25_5A61",        # 19, 25
        "Function_26_5AD5",        # 1A, 26
        "Function_27_5BC1",        # 1B, 27
        "Function_28_5C13",        # 1C, 28
        "Function_29_5C4C",        # 1D, 29
        "Function_30_5C92",        # 1E, 30
        "Function_31_5CE6",        # 1F, 31
        "Function_32_5D52",        # 20, 32
        "Function_33_5E32",        # 21, 33
        "Function_34_5E7E",        # 22, 34
        "Function_35_5ED5",        # 23, 35
        "Function_36_5F46",        # 24, 36
        "Function_37_611D",        # 25, 37
        "Function_38_63B3",        # 26, 38
        "Function_39_666A",        # 27, 39
        "Function_40_682A",        # 28, 40
        "Function_41_686E",        # 29, 41
        "Function_42_6936",        # 2A, 42
        "Function_43_6A67",        # 2B, 43
        "Function_44_6CF2",        # 2C, 44
        "Function_45_7162",        # 2D, 45
        "Function_46_7780",        # 2E, 46
        "Function_47_A12B",        # 2F, 47
        "Function_48_A168",        # 30, 48
        "Function_49_A1AF",        # 31, 49
        "Function_50_A1F6",        # 32, 50
        "Function_51_A23D",        # 33, 51
        "Function_52_A284",        # 34, 52
        "Function_53_A42B",        # 35, 53
        "Function_54_A872",        # 36, 54
        "Function_55_AD5C",        # 37, 55
        "Function_56_B899",        # 38, 56
        "Function_57_BCED",        # 39, 57
        "Function_58_BD9A",        # 3A, 58
    ))


    def Function_0_914(): pass

    label("Function_0_914")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_954"),
        (1, "loc_960"),
        (2, "loc_96C"),
        (3, "loc_978"),
        (4, "loc_984"),
        (5, "loc_990"),
        (6, "loc_99C"),
        (SWITCH_DEFAULT, "loc_9A8"),
    )


    label("loc_954")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_960")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_96C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_978")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_984")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_990")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_99C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9CB")

    Return()

    # Function_0_914 end

    def Function_1_9CC(): pass

    label("Function_1_9CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7C")
    OP_95(0xFE, 14600, 0, 11500, 1000, 0x0)
    OP_95(0xFE, 20200, 0, 8200, 1000, 0x0)
    OP_95(0xFE, 20200, 0, -6200, 1000, 0x0)
    OP_95(0xFE, 14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -20000, 0, -6400, 1000, 0x0)
    OP_95(0xFE, -20000, 0, 6000, 1000, 0x0)
    OP_95(0xFE, -13200, 0, 11500, 1000, 0x0)
    Jump("Function_1_9CC")

    label("loc_A7C")

    Return()

    # Function_1_9CC end

    def Function_2_A7D(): pass

    label("Function_2_A7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB6")
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
    Jump("Function_2_A7D")

    label("loc_BB6")

    Return()

    # Function_2_A7D end

    def Function_3_BB7(): pass

    label("Function_3_BB7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C67")
    OP_95(0xFE, -13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 18000, 0, -4300, 4000, 0x0)
    OP_95(0xFE, 18000, 0, 7040, 4000, 0x0)
    OP_95(0xFE, 13000, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -12700, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -18000, 0, 5200, 4000, 0x0)
    OP_95(0xFE, -18000, 0, -5750, 4000, 0x0)
    Jump("Function_3_BB7")

    label("loc_C67")

    Return()

    # Function_3_BB7 end

    def Function_4_C68(): pass

    label("Function_4_C68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C92")
    OP_94(0xFE, 0x708, 0xF32, 0xFFFFF9A2, 0xC3A, 0x3E8)
    Sleep(300)
    Jump("Function_4_C68")

    label("loc_C92")

    Return()

    # Function_4_C68 end

    def Function_5_C93(): pass

    label("Function_5_C93")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_5_C93 end

    def Function_6_CBE(): pass

    label("Function_6_CBE")

    OP_93(0xFE, 0xB4, 0x2BC)
    OP_93(0xFE, 0x5A, 0x2BC)
    OP_93(0xFE, 0x0, 0x2BC)
    OP_93(0xFE, 0x10E, 0x2BC)
    OP_93(0xFE, 0xB4, 0x2BC)
    OP_93(0xFE, 0x5A, 0x2BC)
    OP_93(0xFE, 0x0, 0x2BC)
    OP_93(0xFE, 0x10E, 0x2BC)
    OP_93(0xFE, 0xB4, 0x2BC)
    Return()

    # Function_6_CBE end

    def Function_7_CFE(): pass

    label("Function_7_CFE")

    OP_93(0xFE, 0x10E, 0x398)
    OP_93(0xFE, 0x0, 0x398)
    OP_93(0xFE, 0x5A, 0x398)
    OP_93(0xFE, 0xB4, 0x398)
    OP_93(0xFE, 0x10E, 0x398)
    OP_93(0xFE, 0x0, 0x398)
    OP_93(0xFE, 0x5A, 0x398)
    OP_93(0xFE, 0xB4, 0x398)
    OP_93(0xFE, 0x13B, 0x398)
    Return()

    # Function_7_CFE end

    def Function_8_D3E(): pass

    label("Function_8_D3E")

    OP_93(0xFE, 0x0, 0x28A)
    OP_93(0xFE, 0x5A, 0x28A)
    OP_93(0xFE, 0xB4, 0x28A)
    OP_93(0xFE, 0x10E, 0x28A)
    OP_93(0xFE, 0x0, 0x28A)
    OP_93(0xFE, 0x5A, 0x28A)
    Return()

    # Function_8_D3E end

    def Function_9_D69(): pass

    label("Function_9_D69")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D93")
    OP_94(0xFE, 0x1F22, 0x546, 0x7D9, 0xFFFFF7FE, 0x3E8)
    Sleep(300)
    Jump("Function_9_D69")

    label("loc_D93")

    Return()

    # Function_9_D69 end

    def Function_10_D94(): pass

    label("Function_10_D94")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC6")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E56")
    SetChrPos(0x0, 4870, 3350, 31570, 180)
    SetChrPos(0x1, 4870, 3350, 31570, 180)
    SetChrPos(0x2, 4870, 3350, 31570, 180)
    SetChrPos(0x3, 4870, 3350, 31570, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E29")
    SetChrPos(0x4, 4870, 3350, 31570, 180)
    SetChrPos(0x5, 4870, 3350, 31570, 180)
    Jump("loc_E48")

    label("loc_E29")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E48")
    SetChrPos(0x4, 4870, 3350, 31570, 180)

    label("loc_E48")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC6")

    label("loc_E56")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F25")
    SetChrPos(0x0, -28110, 2000, 23520, 90)
    SetChrPos(0x1, -28110, 2000, 23520, 90)
    SetChrPos(0x2, -28110, 2000, 23520, 90)
    SetChrPos(0x3, -28110, 2000, 23520, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF8")
    SetChrPos(0x4, -28110, 2000, 23520, 90)
    SetChrPos(0x5, -28110, 2000, 23520, 90)
    Jump("loc_F17")

    label("loc_EF8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F17")
    SetChrPos(0x4, -28110, 2000, 23520, 90)

    label("loc_F17")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC6")

    label("loc_F25")

    SetChrPos(0x0, -19600, 0, -27950, 0)
    SetChrPos(0x1, -19600, 0, -27950, 0)
    SetChrPos(0x2, -19600, 0, -27950, 0)
    SetChrPos(0x3, -19600, 0, -27950, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9E")
    SetChrPos(0x4, -19600, 0, -27950, 0)
    SetChrPos(0x5, -19600, 0, -27950, 0)
    Jump("loc_FBD")

    label("loc_F9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FBD")
    SetChrPos(0x4, -19600, 0, -27950, 0)

    label("loc_FBD")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC6")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_FE3")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 46)
    Jump("loc_101A")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_FF7")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 52)
    Jump("loc_101A")

    label("loc_FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_100B")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 53)
    Jump("loc_101A")

    label("loc_100B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_101A")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 55)

    label("loc_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_105B")
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 2870, -700, -1190, 0)
    ClearChrFlags(0x1A, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1056")
    ClearChrFlags(0x1C, 0x80)
    OP_93(0x9, 0x87, 0x0)

    label("loc_1056")

    Jump("loc_1286")

    label("loc_105B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1073")
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_1286")

    label("loc_1073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1110")
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x8, 7270, 200, 16400, 135)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xB, 17010, 0, -6810, 0)
    SetChrPos(0xC, 15600, 0, -7280, 45)
    SetChrChipByIndex(0xB, 0x16)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F1")
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)

    label("loc_10F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_110B")
    SetChrPos(0x21, 20500, 0, 15200, 180)

    label("loc_110B")

    Jump("loc_1286")

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1123")
    SetChrFlags(0xC, 0x10)
    Jump("loc_1286")

    label("loc_1123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_113B")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_1286")

    label("loc_113B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1149")
    Jump("loc_1286")

    label("loc_1149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_115C")
    SetChrFlags(0xC, 0x10)
    Jump("loc_1286")

    label("loc_115C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1182")
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_117D")
    ClearChrFlags(0x24, 0x80)

    label("loc_117D")

    Jump("loc_1286")

    label("loc_1182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1195")
    SetChrFlags(0xC, 0x80)
    Jump("loc_1286")

    label("loc_1195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_11CE")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 800, -700, 3300, 270)
    BeginChrThread(0x20, 0, 0, 4)
    Jump("loc_1286")

    label("loc_11CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1204")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_1286")

    label("loc_1204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1232")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 33460, -2500, 1730, 0)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_1286")

    label("loc_1232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_125E")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    Jump("loc_1286")

    label("loc_125E")

    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)

    label("loc_1286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129D")
    SetMapFlags(0x10000000)
    Event(0, 44)

    label("loc_129D")

    Return()

    # Function_10_D94 end

    def Function_11_129E(): pass

    label("Function_11_129E")

    OP_65(0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12C4")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_12C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12DC")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_12DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FD")
    SetMapObjFrame(0xFF, "kurotuki01", 0x0, 0x1)
    Jump("loc_130F")

    label("loc_12FD")

    SetMapObjFrame(0xFF, "kurotuki00", 0x0, 0x1)

    label("loc_130F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1327")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_1327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133F")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_133F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_END)), "loc_1352")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_1352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136A")
    OP_65(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_136A")

    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13C1")
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_71(0x6, 0x12C, 0x12C, 0x0, 0x0)

    label("loc_13C1")

    SetMapObjFlags(0x5, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DB")
    ClearMapObjFlags(0x5, 0x4)

    label("loc_13DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x32, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x37, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142C")
    OP_65(0x1, 0x1)

    label("loc_142C")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 68040, -3500, 11820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E1(0x13DE4, 0x0, 0x71E8)
    OP_E1(0x13C54, 0x0, 0xD1B0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14ED")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_154E")

    label("loc_14ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1529")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_154E")

    label("loc_1529")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_154E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156A")
    Jump("loc_156F")

    label("loc_156A")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_156F")

    Return()

    # Function_11_129E end

    def Function_12_1570(): pass

    label("Function_12_1570")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159D")
    TurnDirection(0x0, 0x8, 0)
    OP_4B(0x8, 0xFF)
    Call(0, 56)
    Return()

    label("loc_159D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1619")

    #C0001
    ChrTalk(
        0xFE,
        (
            "竟然把车票弄丢，\x01",
            "真是位粗心的游客呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "一想到他正在满城寻找，\x01",
            "就觉得很可怜啊。\x01",
            "快点给他送过去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_1619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_16DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1667")

    #C0003
    ChrTalk(
        0xFE,
        (
            "自治州议会\x01",
            "终于结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "真期待预算的发表。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16DA")

    label("loc_1667")


    #C0005
    ChrTalk(
        0xFE,
        (
            "听说自治州议会\x01",
            "终于结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "呼……真是开了很久啊。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "不知道麦克道尔市长\x01",
            "最后是否为我们努力了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_16DA")

    Jump("loc_2201")

    label("loc_16DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1771")

    #C0008
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔时代周刊的记者\x01",
            "采访了我。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "是个感觉有些娃娃脸的好青年……⊥\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "虽然男子气概还差了那么一点，\x01",
            "不过应该很有前途。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_1771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_17D0")

    #C0011
    ChrTalk(
        0xFE,
        "今天我本来想去散步……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "但竟然有警察在守卫着，\x01",
            "气氛还真是有些紧张呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_17D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1909")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1858")

    #C0013
    ChrTalk(
        0xFE,
        (
            "哈尔特曼议长\x01",
            "几乎不在媒体上露面，\x01",
            "是那种喜欢在幕后指挥的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "可是，作为市民，\x01",
            "还是想多了解他一点呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1904")

    label("loc_1858")


    #C0015
    ChrTalk(
        0xFE,
        (
            "哈尔特曼议长那沉着的架势，\x01",
            "给人以滴水不漏的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "他几乎不曾出现在媒体上呢。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "但有传言说，\x01",
            "他准备参加这次市长选举……\x01",
            "对市民来说，他是个值得关注的人物吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1904")

    Jump("loc_2201")

    label("loc_1909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_197A")

    #C0018
    ChrTalk(
        0xFE,
        (
            "米修拉姆的商店街\x01",
            "好像发生了事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "但是，既没有看到新闻，\x01",
            "也听不到什么传言呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A13")

    label("loc_197A")


    #C0020
    ChrTalk(
        0xFE,
        (
            "我听小道消息说，\x01",
            "米修拉姆的商店街\x01",
            "好像发生了事件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，\x01",
            "竟然出现了那种大乱子。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "但奇怪的是……\x01",
            "新闻中却没有进行任何报道。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1A13")

    Jump("loc_2201")

    label("loc_1A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A54")

    #C0023
    ChrTalk(
        0xFE,
        (
            "今年会有什么样\x01",
            "的娱乐表演呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB0")

    label("loc_1A54")


    #C0024
    ChrTalk(
        0xFE,
        "从下个月开始，就是纪念庆典了……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "今年的庆典好像要持续五天，\x01",
            "必须安排好日程啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1AB0")

    Jump("loc_2201")

    label("loc_1AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1B94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1AFF")

    #C0026
    ChrTalk(
        0xFE,
        (
            "唯一的遗憾就是，\x01",
            "只能从杂志上欣赏他的照片……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8F")

    label("loc_1AFF")


    #C0027
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ的库罗伊斯总裁\x01",
            "只有四十多岁呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "在年轻时就已历任要职，\x01",
            "是个超级精干的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "再加上又帅又成熟……！\x01",
            "实在是个完美的男人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1B8F")

    Jump("loc_2201")

    label("loc_1B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1CCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1C14")

    #C0030
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的男演员\x01",
            "各有各的风格。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "虽然我都很喜欢……\x01",
            "但一定要选一个的话，\x01",
            "我还是首选尤金大人哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_1C14")


    #C0032
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的那两位\x01",
            "男演员都很棒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "『金发王子』尤金大人和\x01",
            "『沉默贵公子』缇奥多尔大人。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "呵呵，要让我选一个的话，\x01",
            "我还是会选尤金大人吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "因为他是王子殿下嘛。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1CC8")

    Jump("loc_2201")

    label("loc_1CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1DC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1D3E")

    #C0036
    ChrTalk(
        0xFE,
        (
            "最近，在这附近\x01",
            "能看到市长的首席秘书。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "……他是个很不错的人，\x01",
            "还会对我打招呼呢⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC1")

    label("loc_1D3E")


    #C0038
    ChrTalk(
        0xFE,
        (
            "最近，在这附近\x01",
            "能看到一个\x01",
            "衣着讲究的青年。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "那个人……好像是\x01",
            "市长的首席秘书吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "他对工作很热心。\x01",
            "还会对我打招呼。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1DC1")

    Jump("loc_2201")

    label("loc_1DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E55")

    #C0041
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的政治局面，\x01",
            "有点乱糟糟的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "但是我觉得，\x01",
            "至少市长还是可以信赖的。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "我是市长的支持者呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1EA9")

    label("loc_1E55")


    #C0044
    ChrTalk(
        0xFE,
        (
            "市长看起来是个意志坚定的人，\x01",
            "给人的感觉很好。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "至少对市长，\x01",
            "我还是支持的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA9")

    Jump("loc_2201")

    label("loc_1EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1F23")

    #C0046
    ChrTalk(
        0xFE,
        (
            "最近，在这个公园里运动\x01",
            "的人好像多起来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "难道是正在兴起\x01",
            "什么热潮吗。\x01",
            "……我也去看看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_1F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1FCE")

    #C0048
    ChrTalk(
        0xFE,
        (
            "在米修拉姆的主题公园里，\x01",
            "有一个很大很大的摩天轮。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "除此之外，\x01",
            "还有过山车和鬼屋之类的游戏设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "我好想坐一次过山车看看啊。\x01",
            "还一次都没有坐过呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_1FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2111")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2051")

    #C0051
    ChrTalk(
        0xFE,
        (
            "最近，在公园的附近，\x01",
            "好像成立了一家东方风格的公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "几乎看不到他们的职员，\x01",
            "到底是做什么的公司呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210C")

    label("loc_2051")


    #C0053
    ChrTalk(
        0xFE,
        (
            "最近，在公园的附近，\x01",
            "好像成立了一家东方风格的公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "他们那栋东方风格的红色建筑\x01",
            "看上去还挺可爱的，\x01",
            "不知什么时候就已经建好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "……他们之前有施工过吗，\x01",
            "我都没有注意到呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_210C")

    Jump("loc_2201")

    label("loc_2111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B1")

    #C0056
    ChrTalk(
        0xFE,
        (
            "在这附近，每到早晨就有很多\x01",
            "穿西装的人路过～\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "那些人就是通常所说的\x01",
            "『商务人士』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "……穿着整洁西装\x01",
            "的男人……\x01",
            "感觉有些帅气呢⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2201")

    label("loc_21B1")


    #C0059
    ChrTalk(
        0xFE,
        (
            "穿西装的男人\x01",
            "还挺帅的。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "每到早晨就能看见很多，\x01",
            "不知不觉就看花了眼呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2201")

    TalkEnd(0xFE)
    Return()

    # Function_12_1570 end

    def Function_13_2205(): pass

    label("Function_13_2205")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A2")

    #C0061
    ChrTalk(
        0x101,
        (
            "#0000F（港湾区的公园……\x01",
            "  这里是遗失了物品的特伦特先生\x01",
            "  途中经过的地方。）\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，请问您在这附近\x01",
            "捡到过什么失物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "呃，你们在找东西吗？\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "这么说来……昨天有个看上去\x01",
            "傻乎乎的青年去过那边的公园。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "走到半路时，突然大喊『背包破啦～』\x01",
            "什么的，吵闹了好久呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0066
    ChrTalk(
        0x103,
        "#0203F应该就是他吧。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "我只是站在远处看到的而已。\x01",
            "并不知道他丢了什么东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0006F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "嗯，不过……\x01",
            "今天早晨，有一位客人\x01",
            "说是捡到了什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "那是一位经常在附近散步的小姑娘，\x01",
            "你们不妨去问问她吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x2, 0x1, 0x3)
    TalkEnd(0xFE)
    Return()

    label("loc_24A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_253D")

    #C0071
    ChrTalk(
        0xFE,
        (
            "今天早晨，有一位客人\x01",
            "说是捡到了什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "那是一位经常在附近散步的小姑娘。\x01",
            "如果你们正在寻找失物，\x01",
            "不妨去问问她吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_253D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2547")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3762")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2597")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2597")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B7")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_375D")

    label("loc_25B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25CB")
    Jump("loc_375D")

    label("loc_25CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_375D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_27A7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2600")
    Call(0, 14)
    Jump("loc_27A2")

    label("loc_2600")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_26C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_265F")

    #C0073
    ChrTalk(
        0xFE,
        "这位客人，您可真有眼光……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "我一定会为您准备\x01",
            "最美味的面条。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C2")

    label("loc_265F")


    #C0075
    ChrTalk(
        0xFE,
        (
            "这位客人，\x01",
            "您是想要最筋道的面条吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "嗯……交给我好了，\x01",
            "就让我为您奉上最美味的面条吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_26C2")

    Jump("loc_27A2")

    label("loc_26C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2715")

    #C0077
    ChrTalk(
        0xFE,
        (
            "那个记者好像是\x01",
            "克洛斯贝尔时代周刊的……\x01",
            "到底在调查什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27A2")

    label("loc_2715")


    #C0078
    ChrTalk(
        0xFE,
        (
            "那些记者们\x01",
            "好像在到处打听呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "在我这里也\x01",
            "没完没了地问了半天。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "比如身边有没有人\x01",
            "变得异常之类的……\x01",
            "……到底在调查些什么呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_27A2")

    Jump("loc_375D")

    label("loc_27A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_28AC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C3")
    Call(0, 14)
    Jump("loc_28A7")

    label("loc_27C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2811")

    #C0081
    ChrTalk(
        0xFE,
        (
            "那个公司的职员\x01",
            "看起来很沉着大胆呢。\x01",
            "已经完全平静下来了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A7")

    label("loc_2811")


    #C0082
    ChrTalk(
        0xFE,
        (
            "据说那个公司昨天遭到了袭击，\x01",
            "但现在已经完全平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "墙上虽然还残留着弹痕，\x01",
            "但职员们却没有表现出丝毫的惊惶……\x01",
            "还真是非常沉着大胆啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_28A7")

    Jump("loc_375D")

    label("loc_28AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_29F4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C8")
    Call(0, 14)
    Jump("loc_29EF")

    label("loc_28C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2924")

    #C0084
    ChrTalk(
        0xFE,
        (
            "不过是这种程度的骚乱罢了，\x01",
            "我才没有关张停业的打算呢。\x01",
            "哼……别小看我啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EF")

    label("loc_2924")


    #C0085
    ChrTalk(
        0xFE,
        (
            "夜里好像发生了什么事件。\x01",
            "从早上开始，警察们就慌慌张张的。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "……我吗？\x01",
            "我可没有关张停业的打算。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "哼……只是这种程度的小骚乱而已，\x01",
            "我怎么可能会因此而关张。\x01",
            "还有很多老顾客在期待我的汤面呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_29EF")

    Jump("loc_375D")

    label("loc_29F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2B32")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A10")
    Call(0, 14)
    Jump("loc_2B2D")

    label("loc_2A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2A8A")

    #C0088
    ChrTalk(
        0xFE,
        (
            "坐在桌子前不停地写文件，\x01",
            "这种工作究竟哪里有乐趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "所谓的商务人士，\x01",
            "真是一种让人难以理解的职业。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B2D")

    label("loc_2A8A")


    #C0090
    ChrTalk(
        0xFE,
        (
            "最近，有一位事业状况\x01",
            "好得出奇的客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "据说他们公司的事业\x01",
            "进展得非常顺利，\x01",
            "所以心情特别好……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "嗯，所谓的商务人士，\x01",
            "真是一种让人难以理解的职业啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2B2D")

    Jump("loc_375D")

    label("loc_2B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2C99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2BAE")

    #C0093
    ChrTalk(
        0xFE,
        (
            "发音不准也就罢了，\x01",
            "但你可不要说这里是\x01",
            "奇形怪状的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "像我这种摊子，\x01",
            "在东方可是很常见的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C94")

    label("loc_2BAE")

    OP_63(0x153, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x153,
        (
            "#1110F喂，这也是露天店吗？\x01",
            "还真是奇形怪状呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "嗯……？竟敢说我的摊子奇形怪状！？\x01",
            "这叫东方风格啦！！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x153,
        "#1107F……洞～方～风～格！\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0098
    ChrTalk(
        0xFE,
        (
            "发音错了……\x01",
            "算、算了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2C94")

    Jump("loc_375D")

    label("loc_2C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2D99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2CE1")

    #C0099
    ChrTalk(
        0xFE,
        (
            "嗯……世界真是很大呢，\x01",
            "我也要继续努力才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D94")

    label("loc_2CE1")


    #C0100
    ChrTalk(
        0xFE,
        (
            "前几天，我去光顾了\x01",
            "东街的那家东方风味饭店。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "他们做的面相当不错呢。\x01",
            "几乎和我做的不相上下，\x01",
            "甚至可能在我之上……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "唔唔……真是服了，\x01",
            "看来我的修行仍然有所不足啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2D94")

    Jump("loc_375D")

    label("loc_2D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2EF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2E33")

    #C0103
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔，\x01",
            "只要向『克洛斯贝尔工商协会』\x01",
            "提交申请，就可以开露天店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "他们不像其它机关那么麻烦，\x01",
            "是一群很好说话的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF4")

    label("loc_2E33")


    #C0105
    ChrTalk(
        0xFE,
        (
            "就快到纪念庆典了……\x01",
            "如果要在庆典时开露天店，\x01",
            "就必须去登记申请。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "另外，克洛斯贝尔的露天店\x01",
            "是由一个叫做『克洛斯贝尔工商协会』\x01",
            "的团体所管理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "那个团体的人很不错，都很好说话。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2EF4")

    Jump("loc_375D")

    label("loc_2EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3133")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2FAB")

    #C0108
    ChrTalk(
        0xFE,
        (
            "以前，在我的老顾客之中，\x01",
            "有一对年轻的警察搭档。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "他们经常一边吃面条，\x01",
            "一边谈论着警察的未来。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0002F…………………………\x01",
            "（哈哈，莫非是……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_312E")

    label("loc_2FAB")


    #C0111
    ChrTalk(
        0xFE,
        (
            "别看我的露天店不起眼，\x01",
            "其实有很多回头客呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "其中有两位据说都是\x01",
            "警察的青年顾客。\x01",
            "他们以前经常来光顾呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "没记错的话，其中一位是个子很高，性格沉着\x01",
            "的男人，还有一位是栗色头发的热血青年……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 500)
    Sleep(500)

    #C0114
    ChrTalk(
        0xFE,
        (
            "对了，那个栗色头发的青年\x01",
            "好像和你长得很像呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0115
    ChrTalk(
        0x101,
        "#0005F哎，和我……吗？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "这么一说的话，气质好像也相似呢。\x01",
            "嗯，那位青年看起来也很诚实。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 0)
    SetScenarioFlags(0x0, 3)

    label("loc_312E")

    Jump("loc_375D")

    label("loc_3133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_326B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_31AC")

    #C0117
    ChrTalk(
        0xFE,
        (
            "我至今仍在\x01",
            "对面条进行研究。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "吃面的时候，如果有什么意见，\x01",
            "请不要有所顾虑，欢迎多多指点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3266")

    label("loc_31AC")


    #C0119
    ChrTalk(
        0xFE,
        "今天的面可是别具一格呢！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "尽管是粗面条，\x01",
            "但在汤汁的搭配下，口感非常柔滑……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "这面条在擀制的时候，\x01",
            "使用了玛因兹山道的小河水。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "这筋道又紧绷的面条，\x01",
            "你们只要一吃便知。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3266")

    Jump("loc_375D")

    label("loc_326B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_336D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_32DD")

    #C0123
    ChrTalk(
        0xFE,
        "不好意思，我可没义务听人发牢骚哦。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "你们也一样，如果想发什么牢骚，\x01",
            "可不要找我哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3368")

    label("loc_32DD")


    #C0125
    ChrTalk(
        0xFE,
        (
            "商人这种职业，\x01",
            "好像非常累人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "有很多客人在下班的路上来这里吃饭，\x01",
            "全都在这里大发牢骚。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "……听别人发牢骚又不是我的义务。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3368")

    Jump("loc_375D")

    label("loc_336D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_34B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_33F6")

    #C0128
    ChrTalk(
        0xFE,
        (
            "嗯……在面条这一点上，\x01",
            "我可是讲究独树一帜的。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "我这里和一般的露天店相比，\x01",
            "可是有本质区别的呢，本质区别！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B3")

    label("loc_33F6")


    #C0130
    ChrTalk(
        0xFE,
        (
            "虽说是露天店的面条，\x01",
            "但你可不能小看哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "我每天早晨都在家擀面，\x01",
            "并将那些在最适当的时间制作出的发酵物\x01",
            "在这里煮熟。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "我这里和一般的露天店相比，\x01",
            "可是有本质区别的呢，本质区别！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_34B3")

    Jump("loc_375D")

    label("loc_34B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_35C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_34FA")

    #C0133
    ChrTalk(
        0xFE,
        (
            "好啦，不必客气。\x01",
            "来尝尝我做的面条吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BD")

    label("loc_34FA")


    #C0134
    ChrTalk(
        0xFE,
        (
            "我是放弃了祖父传下来的店面，\x01",
            "开始经营这个露天店的。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "这也是为了追求极致，\x01",
            "做出最好的面条而进行的修行……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "为了听取更多顾客的意见，\x01",
            "所以我才做出了这个选择。\x01",
            "你们也一定要尝一尝啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_35BD")

    Jump("loc_375D")

    label("loc_35C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_36B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_363D")

    #C0137
    ChrTalk(
        0xFE,
        (
            "在这附近，\x01",
            "旧城区的不良少年有时会出现。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "再闹个没完，小心我把面条塞进他们嘴里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AF")

    label("loc_363D")


    #C0139
    ChrTalk(
        0xFE,
        (
            "在这附近，经常有\x01",
            "旧城区的不良少年出没。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "从傍晚到深夜，\x01",
            "动不动就大叫大嚷地胡闹。\x01",
            "真是没少给我们添乱。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_36AF")

    Jump("loc_375D")

    label("loc_36B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_36FD")

    #C0141
    ChrTalk(
        0xFE,
        (
            "我做的面条可是天下第一呢。\x01",
            "您要是怀疑的话，尝尝便知！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_375D")

    label("loc_36FD")


    #C0142
    ChrTalk(
        0xFE,
        "面条就是要筋道才好吃！\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        "必须要像这样富有弹性！\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "怎么样啊，你们也\x01",
            "来一碗尝尝吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_375D")

    Jump("loc_2547")

    label("loc_3762")

    TalkEnd(0xFE)
    Return()

    # Function_13_2205 end

    def Function_14_3766(): pass

    label("Function_14_3766")


    #C0145
    ChrTalk(
        0xFE,
        (
            "我想要挑战一下新口味，\x01",
            "于是尝试着做了一下\x01",
            "龙老饭店的汤面……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "模仿果然是行不通的啊。\x01",
            "这个食谱就送给你们好了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x191),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x191),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x1)
    Return()

    # Function_14_3766 end

    def Function_15_3849(): pass

    label("Function_15_3849")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_395E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_38C1")

    #C0149
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ的安保体系\x01",
            "好像是世界顶尖的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "据说花了不少米拉……\x01",
            "或许比警察局还要可靠吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3959")

    label("loc_38C1")


    #C0151
    ChrTalk(
        0xFE,
        "ＩＢＣ的保安部门很厉害呢。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "好像连送来的邮包都要\x01",
            "先用导力探知机来检测呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "负责警备工作的全是些\x01",
            "性情温和的人，\x01",
            "但他们的能力都很优秀呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3959")

    Jump("loc_3EAF")

    label("loc_395E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_39B0")

    #C0154
    ChrTalk(
        0xFE,
        (
            "今天的航空邮件\x01",
            "还没有送到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "好奇怪啊……\x01",
            "出了什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAF")

    label("loc_39B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_39EF")

    #C0156
    ChrTalk(
        0xFE,
        (
            "今天总是\x01",
            "有警车停驻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        "出什么事了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EAF")

    label("loc_39EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3AFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3A5D")

    #C0158
    ChrTalk(
        0xFE,
        (
            "从今往后，克洛斯贝尔\x01",
            "应该会越发繁荣起来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        "但我们的工作量也会因此而增加呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AF6")

    label("loc_3A5D")


    #C0160
    ChrTalk(
        0xFE,
        (
            "自从纪念庆典开始，\x01",
            "这条商业街变得热闹了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "目睹了纪念庆典的兴隆，\x01",
            "似乎有非常多的公司\x01",
            "计划进驻至此。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "工作量又要增加了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3AF6")

    Jump("loc_3EAF")

    label("loc_3AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3B4D")

    #C0163
    ChrTalk(
        0xFE,
        (
            "糟糕，今天是\x01",
            "ＩＢＣ的休息日呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "啊啊，白将货物\x01",
            "搬来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAF")

    label("loc_3B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3BC6")

    #C0165
    ChrTalk(
        0xFE,
        (
            "最近好像有不少企业在\x01",
            "引进一种叫做导力网络的东西，\x01",
            "不知那是零件还是什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "要小心些处理。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C2A")

    label("loc_3BC6")


    #C0167
    ChrTalk(
        0xFE,
        (
            "最近，标记为精密仪器的\x01",
            "小包裹变多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "好像是结晶回路什么的。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "那个也要轻拿轻放呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3C2A")

    Jump("loc_3EAF")

    label("loc_3C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3C8D")

    #C0170
    ChrTalk(
        0xFE,
        (
            "有一些公司\x01",
            "会给很多的小费呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "到那些公司去送快递，\x01",
            "还真是令人期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAF")

    label("loc_3C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3CCC")

    #C0172
    ChrTalk(
        0xFE,
        (
            "我们公司要是也能\x01",
            "给我们配备导力车就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAF")

    label("loc_3CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3D31")

    #C0173
    ChrTalk(
        0xFE,
        (
            "之前的休假，因为突然\x01",
            "接到紧急工作，被迫取消了。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        "呵呵……服务业真是很辛苦啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EAF")

    label("loc_3D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3D88")

    #C0175
    ChrTalk(
        0xFE,
        (
            "这个假期，我准备去米修拉姆\x01",
            "好好放松一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        "现在就有些等不及了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EAF")

    label("loc_3D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3DE1")

    #C0177
    ChrTalk(
        0xFE,
        "嗯～这个公司在哪里呢？\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "好像是不久前刚建成的，\x01",
            "一时想不起地址呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAF")

    label("loc_3DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3E36")

    #C0179
    ChrTalk(
        0xFE,
        (
            "据说旧城区那里\x01",
            "发生了斗殴事件？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "真可怕啊，我们也得小心一点。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EAF")

    label("loc_3E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3E79")

    #C0181
    ChrTalk(
        0xFE,
        (
            "这一带的建筑物大多都是公司。\x01",
            "包裹多得送不过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAF")

    label("loc_3E79")


    #C0182
    ChrTalk(
        0xFE,
        "嗯，接下来的配送地点是……\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        "喂，让开让开～！\x02",
    )

    CloseMessageWindow()

    label("loc_3EAF")

    TalkEnd(0xFE)
    Return()

    # Function_15_3849 end

    def Function_16_3EB3(): pass

    label("Function_16_3EB3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3F60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3F0F")

    #C0184
    ChrTalk(
        0xFE,
        (
            "我让孙女\x01",
            "费了不少心呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "我似乎是有些\x01",
            "顽固过头了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F5B")

    label("loc_3F0F")


    #C0186
    ChrTalk(
        0xFE,
        "……我的孙女真是个好孩子。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "我这个老家伙真不该\x01",
            "让她那么操心……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_3F5B")

    Jump("loc_4898")

    label("loc_3F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_405D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3FDC")

    #C0188
    ChrTalk(
        0xFE,
        (
            "孙女说，哪怕只有今天一天也好，\x01",
            "希望一直陪在我身边……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "……难不成，是在\x01",
            "担心我的身体吗…… \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4058")

    label("loc_3FDC")


    #C0190
    ChrTalk(
        0xFE,
        (
            "我都和孙女说了，\x01",
            "让她赶快回家去……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0191
    ChrTalk(
        0xFE,
        (
            "据说昨天发生了枪击事件，\x01",
            "小孩子应该赶快回家啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4058")

    Jump("loc_4898")

    label("loc_405D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_40EF")
    TurnDirection(0xFE, 0x0, 0)

    #C0192
    ChrTalk(
        0xFE,
        "真是一起让人不安的事件啊。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "……今天还是让孙女\x01",
            "早点回去为好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "我无论如何也不希望\x01",
            "让孙女遇到什么危险。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    Jump("loc_4898")

    label("loc_40EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4154")

    #C0195
    ChrTalk(
        0xFE,
        "我才不想吃药呢。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        "我只要能钓鱼就好了。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "我已经决定了，\x01",
            "就要这么度过余生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4898")

    label("loc_4154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_41AE")

    #C0198
    ChrTalk(
        0xFE,
        (
            "在纪念庆典这段时间，\x01",
            "都没能好好钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "哼，所有人都\x01",
            "兴奋过头了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4898")

    label("loc_41AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4242")

    #C0200
    ChrTalk(
        0xFE,
        "……孙女的心情我也明白。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "她是个好孩子，\x01",
            "心地很善良呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "但是我也活不了多久了，\x01",
            "人生的最后一段，就让我随心所欲地享受吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4898")

    label("loc_4242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4291")

    #C0203
    ChrTalk(
        0xFE,
        "……孙女今天也来了呢。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "唔，但是不巧，\x01",
            "我今天也很忙呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4898")

    label("loc_4291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_42F2")

    #C0205
    ChrTalk(
        0xFE,
        "钓鱼是我唯一的乐趣……\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "今天也靠钓鱼来打发一整天的时间吧，\x01",
            "可别打扰我哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4898")

    label("loc_42F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_43B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4328")

    #C0207
    ChrTalk(
        0xFE,
        (
            "哼，我可不喜欢\x01",
            "集体活动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B2")

    label("loc_4328")


    #C0208
    ChrTalk(
        0xFE,
        (
            "最近有一伙叫什么『钓公师团』\x01",
            "的家伙们来邀请我加入。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        "哼，但我可不喜欢集体活动。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        "说什么『享受钓鱼的乐趣』？真是不知所谓。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_43B2")

    Jump("loc_4898")

    label("loc_43B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_443D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4435")

    #C0211
    ChrTalk(
        0xFE,
        (
            "我可是早就决定好了，\x01",
            "要把剩下的时间全部用来专心钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        "虽然有些对不起孙女，但是我可不想吃药。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4438")

    label("loc_4435")

    Call(0, 18)

    label("loc_4438")

    Jump("loc_4898")

    label("loc_443D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_44E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4489")

    #C0213
    ChrTalk(
        0xFE,
        (
            "这样下去的话，连条鱼都钓不上来了。\x01",
            "真是的……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44DD")

    label("loc_4489")


    #C0214
    ChrTalk(
        0xFE,
        "嘁，没事搞什么水上巴士……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "是不是存心给我捣乱啊。\x01",
            "真讨厌，让人火大……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_44DD")

    Jump("loc_4898")

    label("loc_44E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_469B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_45B0")

    #C0216
    ChrTalk(
        0xFE,
        (
            "警察局的搜查一科中\x01",
            "汇集了很多精英男子。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "比如我在几年前遇到的那个搜查官，\x01",
            "年纪轻轻的，眼神却坚定诚实，感觉很不错……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "男人若是没有那种程度的热忱和实力，\x01",
            "我是不会认可的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4696")

    label("loc_45B0")


    #C0219
    ChrTalk(
        0xFE,
        "克洛斯贝尔的公务人员都让人信不过。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        "其中最差的当属警察了。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "连调查工作都做不好，\x01",
            "还会迫于政治家的压力，\x01",
            "做出保释坏人之类的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "哼，真是群一无是处的家伙们。\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "能得到老夫认同的，\x01",
            "也就只有『搜查一科』了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4696")

    Jump("loc_4898")

    label("loc_469B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4804")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_46F0")

    #C0224
    ChrTalk(
        0xFE,
        "哼，我非常不喜欢克洛斯贝尔人，\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        "厌恶到了想吐的程度。\x02",
    )

    CloseMessageWindow()
    Jump("loc_47FF")

    label("loc_46F0")


    #C0226
    ChrTalk(
        0xFE,
        "我很反感克洛斯贝尔人，\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "整天就只想着赚钱，\x01",
            "不懂尊重古来的传统与规矩……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "他们很容易被流行牵着鼻子走，\x01",
            "只关注那些风言风语的报道。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "而且还都喜欢聚在一起搞什么庆典。\x01",
            "真是群只知道胡闹的无聊家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "……算啦，说到底，其实我也是\x01",
            "生长在克洛斯贝尔的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_47FF")

    Jump("loc_4898")

    label("loc_4804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_483B")

    #C0231
    ChrTalk(
        0xFE,
        (
            "一个一个的全都这么\x01",
            "不成气候，唉……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4898")

    label("loc_483B")


    #C0232
    ChrTalk(
        0xFE,
        (
            "怎么，年轻人，\x01",
            "你们是来给我捣乱的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "赶快走开，\x01",
            "你们把鱼都吓跑了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    SetChrFlags(0xB, 0x10)
    OP_93(0xB, 0xB4, 0x0)

    label("loc_4898")

    TalkEnd(0xFE)
    Return()

    # Function_16_3EB3 end

    def Function_17_489C(): pass

    label("Function_17_489C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_498E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_48FE")

    #C0234
    ChrTalk(
        0xFE,
        (
            "我想通了，\x01",
            "以后不必太勉强爷爷。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "因为爷爷还是\x01",
            "非常有精神的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4989")

    label("loc_48FE")


    #C0236
    ChrTalk(
        0xFE,
        (
            "我决定了，\x01",
            "以后不再缠着爷爷了～\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "虽然我还是很想让爷爷\x01",
            "去医院看病，好好按时吃药。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "但不管怎么说，\x01",
            "爷爷毕竟还是\x01",
            "很有精神的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4989")

    Jump("loc_4D89")

    label("loc_498E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_49CA")

    #C0239
    ChrTalk(
        0xFE,
        (
            "希望爷爷今天\x01",
            "能钓到一大堆鱼啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A61")

    label("loc_49CA")


    #C0240
    ChrTalk(
        0xFE,
        (
            "嗯，我决定了，\x01",
            "今天要陪在\x01",
            "爷爷的身边。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "因为，让爷爷独自一人的话，\x01",
            "我会担心嘛……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "钓鱼的时候，爷爷好像很开心，\x01",
            "我最喜欢这样的爷爷了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4A61")

    Jump("loc_4D89")

    label("loc_4A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4A8E")

    #C0243
    ChrTalk(
        0xFE,
        "哎呀～发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D89")

    label("loc_4A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4AEF")

    #C0244
    ChrTalk(
        0xFE,
        (
            "我来啦，爷爷。\x01",
            "我又把药取来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "您按时吃药了吗？\x01",
            "不听医生的话\x01",
            "可不行哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D89")

    label("loc_4AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4B98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4B35")

    #C0246
    ChrTalk(
        0xFE,
        (
            "明年要是能和爷爷一起\x01",
            "开心地逛庆典就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B93")

    label("loc_4B35")


    #C0247
    ChrTalk(
        0xFE,
        (
            "呼，纪念庆典\x01",
            "结束了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "我最后\x01",
            "也没能去玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "我原本很想\x01",
            "和爷爷一起去逛逛呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4B93")

    Jump("loc_4D89")

    label("loc_4B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4C77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4BD2")

    #C0250
    ChrTalk(
        0xFE,
        (
            "呼，我很想为爷爷\x01",
            "做点什么……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C72")

    label("loc_4BD2")


    #C0251
    ChrTalk(
        0xFE,
        (
            "直到去年为止，\x01",
            "爷爷他一直都在住院。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "但他说不喜欢医院，\x01",
            "于是就自作主张地溜出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "呼，爷爷的心情，我也很理解……\x01",
            "但是，这样下去还是不好吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4C72")

    Jump("loc_4D89")

    label("loc_4C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4CD8")

    #C0254
    ChrTalk(
        0xFE,
        (
            "爷爷他总是\x01",
            "皱着眉头钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "医院开的药也不吃……\x01",
            "呼，我好担心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D25")

    label("loc_4CD8")


    #C0256
    ChrTalk(
        0xFE,
        (
            "爷爷，今天难道\x01",
            "不想去东街看看吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        "好不好嘛，一起去逛逛吧！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xC, 0x10)

    label("loc_4D25")

    Jump("loc_4D89")

    label("loc_4D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4D86")

    #C0258
    ChrTalk(
        0xFE,
        (
            "我爷爷是个\x01",
            "非常顽固的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "而且他很讨厌医院。\x01",
            "呼，很让人担心啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D89")

    label("loc_4D86")

    Call(0, 18)

    label("loc_4D89")

    TalkEnd(0xFE)
    Return()

    # Function_17_489C end

    def Function_18_4D8D(): pass

    label("Function_18_4D8D")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0260
    ChrTalk(
        0xC,
        (
            "爷爷～\x01",
            "我把药拿来了哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        (
            "我说……您有没有\x01",
            "每天按时吃药啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xB,
        "烦死人了……\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xB,
        (
            "我才不需要吃什么药，\x01",
            "赶快回家去。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "又这样说……\x01",
            "这怎么行啊，爷爷！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xC, 0x10)
    Return()

    # Function_18_4D8D end

    def Function_19_4E48(): pass

    label("Function_19_4E48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED9")

    #C0265
    ChrTalk(
        0xFE,
        "哎呀……\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "缇欧，在这种时间，\x01",
            "你要去哪里啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "警察的工作也很辛苦啊……\x01",
            "一定要当心哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x103,
        "#0200F嗯，没问题的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4F16")

    label("loc_4ED9")


    #C0269
    ChrTalk(
        0xFE,
        "警察的工作也很辛苦啊。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "缇欧和各位\x01",
            "都要注意安全哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F16")

    TalkEnd(0xFE)
    Return()

    # Function_19_4E48 end

    def Function_20_4F1A(): pass

    label("Function_20_4F1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4F7F")

    #C0271
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈从早上开始就\x01",
            "特别在意那个传闻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        "好像是有什么情况吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_501F")

    label("loc_4F7F")


    #C0273
    ChrTalk(
        0xFE,
        (
            "有消息说，从今天早晨开始，\x01",
            "就有人相继失踪。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "现在正在进行调查，\x01",
            "并搜集相关的情报……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "这个事件肯定有写成新闻的价值吧？\x01",
            "虽然是比较古怪的事件……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_501F")

    Jump("loc_51A6")

    label("loc_5024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5089")

    #C0276
    ChrTalk(
        0xFE,
        (
            "啊啊，好想早点回家……\x01",
            "但又不能把前辈一个人扔下……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        "呼，我到底该如何是好……\x02",
    )

    CloseMessageWindow()
    Jump("loc_51A6")

    label("loc_5089")


    #C0278
    ChrTalk(
        0xFE,
        "哎呀呀，怎么办呢……\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈扔下我一个人，\x01",
            "去紧急采访了呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0280
    ChrTalk(
        0x101,
        "#0005F难、难道是……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        "#0205F去了黑月的事务所吗……？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        "……（紧张）\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "前辈……还是放弃吧。\x01",
            "我可没法和你一起去啊～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    SetScenarioFlags(0xD0, 3)

    label("loc_51A6")

    TalkEnd(0xFE)
    Return()

    # Function_20_4F1A end

    def Function_21_51AA(): pass

    label("Function_21_51AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 4)), scpexpr(EXPR_END)), "loc_52B5")

    #C0284
    ChrTalk(
        0x1A,
        (
            "#2103F鲁巴彻也好，\x01",
            "失踪的市民也好……\x02\x03",

            "好像总有种\x01",
            "不详的预感呢。\x02\x03",

            "#2101F如果你们准备继续调查的话，\x01",
            "一定要多加小心。\x02\x03",

            "#2109F然后，还要平安无事地\x01",
            "把独家新闻拿给我！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B0")

    #C0285
    ChrTalk(
        0x101,
        "#0002F哈哈……明白了。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        (
            "#0104F格蕾丝小姐也\x01",
            "不要太勉强啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_52B0")

    Jump("loc_55BB")

    label("loc_52B5")


    #C0287
    ChrTalk(
        0x1A,
        (
            "#2105F啊呀，这不是支援科的诸位嘛。\x02\x03",

            "#2101F据说，黑手党的人都失踪了，\x01",
            "是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        "#0011F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        (
            "#0101F这件事……\x01",
            "您是从哪里听来的？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x1A,
        (
            "#2103F哈，我们也有\x01",
            "一些自己的情报网呢。\x02\x03",

            "先不提这些，听说，冈兹先生\x01",
            "昨天也失踪了……\x02\x03",

            "#2101F除此之外，市内的失踪人数\x01",
            "还在急剧增加。\x02\x03",

            "这种情况……总感觉～\x01",
            "非常不妙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#0013F……嗯。\x01",
            "总之，无论如何也要尽快\x01",
            "查清究竟发生了什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x1A,
        (
            "#2104F嗯，这么说来，\x01",
            "你们也正在追查这件事吧……\x01",
            "（做笔记……）\x02\x03",

            "#2110F好啦～基本明白了。\x01",
            "要是有什么发现的话，请再通知我！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0293
    ChrTalk(
        0x103,
        (
            "#0211F罗伊德前辈，\x01",
            "你还是说漏嘴了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        (
            "#0006F……真惭愧，\x01",
            "我明明还留心提防了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x104,
        (
            "#0300F算啦，在刚才那种情况下，\x01",
            "说漏嘴也是没办法的，别介意啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 4)

    label("loc_55BB")

    TalkEnd(0xFE)
    Return()

    # Function_21_51AA end

    def Function_22_55BF(): pass

    label("Function_22_55BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_582B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57F7")
    OP_4B(0x1D, 0xFF)
    OP_4B(0x1E, 0xFF)

    #C0296
    ChrTalk(
        0x1D,
        (
            "呦，帕、帕尔，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x1E,
        "嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x1E,
        (
            "……我以为你把我忘得\x01",
            "干干净净了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0299
    ChrTalk(
        0x1D,
        (
            "那、那怎么可能嘛！\x01",
            "因为游击士的工作\x01",
            "太忙了啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x1E,
        "……呵呵，开玩笑啦⊥\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x1E,
        (
            "你在游击士的工作中所付出的努力，\x01",
            "我可是最清楚不过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x1D,
        "帕、帕尔……⊥\x02",
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(20)
    OP_63(0x1E, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0303
    ChrTalk(
        0x153,
        "#1109F……气氛真好呀～！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x153, 500)
    TurnDirection(0x1E, 0x153, 500)
    OP_63(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0304
    ChrTalk(
        0x101,
        (
            "#0006F（琪、琪雅！\x01",
            "  不要去给人家捣乱……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x1E,
        "那、那个……\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x1D,
        "哈、哈哈……\x02",
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x5A, 0x0)
    OP_93(0x1E, 0x10E, 0x0)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x1E, 0xFF)
    SetScenarioFlags(0x1, 3)
    Jump("loc_582B")

    label("loc_57F7")


    #C0307
    ChrTalk(
        0xFE,
        (
            "那、那么……\x01",
            "我们就重振精神，\x01",
            "先去吃个饭如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_582B")

    TalkEnd(0xFE)
    Return()

    # Function_22_55BF end

    def Function_23_582F(): pass

    label("Function_23_582F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584D")
    Call(0, 22)
    Jump("loc_5882")

    label("loc_584D")


    #C0308
    ChrTalk(
        0xFE,
        "……嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "难得的机会，\x01",
            "慢慢走着去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5882")

    TalkEnd(0xFE)
    Return()

    # Function_23_582F end

    def Function_24_5886(): pass

    label("Function_24_5886")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_591A")
    Jump("loc_5964")

    label("loc_591A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_593A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5964")

    label("loc_593A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_595A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5964")

    label("loc_595A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5964")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_59EB")

    #C0310
    ChrTalk(
        0xFE,
        (
            "哎呀呀，这个料理\x01",
            "很好吃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "是在那边的露天店买的，\x01",
            "有种让人怀念的味道呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_59EB")


    #C0312
    ChrTalk(
        0xFE,
        (
            "这里正好有个公园，\x01",
            "就稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "哎呀呀，克洛斯贝尔市可真大啊。\x01",
            "带着小孩来逛，似乎是个错误呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A59")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_5886 end

    def Function_25_5A61(): pass

    label("Function_25_5A61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5A9B")

    #C0314
    ChrTalk(
        0xFE,
        (
            "那家露天店的荞麦面\x01",
            "非常非常好吃哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AD1")

    label("loc_5A9B")


    #C0315
    ChrTalk(
        0xFE,
        "逛来逛去的，真是累坏了呢～\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        "好想吃冰激凌啊～\x02",
    )

    CloseMessageWindow()

    label("loc_5AD1")

    TalkEnd(0xFE)
    Return()

    # Function_25_5A61 end

    def Function_26_5AD5(): pass

    label("Function_26_5AD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5B56")

    #C0317
    ChrTalk(
        0xFE,
        (
            "吃过午饭之后，\x01",
            "没能赶上水上巴士呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        "但是没想到，很快就又来了一艘。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "早知如此，\x01",
            "根本就不该着急嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BBD")

    label("loc_5B56")


    #C0320
    ChrTalk(
        0xFE,
        (
            "嗯嗯，前往米修拉姆的\x01",
            "水上巴士是在这里搭乘吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "听说米修拉姆\x01",
            "有很多漂亮的店铺，\x01",
            "很令人期待呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BBD")

    TalkEnd(0xFE)
    Return()

    # Function_26_5AD5 end

    def Function_27_5BC1(): pass

    label("Function_27_5BC1")

    TalkBegin(0xFE)

    #C0322
    ChrTalk(
        0xFE,
        "我要和女儿一起去米修拉姆。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "可以乘坐水上巴士，\x01",
            "真让人有点兴奋呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_5BC1 end

    def Function_28_5C13(): pass

    label("Function_28_5C13")

    TalkBegin(0xFE)

    #C0324
    ChrTalk(
        0xFE,
        "哇～好大的船啊～！\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        "我是第一次坐船呢～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_5C13 end

    def Function_29_5C4C(): pass

    label("Function_29_5C4C")

    TalkBegin(0xFE)

    #C0326
    ChrTalk(
        0xFE,
        (
            "听说米修拉姆\x01",
            "有很多的娱乐场所呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        "嘿嘿嘿，很期待呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_5C4C end

    def Function_30_5C92(): pass

    label("Function_30_5C92")

    TalkBegin(0xFE)

    #C0328
    ChrTalk(
        0xFE,
        (
            "（嘀嘀咕咕）……\x01",
            "果然是鲁巴彻搞的鬼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        "所以说，黑手党就是可怕……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_5C92 end

    def Function_31_5CE6(): pass

    label("Function_31_5CE6")

    TalkBegin(0xFE)

    #C0330
    ChrTalk(
        0xFE,
        (
            "黑月贸易公司……\x01",
            "从来没听说过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "难道是做了什么\x01",
            "招人怨恨的事情吗？\x01",
            "女神保佑，女神保佑……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_5CE6 end

    def Function_32_5D52(): pass

    label("Function_32_5D52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD7")

    #C0332
    ChrTalk(
        0xFE,
        "这种事件，经常会发生吧……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "不过，办公区的公司遭遇袭击，\x01",
            "或许还真是第一次呢。\x01",
            "实在是让我也吃了一惊啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_5E2E")

    label("loc_5DD7")


    #C0334
    ChrTalk(
        0xFE,
        "也不知道警察都在干些什么。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "每次都是等到事件发生之后，\x01",
            "他们才慢悠悠地到来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E2E")

    TalkEnd(0xFE)
    Return()

    # Function_32_5D52 end

    def Function_33_5E32(): pass

    label("Function_33_5E32")

    TalkBegin(0xFE)
    OP_4B(0x17, 0xFF)

    #C0336
    ChrTalk(
        0xFE,
        "哇，好破烂啊～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0xFE, 500)
    Sleep(300)

    #C0337
    ChrTalk(
        0x17,
        "嘘，不可以靠近哦！\x02",
    )

    CloseMessageWindow()
    OP_93(0x17, 0x2D, 0x0)
    OP_4C(0x17, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_33_5E32 end

    def Function_34_5E7E(): pass

    label("Function_34_5E7E")

    TalkBegin(0xFE)

    #C0338
    ChrTalk(
        0xFE,
        (
            "我经常来这个公园\x01",
            "玩呢，竟然会……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "真是的，警察到底\x01",
            "都在干什么啊……！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_5E7E end

    def Function_35_5ED5(): pass

    label("Function_35_5ED5")

    TalkBegin(0xFE)

    #C0340
    ChrTalk(
        0xFE,
        "……您有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        "#0005F啊，没什么……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 3)), scpexpr(EXPR_END)), "loc_5F42")

    #C0342
    ChrTalk(
        0x102,
        (
            "#0106F（格蕾丝小姐也真是\x01",
            "  够厉害的……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F42")

    TalkEnd(0xFE)
    Return()

    # Function_35_5ED5 end

    def Function_36_5F46(): pass

    label("Function_36_5F46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_5FA5")

    #C0343
    ChrTalk(
        0xFE,
        (
            "前往米修拉姆的乘客，\x01",
            "请稍等片刻。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "本班水上巴士将于\x01",
            "五分钟之后出航。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6119")

    label("loc_5FA5")


    #C0345
    ChrTalk(
        0xFE,
        (
            "前往米修拉姆的乘客，\x01",
            "请稍等片刻。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "本班水上巴士将于\x01",
            "五分钟之后出航。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#0005F哦，这就是开往那个著名『米修拉姆』\x01",
            "的水上巴士啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#0300F听说那边有主题公园\x01",
            "和商店街之类的地方，\x01",
            "非常适合游玩呢。\x02\x03",

            "#0305F……对了，罗伊德，\x01",
            "你去过那边吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#0006F没有，那里毕竟是\x01",
            "在我离开克洛斯贝尔的期间\x01",
            "建成的设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x102,
        (
            "#0100F算了，不管怎么说，\x01",
            "现在可没有闲工夫乘坐哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_6119")

    TalkEnd(0xFE)
    Return()

    # Function_36_5F46 end

    def Function_37_611D(): pass

    label("Function_37_611D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_END)), "loc_6312")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_61BF")

    #C0351
    ChrTalk(
        0xFE,
        (
            "说起来，刚才还被\x01",
            "达德利警官和艾玛警官\x01",
            "狠狠瞪了一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "黑月的成员也在这附近晃来晃去的……\x01",
            "真是不想负责这种地方\x01",
            "的巡逻工作啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_630D")

    label("loc_61BF")


    #C0353
    ChrTalk(
        0xFE,
        (
            "哎呀，从刚才开始，\x01",
            "黑月的成员就\x01",
            "一直在晃来晃去的呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "啊，不是成员，\x01",
            "该说是『职员』才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "虽然现在不见了……\x01",
            "但稍后肯定还会再出现吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#0003F不好意思，弗兰茨，这里就拜托你了。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        (
            "#0200F不过，应该不会有人来袭击的。\x01",
            "我觉得不必担心。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0358
    ChrTalk(
        0xFE,
        (
            "呼，话是这么说啦……\x01",
            "但还是没法彻底放心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)

    label("loc_630D")

    Jump("loc_63AF")

    label("loc_6312")


    #C0359
    ChrTalk(
        0xFE,
        (
            "虽说是大半夜，\x01",
            "但竟然会在离公园这么近的地方\x01",
            "真刀真枪地发生战斗……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "对了，至于达德利警官那边，\x01",
            "你能帮我稍微敷衍一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        "我可不想再遭他的白眼。\x02",
    )

    CloseMessageWindow()

    label("loc_63AF")

    TalkEnd(0xFE)
    Return()

    # Function_37_611D end

    def Function_38_63B3(): pass

    label("Function_38_63B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_63FB")

    #C0362
    ChrTalk(
        0xFE,
        (
            "哼，我这次一定要争取到角色。\x01",
            "一、二……一、二……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6666")

    label("loc_63FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6497")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6467")

    #C0363
    ChrTalk(
        0xFE,
        "瑟、瑟蕾奴前辈来了吗……！？\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "下周就要公布演员表了。\x01",
            "谁都坐不住了吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6492")

    label("loc_6467")


    #C0365
    ChrTalk(
        0xFE,
        (
            "下周就要公布了呢……\x01",
            "呼，压力好大……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6492")

    Jump("loc_6666")

    label("loc_6497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6517")

    #C0366
    ChrTalk(
        0xFE,
        (
            "每天练习跑步的话，\x01",
            "肚子会饿得不行呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "但体重增加的话，\x01",
            "弹跳力就会下降……\x01",
            "呼，真辛苦……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6534")

    label("loc_6517")


    #C0368
    ChrTalk(
        0xFE,
        (
            "呼，必须要\x01",
            "努力锻炼……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6534")

    Jump("loc_6666")

    label("loc_6539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_65D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65BA")

    #C0369
    ChrTalk(
        0xFE,
        "一、二……一、二……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "……听说，在这个公园附近，\x01",
            "有家东西很好吃的露天店呢。\x01",
            "嗯～好想尝尝……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_65D2")

    label("loc_65BA")


    #C0371
    ChrTalk(
        0xFE,
        "啊……肚子饿了……\x02",
    )

    CloseMessageWindow()

    label("loc_65D2")

    Jump("loc_6666")

    label("loc_65D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6666")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_663F")

    #C0372
    ChrTalk(
        0xFE,
        "一、二……一、二……\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "……嘿哟……\x01",
            "首先要从基础的体力开始锻炼啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6666")

    label("loc_663F")


    #C0374
    ChrTalk(
        0xFE,
        (
            "干、干什么……？\x01",
            "你可别妨碍我啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6666")

    TalkEnd(0xFE)
    Return()

    # Function_38_63B3 end

    def Function_39_666A(): pass

    label("Function_39_666A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_676F")

    label("loc_6676")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_6693")
    OP_4C(0x20, 0xFF)
    Jump("loc_6698")

    label("loc_6693")

    Jump("loc_66A0")

    label("loc_6698")

    Sleep(200)
    Jump("loc_6676")

    label("loc_66A0")

    OP_4B(0x20, 0xFF)
    TurnDirection(0xFE, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_671B")

    #C0375
    ChrTalk(
        0xFE,
        (
            "马上就要正式公布演员阵容了，\x01",
            "可不是悠闲享乐的时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "在休息日也\x01",
            "一定要努力练习……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_6766")

    label("loc_671B")


    #C0377
    ChrTalk(
        0xFE,
        "我这次可是以二号主角为目标呢。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "一定要争取到一个\x01",
            "重要的角色……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6766")

    OP_4C(0x20, 0xFF)
    Jump("loc_6826")

    label("loc_676F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6826")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_680A")

    #C0379
    ChrTalk(
        0xFE,
        (
            "尼克鲁那家伙，竟然在\x01",
            "这种地方做跑步训练啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        "我也不会输给他的！\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "光是一个莉夏就让人压力很大了……\x01",
            "…………呼………\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_6826")

    label("loc_680A")


    #C0382
    ChrTalk(
        0xFE,
        "我、我也不会输给他的！\x02",
    )

    CloseMessageWindow()

    label("loc_6826")

    TalkEnd(0xFE)
    Return()

    # Function_39_666A end

    def Function_40_682A(): pass

    label("Function_40_682A")

    TalkBegin(0xFE)

    #N0383
    NpcTalk(
        0x24,
        "东方长相的男人",
        (
            "#5P分公司经理愿意见你们，\x01",
            "——请入内吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_682A end

    def Function_41_686E(): pass

    label("Function_41_686E")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0384
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
    )

    CloseMessageWindow()
    OP_68(63790, 0, 7940, 1500)
    MoveCamera(45, 23, 0, 1500)
    OP_6E(280, 1500)
    SetCameraDistance(29000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0385
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6931")
    OP_E0(0x2)
    MiniGame(0x6, 0x1, 0x10BE4, 0xFFFFF63C, 0x4074, 0xB4, 0x109C8, 0xFFFFF254, 0x2E2C)

    label("loc_6931")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_41_686E end

    def Function_42_6936(): pass

    label("Function_42_6936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6952")
    TalkBegin(0xFF)
    Call(0, 43)
    TalkEnd(0xFF)
    Jump("loc_6A66")

    label("loc_6952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6968")
    Call(0, 45)
    Jump("loc_6A66")

    label("loc_6968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6984")
    TalkBegin(0xFF)
    Call(0, 43)
    TalkEnd(0xFF)
    Jump("loc_6A66")

    label("loc_6984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5D")
    TalkBegin(0xFF)
    Call(0, 43)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A55")

    #C0386
    ChrTalk(
        0x101,
        (
            "#0001F（想再进去一次的话……\x01",
            "  ……恐怕很难吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#0103F（那位分公司经理\x01",
            "  大概也正忙着应付\x01",
            "  各种各样的『工作』吧……）\x02\x03",

            "#0101F（能问到这些话，\x01",
            "  已经算是幸运了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_6A55")

    TalkEnd(0xFF)
    Jump("loc_6A66")

    label("loc_6A5D")

    TalkBegin(0xFF)
    Call(0, 43)
    TalkEnd(0xFF)

    label("loc_6A66")

    Return()

    # Function_42_6936 end

    def Function_43_6A67(): pass

    label("Function_43_6A67")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0388
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁，\x01",
            "并挂着一块牌子。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0389
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『黑月贸易公司·克洛斯贝尔分公司』\x01",
            "※若有要事，敬请敲门。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CEE")

    #C0390
    ChrTalk(
        0x101,
        (
            "#0001F『黑月贸易公司』……\x02\x03",

            "难道这里就是\x01",
            "伊安律师曾说过的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x104,
        (
            "#0301F是从共和国进驻这里的\x01",
            "那个黑手党组织的据点吧。\x02\x03",

            "#0306F话虽如此，\x01",
            "不过，看起来还真像是个普通的公司啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x102,
        (
            "#0101F普通的也只是外表而已吧。\x02\x03",

            "内部是个什么样的组织，\x01",
            "却完全弄不清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x103,
        (
            "#0200F不管怎么说，他们应该和鲁巴彻一样，\x01",
            "都不是我们可以随便\x01",
            "干涉的对象呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        (
            "#0001F嗯，而且我们目前\x01",
            "也没有任何证据\x01",
            "能表明他们是犯罪组织。\x02\x03",

            "#0003F（……但如果有机会，真想好好调查\x01",
            "  一下这个地方呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CEE")

    SetScenarioFlags(0x94, 0)
    Return()

    # Function_43_6A67 end

    def Function_44_6CF2(): pass

    label("Function_44_6CF2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(45480, 0, 3700, 0)
    MoveCamera(45, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(29000, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_68(1340, 1800, -380, 10000)
    MoveCamera(45, 24, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(26000, 10000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-7040, 4500, 24940, 0)
    MoveCamera(20, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    OP_68(-2790, 2500, 5490, 8000)
    MoveCamera(35, 32, 0, 8000)
    OP_6E(600, 8000)
    SetCameraDistance(51580, 8000)
    PlaceName2(340, 200, "c_plac31", 0x0, 4000)
    OP_6F(0x79)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FF5")

    #A0395
    AnonymousTalk(
        0x102,
        (
            "#0104F面朝羽扇河，\x01",
            "南望艾鲁姆湖的港湾区域……\x02\x03",

            "#0100F这附近是办公区吧。\x01",
            "北侧的建筑全都是公司呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0396
    AnonymousTalk(
        0x104,
        (
            "#0309F哈哈，但是也有个\x01",
            "感觉很不错的公园呢。\x02\x03",

            "#0302F那里是给人休息的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #A0397
    AnonymousTalk(
        0x103,
        (
            "#0203F据数据库的记载，那个地方\x01",
            "好像叫做『港湾公园』。\x01",
            "……一直都没变化呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0398
    AnonymousTalk(
        0x101,
        "#0005F啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-13890, 5100, 25220, 0)
    MoveCamera(0, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    OP_0D()
    Sleep(500)

    #A0399
    AnonymousTalk(
        0x101,
        (
            "#0000F是克洛斯贝尔时代周刊社。\x01",
            "原来已经搬到那里了啊。\x02\x03",

            "#0003F（嗯，过了三年的时间，\x01",
            "  果然变化不少呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6FF5")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0400
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "港湾区是位于城市东北方向的商业街。\x02",
        )
    )

    CloseMessageWindow()

    #A0401
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在克洛斯贝尔最大的河流——羽扇河的对面，\x01",
            "有一座公园，是游客与市民们的休息之所。\x02",
        )
    )

    CloseMessageWindow()

    #A0402
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "除了各大公司，知名的『克洛斯贝尔通讯社』\x01",
            "大楼也矗立于此。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_715C")
    OP_68(-19600, 2500, -27950, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)

    label("loc_715C")

    SetScenarioFlags(0x45, 2)
    EventEnd(0x5)
    Return()

    # Function_44_6CF2 end

    def Function_45_7162(): pass

    label("Function_45_7162")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 18600, 0, 17800, 0)
    SetChrPos(0x102, 19700, 0, 17800, 0)
    SetChrPos(0x103, 18600, 0, 16600, 0)
    SetChrPos(0x104, 19700, 0, 16600, 0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_726A")
    OP_68(22000, 3700, 20500, 0)
    MoveCamera(24, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    MoveCamera(37, 6, 0, 6000)
    SetCameraDistance(18000, 6000)
    OP_0D()
    PlaceName2(340, 200, "c_plac13", 0x0, 1000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(22000, 1000, 21000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(21500, 0)
    OP_68(22000, 0, 21000, 2000)
    OP_6F(0x1)
    OP_0D()
    Jump("loc_7299")

    label("loc_726A")

    OP_68(22000, 0, 21000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(21500, 0)
    OP_0D()

    label("loc_7299")

    Call(0, 43)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72C5")

    #C0403
    ChrTalk(
        0x101,
        "#12P#0001F是这里吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x88, 3)

    label("loc_72C5")

    TurnDirection(0x102, 0x101, 500)

    #C0404
    ChrTalk(
        0x102,
        "#11P#0101F……要怎么办呢？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【敲门】\x01",      # 0
            "【离开】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7338"),
        (1, "loc_7759"),
        (SWITCH_DEFAULT, "loc_777F"),
    )


    label("loc_7338")


    def lambda_733D():

        label("loc_733D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_733D")

    QueueWorkItem2(0x102, 2, lambda_733D)

    def lambda_734F():
        OP_96(0xFE, 0x4A9C, 0x0, 0x4CF4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_734F)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x2)
    Sleep(300)
    Sound(811, 0, 100, 0)
    Sleep(500)

    #C0405
    ChrTalk(
        0x101,
        (
            "#11P#0001F──不好意思！\x01",
            "请问有人在吗！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    VolumeBGM(0x3C, 0x12C)
    Sound(855, 0, 100, 0)
    Sleep(3000)
    SetChrPos(0x24, 19100, 350, 21500, 180)
    OP_4B(0x24, 0xFF)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)

    #N0406
    NpcTalk(
        0x24,
        "男人的声音",
        "#5P#2S……请问是哪位？\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#12P#0003F………我们是克洛斯贝尔警察局·特别\x01",
            "任务支援科的成员。\x02\x03",

            "#0001F关于某个事件，\x01",
            "希望能向贵公司的分公司经理先生\x01",
            "进行简短的询问。\x02",
        )
    )

    CloseMessageWindow()

    #N0408
    NpcTalk(
        0x24,
        "男人的声音",
        "#5P#2S#40W………………………………\x02",
    )

    CloseMessageWindow()

    #N0409
    NpcTalk(
        0x24,
        "男人的声音",
        "#5P#2S……请各位稍等。\x02",
    )

    CloseMessageWindow()
    Sound(855, 0, 100, 0)
    Sleep(3000)
    VolumeBGM(0x64, 0x12C)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0410
    ChrTalk(
        0x101,
        "#0006F#5P那么……\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x104,
        "#12P#0303F那位经理究竟是龙是蛇呢……\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        (
            "#6P#0201F#6P……还真是很期待\x01",
            "会面的瞬间啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x24, 0x4)
    SetChrPos(0x24, 19100, 350, 21500, 180)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 18600, 0, 17800, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)

    def lambda_762D():
        OP_95(0xFE, 19100, 0, 19700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_762D)

    def lambda_7647():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_7647)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x24, 2)
    Sleep(300)

    #N0413
    NpcTalk(
        0x24,
        "东方长相的男人",
        "#5P──让各位久等了。\x02",
    )

    CloseMessageWindow()

    #N0414
    NpcTalk(
        0x24,
        "东方长相的男人",
        (
            "#5P分公司经理愿意见你们，\x01",
            "请入内吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x24, 0xE1, 0x190)

    def lambda_76CD():
        OP_96(0xFE, 0x4DA8, 0x0, 0x4CAE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_76CD)
    WaitChrThread(0x24, 1)

    #C0415
    ChrTalk(
        0x101,
        "#6P#0000F谢、谢谢。\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x102,
        "#12P#0103F……打扰了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 19100, 0, 17200, 0)
    OP_4C(0x24, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x4, 0x2)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x81, 2)
    EventEnd(0x5)
    Jump("loc_777F")

    label("loc_7759")

    SetChrPos(0x0, 19100, 0, 17200, 0)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    EventEnd(0x5)
    Jump("loc_777F")

    label("loc_777F")

    Return()

    # Function_45_7162 end

    def Function_46_7780(): pass

    label("Function_46_7780")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    OP_68(22000, 0, 19000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 19100, 350, 21500, 180)
    SetChrPos(0x102, 19100, 350, 21500, 180)
    SetChrPos(0x103, 19100, 350, 21500, 180)
    SetChrPos(0x104, 19100, 350, 21500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x24, 0x4)
    SetChrPos(0x24, 19100, 350, 21500, 180)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x24, 0xFF)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x5, 0x27)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x27, 5300, 0, -12500, 270)
    OP_D3(0x27, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    SetCameraDistance(20500, 6000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)

    def lambda_7926():
        OP_96(0xFE, 0x4CF4, 0x0, 0x3908, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7926)

    def lambda_7940():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7940)
    Sleep(500)

    def lambda_7954():
        OP_96(0xFE, 0x48A8, 0x0, 0x3908, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7954)

    def lambda_796E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_796E)
    Sleep(600)

    def lambda_7982():
        OP_96(0xFE, 0x4CF4, 0x0, 0x3DB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7982)

    def lambda_799C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_799C)
    Sleep(500)

    def lambda_79B0():
        OP_96(0xFE, 0x48A8, 0x0, 0x3DB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79B0)

    def lambda_79CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_79CA)
    WaitChrThread(0x104, 1)

    def lambda_79DF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_79DF)
    WaitChrThread(0x103, 1)

    def lambda_79F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_79F0)
    WaitChrThread(0x102, 1)

    def lambda_7A01():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7A01)
    WaitChrThread(0x101, 1)

    def lambda_7A12():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A12)

    def lambda_7A1F():
        OP_95(0xFE, 19100, 0, 17700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_7A1F)

    def lambda_7A39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_7A39)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x24, 2)
    OP_6F(0x10)

    #N0417
    NpcTalk(
        0x24,
        "东方长相的男人",
        "#5P……各位辛苦了。\x02",
    )

    CloseMessageWindow()

    #N0418
    NpcTalk(
        0x24,
        "东方长相的男人",
        (
            "#5P如果还有什么事情，\x01",
            "欢迎随时光临。\x01",
            "这是分公司经理让我给各位的传言。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        "#12P#0003F……多谢关照。\x02",
    )

    CloseMessageWindow()
    OP_93(0x24, 0x0, 0x1F4)

    def lambda_7AFB():
        OP_95(0xFE, 19100, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_7AFB)
    Sleep(1000)

    def lambda_7B18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_7B18)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x24, 2)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x4)
    ClearMapObjFlags(0x4, 0x10)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    Sleep(700)
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_68(22000, 0, 17870, 2000)
    MoveCamera(45, 20, 0, 2000)
    SetCameraDistance(18950, 2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    Sleep(300)

    #C0420
    ChrTalk(
        0x101,
        (
            "#0006F#5P继鲁巴彻之后，\x01",
            "这里也是如此吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x104,
        (
            "#0306F#12P呼，不过和那边相比，\x01",
            "这边的态度起码要友好了很多……\x02\x03",

            "#0301F但也可能正好相反，他们其实更加瞧不起我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x103,
        "#12P#0206F#6P那种可能性也无法否认……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_64(0x102)

    def lambda_7D08():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D08)
    Sleep(50)

    def lambda_7D18():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7D18)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)
    Sleep(300)

    #C0423
    ChrTalk(
        0x101,
        "#6P#0005F艾莉，怎么了……？\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x103,
        (
            "#6P#0201F难道……\x01",
            "你身体不舒服吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)
    Sleep(300)

    #C0425
    ChrTalk(
        0x102,
        (
            "#5P#0104F不，没事的。\x02\x03",

            "#0108F……话说回来，\x01",
            "按照曹先生的说法，那个叫『银』的\x01",
            "强大刺客已经潜入到克洛斯贝尔了……\x02\x03",

            "#0101F感觉这个情报应该是真的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        (
            "#6P#0001F嗯……\x01",
            "从他的态度来看，应该没错。\x02\x03",

            "#0008F只是，我觉得那个分公司经理\x01",
            "并不是向彩虹剧团和伊莉娅小姐\x01",
            "发出恐吓的人呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0427
    ChrTalk(
        0x104,
        (
            "#0301F#11P嗯，我也有同感。\x02\x03",

            "如果他们真是犯人的话，\x01",
            "也就完全没有必要把自己\x01",
            "与『银』的关系暗示给我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x103,
        (
            "#6P#0208F……如此说来……\x02\x03",

            "#0201F莫非恐吓信只是那个名叫『银』\x01",
            "的暗杀者擅自做出的行动，\x01",
            "与其雇主『黑月』完全无关？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0429
    ChrTalk(
        0x101,
        (
            "#0006F#5P如果是那样的话……\x01",
            "我们的调查工作可就真的无从下手了。\x02\x03",

            "#0001F假如刚才那些话都是真的……\x01",
            "那么，也许连那个分公司经理\x01",
            "也都不了解『银』的底细吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x104,
        (
            "#0301F也就是说，目前唯一的办法\x01",
            "就只有抓住他本人，把情况问清楚了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x102,
        "#5P#0108F也许吧……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    #C0432
    ChrTalk(
        0x102,
        (
            "#5P#0103F如果那个叫『银』的刺客\x01",
            "是以伊莉娅小姐为目标的话……\x02\x03",

            "事情恐怕就已经超出了\x01",
            "我们的任务范围。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_814E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_814E)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)

    #C0433
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x102,
        (
            "#5P#0100F他的身手似乎非常高超，\x01",
            "单凭我们，完全没有把握将其顺利抓捕。\x02\x03",

            "所以说，如今是不是应该\x01",
            "把任务转交给警察局总部呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        "#6P#0011F这个……\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x103,
        (
            "#6P#0205F但他们也许又会像旧城区事件时一样，\x01",
            "假装什么都没听到呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        (
            "#5P#0103F不，对于克洛斯贝尔市而言，\x01",
            "彩虹剧团与伊莉娅·普拉提耶\x01",
            "都是极其重要的存在。\x02\x03",

            "#0101F如果她陷入了危险状况，\x01",
            "警察局总部也绝对不会坐视不理……\x02\x03",

            "即使赌上警察的威信，也必须将事件解决吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 19400, 0, 6200, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    #Sound(1557, 255, 100, 0)    #voice#Dudley

    #N0438
    NpcTalk(
        0x25,
        "男人的声音",
        "──正是如此。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(22000, 0, 16000, 2500)
    SetCameraDistance(20500, 2500)

    def lambda_83C5():
        OP_96(0xFE, 0x4BC8, 0x0, 0x2BC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_83C5)

    def lambda_83DF():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_83DF)
    Sleep(100)

    def lambda_83EF():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_83EF)
    Sleep(100)

    def lambda_83FF():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_83FF)
    Sleep(100)

    def lambda_840F():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_840F)
    WaitChrThread(0x25, 1)
    OP_6F(0x11)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0439
    ChrTalk(
        0x101,
        "#0011F#5P您、您是……！\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x102,
        "#5P#0105F是搜查一科的……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x25,
        (
            "#11P#0603F一科的达德利。\x02\x03",

            "#0601F跟我来。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        "#0005F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x25,
        (
            "#11P#0601F……怎么会有人蠢到\x01",
            "在这种地方闲聊个没完。\x02\x03",

            "好了，赶快跟我过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x101,
        "#0011F#5P明、明白了。\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x104,
        "#5P#0301F喂，这是怎么回事啊……\x02",
    )

    CloseMessageWindow()
    OP_93(0x25, 0xB4, 0x1F4)
    SetCameraDistance(21000, 1500)

    def lambda_85AC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_85AC)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_85D3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_85D3)
    Sleep(150)

    def lambda_85F0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_85F0)
    Sleep(150)

    def lambda_860D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_860D)
    Sleep(150)

    def lambda_862A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_862A)
    OP_0D()
    EndChrThread(0x25, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x101, 0x1)
    OP_6F(0x10)
    OP_68(12300, 900, -10300, 0)
    MoveCamera(310, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x25, 17600, 0, -6000, 225)
    SetChrPos(0x101, 19600, 0, -4000, 225)
    SetChrPos(0x102, 20600, 0, -3000, 225)
    SetChrPos(0x103, 21600, 0, -2000, 225)
    SetChrPos(0x104, 22600, 0, -1000, 225)
    BeginChrThread(0x25, 3, 0, 47)
    BeginChrThread(0x101, 3, 0, 48)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 50)
    BeginChrThread(0x104, 3, 0, 51)
    OP_68(8200, 900, -10300, 8000)
    MoveCamera(315, 25, 0, 8000)
    SetCameraDistance(19500, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x25, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    OP_93(0x25, 0x5A, 0x1F4)
    Sleep(150)
    Sound(1555, 255, 100, 0)    #voice#Dudley
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0446
    AnonymousTalk(
        0x25,
        (
            "……你们难道是白痴吗？\x02\x03",

            "虽然不知你们有何目的，\x01",
            "但怎么能如此冒失地闯进去……\x02\x03",

            "而且居然还在对方的门前\x01",
            "若无其事地悠闲讨论案情。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0447
    ChrTalk(
        0x101,
        "#6P#0006F对、对不起……\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x102,
        (
            "#0108F#12P……我们确实\x01",
            "有些考虑不周。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x25,
        (
            "#5P#0603F哼……算了。\x02\x03",

            "#0600F──那么，说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0450
    ChrTalk(
        0x101,
        "#6P#0005F说……说什么啊？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x25,
        (
            "#5P#0601F你们刚才不是一直\x01",
            "在说什么彩虹剧团吗？\x02\x03",

            "你们前来探访『黑月』，\x01",
            "与它有何关系……\x02\x03",

            "一五一十地说出来吧。\x02",
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
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0452
    ChrTalk(
        0x101,
        "#6P#0013F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x104,
        (
            "#12P#0301F喂喂……\x01",
            "你在说什么啊，太唐突了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x103,
        (
            "#12P#0211F突然出现，还理所当然似地\x01",
            "提出这么厚脸皮的要求……\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x25,
        (
            "#5P#0604F哼……\x01",
            "到底是谁更厚脸皮啊？\x02\x03",

            "我们一科从一个多月以前\x01",
            "就已经盯上了『黑月』……\x02\x03",

            "#0601F什么招呼也没打，\x01",
            "突然插手进来的可是你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        "#6P#0011F是、是这样吗……？\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x102,
        (
            "#0101F#12P难道说……\x01",
            "一科那边也在调查『银』？\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x25,
        (
            "#5P#0603F哼……\x01",
            "你们也知道这个名字了吗？\x02\x03",

            "#0601F总之，要把你们了解到的情报\x01",
            "毫无隐瞒地交代清楚。\x02\x03",

            "如果不服从的话……\x01",
            "我就会以妨碍一科调查案件为由，\x01",
            "向赛尔盖长官提出严重抗议。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#6P#0008F可恶……明白了。\x02\x03",

            "#0013F只是……\x01",
            "这毕竟是我们支援科接受的委托。\x02\x03",

            "希望您不要随便外传，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x25,
        (
            "#5P#0603F那要由我来判断。\x02\x03",

            "#0601F好了，快说吧——这是命令。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    OP_63(0x25, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    SetCameraDistance(19500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0x25)
    OP_6F(0x10)

    #C0461
    ChrTalk(
        0x25,
        (
            "#5P#0604F──嗯，原来如此。\x02\x03",

            "本以为毫无头绪……\x01",
            "结果他总算露出狐狸尾巴了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x102,
        (
            "#0101F#12P狐狸尾巴……\x01",
            "是指『银』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x25,
        (
            "#5P#0600F……是的。\x02\x03",

            "#0603F为了与『鲁巴彻』对抗，\x01",
            "『黑月』特别雇佣的强悍刺客，\x01",
            "算得上是『黑月』的最终王牌。\x02\x03",

            "从经由某个途径得到情报以来，\x01",
            "我们一科就一直在监视『黑月』。\x02\x03",

            "#0601F不过……\x01",
            "真是没想到，竟会被你们这些\x01",
            "菜鸟们误打误撞地发现了马脚。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x104,
        (
            "#12P#0304F嘿……\x01",
            "还真会说呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x103,
        (
            "#12P#0201F不过……\x01",
            "为什么只监视『黑月』呢？\x02\x03",

            "警察局对『鲁巴彻』那边\x01",
            "好像一直都是放任不管的……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x25,
        (
            "#5P#0604F哼，这叫什么话？\x02\x03",

            "『鲁巴彻』的大体动向，\x01",
            "我们也已经掌握了。\x02\x03",

            "#0602F旧城区的事件与军犬的使用……\x02\x03",

            "你们处理的那一连串的事件，\x01",
            "我们在事前都有一定程度的了解。\x02",
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
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0467
    ChrTalk(
        0x101,
        "#6P#0005F#4S什么……！？\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x103,
        "#12P#0201F既然如此，为什么……\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x25,
        (
            "#5P#0603F哼……那种程度的小事情，\x01",
            "要是处理起来就没完没了了，还不值得我们浪费人力。\x02\x03",

            "#0600F又不是什么杀人事件，\x01",
            "只不过是一些小小的纷争而已。\x02\x03",

            "我们怎能把其它重要案件搁置不管，\x01",
            "将有限的人力用于这等琐碎小事？\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#6P#0007F话虽如此，但是……！\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x25,
        (
            "#5P#0601F──我们搜查一科\x01",
            "和你们这群半吊子可不一样！\x02\x03",

            "#0603F在这座正义难以得到彻底伸张的城市中，\x01",
            "我们至少要将基本秩序维持住……\x02\x03",

            "遏止杀人一类的重大犯罪，\x01",
            "与犯罪组织和国外的间谍机关对抗，\x01",
            "保障市民与社会的安全……\x02\x03",

            "#0601F我们的艰辛，你们理解得了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x101,
        "#6P#0005F！？\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#0108F#12P果然……是这样吗……\x02\x03",

            "#0106F克洛斯贝尔的和平与繁荣……\x01",
            "只是建立在一层薄冰之上。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x25,
        (
            "#5P#0606F哼，但大多数市民\x01",
            "却注意不到这个事实。\x02\x03",

            "#0600F『鲁巴彻』与帝国派议员\x01",
            "相互勾结，可以说是众所周知了……\x02\x03",

            "而『黑月』与共和国派议员关系密切的\x01",
            "事情却鲜有人知。\x02\x03",

            "#0603F以目前的形势来看，无论针对哪一方，\x01",
            "我们都不可能直接出手。\x02\x03",

            "#0601F不仅如此……\x01",
            "由于没有处理外国间谍的相关法律，\x01",
            "所以，外国谍报员根本就是为所欲为。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x101,
        "#6P#0013F……怎么会………\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x103,
        "#12P#0206F……真是难以置信。\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x104,
        (
            "#12P#0306F好像有种……\x01",
            "无药可救的感觉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x102,
        "#0108F#40W#12P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x25,
        (
            "#5P#0603F然而，即使在这种绝望的状态之下，\x01",
            "我们也仍然坚定信念，做好自己力所能及之事。\x02\x03",

            "我们会权衡所有案件的危险程度，\x01",
            "就算无法从根本上解决问题，\x01",
            "至少也要为了抑制犯罪而不断努力……\x02\x03",

            "#0600F『银』的问题也只不过是其中的一环罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x101,
        "#6P#0005F啊……\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x25,
        (
            "#5P#0600F关于彩虹剧团的事情，\x01",
            "我们并没有察觉到。\x02\x03",

            "感谢你们提供的情报。\x02\x03",

            "以后的事情就交给我们一科来处理，\x01",
            "你们可以回去执行日常任务了。\x02",
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
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0482
    ChrTalk(
        0x101,
        "#6P#0007F#4S什么……！？\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x104,
        "#12P#0307F喂喂，为什么会是这样啊！？\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x25,
        (
            "#5P#0603F根据目前的情况来看，\x01",
            "基本可以确定『银』是真实存在的了。\x02\x03",

            "既要监视『黑月』的动向，\x01",
            "同时还要在神秘杀手的威胁之下，\x01",
            "保护好伊莉娅·普拉提耶……\x02\x03",

            "#0602F你们能胜任这项工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x101,
        "#6P#0010F唔……\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x103,
        (
            "#12P#0206F……如果没有足够的人手，\x01",
            "或许真的很勉强呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x25, 0x10E, 0x1F4)
    OP_68(6890, 900, -9560, 2000)

    def lambda_984B():
        OP_95(0xFE, 5000, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_984B)
    WaitChrThread(0x25, 1)
    OP_93(0x25, 0xB4, 0x1F4)
    OP_71(0x5, 0xF1, 0x10E, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0x5)
    Sleep(500)

    #C0487
    ChrTalk(
        0x25,
        (
            "#0603F#5P联络彩虹剧团的任务\x01",
            "就交给你们吧。\x02\x03",

            "至于恐吓事件的应对工作，\x01",
            "就由我们搜查一科来接手……\x02\x03",

            "#0600F你们去把状况解释清楚吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_990D():
        OP_95(0xFE, 5000, 0, -11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_990D)
    Sleep(100)

    def lambda_992A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_992A)
    WaitChrThread(0x25, 1)
    WaitChrThread(0x25, 2)
    OP_71(0x5, 0x10F, 0x12C, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x5)
    Sound(457, 0, 100, 0)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)

    def lambda_9979():
        OP_95(0xFE, -14000, 0, -12500, 6500, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_9979)
    Sleep(1250)
    Sound(458, 0, 100, 0)
    Fade(500)
    OP_68(-14500, 1000, -12500, 0)
    MoveCamera(40, 35, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_68(-19500, 1000, -19500, 4000)
    MoveCamera(60, 25, 0, 4000)
    SetCameraDistance(16500, 4000)
    WaitChrThread(0x27, 1)

    def lambda_99F8():
        OP_9E(0xFE, 0xFFFFC950, 0xFFFFB7BC, 0xFFFEA070, 0x1964, 0x1)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_99F8)
    WaitChrThread(0x27, 1)

    def lambda_9A17():
        OP_95(0xFE, -20000, 0, -33500, 6500, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_9A17)
    WaitChrThread(0x27, 1)
    OP_6F(0x79)
    ClearChrFlags(0x25, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x1000)
    StopBGM(0x1770)
    Fade(1000)
    OP_68(7700, 900, -10300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(9810, 900, -10230, 3000)
    OP_6F(0x1)
    Sleep(500)

    #C0488
    ChrTalk(
        0x104,
        (
            "#0301F#12P可恶，把自己想说的话说完之后\x01",
            "就立刻走掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x103,
        (
            "#12P#0211F而且还有专用车，\x01",
            "更是让人感到火大……\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x102,
        "#0103F#11P#40W………………………………\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x101,
        (
            "#0008F#5P……不过，他说的这些话，\x01",
            "也并不是无法理解。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0492
    ChrTalk(
        0x102,
        "#0105F#11P哎……\x02",
    )

    CloseMessageWindow()

    def lambda_9BAD():
        OP_93(0xFE, 0x59, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9BAD)
    Sleep(50)

    def lambda_9BBD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9BBD)
    Sleep(50)
    OP_93(0x104, 0xE1, 0x1F4)
    Sleep(300)

    #C0493
    ChrTalk(
        0x101,
        (
            "#0006F#5P这次的事件，确实已经超出了\x01",
            "我们的能力范畴。\x02\x03",

            "至于莉夏与伊莉娅小姐那边，我们能做的\x01",
            "也只有说明缘由和道歉了……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x104,
        "#0306F呼，也只能这样了吗……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x103,
        "#12P#0208F没有……办法了呢。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0496
    ChrTalk(
        0x102,
        "#0107F#11P等、等一下！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9CDB():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9CDB)
    Sleep(50)

    def lambda_9CEB():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9CEB)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)

    #C0497
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    SetCameraDistance(19000, 20000)

    #C0498
    ChrTalk(
        0x102,
        (
            "#0106F#11P罗伊德……\x01",
            "你竟然会说这种话！？\x02\x03",

            "#0101F你不是说过，要跨越『壁障』吗……\x01",
            "只要大家齐心协力，就一定能跨越任何壁障，\x01",
            "这不是你自己说过的话吗……！\x02\x03",

            "#0107F但现在，你为什么会……！\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        "#6P#0011F艾、艾莉……？\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x104,
        (
            "#12P#0305F喂喂，怎么了啊？\x02\x03",

            "#0301F大小姐，\x01",
            "你刚才不是也说过，\x01",
            "应该把工作交给警察局总部吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0501
    ChrTalk(
        0x102,
        (
            "#0105F#11P#40W啊……\x02\x03",

            "#0108F#50W……是、是啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x103,
        "#6P#0205F艾莉前辈……\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x101,
        (
            "#6P#0006F那个……\x02\x03",

            "那个，其实我也很不甘心啊，\x01",
            "也想要做点什么。\x02\x03",

            "#0000F既然艾莉都这么说了，\x01",
            "那我们就考虑一些其它办法……\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x102,
        (
            "#0106F#11P不必了……\x02\x03",

            "#0102F……对不起，\x01",
            "我好像是有点累了。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        "#6P#0001F艾莉……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x104,
        (
            "#12P#0306F唔，这也难怪。\x01",
            "毕竟今天交涉的对象\x01",
            "全都是一些难缠的家伙。\x02\x03",

            "#0300F先去彩虹剧团，\x01",
            "向伊莉娅小姐他们报告一下，\x01",
            "然后就回去休息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x103,
        (
            "#6P#0203F是啊……\x01",
            "我也赞成。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x101,
        (
            "#6P#0003F……嗯。\x02\x03",

            "#0000F艾莉，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x102,
        (
            "#0104F#11P嗯……谢谢大家……\x02\x03",

            "#0100F那我们现在\x01",
            "就去彩虹剧团吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    StopBGM(0xBB8)
    SetChrPos(0x0, 9600, 0, -10300, 270)
    SetScenarioFlags(0x81, 3)
    OP_29(0x42, 0x1, 0x8)
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    EventEnd(0x5)
    Return()

    # Function_46_7780 end

    def Function_47_A12B(): pass

    label("Function_47_A12B")


    def lambda_A130():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_A130)
    WaitChrThread(0x25, 1)

    def lambda_A14E():
        OP_95(0xFE, 6700, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_A14E)
    WaitChrThread(0x25, 1)
    Return()

    # Function_47_A12B end

    def Function_48_A168(): pass

    label("Function_48_A168")

    Sleep(500)

    def lambda_A170():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A170)
    WaitChrThread(0x101, 1)

    def lambda_A18E():
        OP_95(0xFE, 9600, 0, -11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A18E)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_48_A168 end

    def Function_49_A1AF(): pass

    label("Function_49_A1AF")

    Sleep(600)

    def lambda_A1B7():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1B7)
    WaitChrThread(0x102, 1)

    def lambda_A1D5():
        OP_95(0xFE, 9600, 0, -9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1D5)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x10E, 0x1F4)
    Return()

    # Function_49_A1AF end

    def Function_50_A1F6(): pass

    label("Function_50_A1F6")

    Sleep(700)

    def lambda_A1FE():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A1FE)
    WaitChrThread(0x103, 1)

    def lambda_A21C():
        OP_95(0xFE, 11000, 0, -11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A21C)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x10E, 0x1F4)
    Return()

    # Function_50_A1F6 end

    def Function_51_A23D(): pass

    label("Function_51_A23D")

    Sleep(800)

    def lambda_A245():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A245)
    WaitChrThread(0x104, 1)

    def lambda_A263():
        OP_95(0xFE, 11000, 0, -9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A263)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_51_A23D end

    def Function_52_A284(): pass

    label("Function_52_A284")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1600, 2500, 5600, 0)
    MoveCamera(55, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29000, 0)
    SetChrPos(0x0, -19600, 0, -28000, 0)
    SetChrPos(0x1, -19600, 0, -28000, 0)
    SetChrPos(0x2, -19600, 0, -28000, 0)
    SetChrPos(0x3, -19600, 0, -28000, 0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -10500, 0, 12000, 180)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 8000, 0, 10000, 270)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -18000, 0, 12500, 180)
    SetChrFlags(0xA, 0x8000)

    def lambda_A383():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A383)
    OP_68(-1600, 1500, 5600, 5000)
    FadeToBright(2000, 0)
    Sleep(1000)

    def lambda_A3BA():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A3BA)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(22140, 2500, 20700, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(21000, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_A284 end

    def Function_53_A42B(): pass

    label("Function_53_A42B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00500.itc", 0x1E)
    LoadChrToIndex("apl/ch50220.itc", 0x1F)
    LoadEffect(0x0, "event\\eva04_00.eff")
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(21500, 7900, 24500, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x26, 0x8000)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x26, 23000, 9500, 24500, 270)
    OP_52(0x26, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_68(21500, 10400, 24500, 5000)
    FadeToBright(2000, 0)
    Sleep(3000)
    PlayEffect(0x1, 0xFF, 0x26, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChip(0x0, 0x26, 0x1E, 0x12C)

    def lambda_A57C():
        OP_95(0xFE, 21500, 9500, 24500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A57C)

    def lambda_A596():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_A596)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x26, 2)
    SetChrChip(0x1, 0x26, 0x0, 0x0)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x1)
    Sleep(500)
    OP_68(14000, 9400, 24500, 700)
    MoveCamera(40, 18, 0, 700)
    SetCameraDistance(17500, 700)
    SetChrChip(0x0, 0x26, 0x1E, 0x12C)
    SetChrSubChip(0x26, 0x0)

    def lambda_A5FA():
        OP_9D(0xFE, 0x36B0, 0x2134, 0x5FB4, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A5FA)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    PlayEffect(0x0, 0xFF, 0x26, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    OP_6F(0x79)
    OP_68(14000, 11800, 31000, 700)
    MoveCamera(35, 15, 0, 700)
    SetCameraDistance(18500, 700)
    SetChrSubChip(0x26, 0x0)

    def lambda_A68A():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_A68A)

    def lambda_A697():
        OP_9D(0xFE, 0x36B0, 0x2A30, 0x7918, 0xCE4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A697)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    PlayEffect(0x0, 0xFF, 0x26, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    OP_6F(0x79)
    OP_68(-4000, 11200, 31000, 2000)
    MoveCamera(45, 27, 0, 2000)
    SetCameraDistance(22500, 2000)
    SetChrSubChip(0x26, 0x0)

    def lambda_A727():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_A727)

    def lambda_A734():
        OP_9D(0xFE, 0x24B8, 0x2C24, 0x7918, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A734)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    SetChrSubChip(0x26, 0x0)

    def lambda_A766():
        OP_9D(0xFE, 0xFFFFF448, 0x2648, 0x7918, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A766)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    PlayEffect(0x0, 0xFF, 0x26, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    SetChrSubChip(0x26, 0x0)

    def lambda_A7CF():
        OP_9D(0xFE, 0xFFFFD314, 0x3458, 0x7918, 0x1324, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A7CF)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    PlayEffect(0x0, 0xFF, 0x26, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    SetChrSubChip(0x26, 0x0)

    def lambda_A838():
        OP_9D(0xFE, 0xFFFFAC04, 0x3458, 0x7918, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A838)
    Sound(854, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x26, 0x1)
    SetScenarioFlags(0x5C, 2)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_A42B end

    def Function_54_A872(): pass

    label("Function_54_A872")

    EventBegin(0x0)
    Fade(1000)
    OP_68(22000, 2000, 20100, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 18600, 0, 12400, 0)
    SetChrPos(0x102, 19600, 0, 12400, 0)
    SetChrPos(0x103, 18600, 0, 11000, 0)
    SetChrPos(0x104, 19600, 0, 11000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, 19100, 0, 16600, 0)
    MoveCamera(30, 30, 0, 5000)
    SetCameraDistance(17000, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(19100, 1100, 13600, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_0D()

    #C0510
    ChrTalk(
        0x101,
        "#12P#0013F这是……\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x103,
        "#12P#0201F是袭击的痕迹吧……\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x104,
        (
            "#0303F似乎正是之前说过的那个\x01",
            "重型机关枪的弹痕呢……\x02\x03",

            "#0301F至少没有使用炸弹，\x01",
            "真是谢天谢地了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x21, 0xFF)
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x21, 0xB4, 0x1F4)

    #C0513
    ChrTalk(
        0x21,
        "#5P呀，这不是罗伊德和各位嘛！\x02",
    )

    CloseMessageWindow()
    OP_68(19100, 1100, 14000, 1200)

    def lambda_AAAC():
        OP_95(0xFE, 19100, 0, 14800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_AAAC)
    WaitChrThread(0x21, 1)
    OP_6F(0x1)

    #C0514
    ChrTalk(
        0x101,
        (
            "#12P#0001F弗兰茨……\x01",
            "现在什么状况？\x02\x03",

            "我们刚刚得知了情况，\x01",
            "就匆忙赶过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x21,
        "#5P我也不太清楚呢。\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x21,
        (
            "#5P只知道在昨天半夜，\x01",
            "似乎发生了枪击事件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x21,
        (
            "#5P达德利警官他们现在\x01",
            "正在进行案情询问。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0518
    ChrTalk(
        0x102,
        (
            "#0106F果然又被一科\x01",
            "捷足先登了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x103,
        "#12P#0206F行动果然迅速。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        (
            "#12P#0003F我们也希望从『黑月』\x01",
            "那里探听一些情报……\x02\x03",

            "#0000F能让我们进去吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x21,
        "#5P嗯，好吧……\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x21,
        (
            "#5P因为长官只是吩咐我说，\x01",
            "不要让一般市民进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x21,
        (
            "#5P不过，达德利警官那边，\x01",
            "你们可得想办法敷衍过去哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x101,
        "#12P#0002F没问题，多谢了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 19100, 0, 13000, 0)
    OP_4C(0x21, 0xFF)
    SetChrPos(0x21, 20500, 0, 15200, 180)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xC2, 3)
    OP_29(0x4B, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_54_A872 end

    def Function_55_AD5C(): pass

    label("Function_55_AD5C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(22000, 0, 21000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 19100, 350, 21500, 180)
    SetChrPos(0x102, 19100, 350, 21500, 180)
    SetChrPos(0x103, 19100, 350, 21500, 180)
    SetChrPos(0x104, 19100, 350, 21500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, 20500, 0, 15200, 180)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetCameraDistance(22500, 4000)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x4)

    def lambda_AE88():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE88)

    def lambda_AEA2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AEA2)
    Sleep(650)

    def lambda_AEB6():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AEB6)

    def lambda_AED0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AED0)
    Sleep(650)

    def lambda_AEE4():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AEE4)

    def lambda_AEFE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AEFE)
    Sleep(650)

    def lambda_AF12():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AF12)

    def lambda_AF2C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AF2C)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    OP_4B(0x101, 0xFF)
    OP_4B(0x102, 0xFF)
    OP_4B(0x103, 0xFF)
    OP_4B(0x104, 0xFF)

    def lambda_AF62():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AF62)

    def lambda_AF6F():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_AF6F)

    def lambda_AF7C():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_AF7C)

    def lambda_AF89():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_AF89)
    Sleep(100)
    OP_4B(0x21, 0xFF)
    TurnDirection(0x21, 0x101, 500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x21)

    def lambda_AFD4():

        label("loc_AFD4")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_AFD4")

    QueueWorkItem2(0x21, 2, lambda_AFD4)

    def lambda_AFE6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AFE6)

    def lambda_AFF3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_AFF3)

    def lambda_B000():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_B000)

    def lambda_B00D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_B00D)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_4C(0x101, 0xFF)
    OP_4C(0x102, 0xFF)
    OP_4C(0x103, 0xFF)
    OP_4C(0x104, 0xFF)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    WaitChrThread(0x101, 1)
    Fade(1000)
    OP_68(21100, 1000, 1800, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    EndChrThread(0x21, 0x2)
    OP_4C(0x21, 0xFF)
    SetChrPos(0x21, 20500, 0, 15200, 180)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrPos(0x101, 21100, 0, 3800, 180)
    SetChrPos(0x102, 21600, 0, 5300, 180)
    SetChrPos(0x103, 20600, 0, 4800, 180)
    SetChrPos(0x104, 21100, 0, 6500, 180)
    OP_68(21100, 1000, -2200, 4000)

    def lambda_B0F8():
        OP_95(0xFE, 21100, 0, -3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B0F8)
    Sleep(50)

    def lambda_B115():
        OP_95(0xFE, 22100, 0, -1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B115)
    Sleep(50)

    def lambda_B132():
        OP_95(0xFE, 20100, 0, -2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B132)
    Sleep(50)

    def lambda_B14F():
        OP_95(0xFE, 21100, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B14F)
    WaitChrThread(0x101, 1)

    def lambda_B16D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B16D)
    WaitChrThread(0x102, 1)

    def lambda_B17E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B17E)
    WaitChrThread(0x103, 1)

    def lambda_B18F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B18F)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)

    #C0525
    ChrTalk(
        0x101,
        "#12P#0006F……真是服了他们。\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x102,
        (
            "#5P#0106F是啊，虽然很感谢他\x01",
            "能告诉我们这么多……\x02\x03",

            "#0101F但真没想到，竟会那么露骨地暗示\x01",
            "他们准备认真开战啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x104,
        (
            "#0303F#5P再这样下去，\x01",
            "真有可能会演变为惨烈的血战呢。\x02\x03",

            "#0301F搞不好的话，下次就有可能直接在市中心开战了。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x103,
        (
            "#6P#0206F而且，还有从『黑月』总部\x01",
            "派来增援的可能性……\x02\x03",

            "#0211F火药味真是相当浓烈啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0529
    ChrTalk(
        0x101,
        (
            "#12P#0003F……不过，既然曹先生那样说，\x01",
            "他们目前应该也还有些犹豫吧。\x02\x03",

            "#0013F总而言之，关于鲁巴彻\x01",
            "这次的袭击，疑点实在是太多了。\x02\x03",

            "在黑月发起正式反击之前，\x01",
            "我们还是努力多调查一下为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x102,
        "#5P#0101F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x103,
        (
            "#6P#0205F也就是说，今天也\x01",
            "要去各处打探吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x101,
        (
            "#12P#0003F不……\x02\x03",

            "#0000F──在如今这种情况下，\x01",
            "还是直接去鲁巴彻一趟吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0533
    ChrTalk(
        0x104,
        "#0305F#5P你认真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x102,
        (
            "#5P#0106F虽、虽然以前也\x01",
            "曾去拜访过……\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x103,
        (
            "#6P#0201F但是毕竟发生过那起竞拍会事件，\x01",
            "直接过去的话，终究还是太过鲁莽了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x101,
        (
            "#12P#0006F……嗯。\x01",
            "所谓的和解，也仅限于琪雅\x01",
            "那一件事情而已。\x02\x03",

            "#0008F只是，有件事情，\x01",
            "我实在是非常在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x103,
        "#6P#0205F非常在意的事是指……？\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x101,
        (
            "#12P#0001F加尔西亚的动向。\x02\x03",

            "我反复思考过好几次，\x01",
            "那个人绝不是愚蠢无谋之辈。\x02\x03",

            "而且，他还给人一种很能服众，\x01",
            "统率能力极强的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x104,
        (
            "#0303F#5P的确，因为他原本就是\x01",
            "一个有名猎兵团的部队长呢。\x02\x03",

            "#0301F从常理来说，这种人绝不会\x01",
            "轻易发动毫无意义的袭击……\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x102,
        (
            "#5P#0103F昨晚那场袭击，到底是他的指示，\x01",
            "还是他的手下擅自妄为呢……\x02\x03",

            "#0101F这个问题的确很令人在意呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x101,
        (
            "#12P#0000F对吧？\x02\x03",

            "哪怕只是在鲁巴彻商会\x01",
            "的附近打听一下情况也好。\x02\x03",

            "我们现在就去看看，如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x102,
        "#5P#0102F唉……真拿你没办法啊。\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x103,
        (
            "#6P#0202F算了，如果只是在附近打探一下，\x01",
            "应该也不会有什么危险吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x104,
        "#0302F#5P好，那我们就去看看吧！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 21100, 0, -2500, 180)
    SetScenarioFlags(0xC2, 4)
    OP_29(0x4B, 0x1, 0x2)
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_55_AD5C end

    def Function_56_B899(): pass

    label("Function_56_B899")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(18120, 2300, 5600, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(14010, 0)
    SetChrPos(0x8, 19940, 0, 9410, 180)
    SetChrPos(0x101, 19200, 0, 7270, 0)
    SetChrPos(0x102, 20640, 0, 7470, 0)
    SetChrPos(0x103, 19150, 0, 5850, 0)
    SetChrPos(0x104, 20640, 0, 6050, 0)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0545
    ChrTalk(
        0x101,
        (
            "#6P#0000F那个，不好意思。\x01",
            "请问您在这附近\x01",
            "捡到过什么失物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x8,
        "#5P哎呀，我是捡到过类似失物的东西呢……\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x8,
        (
            "#5P我之前发现公园边上\x01",
            "的草丛里挂着一个东西，\x01",
            "于是就捡了起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x8,
        "#5P当时好像都快要被风吹走了呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0549
    ChrTalk(
        0x101,
        "#6P#0005F快要被风吹走……？\x02",
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x103,
        (
            "#0200F#12P这么一说，\x01",
            "委托人当时好像也曾说过，\x01",
            "已经忘记最后一件遗失物是什么了。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        "#0100F#11P到底会是什么呢？\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x8,
        (
            "#5P你们正在找它吗？\x01",
            "那就交给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0553
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x339),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "拿到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x339, 1)

    #C0554
    ChrTalk(
        0x104,
        (
            "#11P#0305F原来是导力列车的车票啊……\x02\x03",

            "#0306F话说，要是没有这个的话，\x01",
            "他就无法回国了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x338, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x339, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC66")

    #C0555
    ChrTalk(
        0x101,
        (
            "#6P#0003F不、不管怎么说，\x01",
            "这样一来，总算全部找到了啊。\x02\x03",

            "#0000F立刻去向特伦特先生汇报吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x102,
        "#0100F#11P嗯，去把这些失物还给他吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC91")

    label("loc_BC66")


    #C0557
    ChrTalk(
        0x101,
        "#6P#0003F……稍后就把失物交还给他吧。\x02",
    )

    CloseMessageWindow()

    label("loc_BC91")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 20110, 0, 7370, 225)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    OP_29(0x2, 0x1, 0x4)
    SetScenarioFlags(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BCE7")
    OP_29(0x2, 0x1, 0x1F)

    label("loc_BCE7")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_56_B899 end

    def Function_57_BCED(): pass

    label("Function_57_BCED")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0558
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "前往『米修拉姆』的水上巴士·时刻表\x01\x01",
            "※米修拉姆引以为豪的主题公园\x01",
            "     『奇幻乐园』开园中！\x01",
            "     请尽情享受欢乐时光！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_57_BCED end

    def Function_58_BD9A(): pass

    label("Function_58_BD9A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0559
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『羽扇河·第一灯塔』\x01\x01",
            "  无关人员禁止入内。\x01",
            "　  ～克洛斯贝尔市～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_58_BD9A end

    SaveToFile()

Try(main)
