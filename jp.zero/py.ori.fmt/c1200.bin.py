from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "クーニャ",               # 1
        "オーゼル",               # 2
        "ビショップ",             # 3
        "クワイン老人",           # 4
        "アミサ",                 # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "観光客",                 # 10
        "観光客",                 # 11
        "市民",                   # 12
        "市民",                   # 13
        "市民",                   # 14
        "市民",                   # 15
        "市民",                   # 16
        "水上バスガイド",         # 17
        "黒月社員",               # 18
        "グレイス",               # 19
        "レインズ",               # 20
        "ロバーツ主任",           # 21
        "遊撃士スコット",         # 22
        "パール",                 # 23
        "ニコル",                 # 24
        "セリーヌ",               # 25
        "フランツ巡査",           # 26
        "黒月社員",               # 27
        "黒月社員",               # 28
        "ラウ",                   # 29
        "ダドリー捜査官",         # 30
        "銀",                     # 31
        "ダドリー車",             # 32
        "中央広場",               # 33
        "西通り",                 # 34
        "行政区",                 # 35
        "住宅街",                 # 36
        "歓楽街",                 # 37
        "東通り",                 # 38
        "旧市街",                 # 39
        "港湾区",                 # 40
        "ＩＢＣ",                 # 41
        "駅前通り",               # 42
        "裏通り",                 # 43
        "ウルスラ間道",           # 44
        "東クロスベル街道",       # 45
        "西クロスベル街道",       # 46
        "マインツ山道",           # 47
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
        "Function_13_243B",        # 0D, 13
        "Function_14_3AFC",        # 0E, 14
        "Function_15_3BFF",        # 0F, 15
        "Function_16_434D",        # 10, 16
        "Function_17_4E2B",        # 11, 17
        "Function_18_5422",        # 12, 18
        "Function_19_54FB",        # 13, 19
        "Function_20_55E7",        # 14, 20
        "Function_21_58C1",        # 15, 21
        "Function_22_5D86",        # 16, 22
        "Function_23_6032",        # 17, 23
        "Function_24_6095",        # 18, 24
        "Function_25_629A",        # 19, 25
        "Function_26_6328",        # 1A, 26
        "Function_27_643C",        # 1B, 27
        "Function_28_649A",        # 1C, 28
        "Function_29_64E1",        # 1D, 29
        "Function_30_6537",        # 1E, 30
        "Function_31_6595",        # 1F, 31
        "Function_32_660B",        # 20, 32
        "Function_33_66FB",        # 21, 33
        "Function_34_674F",        # 22, 34
        "Function_35_67B4",        # 23, 35
        "Function_36_682F",        # 24, 36
        "Function_37_6A3E",        # 25, 37
        "Function_38_6D00",        # 26, 38
        "Function_39_7019",        # 27, 39
        "Function_40_71FF",        # 28, 40
        "Function_41_7245",        # 29, 41
        "Function_42_7319",        # 2A, 42
        "Function_43_7462",        # 2B, 43
        "Function_44_771F",        # 2C, 44
        "Function_45_7C09",        # 2D, 45
        "Function_46_825D",        # 2E, 46
        "Function_47_AE6E",        # 2F, 47
        "Function_48_AEAB",        # 30, 48
        "Function_49_AEF2",        # 31, 49
        "Function_50_AF39",        # 32, 50
        "Function_51_AF80",        # 33, 51
        "Function_52_AFC7",        # 34, 52
        "Function_53_B16E",        # 35, 53
        "Function_54_B5B5",        # 36, 54
        "Function_55_BB0B",        # 37, 55
        "Function_56_C6C2",        # 38, 56
        "Function_57_CB3E",        # 39, 57
        "Function_58_CBF7",        # 3A, 58
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_162F")

    #C0001
    ChrTalk(
        0xFE,
        (
            "鉄道のチケットを落とすなんて\x01",
            "間の抜けた観光客ねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "まあ街中を探し回ってたのなら\x01",
            "気の毒だったわ。\x01",
            "早く届けてあげてね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2437")

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_168D")

    #C0003
    ChrTalk(
        0xFE,
        (
            "自治州議会、\x01",
            "ようやく終わったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "予算の発表が楽しみだわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_170E")

    label("loc_168D")


    #C0005
    ChrTalk(
        0xFE,
        (
            "自治州議会、\x01",
            "ようやく終わったって話よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "ふう……長かったわね。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "最後にマクダエル市長が\x01",
            "頑張ってくれたのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_170E")

    Jump("loc_2437")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_17BB")

    #C0008
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズの記者さんに\x01",
            "聞き込みをされたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "ちょっと童顔な感じの好青年……㈱\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "オトコとしてはまだまだだけど\x01",
            "将来性はあるわね、うん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2437")

    label("loc_17BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1826")

    #C0011
    ChrTalk(
        0xFE,
        "今日も散歩しようと思ったのに……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "警官の人まで立っちゃって\x01",
            "何だか物々しいわねえ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2437")

    label("loc_1826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18C0")

    #C0013
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長って\x01",
            "メディアにもあんまり出ないで\x01",
            "部下を動かすタイプなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "市民としては\x01",
            "もう少し詳しい話が知りたいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_18C0")


    #C0015
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長って\x01",
            "どっしり構えてて隙のない感じよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "メディアにもあんまり出てこないのよ。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "でも今度の市長選を\x01",
            "狙ってるって噂もあるし……\x01",
            "市民としては気になる存在なのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_197E")

    Jump("loc_2437")

    label("loc_1983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1ADA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A12")

    #C0018
    ChrTalk(
        0xFE,
        (
            "ミシュラムのアーケード街で\x01",
            "事件があったそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "ニュースにもなってないし、\x01",
            "あんまり噂も聞かないのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD5")

    label("loc_1A12")


    #C0020
    ChrTalk(
        0xFE,
        (
            "噂で聞いたんだけど、\x01",
            "ミシュラムのアーケード街で\x01",
            "事件があったんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "記念祭の最中だっていうのに\x01",
            "酷い騒ぎだったそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "でも不思議なことに……\x01",
            "ニュースにはなってないのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1AD5")

    Jump("loc_2437")

    label("loc_1ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1B7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B1C")

    #C0023
    ChrTalk(
        0xFE,
        (
            "今年はどんな\x01",
            "催し物があるのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B76")

    label("loc_1B1C")


    #C0024
    ChrTalk(
        0xFE,
        "来月からは記念祭ね……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "今年は５日間もあるそうだし\x01",
            "予定を考えておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1B76")

    Jump("loc_2437")

    label("loc_1B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1BD5")

    #C0026
    ChrTalk(
        0xFE,
        (
            "ただ、雑誌の写真くらいでしか\x01",
            "お目にかかれないのが難点よね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C77")

    label("loc_1BD5")


    #C0027
    ChrTalk(
        0xFE,
        (
            "ＩＢＣのクロイス総裁って\x01",
            "まだ４０代なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "若い頃から重役を歴任してきた\x01",
            "超が付くやり手なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "おまけにハンサムで年上……！\x01",
            "ポイント高いわよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1C77")

    Jump("loc_2437")

    label("loc_1C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1D10")

    #C0030
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの男優は\x01",
            "好みで別れるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "どっちもステキだけど……\x01",
            "どちらかを選ぶなら\x01",
            "私はユージーン様を推すわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDE")

    label("loc_1D10")


    #C0032
    ChrTalk(
        0xFE,
        (
            "アルカンシェルって\x01",
            "男優の２人もステキよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "《金髪の王子》ユージーン様と\x01",
            "《沈黙の貴公子》テオドール様。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "うふふ、私はどちらかと言うと\x01",
            "ユージーン様派かなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "だって王子様なんだもの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1DDE")

    Jump("loc_2437")

    label("loc_1DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1E6E")

    #C0036
    ChrTalk(
        0xFE,
        (
            "最近、この辺りで\x01",
            "市長の第一秘書さんを見かけるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "……ちょっとステキな人でね、\x01",
            "私にも挨拶してくださるの㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F17")

    label("loc_1E6E")


    #C0038
    ChrTalk(
        0xFE,
        (
            "最近、この辺りで\x01",
            "きっちりした身なりの青年を\x01",
            "見かけるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "あの人……確か市長の\x01",
            "第一秘書じゃなかったかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "仕事熱心よね。\x01",
            "私にも挨拶してくださったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1F17")

    Jump("loc_2437")

    label("loc_1F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_201E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FBB")

    #C0041
    ChrTalk(
        0xFE,
        (
            "クロスベルの政治って\x01",
            "なんだかメチャクチャよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "でも市長だけは\x01",
            "信頼できる気がするの。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "私、市長のことは応援してるわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2019")

    label("loc_1FBB")


    #C0044
    ChrTalk(
        0xFE,
        (
            "市長ってほら、見た目も渋くて\x01",
            "いい感じじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "私、市長のことだけは\x01",
            "応援してるの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2019")

    Jump("loc_2437")

    label("loc_201E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_20B9")

    #C0046
    ChrTalk(
        0xFE,
        (
            "最近、この公園で\x01",
            "運動をする人が多い気がするわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "もしかして何かの\x01",
            "ブームだったりするのかしら。\x01",
            "……一応チェックしておこうっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2437")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2198")

    #C0048
    ChrTalk(
        0xFE,
        (
            "ミシュラムのテーマパークには\x01",
            "すごく大きな観覧車があるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "それからジェットコースターとか\x01",
            "ホラーハウスとかもあるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "私、ジェットコースターに乗ってみたいな。\x01",
            "まだ乗ったことないのよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2437")

    label("loc_2198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_22F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2225")

    #C0051
    ChrTalk(
        0xFE,
        (
            "最近公園の近くに\x01",
            "東方風の会社ができたみたいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "あまり社員の人も見かけないけど\x01",
            "何をしている会社なのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22EE")

    label("loc_2225")


    #C0053
    ChrTalk(
        0xFE,
        (
            "最近公園の近くに\x01",
            "東方風の会社ができたみたいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "東方風の赤くって\x01",
            "ちょっと可愛らしいビルなんだけど\x01",
            "いつの間にか建っていたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "……工事なんてしていたかしら。\x01",
            "私も気付かなかったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_22EE")

    Jump("loc_2437")

    label("loc_22F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C7")

    #C0056
    ChrTalk(
        0xFE,
        (
            "この辺りって、朝はスーツの人たちが\x01",
            "たくさん通りがかるのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "ああいうのって『ビジネスマン』って\x01",
            "呼ぶそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "……びしっとスーツを着た\x01",
            "男の人って……\x01",
            "ちょっとカッコイイわよね㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2437")

    label("loc_23C7")


    #C0059
    ChrTalk(
        0xFE,
        (
            "スーツを着た男の人って\x01",
            "ちょっとカッコイイわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "朝はたくさん見かけるから\x01",
            "ついつい目移りしちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2437")

    TalkEnd(0xFE)
    Return()

    # Function_12_1570 end

    def Function_13_243B(): pass

    label("Function_13_243B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2718")

    #C0061
    ChrTalk(
        0x101,
        (
            "#0000F（港湾区の公園……\x01",
            "  落し物をしたトロントさんが\x01",
            "  立ち寄っていた場所だな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0000Fすみません、この辺りで\x01",
            "落し物を見かけませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "ふむ、落し物を探しているのか？\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "そういえば……昨日そこの公園に\x01",
            "能天気な青年が来ていたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "途中から『バッグが破れてた～』\x01",
            "とか叫んで大騒ぎしていたが。\x02",
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
        "#0203F間違いないですね。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "だが私は\x01",
            "遠目に見ていただけなのでな。\x01",
            "落し物の類は知らないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0006Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "ふむ、だが……\x01",
            "今朝方、客の１人が\x01",
            "何かを拾ったと言っていたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "よくこの辺りを散歩している娘だ。\x01",
            "話を聞いてみるといいかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x2, 0x1, 0x3)
    TalkEnd(0xFE)
    Return()

    label("loc_2718")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27CD")

    #C0071
    ChrTalk(
        0xFE,
        (
            "今朝方、客の１人が\x01",
            "何かを拾ったと言っていたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "よくこの辺りを散歩している娘だ。\x01",
            "落し物を探しているなら\x01",
            "話を聞いてみるといいかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_27CD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2835")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2835")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2855")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3AF3")

    label("loc_2855")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2869")
    Jump("loc_3AF3")

    label("loc_2869")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2A93")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289E")
    Call(0, 14)
    Jump("loc_2A8E")

    label("loc_289E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_297B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2909")

    #C0073
    ChrTalk(
        0xFE,
        "この客人、中々見る目がある……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "最高の一品を\x01",
            "用意してやろうではないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2976")

    label("loc_2909")


    #C0075
    ChrTalk(
        0xFE,
        (
            "この客人は\x01",
            "一番コシの強い麺をご所望だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "フ……任せたまえ。\x01",
            "この私が最高の一品を用意してやろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2976")

    Jump("loc_2A8E")

    label("loc_297B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_29D1")

    #C0077
    ChrTalk(
        0xFE,
        (
            "あの記者は確か\x01",
            "クロスベルタイムズの……\x01",
            "一体何を調べているのかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8E")

    label("loc_29D1")


    #C0078
    ChrTalk(
        0xFE,
        (
            "あの記者たち、方々に\x01",
            "聞き込みまわっているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "私にも、それはもう\x01",
            "しつこく尋ねていったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "身内におかしくなった\x01",
            "人間は居ないかなど……\x01",
            "……一体何を調べているのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2A8E")

    Jump("loc_3AF3")

    label("loc_2A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2BC0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAF")
    Call(0, 14)
    Jump("loc_2BBB")

    label("loc_2AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2B17")

    #C0081
    ChrTalk(
        0xFE,
        (
            "あの商社の従業員は\x01",
            "ともかく肝が据わっておるようだ。\x01",
            "すっかり静かになってしまったぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBB")

    label("loc_2B17")


    #C0082
    ChrTalk(
        0xFE,
        (
            "一昨日襲撃されたという商社だが、\x01",
            "すっかり静かになってしまったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "壁に銃痕が残っているものの\x01",
            "従業員は慌てた風も無い……\x01",
            "よほど肝が据わっておるのだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2BBB")

    Jump("loc_3AF3")

    label("loc_2BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2D10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDC")
    Call(0, 14)
    Jump("loc_2D0B")

    label("loc_2BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2C3A")

    #C0084
    ChrTalk(
        0xFE,
        (
            "この程度の騒動で\x01",
            "店を諦めるつもりはないぞ。\x01",
            "フ……私を舐めないで貰おうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D0B")

    label("loc_2C3A")


    #C0085
    ChrTalk(
        0xFE,
        (
            "夜の間に事件があったようでな。\x01",
            "朝から警官が慌しくしているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "……私か？\x01",
            "私は店を辞めるつもりはないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "フ……この程度の騒動で\x01",
            "諦めるほどヤワではない。\x01",
            "私を待っている常連客もいるのだからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2D0B")

    Jump("loc_3AF3")

    label("loc_2D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2E58")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D2C")
    Call(0, 14)
    Jump("loc_2E53")

    label("loc_2D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2DA8")

    #C0088
    ChrTalk(
        0xFE,
        (
            "机に向かって書類を書き続けるなど、\x01",
            "一体どこが楽しいのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "ビジネスマンという\x01",
            "人種はよく分からぬな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E53")

    label("loc_2DA8")


    #C0090
    ChrTalk(
        0xFE,
        (
            "近頃、妙に調子のよい\x01",
            "客人がいるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "何でも会社の仕事が\x01",
            "バリバリとはかどって\x01",
            "非常に気持ちが良いとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "ふむ、ビジネスマンという\x01",
            "人種はよく分からぬな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2E53")

    Jump("loc_3AF3")

    label("loc_2E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2FD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2EE6")

    #C0093
    ChrTalk(
        0xFE,
        (
            "発音の事は、まあよい。\x01",
            "だがへんてこと\x01",
            "呼ぶのはやめてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "こういった屋台は\x01",
            "東方ではよくある物なのだぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCE")

    label("loc_2EE6")

    OP_63(0x153, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x153,
        (
            "#1110Fねえ、これもおミセ？\x01",
            "へんてこな形だねーっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "む……へんてこだと！？\x01",
            "東方風と言え！！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x153,
        "#1107F……とーほーふー！\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0098
    ChrTalk(
        0xFE,
        (
            "発音が違うのだが……\x01",
            "ま、まあよいか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2FCE")

    Jump("loc_3AF3")

    label("loc_2FD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_30DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_301D")

    #C0099
    ChrTalk(
        0xFE,
        (
            "フ……世の中は広いな。\x01",
            "私も精進するとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30D6")

    label("loc_301D")


    #C0100
    ChrTalk(
        0xFE,
        (
            "先日、東通りの\x01",
            "中華飯店に立ち寄ったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "中々よい麺を振舞っていた。\x01",
            "あれは私と互角か、\x01",
            "それ以上の腕前の持ち主……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "ムム……参ったな。\x01",
            "私もまだ修行不足ということか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_30D6")

    Jump("loc_3AF3")

    label("loc_30DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3231")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3171")

    #C0103
    ChrTalk(
        0xFE,
        (
            "クロスベルでは\x01",
            "『クロスベル商工会』に申請を出せば\x01",
            "出店を開けるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "面倒なお役所などと違って\x01",
            "実に話の判る連中だぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_322C")

    label("loc_3171")


    #C0105
    ChrTalk(
        0xFE,
        (
            "そろそろ記念祭だな……\x01",
            "祭りの出店として\x01",
            "登録を出さねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "ちなみにクロスベルの出店は\x01",
            "『クロスベル商工会』という所が\x01",
            "管理しているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "話の判る、中々よい団体だぞ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_322C")

    Jump("loc_3AF3")

    label("loc_3231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_346B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_32ED")

    #C0108
    ChrTalk(
        0xFE,
        (
            "以前、常連客に\x01",
            "若い警察コンビがいたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "よく麺を食いながら\x01",
            "警察の将来について語っていたものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0002F…………………………\x01",
            "（はは、もしかして……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3466")

    label("loc_32ED")


    #C0111
    ChrTalk(
        0xFE,
        (
            "私の店は\x01",
            "これで常連客も多いのだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "中には警察に勤めているという\x01",
            "青年コンビもいてな。\x01",
            "以前はよく立ち寄ってくれたものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "確か長身冷静な男と\x01",
            "栗髪の情熱をもった青年だったが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 500)
    Sleep(500)

    #C0114
    ChrTalk(
        0xFE,
        (
            "そう、栗髪の青年は\x01",
            "君に良く似ていたぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0115
    ChrTalk(
        0x101,
        "#0005Fえ、俺……ですか？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "そういえば雰囲気も似ているな。\x01",
            "フム、あの青年も誠実そうだったぞ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 0)
    SetScenarioFlags(0x0, 3)

    label("loc_3466")

    Jump("loc_3AF3")

    label("loc_346B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_35B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_34E8")

    #C0117
    ChrTalk(
        0xFE,
        (
            "私は今でも\x01",
            "麺の研究を続けているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "食してなにか意見があれば\x01",
            "忌憚なく聞かせてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35AC")

    label("loc_34E8")


    #C0119
    ChrTalk(
        0xFE,
        "今日の麺は一味違うぞ！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "太めにもかかわらず\x01",
            "しなやかにツユの中を泳ぐ麺……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "これはマインツ山道の\x01",
            "小川の水を使って打ったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "静謐で引き締まった麺、\x01",
            "君たちも食していくがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_35AC")

    Jump("loc_3AF3")

    label("loc_35B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_36DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_362F")

    #C0123
    ChrTalk(
        0xFE,
        "生憎と私は愚痴の聞き役ではない。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "君たちも、私に愚痴をこぼすような\x01",
            "真似はやめてくれたまえよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36DA")

    label("loc_362F")


    #C0125
    ChrTalk(
        0xFE,
        (
            "ビジネスマンという\x01",
            "職業は大層疲れるようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "仕事帰りに食していく客が多いのだが、\x01",
            "みな一様に愚痴をこぼしていくぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "……私は愚痴の聞き役ではないのだが。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_36DA")

    Jump("loc_3AF3")

    label("loc_36DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3760")

    #C0128
    ChrTalk(
        0xFE,
        (
            "フ……私は麺にかけては\x01",
            "並々ならぬこだわりがあるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "そこいらの屋台とは\x01",
            "格が違うのだよ、格が！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3813")

    label("loc_3760")


    #C0130
    ChrTalk(
        0xFE,
        (
            "屋台の麺だからといって\x01",
            "甘く見てもらっては困るな。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "私は毎朝自宅で麺を打ち、\x01",
            "適切な時間寝かせた物を\x01",
            "この場で茹でている。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "そこいらの屋台とは\x01",
            "格が違うのだよ、格が！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3813")

    Jump("loc_3AF3")

    label("loc_3818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3868")

    #C0133
    ChrTalk(
        0xFE,
        (
            "さあ遠慮する事はない。\x01",
            "うちの麺を食してみるがいい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_391D")

    label("loc_3868")


    #C0134
    ChrTalk(
        0xFE,
        (
            "私は祖父の代から続いた\x01",
            "店を捨て、屋台を始めたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "これもより良い麺を\x01",
            "極めるための修行……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "より多くの意見を\x01",
            "拝聴するための選択だ。\x01",
            "君たちもぜひ食していくがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_391D")

    Jump("loc_3AF3")

    label("loc_3922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3A36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_39A1")

    #C0137
    ChrTalk(
        0xFE,
        (
            "この辺りには、旧市街の\x01",
            "不良達が現れる事があるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "まったく……\x01",
            "口に麺を押し込んでやろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A31")

    label("loc_39A1")


    #C0139
    ChrTalk(
        0xFE,
        (
            "この辺りには、時々\x01",
            "旧市街の不良達が現れる事がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "夕方から夜にかけて\x01",
            "バカ騒ぎを始めたりしてな。\x01",
            "こちらとしては多分に迷惑な話だ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3A31")

    Jump("loc_3AF3")

    label("loc_3A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3A83")

    #C0141
    ChrTalk(
        0xFE,
        (
            "うちの麺は天下一品だぞ。\x01",
            "嘘だと思うなら試してみるがいい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF3")

    label("loc_3A83")


    #C0142
    ChrTalk(
        0xFE,
        "麺はコシだ！\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        "こうキュキュッ、ドーンと来る奴だ！\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "どうかな、君たちも\x01",
            "一杯引っ掛けていかないか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3AF3")

    Jump("loc_27D7")

    label("loc_3AF8")

    TalkEnd(0xFE)
    Return()

    # Function_13_243B end

    def Function_14_3AFC(): pass

    label("Function_14_3AFC")


    #C0145
    ChrTalk(
        0xFE,
        (
            "新しい味に挑戦しようと思って\x01",
            "龍老飯店のタンメンを\x01",
            "作ってみたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "やはりマネはだめだな。\x01",
            "このレシピはお前たちにやるとしよう。\x02",
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
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x191),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x1)
    Return()

    # Function_14_3AFC end

    def Function_15_3BFF(): pass

    label("Function_15_3BFF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3C7D")

    #C0149
    ChrTalk(
        0xFE,
        (
            "ＩＢＣのセキュリティは\x01",
            "世界屈指らしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "ミラも掛けてるらしいし……\x01",
            "警察より上手かもね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D25")

    label("loc_3C7D")


    #C0151
    ChrTalk(
        0xFE,
        "ＩＢＣの保安部って凄いよね。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "郵送物も導力探知機で\x01",
            "全部チェックしてるらしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "警備に立ってるのは\x01",
            "気のいい人ばかりだけど、\x01",
            "みんな優秀なんだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3D25")

    Jump("loc_4349")

    label("loc_3D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3D90")

    #C0154
    ChrTalk(
        0xFE,
        (
            "今日はまだ\x01",
            "空輸便の荷物が届いてないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "おかしいなぁ……\x01",
            "どうなってんだろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4349")

    label("loc_3D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3DDF")

    #C0156
    ChrTalk(
        0xFE,
        (
            "今日は警察車両が\x01",
            "よく停まってるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        "何かあったのかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4349")

    label("loc_3DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3EFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3E4F")

    #C0158
    ChrTalk(
        0xFE,
        (
            "こうしてクロスベルは\x01",
            "ますます繁栄するって訳だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        "僕らの仕事は増えちゃうけどね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EF8")

    label("loc_3E4F")


    #C0160
    ChrTalk(
        0xFE,
        (
            "記念祭からこっち、\x01",
            "ビジネス街は随分賑わってるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "記念祭の賑わいを見て\x01",
            "会社進出を考えている人も\x01",
            "多いみたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "また仕事が増えちゃうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3EF8")

    Jump("loc_4349")

    label("loc_3EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3F6B")

    #C0163
    ChrTalk(
        0xFE,
        (
            "しまった、今日は\x01",
            "ＩＢＣは休行日だった……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "あーあ、余計な荷物まで\x01",
            "運んできちゃったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4349")

    label("loc_3F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4071")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3FF6")

    #C0165
    ChrTalk(
        0xFE,
        (
            "最近じゃ導力ネットとかいうのを\x01",
            "引いてる企業もあるらしいし、\x01",
            "その部品か何かかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "取り扱いにも気を遣うよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_406C")

    label("loc_3FF6")


    #C0167
    ChrTalk(
        0xFE,
        (
            "最近、精密機器って書かれた\x01",
            "小包が増えてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "結晶回路か何かみたいだね。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "取り扱いにも気を遣うよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_406C")

    Jump("loc_4349")

    label("loc_4071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_40E3")

    #C0170
    ChrTalk(
        0xFE,
        (
            "会社によっては\x01",
            "チップを弾んでくれる所もあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "そういう所に\x01",
            "配達に行くのは楽しみだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4349")

    label("loc_40E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_412A")

    #C0172
    ChrTalk(
        0xFE,
        (
            "うちの会社も導力車を\x01",
            "買ってくれればいいのになぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4349")

    label("loc_412A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4199")

    #C0173
    ChrTalk(
        0xFE,
        (
            "この前の休暇、急に仕事が\x01",
            "入ってキャンセルになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        "とほほ……サービス業は辛いね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4349")

    label("loc_4199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_41FC")

    #C0175
    ChrTalk(
        0xFE,
        (
            "今度の休暇はミシュラムで\x01",
            "のんびり過ごす予定なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        "今から待ちきれないよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4349")

    label("loc_41FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_425D")

    #C0177
    ChrTalk(
        0xFE,
        "うーん、この会社はどこだ？\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "最近出来たビルらしくて\x01",
            "住所がぴんと来ないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4349")

    label("loc_425D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_42BE")

    #C0179
    ChrTalk(
        0xFE,
        (
            "旧市街の方で\x01",
            "乱闘騒ぎがあったんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "怖いなぁ、僕らも気を付けないと。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4349")

    label("loc_42BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4309")

    #C0181
    ChrTalk(
        0xFE,
        (
            "この辺りは会社ばっかりだな。\x01",
            "小包が多くてかなわないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4349")

    label("loc_4309")


    #C0182
    ChrTalk(
        0xFE,
        "ふう、次の配達先はっと……\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        "ほらほら、どいてどいて～！\x02",
    )

    CloseMessageWindow()

    label("loc_4349")

    TalkEnd(0xFE)
    Return()

    # Function_15_3BFF end

    def Function_16_434D(): pass

    label("Function_16_434D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_441A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_43B9")

    #C0184
    ChrTalk(
        0xFE,
        (
            "孫娘には随分と\x01",
            "心配をかけてきたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "ワシも少し\x01",
            "頑固が過ぎたかのう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4415")

    label("loc_43B9")


    #C0186
    ChrTalk(
        0xFE,
        "……孫娘はほんにいい子じゃの。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "年寄りがあまり\x01",
            "心配を掛けるもんじゃないのう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4415")

    Jump("loc_4E27")

    label("loc_441A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_452E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4497")

    #C0188
    ChrTalk(
        0xFE,
        (
            "孫娘は今日に限って\x01",
            "一日付き合うというんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "……まさかワシの身を\x01",
            "案じておるのかのう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4529")

    label("loc_4497")


    #C0190
    ChrTalk(
        0xFE,
        (
            "孫娘には家に帰っとれと\x01",
            "言ったんじゃがな……\x02",
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
            "昨日は発砲事件もあったそうじゃ。\x01",
            "子供は帰っとるべきじゃわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4529")

    Jump("loc_4E27")

    label("loc_452E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_45D4")
    TurnDirection(0xFE, 0x0, 0)

    #C0192
    ChrTalk(
        0xFE,
        "まったく物騒な事件じゃな。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "……今日は孫娘は\x01",
            "帰らせた方がよいじゃろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "孫娘にだけは危ない目に\x01",
            "遭わせたくないもんじゃて。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    Jump("loc_4E27")

    label("loc_45D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4657")

    #C0195
    ChrTalk(
        0xFE,
        "薬なんぞ飲みとうないわい。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        "ワシは釣りさえできれば十分。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "ワシは余生を\x01",
            "こうやって過ごすと決めたんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E27")

    label("loc_4657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_46C3")

    #C0198
    ChrTalk(
        0xFE,
        (
            "記念祭の間は\x01",
            "ろくに釣れんかったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "フン、どいつもこいつも\x01",
            "浮かれおってからに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E27")

    label("loc_46C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_476B")

    #C0200
    ChrTalk(
        0xFE,
        "……孫娘の気持ちも分かっとるんじゃ。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "この子はええ子じゃ。\x01",
            "心が清らかでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "じゃがワシは老い先短いんじゃ。\x01",
            "人生の最後、好きにさせてくれい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E27")

    label("loc_476B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_47C6")

    #C0203
    ChrTalk(
        0xFE,
        "……今日は娘が来とるんじゃ。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "フン、悪いがワシは\x01",
            "今日も忙しいでな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E27")

    label("loc_47C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_482F")

    #C0205
    ChrTalk(
        0xFE,
        "釣りだけがワシの楽しみ……\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "今日も一日釣りで潰すんじゃ。\x01",
            "邪魔せんでもらおうかい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E27")

    label("loc_482F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_48F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4871")

    #C0207
    ChrTalk(
        0xFE,
        (
            "へっ、ワシは\x01",
            "群れるのは好かんのじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48F1")

    label("loc_4871")


    #C0208
    ChrTalk(
        0xFE,
        (
            "最近『釣公師団』とかいう\x01",
            "連中が勧誘にくるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        "へっ、ワシは群れるのは好かん。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        "なにが『楽しく釣りを』じゃ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_48F1")

    Jump("loc_4E27")

    label("loc_48F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_496A")

    #C0211
    ChrTalk(
        0xFE,
        (
            "ワシは残りの命を\x01",
            "釣り三昧で過ごすと決めたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        "孫娘には悪いが、薬なんぞいらん。\x02",
    )

    CloseMessageWindow()
    Jump("loc_496D")

    label("loc_496A")

    Call(0, 18)

    label("loc_496D")

    Jump("loc_4E27")

    label("loc_4972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_49BE")

    #C0213
    ChrTalk(
        0xFE,
        (
            "これではろくな魚が掛からんわい。\x01",
            "まったく……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A28")

    label("loc_49BE")


    #C0214
    ChrTalk(
        0xFE,
        "チッ、水上バスなんぞ走らせおって……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "ワシの邪魔をする気じゃな。\x01",
            "気に入らん、頭にくるわい……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4A28")

    Jump("loc_4E27")

    label("loc_4A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4C0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4B01")

    #C0216
    ChrTalk(
        0xFE,
        (
            "警察の中でも捜査一課には\x01",
            "デキル男が集まっておるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "何年か前に出会った捜査官など\x01",
            "若いくせにいい眼をしておった……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "あのくらい熱意と実力のある\x01",
            "男でないと、ワシは認めんぞ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C05")

    label("loc_4B01")


    #C0219
    ChrTalk(
        0xFE,
        "クロスベルの役人どもは信用できん。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        "中でも最悪なのが警察じゃな。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "ろくに事件の捜査もせんし、\x01",
            "政治家どもの圧力で\x01",
            "悪党を保釈することもあるという。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "フン、どこまでも不甲斐ない連中じゃ。\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "ワシが認めとるのは\x01",
            "『捜査一課』くらいのもんじゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4C05")

    Jump("loc_4E27")

    label("loc_4C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4D6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4C61")

    #C0224
    ChrTalk(
        0xFE,
        "へっ、ワシはクロスベル人は好かん。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        "反吐が出るほどな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D6A")

    label("loc_4C61")


    #C0226
    ChrTalk(
        0xFE,
        "ワシはクロスベル人は好かん。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "金儲けばかり考えておるし\x01",
            "古い伝統や規則を大切にせんし……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "流行に流されやすいわ\x01",
            "ゴシップ記事が大好きだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "おまけに揃って祭り好きときた。\x01",
            "バカ騒ぎばかりしとる連中じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "……まあ、ワシも\x01",
            "クロスベル育ちじゃが？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4D6A")

    Jump("loc_4E27")

    label("loc_4D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4DAE")

    #C0231
    ChrTalk(
        0xFE,
        (
            "どいつもこいつも\x01",
            "なっちょらん、ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E27")

    label("loc_4DAE")


    #C0232
    ChrTalk(
        0xFE,
        (
            "なんじゃ、若いの。\x01",
            "ワシの邪魔をする気かい。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "さっさと退散するがええ。\x01",
            "魚が逃げてしまうじゃろが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    SetChrFlags(0xB, 0x10)
    OP_93(0xB, 0xB4, 0x0)

    label("loc_4E27")

    TalkEnd(0xFE)
    Return()

    # Function_16_434D end

    def Function_17_4E2B(): pass

    label("Function_17_4E2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4EA3")

    #C0234
    ChrTalk(
        0xFE,
        (
            "あんまりうるさく\x01",
            "言わない事にしたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "だっておじいちゃん、\x01",
            "すっごく元気なんだもん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F54")

    label("loc_4EA3")


    #C0236
    ChrTalk(
        0xFE,
        (
            "あんまりおじいちゃんに\x01",
            "うるさく言わない事にしたんだー。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "ほんとは病院に通って\x01",
            "お薬も飲んでほしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "おじいちゃん、\x01",
            "何だかんだ言って\x01",
            "すっごく元気だもんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4F54")

    Jump("loc_541E")

    label("loc_4F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_504B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4F9B")

    #C0239
    ChrTalk(
        0xFE,
        (
            "今日はお魚、\x01",
            "いっぱい釣れるといいね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5046")

    label("loc_4F9B")


    #C0240
    ChrTalk(
        0xFE,
        (
            "あのね、今日は\x01",
            "おじいちゃんに\x01",
            "付き合ってあげるんだー。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "だっておじいちゃん\x01",
            "１人じゃ心配だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "釣りをしてるおじいちゃんって\x01",
            "たのしそうで好きなんだもん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_5046")

    Jump("loc_541E")

    label("loc_504B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_507B")

    #C0243
    ChrTalk(
        0xFE,
        "あれ～、何かあったのかなぁ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_541E")

    label("loc_507B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_50F8")

    #C0244
    ChrTalk(
        0xFE,
        (
            "はいおじいちゃん、\x01",
            "またお薬もらってきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "ちゃんと飲んでるの？\x01",
            "先生のいうこと\x01",
            "聞かなきゃダメだよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_541E")

    label("loc_50F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_51DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_514C")

    #C0246
    ChrTalk(
        0xFE,
        (
            "来年はおじいちゃんと\x01",
            "たのしく回れたらいいんだけどなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D6")

    label("loc_514C")


    #C0247
    ChrTalk(
        0xFE,
        (
            "はあ、記念祭\x01",
            "終わっちゃったねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "わたし、結局\x01",
            "遊びにいけなかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "おじいちゃんと一緒に\x01",
            "回りたかったんだけどなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_51D6")

    Jump("loc_541E")

    label("loc_51DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_52D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_521F")

    #C0250
    ChrTalk(
        0xFE,
        (
            "ふう、何とかして\x01",
            "あげたいんだけどな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52D3")

    label("loc_521F")


    #C0251
    ChrTalk(
        0xFE,
        (
            "おじいちゃん、\x01",
            "去年まで入院してたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "だけど病院なんて気に入らないって\x01",
            "言って、抜け出してきちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "ふう、気持ちは分かるけど……\x01",
            "このままじゃよくないよね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_52D3")

    Jump("loc_541E")

    label("loc_52D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_53AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5357")

    #C0254
    ChrTalk(
        0xFE,
        (
            "おじいちゃん、いつも\x01",
            "しかめっ面で釣りばかりなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "病院のお薬も飲まないし……\x01",
            "ふう、心配かも。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53AA")

    label("loc_5357")


    #C0256
    ChrTalk(
        0xFE,
        (
            "おじいちゃん、今日は\x01",
            "東通りの方に行ってみない？\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        "ね、一緒に遊ぼ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xC, 0x10)

    label("loc_53AA")

    Jump("loc_541E")

    label("loc_53AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_541B")

    #C0258
    ChrTalk(
        0xFE,
        (
            "ウチのおじいちゃん、\x01",
            "すっごい頑固なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "その上病院嫌いだし……\x01",
            "ふう、困ったなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_541E")

    label("loc_541B")

    Call(0, 18)

    label("loc_541E")

    TalkEnd(0xFE)
    Return()

    # Function_17_4E2B end

    def Function_18_5422(): pass

    label("Function_18_5422")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0260
    ChrTalk(
        0xC,
        (
            "おじいちゃん、\x01",
            "お薬持って来たよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        (
            "ねえ……ちゃんと\x01",
            "毎日飲んでるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xB,
        "うるさいのぅ……\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xB,
        (
            "薬なんぞいらん。\x01",
            "さっさと帰れ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "またそんなこと言って……\x01",
            "ダメだよ、おじいちゃん！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xC, 0x10)
    Return()

    # Function_18_5422 end

    def Function_19_54FB(): pass

    label("Function_19_54FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55A0")

    #C0265
    ChrTalk(
        0xFE,
        "おや……\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "ティオ君、こんな時間から\x01",
            "どこかに行くのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "警察の仕事も大変だね……\x01",
            "気を付けるんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x103,
        "#0200Fはい、大丈夫です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_55E3")

    label("loc_55A0")


    #C0269
    ChrTalk(
        0xFE,
        "警察の仕事も大変だね。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "ティオ君にみんな、\x01",
            "気をつけてね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E3")

    TalkEnd(0xFE)
    Return()

    # Function_19_54FB end

    def Function_20_55E7(): pass

    label("Function_20_55E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5656")

    #C0271
    ChrTalk(
        0xFE,
        (
            "グレイス先輩、朝から妙に\x01",
            "この噂に拘ってるんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        "何かあるんですかね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5710")

    label("loc_5656")


    #C0273
    ChrTalk(
        0xFE,
        (
            "今朝から行方が判らない人が\x01",
            "相次いでいるって噂があるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "いま聞き込みをして\x01",
            "情報集めてる所なんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "記事になるような事件なんですか？\x01",
            "確かに変な話ですけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_5710")

    Jump("loc_58BD")

    label("loc_5715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5786")

    #C0276
    ChrTalk(
        0xFE,
        (
            "ああ、はやく帰りたい……\x01",
            "でも先輩を置いていくわけには……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        "はうう、僕は一体どうすれば……\x02",
    )

    CloseMessageWindow()
    Jump("loc_58BD")

    label("loc_5786")


    #C0278
    ChrTalk(
        0xFE,
        "はわわ、どうしよう……\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "グレイス先輩、僕をおいて\x01",
            "直撃取材に行っちゃたんですよ！\x02",
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
        "#0005Fま、まさか……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        "#0205F黒月の事務所に、ですか？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        "……コクリ。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "先輩……もうやめて下さいよう。\x01",
            "僕ついて行けませんよ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    SetScenarioFlags(0xD0, 3)

    label("loc_58BD")

    TalkEnd(0xFE)
    Return()

    # Function_20_55E7 end

    def Function_21_58C1(): pass

    label("Function_21_58C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 4)), scpexpr(EXPR_END)), "loc_5A0A")

    #C0284
    ChrTalk(
        0x1A,
        (
            "#2103Fルバーチェといい、\x01",
            "行方不明の市民といい……\x02\x03",

            "何だかちょっと\x01",
            "ヤバイかもしれないわね。\x02\x03",

            "#2101F君たちも捜査を続けるなら\x01",
            "くれぐれも気をつけてね。\x02\x03",

            "#2109Fそれで無事、大スクープを\x01",
            "あたしに提供してちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A05")

    #C0285
    ChrTalk(
        0x101,
        "#0002Fはは……判りました。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        (
            "#0104Fグレイスさんも\x01",
            "あまり無理はなさらずに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_5A05")

    Jump("loc_5D82")

    label("loc_5A0A")


    #C0287
    ChrTalk(
        0x1A,
        (
            "#2105Fあら、支援課の面々じゃない。\x02\x03",

            "#2101Fマフィアたちの姿が\x01",
            "消えちゃったってホント？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        "#0011Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        (
            "#0101Fその情報……\x01",
            "どこで聞かれたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x1A,
        (
            "#2103Fま、あたしたちにも\x01",
            "ちょっとした情報網があってね。\x02\x03",

            "それとは別に、昨日のガンツさんも\x01",
            "消えちゃったって聞いたし……\x02\x03",

            "#2101Fそれ以外にも行方が判らない人が\x01",
            "市内で急増してるらしいのよ。\x02\x03",

            "これって……な～んか\x01",
            "ヤバイ気がするんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#0013F……ええ。\x01",
            "とにかく何が起こっているのか\x01",
            "一刻も早く掴まないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x1A,
        (
            "#2104Fふむ、ということは君たちも\x01",
            "追っかけてる最中って訳か……\x01",
            "（サラサラ……）\x02\x03",

            "#2110Fオーケー、大体分かったわ。\x01",
            "また何かあったら知らせて頂戴！\x02",
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
            "#0211Fロイドさん、\x01",
            "喋ってしまいましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        (
            "#0006F……面目ない。\x01",
            "気をつけてはいたんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x104,
        (
            "#0300Fまあ、今のは仕方ねえさ。\x01",
            "ドンマイ、ドンマイ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 4)

    label("loc_5D82")

    TalkEnd(0xFE)
    Return()

    # Function_21_58C1 end

    def Function_22_5D86(): pass

    label("Function_22_5D86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_602E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FEC")
    OP_4B(0x1D, 0xFF)
    OP_4B(0x1E, 0xFF)

    #C0296
    ChrTalk(
        0x1D,
        (
            "や、やあパール。\x01",
            "久しぶりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x1E,
        "ええ、ホント。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x1E,
        (
            "……私のことなんて\x01",
            "すっかり忘れてると思ってた。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0299
    ChrTalk(
        0x1D,
        (
            "い、いやそれは！\x01",
            "遊撃士の仕事が\x01",
            "忙しかったからで……！\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x1E,
        "……ふふ、冗談よ㈱\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x1E,
        (
            "あなたが遊撃士を頑張ってるのは\x01",
            "私が一番よく分かってるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x1D,
        "パ、パール……㈱\x02",
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
        "#1109F……いいフンイキだねー！\x02",
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
            "#0006F（キ、キーア！\x01",
            "  邪魔しちゃだめだって……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x1E,
        "え、えーっと……\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x1D,
        "は、はは……\x02",
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x5A, 0x0)
    OP_93(0x1E, 0x10E, 0x0)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x1E, 0xFF)
    SetScenarioFlags(0x1, 3)
    Jump("loc_602E")

    label("loc_5FEC")


    #C0307
    ChrTalk(
        0xFE,
        (
            "そ、それじゃあ……\x01",
            "気を取り直して、\x01",
            "ご飯でも食べに行こうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_602E")

    TalkEnd(0xFE)
    Return()

    # Function_22_5D86 end

    def Function_23_6032(): pass

    label("Function_23_6032")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6091")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6050")
    Call(0, 22)
    Jump("loc_6091")

    label("loc_6050")


    #C0308
    ChrTalk(
        0xFE,
        "……ええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "せっかくだし、\x01",
            "色々歩きましょうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6091")

    TalkEnd(0xFE)
    Return()

    # Function_23_6032 end

    def Function_24_6095(): pass

    label("Function_24_6095")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6129")
    Jump("loc_6173")

    label("loc_6129")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6149")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6173")

    label("loc_6149")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6169")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6173")

    label("loc_6169")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6173")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_620C")

    #C0310
    ChrTalk(
        0xFE,
        (
            "あらら、このお料理\x01",
            "美味しいわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "そこの出店で買ったのだけど。\x01",
            "何だか懐かしい味がするわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6292")

    label("loc_620C")


    #C0312
    ChrTalk(
        0xFE,
        (
            "ちょうどいい所に\x01",
            "公園があったから休んでいるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "やれやれ、クロスベル市は広いわねえ。\x01",
            "子供連れで回るなんて無茶だったかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6292")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_6095 end

    def Function_25_629A(): pass

    label("Function_25_629A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_62DE")

    #C0314
    ChrTalk(
        0xFE,
        (
            "そこの出店のおそば、\x01",
            "とってもおいしかったよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6324")

    label("loc_62DE")


    #C0315
    ChrTalk(
        0xFE,
        "歩き回って疲れちゃったよー。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        "アイスクリームが食べたいな～。\x02",
    )

    CloseMessageWindow()

    label("loc_6324")

    TalkEnd(0xFE)
    Return()

    # Function_25_629A end

    def Function_26_6328(): pass

    label("Function_26_6328")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_63B5")

    #C0317
    ChrTalk(
        0xFE,
        (
            "お昼を食べてたら\x01",
            "乗り遅れちゃったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        "意外と早く次の便が来たよ。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "もしかして\x01",
            "焦らなくてよかったのかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6438")

    label("loc_63B5")


    #C0320
    ChrTalk(
        0xFE,
        (
            "ふむふむ、ミシュラム行き\x01",
            "水上バスの乗り場っていうのはここか。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "ミシュラムには\x01",
            "綺麗なお店が沢山あるって聞くし\x01",
            "楽しみだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6438")

    TalkEnd(0xFE)
    Return()

    # Function_26_6328 end

    def Function_27_643C(): pass

    label("Function_27_643C")

    TalkBegin(0xFE)

    #C0322
    ChrTalk(
        0xFE,
        "娘とミシュラムに行ってくるの。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "水上バスで行くなんて\x01",
            "ワクワクしちゃうわねえ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_643C end

    def Function_28_649A(): pass

    label("Function_28_649A")

    TalkBegin(0xFE)

    #C0324
    ChrTalk(
        0xFE,
        "わーい、おっきなお船だ～！\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        "あたし船に乗るの初めて～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_649A end

    def Function_29_64E1(): pass

    label("Function_29_64E1")

    TalkBegin(0xFE)

    #C0326
    ChrTalk(
        0xFE,
        (
            "ミシュラムには\x01",
            "沢山遊ぶ場所があると聞くぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        "むほほ、楽しみじゃのう。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_64E1 end

    def Function_30_6537(): pass

    label("Function_30_6537")

    TalkBegin(0xFE)

    #C0328
    ChrTalk(
        0xFE,
        (
            "ヒソヒソ……\x01",
            "やっぱりルバーチェの仕業よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        "これだからマフィアは怖いのよ……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_6537 end

    def Function_31_6595(): pass

    label("Function_31_6595")

    TalkBegin(0xFE)

    #C0330
    ChrTalk(
        0xFE,
        (
            "黒月貿易公司……\x01",
            "聞かない会社だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "何か恨まれることでも\x01",
            "やっちまったのか？\x01",
            "くわばら、くわばら……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_6595 end

    def Function_32_660B(): pass

    label("Function_32_660B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669C")

    #C0332
    ChrTalk(
        0xFE,
        "時々あるんだよね、こういう事件……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "でもオフィス街の会社が\x01",
            "襲われるなんて初めてかも。\x01",
            "さすがにビックリしちまうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_66F7")

    label("loc_669C")


    #C0334
    ChrTalk(
        0xFE,
        "警察も何をしてたんだろ。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "いっつも事件が起こってから\x01",
            "のんびり来るんだからさぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F7")

    TalkEnd(0xFE)
    Return()

    # Function_32_660B end

    def Function_33_66FB(): pass

    label("Function_33_66FB")

    TalkBegin(0xFE)
    OP_4B(0x17, 0xFF)

    #C0336
    ChrTalk(
        0xFE,
        "わ、穴ぼこだ～。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0xFE, 500)
    Sleep(300)

    #C0337
    ChrTalk(
        0x17,
        "しっ、近づいちゃダメよ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x17, 0x2D, 0x0)
    OP_4C(0x17, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_33_66FB end

    def Function_34_674F(): pass

    label("Function_34_674F")

    TalkBegin(0xFE)

    #C0338
    ChrTalk(
        0xFE,
        (
            "この公園、時々遊ばせに\x01",
            "来てたってのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "まったく、警察は\x01",
            "何をしてたのかしら……！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_674F end

    def Function_35_67B4(): pass

    label("Function_35_67B4")

    TalkBegin(0xFE)

    #C0340
    ChrTalk(
        0xFE,
        "……何か御用でしょうか？\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        "#0005Fいえ、特には……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 3)), scpexpr(EXPR_END)), "loc_682B")

    #C0342
    ChrTalk(
        0x102,
        (
            "#0106F（グレイスさんも\x01",
            "  相当な人よね……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_682B")

    TalkEnd(0xFE)
    Return()

    # Function_35_67B4 end

    def Function_36_682F(): pass

    label("Function_36_682F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_689E")

    #C0343
    ChrTalk(
        0xFE,
        (
            "ミシュラムに向かわれる方は\x01",
            "少々お待ちくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "当便は５分後に\x01",
            "出航となります。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A3A")

    label("loc_689E")


    #C0345
    ChrTalk(
        0xFE,
        (
            "ミシュラムに向かわれる方は\x01",
            "少々お待ちくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "当便は５分後に\x01",
            "出航となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#0005Fへえ、これが有名な\x01",
            "《ミシュラム》行きの水上バスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#0300Fテーマパークとか\x01",
            "ショッピング街とか\x01",
            "色々遊べる場所だよな。\x02\x03",

            "#0305F……ってロイド、\x01",
            "お前行った事ねえのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#0006Fいやだって、俺が\x01",
            "クロスベルを離れている間に\x01",
            "できた施設だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x102,
        (
            "#0100Fまあいずれにせよ\x01",
            "今は乗り込んでいる暇は無いわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_6A3A")

    TalkEnd(0xFE)
    Return()

    # Function_36_682F end

    def Function_37_6A3E(): pass

    label("Function_37_6A3E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_END)), "loc_6C63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_6AF8")

    #C0351
    ChrTalk(
        0xFE,
        (
            "そういえばさっき\x01",
            "ダドリーさんとエマさんにも\x01",
            "ジロッて睨まれたんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "黒月の構成員もウロウロしてるし……\x01",
            "こんな場所で見張りなんて\x01",
            "やりたくないぜ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C5E")

    label("loc_6AF8")


    #C0353
    ChrTalk(
        0xFE,
        (
            "はあ、さっきから\x01",
            "黒月の構成員が\x01",
            "ウロウロしてるんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "あ、構成員じゃなくて\x01",
            "“社員”だっけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "今は居なくなったけど……\x01",
            "また出てくるんだろうなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#0003Fすまんフランツ、ここを頼む。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        (
            "#0200Fまあ襲ってくる事は無いでしょう。\x01",
            "安心していいかと。\x02",
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
            "まあそうなんだけど……\x01",
            "そう簡単に安心できないって。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)

    label("loc_6C5E")

    Jump("loc_6CFC")

    label("loc_6C63")


    #C0359
    ChrTalk(
        0xFE,
        (
            "真夜中とはいえ\x01",
            "こんな公園の近くで\x01",
            "ドンパチやらかすなんてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "あ、ダドリーさんには適当に\x01",
            "誤魔化しといてくれよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        "俺まだ睨まれたくないし。\x02",
    )

    CloseMessageWindow()

    label("loc_6CFC")

    TalkEnd(0xFE)
    Return()

    # Function_37_6A3E end

    def Function_38_6D00(): pass

    label("Function_38_6D00")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6D56")

    #C0362
    ChrTalk(
        0xFE,
        (
            "ええい、今回は僕だって役を貰うんだ！\x01",
            "えっほっ……えっほっ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7015")

    label("loc_6D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6E16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DDA")

    #C0363
    ChrTalk(
        0xFE,
        "セ、セリーヌ先輩が来てる……！？\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "来週は配役の発表だもんな。\x01",
            "誰だってゆっくりしてられないか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6E11")

    label("loc_6DDA")


    #C0365
    ChrTalk(
        0xFE,
        (
            "いよいよ来週発表……\x01",
            "はあ、プレッシャーだなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E11")

    Jump("loc_7015")

    label("loc_6E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6EDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EAE")

    #C0366
    ChrTalk(
        0xFE,
        (
            "毎日走りこみをしてると\x01",
            "腹がへって仕方ないんだよなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "でも体重増えると\x01",
            "ジャンプ力が落ちるし……\x01",
            "はあ、辛いよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6ED9")

    label("loc_6EAE")


    #C0368
    ChrTalk(
        0xFE,
        (
            "はあ、頑張って\x01",
            "もっと鍛えないとな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ED9")

    Jump("loc_7015")

    label("loc_6EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6F80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F5D")

    #C0369
    ChrTalk(
        0xFE,
        "えっほっ……えっほっ……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "……この公園って\x01",
            "うまそうな出店が出てるよね。\x01",
            "う～、気になる……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6F7B")

    label("loc_6F5D")


    #C0371
    ChrTalk(
        0xFE,
        "あー、腹が減ったなぁ……\x02",
    )

    CloseMessageWindow()

    label("loc_6F7B")

    Jump("loc_7015")

    label("loc_6F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7015")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FE8")

    #C0372
    ChrTalk(
        0xFE,
        "えっほっ……えっほっ……\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "……ぜえぜえ……\x01",
            "まずは基礎体力だよな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_7015")

    label("loc_6FE8")


    #C0374
    ChrTalk(
        0xFE,
        (
            "な、なんだい……？\x01",
            "邪魔しないでくれよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7015")

    TalkEnd(0xFE)
    Return()

    # Function_38_6D00 end

    def Function_39_7019(): pass

    label("Function_39_7019")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7136")

    label("loc_7025")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_704F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_7042")
    OP_4C(0x20, 0xFF)
    Jump("loc_7047")

    label("loc_7042")

    Jump("loc_704F")

    label("loc_7047")

    Sleep(200)
    Jump("loc_7025")

    label("loc_704F")

    OP_4B(0x20, 0xFF)
    TurnDirection(0xFE, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70DA")

    #C0375
    ChrTalk(
        0xFE,
        (
            "もうすぐ配役の正式発表ですし、\x01",
            "のんびりしていられませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "お休みの日にも\x01",
            "練習に励みませんと……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_712D")

    label("loc_70DA")


    #C0377
    ChrTalk(
        0xFE,
        "私、今回は準主役の狙ってますの。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "絶対にいい役を\x01",
            "いただくんですから……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_712D")

    OP_4C(0x20, 0xFF)
    Jump("loc_71FB")

    label("loc_7136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_71FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71D9")

    #C0379
    ChrTalk(
        0xFE,
        (
            "ニコルの奴、こんな所で\x01",
            "走りこみをしてましたのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        "私も負けてられませんわ！\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "ただでさえリーシャに……\x01",
            "…………なのに………\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_71FB")

    label("loc_71D9")


    #C0382
    ChrTalk(
        0xFE,
        "わ、私も負けてられませんわ！\x02",
    )

    CloseMessageWindow()

    label("loc_71FB")

    TalkEnd(0xFE)
    Return()

    # Function_39_7019 end

    def Function_40_71FF(): pass

    label("Function_40_71FF")

    TalkBegin(0xFE)

    #N0383
    NpcTalk(
        0x24,
        "東方風の男",
        (
            "#5P支社長が会われるそうです。\x01",
            "──どうぞ中へ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_71FF end

    def Function_41_7245(): pass

    label("Function_41_7245")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0384
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7314")
    OP_E0(0x2)
    MiniGame(0x6, 0x1, 0x10BE4, 0xFFFFF63C, 0x4074, 0xB4, 0x109C8, 0xFFFFF254, 0x2E2C)

    label("loc_7314")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_41_7245 end

    def Function_42_7319(): pass

    label("Function_42_7319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7335")
    TalkBegin(0xFF)
    Call(0, 43)
    TalkEnd(0xFF)
    Jump("loc_7461")

    label("loc_7335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_734B")
    Call(0, 45)
    Jump("loc_7461")

    label("loc_734B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7367")
    TalkBegin(0xFF)
    Call(0, 43)
    TalkEnd(0xFF)
    Jump("loc_7461")

    label("loc_7367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7458")
    TalkBegin(0xFF)
    Call(0, 43)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7450")

    #C0386
    ChrTalk(
        0x101,
        (
            "#0001F（もう一度中に入れてもらう……\x01",
            "  ……のは難しそうだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#0103F（あの支社長も\x01",
            "  色々と“仕事”をしている\x01",
            "  最中なんでしょう……）\x02\x03",

            "#0101F（話が聞けただけでも\x01",
            "  幸運と思いましょう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_7450")

    TalkEnd(0xFF)
    Jump("loc_7461")

    label("loc_7458")

    TalkBegin(0xFF)
    Call(0, 43)
    TalkEnd(0xFF)

    label("loc_7461")

    Return()

    # Function_42_7319 end

    def Function_43_7462(): pass

    label("Function_43_7462")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0388
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

    #A0389
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_771B")

    #C0390
    ChrTalk(
        0x101,
        (
            "#0001F『黒月貿易公司』……\x02\x03",

            "もしかしてここが\x01",
            "イアン先生の言っていた……？\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x104,
        (
            "#0301F共和国から進出してきたっていう\x01",
            "マフィアの根城かよ。\x02\x03",

            "#0306Fにしちゃあ、\x01",
            "真っ当な会社って感じだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x102,
        (
            "#0101Fあくまで外見は、でしょう。\x02\x03",

            "どんな組織かなんて\x01",
            "分からないものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x103,
        (
            "#0200Fいずれにせよ、ルバーチェと同じく\x01",
            "無闇に手を出せる相手では\x01",
            "なさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        (
            "#0001Fああ、今の所\x01",
            "犯罪に組しているという証拠も\x01",
            "ないわけだし。\x02\x03",

            "#0003F（……いつかきちんと\x01",
            "  調べてみたい所だけどな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_771B")

    SetScenarioFlags(0x94, 0)
    Return()

    # Function_43_7462 end

    def Function_44_771F(): pass

    label("Function_44_771F")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A74")

    #A0395
    AnonymousTalk(
        0x102,
        (
            "#0104Fルピナス川に面し、\x01",
            "南のエルム湖を望む港湾区画#8Rウォーターフロント#……\x02\x03",

            "#0100Fこの辺りはオフィス街なのよね。\x01",
            "北側には会社ばかり建っているわ。\x02",
        )
    )

    CloseMessageWindow()

    #A0396
    AnonymousTalk(
        0x104,
        (
            "#0309Fはは、でもいいカンジで\x01",
            "公園があるじゃん。\x02\x03",

            "#0302F休んでいけってことじゃねえ？\x02",
        )
    )

    CloseMessageWindow()

    #A0397
    AnonymousTalk(
        0x103,
        (
            "#0203Fデータベースによると\x01",
            "『港湾公園』というそうですね。\x01",
            "……そのままですが。\x02",
        )
    )

    CloseMessageWindow()

    #A0398
    AnonymousTalk(
        0x101,
        "#0005Fあ……\x02",
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
            "#0000Fクロスベルタイムズだ。\x01",
            "こんな所に移転してたのか。\x02\x03",

            "#0003F（うーん、やっぱり３年も経つと\x01",
            "  いろいろ変わってるなぁ。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7A74")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0400
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "港湾区は、街の北東にあるビジネス街です。\x02",
        )
    )

    CloseMessageWindow()

    #A0401
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル最大の河川・ルピナス川に面した公園があり、\x01",
            "観光客や市民の憩いの場となっています。\x02",
        )
    )

    CloseMessageWindow()

    #A0402
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "またいくつかの大会社とともに、有名な\x01",
            "《クロスベル通信社》がビルを構えています。\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C03")
    OP_68(-19600, 2500, -27950, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)

    label("loc_7C03")

    SetScenarioFlags(0x45, 2)
    EventEnd(0x5)
    Return()

    # Function_44_771F end

    def Function_45_7C09(): pass

    label("Function_45_7C09")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 18600, 0, 17800, 0)
    SetChrPos(0x102, 19700, 0, 17800, 0)
    SetChrPos(0x103, 18600, 0, 16600, 0)
    SetChrPos(0x104, 19700, 0, 16600, 0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D11")
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
    Jump("loc_7D40")

    label("loc_7D11")

    OP_68(22000, 0, 21000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(21500, 0)
    OP_0D()

    label("loc_7D40")

    Call(0, 43)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D6A")

    #C0403
    ChrTalk(
        0x101,
        "#12P#0001Fここか……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x88, 3)

    label("loc_7D6A")

    TurnDirection(0x102, 0x101, 500)

    #C0404
    ChrTalk(
        0x102,
        "#11P#0101F……どうするの？\x02",
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
            "【ノックする】\x01",          # 0
            "【その場を離れる】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7DED"),
        (1, "loc_8236"),
        (SWITCH_DEFAULT, "loc_825C"),
    )


    label("loc_7DED")


    def lambda_7DF2():

        label("loc_7DF2")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_7DF2")

    QueueWorkItem2(0x102, 2, lambda_7DF2)

    def lambda_7E04():
        OP_96(0xFE, 0x4A9C, 0x0, 0x4CF4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E04)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x2)
    Sleep(300)
    Sound(811, 0, 100, 0)
    Sleep(500)

    #C0405
    ChrTalk(
        0x101,
        (
            "#11P#0001F──すみません！\x01",
            "いらっしゃいますか！？\x02",
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
        "男の声",
        "#5P#2S……どちら様でしょうか？\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#12P#0003F………クロスベル警察、\x01",
            "特務支援課に所属する者です。\x02\x03",

            "#0001Fとある事件に関して\x01",
            "こちらの支社長さんの話を\x01",
            "聞かせて頂ければと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #N0408
    NpcTalk(
        0x24,
        "男の声",
        "#5P#2S#40W………………………………\x02",
    )

    CloseMessageWindow()

    #N0409
    NpcTalk(
        0x24,
        "男の声",
        "#5P#2S……少々、お待ちください。\x02",
    )

    CloseMessageWindow()
    Sound(855, 0, 100, 0)
    Sleep(3000)
    VolumeBGM(0x64, 0x12C)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0410
    ChrTalk(
        0x101,
        "#0006F#5Pさてと……\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x104,
        "#12P#0303F鬼が出るか、蛇が出るか……\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        (
            "#6P#0201F#6P……扉が開いてみての\x01",
            "お楽しみですね。\x02",
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

    def lambda_8102():
        OP_95(0xFE, 19100, 0, 19700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_8102)

    def lambda_811C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_811C)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x24, 2)
    Sleep(300)

    #N0413
    NpcTalk(
        0x24,
        "東方風の男",
        "#5P──お待たせしました。\x02",
    )

    CloseMessageWindow()

    #N0414
    NpcTalk(
        0x24,
        "東方風の男",
        (
            "#5P支社長が会われるそうです。\x01",
            "どうぞ中へ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x24, 0xE1, 0x190)

    def lambda_81A4():
        OP_96(0xFE, 0x4DA8, 0x0, 0x4CAE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_81A4)
    WaitChrThread(0x24, 1)

    #C0415
    ChrTalk(
        0x101,
        "#6P#0000Fど、どうも。\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x102,
        "#12P#0103F……失礼します。\x02",
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
    Jump("loc_825C")

    label("loc_8236")

    SetChrPos(0x0, 19100, 0, 17200, 0)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    EventEnd(0x5)
    Jump("loc_825C")

    label("loc_825C")

    Return()

    # Function_45_7C09 end

    def Function_46_825D(): pass

    label("Function_46_825D")

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

    def lambda_8403():
        OP_96(0xFE, 0x4CF4, 0x0, 0x3908, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8403)

    def lambda_841D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_841D)
    Sleep(500)

    def lambda_8431():
        OP_96(0xFE, 0x48A8, 0x0, 0x3908, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8431)

    def lambda_844B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_844B)
    Sleep(600)

    def lambda_845F():
        OP_96(0xFE, 0x4CF4, 0x0, 0x3DB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_845F)

    def lambda_8479():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8479)
    Sleep(500)

    def lambda_848D():
        OP_96(0xFE, 0x48A8, 0x0, 0x3DB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_848D)

    def lambda_84A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_84A7)
    WaitChrThread(0x104, 1)

    def lambda_84BC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_84BC)
    WaitChrThread(0x103, 1)

    def lambda_84CD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_84CD)
    WaitChrThread(0x102, 1)

    def lambda_84DE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_84DE)
    WaitChrThread(0x101, 1)

    def lambda_84EF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_84EF)

    def lambda_84FC():
        OP_95(0xFE, 19100, 0, 17700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_84FC)

    def lambda_8516():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_8516)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x24, 2)
    OP_6F(0x10)

    #N0417
    NpcTalk(
        0x24,
        "東方風の男",
        "#5P……お疲れ様でした。\x02",
    )

    CloseMessageWindow()

    #N0418
    NpcTalk(
        0x24,
        "東方風の男",
        (
            "#5Pまた何かあればいつでも\x01",
            "いらっしゃって下さいとの\x01",
            "支社長からの伝言です。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        "#12P#0003F……どうもご親切に。\x02",
    )

    CloseMessageWindow()
    OP_93(0x24, 0x0, 0x1F4)

    def lambda_85DE():
        OP_95(0xFE, 19100, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_85DE)
    Sleep(1000)

    def lambda_85FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_85FB)
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
            "#0006F#5Pルバーチェに続いて\x01",
            "こちらもだったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x104,
        (
            "#0306F#12Pま、あっちよりは\x01",
            "遥かに友好的だったが……\x02\x03",

            "#0301F逆に舐められてたのかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x103,
        "#12P#0206F#6Pその可能性は否定できないかと……\x02",
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

    def lambda_87DF():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_87DF)
    Sleep(50)

    def lambda_87EF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_87EF)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)
    Sleep(300)

    #C0423
    ChrTalk(
        0x101,
        "#6P#0005Fエリィ……？\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x103,
        (
            "#6P#0201Fひょっとして……\x01",
            "具合が悪いんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)
    Sleep(300)

    #C0425
    ChrTalk(
        0x102,
        (
            "#5P#0104Fううん、大丈夫よ。\x02\x03",

            "#0108F……それよりも、\x01",
            "《銀#2Rイン#》という凄腕の刺客が\x01",
            "クロスベルに潜入している……\x02\x03",

            "#0101Fその情報は確かみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        (
            "#6P#0001Fああ……\x01",
            "あの調子だと間違いないだろう。\x02\x03",

            "#0008Fただ、あの支社長が\x01",
            "アルカンシェルやイリアさんを\x01",
            "脅迫したとは思えないんだよな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0427
    ChrTalk(
        0x104,
        (
            "#0301F#11Pああ、そんな感じはしたな。\x02\x03",

            "もしそうだったら、\x01",
            "そもそも《銀》との関係を\x01",
            "仄#2Rほの#めかしたりはしねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x103,
        (
            "#6P#0208F……という事は……\x02\x03",

            "#0201F《銀》という暗殺者が、\x01",
            "雇い主である《黒月》に関係なく\x01",
            "勝手にやった事なのでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0429
    ChrTalk(
        0x101,
        (
            "#0006F#5Pそうだとしたら……\x01",
            "正直、手詰まりになりそうだ。\x02\x03",

            "#0001Fさっきの話が本当なら……\x01",
            "あの支社長も《銀》の素性を\x01",
            "知ってるわけじゃないんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x104,
        (
            "#0301Fとなると、本人を捕まえるしか\x01",
            "聞き出す方法が無いってわけか？\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x102,
        "#5P#0108Fそうね……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    #C0432
    ChrTalk(
        0x102,
        (
            "#5P#0103Fもし、その《銀》という刺客が\x01",
            "イリアさんを狙っているなら……\x02\x03",

            "これはもう、私たちの仕事では\x01",
            "無いかもしれない……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8C59():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C59)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)

    #C0433
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x102,
        (
            "#5P#0100Fどうやら相当な凄腕みたいだし\x01",
            "私たちで捕まえられる保証もない。\x02\x03",

            "だったら今回は、警察本部に\x01",
            "任せた方がいいんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        "#6P#0011Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x103,
        (
            "#6P#0205Fまた旧市街の時のように\x01",
            "知らぬ顔をされるのでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        (
            "#5P#0103Fううん、アルカンシェルや\x01",
            "イリア・プラティエという存在は\x01",
            "クロスベル市にとって非常に重要よ。\x02\x03",

            "#0101Fその身に危険が迫っているなら\x01",
            "警察本部だって絶対に動くはず……\x02\x03",

            "それこそ警察の威信に賭けてもね。\x02",
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
        "男の声",
        "──その通りだ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(22000, 0, 16000, 2500)
    SetCameraDistance(20500, 2500)

    def lambda_8EE4():
        OP_96(0xFE, 0x4BC8, 0x0, 0x2BC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_8EE4)

    def lambda_8EFE():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8EFE)
    Sleep(100)

    def lambda_8F0E():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8F0E)
    Sleep(100)

    def lambda_8F1E():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8F1E)
    Sleep(100)

    def lambda_8F2E():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F2E)
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
        "#0011F#5Pあ、あなたは……！\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x102,
        "#5P#0105Fたしか捜査一課の……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x25,
        (
            "#11P#0603F一課のダドリーだ。\x02\x03",

            "#0601F来い。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        "#0005F#5Pへ……\x02",
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x25,
        (
            "#11P#0601F……こんな場所で悠長に\x01",
            "話をする馬鹿がどこにいる。\x02\x03",

            "いいから付いて来い。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x101,
        "#0011F#5Pわ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x104,
        "#5P#0301Fおいおい、何だってんだ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x25, 0xB4, 0x1F4)
    SetCameraDistance(21000, 1500)

    def lambda_90E7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_90E7)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_910E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_910E)
    Sleep(150)

    def lambda_912B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_912B)
    Sleep(150)

    def lambda_9148():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9148)
    Sleep(150)

    def lambda_9165():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9165)
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
            "……お前たちは阿呆か。\x02\x03",

            "何のつもりかは知らんが\x01",
            "ノコノコと乗り込んで……\x02\x03",

            "挙句の果てにあんな場所で\x01",
            "悠長に相談事をするとはな。\x02",
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
        "#6P#0006Fす、すみません……\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x102,
        (
            "#0108F#12P……確かに少々、\x01",
            "配慮が足りませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x25,
        (
            "#5P#0603Fフン……まあいい。\x02\x03",

            "#0600F──で？\x02",
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
        "#6P#0005Fで……とは？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x25,
        (
            "#5P#0601Fアルカンシェルがどうとか\x01",
            "口走っていただろう。\x02\x03",

            "それと、お前たちが《黒月》を\x01",
            "訪れたことに何の関係があるか……\x02\x03",

            "洗いざらい話せと言っている。\x02",
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
        "#6P#0013Fなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x104,
        (
            "#12P#0301Fおいおい……\x01",
            "いきなり何言ってんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x103,
        (
            "#12P#0211F唐突に現れたわりには\x01",
            "図々しい要求ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x25,
        (
            "#5P#0604Fフン……\x01",
            "図々しいのはどちらだ。\x02\x03",

            "我々一課は、一月以上前から\x01",
            "《黒月》をマークしている……\x02\x03",

            "#0601Fいきなり何の断りもなく\x01",
            "割って入ったのはお前たちだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        "#6P#0011Fそ、そうなんですか……？\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x102,
        (
            "#0101F#12Pもしかして……\x01",
            "一課の方でも《銀#2Rイン#》を？\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x25,
        (
            "#5P#0603Fフン……\x01",
            "その名前を知っていたか。\x02\x03",

            "#0601Fとにかく、知っていることを\x01",
            "包み隠さず話してもらおう。\x02\x03",

            "従わなかった場合……\x01",
            "こちらの捜査妨害を行ったとして\x01",
            "セルゲイさんに厳重抗議する。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#6P#0008Fくっ……分かりました。\x02\x03",

            "#0013Fただし……\x01",
            "あくまで支援課で受けた話です。\x02\x03",

            "他言は無用にお願いしますよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x25,
        (
            "#5P#0603Fそれは私が判断する。\x02\x03",

            "#0601Fいいから話せ──これは命令だ。\x02",
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
            "#5P#0604F──ふむ、なるほどな。\x02\x03",

            "手がかりがないと思ったが……\x01",
            "ようやく尻尾を出したというわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x102,
        (
            "#0101F#12Pそれは……\x01",
            "《銀#2Rイン#》のことですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x25,
        (
            "#5P#0600F……そうだ。\x02\x03",

            "#0603F《ルバーチェ》に対抗するため\x01",
            "《黒月#4Rヘイユエ#》が切り札として雇ったという\x01",
            "凄腕の刺客にして暗殺者。\x02\x03",

            "ある筋から情報を入手して以来、\x01",
            "我々一課は《黒月》を監視してきた。\x02\x03",

            "#0601Fだが……\x01",
            "まさかお前たちのような仔犬どもに\x01",
            "首を突っ込まれる隙を作るとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x104,
        (
            "#12P#0304Fヘッ……\x01",
            "言ってくれるじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x103,
        (
            "#12P#0201Fですが……\x01",
            "どうして《黒月》だけ監視を？\x02\x03",

            "《ルバーチェ》の方は\x01",
            "放置しているようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x25,
        (
            "#5P#0604Fフン、何を言っている？\x02\x03",

            "《ルバーチェ》についても\x01",
            "大体の動きは把握しているぞ。\x02\x03",

            "#0602F旧市街の一件や、軍用犬の使用……\x02\x03",

            "お前たちが関わった一連の事件も\x01",
            "ある程度のことは事前に掴んでいた。\x02",
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
        "#6P#0005F#4Sな……！？\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x103,
        "#12P#0201Fだったらどうして……\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x25,
        (
            "#5P#0603Fフン……あの程度で動いていては\x01",
            "キリが無いというだけだ。\x02\x03",

            "#0600F殺人が起こったわけでもなし、\x01",
            "ただの小さなイザコザにすぎん。\x02\x03",

            "どうして他の重要案件を後回しにして\x01",
            "限りある人員を割かなくてはならん？\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#6P#0007Fそ、そうは言っても……！\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x25,
        (
            "#5P#0601F──我々捜査一課は\x01",
            "お前たちのようなボンクラとは違う。\x02\x03",

            "#0603Fこの、正義が守りきれない街で\x01",
            "一定以上の秩序を保ち続けること……\x02\x03",

            "殺人などの重犯罪を抑止し、\x01",
            "犯罪組織や外国の諜報機関から\x01",
            "可能な限り人と社会を守ること……\x02\x03",

            "#0601Fその苦労がお前たちに分かるのか？\x02",
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
            "#0108F#12Pやはり……そうなんですね。\x02\x03",

            "#0106Fクロスベルの平和と繁栄は……\x01",
            "薄皮一枚の上に成り立っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x25,
        (
            "#5P#0606Fフン、市民の大半は\x01",
            "その事実に気付いていないがな。\x02\x03",

            "#0600F《ルバーチェ》が帝国派議員と\x01",
            "結びついている話は有名だが……\x02\x03",

            "あの《黒月》にしたところで\x01",
            "共和国派議員と関係を深めている。\x02\x03",

            "#0603Fその時点で、直接手を出すのは\x01",
            "どちらも不可能になってしまっている。\x02\x03",

            "#0601Fそれだけではない……\x01",
            "スパイを取り締まれる法律がないから\x01",
            "外国の諜報員なども入りたい放題だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x101,
        "#6P#0013F……そんな………\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x103,
        "#12P#0206F……信じられません。\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x104,
        (
            "#12P#0306Fなんつーか……\x01",
            "末期状態かもしれねぇな。\x02",
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
            "#5P#0603Fだが、そんな絶望的な状況でも\x01",
            "我々はやれることをやるだけだ。\x02\x03",

            "全ての案件の危険度を査定し、\x01",
            "たとえ根本的に解決できなくても\x01",
            "抑止できるように働きかける……\x02\x03",

            "#0600F《銀》の問題もその一環にすぎん。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x25,
        (
            "#5P#0600Fアルカンシェルの一件については\x01",
            "こちらの目が行き届いていなかった。\x02\x03",

            "情報提供に感謝する。\x02\x03",

            "あとは一課が引き継ぐから\x01",
            "お前たちは通常業務に戻るがいい。\x02",
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
        "#6P#0007F#4Sな……！？\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x104,
        "#12P#0307Fおいおい、何でそうなる！？\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x25,
        (
            "#5P#0603Fどうやら状況を判断する限り\x01",
            "《銀》が実在するのは確かだろう。\x02\x03",

            "《黒月》の動向にも気を配りつつ\x01",
            "姿無き謎の暗殺者の手から\x01",
            "イリア・プラティエを守りきる……\x02\x03",

            "#0602Fそんな真似がお前たちにできるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x101,
        "#6P#0010Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x103,
        (
            "#12P#0206F……人手がなければ\x01",
            "難しいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x25, 0x10E, 0x1F4)
    OP_68(6890, 900, -9560, 2000)

    def lambda_A4D2():
        OP_95(0xFE, 5000, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_A4D2)
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
            "#0603F#5Pアルカンシェルへの連絡だけは\x01",
            "せめてお前たちに任せてやる。\x02\x03",

            "脅迫事件の対策が\x01",
            "捜査一課に引き継がれること……\x02\x03",

            "#0600Fきちんと説明しておけよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A5A8():
        OP_95(0xFE, 5000, 0, -11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_A5A8)
    Sleep(100)

    def lambda_A5C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_A5C5)
    WaitChrThread(0x25, 1)
    WaitChrThread(0x25, 2)
    OP_71(0x5, 0x10F, 0x12C, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x5)
    Sound(457, 0, 100, 0)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)

    def lambda_A614():
        OP_95(0xFE, -14000, 0, -12500, 6500, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_A614)
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

    def lambda_A693():
        OP_9E(0xFE, 0xFFFFC950, 0xFFFFB7BC, 0xFFFEA070, 0x1964, 0x1)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_A693)
    WaitChrThread(0x27, 1)

    def lambda_A6B2():
        OP_95(0xFE, -20000, 0, -33500, 6500, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_A6B2)
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
            "#0301F#12Pクソ、言うだけ言って\x01",
            "とっとと行きやがったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x103,
        (
            "#12P#0211Fしかも専用車でというのが\x01",
            "さらにムカつく感じです……\x02",
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
            "#0008F#5P……でも、彼の言うことも\x01",
            "納得できないわけじゃない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0492
    ChrTalk(
        0x102,
        "#0105F#11Pえ……\x02",
    )

    CloseMessageWindow()

    def lambda_A862():
        OP_93(0xFE, 0x59, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A862)
    Sleep(50)

    def lambda_A872():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A872)
    Sleep(50)
    OP_93(0x104, 0xE1, 0x1F4)
    Sleep(300)

    #C0493
    ChrTalk(
        0x101,
        (
            "#0006F#5P実際、こちらで処理できる\x01",
            "範疇を超えてきている気がする。\x02\x03",

            "リーシャとイリアさんには\x01",
            "事情を説明して謝るしかないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x104,
        "#0306Fふう、それしかねぇか……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x103,
        "#12P#0208F仕方……ありませんね。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0496
    ChrTalk(
        0x102,
        "#0107F#11Pちょ、ちょっと待って！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A9A6():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A9A6)
    Sleep(50)

    def lambda_A9B6():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A9B6)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)

    #C0497
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
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
            "#0106F#11Pロイド……\x01",
            "あなたがそんな事を言うの！？\x02\x03",

            "#0101F《壁》を乗り越えるって……\x01",
            "みんなでなら乗り越えられるって\x01",
            "言ってくれたじゃない……！\x02\x03",

            "#0107Fなのにどうして……っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        "#6P#0011Fエ、エリィ……？\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x104,
        (
            "#12P#0305Fおいおい、どうしたんだ？\x02\x03",

            "#0301Fお嬢だってさっきは、\x01",
            "警察本部に任せるべきだって\x01",
            "言ってただろうが？\x02",
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
            "#0105F#11P#40Wあ……\x02\x03",

            "#0108F#50W……そう、そうよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x103,
        "#6P#0205Fエリィさん……\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x101,
        (
            "#6P#0006Fえっと……\x02\x03",

            "その、俺だって悔しいし、\x01",
            "何とかしたいと思ってるさ。\x02\x03",

            "#0000Fエリィがそう言うなら\x01",
            "何とか別の手を考えて……\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x102,
        (
            "#0106F#11Pううん、いいの……\x02\x03",

            "#0102F……ごめんなさい。\x01",
            "ちょっと疲れているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        "#6P#0001Fエリィ……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x104,
        (
            "#12P#0306Fま、今日は色々と\x01",
            "やっかいな連中とばかり\x01",
            "顔を合わせたからな。\x02\x03",

            "#0300Fアルカンシェルに行って\x01",
            "イリアさんたちに報告したら\x01",
            "戻って一休みしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x103,
        (
            "#6P#0203Fそうですね……\x01",
            "それがいいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x101,
        (
            "#6P#0003F……そうだな。\x02\x03",

            "#0000Fエリィ、それでいいかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x102,
        (
            "#0104F#11Pええ……みんなありがとう。\x02\x03",

            "#0100Fそれじゃあ、\x01",
            "アルカンシェルに行きましょう。\x02",
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

    # Function_46_825D end

    def Function_47_AE6E(): pass

    label("Function_47_AE6E")


    def lambda_AE73():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_AE73)
    WaitChrThread(0x25, 1)

    def lambda_AE91():
        OP_95(0xFE, 6700, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_AE91)
    WaitChrThread(0x25, 1)
    Return()

    # Function_47_AE6E end

    def Function_48_AEAB(): pass

    label("Function_48_AEAB")

    Sleep(500)

    def lambda_AEB3():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AEB3)
    WaitChrThread(0x101, 1)

    def lambda_AED1():
        OP_95(0xFE, 9600, 0, -11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AED1)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_48_AEAB end

    def Function_49_AEF2(): pass

    label("Function_49_AEF2")

    Sleep(600)

    def lambda_AEFA():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AEFA)
    WaitChrThread(0x102, 1)

    def lambda_AF18():
        OP_95(0xFE, 9600, 0, -9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF18)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x10E, 0x1F4)
    Return()

    # Function_49_AEF2 end

    def Function_50_AF39(): pass

    label("Function_50_AF39")

    Sleep(700)

    def lambda_AF41():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AF41)
    WaitChrThread(0x103, 1)

    def lambda_AF5F():
        OP_95(0xFE, 11000, 0, -11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AF5F)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x10E, 0x1F4)
    Return()

    # Function_50_AF39 end

    def Function_51_AF80(): pass

    label("Function_51_AF80")

    Sleep(800)

    def lambda_AF88():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AF88)
    WaitChrThread(0x104, 1)

    def lambda_AFA6():
        OP_95(0xFE, 11000, 0, -9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AFA6)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_51_AF80 end

    def Function_52_AFC7(): pass

    label("Function_52_AFC7")

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

    def lambda_B0C6():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B0C6)
    OP_68(-1600, 1500, 5600, 5000)
    FadeToBright(2000, 0)
    Sleep(1000)

    def lambda_B0FD():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B0FD)
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

    # Function_52_AFC7 end

    def Function_53_B16E(): pass

    label("Function_53_B16E")

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

    def lambda_B2BF():
        OP_95(0xFE, 21500, 9500, 24500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_B2BF)

    def lambda_B2D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_B2D9)
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

    def lambda_B33D():
        OP_9D(0xFE, 0x36B0, 0x2134, 0x5FB4, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_B33D)
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

    def lambda_B3CD():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_B3CD)

    def lambda_B3DA():
        OP_9D(0xFE, 0x36B0, 0x2A30, 0x7918, 0xCE4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_B3DA)
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

    def lambda_B46A():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_B46A)

    def lambda_B477():
        OP_9D(0xFE, 0x24B8, 0x2C24, 0x7918, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_B477)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    SetChrSubChip(0x26, 0x0)

    def lambda_B4A9():
        OP_9D(0xFE, 0xFFFFF448, 0x2648, 0x7918, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_B4A9)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    PlayEffect(0x0, 0xFF, 0x26, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    SetChrSubChip(0x26, 0x0)

    def lambda_B512():
        OP_9D(0xFE, 0xFFFFD314, 0x3458, 0x7918, 0x1324, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_B512)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    PlayEffect(0x0, 0xFF, 0x26, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    SetChrSubChip(0x26, 0x0)

    def lambda_B57B():
        OP_9D(0xFE, 0xFFFFAC04, 0x3458, 0x7918, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_B57B)
    Sound(854, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x26, 0x1)
    SetScenarioFlags(0x5C, 2)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_B16E end

    def Function_54_B5B5(): pass

    label("Function_54_B5B5")

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
        "#12P#0013Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x103,
        "#12P#0201F襲撃の跡、ですね……\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x104,
        (
            "#0303F例の重機関銃が使われた\x01",
            "跡っぽいな……\x02\x03",

            "#0301F爆発物を使わないだけ\x01",
            "マシだったみてぇだが……\x02",
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
        "#5Pやあ、ロイドたちじゃないか。\x02",
    )

    CloseMessageWindow()
    OP_68(19100, 1100, 14000, 1200)

    def lambda_B7F3():
        OP_95(0xFE, 19100, 0, 14800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B7F3)
    WaitChrThread(0x21, 1)
    OP_6F(0x1)

    #C0514
    ChrTalk(
        0x101,
        (
            "#12P#0001Fフランツ……\x01",
            "状況はどうなってるんだ？\x02\x03",

            "さっき話を聞いて\x01",
            "慌ててやって来たんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x21,
        "#5P俺にも分からないって。\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x21,
        (
            "#5Pただまあ、昨日の真夜中に\x01",
            "ドンパチやらかしたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x21,
        (
            "#5P今、ダドリーさんたちが\x01",
            "事情聴取をしてるぜ。\x02",
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
            "#0106Fやっぱり一課に\x01",
            "先を越されていたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x103,
        "#12P#0206Fさすがのフットワークかと。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        (
            "#12P#0003F俺たちも《黒月》から\x01",
            "話を聞いておきたいんだけど……\x02\x03",

            "#0000F中に通してもらってもいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x21,
        "#5Pう、うーん……\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x21,
        (
            "#5Pまあ、一般市民は通すなって\x01",
            "言われただけだからいいか。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x21,
        (
            "#5Pダドリーさんには適当に\x01",
            "誤魔化しといてくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x101,
        "#12P#0002Fああ、助かるよ。\x02",
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

    # Function_54_B5B5 end

    def Function_55_BB0B(): pass

    label("Function_55_BB0B")

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

    def lambda_BC37():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC37)

    def lambda_BC51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BC51)
    Sleep(650)

    def lambda_BC65():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BC65)

    def lambda_BC7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BC7F)
    Sleep(650)

    def lambda_BC93():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BC93)

    def lambda_BCAD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BCAD)
    Sleep(650)

    def lambda_BCC1():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BCC1)

    def lambda_BCDB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BCDB)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    OP_4B(0x101, 0xFF)
    OP_4B(0x102, 0xFF)
    OP_4B(0x103, 0xFF)
    OP_4B(0x104, 0xFF)

    def lambda_BD11():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BD11)

    def lambda_BD1E():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_BD1E)

    def lambda_BD2B():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_BD2B)

    def lambda_BD38():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_BD38)
    Sleep(100)
    OP_4B(0x21, 0xFF)
    TurnDirection(0x21, 0x101, 500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x21)

    def lambda_BD83():

        label("loc_BD83")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_BD83")

    QueueWorkItem2(0x21, 2, lambda_BD83)

    def lambda_BD95():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BD95)

    def lambda_BDA2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_BDA2)

    def lambda_BDAF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_BDAF)

    def lambda_BDBC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_BDBC)
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

    def lambda_BEA7():
        OP_95(0xFE, 21100, 0, -3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BEA7)
    Sleep(50)

    def lambda_BEC4():
        OP_95(0xFE, 22100, 0, -1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BEC4)
    Sleep(50)

    def lambda_BEE1():
        OP_95(0xFE, 20100, 0, -2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BEE1)
    Sleep(50)

    def lambda_BEFE():
        OP_95(0xFE, 21100, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BEFE)
    WaitChrThread(0x101, 1)

    def lambda_BF1C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BF1C)
    WaitChrThread(0x102, 1)

    def lambda_BF2D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BF2D)
    WaitChrThread(0x103, 1)

    def lambda_BF3E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BF3E)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)

    #C0525
    ChrTalk(
        0x101,
        "#12P#0006F……参ったな。\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x102,
        (
            "#5P#0106Fええ、色々と教えてくれたのは\x01",
            "助かったけど……\x02\x03",

            "#0101Fまさかあそこまで露骨に\x01",
            "本格的な抗争を仄#2Rほの#めかすなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x104,
        (
            "#0303F#5Pこのままだと確実に\x01",
            "ドンパチが始まるだろうな。\x02\x03",

            "#0301F下手すりゃ今回みたいな市街地で。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x103,
        (
            "#6P#0206Fしかも《黒月》本体からの\x01",
            "増援の可能性アリですか……\x02\x03",

            "#0211F相当、キナ臭くなってきましたね。\x02",
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
            "#12P#0003F……ツァオがああ言った以上、\x01",
            "まだ猶予はあると思っていいだろう。\x02\x03",

            "#0013Fいずれにせよ、ルバーチェの\x01",
            "今回の襲撃には不審な点が多すぎる。\x02\x03",

            "黒月が本格的に動き始める前に\x01",
            "色々調べてみた方が良さそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x102,
        "#5P#0101Fええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x103,
        (
            "#6P#0205Fとなると今日も、\x01",
            "各方面で聞き込みを？\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x101,
        (
            "#12P#0003Fいや……\x02\x03",

            "#0000F──やはりここは直接、\x01",
            "ルバーチェを当たってみないか？\x02",
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
        "#0305F#5Pマジか……！？\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x102,
        (
            "#5P#0106Fた、確かに以前も\x01",
            "訪ねたことはあったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x103,
        (
            "#6P#0201F競売会の一件もありますし、\x01",
            "さすがに無謀すぎるのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x101,
        (
            "#12P#0006F……ああ。\x01",
            "いくら手打ちの話があっても\x01",
            "キーアの件についてだけだしな。\x02\x03",

            "#0008Fただ、どうしても\x01",
            "気になることがあってさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x103,
        "#6P#0205F気になること……？\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x101,
        (
            "#12P#0001Fあのガルシアの動向さ。\x02\x03",

            "何度かやり合って思ったんだが\x01",
            "彼は決して愚かでも無謀でもない。\x02\x03",

            "そして手下もちゃんと押さえて\x01",
            "統率している印象だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x104,
        (
            "#0303F#5P確かに、元は名の知れた\x01",
            "猟兵団の部隊長だったしな。\x02\x03",

            "#0301F普通だったら意味もない襲撃を\x01",
            "やらせるとは思えねぇが……\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x102,
        (
            "#5P#0103F昨晩の襲撃を彼が指示したのか\x01",
            "それとも手下の暴走なのか……\x02\x03",

            "#0101F確かに知りたい情報ではあるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x101,
        (
            "#12P#0000Fだろ？\x02\x03",

            "ルバーチェ商会の周辺を\x01",
            "聞き込んでみるくらいでもいい。\x02\x03",

            "今から行ってみないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x102,
        "#5P#0102Fはあ……仕方ないわね。\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x103,
        (
            "#6P#0202Fまあ、周辺を聞き込む程度なら\x01",
            "危険は少ないのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x104,
        "#0302F#5Pしゃあねえ、行ってみるか！\x02",
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

    # Function_55_BB0B end

    def Function_56_C6C2(): pass

    label("Function_56_C6C2")

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
            "#6P#0000Fあの、すみません。\x01",
            "この辺りで落し物を\x01",
            "拾われたりしていませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x8,
        "#5Pあら、落し物っていうか……\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x8,
        (
            "#5P公園外れの草むらに\x01",
            "引っかかっている物があったから、\x01",
            "気になって拾ったわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x8,
        "#5P風で飛びそうになっていたし。\x02",
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
        "#6P#0005F風で飛びそう……？\x02",
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x103,
        (
            "#0200F#12Pそういえば依頼主の方は\x01",
            "最後の一つが思い出せないと\x01",
            "言っていましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        "#0100F#11P一体何だったのかしら。\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x8,
        (
            "#5Pあなた達が探していたの？\x01",
            "それじゃ渡しておくわね。\x02",
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
            "を預かった。\x02",
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
            "#11P#0305F鉄道の乗車チケットか……\x02\x03",

            "#0306Fつーかこれがないと\x01",
            "国に帰れないんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x338, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x339, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CABB")

    #C0555
    ChrTalk(
        0x101,
        (
            "#6P#0003Fと、ともかくこれで\x01",
            "全部見つかったみたいだ。\x02\x03",

            "#0000Fトロントさんに報告しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x102,
        "#0100F#11Pええ、届けてあげましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CAE2")

    label("loc_CABB")


    #C0557
    ChrTalk(
        0x101,
        "#6P#0003F……後で届けてあげよう。\x02",
    )

    CloseMessageWindow()

    label("loc_CAE2")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 20110, 0, 7370, 225)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    OP_29(0x2, 0x1, 0x4)
    SetScenarioFlags(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB38")
    OP_29(0x2, 0x1, 0x1F)

    label("loc_CB38")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_56_C6C2 end

    def Function_57_CB3E(): pass

    label("Function_57_CB3E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0558
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《ミシュラム》行き水上バス・時刻表\x01\x01",
            "※ミシュラムが誇るテーマパーク\x01",
            "  『ワンダーランド』開園中！\x01",
            "  楽しいひと時をお楽しみ下さい！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_57_CB3E end

    def Function_58_CBF7(): pass

    label("Function_58_CBF7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0559
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　《ルピナス川・第一灯台》\x01\x01",
            "関係者以外の立ち入りを禁ずる。\x01",
            "　　　　　　～クロスベル市～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_58_CBF7 end

    SaveToFile()

Try(main)
