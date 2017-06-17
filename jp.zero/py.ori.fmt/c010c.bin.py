from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "アベル",                 # 1
        "ミミ",                   # 2
        "ジーナ",                 # 3
        "コンテ老人",             # 4
        "プルーナ",               # 5
        "リナリー",               # 6
        "ハース",                 # 7
        "アロナ",                 # 8
        "ナードル",               # 9
        "メイジ",                 # 10
        "ノンノ",                 # 11
        "リュウ",                 # 12
        "コウケン",               # 13
        "フェイ",                 # 14
        "パンセ",                 # 15
        "看護師シロン",           # 16
        "看護師メイファ",         # 17
        "ケイト巡査",             # 18
        "観光客",                 # 19
        "観光客",                 # 20
        "観光客",                 # 21
        "観光客",                 # 22
        "ツァイト",               # 23
        "コッペ",                 # 24
        "客",                     # 25
        "客",                     # 26
        "客",                     # 27
        "青年",                   # 28
        "青年",                   # 29
        "SE制御",                 # 30
        "中央広場",               # 31
        "西通り",                 # 32
        "行政区",                 # 33
        "住宅街",                 # 34
        "歓楽街",                 # 35
        "東通り",                 # 36
        "旧市街",                 # 37
        "港湾区",                 # 38
        "ＩＢＣ",                 # 39
        "駅前通り",               # 40
        "裏通り",                 # 41
        "ウルスラ間道",           # 42
        "東クロスベル街道",       # 43
        "西クロスベル街道",       # 44
        "マインツ山道",           # 45
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
        "Function_9_1636",         # 09, 9
        "Function_10_1A4E",        # 0A, 10
        "Function_11_217F",        # 0B, 11
        "Function_12_2555",        # 0C, 12
        "Function_13_2B5D",        # 0D, 13
        "Function_14_2DB4",        # 0E, 14
        "Function_15_301A",        # 0F, 15
        "Function_16_33C4",        # 10, 16
        "Function_17_3B44",        # 11, 17
        "Function_18_3C55",        # 12, 18
        "Function_19_4342",        # 13, 19
        "Function_20_4D7B",        # 14, 20
        "Function_21_4E53",        # 15, 21
        "Function_22_5649",        # 16, 22
        "Function_23_5850",        # 17, 23
        "Function_24_58F9",        # 18, 24
        "Function_25_595D",        # 19, 25
        "Function_26_5A25",        # 1A, 26
        "Function_27_5B49",        # 1B, 27
        "Function_28_6069",        # 1C, 28
        "Function_29_622D",        # 1D, 29
        "Function_30_6357",        # 1E, 30
        "Function_31_6535",        # 1F, 31
        "Function_32_67C2",        # 20, 32
        "Function_33_69D3",        # 21, 33
        "Function_34_7CEB",        # 22, 34
        "Function_35_7EE4",        # 23, 35
        "Function_36_8035",        # 24, 36
        "Function_37_80E1",        # 25, 37
        "Function_38_837E",        # 26, 38
        "Function_39_83E4",        # 27, 39
        "Function_40_8911",        # 28, 40
        "Function_41_91B9",        # 29, 41
        "Function_42_937B",        # 2A, 42
        "Function_43_93C7",        # 2B, 43
        "Function_44_9585",        # 2C, 44
        "Function_45_9C5B",        # 2D, 45
        "Function_46_A3A6",        # 2E, 46
        "Function_47_A3CC",        # 2F, 47
        "Function_48_A413",        # 30, 48
        "Function_49_A4AF",        # 31, 49
        "Function_50_A54B",        # 32, 50
        "Function_51_A5EC",        # 33, 51
        "Function_52_A615",        # 34, 52
        "Function_53_A64D",        # 35, 53
        "Function_54_A676",        # 36, 54
        "Function_55_A6A3",        # 37, 55
        "Function_56_A6D0",        # 38, 56
        "Function_57_A6EC",        # 39, 57
        "Function_58_A708",        # 3A, 58
        "Function_59_A720",        # 3B, 59
        "Function_60_A74F",        # 3C, 60
        "Function_61_AD39",        # 3D, 61
        "Function_62_B1A0",        # 3E, 62
        "Function_63_B1F3",        # 3F, 63
        "Function_64_B26F",        # 40, 64
        "Function_65_B2EB",        # 41, 65
        "Function_66_B33E",        # 42, 66
        "Function_67_B3BA",        # 43, 67
        "Function_68_B3D6",        # 44, 68
        "Function_69_B4F1",        # 45, 69
        "Function_70_B550",        # 46, 70
        "Function_71_B5B3",        # 47, 71
        "Function_72_B61E",        # 48, 72
        "Function_73_B672",        # 49, 73
        "Function_74_B6DB",        # 4A, 74
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15FF")
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
    Jump("loc_1624")

    label("loc_15FF")


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

    label("loc_1624")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_14D3 end

    def Function_9_1636(): pass

    label("Function_9_1636")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16C9")

    #C0003
    ChrTalk(
        0xFE,
        (
            "期間中、ミミには特別な事は\x01",
            "何一つしてあげられなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "ああやって楽しんでくれてるんだ。\x01",
            "それだけで僕は満足だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A4A")

    label("loc_16C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1746")

    #C0005
    ChrTalk(
        0xFE,
        "パレードが無事終了してよかったよ。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "記念祭の一大イベントだからね、\x01",
            "交通には特に気を遣っていたようだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A4A")

    label("loc_1746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_17ED")

    #C0007
    ChrTalk(
        0xFE,
        (
            "パレードがあるからかな、\x01",
            "昨日と比べても\x01",
            "更に賑やかな気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "導力車とかち合ったりしたら台無しだし、\x01",
            "道路整理をきちんとしてもらわないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A4A")

    label("loc_17ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_189D")

    #C0009
    ChrTalk(
        0xFE,
        (
            "港湾区でやっていたライブが\x01",
            "なかなか楽しくてね。\x01",
            "ミミも随分喜んでくれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "記念祭中はずっと\x01",
            "何かやってるみたいだし、\x01",
            "ちょくちょく見に行ってみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A4A")

    label("loc_189D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1950")

    #C0011
    ChrTalk(
        0xFE,
        (
            "昨日からミミと一緒に\x01",
            "出店を回ったりしているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "楽しみにしてたアルカンシェル公演は\x01",
            "チケットが取れなかったからね。\x01",
            "そのせめてもの埋め合わせというわけさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A4A")

    label("loc_1950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19EF")

    #C0013
    ChrTalk(
        0xFE,
        (
            "各街道への出入り口、\x01",
            "昨日からすごいことになってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "外国の導力車が沢山止めてあるけど、\x01",
            "あれ全部許可とってるのかなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A4A")

    label("loc_19EF")


    #C0015
    ChrTalk(
        0xFE,
        (
            "各街道への出入り口、\x01",
            "昨日からすごいことになってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "違法駐車も多そうだなぁ……\x02",
    )

    CloseMessageWindow()

    label("loc_1A4A")

    TalkEnd(0xFE)
    Return()

    # Function_9_1636 end

    def Function_10_1A4E(): pass

    label("Function_10_1A4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1AC2")

    #C0017
    ChrTalk(
        0xFE,
        (
            "ミシュラムにもアルカンシェルにも\x01",
            "行けなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "お父さんと色々遊べて楽しかったよ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_217B")

    label("loc_1AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_1B12")

    #C0019
    ChrTalk(
        0xFE,
        "パレード楽しかったよ！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "ロイドくんたちは見なかったのー？\x02",
    )

    CloseMessageWindow()
    Jump("loc_217B")

    label("loc_1B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1D96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF2")

    #C0021
    ChrTalk(
        0x101,
        (
            "#0000F（うん、この子なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0023
    ChrTalk(
        0xFE,
        "え？　この子……？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "うーん、そういえば……\x01",
            "パレードについて行った子かも！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#0005F心当たりがあるのかい？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "うん、一番最後でねー、\x01",
            "パレードの後をトコトコ歩いてたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "たぶんその子だと思う～。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0003Fそうか……\x01",
            "（エリィから聞いた情報と一致するな。）\x02\x03",

            "#0000Fありがとう、助かったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 36)
    Jump("loc_1D91")

    label("loc_1CF2")


    #C0029
    ChrTalk(
        0xFE,
        (
            "ミミ、パレードも\x01",
            "しっかり見てたから覚えてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "一番最後でねー、パレードの後を\x01",
            "トコトコ歩いてたの！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x160,
        (
            "#3300Fふふ……\x01",
            "……好奇心の強い子みたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D91")

    Jump("loc_217B")

    label("loc_1D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1DE6")

    #C0032
    ChrTalk(
        0xFE,
        "パレード楽しかったよ！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "ロイドくんたちは見なかったのー？\x02",
    )

    CloseMessageWindow()
    Jump("loc_217B")

    label("loc_1DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1E39")

    #C0034
    ChrTalk(
        0xFE,
        (
            "今日はお父さんと\x01",
            "パレード見に行くんだー。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "すごく楽しみー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_217B")

    label("loc_1E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1EBD")

    #C0036
    ChrTalk(
        0xFE,
        (
            "ライブ、たのしかった！\x01",
            "ちょっとクラクラしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "もうね、すごいの！\x01",
            "ステージの上で、ジャジャーン♪って！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217B")

    label("loc_1EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1F49")

    #C0038
    ChrTalk(
        0xFE,
        "もくもく……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "ポップコーン、昨日も食べたけど\x01",
            "やっぱりおいしーね！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "もともとトウモロコシだなんて\x01",
            "信じられなーい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217B")

    label("loc_1F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_217B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211B")

    #C0041
    ChrTalk(
        0xFE,
        (
            "あ、ロイドくんにエリィちゃんに\x01",
            "ティオちゃんにランディくんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "今日は記念祭で遊ぶの？\x01",
            "ミミたちといっしょに遊ぶ？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#0000Fああ、誘ってくれて悪いけど\x01",
            "今日は仕事なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "ふーん、\x01",
            "とくむしれ#2R・#んかも大変だねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#0106Fミ、ミミちゃん……\x01",
            "私たちの名前を覚えてくれたのは\x01",
            "すごく嬉しいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#0200F特務しれん課……\x01",
            "まぁ、試練の多い課であることは\x01",
            "否定できかねますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0306F洒落になってねぇぞ\x01",
            "ティオすけ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_217B")

    label("loc_211B")


    #C0048
    ChrTalk(
        0xFE,
        (
            "あたしはこれから\x01",
            "お父さんと色々な店を\x01",
            "見て回るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "そっちはお仕事がんばってねー。\x02",
    )

    CloseMessageWindow()

    label("loc_217B")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A4E end

    def Function_11_217F(): pass

    label("Function_11_217F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_226C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221F")

    #C0050
    ChrTalk(
        0xFE,
        (
            "今日は歓楽街で遊んだ後\x01",
            "港湾公園の出店をもう一回りして\x01",
            "夜はミシュラムで花火を見るの。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "記念祭は最後まで楽しまないとね～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2267")

    label("loc_221F")


    #C0052
    ChrTalk(
        0xFE,
        "今日は家族で回る予定なの。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "記念祭は最後まで楽しまないとね～。\x02",
    )

    CloseMessageWindow()

    label("loc_2267")

    Jump("loc_2551")

    label("loc_226C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_22CD")

    #C0054
    ChrTalk(
        0xFE,
        "パレードは中々の物だったわね。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "うんうん、今年の\x01",
            "記念祭もマンゾクしたわ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2551")

    label("loc_22CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_239E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2343")

    #C0056
    ChrTalk(
        0xFE,
        "ふう、朝からお腹いっぱいよ。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "これは記念祭中に\x01",
            "全部の出店を回るのは無理かもね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2399")

    label("loc_2343")


    #C0058
    ChrTalk(
        0xFE,
        (
            "クロスベルの街中に\x01",
            "出店が出てるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "やっぱり全部\x01",
            "回るなんて無理よね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2399")

    Jump("loc_2551")

    label("loc_239E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2420")

    #C0060
    ChrTalk(
        0xFE,
        (
            "さっき観光客の人にぶつかって\x01",
            "ジュースかけられちゃったの！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "うー、帰って着替えないと\x01",
            "シミになっちゃうわ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2551")

    label("loc_2420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2492")

    #C0062
    ChrTalk(
        0xFE,
        (
            "昨日は友達の家に泊まって\x01",
            "一晩中まくら投げをしたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "ふ～、楽しかった。\x01",
            "記念祭サイコー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2551")

    label("loc_2492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2551")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2522")

    #C0064
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "港湾公園の方にも出店が\x01",
            "たくさん出てたわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "時間があるなら見てきたら？\x01",
            "これ、結構イケルわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2551")

    label("loc_2522")


    #C0066
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "次はどこを見に行こうかな～♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2551")

    TalkEnd(0xFE)
    Return()

    # Function_11_217F end

    def Function_12_2555(): pass

    label("Function_12_2555")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25E9")
    Jump("loc_2633")

    label("loc_25E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2609")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2633")

    label("loc_2609")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2629")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2633")

    label("loc_2629")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2633")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_27D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273E")

    #C0067
    ChrTalk(
        0xFE,
        (
            "ミシュラム保養地では、\x01",
            "毎年最終日に特大の花火を\x01",
            "上げることになっておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "わしも去年はミシュラムで\x01",
            "記念祭の最終日を過ごしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "普段の夜の部とは\x01",
            "比べ物にならんほど\x01",
            "素晴らしい光景じゃぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_27D0")

    label("loc_273E")


    #C0070
    ChrTalk(
        0xFE,
        (
            "せっかくの記念祭じゃ、\x01",
            "若いものがこんな所で\x01",
            "油を売っていてどうする。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "ミシュラムへ\x01",
            "記念祭最終日限定の特大花火でも\x01",
            "見物にいくとよかろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D0")

    Jump("loc_2B55")

    label("loc_27D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_28A0")

    #C0072
    ChrTalk(
        0xFE,
        (
            "今年のパレードは去年のものより\x01",
            "幾分か長かったようじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "時間をかけて、多くの市民に\x01",
            "見せようとしていたようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "今年の記念祭で最も力を入れた\x01",
            "催しだったのかもしれぬのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B55")

    label("loc_28A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2954")

    #C0075
    ChrTalk(
        0xFE,
        (
            "パレードに使われる車両を\x01",
            "見てきたわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "今年は去年よりも１台多い、\x01",
            "７台もの導力車で\x01",
            "順路を巡るそうじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "さぞ、豪華なパレードに\x01",
            "なるに違いないのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B55")

    label("loc_2954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_29D9")

    #C0078
    ChrTalk(
        0xFE,
        "ほっほっほ、楽しんでおるかな？\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "いくら仕事といえど、楽しまねば損じゃぞ。\x01",
            "年に一度の創立記念祭なのじゃからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B55")

    label("loc_29D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2A76")

    #C0080
    ChrTalk(
        0xFE,
        (
            "しかし、今年の記念祭は\x01",
            "例年に増して華やかじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "これも、年々右肩上がりに\x01",
            "景気を良くしているクロスベルの姿を\x01",
            "表しているといえよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B55")

    label("loc_2A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2B55")

    #C0082
    ChrTalk(
        0xFE,
        (
            "昨日、マクダエル市長は\x01",
            "開会式の壇上に立った訳だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "秘書による暗殺事件にあったと聞いたが、\x01",
            "思うたより元気そうでよかったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "老いてなお折れぬ\x01",
            "強い芯があるからこそ、\x01",
            "マクダエル市長というものじゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B55")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_2555 end

    def Function_13_2B5D(): pass

    label("Function_13_2B5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2BC3")

    #C0085
    ChrTalk(
        0xFE,
        (
            "なんとか出店を\x01",
            "回りきれちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "……体重計に乗るのが怖いわ、あたし。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB0")

    label("loc_2BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2C33")

    #C0087
    ChrTalk(
        0xFE,
        (
            "んー、アイスクリームも\x01",
            "なかなかよかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "やっぱあたしは\x01",
            "そこのポップコーンかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB0")

    label("loc_2C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2CA9")

    #C0089
    ChrTalk(
        0xFE,
        (
            "ねー、今日まで回った出店で\x01",
            "どこが一番美味しかった？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "あたしはやっぱ、\x01",
            "そこのハンバーガーかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB0")

    label("loc_2CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2D01")

    #C0091
    ChrTalk(
        0xFE,
        (
            "……ねぇ、やっぱり\x01",
            "こういう賑やかなイベント事は\x01",
            "彼氏と回りたくない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB0")

    label("loc_2D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2D58")

    #C0092
    ChrTalk(
        0xFE,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "……あー、出店ばっか回ってたら\x01",
            "絶対太るわ、これ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB0")

    label("loc_2D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2DB0")

    #C0094
    ChrTalk(
        0xFE,
        "ね、次どこ行く？\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "中央広場ばっかぶらぶらするの\x01",
            "なんだか飽きちゃった。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB0")

    TalkEnd(0xFE)
    Return()

    # Function_13_2B5D end

    def Function_14_2DB4(): pass

    label("Function_14_2DB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2E16")

    #C0096
    ChrTalk(
        0xFE,
        "ん～同感。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "でも、現実を知らずに太り続ける方が\x01",
            "もっと怖いと思うけど～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3016")

    label("loc_2E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2EA9")

    #C0098
    ChrTalk(
        0xFE,
        (
            "ちょっと、さっきは\x01",
            "ハンバーガーが良かったって\x01",
            "言ってなかった～？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "ま、あたしはやっぱり\x01",
            "アイスクリームが一番だと思うけど～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3016")

    label("loc_2EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2F18")

    #C0100
    ChrTalk(
        0xFE,
        "え～！？　断然アイスクリームでしょ！\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "……わかった、後でまた\x01",
            "食べくらべてみましょ～よ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3016")

    label("loc_2F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2F4C")

    #C0102
    ChrTalk(
        0xFE,
        "……それは言わない約束でしょ～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3016")

    label("loc_2F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2FB8")

    #C0103
    ChrTalk(
        0xFE,
        (
            "大丈夫大丈夫。\x01",
            "記念祭終わったら\x01",
            "ダイエットすればいいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "今は楽しんだもの勝ちよ～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3016")

    label("loc_2FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3016")

    #C0105
    ChrTalk(
        0xFE,
        "そうね、港湾区行ってみる？\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "昨日から、なんかライブとか\x01",
            "やってるらしいよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3016")

    TalkEnd(0xFE)
    Return()

    # Function_14_2DB4 end

    def Function_15_301A(): pass

    label("Function_15_301A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_30AD")

    #C0107
    ChrTalk(
        0xFE,
        (
            "記念採用の風船のストック、\x01",
            "今日でピッタリなくなるといいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "パーフェクトで配り終えたら\x01",
            "ボーナスが出る予定なんだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C0")

    label("loc_30AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_314C")

    #C0109
    ChrTalk(
        0xFE,
        (
            "おっと……空に飛んでった\x01",
            "風船の行方を考えてて\x01",
            "ぼうっとしちまってたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "……まあ、普通に考えたら\x01",
            "ガスが抜けて落ちちゃうんだろうけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C0")

    label("loc_314C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_327B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3211")

    #C0111
    ChrTalk(
        0xFE,
        (
            "たまに俺の配った風船が\x01",
            "空の彼方に飛んでいくのが見えるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "飛んでって飛んでって……\x01",
            "最後は女神様のもとに行き着くのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "なんてか、物寂しい光景だよな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3276")

    label("loc_3211")


    #C0114
    ChrTalk(
        0xFE,
        (
            "たまに風船が大空に向かって\x01",
            "飛んでいくのが見えるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "やっぱり女神様のもとに行くのかな……\x02",
    )

    CloseMessageWindow()

    label("loc_3276")

    Jump("loc_33C0")

    label("loc_327B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_32C3")

    #C0116
    ChrTalk(
        0xFE,
        "風船、風船～。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "楽しいよ～、フワフワ浮かぶよ～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_33C0")

    label("loc_32C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_334B")

    #C0118
    ChrTalk(
        0xFE,
        (
            "ちぇっ、どいつもこいつも\x01",
            "カップルで歩いてやがってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "俺の風船を持って、\x01",
            "その繋いだお手手を離しやがれってんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C0")

    label("loc_334B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_33C0")

    #C0120
    ChrTalk(
        0xFE,
        "はいよー、どぞどぞ！　風船だよー。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "記念祭中は\x01",
            "バイト代も割り増しなんだ。\x01",
            "こいつぁ気合が入るぜ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C0")

    TalkEnd(0xFE)
    Return()

    # Function_15_301A end

    def Function_16_33C4(): pass

    label("Function_16_33C4")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B40")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_342F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_342F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344F")
    OP_AF(0x7A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B3B")

    label("loc_344F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3463")
    Jump("loc_3B3B")

    label("loc_3463")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B3B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3753")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E5")

    #C0122
    ChrTalk(
        0x101,
        (
            "#0001Fすみません、少しお話を\x01",
            "伺ってもいいですか？\x02\x03",

            "窃盗事件について\x01",
            "捜査をしているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "ああ……何でもあちこちの店が\x01",
            "やられてるんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "ウチは大丈夫だと思うわよ。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "中央広場のど真ん中だもの！\x01",
            "このお客さんの数じゃ、\x01",
            "誰も手出しできないわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x103,
        (
            "#0200Fいや、観光客の皆さんは\x01",
            "注意しているわけではありませんし。\x02\x03",

            "逆に人ごみに\x01",
            "まぎれるという可能性が。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "大丈夫よ、絶対平気。\x01",
            "私に任せてといて！\x02",
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
        "#0104F（微妙に不安な店主さんねぇ……）\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x7)
    Jump("loc_374E")

    label("loc_36E5")


    #C0129
    ChrTalk(
        0xFE,
        "中央広場でも１店舗やられたそうね。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "あの東通りの近くにある出店よ。\x01",
            "警戒が足りなかったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374E")

    Jump("loc_3B3B")

    label("loc_3753")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3766")
    Call(0, 17)
    Jump("loc_3B3B")

    label("loc_3766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_37E3")

    #C0131
    ChrTalk(
        0xFE,
        (
            "軽い食感の\x01",
            "ポップコーンはいかがかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "今日の最終便で\x01",
            "帰っちゃうつもりだから、\x01",
            "買うならお早めにね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3B")

    label("loc_37E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_385B")

    #C0133
    ChrTalk(
        0xFE,
        (
            "あらら……持ち込んだ材料が\x01",
            "切れてきちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "丁度百貨店があるし、\x01",
            "あとで買い物にいかないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3B")

    label("loc_385B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_39AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_390B")

    #C0135
    ChrTalk(
        0xFE,
        "窃盗犯、ついに捕まったそうね！\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "ふん、やっぱり悪いコトしてると\x01",
            "天罰が下るのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "そんなにミラが欲しいなら\x01",
            "自分でお商売でも始めることね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39A5")

    label("loc_390B")


    #C0138
    ChrTalk(
        0xFE,
        (
            "この国の人達は\x01",
            "サイフのヒモがゆるいみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "前に帝国で商売したときは、\x01",
            "閑古鳥が鳴いている有様だったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "うふ、クロスベルに来て大正解ね。\x02",
    )

    CloseMessageWindow()

    label("loc_39A5")

    Jump("loc_3B3B")

    label("loc_39AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3A46")

    #C0141
    ChrTalk(
        0xFE,
        (
            "思ったとおり、\x01",
            "観光をしてるヒマが\x01",
            "まったく作れないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "うふ、喜ばしいことだわ。\x01",
            "忙しいということは\x01",
            "繁盛してるということですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3B")

    label("loc_3A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3AC2")

    #C0143
    ChrTalk(
        0xFE,
        (
            "香ばしくておいしい\x01",
            "ポップコーン、売れ行き好調よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "お買い上げの際には\x01",
            "こぼさないように気を付けてね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3B")

    label("loc_3AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3B3B")

    #C0145
    ChrTalk(
        0xFE,
        (
            "おいしいおいしい\x01",
            "ポップコーンはいかがかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "劇やライブを見に行くなら\x01",
            "これほど最適なお供はないわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B3B")

    Jump("loc_33D1")

    label("loc_3B40")

    TalkEnd(0xFE)
    Return()

    # Function_16_33C4 end

    def Function_17_3B44(): pass

    label("Function_17_3B44")


    #C0147
    ChrTalk(
        0xFE,
        (
            "おいしいおいしい\x01",
            "ポップコーンはいかがかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "私のポップコーンは\x01",
            "とっても工夫を重ねているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "だからおいしいのよ。\x01",
            "あなた達も試してみてね。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1CA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0151
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x14)
    Return()

    # Function_17_3B44 end

    def Function_18_3C55(): pass

    label("Function_18_3C55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C7F")
    Call(0, 44)
    Return()

    label("loc_3C7F")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C8C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_433E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CEA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3CEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0A")
    OP_AF(0x78)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4339")

    label("loc_3D0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D1E")
    Jump("loc_4339")

    label("loc_3D1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4339")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DB5")

    #C0152
    ChrTalk(
        0xFE,
        "君は……確か警察の。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "話は聞いた……\x01",
            "窃盗犯を捕まえたらしいじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E0A")

    label("loc_3DB5")


    #C0154
    ChrTalk(
        0xFE,
        "君たちは……確か警察の。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "話は聞いた……\x01",
            "窃盗犯を捕まえたらしいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E0A")


    #C0156
    ChrTalk(
        0xFE,
        (
            "凄いな……これで\x01",
            "安心して店が続けられるよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "よかったらこれ、\x01",
            "持って行ってくれ……\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1AE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1AE, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EEF")

    #C0159
    ChrTalk(
        0x101,
        "#0002Fはは……ありがとうございます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F11")

    label("loc_3EEF")


    #C0160
    ChrTalk(
        0x103,
        "#0203Fありがとうございます。\x02",
    )

    CloseMessageWindow()

    label("loc_3F11")


    #C0161
    ChrTalk(
        0xFE,
        (
            "礼を言うのはこちらの方だ……\x01",
            "どうもありがとうな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBC, 6)
    Jump("loc_4339")

    label("loc_3F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3FBF")

    #C0162
    ChrTalk(
        0xFE,
        "ハンバーガー……おいしいよ。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "ある程度保存も利くし、\x01",
            "よかったら……沢山買ってくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4339")

    label("loc_3FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4050")

    #C0164
    ChrTalk(
        0xFE,
        (
            "……最近、共和国のほうでは\x01",
            "リブサンドとかケバブサンドとかも\x01",
            "流行ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "……僕はハンバーガーのほうが\x01",
            "好きだけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4339")

    label("loc_4050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_41EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_40B7")

    #C0166
    ChrTalk(
        0xFE,
        (
            "ようやく安心して\x01",
            "店を続けられる……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "君たち、どうもありがとうな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_41EA")

    label("loc_40B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4170")

    #C0168
    ChrTalk(
        0xFE,
        (
            "こんな大都会で\x01",
            "出店をやるのは、初めてでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "盗みに遭ったのも\x01",
            "今日が初めてなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "いつの間に盗まれたのか……\x01",
            "まったく、今もって謎だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41EA")

    label("loc_4170")


    #C0171
    ChrTalk(
        0xFE,
        "ハンバーガー……売ってるよ。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "作るのも決して難しくないし、\x01",
            "出来そうだと思ったら\x01",
            "自分で作ってみるのもいいかもね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41EA")

    Jump("loc_4339")

    label("loc_41EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4264")

    #C0173
    ChrTalk(
        0xFE,
        "景気のいい場所だ、クロスベル……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "僕のような集客下手の店にも\x01",
            "たくさんのお客が来るんだからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4339")

    label("loc_4264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_42CB")

    #C0175
    ChrTalk(
        0xFE,
        "ハンバーガー……どうだね？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "……無理にとは言わない。\x01",
            "気が向いたら買ってくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4339")

    label("loc_42CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4339")

    #C0177
    ChrTalk(
        0xFE,
        "ハンバーガー……食べるかい？\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "肉と野菜と炭水化物のハーモニー……\x01",
            "絶妙なジャンクフードだぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4339")

    Jump("loc_3C8C")

    label("loc_433E")

    TalkEnd(0xFE)
    Return()

    # Function_18_3C55 end

    def Function_19_4342(): pass

    label("Function_19_4342")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_434F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D77")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43AD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_43AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43CD")
    OP_AF(0x79)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D72")

    label("loc_43CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43E1")
    Jump("loc_4D72")

    label("loc_43E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D72")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46A5")

    #C0179
    ChrTalk(
        0xFE,
        (
            "あらぁ、さっき助けてくれた\x01",
            "警察の人じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "さっきどうもありがとぉ。\x01",
            "お陰で被害に遭わずに済んだわぁ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_44D0")

    #C0181
    ChrTalk(
        0x101,
        "#0002Fはは、あれは危ない所でしたね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_44FA")

    label("loc_44D0")


    #C0182
    ChrTalk(
        0x101,
        "#0012Fはは、あれは危ない所でしたね。\x02",
    )

    CloseMessageWindow()

    label("loc_44FA")

    Jump("loc_4583")

    label("loc_44FF")


    #C0183
    ChrTalk(
        0x101,
        "#0000Fはは、危ない所でした。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_455D")

    #C0184
    ChrTalk(
        0x104,
        "#0304Fま、全てお見通しだったけどな！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4583")

    label("loc_455D")


    #C0185
    ChrTalk(
        0x104,
        "#0303Fまさに油断大敵って奴だな。\x02",
    )

    CloseMessageWindow()

    label("loc_4583")


    #C0186
    ChrTalk(
        0xFE,
        (
            "これ、持ってって頂戴～。\x01",
            "ほんのお礼よぉ㈱\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1C0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1C0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4644")

    #C0188
    ChrTalk(
        0x101,
        (
            "#0000Fありがとうございます。\x01",
            "頂いておきますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_466E")

    label("loc_4644")


    #C0189
    ChrTalk(
        0x102,
        "#0100Fありがとう、頂いておきますね。\x02",
    )

    CloseMessageWindow()

    label("loc_466E")


    #C0190
    ChrTalk(
        0xFE,
        (
            "うふふ、警察の人も\x01",
            "お仕事頑張ってねぇん㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 0)
    Jump("loc_4D72")

    label("loc_46A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4735")

    #C0191
    ChrTalk(
        0xFE,
        (
            "ああん、さびしいわぁ。\x01",
            "今日でお祭りがおしまいなんてぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "来年もスイーツ屋台で来るから、\x01",
            "あたしのことわすれないでよねぇ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D72")

    label("loc_4735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_47A5")

    #C0193
    ChrTalk(
        0xFE,
        "カロリー控えめなんて幻想よぉ。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "それでも、\x01",
            "本当に甘いものが好きなら\x01",
            "食べちゃうわよねぇ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D72")

    label("loc_47A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4BF2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4829")

    #C0195
    ChrTalk(
        0xFE,
        (
            "さっきはどうもありがとぉ。\x01",
            "お陰で被害に遭わずに済んだわぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "警察の人も\x01",
            "意外と頼りになるのねぇ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BED")

    label("loc_4829")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B88")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AD9")

    #C0197
    ChrTalk(
        0x101,
        (
            "#0001Fすみません、少しお話を\x01",
            "伺ってもいいですか？\x02\x03",

            "窃盗事件について\x01",
            "捜査をしているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "ああ、窃盗の話ね～。\x01",
            "商工会の人が気を付けるように\x01",
            "言って来たわ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x104,
        (
            "#0300F中央広場でもやられたそうッスけど。\x02\x03",

            "何か心当たりとかは無いッスか？\x01",
            "逃げる犯人を目撃したとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "ないわね～㈱\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "ウチは大繁盛なの。\x01",
            "お商売に忙しいから\x01",
            "他の店まで気にしてられないわ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#0006Fそ、そうですか……\x02",
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
            "#0008Fたしかに、百貨店の前だし\x01",
            "裏通りのすぐ傍だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "おまけにそこの通りは\x01",
            "行政区に続いてるのよ～㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "今日なんてパレードを見に来た客が\x01",
            "沢山なんだから～㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        "#0103Fお、お忙しいみたいね。\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x8)
    Jump("loc_4B83")

    label("loc_4AD9")


    #C0207
    ChrTalk(
        0xFE,
        "窃盗犯に心当たりは無いわね～。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "むしろ来るなら来なさいってカンジ？\x01",
            "あたしがとっ捕まえてあげるからぁ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#0006Fうーん、民間人に\x01",
            "無理はしないで欲しいんですが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B83")

    Jump("loc_4BED")

    label("loc_4B88")


    #C0210
    ChrTalk(
        0xFE,
        "甘くて美味しいスイーツはいかがぁ？\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "お祭りで歩き疲れてるなら\x01",
            "体力回復にもってこいかもねぇ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BED")

    Jump("loc_4D72")

    label("loc_4BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4C72")

    #C0212
    ChrTalk(
        0xFE,
        (
            "こんなお店をやってるけど、\x01",
            "あたしは控えめな甘さが\x01",
            "好みなのよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "ただ甘いだけのお菓子なんて……ねぇ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D72")

    label("loc_4C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4CE1")

    #C0214
    ChrTalk(
        0xFE,
        (
            "やっぱりぃ、\x01",
            "女の子のお客さんが\x01",
            "多いのよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "女の子は大体、\x01",
            "甘い物大好きだものねぇ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D72")

    label("loc_4CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4D72")

    #C0216
    ChrTalk(
        0xFE,
        (
            "こんにちはぁ、\x01",
            "スイーツ屋台へようこそぉ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "……あらぁ、男女４人で……\x01",
            "ダブルデートってやつぅ？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "お姉さん、羨ましいわぁ～㈱\x02",
    )

    CloseMessageWindow()

    label("loc_4D72")

    Jump("loc_434F")

    label("loc_4D77")

    TalkEnd(0xFE)
    Return()

    # Function_19_4342 end

    def Function_20_4D7B(): pass

    label("Function_20_4D7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4D8C")
    Jump("loc_4E4F")

    label("loc_4D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4DCD")

    #C0219
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませー！\x01",
            "お食事はいかがですか～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E4F")

    label("loc_4DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E46")

    #C0220
    ChrTalk(
        0xFE,
        (
            "こんにちは～！\x01",
            "お食事はいかがですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "ウチも客引きを\x01",
            "始めてみたんです。\x01",
            "かきいれ時ですものね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E4F")

    label("loc_4E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4E4F")

    label("loc_4E4F")

    TalkEnd(0xFE)
    Return()

    # Function_20_4D7B end

    def Function_21_4E53(): pass

    label("Function_21_4E53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4FF2")
    OP_93(0xFE, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F78")
    OP_4B(0x14, 0xFF)

    #C0222
    ChrTalk(
        0xFE,
        (
            "え～、ミシュラム行こうぜ、\x01",
            "ミシュラム～！\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "ホテルに泊まってさぁ\x01",
            "テーマパークで遊ぼうぜっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x14,
        (
            "バ、バカモン。\x01",
            "ミシュラムのホテルが\x01",
            "いくらすると思っとるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x14,
        (
            "今日は閉会式を見るんじゃ。\x01",
            "リュウ、あまり\x01",
            "うろちょろするんじゃないぞ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    SetScenarioFlags(0x0, 6)
    Jump("loc_4FED")

    label("loc_4F78")


    #C0226
    ChrTalk(
        0xFE,
        (
            "ぶーぶー、閉会式なんて\x01",
            "ジミすぎだってのー！\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "姉ちゃんも誘ってさぁ\x01",
            "ミシュラム行こうぜ、\x01",
            "なあ父ちゃん～……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FED")

    Jump("loc_5645")

    label("loc_4FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_50D0")
    OP_93(0xFE, 0x5A, 0x0)
    OP_4B(0x14, 0xFF)

    #C0228
    ChrTalk(
        0xFE,
        (
            "なあ父ちゃん、\x01",
            "あれ買ってくれよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "あとジュースとポップコーン！\x01",
            "へへっ、祭りなんだしさぁ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x14,
        "わはは、そいつはよいな……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x14,
        (
            "……って、調子に乗りすぎじゃ！\x01",
            "少しは遠慮せんかい！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_5645")

    label("loc_50D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52FB")

    #C0232
    ChrTalk(
        0x101,
        (
            "#0003F（一応リュウにも\x01",
            "  聞いてみるか……）\x02\x03",

            "#0000Fちょっといいか？\x01",
            "男の子を捜してるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0234
    ChrTalk(
        0xFE,
        "へー、こいつ迷子なワケ？\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "そういや見たような、\x01",
            "見てないような……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x160,
        (
            "#3306F随分と曖昧なのね。\x02\x03",

            "#3300Fくす……男なら\x01",
            "ハッキリしたらどうかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        "うぐ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0238
    ChrTalk(
        0xFE,
        (
            "そ、そういや\x01",
            "ちらっと見たかもなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "パレードに夢中だったしさ、\x01",
            "コドモなんてあんま見てねえけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#0000Fそうか……\x01",
            "ありがとう、助かったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 36)
    Jump("loc_5410")

    label("loc_52FB")


    #C0241
    ChrTalk(
        0xFE,
        (
            "パレードに夢中だったし\x01",
            "あんま見てなかったけど、\x01",
            "そういや見かけた気がするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "……ところで\x01",
            "そのオンナ、誰なんだ～？\x01",
            "ナマイキな感じだな～！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x160,
        (
            "#3302Fクスクス……レディに\x01",
            "そんな口の利き方をして\x01",
            "いいのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#0012F（はは……\x01",
            "  リュウには少し荷が重い相手かな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5410")

    Jump("loc_5645")

    label("loc_5415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5494")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0245
    ChrTalk(
        0xFE,
        (
            "うっひょお……\x01",
            "すっげかったなぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "へへっ、姉ちゃんも\x01",
            "見にくりゃよかったのにさ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5645")

    label("loc_5494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_54E8")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0247
    ChrTalk(
        0xFE,
        (
            "うおぉ～……\x01",
            "パレード、早く来ねえかな～っ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5645")

    label("loc_54E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5561")
    OP_93(0xFE, 0x0, 0x0)

    #C0248
    ChrTalk(
        0xFE,
        (
            "なー父ちゃん、\x01",
            "百貨店行こうぜ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "商売先だっていいじゃん！\x01",
            "シジョーチョーサってやつだよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5645")

    label("loc_5561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_55B3")
    OP_93(0xFE, 0x0, 0x0)

    #C0250
    ChrTalk(
        0xFE,
        (
            "あ、百貨店がセールやってる。\x01",
            "父ちゃん、見ていこうぜっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5645")

    label("loc_55B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5645")

    #C0251
    ChrTalk(
        0xFE,
        "あ、支援課お兄ちゃんたちだ。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "祭りの日にパトかよ。\x01",
            "へへっ、残念だな～！\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#0000Fはいはい。\x01",
            "……あんまり\x01",
            "はしゃぎすぎるなよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5645")

    TalkEnd(0xFE)
    Return()

    # Function_21_4E53 end

    def Function_22_5649(): pass

    label("Function_22_5649")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_56C0")

    #C0254
    ChrTalk(
        0xFE,
        (
            "今日は午後から\x01",
            "祭りの閉会式があるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "市民として、締めくくりに\x01",
            "見にいかんとな、わはは！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_584C")

    label("loc_56C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5724")

    #C0256
    ChrTalk(
        0xFE,
        "わはは、やはり祭りは良いな。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "パレードは\x01",
            "クロスベル人の心じゃ、\x01",
            "わはははは！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_584C")

    label("loc_5724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_578F")

    #C0258
    ChrTalk(
        0xFE,
        (
            "リュウ、パレードの車が来たら\x01",
            "ピースをするんじゃ！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "写真にとってやるからな、わはは！\x02",
    )

    CloseMessageWindow()
    Jump("loc_584C")

    label("loc_578F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_57D3")
    OP_93(0xFE, 0x0, 0x0)

    #C0260
    ChrTalk(
        0xFE,
        (
            "……リュウ、お前意外と\x01",
            "言葉を知ってるな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_584C")

    label("loc_57D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5823")
    OP_93(0xFE, 0x0, 0x0)

    #C0261
    ChrTalk(
        0xFE,
        (
            "うっ……祭りの日にまで\x01",
            "商売先に顔を出したくないわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_584C")

    label("loc_5823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_584C")

    #C0262
    ChrTalk(
        0xFE,
        "わはは、めでたいですなぁ！\x02",
    )

    CloseMessageWindow()

    label("loc_584C")

    TalkEnd(0xFE)
    Return()

    # Function_22_5649 end

    def Function_23_5850(): pass

    label("Function_23_5850")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58C0")

    #C0263
    ChrTalk(
        0xFE,
        (
            "ウェンディはこの辺りの\x01",
            "店に勤めているんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        "折角だから見ていこうじゃないか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_58F5")

    label("loc_58C0")


    #C0265
    ChrTalk(
        0xFE,
        (
            "どーれ、わが娘の\x01",
            "働く姿を拝ませてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58F5")

    TalkEnd(0xFE)
    Return()

    # Function_23_5850 end

    def Function_24_58F9(): pass

    label("Function_24_58F9")

    TalkBegin(0xFE)

    #C0266
    ChrTalk(
        0xFE,
        "えー、百貨店に行きたい～！\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "おねーちゃんの様子なんて\x01",
            "いつでも見に来れるじゃな～い。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_58F9 end

    def Function_25_595D(): pass

    label("Function_25_595D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59EE")
    OP_4B(0x18, 0xFF)

    #C0268
    ChrTalk(
        0xFE,
        (
            "きゃ～見て見てメイファちゃん。\x01",
            "出店がでてるよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "わたしアレ食べたーい！\x01",
            "買って買って！\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x18,
        "自分で買えっ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x18, 0xFF)
    Jump("loc_5A21")

    label("loc_59EE")


    #C0271
    ChrTalk(
        0xFE,
        (
            "ねぇ、メイファちゃんってば。\x01",
            "アレ買ってよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A21")

    TalkEnd(0xFE)
    Return()

    # Function_25_595D end

    def Function_26_5A25(): pass

    label("Function_26_5A25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ACB")
    TurnDirection(0xFE, 0x0, 0)

    #C0272
    ChrTalk(
        0xFE,
        (
            "休暇が取れたから\x01",
            "ウルスラ病院から遊びに来たのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "日々の看護師生活で\x01",
            "溜まりに溜まった疲れ……\x01",
            "今日一日でぶっとばすわよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x87, 0x0)
    SetScenarioFlags(0x1, 1)
    Jump("loc_5B45")

    label("loc_5ACB")


    #C0274
    ChrTalk(
        0xFE,
        (
            "……あーもう、うるっさい！\x01",
            "子供みたいにハシャがないの！\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "ったく、折角の休日なのに\x01",
            "なんでシロンのお守りなんか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B45")

    TalkEnd(0xFE)
    Return()

    # Function_26_5A25 end

    def Function_27_5B49(): pass

    label("Function_27_5B49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5C4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BCD")

    #C0276
    ChrTalk(
        0xFE,
        (
            "駅の方には遊撃士の人が\x01",
            "回ってくれているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "……やっぱり……\x01",
            "遊撃士の人って頼りになるわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5C49")

    label("loc_5BCD")


    #C0278
    ChrTalk(
        0xFE,
        (
            "遊撃士の人って手際が良くて、\x01",
            "市民の事もちゃんと見てるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "やっぱり頼りになるのよね。\x01",
            "警察官としては複雑だけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C49")

    Jump("loc_6065")

    label("loc_5C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5C5C")
    Jump("loc_6065")

    label("loc_5C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5C6A")
    Jump("loc_6065")

    label("loc_5C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5CF1")
    OP_93(0xFE, 0xC5, 0x0)

    #C0280
    ChrTalk(
        0xFE,
        (
            "ピッピー、ピッピーッ！\x01",
            "導力車は徐行してくださ～い。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "路上にいらっしゃる方は\x01",
            "どうか道を空けてくださーい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6065")

    label("loc_5CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6065")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5DA2")

    #C0282
    ChrTalk(
        0xFE,
        "あ、お疲れ様～。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "開会式があった\x01",
            "初日ほどじゃないけど……\x01",
            "やっぱり大した人出だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "これは本部に応援を頼んだ方が\x01",
            "いいかもしれないわね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6065")

    label("loc_5DA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_5FCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_5E73")

    #C0285
    ChrTalk(
        0x19,
        (
            "駐車車両は街の\x01",
            "西口と東口に集中してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x19,
        (
            "全部の車両を調べ終わったら\x01",
            "本部受付のレベッカさんに\x01",
            "声を掛けてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x19,
        (
            "私たち……ちょっと忙しくて\x01",
            "手が離せそうにないのよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FC9")

    label("loc_5E73")


    #C0288
    ChrTalk(
        0x19,
        (
            "違法駐車の件は\x01",
            "ホントは私たち新人警官が\x01",
            "やるはずだったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x19,
        "いろいろ忙しくって……ごめんね。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#0000Fはは、大丈夫です。\x01",
            "こっちで引き受けますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x19,
        "ありがと、それと……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x19,
        (
            "車両に貼る警告ステッカーは\x01",
            "一度貼りつけると中々取れないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x19,
        (
            "間違って貼らないように\x01",
            "気をつけてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        "#0300F了解、任せてくださいッス！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_5FC9")

    Jump("loc_6065")

    label("loc_5FCE")


    #C0295
    ChrTalk(
        0xFE,
        "あ、お疲れ様～。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "開会式があった\x01",
            "初日ほどじゃないけど……\x01",
            "やっぱり大した人出だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "これは本部に応援を頼んだ方が\x01",
            "いいかもしれないわね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6065")

    TalkEnd(0xFE)
    Return()

    # Function_27_5B49 end

    def Function_28_6069(): pass

    label("Function_28_6069")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_60EA")

    #C0298
    ChrTalk(
        0xFE,
        (
            "まだまだ楽しめそうだから、\x01",
            "滞在期間を４日ほど延長したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "これでのーんびり\x01",
            "遊ぶことが出来そうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6229")

    label("loc_60EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6159")

    #C0300
    ChrTalk(
        0xFE,
        (
            "行き当たりばったりで観光していたら\x01",
            "目的がなくなってしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        "今日はなにをしようか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6229")

    label("loc_6159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_61D6")

    #C0302
    ChrTalk(
        0xFE,
        (
            "昨日は賑やかだった港湾区に\x01",
            "行ってきてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "ガラは悪かったが\x01",
            "不良グループというのも\x01",
            "なかなかやるねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6229")

    label("loc_61D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6229")

    #C0304
    ChrTalk(
        0xFE,
        "彼女とハネムーンに来たのだよ。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        "沢山の思い出が出来るといいねぇ。\x02",
    )

    CloseMessageWindow()

    label("loc_6229")

    TalkEnd(0xFE)
    Return()

    # Function_28_6069 end

    def Function_29_622D(): pass

    label("Function_29_622D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_629C")

    #C0306
    ChrTalk(
        0xFE,
        (
            "ちょっと長くなってしまうけど……\x01",
            "一生に一度のハネムーンだもの、\x01",
            "もっと楽しみたいわよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6353")

    label("loc_629C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_62E3")

    #C0307
    ChrTalk(
        0xFE,
        (
            "もう、だからツアープランに\x01",
            "しようって言ったのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6353")

    label("loc_62E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6315")

    #C0308
    ChrTalk(
        0xFE,
        "男の人ってああいうの好きよね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6353")

    label("loc_6315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6353")

    #C0309
    ChrTalk(
        0xFE,
        (
            "ふふ、楽しみだわ。\x01",
            "前から来てみたかったのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6353")

    TalkEnd(0xFE)
    Return()

    # Function_29_622D end

    def Function_30_6357(): pass

    label("Function_30_6357")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_63D6")

    #C0310
    ChrTalk(
        0xFE,
        (
            "ああ、もうすぐ帰りの列車が\x01",
            "出てしまうじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "だがもう少し……\x01",
            "もう少しだけこの街を見ていたい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6531")

    label("loc_63D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6459")

    #C0312
    ChrTalk(
        0xFE,
        (
            "オーバルストア！\x01",
            "あそこは斬新だった！\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "あんな種類の導力器が\x01",
            "エレガントに展示されている様は\x01",
            "圧巻の一言だよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6531")

    label("loc_6459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_64D3")

    #C0314
    ChrTalk(
        0xFE,
        (
            "百貨店！\x01",
            "あそこは最高だった！\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "私は色々な国の商店を見てきたが、\x01",
            "ここまで大規模なものは初めてだよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6531")

    label("loc_64D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6531")

    #C0316
    ChrTalk(
        0xFE,
        "珍しい店がいっぱいあるなぁ。\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "どこから見て行けばいいか\x01",
            "目移りしてしまうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6531")

    TalkEnd(0xFE)
    Return()

    # Function_30_6357 end

    def Function_31_6535(): pass

    label("Function_31_6535")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_65CB")

    #C0318
    ChrTalk(
        0xFE,
        (
            "さて……クロスベルの料理屋も\x01",
            "あらかた回ってしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "さて、どうしたものか。\x01",
            "噂のミシュラムとやらに\x01",
            "足を運ぼうかの……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67BE")

    label("loc_65CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_669A")

    #C0320
    ChrTalk(
        0xFE,
        (
            "東通りにあった東方風の料理屋に\x01",
            "行ったのだが……いや、すばらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "あそこまで本格的なものが食えるとは\x01",
            "想像だにしておらんかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "フフ……思い出しただけでも\x01",
            "よだれが止まらんわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67BE")

    label("loc_669A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_671D")

    #C0323
    ChrTalk(
        0xFE,
        (
            "昨日もここで食事をとったのだが……\x01",
            "いや、なかなか美味じゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        "次はジャンクフード巡りでもしてみるかのう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_67BE")

    label("loc_671D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_67BE")

    #C0325
    ChrTalk(
        0xFE,
        (
            "様々な文化が入り混じった\x01",
            "クロスベル……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        (
            "ここなら、わしの舌を唸らせる\x01",
            "料理と出会えるかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        "さあて、さっそく食事をとるとしようか。\x02",
    )

    CloseMessageWindow()

    label("loc_67BE")

    TalkEnd(0xFE)
    Return()

    # Function_31_6535 end

    def Function_32_67C2(): pass

    label("Function_32_67C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_67EF")

    #C0328
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()
    Jump("loc_69CF")

    label("loc_67EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_67FD")
    Jump("loc_69CF")

    label("loc_67FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6827")

    #C0329
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()
    Jump("loc_69CF")

    label("loc_6827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6851")

    #C0330
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()
    Jump("loc_69CF")

    label("loc_6851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_69CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_697E")

    #C0331
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#0202Fなでなで……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x102,
        "#0102Fなでなで……\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#0000Fうーん、平和だなぁ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0335
    ChrTalk(
        0x104,
        (
            "#0306Fなぜここに来ると\x01",
            "全員呆けモードになるかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x103,
        (
            "#0204F仕方がありません。\x01",
            "日向ぼっこしているツァイトは\x01",
            "毛もフカフカですから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_69CF")

    label("loc_697E")


    #C0337
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x103,
        (
            "#0202F（後で骨付き肉を\x01",
            "  買って来ようかな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69CF")

    TalkEnd(0xFE)
    Return()

    # Function_32_67C2 end

    def Function_33_69D3(): pass

    label("Function_33_69D3")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x1, 3)
    Call(0, 35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A65")

    #C0339
    ChrTalk(
        0x101,
        (
            "#0004F（そういえば……\x01",
            "  エサになりそうな物があったっけ。）\x02\x03",

            "#0000F（コッペにあげても\x01",
            "  いいかもしれないな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x52, 0)

    label("loc_6A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CE4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6ADA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CDF")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "話をする")
    MenuCmd(1, 1, "エサをやる")
    MenuCmd(1, 1, "やめる")
    ClearScenarioFlags(0x1, 3)
    Call(0, 35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B2E")
    MenuCmd(3, 1, 0x1)

    label("loc_6B2E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B60")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6B60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CAA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_6BA3")
    MenuCmd(1, 1, "スノーシュラブ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BA3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_6BCA")
    MenuCmd(1, 1, "アルモリカブナ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_6BEB")
    MenuCmd(1, 1, "オロショ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BEB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_6C0A")
    MenuCmd(1, 1, "ロック")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_6C29")
    MenuCmd(1, 1, "カルプ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_6C4A")
    MenuCmd(1, 1, "レイニー")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C4A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_6C6B")
    MenuCmd(1, 1, "エーゼル")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_6C8C")
    MenuCmd(1, 1, "カサギン")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C8C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_6CAF")
    MenuCmd(1, 1, "レインボウ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CAF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_6CD0")
    MenuCmd(1, 1, "トラード")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_6CF1")
    MenuCmd(1, 1, "サモーナ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_6D10")
    MenuCmd(1, 1, "イール")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D10")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_6D35")
    MenuCmd(1, 1, "パールグラス")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_6D5A")
    MenuCmd(1, 1, "グラトンバス")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_6D81")
    MenuCmd(1, 1, "バイパーヘッド")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D81")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_6DA8")
    MenuCmd(1, 1, "パイソンヘッド")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DA8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_6DC9")
    MenuCmd(1, 1, "タイタン")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_6DEE")
    MenuCmd(1, 1, "クインシザー")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_6E13")
    MenuCmd(1, 1, "エレキイール")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E13")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_6E3A")
    MenuCmd(1, 1, "デモンタイタン")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_6E61")
    MenuCmd(1, 1, "アークシュラブ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_6E88")
    MenuCmd(1, 1, "ゴルドサモーナ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_6EAF")
    MenuCmd(1, 1, "ノーブルカルプ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EAF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_6ED8")
    MenuCmd(1, 1, "サーペントヘッド")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6ED8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_6EFB")
    MenuCmd(1, 1, "ねこまんま")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EFB")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F45")
    Jump("loc_7C9B")

    label("loc_6F45")

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
        "にゃんにゃん……㈱\x02",
    )

    CloseMessageWindow()

    def lambda_700F():

        label("loc_700F")

        TurnDirection(0x0, 0x1F, 0)
        Yield()
        Jump("loc_700F")

    QueueWorkItem2(0x0, 1, lambda_700F)

    def lambda_7021():

        label("loc_7021")

        TurnDirection(0x1, 0x1F, 0)
        Yield()
        Jump("loc_7021")

    QueueWorkItem2(0x1, 1, lambda_7021)

    def lambda_7033():

        label("loc_7033")

        TurnDirection(0x2, 0x1F, 0)
        Yield()
        Jump("loc_7033")

    QueueWorkItem2(0x2, 1, lambda_7033)

    def lambda_7045():

        label("loc_7045")

        TurnDirection(0x3, 0x1F, 0)
        Yield()
        Jump("loc_7045")

    QueueWorkItem2(0x3, 1, lambda_7045)

    def lambda_7057():

        label("loc_7057")

        TurnDirection(0x4, 0x1F, 0)
        Yield()
        Jump("loc_7057")

    QueueWorkItem2(0x4, 1, lambda_7057)

    def lambda_7069():

        label("loc_7069")

        TurnDirection(0x5, 0x1F, 0)
        Yield()
        Jump("loc_7069")

    QueueWorkItem2(0x5, 1, lambda_7069)
    SetChrFlags(0x1F, 0x8000)
    OP_93(0x1F, 0x0, 0x1F4)
    Sleep(50)
    ClearChrFlags(0x1F, 0x1)
    Sound(814, 0, 80, 0)

    def lambda_7095():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x708, 0x1F40)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7095)
    WaitChrThread(0x1F, 1)
    Sound(814, 0, 80, 0)

    def lambda_70BC():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1130, 0x1388)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_70BC)
    WaitChrThread(0x1F, 1)
    Sound(854, 0, 80, 0)

    def lambda_70E3():
        OP_9D(0xFE, 0xFFFFA75E, 0x514, 0xFFFFDFBC, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_70E3)
    WaitChrThread(0x1F, 1)
    Sleep(2000)
    OP_93(0x1F, 0xB4, 0x1F4)
    Sound(814, 0, 80, 0)

    def lambda_7114():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1194, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7114)
    WaitChrThread(0x1F, 1)
    Sound(814, 0, 80, 0)

    def lambda_713B():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_713B)
    WaitChrThread(0x1F, 1)
    Sound(854, 0, 80, 0)

    def lambda_7162():
        OP_9D(0xFE, 0xFFFFAA24, 0x514, 0xFFFFB49C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7162)
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
        "ふにゃ～……\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_7236")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_722C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15E, 1)

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x70),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x70, 1)

    label("loc_722C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7236")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_7284")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_727A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15F, 1)

    #A0343
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x79),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x79, 1)

    label("loc_727A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7284")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_72D2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x160, 1)

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x6A, 1)

    label("loc_72C8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_72D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_7320")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7316")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x161, 1)

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x6D, 1)

    label("loc_7316")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7320")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_736E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7364")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x162, 1)

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x73),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x73, 1)

    label("loc_7364")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_736E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_73BC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73B2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x163, 1)

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x67, 1)

    label("loc_73B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_73BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_740A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7400")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x164, 1)

    #A0348
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x8A, 1)

    label("loc_7400")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_740A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_7458")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_744E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x165, 1)

    #A0349
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x85),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x85, 1)

    label("loc_744E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7458")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_74A6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_749C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x166, 1)

    #A0350
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x99),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x99, 1)

    label("loc_749C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_74A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_74F4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74EA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x167, 1)

    #A0351
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x82, 1)

    label("loc_74EA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_74F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_7542")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7538")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x168, 1)

    #A0352
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x92),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x92, 1)

    label("loc_7538")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7542")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_7590")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7586")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x169, 1)

    #A0353
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x7F, 1)

    label("loc_7586")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7590")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_75DE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75D4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16A, 1)

    #A0354
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x76),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x76, 1)

    label("loc_75D4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_75DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_762C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7622")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16B, 1)

    #A0355
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x7C, 1)

    label("loc_7622")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_762C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_767A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7670")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16C, 1)

    #A0356
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x8B, 1)

    label("loc_7670")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_767A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_76C8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76BE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16D, 1)

    #A0357
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x8D, 1)

    label("loc_76BE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_76C8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_7716")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_770C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16E, 1)

    #A0358
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x8E, 1)

    label("loc_770C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7716")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_7764")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_775A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16F, 1)

    #A0359
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x83),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x83, 1)

    label("loc_775A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7764")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_77B2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77A8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x170, 1)

    #A0360
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0xA9, 1)

    label("loc_77A8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_77B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_7800")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77F6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x171, 1)

    #A0361
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x81),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x81, 1)

    label("loc_77F6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7800")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_784E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7844")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x172, 1)

    #A0362
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x72, 1)

    label("loc_7844")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_784E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_789C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7892")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x173, 1)

    #A0363
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x9A, 1)

    label("loc_7892")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_789C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_78EA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78E0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x174, 1)

    #A0364
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x95),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x95, 1)

    label("loc_78E0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_78EA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_7938")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_792E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x175, 1)

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0xA0, 1)

    label("loc_792E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7938")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_798A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7980")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D9, 1)

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×３を受け取った。\x02",
        )
    )

    AddItemNumber(0x12D, 3)

    label("loc_7980")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_798A")

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79B1")
    SetScenarioFlags(0x4B, 3)

    label("loc_79B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79C2")
    SetScenarioFlags(0x52, 1)

    label("loc_79C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79D3")
    SetScenarioFlags(0x52, 2)

    label("loc_79D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79E4")
    SetScenarioFlags(0x52, 3)

    label("loc_79E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79F5")
    SetScenarioFlags(0x52, 4)

    label("loc_79F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A06")
    SetScenarioFlags(0x52, 5)

    label("loc_7A06")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A17")
    SetScenarioFlags(0x52, 6)

    label("loc_7A17")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_END)), "loc_7A34")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_END)), "loc_7A47")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_END)), "loc_7A5A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_END)), "loc_7A6D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_END)), "loc_7A80")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_END)), "loc_7A93")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B10")

    #C0367
    ChrTalk(
        0xFE,
        "にゃんにゃんにゃ～ん……♪\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0xA6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0xA6, 1)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_7B10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7B50")

    #C0369
    ChrTalk(
        0x102,
        "#0105Fあら……これをくれるの？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C00")

    label("loc_7B50")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7B8E")

    #C0370
    ChrTalk(
        0x103,
        "#0205Fこれをくれるんですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C00")

    label("loc_7B8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7C00")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7BDC")

    #C0371
    ChrTalk(
        0x104,
        "#0305Fこれをくれるってのか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C00")

    label("loc_7BDC")


    #C0372
    ChrTalk(
        0x101,
        "#0005Fこれをくれるのかい……？\x02",
    )

    CloseMessageWindow()

    label("loc_7C00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C4F")

    #C0373
    ChrTalk(
        0x101,
        (
            "#0000Fはは、サンキュー。\x01",
            "ありがたく使わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C95")

    label("loc_7C4F")


    #C0374
    ChrTalk(
        0x101,
        (
            "#0000Fはは、サンキュー。\x01",
            "……でもどこから\x01",
            "持って来たんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C95")

    TalkEnd(0xFE)
    EventEnd(0x4)
    Return()

    label("loc_7C9B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7CDA")

    label("loc_7CAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CBE")
    Jump("loc_7CDA")

    label("loc_7CBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CDA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 34)

    label("loc_7CDA")

    Jump("loc_6ADA")

    label("loc_7CDF")

    Jump("loc_7CE7")

    label("loc_7CE4")

    Call(0, 34)

    label("loc_7CE7")

    TalkEnd(0x1F)
    Return()

    # Function_33_69D3 end

    def Function_34_7CEB(): pass

    label("Function_34_7CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D82")

    #C0375
    ChrTalk(
        0x1F,
        "ふにやゃ～～ご……\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x103,
        (
            "#0200F……しーっ、\x01",
            "ツァイトは眠いようです。\x01",
            "あまり構わない方がいいかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x1F,
        "ふにゃん……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 4)
    Jump("loc_7EE3")

    label("loc_7D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7DAA")

    #C0378
    ChrTalk(
        0x1F,
        "……にやぁおお～ん。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E43")

    label("loc_7DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7DB8")
    Jump("loc_7E43")

    label("loc_7DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7DD8")

    #C0379
    ChrTalk(
        0x1F,
        "にゃおん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E43")

    label("loc_7DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_7DFE")

    #C0380
    ChrTalk(
        0x1F,
        "ふにやゃ～～ご……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E43")

    label("loc_7DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7E24")

    #C0381
    ChrTalk(
        0x1F,
        "ふにやゃ～～ご……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E43")

    label("loc_7E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7E43")

    #C0382
    ChrTalk(
        0x1F,
        "……にゃおん……\x02",
    )

    CloseMessageWindow()

    label("loc_7E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EE3")

    #C0383
    ChrTalk(
        0x101,
        (
            "#0004F（コッペはずっと支援課に\x01",
            "  住み着いてる猫なんだよな……）\x02\x03",

            "#0000F（まあ気ままな奴だし、\x01",
            "  時々エサを持ってきて\x01",
            "  やってる程度だけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 3)

    label("loc_7EE3")

    Return()

    # Function_34_7CEB end

    def Function_35_7EE4(): pass

    label("Function_35_7EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_7EF2")
    SetScenarioFlags(0x1, 3)

    label("loc_7EF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_7F00")
    SetScenarioFlags(0x1, 3)

    label("loc_7F00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_7F0E")
    SetScenarioFlags(0x1, 3)

    label("loc_7F0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_7F1C")
    SetScenarioFlags(0x1, 3)

    label("loc_7F1C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_7F2A")
    SetScenarioFlags(0x1, 3)

    label("loc_7F2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_7F38")
    SetScenarioFlags(0x1, 3)

    label("loc_7F38")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_7F46")
    SetScenarioFlags(0x1, 3)

    label("loc_7F46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_7F54")
    SetScenarioFlags(0x1, 3)

    label("loc_7F54")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_7F62")
    SetScenarioFlags(0x1, 3)

    label("loc_7F62")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_7F70")
    SetScenarioFlags(0x1, 3)

    label("loc_7F70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_7F7E")
    SetScenarioFlags(0x1, 3)

    label("loc_7F7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_7F8C")
    SetScenarioFlags(0x1, 3)

    label("loc_7F8C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_7F9A")
    SetScenarioFlags(0x1, 3)

    label("loc_7F9A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_7FA8")
    SetScenarioFlags(0x1, 3)

    label("loc_7FA8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_7FB6")
    SetScenarioFlags(0x1, 3)

    label("loc_7FB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_7FC4")
    SetScenarioFlags(0x1, 3)

    label("loc_7FC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_7FD2")
    SetScenarioFlags(0x1, 3)

    label("loc_7FD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_7FE0")
    SetScenarioFlags(0x1, 3)

    label("loc_7FE0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_7FEE")
    SetScenarioFlags(0x1, 3)

    label("loc_7FEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_7FFC")
    SetScenarioFlags(0x1, 3)

    label("loc_7FFC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_800A")
    SetScenarioFlags(0x1, 3)

    label("loc_800A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_8018")
    SetScenarioFlags(0x1, 3)

    label("loc_8018")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_8026")
    SetScenarioFlags(0x1, 3)

    label("loc_8026")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_8034")
    SetScenarioFlags(0x1, 3)

    label("loc_8034")

    Return()

    # Function_35_7EE4 end

    def Function_36_8035(): pass

    label("Function_36_8035")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80E0")

    #C0384
    ChrTalk(
        0x160,
        (
            "#3300F（中央広場の聞き込みは\x01",
            "  こんな所かしら？）\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        (
            "#0000F（ああ、十分だと思う。）\x02\x03",

            "（次は駅前通りで\x01",
            "  聞き込みをしてみよう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)
    Call(0, 7)

    label("loc_80E0")

    Return()

    # Function_36_8035 end

    def Function_37_80E1(): pass

    label("Function_37_80E1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0386
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

    #A0387
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_837A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82F6")

    #C0388
    ChrTalk(
        0x101,
        (
            "#0003F《クロスベルの鐘》……\x01",
            "まさにこの街の“象徴”と\x01",
            "言うべきものだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x102,
        "#0105F……ねえロイド、もしかして……\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        (
            "#0000Fああ……\x01",
            "何とか中を調べられないかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_837A")

    label("loc_82F6")


    #C0391
    ChrTalk(
        0x101,
        (
            "#0001F《クロスベルの鐘》……\x01",
            "この街の“象徴”と言うべきものだ。\x02\x03",

            "#0003Fうーん……地下からなら\x01",
            "内部を調べられるかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_837A")

    TalkEnd(0xFF)
    Return()

    # Function_37_80E1 end

    def Function_38_837E(): pass

    label("Function_38_837E")

    EventBegin(0x1)

    #A0392
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83E1")
    EventEnd(0x5)
    NewScene("m0000", 125, 0, 0)
    IdleLoop()
    Jump("loc_83E3")

    label("loc_83E1")

    EventEnd(0x5)

    label("loc_83E3")

    Return()

    # Function_38_837E end

    def Function_39_83E4(): pass

    label("Function_39_83E4")

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

    def lambda_847A():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_847A)
    Sleep(50)

    def lambda_8497():
        OP_96(0xFE, 0xFFFFCC0C, 0x0, 0x3200, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_8497)
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

    def lambda_84EE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_84EE)
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

    def lambda_8556():
        OP_9A(0xFE, 0x101, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_8556)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0393
    AnonymousTalk(
        0x101,
        "#0005Fもしもし？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1189, 255, 100, 0)    #voice#Elie
    Sleep(1200)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エリィの声")

    #A0394
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィです。\x01",
            "行政区の捜索が終わったわ。\x02\x03",

            "コリン君は見つからなかったけど\x01",
            "似た子を見たという人がいて……\x02\x03",

            "親御さんがいない状態で\x01",
            "パレードの最後尾のあたりを\x01",
            "追いかけていたみたいね。\x02",
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
            "#0003Fそうか……それっぽいな。\x02\x03",

            "#0001F引き続き、港湾区の捜索を頼む。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エリィの声")

    #A0396
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、了解よ。\x02",
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

    def lambda_8717():
        OP_96(0xFE, 0xFFFFCC0C, 0x0, 0x3200, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_8717)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    WaitChrThread(0x160, 1)
    Sleep(300)

    #C0397
    ChrTalk(
        0x160,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#3304Fパレードの最後尾……\x01",
            "なるほど、あの車両ね。\x02",
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
            "#11P#0012Fって、聞いてたのか。\x02\x03",

            "#0000Fどんな車両だったんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x160,
        (
            "#5P#3302F『みっしぃ』っていう\x01",
            "マスコットキャラが乗った車両よ。\x02\x03",

            "なかなか楽しいデザインだったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        (
            "#11P#0008Fなるほど……\x01",
            "いかにも子供が好きそうだな。\x02\x03",

            "#0003F（となると、出店は外して\x01",
            "  子供や受付の人を中心に\x01",
            "  聞いてみるべきかな……？）\x02",
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

    # Function_39_83E4 end

    def Function_40_8911(): pass

    label("Function_40_8911")

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

    def lambda_89A7():
        OP_96(0xFE, 0x11F8, 0x0, 0xFFFFB9B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_89A7)
    Sleep(50)

    def lambda_89C4():
        OP_96(0xFE, 0xD48, 0x0, 0xFFFFB8E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_89C4)
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

    def lambda_8A25():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_8A25)
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

    def lambda_8A83():
        OP_9A(0xFE, 0x101, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_8A83)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0401
    AnonymousTalk(
        0x101,
        "#0001Fもしもし？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ランディの声")

    #A0402
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディだ。\x01",
            "今、旧市街を回っている所だ。\x02\x03",

            "例の坊主だが……\x01",
            "旧市街をうろついてたらしいぞ。\x02",
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
            "#0011Fな……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ランディの声")

    #A0404
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "パレードの見物をしてる時に\x01",
            "旧市街の子供に誘われて\x01",
            "しばらく遊んでいたらしい。\x02\x03",

            "その後、ふらっと東通りの方に\x01",
            "戻っちまったみてぇだが……\x02",
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
            "#0008Fそうか……\x02\x03",

            "#0006Fしかし好奇心旺盛というか\x01",
            "物怖じしない子だな……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ランディの声")

    #A0406
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "まったくだぜ……\x02",
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
    SetChrName("ティオの声")

    #A0407
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……ティオです。\x01",
            "横から失礼します。\x02",
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
            "#0005Fティオ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ランディの声")

    #A0409
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なんだ、この端末、\x01",
            "複数で会話できるのかよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ティオの声")

    #A0410
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一応、そういう仕様です。\x02\x03",

            "街の東口ですが、\x01",
            "あの子の匂いはしませんでした。\x02\x03",

            "今、港湾区を通って\x01",
            "北口に向かっている所です。\x02",
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
            "#0000Fああ、よろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ランディの声")

    #A0412
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "俺の方はもう一度\x01",
            "東通りを回ってみるか？\x02",
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
            "#0003Fああ、そのあたりを\x01",
            "通ったのは確実みたいだ。\x02\x03",

            "#0001F念のため回ってみてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ランディの声")

    #A0414
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おう、任せとけ。\x02",
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

    def lambda_8F47():
        OP_96(0xFE, 0xD48, 0x0, 0xFFFFB8E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_8F47)
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    WaitChrThread(0x160, 1)
    Sleep(300)

    #C0415
    ChrTalk(
        0x160,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#3302Fうふふ……あの子、\x01",
            "なかなか鬼ごっこが上手ね。\x02\x03",

            "#3304F行政区から歓楽街、裏通り、\x01",
            "中央広場、東通りとパレードを\x01",
            "追いかけて、急に旧市街へ移動……\x02\x03",

            "その後、東通りに戻って\x01",
            "港湾区あたりに向かった……\x02\x03",

            "#3300Fそんなルートかもしれないわね。\x02",
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
            "#0004F#11P本当に鋭いな……\x01",
            "俺の予想も全く同じだよ。\x02\x03",

            "#0000F一応、仲間が捜索しているから\x01",
            "そっち方面は任せるとして……\x02\x03",

            "念のため西通りを確かめるけど\x01",
            "構わないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x160,
        (
            "#6P#3300Fふふ、いいんじゃないかしら？\x01",
            "選択肢を潰すのも有意義だものね。\x02",
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

    # Function_40_8911 end

    def Function_41_91B9(): pass

    label("Function_41_91B9")

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

    # Function_41_91B9 end

    def Function_42_937B(): pass

    label("Function_42_937B")

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

    # Function_42_937B end

    def Function_43_93C7(): pass

    label("Function_43_93C7")

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

    # Function_43_93C7 end

    def Function_44_9585(): pass

    label("Function_44_9585")

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
            "#11P#0100F（『ナードルバーガー』……\x01",
            "  被害があった出店ね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        (
            "#6P#0001Fすみません、少しよろしいですか？\x01",
            "窃盗事件の捜査で伺ったんですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0420
    ChrTalk(
        0x10,
        (
            "#5Pあ、き、君たち……\x01",
            "商工会の人が言っていた\x01",
            "警察の人か？\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x10,
        (
            "#5Pはあ、実は今朝\x01",
            "被害に遭ったばかりなんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x103,
        (
            "#12P#0200Fそうでしたか……\x02\x03",

            "その時の状況を\x01",
            "詳しく聞かせてもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x10,
        "#5Pいや、それが……\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x10,
        (
            "#5P実はいつの間にか盗られていて、\x01",
            "サッパリ分からないんだ。\x02",
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
        "#12P#0305Fどういうことだ……？\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x10,
        (
            "#5P可能性があるとすれば、あの時……\x01",
            "お喋りな青年の接客をしていた頃だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x10,
        (
            "#5P大方、記念祭を見に\x01",
            "クロスベルを訪れた観光客なんだろう。\x01",
            "とにかくお喋りな青年だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x10,
        (
            "#5Pその人に商品を渡しているときに\x01",
            "背後から音がしてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x10,
        (
            "#5P慌てて振り向いたが、\x01",
            "誰の姿も無かった……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x10,
        (
            "#5Pでも、しばらくしてから\x01",
            "レジを開けたら、\x01",
            "売上が綺麗に消えていたんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x102,
        (
            "#11P#0101Fその時に盗まれたかもしれない、\x01",
            "という事ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x10,
        (
            "#5Pそれ以上は分からない。\x01",
            "まったくもって、謎だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x101,
        "#6P#0003Fそうですか……\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9C38")
    OP_68(9490, 1900, 3320, 1200)
    MoveCamera(140, 32, 0, 1200)
    SetCameraDistance(14000, 1200)

    def lambda_9AB3():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9AB3)

    def lambda_9AC0():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9AC0)

    def lambda_9ACD():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9ACD)

    def lambda_9ADA():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9ADA)
    Sleep(1200)

    #C0434
    ChrTalk(
        0x101,
        "#6P#0000F聞き込みはこんな所かな……\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x104,
        (
            "#11P#0300Fだな、そろそろ戻って\x01",
            "整理してみようぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C32")

    #C0436
    ChrTalk(
        0x102,
        (
            "#11P#0100F商工会から連絡もないし、\x01",
            "まだ次の犯行は\x01",
            "行われてないみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x103,
        (
            "#12P#0203Fですね。\x02\x03",

            "#0200F……念のため、\x01",
            "出店を見て回りながら戻った方が\x01",
            "いいかもしれませんが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C32")

    OP_29(0x20, 0x1, 0xD)

    label("loc_9C38")

    OP_5A()
    SetChrPos(0x0, 11180, 0, 2990, 90)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_44_9585 end

    def Function_45_9C5B(): pass

    label("Function_45_9C5B")

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
            "ロイド達は目星をつけた街区へ向かい\x01",
            "張り込みを行う事にした。\x07\x00\x02",
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

            "この客じゃなさそうだな……\x02",
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
            "#0001F今度の客は青年か……\x01",
            "観光客みたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #A0441
    AnonymousTalk(
        0x104,
        (
            "#0305F待てロイド……\x01",
            "もう一人来たみたいだぜ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_9F35")
    Sleep(500)
    Jump("loc_9F24")

    label("loc_9F35")

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
            "青年は屋台のレジ台に手を伸ばした。\x07\x00\x02",
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
        "#6P#0301Fやりやがった……！\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x101,
        "#12P#0001Fよし、今だ……！\x02",
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
        "#0007F#10Aまて、その２人！！\x02",
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

    def lambda_A091():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A091)

    def lambda_A09E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_A09E)
    Sleep(200)

    #C0446
    ChrTalk(
        0x23,
        "#5Pチッ、しまった……！\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x24,
        "#11Pバレたぞ、ずらかれッ！！\x02",
    )

    CloseMessageWindow()
    OP_68(-680, 1900, 16400, 800)
    MoveCamera(326, 38, 0, 800)
    OP_6E(480, 800)
    SetCameraDistance(20960, 800)

    def lambda_A11B():

        label("loc_A11B")

        TurnDirection(0xFE, 0x23, 300)
        Yield()
        Jump("loc_A11B")

    QueueWorkItem2(0x11, 1, lambda_A11B)
    BeginChrThread(0x23, 1, 0, 53)
    OP_95(0x24, 410, 0, 17550, 7000, 0x0)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    def lambda_A14F():
        OP_95(0xFE, -390, 0, 17340, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_A14F)

    def lambda_A169():
        OP_95(0xFE, 870, 0, 19220, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A169)
    Sound(819, 0, 100, 0)
    OP_63(0x24, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    Sound(24, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    #C0448
    ChrTalk(
        0x24,
        "#6P#15Aうおっ……！\x02",
    )
    #Auto


    #C0449
    ChrTalk(
        0xC,
        "#11P#15Aぎゃふ～ん！？\x02",
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
        "#11P#0307Fお嬢、ティオすけ！\x02",
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
        "#0100F#11Pあら、こっちは行き止まりよ？\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x103,
        "#0201F#12Pチェックメイト、ですね。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x23, 1, 0, 59)
    Sleep(800)

    #C0453
    ChrTalk(
        0x23,
        "#6Pく、く、く……\x02",
    )

    Sleep(1000)
    OP_57(0x0)
    SetCameraDistance(13500, 1800)
    OP_82(0x64, 0xC8, 0xBB8, 0x320)

    #C0454
    ChrTalk(
        0x23,
        "#6P#30A#4Sくっそおおおおっ！！\x02",
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

    # Function_45_9C5B end

    def Function_46_A3A6(): pass

    label("Function_46_A3A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A3CB")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_46_A3A6")

    label("loc_A3CB")

    Return()

    # Function_46_A3A6 end

    def Function_47_A3CC(): pass

    label("Function_47_A3CC")

    OP_95(0xFE, -3920, 0, 14640, 1500, 0x0)
    OP_95(0xFE, 1060, 0, 15050, 1500, 0x0)
    OP_95(0xFE, 5750, 0, 9900, 1500, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_47_A3CC end

    def Function_48_A413(): pass

    label("Function_48_A413")

    SetChrPos(0xFE, 4800, 0, 11810, 270)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_A43E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A43E)
    OP_95(0xFE, -100, 0, 12810, 1500, 0x0)
    OP_95(0xFE, -5290, 0, 10890, 1500, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(2800)
    OP_95(0xFE, -9280, 0, 9400, 1500, 0x0)
    OP_95(0xFE, -17320, 0, 16450, 1500, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_48_A413 end

    def Function_49_A4AF(): pass

    label("Function_49_A4AF")

    SetChrPos(0xFE, 4800, 0, 12810, 270)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_A4DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A4DA)
    OP_95(0xFE, -100, 0, 13810, 1500, 0x0)
    OP_95(0xFE, -5290, 0, 11890, 1500, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(2800)
    OP_95(0xFE, -9280, 0, 10400, 1500, 0x0)
    OP_95(0xFE, -17320, 0, 17450, 1500, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_49_A4AF end

    def Function_50_A54B(): pass

    label("Function_50_A54B")

    Sleep(2500)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    OP_79(0x4)

    def lambda_A56E():
        OP_95(0xFE, -280, 800, 23120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A56E)
    Sleep(1000)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    OP_95(0xFE, -1680, 0, 18230, 2000, 0x0)

    label("loc_A5B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A5EB")
    Sleep(800)
    OP_93(0xFE, 0x87, 0x190)
    Sleep(800)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(800)
    OP_93(0xFE, 0xE1, 0x190)
    ClearScenarioFlags(0x1, 4)
    Jump("loc_A5B0")

    label("loc_A5EB")

    Return()

    # Function_50_A54B end

    def Function_51_A5EC(): pass

    label("Function_51_A5EC")

    OP_95(0xFE, -19540, 0, -1160, 4000, 0x0)
    OP_95(0xFE, -13740, 0, 4530, 4000, 0x0)
    Return()

    # Function_51_A5EC end

    def Function_52_A615(): pass

    label("Function_52_A615")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFAA6A, 0x0, 0x46A, 0x320, 0x9C4)
    SetChrChipByIndex(0xFE, 0xFF)
    OP_95(0xFE, -18470, 0, 4490, 4000, 0x0)
    Return()

    # Function_52_A615 end

    def Function_53_A64D(): pass

    label("Function_53_A64D")

    OP_95(0xFE, -300, 0, 15200, 7000, 0x0)
    OP_95(0xFE, 8700, 0, 16500, 7000, 0x0)
    Return()

    # Function_53_A64D end

    def Function_54_A676(): pass

    label("Function_54_A676")

    SetChrPos(0xFE, -10000, 0, 9420, 318)
    OP_95(0xFE, -1300, 0, 17110, 7000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_54_A676 end

    def Function_55_A6A3(): pass

    label("Function_55_A6A3")

    SetChrPos(0xFE, -6890, 0, 11470, 48)
    OP_95(0xFE, 690, 0, 16880, 7000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_55_A6A3 end

    def Function_56_A6D0(): pass

    label("Function_56_A6D0")

    OP_95(0xFE, 11800, 0, 19560, 5000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_56_A6D0 end

    def Function_57_A6EC(): pass

    label("Function_57_A6EC")

    OP_95(0xFE, 10450, 0, 11630, 5000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_57_A6EC end

    def Function_58_A708(): pass

    label("Function_58_A708")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A71F")
    OP_A0(0xFE, 3000, 0x0, 0xFB)
    Jump("Function_58_A708")

    label("loc_A71F")

    Return()

    # Function_58_A708 end

    def Function_59_A720(): pass

    label("Function_59_A720")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A74E")
    OP_93(0xFE, 0x87, 0x190)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(500)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1200)
    Jump("Function_59_A720")

    label("loc_A74E")

    Return()

    # Function_59_A720 end

    def Function_60_A74F(): pass

    label("Function_60_A74F")

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

    def lambda_A8B4():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A8B4)

    def lambda_A8C9():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A8C9)

    def lambda_A8DE():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A8DE)

    def lambda_A8F3():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A8F3)
    FadeToBright(1000, 0)
    OP_0D()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    #C0455
    ChrTalk(
        0x101,
        "#0011Fあっ……\x02",
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
        "#11Pた、助けてくれ～っ！？\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x23,
        (
            "#12Pきゅ、きゅう……\x01",
            "何なんだこいつはぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x1E,
        "#5P#1201Fグルル、ガルルル……！\x02",
    )

    CloseMessageWindow()

    def lambda_A9EF():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A9EF)

    def lambda_AA04():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AA04)

    def lambda_AA19():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AA19)

    def lambda_AA2E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AA2E)
    Sleep(2600)

    #C0459
    ChrTalk(
        0x104,
        (
            "#12P#0305Fツァイト、\x01",
            "お前来てやがったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x103,
        (
            "#12P#0200Fもしかしてその２人……\x01",
            "窃盗犯の……？\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x1E,
        "#5P#1203F……ウォン！\x02",
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
            "#6P#0000Fひょっとして、支援課の屋上から\x01",
            "犯行現場が見えたりしたのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x102,
        "#12P#0100Fふう、さすがね……\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x11,
        (
            "#5Pあ、あの、このワンちゃんの\x01",
            "飼い主のかた～？\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x11,
        "#5Pビックリしたわよ、もう～！\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x101,
        "#6P#0002Fはは、すみません……\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        (
            "#12P#0300Fこう見えて物分りの\x01",
            "いい奴なんで大丈夫っすよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x102,
        (
            "#12P#0106Fまたツァイトのお世話に\x01",
            "なっちゃったけど……\x02\x03",

            "#0100Fお陰でどうにか\x01",
            "犯人を捕まえる事が\x01",
            "出来たみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x103,
        "#12P#0202Fツァイト、助かりました。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x1E,
        "#5P#1200Fグルルル、ウォン……！\x02",
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

    # Function_60_A74F end

    def Function_61_AD39(): pass

    label("Function_61_AD39")

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
        "#12P#0306Fあう……頭を打っちまったぜ。\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそういえば、鐘って\x01",
            "内側から仰げば真っ暗だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#6P#0100F『昏き天』ね……\x01",
            "もしかして『時告げぬ街の象徴』は\x01",
            "この鐘を指しているのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x103,
        (
            "#6P#0200Fロイドさん、鐘の内側に\x01",
            "カードが貼り付けられているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x101,
        (
            "#12P#0005F本当だ……\x01",
            "ちょっと待って、調べてみる。\x02",
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
            "鐘に貼り付けられていた\x01",
            "カードを見つけた。\x02",
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
            "　 次なる鍵は楽土の中 　\x01",
            "　 暖かき水の小楽園で 　\x01",
            "輝ける者だけが知っている\x02",
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
        "#12P#0005Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x104,
        "#12P#0305Fなんだ、また謎掛けか？\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x102,
        (
            "#6P#0103F怪盗Ｂ、やっぱり\x01",
            "一筋縄では行かないわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x103,
        (
            "#6P#0200F『暖かき水の小楽園』……\x01",
            "どういう事でしょうか。\x02",
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

    # Function_61_AD39 end

    def Function_62_B1A0(): pass

    label("Function_62_B1A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1C9")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_B1C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1F2")
    EventBegin(0x1)
    Call(0, 69)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_B1F2")

    Return()

    # Function_62_B1A0 end

    def Function_63_B1F3(): pass

    label("Function_63_B1F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B21C")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_B21C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B245")
    EventBegin(0x1)
    Call(0, 71)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_B245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B26E")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_B26E")

    Return()

    # Function_63_B1F3 end

    def Function_64_B26F(): pass

    label("Function_64_B26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B298")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_B298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2C1")
    EventBegin(0x1)
    Call(0, 73)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_B2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2EA")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_B2EA")

    Return()

    # Function_64_B26F end

    def Function_65_B2EB(): pass

    label("Function_65_B2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B314")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_B314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B33D")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_B33D")

    Return()

    # Function_65_B2EB end

    def Function_66_B33E(): pass

    label("Function_66_B33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B367")
    EventBegin(0x1)
    Call(0, 70)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_B367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B390")
    EventBegin(0x1)
    Call(0, 69)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_B390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3B9")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_B3B9")

    Return()

    # Function_66_B33E end

    def Function_67_B3BA(): pass

    label("Function_67_B3BA")

    EventBegin(0x1)
    Call(0, 74)
    Sleep(50)
    SetChrPos(0x0, -28500, -8200, -25010, 180)
    EventEnd(0x4)
    Return()

    # Function_67_B3BA end

    def Function_68_B3D6(): pass

    label("Function_68_B3D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B48C")

    #C0482
    ChrTalk(
        0x103,
        (
            "#0200Fロイドさん、ヨナから\x01",
            "連絡があるかもしれません。\x02\x03",

            "あまり遠くへ行くのはどうかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#0000Fそうだな……\x01",
            "支度を済ませて\x01",
            "早めにジオフロントに向かおうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4F0")

    label("loc_B48C")


    #C0484
    ChrTalk(
        0x103,
        (
            "#0200F……ヨナから\x01",
            "連絡があるかもしれないし。\x02\x03",

            "支度を済ませたら\x01",
            "早めにジオフロントに向かおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4F0")

    Return()

    # Function_68_B3D6 end

    def Function_69_B4F1(): pass

    label("Function_69_B4F1")


    #C0485
    ChrTalk(
        0x101,
        (
            "#0000Fいや、まだ十分に\x01",
            "聞き込みをしていない……\x02\x03",

            "もう少しこの辺りで\x01",
            "情報を集めてみよう。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_69_B4F1 end

    def Function_70_B550(): pass

    label("Function_70_B550")


    #C0486
    ChrTalk(
        0x101,
        (
            "#0000Fいや……先に駅前通りの\x01",
            "聞き込みをやってしまおう。\x02\x03",

            "街の外に出ていたら\x01",
            "大変だからな……\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_70_B550 end

    def Function_71_B5B3(): pass

    label("Function_71_B5B3")


    #C0487
    ChrTalk(
        0x101,
        (
            "#0000Fこっちはランディが\x01",
            "調べてくれているはずだ。\x02\x03",

            "予定通り、分担した街区で\x01",
            "聞き込みを続けていこう。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_71_B5B3 end

    def Function_72_B61E(): pass

    label("Function_72_B61E")


    #C0488
    ChrTalk(
        0x101,
        (
            "#0000F寄り道してる場合じゃない……\x02\x03",

            "なるべく急いで\x01",
            "西クロスベル街道に行こう！\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_72_B61E end

    def Function_73_B672(): pass

    label("Function_73_B672")


    #C0489
    ChrTalk(
        0x101,
        (
            "#0000Fこっちはエリィが\x01",
            "調べてくれているはずだ。\x02\x03",

            "予定通り、分担した街区で\x01",
            "聞き込みを続けていこう。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_73_B672 end

    def Function_74_B6DB(): pass

    label("Function_74_B6DB")


    #C0490
    ChrTalk(
        0x101,
        (
            "#0001F今は特に用事がないな……\x01",
            "コリン君の捜索に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_74_B6DB end

    SaveToFile()

Try(main)
