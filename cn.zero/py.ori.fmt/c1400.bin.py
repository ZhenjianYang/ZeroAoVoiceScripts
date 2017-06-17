from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1400.bin",                # FileName
        "c1400",                    # MapName
        "c1400",                    # Location
        0x002E,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 46, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1400",                  # 0
        "迪诺",                   # 1
        "帕欧拉婆婆",             # 2
        "王",                     # 3
        "露茜",                   # 4
        "卡农",                   # 5
        "修伊",                   # 6
        "斯拉修",                 # 7
        "琴兹",                   # 8
        "哈缇娜修女",             # 9
        "寇奇",                   # 10
        "蓝衣青年",               # 11
        "蓝衣青年",               # 12
        "蓝衣青年",               # 13
        "蓝衣青年",               # 14
        "红衣青年",               # 15
        "红衣青年",               # 16
        "红衣青年",               # 17
        "红衣青年",               # 18
        "瓦吉",                   # 19
        "瓦鲁多",                 # 20
        "阿巴斯",                 # 21
        "格蕾丝",                 # 22
        "良",                     # 23
        "贝赛",                   # 24
        "亚泽尔",                 # 25
        "杰德",                   # 26
        "BC1400",                 # 27
        "BC1400",                 # 28
        "BC1400",                 # 29
        "BC1400",                 # 30
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

    ATBonus("ATBonus_708", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_7C8", 7, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_7CC", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D0", 10, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_7AC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_7B0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_7B4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_7B8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_7BC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_7C0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_7E8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7EC", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F4", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_800", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_804", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_808", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_80C", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_810", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_814", 11, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_818", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_81C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_820", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_824", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_828", 10, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_82C", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_830", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_834", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_838", 4, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_83C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_840", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_844", 3, 10, 180)

    # monster count: 0

    # event battle count: 4

    BattleInfo(
        "BattleInfo_848", 0x0002, 3, 6, 180, 0, 0, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms30800.dat", "ms31700.dat", "ms30900.dat", "ms31800.dat", 0, 0, 0, 0, "MonsterBattlePostion_7C8", "MonsterBattlePostion_7A8", "ed7401", "ed7403", "ATBonus_708"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_88C", 0x0002, 26, 6, 180, 0, 1, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31801.dat", "ms30901.dat", "ms30902.dat", "ms30903.dat", 0, 0, 0, 0, "MonsterBattlePostion_7E8", "MonsterBattlePostion_7A8", "ed7401", "ed7403", "ATBonus_708"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_8D0", 0x0002, 26, 6, 180, 0, 1, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31701.dat", "ms30801.dat", "ms31702.dat", "ms30802.dat", 0, 0, 0, 0, "MonsterBattlePostion_808", "MonsterBattlePostion_7A8", "ed7401", "ed7403", "ATBonus_708"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_914", 0x0022, 26, 6, 180, 0, 1, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31801.dat", "ms30901.dat", "ms30902.dat", "ms30903.dat", "ms31701.dat", "ms30801.dat", "ms31702.dat", "ms30802.dat", "MonsterBattlePostion_828", "MonsterBattlePostion_7A8", "ed7402", "ed7403", "ATBonus_708"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch06800.itc",                   # 00
        "chr/ch23302.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch24700.itc",                   # 03
        "chr/ch23800.itc",                   # 04
        "chr/ch31700.itc",                   # 05
        "chr/ch30800.itc",                   # 06
        "chr/ch31800.itc",                   # 07
        "chr/ch25500.itc",                   # 08
    ))

    DeclNpc(44880,   -2500,   -20090,  225,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(15449,   100,     -19,     270,  261,  0x0, 0,   1,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(9640,    0,       850,     180,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10279,   0,       -550,    315,  261,  0x0, 0,   3,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(34080,   -6500,   -38270,  45,   261,  0x0, 0,   4,   0,   0,   1,   0,   18,  255,  0)
    DeclNpc(45090,   -2500,   -21969,  180,  405,  0x0, 0,   5,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(45099,   -2500,   -23700,  0,    405,  0x0, 0,   6,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-17750,  0,       -9270,   225,  405,  0x0, 0,   7,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(1590,    0,       6789,    180,  389,  0x0, 0,   8,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(43650,   -2500,   -19120,  135,  389,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
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

    DeclEvent(0x0000, 0, 37,  -19.450000762939453,   -6.659999847412109,    -0.7099999785423279,   16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.862500190734863,     3.3299999237060547,    0.1420000046491623,    1.0])

    DeclActor(-28460,  2800,    -29590,  1200,    -28460,  3800,    -29590,  0x007C, 0,  6,  0x0000)
    DeclActor(-13130,  0,       -7750,   1500,    -13130,  1500,    -7750,   0x007C, 0,  39, 0x0000)
    DeclActor(48640,   -2100,   -22590,  1500,    48640,   -600,    -22590,  0x007C, 0,  38, 0x0000)
    DeclActor(34830,   2450,    -19780,  1500,    34830,   3950,    -19780,  0x007C, 0,  40, 0x0000)

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
    PlaceName(-97.75, 0.0, 93.1500015258789, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_A50",          # 00, 0
        "Function_1_B08",          # 01, 1
        "Function_2_B33",          # 02, 2
        "Function_3_C0C",          # 03, 3
        "Function_4_C55",          # 04, 4
        "Function_5_11B8",         # 05, 5
        "Function_6_12F1",         # 06, 6
        "Function_7_1427",         # 07, 7
        "Function_8_1FF0",         # 08, 8
        "Function_9_2128",         # 09, 9
        "Function_10_231A",        # 0A, 10
        "Function_11_2717",        # 0B, 11
        "Function_12_2E84",        # 0C, 12
        "Function_13_36B3",        # 0D, 13
        "Function_14_3768",        # 0E, 14
        "Function_15_3802",        # 0F, 15
        "Function_16_3911",        # 10, 16
        "Function_17_39DB",        # 11, 17
        "Function_18_3F22",        # 12, 18
        "Function_19_4A15",        # 13, 19
        "Function_20_4B3D",        # 14, 20
        "Function_21_4D00",        # 15, 21
        "Function_22_4D5B",        # 16, 22
        "Function_23_5146",        # 17, 23
        "Function_24_5279",        # 18, 24
        "Function_25_5684",        # 19, 25
        "Function_26_69CE",        # 1A, 26
        "Function_27_9AF4",        # 1B, 27
        "Function_28_9B2A",        # 1C, 28
        "Function_29_9B60",        # 1D, 29
        "Function_30_9BBB",        # 1E, 30
        "Function_31_9C20",        # 1F, 31
        "Function_32_9C66",        # 20, 32
        "Function_33_9CB0",        # 21, 33
        "Function_34_9CF1",        # 22, 34
        "Function_35_AB48",        # 23, 35
        "Function_36_BFA2",        # 24, 36
        "Function_37_CAE8",        # 25, 37
        "Function_38_CBCC",        # 26, 38
        "Function_39_CCEC",        # 27, 39
        "Function_40_CD3D",        # 28, 40
        "Function_41_CE01",        # 29, 41
        "Function_42_D438",        # 2A, 42
        "Function_43_D691",        # 2B, 43
        "Function_44_DAC1",        # 2C, 44
        "Function_45_DE68",        # 2D, 45
        "Function_46_F1DB",        # 2E, 46
        "Function_47_FE0E",        # 2F, 47
        "Function_48_FE26",        # 30, 48
        "Function_49_FE3E",        # 31, 49
        "Function_50_10582",       # 32, 50
        "Function_51_10F39",       # 33, 51
        "Function_52_1162D",       # 34, 52
        "Function_53_11642",       # 35, 53
        "Function_54_11657",       # 36, 54
        "Function_55_1166C",       # 37, 55
        "Function_56_11681",       # 38, 56
        "Function_57_116A7",       # 39, 57
        "Function_58_116F8",       # 3A, 58
        "Function_59_11749",       # 3B, 59
        "Function_60_1179A",       # 3C, 60
        "Function_61_117EB",       # 3D, 61
    ))


    def Function_0_A50(): pass

    label("Function_0_A50")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_A90"),
        (1, "loc_A9C"),
        (2, "loc_AA8"),
        (3, "loc_AB4"),
        (4, "loc_AC0"),
        (5, "loc_ACC"),
        (6, "loc_AD8"),
        (SWITCH_DEFAULT, "loc_AE4"),
    )


    label("loc_A90")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_A9C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AA8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AB4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AC0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_ACC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AD8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AE4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AF0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B07")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_B07")

    Return()

    # Function_0_A50 end

    def Function_1_B08(): pass

    label("Function_1_B08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B32")
    OP_94(0xFE, 0x8D04, 0xFFFF6E7E, 0x7800, 0xFFFF612C, 0x3E8)
    Sleep(300)
    Jump("Function_1_B08")

    label("loc_B32")

    Return()

    # Function_1_B08 end

    def Function_2_B33(): pass

    label("Function_2_B33")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C0B")
    OP_95(0xFE, 5840, 0, -6890, 5000, 0x0)
    OP_95(0xFE, 13450, -1420, -18510, 5000, 0x0)
    OP_95(0xFE, 21750, -2500, -24790, 5000, 0x0)
    OP_95(0xFE, 21750, -6500, -38390, 5000, 0x0)
    OP_95(0xFE, 7790, -6320, -37990, 5000, 0x0)
    OP_95(0xFE, -3730, -3830, -27600, 5000, 0x0)
    OP_95(0xFE, -12250, -3030, -23600, 5000, 0x0)
    OP_95(0xFE, -12250, 0, -12120, 5000, 0x0)
    OP_95(0xFE, -10970, 0, -11360, 5000, 0x0)
    OP_95(0xFE, -5510, 0, -7900, 5000, 0x0)
    Jump("Function_2_B33")

    label("loc_C0B")

    Return()

    # Function_2_B33 end

    def Function_3_C0C(): pass

    label("Function_3_C0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C54")
    Sleep(4000)
    OP_95(0xFE, -6960, -3800, -27910, 1000, 0x0)
    Sleep(4000)
    OP_95(0xFE, -13650, -3010, -25240, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x12C)
    Sleep(1900)
    Jump("Function_3_C0C")

    label("loc_C54")

    Return()

    # Function_3_C0C end

    def Function_4_C55(): pass

    label("Function_4_C55")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D32")
    SetChrPos(0x0, 2050, 0, 14590, 180)
    SetChrPos(0x1, 2050, 0, 14590, 180)
    SetChrPos(0x2, 2050, 0, 14590, 180)
    SetChrPos(0x3, 2050, 0, 14590, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CDC")
    SetChrPos(0x4, 2050, 0, 14590, 180)
    SetChrPos(0x5, 2050, 0, 14590, 180)
    Jump("loc_CFB")

    label("loc_CDC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFB")
    SetChrPos(0x4, 2050, 0, 14590, 180)

    label("loc_CFB")

    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D32")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D51")
    Event(0, 41)
    Jump("loc_D9B")

    label("loc_D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D67")
    Event(0, 35)
    Jump("loc_D9B")

    label("loc_D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D82")
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_D9B")

    label("loc_D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9B")
    Event(0, 36)

    label("loc_D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_DAF")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 26)
    Jump("loc_DBE")

    label("loc_DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_DBE")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 43)

    label("loc_DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_DDB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_11A0")

    label("loc_DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_E26")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_11A0")

    label("loc_E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E4C")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_E47")
    SetChrFlags(0x8, 0x80)

    label("loc_E47")

    Jump("loc_11A0")

    label("loc_E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E5F")
    SetChrFlags(0x8, 0x80)
    Jump("loc_11A0")

    label("loc_E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_E77")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_11A0")

    label("loc_E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_E99")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_11A0")

    label("loc_E99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_EFA")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 11340, 0, 1320, 225)
    OP_93(0x8, 0x2D, 0x0)
    TurnDirection(0xA, 0x10, 0)
    TurnDirection(0xB, 0x10, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDC")
    SetChrFlags(0x8, 0x10)

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF5")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x10, 0x10)

    label("loc_EF5")

    Jump("loc_11A0")

    label("loc_EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_F75")
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_F38")
    SetChrPos(0xA, -10970, 0, -9240, 135)
    SetChrPos(0xB, -11920, 0, -9620, 45)
    Jump("loc_F70")

    label("loc_F38")

    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)

    label("loc_F70")

    Jump("loc_11A0")

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_FB4")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xD, 2820, 0, -2350, 45)
    SetChrPos(0xE, 3020, 0, -950, 45)
    Jump("loc_11A0")

    label("loc_FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_FF7")
    SetChrPos(0xA, 1220, 0, -1610, 135)
    SetChrPos(0xB, 2410, 0, -2740, 315)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FF2")
    SetChrFlags(0xA, 0x10)

    label("loc_FF2")

    Jump("loc_11A0")

    label("loc_FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1058")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -11120, -220, -14560, 45)
    SetChrPos(0xB, -11150, -820, -15530, 45)
    SetChrPos(0xD, 5010, 0, -7740, 0)
    SetChrPos(0xE, 4090, 0, -6750, 45)
    Jump("loc_11A0")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_10BD")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    OP_93(0x8, 0x13B, 0x0)
    SetChrFlags(0x8, 0x10)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_10B8")
    SetChrFlags(0x11, 0x10)

    label("loc_10B8")

    Jump("loc_11A0")

    label("loc_10BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1112")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_11A0")

    label("loc_1112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_1172")
    SetChrPos(0xA, 8620, 0, 8810, 180)
    SetChrPos(0xB, 7900, 0, 9630, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_115C")
    SetChrPos(0x8, 44880, -2500, -20090, 225)
    Jump("loc_116D")

    label("loc_115C")

    SetChrPos(0x8, 48000, -2100, -22500, 270)

    label("loc_116D")

    Jump("loc_11A0")

    label("loc_1172")

    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x8, 48000, -2100, -22500, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_11A0")
    SetChrFlags(0xA, 0x10)

    label("loc_11A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11B7")
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_11B7")

    Return()

    # Function_4_C55 end

    def Function_5_11B8(): pass

    label("Function_5_11B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11CF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11F9")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_122C")

    label("loc_11F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_121E")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_122C")

    label("loc_121E")

    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_122C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123F")
    OP_70(0x7, 0x0)
    Jump("loc_1243")

    label("loc_123F")

    OP_70(0x7, 0x1E)

    label("loc_1243")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_125B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_125B")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1279")
    ClearMapObjFlags(0x4, 0x10)

    label("loc_1279")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1291")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_1291")

    OP_65(0x3, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AF")
    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_12AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CB")
    Jump("loc_12D0")

    label("loc_12CB")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_12D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F0")
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_12F0")

    Return()

    # Function_5_11B8 end

    def Function_6_12F1(): pass

    label("Function_6_12F1")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DE")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('加速跑鞋', 1)"), scpexpr(EXPR_END)), "loc_1370")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '加速跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_13D9")

    label("loc_1370")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '加速跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '加速跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13D9")

    Jump("loc_141B")

    label("loc_13DE")

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

    label("loc_141B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_12F1 end

    def Function_7_1427(): pass

    label("Function_7_1427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_143D")
    Call(0, 34)
    Jump("loc_1FEF")

    label("loc_143D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1458")
    Call(0, 10)
    Jump("loc_1FEF")

    label("loc_1458")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_154B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14E0")

    #C0004
    ChrTalk(
        0x8,
        (
            "……要进去吗？\x01",
            "里面的家伙现在正吓得发抖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "哈哈哈，这样一来，从明天开始，\x01",
            "我就是剑蛇帮的大干部啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1546")

    label("loc_14E0")


    #C0006
    ChrTalk(
        0x8,
        "哈哈，真是太爽了！\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "我以前就看那家伙很不顺眼了。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "老是强迫别人做一些\x01",
            "打杂跑腿的事……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1546")

    Jump("loc_1FEC")

    label("loc_154B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_16CF")
    OP_64(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167B")

    #C0009
    ChrTalk(
        0xFE,
        (
            "我……在纪念庆典的最终日\x01",
            "被一个不好惹的游客缠住……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "虽然尽全力和他战斗了……\x01",
            "但、但还是输了……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "我明明是剑蛇帮的成员，竟然……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1670")

    #C0012
    ChrTalk(
        0x101,
        (
            "#0003F是、是吗……\x01",
            "（这个人好像不太擅长格斗啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x153,
        (
            "#1111F？？？\x01",
            "（好奇怪的打扮哦～）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1670")

    SetScenarioFlags(0xD8, 2)
    SetScenarioFlags(0x0, 0)
    Jump("loc_16B8")

    label("loc_167B")


    #C0014
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "我明明是剑蛇帮的成员，竟然……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B8")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1FEC")

    label("loc_16CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1713")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_170B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 0)), scpexpr(EXPR_END)), "loc_16F5")
    Call(0, 8)
    Jump("loc_1706")

    label("loc_16F5")

    TurnDirection(0x8, 0x0, 0)
    Call(0, 9)
    OP_93(0x8, 0x2D, 0x0)

    label("loc_1706")

    Jump("loc_170E")

    label("loc_170B")

    Call(0, 8)

    label("loc_170E")

    Jump("loc_1FEC")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_17E7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 0)), scpexpr(EXPR_END)), "loc_175B")

    #C0015
    ChrTalk(
        0x8,
        (
            "我、我以后也是要\x01",
            "参加战斗的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_175B")

    Call(0, 9)

    label("loc_175E")

    Jump("loc_17E2")

    label("loc_1763")


    #C0016
    ChrTalk(
        0x8,
        (
            "好羡慕啊，我也想参加\x01",
            "早上的训练啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "嘿嘿……努力参加训练，\x01",
            "然后总有一天，我也要成为\x01",
            "像瓦鲁多大哥那么强的男人……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E2")

    Jump("loc_1FEC")

    label("loc_17E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1915")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_186C")

    #C0018
    ChrTalk(
        0xFE,
        (
            "我也是剑蛇帮的成员。\x01",
            "从今年开始，在庆典时期也不能再玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "……话先说在前面，\x01",
            "我可没有觉得遗憾哦！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1910")

    label("loc_186C")


    #C0020
    ChrTalk(
        0xFE,
        (
            "随着纪念庆典的临近，\x01",
            "老是能看见一些满脸兴奋的家伙……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "哼、哼，真是够幼稚的哦。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "我们剑蛇帮是硬派组织，\x01",
            "才不会因为庆典这种无聊的活动\x01",
            "而觉得兴奋呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1910")

    Jump("loc_1FEC")

    label("loc_1915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_196F")

    #C0023
    ChrTalk(
        0x8,
        "我已经不会再受骗了。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "去去，一边去！\x01",
            "你们打扰到前辈们啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A03")

    label("loc_196F")


    #C0025
    ChrTalk(
        0x8,
        "噢，您辛苦了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0026
    ChrTalk(
        0x8,
        "我说，怎么又是你们啊！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "真是的……\x01",
            "是故意来捣乱的吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0006F不，我们并不是故意\x01",
            "来捣乱的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A03")

    Jump("loc_1FEC")

    label("loc_1A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1BE0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1ABF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A69")

    #C0029
    ChrTalk(
        0x8,
        (
            "我很有礼貌地打了招呼！\x01",
            "不过瓦鲁多大哥\x01",
            "只是哦了一声而已！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABA")

    label("loc_1A69")


    #C0030
    ChrTalk(
        0x8,
        (
            "刚才瓦鲁多大哥\x01",
            "回来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "噢，您辛苦了！\x01",
            "……我很有礼貌地打了招呼！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1ABA")

    Jump("loc_1BDB")

    label("loc_1ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B7A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B52")

    #C0032
    ChrTalk(
        0xFE,
        (
            "话说，好像一直有咚咚啪啪\x01",
            "的怪声音啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "好像也不是从鬼火中传来的……\x01",
            "到底是哪里的声音呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B75")

    label("loc_1B52")


    #C0034
    ChrTalk(
        0x8,
        (
            "前辈们都很忙啊！\x01",
            "不要来捣乱！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B75")

    Jump("loc_1BDB")

    label("loc_1B7A")


    #C0035
    ChrTalk(
        0x8,
        "噢，您辛苦了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x8,
        "怎么，是你们啊！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "真是的……\x01",
            "不要来添乱啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BDB")

    Jump("loc_1FEC")

    label("loc_1BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1C3E")
    OP_4B(0x11, 0xFF)

    #C0038
    ChrTalk(
        0x8,
        "喔！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x11,
        "不是喔，是噢才对！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0040
    ChrTalk(
        0x8,
        "噢、噢！\x02",
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_4C(0x11, 0xFF)
    Jump("loc_1FEC")

    label("loc_1C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1D15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C9B")

    #C0041
    ChrTalk(
        0x8,
        (
            "我接下来要去\x01",
            "医院探病。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "……要是敢碍事，\x01",
            "我可不会轻饶你们！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D10")

    label("loc_1C9B")


    #C0043
    ChrTalk(
        0x8,
        (
            "被圣书会的那些家伙\x01",
            "打伤的是一位名叫\x01",
            "寇奇的前辈。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "在组织中，他可是\x01",
            "最关照我的人，但竟然……\x01",
            "……呜呜……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D10")

    Jump("loc_1FEC")

    label("loc_1D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1E7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D59")

    #C0045
    ChrTalk(
        0x8,
        (
            "赶、赶快回去！\x01",
            "我再也不会相信你们了！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E76")

    label("loc_1D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 6)), scpexpr(EXPR_END)), "loc_1DB2")

    #C0046
    ChrTalk(
        0x8,
        "竟、竟然把瓦鲁多大哥……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "赶、赶快回去！\x01",
            "我再也不会相信你们了！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E14")

    label("loc_1DB2")


    #C0048
    ChrTalk(
        0x8,
        (
            "竟、竟然能和瓦鲁多大哥\x01",
            "打成平手……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "你小子，肯定耍了什么卑鄙手段吧！\x01",
            "别以为我不知道！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E14")


    #C0050
    ChrTalk(
        0x101,
        "#0003F（嗯～这孩子可真是……）\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0300F（哈哈，他好像很崇拜\x01",
            "  那个叫瓦鲁多的家伙呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E76")

    Jump("loc_1FEC")

    label("loc_1E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1EF9")

    #C0052
    ChrTalk(
        0x8,
        "瓦鲁多大哥叫你们进去！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "光是进去的话当然没关系……\x01",
            "但如果敢做出什么可疑的举动，\x01",
            "我可不会轻易放过你们！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEC")

    label("loc_1EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_1F88")

    #N0054
    NpcTalk(
        0xFE,
        "红衣少年",
        (
            "喂，可恶的警察，\x01",
            "看什么看啊！\x02",
        )
    )

    CloseMessageWindow()

    #N0055
    NpcTalk(
        0xFE,
        "红衣少年",
        "赶快滚回去！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0001F（没办法……\x01",
            "  还是先去另一个\x01",
            "  组织看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEC")

    label("loc_1F88")


    #N0057
    NpcTalk(
        0x8,
        "红衣少年",
        (
            "你、你们是干什么的！\x01",
            "有什么好看的啊！\x02",
        )
    )

    CloseMessageWindow()

    #N0058
    NpcTalk(
        0x8,
        "红衣少年",
        "快点给我滚到一边去！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FEC")
    SetScenarioFlags(0x53, 4)

    label("loc_1FEC")

    TalkEnd(0xFE)

    label("loc_1FEF")

    Return()

    # Function_7_1427 end

    def Function_8_1FF0(): pass

    label("Function_8_1FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2065")

    #C0059
    ChrTalk(
        0x8,
        (
            "用不了多久，我也就是\x01",
            "有木刀的人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "到时候，不管是你们，\x01",
            "还是圣书会的家伙，\x01",
            "我都能轻松干掉！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2127")

    label("loc_2065")


    #C0061
    ChrTalk(
        0x8,
        (
            "喝哈……！\x01",
            "看招～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0062
    ChrTalk(
        0x8,
        "干、干什么啊！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "我正在练习格斗呢。\x01",
            "不要来捣乱！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#0305F练习格斗……\x01",
            "用这种幻想的方式吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "这、这也是没办法的吧！\x01",
            "毕竟我没有木刀！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x0)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_2127")

    Return()

    # Function_8_1FF0 end

    def Function_9_2128(): pass

    label("Function_9_2128")


    #C0066
    ChrTalk(
        0x8,
        (
            "你、你们几个！\x01",
            "来干什么的啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        "小、小、小……小心我打扁你们啊！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0002F那个，一直在努力看守，真是辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        "呜呜，少看不起人！\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "下、下一次的战斗，\x01",
            "我也会参加的！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        (
            "#0205F说起来……你好像\x01",
            "都不参加训练呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "……杰德前辈之前把我扔下不管，\x01",
            "跑去打架了……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "啊，不过他已经回来了！\x01",
            "我并没有觉得寂寞啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#0303F啊～那个，抱歉，\x01",
            "是我们多管闲事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#0100F要是你以后也能\x01",
            "一起参加练习就好了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0076
    ChrTalk(
        0x8,
        (
            "什、什么话！\x01",
            "不是让你们不要小看我了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    SetScenarioFlags(0x91, 0)
    Return()

    # Function_9_2128 end

    def Function_10_231A(): pass

    label("Function_10_231A")

    EventBegin(0x0)
    Fade(500)
    OP_68(45000, -1500, -22500, 0)
    MoveCamera(37, 30, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 43700, -2500, -23300, 90)
    SetChrPos(0x102, 43700, -2500, -21900, 90)
    SetChrPos(0x103, 42600, -2500, -23100, 90)
    SetChrPos(0x104, 42600, -2500, -21700, 90)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 47500, -2100, -22500, 270)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0077
    NpcTalk(
        0x8,
        "红衣少年",
        "你、你们是……！\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#6P#0005F这种打扮……\x02\x03",

            "#0001F莫非这里就是\x01",
            "『剑蛇帮』的据点吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        (
            "#3P#0200F小剧场『鬼火』……\x02\x03",

            "这里原来好像是仓库，然后才被\x01",
            "改造成小剧场的。\x02\x03",

            "#0203F因为没有交纳税金，\x01",
            "所以具体情况也不太了解……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24B6():
        OP_96(0xFE, 0xB4DC, 0xFFFFF704, 0xFFFFA81C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_24B6)
    WaitChrThread(0x8, 1)

    #N0080
    NpcTalk(
        0x8,
        "红衣少年",
        "不、不要无视我啊！\x02",
    )

    CloseMessageWindow()

    #N0081
    NpcTalk(
        0x8,
        "红衣少年",
        (
            "虽说我只是个新人，\x01",
            "但好歹也是剑蛇帮的一员！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊……抱歉。\x02\x03",

            "#0000F那个……我们这次过来，\x01",
            "是有些事情想问问你们的首领……\x02\x03",

            "可以帮忙传达一声吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0083
    NpcTalk(
        0x8,
        "红衣少年",
        "找瓦鲁多大哥？\x02",
    )

    CloseMessageWindow()

    #N0084
    NpcTalk(
        0x8,
        "红衣少年",
        (
            "哼，你们这种警察局的走狗，\x01",
            "瓦鲁多大哥怎么会搭理！\x02",
        )
    )

    CloseMessageWindow()

    #N0085
    NpcTalk(
        0x8,
        "红衣少年",
        "去去，赶快滚回去！\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#6P#0003F（嗯～看样子，不像是\x01",
            "  那么轻易就能进去啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#0300F（用武力硬闯也显得\x01",
            "  太不成熟了。）\x02\x03",

            "（不然还是先去探访\x01",
            "  另一个组织吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#0101F（是啊……去过那边之后，\x01",
            "  再回这里看看好了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 48000, -2100, -22500, 270)
    SetChrPos(0x0, 43000, -2500, -22500, 90)
    SetScenarioFlags(0x52, 7)
    EventEnd(0x5)
    Return()

    # Function_10_231A end

    def Function_11_2717(): pass

    label("Function_11_2717")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27AB")
    Jump("loc_27F5")

    label("loc_27AB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_27CB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27F5")

    label("loc_27CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27EB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27F5")

    label("loc_27EB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27F5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2875")

    #C0089
    ChrTalk(
        0x9,
        (
            "啊，太阳好像都已经\x01",
            "下山了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "都这么晚了，\x01",
            "我差不多也该\x01",
            "回家了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_28BA")

    #C0091
    ChrTalk(
        0x9,
        "啊……怎么了？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "我的耳朵有点背，\x01",
            "听不太清楚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_28BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2914")

    #C0093
    ChrTalk(
        0x9,
        (
            "刚才，那边有蝴蝶\x01",
            "在飞舞呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "呵呵……天气好像\x01",
            "已经完全暖起来了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_29E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298D")

    #C0095
    ChrTalk(
        0xFE,
        (
            "最近，那些不良组织的孩子们\x01",
            "好像很奇怪的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "哎呀……我的耳朵有点背，\x01",
            "听不太清楚。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29DE")

    label("loc_298D")


    #C0097
    ChrTalk(
        0xFE,
        (
            "不过，那些红外衣的孩子们…\x01",
            "样子好像有点奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "大概是出了什么事吧……\x02",
    )

    CloseMessageWindow()

    label("loc_29DE")

    Jump("loc_2E7C")

    label("loc_29E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2A1C")

    #C0099
    ChrTalk(
        0x9,
        (
            "（半睡半醒）……\x01",
            "今天也是个好天气啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2A79")

    #C0100
    ChrTalk(
        0x9,
        "（半睡半醒）……啊，不行不行。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "天气一转暖，\x01",
            "就不自觉地开始打瞌睡了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2ADB")

    #C0102
    ChrTalk(
        0x9,
        (
            "我的腿脚不怎么好，\x01",
            "没法走太远。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "所以，看到孩子们精力十足，\x01",
            "我就会很开心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2B2B")

    #C0104
    ChrTalk(
        0x9,
        (
            "今天的晚饭\x01",
            "要做什么好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "偶尔也想吃点\x01",
            "美味的东西啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2B87")

    #C0106
    ChrTalk(
        0x9,
        "啊……有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "刚才也有人\x01",
            "想问我一些事情……\x01",
            "但我的耳朵有点背。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2BDE")

    #C0108
    ChrTalk(
        0x9,
        "啊呀，那些穿红衣服的孩子……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "最近经常能看见，\x01",
            "出了什么事吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2C8F")

    #C0110
    ChrTalk(
        0x9,
        (
            "克洛斯贝尔车站大概是\x01",
            "二十年前左右建成的。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "那个时候，市民们都为此欢欣雀跃，\x01",
            "真是骚动一时呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "现在连空港都建起来了，和以前相比，\x01",
            "实在是便利了很多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2CEC")

    #C0113
    ChrTalk(
        0x9,
        "孩子们今天也很有精神。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "阳光也这么明媚温暖，\x01",
            "想必又会是美好的一天啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2D7B")

    #C0115
    ChrTalk(
        0x9,
        (
            "那些穿红衣服的孩子们\x01",
            "经常会从这里通过。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "我的耳朵有点背，\x01",
            "不太明白他们在说什么，做什么……\x01",
            "不过大家都很有精神，这就好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_2DF3")

    #C0117
    ChrTalk(
        0x9,
        "哎呀，出什么事了吗？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "年轻的孩子们好像\x01",
            "都聚集在一起了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "我的耳朵有点背，\x01",
            "听不太清楚呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E3D")

    #C0120
    ChrTalk(
        0x9,
        (
            "哎……\x01",
            "找我有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "不好意思啊，\x01",
            "我有点耳背。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2E3D")


    #C0122
    ChrTalk(
        0x9,
        (
            "啊啊，今天也是个\x01",
            "好天气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "要不要再\x01",
            "晒晒太阳呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E7C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_2717 end

    def Function_12_2E84(): pass

    label("Function_12_2E84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2F43")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2EF5")

    #C0124
    ChrTalk(
        0xFE,
        "嘻嘻……又打起来了吗～？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "比起修女的授课，\x01",
            "还是那边更有趣啊～！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    Jump("loc_2F3E")

    label("loc_2EF5")


    #C0126
    ChrTalk(
        0xFE,
        "嘻嘻……又打起来了吗～？\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "比起修女的授课，\x01",
            "还是那边更有趣啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F3E")

    Jump("loc_36AF")

    label("loc_2F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2FBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2FB6")
    OP_4B(0xB, 0xFF)

    #C0128
    ChrTalk(
        0xA,
        (
            "我家那个臭老爸，\x01",
            "一天到晚就知道喝酒～\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "真没办法啊～\x01",
            "去他那里找点剩饭吃吧～\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_2FB9")

    label("loc_2FB6")

    Call(0, 13)

    label("loc_2FB9")

    Jump("loc_36AF")

    label("loc_2FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_300D")

    #C0130
    ChrTalk(
        0xA,
        (
            "今天没有看见那些\x01",
            "不良团伙的哥哥们呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        "呼，真没劲啊～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_36AF")

    label("loc_300D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_309D")
    OP_4B(0xB, 0xFF)

    #C0132
    ChrTalk(
        0xA,
        (
            "不良团伙的那个哥哥，\x01",
            "稍微有点可怕啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        "感觉阴森森的，很恐怖～……\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "露茜，绝对不要\x01",
            "接近他那种人哦，知道了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_36AF")

    label("loc_309D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_30F5")

    #C0135
    ChrTalk(
        0xFE,
        (
            "那个修女好像到\x01",
            "金格那里去了啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "嘻嘻……就趁现在\x01",
            "赶快藏起来吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AF")

    label("loc_30F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3106")
    Call(0, 14)
    Jump("loc_36AF")

    label("loc_3106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3144")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_313C")

    #C0137
    ChrTalk(
        0xA,
        (
            "嘻嘻，才不要去\x01",
            "上课呢～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313F")

    label("loc_313C")

    Call(0, 15)

    label("loc_313F")

    Jump("loc_36AF")

    label("loc_3144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_31E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_319A")

    #C0138
    ChrTalk(
        0xA,
        (
            "我家那个臭老爸，\x01",
            "就只知道喝酒～……¤\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        "哇哈哈哈哈哈！\x02",
    )

    CloseMessageWindow()
    Jump("loc_31E2")

    label("loc_319A")


    #C0140
    ChrTalk(
        0xA,
        (
            "哇哈哈哈！\x01",
            "露茜，今天要玩些什么～？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        "要不要来玩推箱子啊～？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_31E2")

    Jump("loc_36AF")

    label("loc_31E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3253")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_324B")
    OP_4B(0xB, 0xFF)

    #C0142
    ChrTalk(
        0xA,
        (
            "不过，老爸一天到晚\x01",
            "总是在喝酒啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        "是不是应该去把他敲醒呢～\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_324E")

    label("loc_324B")

    Call(0, 16)

    label("loc_324E")

    Jump("loc_36AF")

    label("loc_3253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_32EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3299")
    OP_4B(0xB, 0xFF)

    #C0144
    ChrTalk(
        0xA,
        (
            "嘿嘿……不然下次就去\x01",
            "抓老鼠吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_32EA")

    label("loc_3299")


    #C0145
    ChrTalk(
        0xA,
        (
            "我把蝾螈扔进\x01",
            "这下水道里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "哇哇，哇哇～！\x01",
            "啊哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x87, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_32EA")

    Jump("loc_36AF")

    label("loc_32EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3351")
    OP_4B(0xB, 0xFF)

    #C0147
    ChrTalk(
        0xA,
        (
            "不好了，露茜，\x01",
            "赶快藏起来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "嘻嘻……又是来\x01",
            "商量打群架的事吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_36AF")

    label("loc_3351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_342D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D6")

    #C0149
    ChrTalk(
        0xA,
        (
            "我的老爸还在屋子里\x01",
            "喝酒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        "都已经中午了啊。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xA,
        (
            "啊啊啊，就知道喝酒，\x01",
            "真是个无可救药的人啊～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3428")

    label("loc_33D6")


    #C0152
    ChrTalk(
        0xA,
        (
            "我的老爸好像\x01",
            "还在喝酒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xA,
        (
            "啊啊啊，就知道喝酒～\x01",
            "真是个无可救药的人啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3428")

    Jump("loc_36AF")

    label("loc_342D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3465")

    #C0154
    ChrTalk(
        0xA,
        "老爸是个超级大酒鬼～！\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xA,
        "呀哈～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_36AF")

    label("loc_3465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3513")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_34C7")

    #C0156
    ChrTalk(
        0xA,
        (
            "不良团伙的大哥哥们～\x01",
            "这次特别能忍啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xA,
        "……难道不准备打群架了吗～\x02",
    )

    CloseMessageWindow()
    Jump("loc_350E")

    label("loc_34C7")


    #C0158
    ChrTalk(
        0xA,
        (
            "哎……？\x01",
            "还以为今天能看到打群架呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        "这是怎么回事～？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_350E")

    Jump("loc_36AF")

    label("loc_3513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_35DA")
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3585")
    OP_93(0xFE, 0xB4, 0x0)

    #C0160
    ChrTalk(
        0xA,
        (
            "哈哈，真刺激呀～\x01",
            "今天终于又开战了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "露茜～\x01",
            "你绝对不要靠近啊～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35D1")

    label("loc_3585")


    #C0162
    ChrTalk(
        0xFE,
        (
            "那些大哥哥\x01",
            "一定很快就会回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿……\x01",
            "今天真是超级惊险啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D1")

    OP_4C(0xB, 0xFF)
    Jump("loc_36AF")

    label("loc_35DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_363F")

    #C0164
    ChrTalk(
        0xA,
        "嗯，下面该玩些什么好呢～？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            "哈哈哈，不然就在水管上挖个洞，\x01",
            "来个大水淹城好了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AF")

    label("loc_363F")


    #C0166
    ChrTalk(
        0xA,
        "哦，是市中心来的家伙。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        "哈，你们要小心啊～\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "这一带的不良团伙，\x01",
            "现在都紧绷着神经呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_36AF")

    TalkEnd(0xFE)
    Return()

    # Function_12_2E84 end

    def Function_13_36B3(): pass

    label("Function_13_36B3")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0169
    ChrTalk(
        0xB,
        "我今天也什么都没吃呢。\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "呜呜……我的肚子\x01",
            "都饿了啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        (
            "没办法了～\x01",
            "不然就去找点剩饭吃吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "哇哇哇哇……\x01",
            "我要吃东西～！\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        "哇呀呀，我要吃东西～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_13_36B3 end

    def Function_14_3768(): pass

    label("Function_14_3768")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0174
    ChrTalk(
        0xA,
        (
            "那个讨厌的修女，\x01",
            "最近真是很烦人。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        "为什么每周都要来啊～？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xB,
        "嘻嘻……不明白啊～\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "反正王会把她赶回去，\x01",
            "怎样都无所谓吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_14_3768 end

    def Function_15_3802(): pass

    label("Function_15_3802")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0178
    ChrTalk(
        0xA,
        "怎么，又来了吗～？\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        (
            "嘻嘻……修女真是个\x01",
            "不接受教训的姐姐～\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x10,
        "嗯，我不会放弃的。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x10,
        (
            "……好啦，我们\x01",
            "赶快走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x10,
        (
            "今天可一定要给你们\x01",
            "好好讲讲课。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        "嘻嘻，真是个嚣张的女人啊～\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x10,
        (
            "唉……首先得从措辞方面\x01",
            "教起啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_15_3802 end

    def Function_16_3911(): pass

    label("Function_16_3911")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0185
    ChrTalk(
        0xA,
        "纪念庆典～？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        "露茜，你有没有什么想去的地方啊～？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xB,
        "不，没有哦。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "只要王在就足够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        "哼，真没意思啊～\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        (
            "不然就把老爸叫起来，\x01",
            "让他带我们去哪里转转吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_16_3911 end

    def Function_17_39DB(): pass

    label("Function_17_39DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3A9C")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_3A52")

    #C0191
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "哥哥们都很强。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "如果……我以后遇到危险，\x01",
            "真希望由你们来救我呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A87")

    label("loc_3A52")


    #C0193
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "哥哥们真是很强呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        "虽然最后输了。\x02",
    )

    CloseMessageWindow()

    label("loc_3A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3A97")
    OP_93(0xFE, 0x2D, 0x0)

    label("loc_3A97")

    Jump("loc_3F1E")

    label("loc_3A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3B17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3B0F")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0195
    ChrTalk(
        0xB,
        (
            "龙老饭店的大姐姐\x01",
            "真是个温柔的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "还把东西分给我吃呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Jump("loc_3B12")

    label("loc_3B0F")

    Call(0, 13)

    label("loc_3B12")

    Jump("loc_3F1E")

    label("loc_3B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3B65")

    #C0197
    ChrTalk(
        0xB,
        (
            "我见到了那些\x01",
            "蓝衣人的头目了。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "他在干什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F1E")

    label("loc_3B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3B9E")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0199
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "嗯，明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Jump("loc_3F1E")

    label("loc_3B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3BF8")

    #C0200
    ChrTalk(
        0xFE,
        (
            "修女讲的课，\x01",
            "金格连一次都没有听过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "修女也真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F1E")

    label("loc_3BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3C09")
    Call(0, 14)
    Jump("loc_3F1E")

    label("loc_3C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3C7B")

    #C0202
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "那个修女姐姐\x01",
            "真是不接受教训啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        (
            "平时明明就总是被王欺负，\x01",
            "竟然还会跑来～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C7E")

    label("loc_3C7B")

    Call(0, 15)

    label("loc_3C7E")

    Jump("loc_3F1E")

    label("loc_3C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3CC8")

    #C0204
    ChrTalk(
        0xB,
        "呀哈哈哈！\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        (
            "边跑边说话，\x01",
            "就、就会喘不过气啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F1E")

    label("loc_3CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3D1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D13")

    #C0206
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "庆典开始之后，\x01",
            "哥哥们准备玩什么呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D16")

    label("loc_3D13")

    Call(0, 16)

    label("loc_3D16")

    Jump("loc_3F1E")

    label("loc_3D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3D62")

    #C0207
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "蝾螈，这就是最后一击啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        "啪啪，啪～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F1E")

    label("loc_3D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3DA9")

    #C0209
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "肚子好饿啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        "真希望能捡到什么吃的啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F1E")

    label("loc_3DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3DF6")

    #C0211
    ChrTalk(
        0xB,
        (
            "呵呵……王可真是幸福啊，\x01",
            "还有个爸爸。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xB,
        "虽然是个酒鬼。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F1E")

    label("loc_3DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3E24")

    #C0213
    ChrTalk(
        0xB,
        "呀哈哈！等一下，等一下～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F1E")

    label("loc_3E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3E65")

    #C0214
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "已经吃够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xB,
        "差不多也该去玩啦～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F1E")

    label("loc_3E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_3EBD")
    OP_4B(0xA, 0xFF)
    OP_93(0xFE, 0x87, 0x0)

    #C0216
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "喂，情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xB,
        "已经进展到什么程度啦？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_3F1E")

    label("loc_3EBD")


    #C0218
    ChrTalk(
        0xB,
        (
            "不良团伙的那些哥哥，\x01",
            "最近看上去好像很烦躁。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "市区来的哥哥们，\x01",
            "你们也要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F1E")

    TalkEnd(0xFE)
    Return()

    # Function_17_39DB end

    def Function_18_3F22(): pass

    label("Function_18_3F22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3FA0")

    #C0220
    ChrTalk(
        0xC,
        "呼，开始有点困了呢……\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xC,
        (
            "今天也做了很多工作，\x01",
            "必须要在天色变暗之前回家啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xC,
        "因为明天也要早起呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A11")

    label("loc_3FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4058")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3FE4")

    #C0223
    ChrTalk(
        0xC,
        (
            "商人们肯定会很高兴吧。\x01",
            "呵呵，真期待啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4053")

    label("loc_3FE4")


    #C0224
    ChrTalk(
        0xC,
        "扫除，扫除……\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        (
            "今天多收集些破铜烂铁，\x01",
            "到时候会有商人来收购的。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "呵呵，商人们应该会\x01",
            "很高兴吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4053")

    Jump("loc_4A11")

    label("loc_4058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_40E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4099")

    #C0227
    ChrTalk(
        0xC,
        (
            "最近总是能听到\x01",
            "怒吼声，\x01",
            "真担心啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40E1")

    label("loc_4099")


    #C0228
    ChrTalk(
        0xC,
        (
            "那些不良团伙的成员们\x01",
            "到底是怎么了……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xC,
        "总觉得有点担心呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_40E1")

    Jump("loc_4A11")

    label("loc_40E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_416A")

    #C0230
    ChrTalk(
        0xC,
        (
            "这石板路上镶嵌着各式各样的石头，\x01",
            "看着它，心情就会平静下来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xC,
        (
            "一边看着石板路，一边打扫，\x01",
            "每天干都不会厌烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A11")

    label("loc_416A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_41C0")
    TurnDirection(0xC, 0x153, 0)

    #C0232
    ChrTalk(
        0xC,
        "打扫的事就交给我吧。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xC,
        "我早就做惯了，很轻松啦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4271")

    label("loc_41C0")


    #C0234
    ChrTalk(
        0xC,
        (
            "你们好啊！\x01",
            "今天的天气也不错啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x153, 0)

    #C0235
    ChrTalk(
        0xC,
        (
            "哎……没见过的小女孩呢……\x01",
            "你也要帮我一起来打扫吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xC,
        (
            "呵呵，虽然很高兴，不过这可不行哦。\x01",
            "因为地上可能会有一些玻璃碎片呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4271")

    Jump("loc_4A11")

    label("loc_4276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_435F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_42CA")

    #C0237
    ChrTalk(
        0xC,
        "我最喜欢庆典了。\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xC,
        (
            "真兴奋……\x01",
            "纪念庆典，快点到来吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_435A")

    label("loc_42CA")


    #C0239
    ChrTalk(
        0xC,
        (
            "只要一听到纪念庆典这四个字，\x01",
            "我就会感觉很兴奋了。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xC,
        "激动，激动……！\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xC,
        "我最喜欢庆典了。\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xC,
        "因为每到这个时候，大家都会笑容满面。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_435A")

    Jump("loc_4A11")

    label("loc_435F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4446")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_43BE")

    #C0243
    ChrTalk(
        0xC,
        (
            "我搞不懂那些\x01",
            "复杂的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xC,
        (
            "不过……\x01",
            "打扫卫生倒是我的特长啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4441")

    label("loc_43BE")


    #C0245
    ChrTalk(
        0xC,
        (
            "扫啊扫……\x01",
            "今天，圣书会的人\x01",
            "还和我打招呼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xC,
        (
            "他们最近正在\x01",
            "这一带巡逻。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "好像说是要保持警戒，\x01",
            "不让黑手党的人进来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4441")

    Jump("loc_4A11")

    label("loc_4446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4562")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_44B1")

    #C0248
    ChrTalk(
        0xC,
        "咦，你们不是政府官员吗？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xC,
        (
            "不好意思啊，\x01",
            "最近总是有政府官员来，\x01",
            "我都搞错了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_455D")

    label("loc_44B1")


    #C0250
    ChrTalk(
        0xC,
        (
            "你们好啊！\x01",
            "……你们是政府部门的官员吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xC,
        (
            "我每天都会在这里打扫卫生，\x01",
            "所以很干净哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        "呵呵，今天也是一尘不染呢！\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "打扫得这么干净，\x01",
            "就算躺上去都没问题哦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_455D")

    Jump("loc_4A11")

    label("loc_4562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4645")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_45C0")

    #C0254
    ChrTalk(
        0xC,
        (
            "我每天早上都会和\x01",
            "那位狼先生打个招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        "它看上去真是非常聪明。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4640")

    label("loc_45C0")


    #C0256
    ChrTalk(
        0xC,
        (
            "就在早上，有头很大的白狼\x01",
            "从这里经过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xC,
        (
            "它有一身很漂亮的毛，\x01",
            "而且好像非常聪明呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xC,
        (
            "呵呵，它是在这一带\x01",
            "巡逻吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4640")

    Jump("loc_4A11")

    label("loc_4645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_46FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_46A8")

    #C0259
    ChrTalk(
        0xC,
        (
            "从早上开始，我一直\x01",
            "在打扫这条街道。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xC,
        (
            "呵呵，是不是\x01",
            "变得很干净了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F8")

    label("loc_46A8")


    #C0261
    ChrTalk(
        0xC,
        "啊，你们好！\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        "呵呵，看啊，看啊！\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xC,
        (
            "这一带是不是\x01",
            "变得非常干净啦？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_46F8")

    Jump("loc_4A11")

    label("loc_46FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4803")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4750")

    #C0264
    ChrTalk(
        0xC,
        (
            "经常会有一些商人\x01",
            "来这里收购钉子、\x01",
            "碎金属之类的东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47FE")

    label("loc_4750")


    #C0265
    ChrTalk(
        0xC,
        (
            "只要看到钉子和碎金属，\x01",
            "我就会把它们装进袋子里。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xC,
        (
            "把它们分门别类地整理好，\x01",
            "到时就会有商人来上门收购啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xC,
        (
            "既能挣钱，又能让街道变得干净整洁，\x01",
            "这不是一举两得吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_47FE")

    Jump("loc_4A11")

    label("loc_4803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_48A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4845")

    #C0268
    ChrTalk(
        0xC,
        (
            "扫啊扫，扫啊扫……\x01",
            "今天也要努力扫除。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_489B")

    label("loc_4845")


    #C0269
    ChrTalk(
        0xC,
        "你们好，真是个美好的早晨啊！\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        (
            "我是来看朝阳的。\x01",
            "很好～今天一天也要努力啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_489B")

    Jump("loc_4A11")

    label("loc_48A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_48FB")

    #C0271
    ChrTalk(
        0xC,
        (
            "几天前，这附近好像\x01",
            "有人打架吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xC,
        (
            "……为什么非要\x01",
            "打架呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_496D")

    label("loc_48FB")


    #C0273
    ChrTalk(
        0xC,
        (
            "几天前，这一带好像\x01",
            "有人打过架吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "留下了很多碎片\x01",
            "和血迹呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "我光是看了看，\x01",
            "就觉得心中很难过。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_496D")

    Jump("loc_4A11")

    label("loc_4972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_49B7")

    #C0276
    ChrTalk(
        0xC,
        (
            "那边的街道上\x01",
            "好像很吵闹……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        "发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A11")

    label("loc_49B7")


    #C0278
    ChrTalk(
        0xC,
        (
            "那个……你们也是来\x01",
            "帮我捡垃圾的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xC,
        (
            "呵呵，谢谢啦。\x01",
            "必须要把街道打扫干净才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A11")

    TalkEnd(0xFE)
    Return()

    # Function_18_3F22 end

    def Function_19_4A15(): pass

    label("Function_19_4A15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4A8E")
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0280
    ChrTalk(
        0xD,
        "……好，广场也没有异常。\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xD,
        (
            "喂，斯拉修，\x01",
            "差不多了吧。\x01",
            "该回去向瓦鲁多大哥报告了！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_4B39")

    label("loc_4A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4ADB")

    #C0282
    ChrTalk(
        0xD,
        "那个女人今天不在啊。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xD,
        (
            "嘁，我本来还想\x01",
            "和她搭个话呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B39")

    label("loc_4ADB")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0284
    ChrTalk(
        0xD,
        "嗯，我也有同感啊。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xD,
        (
            "像那样的家伙，\x01",
            "必须要马上干掉才行！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B31")
    SetScenarioFlags(0x53, 4)

    label("loc_4B31")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)

    label("loc_4B39")

    TalkEnd(0xFE)
    Return()

    # Function_19_4A15 end

    def Function_20_4B3D(): pass

    label("Function_20_4B3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4BE1")
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0286
    ChrTalk(
        0xE,
        (
            "说起来，最近都\x01",
            "没有看到那个女人啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xE,
        (
            "哼哼，她好像说练习很忙，\x01",
            "是因为这个缘故吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        (
            "#0005F（…………？\x01",
            "  是在说谁呢？）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_4CFC")

    label("loc_4BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4CA0")
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4C2D")

    #C0289
    ChrTalk(
        0xE,
        (
            "嘁，那女人～……\x01",
            "今天没从这里经过吗～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C93")

    label("loc_4C2D")


    #C0290
    ChrTalk(
        0xE,
        "一直都没看到啊～……\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xE,
        (
            "说起来，那个女人\x01",
            "一天到晚总是吵着要练习。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xE,
        "哼哼，练什么练啊～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4C93")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_4CFC")

    label("loc_4CA0")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0293
    ChrTalk(
        0xE,
        "哈！谁会管那么多！\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xE,
        (
            "瓦鲁多大哥心里其实\x01",
            "也是很恼火的！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CF4")
    SetScenarioFlags(0x53, 4)

    label("loc_4CF4")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)

    label("loc_4CFC")

    TalkEnd(0xFE)
    Return()

    # Function_20_4B3D end

    def Function_21_4D00(): pass

    label("Function_21_4D00")

    TalkBegin(0xFE)

    #C0295
    ChrTalk(
        0xF,
        (
            "呜，这种事情\x01",
            "怎么能轻易饶恕……！\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xF,
        "可是……瓦吉都那么说了……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D57")
    SetScenarioFlags(0x53, 4)

    label("loc_4D57")

    TalkEnd(0xFE)
    Return()

    # Function_21_4D00 end

    def Function_22_4D5B(): pass

    label("Function_22_4D5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FBA")
    TurnDirection(0xFE, 0x0, 0)

    #C0297
    ChrTalk(
        0xFE,
        (
            "唉，警察竟然会和不良成员们\x01",
            "一起打群架……！\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        (
            "#0005F不，那并不是在打架，\x01",
            "只是防身术的训练……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "不管是什么理由，\x01",
            "也不可以使用暴力！\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        (
            "#0104F我们只是通过与他们的\x01",
            "交流比赛，让他们领会到\x01",
            "竞技精神中蕴含的道德与友谊。\x02\x03",

            "#0100F为了让他们改过自新，\x01",
            "我们会定期常来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0301
    ChrTalk(
        0xFE,
        (
            "是吗，原来是这样啊……\x01",
            "那可真是失礼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "不过，你们竟然试图让那些粗暴\x01",
            "的孩子们敞开心扉……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "实在是了不起！\x01",
            "我身为一名教育者，也必须以你们为榜样。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x103,
        (
            "#0200F（真不愧是艾莉前辈，\x01",
            "  很擅长说服交涉呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x104,
        "#0300F（哈哈，说实话，确实帮了大忙。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x94, 5)
    SetScenarioFlags(0x0, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4FB5")
    OP_93(0xFE, 0xE1, 0x0)

    label("loc_4FB5")

    Jump("loc_5142")

    label("loc_4FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_504D")
    TurnDirection(0xFE, 0x0, 0)

    #C0306
    ChrTalk(
        0xFE,
        (
            "你们竟然试图让那些粗暴\x01",
            "的孩子们敞开心扉……\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "实在是了不起呀！\x01",
            "我身为一名教育者，也必须以你们为榜样。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5048")
    OP_93(0xFE, 0xE1, 0x0)

    label("loc_5048")

    Jump("loc_5142")

    label("loc_504D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_50E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_50D8")

    #C0308
    ChrTalk(
        0x10,
        (
            "……那些孩子，\x01",
            "好像一点学习\x01",
            "的欲望都没有。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x10,
        (
            "既然他们不愿意来主日学校，\x01",
            "我就想来这里好好辅导他们，\x01",
            "可是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50DB")

    label("loc_50D8")

    Call(0, 15)

    label("loc_50DB")

    Jump("loc_5142")

    label("loc_50E0")


    #C0310
    ChrTalk(
        0x10,
        (
            "我离开大圣堂，到这里来进行\x01",
            "主日学校的外出授课。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x10,
        (
            "那么……希望他们今天\x01",
            "能好好听我讲课啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5142")

    TalkEnd(0xFE)
    Return()

    # Function_22_4D5B end

    def Function_23_5146(): pass

    label("Function_23_5146")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_51B5")

    #C0312
    ChrTalk(
        0x11,
        "听好，首先要学的是打招呼哦。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x11,
        (
            "如果遇到瓦鲁多大哥，\x01",
            "或者其他的干部们，\x01",
            "必须要说您好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5275")

    label("loc_51B5")

    OP_4B(0x8, 0xFF)

    #C0314
    ChrTalk(
        0x11,
        "迪诺是新来的。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x11,
        (
            "我得把我们的规矩\x01",
            "一条一条教给他。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x8, 500)

    #C0316
    ChrTalk(
        0x11,
        "听好，首先要学的是打招呼哦。\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x11,
        (
            "如果遇到瓦鲁多大哥，\x01",
            "或者其他的干部们，\x01",
            "必须要说您好。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        "您、您好！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_5275")

    TalkEnd(0xFE)
    Return()

    # Function_23_5146 end

    def Function_24_5279(): pass

    label("Function_24_5279")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-4950, -1840, -23330, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29500, 0)
    SetMapObjFlags(0x5, 0x1000)
    FadeToBright(1000, 0)
    OP_68(-14810, 2000, -9650, 5000)
    MoveCamera(44, 27, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(24500, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(11430, 2000, 960, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29500, 0)
    ClearMapObjFlags(0x5, 0x1000)
    OP_68(38910, 2200, -19760, 7000)
    MoveCamera(32, 17, 0, 7000)
    OP_6E(500, 7000)
    SetCameraDistance(30920, 7000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(2190, 2000, -10020, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(35000, 0)
    SetCameraDistance(48000, 5000)
    OP_0D()
    PlaceName2(340, 200, "c_plac10", 0x0, 0)
    OP_6F(0x10)
    Sleep(500)

    #A0319
    AnonymousTalk(
        0x104,
        (
            "#0305F这地方还真荒凉啊……\x01",
            "这里真的属于克洛斯贝尔市吗？\x02",
        )
    )

    CloseMessageWindow()

    #A0320
    AnonymousTalk(
        0x102,
        "#0108F……是的，这里是旧城区哦。\x02",
    )

    CloseMessageWindow()

    #A0321
    AnonymousTalk(
        0x101,
        (
            "#0001F嗯……不过我也\x01",
            "几乎没有来过呢。\x02\x03",

            "据说是在当年的都市开发计划中\x01",
            "被遗留下来的区域……\x02",
        )
    )

    CloseMessageWindow()

    #A0322
    AnonymousTalk(
        0x103,
        (
            "#0200F根据数据库中的资料所记载，\x01",
            "现在也仍然有为数不少的居民\x01",
            "在这里过着正常生活呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0323
    AnonymousTalk(
        0x101,
        (
            "#0003F是吗……\x02\x03",

            "#0000F也就是说，这里同样是警察局的辖区之一啊。\x01",
            "我们还是先四处看看，熟悉一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旧城区是位于城市边缘的萧条街区。\x02",
        )
    )

    CloseMessageWindow()

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "虽然也建有不少便利的设施，\x01",
            "但在游戏初期是无法进入的。\x02",
        )
    )

    CloseMessageWindow()

    #A0326
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当剧情进展到一定程度之后，\x01",
            "可以再来这里看看。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetScenarioFlags(0x45, 1)
    EventEnd(0x5)
    Return()

    # Function_24_5279 end

    def Function_25_5684(): pass

    label("Function_25_5684")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30850.itc", 0x1F)
    LoadChrToIndex("chr/ch30900.itc", 0x20)
    LoadChrToIndex("chr/ch30950.itc", 0x21)
    LoadChrToIndex("chr/ch31750.itc", 0x23)
    LoadChrToIndex("chr/ch31850.itc", 0x25)
    LoadChrToIndex("chr/ch00050.itc", 0x26)
    LoadChrToIndex("chr/ch00150.itc", 0x27)
    LoadChrToIndex("chr/ch00250.itc", 0x28)
    LoadChrToIndex("chr/ch00350.itc", 0x29)
    LoadChrToIndex("apl/ch50014.itc", 0x2A)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_68(1700, 1000, 8700, 0)
    MoveCamera(50, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1100, 0, 8000, 180)
    SetChrPos(0x102, 2300, 0, 8000, 180)
    SetChrPos(0x103, 1100, 0, 9400, 180)
    SetChrPos(0x104, 2300, 0, 9400, 180)
    SetChrChipByIndex(0x12, 0x7)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -1000, 0, -5200, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -1500, 0, -3700, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -1500, 0, -6700, 90)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -2600, 0, -5600, 90)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x6)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x6)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 3100, 0, -5200, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 3600, 0, -3700, 270)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 3600, 0, -6700, 270)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 4600, 0, -5400, 270)
    ClearMapFlags(0x10000000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00001.itp")
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0327
    ChrTalk(
        0x101,
        "#5P#0013F那是……！\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x104,
        (
            "#5P#0305F噢噢～\x01",
            "看起来，这情况似乎是一触即发呢。\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7517", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x205), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(1100, 900, -5200, 3000)
    MoveCamera(55, 23, 0, 3000)
    SetCameraDistance(18000, 3000)
    OP_6F(0x79)

    #C0329
    ChrTalk(
        0x16,
        "#2P喂喂，蓝衣小子们……\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x16,
        (
            "#2P太过嚣张的话，\x01",
            "我真的会把你们宰掉哦……！\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x17,
        (
            "#11P哈，我们早就\x01",
            "看你们不爽了！\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x17,
        (
            "#11P居然使用如此\x01",
            "肮脏卑鄙的手段！\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x12,
        (
            "#6P哼……所以说，真受不了\x01",
            "你们这群低智商的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x12,
        (
            "#6P对付你们这种街边小混混，\x01",
            "根本用不着使用什么卑鄙手段。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x13,
        (
            "#3P而、而且你们竟然还把\x01",
            "我们的同伴打到住院……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x13,
        (
            "#3P以眼还眼、以牙还牙……\x01",
            "……你、你们给我做好觉悟吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x16,
        "#2P算你们有种！蓝衣服的小子们！\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x16,
        "#2P用不着瓦鲁多大哥出马了！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    #C0339
    ChrTalk(
        0x12,
        (
            "#6P这话应该由我们说才对！\x01",
            "不需要劳烦瓦吉动手了……\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x12,
        (
            "#6P全体成员，准备圣战！\x01",
            "歼灭剑蛇帮！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x12, 0x25)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    #Sound(1086, 255, 100, 0)    #voice#Lloyd
    OP_82(0x96, 0x0, 0xBB8, 0x12C)

    #N0341
    NpcTalk(
        0x101,
        "声音",
        "#4S──等一下！\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x6)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x6)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x12, 0x7)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    OP_0D()
    Fade(500)
    OP_68(1100, 1000, 800, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 600, 0, 7000, 180)
    SetChrPos(0x102, 1800, 0, 9300, 180)
    SetChrPos(0x103, 600, 0, 9300, 180)
    SetChrPos(0x104, 1800, 0, 7000, 180)
    OP_68(1100, 1000, -3200, 2500)
    SetCameraDistance(17500, 2500)

    def lambda_5E17():
        OP_95(0xFE, 600, 0, -1800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E17)
    Sleep(50)

    def lambda_5E34():
        OP_95(0xFE, 1800, 0, -1800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E34)
    Sleep(50)

    def lambda_5E51():
        OP_96(0xFE, 0x258, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E51)
    Sleep(50)

    def lambda_5E6E():
        OP_96(0xFE, 0x708, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E6E)
    OP_0D()

    def lambda_5E89():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5E89)

    def lambda_5E96():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_5E96)
    Sleep(50)

    def lambda_5EA6():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5EA6)

    def lambda_5EB3():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_5EB3)

    def lambda_5EC0():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5EC0)

    def lambda_5ECD():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_5ECD)
    Sleep(50)

    def lambda_5EDD():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_5EDD)

    def lambda_5EEA():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_5EEA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)

    #C0342
    ChrTalk(
        0x16,
        "#2P什么……？\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x12,
        "#6P没见过的生面孔啊……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0344
    AnonymousTalk(
        0x101,
        (
            "双方都请住手，立刻停止争斗！\x02\x03",

            "这里可是公共场所！\x01",
            "你们会影响到其他居民的！\x02",
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

    #C0345
    ChrTalk(
        0x17,
        "#11P哈……？\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x13,
        (
            "#6P你、你是干什么的啊……\x01",
            "没头没脑地冒出来，还口出狂言……\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x104,
        "#5P#0306F（呼，免不了要遇到这种情况啊。）\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x102,
        "#5P#0108F（……怎么办呢？）\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        "#5P#0003F（嗯……）\x02",
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
            "【先出示调查手册给对方看】\x01",        # 0
            "【不表明身份，继续进行仲裁】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6111"),
        (1, "loc_61BE"),
        (SWITCH_DEFAULT, "loc_63F0"),
    )


    label("loc_6111")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    def lambda_6124():
        OP_96(0xFE, 0x1F4, 0x0, 0xFFFFF704, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6124)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0350
    ChrTalk(
        0x101,
        (
            "#5P#0007F我们是克洛斯贝尔的警察局·特别任务支援科的人。\x02\x03",

            "接到附近居民的请求，\x01",
            "前来制止你们的争斗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F0")

    label("loc_61BE")

    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0351
    ChrTalk(
        0x12,
        (
            "#6P是吗，你们几个……\x01",
            "是游击士协会的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x12,
        (
            "#6P从来没见过，\x01",
            "是新来的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6242():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6242)
    Sleep(1000)

    #C0353
    ChrTalk(
        0x101,
        "#5P#0011F不、不是……\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x103,
        "#5P#0206F……又被人误解了啊。\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x16,
        (
            "#2P哼，你们这群烦人的家伙，\x01",
            "每次都来碍我们的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x16,
        (
            "#2P不过，这次是绝对不会\x01",
            "让你们得逞的！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_62F4():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62F4)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0357
    ChrTalk(
        0x101,
        "#5P#0013F稍、稍等一下！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_633D():
        OP_96(0xFE, 0x1F4, 0x0, 0xFFFFF704, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_633D)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0358
    ChrTalk(
        0x101,
        (
            "#5P#0007F我们并不是游击士。\x02\x03",

            "我们是克洛斯贝尔的警察，\x01",
            "隶属于『特别任务支援科』。\x02\x03",

            "接到附近居民的请求，\x01",
            "前来制止你们的争斗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F0")

    label("loc_63F0")

    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0359
    ChrTalk(
        0x16,
        "#2P#4S哇哈哈哈，警察！？\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x17,
        (
            "#11P呀哈哈哈哈！\x01",
            "别来搞笑了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x13,
        (
            "#6P警察平时根本就不会来这里，\x01",
            "怎、怎么可能会管这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x12,
        (
            "#6P真是的……就算你想骗人，\x01",
            "起码也得编个稍微像样点的谎话啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    #C0363
    ChrTalk(
        0x101,
        (
            "#5P#0003F……总、总之！\x02\x03",

            "#0013F你们的争斗已经\x01",
            "影响到了其他的居民！\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x104,
        (
            "#5P#0300F如果非要打架的话，\x01",
            "到市外去打如何？\x02\x03",

            "也算是不错的运动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x16,
        "#2P嘿，你可真有种……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x16,
        (
            "#2P竟然敢在这旧城区\x01",
            "对我们用那么嚣张的口气说话……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x12,
        "#6P旧城区有旧城区的规矩。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x12,
        (
            "#6P要是敢自以为是地胡说八道，\x01",
            "可是会吃苦头的。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x12, 0x25)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0369
    ChrTalk(
        0x101,
        "#5P#0013F呜……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        "#5P#0306F看这样子，交涉好像行不通啊。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x103,
        (
            "#5P#0211F……结果\x01",
            "还是变成这样了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        "#5P#0101F呼……真没办法啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0373
    ChrTalk(
        0x16,
        (
            "#2P哎哟，仔细一看，\x01",
            "原来还带着两个可爱的女孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x16,
        (
            "#2P是想在她们的面前\x01",
            "耍帅逞威风吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x17,
        (
            "#11P喂喂，别理这种蠢货啦，\x01",
            "来和我们约会如何啊～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x16, 500)
    Sleep(200)

    #C0376
    ChrTalk(
        0x12,
        (
            "#6P你们是白痴啊……\x01",
            "现在是搭讪的场合吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x17, 500)
    Sleep(200)

    #C0377
    ChrTalk(
        0x13,
        (
            "#6P先、先把这些捣乱的家伙赶走，\x01",
            "然后我们再重新开战……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x13,
        "#6P没、没意见吧，红色爬虫们……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x12, 500)
    Sleep(200)

    #C0379
    ChrTalk(
        0x16,
        "#2P噢，正合我意！\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0x13B, 0x1F4)
    Sleep(200)

    #C0380
    ChrTalk(
        0x16,
        (
            "#2P先把这些家伙干掉，\x01",
            "然后再说别的～！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6995():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6995)
    Sleep(50)
    OP_93(0x13, 0x2D, 0x1F4)
    StopBGM(0x3E8)
    Battle("BattleInfo_848", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CA(0x1, 0xFF, 0x0)
    Call(0, 26)
    Return()

    # Function_25_5684 end

    def Function_26_69CE(): pass

    label("Function_26_69CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30850.itc", 0x1F)
    LoadChrToIndex("chr/ch30853.itc", 0x20)
    LoadChrToIndex("chr/ch30900.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch30953.itc", 0x23)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch31753.itc", 0x26)
    LoadChrToIndex("chr/ch31850.itc", 0x28)
    LoadChrToIndex("chr/ch31853.itc", 0x29)
    LoadChrToIndex("chr/ch00400.itc", 0x2A)
    LoadChrToIndex("chr/ch02100.itc", 0x2B)
    LoadChrToIndex("chr/ch06700.itc", 0x2C)
    LoadChrToIndex("chr/ch00050.itc", 0x2D)
    LoadChrToIndex("chr/ch00150.itc", 0x2E)
    LoadChrToIndex("chr/ch00250.itc", 0x2F)
    LoadChrToIndex("chr/ch00350.itc", 0x30)
    LoadChrToIndex("apl/ch50015.itc", 0x31)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_68(1100, 1000, -4200, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x101, 0x2D)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2E)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 600, 0, -1800, 180)
    SetChrPos(0x102, 1800, 0, 0, 180)
    SetChrPos(0x103, 600, 0, 0, 180)
    SetChrPos(0x104, 1800, 0, -1800, 180)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x3)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x3)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrPos(0x12, -1000, 0, -5200, 45)
    SetChrPos(0x13, -1500, 0, -3700, 45)
    SetChrPos(0x14, -1500, 0, -6700, 45)
    SetChrPos(0x15, -2600, 0, -5600, 45)
    SetChrChipByIndex(0x16, 0x26)
    SetChrSubChip(0x16, 0x3)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x3)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrPos(0x16, 3100, 0, -5200, 315)
    SetChrPos(0x17, 3600, 0, -3700, 315)
    SetChrPos(0x18, 3600, 0, -6700, 315)
    SetChrPos(0x19, 4600, 0, -5400, 315)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1B, 0x2B)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1A, 0x2A)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1C, 0x2C)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00400.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01600.itp")
    OP_63(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light", 0x0, 0x1)
    OP_68(1100, 1000, -3200, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    def lambda_6D1E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_6D1E)
    WaitChrThread(0x13, 2)

    #C0381
    ChrTalk(
        0x13,
        (
            "#6P这、这些家伙……\x01",
            "好像不是等闲之辈啊……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D6D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_6D6D)
    WaitChrThread(0x16, 2)

    #C0382
    ChrTalk(
        0x16,
        (
            "那、那两个女人……\x01",
            "本来还以为只是跟班的……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6DBB():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6DBB)
    WaitChrThread(0x12, 2)

    #C0383
    ChrTalk(
        0x12,
        (
            "#6P那手杖到底是什么东西啊……？\x01",
            "………电得我全身发麻………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E18():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_6E18)
    WaitChrThread(0x17, 2)

    #C0384
    ChrTalk(
        0x17,
        (
            "#2P可恶……！\x01",
            "你们果然是游击士吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        (
            "#5P#0006F不，刚才不是都说了吗，\x01",
            "我们是警察……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x102,
        (
            "#1P#0106F呼……\x01",
            "他们好像根本不信呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x16,
        "哼，好啊……\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x16,
        (
            "既然如此，我们大家一起上，\x01",
            "就不信打不过他们……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F06():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_6F06)
    SetChrSubChip(0x16, 0x2)
    Sound(808, 0, 100, 0)
    Sleep(80)
    BeginChrThread(0x17, 3, 0, 27)
    SetChrSubChip(0x16, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    OP_64(0x18)
    OP_64(0x19)
    OP_0D()
    WaitChrThread(0x17, 3)

    #C0389
    ChrTalk(
        0x12,
        "#6P我们也不能落于人后啊……！\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x12,
        (
            "#6P就算与游击士为敌，\x01",
            "也要让他们见识到我们圣书会的骨气！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6FB2():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6FB2)
    SetChrSubChip(0x12, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(80)
    BeginChrThread(0x13, 3, 0, 28)
    SetChrSubChip(0x12, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x12, 0x28)
    SetChrSubChip(0x12, 0x0)
    OP_64(0x14)
    OP_64(0x15)
    OP_0D()
    WaitChrThread(0x13, 3)

    #C0391
    ChrTalk(
        0x101,
        "#5P#0013F呜……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x8)
    SetChrPos(0x1B, 15500, -1000, -10500, 315)
    SetChrPos(0x1A, -8300, 0, -10800, 60)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    StopBGM(0xBB8)
    #Sound(1804, 255, 100, 0)    #voice#Wald

    #N0392
    NpcTalk(
        0x1B,
        "凶狠的声音",
        "#1P喂喂……在干什么呢？！\x02",
    )

    CloseMessageWindow()
    #Sound(1427, 255, 100, 0)    #voice#Lazy

    #N0393
    NpcTalk(
        0x1A,
        "冷静的声音",
        "#5P到此为止吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    Fade(500)
    OP_68(8300, 900, -12000, 0)
    MoveCamera(173, 27, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(17500, 0)
    ClearChrFlags(0x1A, 0x8)
    SetChrPos(0x1A, -8300, 0, -10800, 60)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1B, 0x8)
    OP_90(0x1B, 12500, -1000, -16500, 315)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -9100, 0, -11800, 60)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 700, 0, -2300, 180)
    SetChrPos(0x104, 1700, 0, -2300, 180)
    SetChrPos(0x102, 2000, 0, -700, 180)
    SetChrPos(0x103, 400, 0, -700, 180)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x6)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x6)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x12, 0x7)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x12, -1600, 0, -4700, 45)
    SetChrPos(0x13, -2400, 0, -3100, 45)
    SetChrPos(0x14, -3700, 0, -4300, 45)
    SetChrPos(0x15, -2700, 0, -5500, 45)
    SetChrPos(0x16, 4000, 0, -4700, 315)
    SetChrPos(0x17, 4800, 0, -3100, 315)
    SetChrPos(0x18, 6100, 0, -4300, 315)
    SetChrPos(0x19, 5100, 0, -5500, 315)

    def lambda_7350():

        label("loc_7350")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7350")

    QueueWorkItem2(0x16, 2, lambda_7350)

    def lambda_7362():

        label("loc_7362")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7362")

    QueueWorkItem2(0x17, 2, lambda_7362)

    def lambda_7374():

        label("loc_7374")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7374")

    QueueWorkItem2(0x18, 2, lambda_7374)

    def lambda_7386():

        label("loc_7386")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7386")

    QueueWorkItem2(0x19, 2, lambda_7386)

    def lambda_7398():

        label("loc_7398")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_7398")

    QueueWorkItem2(0x12, 2, lambda_7398)

    def lambda_73AA():

        label("loc_73AA")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_73AA")

    QueueWorkItem2(0x13, 2, lambda_73AA)

    def lambda_73BC():

        label("loc_73BC")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_73BC")

    QueueWorkItem2(0x14, 2, lambda_73BC)

    def lambda_73CE():

        label("loc_73CE")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_73CE")

    QueueWorkItem2(0x15, 2, lambda_73CE)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    SetMapObjFrame(0xFF, "light", 0x1, 0x1)
    MoveCamera(163, 27, 0, 3000)
    SetCameraDistance(16500, 3000)

    def lambda_7429():
        OP_95(0xFE, 8300, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_7429)
    WaitChrThread(0x1B, 1)
    SetChrFlags(0x1B, 0x4)
    OP_6F(0x40)
    OP_6F(0x10)

    #C0394
    ChrTalk(
        0x16,
        "#1P瓦、瓦鲁多大哥……！！\x02",
    )

    CloseMessageWindow()

    def lambda_746F():
        OP_95(0xFE, 2900, 0, -5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_746F)
    Sleep(2000)
    Fade(500)
    OP_68(-5700, 900, -9300, 0)
    MoveCamera(210, 30, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(16000, 0)
    EndChrThread(0x1B, 0x1)
    MoveCamera(200, 30, 0, 1500)
    SetCameraDistance(15000, 1500)

    def lambda_74D7():
        OP_95(0xFE, -5700, 0, -9300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_74D7)

    def lambda_74F1():
        OP_95(0xFE, -6500, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_74F1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1C, 1)
    OP_6F(0x40)
    OP_6F(0x10)

    #C0395
    ChrTalk(
        0x12,
        "#2P瓦吉……你来了啊。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x101,
        "#0005F（……难道是……）\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x104,
        (
            "#0301F（两方团伙的头目\x01",
            "  好像登场了啊……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7581():
        OP_95(0xFE, -500, 0, -5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_7581)
    Sleep(50)

    def lambda_759E():
        OP_95(0xFE, -1100, 0, -6500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_759E)
    Sleep(1000)

    def lambda_75BB():
        OP_95(0xFE, 2900, 0, -5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_75BB)
    Sleep(1000)
    Fade(500)
    OP_68(1200, 800, -4800, 0)
    MoveCamera(180, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 1500)
    ClearChrFlags(0x16, 0x8)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x8)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1C, 2)
    OP_6F(0x10)

    #N0398
    NpcTalk(
        0x1B,
        "看似凶狠的青年",
        (
            "#5P#1604F呵呵，趁着别人睡午觉的时候，\x01",
            "居然在做这么有趣的事。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x16, 500)
    Sleep(300)

    #N0399
    NpcTalk(
        0x1B,
        "看似凶狠的青年",
        (
            "#11P#1602F喂，你们几个……\x01",
            "这里到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x16,
        (
            "#3P这个……\x01",
            "嘿嘿，该怎么说才好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x16,
        (
            "#3P我们正想把这些\x01",
            "蓝衣小子收拾一顿，\x01",
            "结果这些怪家伙突然出来碍事……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_775E():
        OP_9B(0x1, 0xFE, 0x0, 0x384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_775E)
    WaitChrThread(0x1B, 1)
    Fade(250)
    SetChrChipByIndex(0x1B, 0x31)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x4)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_7799():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_7799)

    def lambda_77B2():
        OP_96(0xFE, 0xFA0, 0x1C2, 0xFFFFEDA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_77B2)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x16, 2)
    ClearChrFlags(0x16, 0x20)

    #C0402
    ChrTalk(
        0x16,
        "#3P哇……！\x02",
    )

    CloseMessageWindow()

    #N0403
    NpcTalk(
        0x1B,
        "看似凶狠的青年",
        (
            "#11P#1601F……蠢货。\x01",
            "不是和你们说过，不要贸然行动吗？\x02\x03",

            "你们这些小卒居然敢冲到最前线，\x01",
            "难道是想把本大爷的脸给丢光吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x16,
        "#3P我、我、我们不是这个意思啊！\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x16,
        (
            "#3P有损瓦鲁多大哥颜面的事情，\x01",
            "我们无论如何也……！\x02",
        )
    )

    CloseMessageWindow()

    #N0406
    NpcTalk(
        0x1B,
        "看似凶狠的青年",
        "#11P#1600F哼……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1B, 0x2B)
    SetChrSubChip(0x1B, 0x0)

    def lambda_7907():
        OP_96(0xFE, 0xB54, 0x0, 0xFFFFEA84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_7907)

    def lambda_7921():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_7921)

    def lambda_793A():
        OP_9D(0xFE, 0xFA0, 0x0, 0xFFFFEDA4, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_793A)
    Sound(819, 0, 100, 0)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x26)
    SetChrSubChip(0x16, 0x3)
    WaitChrThread(0x16, 2)
    ClearChrFlags(0x16, 0x4)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0407
    ChrTalk(
        0x16,
        "#3P咳咳、咳咳……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1B, 1)

    def lambda_7998():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_7998)
    Sleep(100)

    def lambda_79A8():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_79A8)
    WaitChrThread(0x1C, 2)

    #N0408
    NpcTalk(
        0x1A,
        "面容冷寂的少年",
        (
            "#5P#0403F你们也是一样……\x01",
            "到底是怎么回事？\x02\x03",

            "#0400F难道不打算听\x01",
            "我的话了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x12,
        "#4P可是，瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x14,
        (
            "#4P是、是这些家伙\x01",
            "先挑衅，我们才……\x02",
        )
    )

    CloseMessageWindow()

    #N0411
    NpcTalk(
        0x1C,
        "高大的光头男子",
        "#5P不必找借口。\x02",
    )

    CloseMessageWindow()

    #N0412
    NpcTalk(
        0x1C,
        "高大的光头男子",
        (
            "#5P我们都是瓦吉的兄弟，\x01",
            "没必要说这些多余的。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x12,
        "#4P……明白了……\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x14,
        "#4P……我、我们会好好反省的……\x02",
    )

    CloseMessageWindow()

    #N0415
    NpcTalk(
        0x1A,
        "面容冷寂的少年",
        (
            "#5P#0404F算了，只要你们\x01",
            "能明白就好。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B34():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_7B34)
    Sleep(160)
    Fade(250)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    OP_0D()
    TurnDirection(0x1B, 0x1A, 500)

    #N0416
    NpcTalk(
        0x1B,
        "看似凶狠的青年",
        (
            "#5P#1602F哼哼……\x01",
            "你们一点都没变，还是这么恶心啊。\x02\x03",

            "竟然让小弟们都打扮成这种样子……\x01",
            "是把自己当成了不起的宗教家了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7BEF():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_7BEF)
    Sleep(100)

    def lambda_7BFF():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_7BFF)
    WaitChrThread(0x1C, 2)

    #N0417
    NpcTalk(
        0x1A,
        "面容冷寂的少年",
        (
            "#11P#0402F呵呵，我并没有强制他们\x01",
            "穿成这样哦。\x02\x03",

            "你才是啊，\x01",
            "总是对手下乱发脾气的话，\x01",
            "可是会被人看出没有当大将的器量呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0418
    NpcTalk(
        0x1B,
        "看似凶狠的青年",
        "#5P#1602F哼哼哼……\x02",
    )

    CloseMessageWindow()

    #N0419
    NpcTalk(
        0x1A,
        "面容冷寂的少年",
        "#11P#0404F呵呵……\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        "#12P#0001F（怎、怎么回事……？）\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        "#0101F#6P#N（他们之间到底是什么关系呢……）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #N0422
    NpcTalk(
        0x1A,
        "面容冷寂的少年",
        "#2P#0404F──算了，先不说这些。\x02",
    )

    CloseMessageWindow()

    def lambda_7D75():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_7D75)
    Sleep(50)

    def lambda_7D85():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_7D85)
    Sleep(50)

    def lambda_7D95():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_7D95)
    WaitChrThread(0x1C, 2)
    Sleep(300)

    #N0423
    NpcTalk(
        0x1A,
        "面容冷寂的少年",
        (
            "#11P#0402F你们真的是警察吗？\x02\x03",

            "呵呵……\x01",
            "看起来不怎么像呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0424
    NpcTalk(
        0x1B,
        "看似凶狠的青年",
        (
            "#5P#1604F哼，不过本事倒还算过得去。\x02\x03",

            "#1602F特别是那个红毛……\x01",
            "体格相当不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x104,
        (
            "#6P#0306F多谢夸奖……\x01",
            "不过还是比不上你。\x02",
        )
    )

    CloseMessageWindow()

    #N0426
    NpcTalk(
        0x1B,
        "看似凶狠的青年",
        (
            "#5P#1602F哈，至于那两位小姐，\x01",
            "不管怎么看都不像警察啊。\x02\x03",

            "呵呵……\x01",
            "不过，倒是相当漂亮的美人嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x102,
        "#0103F#6P#N……谢谢夸奖。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0428
    ChrTalk(
        0x103,
        "#0211F#12P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0429
    ChrTalk(
        0x101,
        (
            "#12P#0003F……虽然还是新人，\x01",
            "但我们所有人都是警察。\x02\x03",

            "#0001F隶属于『特别任务支援科』……\x01",
            "一个新成立\x01",
            "没多久的部门。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0430
    NpcTalk(
        0x1A,
        "面容冷寂的少年",
        (
            "#11P#0405F哎，今天发行的\x01",
            "克洛斯贝尔时代周刊上报道的\x01",
            "那些人就是你们吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_END)), "loc_808D")

    #C0431
    ChrTalk(
        0x101,
        "#12P#0011F唔……\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x102,
        (
            "#0106F#6P#N真不愧是克洛斯贝尔时代周刊……\x01",
            "这么快就传开了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8166")

    label("loc_808D")

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

    #C0433
    ChrTalk(
        0x101,
        (
            "#12P#0005F刊登在克洛斯贝尔时代周刊上，\x01",
            "也就是说……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x102,
        (
            "#6P#0105F#N难道是……\x01",
            "将孩子们救出时的报道吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8166")

    TurnDirection(0x1B, 0x1A, 500)
    Sleep(300)

    #N0435
    NpcTalk(
        0x1B,
        "看似凶狠的青年",
        (
            "#5P#1605F什么啊？\x01",
            "这些家伙们做了什么了不得的事吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0436
    NpcTalk(
        0x1A,
        "面容冷寂的少年",
        (
            "#11P#0404F嗯，作为游击士协会的陪衬，\x01",
            "好像还挺活跃呢。\x02\x03",

            "#0402F哎呀，抱歉抱歉。\x01",
            "你们当时好像也派上了一点用场吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        "#12P#0013F呜……\x02",
    )

    CloseMessageWindow()

    #N0438
    NpcTalk(
        0x1A,
        "面容冷寂的少年",
        (
            "#11P#0404F呵呵，好了，\x01",
            "不欺负你们了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(450)
    #Sound(1435, 255, 100, 0)    #voice#Lazy
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("面容冷寂的少年")

    #A0439
    AnonymousTalk(
        0xFF,
        (
            "──我叫瓦吉，\x01",
            "瓦吉·赫米斯菲亚。\x02\x03",

            "应该可以算是『圣书会』\x01",
            "的首领吧？\x02",
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

    #N0440
    NpcTalk(
        0x1C,
        "高大的光头男子",
        "#11P……为什么要使用疑问句啊？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x1C, 500)

    #C0441
    ChrTalk(
        0x1A,
        (
            "#6P#0402F因为你才更像是\x01",
            "真正的首领吧。\x02\x03",

            "#0409F呵呵，那光头不是\x01",
            "很有老大的派头嘛。\x02",
        )
    )

    CloseMessageWindow()

    #N0442
    NpcTalk(
        0x1C,
        "高大的光头男子",
        "#11P…………………………\x02",
    )

    CloseMessageWindow()

    #N0443
    NpcTalk(
        0x1B,
        "看似凶狠的青年",
        "#5P#1603F哼……玩笑就开到这里吧。\x02",
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x13B, 0x1F4)
    Sleep(300)
    #Sound(1805, 255, 100, 0)    #voice#Wald
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("看似凶狠的青年")

    #A0444
    AnonymousTalk(
        0xFF,
        (
            "──我是瓦鲁多，\x01",
            "瓦鲁多·瓦雷斯。\x02\x03",

            "『剑蛇帮』的头目。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    OP_93(0x1A, 0x2D, 0x1F4)
    Sleep(300)

    #C0445
    ChrTalk(
        0x101,
        (
            "#12P#0003F瓦吉和瓦鲁多吗……\x02\x03",

            "#0000F正式自我介绍一下──\x01",
            "我是克洛斯贝尔警察局·特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02\x03",

            "看来，你们两位好像并没有打算\x01",
            "让事态进一步扩大化……\x02\x03",

            "那这里就交给你们了，没问题吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0446
    ChrTalk(
        0x1B,
        "#5P#1604F哼哼哼……\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x1A,
        "#11P#0404F呵呵……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    SetCameraDistance(17500, 1000)
    #Sound(1809, 255, 100, 0)    #voice#Wald
    #Sound(1431, 255, 100, 1)    #voice#Lazy

    #C0448
    ChrTalk(
        0x1B,
        (
            "#1P#1609F#4S#1K哈哈哈哈哈\x01",
            "哈哈哈！\x02",
        )
    )


    #C0449
    ChrTalk(
        0x1A,
        (
            "#2P#0409F#4S#1K啊哈哈哈哈\x01",
            "哈哈哈！\x02",
        )
    )

    OP_57(0x1)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0450
    ChrTalk(
        0x101,
        "#12P#0013F有、有什么好笑的？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x1A,
        (
            "#11P#0404F没什么，没什么，\x01",
            "只是觉得你们天真得可爱～\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x1B,
        (
            "#5P#1602F没打算把事态继续扩大？\x02\x03",

            "哼哼……\x01",
            "你在说什么梦话呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        "#12P#0005F……什么………\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x1A,
        (
            "#11P#0404F今天就此罢手，\x01",
            "只是因为还没有准备就绪而已……\x02\x03",

            "#0402F──一旦准备工作结束，\x01",
            "就会开始彻底的对决。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x1B,
        (
            "#5P#1602F而且，到时候可就不是\x01",
            "现在这种小打小闹了……\x02\x03",

            "不把对方彻底击溃，绝不停手，\x01",
            "只有一边可以存活下来！\x02",
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

    #C0456
    ChrTalk(
        0x101,
        "#12P#0007F什么！？\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x104,
        (
            "#6P#0301F喂喂……\x01",
            "难道你们真要互相厮杀吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x1B,
        (
            "#5P#1604F哼哼，这也没什么\x01",
            "值得奇怪的吧。\x02\x03",

            "#1602F不过，哪一边会被打得倒地吐血，\x01",
            "其实现在就已经显而易见了吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x1A,
        (
            "#11P#0400F呵呵……就让你逞一时口舌之快好了。\x02\x03",

            "#0404F算了，到时不管谁胜谁负，\x01",
            "也不需要你们来添乱。\x02\x03",

            "#0402F懦弱无能的警察走狗别想插手──\x01",
            "更何况是你们这种小角色。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x101,
        "#12P#0013F唔……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x16, 500)
    Sleep(300)
    #Sound(1807, 255, 100, 0)    #voice#Wald
    Sleep(500)

    #C0461
    ChrTalk(
        0x1B,
        (
            "#11P#1602F哼哼……\x01",
            "你们几个，回去了！\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x16,
        "#3P是、是！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x12, 500)
    Sleep(300)
    #Sound(1429, 255, 100, 0)    #voice#Lazy
    Sleep(500)

    #C0463
    ChrTalk(
        0x1A,
        (
            "#5P#0400F呵呵……\x01",
            "我们也回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0464
    NpcTalk(
        0x1C,
        "高大的光头男子",
        "#5P……了解。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 10000)
    BeginChrThread(0x1B, 3, 0, 29)
    BeginChrThread(0x1A, 3, 0, 30)
    OP_6F(0x10)
    WaitChrThread(0x1B, 3)
    WaitChrThread(0x1A, 3)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    Fade(1000)
    OP_68(1200, 900, -1500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 500, 0, -2200, 180)
    SetChrPos(0x104, 1900, 0, -2200, 180)
    SetChrPos(0x102, 1900, 0, -800, 180)
    SetChrPos(0x103, 500, 0, -800, 180)
    OP_0D()

    #C0465
    ChrTalk(
        0x101,
        "#5P#0001F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)
    Sleep(300)

    #C0466
    ChrTalk(
        0x102,
        (
            "#5P#0106F……真是一群令人头疼的人啊。\x02\x03",

            "#0101F而且，看起来，他们两边\x01",
            "好像都相当认真呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x13B, 0x1F4)

    #C0467
    ChrTalk(
        0x104,
        (
            "#2P#0301F是啊，按照现在这种状况来看，\x01",
            "估计最近这几天就要开战了吧。\x02\x03",

            "到时候必然要见血啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x87, 0x1F4)
    Sleep(300)

    #C0468
    ChrTalk(
        0x103,
        (
            "#1P#0206F可是，科长交代给我们的任务\x01",
            "已经算是圆满完成了…………\x02\x03",

            "#0200F之后的事情并不在我们的任务范围之内吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x101,
        "#5P#0003F…………不。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0470
    ChrTalk(
        0x101,
        (
            "#6P#0001F如果就此罢手，\x01",
            "并不能算是真正完成了任务。\x02\x03",

            "放任他们不管的话……\x01",
            "市民们对警察的信赖\x01",
            "恐怕永远都无法恢复。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8E3E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8E3E)

    def lambda_8E4B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8E4B)

    def lambda_8E58():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8E58)
    WaitChrThread(0x104, 2)

    #C0471
    ChrTalk(
        0x103,
        "#1P#0203F……啊，倒也确实如此。\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x102,
        (
            "#5P#0103F说的对啊……\x02\x03",

            "#0101F既然我们都已经知道了，\x01",
            "无论如何也该想办法去制止吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x104,
        (
            "#2P#0306F可是，要想制止的话，\x01",
            "实在是相当困难吧？\x02\x03",

            "#0301F那些家伙可不是光靠一句『请你们和睦相处』\x01",
            "就能轻松打发掉的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x101,
        "#6P#0008F是啊……\x02",
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
            "【请求总部的支援】\x01",        # 0
            "【不请求总部的支援】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8FD3"),
        (1, "loc_9201"),
        (SWITCH_DEFAULT, "loc_94D8"),
    )


    label("loc_8FD3")


    #C0475
    ChrTalk(
        0x101,
        (
            "#6P#0006F……看来，我们也只有\x01",
            "向总部报告，要求强化\x01",
            "旧城区的巡逻工作了。\x02\x03",

            "#0001F那种规模的帮派如果发生了冲突，\x01",
            "光凭我们几个人，实在是\x01",
            "无计可施呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x102,
        (
            "#5P#0100F确实啊，如果有警察巡逻的话，\x01",
            "或许能起到一定的抑制作用吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x104,
        "#2P#0306F嗯～不知道能不能行得通啊。\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x103,
        (
            "#1P#0203F……根据数据库中的资料记载，\x01",
            "最近这段时间，旧城区的巡逻人员\x01",
            "数量好像被大幅度削减了。\x02\x03",

            "#0200F好像是以减少预算为名义……\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x101,
        (
            "#6P#0005F有、有这种事吗！？\x02\x03",

            "#0008F可恶，感觉已经决定要将\x01",
            "这里完全弃之不顾了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x102,
        (
            "#5P#0106F既然如此，就算提出那种建议，\x01",
            "恐怕也只会石沉大海吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94D8")

    label("loc_9201")

    OP_2C(0x3E, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0481
    ChrTalk(
        0x101,
        (
            "#6P#0008F……就算向总部报告，\x01",
            "恐怕也得不到什么支援。\x02\x03",

            "这种时候，我们也只能\x01",
            "依靠自己的力量来想些对策了。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x102,
        (
            "#5P#0105F哎……\x01",
            "至少也应该报告一下吧？\x02\x03",

            "说不定，上边会对旧城区的巡逻工作\x01",
            "进行一定程度的强化呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#6P#0003F不……这大概很难实现。\x02\x03",

            "刚才明明都已经引起那种程度的骚乱了，\x01",
            "他们还是完全不在意被警察发现。\x02\x03",

            "#0001F我想，这旧城区多半已经被\x01",
            "故意弃之不管了。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x102,
        "#5P#0101F啊……\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x103,
        (
            "#1P#0203F确实，数据库中的资料也有记载，\x01",
            "最近这段时间，旧城区的巡逻人员\x01",
            "数量好像被大幅度削减了。\x02\x03",

            "#0200F好像是以减少预算为名义……\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x104,
        (
            "#2P#0301F哼，看来是猜对了啊。\x02\x03",

            "#0306F可是……如果是这样的话，\x01",
            "我们岂不是更加无能为力了吗？\x02\x03",

            "#0300F要不，我们干脆\x01",
            "找上门去跟那两边各打一场，\x01",
            "让他们乖乖听话吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        "#6P#0006F那个……\x02",
    )

    CloseMessageWindow()
    Jump("loc_94D8")

    label("loc_94D8")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0488
    ChrTalk(
        0x101,
        "#6P#0005F──等一下。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0489
    ChrTalk(
        0x101,
        (
            "#6P#0008F回想起来……\x01",
            "他们两个组织，为什么\x01",
            "要把对方『彻底击溃』呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0490
    ChrTalk(
        0x102,
        "#5P#0105F理由的话……\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x104,
        (
            "#2P#0305F那还用说，肯定是为了争地盘，\x01",
            "不然就是意气用事呗。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x101,
        (
            "#6P#0003F不对，如果只是这种原因的话，\x01",
            "在一般情况下，并不会展开彻底的厮杀。\x02\x03",

            "#0008F如果彼此之间存在什么重要的利害关系倒好理解，\x01",
            "但这只是街区里的不良少年团伙在起冲突而已……\x02\x03",

            "#0013F有必要做足充分的准备工作，\x01",
            "把对方彻底消灭掉吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0493
    ChrTalk(
        0x103,
        "#1P#0205F……真是吃惊。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x102,
        "#5P#0100F嗯，我也是。\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x104,
        "#2P#0302F呼～原来如此啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0496
    ChrTalk(
        0x101,
        (
            "#6P#0011F怎、怎么了……\x01",
            "我说了什么奇怪的话吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x102,
        (
            "#5P#0104F没有啦，我只是在想，\x01",
            "你真不愧是拥有搜查官资格的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x104,
        (
            "#2P#0300F确实是很不错的切入点呢。\x02\x03",

            "从表面上看来，那两个头目\x01",
            "之间的关系好像并没有那么\x01",
            "恶劣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x103,
        (
            "#1P#0203F……多半……\x01",
            "还存在着其它的理由吧。\x02\x03",

            "#0201F只有当事人自己才知晓的，\x01",
            "使他们决心要互相厮杀的理由。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，没错。\x01",
            "我就是这么想的。\x02\x03",

            "既然如此──\x01",
            "我们该做的事情也就只有一件了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x104,
        "#2P#0304F是啊。\x02",
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x102,
        (
            "#5P#0100F去拜访『剑蛇帮』\x01",
            "和『圣书会』……\x02\x03",

            "那么，先去哪一边进行\x01",
            "询问呢？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)
    OP_D5(0x30)
    OP_D5(0x31)
    SetMapObjFrame(0xFF, "h_kage", 0x1, 0x1)
    OP_68(1200, 2000, -1500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 1200, 0, -1500, 180)
    SetChrPos(0x1, 1200, 0, -1500, 180)
    SetChrPos(0x2, 1200, 0, -1500, 180)
    SetChrPos(0x3, 1200, 0, -1500, 180)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0xA, 8620, 0, 8810, 180)
    SetChrPos(0xB, 7900, 0, 9630, 135)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetScenarioFlags(0x42, 0)
    OP_29(0x3E, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_26_69CE end

    def Function_27_9AF4(): pass

    label("Function_27_9AF4")


    def lambda_9AF9():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_9AF9)
    SetChrSubChip(0x17, 0x2)
    Sleep(80)
    SetChrSubChip(0x17, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    Return()

    # Function_27_9AF4 end

    def Function_28_9B2A(): pass

    label("Function_28_9B2A")


    def lambda_9B2F():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_9B2F)
    SetChrSubChip(0x13, 0x2)
    Sleep(80)
    SetChrSubChip(0x13, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    OP_0D()
    Return()

    # Function_28_9B2A end

    def Function_29_9B60(): pass

    label("Function_29_9B60")

    OP_93(0x1B, 0x87, 0x1F4)
    ClearChrFlags(0x1B, 0x4)

    def lambda_9B71():
        OP_95(0xFE, 15100, -1600, -17800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_9B71)
    Sleep(1600)
    BeginChrThread(0x19, 3, 0, 31)
    Sleep(400)
    BeginChrThread(0x18, 3, 0, 31)
    Sleep(900)
    BeginChrThread(0x16, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 31)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x19, 3)
    Return()

    # Function_29_9B60 end

    def Function_30_9BBB(): pass

    label("Function_30_9BBB")

    BeginChrThread(0x1C, 3, 0, 32)
    OP_93(0x1A, 0xF0, 0x1F4)

    def lambda_9BCD():
        OP_95(0xFE, -11600, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_9BCD)
    Sleep(2400)
    BeginChrThread(0x15, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x14, 3, 0, 33)
    Sleep(800)
    BeginChrThread(0x12, 3, 0, 33)
    Sleep(400)
    BeginChrThread(0x13, 3, 0, 33)
    StopBGM(0x1F40)
    WaitChrThread(0x1C, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    Return()

    # Function_30_9BBB end

    def Function_31_9C20(): pass

    label("Function_31_9C20")

    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)

    def lambda_9C2E():
        OP_95(0xFE, 6100, 0, -7700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C2E)
    WaitChrThread(0xFE, 1)

    def lambda_9C4C():
        OP_95(0xFE, 15100, -1600, -17800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C4C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_31_9C20 end

    def Function_32_9C66(): pass

    label("Function_32_9C66")

    OP_93(0x1C, 0x14A, 0x1F4)

    def lambda_9C72():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFE4A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9C72)
    WaitChrThread(0x1C, 1)
    Sleep(400)
    OP_93(0x1C, 0xF0, 0x1F4)

    def lambda_9C9A():
        OP_95(0xFE, -11600, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9C9A)
    Return()

    # Function_32_9C66 end

    def Function_33_9CB0(): pass

    label("Function_33_9CB0")

    EndChrThread(0xFE, 0x2)

    def lambda_9CB9():
        OP_95(0xFE, -3700, 0, -7400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9CB9)
    WaitChrThread(0xFE, 1)

    def lambda_9CD7():
        OP_95(0xFE, -11600, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9CD7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_33_9CB0 end

    def Function_34_9CF1(): pass

    label("Function_34_9CF1")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00150.itc", 0x1E)
    LoadChrToIndex("apl/ch50017.itc", 0x1F)
    OP_68(45000, -1500, -22500, 0)
    MoveCamera(37, 30, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 43700, -2500, -23300, 90)
    SetChrPos(0x102, 43700, -2500, -21900, 90)
    SetChrPos(0x103, 42600, -2500, -23100, 90)
    SetChrPos(0x104, 42600, -2500, -21700, 90)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 47500, -2100, -22500, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 7)), scpexpr(EXPR_END)), "loc_9E6B")

    #N0503
    NpcTalk(
        0x8,
        "红衣少年",
        "#11P又、又来了吗！？\x02",
    )

    CloseMessageWindow()

    def lambda_9DFF():
        OP_96(0xFE, 0xB4DC, 0xFFFFF704, 0xFFFFA81C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9DFF)
    WaitChrThread(0x8, 1)

    #N0504
    NpcTalk(
        0x8,
        "红衣少年",
        (
            "#11P不是说过吗！像你们这种警察局的走狗，\x01",
            "别想和瓦鲁多大哥对话！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0EB")

    label("loc_9E6B")


    #N0505
    NpcTalk(
        0x8,
        "红衣少年",
        "#11P你、你们是……！\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x101,
        (
            "#6P#0005F这种打扮……\x02\x03",

            "#0001F莫非这里就是\x01",
            "『剑蛇帮』的据点吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x103,
        (
            "#6P#0203F小剧场『鬼火』……\x02\x03",

            "#0200F这里原来好像是仓库，然后才被\x01",
            "改造成小剧场的。\x02\x03",

            "因为没有交纳税金，\x01",
            "所以具体情况也不太了解……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9F5C():
        OP_96(0xFE, 0xB4DC, 0xFFFFF704, 0xFFFFA81C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9F5C)
    WaitChrThread(0x8, 1)

    #N0508
    NpcTalk(
        0x8,
        "红衣少年",
        "#11P不、不要无视我啊！\x02",
    )

    CloseMessageWindow()

    #N0509
    NpcTalk(
        0x8,
        "红衣少年",
        (
            "#11P虽说我只是个新人，\x01",
            "但好歹也是剑蛇帮的一员！\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x101,
        (
            "#6P#0006F啊……抱歉。\x02\x03",

            "#0001F那个……我们这次过来，\x01",
            "是有些事情想问问你们的首领……\x02\x03",

            "可以帮忙传达一声吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0511
    NpcTalk(
        0x8,
        "红衣少年",
        "#11P找瓦鲁多大哥？\x02",
    )

    CloseMessageWindow()

    #N0512
    NpcTalk(
        0x8,
        "红衣少年",
        (
            "#11P哼，你们这种警察局的走狗，\x01",
            "瓦鲁多大哥怎么会搭理！\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        "#6P#0011F那个，可是……\x02",
    )

    CloseMessageWindow()

    #N0514
    NpcTalk(
        0x8,
        "红衣少年",
        "#11P说不行就是不行！\x02",
    )

    CloseMessageWindow()

    label("loc_A0EB")


    #N0515
    NpcTalk(
        0x8,
        "红衣少年",
        "#11P赶快滚回去吧！\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x101,
        "#6P#0001F（这下棘手了……）\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x104,
        (
            "#0300F#6P（不过，就不良少年来说，\x01",
            "  这小鬼还真挺可爱的……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    #C0518
    ChrTalk(
        0x102,
        (
            "#0102F#5P──请问，\x01",
            "你叫什么名字呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A201():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A201)

    def lambda_A20E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A20E)

    def lambda_A21B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A21B)
    WaitChrThread(0x101, 2)

    #N0519
    NpcTalk(
        0x8,
        "红衣少年",
        "#11P我、我吗？\x02",
    )

    CloseMessageWindow()

    #N0520
    NpcTalk(
        0x8,
        "红衣少年",
        "#11P叫、叫迪诺啦。\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x102,
        (
            "#0104F#5P是吗，迪诺啊。\x02\x03",

            "#0100F迪诺，你的工作是在这里看守，\x01",
            "防止可疑人员接近吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x8,
        "#11P对、对啊！\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x8,
        (
            "#11P这可是瓦鲁多大哥亲自交给我的任务，\x01",
            "他让我在这里好好看守，\x01",
            "不要放圣书会的那群家伙进去！\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x8,
        (
            "#11P才、才不是被其他前辈\x01",
            "强迫看门的哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x102,
        (
            "#0103F#5P原来如此，确实是很重要的工作呢。\x02\x03",

            "#0101F不过，我们并不是\x01",
            "圣书会的成员哦。\x02\x03",

            "所以，你就算让我们进去\x01",
            "也没关系吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x8,
        "#11P可、可是……\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        (
            "#11P你们刚刚还和前辈们打过架，\x01",
            "要是让你们进去的话……\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x102,
        (
            "#0109F#5P呵呵，虽说是战斗过，\x01",
            "但那种程度的小争斗，对你们来说，\x01",
            "不就像打个招呼一样吗？\x02\x03",

            "#0102F你们的首领好像也\x01",
            "没放在心上呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x8,
        "#11P但、但是……\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x102,
        (
            "#0106F#5P嗯～如果你还是\x01",
            "不能相信我们的话──\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A4F9():

        label("loc_A4F9")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_A4F9")

    QueueWorkItem2(0x101, 2, lambda_A4F9)

    def lambda_A50B():

        label("loc_A50B")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_A50B")

    QueueWorkItem2(0x103, 2, lambda_A50B)
    OP_68(45330, -1500, -22310, 1000)

    def lambda_A52E():
        OP_96(0xFE, 0xB02C, 0xFFFFF63C, 0xFFFFA81C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A52E)
    WaitChrThread(0x102, 1)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0531
    ChrTalk(
        0x8,
        "#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x101,
        "#6P#0005F喂、喂……！？\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x103,
        "#6P#0205F艾莉前辈……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    #Sound(1174, 255, 100, 0)    #voice#Elie
    Fade(250)
    SetChrFlags(0x102, 0x10)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sleep(800)

    #C0534
    ChrTalk(
        0x102,
        (
            "#5P#0100F──把我的枪\x01",
            "交给你保管也可以啊。\x02\x03",

            "对我来说，这可是非常重要的东西，\x01",
            "所以希望你之后能完好无损地还给我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x8,
        "#11P……～～这～～……！\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x8,
        (
            "#11P好、好啦！\x01",
            "也、也用不着这样啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x8,
        (
            "#11P我去问问瓦鲁多大哥就是了！\x01",
            "你们可绝对不要趁机进来啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)

    def lambda_A75E():
        OP_95(0xFE, 48000, -2100, -22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A75E)
    Sleep(800)
    Fade(100)
    ClearChrFlags(0x102, 0x10)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    WaitChrThread(0x8, 1)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xF, 0x0, 0x0)
    Sound(116, 0, 100, 0)
    OP_79(0x4)

    def lambda_A7B2():
        OP_95(0xFE, 50000, -2100, -22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A7B2)

    def lambda_A7CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A7CC)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    OP_71(0x4, 0xF, 0x0, 0x0, 0x0)
    Sound(117, 0, 100, 0)
    OP_79(0x4)
    OP_68(44610, -1500, -22020, 1200)

    def lambda_A80B():
        OP_96(0xFE, 0xAAB4, 0xFFFFF63C, 0xFFFFAA74, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A80B)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x1)

    #C0538
    ChrTalk(
        0x104,
        "#0302F#6P哎呀呀，你可真够大胆啊。\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x103,
        "#6P#0206F吓了一跳呢……\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        (
            "#12P#0004F……好厉害啊，艾莉。\x02\x03",

            "#0002F那么高明的交涉手段，\x01",
            "我无论如何也做不到呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    #C0541
    ChrTalk(
        0x102,
        (
            "#0104F#5P呵呵，像这类交涉我早就习惯了，\x01",
            "有这种事的话，交给我就好。\x02\x03",

            "#0108F不过，对瓦鲁多那样的人\x01",
            "应该是行不通的。\x02\x03",

            "#0101F到时还是由你来出面交涉吧，\x01",
            "就像和瓦吉交谈时那样。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        "#12P#0000F……嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    OP_71(0x4, 0x0, 0xF, 0x0, 0x0)
    Sound(116, 0, 100, 0)
    OP_79(0x4)

    def lambda_A9C0():
        OP_95(0xFE, 46200, -2400, -22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A9C0)

    def lambda_A9DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A9DA)

    def lambda_A9EB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A9EB)
    Sleep(50)

    def lambda_A9FB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A9FB)
    Sleep(50)

    def lambda_AA0B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AA0B)
    Sleep(50)

    def lambda_AA1B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AA1B)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    OP_71(0x4, 0xF, 0x0, 0x0, 0x0)
    Sound(117, 0, 100, 0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)

    #C0543
    ChrTalk(
        0x8,
        "#11P瓦鲁多大哥叫你们进去！\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x8,
        (
            "#11P光是进去的话当然没关系……\x01",
            "但如果敢做出什么可疑的举动，\x01",
            "我可不会轻易放过你们！\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x102,
        "#0109F#6P呵呵，谢谢你。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x101,
        "#6P#0002F那我们就先失陪了。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 44880, -2500, -20090, 225)
    SetChrPos(0x0, 43000, -2500, -22500, 90)
    SetScenarioFlags(0x42, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_34_9CF1 end

    def Function_35_AB48(): pass

    label("Function_35_AB48")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("apl/ch50010.itc", 0x1F)
    LoadEffect(0x0, "event\\eva02_00.eff")
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_68(40100, -1300, -23900, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 44400, -2500, -23600, 270)
    SetChrPos(0x102, 44400, -2500, -22200, 270)
    SetChrPos(0x103, 45800, -2500, -23600, 270)
    SetChrPos(0x104, 45800, -2500, -22200, 270)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    OP_52(0x1D, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")

    def lambda_AC53():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC53)
    Sleep(50)

    def lambda_AC70():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AC70)
    Sleep(50)

    def lambda_AC8D():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC8D)
    Sleep(50)

    def lambda_ACAA():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ACAA)
    SetCameraDistance(19500, 3000)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)

    def lambda_ACDA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ACDA)
    WaitChrThread(0x102, 1)

    def lambda_ACEB():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_ACEB)
    WaitChrThread(0x103, 1)

    def lambda_ACFC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_ACFC)
    WaitChrThread(0x104, 1)

    def lambda_AD0D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AD0D)
    WaitChrThread(0x104, 2)
    OP_6F(0x10)

    #C0547
    ChrTalk(
        0x102,
        (
            "#1P#0108F……这是怎么回事呢？\x02\x03",

            "#0101F两边的成员\x01",
            "竟然都遭到了暗算。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x103,
        (
            "#2P#0203F其中有一方在说谎……？\x01",
            "好像也不是这么回事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x101,
        "#6P#0008F…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AE24():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AE24)

    def lambda_AE31():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AE31)

    def lambda_AE3E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AE3E)
    WaitChrThread(0x103, 2)

    #C0550
    ChrTalk(
        0x102,
        "#1P#0105F……怎么了？\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x104,
        (
            "#5P#0301F难道是刚才单挑的时候，\x01",
            "伤到哪里了吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x101,
        (
            "#6P#0000F啊，没有……\x02\x03",

            "对方也有手下留情，\x01",
            "没什么大碍。\x02\x03",

            "#0003F只是，感觉有点奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x103,
        "#2P#0205F奇怪……吗？\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯……\x02\x03",

            "#0008F双方的成员都是在五天前的夜晚被人暗算……\x01",
            "在不同的场所，同时遭到袭击。\x02\x03",

            "就算两边的人是在偶然的情况下，\x01",
            "正好在同一时间去暗算对方……\x02\x03",

            "#0001F可那么多人同时行动，双方却都\x01",
            "没有察觉到对方，这可能吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x102,
        "#1P#0101F啊……\x02",
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x104,
        (
            "#5P#0303F……确实如此。\x02\x03",

            "#0301F毕竟两方都不是专业的战斗人员，\x01",
            "一般来说，这种情况是不可能发生的。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x103,
        (
            "#2P#0201F那么，会不会是其中一方先被偷袭了，\x01",
            "然后另一方为了报复而展开行动呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x102,
        (
            "#1P#0103F不，那样也很难说得通。\x02\x03",

            "#0108F先出手暗算的一方，肯定会有所警戒，\x01",
            "防止对方前来报复的……\x02\x03",

            "可是，双方的成员都是在\x01",
            "丝毫没有防备的情况下遭到袭击的……\x02\x03",

            "#0101F……是这样吧，罗伊德？\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯……\x01",
            "这个事件，确实有些蹊跷。\x02\x03",

            "#0008F我们现在缺少的，\x01",
            "似乎是拼图中最关键的那一片啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x1D, 31700, -2500, -23600, 90)
    SetChrFlags(0x1D, 0x8)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)

    #N0560
    NpcTalk(
        0x1D,
        "女性的声音",
        "哼哼，你们好像遇到困难了吧？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B2A1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B2A1)

    def lambda_B2AE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B2AE)

    def lambda_B2BB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B2BB)

    def lambda_B2C8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B2C8)
    WaitChrThread(0x101, 2)
    Fade(500)
    OP_68(33700, -1400, -23600, 0)
    MoveCamera(313, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 39300, -2500, -24200, 270)
    SetChrPos(0x102, 39300, -2500, -23000, 270)
    SetChrPos(0x103, 40800, -2500, -24200, 270)
    SetChrPos(0x104, 40800, -2500, -23000, 270)
    ClearChrFlags(0x1D, 0x8)
    SetChrPos(0x1D, 31700, -2500, -23600, 90)
    OP_68(38200, -1400, -23600, 2500)
    SetCameraDistance(20500, 2500)

    def lambda_B380():
        OP_95(0xFE, 36700, -2500, -23600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B380)
    WaitChrThread(0x1D, 1)
    OP_6F(0x11)

    #C0561
    ChrTalk(
        0x101,
        "#12P#0005F您、您是……！？\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x102,
        "#0105F克洛斯贝尔时代周刊的……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("女性")

    #A0563
    AnonymousTalk(
        0xFF,
        (
            "Ｈｅｌｌｏ、ｈｅｌｌｏ～\x01",
            "又见面了哦。\x02\x03",

            "哦，很不错的画面呢。\x02",
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

    def lambda_B48C():
        OP_96(0xFE, 0x8F5C, 0xFFFFF63C, 0xFFFFA1DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B48C)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0x1D, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)

    def lambda_B4FD():
        OP_96(0xFE, 0x8F5C, 0xFFFFF63C, 0xFFFFA5C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B4FD)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0x1D, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)

    def lambda_B56E():
        OP_96(0xFE, 0x8F5C, 0xFFFFF63C, 0xFFFFA3D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B56E)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0x1D, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)

    #C0564
    ChrTalk(
        0x101,
        "#12P#0001F这……\x02",
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x103,
        "#12P#0211F……您这是侵犯肖像权。\x02",
    )

    CloseMessageWindow()

    #N0566
    NpcTalk(
        0x1D,
        "女性",
        (
            "#2109F#5P呀哈哈～只是职业病啦，\x01",
            "一看到不错的画面，就会不自觉地\x01",
            "拍下来，已经形成条件反射了。\x02\x03",

            "#2102F而且，我到时说不定还会\x01",
            "将这张照片用在报道里，\x02\x03",

            "你们就别这么小气了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x101,
        "#12P#0001F那、那个……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_END)), "loc_B71F")

    #C0568
    ChrTalk(
        0x102,
        (
            "#0101F您又想写一些那样的报道，\x01",
            "然后来取笑我们吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B789")

    label("loc_B71F")


    #C0569
    ChrTalk(
        0x102,
        (
            "#0103F您之前好像就给我们\x01",
            "写了一篇很有趣的报道……\x02\x03",

            "#0101F难道又想写些那样的报道，\x01",
            "然后来取笑我们吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B789")

    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    OP_0D()
    Sleep(300)

    #N0570
    NpcTalk(
        0x1D,
        "女性",
        (
            "#2109F#5P啊哈哈，多亏了各位表现活跃，\x01",
            "那篇报道好像引起了很大的反响呢～\x02\x03",

            "#2100F先不说那个啦，你们这次好像\x01",
            "又探听到了什么有趣的消息吧？\x02\x03",

            "姐姐我正好出来取材，\x01",
            "能不能帮点忙啊？\x02\x03",

            "作为给上次那篇报道提供素材的谢礼，\x01",
            "姐姐就请你们吃顿饭吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x101,
        (
            "#12P#0003F这……\x02\x03",

            "#0001F调查过程中掌握到的情报，\x01",
            "是不可能那么轻易就泄露给外人的吧。\x02\x03",

            "更别说是媒体界的人士了。\x02",
        )
    )

    CloseMessageWindow()

    #N0572
    NpcTalk(
        0x1D,
        "女性",
        (
            "#2106F#5P真是的，好不给面子啊。\x02\x03",

            "难得我想请你们吃顿\x01",
            "美味的东方料理……\x02\x03",

            "#2102F……作为饭后的甜点，\x01",
            "还可以给你们上一道『拼图碎片』哦。\x02",
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

    #C0573
    ChrTalk(
        0x101,
        "#12P#0005F什么……\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x104,
        (
            "#0303F原来如此……\x01",
            "是想交换情报啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0575
    NpcTalk(
        0x1D,
        "女性",
        (
            "#2104F#5P哼哼哼，如何……¤\x02\x03",

            "#2100F如果有兴趣的话，\x01",
            "就来东街出口附近的\x01",
            "『龙老饭店』找我吧。\x02\x03",

            "姐姐我一个人先过去，\x01",
            "到那里边喝东西边等你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x10E, 0x1F4)

    def lambda_BAE0():
        OP_95(0xFE, 35700, -2500, -23600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BAE0)
    WaitChrThread(0x1D, 1)
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x1D, 0x5A, 0x1F4)

    #N0576
    NpcTalk(
        0x1D,
        "女性",
        (
            "#5P#2105F──对了对了，\x01",
            "都还没有报上名字呢。\x02\x03",

            "#2100F我是《克洛斯贝尔时代周刊》的记者，\x01",
            "格蕾丝·琳。\x02\x03",

            "#2109F你们可以叫我格蕾丝姐姐哦¤\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x10E, 0x1F4)

    def lambda_BBB1():
        OP_95(0xFE, 25700, -2500, -23600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BBB1)
    Sleep(3000)
    Fade(1000)
    OP_68(40100, -1300, -23900, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 39400, -2500, -24600, 270)
    SetChrPos(0x102, 39400, -2500, -23200, 270)
    SetChrPos(0x103, 40800, -2500, -24600, 270)
    SetChrPos(0x104, 40800, -2500, -23200, 270)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    WaitChrThread(0x1D, 1)
    ClearChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)

    #C0577
    ChrTalk(
        0x101,
        (
            "#11P#0001F格蕾丝·琳……\x01",
            "克洛斯贝尔时代周刊的记者吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xE1, 0x190)

    #C0578
    ChrTalk(
        0x104,
        (
            "#5P#0300F虽然那个姐姐的举动很可疑，\x01",
            "但好像确实掌握了不少情报呢。\x02\x03",

            "要不要接受她的邀请呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BD50():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BD50)
    Sleep(100)

    def lambda_BD60():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BD60)
    Sleep(50)

    def lambda_BD70():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BD70)
    WaitChrThread(0x101, 2)

    #C0579
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯、嗯～……\x02\x03",

            "#0001F吃饭什么的倒无所谓，\x01",
            "先去听听她要说什么吧。\x02\x03",

            "既然已经无法指望总部帮忙了，\x01",
            "至少也要多搜集一些情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x102,
        (
            "#1P#0103F……是啊。\x01",
            "毕竟是记者，应该会有不少情报吧。\x02\x03",

            "#0101F只是，我们也要注意，\x01",
            "不要泄露不该说的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x103,
        (
            "#2P#0203F……同感。\x02\x03",

            "#0211F她好像是那种，只要别人稍微放松警惕，\x01",
            "就会马上穷追猛打的类型呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x101,
        (
            "#6P#0002F（嗯～……\x01",
            "  说得还真是一针见血啊。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(40100, -500, -23900, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 40100, -2500, -23900, 270)
    SetChrPos(0x1, 40100, -2500, -23900, 270)
    SetChrPos(0x2, 40100, -2500, -23900, 270)
    SetChrPos(0x3, 40100, -2500, -23900, 270)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetScenarioFlags(0x42, 4)
    OP_29(0x3E, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_35_AB48 end

    def Function_36_BFA2(): pass

    label("Function_36_BFA2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-19000, 1000, -10300, 0)
    MoveCamera(60, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -19700, 0, -11000, 45)
    SetChrPos(0x102, -18300, 0, -11000, 315)
    SetChrPos(0x103, -19700, 0, -9600, 135)
    SetChrPos(0x104, -18300, 0, -9600, 225)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    MoveCamera(70, 30, 0, 3000)
    SetCameraDistance(17500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0583
    ChrTalk(
        0x102,
        (
            "#0106F……没想到所有的人\x01",
            "都失踪了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x104,
        (
            "#5P#0303F不祥的预感应验了呢…… \x02\x03",

            "#0301F是自发性的离开，\x01",
            "还是被人绑架了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x103,
        (
            "#6P#0206F现阶段的情报实在太少了，\x01",
            "两种可能性都要考虑到。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_C1CE")

    #C0586
    ChrTalk(
        0x101,
        (
            "#12P#0003F……这五名失踪人员\x01",
            "说不定只是冰山一角。\x02\x03",

            "#0001F在克洛斯贝尔全市，\x01",
            "很可能已经有相当多的人\x01",
            "失踪了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C243")

    label("loc_C1CE")


    #C0587
    ChrTalk(
        0x101,
        (
            "#12P#0003F……这四名失踪人员\x01",
            "说不定只是冰山一角。\x02\x03",

            "#0001F在克洛斯贝尔全市，\x01",
            "很可能已经有相当多的人\x01",
            "失踪了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C243")


    #C0588
    ChrTalk(
        0x102,
        (
            "#0108F嗯……\x01",
            "到底有多少人\x01",
            "下落不明了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x104,
        (
            "#5P#0301F怎么办，罗伊德？\x02\x03",

            "要一个一个找的话，\x01",
            "实在是太勉强了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x101,
        (
            "#12P#0006F嗯……凭我们的人手，\x01",
            "确实是严重不足。\x02\x03",

            "#0008F在这种时候，一科却迫于上层的压力\x01",
            "而无法行动，真是让人头疼啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x103,
        (
            "#6P#0202F不然去找二科的多诺邦警督，\x01",
            "问问他能不能帮忙吧？\x02\x03",

            "毕竟我们以前也帮过他的忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#12P#0003F不行……这应该也很难。\x02\x03",

            "#0001F既然连达德利搜查官都无计可施，\x01",
            "只能前来请求支援科帮忙，\x01",
            "二科想必也承受着相当的压力。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x103,
        "#6P#0206F原来如此……的确呢。\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x102,
        (
            "#0108F如此说来，公共安全科\x01",
            "的情况应该也是一样吧……\x02\x03",

            "#0106F如果能借助警队的人力，\x01",
            "情况就会大有改善了……\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C4F8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C4F8)
    Sleep(50)

    def lambda_C508():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C508)
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
    SetMessageWindowPos(90, 130, -1, -1)

    #A0595
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性的声音")

    #A0596
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "喂，新人们……！\x02\x03",

            "你们没干什么\x01",
            "多余的事吧……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0597
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011F哎……\x02\x03",

            "#0001F这声音……莫非是\x01",
            "达德利搜查官吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0598
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "什么莫非不莫非的！\x02\x03",

            "你们几个难道又擅自行动，\x01",
            "到鲁巴彻那边捣乱了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0599
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F没、没有……\x02\x03",

            "#0003F我们现在正在专心\x01",
            "调查药物方面的事情呢。\x02\x03",

            "#0001F……请问发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0600
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那还用问吗！\x01",
            "他们的事务所……\x02\x03",

            "……咳咳，没什么。\x02\x03",

            "既然不是你们干的，那就没事了。\x01",
            "继续调查你们的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(825, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0601
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F啊……\x02",
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
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0602
    ChrTalk(
        0x101,
        "#12P#0013F………………………………\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x102,
        (
            "#0101F是达德利搜查官吗？\x01",
            "发生什么事了？\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x101,
        "#12P#0006F这个……\x02",
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
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0605
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将与达德利的谈话内容\x01",
            "转告给了艾莉等人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0606
    ChrTalk(
        0x104,
        "#5P#0301F那是什么意思啊……\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x103,
        (
            "#6P#0206F……明显很蹊跷呢。\x02\x03",

            "#0201F难道鲁巴彻商会那里\x01",
            "发生了什么情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x101,
        "#12P#0003F很有可能……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0609
    ChrTalk(
        0x104,
        (
            "#5P#0300F既然如此，我们也只能\x01",
            "过去看看情况了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x102,
        (
            "#0103F是啊……虽然已经被警告过，\x01",
            "让我们别再去管黑手党内斗的事情了……\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x103,
        (
            "#6P#0202F不过，如果失踪人员与黑手党有关，\x01",
            "我们应该就可以名正言顺地展开调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x101,
        (
            "#12P#0001F嗯……\x01",
            "赶快前往鲁巴彻商会吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -19000, 0, -10000, 180)
    SetScenarioFlags(0xC3, 7)
    OP_29(0x4C, 0x1, 0xC)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_36_BFA2 end

    def Function_37_CAE8(): pass

    label("Function_37_CAE8")

    EventBegin(0x1)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB69")

    #C0613
    ChrTalk(
        0xF,
        "……等一下。\x02",
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xF,
        (
            "不好意思，瓦吉他们正在谈事情。\x01",
            "不能让你们\x01",
            "进去打扰。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xF,
        "无关人员请离开。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_CBAA")

    label("loc_CB69")


    #C0616
    ChrTalk(
        0xF,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xF,
        (
            "如果是客人的话，\x01",
            "请过两天再来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBAA")

    Sleep(50)
    SetChrPos(0x0, -19660, 0, -10600, 180)
    OP_93(0xF, 0xE1, 0x0)
    OP_4C(0xF, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_37_CAE8 end

    def Function_38_CBCC(): pass

    label("Function_38_CBCC")

    TalkBegin(0xFF)
    OP_4B(0x8, 0xFF)
    SetChrName("")

    #A0618
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可以听到嘈杂的音乐声\x01",
            "隐隐从里面传出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0x0, 500)

    #C0619
    ChrTalk(
        0x8,
        (
            "喂、喂！\x01",
            "这里是禁止外部人员入内的！\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x8,
        "到一边去！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCDD")
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0621
    ChrTalk(
        0x101,
        "#0001F（总觉得情况有些可疑……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 0)

    label("loc_CCDD")

    OP_93(0x8, 0xE1, 0x1F4)
    OP_4C(0x8, 0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_38_CBCC end

    def Function_39_CCEC(): pass

    label("Function_39_CCEC")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0622
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『纳因瓦利』\x01",
            "　　　今天临时停业。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_39_CCEC end

    def Function_40_CD3D(): pass

    label("Function_40_CD3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD60")
    Call(0, 42)
    Jump("loc_CE00")

    label("loc_CD60")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0623
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "公寓『伊梅尔达馆』\x01\x01",
            "～ 目前停止经营 ～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDFD")

    #C0624
    ChrTalk(
        0x101,
        (
            "#0001F非常肮脏……\x01",
            "好像已经很长时间无人使用了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 7)

    label("loc_CDFD")

    TalkEnd(0xFF)

    label("loc_CE00")

    Return()

    # Function_40_CD3D end

    def Function_41_CE01(): pass

    label("Function_41_CE01")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00400.itc", 0x1E)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    OP_71(0x4, 0xF, 0xF, 0x0, 0x0)
    OP_68(43800, -490, -23000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 49400, -2500, -23600, 270)
    SetChrPos(0x102, 49400, -2500, -22200, 270)
    SetChrPos(0x103, 50800, -2500, -23600, 270)
    SetChrPos(0x104, 50800, -2500, -22200, 270)
    SetChrPos(0x1A, 34870, -2490, -22900, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_CEE0():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CEE0)

    def lambda_CEFA():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CEFA)
    Sleep(50)

    def lambda_CF0E():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CF0E)

    def lambda_CF28():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CF28)
    Sleep(50)

    def lambda_CF3C():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CF3C)

    def lambda_CF56():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CF56)
    Sleep(50)

    def lambda_CF6A():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CF6A)

    def lambda_CF84():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CF84)
    SetCameraDistance(20000, 3000)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)

    def lambda_CFAB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CFAB)
    WaitChrThread(0x102, 1)

    def lambda_CFBC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CFBC)
    WaitChrThread(0x103, 1)

    def lambda_CFCD():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CFCD)
    WaitChrThread(0x104, 1)

    def lambda_CFDE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CFDE)
    WaitChrThread(0x104, 2)
    OP_6F(0x10)
    OP_71(0x4, 0xF, 0x0, 0x0, 0x0)
    Sound(117, 0, 100, 0)

    #C0625
    ChrTalk(
        0x104,
        "#0301F这是怎么回事啊……\x02",
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x102,
        (
            "#0108F虽然还不了解具体情况，\x01",
            "但没有找到名单上的\x01",
            "迪诺呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x101,
        (
            "#0003F#6P嗯，而且那些家伙的样子\x01",
            "好像也不太正常……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)

    #N0628
    NpcTalk(
        0x1A,
        "冷静的声音",
        "──哟，现在方便吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(42800, -490, -23000, 2000)

    def lambda_D122():
        OP_97(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_D122)

    def lambda_D13C():
        TurnDirection(0x101, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D13C)
    Sleep(50)

    def lambda_D14C():
        TurnDirection(0x102, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D14C)
    Sleep(50)

    def lambda_D15C():
        TurnDirection(0x103, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D15C)
    Sleep(50)

    def lambda_D16C():
        TurnDirection(0x104, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D16C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x1A, 1)

    #C0629
    ChrTalk(
        0x103,
        (
            "#0205F#11P瓦吉先生，\x01",
            "你为什么会在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x1A,
        (
            "#0404F因为我很在意剑蛇帮的情况。\x02\x03",

            "#0400F新加入不久的那个少年，\x01",
            "从今天早上开始就不见人影了。\x02\x03",

            "#0406F呼，不过，毕竟他干出了那样的事，\x01",
            "我倒是隐隐猜到会变成这样了……\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x104,
        "#0305F#11P你……知道些什么吗？\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x1A,
        (
            "#0402F算是吧。\x02\x03",

            "#0409F别在这里傻站着，\x01",
            "来崔尼蒂说吧。\x02\x03",

            "只要是我知道的，\x01",
            "全都会告诉你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x10E, 0x1F4)
    OP_97(0x1A, 0xFFFFE890, 0x0, 0x0, 0xBB8, 0x0)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x8000)

    #C0633
    ChrTalk(
        0x101,
        (
            "#0006F#11P……关于剑蛇帮\x01",
            "的情报，似乎也只能\x01",
            "依靠瓦吉了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x102,
        (
            "#0101F#11P是啊……\x01",
            "剑蛇帮内部曾经发生过什么，\x01",
            "似乎只有这点确凿无疑呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_71(0x4, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x10)
    OP_68(43500, -490, -22900, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 43500, -2490, -22900, 270)
    SetChrPos(0x1, 43500, -2490, -22900, 270)
    SetChrPos(0x2, 43500, -2490, -22900, 270)
    SetChrPos(0x3, 43500, -2490, -22900, 270)
    SetScenarioFlags(0xD0, 5)
    OP_29(0x4C, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_41_CE01 end

    def Function_42_D438(): pass

    label("Function_42_D438")

    EventBegin(0x0)
    Fade(500)
    OP_68(34400, 3600, -20130, 0)
    MoveCamera(35, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19680, 0)
    SetChrPos(0x101, 34840, 2450, -21150, 0)
    SetChrPos(0x102, 35840, 2450, -21150, 315)
    SetChrPos(0x103, 33840, 2450, -21150, 45)
    SetChrPos(0x104, 32840, 2450, -21150, 45)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0635
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "公寓『伊梅尔达馆』\x01\x01",
            "～ 目前停止经营 ～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0636
    ChrTalk(
        0x101,
        (
            "#11P#0000F这里好像就是伊梅尔达夫人\x01",
            "说的那家公寓吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x102,
        (
            "#11P#0100F现在停止经营……\x01",
            "都已经相当肮脏破旧了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x103,
        (
            "#5P#0200F不管怎么说，\x01",
            "我们先进去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x101,
        "#11P#0000F啊，稍等一下。\x02",
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(200)
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)

    #C0640
    ChrTalk(
        0x101,
        (
            "#5P#0003F好，打开了。\x02\x03",

            "#0001F里面会有魔兽徘徊，所以\x01",
            "一定不要大意啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x104,
        (
            "#5P#0300F好，那我们就拿出干劲，\x01",
            "进去消灭它们吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 34840, 2450, -20500, 0)
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x1, 0x10)
    SetScenarioFlags(0x6E, 6)
    EventEnd(0x5)
    Return()

    # Function_42_D438 end

    def Function_43_D691(): pass

    label("Function_43_D691")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0x11, 0x40)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    Call(0, 44)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch30953.itc", 0x2A)
    LoadChrToIndex("chr/ch31853.itc", 0x2B)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Call(0, 45)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch30853.itc", 0x2C)
    LoadChrToIndex("chr/ch31753.itc", 0x2D)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    LoadChrToIndex("chr/ch30951.itc", 0x32)
    LoadChrToIndex("chr/ch31851.itc", 0x33)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Call(0, 46)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8CE")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch30953.itc", 0x2A)
    LoadChrToIndex("chr/ch31853.itc", 0x2B)
    LoadChrToIndex("chr/ch30853.itc", 0x2C)
    LoadChrToIndex("chr/ch31753.itc", 0x2D)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_29(0x12, 0x1, 0x4)
    OP_2C(0x12, 0x5)
    Call(0, 49)
    Jump("loc_D977")

    label("loc_D8CE")

    OP_32(0x0, 0xFC, 0x1)
    OP_32(0x1, 0xFC, 0x1)
    OP_32(0x2, 0xFC, 0x1)
    OP_32(0x3, 0xFC, 0x1)
    OP_32(0x0, 0x2, 0x1)
    OP_32(0x1, 0x2, 0x1)
    OP_32(0x2, 0x2, 0x1)
    OP_32(0x3, 0x2, 0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch00153.itc", 0x27)
    LoadChrToIndex("chr/ch00253.itc", 0x28)
    LoadChrToIndex("chr/ch00353.itc", 0x29)
    LoadChrToIndex("chr/ch30853.itc", 0x2C)
    LoadChrToIndex("chr/ch31753.itc", 0x2D)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_29(0x12, 0x1, 0x3)
    Call(0, 50)

    label("loc_D977")

    Call(0, 51)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0642
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【圣书会的训练委托】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9F0")
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)
    Jump("loc_DA0E")

    label("loc_D9F0")

    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)

    label("loc_DA0E")

    SetChrPos(0x0, 130, 0, -5310, 0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0x21, 0x40)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAAD")
    SetChrPos(0xA, -10970, 0, -9240, 135)
    SetChrPos(0xB, -11920, 0, -9620, 45)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 0)

    label("loc_DAAD")

    OP_29(0x12, 0x4, 0x10)
    OP_29(0x12, 0x1, 0x5)
    SetScenarioFlags(0x0, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_43_D691 end

    def Function_44_DAC1(): pass

    label("Function_44_DAC1")

    OP_68(830, 1200, -3860, 0)
    MoveCamera(176, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22640, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3150, 0, -4000, 270)
    SetChrPos(0x1F, 4080, 0, -4770, 270)
    SetChrPos(0x20, 4550, 0, -3310, 270)
    SetChrPos(0x1E, 5260, 0, -4350, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x22)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x22)
    SetChrSubChip(0x20, 0x0)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetCameraDistance(20640, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0643
    ChrTalk(
        0x1C,
        "#5P形式是四对四的战斗。\x02",
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x1C,
        (
            "#5P圣书会的成员要全力以赴，\x01",
            "向特别任务支援科发动攻击！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 40, -1, -1)
    SetChrName("众成员")

    #A0645
    AnonymousTalk(
        0xFF,
        "#5S收到！  \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0646
    ChrTalk(
        0x1F,
        (
            "就、就让我们好好领教一下\x01",
            "警察的防身术吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xF,
        (
            "哼，我们这边可是会\x01",
            "全力攻击的……\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0xF,
        (
            "你们要是太没用，\x01",
            "就只能被当场打倒。\x01",
            "做好觉悟吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x104,
        (
            "#12P#0300F喔喔～\x01",
            "真是群充满活力的家伙，不错不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x101,
        (
            "#12P#0003F本以为，只要展示一下我们的战斗方式，\x01",
            "把他们压制住就可以完成任务了……\x02\x03",

            "#0001F但我们要是手下留情，\x01",
            "也就达不到训练的目的了。\x02\x03",

            "各位，用不着客气。\x01",
            "拿出全力吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x102,
        "#11P#0101F嗯！\x02",
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x103,
        "#12P#0201F了解！\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x1C,
        "#5P#4S──那么，战斗开始！\x02",
    )

    CloseMessageWindow()
    StopBGM(0x3E8)
    Battle("BattleInfo_88C", 0x0, 0x0, 0x4, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_44_DAC1 end

    def Function_45_DE68(): pass

    label("Function_45_DE68")

    OP_68(830, 1200, -3860, 0)
    MoveCamera(176, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20640, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3150, 0, -4000, 270)
    SetChrPos(0x1F, 4080, 0, -4770, 270)
    SetChrPos(0x20, 4550, 0, -3310, 270)
    SetChrPos(0x1E, 5260, 0, -4350, 270)
    SetChrPos(0x21, 10500, -230, -14120, 314)
    SetChrPos(0xD, 11110, -680, -15910, 314)
    SetChrPos(0xE, 12100, -550, -14490, 314)
    SetChrPos(0x11, 13530, -1180, -16690, 314)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x3)
    SetChrChipByIndex(0xF, 0x2B)
    SetChrSubChip(0xF, 0x3)
    SetChrChipByIndex(0x1F, 0x2A)
    SetChrSubChip(0x1F, 0x3)
    SetChrChipByIndex(0x1E, 0x2A)
    SetChrSubChip(0x1E, 0x3)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrSubChip(0x20, 0x3)
    SetChrChipByIndex(0x21, 0x5)
    SetChrSubChip(0x21, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0654
    ChrTalk(
        0x101,
        (
            "#12P#0003F呼，这样就行了吧……\x02\x03",

            "#0000F你们几个，不要紧吧？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_95(0x101, -880, 0, -4000, 1000, 0x0)
    Sleep(300)

    #C0655
    ChrTalk(
        0x1F,
        "#5P被、被、被打败了啊……\x02",
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0xF,
        "#5P啊啊，果然很强……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x2E)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x2E)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0657
    ChrTalk(
        0x20,
        (
            "#5P都已经这么拼命攻击了……\x01",
            "为什么还是不能干掉他们！？\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x101,
        (
            "#12P#0000F这就是警察所使用的压制格斗技。\x02\x03",

            "是高级课程中所教授的内容，\x01",
            "在四人组合战中也能派上用场。\x02\x03",

            "#0003F身为警察，并不能只考虑自己，\x01",
            "也必须要守护好自己\x01",
            "背后的人们才行。\x02\x03",

            "所以，无论如何也不能输……\x01",
            "我们就是在这样的心态下，不断经受各种训练的。\x02\x03",

            "#0000F……不过，你们目前\x01",
            "只需要保护好自己就可以了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x20, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)
    OP_64(0x20)
    OP_64(0x1E)
    OP_64(0x1F)
    Sleep(300)

    #C0659
    ChrTalk(
        0xF,
        (
            "#5P……原来警察也不是\x01",
            "外强中干的草包啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0xF,
        "#5P好像学到了很多东西呢。\x02",
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x1E,
        (
            "#5P嗯，这场虽然完全输掉了……\x01",
            "但下次应该就能活用今天学到的东西了。\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x104,
        (
            "#12P#0300F嘿，经过这么一番战斗，\x01",
            "发现这些家伙其实挺坦率的，这还真是意外。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x102,
        (
            "#12P#0100F对战的时候\x01",
            "我们没有手下留情呢……\x01",
            "是不是有些过分了呢，他们没事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x103,
        (
            "#12P#0200F从他们的样子来看，\x01",
            "我想是没什么大问题……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(10, 10, -1, -1)
    SetChrName("青年的声音")

    #A0665
    AnonymousTalk(
        0xFF,
        "#4P──渣滓们。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_E4AB():

        label("loc_E4AB")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_E4AB")

    QueueWorkItem2(0x0, 1, lambda_E4AB)

    def lambda_E4BD():

        label("loc_E4BD")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_E4BD")

    QueueWorkItem2(0x1, 1, lambda_E4BD)

    def lambda_E4CF():

        label("loc_E4CF")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_E4CF")

    QueueWorkItem2(0x2, 1, lambda_E4CF)

    def lambda_E4E1():

        label("loc_E4E1")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_E4E1")

    QueueWorkItem2(0x3, 1, lambda_E4E1)

    def lambda_E4F3():

        label("loc_E4F3")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_E4F3")

    QueueWorkItem2(0xF, 1, lambda_E4F3)

    def lambda_E505():

        label("loc_E505")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_E505")

    QueueWorkItem2(0x1F, 1, lambda_E505)

    def lambda_E517():

        label("loc_E517")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_E517")

    QueueWorkItem2(0x1E, 1, lambda_E517)

    def lambda_E529():

        label("loc_E529")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_E529")

    QueueWorkItem2(0x20, 1, lambda_E529)

    def lambda_E53B():

        label("loc_E53B")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_E53B")

    QueueWorkItem2(0x1C, 1, lambda_E53B)
    Sleep(800)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7517", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x205), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(8710, 2000, -11680, 0)
    MoveCamera(136, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32390, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_0D()

    #C0666
    ChrTalk(
        0x101,
        "#11P#0005F#N哎，剑蛇帮的人？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0667
    ChrTalk(
        0x102,
        "#11P#0105F#N怎么回事……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x21, 0, 0, 52)
    BeginChrThread(0xD, 0, 0, 53)
    BeginChrThread(0xE, 0, 0, 54)
    BeginChrThread(0x11, 0, 0, 55)
    OP_68(3520, 2000, -6230, 4000)
    MoveCamera(152, 19, 0, 4000)

    #C0668
    ChrTalk(
        0xE,
        "#5P嘿，在干什么呢～？\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xD,
        (
            "#11P嘿，身为警察，\x01",
            "竟然敢在旧城区打架！\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x11,
        (
            "#5P不过，蓝衣服的小子们好像\x01",
            "被打败了啊，啊哈哈哈……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0671
    ChrTalk(
        0xF,
        "#12P你、你说什么……？\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x20,
        (
            "#6P唯、唯独不想被\x01",
            "你们这样说啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x1E,
        "#6P有什么不满的话……不如就在这里打一场吧。\x02",
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x21,
        (
            "#11P慢着。\x01",
            "在那之前，有一点需要纠正。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x21, 0)
    OP_68(1780, 700, -7220, 3500)
    MoveCamera(172, 22, 0, 3500)
    OP_95(0x21, 4910, -10, -7940, 2000, 0x0)
    OP_95(0x21, 2029, -10, -7760, 2000, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x1C, 0x1)
    OP_93(0xF, 0xE1, 0x1F4)

    #C0675
    ChrTalk(
        0x21,
        (
            "#5P这是什么意思啊，\x01",
            "不是你们叫我们\x01",
            "来决斗的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x21,
        (
            "#5P首领不参加，双方进行\x01",
            "四对四的决战……\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x21,
        (
            "#5P说得这么郑重其事，\x01",
            "结果却在和警察玩游戏？\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x1C,
        "#11P……你们应邀而来了啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x12C)
    Sleep(400)

    #C0679
    ChrTalk(
        0x1C,
        (
            "#11P那么，接下来，特别任务支援科\x01",
            "与剑蛇帮的训练比赛就要开始了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(200)

    def lambda_EA4B():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EA4B)

    def lambda_EA58():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_EA58)

    def lambda_EA65():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_EA65)

    def lambda_EA72():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_EA72)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_EB0F():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EB0F)

    def lambda_EB24():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_EB24)

    def lambda_EB39():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_EB39)
    Sleep(1500)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    OP_64(0x21)
    OP_64(0xD)
    OP_64(0xE)
    OP_64(0x11)
    Sleep(100)

    #C0680
    ChrTalk(
        0xD,
        "#5P哈……！？\x02",
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "#12P#0011F哎……等、等一下！？\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x21,
        "#5P这、这是什么意思啊！！\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x5A, 0x190)
    Sleep(400)

    #C0683
    ChrTalk(
        0x1C,
        (
            "#11P就是希望你们也借此机会，\x01",
            "学习一下防身术。\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x1C,
        (
            "#11P必须要提防黑手党暗算的人并不是只有我们，\x01",
            "你们也是一样的……\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x1C,
        (
            "#11P对你们来说，通过实战来进行训练，\x01",
            "应该也是最有效率的方法。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetMessageWindowPos(130, 115, -1, -1)
    SetChrName("众人")

    #A0686
    AnonymousTalk(
        0xFF,
        "#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(200)

    #C0687
    ChrTalk(
        0x11,
        (
            "#6P也就是说……让这些警察\x01",
            "对我们进行训练吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0xE,
        (
            "#5P哼，这个大块头说的话\x01",
            "永远都是这么难懂～！\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0xE,
        "#5P我们为什么非要让警察训练啊～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0xD, 500)
    TurnDirection(0x101, 0x21, 500)
    Sleep(300)

    #C0690
    ChrTalk(
        0x21,
        (
            "#12P哼……真是无聊透顶，\x01",
            "无能的警官又能\x01",
            "教给我们什么东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x21,
        "#12P训练？别开玩笑了。\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x2BC)

    #C0692
    ChrTalk(
        0x21,
        (
            "#4S#12P……总之，只要证明\x01",
            "我们剑蛇帮比警察更强\x01",
            "就可以了吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(5)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0693
    ChrTalk(
        0xD,
        (
            "#5P哈，那就来吧！\x01",
            "把这些警察打垮就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x11,
        (
            "#5P哼哼……\x01",
            "一定要把你们打得落花流水！！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x101, 400)
    BeginChrThread(0x21, 2, 0, 56)
    Sleep(10)
    BeginChrThread(0xD, 2, 0, 56)
    Sleep(8)
    BeginChrThread(0xE, 2, 0, 56)
    Sleep(12)
    BeginChrThread(0x11, 2, 0, 56)
    Fade(250)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_68(750, 700, -5890, 3000)
    OP_93(0x1C, 0x0, 0x1F4)

    def lambda_EF36():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_EF36)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_6F(0x1)

    #C0695
    ChrTalk(
        0x101,
        (
            "#12P#0011F请稍等一下，\x01",
            "这好像和说好的内容不太一样吧……\x02\x03",

            "#0006F我说……唉，真是的！\x01",
            "根本就没人在听我说话啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x104,
        (
            "#12P#0301F喂，罗伊德，好像要进行连续战斗啊。\x01",
            "……怎么办？\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x101,
        "#12P#0006F没、没办法啊……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0698
    ChrTalk(
        0x101,
        "#12P#0001F艾莉、缇欧，你们没问题吧？\x02",
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x102,
        "#12P#0101F嗯，我没问题。\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x103,
        (
            "#12P#0201F事态既然已经发展至此，\x01",
            "也只有全力以赴了。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x101,
        (
            "#12P#0001F嗯，再怎么说，\x01",
            "我们也绝对不能输……\x01",
            "全力迎战吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x1C,
        (
            "#11P那么，接下来就是\x01",
            "特别任务支援科对剑蛇帮……\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x1C,
        "#11P#4S──战斗开始！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x21, 0x2)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xE, 0x2)
    EndChrThread(0x11, 0x2)
    StopBGM(0x3E8)
    Battle("BattleInfo_8D0", 0x0, 0x0, 0x4, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_45_DE68 end

    def Function_46_F1DB(): pass

    label("Function_46_F1DB")

    OP_68(-360, 2000, -2190, 0)
    MoveCamera(154, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32390, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0x21, 3150, 0, -4000, 270)
    SetChrPos(0xD, 4080, 0, -4770, 270)
    SetChrPos(0xE, 4550, 0, -3310, 270)
    SetChrPos(0x11, 5260, 0, -4350, 270)
    SetChrPos(0xF, 4610, 0, -8510, 315)
    SetChrPos(0x1F, 5940, 0, -10170, 315)
    SetChrPos(0x20, 5790, 0, -8490, 315)
    SetChrPos(0x1E, 4910, 0, -10200, 315)
    SetChrChipByIndex(0x21, 0x2D)
    SetChrSubChip(0x21, 0x2)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x2)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0x11, 0x2C)
    SetChrSubChip(0x11, 0x3)
    OP_29(0x12, 0x1, 0x2)
    FadeToBright(1000, 0)
    OP_0D()

    #C0704
    ChrTalk(
        0x101,
        "#12P#0006F呼……还真是险象环生啊。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0705
    ChrTalk(
        0xD,
        "#5P可、可恶……！\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x21,
        "#5P混蛋……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0707
    ChrTalk(
        0x21,
        (
            "#5P岂有此理，四对四的战斗，我们竟然输了……？\x01",
            "开什么玩笑啊！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0708
    ChrTalk(
        0x21,
        (
            "#5P#4S这样一来，我们岂不是\x01",
            "和那些蓝衣服小子一样没用了吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0xE,
        "#5P哈，这怎么可能啊～！！\x02",
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0xE,
        (
            "#5P当然是我们比他们\x01",
            "强得多才对吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(15)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0711
    ChrTalk(
        0x102,
        (
            "#12P#0106F竟然在这种问题上\x01",
            "纠缠不休啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x104,
        "#12P#0300F真不愧是多年的宿敌呢……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(2040, 2000, -6710, 0)
    MoveCamera(98, 32, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32390, 0)
    OP_0D()

    #C0713
    ChrTalk(
        0xF,
        "#11P说、说起来……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x22)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x22)
    SetChrSubChip(0x20, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    #C0714
    ChrTalk(
        0xF,
        (
            "#11P我们圣书会的人\x01",
            "才没有可能比剑蛇帮\x01",
            "的家伙们差吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0xF,
        (
            "#11P多动动你们那低智商的脑子，\x01",
            "好好想清楚再说话啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x1F,
        (
            "#11P说、说的没错。\x01",
            "我们和你们才不是一个级别的！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F68F():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_F68F)
    Sleep(8)

    def lambda_F69F():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F69F)
    Sleep(2)

    def lambda_F6AF():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_F6AF)
    Sleep(5)

    def lambda_F6BF():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F6BF)
    Sleep(200)

    #C0717
    ChrTalk(
        0x11,
        "#6P可恶，说什么呢！！\x02",
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0xD,
        "#6P打死你们啊！这群混蛋！！\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x101,
        "#12P#0005F#N等一下，不能打架啊！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0720
    ChrTalk(
        0x103,
        "#12P#0206F#N全都是些一点就爆的人呢。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0721
    ChrTalk(
        0x1C,
        (
            "#12P嗯……\x01",
            "看起来，双方都还精力十足，\x01",
            "保存着不少余力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x1C,
        "#12P那么，接下来就进入最终战吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_F89C():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F89C)

    def lambda_F8A9():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_F8A9)

    def lambda_F8B6():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_F8B6)

    def lambda_F8C3():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_F8C3)

    def lambda_F8D0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_F8D0)

    def lambda_F8DD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_F8DD)

    def lambda_F8EA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_F8EA)

    def lambda_F8F7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_F8F7)

    def lambda_F904():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_F904)

    def lambda_F911():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F911)

    def lambda_F91E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_F91E)

    def lambda_F92B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F92B)
    Sleep(300)

    #C0723
    ChrTalk(
        0x101,
        "#12P#0011F#N哎……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0724
    ChrTalk(
        0x11,
        "#5P最终战……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x190)
    Sleep(200)

    #C0725
    ChrTalk(
        0x1C,
        "#12P规则很简单。\x02",
    )

    CloseMessageWindow()
    OP_68(660, 2000, -3670, 3000)
    MoveCamera(173, 31, 0, 3000)
    OP_6E(340, 3000)
    SetCameraDistance(33840, 3000)
    OP_6F(0x79)

    #C0726
    ChrTalk(
        0x1C,
        (
            "#11P一起攻击这些警用防身术的高手，\x01",
            "看哪边能先把他们解决……\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x1C,
        (
            "#11P用这种方式来分出优劣，\x01",
            "你们意下如何？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(10, 0, -1, -1)
    SetChrName("圣书会众成员")

    #A0728
    AnonymousTalk(
        0xFF,
        "#60W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(200)
    SetMessageWindowPos(20, 150, -1, -1)
    SetChrName("剑蛇帮众成员")

    #A0729
    AnonymousTalk(
        0xFF,
        "#60W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(100)

    #C0730
    ChrTalk(
        0x101,
        (
            "#12P#0011F你、你在说什么呢……\x01",
            "再怎么说，这样也太乱来了吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x13B, 0x190)
    Sleep(300)

    #C0731
    ChrTalk(
        0x1C,
        "#5P……是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x1C,
        (
            "#5P这种充满危机感的境况，\x01",
            "才能让你们拿出真本事，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FB73():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_FB73)

    def lambda_FB80():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FB80)

    def lambda_FB8D():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_FB8D)

    def lambda_FB9A():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_FB9A)
    Sleep(200)
    OP_82(0xC8, 0x0, 0xBB8, 0xC8)

    #C0733
    ChrTalk(
        0x21,
        "#6P#5S大家上啊！！\x02",
    )

    CloseMessageWindow()

    def lambda_FBD3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FBD3)

    def lambda_FBE0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_FBE0)

    def lambda_FBED():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_FBED)

    def lambda_FBFA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_FBFA)
    SetChrChipByIndex(0xF, 0x33)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x32)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x32)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x32)
    SetChrSubChip(0x20, 0x0)
    BeginChrThread(0xF, 1, 0, 48)
    BeginChrThread(0x1F, 1, 0, 47)
    BeginChrThread(0x1E, 1, 0, 47)
    BeginChrThread(0x20, 1, 0, 47)

    #C0734
    ChrTalk(
        0xF,
        "#5S#5P别被他们抢了先！\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0xE,
        "#6P#4S好啊！！\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x20,
        "#5P#4S上啊……！！\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(640, 2000, -2860, 2000)
    MoveCamera(171, 26, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(34010, 2000)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_6F(0x79)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x1F, 1)
    WaitChrThread(0x1E, 1)
    WaitChrThread(0x20, 1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0737
    ChrTalk(
        0x101,
        (
            "#12P#0003F不、不行。\x01",
            "已经无法阻止他们了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x104,
        "#12P#0301F好像也只能硬着头皮上了啊……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x190)
    Sleep(300)

    #C0739
    ChrTalk(
        0x1C,
        "#5P#4S──很好#500W，#20W最终战开始！！\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_914", 0x0, 0x0, 0x4, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_46_F1DB end

    def Function_47_FE0E(): pass

    label("Function_47_FE0E")

    OP_9B(0x0, 0xFE, 0x28, 0x7D0, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_47_FE0E end

    def Function_48_FE26(): pass

    label("Function_48_FE26")

    OP_9B(0x0, 0xFE, 0x28, 0x7D0, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_48_FE26 end

    def Function_49_FE3E(): pass

    label("Function_49_FE3E")

    OP_68(3950, 2000, -4170, 0)
    MoveCamera(127, 27, -1, 0)
    OP_6E(500, 0)
    SetCameraDistance(18720, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3020, 0, -5730, 270)
    SetChrPos(0x1F, 3960, 0, -7270, 270)
    SetChrPos(0x20, 4520, 0, -5070, 270)
    SetChrPos(0x1E, 5330, 0, -6480, 270)
    SetChrPos(0x21, 3310, 0, -2870, 270)
    SetChrPos(0xD, 3950, 0, -4170, 270)
    SetChrPos(0xE, 4270, 50, -1940, 270)
    SetChrPos(0x11, 5080, 0, -3400, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0xF, 0x2B)
    SetChrSubChip(0xF, 0x3)
    SetChrChipByIndex(0x1F, 0x2A)
    SetChrSubChip(0x1F, 0x3)
    SetChrChipByIndex(0x1E, 0x2A)
    SetChrSubChip(0x1E, 0x3)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrSubChip(0x20, 0x3)
    SetChrChipByIndex(0x21, 0x2D)
    SetChrSubChip(0x21, 0x2)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x2)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0x11, 0x2C)
    SetChrSubChip(0x11, 0x3)
    SetCameraDistance(23720, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(500)
    OP_68(-500, 2000, -2270, 0)
    MoveCamera(150, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(34010, 0)
    OP_0D()

    #C0740
    ChrTalk(
        0x101,
        "#12P#0006F呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x104,
        "#12P#0301F……结束了吗。\x02",
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x103,
        "#12P#0200F虽然总算是赢了，不过……\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x102,
        "#12P#0103F可真是狼狈不堪啊……\x02",
    )

    CloseMessageWindow()
    OP_A6(0xF, 0xC8, 0x0, 0x3, 0xBB8)

    #C0744
    ChrTalk(
        0xF,
        (
            "#5P竟、竟然能同时打败\x01",
            "我们两组人马……\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x21, 0xC8, 0x0, 0x3, 0xBB8)

    #C0745
    ChrTalk(
        0x21,
        (
            "#5P呜……\x01",
            "实在是无法接受……\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(200)
    SetChrSubChip(0x21, 0x1)
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(500)
    SetChrChipByIndex(0x21, 0x5)
    SetChrSubChip(0x21, 0x0)
    Sound(804, 0, 100, 0)
    OP_95(0x1C, 1780, 0, -3880, 1500, 0x0)
    TurnDirection(0x1C, 0x21, 500)
    TurnDirection(0x21, 0x1C, 500)
    Sleep(300)

    #C0746
    ChrTalk(
        0x1C,
        (
            "#11P现在已经明白了吧？\x01",
            "你们的战斗方式\x01",
            "只是一味依靠力量而已，太过天真……\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x1C,
        (
            "#11P其实根本就没有掌握\x01",
            "可以保护自己的格斗技。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x1C,
        (
            "#11P也就是说，目前的你们很不成熟，\x01",
            "还差得远呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)

    #C0749
    ChrTalk(
        0x21,
        "#5P呜……！？\x02",
    )

    CloseMessageWindow()
    Fade(200)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(250)
    Fade(200)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    OP_93(0xF, 0x13B, 0x0)
    Sleep(500)
    Fade(200)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    OP_93(0xE, 0xE1, 0x0)
    SetChrChipByIndex(0x1F, 0x2E)
    SetChrSubChip(0x1F, 0x0)
    OP_93(0x1F, 0x13B, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(250)
    Fade(200)
    SetChrChipByIndex(0x1E, 0x2E)
    SetChrSubChip(0x1E, 0x0)
    OP_93(0x1E, 0x13B, 0x0)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    OP_93(0x20, 0x13B, 0x0)
    Sleep(500)

    #C0750
    ChrTalk(
        0x11,
        (
            "#5P虽、虽然还是不太明白，\x01",
            "但好像突然被这家伙说教了……\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0xE,
        "#6P搞不懂他在说什么啊～……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0752
    ChrTalk(
        0x101,
        (
            "#12P#0004F不过，你们其实已经很强了。\x01",
            "以普通人的标准来说，算是无可挑剔的。\x02\x03",

            "#0000F如果有兴趣，\x01",
            "我们也可以教你们一些防身术……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x10E, 0x1F4)
    Sleep(300)

    #C0753
    ChrTalk(
        0x21,
        (
            "#5P……可恶，我们怎么可能\x01",
            "会接受警察的指导啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x5A, 0x190)
    Sleep(300)

    #C0754
    ChrTalk(
        0x21,
        "#5P兄弟们，撤退了！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 40, -1, -1)
    SetChrName("剑蛇帮众成员")

    #A0755
    AnonymousTalk(
        0xFF,
        "#4S噢、噢噢～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_1046A():

        label("loc_1046A")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_1046A")

    QueueWorkItem2(0x0, 1, lambda_1046A)

    def lambda_1047C():

        label("loc_1047C")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_1047C")

    QueueWorkItem2(0x1, 1, lambda_1047C)

    def lambda_1048E():

        label("loc_1048E")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_1048E")

    QueueWorkItem2(0x2, 1, lambda_1048E)

    def lambda_104A0():

        label("loc_104A0")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_104A0")

    QueueWorkItem2(0x3, 1, lambda_104A0)

    def lambda_104B2():

        label("loc_104B2")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_104B2")

    QueueWorkItem2(0xF, 1, lambda_104B2)

    def lambda_104C4():

        label("loc_104C4")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_104C4")

    QueueWorkItem2(0x1F, 1, lambda_104C4)

    def lambda_104D6():

        label("loc_104D6")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_104D6")

    QueueWorkItem2(0x1E, 1, lambda_104D6)

    def lambda_104E8():

        label("loc_104E8")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_104E8")

    QueueWorkItem2(0x20, 1, lambda_104E8)

    def lambda_104FA():

        label("loc_104FA")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_104FA")

    QueueWorkItem2(0x1C, 1, lambda_104FA)
    BeginChrThread(0x21, 1, 0, 57)
    Sleep(1200)
    BeginChrThread(0xD, 1, 0, 58)
    Sleep(800)
    BeginChrThread(0x11, 1, 0, 60)
    Sleep(400)
    BeginChrThread(0xE, 1, 0, 59)

    #C0756
    ChrTalk(
        0xE,
        (
            "#6P那个大块头的男人，总是说一些\x01",
            "让人听不懂的话啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0xD,
        "#4P嘁，谁有空管他说些什么！\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_49_FE3E end

    def Function_50_10582(): pass

    label("Function_50_10582")

    OP_68(810, 1500, -4230, 0)
    MoveCamera(150, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(34010, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3020, 0, -5730, 270)
    SetChrPos(0x1F, 3960, 0, -7270, 270)
    SetChrPos(0x20, 4520, 0, -5070, 270)
    SetChrPos(0x1E, 5330, 0, -6480, 270)
    SetChrPos(0x21, 3310, 0, -2870, 270)
    SetChrPos(0xD, 3950, 0, -4170, 270)
    SetChrPos(0xE, 4270, 50, -1940, 270)
    SetChrPos(0x11, 5080, 0, -3400, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x3)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x3)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x22)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x22)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0758
    ChrTalk(
        0x101,
        "#12P#0010F呼、呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x104,
        "#12P#0310F#N可恶……失败了吗。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0760
    ChrTalk(
        0x21,
        "#6P哈……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x2BC)

    #C0761
    ChrTalk(
        0xE,
        (
            "#6P#4S哇哈哈哈，睁大眼睛看好啊！\x01",
            "这些家伙被我们打到了～！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x21, 0x5)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x2E)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x2E)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_93(0xF, 0x0, 0x190)
    Sleep(400)

    #C0762
    ChrTalk(
        0xF,
        (
            "#11P等一下！\x01",
            "那还不是因为我的那一击发挥了效果！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10882():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_10882)
    Sleep(10)

    def lambda_10892():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_10892)
    Sleep(5)

    def lambda_108A2():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_108A2)
    Sleep(180)

    def lambda_108B2():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_108B2)
    Sleep(14)

    def lambda_108C2():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_108C2)
    Sleep(8)

    def lambda_108D2():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_108D2)
    Sleep(12)

    def lambda_108E2():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_108E2)

    #C0763
    ChrTalk(
        0x1F,
        (
            "#11P对、对啊。\x01",
            "我们也有帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x1F,
        (
            "#11P能打赢这一仗，才不是因为\x01",
            "你们的实力强呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x11,
        (
            "#6P你说什么！？\x01",
            "虽、虽然……\x01",
            "你们确实是帮了点小忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x1C,
        "#11P──这样的战果，并不能算是胜利。\x02",
    )

    CloseMessageWindow()

    def lambda_109AC():

        label("loc_109AC")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_109AC")

    QueueWorkItem2(0x101, 1, lambda_109AC)

    def lambda_109BE():

        label("loc_109BE")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_109BE")

    QueueWorkItem2(0xF, 1, lambda_109BE)

    def lambda_109D0():

        label("loc_109D0")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_109D0")

    QueueWorkItem2(0x1F, 1, lambda_109D0)

    def lambda_109E2():

        label("loc_109E2")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_109E2")

    QueueWorkItem2(0x1E, 1, lambda_109E2)

    def lambda_109F4():

        label("loc_109F4")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_109F4")

    QueueWorkItem2(0x20, 1, lambda_109F4)

    def lambda_10A06():

        label("loc_10A06")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_10A06")

    QueueWorkItem2(0x21, 1, lambda_10A06)

    def lambda_10A18():

        label("loc_10A18")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_10A18")

    QueueWorkItem2(0xD, 1, lambda_10A18)

    def lambda_10A2A():

        label("loc_10A2A")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_10A2A")

    QueueWorkItem2(0xE, 1, lambda_10A2A)

    def lambda_10A3C():

        label("loc_10A3C")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_10A3C")

    QueueWorkItem2(0x11, 1, lambda_10A3C)
    OP_95(0x1C, 1780, 0, -3880, 1500, 0x0)
    TurnDirection(0x1C, 0x21, 500)
    TurnDirection(0x21, 0x1C, 500)
    Sleep(300)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x11, 0x1)

    #C0767
    ChrTalk(
        0x1C,
        (
            "#11P不要忘了，特别任务支援科\x01",
            "毕竟都已经连续战斗了三场……\x01",
            "一直连续战斗到现在，还能有如此表现，已经很出色了。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x1C,
        "#11P想想看，如果换成你们的话，能做得到吗？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 40, -1, -1)
    SetChrName("剑蛇帮众成员")

    #A0769
    AnonymousTalk(
        0xFF,
        "#30W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(200)

    #C0770
    ChrTalk(
        0x1C,
        (
            "#11P明白了吧？\x01",
            "你们的战斗方式\x01",
            "只是一味依靠力量而已，太过天真……\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x1C,
        (
            "#11P其实根本就没有掌握\x01",
            "可以保护自己的格斗技。\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x1C,
        (
            "#11P也就是说，目前的你们很不成熟，\x01",
            "还差得远呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)

    #C0773
    ChrTalk(
        0x21,
        "#5P呜……！？\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x11,
        (
            "#5P虽、虽然还是不太明白，\x01",
            "但好像突然被这家伙说教了……\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0xE,
        "#6P搞不懂他在说什么啊～……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0776
    ChrTalk(
        0x101,
        (
            "#12P#0004F不过，你们其实已经很强了。\x01",
            "以普通人的标准来说，算是无可挑剔的。\x02\x03",

            "#12P#0000F虽然我们最后输掉了，\x01",
            "不过，如果有兴趣，\x01",
            "我们也可以教你们一些防身术哦……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x10E, 0x1F4)
    Sleep(300)

    #C0777
    ChrTalk(
        0x21,
        (
            "#5P……可恶，我们怎么可能\x01",
            "会接受警察的指导啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x5A, 0x190)
    Sleep(300)

    #C0778
    ChrTalk(
        0x21,
        "#5P兄弟们，撤退了！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 40, -1, -1)
    SetChrName("剑蛇帮众成员")

    #A0779
    AnonymousTalk(
        0xFF,
        "#4S 噢噢～！ \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_10E20():

        label("loc_10E20")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_10E20")

    QueueWorkItem2(0x0, 1, lambda_10E20)

    def lambda_10E32():

        label("loc_10E32")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_10E32")

    QueueWorkItem2(0x1, 1, lambda_10E32)

    def lambda_10E44():

        label("loc_10E44")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_10E44")

    QueueWorkItem2(0x2, 1, lambda_10E44)

    def lambda_10E56():

        label("loc_10E56")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_10E56")

    QueueWorkItem2(0x3, 1, lambda_10E56)

    def lambda_10E68():

        label("loc_10E68")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_10E68")

    QueueWorkItem2(0xF, 1, lambda_10E68)

    def lambda_10E7A():

        label("loc_10E7A")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_10E7A")

    QueueWorkItem2(0x1F, 1, lambda_10E7A)

    def lambda_10E8C():

        label("loc_10E8C")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_10E8C")

    QueueWorkItem2(0x1E, 1, lambda_10E8C)

    def lambda_10E9E():

        label("loc_10E9E")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_10E9E")

    QueueWorkItem2(0x20, 1, lambda_10E9E)

    def lambda_10EB0():

        label("loc_10EB0")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_10EB0")

    QueueWorkItem2(0x1C, 1, lambda_10EB0)
    BeginChrThread(0x21, 1, 0, 57)
    Sleep(1200)
    BeginChrThread(0xD, 1, 0, 58)
    Sleep(800)
    BeginChrThread(0x11, 1, 0, 60)
    Sleep(400)
    BeginChrThread(0xE, 1, 0, 59)

    #C0780
    ChrTalk(
        0xE,
        (
            "#6P那个大块头的男人，总是说一些\x01",
            "让人听不懂的话啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0xD,
        "#12P嘁，谁有空管他说些什么！\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_50_10582 end

    def Function_51_10F39(): pass

    label("Function_51_10F39")

    Sleep(2500)
    WaitChrThread(0xE, 1)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x11, 0x80)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x1C, 0x1)

    #C0782
    ChrTalk(
        0xF,
        (
            "#11P哼……一点都没变，\x01",
            "还是一群无脑蠢货啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x1F,
        (
            "#12P让、让那些家伙学防身术？\x01",
            "就算花上一辈子大概都不够。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x20,
        "#5P是啊，我也这么想。\x02",
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x1E,
        "#6P不过，真是得到了很宝贵的经验啊。\x02",
    )

    CloseMessageWindow()

    def lambda_1102F():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1102F)

    def lambda_1103C():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1103C)
    Sleep(20)

    def lambda_1104C():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1104C)
    Sleep(10)

    def lambda_1105C():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1105C)
    Sleep(100)

    def lambda_1106C():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1106C)
    Sleep(20)

    def lambda_1107C():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1107C)

    def lambda_11089():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_11089)
    Sleep(18)

    def lambda_11099():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_11099)

    def lambda_110A6():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_110A6)
    Sleep(300)

    #C0786
    ChrTalk(
        0x101,
        (
            "#12P#0003F算了，就算他们一时想不通，\x01",
            "只要能让你们有所收获，\x01",
            "我们的努力也就没有白费啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x102,
        "#12P#0103F是啊，虽然大家都打得很累。\x02",
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x1C,
        (
            "#5P那么，我们也\x01",
            "就此告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x1C,
        (
            "#5P……特别任务支援科的各位，如果你们需要休息，\x01",
            "稍后也可以来我们酒吧里坐坐。\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x1C,
        (
            "#5P呵……对你们来说，这也算是\x01",
            "一次不错的训练吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x87, 0x190)
    Sleep(400)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0791
    ChrTalk(
        0x104,
        "#12P#0305F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x101,
        "#12P#0005F……………………？\x02",
    )

    CloseMessageWindow()

    def lambda_11277():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_11277)
    Sleep(10)

    def lambda_11287():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_11287)

    def lambda_11294():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_11294)
    Sleep(12)

    def lambda_112A4():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_112A4)
    Sleep(400)

    #C0793
    ChrTalk(
        0x1C,
        "#5P#4S──战斗结束，撤退！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("圣书会众成员")

    #A0794
    AnonymousTalk(
        0xFF,
        "#5S收到！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_11306():

        label("loc_11306")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_11306")

    QueueWorkItem2(0x0, 1, lambda_11306)

    def lambda_11318():

        label("loc_11318")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_11318")

    QueueWorkItem2(0x1, 1, lambda_11318)

    def lambda_1132A():

        label("loc_1132A")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_1132A")

    QueueWorkItem2(0x2, 1, lambda_1132A)

    def lambda_1133C():

        label("loc_1133C")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_1133C")

    QueueWorkItem2(0x3, 1, lambda_1133C)
    OP_68(-4030, 2000, -6480, 5500)
    MoveCamera(228, 29, -1, 5500)
    OP_6E(500, 5500)
    SetCameraDistance(21190, 5500)
    BeginChrThread(0x1C, 1, 0, 61)
    Sleep(1100)
    BeginChrThread(0xF, 1, 0, 61)
    Sleep(700)
    BeginChrThread(0x1F, 1, 0, 61)
    Sleep(400)
    BeginChrThread(0x20, 1, 0, 61)
    Sleep(700)
    BeginChrThread(0x1E, 1, 0, 61)
    Sleep(3800)
    StopBGM(0x1388)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(3000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    Fade(800)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x20, 0x80)
    OP_68(-1140, 2000, -2670, 0)
    MoveCamera(228, 29, -1, 0)
    OP_6E(520, 0)
    SetCameraDistance(16580, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7101", 0)

    #C0795
    ChrTalk(
        0x101,
        (
            "#6P#0005F那个叫阿巴斯的家伙……\x01",
            "从一开始就是这么打算的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x102,
        (
            "#5P#0106F结果把两个组织的成员\x01",
            "都拉来做了一次训练。\x02\x03",

            "#0100F确实，他好像从一开始\x01",
            "就有这样的预谋呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x104,
        (
            "#11P#0306F到头来，我们完全被他算计了啊。\x01",
            "……真是个大意不得的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x103,
        (
            "#12P#0206F是啊……身体相当疲劳呢。\x02\x03",

            "#0200F不过，多亏他的说教，\x01",
            "不良团伙成员们应该\x01",
            "会变得安分不少吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x101,
        (
            "#6P#0000F也是，无论如何，\x01",
            "我们都达到了最初的目的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_115B1():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_115B1)

    def lambda_115BE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_115BE)

    def lambda_115CB():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_115CB)

    def lambda_115D8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_115D8)
    Sleep(400)

    #C0800
    ChrTalk(
        0x101,
        (
            "#6P#0000F好，那我们差不多\x01",
            "也该回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x102,
        "#5P#0100F嗯，我们走吧。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_51_10F39 end

    def Function_52_1162D(): pass

    label("Function_52_1162D")

    OP_95(0x21, 5880, -10, -9390, 2000, 0x0)
    Return()

    # Function_52_1162D end

    def Function_53_11642(): pass

    label("Function_53_11642")

    OP_95(0xD, 6450, 0, -11270, 2000, 0x0)
    Return()

    # Function_53_11642 end

    def Function_54_11657(): pass

    label("Function_54_11657")

    OP_95(0xE, 7550, 0, -9860, 2000, 0x0)
    Return()

    # Function_54_11657 end

    def Function_55_1166C(): pass

    label("Function_55_1166C")

    OP_95(0x11, 7860, 0, -11350, 2000, 0x0)
    Return()

    # Function_55_1166C end

    def Function_56_11681(): pass

    label("Function_56_11681")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_116A6")
    OP_63(0xFE, 0xC8, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_56_11681")

    label("loc_116A6")

    Return()

    # Function_56_11681 end

    def Function_57_116A7(): pass

    label("Function_57_116A7")

    OP_95(0xFE, 4400, 0, -3520, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_57_116A7 end

    def Function_58_116F8(): pass

    label("Function_58_116F8")

    OP_95(0xFE, 5830, 0, -5010, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_58_116F8 end

    def Function_59_11749(): pass

    label("Function_59_11749")

    OP_95(0xFE, 5830, 0, -5010, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_59_11749 end

    def Function_60_1179A(): pass

    label("Function_60_1179A")

    OP_95(0xFE, 5830, 0, -5010, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_60_1179A end

    def Function_61_117EB(): pass

    label("Function_61_117EB")

    OP_95(0xFE, 390, 0, -7500, 2000, 0x0)
    OP_95(0xFE, -5110, 0, -8500, 2000, 0x0)
    OP_95(0xFE, -10460, 0, -11450, 2000, 0x0)
    OP_95(0xFE, -15990, 0, -11600, 2000, 0x0)
    Return()

    # Function_61_117EB end

    SaveToFile()

Try(main)
