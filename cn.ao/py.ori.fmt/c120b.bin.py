from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c120b.bin",                # FileName
        "c120b",                    # MapName
        "c120b",                    # Location
        0x001A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 26, 0, 1, 0, 2],
    )

    BuildStringList((
        "c120b",                  # 0
        "警备员珀尔",             # 1
        "接待小姐兰菲",           # 2
        "罗伯兹主任",             # 3
        "约纳",                   # 4
        "警备员比尔斯",           # 5
        "警备员汪古",             # 6
        "研究员库雷",             # 7
        "研究员达比德",           # 8
        "贸易商利泽罗",           # 9
        "ＩＢＣ顾客Ａ",           # 10
        "猎兵",                   # 11
        "猎兵",                   # 12
        "猎兵",                   # 13
        "猎兵",                   # 14
        "猎兵",                   # 15
        "猎兵",                   # 16
        "战鬼西格蒙德",           # 17
        "黑月成员",               # 18
        "黑月成员",               # 19
        "黑月成员",               # 20
        "黑月成员",               # 21
        "黑月成员",               # 22
        "黑月成员",               # 23
        "刘",                     # 24
        "车",                     # 25
        "偃月轮",                 # 26
        "偃月轮",                 # 27
        "路人",                   # 28
        "SE控制",                 # 29
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
        "兰花塔",                 # 45
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch27900.itc",                   # 01
        "chr/ch29300.itc",                   # 02
        "chr/ch06100.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
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

    DeclNpc(2720,    2000,    23920,   0,    385,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(1309,    2000,    24540,   0,    385,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(7329,    2000,    22520,   0,    385,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5929,    2000,    23920,   0,    385,  0x0, 0,   3,   0,   0,   0,   0,   4,   255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 62,  4.5,                   28.0,                  1.0,                   400.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.44999998807907104,  -7.0,                  -0.19999998807907104,  1.0])

    DeclActor(16750,   -1000,   -15740,  1200,    16750,   0,       -15740,  0x007C, 0,  3,  0x0000)
    DeclActor(21600,   0,       17000,   3000,    21600,   2000,    18500,   0x007C, 0,  66, 0x0000)
    DeclActor(-18200,  0,       -19000,  3000,    -18200,  2000,    -19000,  0x007C, 0,  67, 0x0000)
    DeclActor(77220,   -2500,   20290,   2000,    77220,   -1000,   20290,   0x007C, 0,  70, 0x0000)

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

    ChipFrameInfo(2204, 0)                                       # 0

    ScpFunction((
        "Function_0_89C",          # 00, 0
        "Function_1_94C",          # 01, 1
        "Function_2_9C3",          # 02, 2
        "Function_3_D47",          # 03, 3
        "Function_4_E82",          # 04, 4
        "Function_5_FBF",          # 05, 5
        "Function_6_1135",         # 06, 6
        "Function_7_1201",         # 07, 7
        "Function_8_1385",         # 08, 8
        "Function_9_152B",         # 09, 9
        "Function_10_15AC",        # 0A, 10
        "Function_11_1640",        # 0B, 11
        "Function_12_1656",        # 0C, 12
        "Function_13_1666",        # 0D, 13
        "Function_14_3036",        # 0E, 14
        "Function_15_306F",        # 0F, 15
        "Function_16_30A8",        # 10, 16
        "Function_17_31A4",        # 11, 17
        "Function_18_3286",        # 12, 18
        "Function_19_3300",        # 13, 19
        "Function_20_33F6",        # 14, 20
        "Function_21_34E7",        # 15, 21
        "Function_22_3561",        # 16, 22
        "Function_23_364D",        # 17, 23
        "Function_24_3737",        # 18, 24
        "Function_25_37B1",        # 19, 25
        "Function_26_38E6",        # 1A, 26
        "Function_27_39AF",        # 1B, 27
        "Function_28_3A51",        # 1C, 28
        "Function_29_3BB1",        # 1D, 29
        "Function_30_3CCA",        # 1E, 30
        "Function_31_3D44",        # 1F, 31
        "Function_32_3E7D",        # 20, 32
        "Function_33_3F82",        # 21, 33
        "Function_34_4005",        # 22, 34
        "Function_35_401D",        # 23, 35
        "Function_36_4071",        # 24, 36
        "Function_37_40A5",        # 25, 37
        "Function_38_40FD",        # 26, 38
        "Function_39_419E",        # 27, 39
        "Function_40_42FA",        # 28, 40
        "Function_41_43E4",        # 29, 41
        "Function_42_43FC",        # 2A, 42
        "Function_43_4471",        # 2B, 43
        "Function_44_4599",        # 2C, 44
        "Function_45_460D",        # 2D, 45
        "Function_46_4625",        # 2E, 46
        "Function_47_4684",        # 2F, 47
        "Function_48_46A0",        # 30, 48
        "Function_49_46BC",        # 31, 49
        "Function_50_46D8",        # 32, 50
        "Function_51_485E",        # 33, 51
        "Function_52_4901",        # 34, 52
        "Function_53_49DC",        # 35, 53
        "Function_54_4A4F",        # 36, 54
        "Function_55_4AC5",        # 37, 55
        "Function_56_4B3B",        # 38, 56
        "Function_57_4B93",        # 39, 57
        "Function_58_4BEB",        # 3A, 58
        "Function_59_4C43",        # 3B, 59
        "Function_60_5877",        # 3C, 60
        "Function_61_5927",        # 3D, 61
        "Function_62_599B",        # 3E, 62
        "Function_63_5B3B",        # 3F, 63
        "Function_64_649E",        # 40, 64
        "Function_65_64DE",        # 41, 65
        "Function_66_653F",        # 42, 66
        "Function_67_68AF",        # 43, 67
        "Function_68_6A20",        # 44, 68
        "Function_69_6A65",        # 45, 69
        "Function_70_6AAA",        # 46, 70
    ))


    def Function_0_89C(): pass

    label("Function_0_89C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_8D4"),
        (1, "loc_8E0"),
        (2, "loc_8EC"),
        (3, "loc_8F8"),
        (4, "loc_904"),
        (5, "loc_910"),
        (6, "loc_91C"),
        (SWITCH_DEFAULT, "loc_928"),
    )


    label("loc_8D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_8E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_8EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_8F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_904")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_910")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_91C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_928")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_934")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_94B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_94B")

    Return()

    # Function_0_89C end

    def Function_1_94C(): pass

    label("Function_1_94C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_95A")
    Jump("loc_977")

    label("loc_95A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 1)), scpexpr(EXPR_END)), "loc_977")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_98B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)
    Jump("loc_9C2")

    label("loc_98B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_99F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)
    Jump("loc_9C2")

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_9B3")
    ClearScenarioFlags(0x22, 2)
    Event(0, 59)
    Jump("loc_9C2")

    label("loc_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_9C2")
    ClearScenarioFlags(0x22, 3)
    Event(0, 63)

    label("loc_9C2")

    Return()

    # Function_1_94C end

    def Function_2_9C3(): pass

    label("Function_2_9C3")

    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x13DE4, 0x0, 0x71E8)
    OP_E3(0x13C54, 0x0, 0xD1B0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0D")
    Sound(868, 1, 60, 0)

    label("loc_A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A20")
    OP_70(0x11, 0x0)
    Jump("loc_A24")

    label("loc_A20")

    OP_70(0x11, 0x1E)

    label("loc_A24")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3C")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_A3C")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 19000, 10, 16000, 6000, 2000, 0)
    OP_10(0x6, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A70")
    OP_10(0x6, 0x1)
    OP_10(0x1, 0x0)

    label("loc_A70")

    OP_1B(0x0, 0x0, 0x44)
    OP_1B(0x2, 0x0, 0x45)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A90")
    OP_66(0x1, 0x1)

    label("loc_A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C72")
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "kurotuki00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "knuki", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lwindow2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ent2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bfire00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bfire01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x1, 0x1)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    ClearChrFlags(0x20, 0x80)
    OP_78(0x12, 0x20)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x0)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    SetChrPos(0x20, -18200, 0, -19000, 0)
    Jump("loc_D46")

    label("loc_C72")

    SetMapObjFrame(0xFF, "kurotuki00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "knuki", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lwindow2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bfire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bfire01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x0, 0x1)
    SetMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x14, 0x4)

    label("loc_D46")

    Return()

    # Function_2_9C3 end

    def Function_3_D47(): pass

    label("Function_3_D47")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E39")
    Sound(14, 0, 100, 0)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('粉红液体', 1)"), scpexpr(EXPR_END)), "loc_DCA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '粉红液体'),
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
    Jump("loc_E34")

    label("loc_DCA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '粉红液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '粉红液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x11, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E34")

    Jump("loc_E76")

    label("loc_E39")

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

    label("loc_E76")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_D47 end

    def Function_4_E82(): pass

    label("Function_4_E82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F53")

    #C0004
    ChrTalk(
        0xB,
        (
            "#02306F我经常在导力网络上看到\x01",
            "有关那些家伙的情报……\x02\x03",

            "#02310F但从没听说过\x01",
            "他们是如此可怕啊！\x02\x03",

            "#02301F你们要是想去找他们，\x01",
            "可千万要多加小心啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#00001F嗯……\x01",
            "你们也要尽快去避难。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FBB")

    label("loc_F53")


    #C0006
    ChrTalk(
        0xB,
        (
            "#02306F那些家伙太可怕了……\x01",
            "尤其是那个红发大叔。\x02\x03",

            "#02301F你们要是想去找他们，\x01",
            "可千万要多加小心啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBB")

    TalkEnd(0xFE)
    Return()

    # Function_4_E82 end

    def Function_5_FBF(): pass

    label("Function_5_FBF")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1131")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "请求回复\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1096")

    #C0007
    ChrTalk(
        0xFE,
        "知道了，交给我吧！\x02",
    )

    CloseMessageWindow()
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

    #C0008
    ChrTalk(
        0xFE,
        "你们一定要小心啊！\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_112C")

    label("loc_1096")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AA")
    Jump("loc_112C")

    label("loc_10AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0009
    ChrTalk(
        0xFE,
        (
            "我把爱普斯泰恩财团\x01",
            "开发中的携带型\x01",
            "回复装置带出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "如果你们需要接受治疗，\x01",
            "随时都可以和我说！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112C")

    Jump("loc_FCC")

    label("loc_1131")

    TalkEnd(0xFE)
    Return()

    # Function_5_FBF end

    def Function_6_1135(): pass

    label("Function_6_1135")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B9")

    #C0011
    ChrTalk(
        0xFE,
        "市内也出现了那么多魔兽……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "总、总之，\x01",
            "这里的人就\x01",
            "交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "我会担负起责任，\x01",
            "引领大家去避难的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11FD")

    label("loc_11B9")


    #C0014
    ChrTalk(
        0xFE,
        (
            "这里的人就\x01",
            "交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "我会担负起责任，\x01",
            "引领大家去避难的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FD")

    TalkEnd(0xFE)
    Return()

    # Function_6_1135 end

    def Function_7_1201(): pass

    label("Function_7_1201")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1313")

    #C0016
    ChrTalk(
        0xFE,
        "各位，请把这些拿去……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了５个。\x02",
        )
    )

    AddItemNumber('中回复药', 5)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了２个。\x02",
        )
    )

    AddItemNumber('圣灵药', 2)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0019
    ChrTalk(
        0xFE,
        (
            "我把接待处中的\x01",
            "紧急用品带出来了，\x01",
            "请大家拿去用吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00000F多谢。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#00103F兰菲小姐，\x01",
            "你们也要小心……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 0)
    Jump("loc_1381")

    label("loc_1313")


    #C0022
    ChrTalk(
        0xFE,
        "为何会发生这种事情……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "幸好玛丽亚贝尔大小姐正在出差，\x01",
            "不用担心她的安危，\x01",
            "但我脑子现在还是一片混乱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1381")

    TalkEnd(0xFE)
    Return()

    # Function_7_1201 end

    def Function_8_1385(): pass

    label("Function_8_1385")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x153, 0x8)
    SoundLoad(468)
    ClearChrFlags(0x20, 0x80)
    OP_78(0x12, 0x20)
    OP_49()
    SetChrPos(0x20, -20150, 2000, 23000, 90)
    OP_D5(0x20, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0x79, 0xB4, 0x1, 0x20)
    SetMapObjFlags(0x13, 0x1000)
    OP_71(0x13, 0x12D, 0x168, 0x0, 0x20)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1443")
    ClearChrFlags(0x23, 0x80)
    LoadChrToIndex("chr/ch25200.itc", 0x1E)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x0)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -7500, 0, 12700, 0)

    label("loc_1443")

    FadeToBright(1000, 0)
    BeginChrThread(0x20, 3, 0, 9)
    BeginChrThread(0x24, 1, 0, 11)
    OP_68(-3550, 1500, 30000, 0)
    MoveCamera(60, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(37150, 0)
    OP_68(3700, 1500, 17800, 10000)
    Sleep(8500)
    OP_0D()
    Fade(500)
    EndChrThread(0x20, 0x3)
    EndChrThread(0x24, 0x1)
    BeginChrThread(0x20, 3, 0, 10)
    BeginChrThread(0x24, 1, 0, 12)
    OP_68(14550, 2200, -6000, 0)
    MoveCamera(65, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20500, 0)
    OP_68(-10600, 1000, -12600, 10500)
    MoveCamera(65, 18, 0, 10500)
    SetCameraDistance(33650, 10500)
    Sleep(8500)
    StopSound(468, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c100B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1385 end

    def Function_9_152B(): pass

    label("Function_9_152B")

    SetChrPos(0xFE, -20150, 2000, 23000, 90)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -2900, 2000, 23000)
    OP_9F(0x1, 1650, 2000, 23000)
    OP_9F(0x1, 3750, 2000, 20000)
    OP_9F(0x1, 4350, 350, 14700)
    OP_9F(0x1, 7440, 150, 12600)
    OP_9F(0x1, 12390, 150, 11900)
    OP_9F(0x1, 17950, 150, 10200)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_9_152B end

    def Function_10_15AC(): pass

    label("Function_10_15AC")

    SetChrPos(0xFE, 20000, 0, 2350, 180)
    OP_D5(0x20, 0x0, 0x2BF20, 0x0, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 20000, 0, -8300)
    OP_9F(0x1, 15500, 0, -11000)
    OP_9F(0x1, 9500, 0, -11000)
    OP_9F(0x1, -5500, 0, -11000)
    OP_9F(0x1, -12000, 0, -11000)
    OP_9F(0x1, -17500, 0, -12000)
    OP_9F(0x1, -18500, 0, -25800)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_10_15AC end

    def Function_11_1640(): pass

    label("Function_11_1640")

    Sound(468, 2, 100, 0)
    Sound(457, 0, 100, 0)
    Sleep(4000)
    Sound(493, 0, 70, 0)
    Return()

    # Function_11_1640 end

    def Function_12_1656(): pass

    label("Function_12_1656")

    Sound(458, 0, 100, 0)
    Sleep(6000)
    Sound(493, 0, 70, 0)
    Return()

    # Function_12_1656 end

    def Function_13_1666(): pass

    label("Function_13_1666")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04500.itp")
    LoadChrToIndex("chr/ch03350.itc", 0x23)
    LoadChrToIndex("chr/ch03351.itc", 0x24)
    LoadChrToIndex("chr/ch03352.itc", 0x25)
    LoadChrToIndex("apl/ch51535.itc", 0x26)
    LoadChrToIndex("chr/ch03354.itc", 0x27)
    LoadChrToIndex("chr/ch41950.itc", 0x37)
    LoadChrToIndex("chr/ch41951.itc", 0x38)
    LoadChrToIndex("chr/ch41952.itc", 0x39)
    LoadChrToIndex("apl/ch51537.itc", 0x3A)
    LoadChrToIndex("chr/ch41953.itc", 0x3B)
    LoadChrToIndex("chr/ch42050.itc", 0x3C)
    LoadChrToIndex("chr/ch42051.itc", 0x3D)
    LoadChrToIndex("chr/ch42052.itc", 0x3E)
    LoadChrToIndex("apl/ch51536.itc", 0x3F)
    LoadChrToIndex("chr/ch42053.itc", 0x40)
    LoadChrToIndex("chr/ch42056.itc", 0x41)
    LoadChrToIndex("chr/ch31400.itc", 0x28)
    LoadChrToIndex("chr/ch31452.itc", 0x29)
    LoadChrToIndex("chr/ch31500.itc", 0x2D)
    LoadChrToIndex("chr/ch31551.itc", 0x2E)
    LoadChrToIndex("chr/ch31552.itc", 0x2F)
    LoadChrToIndex("chr/ch31553.itc", 0x30)
    LoadChrToIndex("chr/ch31556.itc", 0x31)
    LoadChrToIndex("chr/ch12500.itc", 0x32)
    LoadChrToIndex("chr/ch12551.itc", 0x33)
    LoadChrToIndex("chr/ch12552.itc", 0x34)
    LoadChrToIndex("chr/ch12553.itc", 0x35)
    LoadChrToIndex("chr/ch12556.itc", 0x36)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev15036.eff")
    LoadEffect(0x2, "battle/ms00001.eff")
    LoadEffect(0x3, "eff/cutin33.eff")
    LoadEffect(0x4, "battle/cr033300.eff")
    LoadEffect(0x5, "battle/cr033301.eff")
    LoadEffect(0x6, "event/ev15035.eff")
    LoadEffect(0x7, "event/ev15041.eff")
    LoadEffect(0x8, "battle/sp003000.eff")
    LoadEffect(0xA, "battle/cr004000.eff")
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(868)
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(926)
    SoundLoad(832)
    SoundLoad(3853)
    SoundLoad(3854)
    SoundLoad(3855)
    SetChrChipByIndex(0x18, 0x26)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 0x3D)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x3D)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x38)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x38)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x38)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x1F, 0x28)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    OP_52(0x1F, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 0x2D)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x32)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x2D)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x32)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x2D)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x32)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x21, 0x31)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x21, 0x2)
    SetChrChipByIndex(0x22, 0x36)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x22, 0x2)
    SetMapObjFrame(0xFF, "kurotuki01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bfire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bfire01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x0, 0x1)
    SetMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_68(-8550, 4500, -9450, 0)
    MoveCamera(55, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29000, 0)
    OP_68(-14250, 4500, 9750, 10000)
    MoveCamera(55, 5, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(29000, 10000)
    Sound(868, 2, 60, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x12, -29000, 2000, 21700, 90)
    SetChrPos(0x13, -30500, 2000, 23700, 90)
    SetChrPos(0x14, -31000, 2000, 21700, 90)
    SetChrPos(0x15, -32500, 2000, 23700, 90)
    SetChrPos(0x16, -33000, 2000, 21700, 90)
    SetChrPos(0x17, -34500, 2000, 23700, 90)
    OP_68(-27000, 3000, 22700, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    OP_68(-15500, 3000, 22700, 4000)
    MoveCamera(335, 15, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15000, 4000)

    def lambda_1C02():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1C02)
    Sleep(50)

    def lambda_1C1A():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1C1A)
    Sleep(50)

    def lambda_1C32():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1C32)
    Sleep(50)

    def lambda_1C4A():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1C4A)
    Sleep(50)

    def lambda_1C62():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1C62)
    Sleep(50)

    def lambda_1C7A():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1C7A)
    OP_0D()
    Sleep(3000)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    Fade(500)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1F, 17300, 0, 13150, 270)
    SetChrPos(0x19, 19300, 0, 12150, 270)
    SetChrPos(0x1A, 19300, 0, 13150, 270)
    SetChrPos(0x1B, 19300, 0, 14150, 270)
    SetChrPos(0x1C, 20800, 0, 12150, 270)
    SetChrPos(0x1D, 20800, 0, 13150, 270)
    SetChrPos(0x1E, 20800, 0, 14150, 270)
    OP_68(17300, 1000, 13150, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 1500)
    OP_0D()
    OP_6F(0x79)

    #C0024
    ChrTalk(
        0x1F,
        "#11P……来了。\x02",
    )

    CloseMessageWindow()
    OP_68(19300, 1000, 13150, 1000)
    OP_6F(0x79)

    #C0025
    ChrTalk(
        0x1F,
        (
            "#11P我们在此死守，\x01",
            "不要让他们接近公司。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("众成员")

    #A0026
    AnonymousTalk(
        0xFF,
        "#4S是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(17300, 1000, 13150, 500)
    Sound(250, 0, 100, 0)
    SetChrChipByIndex(0x19, 0x2E)
    BeginChrThread(0x19, 1, 0, 14)
    Sleep(50)
    SetChrChipByIndex(0x1B, 0x2E)
    BeginChrThread(0x1B, 1, 0, 15)
    Sleep(50)
    SetChrChipByIndex(0x1A, 0x33)
    BeginChrThread(0x1A, 1, 0, 14)
    Sleep(50)
    Sound(255, 0, 60, 0)
    SetChrChipByIndex(0x1E, 0x33)
    BeginChrThread(0x1E, 1, 0, 15)
    Sleep(50)
    SetChrChipByIndex(0x1C, 0x33)
    BeginChrThread(0x1C, 1, 0, 14)
    Sleep(50)
    SetChrChipByIndex(0x1D, 0x2E)
    BeginChrThread(0x1D, 1, 0, 15)
    Sleep(500)
    Fade(500)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    SetChrChip(0x1, 0x19, 0x0, 0x0)
    SetChrChip(0x1, 0x1A, 0x0, 0x0)
    SetChrChip(0x1, 0x1B, 0x0, 0x0)
    SetChrChip(0x1, 0x1C, 0x0, 0x0)
    SetChrChip(0x1, 0x1D, 0x0, 0x0)
    SetChrChip(0x1, 0x1E, 0x0, 0x0)
    SetChrPos(0x1F, 15300, 0, 12000, 270)
    SetChrPos(0x19, 10550, 0, 13400, 270)
    SetChrPos(0x1A, 11150, 0, 11000, 270)
    SetChrPos(0x1B, 12150, 0, 12000, 270)
    SetChrPos(0x1C, 13250, 0, 14000, 270)
    SetChrPos(0x1D, 12550, 0, 9800, 270)
    SetChrPos(0x1E, 13800, 0, 14850, 270)
    SetChrPos(0x18, -6150, 10, 12000, 90)
    SetChrPos(0x12, -2450, 0, 13400, 90)
    SetChrPos(0x13, -1850, 0, 11500, 90)
    SetChrPos(0x14, -4750, 0, 14500, 90)
    SetChrPos(0x15, -6700, 0, 13350, 90)
    SetChrPos(0x16, -6100, 0, 11550, 90)
    SetChrPos(0x17, -4500, 0, 10450, 90)
    OP_68(3000, 1000, 13250, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_68(3000, 1000, 12250, 2000)
    MoveCamera(45, 20, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(16000, 2000)
    BeginChrThread(0x12, 0, 0, 41)
    Sleep(50)
    BeginChrThread(0x13, 0, 0, 45)
    Sleep(50)
    BeginChrThread(0x14, 0, 0, 46)
    Sleep(50)
    BeginChrThread(0x15, 0, 0, 47)
    Sleep(50)
    BeginChrThread(0x16, 0, 0, 48)
    Sleep(50)
    BeginChrThread(0x17, 0, 0, 49)
    OP_0D()
    Sound(250, 0, 100, 0)
    BeginChrThread(0x19, 0, 0, 16)
    Sleep(200)
    BeginChrThread(0x1E, 0, 0, 31)
    Sleep(200)
    BeginChrThread(0x1A, 0, 0, 19)
    Sleep(200)
    BeginChrThread(0x1C, 0, 0, 25)
    Sleep(200)
    BeginChrThread(0x1D, 0, 0, 28)
    Sleep(200)
    BeginChrThread(0x1B, 0, 0, 22)
    OP_6F(0x79)
    WaitChrThread(0x19, 0)
    WaitChrThread(0x1A, 0)
    WaitChrThread(0x1B, 0)
    WaitChrThread(0x1C, 0)
    WaitChrThread(0x1D, 0)
    WaitChrThread(0x1E, 0)
    StopSound(865, 500, 90)
    StopSound(861, 500, 50)
    StopEffect(0x0, 0x2)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)

    #C0027
    ChrTalk(
        0x12,
        "#6P啧……！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x13,
        "#6P是黑月的拳士们……！\x02",
    )

    CloseMessageWindow()
    OP_A6(0x12, 0x0, 0x32, 0x1F4, 0xBB8)
    Fade(100)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x12, 0x3C)
    SetChrSubChip(0x12, 0x0)
    OP_0D()

    def lambda_2123():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_2123)
    Sleep(50)
    OP_A6(0x17, 0x0, 0x32, 0x1F4, 0xBB8)
    Fade(100)
    Sound(531, 0, 60, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0x14, 0x39)
    SetChrSubChip(0x14, 0x1)
    SetChrChipByIndex(0x17, 0x39)
    SetChrSubChip(0x17, 0x1)
    OP_0D()
    OP_68(2000, 1000, 12250, 1000)
    SetCameraDistance(17000, 1000)
    SetChrChipByIndex(0x14, 0x3A)

    def lambda_2192():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2192)
    Sleep(50)
    SetChrChipByIndex(0x17, 0x3A)

    def lambda_21AE():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_21AE)
    Sleep(50)
    SetChrChipByIndex(0x15, 0x3A)

    def lambda_21CA():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_21CA)
    Sleep(50)
    SetChrChipByIndex(0x16, 0x3A)

    def lambda_21E6():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_21E6)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x3F)

    def lambda_2202():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2202)
    Sleep(50)
    SetChrChipByIndex(0x13, 0x3F)

    def lambda_221E():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_221E)
    WaitChrThread(0x12, 1)
    Sound(531, 0, 50, 0)
    Sound(538, 0, 40, 0)
    Sound(540, 0, 40, 0)
    SetChrChipByIndex(0x12, 0x3C)
    SetChrSubChip(0x12, 0x0)
    WaitChrThread(0x13, 1)
    SetChrChipByIndex(0x13, 0x3C)
    SetChrSubChip(0x13, 0x0)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x37)
    SetChrSubChip(0x14, 0x0)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x37)
    SetChrSubChip(0x17, 0x0)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x37)
    SetChrSubChip(0x15, 0x0)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x37)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x18, 0x80)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #N0029
    NpcTalk(
        0x18,
        "豪气的声音",
        (
            "#3853V#37A#30W呵……\x01",
            "很有精神啊，不错。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(-1350, 1000, 12000, 0)
    MoveCamera(310, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_F0(0x0, 0x1)
    OP_68(6360, 1000, 12200, 3000)
    MoveCamera(310, 20, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16000, 3000)
    SetChrPos(0x18, 0, 0, 12000, 90)

    def lambda_234F():
        OP_95(0xFE, 5350, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_234F)
    SetChrChipByIndex(0x19, 0x2F)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x34)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x2F)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x34)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x2F)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x34)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x19, 10050, 0, 12700, 0)
    SetChrPos(0x1A, 10050, 0, 10200, 0)
    SetChrPos(0x1B, 10500, 0, 11500, 0)
    SetChrPos(0x1C, 9750, 0, 14200, 0)
    SetChrPos(0x1D, 9050, 0, 9300, 0)
    SetChrPos(0x1E, 8300, 0, 14850, 0)
    SetChrPos(0x12, -1450, 0, 13400, 90)
    SetChrPos(0x13, -850, 0, 10500, 90)
    SetChrPos(0x14, -2750, 0, 14500, 90)
    SetChrPos(0x15, -4700, 0, 13250, 90)
    SetChrPos(0x16, -4100, 0, 10550, 90)
    SetChrPos(0x17, -2500, 0, 9450, 90)

    def lambda_2465():

        label("loc_2465")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_2465")

    QueueWorkItem2(0x19, 2, lambda_2465)

    def lambda_2477():

        label("loc_2477")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_2477")

    QueueWorkItem2(0x1A, 2, lambda_2477)

    def lambda_2489():

        label("loc_2489")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_2489")

    QueueWorkItem2(0x1B, 2, lambda_2489)

    def lambda_249B():

        label("loc_249B")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_249B")

    QueueWorkItem2(0x1C, 2, lambda_249B)

    def lambda_24AD():

        label("loc_24AD")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_24AD")

    QueueWorkItem2(0x1D, 2, lambda_24AD)

    def lambda_24BF():

        label("loc_24BF")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_24BF")

    QueueWorkItem2(0x1E, 2, lambda_24BF)
    WaitChrThread(0x18, 1)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    OP_0D()
    OP_6F(0x79)

    #C0030
    ChrTalk(
        0x19,
        "#11P……！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x1A,
        "#12P『赤色战鬼』……！\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0032
    AnonymousTalk(
        0x18,
        (
            "#3854V#30W哼哼，现在是特别优待时间，\x01",
            "就给你们一个摘下我脑袋的好机会。\x02\x03",

            "#3855V所有人一起上吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF0F)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0033
    ChrTalk(
        0x1B,
        "#12P什么……！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x1C,
        "#11P竟敢小看我们……！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x1F,
        "快退开！那家伙可是……！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 80, 0)
    Sound(372, 0, 60, 0)
    SetChrChipByIndex(0x18, 0x27)
    SetChrSubChip(0x18, 0x0)
    OP_0D()
    OP_68(5350, 1000, 12000, 2000)
    MoveCamera(315, 35, -15, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x19, 0, 0, 17)
    Sleep(100)
    BeginChrThread(0x1D, 0, 0, 29)
    Sleep(100)
    BeginChrThread(0x1B, 0, 0, 23)
    Sleep(100)
    BeginChrThread(0x1A, 0, 0, 20)
    Sleep(100)
    BeginChrThread(0x1C, 0, 0, 26)
    Sleep(100)
    BeginChrThread(0x1E, 0, 0, 32)
    WaitChrThread(0x19, 0)
    WaitChrThread(0x1A, 0)
    WaitChrThread(0x1B, 0)
    WaitChrThread(0x1C, 0)
    WaitChrThread(0x1D, 0)
    WaitChrThread(0x1E, 0)

    #C0036
    ChrTalk(
        0x18,
        "#04503F#5P哼，只有这点实力吗？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x18, 0, 0, 50)
    MoveCamera(310, 35, -5, 2500)
    SetCameraDistance(14000, 2500)
    Sleep(2500)
    OP_68(5350, 1300, 12000, 300)
    MoveCamera(225, 25, -5, 300)
    SetCameraDistance(12000, 300)
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x19, 0, 0, 18)
    Sleep(50)
    BeginChrThread(0x1A, 0, 0, 21)
    Sleep(50)
    BeginChrThread(0x1B, 0, 0, 24)
    Sleep(50)
    BeginChrThread(0x1C, 0, 0, 27)
    Sleep(50)
    BeginChrThread(0x1D, 0, 0, 30)
    Sleep(50)
    BeginChrThread(0x1E, 0, 0, 33)
    Sleep(500)
    Fade(500)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1B, 0x0)
    EndChrThread(0x1C, 0x0)
    EndChrThread(0x1D, 0x0)
    EndChrThread(0x1E, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrPos(0x19, 8150, 0, 11900, 0)
    SetChrPos(0x1A, 4750, 0, 9450, 0)
    SetChrPos(0x1B, 6850, 0, 9800, 0)
    SetChrPos(0x1C, 7150, 0, 14000, 0)
    SetChrPos(0x1D, 3100, 0, 10500, 0)
    SetChrPos(0x1E, 5300, 0, 15750, 0)
    SetChrChipByIndex(0x19, 0x2F)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x34)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x2F)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x34)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x31)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x36)
    SetChrSubChip(0x1E, 0x0)
    OP_68(5350, 1000, 12000, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(10000, 0)
    BeginChrThread(0x18, 0, 0, 52)
    MoveCamera(146, 23, -5, 300)
    SetCameraDistance(12000, 300)
    BeginChrThread(0x19, 0, 0, 18)
    Sleep(50)
    BeginChrThread(0x1A, 0, 0, 21)
    Sleep(50)
    BeginChrThread(0x1B, 0, 0, 24)
    Sleep(50)
    BeginChrThread(0x1C, 0, 0, 27)
    Sleep(50)
    BeginChrThread(0x1D, 0, 0, 30)
    Sleep(50)
    BeginChrThread(0x1E, 0, 0, 33)
    Sleep(500)
    Fade(500)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1B, 0x0)
    EndChrThread(0x1C, 0x0)
    EndChrThread(0x1D, 0x0)
    EndChrThread(0x1E, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrPos(0x19, 8150, 0, 11900, 0)
    SetChrPos(0x1A, 4750, 0, 9450, 0)
    SetChrPos(0x1B, 6850, 0, 9800, 0)
    SetChrPos(0x1C, 7150, 0, 14000, 0)
    SetChrPos(0x1D, 3100, 0, 10500, 0)
    SetChrPos(0x1E, 5300, 0, 15750, 0)
    SetChrChipByIndex(0x19, 0x2F)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x34)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x2F)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x34)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x31)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x36)
    SetChrSubChip(0x1E, 0x0)
    OP_68(5350, 1000, 12000, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(10000, 0)
    BeginChrThread(0x18, 0, 0, 52)
    OP_68(5350, 1300, 12000, 300)
    MoveCamera(25, 10, -5, 300)
    SetCameraDistance(12000, 300)
    BeginChrThread(0x19, 0, 0, 18)
    Sleep(50)
    BeginChrThread(0x1A, 0, 0, 21)
    Sleep(50)
    BeginChrThread(0x1B, 0, 0, 24)
    Sleep(50)
    BeginChrThread(0x1C, 0, 0, 27)
    Sleep(50)
    BeginChrThread(0x1D, 0, 0, 30)
    Sleep(50)
    BeginChrThread(0x1E, 0, 0, 33)
    WaitChrThread(0x18, 0)
    WaitChrThread(0x19, 0)
    WaitChrThread(0x1A, 0)
    WaitChrThread(0x1B, 0)
    WaitChrThread(0x1C, 0)
    WaitChrThread(0x1D, 0)
    WaitChrThread(0x1E, 0)
    EndChrThread(0x19, 0x2)
    EndChrThread(0x1A, 0x2)
    EndChrThread(0x1B, 0x2)
    EndChrThread(0x1C, 0x2)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1E, 0x2)
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0037
    ChrTalk(
        0x1E,
        "哇……！\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x1B,
        "……怎、怎么可能……\x02",
    )

    CloseMessageWindow()
    OP_68(15300, 800, 12000, 2000)
    MoveCamera(45, 25, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(17000, 2000)
    OP_6F(0x79)

    #C0039
    ChrTalk(
        0x1F,
        "#11P唔……！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x1F, 0x29)
    SetChrSubChip(0x1F, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sound(881, 0, 80, 0)
    PlayEffect(0x6, 0x0, 0x1F, 0x1, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x5DC)
    SetCameraDistance(15000, 1600)
    OP_A6(0x1F, 0x0, 0xA, 0x640, 0xBB8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    SetCameraDistance(16000, 100)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    Sound(259, 0, 70, 0)
    Sound(832, 2, 100, 0)
    OP_A6(0x1F, 0x0, 0x14, 0x1F4, 0xBB8)
    PlayEffect(0x7, 0x0, 0x1F, 0x1, 0, 100, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0040
    ChrTalk(
        0x18,
        (
            "#04502F#6P#N哼哼……是曹的左膀右臂啊。\x02\x03",

            "原本可以陪你玩玩，\x01",
            "但我还要去找你们的老大。\x02\x03",

            "#04504F全员齐上，干掉他。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0xC8)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("众猎兵")

    #A0041
    AnonymousTalk(
        0xFF,
        "#5S是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0042
    ChrTalk(
        0x1F,
        "#11P啧……！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x12, 7000, 0, 12900, 90)
    SetChrPos(0x13, 7000, 0, 11450, 90)
    BeginChrThread(0x12, 0, 0, 38)
    Sleep(400)
    BeginChrThread(0x13, 0, 0, 42)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    Fade(500)
    EndChrThread(0x1F, 0x1)
    SetChrPos(0x1F, 20000, 0, 12500, 270)
    SetChrPos(0x18, 10550, 0, 14450, 90)
    SetChrPos(0x12, 17550, 0, 13400, 90)
    SetChrPos(0x13, 18150, 0, 10500, 90)
    SetChrPos(0x14, 11750, 0, 13500, 90)
    SetChrPos(0x15, 9700, 0, 12250, 90)
    SetChrPos(0x16, 8100, 0, 10550, 90)
    SetChrPos(0x17, 11000, 0, 9450, 90)
    BeginChrThread(0x18, 0, 0, 51)
    ClearChrFlags(0x14, 0x20)
    ClearChrFlags(0x15, 0x20)
    ClearChrFlags(0x16, 0x20)
    ClearChrFlags(0x17, 0x20)
    SetChrChipByIndex(0x12, 0x3C)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x3C)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x38)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x38)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x38)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)

    def lambda_2DDA():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2DDA)

    def lambda_2DEF():
        OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2DEF)

    def lambda_2E04():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2E04)

    def lambda_2E19():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2E19)

    def lambda_2E2E():

        label("loc_2E2E")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_2E2E")

    QueueWorkItem2(0x14, 2, lambda_2E2E)

    def lambda_2E40():

        label("loc_2E40")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_2E40")

    QueueWorkItem2(0x17, 2, lambda_2E40)

    def lambda_2E52():

        label("loc_2E52")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_2E52")

    QueueWorkItem2(0x15, 2, lambda_2E52)

    def lambda_2E64():

        label("loc_2E64")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_2E64")

    QueueWorkItem2(0x16, 2, lambda_2E64)
    OP_68(17500, 800, 12500, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(21500, 800, 12000, 1000)
    MoveCamera(305, 25, 0, 10000)
    SetCameraDistance(20000, 10000)
    BeginChrThread(0x12, 0, 0, 39)
    OP_0D()
    WaitChrThread(0x14, 1)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 70, 0)
    BeginChrThread(0x14, 0, 0, 35)
    BeginChrThread(0x14, 3, 0, 36)
    WaitChrThread(0x17, 1)
    BeginChrThread(0x17, 0, 0, 35)
    BeginChrThread(0x17, 3, 0, 36)
    WaitChrThread(0x15, 1)
    BeginChrThread(0x15, 0, 0, 35)
    BeginChrThread(0x15, 3, 0, 36)
    WaitChrThread(0x16, 1)
    BeginChrThread(0x16, 0, 0, 35)
    BeginChrThread(0x16, 3, 0, 36)
    Sleep(1200)
    BeginChrThread(0x13, 0, 0, 43)
    Sleep(1200)
    BeginChrThread(0x12, 0, 0, 40)
    Sleep(1500)
    BeginChrThread(0x13, 0, 0, 44)
    Sleep(500)
    StopSound(865, 300, 90)
    StopSound(861, 300, 60)
    EndChrThread(0x14, 0x2)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x3)
    SetChrChipByIndex(0x14, 0x38)
    SetChrSubChip(0x14, 0x0)

    def lambda_2F5A():
        OP_95(0xFE, 26000, 0, 13500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2F5A)
    Sleep(100)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)

    def lambda_2F8B():
        OP_95(0xFE, 20000, 0, 9140, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2F8B)
    Sleep(100)
    EndChrThread(0x15, 0x2)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    SetChrChipByIndex(0x15, 0x38)
    SetChrSubChip(0x15, 0x0)

    def lambda_2FBC():
        OP_95(0xFE, 23800, 0, 13000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2FBC)
    Sleep(100)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x16, 0x2)
    SetChrChipByIndex(0x16, 0x38)
    SetChrSubChip(0x16, 0x0)

    def lambda_2FED():
        OP_95(0xFE, 21000, 0, 10350, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2FED)
    FadeToDark(1000, 0, -1)
    Sleep(100)
    StopSound(868, 900, 50)
    StopSound(832, 900, 90)
    OP_0D()
    OP_24(0x361)
    OP_24(0x35D)
    OP_24(0x39E)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c121D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1666 end

    def Function_14_3036(): pass

    label("Function_14_3036")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x442A, 0x0, 0x38D6, 0x4E20, 0x0)
    OP_96(0xFE, 0x24EA, 0x0, 0x38D6, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_14_3036 end

    def Function_15_306F(): pass

    label("Function_15_306F")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x442A, 0x0, 0x2D1E, 0x4E20, 0x0)
    OP_96(0xFE, 0x24EA, 0x0, 0x2D1E, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_15_306F end

    def Function_16_30A8(): pass

    label("Function_16_30A8")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0xCB2, 0x0, 0x3458, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    WaitChrThread(0x12, 0)
    Sound(815, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)

    def lambda_3149():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3149)
    OP_A6(0x12, 0x0, 0x32, 0x1F4, 0xBB8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 80, 0)
    OP_9D(0xFE, 0x254E, 0x0, 0x3390, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_30A8 end

    def Function_17_31A4(): pass

    label("Function_17_31A4")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrSubChip(0xFE, 0x2)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(534, 0, 100, 0)
    OP_9D(0xFE, 0x1A2C, 0x0, 0x2FA8, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x18, 0x0)

    def lambda_3256():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3256)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x14, 0xFFFFFA24, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_17_31A4 end

    def Function_18_3286(): pass

    label("Function_18_3286")


    def lambda_328B():
        OP_9D(0xFE, 0x399E, 0x0, 0x44F2, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_328B)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(815, 0, 100, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_18_3286 end

    def Function_19_3300(): pass

    label("Function_19_3300")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x1004, 0x0, 0x2BC0, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrSubChip(0xFE, 0x2)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(862, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)

    def lambda_3397():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3397)
    OP_A6(0x13, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(250, 0, 100, 0)
    OP_9D(0xFE, 0x254E, 0x0, 0x2AF8, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_3300 end

    def Function_20_33F6(): pass

    label("Function_20_33F6")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x12C0, 0x0, 0x22C4, 0x3E8, 0x1388)
    TurnDirection(0xFE, 0x18, 1000)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0x1450, 0x0, 0x2C88, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x18, 0x0)

    def lambda_34B7():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_34B7)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFF830, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_33F6 end

    def Function_21_34E7(): pass

    label("Function_21_34E7")


    def lambda_34EC():
        OP_9D(0xFE, 0x960, 0xFFFFFD44, 0xEA6, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34EC)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_21_34E7 end

    def Function_22_3561(): pass

    label("Function_22_3561")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x1004, 0x0, 0x2EAE, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(885, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)

    def lambda_35F8():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFF830, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_35F8)
    OP_A6(0x13, 0x0, 0x32, 0x1F4, 0xBB8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x2710, 0x0, 0x2EE0, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_3561 end

    def Function_23_364D(): pass

    label("Function_23_364D")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x1932, 0x0, 0x2774, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0x1770, 0x0, 0x2B2A, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x18, 0x0)

    def lambda_3707():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3707)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_23_364D end

    def Function_24_3737(): pass

    label("Function_24_3737")


    def lambda_373C():
        OP_9D(0xFE, 0x40A6, 0x0, 0xFA, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_373C)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_24_3737 end

    def Function_25_37B1(): pass

    label("Function_25_37B1")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x2)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xDAC, 0x0, 0x3426, 0x5DC, 0x2710)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(815, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 0x40)
    SetChrSubChip(0x12, 0x3)

    def lambda_3871():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3871)
    OP_A6(0x12, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Sound(844, 0, 80, 0)
    OP_9D(0xFE, 0x1482, 0x0, 0x34BC, 0x3E8, 0x2710)
    SetChrSubChip(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x2422, 0x0, 0x3778, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_37B1 end

    def Function_26_38E6(): pass

    label("Function_26_38E6")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x18CE, 0x0, 0x31CE, 0x2710, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(815, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x18, 0x0)

    def lambda_397F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_397F)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xFFEC, 0xFFFFFA24, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_26_38E6 end

    def Function_27_39AF(): pass

    label("Function_27_39AF")


    def lambda_39B4():
        OP_9D(0xFE, 0x32C8, 0xBB8, 0x4E20, 0x2B, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39B4)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3A16():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3A16)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    OP_96(0xFE, 0x32C8, 0x0, 0x4E20, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_27_39AF end

    def Function_28_3A51(): pass

    label("Function_28_3A51")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x2166, 0x0, 0x2648, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    Sound(531, 0, 80, 0)
    Sound(540, 0, 50, 0)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    SetChrPos(0x21, 8550, 0, 9800, 0)
    BeginChrThread(0x21, 3, 0, 34)
    ClearChrFlags(0x21, 0x80)
    Sound(926, 2, 100, 0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x1, 0x0, 0x21, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0x21, 0x17, 0x3E8, 0x3A98, 0x0)
    StopEffect(0x0, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    Sound(815, 0, 100, 0)
    Sound(501, 0, 100, 0)
    SetChrChipByIndex(0x17, 0x3B)
    BeginChrThread(0x17, 2, 0, 37)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3B2E():
        OP_9D(0xFE, 0xFFFFFE0C, 0x0, 0x28D2, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3B2E)
    PlayEffect(0x2, 0xFF, 0x17, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9A(0x21, 0xFE, 0x0, 0x3A98, 0x0)
    OP_24(0x39E)
    Sound(308, 0, 100, 0)
    EndChrThread(0x21, 0x3)
    SetChrFlags(0x21, 0x80)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x17, 1)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_28_3A51 end

    def Function_29_3BB1(): pass

    label("Function_29_3BB1")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    Sound(844, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x12C0, 0x0, 0x22C4, 0x3E8, 0x2710)
    OP_9D(0xFE, 0xC1C, 0x0, 0x2904, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xFE, 0x18, 1000)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    SetChrPos(0x21, 3100, 0, 10500, 0)
    BeginChrThread(0x21, 3, 0, 34)
    ClearChrFlags(0x21, 0x80)
    PlayEffect(0x1, 0x0, 0x21, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0x21, 0x18, 0x3E8, 0x2710, 0x0)
    StopEffect(0x0, 0x0)
    EndChrThread(0x18, 0x0)
    Sound(566, 0, 50, 0)

    def lambda_3C8C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3C8C)
    OP_9A(0x21, 0xFE, 0x0, 0x2710, 0x0)
    Sound(308, 0, 100, 0)
    EndChrThread(0x21, 0x3)
    SetChrFlags(0x21, 0x80)
    SetChrSubChip(0xFE, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_29_3BB1 end

    def Function_30_3CCA(): pass

    label("Function_30_3CCA")


    def lambda_3CCF():
        OP_9D(0xFE, 0xFFFFEAB6, 0xFFFFFD44, 0x6A4, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CCF)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_30_3CCA end

    def Function_31_3D44(): pass

    label("Function_31_3D44")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x1E78, 0x0, 0x3A02, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    SetChrPos(0x22, 7800, 0, 14850, 0)
    BeginChrThread(0x22, 3, 0, 34)
    ClearChrFlags(0x22, 0x80)
    PlayEffect(0x1, 0x1, 0x22, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0x22, 0x14, 0x3E8, 0x3A98, 0x0)
    StopEffect(0x1, 0x0)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x3)
    SetChrChipByIndex(0x14, 0x40)
    Sound(501, 0, 100, 0)
    BeginChrThread(0x14, 2, 0, 37)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3E03():
        OP_9D(0xFE, 0xFFFFFD12, 0x0, 0x38A4, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3E03)
    PlayEffect(0x2, 0xFF, 0x14, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9A(0x22, 0xFE, 0x0, 0x3A98, 0x0)
    EndChrThread(0x22, 0x3)
    SetChrFlags(0x22, 0x80)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_31_3D44 end

    def Function_32_3E7D(): pass

    label("Function_32_3E7D")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x14B4, 0x0, 0x3D86, 0x3E8, 0x1388)
    TurnDirection(0xFE, 0x18, 1000)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Sound(532, 0, 100, 0)
    Sound(281, 0, 70, 0)
    SetChrSubChip(0xFE, 0x1)
    SetChrPos(0x22, 5300, 0, 15750, 0)
    BeginChrThread(0x22, 3, 0, 34)
    ClearChrFlags(0x22, 0x80)
    PlayEffect(0x1, 0x1, 0x22, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0x22, 0x18, 0x3E8, 0x3A98, 0x0)
    StopEffect(0x1, 0x0)
    EndChrThread(0x18, 0x0)

    def lambda_3F44():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3F44)
    OP_9A(0x22, 0xFE, 0x0, 0x3A98, 0x0)
    Sound(308, 0, 100, 0)
    EndChrThread(0x22, 0x3)
    SetChrFlags(0x22, 0x80)
    SetChrSubChip(0xFE, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_32_3E7D end

    def Function_33_3F82(): pass

    label("Function_33_3F82")


    def lambda_3F87():
        OP_9D(0xFE, 0x1324, 0x7D0, 0x5FB4, 0xBB8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F87)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Sound(514, 0, 100, 0)
    Return()

    # Function_33_3F82 end

    def Function_34_4005(): pass

    label("Function_34_4005")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_401C")
    OP_A0(0xFE, 5000, 0x10, 0x17)
    Jump("Function_34_4005")

    label("loc_401C")

    Return()

    # Function_34_4005 end

    def Function_35_401D(): pass

    label("Function_35_401D")

    SetChrChipByIndex(0xFE, 0x39)

    label("loc_4021")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4070")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("loc_4021")

    label("loc_4070")

    Return()

    # Function_35_401D end

    def Function_36_4071(): pass

    label("Function_36_4071")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40A4")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4098")
    OP_4C(0xFE, 0x0)
    Jump("loc_409C")

    label("loc_4098")

    OP_4B(0xFE, 0x0)

    label("loc_409C")

    Sleep(500)
    Jump("Function_36_4071")

    label("loc_40A4")

    Return()

    # Function_36_4071 end

    def Function_37_40A5(): pass

    label("Function_37_40A5")

    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_37_40A5 end

    def Function_38_40FD(): pass

    label("Function_38_40FD")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_95(0xFE, 11200, 0, 12300, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x1)
    Sound(538, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x3778, 0x0, 0x2F44, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1F, 0x20)

    def lambda_4165():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4165)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_38_40FD end

    def Function_39_419E(): pass

    label("Function_39_419E")


    def lambda_41A3():

        label("loc_41A3")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_41A3")

    QueueWorkItem2(0x1F, 2, lambda_41A3)

    def lambda_41B5():

        label("loc_41B5")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_41B5")

    QueueWorkItem2(0x12, 2, lambda_41B5)
    OP_52(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0x1F, 0x558C, 0x0, 0x319C, 0x3E8, 0x2710)
    OP_52(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x3D)
    OP_99(0xFE, 0x1F, 0x3E8, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x1)
    Sound(538, 0, 100, 0)
    Sleep(50)
    SetChrFlags(0x1F, 0x20)

    def lambda_4227():
        OP_9B(0x1, 0x1F, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4227)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0x1F, 1)
    OP_A6(0x1F, 0x0, 0xA, 0x1F4, 0xBB8)
    OP_9A(0x1F, 0x12, 0x3E8, 0x2710, 0x0)
    SetChrSubChip(0x1F, 0x1)
    Sound(533, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x40)
    Sound(501, 0, 100, 0)
    BeginChrThread(0xFE, 1, 0, 37)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0x445C, 0x0, 0x32C8, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x1F, 0x0)
    Sleep(500)
    OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Sound(532, 0, 100, 0)
    Return()

    # Function_39_419E end

    def Function_40_42FA(): pass

    label("Function_40_42FA")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_96(0xFE, 0x51D6, 0xA, 0x2CEC, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x20)
    Sound(538, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x5B0E, 0xA, 0x288C, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1F, 0x20)

    def lambda_4367():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4367)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Sound(538, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x55F0, 0xA, 0x24A4, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_40_42FA end

    def Function_41_43E4(): pass

    label("Function_41_43E4")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_43E4 end

    def Function_42_43FC(): pass

    label("Function_42_43FC")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_95(0xFE, 15400, 0, 11300, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x1)
    Sound(538, 0, 100, 0)
    SetChrFlags(0x1F, 0x20)

    def lambda_4431():
        OP_9B(0x1, 0xFE, 0xFFE2, 0xFFFFF830, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4431)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_42_43FC end

    def Function_43_4471(): pass

    label("Function_43_4471")


    def lambda_4476():

        label("loc_4476")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_4476")

    QueueWorkItem2(0x1F, 2, lambda_4476)

    def lambda_4488():

        label("loc_4488")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_4488")

    QueueWorkItem2(0x13, 2, lambda_4488)
    Sound(540, 0, 100, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x523A, 0x0, 0x2D1E, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1F, 0x20)

    def lambda_44E5():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_44E5)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Sound(538, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x1)
    SetChrFlags(0xFE, 0x20)
    OP_96(0xFE, 0x5730, 0x0, 0x2EE0, 0x2710, 0x0)
    SetChrFlags(0x1F, 0x20)

    def lambda_454E():
        OP_9B(0x1, 0xFE, 0x5A, 0xFFFFF830, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_454E)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_43_4471 end

    def Function_44_4599(): pass

    label("Function_44_4599")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_9A(0xFE, 0x1F, 0x3E8, 0x1770, 0x0)
    Sound(540, 0, 100, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x1)
    SetChrFlags(0x1F, 0x20)

    def lambda_45CD():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_45CD)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_44_4599 end

    def Function_45_460D(): pass

    label("Function_45_460D")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_45_460D end

    def Function_46_4625(): pass

    label("Function_46_4625")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 70, 0)
    PlayEffect(0x8, 0x0, 0xFF, 0x0, 4500, 0, 12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_46_4625 end

    def Function_47_4684(): pass

    label("Function_47_4684")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_47_4684 end

    def Function_48_46A0(): pass

    label("Function_48_46A0")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_48_46A0 end

    def Function_49_46BC(): pass

    label("Function_49_46BC")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_49_46BC end

    def Function_50_46D8(): pass

    label("Function_50_46D8")

    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xCD, 0x8C, 0x82, 0x0, 0x5DC)
    OP_82(0x32, 0x0, 0xBB8, 0x9C4)
    Sleep(1000)
    Sound(3810, 255, 100, 0)    #voice#Sigmund
    Sound(197, 0, 100, 0)
    Sound(183, 0, 100, 0)
    Sound(881, 0, 80, 0)
    PlayEffect(0x5, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0xA, 0x5DC, 0xBB8)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(196, 0, 100, 0)
    Sound(253, 0, 100, 0)
    Sound(538, 0, 100, 0)
    Sound(3809, 255, 100, 0)    #voice#Sigmund
    PlayEffect(0x4, 0x1, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x5)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    CancelBlur(1000)
    SetChrSubChip(0xFE, 0x4)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    Sound(833, 0, 100, 0)
    OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x3E8)
    Sleep(1000)
    Return()

    # Function_50_46D8 end

    def Function_51_485E(): pass

    label("Function_51_485E")

    SetChrChipByIndex(0x18, 0x26)
    OP_95(0x18, 19200, 0, 14450, 3000, 0x0)
    OP_95(0x18, 19200, 0, 19500, 3000, 0x0)
    Sound(893, 0, 100, 0)
    SetChrChipByIndex(0x18, 0x25)
    OP_A1(0x18, 0x7D0, 0x5, 0x0, 0x0, 0x0, 0x1, 0x2)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(196, 0, 80, 0)
    Sound(880, 0, 80, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    SetMapObjFlags(0x4, 0x4)
    Sleep(500)
    SetChrChipByIndex(0x18, 0x26)

    def lambda_48DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_48DF)

    def lambda_48F0():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_48F0)
    Return()

    # Function_51_485E end

    def Function_52_4901(): pass

    label("Function_52_4901")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_7D(0xCD, 0x8C, 0x82, 0x0, 0x0)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(196, 0, 100, 0)
    Sound(253, 0, 100, 0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x4, 0x1, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x5)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    CancelBlur(1000)
    SetChrSubChip(0xFE, 0x4)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    Sound(833, 0, 100, 0)
    OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x3E8)
    Sleep(1000)
    Return()

    # Function_52_4901 end

    def Function_53_49DC(): pass

    label("Function_53_49DC")


    def lambda_49E1():
        OP_95(0xFE, -22000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49E1)

    def lambda_49FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_49FB)
    WaitChrThread(0xFE, 1)

    def lambda_4A10():
        OP_95(0xFE, -22000, 0, -14500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A10)
    WaitChrThread(0xFE, 1)

    def lambda_4A2E():
        OP_95(0xFE, -19300, 0, -12200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A2E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_53_49DC end

    def Function_54_4A4F(): pass

    label("Function_54_4A4F")

    Sleep(600)

    def lambda_4A57():
        OP_95(0xFE, -22000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A57)

    def lambda_4A71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A71)
    WaitChrThread(0xFE, 1)

    def lambda_4A86():
        OP_95(0xFE, -22000, 0, -14500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A86)
    WaitChrThread(0xFE, 1)

    def lambda_4AA4():
        OP_95(0xFE, -19300, 0, -13300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4AA4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_54_4A4F end

    def Function_55_4AC5(): pass

    label("Function_55_4AC5")

    Sleep(1200)

    def lambda_4ACD():
        OP_95(0xFE, -22000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4ACD)

    def lambda_4AE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4AE7)
    WaitChrThread(0xFE, 1)

    def lambda_4AFC():
        OP_95(0xFE, -22000, 0, -14500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4AFC)
    WaitChrThread(0xFE, 1)

    def lambda_4B1A():
        OP_95(0xFE, -20500, 0, -12700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B1A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_55_4AC5 end

    def Function_56_4B3B(): pass

    label("Function_56_4B3B")

    Sleep(100)

    def lambda_4B43():
        OP_95(0xFE, -18000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B43)

    def lambda_4B5D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4B5D)
    WaitChrThread(0xFE, 1)

    def lambda_4B72():
        OP_95(0xFE, -18000, 0, -13300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B72)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_56_4B3B end

    def Function_57_4B93(): pass

    label("Function_57_4B93")

    Sleep(700)

    def lambda_4B9B():
        OP_95(0xFE, -18000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B9B)

    def lambda_4BB5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BB5)
    WaitChrThread(0xFE, 1)

    def lambda_4BCA():
        OP_95(0xFE, -17000, 0, -14100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BCA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_57_4B93 end

    def Function_58_4BEB(): pass

    label("Function_58_4BEB")

    Sleep(1300)

    def lambda_4BF3():
        OP_95(0xFE, -18000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BF3)

    def lambda_4C0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C0D)
    WaitChrThread(0xFE, 1)

    def lambda_4C22():
        OP_95(0xFE, -18000, 0, -14300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C22)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_58_4BEB end

    def Function_59_4C43(): pass

    label("Function_59_4C43")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -20500, 100, -17800, 270)
    SetChrPos(0x102, -20500, 100, -17800, 270)
    SetChrPos(0x103, -19500, 100, -17800, 90)
    SetChrPos(0x104, -20500, 100, -17800, 270)
    SetChrPos(0x109, -19500, 100, -17800, 90)
    SetChrPos(0x105, -19500, 100, -17800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SoundLoad(868)
    Sound(868, 2, 100, 0)
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "kurotuki00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "knuki", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lwindow2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ent2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bfire00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bfire01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x1, 0x1)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    ClearChrFlags(0x20, 0x80)
    OP_78(0x12, 0x20)
    OP_49()
    SetChrPos(0x20, -20000, 0, -41000, 0)
    OP_D5(0x20, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0xB5, 0xF0, 0x1, 0x20)
    VolumeBGM(0x64, 0x3E8)
    OP_68(-5000, 1000, 0, 0)
    MoveCamera(45, 11, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(25500, 0)
    MoveCamera(30, 11, 0, 7000)
    SetCameraDistance(30500, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(22150, 2500, 20700, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27000, 0)
    SetCameraDistance(23000, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-20000, 1900, -31000, 0)
    MoveCamera(45, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(24500, 0)
    OP_68(-20000, 1500, -18300, 3500)
    MoveCamera(45, 27, 0, 3500)
    SetCameraDistance(14500, 3500)
    Sound(459, 0, 100, 0)
    Sound(493, 0, 100, 0)

    def lambda_4FED():
        OP_96(0xFE, 0xFFFFB1E0, 0x0, 0xFFFFB9B0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4FED)
    Sleep(2000)
    Sound(492, 0, 100, 0)
    WaitChrThread(0x20, 1)
    OP_71(0x12, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x12)
    OP_6F(0x79)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    Sound(462, 0, 100, 0)
    OP_71(0x12, 0x1, 0x1E, 0x1, 0x0)
    OP_79(0x12)
    OP_68(-20000, 1900, -14300, 3000)
    BeginChrThread(0x101, 3, 0, 53)
    BeginChrThread(0x102, 3, 0, 54)
    BeginChrThread(0x103, 3, 0, 57)
    BeginChrThread(0x104, 3, 0, 55)
    BeginChrThread(0x109, 3, 0, 56)
    BeginChrThread(0x105, 3, 0, 58)
    WaitChrThread(0x101, 3)

    #C0043
    ChrTalk(
        0x101,
        "#5P#00010F唔……『黑月』的房子……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)

    #C0044
    ChrTalk(
        0x105,
        (
            "#12P#10306F不必担心，曹那伙人\x01",
            "是不会被轻易干掉的。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        (
            "#6P#00307F没时间磨蹭了……\x01",
            "我们赶快去ＩＢＣ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "兰迪在一定期间内\x01",
            "强制加入参战队伍。\x02\x03",

            "请从现在的参战队伍中\x01",
            "选择一名要换下的角色。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51D1")
    MenuCmd(1, 0, "将瓦吉替换为援护队员")

    label("loc_51D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51FD")
    MenuCmd(1, 0, "将诺艾尔替换为援护队员")

    label("loc_51FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5229")
    MenuCmd(1, 0, "将罗伊德替换为援护队员")

    label("loc_5229")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5253")
    MenuCmd(1, 0, "将艾莉替换为援护队员")

    label("loc_5253")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_527D")
    MenuCmd(1, 0, "将缇欧替换为援护队员")

    label("loc_527D")

    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_52CB"),
        (1, "loc_53ED"),
        (2, "loc_550F"),
        (3, "loc_5631"),
        (SWITCH_DEFAULT, "loc_5753"),
    )


    label("loc_52CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5304")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5304")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5304")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_533D")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_533D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_533D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5376")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5376")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5376")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53AF")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53AF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53E8")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53E8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53E8")

    Jump("loc_5753")

    label("loc_53ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5426")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5426")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5426")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_545F")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_545F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_545F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5498")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5498")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5498")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54D1")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54D1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_54D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_550A")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_550A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_550A")

    Jump("loc_5753")

    label("loc_550F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5548")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5548")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5548")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5581")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5581")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5581")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55BA")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55BA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F3")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_562C")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_562C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_562C")

    Jump("loc_5753")

    label("loc_5631")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_566A")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_566A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_566A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56A3")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56A3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56DC")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56DC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5715")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5715")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5715")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_574E")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_574E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_574E")

    Jump("loc_5753")

    label("loc_5753")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (4, "loc_577B"),
        (8, "loc_5795"),
        (0, "loc_57AE"),
        (1, "loc_57C7"),
        (2, "loc_57E0"),
        (SWITCH_DEFAULT, "loc_57F9"),
    )


    label("loc_577B")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    OP_49()
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_57F9")

    label("loc_5795")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_57F9")

    label("loc_57AE")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x0, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x0, 0xFF, 0xFF)
    Jump("loc_57F9")

    label("loc_57C7")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x1, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_57F9")

    label("loc_57E0")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x2, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_57F9")

    label("loc_57F9")

    SetChrPos(0x0, -20000, 0, -14000, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x20, -18200, 0, -19000, 0)
    ClearMapObjFlags(0x12, 0x1000)
    OP_70(0x12, 0x0)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFF, 0x0)
    OP_66(0x1, 0x1)
    SetScenarioFlags(0x180, 0)
    OP_29(0xAB, 0x4, 0x2)
    OP_29(0xAB, 0x1, 0x0)
    ModifyEventFlags(1, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_59_4C43 end

    def Function_60_5877(): pass

    label("Function_60_5877")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_589B")
    RemoveParty(0x4, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5926")

    label("loc_589B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58BF")
    RemoveParty(0x8, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5926")

    label("loc_58BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58E3")
    RemoveParty(0x0, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5926")

    label("loc_58E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5907")
    RemoveParty(0x1, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5926")

    label("loc_5907")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5926")
    RemoveParty(0x2, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5926")

    Return()

    # Function_60_5877 end

    def Function_61_5927(): pass

    label("Function_61_5927")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_593F")
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_599A")

    label("loc_593F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5957")
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_599A")

    label("loc_5957")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_596F")
    AddParty(0x0, 0xFF, 0xFF)
    Jump("loc_599A")

    label("loc_596F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5987")
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_599A")

    label("loc_5987")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_599A")
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_599A")

    Return()

    # Function_61_5927 end

    def Function_62_599B(): pass

    label("Function_62_599B")

    EventBegin(0x0)
    Fade(500)
    OP_68(4500, 2900, 23200, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 4000, 2000, 23200, 0)
    SetChrPos(0x102, 5000, 2000, 23200, 0)
    SetChrPos(0x103, 3000, 2000, 22200, 0)
    SetChrPos(0x104, 6000, 2000, 22200, 0)
    SetChrPos(0x109, 5500, 2000, 21200, 0)
    SetChrPos(0x105, 3500, 2000, 21200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sound(878, 0, 100, 0)
    Sleep(200)
    Sound(871, 0, 40, 0)
    Sleep(200)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(4500, 4900, 32200, 3000)
    MoveCamera(15, 7, 0, 3000)
    Sleep(1000)
    StopSound(868, 2000, 80)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 0)
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_62_599B end

    def Function_63_5B3B(): pass

    label("Function_63_5B3B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch27700.itc", 0x1E)
    LoadChrToIndex("chr/ch32800.itc", 0x1F)
    LoadChrToIndex("chr/ch28100.itc", 0x20)
    LoadChrToIndex("chr/ch29400.itc", 0x21)
    SetChrPos(0x101, 4300, 2000, 21100, 0)
    SetChrPos(0x102, 5100, 2000, 20500, 0)
    SetChrPos(0x103, 2700, 2000, 20700, 45)
    SetChrPos(0x104, 6700, 2000, 21000, 315)
    SetChrPos(0x109, 7300, 2000, 22600, 315)
    SetChrPos(0x105, 1500, 2000, 21200, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 2100, 2000, 23000, 180)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6800, 2000, 23800, 180)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    OP_90(0xA, 4900, 5120, 38700, 180)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    OP_90(0xB, 3900, 5120, 38900, 180)
    SetChrChipByIndex(0xC, 0x0)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 1000, 2000, 24300, 180)
    SetChrChipByIndex(0xD, 0x0)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 5100, 2000, 22800, 180)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 5700, 2000, 24300, 180)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 3800, 2000, 22700, 180)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 3700, 2000, 25100, 180)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 2100, 2000, 24400, 180)
    OP_68(4500, 2900, 23200, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(18500, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0047
    ChrTalk(
        0x101,
        "#12P#00007F大家都没事吧！？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        "#00307F#12P到底发生了什么事！？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xF,
        "#5P该、该从何说起才好……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x10,
        (
            "#5P一群持枪的家伙突然闯了进去，\x01",
            "命令我们离开大楼……！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#5P他们转瞬之间就破坏了那道\x01",
            "用特殊合金制造的防护门……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xD,
        (
            "#5P『赤色星座』……虽然听说过他们的\x01",
            "危险度是Ｓ级，但没想到竟然这么……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)

    #N0053
    NpcTalk(
        0xB,
        "少年的声音",
        "#4P是、是你们！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(4500, 3900, 31200, 0)
    MoveCamera(1, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(4740, 2900, 22650, 4000)
    MoveCamera(1, 24, 0, 4000)
    SetCameraDistance(16700, 4000)

    def lambda_5F1F():
        OP_96(0xFE, 0xE10, 0x7D0, 0x5DC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5F1F)

    def lambda_5F39():
        OP_96(0xFE, 0x17D4, 0x7D0, 0x6338, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5F39)

    def lambda_5F53():
        OP_96(0xFE, 0x1644, 0x7D0, 0x5EEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5F53)

    def lambda_5F6D():
        OP_96(0xFE, 0xC80, 0x7D0, 0x620C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5F6D)
    BeginChrThread(0xA, 3, 0, 64)
    Sleep(100)
    BeginChrThread(0xB, 3, 0, 65)
    Sleep(3000)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)
    OP_95(0x103, 3060, 2000, 21430, 2000, 0x0)

    #C0054
    ChrTalk(
        0x103,
        (
            "#6P#00202F约纳、主任……\x01",
            "你们都没事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        "#11P呼……呼……总算逃出来了。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        (
            "#11P冰、冰冷冷的枪\x01",
            "突然就顶在了我的身上……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "#02311F#5P那、那些家伙远比\x01",
            "情报上形容的可怕啊！\x02\x03",

            "#02310F尤其那个红头发的大叔……\x01",
            "那是他们的首领吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0058
    ChrTalk(
        0x101,
        "#6P#00007F首领……！\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        "#00310F#12P『赤色战鬼』吗！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xB,
        (
            "#02307F#5P嗯！\x01",
            "那个大叔简直就像怪物一样！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#12P#00107F贝尔呢……！？\x01",
            "贝尔逃出来了吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 500)
    Sleep(100)

    #C0062
    ChrTalk(
        0x9,
        (
            "#11P大、大小姐正好\x01",
            "去米修拉姆视察了……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        "#11P因此逃过一劫呢！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(100)

    #C0064
    ChrTalk(
        0x102,
        "#6P#00106F是、是吗……太好了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0065
    ChrTalk(
        0x105,
        (
            "#5P#10303F看来他们把所有\x01",
            "民间人士都放出来了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0066
    ChrTalk(
        0x109,
        (
            "#10110F#11P他们究竟有\x01",
            "什么企图呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#00301F#12P猜不到……\x01",
            "但总有极度不祥的预感。\x02\x03",

            "#00307F总之，我们赶快过去吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#6P#00007F嗯……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 500)
    Sleep(100)

    #C0069
    ChrTalk(
        0x102,
        (
            "#12P#00107F东街那边比较安全！\x02\x03",

            "请大家到那里\x01",
            "请求协会帮助！\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xD,
        "#11P知、知道了！\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x5A, 0x1F4)

    #C0071
    ChrTalk(
        0xC,
        (
            "#5P我来为各位带路，\x01",
            "请大家跟紧我！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 2720, 2000, 23920, 0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1310, 2000, 24540, 0)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 7330, 2000, 22520, 0)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 5930, 2000, 23920, 0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_37()
    SetChrPos(0x0, 4500, 2000, 21000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x180, 1)
    ModifyEventFlags(0, 0, 0x80)
    OP_10(0x6, 0x1)
    OP_10(0x1, 0x0)
    Sleep(1000)
    EventEnd(0x5)
    Return()

    # Function_63_5B3B end

    def Function_64_649E(): pass

    label("Function_64_649E")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_64B5():
        OP_95(0xFE, 4900, 2000, 22700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_64B5)
    WaitChrThread(0xA, 1)
    SetChrFlags(0xA, 0x4)
    OP_64(0xFE)
    OP_93(0xA, 0xB4, 0x1F4)
    Return()

    # Function_64_649E end

    def Function_65_64DE(): pass

    label("Function_65_64DE")

    Sleep(100)
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_64F8():
        OP_95(0xFE, 4400, 2000, 23900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_64F8)
    WaitChrThread(0xB, 1)

    def lambda_6516():
        OP_95(0xFE, 3900, 2000, 22900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6516)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xB, 0x4)
    OP_64(0xFE)
    OP_93(0xB, 0xB4, 0x1F4)
    Return()

    # Function_65_64DE end

    def Function_66_653F(): pass

    label("Function_66_653F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6855")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 21780, 0, 14720, 0)
    SetChrPos(0x102, 23710, 0, 14820, 0)
    SetChrPos(0x103, 22300, 0, 13530, 0)
    SetChrPos(0x104, 19210, 0, 15090, 15)
    SetChrPos(0x105, 20060, 0, 14060, 15)
    SetChrPos(0x109, 20890, 0, 13130, 0)
    OP_68(20970, 1600, 15970, 0)
    MoveCamera(36, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19850, 0)
    OP_0D()
    Sleep(1000)

    #C0072
    ChrTalk(
        0x101,
        "#12P#00001F黑月贸易公司被彻底破坏了……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x104,
        (
            "#6P#00301F从现场状况来看，\x01",
            "肯定是叔叔他们干的。\x02\x03",

            "#00303F这种火药味……\x01",
            "正是『赤色星座』\x01",
            "所使用的那种炸药。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x109,
        (
            "#12P#10101F和以前在旧矿山使用\x01",
            "的炸药好像是同一类别呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x105,
        (
            "#6P#10303F没有发现曹\x01",
            "和其他成员。\x02\x03",

            "#10301F看来他们已经顺利逃脱，\x01",
            "并没有遇害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        (
            "#12P#00108F但从现场的惨状来看，\x01",
            "恐怕并没有全身而退……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#12P#00203F说起来，『银』……\x01",
            "莉夏小姐没事吧？\x02\x03",

            "#00202F今天正好是彩虹剧团\x01",
            "新版舞剧的公演日。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#12P#00003F……虽然很令人担心，\x01",
            "但我们现在没时间去确认了。\x02\x03",

            "#00001F尽快赶往ＩＢＣ吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 21780, 0, 14720, 0)
    SetScenarioFlags(0x190, 2)
    EventEnd(0x5)
    Jump("loc_68AE")

    label("loc_6855")

    TalkBegin(0xFF)

    #C0079
    ChrTalk(
        0x101,
        (
            "#00003F……曹他们应该\x01",
            "不会被轻易干掉。\x02\x03",

            "#00001F我们现在还是尽快赶往ＩＢＣ吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_68AE")

    Return()

    # Function_66_653F end

    def Function_67_68AF(): pass

    label("Function_67_68AF")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A0A")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_6935")
    MenuCmd(1, 0, "在导力车内休息")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6935")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6985")

    #C0080
    ChrTalk(
        0x101,
        (
            "#00001F没时间了，\x01",
            "我们尽快赶往ＩＢＣ吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A05")

    label("loc_6985")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69FB")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_69BE")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_69D6")

    label("loc_69BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_69D1")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_69D6")

    label("loc_69D1")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_69D6")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A05")

    label("loc_69FB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A05")

    Jump("loc_68CE")

    label("loc_6A0A")

    SetMapObjFrame(0x12, "light", 0x1, 0x1)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_67_68AF end

    def Function_68_6A20(): pass

    label("Function_68_6A20")

    EventBegin(0x1)

    #C0081
    ChrTalk(
        0x101,
        (
            "#00001F没时间了，\x01",
            "我们尽快赶往ＩＢＣ吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -20180, 0, -24790, 0)
    EventEnd(0x4)
    Return()

    # Function_68_6A20 end

    def Function_69_6A65(): pass

    label("Function_69_6A65")

    EventBegin(0x1)

    #C0082
    ChrTalk(
        0x101,
        (
            "#00001F没时间了，\x01",
            "我们尽快赶往ＩＢＣ吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -25280, 2000, 23520, 89)
    EventEnd(0x4)
    Return()

    # Function_69_6A65 end

    def Function_70_6AAA(): pass

    label("Function_70_6AAA")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0083
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

    # Function_70_6AAA end

    SaveToFile()

Try(main)
