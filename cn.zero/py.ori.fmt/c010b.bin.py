from ZeroScenarioHelper import *

def main():
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
        "吉娜",                   # 1
        "昆提老人",               # 2
        "普鲁娜",                 # 3
        "利娜莉",                 # 4
        "哈斯",                   # 5
        "柯贝",                   # 6
        "赛尔盖科长",             # 7
        "隆",                     # 8
        "亨利",                   # 9
        "艾莉",                   # 10
        "蔡特",                   # 11
        "警备队员",               # 12
        "警备队员",               # 13
        "警备队员",               # 14
        "警备队员",               # 15
        "警备队员",               # 16
        "警备队员",               # 17
        "警备队员",               # 18
        "警备队员",               # 19
        "车１",                   # 20
        "车２",                   # 21
        "事件用ＮＰＣ",           # 22
        "事件用ＮＰＣ",           # 23
        "事件用ＮＰＣ",           # 24
        "事件用ＮＰＣ",           # 25
        "事件用ＮＰＣ",           # 26
        "SE控制",                 # 27
        "中央广场",               # 28
        "西街",                   # 29
        "行政区",                 # 30
        "住宅街",                 # 31
        "欢乐街",                 # 32
        "东街",                   # 33
        "旧城区",                 # 34
        "港湾区",                 # 35
        "ＩＢＣ",                 # 36
        "站前街道",               # 37
        "后巷",                   # 38
        "乌尔斯拉间道",           # 39
        "东克洛斯贝尔街道",       # 40
        "西克洛斯贝尔街道",       # 41
        "玛因兹山道",             # 42
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
        "Function_0_8D8",          # 00, 0
        "Function_1_990",          # 01, 1
        "Function_2_9DD",          # 02, 2
        "Function_3_A08",          # 03, 3
        "Function_4_A24",          # 04, 4
        "Function_5_11E1",         # 05, 5
        "Function_6_1273",         # 06, 6
        "Function_7_12D8",         # 07, 7
        "Function_8_142C",         # 08, 8
        "Function_9_1482",         # 09, 9
        "Function_10_14E3",        # 0A, 10
        "Function_11_153E",        # 0B, 11
        "Function_12_15C8",        # 0C, 12
        "Function_13_1702",        # 0D, 13
        "Function_14_1AEB",        # 0E, 14
        "Function_15_2372",        # 0F, 15
        "Function_16_23BE",        # 10, 16
        "Function_17_2495",        # 11, 17
        "Function_18_3209",        # 12, 18
        "Function_19_324D",        # 13, 19
        "Function_20_3294",        # 14, 20
        "Function_21_32DB",        # 15, 21
        "Function_22_35DB",        # 16, 22
        "Function_23_6474",        # 17, 23
        "Function_24_67EE",        # 18, 24
        "Function_25_68E2",        # 19, 25
        "Function_26_6C36",        # 1A, 26
        "Function_27_6C6D",        # 1B, 27
        "Function_28_756C",        # 1C, 28
        "Function_29_75B6",        # 1D, 29
        "Function_30_7603",        # 1E, 30
        "Function_31_7650",        # 1F, 31
        "Function_32_769D",        # 20, 32
        "Function_33_76EE",        # 21, 33
        "Function_34_7765",        # 22, 34
        "Function_35_78F6",        # 23, 35
        "Function_36_7910",        # 24, 36
        "Function_37_8507",        # 25, 37
        "Function_38_8565",        # 26, 38
        "Function_39_858B",        # 27, 39
        "Function_40_85CA",        # 28, 40
        "Function_41_8614",        # 29, 41
        "Function_42_865E",        # 2A, 42
        "Function_43_86A4",        # 2B, 43
        "Function_44_86EA",        # 2C, 44
        "Function_45_876A",        # 2D, 45
        "Function_46_87E7",        # 2E, 46
        "Function_47_881F",        # 2F, 47
        "Function_48_8857",        # 30, 48
        "Function_49_88C9",        # 31, 49
        "Function_50_893B",        # 32, 50
        "Function_51_8957",        # 33, 51
        "Function_52_8973",        # 34, 52
        "Function_53_898F",        # 35, 53
        "Function_54_89AB",        # 36, 54
        "Function_55_89C7",        # 37, 55
        "Function_56_89E3",        # 38, 56
        "Function_57_89FF",        # 39, 57
        "Function_58_8A1B",        # 3A, 58
        "Function_59_8B1F",        # 3B, 59
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
            "糟糕了～！\x01",
            "天色都这么暗了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "明明是出来买晚饭的食材的～……\x01",
            "呜呜，这下绝对要挨骂了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1273 end

    def Function_7_12D8(): pass

    label("Function_7_12D8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_136C")
    Jump("loc_13B6")

    label("loc_136C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_138C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13B6")

    label("loc_138C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13AC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13B6")

    label("loc_13AC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13B6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0003
    ChrTalk(
        0xFE,
        "哦哦……不知不觉都这么晚了啊。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "最近不太安宁，\x01",
            "还是赶快回家吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_12D8 end

    def Function_8_142C(): pass

    label("Function_8_142C")

    TalkBegin(0xFE)

    #C0005
    ChrTalk(
        0xFE,
        (
            "果然，想变瘦的话，\x01",
            "还是需要适度的运动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "你啊，明天开始坚持跑步吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_142C end

    def Function_9_1482(): pass

    label("Function_9_1482")

    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        (
            "哎～……\x01",
            "让我一个人跑步？才不要呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "我说，陪我一起跑啦～\x01",
            "那样我才能坚持下去嘛。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_1482 end

    def Function_10_14E3(): pass

    label("Function_10_14E3")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        (
            "嘿哟……\x01",
            "差不多该收摊了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "啊，你们想要的话，\x01",
            "可以把剩下的气球都拿走哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_14E3 end

    def Function_11_153E(): pass

    label("Function_11_153E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B3")
    Sound(823, 0, 100, 0)

    #C0011
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……好像\x01",
            "十分惬意嘛。\x02\x03",

            "看这样子，果然是很早之前\x01",
            "就在这栋楼里安家落户了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 6)
    Jump("loc_15C4")

    label("loc_15B3")


    #N0012
    NpcTalk(
        0xFE,
        "黑猫",
        "喵哦？\x02",
    )

    CloseMessageWindow()

    label("loc_15C4")

    TalkEnd(0xFE)
    Return()

    # Function_11_153E end

    def Function_12_15C8(): pass

    label("Function_12_15C8")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0013
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

    #A0014
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

    # Function_12_15C8 end

    def Function_13_1702(): pass

    label("Function_13_1702")

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

    def lambda_17C4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17C4)

    def lambda_17DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17DE)
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x7)
    Sleep(300)

    #C0015
    ChrTalk(
        0x101,
        "#0003F#5P呼……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0016
    ChrTalk(
        0x101,
        "#0002F#5P哈哈，好棒的夜景啊……\x02",
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
            "#0002F#5P克洛斯贝尔到底是大都市啊。\x01",
            "虽然叔叔家所在的城市\x01",
            "也绝不算小……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    #C0018
    ChrTalk(
        0x101,
        "#0008F#5P……我还是回来了啊。\x02",
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
        "#0005F#5P咦……？\x02",
    )

    CloseMessageWindow()
    OP_68(-26650, 3900, -20900, 2000)
    OP_93(0x101, 0x10E, 0x1F4)
    OP_6F(0x1)

    #C0020
    ChrTalk(
        0x101,
        (
            "#0005F#11P怎么，是猫啊……\x02\x03",

            "#0000F出现在这栋楼里……\x01",
            "也就是说，在支援科\x01",
            "入驻之前就在这里安家了吗？\x02\x03",

            "#0012F哈哈……抱歉，打扰你啦。\x01",
            "我再待一会就回去了。\x02",
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

    # Function_13_1702 end

    def Function_14_1AEB(): pass

    label("Function_14_1AEB")

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

    def lambda_1D98():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1D98)

    def lambda_1DB2():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1DB2)

    def lambda_1DCC():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_1DCC)
    Sound(458, 0, 100, 0)

    def lambda_1DED():
        OP_96(0xFE, 0x4E20, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1DED)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x22, 1, 0, 15)
    FadeToBright(2000, 0)
    Sleep(4400)

    def lambda_1E36():
        OP_95(0xFE, -22000, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E36)
    Sleep(200)

    def lambda_1E53():
        OP_95(0xFE, -21900, -8200, -25600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E53)
    Sleep(200)

    def lambda_1E70():
        OP_95(0xFE, -22000, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E70)
    Sleep(200)

    def lambda_1E8D():
        OP_95(0xFE, -21900, -8200, -25600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E8D)
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

    def lambda_1F54():
        OP_95(0xFE, -28400, -8200, -25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F54)
    WaitChrThread(0x102, 1)

    def lambda_1F72():
        OP_95(0xFE, -28500, -8200, -26100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F72)
    WaitChrThread(0x103, 1)

    def lambda_1F90():
        OP_95(0xFE, -26700, -8200, -25200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F90)
    WaitChrThread(0x104, 1)

    def lambda_1FAE():
        OP_95(0xFE, -26800, -8200, -26300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1FAE)
    WaitChrThread(0x101, 1)

    def lambda_1FCC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FCC)
    WaitChrThread(0x103, 1)

    def lambda_1FDD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1FDD)
    WaitChrThread(0x102, 1)

    def lambda_1FEE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1FEE)
    WaitChrThread(0x104, 1)

    def lambda_1FFF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1FFF)
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
            "#12P#0005F这里……\x01",
            "不是那栋杂居公寓吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#12P#0306F什么啊，\x01",
            "好破旧的建筑物啊。\x02\x03",

            "#0301F和那边的百货店相比，\x01",
            "显得好陈旧啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0206F#11P已建三十年……\x01",
            "临近拆除的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#12P#0108F……这里真的是\x01",
            "『特别任务支援科』的部门楼吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#12P#0001F嗯，是啊。\x01",
            "我想应该没错……\x02",
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
        "男性的声音",
        "#2P哦，来得真迟啊。\x02",
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

    def lambda_2204():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2204)

    def lambda_2215():
        OP_95(0xFE, -28500, -8200, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2215)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xE, 1)

    #C0027
    ChrTalk(
        0x101,
        "#12P#0005F赛尔盖科长……\x02",
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
            "快进来吧。\x02\x03",

            "我们『特别任务支援科』\x01",
            "是一个怎样的部门……\x02\x03",

            "你们的所有疑问，\x01",
            "我都会好好解答的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_93(0xE, 0x0, 0x1F4)

    def lambda_2317():
        OP_95(0xFE, -28500, -8200, -20500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2317)
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(1000)

    def lambda_2347():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2347)
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

    # Function_14_1AEB end

    def Function_15_2372(): pass

    label("Function_15_2372")

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

    # Function_15_2372 end

    def Function_16_23BE(): pass

    label("Function_16_23BE")

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

    # Function_16_23BE end

    def Function_17_2495(): pass

    label("Function_17_2495")

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

    def lambda_25B8():
        OP_95(0xFE, -28800, -8200, -27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25B8)
    SetCameraDistance(15500, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267B")

    #C0029
    ChrTalk(
        0x101,
        (
            "#5P#0004F呼……\x01",
            "好舒服的风啊。\x02\x03",

            "#0002F话说回来，\x01",
            "克洛斯贝尔还真是\x01",
            "很有大都市的感觉啊……\x02\x03",

            "虽然叔叔家所在的城市\x01",
            "也绝不算小……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_269F")

    label("loc_267B")


    #C0030
    ChrTalk(
        0x101,
        (
            "#5P#0002F呼……\x01",
            "好舒服的风啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_269F")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_26B9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26B9)
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
            "#0005F『贝尔海姆』……\x01",
            "是吗，从这里能看到啊。\x02",
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
            "#0004F哈哈……现在应该\x01",
            "已经有其他人入住了吧。\x02\x03",

            "#0000F但塞茜尔姐姐的家\x01",
            "应该还在老地方……\x02\x03",

            "#0005F对了，稍后还得去\x01",
            "跟她的父母打声招呼才行……\x02",
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
            "#11P#0003F#30W（从那时起，已经过去了三年……）\x02\x03",

            "（我在叔叔家寄住了一段时间之后，\x01",
            "  进入警察学校……）\x02\x03",

            "（不顾一切地努力学习和训练，\x01",
            "  终于取得了搜查官的资格……）\x02\x03",

            "#0008F（可结果，我……）\x02\x03",

            "（我……当上搜查官，\x01",
            "  究竟是想干什么呢……？）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xF, -14000, -4200, -17500, 225)
    SetChrFlags(0xF, 0x8)
    ClearChrFlags(0xF, 0x80)

    #N0034
    NpcTalk(
        0xF,
        "男孩子的声音",
        "#2S喂～！\x02",
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

    def lambda_2A16():
        OP_96(0xFE, 0xFFFF923C, 0xFFFFDFF8, 0xFFFF99A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A16)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)

    #C0035
    ChrTalk(
        0x101,
        "#6P#0005F你们是……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xF,
        "#2P哎呀～让我们好找。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xF,
        (
            "#2P先是去了警察局，\x01",
            "可他们说大哥哥你们\x01",
            "不在那里嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x10,
        (
            "#11P然后就把这个地址\x01",
            "告诉我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x10,
        (
            "#11P那个，这里是叫\x01",
            "支援科没错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#6P#0000F啊，没错。\x02\x03",

            "为什么要特地找来……？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xF,
        "#2P那、那个……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xF,
        (
            "#2P就是，突然想起来，\x01",
            "好像还没有好好谢过你们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x10,
        (
            "#11P要是没有大哥哥你们在，\x01",
            "我们两个大概\x01",
            "就都要受重伤了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x10,
        (
            "#11P所以，那个……\x01",
            "想再来向你们道个谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#6P#0002F……是吗………\x02\x03",

            "谢谢你们了。\x01",
            "这么晚了，还特地找过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xF,
        (
            "#2P虽、虽然说，\x01",
            "你们和亚里欧斯先生比起来\x01",
            "还很不可靠……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xF,
        (
            "#2P不过，作为巡逻的警察来说，\x01",
            "表现还是可圈可点的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xF,
        (
            "#2P就算能力不足也没关系，\x01",
            "只要从现在开始努力不就好了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0xE1, 0x1F4)
    OP_63(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0050
    ChrTalk(
        0x10,
        "#5P喂喂，隆。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x10,
        (
            "#5P明明是来道谢的，\x01",
            "你的态度怎么还这么嚣张啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#6P#0009F哈哈……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0053
    ChrTalk(
        0x101,
        (
            "#6P#0004F──你说得对呢。\x01",
            "从现在开始努力磨练自己就好啦。\x02\x03",

            "#0000F对了，你们两个\x01",
            "住在哪里？\x02\x03",

            "要不然，我送你们回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xF,
        (
            "#2P啊，没事～没事～\x01",
            "我就住在西街，很近的啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x10E, 0x1F4)

    #C0055
    ChrTalk(
        0x10,
        (
            "#11P嗯，我住在住宅街那边，\x01",
            "不过也没关系的。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x10,
        (
            "#11P那个，也请代我们\x01",
            "向其余的哥哥姐姐问个好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#6P#0002F嗯，我会的。\x02\x03",

            "你们两个回去时也要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xF,
        "#2P嗯！\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x10,
        "#11P那么，再见啦！\x02",
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

    def lambda_2F91():
        OP_95(0xFE, -28800, -8200, -27000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F91)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    #C0060
    ChrTalk(
        0x101,
        (
            "#5P#0012F哈哈……我也真够单纯啊。\x02\x03",

            "#0002F只是这样的一句道谢，\x01",
            "心情就马上云开雾散了……\x02\x03",

            "#0004F关键还是要看\x01",
            "自己的心态吗……\x02",
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
            "#30W──听好了，罗伊德。\x02\x03",

            "身为男子汉，面对眼前的任何事物，\x01",
            "都要勇往直前地撞上去试试。\x02\x03",

            "要用你自己的心，去抓住\x01",
            "只属于你的真相。\x02\x03",

            "这样的话，你应该\x01",
            "就能找到自己的目标了。\x07\x00\x02",
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

            "……嗯，也是啊。\x02",
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
            "#12P#0000F不先撞上去试试的话，\x01",
            "便无法弄清任何东西吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetCameraDistance(17000, 2000)

    def lambda_31CF():
        OP_95(0xFE, -28800, -8200, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31CF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    OP_CA(0x1, 0xFF, 0x0)
    SetMapFlags(0x10000000)
    SetScenarioFlags(0x5C, 2)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2495 end

    def Function_18_3209(): pass

    label("Function_18_3209")


    def lambda_320E():
        OP_95(0xFE, -21500, -8200, -24000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_320E)
    WaitChrThread(0xF, 1)
    OP_93(0xF, 0x10E, 0x0)

    def lambda_3233():
        OP_96(0xFE, 0xFFFF9A70, 0xFFFFDFF8, 0xFFFF987C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3233)
    WaitChrThread(0xF, 1)
    Return()

    # Function_18_3209 end

    def Function_19_324D(): pass

    label("Function_19_324D")

    Sleep(300)

    def lambda_3255():
        OP_95(0xFE, -21500, -8200, -24000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3255)
    WaitChrThread(0x10, 1)
    OP_93(0x10, 0x10E, 0x0)

    def lambda_327A():
        OP_96(0xFE, 0xFFFF9C64, 0xFFFFDFF8, 0xFFFF9C64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_327A)
    WaitChrThread(0x10, 1)
    Return()

    # Function_19_324D end

    def Function_20_3294(): pass

    label("Function_20_3294")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)

    def lambda_32A3():
        OP_96(0xFE, 0xFFFFAC04, 0xFFFFDFF8, 0xFFFFA240, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32A3)
    WaitChrThread(0xFE, 1)

    def lambda_32C1():
        OP_95(0xFE, -14000, -4200, -17500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32C1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_3294 end

    def Function_21_32DB(): pass

    label("Function_21_32DB")

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

    def lambda_351E():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_351E)

    def lambda_3538():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3538)

    def lambda_3552():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3552)
    Sound(457, 0, 100, 0)

    def lambda_3573():
        OP_96(0xFE, 0x4E20, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3573)
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

    # Function_21_32DB end

    def Function_22_35DB(): pass

    label("Function_22_35DB")

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

    def lambda_3712():
        OP_96(0xFE, 0xFFFF8F80, 0x514, 0xFFFFBADC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3712)

    def lambda_372C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_372C)
    WaitChrThread(0x101, 1)
    OP_71(0x7, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_93(0x101, 0x5A, 0x1F4)

    #C0064
    ChrTalk(
        0x101,
        "#6P#0005F（…………啊……………）\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(1178, 255, 90, 0)    #voice#Elie

    #C0065
    ChrTalk(
        0x11,
        "#5P#30W罗伊德……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x1388)
    ReplaceBGM("ed7513", "ed7000")
    OP_68(-22610, 2300, -17660, 2000)

    def lambda_37EB():
        OP_96(0xFE, 0xFFFF9B38, 0x514, 0xFFFFBADC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37EB)
    WaitChrThread(0x101, 1)
    Sleep(500)

    #C0066
    ChrTalk(
        0x101,
        (
            "#3P#0000F嗯……\x01",
            "你怎么知道是我？\x02",
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
            "#30W大概就是，直觉吧……\x02\x03",

            "#30W不知为何，\x01",
            "就是隐隐约约感觉\x01",
            "你应该会来。\x02",
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
        "#6P#0004F是吗……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_3914():

        label("loc_3914")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3914")

    QueueWorkItem2(0x11, 2, lambda_3914)

    def lambda_3926():
        OP_96(0xFE, 0xFFFFAAD8, 0x514, 0xFFFFB5C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3926)
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

    def lambda_39A5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_39A5)
    OP_0D()
    Sleep(1000)

    #A0069
    AnonymousTalk(
        0x101,
        (
            "#0002F真美啊……\x02\x03",

            "那边那座能望得到的建筑……\x01",
            "是ＩＢＣ大厦吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0070
    AnonymousTalk(
        0x11,
        (
            "#0104F#30W就算找遍整个大陆，\x01",
            "大概也找不到比这座城市\x01",
            "更美的夜景了吧。\x02\x03",

            "#0108F可是……\x01",
            "城市的灯光越明亮，\x01",
            "星光就会变得越暗淡……\x02\x03",

            "女神慈爱的证明，那纯净的星光都……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_3AA7():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AA7)

    #A0071
    AnonymousTalk(
        0x101,
        "#0001F……艾莉……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0072
    AnonymousTalk(
        0x11,
        (
            "#0106F#30W白天的事……\x01",
            "你还记得吧？\x02\x03",

            "#0108F鲁巴彻，黑月，\x01",
            "还有达德利搜查官所说的话。\x02",
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
            "──无论你们怎么努力，\x01",
            "都无法改变这座城市的现状……\x02\x03",

            "更别想把我们给怎么样了，\x01",
            "那是完全不可能的。\x02",
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
            "呵呵，我所说的也只是\x01",
            "『商业』方面的竞争而已啦。\x02\x03",

            "在克洛斯贝尔这个地方，\x01",
            "自由竞争可是受法律保护的……\x02\x03",

            "难道有什么问题吗？\x02",
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
            "在这座正义难以得到彻底伸张的城市中，\x01",
            "我们至少要将基本秩序维持住……\x02\x03",

            "遏止杀人一类的重大犯罪，\x01",
            "与犯罪组织和国外的间谍机关对抗，\x01",
            "保障市民与社会的安全……\x02\x03",

            "我们的艰辛，你们理解得了吗？\x02",
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
            "#5P#0103F那些，都是这座城市的阴暗面……\x01",
            "也是克洛斯贝尔这个自治州的真实写照。\x02\x03",

            "#0108F在帝国与共和国的夹缝中力求生存，\x01",
            "尊严尽失，充满谎言与欺骗……\x02\x03",

            "依靠从外国聚集而来的财富，\x01",
            "沉溺于一时的繁荣与享乐……\x02\x03",

            "#0106F每个人都认为这是无可奈何的问题，因而放弃面对，\x01",
            "被每日的繁忙压得喘不过气……\x02\x03",

            "#0101F我们就是生活在这样的城市中。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#12P#0003F是吗……\x02\x03",

            "#0000F艾莉你……\x01",
            "不想放弃吧？\x02",
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

            "#0103F……我本来是有父母的。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x11,
        (
            "#5P#0102F呵呵，我这种说法，\x01",
            "就好像他们已经去世了一样。\x02\x03",

            "其实两人都还健在呢。\x02\x03",

            "#0104F只不过离了婚，\x01",
            "分别住在帝国和共和国。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        "#12P#0003F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x11,
        (
            "#5P#0100F父亲本来是共和国的人。\x02\x03",

            "来到这座城市后，与母亲相遇……\x02\x03",

            "入赘到麦克道尔家以后，\x01",
            "就立志踏上了政治家的道路。\x02\x03",

            "#0103F然后，在他当上了议员之后，\x01",
            "便立刻察觉到了这座城市的扭曲现状。\x02\x03",

            "他是个正义感很强的人，\x01",
            "所以很想改变些什么吧。\x02\x03",

            "于是历经数年，锲而不舍，\x01",
            "提出了各种各样的改革方案。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        "#12P#0002F……真厉害啊。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x11,
        (
            "#5P#0101F不……\x01",
            "最终，父亲的改革方案都被否决了。\x02\x03",

            "#0103F帝国派和共和国派……\x01",
            "两边都排斥他。\x02",
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
            "#5P#0108F曾经相互信任的同伴们也都背叛了他，\x01",
            "失去了朋友，还被政敌冷嘲热讽……\x02\x03",

            "外公也由于身处克洛斯贝尔市长\x01",
            "这个中立的立场上，无法帮助父亲……\x02\x03",

            "#0106F父亲他……便对克洛斯贝尔这座城市\x01",
            "彻底绝望了。\x02\x03",

            "于是，他辞去了议员职位，告别了妻女，\x01",
            "选择了回归卡尔瓦德的道路……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#12P#0013F啊……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x11,
        (
            "#5P#0108F母亲无法阻止父亲……\x02\x03",

            "然而，也不能带着幼小的我，\x01",
            "跟随父亲而去……\x02\x03",

            "#0103F于是，达成了离婚协议……\x01",
            "父亲就这样走掉了。\x02\x03",

            "#0102F母亲虽然也恨过父亲……\x01",
            "但应该还是爱着他吧。\x02\x03",

            "住在失去了丈夫的克洛斯贝尔，\x01",
            "令她感到万分痛苦……\x01",
            "于是就去投奔帝国的亲戚。\x02\x03",

            "#0104F而我……\x01",
            "就被外公收养了。\x02",
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
            "#5P#0102F……我决心走上政治之路，\x01",
            "也是从那时开始的。\x02\x03",

            "倒不是为了\x01",
            "给父亲报仇什么的。\x02\x03",

            "#0104F我只是，无法接受。\x02\x03",

            "原本那样幸福的家庭，\x01",
            "怎么会说散就散了呢。\x02",
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
            "#5P#0103F在外公的帮助下……\x01",
            "我一边到各地留学，\x01",
            "一边学习政治、经济。\x02\x03",

            "#0108F可是，学得越多，\x01",
            "我就越能体会到克洛斯贝尔\x01",
            "所处的境况是多么复杂难解。\x02\x03",

            "结果，在帝国和共和国……\x02\x03",

            "这两个大国的重压之下，\x01",
            "正义与各种利害关系纠缠不清，\x01",
            "就无可避免地产生了扭曲。\x02\x03",

            "#0103F我撞上了『壁障』。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        "#6P#0001F……『壁障』吗？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x11,
        (
            "#5P#0108F嗯……父亲也是一样，\x01",
            "或许，外公也感觉到了这面『壁障』。\x02\x03",

            "#0100F我说，罗伊德。\x01",
            "克洛斯贝尔自治州的政府代表，\x01",
            "你知道是谁吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#6P#0005F这个……\x01",
            "不是麦克道尔市长吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x11,
        (
            "#5P#0104F不，正确地说，\x01",
            "是『克洛斯贝尔市市长』\x01",
            "和『自治州议会议长』两个人。\x02\x03",

            "也就是说，如今，我外公\x01",
            "与帝国派的哈尔特曼议长两个人\x01",
            "就是克洛斯贝尔政府的共同代表。\x02\x03",

            "这是由自治州法所规定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#6P#0006F是吗，我孤陋寡闻了……\x02\x03",

            "#0005F可是，为什么\x01",
            "要采取这种繁琐的体制呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x11,
        (
            "#5P#0103F这还用说吗。\x02\x03",

            "#0101F──因为，只要有两个同级别的代表，\x01",
            "就很难发动政治改革了。\x02",
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
            "#6P#0011F怎么会……！\x02\x03",

            "#0008F……不，可是……\x01",
            "仔细一想，好像确实是这样……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x11,
        (
            "#5P#0106F嗯，在两个人同时位于顶层的情况下，\x01",
            "无论哪一方试图发起改革，\x01",
            "另一方必然会进行牵制……\x02\x03",

            "从政治力学上来说，\x01",
            "这种体制已经是历史的必然了。\x02\x03",

            "#0108F七十年前……\x01",
            "在帝国和共和国双方的认可下，\x01",
            "克洛斯贝尔自治州成立了……\x02\x03",

            "当时，制定自治州法的\x01",
            "似乎是两国的法律专家……\x02\x03",

            "#0103F如今想来，那简直就是『诅咒』呢。\x02",
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
            "#5P#0108F我……已经走进了死胡同。\x02\x03",

            "如果就这样踏入政界，\x01",
            "必然会被这诅咒所侵蚀……\x02\x03",

            "#0103F所以，我想选择与父亲以及外公\x01",
            "都不同的另一道突破口。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#6P#0000F那就是……警察吗？\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x11,
        (
            "#5P#0104F嗯，在警界可以从有别于政治的视角\x01",
            "来观察各种扭曲的现象。\x02\x03",

            "我认为，在这里积累的经验，总有一天\x01",
            "会成为踏入政界时的武器。\x02\x03",

            "#0108F父亲失败了，外公也未能实行的\x01",
            "克洛斯贝尔改革……\x02\x03",

            "#0100F我想，在这里得到的经验，\x01",
            "以后说不定能成为实现它的关键。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#6P#0000F是吗……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x11,
        (
            "#5P#0108F……可是，或许这依然\x01",
            "只是一种逃避。\x02\x03",

            "#0106F今天所遇到的事，\x01",
            "其实全部都在预料之中……\x02\x03",

            "可是却又超乎预想地沉重和冰冷。\x02\x03",

            "面对这样的事态……\x01",
            "我又陷入了走投无路的境地。\x02\x03",

            "#0108F说到底……凭我自己一个人，\x01",
            "或许什么也做不到。\x02\x03",

            "也许我仍然只是个被父母遗弃……\x01",
            "毫无成长的年幼少女吧。\x02",
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
        "#6P#0004F──这样也没什么不好吧。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x11,
        "#0105F#5P……哎…………\x02",
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
            "#12P#0000F艾莉你啊，就是太过完美了。\x02\x03",

            "什么事情都想靠自己来完成，\x01",
            "一次失败也不能忍受……\x02\x03",

            "你是不是这么想的？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x11,
        "#0101F#5P#40W没……没有啊……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#12P#0006F……今天确实是遇到了许多\x01",
            "令人沮丧的事情。\x02\x03",

            "#0001F不过，像这样的事情，\x01",
            "只要工作，就一定会碰到的。\x02\x03",

            "#0000F况且……\x01",
            "今天无法逾越的『壁障』，\x01",
            "说不定明天就能越过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x11,
        "#0105F#5P『壁障』……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#12P#0003F在如今的状况下，我们眼前的『壁障』\x01",
            "就是恐吓信事件。\x02\x03",

            "#0008F这个使一科出动，逐渐脱离了\x01",
            "我们掌握的事件……\x02\x03",

            "#0001F如果可能的话，我想和一科\x01",
            "采取不同的行动，尝试独立调查。\x02",
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
            "#0101F#5P哎……！？\x02\x03",

            "#0108F可、可是，我们接下来\x01",
            "还能做些什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#12P#0003F一科也许确实有他们的\x01",
            "独到之处，非常了不起……\x02\x03",

            "但他们却只能依照警察的理论来行动，\x01",
            "这一点，我想是不会错的。\x02\x03",

            "#0008F所以，说不定我们还可以从其它的\x01",
            "突破口来追查事件……\x02\x03",

            "#0000F我总有这种感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x11,
        "#0105F#5P罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#12P#0004F对了，这和艾莉刚才\x01",
            "说的那些不是一回事吗？\x02\x03",

            "#0000F如果我们能抢在一科之前，\x01",
            "爆冷立个大功……\x02\x03",

            "那么，这就说明艾莉的目标并非\x01",
            "完全不可能实现，不是吗？\x02",
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
            "#12P#0008F当然了，这次的事件\x01",
            "或许无法和整个克洛斯贝尔的\x01",
            "大问题相提并论。\x02\x03",

            "#0003F可是……我们最需要的\x01",
            "是跨越『壁障』的力量。\x02\x03",

            "#0000F只要一步一步地\x01",
            "跨越这种小『壁障』……\x02\x03",

            "说不定，我们有朝一日\x01",
            "就能获得跨越巨大『壁障』的\x01",
            "力量了，不是吗？\x02",
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
            "#0106F#5P──这两个月以来，\x01",
            "我们朝夕相处，我多少也能察觉到。\x02\x03",

            "你也一直怀着\x01",
            "和我不一样的烦恼。\x02\x03",

            "#0108F可是……你为什么\x01",
            "还能如此乐观呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#12P#0005F……我吗，该怎么说呢……\x02\x03",

            "#0000F或许是因为有一个视为目标的人，\x01",
            "所以才能一直坚持前进吧。\x02\x03",

            "#0012F不过，这种方法……\x01",
            "说不定也是个问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x11,
        (
            "#0104F#5P是吗……\x02\x03",

            "#0108F……但是我……\x01",
            "好像没有你那么坚强呢。\x02\x03",

            "我有点……累了……\x02",
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
            "#0106F#5P#30W……本来没打算\x01",
            "提起往事的……\x02\x03",

            "可是……不知怎么回事，\x01",
            "总觉得实在无法忍耐了……\x02\x03",

            "#0108F#40W再这样下去的话，\x01",
            "说不定我真的会拖你们的后腿……\x02\x03",

            "那样的话，还不如……干脆……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#12P#0004F──艾莉。\x02",
    )

    CloseMessageWindow()

    def lambda_55E7():
        OP_96(0xFE, 0xFFFFAAD8, 0x514, 0xFFFFB7BC, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55E7)
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

    def lambda_5674():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5674)
    WaitChrThread(0x11, 2)
    Sleep(500)

    #C0127
    ChrTalk(
        0x11,
        "#0105F#5P#40W……啊…………\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#12P#0001F我……\x01",
            "我们都需要艾莉。\x02\x03",

            "你的射击本领、交涉能力、\x01",
            "政治经济方面的知识与平衡感……\x02\x03",

            "要解决这个城市中发生的问题，\x01",
            "你的每一样能力都是不可或缺的。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x11,
        "#0108F#5P#40W……但、但是………\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#12P#0004F不……不对。\x02\x03",

            "虽然这些也都是实话，\x01",
            "但更重要的是……\x02\x03",

            "#0002F只要有艾莉在身边，\x01",
            "我就会感到很开心。\x02",
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
        "#0112F#5P#40W哎……\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#12P#0004F我们几人本来毫无共性，像是一盘散沙，\x01",
            "但经过这两个月的相处，也逐渐变得默契合拍了。\x02\x03",

            "虽然每天都忙得不可开交，\x01",
            "但还商量好了轮流做饭的次序……\x02\x03",

            "#0000F还有，对于各自所擅长的领域，\x01",
            "什么也不用说，就能相互信赖。\x02\x03",

            "能有这样的伙伴，\x01",
            "本身不就是很值得开心的事情吗？\x02",
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
        "#0102F#5P#30W………啊………………\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#12P#0006F……我们毕竟是年轻人。\x02\x03",

            "把世界看得太简单，\x01",
            "或是对其绝望，都还为时过早。\x02\x03",

            "#0008F应该竭尽全力，做好力所能及的事情，\x01",
            "即使历经失败，也要永不放弃地继续挑战……\x02\x03",

            "#0002F如果这样还是不行的话……\x01",
            "到时大家再一起想办法就是了。\x02\x03",

            "我自不必说，兰迪和缇欧\x01",
            "也一定会帮忙的。\x02\x03",

            "别看科长平时那副样子，\x01",
            "其实也默默帮我们打通了不少门路……\x02\x03",

            "而且还有蔡特这个\x01",
            "奇怪的帮手主动找上门呢。\x02\x03",

            "#0009F艾莉──你并不是孤单一人。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x11,
        (
            "#0112F#30W#5P…………………………………\x02\x03",

            "#0104F#30W……呵呵………\x02",
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
            "#0104F#5P#30W并不是孤单一人吗……\x02\x03",

            "……说得对。\x02\x03",

            "这么理所当然的事情……\x01",
            "我刚才也许都忘了呢。\x02",
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
            "#0102F#5P──谢谢你，罗伊德。\x02\x03",

            "虽然我自己的问题\x01",
            "并不是那么简单就能解决的……\x02\x03",

            "#0109F不过，多少也感觉\x01",
            "轻松了一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        "#12P#0002F是吗……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x11,
        (
            "#0113F#5P呼……话说回来。\x02\x03",

            "先不说你那种青春校园剧一样的台词……\x01",
            "我还真是被你吓了一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#12P#0006F呜……\x01",
            "我知道自己说话有点夸张啦。\x02\x03",

            "#0005F不过，怎么会吓一跳？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x11,
        (
            "#0113F#5P因、因为……\x02\x03",

            "……说什么需要我，\x01",
            "留在身边会很开心什么的……\x02\x03",

            "我还以为你\x01",
            "接下来肯定要表白……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
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

    def lambda_5E82():
        OP_96(0xFE, 0xFFFFAAD8, 0x514, 0xFFFFB5C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E82)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)

    #C0143
    ChrTalk(
        0x101,
        (
            "#12P#0011F不、不是啦！\x01",
            "我并不是那个意思……！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x11,
        (
            "#0101F#5P哎呀……？\x02\x03",

            "莫非你是觉得，\x01",
            "像我这种人，连表白的价值都没有吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            "#12P#0006F也、也不是这个意思……\x02\x03",

            "#0013F啊啊，真要命……\x01",
            "艾莉，你是在戏弄我吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x11,
        (
            "#0104F#5P呵呵……小小的报复啦。\x02\x03",

            "#0102F不过你啊，还是\x01",
            "稍微注意一点比较好哦。\x02\x03",

            "该说是天生性格便是如此吗……\x01",
            "有些时候，真的会给人一种处处留情的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#12P#0011F等、等一下！\x02\x03",

            "这话用来形容兰迪倒也罢了，\x01",
            "为什么会说我是……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x11,
        (
            "#0111F#5P……而且没有一点自知之明。\x01",
            "加上这一条，性质就更加恶劣了呢……\x02\x03",

            "#0113F呼……真是服了你。\x02\x03",

            "……没想到，仅因那么几句话，\x01",
            "我的心境就会有如此大的变化……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x11,
        (
            "#0101F#5P没、没什么啦。\x02\x03",

            "#0106F那个──向科长报告的工作\x01",
            "都推给你们了，真是抱歉。\x02\x03",

            "#0100F关于恐吓信的调查……\x01",
            "你有什么计划吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#12P#0006F不，现在还没有。\x02\x03",

            "#0000F不过，说到底……\x01",
            "我觉得一切都要看『银』的目的。\x02\x03",

            "我打算明天和大家商量商量，\x01",
            "看看能不能发现什么突破口。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x11,
        (
            "#0104F#5P我明白了。\x02\x03",

            "#0102F多亏了你……\x01",
            "看来今晚能好好休息一下了。\x02\x03",

            "彼此都清醒一下头脑，\x01",
            "准备明天的会议吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        "#12P#0002F嗯……！\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 2)), scpexpr(EXPR_END)), "loc_6399")
    AddCraft(0x0, 0x154)
    AddCraft(0x1, 0x154)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和艾莉习得了组合战技\x01\x07\x02",

            "『星辰爆击Ⅱ』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    #A0155
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_6430")

    label("loc_6399")

    AddCraft(0x0, 0x14A)
    AddCraft(0x1, 0x14A)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和艾莉习得了组合战技\x01\x07\x02",

            "『星辰爆击』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6430")

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

    # Function_22_35DB end

    def Function_23_6474(): pass

    label("Function_23_6474")

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

    def lambda_66B7():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_66B7)

    def lambda_66D1():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_66D1)

    def lambda_66EB():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_66EB)
    Sound(458, 0, 100, 0)

    def lambda_670C():
        OP_96(0xFE, 0x4E20, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_670C)
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

    # Function_23_6474 end

    def Function_24_67EE(): pass

    label("Function_24_67EE")

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

    # Function_24_67EE end

    def Function_25_68E2(): pass

    label("Function_25_68E2")

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
            "#1K同日，２０：４５──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7516", 0)

    def lambda_6B5D():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6B5D)

    def lambda_6B77():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6B77)

    def lambda_6B91():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_6B91)
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

    # Function_25_68E2 end

    def Function_26_6C36(): pass

    label("Function_26_6C36")

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

    # Function_26_6C36 end

    def Function_27_6C6D(): pass

    label("Function_27_6C6D")

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

    def lambda_6F33():
        OP_96(0xFE, 0xFFFFCA18, 0x0, 0xFFFFF31C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F33)
    Sleep(50)

    def lambda_6F50():
        OP_96(0xFE, 0xFFFFC9B4, 0x0, 0xFFFFEC78, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F50)
    Sleep(100)

    def lambda_6F6D():
        OP_96(0xFE, 0xFFFFC310, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6F6D)
    Sleep(50)

    def lambda_6F8A():
        OP_96(0xFE, 0xFFFFC3D8, 0x0, 0xFFFFF704, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F8A)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 3, 0, 3)

    def lambda_6FCB():
        OP_96(0xFE, 0xFFFFBCD0, 0x0, 0xFFFFF9C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6FCB)
    Sleep(100)

    def lambda_6FE8():
        OP_96(0xFE, 0xFFFFBCD0, 0x0, 0xFFFFEE08, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6FE8)
    Sleep(50)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_700D():
        OP_96(0xFE, 0xFFFFBFF0, 0x0, 0xFFFFE9BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_700D)
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

    def lambda_7132():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7132)
    Sleep(50)

    def lambda_7142():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7142)
    Sleep(50)

    def lambda_7152():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7152)
    Sleep(50)

    def lambda_7162():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7162)
    Sleep(50)

    def lambda_7172():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_7172)
    Sleep(50)

    def lambda_7182():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_7182)
    Sleep(50)

    def lambda_7192():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7192)
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
            "#5P#0010F唔……\x01",
            "该怎么办……！\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#5P#0107F要去警察局总部的话，\x01",
            "就直接去行政区……！\x02",
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
        "#6P#0207F不、不行……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(12700, 900, 27800, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)

    def lambda_72A9():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_72A9)

    def lambda_72B6():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_72B6)

    def lambda_72C3():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_72C3)

    def lambda_72D0():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_72D0)

    def lambda_72DD():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_72DD)

    def lambda_72EA():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_72EA)
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

    def lambda_73B1():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_73B1)

    def lambda_73CB():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_73CB)
    Sleep(50)

    def lambda_73E8():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_73E8)

    def lambda_7402():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7402)
    Sleep(50)

    def lambda_741F():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_741F)

    def lambda_7439():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7439)
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
        "#6P#0607F走后巷过去……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0163
    ChrTalk(
        0x101,
        "#11P#0007F是……！\x02",
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

    # Function_27_6C6D end

    def Function_28_756C(): pass

    label("Function_28_756C")

    OP_92(0x101, 0xFFFFD314, 0x2EE0, 0x1F4)

    def lambda_757E():
        OP_95(0xFE, -11500, 0, 12000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_757E)
    WaitChrThread(0x101, 1)

    def lambda_759C():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_759C)
    WaitChrThread(0x101, 1)
    Return()

    # Function_28_756C end

    def Function_29_75B6(): pass

    label("Function_29_75B6")

    Sleep(300)
    OP_92(0x104, 0xFFFFD314, 0x2EE0, 0x1F4)

    def lambda_75CB():
        OP_95(0xFE, -11500, 0, 12000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75CB)
    WaitChrThread(0x104, 1)

    def lambda_75E9():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75E9)
    WaitChrThread(0x104, 1)
    Return()

    # Function_29_75B6 end

    def Function_30_7603(): pass

    label("Function_30_7603")

    Sleep(900)
    OP_92(0x102, 0xFFFFCD9C, 0x2AF8, 0x1F4)

    def lambda_7618():
        OP_95(0xFE, -12900, 0, 11000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7618)
    WaitChrThread(0x102, 1)

    def lambda_7636():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7636)
    WaitChrThread(0x102, 1)
    Return()

    # Function_30_7603 end

    def Function_31_7650(): pass

    label("Function_31_7650")

    Sleep(1200)
    OP_92(0x103, 0xFFFFCD9C, 0x2AF8, 0x1F4)

    def lambda_7665():
        OP_95(0xFE, -12900, 0, 11000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7665)
    WaitChrThread(0x103, 1)

    def lambda_7683():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7683)
    WaitChrThread(0x103, 1)
    Return()

    # Function_31_7650 end

    def Function_32_769D(): pass

    label("Function_32_769D")

    Sleep(2500)

    def lambda_76A5():
        OP_95(0xFE, -12800, 0, 12000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_76A5)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0xB4, 0x1F4)
    Sleep(1500)
    OP_93(0x10A, 0x13B, 0x1F4)

    def lambda_76D4():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_76D4)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_32_769D end

    def Function_33_76EE(): pass

    label("Function_33_76EE")

    Sleep(2000)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_76FE():
        OP_95(0xFE, -11500, 0, 13300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_76FE)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    OP_93(0xE, 0x5A, 0x1F4)
    Sound(531, 0, 100, 0)
    Sleep(1550)
    OP_93(0xE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_7743():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7743)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    Return()

    # Function_33_76EE end

    def Function_34_7765(): pass

    label("Function_34_7765")

    Sleep(3000)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 3)
    BeginChrThread(0x22, 1, 0, 35)

    def lambda_7797():
        OP_95(0xFE, -15300, 0, 8300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7797)
    WaitChrThread(0x12, 1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x22, 0x1)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_77DB():
        OP_92(0xFE, 0xFFFFB690, 0x300C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_77DB)
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

    def lambda_783F():
        OP_9D(0xFE, 0xFFFFB690, 0x6A4, 0x300C, 0x898, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_783F)
    Sleep(600)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x2)
    WaitChrThread(0x12, 1)

    def lambda_786E():
        OP_92(0xFE, 0xFFFFB690, 0x4F4C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_786E)
    SetChrSubChip(0x12, 0x3)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_7892():
        OP_9D(0xFE, 0xFFFFB690, 0x0, 0x4F4C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7892)
    Sleep(500)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x2)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x3)
    Sleep(50)
    BeginChrThread(0x12, 0, 0, 3)
    BeginChrThread(0x22, 1, 0, 35)

    def lambda_78D4():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_78D4)
    WaitChrThread(0x12, 1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x22, 0x1)
    Return()

    # Function_34_7765 end

    def Function_35_78F6(): pass

    label("Function_35_78F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_790F")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_35_78F6")

    label("loc_790F")

    Return()

    # Function_35_78F6 end

    def Function_36_7910(): pass

    label("Function_36_7910")

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

    def lambda_7C32():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C32)
    Sleep(50)

    def lambda_7C4F():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C4F)
    Sleep(50)

    def lambda_7C6C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C6C)
    Sleep(50)

    def lambda_7C89():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7C89)
    Sleep(50)

    def lambda_7CA6():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7CA6)
    Sleep(50)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_7CCB():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7CCB)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    BeginChrThread(0x12, 0, 0, 3)

    def lambda_7CF6():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7CF6)
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
        "#5P#0006F呼、呼……\x02",
    )

    CloseMessageWindow()

    #N0165
    NpcTalk(
        0x101,
        "琪雅",
        "#6P#1105F回来了呢～\x02",
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
            "#5P#0202F不过，似乎没看到\x01",
            "警备队的人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0167
    ChrTalk(
        0x104,
        "#0302F#11P顺利甩开了吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0xE, 500)

    #C0168
    ChrTalk(
        0x10A,
        "#11P#0600F赛尔盖长官……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xE,
        "#5P#1003F……嗯。\x02",
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
            "#1002F#5P──好，\x01",
            "从现在开始分头行动。\x02\x03",

            "你们穿过东街，\x01",
            "逃出克洛斯贝尔市吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7F58():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7F58)
    Sleep(50)

    def lambda_7F68():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7F68)
    Sleep(50)

    def lambda_7F78():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7F78)
    Sleep(50)

    def lambda_7F88():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7F88)
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
            "#1003F#5P看样子，失控的\x01",
            "似乎是贝尔加德门的警备队。\x02\x03",

            "索妮亚的部下们\x01",
            "应该可以依靠吧。\x02\x03",

            "#1001F离开市区之后，\x01",
            "就立刻联络唐古拉姆门，\x01",
            "让他们派车来接。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#12P#0001F明、明白了……\x01",
            "但是，科长你们呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xE,
        (
            "#1003F#5P我和达德利\x01",
            "留在这里，扰乱他们的视线。\x02\x03",

            "#1002F由我们来吸引他们的注意力，\x01",
            "阻挠他们的追击。\x02",
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
        "#12P#0007F那、那怎么行……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        (
            "#0307F喂喂，\x01",
            "这也太乱来了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x10A,
        (
            "#5P#0604F哼，凭我们两人，\x01",
            "要扰乱敌方视线之后再撤退，\x01",
            "简直就是易如反掌。\x02\x03",

            "#0607F别磨磨蹭蹭了！\x01",
            "形势刻不容缓！快走！\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#12P#0008F达德利警官……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0179
    ChrTalk(
        0x102,
        "#5P#0101F……我们走吧！\x02",
    )

    CloseMessageWindow()

    #N0180
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#1101F#11P科长～！\x01",
            "要小心哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xE,
        "#1002F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_68(15400, 900, -1100, 4000)

    def lambda_829C():

        label("loc_829C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_829C")

    QueueWorkItem2(0xE, 2, lambda_829C)

    def lambda_82AE():

        label("loc_82AE")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_82AE")

    QueueWorkItem2(0x10A, 2, lambda_82AE)
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
            "#11P#1003F──达德利。\x02\x03",

            "#1002F一科王牌的实力，\x01",
            "就让我正式见识一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x10A,
        (
            "#0604F#5P彼此彼此……\x02\x03",

            "#0602F曾经带领过那两人的\x01",
            "传说之班长的实力，\x01",
            "我才真是拭目以待啊！\x02",
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

    # Function_36_7910 end

    def Function_37_8507(): pass

    label("Function_37_8507")

    Sound(489, 0, 100, 0)
    ClearMapObjFlags(0x11, 0x4)

    def lambda_8518():
        OP_96(0xFE, 0x3138, 0x0, 0x34BC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_8518)
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

    # Function_37_8507 end

    def Function_38_8565(): pass

    label("Function_38_8565")

    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_8571():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8571)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_8565 end

    def Function_39_858B(): pass

    label("Function_39_858B")

    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    BeginChrThread(0x12, 0, 0, 3)
    BeginChrThread(0x22, 1, 0, 35)

    def lambda_85AB():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85AB)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0x12, 0x8)
    Return()

    # Function_39_858B end

    def Function_40_85CA(): pass

    label("Function_40_85CA")

    Sleep(1500)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)

    def lambda_85DA():
        OP_95(0xFE, 11600, 0, 300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_85DA)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x0, 0x1F4)
    SetChrChipByIndex(0x10A, 0x2A)
    SetChrSubChip(0x10A, 0x0)
    Sleep(300)
    SetChrChipByIndex(0x10A, 0x2C)
    SetChrSubChip(0x10A, 0x0)
    Sound(531, 0, 100, 0)
    Return()

    # Function_40_85CA end

    def Function_41_8614(): pass

    label("Function_41_8614")

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

    # Function_41_8614 end

    def Function_42_865E(): pass

    label("Function_42_865E")

    Sleep(3000)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_866E():
        OP_96(0xFE, 0x12C0, 0x0, 0xFFFFF5D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_866E)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 100, 0)
    Return()

    # Function_42_865E end

    def Function_43_86A4(): pass

    label("Function_43_86A4")

    Sleep(3500)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_86B4():
        OP_96(0xFE, 0x19C8, 0x0, 0xFFFFEA84, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86B4)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 100, 0)
    Return()

    # Function_43_86A4 end

    def Function_44_86EA(): pass

    label("Function_44_86EA")

    WaitChrThread(0x1B, 3)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_86FE():
        OP_95(0xFE, 10300, 0, 13800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86FE)

    def lambda_8718():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8718)
    WaitChrThread(0xFE, 1)

    def lambda_872D():
        OP_95(0xFE, 8100, 0, 5500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_872D)
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

    # Function_44_86EA end

    def Function_45_876A(): pass

    label("Function_45_876A")

    WaitChrThread(0x1B, 3)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_877B():
        OP_95(0xFE, 10300, 0, 13800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_877B)

    def lambda_8795():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8795)
    WaitChrThread(0xFE, 1)

    def lambda_87AA():
        OP_95(0xFE, 9900, 0, 6900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87AA)
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

    # Function_45_876A end

    def Function_46_87E7(): pass

    label("Function_46_87E7")

    Sleep(3000)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_87F7():
        OP_96(0xFE, 0x1324, 0x0, 0xFFFFEE6C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87F7)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    Return()

    # Function_46_87E7 end

    def Function_47_881F(): pass

    label("Function_47_881F")

    Sleep(3600)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_882F():
        OP_96(0xFE, 0x1B58, 0x0, 0xFFFFE570, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_882F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    Return()

    # Function_47_881F end

    def Function_48_8857(): pass

    label("Function_48_8857")

    WaitChrThread(0x1B, 3)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_886B():
        OP_95(0xFE, 14700, 0, 8500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_886B)

    def lambda_8885():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8885)
    WaitChrThread(0xFE, 1)

    def lambda_889A():
        OP_95(0xFE, 13300, 0, 7100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_889A)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_48_8857 end

    def Function_49_88C9(): pass

    label("Function_49_88C9")

    WaitChrThread(0x1B, 3)
    Sleep(2000)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_88DD():
        OP_95(0xFE, 10300, 0, 13800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_88DD)

    def lambda_88F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_88F7)
    WaitChrThread(0xFE, 1)

    def lambda_890C():
        OP_95(0xFE, 8900, 0, 10100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_890C)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_49_88C9 end

    def Function_50_893B(): pass

    label("Function_50_893B")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)
    Return()

    # Function_50_893B end

    def Function_51_8957(): pass

    label("Function_51_8957")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)
    Return()

    # Function_51_8957 end

    def Function_52_8973(): pass

    label("Function_52_8973")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)
    Return()

    # Function_52_8973 end

    def Function_53_898F(): pass

    label("Function_53_898F")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)
    Return()

    # Function_53_898F end

    def Function_54_89AB(): pass

    label("Function_54_89AB")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -270, 800, 22820, 180)
    EventEnd(0x4)
    Return()

    # Function_54_89AB end

    def Function_55_89C7(): pass

    label("Function_55_89C7")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -21330, 0, 6200, 135)
    EventEnd(0x4)
    Return()

    # Function_55_89C7 end

    def Function_56_89E3(): pass

    label("Function_56_89E3")

    EventBegin(0x1)
    Call(0, 59)
    Sleep(50)
    SetChrPos(0x0, 14920, 0, 5200, 270)
    EventEnd(0x4)
    Return()

    # Function_56_89E3 end

    def Function_57_89FF(): pass

    label("Function_57_89FF")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -8420, -4200, -21200, 270)
    EventEnd(0x4)
    Return()

    # Function_57_89FF end

    def Function_58_8A1B(): pass

    label("Function_58_8A1B")


    #C0184
    ChrTalk(
        0x101,
        (
            "#0000F太阳都落山了吗……\x02\x03",

            "琪雅还在等着我们呢，\x01",
            "不要绕道了，直接回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AA8")

    #C0185
    ChrTalk(
        0x102,
        (
            "#0100F是呀，工作\x01",
            "差不多也告一段落了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B1E")

    label("loc_8AA8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8ADF")

    #C0186
    ChrTalk(
        0x103,
        "#0200F说得是呢，快点回去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B1E")

    label("loc_8ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B1E")

    #C0187
    ChrTalk(
        0x104,
        (
            "#0300F是啊，赶快回去，\x01",
            "看看阿琪的小脸吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B1E")

    Return()

    # Function_58_8A1B end

    def Function_59_8B1F(): pass

    label("Function_59_8B1F")


    #C0188
    ChrTalk(
        0x101,
        (
            "#0000F导力商店似乎\x01",
            "该到闭店的时间了吧。\x02\x03",

            "琪雅还在等着我们呢，\x01",
            "不要绕道了，直接回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BBB")

    #C0189
    ChrTalk(
        0x102,
        (
            "#0100F是呀，工作\x01",
            "差不多也告一段落了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C31")

    label("loc_8BBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BF2")

    #C0190
    ChrTalk(
        0x103,
        "#0200F说得是呢，快点回去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C31")

    label("loc_8BF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C31")

    #C0191
    ChrTalk(
        0x104,
        (
            "#0300F是啊，赶快回去，\x01",
            "看看阿琪的小脸吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C31")

    Return()

    # Function_59_8B1F end

    SaveToFile()

Try(main)
