from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c140d.bin",                # FileName
        "c140d",                    # MapName
        "c140d",                    # Location
        0x002E,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\x1c\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c140d",                  # 0
        "帕欧拉婆婆",             # 1
        "王",                     # 2
        "露茜",                   # 3
        "卡农",                   # 4
        "迪诺",                   # 5
        "坦特斯老人",             # 6
        "巴克斯",                 # 7
        "利玛",                   # 8
        "梅尔斯",                 # 9
        "琴兹",                   # 10
        "贝赛",                   # 11
        "阿巴斯",                 # 12
        "修伊",                   # 13
        "斯拉修",                 # 14
        "良",                     # 15
        "亚泽尔",                 # 16
        "瓦鲁多",                 # 17
        "中央广场",               # 18
        "西街",                   # 19
        "行政区",                 # 20
        "住宅街",                 # 21
        "欢乐街",                 # 22
        "东街",                   # 23
        "旧城区",                 # 24
        "港湾区",                 # 25
        "ＩＢＣ",                 # 26
        "站前街道",               # 27
        "后巷",                   # 28
        "乌尔斯拉间道",           # 29
        "东克洛斯贝尔街道",       # 30
        "西克洛斯贝尔街道",       # 31
        "玛因兹山道",             # 32
        "兰花塔",                 # 33
    ))

    AddCharChip((
        "chr/ch31800.itc",                   # 00
        "chr/ch30900.itc",                   # 01
        "chr/ch06700.itc",                   # 02
        "chr/ch23800.itc",                   # 03
        "chr/ch23300.itc",                   # 04
        "chr/ch23000.itc",                   # 05
        "chr/ch24700.itc",                   # 06
        "chr/ch06800.itc",                   # 07
        "chr/ch24000.itc",                   # 08
        "chr/ch23302.itc",                   # 09
        "chr/ch20700.itc",                   # 0A
        "chr/ch26200.itc",                   # 0B
        "chr/ch23400.itc",                   # 0C
        "apl/ch50375.itc",                   # 0D
        "chr/ch30800.itc",                   # 0E
        "chr/ch31700.itc",                   # 0F
    ))

    DeclNpc(15449,   100,     -19,     270,  261,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(9640,    0,       850,     180,  261,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(10279,   0,       -550,    315,  261,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(34080,   -6500,   -38270,  45,   261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(44880,   -2500,   -20090,  225,  261,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4269,    0,       -52159,  90,   389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(32799,   -6500,   -36950,  315,  389,  0x0, 0,   12,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(10270,   3500,    11050,   135,  389,  0x0, 0,   10,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(9609,    3500,    13869,   135,  389,  0x0, 0,   11,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(18700,   4000,    -8210,   315,  389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(1779,    0,       -5260,   90,   389,  0x0, 0,   14,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   13,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(27560,   -1410,   -16129,  1200,    27560,   -410,    -16129,  0x007C, 0,  29, 0x0000)
    DeclActor(45450,   -2500,   -19950,  1200,    45450,   -1500,   -19950,  0x007C, 0,  30, 0x0000)
    DeclActor(11700,   -6450,   -32850,  1200,    11700,   -5450,   -32850,  0x007C, 0,  31, 0x0000)
    DeclActor(-16450,  0,       -9550,   1200,    -16450,  1000,    -9550,   0x007C, 0,  32, 0x0000)
    DeclActor(17410,   -6500,   -35760,  1200,    17410,   -5500,   -35760,  0x007C, 0,  33, 0x0000)
    DeclActor(-16690,  -3110,   -26340,  1200,    -16050,  -2080,   -26200,  0x007C, 0,  34, 0x0000)
    DeclActor(15480,   0,       310,     1200,    14350,   1000,    -550,    0x007C, 0,  35, 0x0000)
    DeclActor(37750,   -6500,   -38500,  1200,    37750,   -5500,   -38500,  0x007C, 0,  40, 0x0000)
    DeclActor(-27350,  2800,    -28500,  1200,    -27350,  3800,    -28500,  0x007C, 0,  41, 0x0000)
    DeclActor(48220,   200,     -38420,  1200,    48220,   1200,    -38420,  0x007C, 0,  42, 0x0000)
    DeclActor(-1780,   -4300,   -31780,  1200,    -1780,   -3300,   -31780,  0x007C, 0,  36, 0x0000)
    DeclActor(39750,   -2500,   -17530,  1200,    39750,   -1500,   -17530,  0x007C, 0,  37, 0x0000)
    DeclActor(8109,    0,       -8220,   1200,    8109,    1000,    -8220,   0x007C, 0,  38, 0x0000)
    DeclActor(42230,   -2500,   -25220,  1200,    42230,   -1500,   -25220,  0x007C, 0,  39, 0x0000)
    DeclActor(47720,   -1100,   -33160,  1200,    47720,   100,     -33160,  0x007C, 0,  5,  0x0000)
    DeclActor(38560,   -6500,   -31160,  1200,    38560,   -4900,   -31160,  0x007C, 0,  6,  0x0000)

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "中央广场")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "西街")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "行政区")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "住宅街")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "欢乐街")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "东街")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "旧城区")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "站前街道")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "后巷")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-238.0500030517578, 0.0, 225.39999389648438, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-88.0, 0.0, 360.0, 0x0000, 0x0000, "兰花塔")
    PlaceName(-135.99000549316406, 0.0, 90.8499984741211, 0x0000, 0x0051, "")
    PlaceName(-74.18000030517578, 0.0, 120.75, 0x0000, 0x0054, "")
    PlaceName(-107.80999755859375, 0.0, 81.6500015258789, 0x0000, 0x0057, "")
    PlaceName(-136.85000610351562, 0.0, 124.19999694824219, 0x0000, 0x0053, "")
    PlaceName(-113.27999877929688, 0.0, 151.8000030517578, 0x0000, 0x0053, "")
    PlaceName(-171.63999938964844, 0.0, 118.44999694824219, 0x0000, 0x0053, "")
    PlaceName(-182.85000610351562, 0.0, 142.60000610351562, 0x0000, 0x0053, "")
    PlaceName(-155.25, 0.0, 179.39999389648438, 0x0000, 0x0052, "")
    PlaceName(-149.7899932861328, 0.0, 164.4499969482422, 0x0000, 0x0053, "")
    PlaceName(-139.72999572753906, 0.0, 154.67999267578125, 0x0000, 0x0053, "")
    PlaceName(-106.94999694824219, 0.0, 236.3300018310547, 0x0000, 0x0051, "")
    PlaceName(21.850000381469727, 0.0, 80.5, 0x0000, 0x0052, "")
    PlaceName(2.299999952316284, 0.0, -23.579999923706055, 0x0000, 0x0053, "")
    PlaceName(-12.649999618530273, 0.0, -2.299999952316284, 0x0000, 0x0053, "")

    ChipFrameInfo(2308, 0)                                       # 0

    ScpFunction((
        "Function_0_904",          # 00, 0
        "Function_1_9B4",          # 01, 1
        "Function_2_9DF",          # 02, 2
        "Function_3_A0A",          # 03, 3
        "Function_4_D63",          # 04, 4
        "Function_5_F50",          # 05, 5
        "Function_6_108B",         # 06, 6
        "Function_7_1136",         # 07, 7
        "Function_8_1381",         # 08, 8
        "Function_9_1487",         # 09, 9
        "Function_10_1532",        # 0A, 10
        "Function_11_15E0",        # 0B, 11
        "Function_12_1818",        # 0C, 12
        "Function_13_1BC9",        # 0D, 13
        "Function_14_1D59",        # 0E, 14
        "Function_15_1F10",        # 0F, 15
        "Function_16_2041",        # 10, 16
        "Function_17_2309",        # 11, 17
        "Function_18_2310",        # 12, 18
        "Function_19_25E8",        # 13, 19
        "Function_20_26A1",        # 14, 20
        "Function_21_2802",        # 15, 21
        "Function_22_2876",        # 16, 22
        "Function_23_28C4",        # 17, 23
        "Function_24_291A",        # 18, 24
        "Function_25_2B0A",        # 19, 25
        "Function_26_3BC5",        # 1A, 26
        "Function_27_3BDB",        # 1B, 27
        "Function_28_405A",        # 1C, 28
        "Function_29_4C3E",        # 1D, 29
        "Function_30_4C93",        # 1E, 30
        "Function_31_4CE8",        # 1F, 31
        "Function_32_4D3D",        # 20, 32
        "Function_33_4D92",        # 21, 33
        "Function_34_4DE7",        # 22, 34
        "Function_35_4E3C",        # 23, 35
        "Function_36_4E91",        # 24, 36
        "Function_37_4EE6",        # 25, 37
        "Function_38_4F3B",        # 26, 38
        "Function_39_4F90",        # 27, 39
        "Function_40_4FE5",        # 28, 40
        "Function_41_503A",        # 29, 41
        "Function_42_508F",        # 2A, 42
        "Function_43_50E4",        # 2B, 43
        "Function_44_53C4",        # 2C, 44
        "Function_45_5791",        # 2D, 45
        "Function_46_60CE",        # 2E, 46
        "Function_47_60F7",        # 2F, 47
        "Function_48_6134",        # 30, 48
        "Function_49_616E",        # 31, 49
        "Function_50_61A8",        # 32, 50
    ))


    def Function_0_904(): pass

    label("Function_0_904")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_93C"),
        (1, "loc_948"),
        (2, "loc_954"),
        (3, "loc_960"),
        (4, "loc_96C"),
        (5, "loc_978"),
        (6, "loc_984"),
        (SWITCH_DEFAULT, "loc_990"),
    )


    label("loc_93C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_948")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_954")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_960")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_96C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_978")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_984")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_990")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_99C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_9B3")

    Return()

    # Function_0_904 end

    def Function_1_9B4(): pass

    label("Function_1_9B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9DE")
    OP_94(0xFE, 0xFFFF8C06, 0xFFFF9F48, 0xFFFF9552, 0xFFFF88E6, 0x3E8)
    Sleep(300)
    Jump("Function_1_9B4")

    label("loc_9DE")

    Return()

    # Function_1_9B4 end

    def Function_2_9DF(): pass

    label("Function_2_9DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A09")
    OP_94(0xFE, 0x8D04, 0xFFFF6E7E, 0x7800, 0xFFFF612C, 0x3E8)
    Sleep(300)
    Jump("Function_2_9DF")

    label("loc_A09")

    Return()

    # Function_2_9DF end

    def Function_3_A0A(): pass

    label("Function_3_A0A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE7")
    SetChrPos(0x0, 2050, 0, 14590, 180)
    SetChrPos(0x1, 2050, 0, 14590, 180)
    SetChrPos(0x2, 2050, 0, 14590, 180)
    SetChrPos(0x3, 2050, 0, 14590, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A91")
    SetChrPos(0x4, 2050, 0, 14590, 180)
    SetChrPos(0x5, 2050, 0, 14590, 180)
    Jump("loc_AB0")

    label("loc_A91")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB0")
    SetChrPos(0x4, 2050, 0, 14590, 180)

    label("loc_AB0")

    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AE7")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x9)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B79")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 2800, 0, -4440, 270)
    BeginChrThread(0x16, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 1100, 0, -4440, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 590, 0, -6640, 135)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -28960, 2800, -28390, 315)
    BeginChrThread(0xE, 0, 0, 1)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_D26")

    label("loc_B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BA0")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_D26")

    label("loc_BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BE7")
    SetChrPos(0xB, 8290, 0, -1190, 45)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0x9, 9640, 0, 850, 180)
    SetChrPos(0xA, 10280, 0, -550, 315)
    Jump("loc_D26")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D26")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C64")
    SetChrPos(0x11, -200, 0, -8460, 180)
    SetChrPos(0x12, 30390, -2500, -21970, 0)
    SetChrPos(0x10, 6500, 0, 5410, 0)
    SetChrPos(0xF, 5490, 0, 5600, 0)
    Jump("loc_CD9")

    label("loc_C64")

    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 2520, -10, -4059, 225)
    SetChrPos(0x11, 2120, -10, -6060, 315)
    SetChrPos(0x12, 310, -10, -4250, 90)
    SetChrPos(0x17, 10930, 0, -3700, 90)
    SetChrPos(0x10, 6500, 0, 5410, 0)
    SetChrPos(0xF, 5490, 0, 5600, 0)
    SetChrFlags(0xF, 0x10)

    label("loc_CD9")

    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 34490, -6500, -37750, 315)
    SetChrPos(0xA, 34490, -6500, -38950, 315)
    SetChrPos(0xB, 34840, -2220, -19610, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D26")
    SetChrFlags(0xB, 0x10)

    label("loc_D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D3A")
    ClearScenarioFlags(0x22, 0)
    Event(0, 24)
    Jump("loc_D62")

    label("loc_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_D4E")
    ClearScenarioFlags(0x22, 1)
    Event(0, 25)
    Jump("loc_D62")

    label("loc_D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_D62")
    ClearScenarioFlags(0x22, 2)
    SetMapFlags(0x10000000)
    Event(0, 45)

    label("loc_D62")

    Return()

    # Function_3_A0A end

    def Function_4_D63(): pass

    label("Function_4_D63")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    OP_65(0x9, 0x1)
    OP_65(0xA, 0x1)
    OP_65(0xB, 0x1)
    OP_65(0xC, 0x1)
    OP_65(0xD, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x375, 0x0)"), scpexpr(EXPR_END)), "loc_DDF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDF")
    LoadEffect(0x7, "event/ev10016.eff")

    label("loc_DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFA")
    ClearMapObjFlags(0x7, 0x4)

    label("loc_DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_E2F")
    SetMapObjFrame(0xFF, "koge2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kenzai", 0x1, 0x1)
    SetMapObjFrame(0xFF, "blue", 0x1, 0x1)
    Jump("loc_E8B")

    label("loc_E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E64")
    SetMapObjFrame(0xFF, "koge2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kenzai", 0x1, 0x1)
    SetMapObjFrame(0xFF, "blue", 0x1, 0x1)
    Jump("loc_E8B")

    label("loc_E64")

    SetMapObjFrame(0xFF, "koge2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kenzai", 0x0, 0x1)
    SetMapObjFrame(0xFF, "blue", 0x0, 0x1)

    label("loc_E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F08")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x6E, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F38")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x24, 0x8C, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4B")
    OP_70(0x5, 0x0)
    Jump("loc_F4F")

    label("loc_F4B")

    OP_70(0x5, 0x1E)

    label("loc_F4F")

    Return()

    # Function_4_D63 end

    def Function_5_F50(): pass

    label("Function_5_F50")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1042")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3D, 1)"), scpexpr(EXPR_END)), "loc_FD3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_103D")

    label("loc_FD3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_103D")

    Jump("loc_107F")

    label("loc_1042")

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

    label("loc_107F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F50 end

    def Function_6_108B(): pass

    label("Function_6_108B")

    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着《用烤箱制作正式料理》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_1132")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1132")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『精力牛排』\x07\x00",
            "的食谱已经记录下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1132")

    TalkEnd(0xFF)
    Return()

    # Function_6_108B end

    def Function_7_1136(): pass

    label("Function_7_1136")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1293")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1228")

    #C0006
    ChrTalk(
        0xFE,
        (
            "呜～嗝……\x01",
            "酒果然是世上最好的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "……话说回来，那棵大得吓人\x01",
            "的树是怎么回事……？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00006F（好、好危险啊，\x01",
            "  竟然在这种地方醉倒……）\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#00300F（算啦，我也能理解\x01",
            "  他这种时候想喝酒的心情。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_128E")

    label("loc_1228")


    #C0010
    ChrTalk(
        0xFE,
        (
            "呜～嗝……\x01",
            "那棵大得吓人的树\x01",
            "难道是天国的植物吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "天国中一定有\x01",
            "无数美酒和\x01",
            "可爱的小姐吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128E")

    Jump("loc_137D")

    label("loc_1293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12A1")
    Jump("loc_137D")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_12AF")
    Jump("loc_137D")

    label("loc_12AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_137D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D7")
    Call(0, 8)
    Jump("loc_132F")

    label("loc_12D7")


    #C0012
    ChrTalk(
        0xFE,
        (
            "真是的，虽说管饭，\x01",
            "但竟然要从白天开始干活。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "赶快把工作搞定，\x01",
            "然后去喝一杯吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132F")

    Jump("loc_137D")

    label("loc_1334")


    #C0014
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "阳光还真是刺眼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "我这种昼伏夜出的人还真是不适应。\x02",
    )

    CloseMessageWindow()

    label("loc_137D")

    TalkEnd(0xFE)
    Return()

    # Function_7_1136 end

    def Function_8_1381(): pass

    label("Function_8_1381")

    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0x9, 0x0, 0)

    #C0016
    ChrTalk(
        0x9,
        (
            "呀哈哈哈，爸爸竟然\x01",
            "在白天工作，太少见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "听说是因为遭到了大家的训斥，\x01",
            "如果再不出来帮忙，\x01",
            "就要被赶出公寓了～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xE, 0x9, 0)

    #C0018
    ChrTalk(
        0xE,
        (
            "喂！王！\x01",
            "不要说那种没用的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xE,
        "赶快闭嘴，过来帮我干活。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_93(0x9, 0x13B, 0x0)
    OP_93(0xE, 0x13B, 0x0)
    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_8_1381 end

    def Function_9_1487(): pass

    label("Function_9_1487")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D1")

    #C0020
    ChrTalk(
        0xFE,
        (
            "好，今天也要\x01",
            "努力工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "首先要测量尺寸……\x02",
    )

    CloseMessageWindow()
    Jump("loc_152E")

    label("loc_14D1")


    #C0022
    ChrTalk(
        0xFE,
        (
            "呼，虽然进展比预计要慢些，\x01",
            "但总算顺利完工，可以喘口气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "好……下午也要继续努力！\x02",
    )

    CloseMessageWindow()

    label("loc_152E")

    TalkEnd(0xFE)
    Return()

    # Function_9_1487 end

    def Function_10_1532(): pass

    label("Function_10_1532")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157B")

    #C0024
    ChrTalk(
        0xFE,
        "爸爸正在为大家努力工作呢。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "是不是很帅～¤\x02",
    )

    CloseMessageWindow()
    Jump("loc_15DC")

    label("loc_157B")

    OP_4B(0x10, 0x0)
    SetChrName("利玛")

    #C0026
    ChrTalk(
        0xF,
        "爸爸，这个汤真好喝！\x02",
    )

    CloseMessageWindow()
    SetChrName("梅尔斯")

    #C0027
    ChrTalk(
        0x10,
        (
            "嗯，是啊，爸爸喝了以后\x01",
            "也感觉全身都是力量。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0x0)

    label("loc_15DC")

    TalkEnd(0xFE)
    Return()

    # Function_10_1532 end

    def Function_11_15E0(): pass

    label("Function_11_15E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16EF")

    #C0028
    ChrTalk(
        0x13,
        (
            "#04100F……对了，机会难得，\x01",
            "把这个给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『阿巴斯的账号』\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 0)
    OP_E4(0x3)

    #C0030
    ChrTalk(
        0x101,
        (
            "#00005F『波波碰！』的账号……？\x01",
            "阿巴斯，你也在玩这个吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x13,
        (
            "#04100F只在有空的时候玩玩而已。\x02\x03",

            "如有兴趣，我可以当你的对手，\x01",
            "尽管向我挑战吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1814")

    label("loc_16EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BD")

    #C0032
    ChrTalk(
        0x13,
        (
            "#04100F特别任务支援科……\x01",
            "你们今天真是帮了大忙。\x02\x03",

            "多亏你们，重建工作进展得很顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#00100F呵呵，不用客气。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x105,
        (
            "#10300F阿巴斯，你们接下来\x01",
            "还要继续加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x13,
        "#04100F嗯，当然。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1814")

    label("loc_17BD")


    #C0036
    ChrTalk(
        0x13,
        (
            "#04100F嗯，必要的材料\x01",
            "已经基本收集到了。\x02\x03",

            "在天黑之前，一定要集中精神，\x01",
            "努力工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1814")

    TalkEnd(0xFE)
    Return()

    # Function_11_15E0 end

    def Function_12_1818(): pass

    label("Function_12_1818")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18DA")

    #C0037
    ChrTalk(
        0xFE,
        (
            "发生了相当惊人\x01",
            "的事情啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "看到那棵蓝白色的大树之后，\x01",
            "我就觉得自己必须要\x01",
            "做一些力所能及的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "至少也要把街道打扫得干净一些，\x01",
            "让大家的心情放松些。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1934")

    label("loc_18DA")


    #C0040
    ChrTalk(
        0xFE,
        (
            "既然已经下定决心了，\x01",
            "就要努力把街道打扫干净。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "只要努力，\x01",
            "就一定能迎来好结果的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1934")

    Jump("loc_1BC5")

    label("loc_1939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1947")
    Jump("loc_1BC5")

    label("loc_1947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_197E")

    #C0042
    ChrTalk(
        0xFE,
        (
            "战、战争……\x01",
            "千万不要发生那种事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC5")

    label("loc_197E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BC5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BA")
    Call(0, 27)
    Return()

    label("loc_19BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A43")
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
            "对话\x01",              # 0
            "交出废弃材料\x01",      # 1
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
        (0, "loc_1A32"),
        (1, "loc_1A37"),
        (SWITCH_DEFAULT, "loc_1A43"),
    )


    label("loc_1A32")

    Jump("loc_1A43")

    label("loc_1A37")

    Call(0, 43)
    TalkEnd(0xB)
    Return()

    label("loc_1A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA0")

    #C0043
    ChrTalk(
        0xFE,
        (
            "（翻来翻去）……\x01",
            "嗯？这个……不是呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "那这个……\x01",
            "唔～这个也不是呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC5")

    label("loc_1AA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B22")

    #C0045
    ChrTalk(
        0xB,
        (
            "大哥哥，你们能\x01",
            "帮我寻找含有\x01",
            "金属的废弃材料吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "虽然我已经找过一遍了，\x01",
            "但应该还有\x01",
            "没发现的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6A")

    label("loc_1B22")


    #C0047
    ChrTalk(
        0xFE,
        "大哥哥，谢谢你们。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "我会去把这些\x01",
            "废弃材料卖掉，\x01",
            "换一些资金的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6A")

    Jump("loc_1BC5")

    label("loc_1B6F")


    #C0049
    ChrTalk(
        0xFE,
        (
            "好，已经把肚子\x01",
            "彻底填饱了，\x01",
            "还要继续加油工作啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "大哥哥，\x01",
            "谢谢你们\x01",
            "帮忙哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC5")

    TalkEnd(0xFE)
    Return()

    # Function_12_1818 end

    def Function_13_1BC9(): pass

    label("Function_13_1BC9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7C")

    #C0051
    ChrTalk(
        0xFE,
        (
            "那棵又大又漂亮的树\x01",
            "到底是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "闪耀着蓝白色的光芒……\x01",
            "美得简直不像是\x01",
            "这个世界的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "那棵大树能不能\x01",
            "把我们引领到\x01",
            "女神的身边呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1CE4")

    label("loc_1C7C")


    #C0054
    ChrTalk(
        0xFE,
        (
            "那棵又大又漂亮的树……\x01",
            "美得简直不像是\x01",
            "这个世界的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "它能不能\x01",
            "把我们引领到\x01",
            "女神的身边呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE4")

    Jump("loc_1D55")

    label("loc_1CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1CF7")
    Jump("loc_1D55")

    label("loc_1CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1D55")

    #C0056
    ChrTalk(
        0xFE,
        (
            "虽然我不是很明白，\x01",
            "但好像发生了\x01",
            "很严重的事态呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "看来暂时还是\x01",
            "别出门为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D55")

    TalkEnd(0xFE)
    Return()

    # Function_13_1BC9 end

    def Function_14_1D59(): pass

    label("Function_14_1D59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1DDA")

    #C0058
    ChrTalk(
        0xFE,
        (
            "爸爸不喝酒的时候\x01",
            "总是说些肉麻的话，\x01",
            "所以我干脆去给他买了些酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "……还是让这个差劲老爸一直喝下去吧～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1DE8")
    Jump("loc_1F0C")

    label("loc_1DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E44")

    #C0060
    ChrTalk(
        0xFE,
        (
            "嘿嘿，市区里好像\x01",
            "发生了很严重的骚乱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "有人说，也许会\x01",
            "发生战争呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1F0C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6C")
    Call(0, 8)
    Jump("loc_1EA1")

    label("loc_1E6C")


    #C0062
    ChrTalk(
        0xFE,
        (
            "哈哈哈，今天的老爸简直\x01",
            "就像个认真工作的正经人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA1")

    Jump("loc_1F0C")

    label("loc_1EA6")


    #C0063
    ChrTalk(
        0xFE,
        (
            "嘿嘿，今天的伙食\x01",
            "也很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "要是每天都能吃上那样的饭菜，\x01",
            "就算一直做什么重建工作都没问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F0C")

    TalkEnd(0xFE)
    Return()

    # Function_14_1D59 end

    def Function_15_1F10(): pass

    label("Function_15_1F10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F8A")

    #C0065
    ChrTalk(
        0xFE,
        (
            "王竟然主动去给他爸爸买酒喝，\x01",
            "真是稀奇啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "何必去买嘛，酒鬼叔叔难得\x01",
            "认真起来，多有趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_203D")

    label("loc_1F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F98")
    Jump("loc_203D")

    label("loc_1F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1FC5")

    #C0067
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "那肯定很不妙吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_203D")

    label("loc_1FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_203D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2008")

    #C0068
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "没想到王的爸爸\x01",
            "那么能干。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_203D")

    label("loc_2008")


    #C0069
    ChrTalk(
        0xFE,
        (
            "晚上还会再管\x01",
            "一顿饭呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "到时能吃到什么呢？\x02",
    )

    CloseMessageWindow()

    label("loc_203D")

    TalkEnd(0xFE)
    Return()

    # Function_15_1F10 end

    def Function_16_2041(): pass

    label("Function_16_2041")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2131")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20FB")

    #C0071
    ChrTalk(
        0xFE,
        (
            "杰德前辈他们\x01",
            "终于肯来帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……虽然发生了那样的事情，\x01",
            "但对我们来说，瓦鲁多大哥\x01",
            "永远都是最重要的头领。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "你们……一定要想办法\x01",
            "把他带回来啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_212C")

    label("loc_20FB")


    #C0074
    ChrTalk(
        0xFE,
        (
            "你们……一定要想办法\x01",
            "把瓦鲁多大哥带回来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_212C")

    Jump("loc_2305")

    label("loc_2131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_213F")
    Jump("loc_2305")

    label("loc_213F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2305")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229D")

    #C0075
    ChrTalk(
        0xFE,
        "啊，你们是特别任务支援科的……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        (
            "#00108F迪诺……\x01",
            "请问，其他成员现在……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "嗯？啊……\x01",
            "伤情最重的寇奇前辈\x01",
            "也总算苏醒过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "至于其他前辈，也有几位已经出院，\x01",
            "回到了旧城区。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "虽然他们肯定不会\x01",
            "马上返回组织……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "不过，只要我一直在这里等，\x01",
            "他们总有一天会露面的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        "#00103F迪诺……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00008F嗯……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 2)
    Jump("loc_2305")

    label("loc_229D")


    #C0083
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "从一大早开始，市区那边就很吵闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "听说一直在讨论什么独立，\x01",
            "真希望他们能安静些。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2305")

    TalkEnd(0xFE)
    Return()

    # Function_16_2041 end

    def Function_17_2309(): pass

    label("Function_17_2309")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_17_2309 end

    def Function_18_2310(): pass

    label("Function_18_2310")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CE")
    SetScenarioFlags(0x191, 6)

    #C0085
    ChrTalk(
        0x17,
        (
            "啊，特别任务支援科的各位，\x01",
            "今天真是谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x17,
        (
            "猪骨汤还有剩下的，\x01",
            "你们再拿走一些吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 4)), scpexpr(EXPR_END)), "loc_23D6")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0087
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x21A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x21A, 6)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    Jump("loc_241E")

    label("loc_23D6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0088
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x21B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x21B, 6)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()

    label("loc_241E")


    #C0089
    ChrTalk(
        0x101,
        (
            "#00000F谢谢，\x01",
            "那我们就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        (
            "#10104F这猪骨汤\x01",
            "真是很美味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        (
            "#00200F嗯，一想到还能再喝到，\x01",
            "实在是很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x17,
        (
            "哈哈，能让你们这么说，\x01",
            "我们就算没白做啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E4")

    label("loc_24CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2570")

    #C0093
    ChrTalk(
        0x17,
        (
            "难得有这么好的猪骨汤，\x01",
            "不然也给姐姐和尤格特\x01",
            "送去一些吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x17,
        (
            "啊，不过这是给参与\x01",
            "重建工作的人喝的。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x17,
        (
            "有了！可以让他们\x01",
            "过来帮忙洗衣服。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_25E4")

    label("loc_2570")


    #C0096
    ChrTalk(
        0x17,
        (
            "难得有这么好的猪骨汤，\x01",
            "不然也给姐姐和尤格特\x01",
            "送去一些吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x17,
        (
            "他们两个今天好像都很闲，\x01",
            "过来帮些忙\x01",
            "应该没问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E4")

    TalkEnd(0xFE)
    Return()

    # Function_18_2310 end

    def Function_19_25E8(): pass

    label("Function_19_25E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2645")

    #C0098
    ChrTalk(
        0xFE,
        (
            "呼，现场作业\x01",
            "果然很消耗体力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "不过这也是一种\x01",
            "很不错的锻炼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_269D")

    label("loc_2645")


    #C0100
    ChrTalk(
        0xFE,
        (
            "嗯，接下来的工作\x01",
            "好像都是更累人的体力活呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "贝赛那家伙不要紧吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_269D")

    TalkEnd(0xFE)
    Return()

    # Function_19_25E8 end

    def Function_20_26A1(): pass

    label("Function_20_26A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273C")

    #C0102
    ChrTalk(
        0x12,
        (
            "说、说起来……\x01",
            "这座公寓被毁得\x01",
            "真、真够彻底啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x12,
        (
            "还好是一座废弃公寓，\x01",
            "要、要是里面还有人住的话……\x01",
            "光是想想就觉得毛骨悚然啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27FE")

    label("loc_273C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AC")

    #C0104
    ChrTalk(
        0x12,
        "……嗝。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x12,
        (
            "因为可以随便添饭……\x01",
            "我、我一不注意就吃多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x12,
        (
            "真、真应该\x01",
            "节制些啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27FE")

    label("loc_27AC")


    #C0107
    ChrTalk(
        0x12,
        (
            "要、要是用力，说不定会把\x01",
            "胃里的东西都吐出来……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x12,
        (
            "真、真应该\x01",
            "节制些啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FE")

    TalkEnd(0xFE)
    Return()

    # Function_20_26A1 end

    def Function_21_2802(): pass

    label("Function_21_2802")

    TalkBegin(0xFE)

    #C0109
    ChrTalk(
        0xFE,
        (
            "我们正在和圣书会的\x01",
            "蓝衣小子联手巡逻。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "哼，要是有人敢在\x01",
            "这旧城区乱来，\x01",
            "我们一定会好好教训他们一顿。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2802 end

    def Function_22_2876(): pass

    label("Function_22_2876")

    TalkBegin(0xFE)

    #C0111
    ChrTalk(
        0xFE,
        (
            "那棵巨大的树\x01",
            "到底是怎么出现的呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        "哇哇，真是搞不懂啊～！！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2876 end

    def Function_23_28C4(): pass

    label("Function_23_28C4")

    TalkBegin(0xFE)

    #C0113
    ChrTalk(
        0xFE,
        (
            "只要在双方的地盘上好好警戒，\x01",
            "应该就可以放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        "好，再去巡逻一圈吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_28C4 end

    def Function_24_291A(): pass

    label("Function_24_291A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -200, 0, -8460, 180)
    SetChrPos(0x12, 30390, -2500, -21970, 0)
    SetChrPos(0x10, 6500, 0, 5410, 0)
    SetChrPos(0xF, 5490, 0, 5600, 0)
    SetChrPos(0x9, 34490, -6500, -37750, 315)
    SetChrPos(0xA, 34490, -6500, -38950, 315)
    SetChrPos(0xB, 34840, -2220, -19610, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_68(32850, -500, -17050, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13250, 0)
    MoveCamera(45, 25, 0, 7000)
    SetCameraDistance(25250, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(32780, -3600, -36810, 0)
    MoveCamera(19, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22320, 0)
    OP_68(32780, -5600, -36810, 5000)
    Sleep(4000)
    Fade(500)
    OP_68(2750, 2000, 4750, 0)
    MoveCamera(55, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_68(-2300, 2000, -8850, 8000)
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_291A end

    def Function_25_2B0A(): pass

    label("Function_25_2B0A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02100.itc", 0x1E)
    LoadChrToIndex("chr/ch30950.itc", 0x20)
    LoadChrToIndex("chr/ch31850.itc", 0x21)
    LoadChrToIndex("apl/ch51601.itc", 0x22)
    LoadChrToIndex("apl/ch51602.itc", 0x23)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis269.itp")
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 17200, -6500, -37400, 0)
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 50000, -2100, -22700, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    EndChrThread(0xC, 0xFF)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 7300, 0, -4300, 180)
    EndChrThread(0x11, 0xFF)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 5900, 0, -3800, 180)
    EndChrThread(0x12, 0xFF)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 8700, 0, -3300, 180)
    EndChrThread(0x16, 0xFF)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 7300, 0, -2800, 180)
    EndChrThread(0x17, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 7300, 0, -4300, 180)
    EndChrThread(0x11, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    OP_63(0x18, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-11350, 2000, -25280, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18590, 0)
    OP_68(7460, 2000, -46280, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_68(17200, -4500, -36400, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(18000, 1000)
    Sleep(1000)
    OP_64(0x18)
    Sleep(500)
    OP_92(0x18, 0x5334, 0xFFFF6DE8, 0x190)
    Sleep(300)

    def lambda_2DD3():
        OP_95(0xFE, 20640, -6500, -36460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2DD3)
    WaitChrThread(0x18, 1)

    def lambda_2DF1():
        OP_95(0xFE, 21800, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2DF1)
    Sleep(2500)
    Fade(500)
    OP_68(22060, -500, -22520, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    MoveCamera(45, 21, 0, 5000)
    SetCameraDistance(17000, 5000)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x2D, 0x190)
    OP_6F(0x79)
    Sleep(300)
    OP_63(0x18, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x18)
    Sleep(500)
    OP_93(0x18, 0x5A, 0x190)

    def lambda_2E87():
        OP_95(0xFE, 41800, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2E87)
    Sleep(2500)
    Fade(500)
    OP_68(35300, -900, -22650, 0)
    MoveCamera(57, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22000, 0)
    OP_68(45300, -900, -22650, 7500)
    MoveCamera(57, 13, 0, 7500)
    SetCameraDistance(19000, 7500)
    WaitChrThread(0x18, 1)
    OP_6F(0x79)
    Sleep(300)

    #C0115
    ChrTalk(
        0x18,
        "#01601F#30W#5P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x18, 0x20)
    Sleep(500)

    #C0116
    ChrTalk(
        0x18,
        "#01608F#30W#5P…………可恶………………\x02",
    )

    CloseMessageWindow()

    #N0117
    NpcTalk(
        0xC,
        "少年的声音",
        "#30W#2S#5P……瓦鲁多……大哥……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x10)
    ClearChrFlags(0x18, 0x2)
    ClearChrFlags(0x18, 0x20)

    def lambda_3017():
        OP_95(0xFE, 47600, -2100, -22700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3017)

    def lambda_3031():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3031)
    WaitChrThread(0xC, 1)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0118
    ChrTalk(
        0x18,
        "#01605F#5P迪诺……你……\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        "#11P瓦、瓦鲁多大哥……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0120
    ChrTalk(
        0xC,
        "#4S#11P真的是瓦鲁多大哥！！\x02",
    )

    CloseMessageWindow()
    OP_68(42200, -1100, -22700, 1500)
    MoveCamera(53, 20, 0, 1300)
    SetCameraDistance(17000, 1300)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3107():
        OP_95(0xFE, 42600, -2100, -22700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3107)
    WaitChrThread(0xC, 1)
    Sound(812, 0, 50, 0)
    OP_6F(0x79)
    Sleep(300)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0121
    ChrTalk(
        0xC,
        (
            "#2P您这段时间到底去什么地方了……！\x01",
            "我真的很担心您啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xC,
        (
            "#2P不、不过，幸好您平安无事……\x01",
            "……呜呜呜呜呜呜呜……！\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x18,
        "#5P#01601F#30W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xC,
        (
            "#2P前、前辈们都受了\x01",
            "很重的伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xC,
        (
            "#2P虽然有些人已经出院了，\x01",
            "但大家都没有再回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xC,
        (
            "#2P不、不过，不要紧的！\x01",
            "只要有瓦鲁多大哥在，就一定……！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x18,
        "#5P#01608F………呜……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0x1)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x18, 0x20)
    Sleep(500)
    SetChrSubChip(0x18, 0x2)
    OP_68(43040, -1100, -22830, 500)
    SetCameraDistance(16149, 500)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    Sound(815, 0, 50, 0)
    Sound(802, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 26)

    def lambda_3310():
        OP_9D(0xFE, 0xAB7C, 0xFFFFF7CC, 0xFFFFA754, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3310)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(862, 0, 30, 0)

    #C0128
    ChrTalk(
        0xC,
        "#11P哇……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 3)

    def lambda_335C():
        OP_A6(0xFE, 0x0, 0x32, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_335C)
    Sleep(300)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    SetChrSubChip(0xC, 0x4)

    #C0129
    ChrTalk(
        0xC,
        "#60W#2S瓦鲁多……大哥……？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x10)
    ClearChrFlags(0x18, 0x2)
    ClearChrFlags(0x18, 0x20)
    OP_93(0x18, 0x10E, 0x1F4)
    Sleep(300)

    #C0130
    ChrTalk(
        0x18,
        (
            "#11P#01603F#30W……剑蛇帮从此解散。\x02\x03",

            "#01608F你以后也别再……\x01",
            "像个跟屁虫一样跟着我。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    #C0131
    ChrTalk(
        0xC,
        "#50W#2S……您是在……开玩笑吧……？\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xC,
        "#50W#2S瓦鲁多大哥……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        (
            "#50W#2S……瓦鲁多大哥可是……\x01",
            "我们最信赖的优秀首领……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(30200, -1100, -22700, 9000)
    MoveCamera(65, 11, 0, 9000)
    OP_6E(550, 9000)
    SetCameraDistance(19000, 9000)

    def lambda_34E4():
        OP_95(0xFE, 17000, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_34E4)
    Sleep(500)
    SetChrSubChip(0xC, 0x5)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(230, 10, -1, -1)

    #A0134
    AnonymousTalk(
        0xC,
        (
            "#57A……那个怪物……\x01",
            "那个把大家打得惨不忍睹的怪物\x01",
            "怎么可能是瓦鲁多大哥！\x02",
        )
    )
    #Auto

    Sleep(5700)
    OP_82(0xC8, 0x0, 0xBB8, 0x7D0)
    SetMessageWindowPos(230, 20, -1, -1)

    #A0135
    AnonymousTalk(
        0xC,
        "#23A#4S那是骗人的吧！？\x02",
    )
    #Auto

    Sleep(2500)
    OP_57(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x18, 0x1)
    OP_6F(0x79)
    Sleep(1000)
    SetChrFlags(0xC, 0x80)
    OP_68(9600, 1100, -13300, 0)
    MoveCamera(100, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    OP_90(0x18, 14100, -1000, -17800, 315)

    def lambda_3605():
        OP_95(0xFE, 9600, 0, -13300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3605)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x18, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #N0136
    NpcTalk(
        0x11,
        "青年的声音",
        "站、站住……唔！\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(805, 0, 100, 0)
    Sound(318, 0, 40, 0)
    OP_68(7850, 1100, -6000, 2500)
    MoveCamera(35, 21, 0, 2500)
    SetCameraDistance(17000, 2500)

    def lambda_36A5():
        OP_95(0xFE, 8400, 0, -8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_36A5)
    WaitChrThread(0x18, 1)
    OP_6F(0x79)

    #C0137
    ChrTalk(
        0x11,
        (
            "#5P瓦鲁多·瓦雷斯！\x01",
            "没、没想到你还敢回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x12,
        (
            "#5P绝不容许你在这\x01",
            "旧城区继续肆意妄为……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x12,
        "#5P我们无论如何也会阻止你的……\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x18,
        "#11P#01600F………………………………\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x11,
        (
            "#5P……你到底\x01",
            "想干什么……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x11,
        (
            "#5P竟、竟然变成那样的怪物，\x01",
            "把旧城区破坏得惨不忍睹……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x17,
        (
            "还把那些如此敬爱着\x01",
            "你的手下给……！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x16,
        "#5P太、太过分了……！\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x18,
        (
            "#11P#01604F哼……\x02\x03",

            "#01602F告诉我，\x01",
            "瓦吉和那个秃头在什么地方？\x02\x03",

            "他们原本就是外来的家伙……\x01",
            "现在已经夹着尾巴逃走了吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0xFA)

    #C0146
    ChrTalk(
        0x11,
        "#5P别、别开玩笑了……！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x12,
        (
            "#5P他们两人一定\x01",
            "会回来的……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0148
    ChrTalk(
        0x18,
        "#11P#01605F什么……？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x16,
        (
            "#5P他、他们有任务在身！\x01",
            "那是必须要完成的使命！\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x16,
        (
            "#5P就算暂时离开城市，\x01",
            "迟早也会回来的！\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x17,
        (
            "虽然不知道那是什么使命……\x01",
            "但我们都相信他们二位！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x18)
    Fade(250)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0x3)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x18, 0x20)
    OP_0D()

    def lambda_39E8():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_39E8)
    WaitChrThread(0x18, 2)
    Sleep(500)

    def lambda_3A08():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3A08)
    WaitChrThread(0x18, 2)
    Sleep(500)

    #C0152
    ChrTalk(
        0x18,
        "#11P#01604F#50W………哼哼……哈哈……………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0153
    ChrTalk(
        0x18,
        "#11P#01609F#5S哈哈哈哈哈哈哈哈哈哈！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(8189, 1200, -8180, 0)
    MoveCamera(166, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16370, 0)
    SetCameraDistance(15370, 1000)
    SetChrSubChip(0x18, 0x4)
    OP_0D()
    OP_6F(0x79)

    #C0154
    ChrTalk(
        0x18,
        (
            "#5P#01604F原来如此……『使命』吗……\x02\x03",

            "看样子，那时候的事情\x01",
            "似乎还可以继续啊……？\x02\x03",

            "#01602F没错吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    MoveCamera(166, 32, 0, 4000)
    SetCameraDistance(25500, 4000)
    SetChrSubChip(0x18, 0x5)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x7D0)

    #C0155
    ChrTalk(
        0x18,
        "#5P#5S#35W#27A#01607F瓦吉！！！！！！\x02",
    )
    #Auto

    Sleep(1700)
    OP_57(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 5)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_2B0A end

    def Function_26_3BC5(): pass

    label("Function_26_3BC5")

    Sleep(120)
    SetChrSubChip(0xC, 0x1)
    WaitChrThread(0xC, 1)
    SetChrSubChip(0xC, 0x2)
    Sound(811, 0, 100, 0)
    Return()

    # Function_26_3BC5 end

    def Function_27_3BDB(): pass

    label("Function_27_3BDB")

    EventBegin(0x0)
    Fade(500)
    OP_68(34400, -500, -21490, 0)
    MoveCamera(45, 38, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19700, 0)
    SetChrPos(0x101, 35030, -2500, -20920, 0)
    SetChrPos(0x102, 34200, -2500, -21240, 0)
    SetChrPos(0x103, 36000, -2500, -21200, 0)
    SetChrPos(0x104, 35080, -2500, -22190, 0)
    SetChrPos(0x105, 33890, -2500, -22230, 0)
    SetChrPos(0x109, 36510, -2500, -22110, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_93(0xB, 0x0, 0x0)
    OP_0D()

    #C0156
    ChrTalk(
        0xB,
        "嗯，这个……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        "……不是。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        "这个……也不是。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "唔，真伤脑筋啊。\x01",
            "再这样下去，就来不及完成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#00000F你在做什么呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0161
    ChrTalk(
        0xB,
        (
            "哦……\x01",
            "我正在帮阿巴斯先生\x01",
            "给废弃材料分类。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "如果发现含有金属的废弃材料，\x01",
            "可以卖到废品回收处\x01",
            "换些钱。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#00305F哦～原来如此。\x02\x03",

            "#00304F旧城区的居民\x01",
            "还真会精打细算啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x105,
        (
            "#10304F这种事情是很普通的。\x02\x03",

            "#10300F旧城区的居民们\x01",
            "全都拥有为了生存\x01",
            "而倾尽全力的信念。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        (
            "#00200F这就是所谓的\x01",
            "『穷人家的孩子早当家』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x109,
        (
            "#10103F唔……我们实在是\x01",
            "学不来呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#00102F这也正是此地居民\x01",
            "的坚强之处呢。\x02\x03",

            "#00100F……对了，有什么事情\x01",
            "需要我们帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        "帮忙……啊，对了。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        (
            "如果可以，\x01",
            "能不能帮我在这旧城区\x01",
            "寻找含有金属的废弃材料？\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "虽然我已经找过一遍了，\x01",
            "但应该还有\x01",
            "没发现的。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#00000F含有金属的废弃材料吗……\x01",
            "明白了，交给我们吧。\x02\x03",

            "#00003F（为了保证寻找效率，\x01",
            "  最好能找个金属探测器\x01",
            "  之类的东西……）\x02\x03",

            "#00000F（去问问\x01",
            "  基约姆师傅吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x196, 4)
    OP_29(0x8E, 0x1, 0x6)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_93(0xB, 0x0, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 34840, -2500, -21110, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_3BDB end

    def Function_28_405A(): pass

    label("Function_28_405A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4135")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40E7")
    TalkBegin(0xFF)

    #C0172
    ChrTalk(
        0x101,
        (
            "#00000F废弃材料已经收集完毕。\x02\x03",

            "该做的事情都做完了，\x01",
            "我们去向阿巴斯报告吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_40E7")

    TalkBegin(0xFF)

    #C0173
    ChrTalk(
        0x101,
        (
            "#00000F废弃材料已经收集完毕。\x02\x03",

            "去看看还有什么事情需要我们帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_4135")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_415A")
    Return()

    label("loc_415A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE4E5A8), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_420C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6BA8), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3F01), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_420C")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_420C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xB18A), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4DEE), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42A4")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_42A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_433C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2DB4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8052), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_433C")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_433C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4042), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x254E), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43D5")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_446D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4402), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8BB0), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_446D")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_446D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4506")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4132), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x66E4), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4506")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_459E")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3C78), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x136), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_459E")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_459E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4636")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9376), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9664), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4636")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46CF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6AD6), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6F54), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46CF")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4767")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xBC5C), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9614), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4767")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4800")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6F4), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7C24), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4800")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4898")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9B46), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x447A), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4898")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4930")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1FAD), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x201C), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4930")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49C8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xA4F6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6284), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49C8")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49C8")

    SetMapFlags(0x80)
    OP_C7(0x0, 0x0)
    OP_49()
    Sleep(30)
    PlayEffect(0x7, 0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(632, 0, 100, 0)
    Sleep(600)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B50")
    TalkBegin(0xFF)
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_64(0x0)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_64(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4ACA"),
        (2, "loc_4AD3"),
        (3, "loc_4ADC"),
        (4, "loc_4AE5"),
        (5, "loc_4AEE"),
        (6, "loc_4AF7"),
        (7, "loc_4B00"),
        (8, "loc_4B09"),
        (9, "loc_4B12"),
        (10, "loc_4B1B"),
        (11, "loc_4B24"),
        (12, "loc_4B2D"),
        (13, "loc_4B36"),
        (14, "loc_4B3F"),
        (SWITCH_DEFAULT, "loc_4B48"),
    )


    label("loc_4ACA")

    OP_66(0x0, 0x1)
    Jump("loc_4B48")

    label("loc_4AD3")

    OP_66(0x1, 0x1)
    Jump("loc_4B48")

    label("loc_4ADC")

    OP_66(0x2, 0x1)
    Jump("loc_4B48")

    label("loc_4AE5")

    OP_66(0x3, 0x1)
    Jump("loc_4B48")

    label("loc_4AEE")

    OP_66(0x4, 0x1)
    Jump("loc_4B48")

    label("loc_4AF7")

    OP_66(0x5, 0x1)
    Jump("loc_4B48")

    label("loc_4B00")

    OP_66(0x6, 0x1)
    Jump("loc_4B48")

    label("loc_4B09")

    OP_66(0x7, 0x1)
    Jump("loc_4B48")

    label("loc_4B12")

    OP_66(0x8, 0x1)
    Jump("loc_4B48")

    label("loc_4B1B")

    OP_66(0x9, 0x1)
    Jump("loc_4B48")

    label("loc_4B24")

    OP_66(0xA, 0x1)
    Jump("loc_4B48")

    label("loc_4B2D")

    OP_66(0xB, 0x1)
    Jump("loc_4B48")

    label("loc_4B36")

    OP_66(0xC, 0x1)
    Jump("loc_4B48")

    label("loc_4B3F")

    OP_66(0xD, 0x1)
    Jump("loc_4B48")

    label("loc_4B48")

    TalkEnd(0xFF)
    Jump("loc_4C37")

    label("loc_4B50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_4BA7")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "极近位置有反应！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_4C37")

    label("loc_4BA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x186A0), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_4BFA")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "附近有反应！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_4C37")

    label("loc_4BFA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "没有反应。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4C37")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_28_405A end

    def Function_29_4C3E(): pass

    label("Function_29_4C3E")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0177
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x196, 6)
    TalkEnd(0xFF)
    Return()

    # Function_29_4C3E end

    def Function_30_4C93(): pass

    label("Function_30_4C93")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0178
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x1, 0x1)
    SetScenarioFlags(0x196, 7)
    TalkEnd(0xFF)
    Return()

    # Function_30_4C93 end

    def Function_31_4CE8(): pass

    label("Function_31_4CE8")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0179
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x38E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x2, 0x1)
    SetScenarioFlags(0x197, 0)
    TalkEnd(0xFF)
    Return()

    # Function_31_4CE8 end

    def Function_32_4D3D(): pass

    label("Function_32_4D3D")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0180
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x197, 1)
    TalkEnd(0xFF)
    Return()

    # Function_32_4D3D end

    def Function_33_4D92(): pass

    label("Function_33_4D92")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0181
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x197, 2)
    TalkEnd(0xFF)
    Return()

    # Function_33_4D92 end

    def Function_34_4DE7(): pass

    label("Function_34_4DE7")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0182
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x5, 0x1)
    SetScenarioFlags(0x197, 3)
    TalkEnd(0xFF)
    Return()

    # Function_34_4DE7 end

    def Function_35_4E3C(): pass

    label("Function_35_4E3C")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0183
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x6, 0x1)
    SetScenarioFlags(0x197, 4)
    TalkEnd(0xFF)
    Return()

    # Function_35_4E3C end

    def Function_36_4E91(): pass

    label("Function_36_4E91")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0184
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xA, 0x1)
    SetScenarioFlags(0x19C, 0)
    TalkEnd(0xFF)
    Return()

    # Function_36_4E91 end

    def Function_37_4EE6(): pass

    label("Function_37_4EE6")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0185
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xB, 0x1)
    SetScenarioFlags(0x19C, 1)
    TalkEnd(0xFF)
    Return()

    # Function_37_4EE6 end

    def Function_38_4F3B(): pass

    label("Function_38_4F3B")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0186
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xC, 0x1)
    SetScenarioFlags(0x19C, 2)
    TalkEnd(0xFF)
    Return()

    # Function_38_4F3B end

    def Function_39_4F90(): pass

    label("Function_39_4F90")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0187
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xD, 0x1)
    SetScenarioFlags(0x19C, 3)
    TalkEnd(0xFF)
    Return()

    # Function_39_4F90 end

    def Function_40_4FE5(): pass

    label("Function_40_4FE5")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0188
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x38E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x7, 0x1)
    SetScenarioFlags(0x197, 5)
    TalkEnd(0xFF)
    Return()

    # Function_40_4FE5 end

    def Function_41_503A(): pass

    label("Function_41_503A")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0189
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x38E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x8, 0x1)
    SetScenarioFlags(0x197, 6)
    TalkEnd(0xFF)
    Return()

    # Function_41_503A end

    def Function_42_508F(): pass

    label("Function_42_508F")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0190
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "取得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x38E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x9, 0x1)
    SetScenarioFlags(0x197, 7)
    TalkEnd(0xFF)
    Return()

    # Function_42_508F end

    def Function_43_50E4(): pass

    label("Function_43_50E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5182")

    #C0191
    ChrTalk(
        0xB,
        (
            "哇……\x01",
            "你们帮我找到了这么多\x01",
            "含有金属的废弃材料吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xB,
        (
            "呵呵，好厉害啊，\x01",
            "竟然有这么多，真开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "可以把这些废弃材料\x01",
            "交给我吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5316")

    label("loc_5182")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5209")

    #C0194
    ChrTalk(
        0xB,
        (
            "你们帮我找到了\x01",
            "含有金属的废弃材料吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        (
            "呵呵，谢谢，\x01",
            "有这些就足够啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "可以把这些废弃材料\x01",
            "交给我吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5316")

    label("loc_5209")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5282")

    #C0197
    ChrTalk(
        0xB,
        (
            "你们帮我找到了\x01",
            "含有金属的废弃材料吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "好像找到了不少呢……\x01",
            "可以把这些废弃材料\x01",
            "交给我吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5316")

    label("loc_5282")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5316")

    #C0199
    ChrTalk(
        0xB,
        (
            "你们帮我找到了\x01",
            "含有金属的废弃材料吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xB,
        (
            "虽然数量有些少……\x01",
            "但这份心意还是很让我开心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        (
            "可以把这些废弃材料\x01",
            "交给我吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5316")

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
            "交出废弃材料\x01",      # 0
            "继续寻找\x01",          # 1
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
        (0, "loc_537C"),
        (1, "loc_5384"),
        (SWITCH_DEFAULT, "loc_53C3"),
    )


    label("loc_537C")

    Call(0, 44)
    Jump("loc_53C3")

    label("loc_5384")


    #C0202
    ChrTalk(
        0xB,
        "啊，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        (
            "那就等你们\x01",
            "收集完之后\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C3")

    label("loc_53C3")

    Return()

    # Function_43_50E4 end

    def Function_44_53C4(): pass

    label("Function_44_53C4")

    EventBegin(0x0)
    Fade(500)
    OP_68(34400, -500, -21490, 0)
    MoveCamera(45, 38, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19700, 0)
    SetChrPos(0x101, 35030, -2500, -20920, 0)
    SetChrPos(0x102, 34200, -2500, -21240, 0)
    SetChrPos(0x103, 36000, -2500, -21200, 0)
    SetChrPos(0x104, 35080, -2500, -22190, 0)
    SetChrPos(0x105, 33890, -2500, -22230, 0)
    SetChrPos(0x109, 36510, -2500, -22110, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_93(0xB, 0xB4, 0x0)
    OP_0D()

    #C0204
    ChrTalk(
        0x101,
        "#00000F好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "将之前寻找到的\x07\x02",

            "废弃材料\x07\x00",
            "交出去了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0206
    ChrTalk(
        0xB,
        "呵呵，非常感谢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5525")
    OP_2C(0x8E, 0x3)
    OP_29(0x8E, 0x1, 0x8)
    Jump("loc_557E")

    label("loc_5525")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5546")
    OP_2C(0x8E, 0x2)
    OP_29(0x8E, 0x1, 0x9)
    Jump("loc_557E")

    label("loc_5546")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5567")
    OP_2C(0x8E, 0x1)
    OP_29(0x8E, 0x1, 0xA)
    Jump("loc_557E")

    label("loc_5567")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_557E")
    OP_29(0x8E, 0x1, 0xB)

    label("loc_557E")

    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)

    #C0207
    ChrTalk(
        0xB,
        (
            "把这些废弃材料换成米拉之后，\x01",
            "一定能为旧城区的\x01",
            "重建计划做出贡献。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#00100F嗯，那可真是\x01",
            "让人高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x109,
        (
            "#10100F希望旧城区\x01",
            "能尽早复兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        (
            "#00303F连这么小的孩子都如此努力，\x01",
            "旧城区一定很快就能复兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x105,
        "#10300F……呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        (
            "#00200F好啦，\x01",
            "我们也该走了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5715")

    #C0213
    ChrTalk(
        0x101,
        (
            "#00000F嗯，该做的事情都做完了，\x01",
            "我们去向阿巴斯报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0xC)
    Jump("loc_5757")

    label("loc_5715")


    #C0214
    ChrTalk(
        0x101,
        (
            "#00000F嗯，去其它地方看看吧，\x01",
            "也许还有别的事情需要我们帮忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5757")

    SetScenarioFlags(0x198, 0)
    OP_4C(0xB, 0xFF)
    OP_93(0xB, 0x0, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 34840, -2500, -21110, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_44_53C4 end

    def Function_45_5791(): pass

    label("Function_45_5791")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(7540, 6230, -5160, 0)
    MoveCamera(64, 37, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(18930, 0)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 11100, 0, -2800, 270)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 11100, 0, -3700, 270)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xE, 9500, 0, -2800, 90)
    SetChrPos(0x9, 9500, 0, -3700, 90)
    SetChrPos(0xA, 8000, 0, -2800, 90)
    SetChrPos(0xB, 8000, 0, -3700, 90)
    SetChrPos(0x11, 7000, 0, -2800, 90)
    SetChrPos(0x12, 7000, 0, -3700, 90)
    SetChrPos(0x10, 6000, 0, -2800, 90)
    SetChrPos(0xF, 6000, 0, -3700, 90)
    SetChrPos(0x8, 5000, 0, -3700, 90)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 990, 0, -7830, 0)
    SetChrPos(0x101, 1590, 0, -6330, 180)
    SetChrPos(0x105, 440, 0, -6060, 180)
    SetChrPos(0x102, 2500, 0, -5450, 180)
    SetChrPos(0x103, -480, 0, -5480, 180)
    SetChrPos(0x104, 490, 0, -4700, 180)
    SetChrPos(0x109, 1580, 0, -4880, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x13, 0xFF)
    ClearMapObjFlags(0x7, 0x4)
    FadeToBright(1000, 0)
    OP_68(8690, 2100, -4190, 15000)
    MoveCamera(39, 44, 0, 15000)
    OP_6E(500, 15000)
    SetCameraDistance(17780, 15000)

    def lambda_59B5():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_59B5)
    Sleep(100)

    def lambda_59D2():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_59D2)
    Sleep(500)

    def lambda_59EF():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_59EF)
    Sleep(250)

    def lambda_5A0C():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5A0C)

    def lambda_5A26():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5A26)
    Sleep(350)
    OP_93(0x17, 0x5A, 0x1F4)

    def lambda_5A4A():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5A4A)
    Sleep(150)
    OP_93(0xD, 0x5A, 0x1F4)

    def lambda_5A6E():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5A6E)

    def lambda_5A88():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5A88)
    Sleep(250)

    def lambda_5AA5():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5AA5)
    Sleep(600)
    OP_93(0x17, 0x10E, 0x1F4)
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(600)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x8, 0x1)
    BeginChrThread(0x9, 3, 0, 47)
    Sleep(100)
    BeginChrThread(0xE, 3, 0, 46)
    Sleep(1000)

    def lambda_5B09():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5B09)
    Sleep(150)

    def lambda_5B26():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5B26)

    def lambda_5B40():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5B40)
    Sleep(250)

    def lambda_5B5D():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5B5D)
    Sleep(50)

    def lambda_5B7A():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5B7A)

    def lambda_5B94():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5B94)
    Sleep(500)
    OP_93(0x17, 0x5A, 0x1F4)

    def lambda_5BB8():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5BB8)
    Sleep(500)
    OP_93(0xD, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0x17, 0x10E, 0x1F4)
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(500)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x8, 0x1)
    BeginChrThread(0xA, 3, 0, 48)
    Sleep(100)
    BeginChrThread(0xB, 3, 0, 49)
    Sleep(1000)

    def lambda_5C26():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5C26)
    Sleep(150)

    def lambda_5C43():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5C43)
    Sleep(50)

    def lambda_5C60():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5C60)
    Sleep(150)

    def lambda_5C7D():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5C7D)
    Sleep(200)

    def lambda_5C9A():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C9A)
    Sleep(1000)
    OP_93(0x17, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0xD, 0x5A, 0x1F4)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_93(0x17, 0x10E, 0x1F4)
    OP_93(0xD, 0x10E, 0x1F4)
    OP_0D()
    OP_68(310, 2100, -7180, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16930, 0)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0xE, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x17, 10930, 0, -3700, 90)
    SetChrPos(0x10, 11070, 0, 660, 135)
    SetChrPos(0xF, 12030, 0, 630, 225)
    SetChrFlags(0xF, 0x10)
    ClearMapObjFlags(0x7, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 34490, -6500, -37750, 315)
    SetChrPos(0xA, 34490, -6500, -38950, 315)
    SetChrPos(0xB, 34840, -2220, -19610, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DF9")
    SetChrFlags(0xB, 0x10)

    label("loc_5DF9")

    SetChrPos(0xE, 32800, -6500, -36950, 315)
    SetChrPos(0x11, 5770, 0, -8300, 270)
    SetChrPos(0x12, 4420, 0, -8080, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0215
    ChrTalk(
        0x13,
        (
            "#04100F……辛苦了，特别任务支援科的各位。\x02\x03",

            "多亏你们的协助，旧城区的\x01",
            "各位总算恢复了一些精神。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        "#00000F能帮上忙，是我们的荣幸。\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        (
            "#00108F但似乎还有各式各样\x01",
            "的问题等着处理……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        (
            "#00303F瓦鲁多的那些小弟\x01",
            "在短时间内恐怕很难振作起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x105,
        (
            "#10306F毕竟剑蛇帮的\x01",
            "成员几乎都\x01",
            "受伤住院了。\x02\x03",

            "#10300F不过，迪诺肯定会努力\x01",
            "处理那些事情的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#00200F那自然是\x01",
            "最好不过。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x109,
        "#10103F是啊……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x13,
        (
            "#04100F总之，委托就此结束。\x02\x03",

            "如果以后再有什么事情，\x01",
            "还请大家继续帮助旧城区的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#00000F嗯，知道了，\x01",
            "随时都可以联系我们。\x02",
        )
    )

    CloseMessageWindow()
    SubItemNumber(0x340, 1)
    SubItemNumber(0x375, 1)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0224
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【支援旧城区的重建】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8E, 0x1, 0xD)
    OP_29(0x8E, 0x4, 0x10)
    OP_4C(0x13, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 990, 0, -6330, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_45_5791 end

    def Function_46_60CE(): pass

    label("Function_46_60CE")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_46_60CE end

    def Function_47_60F7(): pass

    label("Function_47_60F7")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    OP_97(0xFE, 0x3E8, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xE, 500)
    Sleep(500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_47_60F7 end

    def Function_48_6134(): pass

    label("Function_48_6134")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_97(0xFE, 0x7D0, 0x0, 0x7D0, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_48_6134 end

    def Function_49_616E(): pass

    label("Function_49_616E")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_97(0xFE, 0x7D0, 0x0, 0x7D0, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xA, 500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_49_616E end

    def Function_50_61A8(): pass

    label("Function_50_61A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62C0")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_61EB"),
        (1, "loc_6205"),
        (2, "loc_621F"),
        (3, "loc_6239"),
        (4, "loc_6253"),
        (5, "loc_626D"),
        (6, "loc_6287"),
        (SWITCH_DEFAULT, "loc_62A1"),
    )


    label("loc_61EB")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_62BB")

    label("loc_6205")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_62BB")

    label("loc_621F")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_62BB")

    label("loc_6239")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_62BB")

    label("loc_6253")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_62BB")

    label("loc_626D")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_62BB")

    label("loc_6287")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_62BB")

    label("loc_62A1")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_62BB")

    label("loc_62BB")

    Jump("Function_50_61A8")

    label("loc_62C0")

    Return()

    # Function_50_61A8 end

    SaveToFile()

Try(main)
