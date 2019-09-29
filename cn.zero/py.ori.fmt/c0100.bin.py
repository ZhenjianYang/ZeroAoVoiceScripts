from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0100.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("c0100", "c0100_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 5, 0, 6],
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
        "阿罗纳",                 # 8
        "凯特巡警",               # 9
        "雷因兹",                 # 10
        "车１",                   # 11
        "柯贝",                   # 12
        "蔡特",                   # 13
        "琪雅",                   # 14
        "老人",                   # 15
        "老妇人",                 # 16
        "车１",                   # 17
        "车２",                   # 18
        "哈罗德",                 # 19
        "赛尔盖科长",             # 20
        "阿奈斯特秘书",           # 21
        "蔡特",                   # 22
        "事件用ＮＰＣ",           # 23
        "事件用ＮＰＣ",           # 24
        "事件用ＮＰＣ",           # 25
        "事件用ＮＰＣ",           # 26
        "事件用ＮＰＣ",           # 27
        "SE控制",                 # 28
        " ",                      # 29
        "中央广场",               # 30
        "西街",                   # 31
        "行政区",                 # 32
        "住宅街",                 # 33
        "欢乐街",                 # 34
        "东街",                   # 35
        "旧城区",                 # 36
        "港湾区",                 # 37
        "ＩＢＣ",                 # 38
        "站前街道",               # 39
        "后巷",                   # 40
        "乌尔斯拉间道",           # 41
        "东克洛斯贝尔街道",       # 42
        "西克洛斯贝尔街道",       # 43
        "玛因兹山道",             # 44
    ))

    AddCharChip((
        "chr/ch21300.itc",                   # 00
        "chr/ch20002.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20700.itc",                   # 03
        "chr/ch20400.itc",                   # 04
        "chr/ch22100.itc",                   # 05
        "chr/ch28100.itc",                   # 06
        "chr/ch24900.itc",                   # 07
        "chr/ch21800.itc",                   # 08
        "chr/ch20600.itc",                   # 09
        "chr/ch21200.itc",                   # 0A
        "chr/ch20800.itc",                   # 0B
        "chr/ch20100.itc",                   # 0C
        "chr/ch21900.itc",                   # 0D
        "chr/ch27800.itc",                   # 0E
        "chr/ch20500.itc",                   # 0F
        "chr/ch26000.itc",                   # 10
        "chr/ch20900.itc",                   # 11
        "chr/ch39200.itc",                   # 12
        "chr/ch02708.itc",                   # 13
        "chr/ch20300.itc",                   # 14
        "chr/ch08200.itc",                   # 15
        "chr/ch30600.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(30000,   0,       -1799,   270,  261,  0x0, 0,   0,   0,   0,   1,   1,   0,   255,  0)
    DeclNpc(-6090,   150,     4449,    270,  341,  0x0, 0,   1,   0,   255, 255, 1,   1,   255,  0)
    DeclNpc(-6099,   0,       -9409,   90,   261,  0x0, 0,   2,   0,   0,   0,   1,   2,   255,  0)
    DeclNpc(-289,    0,       -10319,  225,  261,  0x0, 0,   3,   0,   0,   2,   1,   3,   255,  0)
    DeclNpc(850,     0,       17969,   90,   277,  0x0, 0,   15,  0,   0,   0,   1,   4,   255,  0)
    DeclNpc(2539,    0,       17870,   270,  277,  0x0, 0,   5,   0,   0,   0,   1,   5,   255,  0)
    DeclNpc(14130,   0,       340,     270,  261,  0x0, 0,   16,  0,   0,   0,   1,   6,   255,  0)
    DeclNpc(2650,    0,       -2960,   315,  389,  0x0, 0,   20,  0,   0,   0,   1,   7,   255,  0)
    DeclNpc(-1210,   0,       -2390,   180,  389,  0x0, 0,   22,  0,   0,   0,   1,   8,   255,  0)
    DeclNpc(-16760,  29,      6889,    315,  389,  0x0, 0,   6,   0,   0,   4,   1,   14,  255,  0)
    DeclNpc(-8010,   0,       16229,   225,  197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-22809,  1299,    -18829,  180,  261,  0x0, 0,   18,  0,   0,   3,   1,   9,   255,  0)
    DeclNpc(-25440,  1299,    -17040,  180,  404,  0x0, 0,   19,  0,   0,   0,   1,   12,  255,  0)
    DeclNpc(-25440,  1299,    -18170,  0,    389,  0x0, 0,   21,  0,   0,   0,   1,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 29,  -19.200000762939453,   -23.0,                 -9.199999809265137,    625.0,                 [0.07071065902709961,  0.14142140746116638,   -0.0,                  0.0,                   -0.07071070373058319,  0.14142131805419922,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.2687014639377594,   5.967981338500977,     1.840000033378601,     1.0])
    DeclEvent(0x0000, 0, 32,  0.0,                   -17.0,                 -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  3.4000000953674316,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 1, 15,  0.0,                   -17.0,                 -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  3.4000000953674316,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 1, 16,  -5.900000095367432,    -17.1299991607666,     -3.2799999713897705,   56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.9666666984558105,    3.425999879837036,     0.656000018119812,     1.0])

    DeclActor(1740,    -950,    3070,    1100,    1740,    550,     3070,    0x007C, 0,  7,  0x0000)
    DeclActor(-290,    -1000,   4400,    600,     -290,    -1000,   4400,    0x007C, 0,  9,  0x0000)
    DeclActor(-270,    0,       -980,    800,     130,     1500,    -10,     0x007C, 0,  8,  0x0000)
    DeclActor(4090,    0,       -16900,  1200,    4090,    2000,    -16900,  0x007C, 0,  12, 0x0000)

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
    PlaceName(5.690000057220459, 0.0, -14.600000381469727, 0x0000, 0x0056, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(5000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1

    ScpFunction((
        "Function_0_A88",          # 00, 0
        "Function_1_B40",          # 01, 1
        "Function_2_B8D",          # 02, 2
        "Function_3_BB8",          # 03, 3
        "Function_4_BE3",          # 04, 4
        "Function_5_C0E",          # 05, 5
        "Function_6_15A6",         # 06, 6
        "Function_7_1840",         # 07, 7
        "Function_8_1995",         # 08, 8
        "Function_9_1ACF",         # 09, 9
        "Function_10_1B25",        # 0A, 10
        "Function_11_20B9",        # 0B, 11
        "Function_12_21A8",        # 0C, 12
        "Function_13_21B6",        # 0D, 13
        "Function_14_317F",        # 0E, 14
        "Function_15_31F3",        # 0F, 15
        "Function_16_3265",        # 10, 16
        "Function_17_32F0",        # 11, 17
        "Function_18_32FA",        # 12, 18
        "Function_19_3632",        # 13, 19
        "Function_20_367E",        # 14, 20
        "Function_21_480E",        # 15, 21
        "Function_22_4855",        # 16, 22
        "Function_23_48A3",        # 17, 23
        "Function_24_5848",        # 18, 24
        "Function_25_5902",        # 19, 25
        "Function_26_5B9B",        # 1A, 26
        "Function_27_5C25",        # 1B, 27
        "Function_28_5C76",        # 1C, 28
        "Function_29_5CC2",        # 1D, 29
        "Function_30_70E5",        # 1E, 30
        "Function_31_749A",        # 1F, 31
        "Function_32_7E5E",        # 20, 32
        "Function_33_88D0",        # 21, 33
        "Function_34_8D0B",        # 22, 34
        "Function_35_8D95",        # 23, 35
        "Function_36_8DE6",        # 24, 36
        "Function_37_8E37",        # 25, 37
        "Function_38_8E88",        # 26, 38
        "Function_39_8ED4",        # 27, 39
        "Function_40_9423",        # 28, 40
        "Function_41_9488",        # 29, 41
        "Function_42_94ED",        # 2A, 42
        "Function_43_9552",        # 2B, 43
        "Function_44_95B7",        # 2C, 44
        "Function_45_9F01",        # 2D, 45
        "Function_46_A21F",        # 2E, 46
        "Function_47_A595",        # 2F, 47
        "Function_48_A8D6",        # 30, 48
        "Function_49_A92E",        # 31, 49
        "Function_50_A986",        # 32, 50
        "Function_51_A9DE",        # 33, 51
        "Function_52_AA08",        # 34, 52
        "Function_53_AA60",        # 35, 53
        "Function_54_AB2A",        # 36, 54
        "Function_55_AB68",        # 37, 55
        "Function_56_ABB3",        # 38, 56
    ))


    def Function_0_A88(): pass

    label("Function_0_A88")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_AC8"),
        (1, "loc_AD4"),
        (2, "loc_AE0"),
        (3, "loc_AEC"),
        (4, "loc_AF8"),
        (5, "loc_B04"),
        (6, "loc_B10"),
        (SWITCH_DEFAULT, "loc_B1C"),
    )


    label("loc_AC8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_B28")

    label("loc_AD4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_B28")

    label("loc_AE0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_B28")

    label("loc_AEC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_B28")

    label("loc_AF8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_B28")

    label("loc_B04")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_B28")

    label("loc_B10")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B28")

    label("loc_B1C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B28")

    label("loc_B28")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B28")

    label("loc_B3F")

    Return()

    # Function_0_A88 end

    def Function_1_B40(): pass

    label("Function_1_B40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B8C")
    OP_95(0xFE, 11850, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 11850, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_1_B40")

    label("loc_B8C")

    Return()

    # Function_1_B40 end

    def Function_2_B8D(): pass

    label("Function_2_B8D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB7")
    OP_94(0xFE, 0x366, 0xFFFFE296, 0xFFFFF236, 0xFFFFD166, 0x3E8)
    Sleep(300)
    Jump("Function_2_B8D")

    label("loc_BB7")

    Return()

    # Function_2_B8D end

    def Function_3_BB8(): pass

    label("Function_3_BB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BE2")
    OP_94(0xFE, 0xFFFFA484, 0xFFFFB348, 0xFFFFA722, 0xFFFFB9BA, 0x3E8)
    Sleep(300)
    Jump("Function_3_BB8")

    label("loc_BE2")

    Return()

    # Function_3_BB8 end

    def Function_4_BE3(): pass

    label("Function_4_BE3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C0D")
    OP_94(0xFE, 0xFFFFBE2E, 0x2184, 0xFFFFB38E, 0x1054, 0x3E8)
    Sleep(300)
    Jump("Function_4_BE3")

    label("loc_C0D")

    Return()

    # Function_4_BE3 end

    def Function_5_C0E(): pass

    label("Function_5_C0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131F")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD0")
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    SetChrPos(0x1, -26950, -1160, -4340, 90)
    SetChrPos(0x2, -26950, -1160, -4340, 90)
    SetChrPos(0x3, -26950, -1160, -4340, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA3")
    SetChrPos(0x4, -26950, -1160, -4340, 90)
    SetChrPos(0x5, -26950, -1160, -4340, 90)
    Jump("loc_CC2")

    label("loc_CA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC2")
    SetChrPos(0x4, -26950, -1160, -4340, 90)

    label("loc_CC2")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131F")

    label("loc_CD0")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D84")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D57")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_D76")

    label("loc_D57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D76")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_D76")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131F")

    label("loc_D84")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E38")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0B")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_E2A")

    label("loc_E0B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2A")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_E2A")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131F")

    label("loc_E38")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEC")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBF")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_EDE")

    label("loc_EBF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EDE")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_EDE")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131F")

    label("loc_EEC")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA0")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F73")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_F92")

    label("loc_F73")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F92")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_F92")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131F")

    label("loc_FA0")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1054")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1027")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_1046")

    label("loc_1027")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1046")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_1046")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131F")

    label("loc_1054")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1108")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DB")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_10FA")

    label("loc_10DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FA")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_10FA")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131F")

    label("loc_1108")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BC")
    SetChrPos(0x0, 4040, 0, -21980, 0)
    SetChrPos(0x1, 4040, 0, -21980, 0)
    SetChrPos(0x2, 4040, 0, -21980, 0)
    SetChrPos(0x3, 4040, 0, -21980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118F")
    SetChrPos(0x4, 4040, 0, -21980, 0)
    SetChrPos(0x5, 4040, 0, -21980, 0)
    Jump("loc_11AE")

    label("loc_118F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11AE")
    SetChrPos(0x4, 4040, 0, -21980, 0)

    label("loc_11AE")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131F")

    label("loc_11BC")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1270")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1243")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_1262")

    label("loc_1243")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1262")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_1262")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131F")

    label("loc_1270")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131F")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F7")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_1316")

    label("loc_12F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1316")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_1316")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_131F")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1336")
    Jump("loc_1444")

    label("loc_1336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1349")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1444")

    label("loc_1349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1357")
    Jump("loc_1444")

    label("loc_1357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1365")
    Jump("loc_1444")

    label("loc_1365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_137D")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_1444")

    label("loc_137D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1390")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1444")

    label("loc_1390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_13A8")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1444")

    label("loc_13A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_13C0")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1444")

    label("loc_13C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_13CE")
    Jump("loc_1444")

    label("loc_13CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_13E1")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1444")

    label("loc_13E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_13F4")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1444")

    label("loc_13F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1407")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1444")

    label("loc_1407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1415")
    Jump("loc_1444")

    label("loc_1415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1423")
    Jump("loc_1444")

    label("loc_1423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1436")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_1444")

    label("loc_1436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1444")
    ClearChrFlags(0x11, 0x80)

    label("loc_1444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1458")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)
    Jump("loc_158D")

    label("loc_1458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1469")
    ClearScenarioFlags(0x5C, 1)
    Jump("loc_158D")

    label("loc_1469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_147D")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 18)
    Jump("loc_158D")

    label("loc_147D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_1491")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 20)
    Jump("loc_158D")

    label("loc_1491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_14A5")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 23)
    Jump("loc_158D")

    label("loc_14A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_14B9")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 25)
    Jump("loc_158D")

    label("loc_14B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_14CA")
    ClearScenarioFlags(0x5C, 6)
    Jump("loc_158D")

    label("loc_14CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_14DE")
    ClearScenarioFlags(0x5C, 7)
    Event(0, 30)
    Jump("loc_158D")

    label("loc_14DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 0)), scpexpr(EXPR_END)), "loc_14F2")
    ClearScenarioFlags(0x5D, 0)
    Event(0, 31)
    Jump("loc_158D")

    label("loc_14F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 1)), scpexpr(EXPR_END)), "loc_1506")
    ClearScenarioFlags(0x5D, 1)
    Event(0, 33)
    Jump("loc_158D")

    label("loc_1506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 2)), scpexpr(EXPR_END)), "loc_151A")
    ClearScenarioFlags(0x5D, 2)
    Event(0, 39)
    Jump("loc_158D")

    label("loc_151A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 3)), scpexpr(EXPR_END)), "loc_152E")
    ClearScenarioFlags(0x5D, 3)
    Event(0, 44)
    Jump("loc_158D")

    label("loc_152E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 4)), scpexpr(EXPR_END)), "loc_1542")
    ClearScenarioFlags(0x5D, 4)
    Event(0, 45)
    Jump("loc_158D")

    label("loc_1542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 5)), scpexpr(EXPR_END)), "loc_1556")
    ClearScenarioFlags(0x5D, 5)
    Event(0, 46)
    Jump("loc_158D")

    label("loc_1556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 6)), scpexpr(EXPR_END)), "loc_1567")
    ClearScenarioFlags(0x5D, 6)
    Jump("loc_158D")

    label("loc_1567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 7)), scpexpr(EXPR_END)), "loc_157E")
    ClearScenarioFlags(0x5D, 7)
    SetScenarioFlags(0x1, 5)
    Event(0, 47)
    Jump("loc_158D")

    label("loc_157E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 0)), scpexpr(EXPR_END)), "loc_158D")
    ClearScenarioFlags(0x5E, 0)
    Event(1, 17)

    label("loc_158D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_15A5")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)

    label("loc_15A5")

    Return()

    # Function_5_C0E end

    def Function_6_15A6(): pass

    label("Function_6_15A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15C2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15F5")

    label("loc_15C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15DE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15F5")

    label("loc_15DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15F5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15F5")

    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_78(0x9, 0x12)
    OP_D3(0x12, 0x0, 0x3BD08, 0x0, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_164A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_164A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_165D")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_165D")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1671")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16C2")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_1733")

    label("loc_16C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_170E")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_1733")

    label("loc_170E")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_1733")

    OP_10(0xB, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1749")
    OP_70(0xA, 0x0)
    Jump("loc_174D")

    label("loc_1749")

    OP_70(0xA, 0x1E)

    label("loc_174D")

    SetMapObjFlags(0xB, 0x4)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17C0")
    ClearMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0x18)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    SetChrPos(0x18, 6000, 0, -16200, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_74(0xB, 0x1E)
    OP_70(0xB, 0x0)
    OP_66(0x3, 0x1)
    Jump("loc_17C5")

    label("loc_17C0")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_17C5")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    OP_1B(0x4, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1805")
    OP_1B(0x0, 0x0, 0x30)
    OP_1B(0x1, 0x0, 0x31)
    OP_1B(0x2, 0x0, 0x32)
    OP_1B(0x3, 0x0, 0x33)
    OP_1B(0x4, 0x0, 0x34)

    label("loc_1805")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_181D")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_181D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_183F")
    OP_1B(0x0, 0x0, 0x30)
    OP_1B(0x1, 0x0, 0x31)
    OP_1B(0x2, 0x0, 0x32)
    OP_1B(0x4, 0x0, 0x34)

    label("loc_183F")

    Return()

    # Function_6_15A6 end

    def Function_7_1840(): pass

    label("Function_7_1840")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1966")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xA, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 30)
    AddSepith(0x1, 30)
    AddSepith(0x2, 30)
    AddSepith(0x3, 30)
    AddSepith(0x4, 30)
    AddSepith(0x5, 30)
    AddSepith(0x6, 30)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×３０\x01\x07\x02",

            "#57I水之耀晶片×３０\x01\x07\x02",

            "#58I火之耀晶片×３０\x01\x07\x02",

            "#59I风之耀晶片×３０\x01\x07\x02",

            "#60I时之耀晶片×３０\x01\x07\x02",

            "#61I空之耀晶片×３０\x01\x07\x02",

            "#62I幻之耀晶片×３０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x111, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1983")

    label("loc_1966")


    #A0002
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

    label("loc_1983")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1840 end

    def Function_8_1995(): pass

    label("Function_8_1995")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "       『克洛斯贝尔之钟』\x01",
            "Ｓ１１８５  在克洛斯贝尔自治州\x01",
            "发掘出土的巨型大钟。\x01",
            "依据出土遗迹的情况来看，\x01",
            "可推断为中世纪时期的物品。\x01",
            "使用多种金属打造而成，\x01",
            "敲打时会发出悦耳的低音。\x02",
        )
    )

    CloseMessageWindow()

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "据推测，是由当时的权贵人士所制造，\x01",
            "但关于其具体用途，\x01",
            "目前仍然诸说纷纭。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1995 end

    def Function_9_1ACF(): pass

    label("Function_9_1ACF")

    EventBegin(0x1)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有梯子。\x01",
            "要下去吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B22")
    EventEnd(0x5)
    NewScene("m0000", 125, 0, 0)
    IdleLoop()
    Jump("loc_1B24")

    label("loc_1B22")

    EventEnd(0x5)

    label("loc_1B24")

    Return()

    # Function_9_1ACF end

    def Function_10_1B25(): pass

    label("Function_10_1B25")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B1")

    Menu(
        0,
        32,
        26,
        1,
        (
            "使用警备队车辆进行移动\x01",      # 0
            "在此处休息\x01",                  # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_204E")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BCB")
    MenuCmd(1, 1, "★克洛斯贝尔市·中央区")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1BE5")

    label("loc_1BCB")

    MenuCmd(1, 1, "　克洛斯贝尔市·中央区")

    label("loc_1BE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C17")
    MenuCmd(1, 1, "★克洛斯贝尔市·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1C31")

    label("loc_1C17")

    MenuCmd(1, 1, "　克洛斯贝尔市·东出口")

    label("loc_1C31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C63")
    MenuCmd(1, 1, "★克洛斯贝尔市·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1C7D")

    label("loc_1C63")

    MenuCmd(1, 1, "　克洛斯贝尔市·西出口")

    label("loc_1C7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CAF")
    MenuCmd(1, 1, "★克洛斯贝尔市·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1CC9")

    label("loc_1CAF")

    MenuCmd(1, 1, "　克洛斯贝尔市·南出口")

    label("loc_1CC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CFB")
    MenuCmd(1, 1, "★克洛斯贝尔市·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1D15")

    label("loc_1CFB")

    MenuCmd(1, 1, "　克洛斯贝尔市·北出口")

    label("loc_1D15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3D")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1D4D")

    label("loc_1D3D")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_1D4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D75")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1D85")

    label("loc_1D75")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_1D85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB3")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1DC9")

    label("loc_1DB3")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_1DC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DF3")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1E05")

    label("loc_1DF3")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_1E05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2F")
    MenuCmd(1, 1, "★玛因兹矿山镇")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1E41")

    label("loc_1E2F")

    MenuCmd(1, 1, "　玛因兹矿山镇")

    label("loc_1E41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E71")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1E89")

    label("loc_1E71")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_1E89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EAF")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1EBD")

    label("loc_1EAF")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_1EBD")

    MenuCmd(1, 1, "　放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_203F")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0xB)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F92"),
        (1, "loc_1FA0"),
        (2, "loc_1FAE"),
        (3, "loc_1FBC"),
        (4, "loc_1FCA"),
        (5, "loc_1FD8"),
        (6, "loc_1FE6"),
        (7, "loc_1FF4"),
        (8, "loc_2002"),
        (9, "loc_2010"),
        (10, "loc_201E"),
        (11, "loc_202C"),
        (SWITCH_DEFAULT, "loc_203A"),
    )


    label("loc_1F92")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_1FA0")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_1FAE")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_1FBC")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_1FCA")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_1FD8")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_1FE6")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_1FF4")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_2002")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_2010")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_201E")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_202C")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_203A")

    label("loc_203A")

    Jump("loc_2049")

    label("loc_203F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2049")

    Jump("loc_20AC")

    label("loc_204E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2099")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_20AC")

    label("loc_2099")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20AC")

    Jump("loc_1B3F")

    label("loc_20B1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1B25 end

    def Function_11_20B9(): pass

    label("Function_11_20B9")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 2400, 0, -16530, 270)
    SetChrPos(0x1, 2400, 0, -16530, 270)
    SetChrPos(0x2, 2400, 0, -16530, 270)
    SetChrPos(0x3, 2400, 0, -16530, 270)
    SetChrPos(0x4, 2400, 0, -16530, 270)
    SetChrPos(0x5, 2400, 0, -16530, 270)
    Sleep(1)
    OP_68(2400, 1900, -16530, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_218D")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_2193")

    label("loc_218D")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_2193")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_20B9 end

    def Function_12_21A8(): pass

    label("Function_12_21A8")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Return()

    # Function_12_21A8 end

    def Function_13_21B6(): pass

    label("Function_13_21B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50003.itc", 0x1E)
    LoadChrToIndex("apl/ch50004.itc", 0x1F)
    LoadChrToIndex("apl/ch50005.itc", 0x20)
    LoadChrToIndex("chr/ch20800.itc", 0x21)
    LoadChrToIndex("chr/ch20900.itc", 0x22)
    LoadChrToIndex("chr/ch21100.itc", 0x23)
    SoundLoad(803)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_68(-18000, 2000, 7500, 0)
    MoveCamera(28, 9, 0, 0)
    OP_6E(820, 0)
    SetCameraDistance(13000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 2900, 0, -21300, 0)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x16, 2600, 0, -23600, 0)
    SetChrPos(0x17, 3700, 0, -23800, 0)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -16700, 0, 2500, 315)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 7100, 0, -16600, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 200, 0, -2300, 270)
    SetChrPos(0xB, -1100, 0, -2300, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, -6300, 0, -9200, 135)
    SetChrPos(0x10, -5300, 0, -10200, 315)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, -4300, 0, 17300, 270)
    SetChrPos(0xD, -6200, 0, 17300, 90)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -6300, 100, 4300, 270)
    OP_4B(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    OP_4B(0xB, 0xFF)
    BeginChrThread(0xB, 0, 0, 0)
    OP_4B(0x11, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x8, 0x18)
    OP_78(0x9, 0x19)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetMapObjFlags(0x8, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x19, 0x4)
    OP_49()
    SetChrPos(0x18, 11500, 0, 19500, 0)
    OP_D3(0x18, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x19, 0, 0, 14000, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x1E)
    OP_E5()
    Sound(803, 2, 0, 0)
    BeginChrThread(0x23, 1, 0, 55)
    OP_68(-17000, 2000, 7000, 9000)
    MoveCamera(18, 9, 0, 9000)
    SetCameraDistance(17000, 9000)
    BeginChrThread(0x11, 3, 0, 16)
    FadeToBright(2000, 0)
    OP_0D()
    BeginChrThread(0x19, 3, 0, 14)
    BeginChrThread(0x23, 2, 0, 17)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(300)
    Fade(500)
    OP_68(2500, 1900, -1600, 0)
    MoveCamera(42, 5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27000, 0)
    ClearMapObjFlags(0x8, 0x4)
    SetCameraDistance(32000, 8000)
    BeginChrThread(0x18, 3, 0, 15)
    OP_6F(0x10)
    Fade(1000)
    PlaceName2(340, 200, "c_plac02", 0x0, 1500)
    OP_68(0, 800, 4000, 0)
    MoveCamera(18, 22, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(28000, 0)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    MoveCamera(42, 22, 0, 9000)
    SetCameraDistance(33000, 9000)
    OP_6F(0x40)
    OP_6F(0x10)
    Fade(500)
    OP_68(3400, 800, -12300, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    Sleep(1)
    SetCameraDistance(19000, 5000)
    EndChrThread(0x23, 0x1)
    BeginChrThread(0x23, 1, 0, 56)

    def lambda_2606():
        OP_95(0xFE, 2900, 0, -11300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2606)
    Sleep(100)

    def lambda_2623():
        OP_95(0xFE, 2600, 0, -13600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2623)
    Sleep(50)

    def lambda_2640():
        OP_95(0xFE, 3700, 0, -13800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2640)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x50, 0x1F4)
    Sleep(500)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x23, 0x2)
    OP_E6()
    Sound(1080, 255, 90, 0)    #voice#Lloyd
    Sleep(1000)

    #C0006
    ChrTalk(
        0x101,
        (
            "#0005F#5P哇～……\x01",
            "还真是大变样啊。\x02\x03",

            "#0012F连百货店也完全\x01",
            "焕然一新了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    #C0007
    ChrTalk(
        0x101,
        "#0005F#5P哎，那边的建筑物是……？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x16,
        (
            "#12P那是去年才刚刚开业的\x01",
            "『导力商店』哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x16,
        (
            "#12P那家店不仅经营各种最新的导力制品，\x01",
            "甚至连导力车都有销售呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x16,
        (
            "#12P帝国产、共和国产、利贝尔产、\x01",
            "爱普斯泰恩产……可谓一应俱全呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0011
    ChrTalk(
        0x101,
        (
            "#0006F#5P哈～那可真是不得了啊。\x02\x03",

            "#0000F而且……\x01",
            "导力车的数量好像也明显增加了。\x02\x03",

            "三年前都还几乎\x01",
            "见不到一辆呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x17,
        (
            "呵呵，即使是现在，那终究也只是\x01",
            "有钱人专用的奢侈品啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x17,
        (
            "不过说心里话，导力巴士增加了班数，\x01",
            "这倒真是一大幸事。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x17,
        (
            "像南边的医院，坐车的话\x01",
            "只要三十分钟左右就能到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0002F#5P嘿，那可真是比以前便利许多啊。\x02\x03",

            "#0004F是吗……\x01",
            "仅仅三年，就有了如此大的变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x16,
        "#12P那么，就在这里说再见吧。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x16,
        "#12P你还要去就职单位报到吧？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0018
    ChrTalk(
        0x101,
        (
            "#0005F#5P啊，是啊……\x02\x03",

            "不过，难得相遇，本来还想帮二位\x01",
            "把行李送到家里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x17,
        "哎呀呀，那可不行哦。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x17,
        (
            "第一次报到出勤，\x01",
            "怎么能迟到呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x16,
        (
            "#12P没错没错。\x01",
            "无论做什么，良好的开端都是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0012F#5P哈哈，确实如此呢。\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 2700, 0, -12500, 2000, 0x0)
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_96(0x101, 0xB54, 0x0, 0xFFFFD3DC, 0x7D0, 0x0)

    #C0023
    ChrTalk(
        0x16,
        (
            "#12P不过，你刚刚回来，\x01",
            "有住的地方吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x16,
        (
            "#12P如果愿意来东街，\x01",
            "我倒是能给你介绍个住宿的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#0002F#5P啊，多谢您的好意了，\x01",
            "不过我们那里似乎会提供宿舍。\x02\x03",

            "托运的行李\x01",
            "应该也都送到那边去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x16,
        "#12P哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x17,
        (
            "我们就住在东街的\x01",
            "出口附近。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x17,
        (
            "要是以后遇到了什么困难，\x01",
            "随时都可以来找我们哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0009F#5P嗯！那就先谢谢您了。\x02\x03",

            "#0002F等我安顿下来之后，\x01",
            "一定会去拜访两位的。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x16,
        "#12P唔，要保重啊。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x17,
        "那就在这里说再见啦。\x02",
    )

    CloseMessageWindow()
    OP_92(0x16, 0x2E18, 0xFFFFEB4C, 0x1F4)

    def lambda_2C7B():
        OP_95(0xFE, 11800, 0, -5300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2C7B)
    Sleep(300)

    def lambda_2C98():

        label("loc_2C98")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_2C98")

    QueueWorkItem2(0x101, 2, lambda_2C98)
    Sleep(200)
    OP_92(0x17, 0x2C24, 0xFFFFE4A8, 0x1F4)

    def lambda_2CBA():
        OP_95(0xFE, 11300, 0, -7000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2CBA)
    WaitChrThread(0x16, 1)

    def lambda_2CD8():
        OP_95(0xFE, 21800, 0, -5300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2CD8)
    WaitChrThread(0x17, 1)

    def lambda_2CF6():
        OP_95(0xFE, 21300, 0, -7000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2CF6)
    Sleep(1000)
    EndChrThread(0x101, 0x2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x10E, 0x1F4)

    #C0032
    ChrTalk(
        0x101,
        "#0005F#11P哎……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    OP_68(-25800, -1600, -16400, 3500)
    MoveCamera(45, 14, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(30500, 3500)
    OP_6F(0x79)
    Sleep(500)

    #A0033
    AnonymousTalk(
        0x101,
        (
            "#0000F那座混居大楼……\x01",
            "还完好地保留着啊。\x02\x03",

            "我记得克洛斯贝尔时代周刊社以前\x01",
            "好像就在这里面……\x02\x03",

            "#0012F哈哈，虽然很怀念，但如此破旧的大楼\x01",
            "坐落在这光鲜亮丽的街道上，看起来还真是突兀呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(3120, 800, -11310, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_0D()

    #C0034
    ChrTalk(
        0x101,
        "#0003F#11P那么……时间差不多也快到了。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德从怀中\x01",
            "取出一封书信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "任命罗伊德·班宁斯警官\x01",
            "至克洛斯贝尔警察局总部的\x01",
            "特别任务支援科就职。\x01",
            "请于指定日期来警察局总部报到。\x01",
            "　　　　　　　　克洛斯贝尔警察局·人事科\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0037
    AnonymousTalk(
        0x101,
        (
            "#0001F#11P特别任务支援科……\x01",
            "在警察学校上课时从来\x01",
            "没听过这个名字。\x02\x03",

            "连制服都还没有收到，\x01",
            "到底是个怎样的部门呢……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    #C0038
    ChrTalk(
        0x101,
        (
            "#0004F#11P──算了。\x01",
            "总之去了就知道了。\x02\x03",

            "幸好警察局的位置应该\x01",
            "没有什么变化……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)
    #Sound(1000, 255, 100, 0)    #voice#Lloyd
    Sleep(500)

    #C0039
    ChrTalk(
        0x101,
        "#0000F#11P好，这就去报到吧！！\x02",
    )

    CloseMessageWindow()

    def lambda_310F():
        OP_95(0xFE, 9000, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_310F)
    Sleep(2000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    OP_6F(0x10)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_21B6 end

    def Function_14_317F(): pass

    label("Function_14_317F")

    Sleep(1000)
    Sound(461, 0, 70, 0)
    OP_71(0x9, 0x1F, 0x3C, 0x0, 0x0)
    OP_79(0x9)
    Sleep(1000)
    OP_71(0x9, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x9)

    def lambda_31AE():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_31AE)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    WaitChrThread(0x19, 2)

    def lambda_31D9():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_31D9)
    WaitChrThread(0x19, 1)
    Return()

    # Function_14_317F end

    def Function_15_31F3(): pass

    label("Function_15_31F3")


    def lambda_31F8():
        OP_96(0xFE, 0x2CEC, 0x0, 0x1964, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_31F8)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    WaitChrThread(0x18, 1)
    WaitChrThread(0x19, 2)
    Sound(458, 0, 100, 0)

    def lambda_322C():
        OP_9E(0xFE, 0x0, 0x1964, 0x15F90, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_322C)
    WaitChrThread(0x18, 1)

    def lambda_324B():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_324B)
    WaitChrThread(0x18, 1)
    Return()

    # Function_15_31F3 end

    def Function_16_3265(): pass

    label("Function_16_3265")


    def lambda_326A():
        OP_95(0xFE, -21700, 100, 7500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_326A)
    WaitChrThread(0x11, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x6)

    def lambda_32A3():
        OP_95(0xFE, -22700, 0, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_32A3)

    def lambda_32BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_32BD)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x11, 2)
    Sleep(500)
    Sound(104, 0, 100, 0)
    OP_71(0x6, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x6)
    SetMapObjFlags(0x6, 0x10)
    Return()

    # Function_16_3265 end

    def Function_17_32F0(): pass

    label("Function_17_32F0")

    Sleep(4000)
    Sound(457, 0, 100, 0)
    Return()

    # Function_17_32F0 end

    def Function_18_32FA(): pass

    label("Function_18_32FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch21200.itc", 0x1F)
    LoadChrToIndex("chr/ch21400.itc", 0x20)
    LoadChrToIndex("chr/ch20000.itc", 0x21)
    LoadChrToIndex("chr/ch23600.itc", 0x22)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xB4, 0xD7, 0xE6, 0xF, 0x82, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 15000, 0, -3000, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, -15000, 0, -6300, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -6800, 0, 4000, 270)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -8300, 0, 2500, 90)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -19300, 0, 19400, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, 7000, 0, 12000, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_3539():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3539)

    def lambda_3553():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3553)

    def lambda_356D():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_356D)
    Sound(458, 0, 100, 0)

    def lambda_358E():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_358E)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x23, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_32FA end

    def Function_19_3632(): pass

    label("Function_19_3632")

    Sound(803, 2, 100, 0)
    Sleep(4000)
    OP_25(0x323, 0x5A)
    Sleep(100)
    OP_25(0x323, 0x50)
    Sleep(100)
    OP_25(0x323, 0x46)
    Sleep(100)
    OP_25(0x323, 0x3C)
    Sleep(100)
    OP_25(0x323, 0x32)
    Sleep(100)
    OP_25(0x323, 0x28)
    Sleep(100)
    OP_25(0x323, 0x1E)
    Sleep(100)
    OP_25(0x323, 0x14)
    Sleep(100)
    OP_25(0x323, 0xA)
    Sleep(100)
    OP_24(0x323)
    Return()

    # Function_19_3632 end

    def Function_20_367E(): pass

    label("Function_20_367E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09300.itc", 0x1E)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    OP_78(0x8, 0x18)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x18, 25000, 0, -2600, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -14500, 0, -500, 90)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -15500, 0, 1000, 90)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_383B():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_383B)

    def lambda_3855():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_3855)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)

    def lambda_388F():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_388F)
    Sleep(2000)

    def lambda_38AC():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_38AC)
    Sleep(1000)
    Sound(456, 0, 100, 0)

    def lambda_38CF():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_38CF)
    Sleep(1000)

    def lambda_38EC():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_38EC)
    WaitChrThread(0x18, 1)
    OP_6F(0x79)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_79(0x8)
    OP_68(0, 1000, -6600, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -600, 0, -7800, 0)
    SetChrPos(0x102, 700, 0, -7800, 0)
    SetChrPos(0x103, -600, 0, -9100, 0)
    SetChrPos(0x104, 700, 0, -9100, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    SetChrPos(0x1A, 0, 0, -5500, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrPos(0x18, 0, 0, -2600, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    ClearChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    OP_70(0x8, 0x1E)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0040
    ChrTalk(
        0x101,
        (
            "#12P#0002F──真是非常感谢，\x01",
            "还麻烦您一直把我们送到这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x1A,
        (
            "#3609F#5P哈哈，这没什么，\x01",
            "不过就是顺路而已。\x02\x03",

            "#3600F各位，事件的调查\x01",
            "还请加油。\x02\x03",

            "我也会声援大家的。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0102F谢谢您。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#12P#0202F……既然要为我们声援，那以后您如果遇到\x01",
            "什么困难，请务必来支援科找我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0309F对对，可以的话，别去找游击士协会了。\x01",
            "优先考虑我们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3BBE():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BBE)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3BE0():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BE0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)

    #C0045
    ChrTalk(
        0x101,
        "#1P#0011F你、你们两个！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#5P#0106F这也……说得太露骨了吧。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0302F哈哈哈，偶尔也要\x01",
            "打打广告才行嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#12P#0204F对营业活动来说，宣传可是很重要的。\x02",
    )

    CloseMessageWindow()

    def lambda_3CA1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CA1)
    Sleep(50)

    def lambda_3CB1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3CB1)

    #C0049
    ChrTalk(
        0x1A,
        (
            "#3609F#5P哈哈，明白了。\x02\x03",

            "#3600F如果以后遇到了什么困难，\x01",
            "我就不客气地登门拜访了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0050
    ChrTalk(
        0x1A,
        (
            "#3605F#5P对了……这东西\x01",
            "对各位有用处吗？\x02\x03",

            "#3600F哈哈，对警察来说，\x01",
            "说不定没有什么用吧……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x6, 1)
    OP_C7(0x1, 0x1000)

    #C0052
    ChrTalk(
        0x102,
        (
            "#0105F这个……\x01",
            "好像是市内的地图啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x1A,
        (
            "#3600F#5P这是从上个月开始，\x01",
            "为游客准备的商品。\x01",
            "不嫌弃的话，就请各位拿去用吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#12P#0002F这个……在市内巡逻时，\x01",
            "说不定真的很便利呢。\x02\x03",

            "#0004F哈罗德先生，非常感谢您。\x01",
            "我们会善加使用的。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x1A,
        (
            "#3609F#5P哈哈，请不要客气，不过是件粗陋之物而已。\x02\x03",

            "#3600F那么，我就先行告辞了，\x01",
            "各位，工作还请多多加油。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_92(0x1A, 0x0, 0xFFFFEF98, 0x1F4)

    def lambda_3F44():
        OP_95(0xFE, 0, 0, -4200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3F44)
    WaitChrThread(0x1A, 1)

    def lambda_3F62():
        OP_95(0xFE, 0, 0, -3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3F62)

    def lambda_3F7C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_3F7C)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1A, 2)
    Sound(461, 0, 100, 0)
    OP_71(0x8, 0x1F, 0x3C, 0x0, 0x0)
    OP_79(0x8)

    def lambda_3FAA():

        label("loc_3FAA")

        TurnDirection(0x101, 0x18, 500)
        Yield()
        Jump("loc_3FAA")

    QueueWorkItem2(0x101, 1, lambda_3FAA)

    def lambda_3FBC():

        label("loc_3FBC")

        TurnDirection(0x102, 0x18, 500)
        Yield()
        Jump("loc_3FBC")

    QueueWorkItem2(0x102, 1, lambda_3FBC)

    def lambda_3FCE():

        label("loc_3FCE")

        TurnDirection(0x103, 0x18, 500)
        Yield()
        Jump("loc_3FCE")

    QueueWorkItem2(0x103, 1, lambda_3FCE)

    def lambda_3FE0():

        label("loc_3FE0")

        TurnDirection(0x104, 0x18, 500)
        Yield()
        Jump("loc_3FE0")

    QueueWorkItem2(0x104, 1, lambda_3FE0)
    Fade(1000)
    OP_68(0, 500, -2600, 0)
    MoveCamera(30, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    Sound(457, 0, 100, 0)
    OP_71(0x8, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x8)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-10000, 500, -2600, 3000)
    SetCameraDistance(18500, 3000)
    MoveCamera(0, 30, 0, 3000)

    def lambda_406C():
        OP_98(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_406C)
    WaitChrThread(0x18, 1)
    OP_6F(0x11)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8000)
    ClearMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x8, 0x4)
    Fade(500)
    OP_68(190, 1000, -8370, 0)
    MoveCamera(337, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17580, 0)
    OP_0D()
    Sleep(300)

    #C0056
    ChrTalk(
        0x101,
        (
            "#11P#0000F呼……\x01",
            "真是个大好人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#6P#0204F……是啊。\x02\x03",

            "#0202F好人等级似乎都可以和\x01",
            "罗伊德前辈相媲美了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0058
    ChrTalk(
        0x101,
        "#11P#0006F那个……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#0303F#12P哈，但再怎么说，\x01",
            "他也是个贸易商。\x02\x03",

            "#0300F如果只是个单纯的老好人，\x01",
            "我想根本就干不下去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#0104F#2P不过，哈罗德先生似乎与\x01",
            "当地产业保持着良好的合作关系，\x01",
            "同时稳定踏实地发展自身业务。\x02\x03",

            "#0100F一直都听说克洛斯贝尔的贸易商\x01",
            "大多都通过国际贸易来不择手段地\x01",
            "大发横财……\x02\x03",

            "在这些人之中，哈罗德先生的\x01",
            "诚实善良算是十分难能可贵吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        "#0305F#12P原来如此，是这样啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0062
    ChrTalk(
        0x101,
        (
            "#11P#0003F既有哈罗德先生这样正直的好人，\x01",
            "也有鲁巴彻商会那种组织。\x02\x03",

            "#0000F……这就是如今的克洛斯贝尔吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        (
            "#0103F#2P嗯，是啊……\x02\x03",

            "#0100F所以我才觉得，现在的克洛斯贝尔\x01",
            "也并非无可救药。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#11P#0004F是啊……我也是这么想的。\x02",
    )

    CloseMessageWindow()

    def lambda_43E5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43E5)
    Sleep(100)

    def lambda_43F5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43F5)
    Sleep(50)

    def lambda_4405():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4405)
    Sleep(50)

    def lambda_4415():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4415)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(500)

    #C0065
    ChrTalk(
        0x101,
        (
            "#5P#0000F──那么，都已经过午了。\x02\x03",

            "接下来，该前往下个目的地了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#0100F#2P嗯……\x01",
            "是『圣乌尔斯拉医科大学』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x103,
        (
            "#6P#0203F……………………………………\x02\x03",

            "#0200F……是在南出口方向吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，从这里一直向南走，\x01",
            "就能看到巴士站了。\x02\x03",

            "听说巴士每三十分钟\x01",
            "就会来一班。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0305F#12P这样啊，那还真是方便。\x02\x03",

            "#0300F好了。\x01",
            "总之，我们就先出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#5P#0000F好的……\x02\x03",

            "#0004F（医科大学吗……\x01",
            "  终于能见到塞茜尔姐姐了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis203.itp")
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可以使用克洛斯贝尔市内地图了。\x02",
        )
    )

    CloseMessageWindow()

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在市内区域中按下START键，\x01",
            "就可以打开市内的全体图。\x01",
            "（再次按下START键，\x01",
            "  就会切换到自治州地图。）\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在市内打开地图时，\x01",
            "可以直接移动到\x01",
            "各区域内。\x02",
        )
    )

    CloseMessageWindow()

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "想要直接移动，请在左边的街区列表中\x01",
            "选择要去的场所。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #A0075
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
    OP_D5(0x1E)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -7800, 0)
    SetScenarioFlags(0x61, 1)
    OP_29(0x3F, 0x1, 0x5)
    EndChrThread(0x23, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_367E end

    def Function_21_480E(): pass

    label("Function_21_480E")

    OP_9F(0x0, 0x18)
    OP_9F(0x1, 17420, 0, -4780)
    OP_9F(0x1, 9540, 0, -2690)
    OP_9F(0x1, 1040, 0, -2580)
    OP_9F(0x2, 0x18, 6000, 0x6)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x8)
    Return()

    # Function_21_480E end

    def Function_22_4855(): pass

    label("Function_22_4855")

    OP_93(0xFE, 0x104, 0x32)
    OP_9F(0x0, 0x18)
    OP_9F(0x1, -5850, 0, -3450)
    OP_9F(0x1, -16290, 0, -3810)
    OP_9F(0x1, -28280, -1380, -3420)
    OP_9F(0x2, 0x18, 6000, 0x6)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x8)
    Return()

    # Function_22_4855 end

    def Function_23_48A3(): pass

    label("Function_23_48A3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    LoadChrToIndex("chr/ch28100.itc", 0x1F)
    LoadChrToIndex("chr/ch21200.itc", 0x20)
    LoadChrToIndex("chr/ch21400.itc", 0x21)
    LoadChrToIndex("chr/ch20000.itc", 0x22)
    LoadChrToIndex("chr/ch23600.itc", 0x23)
    LoadEffect(0x0, "event\\eva05_00.eff")
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -30600, -8200, -24900, 270)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 15000, 0, -3000, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, -15000, 0, -6300, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -6800, 0, 4000, 270)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -8300, 0, 2500, 90)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -19300, 0, 19400, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, 7000, 0, 12000, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_4AD5():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4AD5)

    def lambda_4AEF():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4AEF)

    def lambda_4B09():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_4B09)
    Sound(458, 0, 100, 0)

    def lambda_4B2A():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4B2A)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    SetChrPos(0x101, 10600, 0, 24000, 180)
    SetChrPos(0x102, 12000, 0, 24000, 180)
    SetChrPos(0x103, 10600, 0, 25400, 180)
    SetChrPos(0x104, 12000, 0, 25400, 180)

    def lambda_4BB7():
        OP_95(0xFE, 10600, 0, 19000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BB7)
    Sleep(100)

    def lambda_4BD4():
        OP_95(0xFE, 12000, 0, 19000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BD4)
    Sleep(100)

    def lambda_4BF1():
        OP_96(0xFE, 0x2968, 0x0, 0x4FB0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4BF1)
    Sleep(100)

    def lambda_4C0E():
        OP_95(0xFE, 12000, 0, 20400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4C0E)
    Sound(829, 0, 100, 0)
    Fade(1000)
    OP_68(11300, 1000, 19700, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(20500, 3000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetMapObjFlags(0x9, 0x4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    #C0076
    ChrTalk(
        0x101,
        "#6P#0006F呼啊啊啊啊～……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        "#0106F#5P真的好困……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#5P#0306F毕竟我们昨天\x01",
            "差不多熬了一个通宵啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#0206F……已经要到极限了。\x02",
    )

    CloseMessageWindow()

    def lambda_4D7B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D7B)
    Sleep(150)

    def lambda_4D8B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D8B)
    Sleep(50)

    def lambda_4D9B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4D9B)
    Sleep(50)

    def lambda_4DAB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4DAB)
    WaitChrThread(0x104, 2)
    Sleep(300)

    #C0080
    ChrTalk(
        0x101,
        (
            "#6P#0004F总之，回去以后，\x01",
            "大家好好睡一觉吧。\x02\x03",

            "#0000F之后再向科长报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        "#0100F好啊……\x02",
    )

    CloseMessageWindow()

    def lambda_4E1F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E1F)
    Sleep(200)

    def lambda_4E2F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E2F)
    Sleep(100)

    def lambda_4E3F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4E3F)
    Sleep(100)

    def lambda_4E4F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4E4F)
    WaitChrThread(0x101, 2)

    def lambda_4E60():
        OP_95(0xFE, 10600, 0, 8800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E60)
    WaitChrThread(0x102, 2)

    def lambda_4E7E():
        OP_95(0xFE, 12000, 0, 8800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E7E)
    WaitChrThread(0x103, 2)

    def lambda_4E9C():
        OP_96(0xFE, 0x2968, 0x0, 0x27D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4E9C)
    WaitChrThread(0x104, 2)

    def lambda_4EBA():
        OP_95(0xFE, 12000, 0, 10200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4EBA)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_6F(0x10)
    EndChrThread(0x23, 0x1)
    OP_68(-19000, -7100, -22800, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    OP_90(0x101, -16400, -6350, -19400, 225)
    OP_90(0x102, -15600, -6350, -20200, 225)
    OP_90(0x104, -15200, -5350, -18200, 225)
    OP_90(0x103, -14400, -5350, -19000, 225)
    PlayEffect(0x0, 0x0, 0x1B, 0x140, 0, 1300, 350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4F9E():
        OP_95(0xFE, -19700, -8200, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F9E)
    Sleep(50)

    def lambda_4FBB():
        OP_96(0xFE, 0xFFFFB62C, 0xFFFFDFF8, 0xFFFFA434, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4FBB)
    Sleep(50)

    def lambda_4FD8():
        OP_95(0xFE, -20900, -8200, -23900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FD8)
    Sleep(50)

    def lambda_4FF5():
        OP_95(0xFE, -20100, -8200, -24700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4FF5)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_501D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_501D)
    WaitChrThread(0x102, 1)

    def lambda_502E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_502E)
    WaitChrThread(0x103, 1)

    def lambda_503F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_503F)
    WaitChrThread(0x104, 1)

    def lambda_5050():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5050)
    OP_6F(0x11)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0082
    ChrTalk(
        0x102,
        "#11P#0105F啊……？\x02",
    )

    CloseMessageWindow()
    OP_68(-28620, -7100, -24980, 2000)
    MoveCamera(35, 23, 0, 2000)
    SetCameraDistance(17000, 2000)
    OP_6F(0x79)
    OP_93(0x1B, 0x5A, 0x1F4)
    Sleep(300)

    #C0083
    ChrTalk(
        0x1B,
        "#6P#1002F哟～大家辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_68(-29600, -7100, -24900, 2000)

    def lambda_5123():
        OP_96(0xFE, 0xFFFF9048, 0xFFFFDFF8, 0xFFFFA0B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5123)
    Sleep(50)

    def lambda_5140():
        OP_96(0xFE, 0xFFFF9048, 0xFFFFDFF8, 0xFFFF9C64, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5140)
    Sleep(50)

    def lambda_515D():
        OP_96(0xFE, 0xFFFF95C0, 0xFFFFDFF8, 0xFFFFA0B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_515D)
    Sleep(50)

    def lambda_517A():
        OP_96(0xFE, 0xFFFF95C0, 0xFFFFDFF8, 0xFFFF9C64, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_517A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)

    #C0084
    ChrTalk(
        0x101,
        "#11P#0011F科长……怎么了？\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0302F难道是特意出来迎接\x01",
            "我们的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_52D8")

    #C0086
    ChrTalk(
        0x1B,
        (
            "#6P#1011F哈，我怎么会做\x01",
            "那种肉麻的事情。\x02\x03",

            "#1002F总之呢，事情的经由，\x01",
            "我在和索妮亚的导力通讯中已经听说了。\x02\x03",

            "就初次进行市外活动来说，\x01",
            "你们已经算是相当努力了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#11P#0000F谢、谢谢……\x01",
            "（……这是在夸奖我们吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54B3")

    label("loc_52D8")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_53CA")

    #C0088
    ChrTalk(
        0x1B,
        (
            "#6P#1011F哈，我怎么会做\x01",
            "那种肉麻的事情。\x02\x03",

            "#1002F总之呢，事情的经由，\x01",
            "我在和索妮亚的导力通讯中已经听说了。\x02\x03",

            "#1004F虽然有些运气成分在内，\x01",
            "但你们也算是很努力了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#11P#0005F是、是的。\x01",
            "（我们果然还是不够成熟吗……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54B3")

    label("loc_53CA")


    #C0090
    ChrTalk(
        0x1B,
        (
            "#6P#1011F哈，我怎么会做\x01",
            "那种肉麻的事情。\x02\x03",

            "#1002F总之呢，事情的经由，\x01",
            "我在和索妮亚的导力通讯中已经听说了。\x02\x03",

            "#1003F虽然觉得你们实在是太过依赖运气了，\x01",
            "不过算了，只要结果ＯＫ就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#11P#0006F……十分抱歉。\x01",
            "（无言以对啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54B3")

    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0092
    ChrTalk(
        0x102,
        (
            "#11P#0100F那……\x01",
            "科长您究竟是在这里做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#11P#0200F如果只是为了在早饭之后出来吸烟，\x01",
            "这地方也太奇怪了吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x1B,
        (
            "#6P#1011F呵……那也没办法吧？\x02\x03",

            "#1001F突然来了那种客人，再怎么说，\x01",
            "也没法继续在那里安安稳稳地吸烟了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0095
    ChrTalk(
        0x101,
        "#11P#0005F那种客人……？\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        "#0305F到底是谁来了？\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x1B,
        (
            "#6P#1000F不认识……\x01",
            "不是来找你们的吗？\x02\x03",

            "该说是莫名其妙地自来熟吗……\x01",
            "总之真是一点也不客气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#11P#0001F哎？\x01",
            "总之，那位客人还在里面吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(300)

    #C0099
    ChrTalk(
        0x102,
        "#12P#0101F……进去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(400)

    def lambda_5708():

        label("loc_5708")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5708")

    QueueWorkItem2(0x1B, 2, lambda_5708)

    def lambda_571A():

        label("loc_571A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_571A")

    QueueWorkItem2(0x103, 2, lambda_571A)

    def lambda_572C():

        label("loc_572C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_572C")

    QueueWorkItem2(0x104, 2, lambda_572C)
    BeginChrThread(0x102, 3, 0, 24)

    def lambda_5744():
        OP_95(0xFE, -28600, -8200, -22600, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5744)
    WaitChrThread(0x101, 1)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_577D():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_577D)
    Sleep(1200)

    def lambda_5795():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5795)
    WaitChrThread(0x101, 2)
    Sleep(300)

    def lambda_57AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_57AD)
    WaitChrThread(0x102, 2)
    Sleep(300)

    def lambda_57C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_57C5)
    WaitChrThread(0x104, 2)
    FadeToDark(1000, 0, -1)
    Sleep(300)

    def lambda_57E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_57E7)
    OP_0D()
    WaitChrThread(0x103, 2)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x1B, 0x2)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    StopEffect(0x0, 0x0)
    SetScenarioFlags(0x5C, 5)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_48A3 end

    def Function_24_5848(): pass

    label("Function_24_5848")

    Sleep(600)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_5858():
        OP_95(0xFE, -29300, -8200, -23000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5858)
    Sleep(800)

    def lambda_5875():
        OP_95(0xFE, -28600, -8200, -24000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5875)
    Sleep(100)

    def lambda_5892():
        OP_95(0xFE, -29300, -8200, -24400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5892)
    WaitChrThread(0x102, 1)

    def lambda_58B0():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58B0)
    WaitChrThread(0x104, 1)

    def lambda_58CE():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_58CE)
    WaitChrThread(0x103, 1)

    def lambda_58EC():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58EC)
    Return()

    # Function_24_5848 end

    def Function_25_5902(): pass

    label("Function_25_5902")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrPos(0x101, -23800, -8200, -23800, 270)
    SetChrPos(0x104, -23000, -8200, -24600, 270)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x8, 0x18)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    ClearMapObjFlags(0x8, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, -1500, 0, -5500, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x8, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -14500, 0, -500, 90)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -15500, 0, 1000, 90)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_5AB0():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_5AB0)

    def lambda_5ACA():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_5ACA)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 28)
    FadeToBright(2000, 0)
    Sleep(4850)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 27)
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    EndChrThread(0x23, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 6)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_5902 end

    def Function_26_5B9B(): pass

    label("Function_26_5B9B")


    def lambda_5BA0():
        OP_95(0xFE, -28400, -8200, -23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BA0)
    WaitChrThread(0x101, 1)

    def lambda_5BBE():
        OP_95(0xFE, -28400, -8200, -22300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BBE)
    WaitChrThread(0x101, 1)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_5BF7():
        OP_95(0xFE, -28400, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BF7)
    Sleep(500)

    def lambda_5C14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C14)
    WaitChrThread(0x101, 1)
    Return()

    # Function_26_5B9B end

    def Function_27_5C25(): pass

    label("Function_27_5C25")


    def lambda_5C2A():
        OP_95(0xFE, -28800, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C2A)
    WaitChrThread(0x104, 1)

    def lambda_5C48():
        OP_95(0xFE, -28800, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C48)
    Sleep(1500)

    def lambda_5C65():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5C65)
    WaitChrThread(0x104, 1)
    Return()

    # Function_27_5C25 end

    def Function_28_5C76(): pass

    label("Function_28_5C76")

    Sound(803, 2, 100, 0)
    Sleep(5000)
    OP_25(0x323, 0x5A)
    Sleep(200)
    OP_25(0x323, 0x50)
    Sleep(200)
    OP_25(0x323, 0x46)
    Sleep(200)
    OP_25(0x323, 0x3C)
    Sleep(200)
    OP_25(0x323, 0x32)
    Sleep(200)
    OP_25(0x323, 0x28)
    Sleep(200)
    OP_25(0x323, 0x1E)
    Sleep(200)
    OP_25(0x323, 0x14)
    Sleep(200)
    OP_25(0x323, 0xA)
    Sleep(200)
    OP_24(0x323)
    Return()

    # Function_28_5C76 end

    def Function_29_5CC2(): pass

    label("Function_29_5CC2")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch02300.itc", 0x1E)
    OP_68(-21100, -7100, -24900, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -20800, -8200, -25500, 270)
    SetChrPos(0x102, -20800, -8200, -24300, 270)
    SetChrPos(0x103, -19400, -8200, -25700, 270)
    SetChrPos(0x104, -19400, -8200, -24500, 270)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -29000, -8200, -24900, 0)
    ModifyEventFlags(0, 0, 0x80)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02600.itp")
    FadeToBright(1000, 0)
    Sleep(600)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x102,
        "#11P#0105F哎……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#11P#0005F那个人是……\x02",
    )

    CloseMessageWindow()
    OP_68(-27700, -7100, -24900, 2500)
    OP_6F(0x1)
    Fade(500)
    OP_68(-27960, -7100, -24530, 0)
    MoveCamera(318, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15420, 0)

    def lambda_5E94():
        OP_95(0xFE, -26800, -8200, -24300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E94)
    Sleep(100)

    def lambda_5EB1():
        OP_95(0xFE, -26800, -8200, -25500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EB1)
    Sleep(100)

    def lambda_5ECE():
        OP_95(0xFE, -25400, -8200, -25700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5ECE)
    Sleep(100)

    def lambda_5EEB():
        OP_95(0xFE, -25400, -8200, -24500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5EEB)
    Sleep(500)
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x1C, 0x5A, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0102
    AnonymousTalk(
        0x1C,
        (
            "──啊啊，太好了！\x02\x03",

            "我还在疑惑到底\x01",
            "是不是在这里。\x02",
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

    #C0103
    ChrTalk(
        0x102,
        (
            "#12P#0105F阿奈斯特先生……\x02\x03",

            "#0100F……莫非你是来\x01",
            "找我的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x1C,
        (
            "#5P#2600F是啊，正好有些事情要去事务所，\x01",
            "所以就顺路过来拜访你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0105
    ChrTalk(
        0x1C,
        (
            "#5P#2605F……艾莉？\x02\x03",

            "#2601F怎么了？\x01",
            "气色好像很不好啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        "#12P#0108F啊……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x1C,
        (
            "#5P#2603F之前你们似乎去了\x01",
            "彩虹剧团……\x02\x03",

            "#2601F是不是警务工作遇到了什么问题？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#12P#0106F……没、没什么。\x01",
            "只是些小事而已。\x02\x03",

            "#0108F那个，其实是剧团的相关人员\x01",
            "曾来找我们进行过商谈……\x02\x03",

            "#0102F只是前去报告一下而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1C)

    #C0109
    ChrTalk(
        0x1C,
        (
            "#5P#2606F……呼，我本来还在犹豫\x01",
            "是不是该来这里。\x02\x03",

            "#2600F看来选择过来，果然还是正确的。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x102,
        "#12P#0105F哎……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x1C,
        (
            "#5P#2603F……我就直截了当地说好了。\x02\x03",

            "#2601F艾莉……\x01",
            "要不要从警察局辞职，然后回来工作？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0112
    ChrTalk(
        0x102,
        "#12P#0105F！？\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        "#6P#0011F（什、什么……！？）\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        (
            "#12P#0301F（喂喂……\x01",
            "  怎么回事，这事态发展也太唐突了吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#12P#0205F（看来似乎也不是……\x01",
            "  与恋爱有关。）\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x1C,
        (
            "#5P#2603F我知道你会选择当警察，\x01",
            "也是有自己的想法的。\x02\x03",

            "#2601F但是，看看你那疲惫的面孔……\x01",
            "像孩子般迷茫的目光。\x02\x03",

            "这真的是……\x01",
            "你该走的道路吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        "#12P#0108F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x1C,
        (
            "#5P#2603F……我也明白，你对\x01",
            "目前的政治状况感到绝望。\x02\x03",

            "而你之所以想加入警察队伍，\x01",
            "恐怕也与这一点有一定关系吧。\x02\x03",

            "#2601F可是，艾莉……\x01",
            "我希望你能稍微体谅一下\x01",
            "市长的辛苦与心情。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        "#12P#0105F哎……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x1C,
        (
            "#5P#2601F由于下个月将要举办纪念庆典……\x01",
            "市长现在已经忙到焦头烂额了。\x02\x03",

            "纪念庆典之后，又必须围绕财政预算\x01",
            "与帝国派和共和国派双方\x01",
            "进行周旋……\x02\x03",

            "#2603F还有半年之后的市长选举……\x02\x03",

            "虽然市长已经决定要从政界引退了，\x01",
            "但由于没有发现可以放心托付的接班人，\x01",
            "所以似乎还在对引退一事相当犹豫。\x02\x03",

            "#2600F要是有你在身边的话，\x01",
            "市长肯定会比现在感到安心许多。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x102,
        "#12P#0106F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1C,
        (
            "#5P#2606F……抱歉，\x01",
            "似乎说了很多僭越之言。\x02\x03",

            "可是，无论如何，我也无法做到\x01",
            "视而不见。\x02\x03",

            "#2600F身为一直尊敬着市长的人……\x01",
            "身为看着你从小长大的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        "#12P#0108F……阿奈斯特先生……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x1C,
        (
            "#5P#2604F当然，你的道路\x01",
            "最终还是要由你自己来决定。可是……\x02\x03",

            "#2600F希望你能再次考虑一下，\x01",
            "自己如今的选择真的是正确的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        (
            "#12P#0108F#30W……………………………………\x02\x03",

            "#0106F#40W……请容我再稍微考虑一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x1F4)
    Sleep(300)

    #C0126
    ChrTalk(
        0x102,
        (
            "#5P#0102F各位，对不起。\x02\x03",

            "#0103F……我稍微有点累了，\x01",
            "先回自己的房间休息一下。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6886():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6886)
    Sleep(50)
    TurnDirection(0x103, 0x102, 300)

    #C0127
    ChrTalk(
        0x101,
        "#6P#0005F啊……好的。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)

    def lambda_68BF():

        label("loc_68BF")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_68BF")

    QueueWorkItem2(0x1C, 2, lambda_68BF)

    def lambda_68D1():
        OP_95(0xFE, -28600, -8200, -23000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68D1)
    WaitChrThread(0x102, 1)

    def lambda_68EF():
        OP_95(0xFE, -28600, -8200, -21800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68EF)
    Sleep(300)

    def lambda_690C():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_690C)
    WaitChrThread(0x102, 1)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_6938():
        OP_95(0xFE, -28600, -8200, -20000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6938)
    Sleep(300)

    def lambda_6955():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6955)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x102, 1)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    EndChrThread(0x1C, 0x2)
    Sleep(500)
    OP_93(0x1C, 0x5A, 0x1F4)
    Sleep(300)

    #C0128
    ChrTalk(
        0x1C,
        (
            "#5P#2603F──你们几位……\x01",
            "突然说这些，实在很抱歉。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_69D2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_69D2)
    Sleep(150)

    def lambda_69E2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_69E2)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x1F4)

    #C0129
    ChrTalk(
        0x101,
        (
            "#6P#0006F……不，大家毕竟\x01",
            "似乎也都各有苦衷。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#12P#0301F不过，不要再说\x01",
            "那种让大小姐难受的话了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#12P#0203F……是啊。\x02\x03",

            "#0211F您说出那些话，好像是想把艾莉前辈\x01",
            "从我们的身边夺走一样呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x1C,
        (
            "#5P#2604F哈哈，其实我的本意也\x01",
            "并非如此……\x02\x03",

            "#2600F只是……她曾经一直都想成为\x01",
            "一名政治家，你们知道吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0x101,
        "#6P#0005F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        "#12P#0305F喂喂，还有那种事吗！？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x103,
        (
            "#12P#0205F确实，她对政治和经济方面\x01",
            "都有着非常详细的了解……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x1C,
        (
            "#5P#2600F嗯，她当时是作为市长的后继者，\x01",
            "一直都立志步入政治之道，\x01",
            "所以学习了很多这方面的知识。\x02\x03",

            "#2603F也正因如此，她才会去各国留学，\x01",
            "以加深修养，以及培养国际化的\x01",
            "政治嗅觉……\x02\x03",

            "#2601F……可是，自从去年回国之后，\x01",
            "她却突然改变主意要当警察了。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#6P#0001F原来是这样的吗……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        "#12P#0206F……之前都不知道呢。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#12P#0306F嗯，虽然很奇怪这种出身名门的大小姐\x01",
            "为什么会愿意当警察……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x1C,
        (
            "#5P#2603F可以的话，在她的结论得出之前，\x01",
            "希望各位能在一旁默默地守护她。\x02\x03",

            "#2601F就算她坚持到了现在……\x01",
            "但像那样怀抱迷惘之心，\x01",
            "应该是无法走到底的吧。\x02",
        )
    )

    CloseMessageWindow()
    Sound(856, 0, 100, 0)
    Sleep(1500)
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0141
    ChrTalk(
        0x1C,
        (
            "#5P#2605F都已经这么晚了吗……\x02\x03",

            "#2600F实在很抱歉，打扰你们了，\x01",
            "我这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#6P#0000F啊，好的。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-26080, -6900, -25260, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(-23700, -7100, -24900, 6000)

    def lambda_6EE9():

        label("loc_6EE9")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6EE9")

    QueueWorkItem2(0x101, 2, lambda_6EE9)

    def lambda_6EFB():

        label("loc_6EFB")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6EFB")

    QueueWorkItem2(0x103, 2, lambda_6EFB)

    def lambda_6F0D():

        label("loc_6F0D")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6F0D")

    QueueWorkItem2(0x104, 2, lambda_6F0D)

    def lambda_6F1F():
        OP_95(0xFE, -27600, -8200, -23500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6F1F)
    WaitChrThread(0x1C, 1)

    def lambda_6F3D():
        OP_95(0xFE, -20600, -8200, -23500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6F3D)
    WaitChrThread(0x1C, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    def lambda_6F67():
        OP_95(0xFE, -13800, -4200, -16600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6F67)
    WaitChrThread(0x1C, 1)
    OP_6F(0x1)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    OP_68(-26080, -6900, -25260, 1500)
    SetCameraDistance(15000, 1500)
    OP_6F(0x1)

    #C0143
    ChrTalk(
        0x101,
        "#6P#0006F……呼。\x02",
    )

    CloseMessageWindow()

    def lambda_6FCC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6FCC)
    Sleep(50)

    def lambda_6FDC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6FDC)
    Sleep(300)

    #C0144
    ChrTalk(
        0x103,
        (
            "#0206F#11P总觉得今天……\x01",
            "令人头疼的事也太多了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        (
            "#5P#0306F是啊……沉重的事情\x01",
            "真是一件接着一件。\x02\x03",

            "#0301F怎么说呢，精神极度疲劳啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#6P#0003F……是啊。\x02\x03",

            "#0000F向科长报告之后，\x01",
            "我们也早点回去休息吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetScenarioFlags(0x5D, 0)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_5CC2 end

    def Function_30_70E5(): pass

    label("Function_30_70E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02707.itc", 0x1E)
    LoadChrToIndex("chr/ch28100.itc", 0x1F)
    LoadChrToIndex("chr/ch21200.itc", 0x20)
    LoadChrToIndex("chr/ch21400.itc", 0x21)
    LoadChrToIndex("chr/ch20000.itc", 0x22)
    LoadChrToIndex("chr/ch23600.itc", 0x23)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -29000, -8150, -24000, 180)
    BeginChrThread(0x1D, 3, 0, 0)
    OP_52(0x1D, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1D, 0x1)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xB4, 0xD7, 0xE6, 0xF, 0x82, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 15000, 0, -3000, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, -15000, 0, -6300, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -6800, 0, 4000, 270)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -8300, 0, 2500, 90)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -19300, 0, 19400, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, 7000, 0, 12000, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_737B():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_737B)

    def lambda_7395():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7395)

    def lambda_73AF():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_73AF)

    def lambda_73CA():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_73CA)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)
    Sleep(500)
    Sound(458, 0, 100, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x23, 0x1)
    OP_52(0x1D, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1D, 0x1)
    SetScenarioFlags(0x5D, 1)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_70E5 end

    def Function_31_749A(): pass

    label("Function_31_749A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50109.itc", 0x1E)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x101, 1000, 0, -16800, 90)
    SetChrPos(0x102, 1000, 0, -15600, 90)
    SetChrPos(0x103, -200, 0, -16800, 90)
    SetChrPos(0x104, -200, 0, -15600, 90)
    SetChrPos(0x109, 3200, 0, -16200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_78(0xB, 0x18)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    ClearMapObjFlags(0xB, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 6000, 0, -16200, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_74(0xB, 0x1E)
    OP_70(0xB, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, 0, 0, -5000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -4500, 0, 11500, 270)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -5500, 0, 13000, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    def lambda_7703():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7703)

    def lambda_771E():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_771E)

    def lambda_7738():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7738)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 28)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(2700, 900, -14200, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_68(2700, 900, -16200, 3000)
    OP_0D()
    OP_6F(0x79)

    #C0147
    ChrTalk(
        0x109,
        (
            "#11P#0500F各位，辛苦了。\x02\x03",

            "#0506F本来我也很想协助\x01",
            "大家的，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        (
            "#0102F#6P哪里，能协助我们探索那座塔\x01",
            "就已经足够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        "#0300F#6P是啊是啊，真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#6P#0204F是啊……\x01",
            "而且还把我们送到了这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#6P#0002F上士，真是谢谢了。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x109,
        (
            "#11P#0509F呵呵，没什么。\x02\x03",

            "#0501F如果再有什么情况，请不用客气，\x01",
            "随时和唐古拉姆门这边联络哦。\x02\x03",

            "今天的事情，\x01",
            "我会向副司令报告的。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#6P#0000F好的……\x01",
            "那到时就万事拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        "#0300F#6P那么，下次再见啦。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x109,
        "#11P#0502F好的……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Sleep(150)
    Sound(1483, 255, 90, 0)    #voice#Noel
    Sleep(1800)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_92(0x109, 0xE74, 0xFFFFBEC4, 0x1F4)

    def lambda_79D4():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_79D4)
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0x5A, 0x1F4)
    OP_71(0xB, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0xB)
    SetChrFlags(0x109, 0x4)

    def lambda_7A13():
        OP_96(0xFE, 0x125C, 0x1F4, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7A13)

    def lambda_7A2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7A2D)
    WaitChrThread(0x109, 1)
    ClearChrFlags(0x109, 0x4)
    OP_71(0xB, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0xB)
    Fade(500)
    OP_68(6000, 1000, -16200, 0)
    MoveCamera(25, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    Sound(470, 0, 100, 0)
    OP_71(0xB, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0xB)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_68(12000, 1000, -4400, 4000)
    MoveCamera(60, 11, 0, 4000)
    SetCameraDistance(19500, 4000)

    def lambda_7AD5():
        OP_96(0xFE, 0x1770, 0x0, 0xFFFFDC10, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7AD5)
    Sound(486, 0, 100, 0)
    Sleep(1500)

    def lambda_7AF8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7AF8)

    def lambda_7B05():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7B05)
    Sleep(300)

    def lambda_7B15():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7B15)

    def lambda_7B22():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7B22)
    WaitChrThread(0x18, 1)
    Sound(471, 0, 100, 0)

    def lambda_7B39():
        OP_9E(0xFE, 0x2EE0, 0xFFFFDC10, 0x15F90, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7B39)
    WaitChrThread(0x18, 1)

    def lambda_7B58():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7B58)
    Sleep(3000)
    OP_6F(0x79)
    Fade(500)
    OP_68(400, 1000, -16200, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    EndChrThread(0x18, 0x1)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8000)
    ClearMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xB, 0x4)
    OP_0D()

    def lambda_7BC5():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7BC5)
    Sleep(150)

    def lambda_7BD5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7BD5)
    Sleep(50)

    def lambda_7BE5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7BE5)
    Sleep(50)

    def lambda_7BF5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7BF5)
    WaitChrThread(0x104, 2)

    #C0156
    ChrTalk(
        0x101,
        (
            "#0003F#11P那么……\x02\x03",

            "#0001F首先是对本周末举行的\x01",
            "预演进行警戒啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        (
            "#5P#0103F总之先回到支援科，\x01",
            "讨论一下具体的行动安排吧。\x02\x03",

            "#0100F而且还要和彩虹剧团进行联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x103,
        (
            "#6P#0203F……搜查一科的动向\x01",
            "也有必要掌握啊。\x02\x03",

            "#0202F我想到时应该可以委托科长\x01",
            "来帮忙探查……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        (
            "#0302F#5P算了，反正肯定是\x01",
            "有得忙了。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x23, 0x1)
    StopBGM(0x1388)
    WaitBGM()
    ReplaceBGM("ed7100", "ed7000")
    SetChrName("")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后──罗伊德一行\x01",
            "与彩虹剧团的相关人员进行联络后，\x01",
            "讨论了预演时警戒工作的行动安排。\x02\x03",

            "最后的结果，是罗伊德和艾莉\x01",
            "当天在剧场内警戒……\x02\x03",

            "兰迪和缇欧则在\x01",
            "剧场外待命。\x02\x03",

            "到了预演当日──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_BA(0x8)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 0)
    NewScene("c040B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_749A end

    def Function_32_7E5E(): pass

    label("Function_32_7E5E")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 800, 4000, 0)
    MoveCamera(18, 22, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(28000, 0)
    Sound(803, 2, 0, 0)
    BeginChrThread(0x23, 1, 0, 55)
    SetChrPos(0x101, 2600, 0, -16600, 0)
    SetChrPos(0xEF, 3700, 0, -16800, 0)
    SetChrPos(0x153, 2900, 0, -14300, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_78(0x9, 0x12)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0x9, 0x4)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x4)
    OP_49()
    SetChrPos(0x12, 16000, 0, -6000, 270)
    OP_D3(0x12, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    MoveCamera(42, 22, 0, 9000)
    SetCameraDistance(33000, 9000)
    OP_6F(0x40)
    OP_6F(0x10)
    OP_0D()
    Fade(500)
    OP_68(3400, 800, -10300, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_8006():
        OP_95(0xFE, 2900, 0, -9300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_8006)
    Sleep(100)

    def lambda_8023():
        OP_95(0xFE, 2600, 0, -11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8023)
    Sleep(50)

    def lambda_8040():
        OP_95(0xFE, 3700, 0, -11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8040)
    WaitChrThread(0x153, 1)
    OP_93(0x153, 0x50, 0x2BC)
    Sleep(750)
    OP_93(0x153, 0x10E, 0x2BC)
    Sleep(500)
    EndChrThread(0x23, 0x1)

    #C0161
    ChrTalk(
        0x153,
        (
            "#1109F#11P哇～！\x01",
            "人山人海啊～！\x02\x03",

            "#1110F这么多人全都是\x01",
            "罗伊德的朋友吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0162
    ChrTalk(
        0x101,
        (
            "#12P#0012F不、不是啦……\x01",
            "那再怎么说也是不可能的。\x02\x03",

            "#0000F不过，和纪念庆典的时候相比，\x01",
            "这种人流已经算少了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_81A6")

    #C0163
    ChrTalk(
        0x102,
        (
            "#12P#0108F琪雅不是克洛斯贝尔\x01",
            "出身的吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8227")

    label("loc_81A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_81E5")

    #C0164
    ChrTalk(
        0x103,
        (
            "#12P#0208F琪雅不是克洛斯贝尔\x01",
            "出身的吧……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8227")

    label("loc_81E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_8227")

    #C0165
    ChrTalk(
        0x104,
        (
            "#12P#0308F也就是说，阿琪不是克洛斯贝尔\x01",
            "出身的啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8227")

    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x153, 0x50, 0x1F4)
    Sound(2032, 255, 100, 0)    #voice#KeA
    Sleep(800)
    Fade(500)
    OP_68(9000, 1200, -6000, 0)
    MoveCamera(75, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    ClearMapObjFlags(0x9, 0x4)

    def lambda_828A():

        label("loc_828A")

        TurnDirection(0xFE, 0x12, 100)
        Yield()
        Jump("loc_828A")

    QueueWorkItem2(0x153, 2, lambda_828A)
    OP_68(-2000, 1200, -6000, 4000)
    MoveCamera(45, 20, 0, 4000)
    SetCameraDistance(16000, 4000)

    def lambda_82C1():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_82C1)
    Sound(458, 0, 100, 0)
    Sleep(2000)
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(2033, 255, 100, 0)    #voice#KeA
    WaitChrThread(0x12, 1)
    EndChrThread(0x153, 0x2)
    ClearMapObjFlags(0x9, 0x1000)
    ClearChrFlags(0x12, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    BeginChrThread(0x23, 1, 0, 56)
    Fade(500)
    OP_68(3400, 800, -10300, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    SetChrPos(0x12, -8010, 0, 16230, 225)
    OP_D3(0x12, 0x0, 0x3BD08, 0x0, 0x0)
    OP_70(0x9, 0x0)
    OP_63(0x153, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_9C(0x153, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0x153, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)

    #C0166
    ChrTalk(
        0x153,
        (
            "#1107F#11P刚才有一个好大的铁箱子\x01",
            "轰隆隆隆～地跑过去了啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#12P#0014F哈哈，那个是车哦。\x02\x03",

            "#0002F你感觉自己是初次见到那个吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0xB4, 0x1F4)

    #C0168
    ChrTalk(
        0x153,
        (
            "#1109F#5P嗯，大概是第一次～！\x02\x03",

            "#1100F嘿嘿，是吗！\x01",
            "那个东西叫做车呀～！\x02\x03",

            "#1110F那个那个，罗伊德，\x01",
            "你们没有车吗～！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0169
    ChrTalk(
        0x101,
        "#12P#0012F嗯～很遗憾啊……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x153,
        (
            "#1100F#5P嗯～这样啊。\x02\x03",

            "我还在想，要是大家一起坐的话，\x01",
            "应该会很有意思呢～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_85E7")

    #C0171
    ChrTalk(
        0x102,
        (
            "#12P#0106F嗯～突然有点羡慕起\x01",
            "搜查一科了……\x02\x03",

            "#0101F不过，这么看来，琪雅确实\x01",
            "不是克洛斯贝尔人吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86CA")

    label("loc_85E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_8659")

    #C0172
    ChrTalk(
        0x103,
        (
            "#12P#0206F总觉得有些羡慕起\x01",
            "搜查一科了……\x02\x03",

            "#0201F不过，这么看来，琪雅果然\x01",
            "不是克洛斯贝尔人吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86CA")

    label("loc_8659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_86CA")

    #C0173
    ChrTalk(
        0x104,
        (
            "#12P#0306F真是的，都有些羡慕\x01",
            "起搜查一科了……\x02\x03",

            "#0301F不过，这么看来，阿琪果然\x01",
            "不是克洛斯贝尔人啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86CA")


    #C0174
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯，如果曾住在这里，\x01",
            "应该已经对车子司空见惯了吧。\x02\x03",

            "#0001F（可是，琪雅好像却知道\x01",
            "  这是可以乘坐的交通工具……）\x02\x03",

            "（……这究竟是怎么回事呢？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0175
    ChrTalk(
        0x153,
        (
            "#1100F#5P怎么了，罗伊德？\x02\x03",

            "不是要去见什么\x01",
            "游击士的吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        "#12P#0000F是啊，那就出发吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_8808")

    #C0177
    ChrTalk(
        0x102,
        "#12P#0100F去东街吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8857")

    label("loc_8808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_8830")

    #C0178
    ChrTalk(
        0x103,
        "#12P#0202F去东街吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8857")

    label("loc_8830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_8857")

    #C0179
    ChrTalk(
        0x104,
        "#12P#0300F向东街出发吧。\x02",
    )

    CloseMessageWindow()

    label("loc_8857")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 3400, 0, -10300, 0)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xA7, 7)
    OP_C7(0x1, 0x1000)
    EndChrThread(0x23, 0x1)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_32_7E5E end

    def Function_33_88D0(): pass

    label("Function_33_88D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x101, -24800, -8200, -23800, 270)
    SetChrPos(0x102, -24000, -8200, -24600, 270)
    SetChrPos(0x103, -22400, -8200, -23800, 270)
    SetChrPos(0x104, -21600, -8200, -24600, 270)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, 9000, 0, 5000, 180)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -14500, 0, -500, 90)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -15500, 0, 1000, 90)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    Sleep(1000)
    SetChrName("")

    #A0180
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后过了三周──\x02\x03",

            "琪雅的记忆完全没有恢复的迹象，\x01",
            "而游击士协会的情报网\x01",
            "最后也没有什么发现。\x02\x03",

            "创立纪念庆典结束，\x01",
            "距离市长选举还有数个月，\x01",
            "相对平静的生活一天天过去……\x02\x03",

            "罗伊德等人已经完全习惯了\x01",
            "与琪雅一同生活，\x01",
            "同时也重新开始处理日常公务。\x02\x03",

            "而琪雅似乎也理解了\x01",
            "罗伊德等人需要工作，\x01",
            "不再任性，而是乖乖留下来看家。\x02\x03",

            "之后──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7201", 0)
    ReplaceBGM("ed7100", "ed7201")

    def lambda_8BDF():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8BDF)

    def lambda_8BFA():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8BFA)

    def lambda_8C14():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_8C14)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 38)
    FadeToBright(2000, 0)
    Sleep(4750)
    BeginChrThread(0x101, 3, 0, 34)
    Sleep(150)
    BeginChrThread(0x102, 3, 0, 35)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 36)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 37)
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    WaitChrThread(0x23, 1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x5D, 4)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_88D0 end

    def Function_34_8D0B(): pass

    label("Function_34_8D0B")


    def lambda_8D10():
        OP_95(0xFE, -28400, -8200, -23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D10)
    WaitChrThread(0x101, 1)

    def lambda_8D2E():
        OP_95(0xFE, -28400, -8200, -22300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D2E)
    WaitChrThread(0x101, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_8D67():
        OP_95(0xFE, -28400, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D67)
    Sleep(500)

    def lambda_8D84():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8D84)
    WaitChrThread(0x101, 1)
    Return()

    # Function_34_8D0B end

    def Function_35_8D95(): pass

    label("Function_35_8D95")


    def lambda_8D9A():
        OP_95(0xFE, -28800, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D9A)
    WaitChrThread(0x102, 1)

    def lambda_8DB8():
        OP_95(0xFE, -28800, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8DB8)
    Sleep(1500)

    def lambda_8DD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8DD5)
    WaitChrThread(0x102, 1)
    Return()

    # Function_35_8D95 end

    def Function_36_8DE6(): pass

    label("Function_36_8DE6")


    def lambda_8DEB():
        OP_95(0xFE, -28400, -8200, -23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8DEB)
    WaitChrThread(0x103, 1)

    def lambda_8E09():
        OP_95(0xFE, -28400, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8E09)
    Sleep(1500)

    def lambda_8E26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8E26)
    WaitChrThread(0x103, 1)
    Return()

    # Function_36_8DE6 end

    def Function_37_8E37(): pass

    label("Function_37_8E37")


    def lambda_8E3C():
        OP_95(0xFE, -28800, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8E3C)
    WaitChrThread(0x104, 1)

    def lambda_8E5A():
        OP_95(0xFE, -28800, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8E5A)
    Sleep(1500)

    def lambda_8E77():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8E77)
    WaitChrThread(0x104, 1)
    Return()

    # Function_37_8E37 end

    def Function_38_8E88(): pass

    label("Function_38_8E88")

    Sound(803, 2, 100, 0)
    Sleep(7000)
    OP_25(0x323, 0x5A)
    Sleep(200)
    OP_25(0x323, 0x50)
    Sleep(200)
    OP_25(0x323, 0x46)
    Sleep(200)
    OP_25(0x323, 0x3C)
    Sleep(200)
    OP_25(0x323, 0x32)
    Sleep(200)
    OP_25(0x323, 0x28)
    Sleep(200)
    OP_25(0x323, 0x1E)
    Sleep(200)
    OP_25(0x323, 0x14)
    Sleep(200)
    OP_25(0x323, 0xA)
    Sleep(200)
    OP_24(0x323)
    Return()

    # Function_38_8E88 end

    def Function_39_8ED4(): pass

    label("Function_39_8ED4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-28700, -7200, -21900, 0)
    MoveCamera(50, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -28700, -8200, -19500, 180)
    SetChrPos(0x102, -28700, -8200, -19500, 180)
    SetChrPos(0x103, -28700, -8200, -19500, 180)
    SetChrPos(0x104, -28700, -8200, -19500, 180)
    SetChrPos(0x109, -28700, -8200, -19500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(-28700, -7200, -24900, 6000)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 42)
    Sleep(1500)

    def lambda_9005():
        OP_95(0xFE, -28700, -8200, -23500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9005)

    def lambda_901F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_901F)
    Sleep(1500)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    #C0181
    ChrTalk(
        0x109,
        (
            "#5P#0500F──警备队的车辆就\x01",
            "停在城市的北出口。\x02\x03",

            "我想，只要是在自治州的范围之内，\x01",
            "可以送大家去任何地方。\x01",
            "如果有什么要求，请不要客气，随时告诉我。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_91C0")

    #C0182
    ChrTalk(
        0x101,
        (
            "#12P#0004F好的，明白了。\x02\x03",

            "#0000F所说的遗迹，应该就是\x01",
            "位于山道隧道中部的\x01",
            "岔路尽头的那个遗迹吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#6P#0203F以前曾经去过那个遗迹的\x01",
            "入口附近呢。\x02\x03",

            "#0200F但当时被警备队的\x01",
            "路障封锁了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92FA")

    label("loc_91C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 7)), scpexpr(EXPR_END)), "loc_925C")

    #C0184
    ChrTalk(
        0x101,
        (
            "#12P#0004F好的，明白了。\x02\x03",

            "#0000F所说的遗迹，应该就是\x01",
            "位于山道隧道中部的\x01",
            "岔路尽头的那个遗迹吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        (
            "#6P#0202F和矿山镇不是同一个\x01",
            "方向呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92FA")

    label("loc_925C")


    #C0186
    ChrTalk(
        0x101,
        (
            "#12P#0004F好的，明白了。\x02\x03",

            "#0000F所说的遗迹，应该就是\x01",
            "位于山道隧道中部的\x01",
            "岔路尽头的那个遗迹吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x103,
        (
            "#6P#0202F确实，在隧道的中段部分\x01",
            "有条很狭窄的岔路呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92FA")


    #C0188
    ChrTalk(
        0x109,
        (
            "#5P#0500F嗯，那边的道路比较险峻，\x01",
            "所以从隧道的中段开始\x01",
            "就要徒步行进了。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x104,
        (
            "#11P#0309F那么，把手头的事情都办完之后，\x01",
            "就向山道的隧道进发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        (
            "#12P#0108F（……呼，\x01",
            "　幽灵出没的遗迹吗……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -28700, -8200, -25000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC0, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_29(0x48, 0x1, 0x9)
    OP_29(0x49, 0x4, 0x2)
    OP_29(0x49, 0x1, 0x0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_39_8ED4 end

    def Function_40_9423(): pass

    label("Function_40_9423")


    def lambda_9428():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9428)

    def lambda_9442():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9442)
    WaitChrThread(0xFE, 1)

    def lambda_9457():
        OP_95(0xFE, -28100, -8200, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9457)
    WaitChrThread(0x101, 1)

    def lambda_9475():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9475)
    WaitChrThread(0x101, 2)
    Return()

    # Function_40_9423 end

    def Function_41_9488(): pass

    label("Function_41_9488")


    def lambda_948D():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_948D)

    def lambda_94A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_94A7)
    WaitChrThread(0xFE, 1)

    def lambda_94BC():
        OP_95(0xFE, -29400, -8200, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94BC)
    WaitChrThread(0x102, 1)

    def lambda_94DA():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_94DA)
    WaitChrThread(0x102, 2)
    Return()

    # Function_41_9488 end

    def Function_42_94ED(): pass

    label("Function_42_94ED")


    def lambda_94F2():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_94F2)

    def lambda_950C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_950C)
    WaitChrThread(0xFE, 1)

    def lambda_9521():
        OP_95(0xFE, -30400, -8200, -25300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9521)
    WaitChrThread(0x103, 1)

    def lambda_953F():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_953F)
    WaitChrThread(0x103, 2)
    Return()

    # Function_42_94ED end

    def Function_43_9552(): pass

    label("Function_43_9552")


    def lambda_9557():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9557)

    def lambda_9571():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9571)
    WaitChrThread(0xFE, 1)

    def lambda_9586():
        OP_95(0xFE, -27000, -8200, -25300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9586)
    WaitChrThread(0x104, 1)

    def lambda_95A4():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_95A4)
    WaitChrThread(0x104, 2)
    Return()

    # Function_43_9552 end

    def Function_44_95B7(): pass

    label("Function_44_95B7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50109.itc", 0x1E)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x101, 1000, 0, -16800, 90)
    SetChrPos(0x102, 1000, 0, -15600, 90)
    SetChrPos(0x103, -200, 0, -16800, 90)
    SetChrPos(0x104, -200, 0, -15600, 90)
    SetChrPos(0x109, 3200, 0, -16200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_78(0xB, 0x18)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    ClearMapObjFlags(0xB, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 6000, 0, -16200, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_74(0xB, 0x1E)
    OP_70(0xB, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, 0, 0, -5000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -4500, 0, 11500, 270)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -5500, 0, 13000, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    def lambda_9802():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_9802)

    def lambda_981D():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_981D)

    def lambda_9837():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9837)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 28)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(2700, 900, -14200, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_68(2700, 900, -16200, 3000)
    OP_0D()
    OP_6F(0x79)

    #C0191
    ChrTalk(
        0x109,
        (
            "#11P#0509F──今天真是\x01",
            "非常感谢！\x02\x03",

            "#0502F这份恩情，我一定会\x01",
            "尽早回报的！\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        "#6P#0002F哈哈，太夸张啦。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x104,
        (
            "#0304F#6P呵呵，我们也经历了一次\x01",
            "很有趣的体验啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x102,
        (
            "#0106F#6P关于那个遗迹──\x01",
            "『僧院』……\x02\x03",

            "#0108F还是去和克洛斯贝尔\x01",
            "大圣堂的人商谈一下\x01",
            "比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x103,
        (
            "#6P#0206F……是啊。\x02\x03",

            "如果涉及到古代遗物的话，\x01",
            "我们也就无能为力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x109,
        (
            "#11P#0503F这样啊……\x02\x03",

            "#0500F明白了，那我先去和副司令商讨\x01",
            "相关对策。\x02\x03",

            "#0505F各位……\x01",
            "接下来还要继续在市内探问情报吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#6P#0004F嗯，准备至少去『巴鲁卡』\x01",
            "调查一下。\x02\x03",

            "#0000F如果你们警备队\x01",
            "有了那方面的情报，就请与\x01",
            "我们进行联络吧，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x109,
        (
            "#11P#0500F明白了，\x01",
            "是有关矿山镇的冈兹先生对吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0199
    ChrTalk(
        0x109,
        (
            "#2P#0502F#11P那我就先告辞了。\x01",
            "各位，辛苦了！\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        "#0302F#6P噢，彼此彼此，你也是啊。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_92(0x109, 0xE74, 0xFFFFBEC4, 0x1F4)

    def lambda_9BBB():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9BBB)
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0x5A, 0x1F4)
    OP_71(0xB, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0xB)
    SetChrFlags(0x109, 0x4)

    def lambda_9BFA():
        OP_96(0xFE, 0x125C, 0x1F4, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9BFA)

    def lambda_9C14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9C14)
    WaitChrThread(0x109, 1)
    ClearChrFlags(0x109, 0x4)
    OP_71(0xB, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0xB)
    Fade(500)
    OP_68(6000, 1000, -16200, 0)
    MoveCamera(25, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    Sound(470, 0, 100, 0)
    OP_71(0xB, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0xB)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_68(12000, 1000, -4400, 4000)
    MoveCamera(60, 11, 0, 4000)
    SetCameraDistance(19500, 4000)
    Sound(486, 0, 100, 0)

    def lambda_9CC2():
        OP_96(0xFE, 0x1770, 0x0, 0xFFFFDC10, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9CC2)
    Sleep(1500)

    def lambda_9CDF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9CDF)

    def lambda_9CEC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9CEC)
    Sleep(300)

    def lambda_9CFC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9CFC)

    def lambda_9D09():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9D09)
    WaitChrThread(0x18, 1)
    Sound(471, 0, 100, 0)

    def lambda_9D20():
        OP_9E(0xFE, 0x2EE0, 0xFFFFDC10, 0x15F90, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9D20)
    WaitChrThread(0x18, 1)

    def lambda_9D3F():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9D3F)
    Sleep(3000)
    OP_6F(0x79)
    Fade(500)
    OP_68(400, 1000, -16200, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    EndChrThread(0x18, 0x1)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8000)
    ClearMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xB, 0x4)
    OP_0D()

    def lambda_9DAC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9DAC)
    Sleep(150)

    def lambda_9DBC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9DBC)
    Sleep(50)

    def lambda_9DCC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9DCC)
    Sleep(50)

    def lambda_9DDC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9DDC)
    WaitChrThread(0x104, 2)

    #C0201
    ChrTalk(
        0x101,
        (
            "#0000F那么……\x01",
            "已经没有多少时间了，\x01",
            "现在就直接去『巴鲁卡』吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102)

    #C0202
    ChrTalk(
        0x102,
        (
            "#5P#0100F嗯，必须去收集那位叫冈兹的\x01",
            "矿工的情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x104,
        (
            "#0309F那咱们就赶快去\x01",
            "欢乐街那边吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_BA(0x8)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_29(0x4A, 0x1, 0x3)
    EndChrThread(0x23, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_95B7 end

    def Function_45_9F01(): pass

    label("Function_45_9F01")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch21200.itc", 0x1F)
    LoadChrToIndex("chr/ch21400.itc", 0x20)
    LoadChrToIndex("chr/ch20000.itc", 0x21)
    LoadChrToIndex("chr/ch23600.itc", 0x22)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xB4, 0xD7, 0xE6, 0xF, 0x82, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 15000, 0, -3000, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, -15000, 0, -6300, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -6800, 0, 4000, 270)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -8300, 0, 2500, 90)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -19300, 0, 19400, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, 7000, 0, 12000, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_A129():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A129)

    def lambda_A143():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A143)

    def lambda_A15D():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_A15D)
    Sound(458, 0, 100, 0)

    def lambda_A17E():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A17E)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x23, 0x1)
    SetScenarioFlags(0x5D, 5)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_9F01 end

    def Function_46_A21F(): pass

    label("Function_46_A21F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch21200.itc", 0x1F)
    LoadChrToIndex("chr/ch21400.itc", 0x20)
    LoadChrToIndex("chr/ch20000.itc", 0x21)
    LoadChrToIndex("chr/ch23600.itc", 0x22)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xB4, 0xD7, 0xE6, 0xF, 0x82, 0x0)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 15000, 0, -3000, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, -15000, 0, -6300, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -6800, 0, 4000, 270)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -8300, 0, 2500, 90)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -19300, 0, 19400, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, 7000, 0, 12000, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K翌日 ８：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7001", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_A4A3():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A4A3)

    def lambda_A4BD():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A4BD)

    def lambda_A4D7():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_A4D7)

    def lambda_A4F2():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A4F2)
    Sound(458, 0, 100, 0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5D, 6)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_A21F end

    def Function_47_A595(): pass

    label("Function_47_A595")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, 0, 0, -5000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -4500, 0, 11500, 270)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -5500, 0, 13000, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K同日 １７：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7100", 0)

    def lambda_A7C0():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A7C0)

    def lambda_A7DB():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A7DB)

    def lambda_A7F5():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_A7F5)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 28)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearScenarioFlags(0x1, 5)
    EndChrThread(0x23, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5D, 7)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_A595 end

    def Function_48_A8D6(): pass

    label("Function_48_A8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A904")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)
    Jump("loc_A92D")

    label("loc_A904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A92D")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_A92D")

    Return()

    # Function_48_A8D6 end

    def Function_49_A92E(): pass

    label("Function_49_A92E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A95C")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)
    Jump("loc_A985")

    label("loc_A95C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A985")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_A985")

    Return()

    # Function_49_A92E end

    def Function_50_A986(): pass

    label("Function_50_A986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9B4")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)
    Jump("loc_A9DD")

    label("loc_A9B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9DD")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_A9DD")

    Return()

    # Function_50_A986 end

    def Function_51_A9DE(): pass

    label("Function_51_A9DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA07")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_AA07")

    Return()

    # Function_51_A9DE end

    def Function_52_AA08(): pass

    label("Function_52_AA08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA36")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)
    Jump("loc_AA5F")

    label("loc_AA36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA5F")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_AA5F")

    Return()

    # Function_52_AA08 end

    def Function_53_AA60(): pass

    label("Function_53_AA60")


    #C0206
    ChrTalk(
        0x101,
        (
            "#0005F啊……还是先去\x01",
            "导力商店看看吧。\x02\x03",

            "#0000F就是街角的那个建筑。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AACC")

    #C0207
    ChrTalk(
        0x103,
        "#0200F了解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB29")

    label("loc_AACC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAFB")

    #C0208
    ChrTalk(
        0x104,
        "#0300F了解，这就走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB29")

    label("loc_AAFB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB29")

    #C0209
    ChrTalk(
        0x102,
        "#0100F是啊，那我们就去吧。\x02",
    )

    CloseMessageWindow()

    label("loc_AB29")

    Return()

    # Function_53_AA60 end

    def Function_54_AB2A(): pass

    label("Function_54_AB2A")


    #C0210
    ChrTalk(
        0x101,
        (
            "#0000F今天已经很累了啊……\x01",
            "别绕远路了，径直回支援科吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_54_AB2A end

    def Function_55_AB68(): pass

    label("Function_55_AB68")

    OP_25(0x323, 0x0)
    Sleep(200)
    OP_25(0x323, 0xA)
    Sleep(200)
    OP_25(0x323, 0x14)
    Sleep(200)
    OP_25(0x323, 0x1E)
    Sleep(200)
    OP_25(0x323, 0x28)
    Sleep(200)
    OP_25(0x323, 0x32)
    Sleep(200)
    OP_25(0x323, 0x3C)
    Sleep(200)
    OP_25(0x323, 0x46)
    Sleep(200)
    OP_25(0x323, 0x50)
    Sleep(200)
    OP_25(0x323, 0x5A)
    Sleep(200)
    OP_25(0x323, 0x64)
    Return()

    # Function_55_AB68 end

    def Function_56_ABB3(): pass

    label("Function_56_ABB3")

    OP_25(0x323, 0x64)
    Sleep(100)
    OP_25(0x323, 0x5A)
    Sleep(100)
    OP_25(0x323, 0x50)
    Sleep(100)
    OP_25(0x323, 0x46)
    Sleep(100)
    OP_25(0x323, 0x3C)
    Sleep(100)
    OP_25(0x323, 0x32)
    Sleep(100)
    OP_25(0x323, 0x28)
    Sleep(100)
    OP_25(0x323, 0x1E)
    Sleep(100)
    OP_25(0x323, 0x14)
    Sleep(100)
    OP_25(0x323, 0xA)
    Sleep(100)
    OP_25(0x323, 0x0)
    OP_24(0x323)
    Return()

    # Function_56_ABB3 end

    SaveToFile()

Try(main)
