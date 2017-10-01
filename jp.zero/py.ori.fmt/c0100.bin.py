from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ジーナ",                 # 1
        "コンテ老人",             # 2
        "アベル",                 # 3
        "ミミ",                   # 4
        "プルーナ",               # 5
        "リナリー",               # 6
        "ハース",                 # 7
        "アロナ",                 # 8
        "ケイト巡査",             # 9
        "レインズ",               # 10
        "車１",                   # 11
        "コッペ",                 # 12
        "ツァイト",               # 13
        "キーア",                 # 14
        "老人",                   # 15
        "老婦人",                 # 16
        "車１",                   # 17
        "車２",                   # 18
        "ハロルド",               # 19
        "セルゲイ課長",           # 20
        "秘書アーネスト",         # 21
        "ツァイト",               # 22
        "イベント用ＮＰＣ",       # 23
        "イベント用ＮＰＣ",       # 24
        "イベント用ＮＰＣ",       # 25
        "イベント用ＮＰＣ",       # 26
        "イベント用ＮＰＣ",       # 27
        "SE制御",                 # 28
        " ",                      # 29
        "中央広場",               # 30
        "西通り",                 # 31
        "行政区",                 # 32
        "住宅街",                 # 33
        "歓楽街",                 # 34
        "東通り",                 # 35
        "旧市街",                 # 36
        "港湾区",                 # 37
        "ＩＢＣ",                 # 38
        "駅前通り",               # 39
        "裏通り",                 # 40
        "ウルスラ間道",           # 41
        "東クロスベル街道",       # 42
        "西クロスベル街道",       # 43
        "マインツ山道",           # 44
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
        "Function_8_19A3",         # 08, 8
        "Function_9_1AE9",         # 09, 9
        "Function_10_1B4F",        # 0A, 10
        "Function_11_20FD",        # 0B, 11
        "Function_12_21EC",        # 0C, 12
        "Function_13_21FA",        # 0D, 13
        "Function_14_3259",        # 0E, 14
        "Function_15_32CD",        # 0F, 15
        "Function_16_333F",        # 10, 16
        "Function_17_33CA",        # 11, 17
        "Function_18_33D4",        # 12, 18
        "Function_19_370C",        # 13, 19
        "Function_20_3758",        # 14, 20
        "Function_21_4A1C",        # 15, 21
        "Function_22_4A63",        # 16, 22
        "Function_23_4AB1",        # 17, 23
        "Function_24_5AB2",        # 18, 24
        "Function_25_5B6C",        # 19, 25
        "Function_26_5E05",        # 1A, 26
        "Function_27_5E8F",        # 1B, 27
        "Function_28_5EE0",        # 1C, 28
        "Function_29_5F2C",        # 1D, 29
        "Function_30_7459",        # 1E, 30
        "Function_31_780E",        # 1F, 31
        "Function_32_82A4",        # 20, 32
        "Function_33_8DEC",        # 21, 33
        "Function_34_927F",        # 22, 34
        "Function_35_9309",        # 23, 35
        "Function_36_935A",        # 24, 36
        "Function_37_93AB",        # 25, 37
        "Function_38_93FC",        # 26, 38
        "Function_39_9448",        # 27, 39
        "Function_40_9A13",        # 28, 40
        "Function_41_9A78",        # 29, 41
        "Function_42_9ADD",        # 2A, 42
        "Function_43_9B42",        # 2B, 43
        "Function_44_9BA7",        # 2C, 44
        "Function_45_A5AF",        # 2D, 45
        "Function_46_A8CD",        # 2E, 46
        "Function_47_AC44",        # 2F, 47
        "Function_48_AF86",        # 30, 48
        "Function_49_AFDE",        # 31, 49
        "Function_50_B036",        # 32, 50
        "Function_51_B08E",        # 33, 51
        "Function_52_B0B8",        # 34, 52
        "Function_53_B110",        # 35, 53
        "Function_54_B1FC",        # 36, 54
        "Function_55_B240",        # 37, 55
        "Function_56_B28B",        # 38, 56
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196C")
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
            "#56I地のセピス×３０\x01\x07\x02",

            "#57I水のセピス×３０\x01\x07\x02",

            "#58I火のセピス×３０\x01\x07\x02",

            "#59I風のセピス×３０\x01\x07\x02",

            "#60I時のセピス×３０\x01\x07\x02",

            "#61I空のセピス×３０\x01\x07\x02",

            "#62I幻のセピス×３０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x111, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1991")

    label("loc_196C")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1991")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1840 end

    def Function_8_19A3(): pass

    label("Function_8_19A3")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "       《クロスベルの鐘》\x01",
            "Ｓ１１８５、クロスベル自治州で\x01",
            "発掘された巨大な鐘。\x01",
            "出土した遺跡の状況から\x01",
            "中世の頃の物と考えられている。\x01",
            "複数の金属から成り、\x01",
            "打つと心地よい低音を響かせる。\x02",
        )
    )

    CloseMessageWindow()

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当時の有力者によって\x01",
            "作られたと推察されているが、\x01",
            "その用途には未だ諸説がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_19A3 end

    def Function_9_1AE9(): pass

    label("Function_9_1AE9")

    EventBegin(0x1)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハシゴがある。\x01",
            "降りますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4C")
    EventEnd(0x5)
    NewScene("m0000", 125, 0, 0)
    IdleLoop()
    Jump("loc_1B4E")

    label("loc_1B4C")

    EventEnd(0x5)

    label("loc_1B4E")

    Return()

    # Function_9_1AE9 end

    def Function_10_1B4F(): pass

    label("Function_10_1B4F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20F5")

    Menu(
        0,
        32,
        26,
        1,
        (
            "警備隊車両で移動をする\x01",      # 0
            "ここで休憩をする\x01",            # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2092")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BFD")
    MenuCmd(1, 1, "★クロスベル市・中央区")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1C17")

    label("loc_1BFD")

    MenuCmd(1, 1, "　クロスベル市・中央区")

    label("loc_1C17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C49")
    MenuCmd(1, 1, "★クロスベル市・東出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1C63")

    label("loc_1C49")

    MenuCmd(1, 1, "　クロスベル市・東出口")

    label("loc_1C63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C95")
    MenuCmd(1, 1, "★クロスベル市・西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1CAF")

    label("loc_1C95")

    MenuCmd(1, 1, "　クロスベル市・西出口")

    label("loc_1CAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE1")
    MenuCmd(1, 1, "★クロスベル市・南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1CFB")

    label("loc_1CE1")

    MenuCmd(1, 1, "　クロスベル市・南出口")

    label("loc_1CFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D2D")
    MenuCmd(1, 1, "★クロスベル市・北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1D47")

    label("loc_1D2D")

    MenuCmd(1, 1, "　クロスベル市・北出口")

    label("loc_1D47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D71")
    MenuCmd(1, 1, "★タングラム門")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1D83")

    label("loc_1D71")

    MenuCmd(1, 1, "　タングラム門")

    label("loc_1D83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DAD")
    MenuCmd(1, 1, "★ベルガード門")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1DBF")

    label("loc_1DAD")

    MenuCmd(1, 1, "　ベルガード門")

    label("loc_1DBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DED")
    MenuCmd(1, 1, "★ウルスラ医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1E03")

    label("loc_1DED")

    MenuCmd(1, 1, "　ウルスラ医科大学")

    label("loc_1E03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2D")
    MenuCmd(1, 1, "★アルモリカ村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1E3F")

    label("loc_1E2D")

    MenuCmd(1, 1, "　アルモリカ村")

    label("loc_1E3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6B")
    MenuCmd(1, 1, "★マインツ鉱山町")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1E7F")

    label("loc_1E6B")

    MenuCmd(1, 1, "　マインツ鉱山町")

    label("loc_1E7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB1")
    MenuCmd(1, 1, "★マインツ山道・隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1ECB")

    label("loc_1EB1")

    MenuCmd(1, 1, "　マインツ山道・隧道内")

    label("loc_1ECB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF1")
    MenuCmd(1, 1, "★星見の塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1EFF")

    label("loc_1EF1")

    MenuCmd(1, 1, "　星見の塔")

    label("loc_1EFF")

    MenuCmd(1, 1, "　やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2083")
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
        (0, "loc_1FD6"),
        (1, "loc_1FE4"),
        (2, "loc_1FF2"),
        (3, "loc_2000"),
        (4, "loc_200E"),
        (5, "loc_201C"),
        (6, "loc_202A"),
        (7, "loc_2038"),
        (8, "loc_2046"),
        (9, "loc_2054"),
        (10, "loc_2062"),
        (11, "loc_2070"),
        (SWITCH_DEFAULT, "loc_207E"),
    )


    label("loc_1FD6")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_1FE4")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_1FF2")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_2000")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_200E")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_201C")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_202A")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_2038")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_2046")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_2054")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_2062")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_2070")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_207E")

    label("loc_207E")

    Jump("loc_208D")

    label("loc_2083")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_208D")

    Jump("loc_20F0")

    label("loc_2092")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DD")
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
    Jump("loc_20F0")

    label("loc_20DD")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20F0")

    Jump("loc_1B69")

    label("loc_20F5")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1B4F end

    def Function_11_20FD(): pass

    label("Function_11_20FD")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21D1")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_21D7")

    label("loc_21D1")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_21D7")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_20FD end

    def Function_12_21EC(): pass

    label("Function_12_21EC")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Return()

    # Function_12_21EC end

    def Function_13_21FA(): pass

    label("Function_13_21FA")

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

    def lambda_264A():
        OP_95(0xFE, 2900, 0, -11300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_264A)
    Sleep(100)

    def lambda_2667():
        OP_95(0xFE, 2600, 0, -13600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2667)
    Sleep(50)

    def lambda_2684():
        OP_95(0xFE, 3700, 0, -13800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2684)
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
            "#0005F#5Pうわ～……\x01",
            "ずいぶん様変わりしたなぁ。\x02\x03",

            "#0012Fデパートなんか\x01",
            "完全に新しくなってるし。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    #C0007
    ChrTalk(
        0x101,
        "#0005F#5Pあれ、そっちの建物は……？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x16,
        (
            "#12P去年オープンしたばかりの\x01",
            "《オーバルストア》じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x16,
        (
            "#12P最新の導力製品から\x01",
            "導力車まで扱っておる店舗でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x16,
        (
            "#12P帝国製、共和国製、リベール製、\x01",
            "エプスタイン製、全て扱っておるぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0011
    ChrTalk(
        0x101,
        (
            "#0006F#5Pは～、大したもんだね。\x02\x03",

            "#0000Fそれに……\x01",
            "けっこう車も増えたみたいだ。\x02\x03",

            "３年前はほとんど\x01",
            "見かけなかったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x17,
        (
            "ふふ、お金持ちにしか\x01",
            "縁がないものだとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x17,
        (
            "導力バスの本数が増えたのは\x01",
            "正直、ありがたいわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x17,
        (
            "南にある病院方面なんか\x01",
            "３０分ごとに走っているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0002F#5Pへえ、それは便利になったね。\x02\x03",

            "#0004Fそうか……\x01",
            "３年でそこまで変わったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x16,
        "#12Pさてと、ここまででいいぞ。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x16,
        "#12P就職先に顔を出すんじゃろ？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0018
    ChrTalk(
        0x101,
        (
            "#0005F#5Pあ、うん……\x02\x03",

            "せっかくだから家まで\x01",
            "運ばせてもらおうと思ったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x17,
        "あらあら、ダメですよ。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x17,
        (
            "せっかくの初出勤、\x01",
            "遅刻でもしたらどうするの？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x16,
        (
            "#12Pそうそう。\x01",
            "何事も始めが肝心じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0012F#5Pはは、確かにそうだね。\x02",
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
            "#12Pしかし、戻ってきたばかりで\x01",
            "住むアテはあるのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x16,
        (
            "#12P東通りでよければ\x01",
            "下宿先を紹介できると思うが。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#0002F#5Pあ、気持ちはありがたいけど\x01",
            "寮が用意されているらしいんだ。\x02\x03",

            "送った荷物も\x01",
            "そちらに届いているはずだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x16,
        "#12Pほう、そうじゃったか。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x17,
        (
            "私たちは、東通りの外れの方で\x01",
            "暮らしているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x17,
        (
            "何か困ったことがあったら\x01",
            "いつでも頼ってらっしゃいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0009F#5Pうん、ありがとう。\x02\x03",

            "#0002F落ち着いたら\x01",
            "挨拶に伺わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x16,
        "#12Pうむ、しっかりな。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x17,
        "それじゃあ、またね。\x02",
    )

    CloseMessageWindow()
    OP_92(0x16, 0x2E18, 0xFFFFEB4C, 0x1F4)

    def lambda_2D31():
        OP_95(0xFE, 11800, 0, -5300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2D31)
    Sleep(300)

    def lambda_2D4E():

        label("loc_2D4E")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_2D4E")

    QueueWorkItem2(0x101, 2, lambda_2D4E)
    Sleep(200)
    OP_92(0x17, 0x2C24, 0xFFFFE4A8, 0x1F4)

    def lambda_2D70():
        OP_95(0xFE, 11300, 0, -7000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2D70)
    WaitChrThread(0x16, 1)

    def lambda_2D8E():
        OP_95(0xFE, 21800, 0, -5300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2D8E)
    WaitChrThread(0x17, 1)

    def lambda_2DAC():
        OP_95(0xFE, 21300, 0, -7000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2DAC)
    Sleep(1000)
    EndChrThread(0x101, 0x2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x10E, 0x1F4)

    #C0032
    ChrTalk(
        0x101,
        "#0005F#11Pあれ……\x02",
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
            "#0000Fあの雑居ビル……\x01",
            "ちゃんと残っていたんだ。\x02\x03",

            "たしかクロスベルタイムズが\x01",
            "入っていたはずだけど……\x02\x03",

            "#0012Fはは、懐かしいけど\x01",
            "この街並みじゃ浮いてるよな。\x02",
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
        "#0003F#11Pさてと……そろそろ時間だ。\x02",
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
            "ロイドは懐から\x01",
            "一枚の封書を取り出した。\x02",
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
            "ロイド・バニングス殿\x01",
            "クロスベル警察本部、\x01",
            "特務支援課への配属を命ずる。\x01",
            "指定日時に警察本部へ出頭せよ。\x01",
            "　　　　　　　　クロスベル警察・人事課\x07\x00\x02",
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
            "#0001F#11P特務支援課……\x01",
            "警察学校のカリキュラムじゃ\x01",
            "聞かなかった名前だけど。\x02\x03",

            "まだ制服も受け取ってないし、\x01",
            "どういう部署なんだろう……？\x02",
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
            "#0004F#11P──まあいい。\x01",
            "とにかく行けば分かるよな。\x02\x03",

            "さすがに警察の場所までは\x01",
            "変わってないだろうし……\x02",
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
        "#0000F#11Pよし、初出勤と行きますか！\x02",
    )

    CloseMessageWindow()

    def lambda_31E9():
        OP_95(0xFE, 9000, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31E9)
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

    # Function_13_21FA end

    def Function_14_3259(): pass

    label("Function_14_3259")

    Sleep(1000)
    Sound(461, 0, 70, 0)
    OP_71(0x9, 0x1F, 0x3C, 0x0, 0x0)
    OP_79(0x9)
    Sleep(1000)
    OP_71(0x9, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x9)

    def lambda_3288():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3288)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    WaitChrThread(0x19, 2)

    def lambda_32B3():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_32B3)
    WaitChrThread(0x19, 1)
    Return()

    # Function_14_3259 end

    def Function_15_32CD(): pass

    label("Function_15_32CD")


    def lambda_32D2():
        OP_96(0xFE, 0x2CEC, 0x0, 0x1964, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_32D2)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    WaitChrThread(0x18, 1)
    WaitChrThread(0x19, 2)
    Sound(458, 0, 100, 0)

    def lambda_3306():
        OP_9E(0xFE, 0x0, 0x1964, 0x15F90, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3306)
    WaitChrThread(0x18, 1)

    def lambda_3325():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3325)
    WaitChrThread(0x18, 1)
    Return()

    # Function_15_32CD end

    def Function_16_333F(): pass

    label("Function_16_333F")


    def lambda_3344():
        OP_95(0xFE, -21700, 100, 7500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3344)
    WaitChrThread(0x11, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x6)

    def lambda_337D():
        OP_95(0xFE, -22700, 0, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_337D)

    def lambda_3397():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3397)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x11, 2)
    Sleep(500)
    Sound(104, 0, 100, 0)
    OP_71(0x6, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x6)
    SetMapObjFlags(0x6, 0x10)
    Return()

    # Function_16_333F end

    def Function_17_33CA(): pass

    label("Function_17_33CA")

    Sleep(4000)
    Sound(457, 0, 100, 0)
    Return()

    # Function_17_33CA end

    def Function_18_33D4(): pass

    label("Function_18_33D4")

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

    def lambda_3613():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3613)

    def lambda_362D():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_362D)

    def lambda_3647():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_3647)
    Sound(458, 0, 100, 0)

    def lambda_3668():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3668)
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

    # Function_18_33D4 end

    def Function_19_370C(): pass

    label("Function_19_370C")

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

    # Function_19_370C end

    def Function_20_3758(): pass

    label("Function_20_3758")

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

    def lambda_3915():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3915)

    def lambda_392F():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_392F)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)

    def lambda_3969():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3969)
    Sleep(2000)

    def lambda_3986():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3986)
    Sleep(1000)
    Sound(456, 0, 100, 0)

    def lambda_39A9():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_39A9)
    Sleep(1000)

    def lambda_39C6():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_39C6)
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
            "#12P#0002F──ありがとうございます。\x01",
            "こんな所まで送っていただいて。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x1A,
        (
            "#3609F#5Pはは、いいんですよ。\x01",
            "それこそついでですしね。\x02\x03",

            "#3600F皆さん、どうか捜査の方、\x01",
            "頑張ってください。\x02\x03",

            "応援させていただきますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0102Fありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#12P#0202F……応援していただけるのなら\x01",
            "今後、何かあれば支援課#6Rわたしたち#の方に。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0309Fそうそう。\x01",
            "できればギルドより先にな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3CC4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CC4)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3CE6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3CE6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)

    #C0045
    ChrTalk(
        0x101,
        "#1P#0011Fちょ、２人とも！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#5P#0106Fもう……露骨すぎるわ。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0302Fはは、たまには\x01",
            "売り込みもしとかねぇとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#12P#0204F営業活動は大事です。\x02",
    )

    CloseMessageWindow()

    def lambda_3DA1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DA1)
    Sleep(50)

    def lambda_3DB1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DB1)

    #C0049
    ChrTalk(
        0x1A,
        (
            "#3609F#5Pはは、分かりました。\x02\x03",

            "#3600Fもし困ったことがあったら\x01",
            "遠慮なく相談させて頂きます。\x02",
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
            "#3605F#5Pそうだ……皆さんは\x01",
            "こんな物はお使いになりますか？\x02\x03",

            "#3600Fはは、警察の方には\x01",
            "不要かもしれませんが……\x02",
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
            "を受け取った。\x02",
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
            "#0105Fこれは……\x01",
            "市内の地図みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x1A,
        (
            "#3600F#5P先月から観光客向けに\x01",
            "取り扱っている商品なんです。\x01",
            "よろしければ皆さんも使って下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#12P#0002Fこれは……確かに市内を見回るのに\x01",
            "便利かもしれません。\x02\x03",

            "#0004Fハロルドさん、ありがとうございます。\x01",
            "活用させてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x1A,
        (
            "#3609F#5Pはは、大した物ではありませんが。\x02\x03",

            "#3600Fそれでは私はこれで。\x01",
            "皆さんもお仕事、頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_92(0x1A, 0x0, 0xFFFFEF98, 0x1F4)

    def lambda_409A():
        OP_95(0xFE, 0, 0, -4200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_409A)
    WaitChrThread(0x1A, 1)

    def lambda_40B8():
        OP_95(0xFE, 0, 0, -3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_40B8)

    def lambda_40D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_40D2)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1A, 2)
    Sound(461, 0, 100, 0)
    OP_71(0x8, 0x1F, 0x3C, 0x0, 0x0)
    OP_79(0x8)

    def lambda_4100():

        label("loc_4100")

        TurnDirection(0x101, 0x18, 500)
        Yield()
        Jump("loc_4100")

    QueueWorkItem2(0x101, 1, lambda_4100)

    def lambda_4112():

        label("loc_4112")

        TurnDirection(0x102, 0x18, 500)
        Yield()
        Jump("loc_4112")

    QueueWorkItem2(0x102, 1, lambda_4112)

    def lambda_4124():

        label("loc_4124")

        TurnDirection(0x103, 0x18, 500)
        Yield()
        Jump("loc_4124")

    QueueWorkItem2(0x103, 1, lambda_4124)

    def lambda_4136():

        label("loc_4136")

        TurnDirection(0x104, 0x18, 500)
        Yield()
        Jump("loc_4136")

    QueueWorkItem2(0x104, 1, lambda_4136)
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

    def lambda_41C2():
        OP_98(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_41C2)
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
            "#11P#0000Fふう……\x01",
            "すごく良い人だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#6P#0204F……そうですね。\x02\x03",

            "#0202Fお人好しのレベルが\x01",
            "ロイドさんに匹敵しそうです。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0058
    ChrTalk(
        0x101,
        "#11P#0006Fあのな……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#0303F#12Pま、それでも\x01",
            "貿易商をやってるくらいだ。\x02\x03",

            "#0300Fただお人好しってだけじゃ\x01",
            "勤まらないと思うけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#0104F#2Pでも、ハロルドさんは\x01",
            "地場産業ときちんと協力しながら\x01",
            "堅実に商売しているみたいね。\x02\x03",

            "#0100Fクロスベルの貿易商は\x01",
            "国際取引で荒稼ぎをする人が\x01",
            "多いって言われているけど……\x02\x03",

            "そんな中では\x01",
            "貴重な存在かもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        "#0305F#12Pなるほど、そういうもんか。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0062
    ChrTalk(
        0x101,
        (
            "#11P#0003Fああいう真っ当な人もいれば\x01",
            "ルバーチェ商会みたいなのもある。\x02\x03",

            "#0000F……それが今のクロスベルか。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        (
            "#0103F#2Pええ、そうね……\x02\x03",

            "#0100Fだから今のクロスベルの全てが\x01",
            "駄目ってことはないと思うの。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#11P#0004Fああ……俺もそう思うよ。\x02",
    )

    CloseMessageWindow()

    def lambda_4561():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4561)
    Sleep(100)

    def lambda_4571():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4571)
    Sleep(50)

    def lambda_4581():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4581)
    Sleep(50)

    def lambda_4591():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4591)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(500)

    #C0065
    ChrTalk(
        0x101,
        (
            "#5P#0000F──さてと、昼過ぎか。\x02\x03",

            "このまま次の目的地に行こうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#0100F#2Pええ……\x01",
            "『聖ウルスラ医科大学』ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x103,
        (
            "#6P#0203F……………………………………\x02\x03",

            "#0200F……たしか南口方面ですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ、このまま南に\x01",
            "まっすぐ抜ければバス停がある。\x02\x03",

            "３０分ごとにバスが出てるって\x01",
            "聞いたことがあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0305F#12Pへえ、そいつは便利だな。\x02\x03",

            "#0300Fまあいい。\x01",
            "とにかく行ってみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ……\x02\x03",

            "#0004F（医科大学か……\x01",
            "  やっとセシル姉に会えるな。）\x02",
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
            "クロスベル市内の地図が利用可能になりました。\x02",
        )
    )

    CloseMessageWindow()

    #A0072
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
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #A0073
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

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "左側の街区リストから\x01",
            "行きたいエリアを選択してください。\x02",
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
            "ただし、状況によっては\x01",
            "市内地図が使えない場合もあります。\x02",
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

    # Function_20_3758 end

    def Function_21_4A1C(): pass

    label("Function_21_4A1C")

    OP_9F(0x0, 0x18)
    OP_9F(0x1, 17420, 0, -4780)
    OP_9F(0x1, 9540, 0, -2690)
    OP_9F(0x1, 1040, 0, -2580)
    OP_9F(0x2, 0x18, 6000, 0x6)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x8)
    Return()

    # Function_21_4A1C end

    def Function_22_4A63(): pass

    label("Function_22_4A63")

    OP_93(0xFE, 0x104, 0x32)
    OP_9F(0x0, 0x18)
    OP_9F(0x1, -5850, 0, -3450)
    OP_9F(0x1, -16290, 0, -3810)
    OP_9F(0x1, -28280, -1380, -3420)
    OP_9F(0x2, 0x18, 6000, 0x6)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x8)
    Return()

    # Function_22_4A63 end

    def Function_23_4AB1(): pass

    label("Function_23_4AB1")

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

    def lambda_4CE3():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4CE3)

    def lambda_4CFD():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4CFD)

    def lambda_4D17():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_4D17)
    Sound(458, 0, 100, 0)

    def lambda_4D38():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4D38)
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

    def lambda_4DC5():
        OP_95(0xFE, 10600, 0, 19000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DC5)
    Sleep(100)

    def lambda_4DE2():
        OP_95(0xFE, 12000, 0, 19000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DE2)
    Sleep(100)

    def lambda_4DFF():
        OP_96(0xFE, 0x2968, 0x0, 0x4FB0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4DFF)
    Sleep(100)

    def lambda_4E1C():
        OP_95(0xFE, 12000, 0, 20400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4E1C)
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
        "#6P#0006Fふわあああぁ～……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        "#0106F#5Pさすがに眠いわね……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#5P#0306F何やかんやで\x01",
            "ほぼ完徹に近いからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#0206F……もう限界です。\x02",
    )

    CloseMessageWindow()

    def lambda_4F93():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F93)
    Sleep(150)

    def lambda_4FA3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4FA3)
    Sleep(50)

    def lambda_4FB3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4FB3)
    Sleep(50)

    def lambda_4FC3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4FC3)
    WaitChrThread(0x104, 2)
    Sleep(300)

    #C0080
    ChrTalk(
        0x101,
        (
            "#6P#0004Fとにかく帰ったら\x01",
            "みんな、一眠りしよう。\x02\x03",

            "#0000F課長への報告はそれからだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        "#0100Fそうね……\x02",
    )

    CloseMessageWindow()

    def lambda_5045():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5045)
    Sleep(200)

    def lambda_5055():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5055)
    Sleep(100)

    def lambda_5065():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5065)
    Sleep(100)

    def lambda_5075():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5075)
    WaitChrThread(0x101, 2)

    def lambda_5086():
        OP_95(0xFE, 10600, 0, 8800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5086)
    WaitChrThread(0x102, 2)

    def lambda_50A4():
        OP_95(0xFE, 12000, 0, 8800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50A4)
    WaitChrThread(0x103, 2)

    def lambda_50C2():
        OP_96(0xFE, 0x2968, 0x0, 0x27D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_50C2)
    WaitChrThread(0x104, 2)

    def lambda_50E0():
        OP_95(0xFE, 12000, 0, 10200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50E0)
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

    def lambda_51C4():
        OP_95(0xFE, -19700, -8200, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_51C4)
    Sleep(50)

    def lambda_51E1():
        OP_96(0xFE, 0xFFFFB62C, 0xFFFFDFF8, 0xFFFFA434, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_51E1)
    Sleep(50)

    def lambda_51FE():
        OP_95(0xFE, -20900, -8200, -23900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51FE)
    Sleep(50)

    def lambda_521B():
        OP_95(0xFE, -20100, -8200, -24700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_521B)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_5243():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5243)
    WaitChrThread(0x102, 1)

    def lambda_5254():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5254)
    WaitChrThread(0x103, 1)

    def lambda_5265():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5265)
    WaitChrThread(0x104, 1)

    def lambda_5276():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5276)
    OP_6F(0x11)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0082
    ChrTalk(
        0x102,
        "#11P#0105Fあら……？\x02",
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
        "#6P#1002Fよー、お疲れさん。\x02",
    )

    CloseMessageWindow()
    OP_68(-29600, -7100, -24900, 2000)

    def lambda_534D():
        OP_96(0xFE, 0xFFFF9048, 0xFFFFDFF8, 0xFFFFA0B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_534D)
    Sleep(50)

    def lambda_536A():
        OP_96(0xFE, 0xFFFF9048, 0xFFFFDFF8, 0xFFFF9C64, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_536A)
    Sleep(50)

    def lambda_5387():
        OP_96(0xFE, 0xFFFF95C0, 0xFFFFDFF8, 0xFFFFA0B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5387)
    Sleep(50)

    def lambda_53A4():
        OP_96(0xFE, 0xFFFF95C0, 0xFFFFDFF8, 0xFFFF9C64, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_53A4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)

    #C0084
    ChrTalk(
        0x101,
        "#11P#0011F課長……どうしたんですか？\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0302Fまさか俺たちを\x01",
            "わざわざ出迎えてくれたのかよ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5522")

    #C0086
    ChrTalk(
        0x1B,
        (
            "#6P#1011Fハッ、そんな\x01",
            "気色悪いことするかよ。\x02\x03",

            "#1002Fただまあ、事件の顛末は\x01",
            "ソーニャからの通信で聞いたぜ。\x02\x03",

            "初めての市外活動にしちゃ\x01",
            "そこそこ頑張った方じゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#11P#0000Fど、どうも……\x01",
            "（……誉めてるんだよな？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5705")

    label("loc_5522")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5622")

    #C0088
    ChrTalk(
        0x1B,
        (
            "#6P#1011Fハッ、そんな\x01",
            "気色悪いことするかよ。\x02\x03",

            "#1002Fただまあ、事件の顛末は\x01",
            "ソーニャからの通信で聞いたぜ。\x02\x03",

            "#1004Fちょいと運任せだったようだが\x01",
            "それなりに頑張ったんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#11P#0005Fは、はあ。\x01",
            "（確かに詰めは甘かったか……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5705")

    label("loc_5622")


    #C0090
    ChrTalk(
        0x1B,
        (
            "#6P#1011Fハッ、そんな\x01",
            "気色悪いことするかよ。\x02\x03",

            "#1002Fただまあ、事件の顛末は\x01",
            "ソーニャからの通信で聞いたぜ。\x02\x03",

            "#1003F運に頼りすぎな気もするが\x01",
            "ま、結果オーライとしてやるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#11P#0006F……すみません。\x01",
            "（言葉も無いな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5705")

    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0092
    ChrTalk(
        0x102,
        (
            "#11P#0100Fそれで……\x01",
            "課長はここで一体何を？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#11P#0200F朝食後の一服にしては\x01",
            "変な所にいますね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x1B,
        (
            "#6P#1011Fいや……無理ねえだろ？\x02\x03",

            "#1001Fあんなのがいきなり訪ねて来たら\x01",
            "さすがに落ち着いて一服できねぇよ。\x02",
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
        "#11P#0005Fあんなの……？\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        "#0305F誰か訪ねてきてるんスか？\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x1B,
        (
            "#6P#1000F知らねぇが……\x01",
            "お前らの客じゃねえのか？\x02\x03",

            "妙に馴れ馴れしいというか、\x01",
            "ふてぶてしい態度だったけどよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#11P#0001F？？？\x01",
            "とにかく中にいるんですよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(300)

    #C0099
    ChrTalk(
        0x102,
        "#12P#0101F……入ってみましょうか。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(400)

    def lambda_5972():

        label("loc_5972")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5972")

    QueueWorkItem2(0x1B, 2, lambda_5972)

    def lambda_5984():

        label("loc_5984")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5984")

    QueueWorkItem2(0x103, 2, lambda_5984)

    def lambda_5996():

        label("loc_5996")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5996")

    QueueWorkItem2(0x104, 2, lambda_5996)
    BeginChrThread(0x102, 3, 0, 24)

    def lambda_59AE():
        OP_95(0xFE, -28600, -8200, -22600, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59AE)
    WaitChrThread(0x101, 1)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_59E7():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59E7)
    Sleep(1200)

    def lambda_59FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_59FF)
    WaitChrThread(0x101, 2)
    Sleep(300)

    def lambda_5A17():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5A17)
    WaitChrThread(0x102, 2)
    Sleep(300)

    def lambda_5A2F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5A2F)
    WaitChrThread(0x104, 2)
    FadeToDark(1000, 0, -1)
    Sleep(300)

    def lambda_5A51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5A51)
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

    # Function_23_4AB1 end

    def Function_24_5AB2(): pass

    label("Function_24_5AB2")

    Sleep(600)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_5AC2():
        OP_95(0xFE, -29300, -8200, -23000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5AC2)
    Sleep(800)

    def lambda_5ADF():
        OP_95(0xFE, -28600, -8200, -24000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5ADF)
    Sleep(100)

    def lambda_5AFC():
        OP_95(0xFE, -29300, -8200, -24400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5AFC)
    WaitChrThread(0x102, 1)

    def lambda_5B1A():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B1A)
    WaitChrThread(0x104, 1)

    def lambda_5B38():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B38)
    WaitChrThread(0x103, 1)

    def lambda_5B56():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B56)
    Return()

    # Function_24_5AB2 end

    def Function_25_5B6C(): pass

    label("Function_25_5B6C")

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

    def lambda_5D1A():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_5D1A)

    def lambda_5D34():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_5D34)
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

    # Function_25_5B6C end

    def Function_26_5E05(): pass

    label("Function_26_5E05")


    def lambda_5E0A():
        OP_95(0xFE, -28400, -8200, -23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E0A)
    WaitChrThread(0x101, 1)

    def lambda_5E28():
        OP_95(0xFE, -28400, -8200, -22300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E28)
    WaitChrThread(0x101, 1)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_5E61():
        OP_95(0xFE, -28400, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E61)
    Sleep(500)

    def lambda_5E7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5E7E)
    WaitChrThread(0x101, 1)
    Return()

    # Function_26_5E05 end

    def Function_27_5E8F(): pass

    label("Function_27_5E8F")


    def lambda_5E94():
        OP_95(0xFE, -28800, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E94)
    WaitChrThread(0x104, 1)

    def lambda_5EB2():
        OP_95(0xFE, -28800, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5EB2)
    Sleep(1500)

    def lambda_5ECF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5ECF)
    WaitChrThread(0x104, 1)
    Return()

    # Function_27_5E8F end

    def Function_28_5EE0(): pass

    label("Function_28_5EE0")

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

    # Function_28_5EE0 end

    def Function_29_5F2C(): pass

    label("Function_29_5F2C")

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
        "#11P#0105Fえ……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#11P#0005Fあの人は……\x02",
    )

    CloseMessageWindow()
    OP_68(-27700, -7100, -24900, 2500)
    OP_6F(0x1)
    Fade(500)
    OP_68(-27960, -7100, -24530, 0)
    MoveCamera(318, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15420, 0)

    def lambda_60FE():
        OP_95(0xFE, -26800, -8200, -24300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60FE)
    Sleep(100)

    def lambda_611B():
        OP_95(0xFE, -26800, -8200, -25500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_611B)
    Sleep(100)

    def lambda_6138():
        OP_95(0xFE, -25400, -8200, -25700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6138)
    Sleep(100)

    def lambda_6155():
        OP_95(0xFE, -25400, -8200, -24500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6155)
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
            "──ああ、良かった！\x02\x03",

            "本当にこの場所でいいのか\x01",
            "迷っていたんだよ。\x02",
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
            "#12P#0105Fアーネストさん……\x02\x03",

            "#0100F……ひょっとして私を\x01",
            "訪ねて来られたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x1C,
        (
            "#5P#2600Fああ、事務所の用事のついでに\x01",
            "訪ねさせてもらったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0105
    ChrTalk(
        0x1C,
        (
            "#5P#2605F……エリィ？\x02\x03",

            "#2601Fどうしたんだい？\x01",
            "元気がないようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        "#12P#0108Fあ……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x1C,
        (
            "#5P#2603F先ほど、アルカンシェルを\x01",
            "訪ねていたようだが……\x02\x03",

            "#2601F何か警察の仕事に問題でも？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#12P#0106F……い、いえ。\x01",
            "大した事じゃないんです。\x02\x03",

            "#0108Fその、劇団の関係者から\x01",
            "相談を受けていたんですけど……\x02\x03",

            "#0102Fその報告に伺っただけなんです。\x02",
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
            "#5P#2606F……ふう、本当はここに\x01",
            "来ようかどうか迷ったんだが。\x02\x03",

            "#2600Fやはり来て正解だったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x102,
        "#12P#0105Fえ……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x1C,
        (
            "#5P#2603F……単刀直入に言おう。\x02\x03",

            "#2601Fエリィ……\x01",
            "警察を辞めて戻ってこないか？\x02",
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
        "#6P#0011F（なっ……！？）\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        (
            "#12P#0301F（おいおい……\x01",
            "  なんだ、この唐突な展開は。）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#12P#0205F（恋愛がらみ……\x01",
            "  では無さそうですけど。）\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x1C,
        (
            "#5P#2603F君にも考えがあって\x01",
            "警察に入ったのは知っている。\x02\x03",

            "#2601Fだが、そんな疲れた顔をして……\x01",
            "子供のように迷った目をして。\x02\x03",

            "本当にそれは……\x01",
            "君が歩むべき道なのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        "#12P#0108Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x1C,
        (
            "#5P#2603F……今の政治状況に\x01",
            "絶望を覚えているのも判る。\x02\x03",

            "おそらく警察入りを志望したのも\x01",
            "その事が関係しているんだろう。\x02\x03",

            "#2601Fだが、エリィ……\x01",
            "少しは市長の苦労と気持ちを\x01",
            "判って差し上げて欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        "#12P#0105Fえ……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x1C,
        (
            "#5P#2601F来月に記念祭を控え……\x01",
            "市長は今、多忙を極めている。\x02\x03",

            "記念祭の後は、予算をめぐって\x01",
            "帝国派と共和国派双方と\x01",
            "やり合わなくてはならない……\x02\x03",

            "#2603Fそして半年後には市長選……\x02\x03",

            "市長は引退されるおつもりだが\x01",
            "後事を託せそうな候補者もおらず、\x01",
            "迷っておられるようだ。\x02\x03",

            "#2600F君が側に居てくれたら\x01",
            "どれほど市長も心強いことか。\x02",
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
            "#5P#2606F……すまない。\x01",
            "差し出がましいことを言って。\x02\x03",

            "だが、どうしても\x01",
            "見過ごすわけには行かなかった。\x02\x03",

            "#2600F市長を尊敬する者として……\x01",
            "昔から君を見てきた者として。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        "#12P#0108F……アーネストさん……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x1C,
        (
            "#5P#2604Fもちろん、君の道は\x01",
            "君が決めるものではあるが……\x02\x03",

            "#2600F本当にそれが正しいのか、\x01",
            "今一度、考えてみてほしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        (
            "#12P#0108F#30W……………………………………\x02\x03",

            "#0106F#40W……少し、考えさせてください。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x1F4)
    Sleep(300)

    #C0126
    ChrTalk(
        0x102,
        (
            "#5P#0102Fみんな、ごめんなさい。\x02\x03",

            "#0103F……少し疲れたから、\x01",
            "ちょっと自室で休ませて。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6B7E():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B7E)
    Sleep(50)
    TurnDirection(0x103, 0x102, 300)

    #C0127
    ChrTalk(
        0x101,
        "#6P#0005Fあ……ああ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)

    def lambda_6BB7():

        label("loc_6BB7")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_6BB7")

    QueueWorkItem2(0x1C, 2, lambda_6BB7)

    def lambda_6BC9():
        OP_95(0xFE, -28600, -8200, -23000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BC9)
    WaitChrThread(0x102, 1)

    def lambda_6BE7():
        OP_95(0xFE, -28600, -8200, -21800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BE7)
    Sleep(300)

    def lambda_6C04():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6C04)
    WaitChrThread(0x102, 1)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_6C30():
        OP_95(0xFE, -28600, -8200, -20000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C30)
    Sleep(300)

    def lambda_6C4D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C4D)
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
            "#5P#2603F──君たち。\x01",
            "いきなり済まなかったね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6CC6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6CC6)
    Sleep(150)

    def lambda_6CD6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6CD6)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x1F4)

    #C0129
    ChrTalk(
        0x101,
        (
            "#6P#0006F……いえ、色々と\x01",
            "事情がおありのようですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#12P#0301Fま、あんまりお嬢のこと\x01",
            "いじめないでやってくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#12P#0203F……ですね。\x02\x03",

            "#0211Fわたしたちからエリィさんを\x01",
            "奪おうとしているみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x1C,
        (
            "#5P#2604Fはは、別にそんなつもりは\x01",
            "無かったんだが……\x02\x03",

            "#2600Fただ君たちは、彼女が元々、\x01",
            "政治家志望なのは知っているかい？\x02",
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
        "#6P#0005Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        "#12P#0305Fおいおい、そうなのかよ！？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x103,
        (
            "#12P#0205F確かに政治や経済のことに\x01",
            "とても詳しいみたいでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x1C,
        (
            "#5P#2600Fああ、市長の後継者として\x01",
            "いずれ政治の道を志すべく、\x01",
            "色々と勉強してきたんだ。\x02\x03",

            "#2603Fそのために各国に留学して、\x01",
            "深い教養と国際的な政治感覚を\x01",
            "養っていたはずだったが……\x02\x03",

            "#2601F……去年、帰国したと思ったら\x01",
            "いきなり警察入りを志望してね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#6P#0001Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        "#12P#0206F……知りませんでした。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#12P#0306Fま、何でこんなセレブなお嬢様が\x01",
            "警察にとは思ったけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x1C,
        (
            "#5P#2603Fできれば、彼女が結論を出すまで\x01",
            "君たちもそっと見守って欲しい。\x02\x03",

            "#2601Fこのまま続けたとしても……\x01",
            "あんな風に迷いを抱えたままでは\x01",
            "とてもやって行けないだろうからね。\x02",
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
            "#5P#2605Fもうこんな時間か……\x02\x03",

            "#2600Fお騒がせをしてしまった。\x01",
            "私はこれで失礼させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#6P#0000Fあ、はい。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-26080, -6900, -25260, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(-23700, -7100, -24900, 6000)

    def lambda_723F():

        label("loc_723F")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_723F")

    QueueWorkItem2(0x101, 2, lambda_723F)

    def lambda_7251():

        label("loc_7251")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_7251")

    QueueWorkItem2(0x103, 2, lambda_7251)

    def lambda_7263():

        label("loc_7263")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_7263")

    QueueWorkItem2(0x104, 2, lambda_7263)

    def lambda_7275():
        OP_95(0xFE, -27600, -8200, -23500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7275)
    WaitChrThread(0x1C, 1)

    def lambda_7293():
        OP_95(0xFE, -20600, -8200, -23500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7293)
    WaitChrThread(0x1C, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    def lambda_72BD():
        OP_95(0xFE, -13800, -4200, -16600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_72BD)
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
        "#6P#0006F……ふう。\x02",
    )

    CloseMessageWindow()

    def lambda_7324():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7324)
    Sleep(50)

    def lambda_7334():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7334)
    Sleep(300)

    #C0144
    ChrTalk(
        0x103,
        (
            "#0206F#11Pなんだか今日は……\x01",
            "溜息をつく事が多いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        (
            "#5P#0306Fああ……濃いイベントが\x01",
            "てんこ盛りだったもんな。\x02\x03",

            "#0301Fなんつーか、精神的に疲れたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#6P#0003F……そうだな。\x02\x03",

            "#0000F課長に報告をしたら\x01",
            "俺たちも早めに上がろう。\x02",
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

    # Function_29_5F2C end

    def Function_30_7459(): pass

    label("Function_30_7459")

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

    def lambda_76EF():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_76EF)

    def lambda_7709():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7709)

    def lambda_7723():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7723)

    def lambda_773E():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_773E)
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

    # Function_30_7459 end

    def Function_31_780E(): pass

    label("Function_31_780E")

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

    def lambda_7A77():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7A77)

    def lambda_7A92():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7A92)

    def lambda_7AAC():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7AAC)
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
            "#11P#0500F皆さん、お疲れさまです。\x02\x03",

            "#0506F本当だったら自分も\x01",
            "協力したい所なんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        (
            "#0102F#6Pううん、塔の探索を\x01",
            "手伝ってくれただけでも十分よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        "#0300F#6Pそうそう、正直助かったぜ。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#6P#0204Fそうですね……\x01",
            "ここまで送ってくれましたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#6P#0002F曹長、本当にありがとう。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x109,
        (
            "#11P#0509Fふふっ、どういたしまして。\x02\x03",

            "#0501Fでも、何かあったら遠慮なく\x01",
            "タングラム門に連絡して下さいね？\x02\x03",

            "今日のことは副司令に\x01",
            "一通り報告しておきますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ……\x01",
            "その時はよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        "#0300F#6Pそんじゃあ、またな。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x109,
        "#11P#0502Fはい……！\x02",
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

    def lambda_7D9C():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7D9C)
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0x5A, 0x1F4)
    OP_71(0xB, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0xB)
    SetChrFlags(0x109, 0x4)

    def lambda_7DDB():
        OP_96(0xFE, 0x125C, 0x1F4, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7DDB)

    def lambda_7DF5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7DF5)
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

    def lambda_7E9D():
        OP_96(0xFE, 0x1770, 0x0, 0xFFFFDC10, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7E9D)
    Sound(486, 0, 100, 0)
    Sleep(1500)

    def lambda_7EC0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7EC0)

    def lambda_7ECD():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7ECD)
    Sleep(300)

    def lambda_7EDD():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7EDD)

    def lambda_7EEA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7EEA)
    WaitChrThread(0x18, 1)
    Sound(471, 0, 100, 0)

    def lambda_7F01():
        OP_9E(0xFE, 0x2EE0, 0xFFFFDC10, 0x15F90, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7F01)
    WaitChrThread(0x18, 1)

    def lambda_7F20():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7F20)
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

    def lambda_7F8D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7F8D)
    Sleep(150)

    def lambda_7F9D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7F9D)
    Sleep(50)

    def lambda_7FAD():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7FAD)
    Sleep(50)

    def lambda_7FBD():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7FBD)
    WaitChrThread(0x104, 2)

    #C0156
    ChrTalk(
        0x101,
        (
            "#0003F#11Pさてと……\x02\x03",

            "#0001Fまずは今週末にある\x01",
            "プレ公演での警戒活動か。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        (
            "#5P#0103Fとりあえず支援課に戻って\x01",
            "段取りについて検討しましょう。\x02\x03",

            "#0100Fアルカンシェルにも連絡しないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x103,
        (
            "#6P#0203F……捜査一課の動向も\x01",
            "掴んでおく必要がありそうですね。\x02\x03",

            "#0202Fそのあたりは課長に頼めば\x01",
            "探ってくれるとは思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        (
            "#0302F#5Pま、いずれにせよ、\x01",
            "メチャクチャ忙しくなりそうだな。\x02",
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
            "その後──ロイドたちは\x01",
            "アルカンシェルの関係者に連絡して\x01",
            "プレ公演での段取りを詰めていった。\x02\x03",

            "その結果、ロイドとエリィが\x01",
            "当日劇場内での警戒活動に当たり……\x02\x03",

            "ランディとティオは\x01",
            "劇場外で待機することにした。\x02\x03",

            "そしてプレ公演当日──\x07\x00\x02",
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

    # Function_31_780E end

    def Function_32_82A4(): pass

    label("Function_32_82A4")

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

    def lambda_844C():
        OP_95(0xFE, 2900, 0, -9300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_844C)
    Sleep(100)

    def lambda_8469():
        OP_95(0xFE, 2600, 0, -11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8469)
    Sleep(50)

    def lambda_8486():
        OP_95(0xFE, 3700, 0, -11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8486)
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
            "#1109F#11Pわあ～！\x01",
            "ヒトがいっぱいいるね～！\x02\x03",

            "#1110Fこのヒトたちもみんな、\x01",
            "ロイドたちのシリアイ！？\x02",
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
            "#12P#0012Fい、いや……\x01",
            "さすがにそれはないけど。\x02\x03",

            "#0000Fでも、これでも記念祭の時よりは\x01",
            "人出は少ないんだけどな……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_861A")

    #C0163
    ChrTalk(
        0x102,
        (
            "#12P#0108Fやっぱりクロスベル市の\x01",
            "出身じゃないのかしら……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86B3")

    label("loc_861A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_8669")

    #C0164
    ChrTalk(
        0x103,
        (
            "#12P#0208Fやはりクロスベルの出身では\x01",
            "ないんでしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86B3")

    label("loc_8669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_86B3")

    #C0165
    ChrTalk(
        0x104,
        (
            "#12P#0308Fやっぱ、クロスベルの出身じゃ\x01",
            "ないってことか……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86B3")

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

    def lambda_8716():

        label("loc_8716")

        TurnDirection(0xFE, 0x12, 100)
        Yield()
        Jump("loc_8716")

    QueueWorkItem2(0x153, 2, lambda_8716)
    OP_68(-2000, 1200, -6000, 4000)
    MoveCamera(45, 20, 0, 4000)
    SetCameraDistance(16000, 4000)

    def lambda_874D():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_874D)
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
            "#1107F#11Pおっきな鉄のハコが\x01",
            "ぶろろろ～って通ってったよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#12P#0014Fはは、あれは車だよ。\x02\x03",

            "#0002F見るのは初めてな感じか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0xB4, 0x1F4)

    #C0168
    ChrTalk(
        0x153,
        (
            "#1109F#5Pうん、たぶんはじめてー！\x02\x03",

            "#1100Fえへへ、そっかぁ！\x01",
            "あれがクルマっていうんだー！\x02\x03",

            "#1110Fねえねえ、ロイドたちは\x01",
            "クルマを持ってないのー！？\x02",
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
        "#12P#0012Fうーん、残念ながら……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x153,
        (
            "#1100F#5Pんー、そっか。\x02\x03",

            "みんなでいっしょに乗れたら\x01",
            "楽しそうって思ったんだけどー。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_8AAD")

    #C0171
    ChrTalk(
        0x102,
        (
            "#12P#0106Fうーん、捜査一課が\x01",
            "羨ましくなってきたわね……\x02\x03",

            "#0101Fでも、やっぱりクロスベルの\x01",
            "出身ではなさそうね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BAC")

    label("loc_8AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_8B2D")

    #C0172
    ChrTalk(
        0x103,
        (
            "#12P#0206F何だか捜査一課が\x01",
            "羨ましくなりますね……\x02\x03",

            "#0201Fしかし、やはりクロスベルの\x01",
            "出身ではなさそうですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BAC")

    label("loc_8B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_8BAC")

    #C0173
    ChrTalk(
        0x104,
        (
            "#12P#0306Fったく、捜査一課が\x01",
            "羨ましくなっちまったな……\x02\x03",

            "#0301Fしかし、やっぱクロスベルの\x01",
            "出身じゃなさそうだな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BAC")


    #C0174
    ChrTalk(
        0x101,
        (
            "#6P#0006Fああ、この街に住んでいたら\x01",
            "毎日のように見てるはずだしな。\x02\x03",

            "#0001F（でも、車に関する\x01",
            "  知識はあるみたいだけど……）\x02\x03",

            "（……どういう事なんだろう？）\x02",
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
            "#1100F#5Pどうしたの、ロイド？\x02\x03",

            "ゆーげきしの人に\x01",
            "会いに行かなくていーの？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        "#12P#0000Fああ、それじゃあ行こうか。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_8D12")

    #C0177
    ChrTalk(
        0x102,
        "#12P#0100F東通りに出ましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D73")

    label("loc_8D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_8D44")

    #C0178
    ChrTalk(
        0x103,
        "#12P#0202F東通りに出ましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D73")

    label("loc_8D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_8D73")

    #C0179
    ChrTalk(
        0x104,
        "#12P#0300F東通りに出るとするか。\x02",
    )

    CloseMessageWindow()

    label("loc_8D73")

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

    # Function_32_82A4 end

    def Function_33_8DEC(): pass

    label("Function_33_8DEC")

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
            "それから３週間──\x02\x03",

            "キーアの記憶は戻る気配もなく、\x01",
            "その素性も、遊撃士協会の情報網に\x01",
            "結局引っかかることはなかった。\x02\x03",

            "創立記念祭が終わり、\x01",
            "市長選を数ヶ月後に控えてはいるが、\x01",
            "比較的落ち着いた日々の中……\x02\x03",

            "ロイドたちは彼女との生活に\x01",
            "完全に馴染んでしまっており、\x01",
            "日常的な業務にも復帰していた。\x02\x03",

            "またキーアも、日中はロイドたちに\x01",
            "仕事があるのを理解したようで、\x01",
            "我儘も言わずに留守番しているのであった。\x02\x03",

            "そして──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7201", 0)
    ReplaceBGM("ed7100", "ed7201")

    def lambda_9153():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_9153)

    def lambda_916E():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_916E)

    def lambda_9188():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9188)
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

    # Function_33_8DEC end

    def Function_34_927F(): pass

    label("Function_34_927F")


    def lambda_9284():
        OP_95(0xFE, -28400, -8200, -23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9284)
    WaitChrThread(0x101, 1)

    def lambda_92A2():
        OP_95(0xFE, -28400, -8200, -22300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92A2)
    WaitChrThread(0x101, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_92DB():
        OP_95(0xFE, -28400, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92DB)
    Sleep(500)

    def lambda_92F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_92F8)
    WaitChrThread(0x101, 1)
    Return()

    # Function_34_927F end

    def Function_35_9309(): pass

    label("Function_35_9309")


    def lambda_930E():
        OP_95(0xFE, -28800, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_930E)
    WaitChrThread(0x102, 1)

    def lambda_932C():
        OP_95(0xFE, -28800, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_932C)
    Sleep(1500)

    def lambda_9349():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9349)
    WaitChrThread(0x102, 1)
    Return()

    # Function_35_9309 end

    def Function_36_935A(): pass

    label("Function_36_935A")


    def lambda_935F():
        OP_95(0xFE, -28400, -8200, -23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_935F)
    WaitChrThread(0x103, 1)

    def lambda_937D():
        OP_95(0xFE, -28400, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_937D)
    Sleep(1500)

    def lambda_939A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_939A)
    WaitChrThread(0x103, 1)
    Return()

    # Function_36_935A end

    def Function_37_93AB(): pass

    label("Function_37_93AB")


    def lambda_93B0():
        OP_95(0xFE, -28800, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_93B0)
    WaitChrThread(0x104, 1)

    def lambda_93CE():
        OP_95(0xFE, -28800, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_93CE)
    Sleep(1500)

    def lambda_93EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_93EB)
    WaitChrThread(0x104, 1)
    Return()

    # Function_37_93AB end

    def Function_38_93FC(): pass

    label("Function_38_93FC")

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

    # Function_38_93FC end

    def Function_39_9448(): pass

    label("Function_39_9448")

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

    def lambda_9579():
        OP_95(0xFE, -28700, -8200, -23500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9579)

    def lambda_9593():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9593)
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
            "#5P#0500F──警備隊の車両は\x01",
            "街の北口に停めてあります。\x02\x03",

            "自治州内であれば\x01",
            "どこでもお送りできると思うので\x01",
            "遠慮なく言ってください。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_975E")

    #C0182
    ChrTalk(
        0x101,
        (
            "#12P#0004Fああ、分かった。\x02\x03",

            "#0000F例の遺跡っていうのは\x01",
            "山道にあるトンネルの途中から\x01",
            "分岐した先にある遺跡だよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#6P#0203F以前、遺跡の入口前まで\x01",
            "行ってみたことはありますね。\x02\x03",

            "#0200Fその時には警備隊のバリケードで\x01",
            "封鎖されていましたが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98D4")

    label("loc_975E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 7)), scpexpr(EXPR_END)), "loc_981C")

    #C0184
    ChrTalk(
        0x101,
        (
            "#12P#0004Fああ、分かった。\x02\x03",

            "#0000F例の遺跡っていうのは\x01",
            "山道にあるトンネルの途中から\x01",
            "分岐した先にあるんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        (
            "#6P#0202F確かに鉱山町方面とは\x01",
            "別の場所に出ましたよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98D4")

    label("loc_981C")


    #C0186
    ChrTalk(
        0x101,
        (
            "#12P#0004Fああ、分かった。\x02\x03",

            "#0000F例の遺跡っていうのは\x01",
            "山道にあるトンネルの途中から\x01",
            "分岐した先にあるんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x103,
        (
            "#6P#0202F確かに、トンネルの途中で\x01",
            "細い道が分かれていましたね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98D4")


    #C0188
    ChrTalk(
        0x109,
        (
            "#5P#0500Fええ、そちらは道が悪いので\x01",
            "トンネルの途中からは\x01",
            "徒歩で行く事になりますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x104,
        (
            "#11P#0309Fそんじゃ、用事を片付けたら\x01",
            "山道のトンネルまで行こうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        (
            "#12P#0108F（……はあ。\x01",
            "  幽霊が出没する遺跡か……）\x02",
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

    # Function_39_9448 end

    def Function_40_9A13(): pass

    label("Function_40_9A13")


    def lambda_9A18():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A18)

    def lambda_9A32():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9A32)
    WaitChrThread(0xFE, 1)

    def lambda_9A47():
        OP_95(0xFE, -28100, -8200, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A47)
    WaitChrThread(0x101, 1)

    def lambda_9A65():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A65)
    WaitChrThread(0x101, 2)
    Return()

    # Function_40_9A13 end

    def Function_41_9A78(): pass

    label("Function_41_9A78")


    def lambda_9A7D():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A7D)

    def lambda_9A97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9A97)
    WaitChrThread(0xFE, 1)

    def lambda_9AAC():
        OP_95(0xFE, -29400, -8200, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9AAC)
    WaitChrThread(0x102, 1)

    def lambda_9ACA():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9ACA)
    WaitChrThread(0x102, 2)
    Return()

    # Function_41_9A78 end

    def Function_42_9ADD(): pass

    label("Function_42_9ADD")


    def lambda_9AE2():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9AE2)

    def lambda_9AFC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9AFC)
    WaitChrThread(0xFE, 1)

    def lambda_9B11():
        OP_95(0xFE, -30400, -8200, -25300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9B11)
    WaitChrThread(0x103, 1)

    def lambda_9B2F():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9B2F)
    WaitChrThread(0x103, 2)
    Return()

    # Function_42_9ADD end

    def Function_43_9B42(): pass

    label("Function_43_9B42")


    def lambda_9B47():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B47)

    def lambda_9B61():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9B61)
    WaitChrThread(0xFE, 1)

    def lambda_9B76():
        OP_95(0xFE, -27000, -8200, -25300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9B76)
    WaitChrThread(0x104, 1)

    def lambda_9B94():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9B94)
    WaitChrThread(0x104, 2)
    Return()

    # Function_43_9B42 end

    def Function_44_9BA7(): pass

    label("Function_44_9BA7")

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

    def lambda_9DF2():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_9DF2)

    def lambda_9E0D():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_9E0D)

    def lambda_9E27():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9E27)
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
            "#11P#0509F──今日は本当に\x01",
            "ありがとうございました！\x02\x03",

            "#0502Fご恩は近いうちに\x01",
            "必ず返させていただきます！\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        "#6P#0002Fはは、大げさだなぁ。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x104,
        (
            "#0304F#6Pま、なかなか興味深い\x01",
            "体験をさせてもらったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x102,
        (
            "#0106F#6Pあの遺跡──\x01",
            "《僧院》についてだけど……\x02\x03",

            "#0108F一応、クロスベル大聖堂に\x01",
            "相談してみた方が\x01",
            "いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x103,
        (
            "#6P#0206F……そうですね。\x02\x03",

            "アーティファクト絡みであれば\x01",
            "他にどうしようもありませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x109,
        (
            "#11P#0503Fなるほど……\x02\x03",

            "#0500F分かりました、副司令と相談して\x01",
            "そのあたりの対応は考えてみます。\x02\x03",

            "#0505F皆さんの方は……\x01",
            "これから街で聞き込みですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#6P#0004Fああ、少なくとも\x01",
            "カジノは訪ねてみるつもりだ。\x02\x03",

            "#0000Fもし、警備隊の方で\x01",
            "それらしい情報があったら\x01",
            "こっちに連絡してくれないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x109,
        (
            "#11P#0500F分かりました。\x01",
            "鉱山町のガンツさんですね。\x02",
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
            "#2P#0502F#11Pそれでは失礼します。\x01",
            "皆さん、お疲れさまでした！\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        "#0302F#6Pおお、そっちこそお疲れ。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_92(0x109, 0xE74, 0xFFFFBEC4, 0x1F4)

    def lambda_A245():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A245)
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0x5A, 0x1F4)
    OP_71(0xB, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0xB)
    SetChrFlags(0x109, 0x4)

    def lambda_A284():
        OP_96(0xFE, 0x125C, 0x1F4, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A284)

    def lambda_A29E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A29E)
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

    def lambda_A34C():
        OP_96(0xFE, 0x1770, 0x0, 0xFFFFDC10, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A34C)
    Sleep(1500)

    def lambda_A369():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A369)

    def lambda_A376():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A376)
    Sleep(300)

    def lambda_A386():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A386)

    def lambda_A393():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A393)
    WaitChrThread(0x18, 1)
    Sound(471, 0, 100, 0)

    def lambda_A3AA():
        OP_9E(0xFE, 0x2EE0, 0xFFFFDC10, 0x15F90, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A3AA)
    WaitChrThread(0x18, 1)

    def lambda_A3C9():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A3C9)
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

    def lambda_A436():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A436)
    Sleep(150)

    def lambda_A446():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A446)
    Sleep(50)

    def lambda_A456():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A456)
    Sleep(50)

    def lambda_A466():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A466)
    WaitChrThread(0x104, 2)

    #C0201
    ChrTalk(
        0x101,
        (
            "#0000Fさてと……\x01",
            "それじゃあ時間もないし、\x01",
            "このままカジノに行ってみるか。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102)

    #C0202
    ChrTalk(
        0x102,
        (
            "#5P#0100Fええ、そのガンツさんっていう\x01",
            "鉱員の情報を集めないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x104,
        (
            "#0309Fそんじゃあとっとと\x01",
            "歓楽街の方に行こうぜ。\x02",
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

    # Function_44_9BA7 end

    def Function_45_A5AF(): pass

    label("Function_45_A5AF")

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

    def lambda_A7D7():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A7D7)

    def lambda_A7F1():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A7F1)

    def lambda_A80B():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_A80B)
    Sound(458, 0, 100, 0)

    def lambda_A82C():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A82C)
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

    # Function_45_A5AF end

    def Function_46_A8CD(): pass

    label("Function_46_A8CD")

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
            "#1K翌日、８：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7001", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_AB52():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_AB52)

    def lambda_AB6C():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_AB6C)

    def lambda_AB86():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_AB86)

    def lambda_ABA1():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_ABA1)
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

    # Function_46_A8CD end

    def Function_47_AC44(): pass

    label("Function_47_AC44")

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
            "#1K同日、１７：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7100", 0)

    def lambda_AE70():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_AE70)

    def lambda_AE8B():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_AE8B)

    def lambda_AEA5():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_AEA5)
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

    # Function_47_AC44 end

    def Function_48_AF86(): pass

    label("Function_48_AF86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFB4")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)
    Jump("loc_AFDD")

    label("loc_AFB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFDD")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_AFDD")

    Return()

    # Function_48_AF86 end

    def Function_49_AFDE(): pass

    label("Function_49_AFDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B00C")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)
    Jump("loc_B035")

    label("loc_B00C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B035")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_B035")

    Return()

    # Function_49_AFDE end

    def Function_50_B036(): pass

    label("Function_50_B036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B064")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)
    Jump("loc_B08D")

    label("loc_B064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B08D")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_B08D")

    Return()

    # Function_50_B036 end

    def Function_51_B08E(): pass

    label("Function_51_B08E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B0B7")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_B0B7")

    Return()

    # Function_51_B08E end

    def Function_52_B0B8(): pass

    label("Function_52_B0B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B0E6")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)
    Jump("loc_B10F")

    label("loc_B0E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B10F")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_B10F")

    Return()

    # Function_52_B0B8 end

    def Function_53_B110(): pass

    label("Function_53_B110")


    #C0206
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……先に\x01",
            "オーバルストアに寄ってみよう。\x02\x03",

            "#0000Fそこの角の建物のはずだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B194")

    #C0207
    ChrTalk(
        0x103,
        "#0200F了解です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1FB")

    label("loc_B194")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1C7")

    #C0208
    ChrTalk(
        0x104,
        "#0300F了解、行ってみるか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1FB")

    label("loc_B1C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1FB")

    #C0209
    ChrTalk(
        0x102,
        "#0100Fそうね、行ってみましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_B1FB")

    Return()

    # Function_53_B110 end

    def Function_54_B1FC(): pass

    label("Function_54_B1FC")


    #C0210
    ChrTalk(
        0x101,
        (
            "#0000F今日はさすがに疲れたな……\x01",
            "寄り道せずに支援課に帰ろう。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_54_B1FC end

    def Function_55_B240(): pass

    label("Function_55_B240")

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

    # Function_55_B240 end

    def Function_56_B28B(): pass

    label("Function_56_B28B")

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

    # Function_56_B28B end

    SaveToFile()

Try(main)
