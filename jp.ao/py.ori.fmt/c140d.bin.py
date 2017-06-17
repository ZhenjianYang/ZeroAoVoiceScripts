from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "パオラ婆さん",           # 1
        "ヴァン",                 # 2
        "ルゼ",                   # 3
        "カノン",                 # 4
        "ディーノ",               # 5
        "タントス老人",           # 6
        "バッカス",               # 7
        "リマ",                   # 8
        "メルスン",               # 9
        "キーンツ",               # 10
        "ベッセ",                 # 11
        "アッバス",               # 12
        "ヒューイ",               # 13
        "スラッシュ",             # 14
        "リャン",                 # 15
        "アゼル",                 # 16
        "ヴァルド",               # 17
        "中央広場",               # 18
        "西通り",                 # 19
        "行政区",                 # 20
        "住宅街",                 # 21
        "歓楽街",                 # 22
        "東通り",                 # 23
        "旧市街",                 # 24
        "港湾区",                 # 25
        "ＩＢＣ",                 # 26
        "駅前通り",               # 27
        "裏通り",                 # 28
        "ウルスラ間道",           # 29
        "東クロスベル街道",       # 30
        "西クロスベル街道",       # 31
        "マインツ山道",           # 32
        "オルキスタワー",         # 33
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

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "中央広場")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "西通り")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "行政区")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "住宅街")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "歓楽街")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "東通り")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "旧市街")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "駅前通り")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "裏通り")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-238.0500030517578, 0.0, 225.39999389648438, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-88.0, 0.0, 360.0, 0x0000, 0x0000, "オルキスタワー")
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
        "Function_6_10A1",         # 06, 6
        "Function_7_1154",         # 07, 7
        "Function_8_1401",         # 08, 8
        "Function_9_153B",         # 09, 9
        "Function_10_15FE",        # 0A, 10
        "Function_11_16C8",        # 0B, 11
        "Function_12_195C",        # 0C, 12
        "Function_13_1DC1",        # 0D, 13
        "Function_14_1FB9",        # 0E, 14
        "Function_15_2198",        # 0F, 15
        "Function_16_2321",        # 10, 16
        "Function_17_2699",        # 11, 17
        "Function_18_26A0",        # 12, 18
        "Function_19_2A1E",        # 13, 19
        "Function_20_2AF3",        # 14, 20
        "Function_21_2C98",        # 15, 21
        "Function_22_2D26",        # 16, 22
        "Function_23_2D8E",        # 17, 23
        "Function_24_2DFC",        # 18, 24
        "Function_25_2FEC",        # 19, 25
        "Function_26_4175",        # 1A, 26
        "Function_27_418B",        # 1B, 27
        "Function_28_46DC",        # 1C, 28
        "Function_29_52E4",        # 1D, 29
        "Function_30_533F",        # 1E, 30
        "Function_31_539A",        # 1F, 31
        "Function_32_53F5",        # 20, 32
        "Function_33_5450",        # 21, 33
        "Function_34_54AB",        # 22, 34
        "Function_35_5506",        # 23, 35
        "Function_36_5561",        # 24, 36
        "Function_37_55BC",        # 25, 37
        "Function_38_5617",        # 26, 38
        "Function_39_5672",        # 27, 39
        "Function_40_56CD",        # 28, 40
        "Function_41_5728",        # 29, 41
        "Function_42_5783",        # 2A, 42
        "Function_43_57DE",        # 2B, 43
        "Function_44_5B32",        # 2C, 44
        "Function_45_5F2F",        # 2D, 45
        "Function_46_68C6",        # 2E, 46
        "Function_47_68EF",        # 2F, 47
        "Function_48_692C",        # 30, 48
        "Function_49_6966",        # 31, 49
        "Function_50_69A0",        # 32, 50
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1050")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3D, 1)"), scpexpr(EXPR_END)), "loc_FD9")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_104B")

    label("loc_FD9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_104B")

    Jump("loc_1095")

    label("loc_1050")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1095")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F50 end

    def Function_6_10A1(): pass

    label("Function_6_10A1")

    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『オーブンで作る本格料理』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_1150")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1150")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『スタミナステーキ』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1150")

    TalkEnd(0xFF)
    Return()

    # Function_6_10A1 end

    def Function_7_1154(): pass

    label("Function_7_1154")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1256")

    #C0006
    ChrTalk(
        0xFE,
        (
            "うぃ～、ヒック……\x01",
            "やっぱ酒は最高だぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "……にしても、なんだあの\x01",
            "バカでけえ木はよぉ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00006F（あ、危ないなあ、\x01",
            "  こんな所で酔っ払って……）\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#00300F（まあ、飲みてぇ気持ちも\x01",
            "  分からないでもねえがな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12E2")

    label("loc_1256")


    #C0010
    ChrTalk(
        0xFE,
        (
            "うぃ～、ヒック……\x01",
            "あのバカでけえ木は、\x01",
            "もしかして天国かぁ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "きっと美味い酒と\x01",
            "カワイイ姉ちゃんが\x01",
            "いっぱいなんだろうなぁ～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E2")

    Jump("loc_13FD")

    label("loc_12E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12F5")
    Jump("loc_13FD")

    label("loc_12F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1303")
    Jump("loc_13FD")

    label("loc_1303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_13FD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132B")
    Call(0, 8)
    Jump("loc_13A3")

    label("loc_132B")


    #C0012
    ChrTalk(
        0xFE,
        (
            "ったく、炊き出しがあるとは言え、\x01",
            "まっ昼間からタダ働きとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "さっさと終わらせて、\x01",
            "早く一杯やりてえモンだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A3")

    Jump("loc_13FD")

    label("loc_13A8")


    #C0014
    ChrTalk(
        0xFE,
        (
            "しっかし、太陽ってヤツは\x01",
            "どんだけ眩しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "夜型人間には毒だぜ、こりゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_13FD")

    TalkEnd(0xFE)
    Return()

    # Function_7_1154 end

    def Function_8_1401(): pass

    label("Function_8_1401")

    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0x9, 0x0, 0)

    #C0016
    ChrTalk(
        0x9,
        (
            "キャハハ、オヤジのやろー、\x01",
            "珍しく昼間から仕事してやがる。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "何でもフッコーを手伝わねえと、\x01",
            "アパートから追い出すって\x01",
            "大家に言われたらしいぜ～？\x02",
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
            "おらぁ、ヴァン。\x01",
            "余計なこと喋ってんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xE,
        "黙って仕事を手伝いやがれ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_93(0x9, 0x13B, 0x0)
    OP_93(0xE, 0x13B, 0x0)
    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_8_1401 end

    def Function_9_153B(): pass

    label("Function_9_153B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159D")

    #C0020
    ChrTalk(
        0xFE,
        (
            "さてと、今日も\x01",
            "ちゃっちゃと片付けるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "まずは寸法を測って、と……\x02",
    )

    CloseMessageWindow()
    Jump("loc_15FA")

    label("loc_159D")


    #C0022
    ChrTalk(
        0xFE,
        (
            "ふう、一足遅くなっちゃったけど\x01",
            "やっと一息付けたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "よしと……午後からも頑張るぞ！\x02",
    )

    CloseMessageWindow()

    label("loc_15FA")

    TalkEnd(0xFE)
    Return()

    # Function_9_153B end

    def Function_10_15FE(): pass

    label("Function_10_15FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165B")

    #C0024
    ChrTalk(
        0xFE,
        "パパ、みんなのためにお仕事してるの。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "とっても、かっこいいの♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C4")

    label("loc_165B")

    OP_4B(0x10, 0x0)
    SetChrName("リマ")

    #C0026
    ChrTalk(
        0xF,
        "パパ、このお汁おいしーねー。\x02",
    )

    CloseMessageWindow()
    SetChrName("メルスン")

    #C0027
    ChrTalk(
        0x10,
        (
            "ああ、本当だね。\x01",
            "パパも力が湧いてくるよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0x0)

    label("loc_16C4")

    TalkEnd(0xFE)
    Return()

    # Function_10_15FE end

    def Function_11_16C8(): pass

    label("Function_11_16C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1815")

    #C0028
    ChrTalk(
        0x13,
        (
            "#04100F……そうだ、せっかくだから\x01",
            "お前たちにこれを渡しておこう。\x02",
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
            "『アッバスのアカウント』\x07\x00",
            "を手に入れた。\x02",
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
            "#00005F『ポムっと！』のアカウント……？\x01",
            "アッバスもやってるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x13,
        (
            "#04100F時間が空いたときだけだがな。\x02\x03",

            "気が向いたら相手をしてやるから、\x01",
            "勝負を申し込んでくるがいい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1958")

    label("loc_1815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F1")

    #C0032
    ChrTalk(
        0x13,
        (
            "#04100F特務支援課……\x01",
            "今日は本当に助かったぞ。\x02\x03",

            "おかげで作業もはかどりそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#00100Fふふ、どういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x105,
        (
            "#10300Fアッバスたちは\x01",
            "この後もがんばってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x13,
        "#04100Fああ、もちろんだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1958")

    label("loc_18F1")


    #C0036
    ChrTalk(
        0x13,
        (
            "#04100Fさて、これで必要な部材も\x01",
            "大体揃った。\x02\x03",

            "日が暮れるまで、集中して\x01",
            "作業をこなしていかんとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1958")

    TalkEnd(0xFE)
    Return()

    # Function_11_16C8 end

    def Function_12_195C(): pass

    label("Function_12_195C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1AB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A48")

    #C0037
    ChrTalk(
        0xFE,
        (
            "なんだか、とんでもない事が\x01",
            "起こっちゃったね……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "あの青白い樹を見ていたら、\x01",
            "僕も何か、出来ることを\x01",
            "やらなくちゃって思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "せめて街を少しでも綺麗にして、\x01",
            "みんなにほっとしてもらわないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1AB2")

    label("loc_1A48")


    #C0040
    ChrTalk(
        0xFE,
        (
            "そうときまれば頑張って、\x01",
            "街を綺麗にしないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "精一杯がんばっていれば、\x01",
            "きっといい事があるよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB2")

    Jump("loc_1DBD")

    label("loc_1AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1AC5")
    Jump("loc_1DBD")

    label("loc_1AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B0A")

    #C0042
    ChrTalk(
        0xFE,
        (
            "せ、戦争だなんて……\x01",
            "そんなのゼッタイにダメだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBD")

    label("loc_1B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DBD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B46")
    Call(0, 27)
    Return()

    label("loc_1B46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BD1")
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
            "話をする\x01",        # 0
            "廃材を渡す\x01",      # 1
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
        (0, "loc_1BC0"),
        (1, "loc_1BC5"),
        (SWITCH_DEFAULT, "loc_1BD1"),
    )


    label("loc_1BC0")

    Jump("loc_1BD1")

    label("loc_1BC5")

    Call(0, 43)
    TalkEnd(0xB)
    Return()

    label("loc_1BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C42")

    #C0043
    ChrTalk(
        0xFE,
        (
            "ガサゴソ……\x01",
            "えっと、これは……ダメか。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "それじゃこっちは……\x01",
            "う～ん、これもハズレだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBD")

    label("loc_1C42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE4")

    #C0045
    ChrTalk(
        0xB,
        (
            "お兄ちゃんたち、\x01",
            "金属を含んだ廃材を\x01",
            "探してきてもらえる？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "一通り片付けはしたけど、\x01",
            "まだ見つかってないものも\x01",
            "あると思うんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D44")

    label("loc_1CE4")


    #C0047
    ChrTalk(
        0xFE,
        "お兄ちゃんたち、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "もらった廃材は\x01",
            "僕が責任を持って\x01",
            "換金させてもらうからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D44")

    Jump("loc_1DBD")

    label("loc_1D49")


    #C0049
    ChrTalk(
        0xFE,
        (
            "さてと、お腹も\x01",
            "一杯になったことだし、\x01",
            "また頑張るぞ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "お兄ちゃんたち、\x01",
            "色々手伝ってくれて\x01",
            "ありがとうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBD")

    TalkEnd(0xFE)
    Return()

    # Function_12_195C end

    def Function_13_1DC1(): pass

    label("Function_13_1DC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E92")

    #C0051
    ChrTalk(
        0xFE,
        (
            "なんでしょうねえ、\x01",
            "あの大きくて立派な樹は。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "青白く光って……\x01",
            "この世のものとは思えない\x01",
            "美しさですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "私たちを女神様の元へ\x01",
            "連れて行ってくれるんじゃ\x01",
            "ないかしらねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1F1C")

    label("loc_1E92")


    #C0054
    ChrTalk(
        0xFE,
        (
            "あの大きくて立派な樹は、\x01",
            "この世のものとは思えない\x01",
            "美しさですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "私たちを女神様の元へ\x01",
            "連れて行ってくれるんじゃ\x01",
            "ないかしらねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1C")

    Jump("loc_1FB5")

    label("loc_1F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F2F")
    Jump("loc_1FB5")

    label("loc_1F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1FB5")

    #C0056
    ChrTalk(
        0xFE,
        (
            "よく分からないけど、\x01",
            "大変な事態になっている\x01",
            "みたいですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "しばらく家からは出ない方が\x01",
            "よいのかもしれませんねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB5")

    TalkEnd(0xFE)
    Return()

    # Function_13_1DC1 end

    def Function_14_1FB9(): pass

    label("Function_14_1FB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2044")

    #C0058
    ChrTalk(
        0xFE,
        (
            "酔ってないオヤジが\x01",
            "あまりにもきしょくわるいから、\x01",
            "酒を調達してきてやったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "……ずっと飲んでろダメオヤジ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2194")

    label("loc_2044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2052")
    Jump("loc_2194")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_20C8")

    #C0060
    ChrTalk(
        0xFE,
        (
            "へへっ、何だか街の方が\x01",
            "スゲエ騒ぎになってんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "誰かが戦争になるかも\x01",
            "しれねえって言ってたぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2194")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2194")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F0")
    Call(0, 8)
    Jump("loc_2123")

    label("loc_20F0")


    #C0062
    ChrTalk(
        0xFE,
        (
            "キャハハ、オヤジのやろー、\x01",
            "まるで真人間だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2123")

    Jump("loc_2194")

    label("loc_2128")


    #C0063
    ChrTalk(
        0xFE,
        (
            "へへっ、今日の炊き出しも\x01",
            "うまかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "あんなのが毎日食えんなら、\x01",
            "ずっとフッコーしててもいいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2194")

    TalkEnd(0xFE)
    Return()

    # Function_14_1FB9 end

    def Function_15_2198(): pass

    label("Function_15_2198")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2230")

    #C0065
    ChrTalk(
        0xFE,
        (
            "ヴァンが自分からお父さんに\x01",
            "お酒をあげるなんて相当だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "まともなバッカスおじさん、\x01",
            "せっかく面白かったのにさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231D")

    label("loc_2230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_223E")
    Jump("loc_231D")

    label("loc_223E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_227B")

    #C0067
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "それってヤベーんじゃないの？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231D")

    label("loc_227B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_231D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D6")

    #C0068
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "ヴァンのお父さんって\x01",
            "意外と頼りになるんだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231D")

    label("loc_22D6")


    #C0069
    ChrTalk(
        0xFE,
        (
            "炊き出しは、\x01",
            "夕方にもう一回あるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "次は何食えんのかな？\x02",
    )

    CloseMessageWindow()

    label("loc_231D")

    TalkEnd(0xFE)
    Return()

    # Function_15_2198 end

    def Function_16_2321(): pass

    label("Function_16_2321")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_245B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2415")

    #C0071
    ChrTalk(
        0xFE,
        (
            "ジェドさんたちがようやく\x01",
            "力になってくれることになったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……あんなことがあったとはいえ、\x01",
            "俺たちにとってヴァルドさんは\x01",
            "やっぱり大切なリーダーだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "お前ら……なんとか\x01",
            "連れ戻してやってくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2456")

    label("loc_2415")


    #C0074
    ChrTalk(
        0xFE,
        (
            "お前ら……なんとかヴァルドさんを\x01",
            "連れ戻してやってくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2456")

    Jump("loc_2695")

    label("loc_245B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2469")
    Jump("loc_2695")

    label("loc_2469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2695")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_261F")

    #C0075
    ChrTalk(
        0xFE,
        "あ、特務支援課……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        (
            "#00108Fディーノ君……\x01",
            "えっと、他のメンバーはその……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "ん、ああ……おかげ様で\x01",
            "一番重症だったコウキ先輩も\x01",
            "何とか意識を取り戻してさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "他の先輩方も、何人かは退院して\x01",
            "旧市街の方に戻って来ているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "まあ流石に、すぐにチームへ\x01",
            "復帰ってのは難しいと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "でも、ここで待っていれば、\x01",
            "必ず顔を出してくれるはずだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        "#00103Fディーノ君……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00008Fそうか……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 2)
    Jump("loc_2695")

    label("loc_261F")


    #C0083
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "朝から街の方が騒がしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "独立がどうのとかって聞いたけど、\x01",
            "もっと静かにやって欲しいよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2695")

    TalkEnd(0xFE)
    Return()

    # Function_16_2321 end

    def Function_17_2699(): pass

    label("Function_17_2699")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_17_2699 end

    def Function_18_26A0(): pass

    label("Function_18_26A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A4")
    SetScenarioFlags(0x191, 6)

    #C0085
    ChrTalk(
        0x17,
        (
            "ああ、支援課のみんな。\x01",
            "今日は本当にありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x17,
        (
            "炊き出しの豚汁が余ったから\x01",
            "良かったら持って行ってよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 4)), scpexpr(EXPR_END)), "loc_277C")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x21A, 6)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    Jump("loc_27CA")

    label("loc_277C")

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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x21B, 6)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()

    label("loc_27CA")


    #C0089
    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、\x01",
            "ありがたく戴いておくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        (
            "#10104Fこの豚汁、本当に\x01",
            "おいしかったですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        (
            "#00200Fええ、また戴けると思うと\x01",
            "嬉しいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x17,
        (
            "はは、そう言ってくれると\x01",
            "こっちも作った甲斐があるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1A")

    label("loc_28A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2978")

    #C0093
    ChrTalk(
        0x17,
        (
            "豚汁、せっかくだから\x01",
            "姉さんとユゴットにも\x01",
            "持って行ってあげようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x17,
        (
            "ああ、でもこれは復興作業を\x01",
            "手伝ってくれた人のものだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x17,
        (
            "そうだな、それなら\x01",
            "洗い物でも手伝ってもらうかな？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2A1A")

    label("loc_2978")


    #C0096
    ChrTalk(
        0x17,
        (
            "豚汁、せっかくだから\x01",
            "姉さんとユゴットにも\x01",
            "持って行ってあげようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x17,
        (
            "２人とも今日は暇してるみたいだし、\x01",
            "ちょっと手伝ってもらうのも\x01",
            "アリかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1A")

    TalkEnd(0xFE)
    Return()

    # Function_18_26A0 end

    def Function_19_2A1E(): pass

    label("Function_19_2A1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A8B")

    #C0098
    ChrTalk(
        0xFE,
        (
            "ふう、やはり\x01",
            "現場作業は体力を使うな。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "でもまあ、これも\x01",
            "良いトレーニングだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AEF")

    label("loc_2A8B")


    #C0100
    ChrTalk(
        0xFE,
        (
            "さてと、ここからは\x01",
            "一層の力仕事って感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "ベッセの奴、大丈夫なのか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AEF")

    TalkEnd(0xFE)
    Return()

    # Function_19_2A1E end

    def Function_20_2AF3(): pass

    label("Function_20_2AF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B98")

    #C0102
    ChrTalk(
        0x12,
        (
            "そ、それにしても……\x01",
            "このアパートの\x01",
            "破壊ぶりは、す、凄まじいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x12,
        (
            "廃アパートで良かったが、\x01",
            "な、中に人がいたらと思うと、\x01",
            "ぞっとするぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C94")

    label("loc_2B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C30")

    #C0104
    ChrTalk(
        0x12,
        "……げっぷ。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x12,
        (
            "おかわりが出来るというから……\x01",
            "つ、ついつい食べ過ぎてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x12,
        (
            "ほ、ほどほどで\x01",
            "止めておくべきだったな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C94")

    label("loc_2C30")


    #C0107
    ChrTalk(
        0x12,
        (
            "ち、力を入れると\x01",
            "逆流してしまうかもしれない……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x12,
        (
            "ほ、ほどほどで\x01",
            "止めておくべきだったな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C94")

    TalkEnd(0xFE)
    Return()

    # Function_20_2AF3 end

    def Function_21_2C98(): pass

    label("Function_21_2C98")

    TalkBegin(0xFE)

    #C0109
    ChrTalk(
        0xFE,
        (
            "テスタメンツの青坊主どもと、\x01",
            "協力して見回ってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "ハッ、旧市街で\x01",
            "勝手なことするヤツがいたら\x01",
            "俺たちがボコボコにしてやるぜ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2C98 end

    def Function_22_2D26(): pass

    label("Function_22_2D26")

    TalkBegin(0xFE)

    #C0111
    ChrTalk(
        0xFE,
        (
            "何をどうしたらあんなでっけぇ木が\x01",
            "現れるってんだ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        "ヒャハ、マジで意味わかんねェ～！！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2D26 end

    def Function_23_2D8E(): pass

    label("Function_23_2D8E")

    TalkBegin(0xFE)

    #C0113
    ChrTalk(
        0xFE,
        (
            "互いの縄張りを見張ってれば\x01",
            "とりあえず安心できそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        "よし、それじゃもう一回りしてくるかな。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2D8E end

    def Function_24_2DFC(): pass

    label("Function_24_2DFC")

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

    # Function_24_2DFC end

    def Function_25_2FEC(): pass

    label("Function_25_2FEC")

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

    def lambda_32B5():
        OP_95(0xFE, 20640, -6500, -36460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_32B5)
    WaitChrThread(0x18, 1)

    def lambda_32D3():
        OP_95(0xFE, 21800, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_32D3)
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

    def lambda_3369():
        OP_95(0xFE, 41800, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3369)
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
        "#01608F#30W#5P…………クソ………………\x02",
    )

    CloseMessageWindow()

    #N0117
    NpcTalk(
        0xC,
        "少年の声",
        "#30W#2S#5P……ヴァルド……さん……？\x02",
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

    def lambda_34F9():
        OP_95(0xFE, 47600, -2100, -22700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_34F9)

    def lambda_3513():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3513)
    WaitChrThread(0xC, 1)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0118
    ChrTalk(
        0x18,
        "#01605F#5Pディーノ……お前……\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        "#11Pヴァ、ヴァルドさん……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0120
    ChrTalk(
        0xC,
        "#4S#11P本当にヴァルドさんだ！！\x02",
    )

    CloseMessageWindow()
    OP_68(42200, -1100, -22700, 1500)
    MoveCamera(53, 20, 0, 1300)
    SetCameraDistance(17000, 1300)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_35F7():
        OP_95(0xFE, 42600, -2100, -22700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_35F7)
    WaitChrThread(0xC, 1)
    Sound(812, 0, 50, 0)
    OP_6F(0x79)
    Sleep(300)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0121
    ChrTalk(
        0xC,
        (
            "#2P今までどこに……！\x01",
            "本当に心配したんですよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xC,
        (
            "#2Pで、でもよく無事で……\x01",
            "……うううううううっ……！\x02",
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
            "#2Pせ、先輩たちは\x01",
            "みんな大ケガを負って……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xC,
        (
            "#2P退院できた人もいるのに\x01",
            "ぜんぜん戻って来てくれなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xC,
        (
            "#2Pで、でも大丈夫です！\x01",
            "ヴァルドさんがいればきっと……！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x18,
        "#5P#01608F………っ……！\x02",
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

    def lambda_380A():
        OP_9D(0xFE, 0xAB7C, 0xFFFFF7CC, 0xFFFFA754, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_380A)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(862, 0, 30, 0)

    #C0128
    ChrTalk(
        0xC,
        "#11Pうあっ……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 3)

    def lambda_385A():
        OP_A6(0xFE, 0x0, 0x32, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_385A)
    Sleep(300)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    SetChrSubChip(0xC, 0x4)

    #C0129
    ChrTalk(
        0xC,
        "#60W#2Sヴァルド……さん……？\x02",
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
            "#11P#01603F#30W……サーベルバイパーは解散だ。\x02\x03",

            "#01608Fてめぇも２度と……\x01",
            "俺のケツを追いかけるんじゃねえ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    #C0131
    ChrTalk(
        0xC,
        "#50W#2S……ウソ……ですよね……\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xC,
        "#50W#2Sだってヴァルドさんは……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        (
            "#50W#2S……ヴァルドさんはいつだって……\x01",
            "頼りになる最高のヘッドで……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(30200, -1100, -22700, 9000)
    MoveCamera(65, 11, 0, 9000)
    OP_6E(550, 9000)
    SetCameraDistance(19000, 9000)

    def lambda_3A0E():
        OP_95(0xFE, 17000, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3A0E)
    Sleep(500)
    SetChrSubChip(0xC, 0x5)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(230, 10, -1, -1)

    #A0134
    AnonymousTalk(
        0xC,
        (
            "#57A……あの鬼が……\x01",
            "みんなを滅茶苦茶にした化物が\x01",
            "ヴァルドさんなんてッ！\x02",
        )
    )
    #Auto

    Sleep(5700)
    OP_82(0xC8, 0x0, 0xBB8, 0x7D0)
    SetMessageWindowPos(230, 20, -1, -1)

    #A0135
    AnonymousTalk(
        0xC,
        "#23A#4Sそんなのウソですよねええッ！？\x02",
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

    def lambda_3B3D():
        OP_95(0xFE, 9600, 0, -13300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3B3D)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x18, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #N0136
    NpcTalk(
        0x11,
        "青年の声",
        "と、止まれ……ッ！\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(805, 0, 100, 0)
    Sound(318, 0, 40, 0)
    OP_68(7850, 1100, -6000, 2500)
    MoveCamera(35, 21, 0, 2500)
    SetCameraDistance(17000, 2500)

    def lambda_3BDD():
        OP_95(0xFE, 8400, 0, -8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3BDD)
    WaitChrThread(0x18, 1)
    OP_6F(0x79)

    #C0137
    ChrTalk(
        0x11,
        (
            "#5Pヴァルド・ヴァレス！\x01",
            "ま、まさか戻ってくるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x12,
        (
            "#5Pこれ以上、旧市街を\x01",
            "お前の好きには、させない……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x12,
        "#5P何としても止めさせてもらう……\x02",
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
            "#5P……君は一体、\x01",
            "何がしたかったんだ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x11,
        (
            "#5Pあ、あんな化物になって\x01",
            "この旧市街を滅茶苦茶にして……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x17,
        (
            "おまけに可愛がってた\x01",
            "手下たちをあんな風に……！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x16,
        "#5Pひ、酷すぎるよ……！\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x18,
        (
            "#11P#01604Fフン……\x02\x03",

            "#01602F──そういえば\x01",
            "ワジとハゲ坊主はどうした？\x02\x03",

            "元々、ヨソ者みてぇだし……\x01",
            "尻尾を巻いて逃げ出したかよ？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0xFA)

    #C0146
    ChrTalk(
        0x11,
        "#5Pば、馬鹿にするな……！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x12,
        (
            "#5Pあの２人なら\x01",
            "必ず戻ってくる……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0148
    ChrTalk(
        0x18,
        "#11P#01605Fなにィ……？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x16,
        (
            "#5Pじ、事情があるそうなんだ！\x01",
            "果たすべき使命があるって！\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x16,
        (
            "#5Pそれで街は離れるけど\x01",
            "いずれまた戻ってくるって！\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x17,
        (
            "何のことか判らないけど……\x01",
            "僕たちは２人を信じるだけだ！\x02",
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

    def lambda_3F82():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3F82)
    WaitChrThread(0x18, 2)
    Sleep(500)

    def lambda_3FA2():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3FA2)
    WaitChrThread(0x18, 2)
    Sleep(500)

    #C0152
    ChrTalk(
        0x18,
        "#11P#01604F#50W………クク……ハハ……………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0153
    ChrTalk(
        0x18,
        "#11P#01609F#5Sハハハハハハハハハハッ！！\x02",
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
            "#5P#01604Fなるほど……“使命”ねぇ。\x02\x03",

            "どうやらあの時の続きが\x01",
            "出来そうじゃねぇか……？\x02\x03",

            "#01602F──そうだろう！？\x02",
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
        "#5P#5S#35W#27A#01607Fワジイイイイイイッ！！！\x02",
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

    # Function_25_2FEC end

    def Function_26_4175(): pass

    label("Function_26_4175")

    Sleep(120)
    SetChrSubChip(0xC, 0x1)
    WaitChrThread(0xC, 1)
    SetChrSubChip(0xC, 0x2)
    Sound(811, 0, 100, 0)
    Return()

    # Function_26_4175 end

    def Function_27_418B(): pass

    label("Function_27_418B")

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
        "えっと、これは……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        "……ちがう。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        "これも……違うなあ。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "うーん、こまったな。\x01",
            "この調子じゃ終わらないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#00000Fきみ、何をしてるんだい？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0161
    ChrTalk(
        0xB,
        (
            "うん……\x01",
            "アッバスさんに頼まれて、\x01",
            "廃材の分別をしてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "金属を含むものだったら、\x01",
            "ジャンク品として、\x01",
            "ミラに換金できるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#00305Fはあ～、なるほどな。\x02\x03",

            "#00304F旧市街の住民って\x01",
            "なんつうか、したたかだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x105,
        (
            "#10304Fここじゃ普通のことさ。\x02\x03",

            "#10300F旧市街の住民たちには、\x01",
            "生きるために全力を尽くすという\x01",
            "信念があるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        (
            "#00200F生活が苦しいからこそ、\x01",
            "というわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x109,
        (
            "#10103Fうーん、なかなか\x01",
            "マネできないなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#00102Fそれがここの人たちの\x01",
            "強さってところかしらね。\x02\x03",

            "#00100F……ねえキミ、なにか私たちに\x01",
            "手伝えることがあるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        "手伝えること……そうだね。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        (
            "それじゃあ、旧市街の中で\x01",
            "金属を含んだ廃材を\x01",
            "探してきてもらえる？\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "一通り片付けはしたけど、\x01",
            "まだ見つかってないものも\x01",
            "あると思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#00000F金属を含んだ廃材か……\x01",
            "分かった、任せてくれ。\x02\x03",

            "#00003F（効率的に探すなら\x01",
            "  金属探知機のようなものが\x01",
            "  欲しいところだな……）\x02\x03",

            "#00000F（ギヨーム親方なら相談に\x01",
            "  乗ってくれるかもしれない。）\x02",
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

    # Function_27_418B end

    def Function_28_46DC(): pass

    label("Function_28_46DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_477B")
    TalkBegin(0xFF)

    #C0172
    ChrTalk(
        0x101,
        (
            "#00000F廃材回収の方はもう大丈夫だ。\x02\x03",

            "手伝いも一通り終わったし、\x01",
            "アッバスの所に報告に行くか。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_477B")

    TalkBegin(0xFF)

    #C0173
    ChrTalk(
        0x101,
        (
            "#00000F廃材回収の方はもう大丈夫だ。\x02\x03",

            "他に手伝えることがないか探そう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_47CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_47F2")
    Return()

    label("loc_47F2")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE4E5A8), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6BA8), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3F01), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48A4")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xB18A), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4DEE), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_493C")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_493C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49D4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2DB4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8052), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49D4")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A6D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4042), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x254E), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A6D")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B05")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4402), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8BB0), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B05")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B9E")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4132), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x66E4), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B9E")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C36")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3C78), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x136), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C36")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CCE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9376), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9664), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CCE")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D67")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6AD6), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6F54), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D67")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DFF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xBC5C), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9614), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DFF")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E98")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6F4), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7C24), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E98")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F30")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9B46), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x447A), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F30")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1FAD), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x201C), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FC8")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5060")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xA4F6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6284), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5060")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5060")

    SetMapFlags(0x80)
    OP_C7(0x0, 0x0)
    OP_49()
    Sleep(30)
    PlayEffect(0x7, 0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(632, 0, 100, 0)
    Sleep(600)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51E8")
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
        (1, "loc_5162"),
        (2, "loc_516B"),
        (3, "loc_5174"),
        (4, "loc_517D"),
        (5, "loc_5186"),
        (6, "loc_518F"),
        (7, "loc_5198"),
        (8, "loc_51A1"),
        (9, "loc_51AA"),
        (10, "loc_51B3"),
        (11, "loc_51BC"),
        (12, "loc_51C5"),
        (13, "loc_51CE"),
        (14, "loc_51D7"),
        (SWITCH_DEFAULT, "loc_51E0"),
    )


    label("loc_5162")

    OP_66(0x0, 0x1)
    Jump("loc_51E0")

    label("loc_516B")

    OP_66(0x1, 0x1)
    Jump("loc_51E0")

    label("loc_5174")

    OP_66(0x2, 0x1)
    Jump("loc_51E0")

    label("loc_517D")

    OP_66(0x3, 0x1)
    Jump("loc_51E0")

    label("loc_5186")

    OP_66(0x4, 0x1)
    Jump("loc_51E0")

    label("loc_518F")

    OP_66(0x5, 0x1)
    Jump("loc_51E0")

    label("loc_5198")

    OP_66(0x6, 0x1)
    Jump("loc_51E0")

    label("loc_51A1")

    OP_66(0x7, 0x1)
    Jump("loc_51E0")

    label("loc_51AA")

    OP_66(0x8, 0x1)
    Jump("loc_51E0")

    label("loc_51B3")

    OP_66(0x9, 0x1)
    Jump("loc_51E0")

    label("loc_51BC")

    OP_66(0xA, 0x1)
    Jump("loc_51E0")

    label("loc_51C5")

    OP_66(0xB, 0x1)
    Jump("loc_51E0")

    label("loc_51CE")

    OP_66(0xC, 0x1)
    Jump("loc_51E0")

    label("loc_51D7")

    OP_66(0xD, 0x1)
    Jump("loc_51E0")

    label("loc_51E0")

    TalkEnd(0xFF)
    Jump("loc_52DD")

    label("loc_51E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_5243")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ごく近くに反応アリ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_52DD")

    label("loc_5243")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x186A0), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_529A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "付近に反応アリ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_52DD")

    label("loc_529A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "反応ありません。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_52DD")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_28_46DC end

    def Function_29_52E4(): pass

    label("Function_29_52E4")

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
            "を手に入れた。\x02",
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

    # Function_29_52E4 end

    def Function_30_533F(): pass

    label("Function_30_533F")

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
            "を手に入れた。\x02",
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

    # Function_30_533F end

    def Function_31_539A(): pass

    label("Function_31_539A")

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
            "を手に入れた。\x02",
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

    # Function_31_539A end

    def Function_32_53F5(): pass

    label("Function_32_53F5")

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
            "を手に入れた。\x02",
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

    # Function_32_53F5 end

    def Function_33_5450(): pass

    label("Function_33_5450")

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
            "を手に入れた。\x02",
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

    # Function_33_5450 end

    def Function_34_54AB(): pass

    label("Function_34_54AB")

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
            "を手に入れた。\x02",
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

    # Function_34_54AB end

    def Function_35_5506(): pass

    label("Function_35_5506")

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
            "を手に入れた。\x02",
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

    # Function_35_5506 end

    def Function_36_5561(): pass

    label("Function_36_5561")

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
            "を手に入れた。\x02",
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

    # Function_36_5561 end

    def Function_37_55BC(): pass

    label("Function_37_55BC")

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
            "を手に入れた。\x02",
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

    # Function_37_55BC end

    def Function_38_5617(): pass

    label("Function_38_5617")

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
            "を手に入れた。\x02",
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

    # Function_38_5617 end

    def Function_39_5672(): pass

    label("Function_39_5672")

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
            "を手に入れた。\x02",
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

    # Function_39_5672 end

    def Function_40_56CD(): pass

    label("Function_40_56CD")

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
            "を手に入れた。\x02",
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

    # Function_40_56CD end

    def Function_41_5728(): pass

    label("Function_41_5728")

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
            "を手に入れた。\x02",
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

    # Function_41_5728 end

    def Function_42_5783(): pass

    label("Function_42_5783")

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
            "を手に入れた。\x02",
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

    # Function_42_5783 end

    def Function_43_57DE(): pass

    label("Function_43_57DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_588E")

    #C0191
    ChrTalk(
        0xB,
        (
            "わあ……\x01",
            "金属を含んだ廃材を\x01",
            "こんなに見つけてくれたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xB,
        (
            "ふふ、すごいや。\x01",
            "これだけあればホクホクだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "それじゃあこれは\x01",
            "もらってもいいかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_588E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_592F")

    #C0194
    ChrTalk(
        0xB,
        (
            "金属を含んだ廃材を\x01",
            "見つけてくれたんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        (
            "ふふ、ありがとう。\x01",
            "これだけあれば十分だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "それじゃあこれは\x01",
            "もらってもいいかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_592F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_59BC")

    #C0197
    ChrTalk(
        0xB,
        (
            "金属を含んだ廃材を\x01",
            "見つけてくれたんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "結構集まったみたいだけど……\x01",
            "それじゃあこれは\x01",
            "もらってもいいかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_59BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5A68")

    #C0199
    ChrTalk(
        0xB,
        (
            "金属を含んだ廃材を\x01",
            "見つけてくれたんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xB,
        (
            "ちょっと数は少ないけど……\x01",
            "探してくれた気持ちがうれしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        (
            "それじゃあこれは\x01",
            "もらってもいいかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A68")

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
            "廃材を渡す\x01",          # 0
            "まだ探してみる\x01",      # 1
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
        (0, "loc_5AD2"),
        (1, "loc_5ADA"),
        (SWITCH_DEFAULT, "loc_5B31"),
    )


    label("loc_5AD2")

    Call(0, 44)
    Jump("loc_5B31")

    label("loc_5ADA")


    #C0202
    ChrTalk(
        0xB,
        "ああ、そうなんだ。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        (
            "それじゃ、\x01",
            "集まったと思ったら\x01",
            "もう一度声をかけてね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B31")

    label("loc_5B31")

    Return()

    # Function_43_57DE end

    def Function_44_5B32(): pass

    label("Function_44_5B32")

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
        "#00000Fああ、受け取ってくれ。\x02",
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
            "手に入れた\x07\x02",

            "廃材\x07\x00",
            "を渡した。\x02",
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
        "ふふ、どうもありがとう。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CA3")
    OP_2C(0x8E, 0x3)
    OP_29(0x8E, 0x1, 0x8)
    Jump("loc_5CFC")

    label("loc_5CA3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5CC4")
    OP_2C(0x8E, 0x2)
    OP_29(0x8E, 0x1, 0x9)
    Jump("loc_5CFC")

    label("loc_5CC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5CE5")
    OP_2C(0x8E, 0x1)
    OP_29(0x8E, 0x1, 0xA)
    Jump("loc_5CFC")

    label("loc_5CE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5CFC")
    OP_29(0x8E, 0x1, 0xB)

    label("loc_5CFC")

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
            "ミラに換金できたら、\x01",
            "旧市街の復興に役立てさせて\x01",
            "もらうからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#00100Fええ、そうしてくれると\x01",
            "うれしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x109,
        (
            "#10100F早く復興できると\x01",
            "いいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        (
            "#00303Fこんな子供もがんばってんだ、\x01",
            "そのうち何とかなるだろうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x105,
        "#10300F……フフ、そうだね。\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        (
            "#00200Fそれじゃあ、\x01",
            "そろそろ行きましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EC1")

    #C0213
    ChrTalk(
        0x101,
        (
            "#00000Fああ、一通り手伝いもすんだし、\x01",
            "アッバスに報告にいこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0xC)
    Jump("loc_5EF5")

    label("loc_5EC1")


    #C0214
    ChrTalk(
        0x101,
        (
            "#00000Fああ、そろそろ他の場所を\x01",
            "回らないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EF5")

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

    # Function_44_5B32 end

    def Function_45_5F2F(): pass

    label("Function_45_5F2F")

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

    def lambda_6153():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6153)
    Sleep(100)

    def lambda_6170():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6170)
    Sleep(500)

    def lambda_618D():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_618D)
    Sleep(250)

    def lambda_61AA():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_61AA)

    def lambda_61C4():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_61C4)
    Sleep(350)
    OP_93(0x17, 0x5A, 0x1F4)

    def lambda_61E8():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_61E8)
    Sleep(150)
    OP_93(0xD, 0x5A, 0x1F4)

    def lambda_620C():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_620C)

    def lambda_6226():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6226)
    Sleep(250)

    def lambda_6243():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6243)
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

    def lambda_62A7():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_62A7)
    Sleep(150)

    def lambda_62C4():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_62C4)

    def lambda_62DE():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_62DE)
    Sleep(250)

    def lambda_62FB():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_62FB)
    Sleep(50)

    def lambda_6318():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6318)

    def lambda_6332():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6332)
    Sleep(500)
    OP_93(0x17, 0x5A, 0x1F4)

    def lambda_6356():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6356)
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

    def lambda_63C4():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_63C4)
    Sleep(150)

    def lambda_63E1():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_63E1)
    Sleep(50)

    def lambda_63FE():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_63FE)
    Sleep(150)

    def lambda_641B():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_641B)
    Sleep(200)

    def lambda_6438():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6438)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6597")
    SetChrFlags(0xB, 0x10)

    label("loc_6597")

    SetChrPos(0xE, 32800, -6500, -36950, 315)
    SetChrPos(0x11, 5770, 0, -8300, 270)
    SetChrPos(0x12, 4420, 0, -8080, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0215
    ChrTalk(
        0x13,
        (
            "#04100F……ご苦労だったな、特務支援課。\x02\x03",

            "おかげで、旧市街の皆も\x01",
            "少しだけ元気を取り戻したようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        "#00000F力になれたなら幸いだよ。\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        (
            "#00108Fまだ、いろいろと問題は\x01",
            "残っていそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        (
            "#00303Fヴァルドの舎弟どもも\x01",
            "しばらく落ち込んでるだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x105,
        (
            "#10306Fそもそも、\x01",
            "バイパーたちはほとんど\x01",
            "入院しているしね。\x02\x03",

            "#10300Fま、そこはあのディーノ君が\x01",
            "フォローしてくれるでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#00200Fそれが一番いいような\x01",
            "気はします。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x109,
        "#10103Fそうだね……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x13,
        (
            "#04100Fともあれ、これで依頼は終了だ。\x02\x03",

            "また何かあったら\x01",
            "旧市街の連中に力を貸してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#00000Fああ、分かった。\x01",
            "またいつでも呼んでくれ。\x02",
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
            "クエスト【旧市街の復興支援】\x07\x00",
            "を達成した！\x02",
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

    # Function_45_5F2F end

    def Function_46_68C6(): pass

    label("Function_46_68C6")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_46_68C6 end

    def Function_47_68EF(): pass

    label("Function_47_68EF")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    OP_97(0xFE, 0x3E8, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xE, 500)
    Sleep(500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_47_68EF end

    def Function_48_692C(): pass

    label("Function_48_692C")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_97(0xFE, 0x7D0, 0x0, 0x7D0, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_48_692C end

    def Function_49_6966(): pass

    label("Function_49_6966")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_97(0xFE, 0x7D0, 0x0, 0x7D0, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xA, 500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_49_6966 end

    def Function_50_69A0(): pass

    label("Function_50_69A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AB8")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_69E3"),
        (1, "loc_69FD"),
        (2, "loc_6A17"),
        (3, "loc_6A31"),
        (4, "loc_6A4B"),
        (5, "loc_6A65"),
        (6, "loc_6A7F"),
        (SWITCH_DEFAULT, "loc_6A99"),
    )


    label("loc_69E3")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6AB3")

    label("loc_69FD")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_6AB3")

    label("loc_6A17")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_6AB3")

    label("loc_6A31")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6AB3")

    label("loc_6A4B")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_6AB3")

    label("loc_6A65")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_6AB3")

    label("loc_6A7F")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6AB3")

    label("loc_6A99")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6AB3")

    label("loc_6AB3")

    Jump("Function_50_69A0")

    label("loc_6AB8")

    Return()

    # Function_50_69A0 end

    SaveToFile()

Try(main)
