from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c010b.bin",                # FileName
        "c010b",                    # MapName
        "c010b",                    # Location
        0x0004,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 4, 0, 5],
    )

    BuildStringList((
        "c010b",                  # 0
        "ジーナ",                 # 1
        "コンテ老人",             # 2
        "プルーナ",               # 3
        "リナリー",               # 4
        "ハース",                 # 5
        "コッペ",                 # 6
        "セルゲイ課長",           # 7
        "リュウ",                 # 8
        "アンリ",                 # 9
        "エリィ",                 # 10
        "ツァイト",               # 11
        "警備隊員",               # 12
        "警備隊員",               # 13
        "警備隊員",               # 14
        "警備隊員",               # 15
        "警備隊員",               # 16
        "警備隊員",               # 17
        "警備隊員",               # 18
        "警備隊員",               # 19
        "車１",                   # 20
        "車２",                   # 21
        "イベント用ＮＰＣ",       # 22
        "イベント用ＮＰＣ",       # 23
        "イベント用ＮＰＣ",       # 24
        "イベント用ＮＰＣ",       # 25
        "イベント用ＮＰＣ",       # 26
        "SE制御",                 # 27
        "中央広場",               # 28
        "西通り",                 # 29
        "行政区",                 # 30
        "住宅街",                 # 31
        "歓楽街",                 # 32
        "東通り",                 # 33
        "旧市街",                 # 34
        "港湾区",                 # 35
        "ＩＢＣ",                 # 36
        "駅前通り",               # 37
        "裏通り",                 # 38
        "ウルスラ間道",           # 39
        "東クロスベル街道",       # 40
        "西クロスベル街道",       # 41
        "マインツ山道",           # 42
    ))

    AddCharChip((
        "chr/ch21300.itc",                   # 00
        "chr/ch20002.itc",                   # 01
        "chr/ch20500.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch26000.itc",                   # 04
        "chr/ch39200.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(30000,   0,       -1799,   270,  261,  0x0, 0,   0,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(-6090,   150,     4449,    270,  341,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(850,     0,       17969,   90,   277,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(2539,    0,       17870,   270,  277,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(14130,   0,       340,     0,    261,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-22809,  1299,    -18829,  180,  261,  0x0, 0,   5,   0,   0,   2,   0,   11,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 54,  -0.0,                  25.799999237060547,    -0.5,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.0,                   -12.899999618530273,   0.09999999403953552,   1.0])
    DeclEvent(0x0000, 0, 55,  -22.200000762939453,   8.229999542236328,     -0.5,                  4.0,                   [-0.35355374217033386, 0.35355305671691895,   0.0,                   0.0,                   -0.35355305671691895,  -0.35355374217033386,  0.0,                   0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -4.939151763916016,    10.758625030517578,    0.10000000894069672,   1.0])
    DeclEvent(0x0000, 0, 56,  19.0,                  6.0,                   -0.5,                  16.0,                  [-1.5993946078651788e-07, 0.5,                   0.0,                   0.0,                   -0.25,                 -3.1987892157303577e-07, 0.0,                   0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.5000029802322388,    -9.499998092651367,    0.10000000149011612,   1.0])
    DeclEvent(0x0000, 0, 57,  -6.429999828338623,    -21.1200008392334,     -4.199999809265137,    16.0,                  [-1.5993946078651788e-07, 0.5,                   0.0,                   0.0,                   -0.25,                 -3.1987892157303577e-07, 0.0,                   0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.280001163482666,    3.2149932384490967,    0.8399999737739563,    1.0])

    DeclActor(-270,    0,       -980,    800,     130,     1500,    -10,     0x007C, 0,  12, 0x0000)

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
        "Function_0_8D8",          # 00, 0
        "Function_1_990",          # 01, 1
        "Function_2_9DD",          # 02, 2
        "Function_3_A08",          # 03, 3
        "Function_4_A24",          # 04, 4
        "Function_5_11E1",         # 05, 5
        "Function_6_1273",         # 06, 6
        "Function_7_12E6",         # 07, 7
        "Function_8_1452",         # 08, 8
        "Function_9_14B2",         # 09, 9
        "Function_10_1523",        # 0A, 10
        "Function_11_1594",        # 0B, 11
        "Function_12_1638",        # 0C, 12
        "Function_13_177E",        # 0D, 13
        "Function_14_1B91",        # 0E, 14
        "Function_15_245C",        # 0F, 15
        "Function_16_24A8",        # 10, 16
        "Function_17_257F",        # 11, 17
        "Function_18_341F",        # 12, 18
        "Function_19_3463",        # 13, 19
        "Function_20_34AA",        # 14, 20
        "Function_21_34F1",        # 15, 21
        "Function_22_37F1",        # 16, 22
        "Function_23_6AC8",        # 17, 23
        "Function_24_6E42",        # 18, 24
        "Function_25_6F36",        # 19, 25
        "Function_26_728A",        # 1A, 26
        "Function_27_72C1",        # 1B, 27
        "Function_28_7BCE",        # 1C, 28
        "Function_29_7C18",        # 1D, 29
        "Function_30_7C65",        # 1E, 30
        "Function_31_7CB2",        # 1F, 31
        "Function_32_7CFF",        # 20, 32
        "Function_33_7D50",        # 21, 33
        "Function_34_7DC7",        # 22, 34
        "Function_35_7F58",        # 23, 35
        "Function_36_7F72",        # 24, 36
        "Function_37_8C0D",        # 25, 37
        "Function_38_8C6B",        # 26, 38
        "Function_39_8C91",        # 27, 39
        "Function_40_8CD0",        # 28, 40
        "Function_41_8D1A",        # 29, 41
        "Function_42_8D64",        # 2A, 42
        "Function_43_8DAA",        # 2B, 43
        "Function_44_8DF0",        # 2C, 44
        "Function_45_8E70",        # 2D, 45
        "Function_46_8EED",        # 2E, 46
        "Function_47_8F25",        # 2F, 47
        "Function_48_8F5D",        # 30, 48
        "Function_49_8FCF",        # 31, 49
        "Function_50_9041",        # 32, 50
        "Function_51_905D",        # 33, 51
        "Function_52_9079",        # 34, 52
        "Function_53_9095",        # 35, 53
        "Function_54_90B1",        # 36, 54
        "Function_55_90CD",        # 37, 55
        "Function_56_90E9",        # 38, 56
        "Function_57_9105",        # 39, 57
        "Function_58_9121",        # 3A, 58
        "Function_59_9237",        # 3B, 59
    ))


    def Function_0_8D8(): pass

    label("Function_0_8D8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_918"),
        (1, "loc_924"),
        (2, "loc_930"),
        (3, "loc_93C"),
        (4, "loc_948"),
        (5, "loc_954"),
        (6, "loc_960"),
        (SWITCH_DEFAULT, "loc_96C"),
    )


    label("loc_918")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_924")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_930")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_93C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_948")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_954")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_960")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_96C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_978")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_98F")

    Return()

    # Function_0_8D8 end

    def Function_1_990(): pass

    label("Function_1_990")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9DC")
    OP_95(0xFE, 11850, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 11850, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_1_990")

    label("loc_9DC")

    Return()

    # Function_1_990 end

    def Function_2_9DD(): pass

    label("Function_2_9DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A07")
    OP_94(0xFE, 0xFFFFA484, 0xFFFFB348, 0xFFFFA722, 0xFFFFB9BA, 0x3E8)
    Sleep(300)
    Jump("Function_2_9DD")

    label("loc_A07")

    Return()

    # Function_2_9DD end

    def Function_3_A08(): pass

    label("Function_3_A08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A23")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_3_A08")

    label("loc_A23")

    Return()

    # Function_3_A08 end

    def Function_4_A24(): pass

    label("Function_4_A24")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DB")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADD")
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    SetChrPos(0x1, -26950, -1160, -4340, 90)
    SetChrPos(0x2, -26950, -1160, -4340, 90)
    SetChrPos(0x3, -26950, -1160, -4340, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB9")
    SetChrPos(0x4, -26950, -1160, -4340, 90)
    SetChrPos(0x5, -26950, -1160, -4340, 90)
    Jump("loc_AD8")

    label("loc_AB9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD8")
    SetChrPos(0x4, -26950, -1160, -4340, 90)

    label("loc_AD8")

    Jump("loc_10DB")

    label("loc_ADD")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B88")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B64")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_B83")

    label("loc_B64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B83")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_B83")

    Jump("loc_10DB")

    label("loc_B88")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C33")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0F")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_C2E")

    label("loc_C0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2E")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_C2E")

    Jump("loc_10DB")

    label("loc_C33")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDE")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBA")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_CD9")

    label("loc_CBA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD9")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_CD9")

    Jump("loc_10DB")

    label("loc_CDE")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D89")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D65")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_D84")

    label("loc_D65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D84")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_D84")

    Jump("loc_10DB")

    label("loc_D89")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E34")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E10")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_E2F")

    label("loc_E10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2F")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_E2F")

    Jump("loc_10DB")

    label("loc_E34")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDF")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBB")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_EDA")

    label("loc_EBB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EDA")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_EDA")

    Jump("loc_10DB")

    label("loc_EDF")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8A")
    SetChrPos(0x0, 4040, 0, -21980, 0)
    SetChrPos(0x1, 4040, 0, -21980, 0)
    SetChrPos(0x2, 4040, 0, -21980, 0)
    SetChrPos(0x3, 4040, 0, -21980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F66")
    SetChrPos(0x4, 4040, 0, -21980, 0)
    SetChrPos(0x5, 4040, 0, -21980, 0)
    Jump("loc_F85")

    label("loc_F66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F85")
    SetChrPos(0x4, 4040, 0, -21980, 0)

    label("loc_F85")

    Jump("loc_10DB")

    label("loc_F8A")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1035")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1011")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_1030")

    label("loc_1011")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1030")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_1030")

    Jump("loc_10DB")

    label("loc_1035")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DB")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BC")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_10DB")

    label("loc_10BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DB")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_10DB")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1103")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_1103")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1122")
    SetMapFlags(0x10000000)
    Event(0, 22)

    label("loc_1122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1136")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)
    Jump("loc_11C0")

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_114A")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 16)
    Jump("loc_11C0")

    label("loc_114A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_115E")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 21)
    Jump("loc_11C0")

    label("loc_115E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_1172")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 23)
    Jump("loc_11C0")

    label("loc_1172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_1186")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 24)
    Jump("loc_11C0")

    label("loc_1186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_119D")
    ClearScenarioFlags(0x5C, 5)
    SetScenarioFlags(0x0, 0)
    Event(0, 25)
    Jump("loc_11C0")

    label("loc_119D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_11B1")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 27)
    Jump("loc_11C0")

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_11C0")
    ClearScenarioFlags(0x5C, 7)
    Event(0, 36)

    label("loc_11C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11E0")
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_11E0")

    Return()

    # Function_4_A24 end

    def Function_5_11E1(): pass

    label("Function_5_11E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11FD")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_120F")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_120F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_120F")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    OP_1B(0x4, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1272")
    OP_1B(0x0, 0x0, 0x32)
    OP_1B(0x1, 0x0, 0x33)
    OP_1B(0x2, 0x0, 0x34)
    OP_1B(0x4, 0x0, 0x35)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1272")

    Return()

    # Function_5_11E1 end

    def Function_6_1273(): pass

    label("Function_6_1273")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "いっけなーい！\x01",
            "すっかり遅くなっちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "夕飯の買い物だったのに～……\x01",
            "うう、これは大目玉決定ね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1273 end

    def Function_7_12E6(): pass

    label("Function_7_12E6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_137A")
    Jump("loc_13C4")

    label("loc_137A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_139A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13C4")

    label("loc_139A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13BA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13C4")

    label("loc_13BA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13C4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0003
    ChrTalk(
        0xFE,
        "おお……いつの間にやらこんな時間か。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "近頃物騒だし、\x01",
            "早いところ家路につくとするかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_12E6 end

    def Function_8_1452(): pass

    label("Function_8_1452")

    TalkBegin(0xFE)

    #C0005
    ChrTalk(
        0xFE,
        (
            "やっぱ、痩せたいなら\x01",
            "適度な運動が必要よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "あんた、明日から走りこみしなさいよ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1452 end

    def Function_9_14B2(): pass

    label("Function_9_14B2")

    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        (
            "え～……\x01",
            "一人で走りこみなんて絶対やーよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "ねぇ、一緒に走ろうよ～。\x01",
            "それだったら長続きするし。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_14B2 end

    def Function_10_1523(): pass

    label("Function_10_1523")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        (
            "よっと……\x01",
            "そろそろ畳んじまわないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "あ、もらってくれるなら\x01",
            "あまってる風船取ってっていいぜ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_1523 end

    def Function_11_1594(): pass

    label("Function_11_1594")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161F")
    Sound(823, 0, 100, 0)

    #C0011
    ChrTalk(
        0x101,
        (
            "#0000Fハハ……随分と\x01",
            "寛いでるみたいだな。\x02\x03",

            "この様子だと、やっぱり前から\x01",
            "このビルに住み着いてるみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 6)
    Jump("loc_1634")

    label("loc_161F")


    #N0012
    NpcTalk(
        0xFE,
        "黒猫",
        "にゃおん？\x02",
    )

    CloseMessageWindow()

    label("loc_1634")

    TalkEnd(0xFE)
    Return()

    # Function_11_1594 end

    def Function_12_1638(): pass

    label("Function_12_1638")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0013
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

    #A0014
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

    # Function_12_1638 end

    def Function_13_177E(): pass

    label("Function_13_177E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-31880, 3900, -19510, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8410, 0)
    SetChrPos(0x101, -28730, 1300, -14730, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetCameraDistance(7410, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_71(0x7, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x7)
    Sleep(500)

    def lambda_1840():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1840)

    def lambda_185A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_185A)
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x7)
    Sleep(300)

    #C0015
    ChrTalk(
        0x101,
        "#0003F#5Pふう……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0016
    ChrTalk(
        0x101,
        "#0002F#5Pはは、凄い夜景だな……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(9220, 3900, 27970, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(26360, 0)
    OP_68(-9090, 3900, -24280, 12000)
    MoveCamera(45, 14, 0, 12000)
    OP_6E(700, 12000)
    SetCameraDistance(22320, 12000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-21610, 3900, -19830, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10170, 0)
    SetChrPos(0x101, -22170, 1300, -17820, 90)
    SetChrPos(0xD, -25810, 1300, -17860, 90)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 0)
    OP_4B(0xD, 0xFF)
    SetChrSubChip(0xD, 0x0)
    SetCameraDistance(9170, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0017
    ChrTalk(
        0x101,
        (
            "#0002F#5Pやっぱりクロスベルは都会だよな。\x01",
            "叔父さん家があった町も\x01",
            "決して小さくはなかったけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    #C0018
    ChrTalk(
        0x101,
        "#0008F#5P……帰ってきたんだよな。\x02",
    )

    CloseMessageWindow()
    Sound(823, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0019
    ChrTalk(
        0x101,
        "#0005F#5Pあれ……？\x02",
    )

    CloseMessageWindow()
    OP_68(-26650, 3900, -20900, 2000)
    OP_93(0x101, 0x10E, 0x1F4)
    OP_6F(0x1)

    #C0020
    ChrTalk(
        0x101,
        (
            "#0005F#11Pなんだ猫か……\x02\x03",

            "#0000Fこのビルにいるって事は……\x01",
            "支援課が入る前から\x01",
            "住み着いてるのかな？\x02\x03",

            "#0012Fはは……邪魔してゴメンな。\x01",
            "適当な所で引き上げるからさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(823, 0, 100, 0)
    Sleep(1000)
    SetCameraDistance(9420, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x4A, 4)
    BeginChrThread(0xD, 0, 0, 2)
    OP_4C(0xD, 0xFF)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_177E end

    def Function_14_1B91(): pass

    label("Function_14_1B91")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    LoadChrToIndex("chr/ch28100.itc", 0x1F)
    LoadChrToIndex("chr/ch20400.itc", 0x20)
    LoadChrToIndex("chr/ch20500.itc", 0x21)
    LoadChrToIndex("chr/ch20800.itc", 0x22)
    LoadChrToIndex("chr/ch23600.itc", 0x23)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_90(0x101, -18000, -8000, -21000, 225)
    OP_90(0x102, -16900, -8000, -22100, 225)
    OP_90(0x103, -17000, -8000, -20000, 225)
    OP_90(0x104, -15900, -8000, -21100, 225)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -28500, -8200, -20500, 180)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x10)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x8, 0x1B)
    OP_78(0x9, 0x1C)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x4)
    OP_49()
    SetChrPos(0x1B, -23000, 0, -3000, 0)
    OP_D3(0x1B, 0x0, 0x15F90, 0x0, 0x0)
    OP_70(0x8, 0x0)
    SetChrPos(0x1C, 8000, 0, 3500, 0)
    OP_D3(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    OP_4B(0x1D, 0xFF)
    SetChrPos(0x1D, 5000, 0, -6300, 270)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -6800, 0, 4000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -8300, 0, 2500, 90)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x22)
    SetChrSubChip(0x20, 0x0)
    OP_4B(0x20, 0xFF)
    SetChrPos(0x20, -10300, 0, 10400, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x23)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, 0, 0, 15000, 315)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)

    def lambda_1E3E():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1E3E)

    def lambda_1E58():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1E58)

    def lambda_1E72():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_1E72)
    Sound(458, 0, 100, 0)

    def lambda_1E93():
        OP_96(0xFE, 0x4E20, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1E93)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x22, 1, 0, 15)
    FadeToBright(2000, 0)
    Sleep(4400)

    def lambda_1EDC():
        OP_95(0xFE, -22000, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EDC)
    Sleep(200)

    def lambda_1EF9():
        OP_95(0xFE, -21900, -8200, -25600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1EF9)
    Sleep(200)

    def lambda_1F16():
        OP_95(0xFE, -22000, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F16)
    Sleep(200)

    def lambda_1F33():
        OP_95(0xFE, -21900, -8200, -25600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F33)
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25000, -4500, -16000, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(31000, 0)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    OP_68(-25000, -7500, -16000, 8000)
    MoveCamera(30, 20, 0, 8000)
    SetCameraDistance(26000, 8000)
    PlaceName2(340, 40, "c_plac34", 0x0, 3000)
    WaitChrThread(0x101, 1)

    def lambda_1FFA():
        OP_95(0xFE, -28400, -8200, -25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FFA)
    WaitChrThread(0x102, 1)

    def lambda_2018():
        OP_95(0xFE, -28500, -8200, -26100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2018)
    WaitChrThread(0x103, 1)

    def lambda_2036():
        OP_95(0xFE, -26700, -8200, -25200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2036)
    WaitChrThread(0x104, 1)

    def lambda_2054():
        OP_95(0xFE, -26800, -8200, -26300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2054)
    WaitChrThread(0x101, 1)

    def lambda_2072():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2072)
    WaitChrThread(0x103, 1)

    def lambda_2083():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2083)
    WaitChrThread(0x102, 1)

    def lambda_2094():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2094)
    WaitChrThread(0x104, 1)

    def lambda_20A5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_20A5)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    EndChrThread(0x22, 0x1)
    Fade(500)
    OP_68(-27800, -7200, -24000, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    #C0021
    ChrTalk(
        0x101,
        (
            "#12P#0005Fここは……\x01",
            "あの雑居ビルじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#12P#0306Fなんだ。\x01",
            "ずいぶんボロイ建物だな。\x02\x03",

            "#0301Fあっちのデパートと比べると\x01",
            "古ぼけて見えるっていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0206F#11P築３０年……\x01",
            "取り壊し間近って感じです。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#12P#0108F……本当にここが\x01",
            "『特務支援課』の分室なの？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#12P#0001Fあ、ああ。\x01",
            "間違いないとは思うけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    Sleep(150)

    #N0026
    NpcTalk(
        0xE,
        "男の声",
        "#2Pおう、遅かったな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x13B, 0x1F4)
    Sleep(50)
    OP_93(0x104, 0x13B, 0x1F4)

    def lambda_22D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_22D4)

    def lambda_22E5():
        OP_95(0xFE, -28500, -8200, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_22E5)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xE, 1)

    #C0027
    ChrTalk(
        0x101,
        "#12P#0005Fセルゲイ課長……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0028
    AnonymousTalk(
        0xE,
        (
            "とっとと中に入れ。\x02\x03",

            "この『特務支援課』が\x01",
            "どういった部署なのか……\x02\x03",

            "お前たちの疑問の全てに\x01",
            "ちゃんと答えてやるからよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_93(0xE, 0x0, 0x1F4)

    def lambda_2401():
        OP_95(0xFE, -28500, -8200, -20500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2401)
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(1000)

    def lambda_2431():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2431)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xE, 1)
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 0)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1B91 end

    def Function_15_245C(): pass

    label("Function_15_245C")

    Sound(803, 2, 100, 0)
    Sleep(4400)
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

    # Function_15_245C end

    def Function_16_24A8(): pass

    label("Function_16_24A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-26000, -6000, -18500, 0)
    MoveCamera(0, 45, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, -24000, -8200, -20000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_68(-26000, -4500, -18500, 8000)
    MoveCamera(0, 25, 0, 8000)
    SetCameraDistance(15500, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 1)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_24A8 end

    def Function_17_257F(): pass

    label("Function_17_257F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20600.itc", 0x1E)
    LoadChrToIndex("chr/ch22200.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis008.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis014.itp")
    OP_C9(0x0, 0x4, 0x0, 0x0, 0x0)
    OP_68(-28800, -7300, -27000, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -28800, -8200, -22700, 180)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    def lambda_26A2():
        OP_95(0xFE, -28800, -8200, -27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26A2)
    SetCameraDistance(15500, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2787")

    #C0029
    ChrTalk(
        0x101,
        (
            "#5P#0004Fふう……\x01",
            "いい風が吹いてるな。\x02\x03",

            "#0002Fそれにしても\x01",
            "やっぱりクロスベルは\x01",
            "大都会って感じだよな……\x02\x03",

            "叔父さん家があった町も\x01",
            "決して小さくはなかったけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B3")

    label("loc_2787")


    #C0030
    ChrTalk(
        0x101,
        (
            "#5P#0002Fふう……\x01",
            "いい風が吹いてるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27B3")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_27CD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27CD)
    OP_68(-48800, -7300, -27000, 3000)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_6F(0x1)
    Sleep(500)

    #A0031
    AnonymousTalk(
        0x101,
        (
            "#0005F《ベルハイム》……\x01",
            "そっか、ここから見えるのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1500)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #A0032
    AnonymousTalk(
        0x101,
        (
            "#0004Fはは……今はもう\x01",
            "別の人が入ってるんだよな。\x02\x03",

            "#0000Fセシル姉の実家は\x01",
            "さすがに残ってるだろうけど……\x02\x03",

            "#0005Fそうだ、おばさんたちにも\x01",
            "後で挨拶しておかないと……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-28800, -7300, -27000, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0033
    ChrTalk(
        0x101,
        (
            "#11P#0003F#30W（あれから３年……）\x02\x03",

            "（叔父さん家で厄介になった後、\x01",
            "  警察学校に入って……）\x02\x03",

            "（がむしゃらに勉強と訓練をして\x01",
            "  捜査官の資格も取ったけど……）\x02\x03",

            "#0008F（結局、俺は……）\x02\x03",

            "（俺は……捜査官になって\x01",
            "  何がしたかったんだ……？）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xF, -14000, -4200, -17500, 225)
    SetChrFlags(0xF, 0x8)
    ClearChrFlags(0xF, 0x80)

    #N0034
    NpcTalk(
        0xF,
        "男の子の声",
        "#2Sお～い！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(-27000, -5300, -26200, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    ClearChrFlags(0xF, 0x8)
    SetChrPos(0xF, -14000, -4200, -17500, 225)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0x10, -13000, -4200, -16500, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    BeginChrThread(0xF, 3, 0, 18)
    BeginChrThread(0x10, 3, 0, 19)
    OP_68(-27000, -7300, -26200, 3500)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_0D()
    Sleep(1000)

    def lambda_2B4A():
        OP_96(0xFE, 0xFFFF923C, 0xFFFFDFF8, 0xFFFF99A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B4A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)

    #C0035
    ChrTalk(
        0x101,
        "#6P#0005F君たちは……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xF,
        "#2Pいや～、探しちゃったぜ。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xF,
        (
            "#2P警察に行ったんだけど\x01",
            "兄ちゃんたちはいないって\x01",
            "言うじゃんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x10,
        (
            "#11Pそれで、この場所を\x01",
            "教えてもらったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x10,
        (
            "#11Pあの、ここが支援課って\x01",
            "ところでいいんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあ、ああ、そうだけど。\x02\x03",

            "どうしてわざわざ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xF,
        "#2Pい、いやさ……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xF,
        (
            "#2Pその、ちゃんとお礼を\x01",
            "言ってなかったと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x10,
        (
            "#11Pお兄さんたちがいなかったら\x01",
            "たぶん、ボクたち２人とも\x01",
            "大ケガをしてたと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x10,
        (
            "#11Pだからその……\x01",
            "もう一度お礼を言おうって。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#6P#0002F……そっか………\x02\x03",

            "２人とも、ありがとな。\x01",
            "こんな時間に訪ねてきてくれて。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xF,
        (
            "#2Pま、まあ、\x01",
            "アリオスさんと比べたら\x01",
            "かなり頼りなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xF,
        (
            "#2P警察のお巡りにしたら\x01",
            "なかなか見所あると思うぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xF,
        (
            "#2P実力不足は、これから\x01",
            "頑張ればいいんじゃね？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0xE1, 0x1F4)
    OP_63(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0050
    ChrTalk(
        0x10,
        "#5Pちょ、ちょっと、リュウ。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x10,
        (
            "#5Pお礼を言いにきたのに\x01",
            "なんだかエラそうだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#6P#0009Fははっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0053
    ChrTalk(
        0x101,
        (
            "#6P#0004F──そうだな。\x01",
            "これから精進すればいいか。\x02\x03",

            "#0000Fそうだ、２人とも\x01",
            "どこらへんに住んでるんだ？\x02\x03",

            "よかったら送って行くよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xF,
        (
            "#2Pああ、へーきへーき。\x01",
            "西通りだからすぐ近くだしさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x10E, 0x1F4)

    #C0055
    ChrTalk(
        0x10,
        (
            "#11Pえっと、ボクは\x01",
            "住宅街の方だけど平気です。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x10,
        (
            "#11Pその、お姉さんたちにも\x01",
            "よろしく伝えといてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#6P#0002Fああ、伝えておくよ。\x02\x03",

            "２人とも、気をつけて帰れよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xF,
        "#2Pおう！\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x10,
        "#11Pそれじゃ、さようなら！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x10, 3, 0, 20)
    Sleep(300)
    BeginChrThread(0xF, 3, 0, 20)
    Sleep(3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitChrThread(0x10, 3)
    SetChrFlags(0x10, 0x80)
    WaitChrThread(0xF, 3)
    SetChrFlags(0xF, 0x80)
    Fade(1000)
    SetChrPos(0x101, -28800, -8200, -26200, 90)
    OP_68(-28800, -7300, -27000, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    OP_0D()
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)
    OP_68(-28940, -7300, -27520, 1500)

    def lambda_3179():
        OP_95(0xFE, -28800, -8200, -27000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3179)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    #C0060
    ChrTalk(
        0x101,
        (
            "#5P#0012Fハハ……俺も単純だなぁ。\x02\x03",

            "#0002Fあんなお礼ひとつで\x01",
            "こんなに気分が晴れるなんて……\x02\x03",

            "#0004F要は、自分自身の\x01",
            "気持ちの持ち方しだいか……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W──いいか、ロイド。\x02\x03",

            "男だったら、目の前のものに\x01",
            "体当たりでぶつかってみろ。\x02\x03",

            "てめえの心で、てめえだけの\x01",
            "真実を掴みとってやるんだよ。\x02\x03",

            "そうすりゃ、てめえが\x01",
            "何をしたいか見えてくるはずだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(500, 0)
    OP_0D()
    OP_C7(0x1, 0x800)
    Sleep(300)

    #C0062
    ChrTalk(
        0x101,
        (
            "#5P#0004F…………………………………\x02\x03",

            "……うん、そうだよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-27780, -7300, -22810, 2500)
    MoveCamera(32, 14, 0, 2500)
    SetCameraDistance(18000, 2500)
    OP_93(0x101, 0x0, 0x12C)
    OP_6F(0x79)

    #C0063
    ChrTalk(
        0x101,
        (
            "#12P#0000Fまずはぶつかってみないと\x01",
            "何も分からないか……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetCameraDistance(17000, 2000)

    def lambda_33E5():
        OP_95(0xFE, -28800, -8200, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33E5)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    OP_CA(0x1, 0xFF, 0x0)
    SetMapFlags(0x10000000)
    SetScenarioFlags(0x5C, 2)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_257F end

    def Function_18_341F(): pass

    label("Function_18_341F")


    def lambda_3424():
        OP_95(0xFE, -21500, -8200, -24000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3424)
    WaitChrThread(0xF, 1)
    OP_93(0xF, 0x10E, 0x0)

    def lambda_3449():
        OP_96(0xFE, 0xFFFF9A70, 0xFFFFDFF8, 0xFFFF987C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3449)
    WaitChrThread(0xF, 1)
    Return()

    # Function_18_341F end

    def Function_19_3463(): pass

    label("Function_19_3463")

    Sleep(300)

    def lambda_346B():
        OP_95(0xFE, -21500, -8200, -24000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_346B)
    WaitChrThread(0x10, 1)
    OP_93(0x10, 0x10E, 0x0)

    def lambda_3490():
        OP_96(0xFE, 0xFFFF9C64, 0xFFFFDFF8, 0xFFFF9C64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3490)
    WaitChrThread(0x10, 1)
    Return()

    # Function_19_3463 end

    def Function_20_34AA(): pass

    label("Function_20_34AA")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)

    def lambda_34B9():
        OP_96(0xFE, 0xFFFFAC04, 0xFFFFDFF8, 0xFFFFA240, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34B9)
    WaitChrThread(0xFE, 1)

    def lambda_34D7():
        OP_95(0xFE, -14000, -4200, -17500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34D7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_34AA end

    def Function_21_34F1(): pass

    label("Function_21_34F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch20400.itc", 0x1F)
    LoadChrToIndex("chr/ch20500.itc", 0x20)
    LoadChrToIndex("chr/ch20800.itc", 0x21)
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
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x8, 0x1B)
    OP_78(0x9, 0x1C)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x4)
    OP_49()
    SetChrPos(0x1B, -23000, 0, -3000, 0)
    OP_D3(0x1B, 0x0, 0x15F90, 0x0, 0x0)
    OP_70(0x8, 0x0)
    SetChrPos(0x1C, 8000, 0, 3500, 0)
    OP_D3(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    OP_4B(0x1D, 0xFF)
    SetChrPos(0x1D, 5000, 0, -6300, 270)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -6800, 0, 4000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -8300, 0, 2500, 90)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    OP_4B(0x20, 0xFF)
    SetChrPos(0x20, -10300, 0, 10400, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, 0, 0, 15000, 315)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)

    def lambda_3734():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3734)

    def lambda_374E():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_374E)

    def lambda_3768():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3768)
    Sound(457, 0, 100, 0)

    def lambda_3789():
        OP_96(0xFE, 0x4E20, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3789)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x22, 1, 0, 15)
    FadeToBright(2000, 0)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    Sleep(1500)
    EndChrThread(0x22, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 4)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_34F1 end

    def Function_22_37F1(): pass

    label("Function_22_37F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00100.itc", 0x1E)
    LoadChrToIndex("apl/ch50214.itc", 0x1F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00101.itp")
    OP_68(-27460, 2300, -18410, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_68(-26090, 2300, -17520, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, -28800, 1300, -14000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, -21800, 1300, -17700, 90)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0xA)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    FadeToBright(1000, 0)

    def lambda_3928():
        OP_96(0xFE, 0xFFFF8F80, 0x514, 0xFFFFBADC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3928)

    def lambda_3942():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3942)
    WaitChrThread(0x101, 1)
    OP_71(0x7, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_93(0x101, 0x5A, 0x1F4)

    #C0064
    ChrTalk(
        0x101,
        "#6P#0005F（…………あ……………）\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(1178, 255, 90, 0)    #voice#Elie

    #C0065
    ChrTalk(
        0x11,
        "#5P#30Wロイド……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x1388)
    ReplaceBGM("ed7513", "ed7000")
    OP_68(-22610, 2300, -17660, 2000)

    def lambda_3A01():
        OP_96(0xFE, 0xFFFF9B38, 0x514, 0xFFFFBADC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A01)
    WaitChrThread(0x101, 1)
    Sleep(500)

    #C0066
    ChrTalk(
        0x101,
        (
            "#3P#0000Fああ……\x01",
            "どうして分かったんだ？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1179, 255, 100, 0)    #voice#Elie
    OP_93(0x11, 0x10E, 0x190)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0067
    AnonymousTalk(
        0x11,
        (
            "#30W何となく、かな……\x02\x03",

            "#30W何となくだけど\x01",
            "あなたが来るんじゃないかって\x01",
            "ぼんやりと思っていた。\x02",
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

    #C0068
    ChrTalk(
        0x101,
        "#6P#0004Fそっか……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_3B4C():

        label("loc_3B4C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3B4C")

    QueueWorkItem2(0x11, 2, lambda_3B4C)

    def lambda_3B5E():
        OP_96(0xFE, 0xFFFFAAD8, 0x514, 0xFFFFB5C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B5E)
    OP_68(-21800, 2800, -18300, 2500)
    WaitChrThread(0x101, 1)
    EndChrThread(0x11, 0x2)
    Sleep(500)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 3300, 4000, 0)
    MoveCamera(18, 11, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(28000, 0)
    MoveCamera(42, 11, 0, 27000)
    SetCameraDistance(33000, 27000)

    def lambda_3BDD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3BDD)
    OP_0D()
    Sleep(1000)

    #A0069
    AnonymousTalk(
        0x101,
        (
            "#0002F綺麗だな……\x02\x03",

            "あっちに見えるのは……\x01",
            "ＩＢＣビルか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0070
    AnonymousTalk(
        0x11,
        (
            "#0104F#30W多分、大陸全土を見回しても\x01",
            "この街ほど夜景が綺麗な所は\x01",
            "無いんじゃないかしら。\x02\x03",

            "#0108Fだけど……\x01",
            "街の明かりが増えれば増えるだけ、\x01",
            "星の光は見えなくなる……\x02\x03",

            "女神#4Rエイドス#の慈愛の証たる、清らかな星の光は……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_3D11():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D11)

    #A0071
    AnonymousTalk(
        0x101,
        "#0001F……エリィ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0072
    AnonymousTalk(
        0x11,
        (
            "#0106F#30W昼間のこと……\x01",
            "覚えているでしょう？\x02\x03",

            "#0108Fルバーチェ、黒月、そして\x01",
            "ダドリー捜査官が言ったこと。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(40, 90, -1, -1)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "──てめぇらが何をしようが\x01",
            "この街#6Rクロスベル#の現実は変わらねぇ……\x02\x03",

            "ましてや俺たちをどうこうする事など\x01",
            "不可能ってことをな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(120, 50, -1, -1)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ふふ、あくまで“ビジネス”の\x01",
            "競争相手としての話ですよ。\x02\x03",

            "クロスベルは自由な競争が\x01",
            "法によって保障されている場所……\x02\x03",

            "何か問題でもありますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(180, 120, -1, -1)
    SetChrName("")

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "この、正義が守りきれない街で\x01",
            "一定以上の秩序を保ち続けること……\x02\x03",

            "殺人などの重犯罪を抑止し、\x01",
            "犯罪組織や外国の諜報機関から\x01",
            "可能な限り人と社会を守ること……\x02\x03",

            "その努力がお前たちに分かるのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_68(-18240, 1700, -17030, 0)
    MoveCamera(53, 7, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16500, 0)
    OP_68(-18240, 2500, -17030, 50000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    #C0076
    ChrTalk(
        0x11,
        (
            "#5P#0103Fあれが、この街の闇……\x01",
            "クロスベルという自治州の真実よ。\x02\x03",

            "#0108F帝国と共和国の狭間で生かされ、\x01",
            "誇りも持てず、嘘と欺瞞にまみれ……\x02\x03",

            "諸外国から集まる富によって\x01",
            "かりそめの繁栄と享楽に溺れる……\x02\x03",

            "#0106F誰もがそれを仕方のない事と諦め、\x01",
            "日々の忙しさに追い立てられる……\x02\x03",

            "#0101F私たちはそんな街で生きている。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそうか……\x02\x03",

            "#0000Fエリィは……\x01",
            "諦めたくないんだな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0078
    ChrTalk(
        0x11,
        (
            "#5P#0108F……………………………………\x02\x03",

            "#0103F……父と母がいたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#12P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x11,
        (
            "#5P#0102Fふふっ、こういう言い方すると\x01",
            "亡くなっているみたいだけど。\x02\x03",

            "二人とも今も元気よ。\x02\x03",

            "#0104Fもっとも離婚して、それぞれ\x01",
            "帝国と共和国で暮らしているけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        "#12P#0003Fそうなのか……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x11,
        (
            "#5P#0100F父は元々、共和国の人だったの。\x02\x03",

            "この街に来て、母と出会い……\x02\x03",

            "マクダエル家に入ることで\x01",
            "政治家としての道を志した。\x02\x03",

            "#0103Fそして議員になってすぐに\x01",
            "この街の歪んだ現実に気付いた。\x02\x03",

            "正義感の強い人だったから\x01",
            "何とかしたいと思ったんでしょうね。\x02\x03",

            "何年もかけて、粘り強く、\x01",
            "様々な改革案を打ち出していった。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        "#12P#0002F……凄いな。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x11,
        (
            "#5P#0101Fううん……\x01",
            "結局、父の改革案は潰された。\x02\x03",

            "#0103F帝国派、共和国派……\x01",
            "どちらからも排斥される形で。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0085
    ChrTalk(
        0x11,
        (
            "#5P#0108F信じていた同志に裏切られ、\x01",
            "友人を無くし、政敵に嘲られ……\x02\x03",

            "祖父もクロスベル市長という\x01",
            "中立的立場から父を助けられず……\x02\x03",

            "#0106F父は……クロスベルそのものに\x01",
            "絶望してしまった。\x02\x03",

            "そして議員を辞め、妻子と別れて\x01",
            "カルバードに帰る道を選択した……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#12P#0013Fあ……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x11,
        (
            "#5P#0108F母は父を引き止められず……\x02\x03",

            "かといって、幼い私を連れて\x01",
            "父に付いていく事もできず……\x02\x03",

            "#0103Fそして離婚が成立して……\x01",
            "父はいなくなってしまった。\x02\x03",

            "#0102F母は父を恨んだみたいだけど……\x01",
            "やっぱり愛していたんでしょうね。\x02\x03",

            "父のいないクロスベルに住むのが\x01",
            "辛くなってしまったみたいで……\x01",
            "親戚のいる帝国に身を寄せてしまった。\x02\x03",

            "#0104Fそして私は……\x01",
            "祖父に引き取られる事になった。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#12P#0008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-21800, 2300, -18300, 0)
    MoveCamera(300, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    MoveCamera(329, 33, 0, 80000)
    OP_0D()

    #C0089
    ChrTalk(
        0x11,
        (
            "#5P#0102F……私が政治の道を\x01",
            "志そうと思ったのはその時からよ。\x02\x03",

            "別に父の仇を取ろうとか\x01",
            "そういうつもりじゃなかった。\x02\x03",

            "#0104Fただ、納得行かなかったの。\x02\x03",

            "あんなにも幸せだった家族が\x01",
            "何で壊れてしまったんだろうって。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#6P#0006F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x11,
        (
            "#5P#0103F祖父の助けもあって……\x01",
            "私は各地で留学をしながら\x01",
            "政治・経済などを学んでいった。\x02\x03",

            "#0108Fでも、勉強すればするほど\x01",
            "クロスベルの置かれている状況は\x01",
            "困難なものである事に気付いたの。\x02\x03",

            "結局は、帝国と共和国……\x02\x03",

            "この二大国の持っている重力に\x01",
            "あらゆる正義と利害は絡め取られ、\x01",
            "歪みを余儀なくされてしまう。\x02\x03",

            "#0103F私は《壁》にぶつかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        "#6P#0001F……《壁》か。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x11,
        (
            "#5P#0108Fええ……父もそうだったけど\x01",
            "祖父も感じているであろう《壁》。\x02\x03",

            "#0100Fねえ、ロイド。\x01",
            "クロスベル自治州の政府代表って、\x01",
            "誰だか知ってる？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#6P#0005Fそれは……\x01",
            "マクダエル市長じゃないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x11,
        (
            "#5P#0104Fううん、正確には\x01",
            "『クロスベル市の市長』と\x01",
            "『自治州議会の議長』の２人よ。\x02\x03",

            "つまり今だと、おじいさまと\x01",
            "帝国派のハルトマン議長という人が\x01",
            "クロスベル政府の共同代表なの。\x02\x03",

            "これは自治州法に定められているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#6P#0006Fそうか、不勉強だったな……\x02\x03",

            "#0005Fでも、どうしてそんな\x01",
            "ややこしい体制になってるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x11,
        (
            "#5P#0103F決まっているわ。\x02\x03",

            "#0101F──同格の代表が２人いたら\x01",
            "政治改革が起こりにくいからよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0098
    ChrTalk(
        0x101,
        (
            "#6P#0011Fそんな……！\x02\x03",

            "#0008F……いや、でも……\x01",
            "確かにそうなるのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x11,
        (
            "#5P#0106Fええ、トップが２人いた場合、\x01",
            "どちらかが改革を起こそうとしても\x01",
            "もう片方が必ず足を引っ張る……\x02\x03",

            "これはもう、政治力学として\x01",
            "そうなるのが歴史の必然なのよね。\x02\x03",

            "#0108F７０年前……\x01",
            "帝国・共和国双方の承認を受けて\x01",
            "創設されたクロスベル自治州……\x02\x03",

            "その時、自治州法を定めたのは\x01",
            "両国の法律家だったそうだけど……\x02\x03",

            "#0103F今にして思うと、まさに“呪い”ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#6P#0001F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x11,
        (
            "#5P#0108F私は……途方にくれてしまった。\x02\x03",

            "政治の世界にそのまま入れば、\x01",
            "その呪いに必ず蝕まれてしまう……\x02\x03",

            "#0103Fだから、父とも祖父とも違う\x01",
            "別の切り口が欲しかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#6P#0000Fそれが……警察だったのか。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x11,
        (
            "#5P#0104Fええ、政治とは別の視点で\x01",
            "様々な歪みが観察できる場所。\x02\x03",

            "そこでの経験は、いずれ政治の世界に\x01",
            "入った時の武器になると思った。\x02\x03",

            "#0108F父が失敗し、祖父がなし得なかった\x01",
            "クロスベルの改革……\x02\x03",

            "#0100Fそれを実現する手がかりに\x01",
            "なるんじゃないかと思ったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#6P#0000Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x11,
        (
            "#5P#0108F……でも、やっぱりそれは\x01",
            "ただの逃げだったのかもしれない。\x02\x03",

            "#0106F今日、あった出来事は\x01",
            "どれも予想の範囲内だったけど……\x02\x03",

            "想像以上に重たく、冷たかった。\x02\x03",

            "それを突きつけられて……\x01",
            "またしても途方にくれてしまった。\x02\x03",

            "#0108F結局私は……自分一人では\x01",
            "何もなし得ないのかもしれない。\x02\x03",

            "父と母に見捨てられた……\x01",
            "幼い少女のままなのかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    #C0106
    ChrTalk(
        0x101,
        "#6P#0001F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(300)

    #C0107
    ChrTalk(
        0x101,
        "#6P#0004F──それで、いいじゃないか。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x11,
        "#0105F#5P……え…………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x11, 0x101, 400)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    Fade(1000)
    OP_68(-21800, 2400, -18300, 0)
    MoveCamera(42, 15, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(15000, 0)
    OP_0D()

    #C0109
    ChrTalk(
        0x101,
        (
            "#12P#0000Fエリィはさ、完璧すぎるんだよ。\x02\x03",

            "全て自分が、一度も失敗しないで\x01",
            "やり遂げる必要がある……\x02\x03",

            "そんな風に思ってるんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x11,
        "#0101F#5P#40Wそ……そんな事は……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#12P#0006F……確かに今日は色々と\x01",
            "ヘコまされることが多かった。\x02\x03",

            "#0001Fでも、そんなのは\x01",
            "働いてれば当たり前の事なんだ。\x02\x03",

            "#0000Fそして……\x01",
            "今日乗り越えられなかった《壁》は\x01",
            "明日には乗り越えられるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x11,
        "#0105F#5P《壁》……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#12P#0003Fこの場合の《壁》ってのは\x01",
            "脅迫状の事件のことだ。\x02\x03",

            "#0008F一課が出張って、俺達の手を\x01",
            "離れかけているこの事件……\x02\x03",

            "#0001Fできれば一課とは別に\x01",
            "独自に動いて追ってみたい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0114
    ChrTalk(
        0x11,
        (
            "#0101F#5Pええっ……！？\x02\x03",

            "#0108Fで、でもこれ以上、\x01",
            "私たちが出来る事なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#12P#0003F一課は一課で\x01",
            "大したものかもしれないけど……\x02\x03",

            "それでも、警察の論理でしか\x01",
            "動いていないのは確かだと思う。\x02\x03",

            "#0008Fひょっとしたら別の切り口で\x01",
            "事件が追えるんじゃないか……\x02\x03",

            "#0000Fそんな気がしてきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x11,
        "#0105F#5Pロイド……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#12P#0004Fそう、さっきエリィが言った\x01",
            "話に似ているだろ？\x02\x03",

            "#0000Fこれでもし、俺たちが大金星を\x01",
            "上げることが出来れば……\x02\x03",

            "エリィが目指そうとしている事だって\x01",
            "決して不可能じゃないんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x11,
        "#0105F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#12P#0008Fもちろん、今回の事件と\x01",
            "クロスベル全体の大きな問題は\x01",
            "一緒にはできないかもしれない。\x02\x03",

            "#0003Fでも……俺たちに必要なのは\x01",
            "《壁》を乗り越えるための力だ。\x02\x03",

            "#0000Fこういった小さな《壁》を\x01",
            "一つずつ乗り越えていければ……\x02\x03",

            "いずれ巨大な《壁》を\x01",
            "乗り越えられる力だって\x01",
            "手に入れられるんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x11,
        "#0108F#5P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x5A, 0x12C)
    Sleep(500)

    #C0121
    ChrTalk(
        0x11,
        (
            "#0106F#5P──この２ヶ月、\x01",
            "一緒にいて何となく分かった。\x02\x03",

            "貴方もまた、\x01",
            "私と違った悩みを抱えている。\x02\x03",

            "#0108Fそれなのに……どうして\x01",
            "そんなに前向きでいられるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#12P#0005F……俺は、そうだな……\x02\x03",

            "#0000F目指している人がいるから\x01",
            "前に進めているのかもしれない。\x02\x03",

            "#0012Fそれはそれで……\x01",
            "問題なのかもしれないけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x11,
        (
            "#0104F#5Pそう……\x02\x03",

            "#0108F……でも私は……\x01",
            "貴方ほど強くないみたい。\x02\x03",

            "少し……疲れちゃった……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        "#12P#0001F………………………………\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x11,
        (
            "#0106F#5P#30W……本当は昔のことなんて　\x01",
            "話すつもりはなかったの……\x02\x03",

            "でも……何だか\x01",
            "耐え切れなくなってしまって……\x02\x03",

            "#0108F#40Wこのままじゃ、本当にあなたたちの\x01",
            "足を引っ張るかもしれない……\x02\x03",

            "だったらいっそ……もう……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#12P#0004F──エリィ。\x02",
    )

    CloseMessageWindow()

    def lambda_5B67():
        OP_96(0xFE, 0xFFFFAAD8, 0x514, 0xFFFFB7BC, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B67)
    OP_68(-21800, 2300, -17700, 1300)
    MoveCamera(43, 15, 0, 1300)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x10)
    SetChrFlags(0x11, 0x2)
    OP_0D()
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x11, 0x11)
    Fade(500)
    SetCameraDistance(14500, 500)
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x11, 0x12)
    Sleep(100)
    Sound(804, 0, 80, 0)
    SetChrSubChip(0x101, 0x3)
    SetChrSubChip(0x11, 0x13)
    OP_0D()
    Sleep(300)

    def lambda_5BF4():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5BF4)
    WaitChrThread(0x11, 2)
    Sleep(500)

    #C0127
    ChrTalk(
        0x11,
        "#0105F#5P#40W……あ…………\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#12P#0001F俺には……\x01",
            "俺たちにはエリィが必要だ。\x02\x03",

            "射撃の腕、交渉センス、\x01",
            "政治経済の知識とバランス感覚……\x02\x03",

            "この街を相手にするには\x01",
            "どれも必要不可欠だと思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x11,
        "#0108F#5P#40W……で、でも………\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#12P#0004Fいや……違うな。\x02\x03",

            "それも確かにそうだけど、\x01",
            "そんな事よりも前に……\x02\x03",

            "#0002Fエリィが側にいてくれたら\x01",
            "俺はそれだけで嬉しいんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x4)
    SetChrSubChip(0x11, 0x14)
    Sleep(100)
    SetChrSubChip(0x101, 0x5)
    SetChrSubChip(0x11, 0x15)
    Sleep(100)
    SetChrSubChip(0x101, 0x6)
    SetChrSubChip(0x11, 0x16)

    #C0131
    ChrTalk(
        0x11,
        "#0112F#5P#40Wえ……\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#12P#0004Fバラバラな俺たちだったけど\x01",
            "この２ヶ月で呼吸も合ってきた。\x02\x03",

            "忙しい毎日に翻弄されながらも\x01",
            "食事当番なんかも決めたりして……\x02\x03",

            "#0000Fお互いの得意分野に関しては\x01",
            "もう何も言わずに信頼できるしな。\x02\x03",

            "そんな仲間がいるっていうのは\x01",
            "それだけで嬉しいもんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x6)
    SetChrSubChip(0x11, 0x16)
    Sleep(100)
    SetChrSubChip(0x101, 0x7)
    SetChrSubChip(0x11, 0x17)
    Sleep(100)
    SetChrSubChip(0x101, 0x8)
    SetChrSubChip(0x11, 0x18)
    Sleep(100)
    SetChrSubChip(0x101, 0x7)
    SetChrSubChip(0x11, 0x17)
    Sleep(100)
    SetChrSubChip(0x101, 0x6)
    SetChrSubChip(0x11, 0x16)
    Sleep(500)

    #C0133
    ChrTalk(
        0x11,
        "#0102F#5P#30W………あ………………\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#12P#0006F……俺たちは若造だ。\x02\x03",

            "世界を甘く見るにも、\x01",
            "絶望するにもまだ早すぎる。\x02\x03",

            "#0008F力を尽くして、やれる事をやって\x01",
            "何度でも諦めずに挑戦して……\x02\x03",

            "#0002Fそれでも駄目なら……\x01",
            "その時はみんなで考えればいい。\x02\x03",

            "俺はもちろん、ランディもティオも\x01",
            "きっと力になってくれる。\x02\x03",

            "ああ見えて課長だって\x01",
            "色々根回しをしてくれているし……\x02\x03",

            "ツァイトなんていう\x01",
            "変わった助っ人も来てくれたしな。\x02\x03",

            "#0009Fエリィ──君は一人じゃないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x11,
        (
            "#0112F#30W#5P…………………………………\x02\x03",

            "#0104F#30W……ふふっ………\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x6)
    SetChrSubChip(0x11, 0x16)
    Sleep(100)
    SetChrSubChip(0x101, 0x7)
    SetChrSubChip(0x11, 0x17)
    Sleep(100)
    SetChrSubChip(0x101, 0x8)
    SetChrSubChip(0x11, 0x18)
    Sleep(500)

    #C0136
    ChrTalk(
        0x11,
        (
            "#0104F#5P#30W一人じゃない……か。\x02\x03",

            "……そうね。\x02\x03",

            "そんな当たり前の事を……\x01",
            "私は忘れていたのかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(120)
    SetChrSubChip(0x101, 0x9)
    SetChrSubChip(0x11, 0x19)
    Sleep(120)
    SetChrSubChip(0x101, 0xA)
    SetChrSubChip(0x11, 0x1A)
    Sleep(120)
    SetChrSubChip(0x101, 0xB)
    SetChrSubChip(0x11, 0x1B)
    Sleep(120)
    SetChrSubChip(0x101, 0xC)
    SetChrSubChip(0x11, 0x1C)
    Sleep(120)
    SetChrSubChip(0x101, 0xD)
    SetChrSubChip(0x11, 0x1D)
    Sleep(1000)

    #C0137
    ChrTalk(
        0x11,
        (
            "#0102F#5P──ありがとう、ロイド。\x02\x03",

            "私自身の問題は簡単に\x01",
            "解決するものではないけど……\x02\x03",

            "#0109Fそれでも少し、\x01",
            "気が楽になった気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        "#12P#0002Fそっか……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x11,
        (
            "#0113F#5Pふう……それにしても。\x02\x03",

            "青春ドラマみたいな台詞はともかく、\x01",
            "少しびっくりしちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#12P#0006Fう……\x01",
            "クサイのは承知してるよ。\x02\x03",

            "#0005Fでも、ビックリしたって？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x11,
        (
            "#0113F#5Pだ、だって……\x02\x03",

            "……私が必要だとか、\x01",
            "側に居てくれて嬉しいとか……\x02\x03",

            "てっきり告白でも\x01",
            "されているのかなって……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#12P#0005Fへ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(1087, 255, 100, 0)    #voice#Lloyd
    OP_68(-21800, 2400, -18300, 800)
    MoveCamera(37, 13, 0, 800)
    SetCameraDistance(15000, 800)
    ClearChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    TurnDirection(0x11, 0x101, 0)
    Sound(804, 0, 100, 0)

    def lambda_6468():
        OP_96(0xFE, 0xFFFFAAD8, 0x514, 0xFFFFB5C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6468)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)

    #C0143
    ChrTalk(
        0x101,
        (
            "#12P#0011Fい、いや！\x01",
            "別にそんな意味じゃ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x11,
        (
            "#0101F#5Pあら……？\x02\x03",

            "私なんか、告白する価値すら\x01",
            "ないっていうことかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            "#12P#0006Fそ、そうじゃなくて……\x02\x03",

            "#0013Fああもう……\x01",
            "エリィ、からかってるだろ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x11,
        (
            "#0104F#5Pふふっ……お返しよ。\x02\x03",

            "#0102Fでも貴方、ちょっと\x01",
            "気をつけた方がいいわね。\x02\x03",

            "天然っていうか……\x01",
            "凄く女たらしな所があるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#12P#0011Fちょ、ちょっと待て！\x02\x03",

            "ランディならともかく\x01",
            "なんで俺がそんな……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x11,
        (
            "#0111F#5P……自覚がない所が\x01",
            "またタチが悪いというか……\x02\x03",

            "#0113Fはあ……参ったわね。\x02\x03",

            "……まさかあんな言葉だけで\x01",
            "こんなに気分が変わるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        "#12P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x11,
        (
            "#0101F#5Pな、何でもありません。\x02\x03",

            "#0106Fその──課長への報告を\x01",
            "任せてしまってごめんなさい。\x02\x03",

            "#0100F脅迫状の捜査だけど……\x01",
            "何かプランはあるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#12P#0006Fいや、今のところは。\x02\x03",

            "#0000Fただ結局のところ……\x01",
            "全ては《銀#2Rイン#》の狙いだと思う。\x02\x03",

            "それを探る糸口が無いか、\x01",
            "明日、みんなで話したいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x11,
        (
            "#0104F#5P分かったわ。\x02\x03",

            "#0102Fおかげで今夜は……\x01",
            "ゆっくり休めそうな気がする。\x02\x03",

            "お互い頭をすっきりとさせて\x01",
            "ミーティングに臨みましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        "#12P#0002Fああ……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    ReplaceBGM("ed7100", "ed7000")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 2)), scpexpr(EXPR_END)), "loc_69C7")
    AddCraft(0x0, 0x154)
    AddCraft(0x1, 0x154)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとエリィがコンビクラフト\x01\x07\x02",

            "『スターブラストⅡ』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0155
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＣＰを１００ずつ消費することで\x01",
            "強力なコンビネーション攻撃が繰り出せます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_6A84")

    label("loc_69C7")

    AddCraft(0x0, 0x14A)
    AddCraft(0x1, 0x14A)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとエリィがコンビクラフト\x01\x07\x02",

            "『スターブラスト』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＣＰを１００ずつ消費することで\x01",
            "強力なコンビネーション攻撃が繰り出せます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6A84")

    OP_CA(0x1, 0xFF, 0x0)
    SetMapFlags(0x10000000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_37F1 end

    def Function_23_6AC8(): pass

    label("Function_23_6AC8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch20400.itc", 0x1F)
    LoadChrToIndex("chr/ch20500.itc", 0x20)
    LoadChrToIndex("chr/ch20800.itc", 0x21)
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
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x8, 0x1B)
    OP_78(0x9, 0x1C)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x4)
    OP_49()
    SetChrPos(0x1B, -23000, 0, -3000, 0)
    OP_D3(0x1B, 0x0, 0x15F90, 0x0, 0x0)
    OP_70(0x8, 0x0)
    SetChrPos(0x1C, 8000, 0, 3500, 0)
    OP_D3(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    OP_4B(0x1D, 0xFF)
    SetChrPos(0x1D, 5000, 0, -6300, 270)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -6800, 0, 4000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -8300, 0, 2500, 90)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    OP_4B(0x20, 0xFF)
    SetChrPos(0x20, -10300, 0, 10400, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, 0, 0, 15000, 315)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)

    def lambda_6D0B():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6D0B)

    def lambda_6D25():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6D25)

    def lambda_6D3F():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_6D3F)
    Sound(458, 0, 100, 0)

    def lambda_6D60():
        OP_96(0xFE, 0x4E20, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6D60)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x22, 1, 0, 15)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-16000, 2400, 17000, 0)
    MoveCamera(355, 35, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetCameraDistance(18500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x22, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 1)
    NewScene("c050B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_6AC8 end

    def Function_24_6E42(): pass

    label("Function_24_6E42")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    OP_68(-1000, 1500, 11000, 5000)
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
    SetScenarioFlags(0x5C, 5)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_6E42 end

    def Function_25_6F36(): pass

    label("Function_25_6F36")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch20400.itc", 0x1F)
    LoadChrToIndex("chr/ch20500.itc", 0x20)
    LoadChrToIndex("chr/ch20800.itc", 0x21)
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
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x8, 0x1B)
    OP_78(0x9, 0x1C)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x4)
    OP_49()
    SetChrPos(0x1B, -23000, 0, -3000, 0)
    OP_D3(0x1B, 0x0, 0x15F90, 0x0, 0x0)
    OP_70(0x8, 0x0)
    SetChrPos(0x1C, 8000, 0, 3500, 0)
    OP_D3(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    OP_4B(0x1D, 0xFF)
    SetChrPos(0x1D, 5000, 0, -6300, 270)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -6800, 0, 4000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -8300, 0, 2500, 90)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    OP_4B(0x20, 0xFF)
    SetChrPos(0x20, -10300, 0, 10400, 0)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, 0, 0, 15000, 315)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K同日、２０：４５──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7516", 0)

    def lambda_71B1():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_71B1)

    def lambda_71CB():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_71CB)

    def lambda_71E5():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_71E5)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x22, 1, 0, 26)
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
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    EndChrThread(0x22, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 7)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_6F36 end

    def Function_26_728A(): pass

    label("Function_26_728A")

    Sound(803, 2, 80, 0)
    Sleep(5000)
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

    # Function_26_728A end

    def Function_27_72C1(): pass

    label("Function_27_72C1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch31250.itc", 0x22)
    LoadChrToIndex("chr/ch31251.itc", 0x23)
    LoadChrToIndex("chr/ch31350.itc", 0x24)
    LoadChrToIndex("chr/ch31351.itc", 0x25)
    LoadChrToIndex("chr/ch00150.itc", 0x26)
    LoadChrToIndex("chr/ch00151.itc", 0x27)
    LoadChrToIndex("chr/ch00250.itc", 0x28)
    LoadChrToIndex("chr/ch00251.itc", 0x29)
    LoadChrToIndex("chr/ch00950.itc", 0x2A)
    LoadChrToIndex("chr/ch00951.itc", 0x2B)
    OP_68(-21800, -1000, -2300, 0)
    MoveCamera(57, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    OP_90(0x101, -33800, 0, -3300, 90)
    SetChrChipByIndex(0x102, 0x26)
    SetChrSubChip(0x102, 0x0)
    OP_90(0x102, -35400, 0, -2300, 90)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    OP_90(0x103, -35600, 0, -4000, 90)
    OP_90(0x104, -33900, 0, -5000, 90)
    SetChrChipByIndex(0x10A, 0x2A)
    SetChrSubChip(0x10A, 0x0)
    OP_90(0x10A, -37200, 0, -4600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    OP_90(0xE, -36400, 0, -5700, 90)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x12, 0x20)
    ClearChrFlags(0x12, 0x4)
    OP_90(0x12, -37200, 0, -1600, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x13, 700, 0, -13500, 225)
    SetChrPos(0x14, 1700, 0, -14500, 225)
    SetChrPos(0x17, -600, 0, -16000, 270)
    SetChrPos(0x18, -600, 0, -17600, 270)
    SetChrPos(0x19, 1400, 0, -16800, 270)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_78(0x11, 0x1B)
    SetMapObjFlags(0x11, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x4)
    OP_49()
    SetChrPos(0x1B, 4000, 0, -11500, 0)
    OP_D3(0x1B, 0x0, 0x4CE78, 0x0, 0x0)
    OP_74(0x11, 0x1E)
    OP_70(0x11, 0x0)

    def lambda_7587():
        OP_96(0xFE, 0xFFFFCA18, 0x0, 0xFFFFF31C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7587)
    Sleep(50)

    def lambda_75A4():
        OP_96(0xFE, 0xFFFFC9B4, 0x0, 0xFFFFEC78, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75A4)
    Sleep(100)

    def lambda_75C1():
        OP_96(0xFE, 0xFFFFC310, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_75C1)
    Sleep(50)

    def lambda_75DE():
        OP_96(0xFE, 0xFFFFC3D8, 0x0, 0xFFFFF704, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75DE)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 3, 0, 3)

    def lambda_761F():
        OP_96(0xFE, 0xFFFFBCD0, 0x0, 0xFFFFF9C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_761F)
    Sleep(100)

    def lambda_763C():
        OP_96(0xFE, 0xFFFFBCD0, 0x0, 0xFFFFEE08, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_763C)
    Sleep(50)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_7661():
        OP_96(0xFE, 0xFFFFBFF0, 0x0, 0xFFFFE9BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7661)
    OP_68(-13800, 0, -2300, 4000)
    MoveCamera(47, 25, 0, 4000)
    SetCameraDistance(19500, 4000)
    FadeToBright(2000, 0)
    BeginChrThread(0x22, 1, 0, 35)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x12, 1)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x22, 0x1)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x10A, 1)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    MoveCamera(40, 25, 0, 3000)
    OP_68(2280, 0, -11990, 3000)

    def lambda_7786():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7786)
    Sleep(50)

    def lambda_7796():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7796)
    Sleep(50)

    def lambda_77A6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_77A6)
    Sleep(50)

    def lambda_77B6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_77B6)
    Sleep(50)

    def lambda_77C6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_77C6)
    Sleep(50)

    def lambda_77D6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_77D6)
    Sleep(50)

    def lambda_77E6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_77E6)
    OP_6F(0x41)
    Sleep(1000)
    Fade(500)
    OP_68(-13800, 0, -2300, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    #C0159
    ChrTalk(
        0x101,
        (
            "#5P#0010Fクッ……\x01",
            "どうすれば……！\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#5P#0107F警察本部に行くなら\x01",
            "このまま行政区に……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x2D, 0x1F4)

    #C0161
    ChrTalk(
        0x103,
        "#6P#0207Fだ、ダメです……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(12700, 900, 27800, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)

    def lambda_7905():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7905)

    def lambda_7912():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7912)

    def lambda_791F():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_791F)

    def lambda_792C():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_792C)

    def lambda_7939():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7939)

    def lambda_7946():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_7946)
    SetChrPos(0x17, 11800, 0, 38800, 180)
    SetChrPos(0x18, 10900, 0, 40300, 180)
    SetChrPos(0x19, 12700, 0, 40600, 180)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x25)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x13, 11800, 0, 43800, 180)
    SetChrPos(0x14, 10900, 0, 45300, 180)
    SetChrPos(0x15, 12700, 0, 45600, 180)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_68(12700, 900, 21800, 4000)
    SetCameraDistance(18500, 4000)

    def lambda_7A0D():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7A0D)

    def lambda_7A27():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_7A27)
    Sleep(50)

    def lambda_7A44():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7A44)

    def lambda_7A5E():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7A5E)
    Sleep(50)

    def lambda_7A7B():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7A7B)

    def lambda_7A95():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7A95)
    OP_6F(0x11)
    Sleep(1000)
    Fade(500)
    OP_68(-13800, 0, -2300, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    EndChrThread(0x17, 0xFF)
    EndChrThread(0x18, 0xFF)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    EndChrThread(0x15, 0xFF)
    OP_93(0x10A, 0x5A, 0x1F4)

    #C0162
    ChrTalk(
        0x10A,
        "#6P#0607F裏通りを抜けろ……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0163
    ChrTalk(
        0x101,
        "#11P#0007Fはい……！\x02",
    )

    CloseMessageWindow()
    OP_68(-12500, 1000, 13000, 4000)
    MoveCamera(7, 20, 0, 4000)
    SetCameraDistance(17500, 4000)
    BeginChrThread(0x101, 3, 0, 28)
    BeginChrThread(0x104, 3, 0, 29)
    BeginChrThread(0x102, 3, 0, 30)
    BeginChrThread(0x103, 3, 0, 31)
    BeginChrThread(0x10A, 3, 0, 32)
    BeginChrThread(0xE, 3, 0, 33)
    BeginChrThread(0x12, 3, 0, 34)
    OP_6F(0x79)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x10A, 0xFF)
    EndChrThread(0xE, 0xFF)
    EndChrThread(0x12, 0xFF)
    SetScenarioFlags(0x5C, 2)
    NewScene("c050B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_72C1 end

    def Function_28_7BCE(): pass

    label("Function_28_7BCE")

    OP_92(0x101, 0xFFFFD314, 0x2EE0, 0x1F4)

    def lambda_7BE0():
        OP_95(0xFE, -11500, 0, 12000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7BE0)
    WaitChrThread(0x101, 1)

    def lambda_7BFE():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7BFE)
    WaitChrThread(0x101, 1)
    Return()

    # Function_28_7BCE end

    def Function_29_7C18(): pass

    label("Function_29_7C18")

    Sleep(300)
    OP_92(0x104, 0xFFFFD314, 0x2EE0, 0x1F4)

    def lambda_7C2D():
        OP_95(0xFE, -11500, 0, 12000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C2D)
    WaitChrThread(0x104, 1)

    def lambda_7C4B():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C4B)
    WaitChrThread(0x104, 1)
    Return()

    # Function_29_7C18 end

    def Function_30_7C65(): pass

    label("Function_30_7C65")

    Sleep(900)
    OP_92(0x102, 0xFFFFCD9C, 0x2AF8, 0x1F4)

    def lambda_7C7A():
        OP_95(0xFE, -12900, 0, 11000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C7A)
    WaitChrThread(0x102, 1)

    def lambda_7C98():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C98)
    WaitChrThread(0x102, 1)
    Return()

    # Function_30_7C65 end

    def Function_31_7CB2(): pass

    label("Function_31_7CB2")

    Sleep(1200)
    OP_92(0x103, 0xFFFFCD9C, 0x2AF8, 0x1F4)

    def lambda_7CC7():
        OP_95(0xFE, -12900, 0, 11000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7CC7)
    WaitChrThread(0x103, 1)

    def lambda_7CE5():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7CE5)
    WaitChrThread(0x103, 1)
    Return()

    # Function_31_7CB2 end

    def Function_32_7CFF(): pass

    label("Function_32_7CFF")

    Sleep(2500)

    def lambda_7D07():
        OP_95(0xFE, -12800, 0, 12000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7D07)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0xB4, 0x1F4)
    Sleep(1500)
    OP_93(0x10A, 0x13B, 0x1F4)

    def lambda_7D36():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7D36)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_32_7CFF end

    def Function_33_7D50(): pass

    label("Function_33_7D50")

    Sleep(2000)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_7D60():
        OP_95(0xFE, -11500, 0, 13300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7D60)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    OP_93(0xE, 0x5A, 0x1F4)
    Sound(531, 0, 100, 0)
    Sleep(1550)
    OP_93(0xE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_7DA5():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7DA5)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    Return()

    # Function_33_7D50 end

    def Function_34_7DC7(): pass

    label("Function_34_7DC7")

    Sleep(3000)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 3)
    BeginChrThread(0x22, 1, 0, 35)

    def lambda_7DF9():
        OP_95(0xFE, -15300, 0, 8300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7DF9)
    WaitChrThread(0x12, 1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x22, 0x1)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_7E3D():
        OP_92(0xFE, 0xFFFFB690, 0x300C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7E3D)
    WaitChrThread(0x12, 2)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x2)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    SetChrSubChip(0x12, 0x3)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_7EA1():
        OP_9D(0xFE, 0xFFFFB690, 0x6A4, 0x300C, 0x898, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7EA1)
    Sleep(600)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x2)
    WaitChrThread(0x12, 1)

    def lambda_7ED0():
        OP_92(0xFE, 0xFFFFB690, 0x4F4C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7ED0)
    SetChrSubChip(0x12, 0x3)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_7EF4():
        OP_9D(0xFE, 0xFFFFB690, 0x0, 0x4F4C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7EF4)
    Sleep(500)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x2)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x3)
    Sleep(50)
    BeginChrThread(0x12, 0, 0, 3)
    BeginChrThread(0x22, 1, 0, 35)

    def lambda_7F36():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7F36)
    WaitChrThread(0x12, 1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x22, 0x1)
    Return()

    # Function_34_7DC7 end

    def Function_35_7F58(): pass

    label("Function_35_7F58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F71")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_35_7F58")

    label("loc_7F71")

    Return()

    # Function_35_7F58 end

    def Function_36_7F72(): pass

    label("Function_36_7F72")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch31252.itc", 0x22)
    LoadChrToIndex("chr/ch31251.itc", 0x23)
    LoadChrToIndex("chr/ch31350.itc", 0x24)
    LoadChrToIndex("chr/ch31351.itc", 0x25)
    LoadChrToIndex("chr/ch00150.itc", 0x26)
    LoadChrToIndex("chr/ch00151.itc", 0x27)
    LoadChrToIndex("chr/ch00250.itc", 0x28)
    LoadChrToIndex("chr/ch00251.itc", 0x29)
    LoadChrToIndex("chr/ch00950.itc", 0x2A)
    LoadChrToIndex("chr/ch00951.itc", 0x2B)
    LoadChrToIndex("chr/ch00952.itc", 0x2C)
    LoadChrToIndex("apl/ch50509.itc", 0x2D)
    SetChrPos(0x101, 11300, 0, 35900, 180)
    SetChrChipByIndex(0x102, 0x26)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 12700, 0, 37800, 180)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 10600, 0, 36800, 180)
    SetChrPos(0x104, 12900, 0, 36300, 180)
    SetChrChipByIndex(0x10A, 0x2A)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x10A, 13100, 0, 39700, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrPos(0xE, 11500, 0, 39100, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    SetChrPos(0x12, 14800, 0, 38800, 180)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x13, -2200, 0, -2600, 90)
    SetChrPos(0x17, -2100, 0, -4500, 90)
    SetChrPos(0x14, 0, 0, -12100, 45)
    SetChrPos(0x18, 400, 0, -13400, 45)
    SetChrPos(0x15, 11600, 500, 13800, 270)
    SetChrPos(0x16, 11600, 500, 13800, 270)
    SetChrPos(0x19, 14700, 0, 13800, 180)
    SetChrPos(0x1A, 11600, 500, 13800, 270)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_78(0x11, 0x1B)
    SetMapObjFlags(0x11, 0x1000)
    SetMapObjFlags(0x11, 0x4)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x4)
    OP_49()
    SetChrPos(0x1B, 12600, 0, 23500, 0)
    OP_D3(0x1B, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x12, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_68(0, 800, 4000, 0)
    MoveCamera(18, 22, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(28000, 0)

    def lambda_8294():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8294)
    Sleep(50)

    def lambda_82B1():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_82B1)
    Sleep(50)

    def lambda_82CE():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_82CE)
    Sleep(50)

    def lambda_82EB():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_82EB)
    Sleep(50)

    def lambda_8308():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_8308)
    Sleep(50)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_832D():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_832D)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    BeginChrThread(0x12, 0, 0, 3)

    def lambda_8358():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8358)
    MoveCamera(42, 22, 0, 9000)
    SetCameraDistance(33000, 9000)
    FadeToBright(2000, 0)
    OP_6F(0x50)
    BeginChrThread(0x22, 1, 0, 35)
    Fade(500)
    OP_68(12700, 1000, -2200, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    WaitChrThread(0x12, 1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x22, 0x1)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)

    #C0164
    ChrTalk(
        0x101,
        "#5P#0006Fはあはあ……\x02",
    )

    CloseMessageWindow()

    #N0165
    NpcTalk(
        0x101,
        "キーア",
        "#6P#1105F戻ってきたねー。\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x13B, 0x2BC)
    Sleep(750)
    OP_93(0x103, 0xE1, 0x2BC)
    Sleep(300)

    #C0166
    ChrTalk(
        0x103,
        (
            "#5P#0202Fでも、警備隊の姿は\x01",
            "居なくなってるみたいです。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0167
    ChrTalk(
        0x104,
        "#0302F#11Pうまく撒#2Rま#けたって事か……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0xE, 500)

    #C0168
    ChrTalk(
        0x10A,
        "#11P#0600Fセルゲイさん……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xE,
        "#5P#1003F……ああ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xE)
    OP_68(12400, 900, -1100, 1000)
    MoveCamera(45, 19, 0, 1000)
    SetCameraDistance(17000, 1000)
    OP_93(0x10A, 0xB4, 0x190)
    OP_6F(0x79)

    #C0170
    ChrTalk(
        0xE,
        (
            "#1002F#5P──よし。\x01",
            "ここから先は別行動だ。\x02\x03",

            "お前たちは東通りを抜けて\x01",
            "クロスベル市から脱出しろ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_85FA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_85FA)
    Sleep(50)

    def lambda_860A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_860A)
    Sleep(50)

    def lambda_861A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_861A)
    Sleep(50)

    def lambda_862A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_862A)
    OP_93(0x104, 0x0, 0x1F4)

    #C0171
    ChrTalk(
        0x101,
        "#12P#0005F！？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xE,
        (
            "#1003F#5Pどうやら暴走してるのは\x01",
            "ベルガード門の警備隊のようだ。\x02\x03",

            "多分、ソーニャの部下たちは\x01",
            "アテに出来るだろう。\x02\x03",

            "#1001F街道に出たら\x01",
            "タングラム門に連絡して\x01",
            "車両で迎えに来てもらえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#12P#0001Fわ、分かりました……\x01",
            "ですが課長たちは？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xE,
        (
            "#1003F#5P俺とダドリーは\x01",
            "撹乱のためここに残る。\x02\x03",

            "#1002F連中の注意を引きつけて\x01",
            "かき回してやるつもりだ。\x02",
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

    #C0175
    ChrTalk(
        0x101,
        "#12P#0007Fそ、そんな……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        (
            "#0307Fおいおい、\x01",
            "なに無茶言ってんだ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x10A,
        (
            "#5P#0604Fフン、私たち２人ならば\x01",
            "撹乱してから撤退することなど\x01",
            "造作もないことだ。\x02\x03",

            "#0607Fグズグズするな！\x01",
            "一刻の猶予もないのだぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#12P#0008Fダドリーさん……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0179
    ChrTalk(
        0x102,
        "#5P#0101F……行きましょう！\x02",
    )

    CloseMessageWindow()

    #N0180
    NpcTalk(
        0x101,
        "キーア",
        (
            "#1101F#11Pかちょー！\x01",
            "気をつけてねー！\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xE,
        "#1002F#5Pああ……！\x02",
    )

    CloseMessageWindow()
    OP_68(15400, 900, -1100, 4000)

    def lambda_898E():

        label("loc_898E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_898E")

    QueueWorkItem2(0xE, 2, lambda_898E)

    def lambda_89A0():

        label("loc_89A0")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_89A0")

    QueueWorkItem2(0x10A, 2, lambda_89A0)
    BeginChrThread(0x104, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 38)
    BeginChrThread(0x12, 3, 0, 39)
    WaitChrThread(0x104, 3)
    EndChrThread(0xE, 0x2)
    EndChrThread(0x10A, 0x2)
    OP_6F(0x1)
    EndChrThread(0x22, 0x1)
    Fade(1000)
    OP_68(10960, 900, 150, 0)
    MoveCamera(50, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    OP_52(0x10A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MoveCamera(42, 11, 0, 8000)
    SetCameraDistance(16000, 8000)
    BeginChrThread(0x10A, 3, 0, 40)
    BeginChrThread(0xE, 3, 0, 41)
    BeginChrThread(0x1B, 3, 0, 37)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    BeginChrThread(0x13, 3, 0, 42)
    BeginChrThread(0x14, 3, 0, 43)
    BeginChrThread(0x15, 3, 0, 44)
    BeginChrThread(0x16, 3, 0, 45)
    BeginChrThread(0x17, 3, 0, 46)
    BeginChrThread(0x18, 3, 0, 47)
    BeginChrThread(0x19, 3, 0, 48)
    BeginChrThread(0x1A, 3, 0, 49)
    OP_6F(0x50)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x19, 3)
    WaitChrThread(0x1A, 3)

    #C0182
    ChrTalk(
        0xE,
        (
            "#11P#1003F──ダドリー。\x02\x03",

            "#1002F一課のエースの実力、\x01",
            "改めて見せてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x10A,
        (
            "#0604F#5Pそちらこそ……\x02\x03",

            "#0602Fかつてあの２人を率いていた\x01",
            "伝説の班長の実力、\x01",
            "見せてもらいましょうか！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    RemoveParty(0x9, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c100B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_7F72 end

    def Function_37_8C0D(): pass

    label("Function_37_8C0D")

    Sound(489, 0, 100, 0)
    ClearMapObjFlags(0x11, 0x4)

    def lambda_8C1E():
        OP_96(0xFE, 0x3138, 0x0, 0x34BC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_8C1E)
    WaitChrThread(0x1B, 1)
    Sound(495, 0, 100, 0)
    SetMapObjFlags(0x11, 0x20)
    OP_71(0x11, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x11)
    OP_24(0x1E9)
    OP_71(0x11, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x11)
    Return()

    # Function_37_8C0D end

    def Function_38_8C6B(): pass

    label("Function_38_8C6B")

    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_8C77():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8C77)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_8C6B end

    def Function_39_8C91(): pass

    label("Function_39_8C91")

    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    BeginChrThread(0x12, 0, 0, 3)
    BeginChrThread(0x22, 1, 0, 35)

    def lambda_8CB1():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8CB1)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0x12, 0x8)
    Return()

    # Function_39_8C91 end

    def Function_40_8CD0(): pass

    label("Function_40_8CD0")

    Sleep(1500)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)

    def lambda_8CE0():
        OP_95(0xFE, 11600, 0, 300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_8CE0)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x0, 0x1F4)
    SetChrChipByIndex(0x10A, 0x2A)
    SetChrSubChip(0x10A, 0x0)
    Sleep(300)
    SetChrChipByIndex(0x10A, 0x2C)
    SetChrSubChip(0x10A, 0x0)
    Sound(531, 0, 100, 0)
    Return()

    # Function_40_8CD0 end

    def Function_41_8D1A(): pass

    label("Function_41_8D1A")

    Sleep(2500)
    OP_93(0xE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x3)
    Sleep(70)
    SetChrSubChip(0xE, 0x2)
    Sleep(70)
    SetChrSubChip(0xE, 0x1)
    Sleep(70)
    SetChrSubChip(0xE, 0x0)
    Sound(531, 0, 100, 0)
    Sleep(70)
    SetChrSubChip(0xE, 0x1)
    Sleep(70)
    SetChrSubChip(0xE, 0x2)
    Sleep(70)
    SetChrSubChip(0xE, 0x3)
    Sleep(70)
    SetChrSubChip(0xE, 0x4)
    Return()

    # Function_41_8D1A end

    def Function_42_8D64(): pass

    label("Function_42_8D64")

    Sleep(3000)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8D74():
        OP_96(0xFE, 0x12C0, 0x0, 0xFFFFF5D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D74)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 100, 0)
    Return()

    # Function_42_8D64 end

    def Function_43_8DAA(): pass

    label("Function_43_8DAA")

    Sleep(3500)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8DBA():
        OP_96(0xFE, 0x19C8, 0x0, 0xFFFFEA84, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8DBA)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 100, 0)
    Return()

    # Function_43_8DAA end

    def Function_44_8DF0(): pass

    label("Function_44_8DF0")

    WaitChrThread(0x1B, 3)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8E04():
        OP_95(0xFE, 10300, 0, 13800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E04)

    def lambda_8E1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8E1E)
    WaitChrThread(0xFE, 1)

    def lambda_8E33():
        OP_95(0xFE, 8100, 0, 5500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E33)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 100, 0)
    Return()

    # Function_44_8DF0 end

    def Function_45_8E70(): pass

    label("Function_45_8E70")

    WaitChrThread(0x1B, 3)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8E81():
        OP_95(0xFE, 10300, 0, 13800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E81)

    def lambda_8E9B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8E9B)
    WaitChrThread(0xFE, 1)

    def lambda_8EB0():
        OP_95(0xFE, 9900, 0, 6900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8EB0)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 100, 0)
    Return()

    # Function_45_8E70 end

    def Function_46_8EED(): pass

    label("Function_46_8EED")

    Sleep(3000)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8EFD():
        OP_96(0xFE, 0x1324, 0x0, 0xFFFFEE6C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8EFD)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    Return()

    # Function_46_8EED end

    def Function_47_8F25(): pass

    label("Function_47_8F25")

    Sleep(3600)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8F35():
        OP_96(0xFE, 0x1B58, 0x0, 0xFFFFE570, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F35)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    Return()

    # Function_47_8F25 end

    def Function_48_8F5D(): pass

    label("Function_48_8F5D")

    WaitChrThread(0x1B, 3)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8F71():
        OP_95(0xFE, 14700, 0, 8500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F71)

    def lambda_8F8B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8F8B)
    WaitChrThread(0xFE, 1)

    def lambda_8FA0():
        OP_95(0xFE, 13300, 0, 7100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FA0)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_48_8F5D end

    def Function_49_8FCF(): pass

    label("Function_49_8FCF")

    WaitChrThread(0x1B, 3)
    Sleep(2000)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8FE3():
        OP_95(0xFE, 10300, 0, 13800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FE3)

    def lambda_8FFD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8FFD)
    WaitChrThread(0xFE, 1)

    def lambda_9012():
        OP_95(0xFE, 8900, 0, 10100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9012)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_49_8FCF end

    def Function_50_9041(): pass

    label("Function_50_9041")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)
    Return()

    # Function_50_9041 end

    def Function_51_905D(): pass

    label("Function_51_905D")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)
    Return()

    # Function_51_905D end

    def Function_52_9079(): pass

    label("Function_52_9079")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)
    Return()

    # Function_52_9079 end

    def Function_53_9095(): pass

    label("Function_53_9095")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)
    Return()

    # Function_53_9095 end

    def Function_54_90B1(): pass

    label("Function_54_90B1")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -270, 800, 22820, 180)
    EventEnd(0x4)
    Return()

    # Function_54_90B1 end

    def Function_55_90CD(): pass

    label("Function_55_90CD")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -21330, 0, 6200, 135)
    EventEnd(0x4)
    Return()

    # Function_55_90CD end

    def Function_56_90E9(): pass

    label("Function_56_90E9")

    EventBegin(0x1)
    Call(0, 59)
    Sleep(50)
    SetChrPos(0x0, 14920, 0, 5200, 270)
    EventEnd(0x4)
    Return()

    # Function_56_90E9 end

    def Function_57_9105(): pass

    label("Function_57_9105")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -8420, -4200, -21200, 270)
    EventEnd(0x4)
    Return()

    # Function_57_9105 end

    def Function_58_9121(): pass

    label("Function_58_9121")


    #C0184
    ChrTalk(
        0x101,
        (
            "#0000Fもう日が暮れたな……\x02\x03",

            "キーアも待ってる事だし\x01",
            "寄り道せずに帰ろう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91B4")

    #C0185
    ChrTalk(
        0x102,
        (
            "#0100Fそうね、一通り\x01",
            "仕事も終わった事だし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9236")

    label("loc_91B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91F1")

    #C0186
    ChrTalk(
        0x103,
        "#0200Fそうですね、そうしましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9236")

    label("loc_91F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9236")

    #C0187
    ChrTalk(
        0x104,
        (
            "#0300Fだな、とっとと帰って\x01",
            "キー坊の顔を拝むか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9236")

    Return()

    # Function_58_9121 end

    def Function_59_9237(): pass

    label("Function_59_9237")


    #C0188
    ChrTalk(
        0x101,
        (
            "#0000Fオーバルストアは\x01",
            "そろそろ閉店時間みたいだな。\x02\x03",

            "キーアも待ってる事だし\x01",
            "寄り道せずに帰ろう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92E3")

    #C0189
    ChrTalk(
        0x102,
        (
            "#0100Fそうね、一通り\x01",
            "仕事も終わった事だし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9365")

    label("loc_92E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9320")

    #C0190
    ChrTalk(
        0x103,
        "#0200Fそうですね、そうしましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9365")

    label("loc_9320")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9365")

    #C0191
    ChrTalk(
        0x104,
        (
            "#0300Fだな、とっとと帰って\x01",
            "キー坊の顔を拝むか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9365")

    Return()

    # Function_59_9237 end

    SaveToFile()

Try(main)
