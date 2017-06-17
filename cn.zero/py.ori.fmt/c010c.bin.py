from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c010c.bin",                # FileName
        "c010c",                    # MapName
        "c010c",                    # Location
        0x0004,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 5, 0, 6],
    )

    BuildStringList((
        "c010c",                  # 0
        "亚贝尔",                 # 1
        "米米",                   # 2
        "吉娜",                   # 3
        "昆提老人",               # 4
        "普鲁娜",                 # 5
        "利娜莉",                 # 6
        "哈斯",                   # 7
        "阿罗纳",                 # 8
        "纳德尔",                 # 9
        "梅吉",                   # 10
        "侬诺",                   # 11
        "隆",                     # 12
        "寇肯",                   # 13
        "菲伊",                   # 14
        "潘莎",                   # 15
        "希伦护士",               # 16
        "梅菲尔护士",             # 17
        "凯特巡警",               # 18
        "游客",                   # 19
        "游客",                   # 20
        "游客",                   # 21
        "游客",                   # 22
        "蔡特",                   # 23
        "柯贝",                   # 24
        "客人",                   # 25
        "客人",                   # 26
        "客人",                   # 27
        "青年",                   # 28
        "青年",                   # 29
        "SE控制",                 # 30
        "中央广场",               # 31
        "西街",                   # 32
        "行政区",                 # 33
        "住宅街",                 # 34
        "欢乐街",                 # 35
        "东街",                   # 36
        "旧城区",                 # 37
        "港湾区",                 # 38
        "ＩＢＣ",                 # 39
        "站前街道",               # 40
        "后巷",                   # 41
        "乌尔斯拉间道",           # 42
        "东克洛斯贝尔街道",       # 43
        "西克洛斯贝尔街道",       # 44
        "玛因兹山道",             # 45
    ))

    AddCharChip((
        "chr/ch20200.itc",                   # 00
        "chr/ch20700.itc",                   # 01
        "chr/ch21300.itc",                   # 02
        "chr/ch20002.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch22100.itc",                   # 05
        "chr/ch20300.itc",                   # 06
        "chr/ch26000.itc",                   # 07
        "chr/ch24500.itc",                   # 08
        "chr/ch25600.itc",                   # 09
        "chr/ch02707.itc",                   # 0A
        "chr/ch39200.itc",                   # 0B
        "chr/ch32300.itc",                   # 0C
        "chr/ch32400.itc",                   # 0D
        "chr/ch32200.itc",                   # 0E
        "chr/ch21600.itc",                   # 0F
        "chr/ch20600.itc",                   # 10
        "chr/ch21000.itc",                   # 11
        "chr/ch32700.itc",                   # 12
        "chr/ch22300.itc",                   # 13
        "chr/ch36500.itc",                   # 14
        "chr/ch36400.itc",                   # 15
        "chr/ch30600.itc",                   # 16
        "chr/ch26900.itc",                   # 17
    ))

    DeclNpc(-6099,   0,       -9409,   90,   261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-289,    0,       -10319,  225,  261,  0x0, 0,   1,   0,   0,   2,   0,   10,  255,  0)
    DeclNpc(30000,   0,       -1799,   270,  261,  0x0, 0,   2,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(-6090,   150,     4449,    270,  341,  0x0, 0,   3,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(850,     0,       17969,   90,   277,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(2539,    0,       17870,   270,  277,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(8310,    0,       -9510,   315,  261,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(1879,    0,       -4300,   180,  261,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(12420,   0,       2730,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-7400,   0,       15560,   180,  261,  0x0, 0,   8,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-17479,  0,       610,     135,  389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-15449,  0,       -2259,   90,   261,  0x0, 0,   16,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-14100,  0,       -2259,   270,  261,  0x0, 0,   17,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-3519,   0,       9729,    225,  405,  0x0, 0,   18,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-4710,   0,       8529,    45,   405,  0x0, 0,   19,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-11829,  0,       -2779,   90,   405,  0x0, 0,   20,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-12090,  0,       -1389,   135,  405,  0x0, 0,   21,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-2579,   0,       -2119,   197,  261,  0x0, 0,   22,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(7300,    0,       -16639,  0,    261,  0x0, 0,   12,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(7300,    0,       -15159,  180,  261,  0x0, 0,   23,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(0,       0,       15109,   0,    261,  0x0, 0,   14,  0,   0,   4,   0,   30,  255,  0)
    DeclNpc(-15829,  0,       7170,    180,  261,  0x0, 0,   15,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(-25440,  1299,    -17040,  225,  276,  0x0, 0,   10,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(-22450,  1299,    -20010,  315,  261,  0x0, 0,   11,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 67,  -28.5,                 -21.5,                 -9.199999809265137,    4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.25,                 10.75,                 1.840000033378601,     1.0])

    DeclActor(-270,    0,       -980,    800,     130,     1500,    -10,     0x007C, 0,  37, 0x0000)
    DeclActor(-290,    -1000,   4400,    600,     -290,    -1000,   4400,    0x007C, 0,  38, 0x0000)
    DeclActor(-20,     -1000,   4760,    800,     800,     1800,    4570,    0x007C, 0,  61, 0x0000)
    DeclActor(1740,    -950,    3070,    1100,    1740,    550,     3070,    0x007C, 0,  8,  0x0000)

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

    ScpFunction((
        "Function_0_89C",          # 00, 0
        "Function_1_954",          # 01, 1
        "Function_2_9A1",          # 02, 2
        "Function_3_9CC",          # 03, 3
        "Function_4_9F7",          # 04, 4
        "Function_5_A80",          # 05, 5
        "Function_6_1327",         # 06, 6
        "Function_7_1428",         # 07, 7
        "Function_8_14D3",         # 08, 8
        "Function_9_1628",         # 09, 9
        "Function_10_1980",        # 0A, 10
        "Function_11_1FA9",        # 0B, 11
        "Function_12_2311",        # 0C, 12
        "Function_13_2833",        # 0D, 13
        "Function_14_2A3E",        # 0E, 14
        "Function_15_2C2E",        # 0F, 15
        "Function_16_2EF4",        # 10, 16
        "Function_17_3534",        # 11, 17
        "Function_18_3619",        # 12, 18
        "Function_19_3C04",        # 13, 19
        "Function_20_44C1",        # 14, 20
        "Function_21_456D",        # 15, 21
        "Function_22_4C1F",        # 16, 22
        "Function_23_4DDE",        # 17, 23
        "Function_24_4E61",        # 18, 24
        "Function_25_4EA9",        # 19, 25
        "Function_26_4F51",        # 1A, 26
        "Function_27_5059",        # 1B, 27
        "Function_28_5457",        # 1C, 28
        "Function_29_55D3",        # 1D, 29
        "Function_30_56CD",        # 1E, 30
        "Function_31_5867",        # 1F, 31
        "Function_32_5A7C",        # 20, 32
        "Function_33_5C77",        # 21, 33
        "Function_34_6E1B",        # 22, 34
        "Function_35_6FC6",        # 23, 35
        "Function_36_7117",        # 24, 36
        "Function_37_71B3",        # 25, 37
        "Function_38_7419",        # 26, 38
        "Function_39_7475",        # 27, 39
        "Function_40_7946",        # 28, 40
        "Function_41_8134",        # 29, 41
        "Function_42_82F6",        # 2A, 42
        "Function_43_8342",        # 2B, 43
        "Function_44_8500",        # 2C, 44
        "Function_45_8B62",        # 2D, 45
        "Function_46_9257",        # 2E, 46
        "Function_47_927D",        # 2F, 47
        "Function_48_92C4",        # 30, 48
        "Function_49_9360",        # 31, 49
        "Function_50_93FC",        # 32, 50
        "Function_51_949D",        # 33, 51
        "Function_52_94C6",        # 34, 52
        "Function_53_94FE",        # 35, 53
        "Function_54_9527",        # 36, 54
        "Function_55_9554",        # 37, 55
        "Function_56_9581",        # 38, 56
        "Function_57_959D",        # 39, 57
        "Function_58_95B9",        # 3A, 58
        "Function_59_95D1",        # 3B, 59
        "Function_60_9600",        # 3C, 60
        "Function_61_9B88",        # 3D, 61
        "Function_62_9F98",        # 3E, 62
        "Function_63_9FEB",        # 3F, 63
        "Function_64_A067",        # 40, 64
        "Function_65_A0E3",        # 41, 65
        "Function_66_A136",        # 42, 66
        "Function_67_A1B2",        # 43, 67
        "Function_68_A1CE",        # 44, 68
        "Function_69_A2AD",        # 45, 69
        "Function_70_A2F8",        # 46, 70
        "Function_71_A341",        # 47, 71
        "Function_72_A392",        # 48, 72
        "Function_73_A3D4",        # 49, 73
        "Function_74_A425",        # 4A, 74
    ))


    def Function_0_89C(): pass

    label("Function_0_89C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_8DC"),
        (1, "loc_8E8"),
        (2, "loc_8F4"),
        (3, "loc_900"),
        (4, "loc_90C"),
        (5, "loc_918"),
        (6, "loc_924"),
        (SWITCH_DEFAULT, "loc_930"),
    )


    label("loc_8DC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_8E8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_8F4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_900")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_90C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_918")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_924")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_930")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_93C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_953")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_953")

    Return()

    # Function_0_89C end

    def Function_1_954(): pass

    label("Function_1_954")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A0")
    OP_95(0xFE, 10430, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 10430, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_1_954")

    label("loc_9A0")

    Return()

    # Function_1_954 end

    def Function_2_9A1(): pass

    label("Function_2_9A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9CB")
    OP_94(0xFE, 0x366, 0xFFFFE296, 0xFFFFF236, 0xFFFFD166, 0x3E8)
    Sleep(300)
    Jump("Function_2_9A1")

    label("loc_9CB")

    Return()

    # Function_2_9A1 end

    def Function_3_9CC(): pass

    label("Function_3_9CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F6")
    OP_94(0xFE, 0xFFFFA9C0, 0xFFFFBD34, 0xFFFF9D36, 0xFFFFB0AA, 0x3E8)
    Sleep(300)
    Jump("Function_3_9CC")

    label("loc_9F6")

    Return()

    # Function_3_9CC end

    def Function_4_9F7(): pass

    label("Function_4_9F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7F")
    OP_95(0xFE, -7290, 0, 11150, 2000, 0x0)
    OP_95(0xFE, -13960, 0, 1780, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x168, 0x190)
    Sleep(100)
    OP_95(0xFE, -7290, 0, 11150, 2000, 0x0)
    OP_95(0xFE, 0, 0, 15110, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    Jump("Function_4_9F7")

    label("loc_A7F")

    Return()

    # Function_4_9F7 end

    def Function_5_A80(): pass

    label("Function_5_A80")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1191")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B42")
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    SetChrPos(0x1, -26950, -1160, -4340, 90)
    SetChrPos(0x2, -26950, -1160, -4340, 90)
    SetChrPos(0x3, -26950, -1160, -4340, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B15")
    SetChrPos(0x4, -26950, -1160, -4340, 90)
    SetChrPos(0x5, -26950, -1160, -4340, 90)
    Jump("loc_B34")

    label("loc_B15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B34")
    SetChrPos(0x4, -26950, -1160, -4340, 90)

    label("loc_B34")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_B42")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF6")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC9")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_BE8")

    label("loc_BC9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE8")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_BE8")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_BF6")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAA")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7D")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_C9C")

    label("loc_C7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9C")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_C9C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_CAA")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5E")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D31")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_D50")

    label("loc_D31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D50")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_D50")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_D5E")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E12")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE5")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_E04")

    label("loc_DE5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E04")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_E04")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_E12")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC6")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E99")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_EB8")

    label("loc_E99")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB8")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_EB8")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_EC6")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7A")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4D")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_F6C")

    label("loc_F4D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F6C")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_F6C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_F7A")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102E")
    SetChrPos(0x0, 4040, 0, -21980, 0)
    SetChrPos(0x1, 4040, 0, -21980, 0)
    SetChrPos(0x2, 4040, 0, -21980, 0)
    SetChrPos(0x3, 4040, 0, -21980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1001")
    SetChrPos(0x4, 4040, 0, -21980, 0)
    SetChrPos(0x5, 4040, 0, -21980, 0)
    Jump("loc_1020")

    label("loc_1001")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1020")
    SetChrPos(0x4, 4040, 0, -21980, 0)

    label("loc_1020")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_102E")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E2")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B5")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_10D4")

    label("loc_10B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D4")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_10D4")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_10E2")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1191")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1169")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_1188")

    label("loc_1169")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1188")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_1188")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1191")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_11C3")
    SetChrPos(0x1F, -26850, 1300, -17520, 89)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_1285")

    label("loc_11C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_11E0")
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_1285")

    label("loc_11E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1204")
    SetChrPos(0x1F, -25480, 1300, -18700, 0)
    SetChrFlags(0x19, 0x80)
    Jump("loc_1285")

    label("loc_1204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1236")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x1F, -28010, 1300, -19360, 45)
    OP_93(0x13, 0x0, 0x0)
    OP_93(0x14, 0x0, 0x0)
    Jump("loc_1285")

    label("loc_1236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1268")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x1F, -28010, 1300, -19360, 45)
    OP_93(0x13, 0x0, 0x0)
    OP_93(0x14, 0x0, 0x0)
    Jump("loc_1285")

    label("loc_1268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1285")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_1285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A0")
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_12B6")

    label("loc_12A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12B6")
    SetMapFlags(0x10000000)
    Event(0, 40)

    label("loc_12B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_12C7")
    ClearScenarioFlags(0x5C, 0)
    Jump("loc_1326")

    label("loc_12C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_12D8")
    ClearScenarioFlags(0x5C, 1)
    Jump("loc_1326")

    label("loc_12D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_12EC")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 41)
    Jump("loc_1326")

    label("loc_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_1300")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 43)
    Jump("loc_1326")

    label("loc_1300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_1317")
    ClearScenarioFlags(0x5C, 4)
    SetScenarioFlags(0x1, 5)
    Event(0, 45)
    Jump("loc_1326")

    label("loc_1317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_1326")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 60)

    label("loc_1326")

    Return()

    # Function_5_A80 end

    def Function_6_1327(): pass

    label("Function_6_1327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_133C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 5)

    label("loc_133C")

    OP_52(0x1E, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)
    OP_10(0xB, 0x0)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_138D")
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)

    label("loc_138D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A0")
    OP_70(0xC, 0x0)
    Jump("loc_13A4")

    label("loc_13A0")

    OP_70(0xC, 0x1E)

    label("loc_13A4")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 10000, -4000, 5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -10000, -4000, 5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_6_1327 end

    def Function_7_1428(): pass

    label("Function_7_1428")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    OP_1B(0x4, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1468")
    OP_1B(0x1, 0x0, 0x3F)
    OP_1B(0x2, 0x0, 0x40)
    OP_1B(0x3, 0x0, 0x41)
    OP_1B(0x4, 0x0, 0x42)

    label("loc_1468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1485")
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x1, 0x0, 0x3F)
    OP_1B(0x2, 0x0, 0x40)

    label("loc_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149D")
    OP_1B(0x0, 0x0, 0x3E)
    OP_1B(0x4, 0x0, 0x42)

    label("loc_149D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B0")
    OP_1B(0x4, 0x0, 0x42)

    label("loc_14B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14D2")
    OP_1B(0x0, 0x0, 0x3E)
    OP_1B(0x1, 0x0, 0x3F)
    OP_1B(0x2, 0x0, 0x40)
    OP_1B(0x3, 0x0, 0x41)

    label("loc_14D2")

    Return()

    # Function_7_1428 end

    def Function_8_14D3(): pass

    label("Function_8_14D3")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F9")
    Sound(14, 0, 100, 0)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xC, 0x1E)
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
    Jump("loc_1616")

    label("loc_15F9")


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

    label("loc_1616")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_14D3 end

    def Function_9_1628(): pass

    label("Function_9_1628")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_169F")

    #C0003
    ChrTalk(
        0xFE,
        (
            "虽然在这期间并没能\x01",
            "为米米做任何特别的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "不过，她还是玩得那么开心。\x01",
            "这样，我也就满足了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197C")

    label("loc_169F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_170C")

    #C0005
    ChrTalk(
        0xFE,
        "还好，游行活动平安结束了。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "这是纪念庆典一项重要的活动，\x01",
            "政府在交通方面似乎特别注意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197C")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_179D")

    #C0007
    ChrTalk(
        0xFE,
        (
            "可能是因为有游行吧，\x01",
            "和昨天比起来，\x01",
            "似乎更加热闹了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "要是与导力车撞上的话，可就全都泡汤了，\x01",
            "希望他们能做好道路指挥啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197C")

    label("loc_179D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_181F")

    #C0009
    ChrTalk(
        0xFE,
        (
            "港湾区的演唱会\x01",
            "还挺有趣的，\x01",
            "米米也看得十分开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，\x01",
            "好像一直有各种活动，\x01",
            "经常去看看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197C")

    label("loc_181F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_18A4")

    #C0011
    ChrTalk(
        0xFE,
        (
            "从昨天起，就和米米一起\x01",
            "逛了各家露天店铺。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "因为没能买到期待已久的\x01",
            "彩虹剧团公演门票，\x01",
            "所以多少也要补偿她一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197C")

    label("loc_18A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_197C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1923")

    #C0013
    ChrTalk(
        0xFE,
        (
            "城市各方向的出入口，\x01",
            "从昨天起可真是不得了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "停了好多的外国导力车，\x01",
            "那些都有准停证吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_197C")

    label("loc_1923")


    #C0015
    ChrTalk(
        0xFE,
        (
            "城市各方向的出入口，\x01",
            "从昨天起可真是不得了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "看起来，违章停车好像也有不少……\x02",
    )

    CloseMessageWindow()

    label("loc_197C")

    TalkEnd(0xFE)
    Return()

    # Function_9_1628 end

    def Function_10_1980(): pass

    label("Function_10_1980")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_19EA")

    #C0017
    ChrTalk(
        0xFE,
        (
            "虽然没能去米修拉姆，\x01",
            "也没能去彩虹剧团……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "可是和爸爸一起到处玩，还是好开心哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FA5")

    label("loc_19EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_1A2E")

    #C0019
    ChrTalk(
        0xFE,
        "游行也好有趣哦！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "罗伊德哥哥，你们没看吗～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FA5")

    label("loc_1A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1C62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BCA")

    #C0021
    ChrTalk(
        0x101,
        (
            "#0000F（嗯，这孩子\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0023
    ChrTalk(
        0xFE,
        "哎？这孩子……？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "嗯～这么说来……\x01",
            "好像是追着游行队伍的那个孩子呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#0005F你有印象吗？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "嗯，他就跟在游行队伍的最后呢～\x01",
            "在队伍后面小步跑着。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "我想应该就是这孩子～\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0003F是吗……\x01",
            "（和艾莉所说的情报一致啊。）\x02\x03",

            "#0000F谢谢，帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 36)
    Jump("loc_1C5D")

    label("loc_1BCA")


    #C0029
    ChrTalk(
        0xFE,
        (
            "米米很认真地看了游行，\x01",
            "所以记得哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "他就跟在游行队伍的最后呢～\x01",
            "在队伍后面小步跑着。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x160,
        (
            "#3300F呵呵……\x01",
            "……似乎是个好奇心旺盛的孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5D")

    Jump("loc_1FA5")

    label("loc_1C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1CA4")

    #C0032
    ChrTalk(
        0xFE,
        "游行好有趣哦！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "罗伊德哥哥，你们没看吗～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FA5")

    label("loc_1CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1CE5")

    #C0034
    ChrTalk(
        0xFE,
        (
            "今天要和爸爸\x01",
            "一起去看游行～\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "好期待哦～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FA5")

    label("loc_1CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1D55")

    #C0036
    ChrTalk(
        0xFE,
        (
            "演唱会好开心哦！\x01",
            "虽然有点晕乎乎的……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "不过呢，真的好棒哦！\x01",
            "就在舞台上，锵锵～¤地敲哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA5")

    label("loc_1D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1DC7")

    #C0038
    ChrTalk(
        0xFE,
        "（嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "我昨天也吃了爆米花，\x01",
            "可真好吃啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "竟然是用玉米做的，\x01",
            "真是难以置信～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA5")

    label("loc_1DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1FA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F67")

    #C0041
    ChrTalk(
        0xFE,
        (
            "啊，是罗伊德哥哥、艾莉姐姐、\x01",
            "缇欧姐姐和兰迪哥哥。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "今天是来逛纪念庆典的吗？\x01",
            "要不要和米米一起玩？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#0000F啊，谢谢你的邀请，\x01",
            "不过我们今天还有工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "哦～\x01",
            "特别任务试炼科还真是辛苦啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#0106F米、米米……\x01",
            "虽然你愿意记住我们的名字，\x01",
            "实在是很令人高兴……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#0200F特别任务试炼科……\x01",
            "嗯，的确是个有很多试炼的科，\x01",
            "这点倒也无法否认呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0306F这一点都不好笑啊，\x01",
            "阿缇……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FA5")

    label("loc_1F67")


    #C0048
    ChrTalk(
        0xFE,
        (
            "我等下\x01",
            "要和爸爸一起\x01",
            "去逛各种店。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "你们工作要加油哦～\x02",
    )

    CloseMessageWindow()

    label("loc_1FA5")

    TalkEnd(0xFE)
    Return()

    # Function_10_1980 end

    def Function_11_1FA9(): pass

    label("Function_11_1FA9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2084")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_203B")

    #C0050
    ChrTalk(
        0xFE,
        (
            "今天要在欢乐街玩过之后，\x01",
            "再去逛港湾公园的露天店，\x01",
            "晚上去米修拉姆看烟花。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "纪念庆典就要开开心心地玩到底呢～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_207F")

    label("loc_203B")


    #C0052
    ChrTalk(
        0xFE,
        "今天计划和家人一起逛街。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "纪念庆典就要开开心心地玩到底呢～\x02",
    )

    CloseMessageWindow()

    label("loc_207F")

    Jump("loc_230D")

    label("loc_2084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_20D5")

    #C0054
    ChrTalk(
        0xFE,
        "游行真是不错呢。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "嗯嗯，今年的\x01",
            "纪念庆典也玩得心满意足呢¤\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230D")

    label("loc_20D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2192")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2147")

    #C0056
    ChrTalk(
        0xFE,
        "呼，一大早就吃得饱饱的。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "看来，想在纪念庆典期间\x01",
            "逛完所有的露天店是不可能了～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_218D")

    label("loc_2147")


    #C0058
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔全市\x01",
            "好像到处都有露天店。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "全部逛完\x01",
            "真是不可能啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218D")

    Jump("loc_230D")

    label("loc_2192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_21FC")

    #C0060
    ChrTalk(
        0xFE,
        (
            "刚才撞到了一个游客，\x01",
            "果汁都洒到衣服上了！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "呜～不赶快回去换衣服的话，\x01",
            "就洗不掉了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230D")

    label("loc_21FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2264")

    #C0062
    ChrTalk(
        0xFE,
        (
            "昨晚我留宿在朋友家，\x01",
            "玩了一晚上丢枕头大战呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "呼～好开心啊。\x01",
            "纪念庆典太棒了～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230D")

    label("loc_2264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_230D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E4")

    #C0064
    ChrTalk(
        0xFE,
        (
            "（嚼嚼）……\x01",
            "港湾公园那边\x01",
            "也多了好多露天店哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "有空的话，不如去看看吧？\x01",
            "这个东西很好吃呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_230D")

    label("loc_22E4")


    #C0066
    ChrTalk(
        0xFE,
        (
            "（嚼嚼）……\x01",
            "接下来要去哪里逛呢～¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_230D")

    TalkEnd(0xFE)
    Return()

    # Function_11_1FA9 end

    def Function_12_2311(): pass

    label("Function_12_2311")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23A5")
    Jump("loc_23EF")

    label("loc_23A5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23C5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23EF")

    label("loc_23C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23E5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23EF")

    label("loc_23E5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23EF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_254B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D0")

    #C0067
    ChrTalk(
        0xFE,
        (
            "在米修拉姆疗养地，\x01",
            "每年的最终日都会有\x01",
            "盛大的烟火表演。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "去年我也在米修拉姆\x01",
            "度过了纪念庆典的最终日……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "那可是平时的夜场\x01",
            "完全无法比拟的\x01",
            "美丽光景哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2546")

    label("loc_24D0")


    #C0070
    ChrTalk(
        0xFE,
        (
            "难得的纪念庆典，\x01",
            "年轻人还在这种地方\x01",
            "摸什么鱼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "还不如去米修拉姆\x01",
            "看看纪念庆典最终日限定的\x01",
            "盛大烟火表演呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2546")

    Jump("loc_282B")

    label("loc_254B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_25E4")

    #C0072
    ChrTalk(
        0xFE,
        (
            "今年的游行队伍\x01",
            "好像比去年长了一点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "似乎是想多花点时间，\x01",
            "让更多市民都能看到吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "今年的纪念庆典或许是\x01",
            "最花心血的活动了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282B")

    label("loc_25E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2670")

    #C0075
    ChrTalk(
        0xFE,
        (
            "我去看了游行\x01",
            "使用的车辆。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "今年比去年还多一辆，\x01",
            "要用七辆导力车\x01",
            "顺着预定路线游行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "一定会是一场\x01",
            "豪华的游行吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282B")

    label("loc_2670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_26ED")

    #C0078
    ChrTalk(
        0xFE,
        "呵呵，玩得很开心吧？\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "就算有工作，也要好好享受，不然可就吃亏了。\x01",
            "因为这可是一年一度的创立纪念庆典啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282B")

    label("loc_26ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2760")

    #C0080
    ChrTalk(
        0xFE,
        (
            "话说回来，今年的\x01",
            "纪念庆典比往年更豪华呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "这也表示\x01",
            "克洛斯贝尔的经济状况\x01",
            "一年更比一年好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282B")

    label("loc_2760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_282B")

    #C0082
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长在昨天的\x01",
            "开幕式中上台演讲了……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "听说他经历了暗杀事件，犯人还是自己的秘书，\x01",
            "不过似乎比想象中要精神不少，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "不服老、不妥协、\x01",
            "意志坚定，\x01",
            "这才是麦克道尔市长啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_282B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_2311 end

    def Function_13_2833(): pass

    label("Function_13_2833")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2889")

    #C0085
    ChrTalk(
        0xFE,
        (
            "总算把露天店铺\x01",
            "全都逛遍了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "……我现在都不敢站上体重秤了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A3A")

    label("loc_2889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_28E1")

    #C0087
    ChrTalk(
        0xFE,
        (
            "嗯～虽然冰激凌\x01",
            "也相当不错……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "不过我还是\x01",
            "更喜欢那边的爆米花呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3A")

    label("loc_28E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_294D")

    #C0089
    ChrTalk(
        0xFE,
        (
            "那个～你觉得在之前逛过的露天店中，\x01",
            "哪家卖的小吃最美味？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "我觉得还是\x01",
            "那边的汉堡包吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3A")

    label("loc_294D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2999")

    #C0091
    ChrTalk(
        0xFE,
        (
            "……我说，这种\x01",
            "热闹的活动，\x01",
            "还是和男朋友一起逛比较好吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3A")

    label("loc_2999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_29EA")

    #C0092
    ChrTalk(
        0xFE,
        "（嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "……啊～一直逛露天店吃小吃，\x01",
            "一定会长胖啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3A")

    label("loc_29EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2A3A")

    #C0094
    ChrTalk(
        0xFE,
        "我说，接下来去哪里？\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "光是在中央广场晃悠，\x01",
            "感觉也有点腻烦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3A")

    TalkEnd(0xFE)
    Return()

    # Function_13_2833 end

    def Function_14_2A3E(): pass

    label("Function_14_2A3E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A96")

    #C0096
    ChrTalk(
        0xFE,
        "嗯～有同感。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "但是，我觉得不面对现实，\x01",
            "继续胖下去才更恐怖啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2A")

    label("loc_2A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2AF5")

    #C0098
    ChrTalk(
        0xFE,
        (
            "喂，你刚才\x01",
            "不是说汉堡包\x01",
            "最好吃吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "可是啊，我还是觉得\x01",
            "冰激凌最好吃～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2A")

    label("loc_2AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2B54")

    #C0100
    ChrTalk(
        0xFE,
        "哎～！？肯定是冰激凌更好吧！\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "……好吧，等下\x01",
            "去吃了两样后再来比较吧～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2A")

    label("loc_2B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2B86")

    #C0102
    ChrTalk(
        0xFE,
        "……我们不是说好不提这个的吗～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C2A")

    label("loc_2B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2BDE")

    #C0103
    ChrTalk(
        0xFE,
        (
            "没事没事，\x01",
            "等纪念庆典结束以后\x01",
            "再减肥就好啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "现在要尽情享受嘛～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C2A")

    label("loc_2BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2C2A")

    #C0105
    ChrTalk(
        0xFE,
        "对了，要不要去港湾区看看？\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "听说从昨天开始\x01",
            "就有演唱会哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2A")

    TalkEnd(0xFE)
    Return()

    # Function_14_2A3E end

    def Function_15_2C2E(): pass

    label("Function_15_2C2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C95")

    #C0107
    ChrTalk(
        0xFE,
        (
            "纪念庆典用的气球存货，\x01",
            "今天要是能全部发完就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "全部发完的话\x01",
            "会有奖金呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF0")

    label("loc_2C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2D1A")

    #C0109
    ChrTalk(
        0xFE,
        (
            "哎呀……想着\x01",
            "飞上天的气球会到哪里去，\x01",
            "一不小心就发呆了。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "……嗯，按照常识来考虑，\x01",
            "应该是漏光气之后掉下来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF0")

    label("loc_2D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2DF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DAD")

    #C0111
    ChrTalk(
        0xFE,
        (
            "偶尔能看到我发出去的气球\x01",
            "飞到天上去。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "飞呀飞呀……\x01",
            "最后能不能飞到女神那里去呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "真是有些寂寥的光景呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2DF0")

    label("loc_2DAD")


    #C0114
    ChrTalk(
        0xFE,
        (
            "偶尔会看到气球\x01",
            "向着蓝天飞去。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "能不能飞到女神那里去呢……\x02",
    )

    CloseMessageWindow()

    label("loc_2DF0")

    Jump("loc_2EF0")

    label("loc_2DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2E2F")

    #C0116
    ChrTalk(
        0xFE,
        "气球，气球～\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "很好玩哦～会飞的哟～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF0")

    label("loc_2E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E89")

    #C0118
    ChrTalk(
        0xFE,
        (
            "啧，怎么全都\x01",
            "成双成对的。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "拿上我的气球，\x01",
            "分开那双黏在一起的手啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF0")

    label("loc_2E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2EF0")

    #C0120
    ChrTalk(
        0xFE,
        "来哟～瞧一瞧、看一看！有气球哦～\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间，\x01",
            "打工费也增加了。\x01",
            "这下我可有干劲了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF0")

    TalkEnd(0xFE)
    Return()

    # Function_15_2C2E end

    def Function_16_2EF4(): pass

    label("Function_16_2EF4")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3530")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F51")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2F51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F71")
    OP_AF(0x7A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_352B")

    label("loc_2F71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F85")
    Jump("loc_352B")

    label("loc_2F85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_352B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_321D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B5")

    #C0122
    ChrTalk(
        0x101,
        (
            "#0001F打扰一下，请问\x01",
            "可以向您打听一些事吗？\x02\x03",

            "我们正在进行\x01",
            "盗窃案的调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "啊……听说各处的露天店\x01",
            "都遇窃了？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "我这里应该没事。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "因为就在中央广场的正中央啊！\x01",
            "这里的客人这么多，\x01",
            "谁也下不了手的！\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x103,
        (
            "#0200F不，各位游客也未必会\x01",
            "特意注意露天店的情况。\x02\x03",

            "而且犯人反而很有可能\x01",
            "混进人群中。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "没关系啦，绝对没事。\x01",
            "放心吧！\x02",
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
    Sleep(1200)

    #C0128
    ChrTalk(
        0x102,
        "#0104F（这位店主还真是有点让人担心……）\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x7)
    Jump("loc_3218")

    label("loc_31B5")


    #C0129
    ChrTalk(
        0xFE,
        "听说中央广场也有一家露天店遭窃了呢。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "好像是那家靠近东街的露天店，\x01",
            "大概是因为不够警觉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3218")

    Jump("loc_352B")

    label("loc_321D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3230")
    Call(0, 17)
    Jump("loc_352B")

    label("loc_3230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3297")

    #C0131
    ChrTalk(
        0xFE,
        (
            "要不要来点\x01",
            "口感松脆的爆米花？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "我打算乘\x01",
            "今天的末班车回去了，\x01",
            "要买的话请趁早哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_352B")

    label("loc_3297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_32F9")

    #C0133
    ChrTalk(
        0xFE,
        (
            "哎呀呀……带来的材料\x01",
            "都用完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "那边正好有百货店，\x01",
            "稍后得去采购一点才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_352B")

    label("loc_32F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3406")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_337F")

    #C0135
    ChrTalk(
        0xFE,
        "听说终于抓到窃贼了呢！\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "哼，做坏事果然\x01",
            "会遭到天谴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "那么想要米拉的话，\x01",
            "不如自己去做生意呀！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3401")

    label("loc_337F")


    #C0138
    ChrTalk(
        0xFE,
        (
            "这个国家的人们，\x01",
            "似乎花钱都挺大方的。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "之前在帝国做生意的时候，\x01",
            "那真是门可罗雀呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "呵，来克洛斯贝尔可真是来对了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3401")

    Jump("loc_352B")

    label("loc_3406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3474")

    #C0141
    ChrTalk(
        0xFE,
        (
            "如我所料，\x01",
            "完全没有\x01",
            "去观光的空闲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "呵，真是令人欢喜啊。\x01",
            "因为繁忙就代表\x01",
            "生意兴隆嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_352B")

    label("loc_3474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_34CE")

    #C0143
    ChrTalk(
        0xFE,
        (
            "香甜可口的\x01",
            "爆米花，卖得很不错哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "吃的时候，\x01",
            "请注意不要撒出来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_352B")

    label("loc_34CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_352B")

    #C0145
    ChrTalk(
        0xFE,
        (
            "美味可口的\x01",
            "爆米花，要不要来一份？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "这可是观赏戏剧或演唱会\x01",
            "时的最佳伴侣哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_352B")

    Jump("loc_2F01")

    label("loc_3530")

    TalkEnd(0xFE)
    Return()

    # Function_16_2EF4 end

    def Function_17_3534(): pass

    label("Function_17_3534")


    #C0147
    ChrTalk(
        0xFE,
        (
            "美味可口的\x01",
            "爆米花，要不要来一份？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "我的爆米花，\x01",
            "做法可是很讲究的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "所以才这么美味嘛。\x01",
            "你们也可以试试哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0150
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '轻快爆米花'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0151
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '轻快爆米花'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x14)
    Return()

    # Function_17_3534 end

    def Function_18_3619(): pass

    label("Function_18_3619")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3643")
    Call(0, 44)
    Return()

    label("loc_3643")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3650")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C00")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36A0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_36A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C0")
    OP_AF(0x78)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BFB")

    label("loc_36C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36D4")
    Jump("loc_3BFB")

    label("loc_36D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BFB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_375B")

    #C0152
    ChrTalk(
        0xFE,
        "你好像……是警察吧。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "我听说了……\x01",
            "你好像抓到了窃贼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A0")

    label("loc_375B")


    #C0154
    ChrTalk(
        0xFE,
        "你们好像……是警察吧。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "我听说了……\x01",
            "你们好像抓到了窃贼呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A0")


    #C0156
    ChrTalk(
        0xFE,
        (
            "真厉害呀……这下\x01",
            "我就能放心做生意了……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "不嫌弃的话，\x01",
            "请收下这个吧……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '双层汉堡'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('双层汉堡', 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3869")

    #C0159
    ChrTalk(
        0x101,
        "#0002F哈哈……十分感谢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_387D")

    label("loc_3869")


    #C0160
    ChrTalk(
        0x103,
        "#0203F谢谢您。\x02",
    )

    CloseMessageWindow()

    label("loc_387D")


    #C0161
    ChrTalk(
        0xFE,
        (
            "要道谢的是我……\x01",
            "真是谢谢了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBC, 6)
    Jump("loc_3BFB")

    label("loc_38AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3917")

    #C0162
    ChrTalk(
        0xFE,
        "汉堡包……很好吃哦。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "从某种程度上来说，保存也很方便，\x01",
            "不嫌弃的话……就请多买一点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BFB")

    label("loc_3917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3982")

    #C0164
    ChrTalk(
        0xFE,
        (
            "……最近，共和国那边\x01",
            "很流行长条三明治和\x01",
            "烤肉三明治呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "……可是我还是\x01",
            "喜欢汉堡包。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BFB")

    label("loc_3982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3AD3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_39D3")

    #C0166
    ChrTalk(
        0xFE,
        (
            "终于可以\x01",
            "放心做生意了……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "真是谢谢你们了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ACE")

    label("loc_39D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A72")

    #C0168
    ChrTalk(
        0xFE,
        (
            "我还是第一次\x01",
            "在这种大都市开露天店。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "遭窃的经历，\x01",
            "今天也是第一次呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "到底是在何时被偷的……\x01",
            "至今都还是个谜呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ACE")

    label("loc_3A72")


    #C0171
    ChrTalk(
        0xFE,
        "我在卖……汉堡包。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "制作一点也不困难，\x01",
            "如果觉得自己能行的话，\x01",
            "大可以试着做做看哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ACE")

    Jump("loc_3BFB")

    label("loc_3AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3B42")

    #C0173
    ChrTalk(
        0xFE,
        "克洛斯贝尔真是个繁荣的地方啊……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "连我这么不会揽客的人开露天店，\x01",
            "也都有这么多客人来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BFB")

    label("loc_3B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B9D")

    #C0175
    ChrTalk(
        0xFE,
        "要不要……来点汉堡包？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "……我不会强买强卖的，\x01",
            "有兴趣的话就来买吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BFB")

    label("loc_3B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3BFB")

    #C0177
    ChrTalk(
        0xFE,
        "吃不吃……汉堡包？\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "肉、蔬菜和碳水化合物的完美搭配……\x01",
            "是绝妙的快餐食品哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BFB")

    Jump("loc_3650")

    label("loc_3C00")

    TalkEnd(0xFE)
    Return()

    # Function_18_3619 end

    def Function_19_3C04(): pass

    label("Function_19_3C04")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44BD")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C61")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3C61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C81")
    OP_AF(0x79)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44B8")

    label("loc_3C81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C95")
    Jump("loc_44B8")

    label("loc_3C95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44B8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EF7")

    #C0179
    ChrTalk(
        0xFE,
        (
            "哎呀，这不是刚才\x01",
            "帮了我忙的警察吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "之前真是谢谢了。\x01",
            "多亏你们，才免遭盗窃啊⊥\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D85")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_3D60")

    #C0181
    ChrTalk(
        0x101,
        "#0002F哈哈，刚才可真险啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D80")

    label("loc_3D60")


    #C0182
    ChrTalk(
        0x101,
        "#0012F哈哈，刚才可真险啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3D80")

    Jump("loc_3DFF")

    label("loc_3D85")


    #C0183
    ChrTalk(
        0x101,
        "#0000F哈哈，刚才好险。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_3DDF")

    #C0184
    ChrTalk(
        0x104,
        "#0304F不过，一切都在我们的预料之中啦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DFF")

    label("loc_3DDF")


    #C0185
    ChrTalk(
        0x104,
        "#0303F正所谓大意必有失啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3DFF")


    #C0186
    ChrTalk(
        0xFE,
        (
            "这个，请拿去吧～\x01",
            "算是一点谢礼啦⊥\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0187
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天上甜点『夜月』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('天上甜点『夜月』', 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EA4")

    #C0188
    ChrTalk(
        0x101,
        (
            "#0000F谢谢您，\x01",
            "那就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC6")

    label("loc_3EA4")


    #C0189
    ChrTalk(
        0x102,
        "#0100F谢谢，我们就不客气了。\x02",
    )

    CloseMessageWindow()

    label("loc_3EC6")


    #C0190
    ChrTalk(
        0xFE,
        (
            "呵呵，警察好像\x01",
            "也在很努力地工作呢⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 0)
    Jump("loc_44B8")

    label("loc_3EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3F69")

    #C0191
    ChrTalk(
        0xFE,
        (
            "唉唉，好失落啊。\x01",
            "庆典竟然在今天就要结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "明年我还会来开露天甜品店的，\x01",
            "可不要忘了我哦⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44B8")

    label("loc_3F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3FCD")

    #C0193
    ChrTalk(
        0xFE,
        "低卡路里那是幻想啦。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "即使如此，\x01",
            "如果真正喜欢甜食的话，\x01",
            "还是会忍不住要吃呢⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44B8")

    label("loc_3FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4370")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4035")

    #C0195
    ChrTalk(
        0xFE,
        (
            "刚才真是谢谢了。\x01",
            "多亏你们，才免遭盗窃啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "警察还真是\x01",
            "意外地可靠呢⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436B")

    label("loc_4035")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4320")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4285")

    #C0197
    ChrTalk(
        0x101,
        (
            "#0001F打扰一下，请问\x01",
            "能向您打听一些事吗？\x02\x03",

            "我们正在进行\x01",
            "盗窃案的调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "哦，盗窃案啊～\x01",
            "工商协会的人之前来过，\x01",
            "还提醒我们多加注意呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x104,
        (
            "#0300F听说中央广场也遇窃了。\x02\x03",

            "您有没有什么线索啊？\x01",
            "比如目击到逃跑的犯人什么的。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "没有呢～⊥\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "我这里的生意十分兴隆嘛。\x01",
            "一直忙着做生意，\x01",
            "根本顾不上其它露天店啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#0006F是、是吗……\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0xFFFFFF2E, 0x56C2, 0x1F4)
    Sleep(500)
    OP_92(0x101, 0xFFFFCC16, 0x36BA, 0x1F4)
    Sleep(500)

    #C0203
    ChrTalk(
        0x101,
        (
            "#0008F的确，这里就在百货店之前，\x01",
            "又紧挨着后巷……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "而且那边的路\x01",
            "还通往行政区呢～⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "今天来了好多\x01",
            "观看游行的客人呢～⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        "#0103F看、看来还真是忙碌啊。\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x8)
    Jump("loc_431B")

    label("loc_4285")


    #C0207
    ChrTalk(
        0xFE,
        "我没有关于盗窃犯的线索呢～\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "他要是敢来的话，就尽管来吧。\x01",
            "这样的话，我就可以把他抓住了⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#0006F嗯～但民间人士最好还是\x01",
            "不要太勉强行事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_431B")

    Jump("loc_436B")

    label("loc_4320")


    #C0210
    ChrTalk(
        0xFE,
        "要不要来点香甜可口的甜点？\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "最适合逛庆典逛累时，\x01",
            "吃些恢复体力哦⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_436B")

    Jump("loc_44B8")

    label("loc_4370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_43EA")

    #C0212
    ChrTalk(
        0xFE,
        (
            "虽然我开着这样的露天店，\x01",
            "不过我个人倒是更喜欢\x01",
            "比较淡的甜味。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "太甜的点心还是有点那个什么……是吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_44B8")

    label("loc_43EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_443F")

    #C0214
    ChrTalk(
        0xFE,
        (
            "客人中果然\x01",
            "还是女孩子\x01",
            "比较多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "女孩子大多\x01",
            "都很喜欢甜食嘛⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44B8")

    label("loc_443F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_44B8")

    #C0216
    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "欢迎光临露天甜品店⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "……哎呀，男女四人……\x01",
            "莫非就是所谓的双对约会？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "姐姐我好羡慕哦～⊥\x02",
    )

    CloseMessageWindow()

    label("loc_44B8")

    Jump("loc_3C11")

    label("loc_44BD")

    TalkEnd(0xFE)
    Return()

    # Function_19_3C04 end

    def Function_20_44C1(): pass

    label("Function_20_44C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_44D2")
    Jump("loc_4569")

    label("loc_44D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4505")

    #C0219
    ChrTalk(
        0xFE,
        (
            "欢迎光临～！\x01",
            "要不要吃点什么～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4569")

    label("loc_4505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4560")

    #C0220
    ChrTalk(
        0xFE,
        (
            "您好～！\x01",
            "要不要吃点什么～？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "我也开始\x01",
            "试着揽客了，\x01",
            "因为正是旺季嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4569")

    label("loc_4560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4569")

    label("loc_4569")

    TalkEnd(0xFE)
    Return()

    # Function_20_44C1 end

    def Function_21_456D(): pass

    label("Function_21_456D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_46B2")
    OP_93(0xFE, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4648")
    OP_4B(0x14, 0xFF)

    #C0222
    ChrTalk(
        0xFE,
        (
            "哎～去米修拉姆吧，\x01",
            "米修拉姆～！\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "住在酒店里，\x01",
            "然后去主题公园玩吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x14,
        (
            "笨、笨蛋，\x01",
            "你知道米修拉姆的\x01",
            "酒店有多贵吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x14,
        (
            "今天要看闭幕式。\x01",
            "隆，你可不要\x01",
            "东跑西窜哦！？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    SetScenarioFlags(0x0, 6)
    Jump("loc_46AD")

    label("loc_4648")


    #C0226
    ChrTalk(
        0xFE,
        (
            "呸呸～闭幕式什么的\x01",
            "实在太无聊啦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "不如叫上姐姐一起\x01",
            "去米修拉姆吧，\x01",
            "好不好嘛，老爸～……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46AD")

    Jump("loc_4C1B")

    label("loc_46B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_4772")
    OP_93(0xFE, 0x5A, 0x0)
    OP_4B(0x14, 0xFF)

    #C0228
    ChrTalk(
        0xFE,
        (
            "我说，老爸，\x01",
            "给我买那个啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "还有果汁和爆米花！\x01",
            "嘿嘿，反正是庆典嘛～！\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x14,
        "哇哈哈，那可真不错……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x14,
        (
            "……才怪，你也太得意忘形了吧！\x01",
            "不会给我客气点吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_4C1B")

    label("loc_4772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4A41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_495F")

    #C0232
    ChrTalk(
        0x101,
        (
            "#0003F（姑且也问问\x01",
            "  隆吧……）\x02\x03",

            "#0000F打扰一下好吗？\x01",
            "我在找一个小男孩……\x02",
        )
    )

    CloseMessageWindow()

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0234
    ChrTalk(
        0xFE,
        "哦～这小子走丢了？\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "这么说来，好像见过，\x01",
            "又好像没见过……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x160,
        (
            "#3306F真是含糊不清呢。\x02\x03",

            "#3300F嘻……是男子汉的话，\x01",
            "就应该干脆一点吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        "呃……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0238
    ChrTalk(
        0xFE,
        (
            "这、这么说来，\x01",
            "好像是瞄到过一眼啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "我当时正在专心看游行呢，\x01",
            "没太注意什么小孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "谢谢，帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 36)
    Jump("loc_4A3C")

    label("loc_495F")


    #C0241
    ChrTalk(
        0xFE,
        (
            "虽然我专心看游行，\x01",
            "没怎么注意，\x01",
            "不过好像看见过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "……对了，\x01",
            "这个女的是谁啊～？\x01",
            "感觉好嚣张啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x160,
        (
            "#3302F嘻嘻……对淑女\x01",
            "这样说话，\x01",
            "是不是不太好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#0012F（哈哈……\x01",
            "  对隆来说，这对手未免太强大了吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A3C")

    Jump("loc_4C1B")

    label("loc_4A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4AA4")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0245
    ChrTalk(
        0xFE,
        (
            "哟哟……\x01",
            "真是太棒啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "嘿嘿，要是姐姐\x01",
            "也来看就好了～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C1B")

    label("loc_4AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4AF6")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0247
    ChrTalk(
        0xFE,
        (
            "噢噢噢～……\x01",
            "游行队伍怎么还不快点来呀～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C1B")

    label("loc_4AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4B59")
    OP_93(0xFE, 0x0, 0x0)

    #C0248
    ChrTalk(
        0xFE,
        (
            "那个～爸爸，\x01",
            "去百货店吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "即使是客户也无所谓吧！\x01",
            "就当是市场调查啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C1B")

    label("loc_4B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4B97")
    OP_93(0xFE, 0x0, 0x0)

    #C0250
    ChrTalk(
        0xFE,
        (
            "啊，百货店在打折。\x01",
            "爸爸，去看看啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C1B")

    label("loc_4B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4C1B")

    #C0251
    ChrTalk(
        0xFE,
        "啊，是支援科的哥哥姐姐。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "庆典时还要巡逻吗。\x01",
            "嘿嘿，好可惜啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#0000F是是。\x01",
            "……对了，你可别\x01",
            "玩得太过火哦？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C1B")

    TalkEnd(0xFE)
    Return()

    # Function_21_456D end

    def Function_22_4C1F(): pass

    label("Function_22_4C1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4C7E")

    #C0254
    ChrTalk(
        0xFE,
        (
            "今天下午\x01",
            "有庆典闭幕式。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "作为市民，可得去看看\x01",
            "最后的收尾啊，哇哈哈！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DDA")

    label("loc_4C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4CDE")

    #C0256
    ChrTalk(
        0xFE,
        "哇哈哈，庆典真不错啊。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "游行就是\x01",
            "克洛斯贝尔人的心灵写照啊，\x01",
            "哇哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DDA")

    label("loc_4CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4D39")

    #C0258
    ChrTalk(
        0xFE,
        (
            "隆，等游行的车子过来时，\x01",
            "要摆个Ｖ字手势哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "我给你拍照片，哇哈哈！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DDA")

    label("loc_4D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4D6F")
    OP_93(0xFE, 0x0, 0x0)

    #C0260
    ChrTalk(
        0xFE,
        (
            "……隆，你还知道\x01",
            "这种词啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DDA")

    label("loc_4D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4DB7")
    OP_93(0xFE, 0x0, 0x0)

    #C0261
    ChrTalk(
        0xFE,
        (
            "唔……我可不想在庆典期间\x01",
            "还去客户那里露面啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DDA")

    label("loc_4DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4DDA")

    #C0262
    ChrTalk(
        0xFE,
        "哇哈哈，真是难得啊！\x02",
    )

    CloseMessageWindow()

    label("loc_4DDA")

    TalkEnd(0xFE)
    Return()

    # Function_22_4C1F end

    def Function_23_4DDE(): pass

    label("Function_23_4DDE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E36")

    #C0263
    ChrTalk(
        0xFE,
        (
            "温蒂就在这附近的\x01",
            "店里工作吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        "机会难得，不如去看看她吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4E5D")

    label("loc_4E36")


    #C0265
    ChrTalk(
        0xFE,
        (
            "来～让我看看女儿\x01",
            "工作时的英姿吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E5D")

    TalkEnd(0xFE)
    Return()

    # Function_23_4DDE end

    def Function_24_4E61(): pass

    label("Function_24_4E61")

    TalkBegin(0xFE)

    #C0266
    ChrTalk(
        0xFE,
        "哎～我想去百货店～！\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "姐姐的工作情况\x01",
            "随时都可以来看啊～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_4E61 end

    def Function_25_4EA9(): pass

    label("Function_25_4EA9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F2A")
    OP_4B(0x18, 0xFF)

    #C0268
    ChrTalk(
        0xFE,
        (
            "呀～梅菲尔，快看快看，\x01",
            "有露天店哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "我想吃那个～！\x01",
            "给我买吧！给我买吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x18,
        "你自己买啦！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x18, 0xFF)
    Jump("loc_4F4D")

    label("loc_4F2A")


    #C0271
    ChrTalk(
        0xFE,
        (
            "我说，梅菲尔，\x01",
            "给我买那个啦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F4D")

    TalkEnd(0xFE)
    Return()

    # Function_25_4EA9 end

    def Function_26_4F51(): pass

    label("Function_26_4F51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE9")
    TurnDirection(0xFE, 0x0, 0)

    #C0272
    ChrTalk(
        0xFE,
        (
            "因为放了假，\x01",
            "就从乌尔斯拉医院过来玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "在日复一日的护士生活中\x01",
            "积下的层层疲劳……\x01",
            "要在今天一天内全部抛开！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x87, 0x0)
    SetScenarioFlags(0x1, 1)
    Jump("loc_5055")

    label("loc_4FE9")


    #C0274
    ChrTalk(
        0xFE,
        (
            "……啊～真是的，吵死啦！\x01",
            "不要像个小孩子似地欢闹啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "真是的，难得的假日，\x01",
            "为什么还要照顾希伦啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5055")

    TalkEnd(0xFE)
    Return()

    # Function_26_4F51 end

    def Function_27_5059(): pass

    label("Function_27_5059")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5122")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50BF")

    #C0276
    ChrTalk(
        0xFE,
        (
            "车站那边有游击士\x01",
            "在帮忙巡逻。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "……果然……\x01",
            "游击士真是可靠啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_511D")

    label("loc_50BF")


    #C0278
    ChrTalk(
        0xFE,
        (
            "游击士办事牢靠，本领高超，\x01",
            "也很关心市民……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "果然很可靠啊。\x01",
            "身为警察，心情有点复杂。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_511D")

    Jump("loc_5453")

    label("loc_5122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5130")
    Jump("loc_5453")

    label("loc_5130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_513E")
    Jump("loc_5453")

    label("loc_513E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5199")
    OP_93(0xFE, 0xC5, 0x0)

    #C0280
    ChrTalk(
        0xFE,
        (
            "哔哔～哔哔～！\x01",
            "导力车请慢行～\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "挡在路中间的行人\x01",
            "请让个路～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5453")

    label("loc_5199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5453")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5228")

    #C0282
    ChrTalk(
        0xFE,
        "啊，辛苦了～\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "虽然比不上\x01",
            "有开幕式的第一天……\x01",
            "不过人还是很多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "看来，还是拜托\x01",
            "总部来支援比较好吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5453")

    label("loc_5228")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_53DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_52CF")

    #C0285
    ChrTalk(
        0x19,
        (
            "车辆似乎都集中\x01",
            "停在西出口和东出口。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x19,
        (
            "调查完所有的车辆以后，\x01",
            "请向总部接待处的\x01",
            "瑞贝卡小姐报告哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x19,
        (
            "我们……实在忙得\x01",
            "脱不开身呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53D9")

    label("loc_52CF")


    #C0288
    ChrTalk(
        0x19,
        (
            "取缔违章停车那件事\x01",
            "本来应该由我们\x01",
            "新警官去做的……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x19,
        "可是我们都很忙……抱歉哦。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，没关系。\x01",
            "我们会完成的。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x19,
        "谢谢，还有……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x19,
        (
            "贴在车辆上的警告标志，\x01",
            "一旦贴上去就很难撕下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x19,
        (
            "一定注意\x01",
            "不要贴错哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        "#0300F明白，包在我们身上！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_53D9")

    Jump("loc_5453")

    label("loc_53DE")


    #C0295
    ChrTalk(
        0xFE,
        "啊，辛苦了～\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "虽然比不上\x01",
            "有开幕式的第一天……\x01",
            "不过人还是很多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "看来，还是拜托\x01",
            "总部来支援比较好吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5453")

    TalkEnd(0xFE)
    Return()

    # Function_27_5059 end

    def Function_28_5457(): pass

    label("Function_28_5457")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_54C8")

    #C0298
    ChrTalk(
        0xFE,
        (
            "好像还有许多好玩的地方，\x01",
            "所以我就把滞留期间延长了四天。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "这下就能悠～闲地\x01",
            "尽情游玩啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CF")

    label("loc_54C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_551F")

    #C0300
    ChrTalk(
        0xFE,
        (
            "毫无计划地四处游览，\x01",
            "结果就完全失去头绪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        "今天要去做什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_55CF")

    label("loc_551F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_558A")

    #C0302
    ChrTalk(
        0xFE,
        (
            "我昨天去了\x01",
            "热闹的港湾区呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "虽然不良团伙的那些人\x01",
            "品行恶劣，不过也\x01",
            "还挺有一套的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CF")

    label("loc_558A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_55CF")

    #C0304
    ChrTalk(
        0xFE,
        "我是和女友来度蜜月的～\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        "希望能留下许多美好回忆啊。\x02",
    )

    CloseMessageWindow()

    label("loc_55CF")

    TalkEnd(0xFE)
    Return()

    # Function_28_5457 end

    def Function_29_55D3(): pass

    label("Function_29_55D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_562E")

    #C0306
    ChrTalk(
        0xFE,
        (
            "虽然延长了一点……\x01",
            "不过这也是一生一次的蜜月嘛，\x01",
            "希望能多享受一下呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56C9")

    label("loc_562E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5663")

    #C0307
    ChrTalk(
        0xFE,
        (
            "真是的，所以我才说\x01",
            "要跟团的嘛……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56C9")

    label("loc_5663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5695")

    #C0308
    ChrTalk(
        0xFE,
        "男人就是喜欢这种胡闹的游戏啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_56C9")

    label("loc_5695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_56C9")

    #C0309
    ChrTalk(
        0xFE,
        (
            "呵呵，好期待呀，\x01",
            "我早就想来这里了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56C9")

    TalkEnd(0xFE)
    Return()

    # Function_29_55D3 end

    def Function_30_56CD(): pass

    label("Function_30_56CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_572A")

    #C0310
    ChrTalk(
        0xFE,
        (
            "啊啊，回程的列车\x01",
            "马上就要开了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "可我还想……\x01",
            "还想再看看这城市！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5863")

    label("loc_572A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_57A7")

    #C0312
    ChrTalk(
        0xFE,
        (
            "导力商店！\x01",
            "那里真是令人耳目一新！\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "那么多品种的导力器\x01",
            "典雅地陈列在橱窗里的样子，\x01",
            "只能说是精彩绝伦啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5863")

    label("loc_57A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_580D")

    #C0314
    ChrTalk(
        0xFE,
        (
            "百货店！\x01",
            "那里简直太棒了！\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "我见过各国的商店，\x01",
            "但这么大规模的却还是头一次见呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5863")

    label("loc_580D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5863")

    #C0316
    ChrTalk(
        0xFE,
        "有好多新奇的商店啊。\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "让人看得目不暇接，\x01",
            "都不知道该逛哪家店才好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5863")

    TalkEnd(0xFE)
    Return()

    # Function_30_56CD end

    def Function_31_5867(): pass

    label("Function_31_5867")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_58EF")

    #C0318
    ChrTalk(
        0xFE,
        (
            "好吧……克洛斯贝尔的餐厅\x01",
            "也基本都转了个遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "那么，接下来该怎么办呢。\x01",
            "要不要去那传说中的\x01",
            "米修拉姆看看呢……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A78")

    label("loc_58EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5992")

    #C0320
    ChrTalk(
        0xFE,
        (
            "我去了东街那家\x01",
            "东方风味的餐厅……哎呀，真是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "我真是做梦都没想到\x01",
            "能吃到那么正宗的美食啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "呼呼……光是想想，\x01",
            "就忍不住要流口水了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A78")

    label("loc_5992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_59FB")

    #C0323
    ChrTalk(
        0xFE,
        (
            "我昨天也在这里用过餐……\x01",
            "哎呀，真是相当美味啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        "接下来，要不要去吃点快餐食品呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A78")

    label("loc_59FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5A78")

    #C0325
    ChrTalk(
        0xFE,
        (
            "各种文化融合交汇的\x01",
            "克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        (
            "在这里，说不定能遇上\x01",
            "令我心满意足的料理啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        "好，赶快去探寻美食吧。\x02",
    )

    CloseMessageWindow()

    label("loc_5A78")

    TalkEnd(0xFE)
    Return()

    # Function_31_5867 end

    def Function_32_5A7C(): pass

    label("Function_32_5A7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5AA9")

    #C0328
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C73")

    label("loc_5AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5AB7")
    Jump("loc_5C73")

    label("loc_5AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5AE1")

    #C0329
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C73")

    label("loc_5AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5B0B")

    #C0330
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C73")

    label("loc_5B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5C73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C24")

    #C0331
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#0202F（抚摸）……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x102,
        "#0102F（抚摸）……\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#0000F嗯～真是和平啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0335
    ChrTalk(
        0x104,
        (
            "#0306F为什么一来到这里，\x01",
            "大家就全都进入发呆模式了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x103,
        (
            "#0204F没办法，\x01",
            "正在晒太阳的蔡特，\x01",
            "身上的毛都松松软软的嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C73")

    label("loc_5C24")


    #C0337
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x103,
        (
            "#0202F（稍后去给它\x01",
            "  买点带骨头的肉来吧……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C73")

    TalkEnd(0xFE)
    Return()

    # Function_32_5A7C end

    def Function_33_5C77(): pass

    label("Function_33_5C77")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x1, 3)
    Call(0, 35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CF5")

    #C0339
    ChrTalk(
        0x101,
        (
            "#0004F（这么说来……\x01",
            "  好像有些东西可以当猫食嘛。）\x02\x03",

            "#0000F（说不定可以拿来\x01",
            "  喂柯贝呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x52, 0)

    label("loc_5CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E14")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E0F")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "对话")
    MenuCmd(1, 1, "喂食")
    MenuCmd(1, 1, "放弃")
    ClearScenarioFlags(0x1, 3)
    Call(0, 35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DB2")
    MenuCmd(3, 1, 0x1)

    label("loc_5DB2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DE4")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5DE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DDA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5E1F")
    MenuCmd(1, 1, "雪花蟹")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5E1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_5E46")
    MenuCmd(1, 1, "阿尔摩利卡鲫鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5E46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5E65")
    MenuCmd(1, 1, "橙河鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5E65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5E84")
    MenuCmd(1, 1, "岩穴鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5E84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5EA1")
    MenuCmd(1, 1, "鲤鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_5EC0")
    MenuCmd(1, 1, "冷水鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5EE3")
    MenuCmd(1, 1, "蓝带神仙鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5F02")
    MenuCmd(1, 1, "银伞鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5F21")
    MenuCmd(1, 1, "虹鳟鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5F3E")
    MenuCmd(1, 1, "黑鲑")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5F5B")
    MenuCmd(1, 1, "鲑鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5F78")
    MenuCmd(1, 1, "鳗鲡")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F78")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_5F97")
    MenuCmd(1, 1, "珍珠草")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5FB8")
    MenuCmd(1, 1, "大口鲈鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5FB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5FD9")
    MenuCmd(1, 1, "云斑蛇头")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5FD9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_5FFA")
    MenuCmd(1, 1, "暗纹蛇鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5FFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6017")
    MenuCmd(1, 1, "巨鲶")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6017")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6036")
    MenuCmd(1, 1, "巨血蟹")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6036")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_6053")
    MenuCmd(1, 1, "电鳗")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6053")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_6074")
    MenuCmd(1, 1, "魔鬼巨鲶")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6074")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_6093")
    MenuCmd(1, 1, "弧光蟹")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6093")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_60B0")
    MenuCmd(1, 1, "金鲑")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_60B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_60CD")
    MenuCmd(1, 1, "锦鲤")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_60CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_60EE")
    MenuCmd(1, 1, "霸王蛇鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_60EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_610B")
    MenuCmd(1, 1, "猫食")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_610B")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6153")
    Jump("loc_6DCB")

    label("loc_6153")

    EventBegin(0x1)
    Fade(500)
    SetChrPos(0x1F, -21980, 1300, -19300, 270)
    SetChrPos(0x0, -23900, 1300, -19070, 89)
    SetChrPos(0x1, -23540, 1300, -20210, 89)
    SetChrPos(0x2, -25020, 1300, -19860, 89)
    SetChrPos(0x3, -25130, 1300, -18930, 89)
    SetChrPos(0x4, -26200, 1300, -19870, 89)
    SetChrPos(0x5, -26790, 1300, -19180, 89)
    OP_68(-23130, 3900, -19610, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    #C0340
    ChrTalk(
        0xFE,
        "喵喵……⊥\x02",
    )

    CloseMessageWindow()

    def lambda_6215():

        label("loc_6215")

        TurnDirection(0x0, 0x1F, 0)
        Yield()
        Jump("loc_6215")

    QueueWorkItem2(0x0, 1, lambda_6215)

    def lambda_6227():

        label("loc_6227")

        TurnDirection(0x1, 0x1F, 0)
        Yield()
        Jump("loc_6227")

    QueueWorkItem2(0x1, 1, lambda_6227)

    def lambda_6239():

        label("loc_6239")

        TurnDirection(0x2, 0x1F, 0)
        Yield()
        Jump("loc_6239")

    QueueWorkItem2(0x2, 1, lambda_6239)

    def lambda_624B():

        label("loc_624B")

        TurnDirection(0x3, 0x1F, 0)
        Yield()
        Jump("loc_624B")

    QueueWorkItem2(0x3, 1, lambda_624B)

    def lambda_625D():

        label("loc_625D")

        TurnDirection(0x4, 0x1F, 0)
        Yield()
        Jump("loc_625D")

    QueueWorkItem2(0x4, 1, lambda_625D)

    def lambda_626F():

        label("loc_626F")

        TurnDirection(0x5, 0x1F, 0)
        Yield()
        Jump("loc_626F")

    QueueWorkItem2(0x5, 1, lambda_626F)
    SetChrFlags(0x1F, 0x8000)
    OP_93(0x1F, 0x0, 0x1F4)
    Sleep(50)
    ClearChrFlags(0x1F, 0x1)
    Sound(814, 0, 80, 0)

    def lambda_629B():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x708, 0x1F40)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_629B)
    WaitChrThread(0x1F, 1)
    Sound(814, 0, 80, 0)

    def lambda_62C2():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1130, 0x1388)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_62C2)
    WaitChrThread(0x1F, 1)
    Sound(854, 0, 80, 0)

    def lambda_62E9():
        OP_9D(0xFE, 0xFFFFA75E, 0x514, 0xFFFFDFBC, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_62E9)
    WaitChrThread(0x1F, 1)
    Sleep(2000)
    OP_93(0x1F, 0xB4, 0x1F4)
    Sound(814, 0, 80, 0)

    def lambda_631A():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1194, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_631A)
    WaitChrThread(0x1F, 1)
    Sound(814, 0, 80, 0)

    def lambda_6341():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_6341)
    WaitChrThread(0x1F, 1)
    Sound(854, 0, 80, 0)

    def lambda_6368():
        OP_9D(0xFE, 0xFFFFAA24, 0x514, 0xFFFFB49C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_6368)
    WaitChrThread(0x1F, 1)
    SetChrFlags(0x1F, 0x1)
    OP_93(0x1F, 0x10E, 0x1F4)
    ClearChrFlags(0x1F, 0x8000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    #C0341
    ChrTalk(
        0xFE,
        "呼喵～……\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6434")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_642A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('斗鱼', 1)

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('防御１', 1)

    label("loc_642A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6434")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_647C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6472")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('雪花蟹', 1)

    #A0343
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('魔防２', 1)

    label("loc_6472")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_647C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_64C4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64BA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('蓝带神仙鱼', 1)

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('ＥＰ３', 1)

    label("loc_64BA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_64C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_650C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6502")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('银伞鱼', 1)

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('攻击２', 1)

    label("loc_6502")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_650C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6554")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_654A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('阿尔摩利卡鲫鱼', 1)

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '琥耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('琥耀珠', 1)

    label("loc_654A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6554")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_659C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6592")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('乌龟', 1)

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '水耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('水耀珠', 1)

    label("loc_6592")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_659C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_65E4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65DA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('橙河鱼', 1)

    #A0348
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '行动力３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('行动力３', 1)

    label("loc_65DA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_65E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_662C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6622")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('岩穴鱼', 1)

    #A0349
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '移动２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('移动２', 1)

    label("loc_6622")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_662C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6674")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_666A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('虹鳟鱼', 1)

    #A0350
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '冻结之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('冻结之刃', 1)

    label("loc_666A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6674")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_66BC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66B2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('食人鱼', 1)

    #A0351
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('回避３', 1)

    label("loc_66B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_66BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6704")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66FA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鲤鱼', 1)

    #A0352
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('省ＥＰ１', 1)

    label("loc_66FA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6704")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_674C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6742")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大口鲈鱼', 1)

    #A0353
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '光耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('光耀珠', 1)

    label("loc_6742")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_674C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_6794")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_678A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('黑鲑', 1)

    #A0354
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('精神３', 1)

    label("loc_678A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6794")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_67DC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67D2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('角斗鱼', 1)

    #A0355
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('命中１', 1)

    label("loc_67D2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_67DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6824")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_681A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('冷水鱼', 1)

    #A0356
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '黑耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('黑耀珠', 1)

    label("loc_681A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6824")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_686C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6862")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('小鲵', 1)

    #A0357
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '妨害２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('妨害２', 1)

    label("loc_6862")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_686C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_68B4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68AA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鲑鱼', 1)

    #A0358
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '绝耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('绝耀珠', 1)

    label("loc_68AA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_68B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_68FC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68F2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('金龙鱼', 1)

    #A0359
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '翠耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('翠耀珠', 1)

    label("loc_68F2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_68FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_6944")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_693A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鳗鲡', 1)

    #A0360
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '冥王铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('冥王铃', 1)

    label("loc_693A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6944")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_698C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6982")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('钢壳龟', 1)

    #A0361
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('回避２', 1)

    label("loc_6982")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_698C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_69D4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨血蟹', 1)

    #A0362
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('防御３', 1)

    label("loc_69CA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_69D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6A1C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A12")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('珍珠龙鱼', 1)

    #A0363
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '封技之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('封技之刃', 1)

    label("loc_6A12")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A1C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_6A64")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A5A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨鲶', 1)

    #A0364
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '金耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('金耀珠', 1)

    label("loc_6A5A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A64")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_6AAC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AA2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('金鲑', 1)

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '破盾之牙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('破盾之牙', 1)

    label("loc_6AA2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6AAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_6AF8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AEE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('猫食', 1)

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽鱼肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×３收下了。\x02",
        )
    )

    AddItemNumber('魔兽鱼肉', 3)

    label("loc_6AEE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6AF8")

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B1F")
    SetScenarioFlags(0x4B, 3)

    label("loc_6B1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B30")
    SetScenarioFlags(0x52, 1)

    label("loc_6B30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B41")
    SetScenarioFlags(0x52, 2)

    label("loc_6B41")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B52")
    SetScenarioFlags(0x52, 3)

    label("loc_6B52")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B63")
    SetScenarioFlags(0x52, 4)

    label("loc_6B63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B74")
    SetScenarioFlags(0x52, 5)

    label("loc_6B74")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B85")
    SetScenarioFlags(0x52, 6)

    label("loc_6B85")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_END)), "loc_6BA2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_END)), "loc_6BB5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_END)), "loc_6BC8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_END)), "loc_6BDB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_END)), "loc_6BEE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_END)), "loc_6C01")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C6C")

    #C0367
    ChrTalk(
        0xFE,
        "喵喵喵～……¤\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0368
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '辰星铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('辰星铃', 1)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_6C6C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CAC")

    #C0369
    ChrTalk(
        0x102,
        "#0105F哎呀……这个要给我们吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D4E")

    label("loc_6CAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CE6")

    #C0370
    ChrTalk(
        0x103,
        "#0205F要把这个给我们吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D4E")

    label("loc_6CE6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6D4E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D2E")

    #C0371
    ChrTalk(
        0x104,
        "#0305F这是给我们的吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D4E")

    label("loc_6D2E")


    #C0372
    ChrTalk(
        0x101,
        "#0005F这个要给我们吗……？\x02",
    )

    CloseMessageWindow()

    label("loc_6D4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D8D")

    #C0373
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，谢啦～\x01",
            "我们会好好使用的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC5")

    label("loc_6D8D")


    #C0374
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，谢啦～\x01",
            "……不过到底是\x01",
            "从哪里拿来的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DC5")

    TalkEnd(0xFE)
    EventEnd(0x4)
    Return()

    label("loc_6DCB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E0A")

    label("loc_6DDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DEE")
    Jump("loc_6E0A")

    label("loc_6DEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E0A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 34)

    label("loc_6E0A")

    Jump("loc_5D6A")

    label("loc_6E0F")

    Jump("loc_6E17")

    label("loc_6E14")

    Call(0, 34)

    label("loc_6E17")

    TalkEnd(0x1F)
    Return()

    # Function_33_5C77 end

    def Function_34_6E1B(): pass

    label("Function_34_6E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E98")

    #C0375
    ChrTalk(
        0x1F,
        "呼喵喵～～咕……\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x103,
        (
            "#0200F……嘘～\x01",
            "蔡特好像睡着了，\x01",
            "还是不要吵醒它为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x1F,
        "呼喵……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 4)
    Jump("loc_6FC5")

    label("loc_6E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6EB8")

    #C0378
    ChrTalk(
        0x1F,
        "……喵呜呜～\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F45")

    label("loc_6EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6EC6")
    Jump("loc_6F45")

    label("loc_6EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6EE2")

    #C0379
    ChrTalk(
        0x1F,
        "喵呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F45")

    label("loc_6EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_6F06")

    #C0380
    ChrTalk(
        0x1F,
        "呼喵喵～～咕……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F45")

    label("loc_6F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6F2A")

    #C0381
    ChrTalk(
        0x1F,
        "呼喵喵～～咕……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F45")

    label("loc_6F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6F45")

    #C0382
    ChrTalk(
        0x1F,
        "……喵呜……\x02",
    )

    CloseMessageWindow()

    label("loc_6F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FC5")

    #C0383
    ChrTalk(
        0x101,
        (
            "#0004F（柯贝是一直住在\x01",
            "  支援科的猫呢……）\x02\x03",

            "#0000F（它是个随性的家伙，\x01",
            "  我们偶尔也会拿点猫食\x01",
            "  来喂喂它。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 3)

    label("loc_6FC5")

    Return()

    # Function_34_6E1B end

    def Function_35_6FC6(): pass

    label("Function_35_6FC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6FD4")
    SetScenarioFlags(0x1, 3)

    label("loc_6FD4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_6FE2")
    SetScenarioFlags(0x1, 3)

    label("loc_6FE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6FF0")
    SetScenarioFlags(0x1, 3)

    label("loc_6FF0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6FFE")
    SetScenarioFlags(0x1, 3)

    label("loc_6FFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_700C")
    SetScenarioFlags(0x1, 3)

    label("loc_700C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_701A")
    SetScenarioFlags(0x1, 3)

    label("loc_701A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7028")
    SetScenarioFlags(0x1, 3)

    label("loc_7028")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7036")
    SetScenarioFlags(0x1, 3)

    label("loc_7036")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7044")
    SetScenarioFlags(0x1, 3)

    label("loc_7044")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7052")
    SetScenarioFlags(0x1, 3)

    label("loc_7052")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7060")
    SetScenarioFlags(0x1, 3)

    label("loc_7060")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_706E")
    SetScenarioFlags(0x1, 3)

    label("loc_706E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_707C")
    SetScenarioFlags(0x1, 3)

    label("loc_707C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_708A")
    SetScenarioFlags(0x1, 3)

    label("loc_708A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7098")
    SetScenarioFlags(0x1, 3)

    label("loc_7098")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_70A6")
    SetScenarioFlags(0x1, 3)

    label("loc_70A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_70B4")
    SetScenarioFlags(0x1, 3)

    label("loc_70B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_70C2")
    SetScenarioFlags(0x1, 3)

    label("loc_70C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_70D0")
    SetScenarioFlags(0x1, 3)

    label("loc_70D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_70DE")
    SetScenarioFlags(0x1, 3)

    label("loc_70DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_70EC")
    SetScenarioFlags(0x1, 3)

    label("loc_70EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_70FA")
    SetScenarioFlags(0x1, 3)

    label("loc_70FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_7108")
    SetScenarioFlags(0x1, 3)

    label("loc_7108")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_7116")
    SetScenarioFlags(0x1, 3)

    label("loc_7116")

    Return()

    # Function_35_6FC6 end

    def Function_36_7117(): pass

    label("Function_36_7117")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71B2")

    #C0384
    ChrTalk(
        0x160,
        (
            "#3300F（中央广场的探听\x01",
            "  就到此为止吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        (
            "#0000F（嗯，应该足够了。）\x02\x03",

            "（接下来，就去站前街道\x01",
            "  打听看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)
    Call(0, 7)

    label("loc_71B2")

    Return()

    # Function_36_7117 end

    def Function_37_71B3(): pass

    label("Function_37_71B3")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0386
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "      『克洛斯贝尔之钟』\x01",
            "Ｓ１１８５  在克洛斯贝尔自治州\x01",
            "发掘出土的巨型大钟。\x01",
            "依据出土遗迹的情况来看，\x01",
            "可推断为中世纪时期的物品。\x01",
            "使用多种金属打造而成，\x01",
            "敲打时会发出悦耳的低音。\x02",
        )
    )

    CloseMessageWindow()

    #A0387
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73A3")

    #C0388
    ChrTalk(
        0x101,
        (
            "#0003F『克洛斯贝尔之钟』……\x01",
            "正可谓是这个城市的\x01",
            "『象征』呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x102,
        "#0105F……那个，罗伊德，难不成……\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        (
            "#0000F嗯……\x01",
            "想办法试试进去调查吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_7415")

    label("loc_73A3")


    #C0391
    ChrTalk(
        0x101,
        (
            "#0001F『克洛斯贝尔之钟』……\x01",
            "正可谓是这个城市的『象征』。\x02\x03",

            "#0003F嗯～……说不定可以\x01",
            "从地下进去，调查内部呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7415")

    TalkEnd(0xFF)
    Return()

    # Function_37_71B3 end

    def Function_38_7419(): pass

    label("Function_38_7419")

    EventBegin(0x1)

    #A0392
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里有架梯子。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7472")
    EventEnd(0x5)
    NewScene("m0000", 125, 0, 0)
    IdleLoop()
    Jump("loc_7474")

    label("loc_7472")

    EventEnd(0x5)

    label("loc_7474")

    Return()

    # Function_38_7419 end

    def Function_39_7475(): pass

    label("Function_39_7475")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-12000, 1000, 13000, 0)
    MoveCamera(350, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -16000, 0, 17000, 135)
    SetChrPos(0x160, -17300, 0, 16800, 135)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")

    def lambda_750B():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_750B)
    Sleep(50)

    def lambda_7528():
        OP_96(0xFE, 0xFFFFCC0C, 0x0, 0x3200, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_7528)
    SetCameraDistance(17500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_757F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_757F)
    Sleep(500)
    WaitChrThread(0x160, 1)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(1085, 255, 100, 0)    #voice#Lloyd

    def lambda_75E7():
        OP_9A(0xFE, 0x101, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_75E7)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0393
    AnonymousTalk(
        0x101,
        "#0005F喂？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1189, 255, 100, 0)    #voice#Elie
    Sleep(1200)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾莉的声音")

    #A0394
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我是艾莉，\x01",
            "行政区的搜索结束了。\x02\x03",

            "虽然没找到柯林，\x01",
            "但有人说，见过与他相似的孩子……\x02\x03",

            "好像没有父母陪同，\x01",
            "就在游行队伍的\x01",
            "末尾跟着跑。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0395
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F是吗……看来很像呢。\x02\x03",

            "#0001F麻烦你继续搜索港湾区了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾莉的声音")

    #A0396
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    WaitChrThread(0x160, 1)

    def lambda_7766():
        OP_96(0xFE, 0xFFFFCC0C, 0x0, 0x3200, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_7766)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    WaitChrThread(0x160, 1)
    Sleep(300)

    #C0397
    ChrTalk(
        0x160,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#3304F游行队伍的末尾……\x01",
            "原来如此，是那辆车啊。\x02",
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
    TurnDirection(0x101, 0x160, 500)

    #C0398
    ChrTalk(
        0x101,
        (
            "#11P#0012F哎，你听到了啊。\x02\x03",

            "#0000F那是怎样的车辆呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x160,
        (
            "#5P#3302F是那个叫做『咪西』的\x01",
            "吉祥物所乘坐的车辆哦。\x02\x03",

            "设计得很有趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        (
            "#11P#0008F原来如此……\x01",
            "很像是小孩子会喜欢的东西呢。\x02\x03",

            "#0003F（这样的话，接下来就应该\x01",
            "  可以排除露天店铺，以小孩子与接待人员\x01",
            "  为中心来探听了吧……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -12400, 0, 13500, 135)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA2, 2)
    OP_29(0x46, 0x1, 0x6)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_39_7475 end

    def Function_40_7946(): pass

    label("Function_40_7946")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(4000, 1000, -20000, 0)
    MoveCamera(47, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 4600, 0, -23500, 0)
    SetChrPos(0x160, 3400, 0, -23700, 0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")

    def lambda_79DC():
        OP_96(0xFE, 0x11F8, 0x0, 0xFFFFB9B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79DC)
    Sleep(50)

    def lambda_79F9():
        OP_96(0xFE, 0xD48, 0x0, 0xFFFFB8E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_79F9)
    OP_68(4000, 1000, -18000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    Sleep(500)
    WaitChrThread(0x160, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_7A5A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_7A5A)
    Sleep(500)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x3)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)

    def lambda_7AB8():
        OP_9A(0xFE, 0x101, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_7AB8)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0401
    AnonymousTalk(
        0x101,
        "#0001F喂？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("兰迪的声音")

    #A0402
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我是兰迪，\x01",
            "现在正在旧城区打听。\x02\x03",

            "那个小孩……\x01",
            "好像曾在旧城区玩耍过一阵哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0403
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011F什么……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("兰迪的声音")

    #A0404
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好像是在参观游行的时候，\x01",
            "受到旧城区孩子的邀请，\x01",
            "暂时在这边玩了一会。\x02\x03",

            "之后，听说是往东街那边\x01",
            "去了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0405
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0008F是吗……\x02\x03",

            "#0006F这孩子，该说是好奇心旺盛，\x01",
            "还是不知天高地厚呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("兰迪的声音")

    #A0406
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "真是头疼啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(806, 2, 100, 0)
    Sleep(1200)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0407
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……我是缇欧。\x01",
            "半途插话，失礼了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0408
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F缇欧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("兰迪的声音")

    #A0409
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "怎么，这个终端\x01",
            "原来还能进行多人对话啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0410
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，是有这个功能的。\x02\x03",

            "我们在城市的东出口，\x01",
            "没有发现那孩子的气味。\x02\x03",

            "现在正经过港湾区，\x01",
            "往北出口前进。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0411
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F嗯，拜托你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("兰迪的声音")

    #A0412
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那我也再回\x01",
            "东街打听一圈吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0413
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F嗯，看来\x01",
            "他确实曾经过那一带。\x02\x03",

            "#0001F保险起见，还是再去打听一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("兰迪的声音")

    #A0414
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好，交给我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    WaitChrThread(0x160, 1)

    def lambda_7F00():
        OP_96(0xFE, 0xD48, 0x0, 0xFFFFB8E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_7F00)
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    WaitChrThread(0x160, 1)
    Sleep(300)

    #C0415
    ChrTalk(
        0x160,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#3302F呵呵……那孩子很\x01",
            "擅长玩捉迷藏呢。\x02\x03",

            "#3304F从行政区到欢乐街，后巷，\x01",
            "中央广场，最后到东街。就这样一路\x01",
            "追着游行队伍，突然又移动到旧城区……\x02\x03",

            "然后就又回到东街，\x01",
            "往港湾区那边去了……\x02\x03",

            "#3300F说不定就是这样的路线吧。\x02",
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
    TurnDirection(0x101, 0x160, 400)
    Sleep(150)

    #C0416
    ChrTalk(
        0x101,
        (
            "#0004F#11P你真的好敏锐呢……\x01",
            "跟我的推测完全相同。\x02\x03",

            "#0000F既然有同伴在搜索，\x01",
            "那边就交给他们吧……\x02\x03",

            "保险起见，我想去西街确认一下，\x01",
            "没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x160,
        (
            "#6P#3300F呵呵，也不错啊。\x01",
            "排除选项也是很有意义的嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    ClearMapFlags(0x10000000)
    SetChrPos(0x0, 4000, 0, -17500, 0)
    SetScenarioFlags(0xA2, 6)
    OP_29(0x46, 0x1, 0xA)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_40_7946 end

    def Function_41_8134(): pass

    label("Function_41_8134")

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
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x25, 1, 0, 42)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -4200, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x8000)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x25, 1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 4)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_8134 end

    def Function_42_82F6(): pass

    label("Function_42_82F6")

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

    # Function_42_82F6 end

    def Function_43_8342(): pass

    label("Function_43_8342")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(885)
    LoadEffect(0x7, "event\\ev308_00.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 12260, -4000, -5860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 2420, -4000, -4019, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -14490, -4000, -1370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x0, 400, 0, -2630, 75)
    SetChrPos(0x1, 400, 0, -2630, 75)
    SetChrPos(0x2, 400, 0, -2630, 75)
    SetChrPos(0x3, 400, 0, -2630, 75)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    Sound(885, 2, 90, 0)
    FadeToBright(2000, 0)
    OP_68(9110, 1900, -4010, 0)
    MoveCamera(351, 38, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22500, 0)
    OP_68(-11370, 1900, -100, 10000)
    MoveCamera(335, 20, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(17000, 10000)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x375)
    SetScenarioFlags(0x5C, 0)
    NewScene("c100C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_8342 end

    def Function_44_8500(): pass

    label("Function_44_8500")

    EventBegin(0x0)
    OP_4B(0x10, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(10960, 1900, 3910, 0)
    MoveCamera(140, 25, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(12830, 0)
    SetChrPos(0x101, 10600, 0, 3200, 90)
    SetChrPos(0x102, 10600, 0, 2100, 90)
    SetChrPos(0x103, 9100, 0, 3100, 90)
    SetChrPos(0x104, 9290, 0, 1920, 90)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0418
    ChrTalk(
        0x102,
        (
            "#11P#0100F（『纳德尔汉堡包』……\x01",
            "  是遭窃的店铺呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        (
            "#6P#0001F对不起，能打扰一下吗？\x01",
            "我们正在进行盗窃案的调查，想询问一下情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0420
    ChrTalk(
        0x10,
        (
            "#5P啊，你、你们……\x01",
            "就是工商协会的人\x01",
            "提到的警察们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x10,
        (
            "#5P唉，其实我这里今天早上\x01",
            "才刚刚遭窃……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x103,
        (
            "#12P#0200F是这样啊……\x02\x03",

            "关于当时的情况，\x01",
            "能详细地告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x10,
        "#5P这、这个……\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x10,
        (
            "#5P其实，不知不觉就被偷了，\x01",
            "我也完全搞不清楚状况。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0425
    ChrTalk(
        0x104,
        "#12P#0305F这是怎么回事……？\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x10,
        (
            "#5P要说有可能遭窃的时机，应该就是那个时候……\x01",
            "当时我正在接待一个健谈的青年顾客。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x10,
        (
            "#5P多半是来克洛斯贝尔\x01",
            "观赏纪念庆典的游客吧，\x01",
            "总之是个非常健谈的青年。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x10,
        (
            "#5P我将餐品交给他的时候，\x01",
            "背后就传来了响动。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x10,
        (
            "#5P我急忙回过头，\x01",
            "可是不见任何人的影子……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x10,
        (
            "#5P可是，过了一会，\x01",
            "当我打开收银盒时，\x01",
            "才发现赚来的钱已经全部消失一空了！\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x102,
        (
            "#11P#0101F这么说，很有可能\x01",
            "是在那时被盗的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x10,
        (
            "#5P其它的我就不清楚了，\x01",
            "真是个谜呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x101,
        "#6P#0003F是这样吗……\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B3F")
    OP_68(9490, 1900, 3320, 1200)
    MoveCamera(140, 32, 0, 1200)
    SetCameraDistance(14000, 1200)

    def lambda_89D4():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_89D4)

    def lambda_89E1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_89E1)

    def lambda_89EE():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_89EE)

    def lambda_89FB():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_89FB)
    Sleep(1200)

    #C0434
    ChrTalk(
        0x101,
        "#6P#0000F探听就到此为止吧……\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x104,
        (
            "#11P#0300F是啊，差不多可以\x01",
            "回去整理一下情报了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B39")

    #C0436
    ChrTalk(
        0x102,
        (
            "#11P#0100F工商协会也没有和我们联络，\x01",
            "看来犯人还没有\x01",
            "再次作案呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x103,
        (
            "#12P#0203F是呀。\x02\x03",

            "#0200F……保险起见，\x01",
            "还是再去各店铺巡视一下，\x01",
            "然后再回去比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B39")

    OP_29(0x20, 0x1, 0xD)

    label("loc_8B3F")

    OP_5A()
    SetChrPos(0x0, 11180, 0, 2990, 90)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_44_8500 end

    def Function_45_8B62(): pass

    label("Function_45_8B62")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch20000.itc", 0x1F)
    LoadChrToIndex("chr/ch00301.itc", 0x20)
    OP_68(-6670, 1900, 14740, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(26840, 0)
    SetChrPos(0x101, -21900, -320, -910, 0)
    SetChrPos(0x102, 10980, 0, 26470, 355)
    SetChrPos(0x103, 11010, 0, 5140, 175)
    SetChrPos(0x104, -23280, -550, -950, 45)
    SetChrPos(0x20, -7420, 0, 13730, 0)
    SetChrPos(0x23, -16170, 0, 18920, 315)
    SetChrPos(0x24, -270, 800, 28250, 355)
    SetChrChipByIndex(0x20, 0x0)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0xD)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0xC)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrName("")

    #A0438
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德一行前往目标街区，\x01",
            "开始埋伏。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-6670, 1000, 14740, 2800)
    PlayBGM("ed7111", 0)
    FadeToBright(2000, 0)
    BeginChrThread(0x11, 1, 0, 46)
    Sleep(150)
    BeginChrThread(0x20, 1, 0, 46)
    OP_0D()
    OP_6F(0x1)

    #A0439
    AnonymousTalk(
        0x101,
        (
            "#0001F………………………………\x02\x03",

            "好像不是这个客人啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x20, 0x1)
    OP_64(0x11)
    OP_64(0x20)
    Sleep(200)
    BeginChrThread(0x20, 1, 0, 47)
    Sleep(1800)
    BeginChrThread(0x21, 1, 0, 48)
    Sleep(200)
    BeginChrThread(0x22, 1, 0, 49)
    Sleep(8000)
    OP_95(0x23, -11360, 0, 14110, 1500, 0x0)
    OP_95(0x23, -7480, 0, 13910, 1500, 0x0)
    OP_93(0x23, 0x0, 0x190)
    BeginChrThread(0x23, 1, 0, 46)
    Sleep(150)
    BeginChrThread(0x11, 1, 0, 46)
    Sleep(500)
    SetScenarioFlags(0x1, 4)
    BeginChrThread(0x24, 1, 0, 50)

    #A0440
    AnonymousTalk(
        0x101,
        (
            "#0001F这次的客人是个青年吗……\x01",
            "好像是个游客。\x02",
        )
    )

    CloseMessageWindow()

    #A0441
    AnonymousTalk(
        0x104,
        (
            "#0305F等等，罗伊德……\x01",
            "好像又来了一个人哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_8E1C")
    Sleep(500)
    Jump("loc_8E0B")

    label("loc_8E1C")

    Sleep(500)
    EndChrThread(0x24, 0x1)
    Sleep(500)
    OP_95(0x24, -3540, 0, 16830, 1500, 0x0)
    Sleep(800)
    OP_95(0x24, -4360, 0, 17140, 2200, 0x0)
    SetChrName("")

    #A0442
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "青年向露天店的收银盒伸出了手。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x7D0)
    OP_68(-20140, 1000, 1410, 1200)
    Sleep(1200)

    #C0443
    ChrTalk(
        0x104,
        "#6P#0301F下手了……！\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x101,
        "#12P#0001F好，就是现在……！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7401", 0)
    BeginChrThread(0x101, 1, 0, 51)
    BeginChrThread(0x104, 1, 0, 52)

    #C0445
    ChrTalk(
        0x101,
        "#0007F#10A站住，你们两个！！\x02",
    )
    #Auto

    CloseMessageWindow()
    Fade(500)
    OP_68(-6320, 1900, 14400, 0)
    MoveCamera(286, 29, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(23340, 0)
    OP_0D()
    OP_4B(0x11, 0xFF)
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x23, 0xFF)
    OP_64(0x11)
    OP_64(0x23)
    OP_63(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(300)

    def lambda_8F70():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8F70)

    def lambda_8F7D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_8F7D)
    Sleep(200)

    #C0446
    ChrTalk(
        0x23,
        "#5P嘁，糟了……！\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x24,
        "#11P穿帮了，快跑！！\x02",
    )

    CloseMessageWindow()
    OP_68(-680, 1900, 16400, 800)
    MoveCamera(326, 38, 0, 800)
    OP_6E(480, 800)
    SetCameraDistance(20960, 800)

    def lambda_8FEC():

        label("loc_8FEC")

        TurnDirection(0xFE, 0x23, 300)
        Yield()
        Jump("loc_8FEC")

    QueueWorkItem2(0x11, 1, lambda_8FEC)
    BeginChrThread(0x23, 1, 0, 53)
    OP_95(0x24, 410, 0, 17550, 7000, 0x0)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    def lambda_9020():
        OP_95(0xFE, -390, 0, 17340, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9020)

    def lambda_903A():
        OP_95(0xFE, 870, 0, 19220, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_903A)
    Sound(819, 0, 100, 0)
    OP_63(0x24, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    Sound(24, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    #C0448
    ChrTalk(
        0x24,
        "#6P#15A呜噢……！\x02",
    )
    #Auto


    #C0449
    ChrTalk(
        0xC,
        "#11P#15A嘎啊～！？\x02",
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 54)
    BeginChrThread(0x104, 1, 0, 55)
    WaitChrThread(0x104, 1)
    Sleep(400)
    WaitChrThread(0x101, 1)
    OP_93(0x104, 0x5A, 0x190)

    #C0450
    ChrTalk(
        0x104,
        "#11P#0307F大小姐，阿缇！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(300)
    OP_68(8360, 2200, 14220, 0)
    MoveCamera(64, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12970, 0)
    SetChrPos(0x23, 3440, 0, 16440, 90)
    BeginChrThread(0x102, 1, 0, 56)
    BeginChrThread(0x103, 1, 0, 57)
    OP_95(0x23, 8700, 0, 16500, 5000, 0x0)
    BeginChrThread(0x23, 0, 0, 58)
    Sleep(300)
    OP_63(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    #C0451
    ChrTalk(
        0x102,
        "#0100F#11P啊呀，此路不通哦。\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x103,
        "#0201F#12P你们被将死了呢。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x23, 1, 0, 59)
    Sleep(800)

    #C0453
    ChrTalk(
        0x23,
        "#6P可、可、可……\x02",
    )

    Sleep(1000)
    OP_57(0x0)
    SetCameraDistance(13500, 1800)
    OP_82(0x64, 0xC8, 0xBB8, 0x320)

    #C0454
    ChrTalk(
        0x23,
        "#6P#30A#4S可恶啊啊啊啊！！\x02",
    )
    #Auto

    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    CloseMessageWindow()
    Sleep(400)
    SetMapObjFlags(0x4, 0x10)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 1)
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_8B62 end

    def Function_46_9257(): pass

    label("Function_46_9257")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_927C")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_46_9257")

    label("loc_927C")

    Return()

    # Function_46_9257 end

    def Function_47_927D(): pass

    label("Function_47_927D")

    OP_95(0xFE, -3920, 0, 14640, 1500, 0x0)
    OP_95(0xFE, 1060, 0, 15050, 1500, 0x0)
    OP_95(0xFE, 5750, 0, 9900, 1500, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_47_927D end

    def Function_48_92C4(): pass

    label("Function_48_92C4")

    SetChrPos(0xFE, 4800, 0, 11810, 270)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_92EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_92EF)
    OP_95(0xFE, -100, 0, 12810, 1500, 0x0)
    OP_95(0xFE, -5290, 0, 10890, 1500, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(2800)
    OP_95(0xFE, -9280, 0, 9400, 1500, 0x0)
    OP_95(0xFE, -17320, 0, 16450, 1500, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_48_92C4 end

    def Function_49_9360(): pass

    label("Function_49_9360")

    SetChrPos(0xFE, 4800, 0, 12810, 270)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_938B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_938B)
    OP_95(0xFE, -100, 0, 13810, 1500, 0x0)
    OP_95(0xFE, -5290, 0, 11890, 1500, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(2800)
    OP_95(0xFE, -9280, 0, 10400, 1500, 0x0)
    OP_95(0xFE, -17320, 0, 17450, 1500, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_49_9360 end

    def Function_50_93FC(): pass

    label("Function_50_93FC")

    Sleep(2500)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    OP_79(0x4)

    def lambda_941F():
        OP_95(0xFE, -280, 800, 23120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_941F)
    Sleep(1000)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    OP_95(0xFE, -1680, 0, 18230, 2000, 0x0)

    label("loc_9461")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_949C")
    Sleep(800)
    OP_93(0xFE, 0x87, 0x190)
    Sleep(800)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(800)
    OP_93(0xFE, 0xE1, 0x190)
    ClearScenarioFlags(0x1, 4)
    Jump("loc_9461")

    label("loc_949C")

    Return()

    # Function_50_93FC end

    def Function_51_949D(): pass

    label("Function_51_949D")

    OP_95(0xFE, -19540, 0, -1160, 4000, 0x0)
    OP_95(0xFE, -13740, 0, 4530, 4000, 0x0)
    Return()

    # Function_51_949D end

    def Function_52_94C6(): pass

    label("Function_52_94C6")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFAA6A, 0x0, 0x46A, 0x320, 0x9C4)
    SetChrChipByIndex(0xFE, 0xFF)
    OP_95(0xFE, -18470, 0, 4490, 4000, 0x0)
    Return()

    # Function_52_94C6 end

    def Function_53_94FE(): pass

    label("Function_53_94FE")

    OP_95(0xFE, -300, 0, 15200, 7000, 0x0)
    OP_95(0xFE, 8700, 0, 16500, 7000, 0x0)
    Return()

    # Function_53_94FE end

    def Function_54_9527(): pass

    label("Function_54_9527")

    SetChrPos(0xFE, -10000, 0, 9420, 318)
    OP_95(0xFE, -1300, 0, 17110, 7000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_54_9527 end

    def Function_55_9554(): pass

    label("Function_55_9554")

    SetChrPos(0xFE, -6890, 0, 11470, 48)
    OP_95(0xFE, 690, 0, 16880, 7000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_55_9554 end

    def Function_56_9581(): pass

    label("Function_56_9581")

    OP_95(0xFE, 11800, 0, 19560, 5000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_56_9581 end

    def Function_57_959D(): pass

    label("Function_57_959D")

    OP_95(0xFE, 10450, 0, 11630, 5000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_57_959D end

    def Function_58_95B9(): pass

    label("Function_58_95B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_95D0")
    OP_A0(0xFE, 3000, 0x0, 0xFB)
    Jump("Function_58_95B9")

    label("loc_95D0")

    Return()

    # Function_58_95B9 end

    def Function_59_95D1(): pass

    label("Function_59_95D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_95FF")
    OP_93(0xFE, 0x87, 0x190)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(500)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1200)
    Jump("Function_59_95D1")

    label("loc_95FF")

    Return()

    # Function_59_95D1 end

    def Function_60_9600(): pass

    label("Function_60_9600")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("apl/ch50379.itc", 0x1F)
    LoadChrToIndex("chr/ch02708.itc", 0x20)
    OP_4B(0x11, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(3680, 1900, 13710, 0)
    MoveCamera(35, 35, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 8770, 0, 14220, 270)
    SetChrPos(0x102, 10300, 0, 15450, 270)
    SetChrPos(0x103, 8870, 0, 15450, 270)
    SetChrPos(0x104, 10200, 0, 14220, 270)
    SetChrPos(0x23, -3470, 200, 15260, 294)
    SetChrPos(0x24, -2120, 0, 16490, 242)
    SetChrPos(0x1E, -3570, 400, 15260, 90)
    SetChrPos(0x11, -5920, 0, 15070, 100)
    SetChrPos(0xD, 1100, 0, 19090, 242)
    SetChrPos(0xC, 2110, 0, 17600, 242)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x23, 0x2)
    SetChrFlags(0x23, 0x20)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x23, 0x1)
    ClearChrFlags(0x1E, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)

    def lambda_9765():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9765)

    def lambda_977A():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_977A)

    def lambda_978F():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_978F)

    def lambda_97A4():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_97A4)
    FadeToBright(1000, 0)
    OP_0D()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    #C0455
    ChrTalk(
        0x101,
        "#0011F啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_68(-1500, 2100, 13860, 3000)
    MoveCamera(337, 42, 0, 3000)
    OP_6E(580, 3000)
    SetCameraDistance(15750, 3000)
    Sleep(3000)

    #C0456
    ChrTalk(
        0x24,
        "#11P饶、饶命啊～！？\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x23,
        (
            "#12P呜、呜……\x01",
            "这家伙是什么呀……\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x1E,
        "#5P#1201F呜噜噜，嘎噜噜噜……！\x02",
    )

    CloseMessageWindow()

    def lambda_988E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_988E)

    def lambda_98A3():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_98A3)

    def lambda_98B8():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_98B8)

    def lambda_98CD():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_98CD)
    Sleep(2600)

    #C0459
    ChrTalk(
        0x104,
        (
            "#12P#0305F蔡特，\x01",
            "你也来助阵了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x103,
        (
            "#12P#0200F莫非这两人……\x01",
            "就是盗窃犯……？\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x1E,
        "#5P#1203F……嗷呜！\x02",
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

    #C0462
    ChrTalk(
        0x101,
        (
            "#6P#0000F难不成，你在支援科的楼顶上\x01",
            "看到了犯罪现场吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x102,
        "#12P#0100F呼，真是佩服……\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x11,
        (
            "#5P那、那个，你们是\x01",
            "这只狗狗的饲主吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x11,
        "#5P吓死人啦，真是的～！\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x101,
        "#6P#0002F哈哈，抱歉……\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        (
            "#12P#0300F别看它外表有点凶，其实是个\x01",
            "很懂事的家伙，不用怕啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x102,
        (
            "#12P#0106F又给蔡特\x01",
            "添麻烦了……\x02\x03",

            "#0100F不过，多亏有它帮忙，\x01",
            "总算是顺利\x01",
            "逮捕到犯人了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x103,
        "#12P#0202F蔡特，你帮大忙了。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x1E,
        "#5P#1200F呜噜噜噜，嗷呜……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1E, 0x1)
    SetScenarioFlags(0x5C, 1)
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_60_9600 end

    def Function_61_9B88(): pass

    label("Function_61_9B88")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50, 4000, 4040, 0)
    MoveCamera(33, 28, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(15130, 0)
    SetChrPos(0x101, -750, -1000, 4560, 135)
    SetChrPos(0x102, -370, -1000, 5710, 180)
    SetChrPos(0x103, -1310, -1000, 5220, 135)
    SetChrPos(0x104, 170, -1000, 4860, 180)
    OP_68(50, 1100, 4040, 3000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(886, 0, 100, 0)
    Sleep(500)

    #C0471
    ChrTalk(
        0x104,
        "#12P#0306F啊呜……撞到头了啊。\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x101,
        (
            "#12P#0003F这么说来，钟这东西，\x01",
            "从里面看的话，还真是一片漆黑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#6P#0100F是『昏暗的天空』呢……\x01",
            "莫非，『不夜之城的象征』\x01",
            "就是指这个钟吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x103,
        (
            "#6P#0200F罗伊德前辈，钟的内侧\x01",
            "好像贴着一张卡片。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x101,
        (
            "#12P#0005F真的……\x01",
            "稍等一下，我看看。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x4)
    Sleep(300)
    OP_9D(0x101, 0x136, 0xFFFFFC18, 0xCE4, 0x190, 0x9C4)
    Sleep(700)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0476
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "找到了贴在\x01",
            "钟里的卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(200)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0477
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   下一把钥匙在乐土之中\x01",
            "唯有可于温暖的水中小乐园内\x01",
            "    绽放光芒者才能得知\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #C0478
    ChrTalk(
        0x101,
        "#12P#0005F这是……\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x104,
        "#12P#0305F怎么，又是猜谜啊？\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x102,
        (
            "#6P#0103F怪盗Ｂ，果然\x01",
            "是个难缠的对手啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x103,
        (
            "#6P#0200F『温暖的水中小乐园』……\x01",
            "这是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -110, -1000, 5480, 135)
    OP_CA(0x1, 0xFF, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    OP_66(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_29(0x22, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_61_9B88 end

    def Function_62_9F98(): pass

    label("Function_62_9F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9FC1")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_9FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9FEA")
    EventBegin(0x1)
    Call(0, 69)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_9FEA")

    Return()

    # Function_62_9F98 end

    def Function_63_9FEB(): pass

    label("Function_63_9FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A014")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_A014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A03D")
    EventBegin(0x1)
    Call(0, 71)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_A03D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A066")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_A066")

    Return()

    # Function_63_9FEB end

    def Function_64_A067(): pass

    label("Function_64_A067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A090")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_A090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0B9")
    EventBegin(0x1)
    Call(0, 73)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_A0B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0E2")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_A0E2")

    Return()

    # Function_64_A067 end

    def Function_65_A0E3(): pass

    label("Function_65_A0E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A10C")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_A10C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A135")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_A135")

    Return()

    # Function_65_A0E3 end

    def Function_66_A136(): pass

    label("Function_66_A136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A15F")
    EventBegin(0x1)
    Call(0, 70)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_A15F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A188")
    EventBegin(0x1)
    Call(0, 69)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_A188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A1B1")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_A1B1")

    Return()

    # Function_66_A136 end

    def Function_67_A1B2(): pass

    label("Function_67_A1B2")

    EventBegin(0x1)
    Call(0, 74)
    Sleep(50)
    SetChrPos(0x0, -28500, -8200, -25010, 180)
    EventEnd(0x4)
    Return()

    # Function_67_A1B2 end

    def Function_68_A1CE(): pass

    label("Function_68_A1CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A262")

    #C0482
    ChrTalk(
        0x103,
        (
            "#0200F罗伊德前辈，约纳\x01",
            "可能会发来联络。\x02\x03",

            "还是不要走太远为好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#0000F说得也是……\x01",
            "做好准备之后，\x01",
            "就赶快去地下空间吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2AC")

    label("loc_A262")


    #C0484
    ChrTalk(
        0x103,
        (
            "#0200F……约纳\x01",
            "可能会发来联络。\x02\x03",

            "做好准备之后，\x01",
            "就赶快去地下空间吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2AC")

    Return()

    # Function_68_A1CE end

    def Function_69_A2AD(): pass

    label("Function_69_A2AD")


    #C0485
    ChrTalk(
        0x101,
        (
            "#0000F不，还没有\x01",
            "探听到足够的情报……\x02\x03",

            "在这一带\x01",
            "再多收集一些情报吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_69_A2AD end

    def Function_70_A2F8(): pass

    label("Function_70_A2F8")


    #C0486
    ChrTalk(
        0x101,
        (
            "#0000F不……先去站前街道\x01",
            "进行探听吧。\x02\x03",

            "要是他出了城\x01",
            "可就麻烦了……\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_70_A2F8 end

    def Function_71_A341(): pass

    label("Function_71_A341")


    #C0487
    ChrTalk(
        0x101,
        (
            "#0000F这边有兰迪负责\x01",
            "调查。\x02\x03",

            "按照原定计划，继续去\x01",
            "我负责的街区探听消息吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_71_A341 end

    def Function_72_A392(): pass

    label("Function_72_A392")


    #C0488
    ChrTalk(
        0x101,
        (
            "#0000F现在不是绕道的时候……\x02\x03",

            "尽快赶往\x01",
            "西克洛斯贝尔街道吧！\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_72_A392 end

    def Function_73_A3D4(): pass

    label("Function_73_A3D4")


    #C0489
    ChrTalk(
        0x101,
        (
            "#0000F这边有艾莉负责\x01",
            "调查。\x02\x03",

            "按照原定计划，继续去\x01",
            "我负责的街区探听消息吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_73_A3D4 end

    def Function_74_A425(): pass

    label("Function_74_A425")


    #C0490
    ChrTalk(
        0x101,
        (
            "#0001F现在没有什么要事……\x01",
            "还是专心寻找柯林吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_74_A425 end

    SaveToFile()

Try(main)
