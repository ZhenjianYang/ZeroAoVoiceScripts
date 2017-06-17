from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0300.bin",                # FileName
        "c0300",                    # MapName
        "c0300",                    # Location
        0x002A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c0300", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 42, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0300",                  # 0
        "雷兹老人",               # 1
        "本特斯",                 # 2
        "尤利",                   # 3
        "塞克斯",                 # 4
        "瑞吉",                   # 5
        "公司职员",               # 6
        "雷克特书记官",           # 7
        "哈罗德",                 # 8
        "菲利克",                 # 9
        "莉丝",                   # 10
        "车",                     # 11
        "飙车族",                 # 12
        "女招待（Ａ）",           # 13
        "女招待（Ｂ）",           # 14
        "玛丽",                   # 15
        "SE控制",                 # 16
        "bc0300",                 # 17
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

    ATBonus("ATBonus_7F4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_78D5", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_844", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_848", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_84C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_850", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_854", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_858", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_85C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_860", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_8A8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_8AC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_8B0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_8B4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_8B8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_8BC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_824", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_828", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_82C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_830", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_834", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_838", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_83C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_840", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_8C4", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0300", "Sepith_78D5", 60, 30, 10, 0,
        (
            ("ms85100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_844", "MonsterBattlePostion_8A4", "ed7450", "ed7453", "ATBonus_7F4"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_824", "MonsterBattlePostion_8A4", "ed7450", "ed7453", "ATBonus_7F4"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_844", "MonsterBattlePostion_8A4", "ed7450", "ed7453", "ATBonus_7F4"),
            (),
        )
    )

    AddCharChip((
        "chr/ch21602.itc",                   # 00
        "chr/ch33000.itc",                   # 01
        "chr/ch44100.itc",                   # 02
        "chr/ch47500.itc",                   # 03
        "chr/ch23600.itc",                   # 04
        "chr/ch49300.itc",                   # 05
        "chr/ch12400.itc",                   # 06
        "chr/ch09300.itc",                   # 07
        "chr/ch22000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
    ))

    DeclNpc(-12850,  -5900,   -31489,  315,  261,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(32279,   0,       -4369,   270,  257,  0x0, 0,   1,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(5699,    200,     4900,    180,  389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(5699,    0,       469,     360,  389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(7900,    200,     2450,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(239,     -750,    -48720,  0,    385,  0x0, 0,   5,   0,   0,   2,   0,   11,  255,  0)
    DeclNpc(-5449,   -6000,   -36279,  270,  385,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(9789,    0,       -11640,  45,   389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-1389,   0,       -30329,  135,  389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-360,    -5920,   0,       0x10100B4,    "BattleInfo_8C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-11280,  -26290,  -6000,   0x10100B4,    "BattleInfo_8C4", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 30,  -7.0,                  -19.739999771118164,   -5.5,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.6999999284744263,    9.869999885559082,     1.0999999046325684,    1.0])
    DeclEvent(0x0000, 0, 40,  -7.0,                  -8.34000015258789,     -1.0,                  100.0,                 [0.09998477250337601,  0.008726206608116627,  -0.0,                  0.0,                   -0.0017452412284910679, 0.49992382526397705,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.6853380799293518,    4.230448246002197,     0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 38,  -7.5,                  -7.0,                  -0.0,                  100.0,                 [0.09993909299373627,  0.0174497552216053,    -0.0,                  0.0,                   -0.0034899513702839613, 0.49969542026519775,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.7251135110855103,    3.6287410259246826,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 41,  2.359999895095825,     -5.079999923706055,    -0.0,                  64.0,                  [0.4993147850036621,   0.006541998125612736,  -0.0,                  0.0,                   -0.026167992502450943, 0.12482869625091553,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.3113162517547607,   0.6186906695365906,    -0.0,                  1.0])

    DeclActor(-5470,   -6000,   -41550,  1200,    -9970,   -6500,   -41930,  0x007C, 0,  19, 0x0000)
    DeclActor(-12580,  0,       -5700,   1500,    -12580,  2000,    -5700,   0x007C, 0,  27, 0x0000)
    DeclActor(-18500,  -5600,   -16600,  2000,    -18500,  -4400,   -16600,  0x007C, 0,  28, 0x0000)
    DeclActor(17650,   0,       -800,    2000,    17650,   1500,    -800,    0x007C, 0,  17, 0x0000)
    DeclActor(0,       0,       -770,    2000,    0,       1500,    -770,    0x007C, 0,  16, 0x0000)
    DeclActor(-35330,  -4950,   -41950,  1200,    -35330,  -3950,   -41950,  0x007C, 0,  5,  0x0000)
    DeclActor(-18500,  -5600,   -16600,  2000,    -18500,  -4400,   -16600,  0x007C, 0,  18, 0x0000)
    DeclActor(-2700,   -6500,   -38000,  2000,    -2700,   -5500,   -38000,  0x007C, 0,  42, 0x0000)

    PlaceName(167.6699981689453, 0.0, -124.73999786376953, 0x0000, 0x0000, "中央广场")
    PlaceName(61.15999984741211, 0.0, -117.44999694824219, 0x0000, 0x0000, "西街")
    PlaceName(211.41000366210938, 0.0, 19.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-37.66999816894531, 0.0, 3.240000009536743, 0x0000, 0x0000, "住宅街")
    PlaceName(80.5999984741211, 0.0, -9.720000267028809, 0x0000, 0x0000, "欢乐街")
    PlaceName(299.29998779296875, 0.0, -162.0, 0x0000, 0x0000, "东街")
    PlaceName(356.80999755859375, 0.0, -251.10000610351562, 0x0000, 0x0000, "旧城区")
    PlaceName(344.6600036621094, 0.0, -55.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(302.5400085449219, 0.0, 97.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(185.89999389648438, 0.0, -236.52000427246094, 0x0000, 0x0000, "站前街道")
    PlaceName(109.76000213623047, 0.0, -68.04000091552734, 0x0000, 0x0000, "后巷")
    PlaceName(181.0399932861328, 0.0, -286.739990234375, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(386.7799987792969, 0.0, -139.32000732421875, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-21.469999313354492, 0.0, -119.87999725341797, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-11.75, 0.0, 42.119998931884766, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(200.0, 0.0, 231.5, 0x0000, 0x0000, "兰花塔")
    PlaceName(132.02999877929688, 0.0, -147.4199981689453, 0x0000, 0x0051, "")
    PlaceName(219.11000061035156, 0.0, -105.30000305175781, 0x0000, 0x0054, "")
    PlaceName(171.72000122070312, 0.0, -160.3800048828125, 0x0000, 0x0057, "")
    PlaceName(130.82000732421875, 0.0, -100.44000244140625, 0x0000, 0x0053, "")
    PlaceName(164.02999877929688, 0.0, -61.560001373291016, 0x0000, 0x0053, "")
    PlaceName(81.80999755859375, 0.0, -108.54000091552734, 0x0000, 0x0053, "")
    PlaceName(66.0199966430664, 0.0, -74.5199966430664, 0x0000, 0x0053, "")
    PlaceName(104.9000015258789, 0.0, -22.68000030517578, 0x0000, 0x0052, "")
    PlaceName(112.58999633789062, 0.0, -43.7400016784668, 0x0000, 0x0053, "")
    PlaceName(126.7699966430664, 0.0, -57.5099983215332, 0x0000, 0x0053, "")
    PlaceName(172.94000244140625, 0.0, 57.5099983215332, 0x0000, 0x0051, "")
    PlaceName(354.3800048828125, 0.0, -162.0, 0x0000, 0x0052, "")
    PlaceName(326.8399963378906, 0.0, -308.6099853515625, 0x0000, 0x0053, "")
    PlaceName(305.7799987792969, 0.0, -278.6400146484375, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_A24",          # 00, 0
        "Function_1_AD4",          # 01, 1
        "Function_2_B35",          # 02, 2
        "Function_3_B96",          # 03, 3
        "Function_4_F91",          # 04, 4
        "Function_5_16DB",         # 05, 5
        "Function_6_1816",         # 06, 6
        "Function_7_228E",         # 07, 7
        "Function_8_2F1F",         # 08, 8
        "Function_9_3011",         # 09, 9
        "Function_10_3080",        # 0A, 10
        "Function_11_31A1",        # 0B, 11
        "Function_12_3265",        # 0C, 12
        "Function_13_3643",        # 0D, 13
        "Function_14_3749",        # 0E, 14
        "Function_15_3F31",        # 0F, 15
        "Function_16_41BE",        # 10, 16
        "Function_17_4579",        # 11, 17
        "Function_18_45CE",        # 12, 18
        "Function_19_45F3",        # 13, 19
        "Function_20_46BB",        # 14, 20
        "Function_21_4847",        # 15, 21
        "Function_22_4890",        # 16, 22
        "Function_23_48BC",        # 17, 23
        "Function_24_48D2",        # 18, 24
        "Function_25_57EE",        # 19, 25
        "Function_26_585F",        # 1A, 26
        "Function_27_5875",        # 1B, 27
        "Function_28_5AE3",        # 1C, 28
        "Function_29_5E09",        # 1D, 29
        "Function_30_62CA",        # 1E, 30
        "Function_31_683A",        # 1F, 31
        "Function_32_6C0A",        # 20, 32
        "Function_33_6C55",        # 21, 33
        "Function_34_6CA0",        # 22, 34
        "Function_35_6CEB",        # 23, 35
        "Function_36_6D36",        # 24, 36
        "Function_37_6D81",        # 25, 37
        "Function_38_6DB8",        # 26, 38
        "Function_39_725B",        # 27, 39
        "Function_40_7774",        # 28, 40
        "Function_41_781D",        # 29, 41
        "Function_42_7886",        # 2A, 42
    ))


    def Function_0_A24(): pass

    label("Function_0_A24")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_A5C"),
        (1, "loc_A68"),
        (2, "loc_A74"),
        (3, "loc_A80"),
        (4, "loc_A8C"),
        (5, "loc_A98"),
        (6, "loc_AA4"),
        (SWITCH_DEFAULT, "loc_AB0"),
    )


    label("loc_A5C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_A68")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_A74")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_A80")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_A8C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_A98")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_AA4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_AB0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_ABC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AD3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_AD3")

    Return()

    # Function_0_A24 end

    def Function_1_AD4(): pass

    label("Function_1_AD4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B34")
    OP_95(0xFE, 2630, 0, -4370, 1000, 0x0)
    OP_95(0xFE, 240, 0, -7350, 1000, 0x0)
    OP_95(0xFE, 240, -750, -48720, 1000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 35280, 0, -4370, 45)
    Jump("Function_1_AD4")

    label("loc_B34")

    Return()

    # Function_1_AD4 end

    def Function_2_B35(): pass

    label("Function_2_B35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B95")
    OP_95(0xFE, 240, 0, -7350, 2000, 0x0)
    OP_95(0xFE, 2630, 0, -4370, 2000, 0x0)
    OP_95(0xFE, 35280, 0, -4370, 2000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 240, -750, -48720, 0)
    Jump("Function_2_B35")

    label("loc_B95")

    Return()

    # Function_2_B35 end

    def Function_3_B96(): pass

    label("Function_3_B96")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D27")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C58")
    SetChrPos(0x0, 230, -750, -38720, 0)
    SetChrPos(0x1, 230, -750, -38720, 0)
    SetChrPos(0x2, 230, -750, -38720, 0)
    SetChrPos(0x3, 230, -750, -38720, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2B")
    SetChrPos(0x4, 230, -750, -38720, 0)
    SetChrPos(0x5, 230, -750, -38720, 0)
    Jump("loc_C4A")

    label("loc_C2B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C4A")
    SetChrPos(0x4, 230, -750, -38720, 0)

    label("loc_C4A")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D27")

    label("loc_C58")

    SetChrPos(0x0, 24330, 0, -4050, 270)
    SetChrPos(0x1, 24330, 0, -4050, 270)
    SetChrPos(0x2, 24330, 0, -4050, 270)
    SetChrPos(0x3, 24330, 0, -4050, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD1")
    SetChrPos(0x4, 24330, 0, -4050, 270)
    SetChrPos(0x5, 24330, 0, -4050, 270)
    Jump("loc_CF0")

    label("loc_CD1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF0")
    SetChrPos(0x4, 24330, 0, -4050, 270)

    label("loc_CF0")

    OP_68(24330, 2000, -4050, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D27")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D44")
    OP_C9(0x0, 0x1000)

    label("loc_D44")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D68")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_EF7")

    label("loc_D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D80")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_EF7")

    label("loc_D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D93")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_EF7")

    label("loc_D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DA1")
    Jump("loc_EF7")

    label("loc_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DAF")
    Jump("loc_EF7")

    label("loc_DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DCC")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_EF7")

    label("loc_DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DDF")
    SetChrFlags(0x8, 0x10)
    Jump("loc_EF7")

    label("loc_DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E43")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, -7580, 0, -5670, 225)
    SetChrPos(0xB, -9090, 0, -5710, 135)
    SetChrPos(0xC, -8560, 0, -7100, 0)
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3E")
    SetChrFlags(0xC, 0x10)

    label("loc_E3E")

    Jump("loc_EF7")

    label("loc_E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E51")
    Jump("loc_EF7")

    label("loc_E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E5F")
    Jump("loc_EF7")

    label("loc_E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_E84")
    SetChrPos(0x9, 13450, 0, -4760, 45)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_EF7")

    label("loc_E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBE")
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBE")
    SetChrFlags(0xE, 0x80)

    label("loc_EBE")

    Jump("loc_EF7")

    label("loc_EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_ED1")
    Jump("loc_EF7")

    label("loc_ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_EEE")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_EF7")

    label("loc_EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_EF7")

    label("loc_EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F0B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 20)
    Jump("loc_F65")

    label("loc_F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F1F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 29)
    Jump("loc_F65")

    label("loc_F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_F33")
    ClearScenarioFlags(0x22, 2)
    Event(0, 31)
    Jump("loc_F65")

    label("loc_F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F65")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F65")
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F90")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_F90")

    Return()

    # Function_3_B96 end

    def Function_4_F91(): pass

    label("Function_4_F91")

    ClearScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_104C")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x64, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_104C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EC")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x64, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_113F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x20, 0x91, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_113F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1157")
    ClearMapFlags(0x2000)
    Jump("loc_115E")

    label("loc_1157")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_115E")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -9970, -6500, -41930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('初级竿', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小巧射手', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('竹竿', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢竿侵略者', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('水中支配者', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11ED")
    OP_65(0x0, 0x1)

    label("loc_11ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1206")
    OP_10(0x1, 0x0)
    OP_10(0xC, 0x1)
    Jump("loc_120C")

    label("loc_1206")

    OP_10(0x1, 0x1)
    OP_10(0xC, 0x0)

    label("loc_120C")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0x0, 0x0)
    OP_70(0x1, 0xA)
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0x0)
    OP_70(0x6, 0xA)
    OP_70(0xC, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1267")
    ClearMapObjFlags(0x2, 0x10)
    Jump("loc_126B")

    label("loc_1267")

    OP_65(0x7, 0x1)

    label("loc_126B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1288")
    ClearMapObjFlags(0xB, 0x10)
    OP_70(0xB, 0x0)

    label("loc_1288")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A3")
    OP_66(0x6, 0x1)

    label("loc_12A3")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E9")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_END)), "loc_12E9")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    SetScenarioFlags(0x0, 7)

    label("loc_12E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12FB")
    OP_66(0x2, 0x1)

    label("loc_12FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1318")
    OP_70(0x5, 0x10)
    OP_65(0x3, 0x1)

    label("loc_1318")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1360")
    ModifyEventFlags(1, 0, 0x80)
    Jump("loc_13A6")

    label("loc_1360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1378")
    ModifyEventFlags(1, 1, 0x80)
    Jump("loc_13A6")

    label("loc_1378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1390")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_13A6")

    label("loc_1390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A6")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_13A6")

    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155B")
    OP_70(0xF, 0x0)
    Jump("loc_155F")

    label("loc_155B")

    OP_70(0xF, 0x1E)

    label("loc_155F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_156B")
    ClearScenarioFlags(0x1, 0)

    label("loc_156B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157C")
    ClearScenarioFlags(0x1, 0)

    label("loc_157C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_158D")
    ClearScenarioFlags(0x1, 0)

    label("loc_158D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159E")
    ClearScenarioFlags(0x1, 0)

    label("loc_159E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15C5")
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)

    label("loc_15C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15D3")
    Jump("loc_16DA")

    label("loc_15D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_15E7")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_15E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_15F5")
    Jump("loc_16DA")

    label("loc_15F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1609")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_1609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1617")
    Jump("loc_16DA")

    label("loc_1617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_162B")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_162B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1653")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_164E")
    SetMapObjFlags(0xE, 0x4)

    label("loc_164E")

    Jump("loc_16DA")

    label("loc_1653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1673")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_166E")
    SetMapObjFlags(0xE, 0x4)

    label("loc_166E")

    Jump("loc_16DA")

    label("loc_1673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1687")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_1687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_169B")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_169B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16AF")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_16AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_16C3")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_16C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_16D1")
    Jump("loc_16DA")

    label("loc_16D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_16DA")

    label("loc_16DA")

    Return()

    # Function_4_F91 end

    def Function_5_16DB(): pass

    label("Function_5_16DB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CD")
    Sound(14, 0, 100, 0)
    OP_74(0xF, 0x1E)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('弹性大衣', 1)"), scpexpr(EXPR_END)), "loc_175E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '弹性大衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_17C8")

    label("loc_175E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '弹性大衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '弹性大衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17C8")

    Jump("loc_180A")

    label("loc_17CD")

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

    label("loc_180A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16DB end

    def Function_6_1816(): pass

    label("Function_6_1816")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1973")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18ED")

    #C0004
    ChrTalk(
        0xFE,
        (
            "那所房子中原本住着\x01",
            "三个自称『高贵之血』\x01",
            "组合的青年……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "在得知结界消失的消息之后，\x01",
            "他们好像立刻就\x01",
            "踏上返乡之路了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "但他们现在已经没有车了，\x01",
            "到底打算怎么返回共和国呢……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_196E")

    label("loc_18ED")


    #C0007
    ChrTalk(
        0xFE,
        (
            "之前住在那所房子中的三个年轻人\x01",
            "已经慌慌张张地\x01",
            "踏上返乡之路了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "但他们现在已经没有车了，\x01",
            "到底打算怎么返回共和国呢……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196E")

    Jump("loc_228A")

    label("loc_1973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1981")
    Jump("loc_228A")

    label("loc_1981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7E")

    #C0009
    ChrTalk(
        0xFE,
        (
            "听了迪塔的演说之后，\x01",
            "我又回想起了四、五年前\x01",
            "发生的那起导力车爆炸事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "当时也是作为事故来报道的，\x01",
            "但如果那是由于帝国与共和国之间的\x01",
            "『暗斗』所引起的，就实在是……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "看来克洛斯贝尔潜藏着\x01",
            "相当惊人的黑暗面呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AFE")

    label("loc_1A7E")


    #C0012
    ChrTalk(
        0xFE,
        (
            "发生在四、五年前的那起爆炸事故……\x01",
            "我记得当时的受害者\x01",
            "是个小女孩……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "看来克洛斯贝尔潜藏着\x01",
            "相当惊人的黑暗面呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AFE")

    Jump("loc_228A")

    label("loc_1B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B71")

    #C0014
    ChrTalk(
        0xFE,
        (
            "之前的那起袭击事件\x01",
            "实在是太过分了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "自那之后，一到了晚上我就害怕，\x01",
            "都不能安心入睡了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228A")

    label("loc_1B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1BCE")

    #C0016
    ChrTalk(
        0xFE,
        (
            "哎呀，竟然发生了占领事件，\x01",
            "世道真是不太平啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "究竟是什么人干的呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_228A")

    label("loc_1BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BDC")
    Jump("loc_228A")

    label("loc_1BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C44")

    #C0018
    ChrTalk(
        0xFE,
        "……ＺＺＺ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0019
    ChrTalk(
        0xFE,
        (
            "嗯……？\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_1C7F")

    label("loc_1C44")


    #C0020
    ChrTalk(
        0xFE,
        (
            "呼，我刚才已经\x01",
            "彻底睡熟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "……发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1C7F")

    Jump("loc_228A")

    label("loc_1C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CD5")

    #C0022
    ChrTalk(
        0xFE,
        (
            "呼啊啊啊……\x01",
            "感觉睡意好强烈……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "再这样下去就要睡着了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_228A")

    label("loc_1CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7D")

    #C0024
    ChrTalk(
        0xFE,
        (
            "居民投票日\x01",
            "已经渐渐临近了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "为了众多年轻人的未来，\x01",
            "我绝不能抱着轻松的心情来观望。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "在投票日到来之前，\x01",
            "一定要整理好自己的想法。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DEC")

    label("loc_1D7D")


    #C0027
    ChrTalk(
        0xFE,
        (
            "为了众多年轻人的未来，\x01",
            "我必须要认真思考\x01",
            "独立的各种利弊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "在投票日到来之前，\x01",
            "一定要整理好自己的想法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DEC")

    Jump("loc_228A")

    label("loc_1DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1ED6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E83")

    #C0029
    ChrTalk(
        0xFE,
        (
            "刚才有辆导力车\x01",
            "开往大圣堂方向了。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "我记得那种高级轿车\x01",
            "好像是接送\x01",
            "各国首脑的……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "嗯……也许是我看错了吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ED1")

    label("loc_1E83")


    #C0032
    ChrTalk(
        0xFE,
        (
            "之前好像有辆\x01",
            "高级轿车\x01",
            "开往大圣堂方向了……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "嗯……也许是我看错了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1ED1")

    Jump("loc_228A")

    label("loc_1ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1F24")

    #C0034
    ChrTalk(
        0xFE,
        (
            "哦哦，天都已经\x01",
            "这么黑了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "我差不多也该\x01",
            "动身回家了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228A")

    label("loc_1F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF3")

    #C0036
    ChrTalk(
        0xFE,
        (
            "说起来，最近很少见到\x01",
            "那个送比萨的送餐员了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "以前几乎每天\x01",
            "都能在这一带看到他……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#00003F（多半是给约纳送比萨的人吧……）\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#00100F（约纳现在应该在列曼自治州呢。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_205C")

    label("loc_1FF3")


    #C0040
    ChrTalk(
        0xFE,
        (
            "以前几乎每天\x01",
            "都能在这一带看到\x01",
            "那个送比萨的送餐员。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "呵呵，附近大概住着一位\x01",
            "非常爱吃比萨的人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_205C")

    Jump("loc_228A")

    label("loc_2061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213D")

    #C0042
    ChrTalk(
        0xFE,
        (
            "我和不久前搬家到这里\x01",
            "的几个年轻人打了招呼，\x01",
            "但他们却根本不理我。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "不仅如此，还用充满蔑视的目光\x01",
            "扫了我一眼，并冷哼了一声……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "唔唔……\x01",
            "以前住在这里的那一家人\x01",
            "真是比他们好相处多了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21A0")

    label("loc_213D")


    #C0045
    ChrTalk(
        0xFE,
        (
            "听说之前搬到这里的\x01",
            "那几个人都是\x01",
            "某大公司高层的儿子……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "唔唔……\x01",
            "真是些让人讨厌的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A0")

    Jump("loc_228A")

    label("loc_21A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21B3")
    Jump("loc_228A")

    label("loc_21B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_228A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2205")

    #C0047
    ChrTalk(
        0xFE,
        (
            "唉呀呀，又是那些年轻人啊……\x01",
            "实在是吵死人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228A")

    label("loc_2205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225A")

    #C0048
    ChrTalk(
        0xFE,
        "唔～这天气让人真舒服啊。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "忍不住想打哈欠呢。\x01",
            "呼～嗯嗯……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_228A")

    label("loc_225A")


    #C0050
    ChrTalk(
        0xFE,
        "这一带真是很宁静啊。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "最适合晒太阳了。\x02",
    )

    CloseMessageWindow()

    label("loc_228A")

    TalkEnd(0xFE)
    Return()

    # Function_6_1816 end

    def Function_7_228E(): pass

    label("Function_7_228E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2341")

    #C0052
    ChrTalk(
        0xFE,
        "听说迪塔总统已经被拘捕了。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "虽然我曾经是支持他的……\x01",
            "但他的做法确实太过强硬了。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "恶有恶报，这果然是\x01",
            "不变的世间常理啊，\x01",
            "我也要时常自省。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23AE")

    label("loc_2341")


    #C0055
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "那棵闪耀着蓝白色光芒的大树\x01",
            "到底是什么东西？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "如今总统已经被逮捕，\x01",
            "要由谁来负责应对呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23AE")

    Jump("loc_2F1B")

    label("loc_23B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23C1")
    Jump("loc_2F1B")

    label("loc_23C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_24DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2475")

    #C0057
    ChrTalk(
        0xFE,
        (
            "『克洛斯贝尔独立国』……\x01",
            "虽然现在还没有什么实际感触……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "但如果真能彻底实现，\x01",
            "对克洛斯贝尔来说，实在是前进了一大步。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "我强烈支持\x01",
            "迪塔总统。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24D6")

    label("loc_2475")


    #C0060
    ChrTalk(
        0xFE,
        (
            "我强烈支持\x01",
            "迪塔总统。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "如果真能彻底实现独立，\x01",
            "对克洛斯贝尔来说，\x01",
            "可以算是前进了一大步。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D6")

    Jump("loc_2F1B")

    label("loc_24DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_261C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A0")

    #C0062
    ChrTalk(
        0xFE,
        (
            "由于伊莉娅负伤倒下，\x01",
            "彩虹剧团已经陷入停业……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "虽然复兴计划一直在进行中，\x01",
            "但我们这些市民的心上\x01",
            "还是笼罩着一层阴影。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "如今哪怕能有一条\x01",
            "正面的好消息也好啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2617")

    label("loc_25A0")


    #C0065
    ChrTalk(
        0xFE,
        (
            "虽然复兴计划一直在进行中，\x01",
            "但我们这些市民的心上\x01",
            "还是笼罩着一层阴影。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "如今哪怕能有一条\x01",
            "正面的好消息也好啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2617")

    Jump("loc_2F1B")

    label("loc_261C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2731")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C3")

    #C0067
    ChrTalk(
        0xFE,
        (
            "警备队现在好像\x01",
            "仍在玛因兹山道\x01",
            "与武装集团作战。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "警备队努力了一整晚\x01",
            "都没能将事件解决……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "唔唔，由此看来，\x01",
            "对手想必非常棘手呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_272C")

    label("loc_26C3")


    #C0070
    ChrTalk(
        0xFE,
        (
            "警备队是专业的战斗集团。\x01",
            "但他们却至今未能\x01",
            "将事件解决……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "唔唔，由此看来，\x01",
            "对手想必非常棘手呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_272C")

    Jump("loc_2F1B")

    label("loc_2731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_273F")
    Jump("loc_2F1B")

    label("loc_273F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_27E5")

    #C0072
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的公演……\x01",
            "据说要由一个名叫修利的新人\x01",
            "来担当新增片段的演出。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "不久前的新人莉夏·毛\x01",
            "现在已经如此活跃……\x01",
            "真是也很期待修利今后的表现啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F1B")

    label("loc_27E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_284E")

    #C0074
    ChrTalk(
        0xFE,
        (
            "距离彩虹剧团的公演\x01",
            "只剩两天了……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "我已经成功买到了\x01",
            "Ａ席的票，\x01",
            "真是太期待演出了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F1B")

    label("loc_284E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_299A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290F")

    #C0076
    ChrTalk(
        0xFE,
        (
            "独立为正式国家……\x01",
            "我认为这相当困难。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "身为宗主国的帝国与共和国\x01",
            "无论如何也不会同意的。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "我虽然明白市长的想法……\x01",
            "但不得不说，他这种提案\x01",
            "实在是太轻率了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2995")

    label("loc_290F")


    #C0079
    ChrTalk(
        0xFE,
        (
            "身为宗主国的帝国与共和国\x01",
            "显然不可能同意\x01",
            "克洛斯贝尔独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "我虽然明白市长的想法……\x01",
            "但不得不说，他这种提案\x01",
            "实在是有勇无谋啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2995")

    Jump("loc_2F1B")

    label("loc_299A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2AAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A44")

    #C0081
    ChrTalk(
        0xFE,
        (
            "我们公司也在\x01",
            "兰花塔内\x01",
            "租用了办公场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "在通商会议结束之后，\x01",
            "就要开始营业了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "这场会议究竟能取得\x01",
            "怎样的成果呢……\x01",
            "真是好期待啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AA8")

    label("loc_2A44")


    #C0084
    ChrTalk(
        0xFE,
        (
            "我们公司也在\x01",
            "兰花塔内\x01",
            "租用了办公场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "通商会议究竟能取得\x01",
            "怎样的成果呢……\x01",
            "真是好期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA8")

    Jump("loc_2F1B")

    label("loc_2AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B49")

    #C0086
    ChrTalk(
        0xFE,
        (
            "我好像听到\x01",
            "有小女孩的声音\x01",
            "从那所房屋中传出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "嗯？可那所房屋\x01",
            "一直都是无人居住的……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "唔，算了，大概只是我幻听吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BB0")

    label("loc_2B49")


    #C0089
    ChrTalk(
        0xFE,
        (
            "说起来，大约在十年前，\x01",
            "还曾流传过那所房屋\x01",
            "有幽灵出现的传闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "呼，但也只是个\x01",
            "无聊的传闻而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BB0")

    Jump("loc_2F1B")

    label("loc_2BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C40")

    #C0091
    ChrTalk(
        0xFE,
        (
            "兰花塔终于\x01",
            "揭下了帷幕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "没想到竟能建成\x01",
            "如此雄伟的建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "嗯，真是\x01",
            "期待今后的发展啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C8C")

    label("loc_2C40")


    #C0094
    ChrTalk(
        0xFE,
        (
            "兰花塔……\x01",
            "竟然能建成如此雄伟的建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "嗯，真是\x01",
            "期待今后的发展啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C8C")

    Jump("loc_2F1B")

    label("loc_2C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D3B")

    #C0096
    ChrTalk(
        0xFE,
        (
            "对了，彩虹剧团下一个\x01",
            "演出剧目的情报已经公布了。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "听说是『金之太阳、银之月』\x01",
            "的全新版本……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "唔……看来还是尽快\x01",
            "把票弄到手为好啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D9C")

    label("loc_2D3B")


    #C0099
    ChrTalk(
        0xFE,
        (
            "『金之太阳、银之月』\x01",
            "的新版究竟\x01",
            "会是什么样子呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "唔……看来还是尽快\x01",
            "把票弄到手为好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D9C")

    Jump("loc_2F1B")

    label("loc_2DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2DAF")
    Jump("loc_2F1B")

    label("loc_2DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2F1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E2E")

    #C0101
    ChrTalk(
        0xFE,
        (
            "我刚才看到了一辆\x01",
            "驾驶得非常野蛮的导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "真是的……万一发生了事故，\x01",
            "可该如何是好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F1B")

    label("loc_2E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EBB")

    #C0103
    ChrTalk(
        0xFE,
        (
            "听说新市政厅大楼\x01",
            "终于在日前竣工了。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "自开工那天算起，\x01",
            "已经过去了很长时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "哎呀呀，真期待\x01",
            "月底的揭幕式啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F1B")

    label("loc_2EBB")


    #C0106
    ChrTalk(
        0xFE,
        (
            "我也以企业家的身份参与了\x01",
            "新市政厅大楼的一些事业计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "哎呀呀，真期待\x01",
            "月底的揭幕式啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F1B")

    TalkEnd(0xFE)
    Return()

    # Function_7_228E end

    def Function_8_2F1F(): pass

    label("Function_8_2F1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FCD")
    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0108
    ChrTalk(
        0xFE,
        (
            "呵呵，把这辆导力车\x01",
            "驾驶得如此出神入化，\x01",
            "也只有你才能做到。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "瑞吉，拜托你继续\x01",
            "带我们开心兜风吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xC,
        "嘿嘿，包在我身上。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_300D")

    label("loc_2FCD")


    #C0111
    ChrTalk(
        0xFE,
        (
            "呵呵，把这辆导力车\x01",
            "驾驶得如此出神入化，\x01",
            "也只有你才能做到。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_300D")

    TalkEnd(0xFE)
    Return()

    # Function_8_2F1F end

    def Function_9_3011(): pass

    label("Function_9_3011")

    TalkBegin(0xFE)

    #C0112
    ChrTalk(
        0xFE,
        (
            "从外表也许看不出，\x01",
            "但瑞吉的驾驶技术非常厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "毕竟他爸爸是乌尔努公司\x01",
            "导力车开发部的一员啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_3011 end

    def Function_10_3080(): pass

    label("Function_10_3080")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_313D")
    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0114
    ChrTalk(
        0xFE,
        (
            "哎呀呀，在郊外\x01",
            "超速飞驰果然是\x01",
            "最高享受啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        (
            "嘿嘿，和在市里兜风不同，\x01",
            "外面并没有多余的障碍物。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        "呵呵，接下来也拜托你啦，瑞吉。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 4)
    Jump("loc_319D")

    label("loc_313D")


    #C0117
    ChrTalk(
        0xFE,
        (
            "哎呀呀，在郊外\x01",
            "超速飞驰果然是\x01",
            "最高享受啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "今后还要继续\x01",
            "改装导力车，\x01",
            "追求更快的速度。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_319D")

    TalkEnd(0xFE)
    Return()

    # Function_10_3080 end

    def Function_11_31A1(): pass

    label("Function_11_31A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3212")

    #C0119
    ChrTalk(
        0xFE,
        (
            "呜呜，不知道是不是\x01",
            "因为下雨的缘故，\x01",
            "今天化的妆有些走形了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        "啊啊，好想重新化一下……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3261")

    label("loc_3212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3261")

    #C0121
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "今天也必须外出工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "呼，但下雨天出门\x01",
            "真是很讨厌啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3261")

    TalkEnd(0xFE)
    Return()

    # Function_11_31A1 end

    def Function_12_3265(): pass

    label("Function_12_3265")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3528")

    #C0123
    ChrTalk(
        0x101,
        (
            "#00005F哎，哈罗德先生……\x01",
            "莫非您正准备\x01",
            "外出吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xF,
        (
            "#03600F嗯，不久前接到了\x01",
            "来自阿尔摩利卡村的邀请。\x02\x03",

            "#03604F伊安律师也劝我过去，\x01",
            "所以原本计划全家\x01",
            "到那边暂住一段时间……\x02\x03",

            "#03608F但万万没想到，在出发之日的早上，\x01",
            "克洛斯贝尔就发生了这么严重的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        "#00103F……我们也感到十分不安。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#00300F不过，既然人家热情邀请，\x01",
            "还是过去为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x103,
        (
            "#00200F是啊……哈罗德先生\x01",
            "好像很久没有休假了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xF,
        (
            "#03603F不……\x01",
            "我准备先把索菲亚和柯林送到村子，\x01",
            "然后立刻返回市里。\x02\x03",

            "#03600F关照我生意的各位似乎也相当慌乱，\x01",
            "不能扔下他们一走了之。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00003F这样啊……\x02\x03",

            "#00001F老实说，今后无论发生\x01",
            "什么情况都不足为奇。\x02\x03",

            "如果要前往市外，\x01",
            "请一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xF,
        (
            "#03600F哈哈……谢谢提醒，\x01",
            "你们也要小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 0)
    Jump("loc_363F")

    label("loc_3528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35E0")

    #C0131
    ChrTalk(
        0xF,
        (
            "#03600F我准备先把索菲亚和柯林送到村子，\x01",
            "然后立刻返回市里。\x02\x03",

            "#03603F虽然很对不起索菲亚和\x01",
            "兴致勃勃的柯林……\x01",
            "但现在的局势太混乱了。\x02\x03",

            "#03600F……各位也要多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_363F")

    label("loc_35E0")


    #C0132
    ChrTalk(
        0xF,
        (
            "#03603F我准备先把索菲亚和柯林送到村子，\x01",
            "然后立刻返回市里。\x02\x03",

            "#03600F……各位也要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_363F")

    TalkEnd(0xFE)
    Return()

    # Function_12_3265 end

    def Function_13_3643(): pass

    label("Function_13_3643")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36D6")

    #C0133
    ChrTalk(
        0xFE,
        (
            "今天好不容易全家团聚，\x01",
            "能一起吃顿晚饭，\x01",
            "我要去买些东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "但只要一出门就会\x01",
            "看到那棵大得夸张的树，\x01",
            "实在是很不安啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3745")

    label("loc_36D6")


    #C0135
    ChrTalk(
        0xFE,
        (
            "……在这种时候，\x01",
            "就更要像奶奶说的那样\x01",
            "保持平常心。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "那棵巨大的树算什么！\x01",
            "吹口哨放松一下就不会害怕啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3745")

    TalkEnd(0xFE)
    Return()

    # Function_13_3643 end

    def Function_14_3749(): pass

    label("Function_14_3749")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -5490, -6000, -34180, 180)
    SetChrPos(0x102, -4510, -6000, -33860, 180)
    SetChrPos(0x104, -5450, -6000, -33100, 180)
    SetChrPos(0x109, -4650, -6000, -31730, 180)
    SetChrPos(0x105, -5460, -6000, -31370, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11500.itp")
    SetChrFlags(0xFE, 0x8000)
    SetChrFlags(0xFE, 0x40)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_68(-7650, -4000, -36130, 0)
    MoveCamera(56, 18, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(11500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    #C0137
    ChrTalk(
        0xFE,
        (
            "#11504F#11P哼哼～呵呵……\x02\x03",

            "#11505F……噢，发现鱼了！\x01",
            "听说最近出现了新种类的鱼，\x01",
            "看来果然是真的呢。\x02\x03",

            "#11509F哎呀呀，早知如此，\x01",
            "真该把钓竿带来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#00001F#5P雷克特先生……\x01",
            "你在这种地方做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0139
    AnonymousTalk(
        0xFE,
        (
            "哦哦，虽然没带钓竿，\x01",
            "但猎物还是上钩了啊。\x02\x03",

            "两手两脚的猎物共计五只……\x01",
            "嗯，这垂钓成果还算不错吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0140
    ChrTalk(
        0x109,
        "#10105F#5P什、什么……！\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        (
            "#00301F#5P莫非你想说，\x01",
            "我们都是被你钓到这里的？\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "#11509F#11P哈哈，的确是想\x01",
            "这样说呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#00003F#5P（……绝对不能顺着\x01",
            "  他的步调走。）\x02\x03",

            "#00001F……雷克特先生，\x01",
            "容我换一个问题吧。\x02\x03",

            "身为将『赤色星座』引入克洛斯贝尔\x01",
            "的帝国军情报局人士，\x01",
            "你在这种地方做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0144
    ChrTalk(
        0xFE,
        "#11509F#11P哈哈，问得真直白啊。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x105,
        (
            "#10302F#5P呵呵，和你这样的人打交道，\x01",
            "这种开门见山的对话方式\x01",
            "不是再合适不过吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 500)

    #C0146
    ChrTalk(
        0xFE,
        (
            "#11504F#12P哈哈，也罢，\x01",
            "我就回答你的问题吧。\x02\x03",

            "#11500F如你们所见，\x01",
            "我来这里只是为了放松休息。\x02\x03",

            "#11506F就算是我，一天到晚总是\x01",
            "守在那大叔的身边也会很累啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0147
    ChrTalk(
        0x101,
        (
            "#00005F#5P大、大叔……\x01",
            "是指奥斯本宰相阁下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        (
            "#00101F#5P我一直隐隐这样觉得……\x01",
            "看来你果然是宰相\x01",
            "身边的亲信吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "#11502F#4P呵呵，这个嘛，\x01",
            "我可从来都不记得\x01",
            "自己这么说过。\x02\x03",

            "#11504F……好啦，\x01",
            "休息时间已经结束，\x01",
            "我也该回大叔那里了。\x02\x03",

            "#11500F就此告辞，\x01",
            "你们加油工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x109,
        "#10105F#5P那、那个……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x2D, 0x1F4)

    def lambda_3E0B():

        label("loc_3E0B")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3E0B")

    QueueWorkItem2(0x101, 2, lambda_3E0B)

    def lambda_3E1D():

        label("loc_3E1D")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3E1D")

    QueueWorkItem2(0x102, 2, lambda_3E1D)

    def lambda_3E2F():

        label("loc_3E2F")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3E2F")

    QueueWorkItem2(0x104, 2, lambda_3E2F)

    def lambda_3E41():

        label("loc_3E41")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3E41")

    QueueWorkItem2(0x109, 2, lambda_3E41)

    def lambda_3E53():

        label("loc_3E53")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3E53")

    QueueWorkItem2(0x105, 2, lambda_3E53)
    OP_68(-7430, -4000, -32960, 6000)
    OP_95(0xFE, -4000, -6000, -34790, 3000, 0x1)
    OP_95(0xFE, -4000, -4310, -16630, 3000, 0x0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    #C0151
    ChrTalk(
        0x104,
        (
            "#00306F#5P哎呀呀，\x01",
            "问题全都被他混过去了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_END)), "loc_3EEC")
    Call(0, 15)

    label("loc_3EEC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, -5490, -6000, -34180, 180)
    ClearChrFlags(0xFE, 0x8000)
    SetChrFlags(0xFE, 0x80)
    OP_CC(0x1, 0x0, 0x0)
    SetScenarioFlags(0x1C7, 3)
    OP_29(0xA3, 0x1, 0xA)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_14_3749 end

    def Function_15_3F31(): pass

    label("Function_15_3F31")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-8100, -4000, -35460, 2000)
    MoveCamera(56, 18, 0, 2000)
    OP_6E(620, 2000)
    SetCameraDistance(11500, 2000)
    Sleep(3000)
    OP_64(0xFFFF)

    #C0152
    ChrTalk(
        0x101,
        (
            "#00003F#6P雷克特先生和雾香小姐……\x02\x03",

            "帝国与共和国的谍报人员\x01",
            "在同一时间段\x01",
            "出现在了市内。\x02\x03",

            "#00001F……各位，你们怎么想？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3FF7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3FF7)
    Sleep(50)

    def lambda_4007():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4007)
    Sleep(50)

    def lambda_4017():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4017)
    Sleep(50)

    def lambda_4027():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4027)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0153
    ChrTalk(
        0x109,
        "#10103F#6P……总觉得有些蹊跷呢。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x105,
        (
            "#10302F#6P呵呵，既然如此，\x01",
            "我们要继续追踪他们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        (
            "#00108F#6P那应该很困难吧。\x02\x03",

            "#00103F在我们赶到的时候，\x01",
            "他们都是一副早已料到的样子……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#00003F#6P……还是去向达德利警官\x01",
            "他们报告吧。\x02\x03",

            "#00000F结合搜查一科的情报，\x01",
            "说不定可以了解到什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x109,
        "#10105F#6P啊……有道理呢。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x104,
        (
            "#00300F#6P好，既然决定了，\x01",
            "那我们就去警察总部吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA3, 0x1, 0xC)
    Return()

    # Function_15_3F31 end

    def Function_16_41BE(): pass

    label("Function_16_41BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 6)), scpexpr(EXPR_END)), "loc_421B")
    EventBegin(0x2)
    ClearMapFlags(0x20)

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里是共和国派议员坎贝尔的宅邸，\x01",
            "现在并无来此拜访的必要。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Jump("loc_4578")

    label("loc_421B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E5")
    TalkBegin(0xFF)

    #C0160
    ChrTalk(
        0x101,
        "#00005F这里好像是……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#00100F是共和国派议员\x01",
            "坎贝尔先生的住宅。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        (
            "#10105F听说不少议员因为\x01",
            "与那起教团事件有所牵连，\x01",
            "纷纷落马……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x102,
        (
            "#00103F嗯，当时并没有\x01",
            "查到坎贝尔议员与\x01",
            "教团事件之间的联系。\x02\x03",

            "#00100F虽然他好像和『黑月』\x01",
            "有一定往来，\x01",
            "但目前并没有违法……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，反正是个\x01",
            "可疑人物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4473")

    #C0165
    ChrTalk(
        0x101,
        (
            "#00000F对了，艾莉\x01",
            "好像认识坎贝尔议员\x01",
            "的女儿吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#00100F是说卡拉小姐吧？\x01",
            "嗯，我们当年一起在主日学校上过课。\x02\x03",

            "#00104F因为存在这层交情，\x01",
            "在得知她父亲与教团之间并无牵连时，\x01",
            "真是松了一口气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x109,
        (
            "#10108F可以理解……\x01",
            "如果熟人的父亲是那样的人，\x01",
            "确实是很难接受。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4473")


    #C0168
    ChrTalk(
        0x101,
        (
            "#00000F嗯，总之……\x01",
            "我们现在也没什么事情，\x01",
            "还是不要进去拜访了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x102,
        (
            "#00100F嗯，是啊，\x01",
            "我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 6)
    TalkEnd(0xFF)
    Jump("loc_4578")

    label("loc_44E5")

    TalkBegin(0xFF)

    #C0170
    ChrTalk(
        0x101,
        (
            "#00000F这里好像是……\x01",
            "共和国派议员\x01",
            "坎贝尔先生的住宅。\x02\x03",

            "我们现在也没什么事情，\x01",
            "还是不要进去拜访了。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#00100F嗯，是啊，\x01",
            "我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 6)
    TalkEnd(0xFF)

    label("loc_4578")

    Return()

    # Function_16_41BE end

    def Function_17_4579(): pass

    label("Function_17_4579")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45A7")
    Call(0, 39)
    Return()

    label("loc_45A7")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_17_4579 end

    def Function_18_45CE(): pass

    label("Function_18_45CE")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_18_45CE end

    def Function_19_45F3(): pass

    label("Function_19_45F3")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0174
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(-10220, -4000, -43550, 1500)
    MoveCamera(45, 35, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(15500, 1500)
    Sleep(1000)
    SetChrName("")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要钓鱼吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46B6")
    OP_E2(0x2)
    MiniGame(0x6, 0x2, 0xFFFFEAA2, 0xFFFFE890, 0xFFFF5DB2, 0x10E, 0xFFFFD90E, 0xFFFFE69C, 0xFFFF5C36)

    label("loc_46B6")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_19_45F3 end

    def Function_20_46BB(): pass

    label("Function_20_46BB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    LoadChrToIndex("apl/ch51107.itc", 0x1E)
    SoundLoad(468)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, 0, -23000, 0)
    ClearChrFlags(0x12, 0x80)
    OP_78(0x10, 0x12)
    OP_49()
    SetChrPos(0x12, 25550, 0, -4600, 0)
    OP_D5(0x12, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFrame(0x10, "light", 0x0, 0x1)
    OP_74(0x10, 0x1E)
    OP_71(0x10, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47C6")
    SetChrFlags(0x9, 0x8000)
    EndChrThread(0x9, 0xFF)
    SetChrPos(0x9, -5000, 0, -5000, 180)

    def lambda_47B6():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_47B6)

    label("loc_47C6")

    FadeToBright(1000, 0)
    BeginChrThread(0x12, 3, 0, 21)
    BeginChrThread(0x11, 3, 0, 22)
    BeginChrThread(0x17, 1, 0, 23)
    OP_68(-650, 2600, -7350, 0)
    MoveCamera(57, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19150, 0)
    OP_68(-6650, 2600, -7350, 7500)
    OP_6F(0x79)
    OP_0D()
    StopSound(468, 1000, 100)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_46BB end

    def Function_21_4847(): pass

    label("Function_21_4847")

    SetChrPos(0xFE, 25550, 0, -4600, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -6000, 0, -4600)
    OP_9F(0x1, -15000, 0, -3100)
    OP_9F(0x1, -16000, 0, 7900)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_21_4847 end

    def Function_22_4890(): pass

    label("Function_22_4890")

    Sleep(2000)
    OP_95(0xFE, 0, 0, -5600, 2000, 0x1)
    OP_95(0xFE, -14000, 0, -5600, 2000, 0x1)
    Return()

    # Function_22_4890 end

    def Function_23_48BC(): pass

    label("Function_23_48BC")

    Sound(468, 2, 100, 0)
    Sound(458, 0, 100, 0)
    Sleep(4500)
    Sound(494, 0, 70, 0)
    Return()

    # Function_23_48BC end

    def Function_24_48D2(): pass

    label("Function_24_48D2")

    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x9, 0x0)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x12, 0x13)
    OP_49()
    SetChrPos(0x13, -15860, 300, 25000, 180)
    OP_D5(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0xB5, 0xF0, 0x1, 0x20)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B76")
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(20100, 2200, -2560, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 19840, 0, -3660, 270)
    SetChrPos(0x102, 20660, 0, -4830, 270)
    SetChrPos(0x109, 21080, 0, -3150, 270)
    SetChrPos(0x105, 22020, 0, -4490, 270)

    def lambda_4A00():
        OP_97(0x101, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A00)
    Sleep(50)

    def lambda_4A1D():
        OP_97(0x102, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A1D)
    Sleep(50)

    def lambda_4A3A():
        OP_97(0x109, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4A3A)
    Sleep(50)

    def lambda_4A57():
        OP_97(0x105, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4A57)
    OP_68(20100, 500, -2560, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sound(488, 0, 70, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0176
    ChrTalk(
        0x101,
        "#00005F这声音是……？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-14390, 500, 10820, 0)
    MoveCamera(70, 35, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(23150, 0)
    SetChrPos(0x101, 3840, 0, -2230, 180)
    SetChrPos(0x102, 4970, 0, -2230, 180)
    SetChrPos(0x109, 6070, 0, -2280, 180)
    SetChrPos(0x105, 7190, 0, -2280, 180)
    OP_0D()
    Jump("loc_4D56")

    label("loc_4B76")

    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(1780, 500, -34350, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -320, 0, -33220, 0)
    SetChrPos(0x102, 890, 0, -33930, 0)
    SetChrPos(0x109, -170, 0, -34990, 0)
    SetChrPos(0x105, 1100, 0, -35480, 0)

    def lambda_4C29():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C29)
    Sleep(50)

    def lambda_4C46():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4C46)
    Sleep(50)

    def lambda_4C63():
        OP_97(0x109, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4C63)
    Sleep(50)

    def lambda_4C80():
        OP_97(0x105, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4C80)
    OP_68(2420, 500, -31230, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sound(488, 0, 70, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0177
    ChrTalk(
        0x101,
        "#00005F这声音是……？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-14390, 500, 10820, 0)
    MoveCamera(70, 35, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(23150, 0)
    OP_0D()

    label("loc_4D56")

    OP_68(-13920, 500, -3320, 1000)
    MoveCamera(31, 31, 0, 1000)
    OP_6E(620, 1000)
    SetCameraDistance(20000, 1000)
    BeginChrThread(0x13, 1, 0, 25)
    BeginChrThread(0x17, 1, 0, 26)

    #N0178
    NpcTalk(
        0x12,
        "青年的声音",
        "#10A呀哈～！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_68(8360, 1450, -3280, 1500)
    MoveCamera(39, 29, 0, 1500)

    #N0179
    NpcTalk(
        0x12,
        "青年的声音",
        "#5A哈哈，太爽啦！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)

    def lambda_4DF3():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DF3)
    Sleep(50)

    def lambda_4E03():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E03)
    Sleep(50)

    def lambda_4E13():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4E13)
    Sleep(50)

    def lambda_4E23():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4E23)
    OP_6F(0x79)
    OP_0D()
    Sleep(1500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4EC5")
    Fade(500)
    OP_68(0, 1450, -27400, 0)
    MoveCamera(46, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -830, 0, -26340, 0)
    SetChrPos(0x102, 780, 0, -26550, 0)
    SetChrPos(0x109, -420, 0, -27750, 0)
    SetChrPos(0x105, 1070, 0, -27950, 0)
    OP_0D()
    Jump("loc_4FF2")

    label("loc_4EC5")

    Fade(500)
    OP_68(5950, 1450, -3730, 0)
    MoveCamera(49, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 3840, 0, -2230, 90)
    SetChrPos(0x102, 4970, 0, -2230, 90)
    SetChrPos(0x109, 6070, 0, -2280, 90)
    SetChrPos(0x105, 7190, 0, -2280, 90)
    OP_0D()

    def lambda_4F42():
        OP_95(0x102, 4970, 0, -5120, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F42)
    Sleep(100)

    def lambda_4F5F():
        OP_95(0x101, 3840, 0, -3970, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F5F)
    Sleep(100)

    def lambda_4F7C():
        OP_95(0x109, 6070, 0, -3420, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4F7C)
    Sleep(100)

    def lambda_4F99():
        OP_95(0x105, 7190, 0, -4250, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F99)
    WaitChrThread(0x109, 1)

    def lambda_4FB7():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4FB7)
    WaitChrThread(0x105, 1)

    def lambda_4FC8():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4FC8)
    WaitChrThread(0x101, 1)

    def lambda_4FD9():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FD9)
    WaitChrThread(0x102, 1)

    def lambda_4FEA():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4FEA)

    label("loc_4FF2")


    #C0180
    ChrTalk(
        0x101,
        (
            "#00005F刚、刚才那是……？\x01",
            "速度未免也\x01",
            "太夸张了。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x109,
        (
            "#10101F明显已经超速行驶了……\x02\x03",

            "驾驶得那么野蛮，\x01",
            "导力车实在是很可怜。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#00101F危险驾驶的导力车……\x01",
            "最近好像有不少人\x01",
            "在市内看到过呢。\x02\x03",

            "#00103F据说狂飙车辆飞驰在各种场所，\x01",
            "给大家带来了很多麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x105,
        "#10305F哎，这样啊？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(50)

    #C0184
    ChrTalk(
        0x105,
        (
            "#10300F那么，身为特别任务支援科，\x01",
            "我们应该怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5152():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5152)
    Sleep(50)

    def lambda_5162():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5162)
    Sleep(50)

    def lambda_5172():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5172)
    Sleep(50)

    #C0185
    ChrTalk(
        0x101,
        (
            "#00003F自然没有\x01",
            "坐视不管\x01",
            "的理由。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5233")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0186
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆在港湾区与凯特巡警是否对过话？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【已对话】\x01",      # 0
            "【未对话】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 4)), scpexpr(EXPR_END)), "loc_52CD")

    #C0187
    ChrTalk(
        0x101,
        (
            "#00004F那辆车好像\x01",
            "驶向了凯特前辈\x01",
            "所负责的欢乐街。\x02\x03",

            "#00000F赶快用艾尼格玛\x01",
            "联络前辈吧。\x02\x03",

            "像这样的案件，\x01",
            "交给公共安全科来处理是最妥善的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5346")

    label("loc_52CD")


    #C0188
    ChrTalk(
        0x101,
        (
            "#00003F……先和公共安全科\x01",
            "的凯特前辈\x01",
            "联络一下吧。\x02\x03",

            "#00000F说不定前辈\x01",
            "已经有所\x01",
            "应对了。\x02\x03",

            "先用艾尼格玛\x01",
            "联络一下前辈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5346")

    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(100)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(823, 0, 100, 0)
    Sleep(2700)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("凯特的声音")

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "您好，我是公共安全科\x01",
            "的凯特巡警。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0190
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F凯特前辈，您辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("凯特的声音")

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，罗伊德，\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0192
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F嗯，有件事情\x01",
            "想和前辈谈谈……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将\x01",
            "飙车族的情况\x01",
            "做了简要说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("凯特的声音")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，你们也\x01",
            "目击到了啊。\x02\x03",

            "嗯，既然如此……\x01",
            "请各位协助我们一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0195
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F协助吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("凯特的声音")

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果你们有时间，\x01",
            "能否先到\x01",
            "我这里来？\x02\x03",

            "我在欢乐街的\x01",
            "酒店附近等你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0197
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F好、好的，\x01",
            "明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("凯特的声音")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，那就稍后见。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 40, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x10E, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x101, 0x105, 500)
    Sleep(100)

    #C0199
    ChrTalk(
        0x102,
        "#00100F……凯特巡警怎么说？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#00000F哦，她希望我们\x01",
            "过去协助一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x109,
        "#10105F要和公共安全科合作吗？\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x105,
        (
            "#10309F强行制止狂飙导力车！\x01",
            "……大概会要我们这样做吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#00006F那、那未免\x01",
            "也太危险了吧……\x02\x03",

            "#00000F总之，我们先去\x01",
            "欢乐街酒店的附近看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x130, 5)
    SetMapObjFlags(0x12, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32280, 0, -4370, 270)
    BeginChrThread(0x9, 0, 0, 1)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57DA")
    SetChrPos(0x0, -320, 0, -25290, 0)
    Jump("loc_57EB")

    label("loc_57DA")

    SetChrPos(0x0, 3840, 0, -3970, 90)

    label("loc_57EB")

    EventEnd(0x5)
    Return()

    # Function_24_48D2 end

    def Function_25_57EE(): pass

    label("Function_25_57EE")

    SetChrPos(0x13, -15860, 300, 20000, 180)
    OP_96(0xFE, 0xFFFFBD7A, 0x0, 0xFFFFF8B2, 0x4E20, 0x0)
    OP_9F(0x0, 0x13)
    OP_9F(0x1, -16800, 0, -2530)
    OP_9F(0x1, -14190, 0, -5130)
    OP_9F(0x1, -12700, 0, -5370)
    OP_9F(0x2, 0x13, 11000, 0x6)
    OP_96(0xFE, 0x767A, 0x0, 0xFFFFE85E, 0x4E20, 0x0)
    Return()

    # Function_25_57EE end

    def Function_26_585F(): pass

    label("Function_26_585F")

    Sound(486, 0, 100, 0)
    Sleep(1000)
    Sound(487, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Return()

    # Function_26_585F end

    def Function_27_5875(): pass

    label("Function_27_5875")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5946")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆是否完成了任务「取缔违法飙车」？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",      # 0
            "【已完成】\x01",        # 1
            "【未完成】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5932")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_5946")

    label("loc_5932")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5946")
    OP_29(0x69, 0x3, 0x10)

    label("loc_5946")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59E4")

    #C0205
    ChrTalk(
        0x101,
        (
            "#00005F这是……\x01",
            "昨天那些不良青年\x01",
            "乘坐的导力车啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        "#00105F为什么会在这种地方……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x109,
        (
            "#10106F不知道……\x01",
            "但总有种不好的预感呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ADF")

    label("loc_59E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A56")

    #C0208
    ChrTalk(
        0x101,
        "#00006F那三个人的导力车吗……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，这么高档的车，\x01",
            "和他们真是完全不相称啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ADF")

    label("loc_5A56")


    #C0210
    ChrTalk(
        0x101,
        (
            "#00005F这是……\x01",
            "好高级的导力车啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x105,
        (
            "#10300F呼，装饰风格\x01",
            "相当招摇呢。\x02\x03",

            "#10304F但如果与车主\x01",
            "的气质不相称，\x01",
            "也只会显得很滑稽而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ADF")

    TalkEnd(0xFF)
    Return()

    # Function_27_5875 end

    def Function_28_5AE3(): pass

    label("Function_28_5AE3")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-17170, -3900, -20000, 0)
    MoveCamera(358, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13200, 0)
    SetChrPos(0x101, -17570, -6000, -17670, 315)
    SetChrPos(0x102, -16410, -6000, -17600, 315)
    SetChrPos(0x109, -17240, -6000, -19410, 315)
    SetChrPos(0x105, -16090, -6000, -19200, 315)
    FadeToBright(1000, 0)
    OP_0D()

    #C0212
    ChrTalk(
        0x101,
        (
            "#12P#00000F与麦克道尔官邸相邻的房屋……\x01",
            "就是这里没错了。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0x0, 0x2EE, 0x3E8, 0x0)
    Sleep(500)
    Sound(808, 0, 100, 0)
    Sleep(500)

    #C0213
    ChrTalk(
        0x101,
        (
            "#12P#00000F不好意思，\x01",
            "请问有人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0214
    ChrTalk(
        0x101,
        "#12P#00003F不行，没反应呢。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        "#12P#00105F大门上锁了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0216
    ChrTalk(
        0x101,
        (
            "#5P#00001F不……\x01",
            "好像并没锁呢。\x02\x03",

            "#00003F而且还能听到\x01",
            "从中传出的说话声……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x109,
        (
            "#12P#10105F是不是聊得太投入，\x01",
            "所以没有听到叫门声呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x105,
        (
            "#12P#10300F好啦，既然门没锁，\x01",
            "我们直接进去也无所谓吧？\x02\x03",

            "#10302F再怎么说，我们也是\x01",
            "堂堂正正的警官嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0219
    ChrTalk(
        0x101,
        (
            "#5P#00006F就算是警察，\x01",
            "也不能擅自闯进别人家的……\x02\x03",

            "#00000F但不管怎么说，\x01",
            "我们也不能放着这里不管，\x01",
            "进去之后再出声打招呼好了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(128, 2000, 90)
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x206), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c0350", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_28_5AE3 end

    def Function_29_5E09(): pass

    label("Function_29_5E09")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-17170, -3900, -20000, 0)
    MoveCamera(358, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13200, 0)
    SetChrPos(0x101, -17570, -6000, -17670, 135)
    SetChrPos(0x102, -16410, -6000, -17600, 225)
    SetChrPos(0x109, -17240, -6000, -19410, 0)
    SetChrPos(0x105, -16090, -6000, -19200, 315)
    FadeToBright(1000, 0)
    OP_0D()

    #C0220
    ChrTalk(
        0x105,
        (
            "#12P#10302F哎呀呀，未免也\x01",
            "太过自由浪荡了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x102,
        (
            "#11P#00106F嗯，真是典型的\x01",
            "浪荡公子哥呢。\x02\x03",

            "#00108F话说回来，\x01",
            "这所住宅竟然会\x01",
            "落到那种人的手中……\x02\x03",

            "#00103F本德先生\x01",
            "肯定很难接受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x109,
        (
            "#6P#10101F不过，房屋合同\x01",
            "好像并无违法之处……\x02\x03",

            "#10106F就算想说些什么也无从开口，\x01",
            "这才是最让人不甘心的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#5P#00003F是啊……但我们现在\x01",
            "也只能不管他们了。\x02\x03",

            "#00000F……总之，\x01",
            "住宅街的调查工作就到此结束。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6134")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0224
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆「调查状况如何？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",                    # 0
            "【尚未去本德的新住所拜访】\x01",      # 1
            "【还有未调查之处】\x01",              # 2
            "【已在六处地点确认完毕】\x01",        # 3
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
        (0, "loc_6105"),
        (1, "loc_610A"),
        (2, "loc_6112"),
        (3, "loc_6123"),
        (SWITCH_DEFAULT, "loc_6134"),
    )


    label("loc_6105")

    Jump("loc_6134")

    label("loc_610A")

    ClearScenarioFlags(0x131, 7)
    Jump("loc_6134")

    label("loc_6112")

    SetScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_6134")

    label("loc_6123")

    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    SetScenarioFlags(0x132, 2)
    Jump("loc_6134")

    label("loc_6134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61FE")

    #C0225
    ChrTalk(
        0x102,
        (
            "#11P#00100F罗伊德，接下来\x01",
            "就去本德先生那里看看吧？\x02\x03",

            "我想问问他搬家一事\x01",
            "的详细原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#5P#00003F嗯，这的确很让人担心呢。\x02\x03",

            "#00000F好，那我们这就去\x01",
            "本德先生位于东街的新住所拜访吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_629A")

    label("loc_61FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6254")

    #C0227
    ChrTalk(
        0x101,
        (
            "#5P#00000F那么，我们继续去\x01",
            "调查剩下的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_629A")

    label("loc_6254")


    #C0228
    ChrTalk(
        0x101,
        (
            "#5P#00000F好，已经全部调查完毕了。\x02\x03",

            "去市民会馆汇报结果吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x6)

    label("loc_629A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_65(0x2, 0x1)
    SetMapObjFlags(0xB, 0x10)
    SetScenarioFlags(0x131, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -17150, -6000, -18250, 180)
    EventEnd(0x5)
    Return()

    # Function_29_5E09 end

    def Function_30_62CA(): pass

    label("Function_30_62CA")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    AddParty(0xA2, 0xFF, 0xFF)
    SetChrPos(0x1A3, -1920, 0, -11670, 225)
    LoadChrToIndex("chr/ch03401.itc", 0x1E)
    OP_68(-9190, -2230, -25380, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(8210, 0)
    SetChrPos(0x101, -6050, -5680, -19360, 180)
    SetChrPos(0x102, -4650, -5660, -19680, 180)
    SetChrPos(0x109, -5250, -4960, -18250, 180)
    SetChrPos(0x105, -3850, -4930, -18360, 180)
    SetChrPos(0x104, -6850, -4980, -17900, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_6397():
        OP_95(0xFE, -6050, -6000, -22480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6397)
    Sleep(50)

    def lambda_63B4():
        OP_95(0xFE, -4650, -6000, -22780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63B4)
    Sleep(50)

    def lambda_63D1():
        OP_95(0xFE, -5250, -6000, -21350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63D1)
    Sleep(50)

    def lambda_63EE():
        OP_95(0xFE, -3850, -6000, -21480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_63EE)
    Sleep(50)

    def lambda_640B():
        OP_95(0xFE, -6850, -6000, -21200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_640B)
    FadeToBright(1000, 0)
    OP_0D()

    #C0229
    ChrTalk(
        0x1A3,
        "#04602F啊～总算来了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_64D1():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64D1)
    Sleep(50)

    def lambda_64E1():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64E1)
    Sleep(50)

    def lambda_64F1():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_64F1)
    Sleep(50)

    def lambda_6501():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6501)
    Sleep(50)

    def lambda_6511():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6511)
    Sleep(1000)
    Fade(500)
    OP_68(-4050, 1670, -12540, 0)
    MoveCamera(42, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14080, 0)
    OP_0D()

    def lambda_6555():

        label("loc_6555")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_6555")

    QueueWorkItem2(0x101, 1, lambda_6555)

    def lambda_6567():

        label("loc_6567")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_6567")

    QueueWorkItem2(0x104, 1, lambda_6567)

    def lambda_6579():

        label("loc_6579")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_6579")

    QueueWorkItem2(0x102, 1, lambda_6579)

    def lambda_658B():

        label("loc_658B")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_658B")

    QueueWorkItem2(0x109, 1, lambda_658B)

    def lambda_659D():

        label("loc_659D")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_659D")

    QueueWorkItem2(0x105, 1, lambda_659D)
    OP_95(0x1A3, -1410, 0, -6320, 5000, 0x0)
    OP_95(0x1A3, -5270, 0, -6140, 5000, 0x0)
    OP_68(-9190, -2230, -25380, 3000)
    MoveCamera(44, 23, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(8210, 3000)
    OP_95(0x1A3, -5230, -5630, -19270, 4000, 0x0)
    OP_93(0x1A3, 0xE1, 0x1F4)
    WaitChrThread(0x1A3, 1)
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)

    #C0230
    ChrTalk(
        0x1A3,
        (
            "#5P#04600F你们的动作实在太慢，\x01",
            "所以我就直接开始找了。\x02\x03",

            "#04609F到底是哪座房子呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        (
            "#12P#00000F哦，就是这里了……\x02\x03",

            "#00006F……唔，可我们并没\x01",
            "答应带你一起行动啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x109, 0x3E8, 0x7D0, 0x0)
    Sleep(300)

    #C0232
    ChrTalk(
        0x1A3,
        (
            "#04600F这位姐姐，\x01",
            "你更喜欢狗还是猫？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x109,
        (
            "#12P#10105F问、问我吗？\x02\x03",

            "#10104F那个……\x01",
            "非要说的话，应该还是猫吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x1A3,
        (
            "#04609F啊哈哈！\x01",
            "和我一样呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0235
    ChrTalk(
        0x104,
        (
            "#6P#00303F（……放弃吧，\x01",
            "  和她说什么都没用的。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0236
    ChrTalk(
        0x101,
        "#12P#00006F（呼……看来是这样呢。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    SetScenarioFlags(0x155, 2)
    OP_C9(0x0, 0x1000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -5940, -6000, -22110, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_30_62CA end

    def Function_31_683A(): pass

    label("Function_31_683A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-17690, -3510, -20970, 0)
    MoveCamera(7, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12430, 0)
    SetChrPos(0x101, -19120, -5610, -16030, 135)
    SetChrPos(0x102, -19120, -5610, -16030, 135)
    SetChrPos(0x109, -19120, -5610, -16030, 135)
    SetChrPos(0x105, -19120, -5610, -16030, 135)
    SetChrPos(0x104, -19120, -5610, -16030, 135)
    SetChrPos(0x1A3, -19120, -5610, -16030, 135)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0xB, 0x10)
    OP_71(0xB, 0x0, 0x10, 0x0, 0x0)
    OP_79(0xB)
    Sleep(500)
    OP_68(-16690, -3510, -20970, 3000)
    BeginChrThread(0x1A3, 3, 0, 37)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 34)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 36)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 35)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 32)
    OP_6F(0x1)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0xB, 0x10, 0x0, 0x0, 0x0)
    OP_79(0xB)
    SetMapObjFlags(0xB, 0x10)
    WaitChrThread(0x101, 3)

    #C0237
    ChrTalk(
        0x1A3,
        "#12P#04609F好，那我们就继续吧！\x02",
    )

    CloseMessageWindow()
    OP_95(0x1A3, -11560, -6000, -23410, 2000, 0x0)

    #C0238
    ChrTalk(
        0x101,
        "#00006F该怎么说好呢……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x102,
        (
            "#00106F嗯……\x01",
            "压迫力真是好强啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x109,
        (
            "#10101F用那么细小的手臂，\x01",
            "竟然能提起两个魁梧的成年男人……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，真不愧是出身于\x01",
            "最强猎兵团的女孩啊。\x02\x03",

            "#10302F刚才那股杀气\x01",
            "毫不逊色于兰迪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#6P#00303F……不要把我和她相提并论。\x02",
    )

    CloseMessageWindow()
    OP_68(-14290, -3510, -23940, 3000)
    OP_6F(0x1)
    OP_93(0x1A3, 0x13B, 0x1F4)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_9C(0x1A3, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    OP_9C(0x1A3, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)

    #C0243
    ChrTalk(
        0x1A3,
        (
            "#12P#04606F真是的，你们在干什么啊？\x02\x03",

            "#04602F再不快点，\x01",
            "可就要找不到了哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        "#6P#00000F啊……我们这就出发。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    SetScenarioFlags(0x155, 3)
    OP_29(0x74, 0x1, 0x4)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -12100, -6000, -22550, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_31_683A end

    def Function_32_6C0A(): pass

    label("Function_32_6C0A")


    def lambda_6C0F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C0F)

    def lambda_6C20():
        OP_95(0xFE, -18140, -5600, -17170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C20)
    WaitChrThread(0x101, 1)
    OP_95(0x101, -17710, -6000, -18270, 2000, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Return()

    # Function_32_6C0A end

    def Function_33_6C55(): pass

    label("Function_33_6C55")


    def lambda_6C5A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C5A)

    def lambda_6C6B():
        OP_95(0xFE, -18140, -5600, -17170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C6B)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -16500, -6000, -17480, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_33_6C55 end

    def Function_34_6CA0(): pass

    label("Function_34_6CA0")


    def lambda_6CA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6CA5)

    def lambda_6CB6():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6CB6)
    WaitChrThread(0x104, 1)
    OP_95(0x104, -15930, -6000, -19920, 2000, 0x0)
    OP_93(0x104, 0x87, 0x1F4)
    Return()

    # Function_34_6CA0 end

    def Function_35_6CEB(): pass

    label("Function_35_6CEB")


    def lambda_6CF0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6CF0)

    def lambda_6D01():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6D01)
    WaitChrThread(0x109, 1)
    OP_95(0x109, -16510, -6000, -18800, 2000, 0x0)
    OP_93(0x109, 0x87, 0x1F4)
    Return()

    # Function_35_6CEB end

    def Function_36_6D36(): pass

    label("Function_36_6D36")


    def lambda_6D3B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6D3B)

    def lambda_6D4C():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6D4C)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -15400, -6000, -18710, 2000, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_36_6D36 end

    def Function_37_6D81(): pass

    label("Function_37_6D81")


    def lambda_6D86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_6D86)

    def lambda_6D97():
        OP_95(0xFE, -14830, -6000, -20120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_6D97)
    WaitChrThread(0x1A3, 1)
    OP_93(0x1A3, 0x13B, 0x1F4)
    Return()

    # Function_37_6D81 end

    def Function_38_6DB8(): pass

    label("Function_38_6DB8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    LoadChrToIndex("chr/ch03401.itc", 0x1F)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 17810, 0, -4050, 90)
    OP_68(-4400, 2000, -6530, 0)
    MoveCamera(37, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, -3430, 0, -5280, 90)
    SetChrPos(0x102, -3980, 0, -6980, 90)
    SetChrPos(0x104, -5330, 0, -4480, 90)
    SetChrPos(0x109, -5080, 0, -6480, 90)
    SetChrPos(0x105, -5830, 0, -5780, 90)
    SetChrPos(0x1A3, -3880, 0, -3980, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x9, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(16720, 2000, -5140, 6000)
    MoveCamera(45, 33, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(14880, 6000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-4400, 2000, -6530, 0)
    MoveCamera(37, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    OP_0D()

    #C0245
    ChrTalk(
        0x102,
        "#6P#00105F罗伊德……看那里！\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#00000F嗯，应该就是玛丽了。\x01",
            "#6P终于找到了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(16720, 2000, -5140, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12580, 0)
    SetChrPos(0x1A3, 7810, 0, -2750, 90)
    SetChrPos(0x101, 8310, 0, -4050, 90)
    SetChrPos(0x102, 7610, 0, -5350, 90)
    SetChrPos(0x104, 6110, 0, -2950, 90)
    SetChrPos(0x109, 5910, 0, -5250, 90)
    SetChrPos(0x105, 5310, 0, -4250, 90)
    OP_0D()
    OP_63(0x16, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x16, 0x0, 0x1F4)
    Sleep(400)
    OP_93(0x16, 0xB4, 0x1F4)
    Sleep(200)
    OP_93(0x16, 0x5A, 0x1F4)
    OP_64(0x16)
    Sleep(1000)
    OP_95(0x16, 31570, 0, -4230, 4000, 0x0)
    SetCameraDistance(14500, 3000)
    SetChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x1A3, 0x1F)
    SetChrSubChip(0x1A3, 0x0)
    SetChrFlags(0x1A3, 0x1000)

    def lambda_70E1():
        OP_95(0xFE, 19310, 0, -4050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70E1)
    Sleep(50)

    def lambda_70FE():
        OP_95(0xFE, 18810, 0, -2750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_70FE)
    Sleep(50)

    def lambda_711B():
        OP_95(0xFE, 18610, 0, -5350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_711B)
    Sleep(50)

    def lambda_7138():
        OP_95(0xFE, 17110, 0, -2950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7138)
    Sleep(50)

    def lambda_7155():
        OP_95(0xFE, 16910, 0, -5250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7155)
    Sleep(50)

    def lambda_7172():
        OP_95(0xFE, 16309, 0, -4250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7172)
    WaitChrThread(0x1A3, 1)
    SetChrChipByIndex(0x1A3, 0xFF)
    SetChrSubChip(0x1A3, 0x0)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    #C0247
    ChrTalk(
        0x104,
        "#6P#00306F被它跑掉了呢。\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x1A3,
        "#5P#04602F去抓住它不就好了嘛。\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#12P#00000F嗯，赶快追上去！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0x155, 4)
    OP_29(0x74, 0x1, 0x5)
    OP_D7(0x1E)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32280, 0, -4370, 270)
    BeginChrThread(0x9, 0, 0, 1)
    ModifyEventFlags(1, 3, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 17810, 0, -4050, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_38_6DB8 end

    def Function_39_725B(): pass

    label("Function_39_725B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(16970, 2000, -2590, 0)
    MoveCamera(35, 22, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17050, 0)
    SetChrPos(0x101, 16600, 0, -3190, 0)
    SetChrPos(0x103, 16400, 0, -4390, 0)
    SetChrPos(0x104, 17590, 0, -5410, 0)
    SetChrPos(0x102, 18770, 0, -3140, 0)
    SetChrPos(0x109, 18940, 0, -4580, 0)
    SetChrPos(0x105, 17570, 0, -3990, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x9, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0250
    ChrTalk(
        0x101,
        (
            "#00005F那个……\x01",
            "配送地址就是\x01",
            "这里没错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        "#00103F嗯，是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0252
    ChrTalk(
        0x104,
        (
            "#00303F……可完全不像是\x01",
            "有人居住的样子呢。\x02\x03",

            "#00301F看来还是有什么地方\x01",
            "搞错了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x109,
        (
            "#10105F莫非是写错了地址，\x01",
            "实际上应该送到\x01",
            "附近的住宅……？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00001F可是……\x01",
            "这张送货单上只写着地址，\x01",
            "并没有填写收货人的姓名。\x02\x03",

            "#00003F我们根本不知\x01",
            "该从何找起啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0255
    ChrTalk(
        0x101,
        "#00005F……怎么了，缇欧？\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x103,
        "#00205F啊，没什么……\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x105,
        "#10305F哎，莫非……\x02",
    )

    CloseMessageWindow()

    def lambda_757B():
        OP_95(0xFE, 17650, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_757B)
    Sleep(300)

    def lambda_7598():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7598)
    Sleep(100)

    def lambda_75A8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_75A8)
    OP_0D()
    WaitChrThread(0x105, 1)
    Sleep(700)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0x0)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    Sound(114, 0, 100, 0)
    OP_79(0x5)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0258
    ChrTalk(
        0x101,
        "#00005F门没锁……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0259
    ChrTalk(
        0x105,
        (
            "#10304F无意中发现有道门缝，\x01",
            "没想到……\x02\x03",

            "#10300F好，那就先进去问问\x01",
            "这所房屋的主人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        "#00003F说、说的对……\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        "#00205F（……………………？）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32280, 0, -4370, 270)
    BeginChrThread(0x9, 0, 0, 1)
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x176, 1)
    OP_29(0x85, 0x1, 0x4)
    SetChrPos(0x0, 17650, 0, -2000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_39_725B end

    def Function_40_7774(): pass

    label("Function_40_7774")

    EventBegin(0x1)

    #C0262
    ChrTalk(
        0x1A3,
        (
            "#04605F哎，为什么要回去？\x01",
            "要找的房子不就在眼前吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x101,
        (
            "#00000F哦，我们这就进去。\x02\x03",

            "#00006F（……果然如兰迪所言，\x01",
            "  无论和她说什么都没用呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -5250, -1550, -11110, 180)
    EventEnd(0x4)
    Return()

    # Function_40_7774 end

    def Function_41_781D(): pass

    label("Function_41_781D")

    EventBegin(0x1)

    #C0264
    ChrTalk(
        0x1A3,
        (
            "#04600F真是的，你在干什么，\x01",
            "赶快去追玛丽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#00000F嗯，赶快去欢乐街吧。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 6340, 0, -5780, 90)
    EventEnd(0x4)
    Return()

    # Function_41_781D end

    def Function_42_7886(): pass

    label("Function_42_7886")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_42_7886 end

    SaveToFile()

Try(main)
