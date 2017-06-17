from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "レイズ老人",             # 1
        "ペントス",               # 2
        "ユーリ",                 # 3
        "サイクス",               # 4
        "レジー",                 # 5
        "ＯＬ",                   # 6
        "レクター書記官",         # 7
        "ハロルド",               # 8
        "フェリック",             # 9
        "リース",                 # 10
        "車",                     # 11
        "暴走車",                 # 12
        "ホステス（Ａ）",         # 13
        "ホステス（Ｂ）",         # 14
        "マリー",                 # 15
        "SE制御",                 # 16
        "bc0300",                 # 17
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

    ATBonus("ATBonus_7F4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_86A1", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_8C4", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0300", "Sepith_86A1", 60, 30, 10, 0,
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

    PlaceName(167.6699981689453, 0.0, -124.73999786376953, 0x0000, 0x0000, "中央広場")
    PlaceName(61.15999984741211, 0.0, -117.44999694824219, 0x0000, 0x0000, "西通り")
    PlaceName(211.41000366210938, 0.0, 19.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-37.66999816894531, 0.0, 3.240000009536743, 0x0000, 0x0000, "住宅街")
    PlaceName(80.5999984741211, 0.0, -9.720000267028809, 0x0000, 0x0000, "歓楽街")
    PlaceName(299.29998779296875, 0.0, -162.0, 0x0000, 0x0000, "東通り")
    PlaceName(356.80999755859375, 0.0, -251.10000610351562, 0x0000, 0x0000, "旧市街")
    PlaceName(344.6600036621094, 0.0, -55.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(302.5400085449219, 0.0, 97.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(185.89999389648438, 0.0, -236.52000427246094, 0x0000, 0x0000, "駅前通り")
    PlaceName(109.76000213623047, 0.0, -68.04000091552734, 0x0000, 0x0000, "裏通り")
    PlaceName(181.0399932861328, 0.0, -286.739990234375, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(386.7799987792969, 0.0, -139.32000732421875, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-21.469999313354492, 0.0, -119.87999725341797, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-11.75, 0.0, 42.119998931884766, 0x0000, 0x0000, "マインツ山道")
    PlaceName(200.0, 0.0, 231.5, 0x0000, 0x0000, "オルキスタワー")
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
        "Function_6_182C",         # 06, 6
        "Function_7_24A4",         # 07, 7
        "Function_8_34A5",         # 08, 8
        "Function_9_35B1",         # 09, 9
        "Function_10_3636",        # 0A, 10
        "Function_11_377D",        # 0B, 11
        "Function_12_387D",        # 0C, 12
        "Function_13_3D5D",        # 0D, 13
        "Function_14_3EAB",        # 0E, 14
        "Function_15_47C7",        # 0F, 15
        "Function_16_4AC2",        # 10, 16
        "Function_17_4F3F",        # 11, 17
        "Function_18_4FA4",        # 12, 18
        "Function_19_4FD9",        # 13, 19
        "Function_20_50AD",        # 14, 20
        "Function_21_5239",        # 15, 21
        "Function_22_5282",        # 16, 22
        "Function_23_52AE",        # 17, 23
        "Function_24_52C4",        # 18, 24
        "Function_25_6324",        # 19, 25
        "Function_26_6395",        # 1A, 26
        "Function_27_63AB",        # 1B, 27
        "Function_28_6663",        # 1C, 28
        "Function_29_69FF",        # 1D, 29
        "Function_30_6F74",        # 1E, 30
        "Function_31_751E",        # 1F, 31
        "Function_32_7910",        # 20, 32
        "Function_33_795B",        # 21, 33
        "Function_34_79A6",        # 22, 34
        "Function_35_79F1",        # 23, 35
        "Function_36_7A3C",        # 24, 36
        "Function_37_7A87",        # 25, 37
        "Function_38_7ABE",        # 26, 38
        "Function_39_7F83",        # 27, 39
        "Function_40_850A",        # 28, 40
        "Function_41_85CD",        # 29, 41
        "Function_42_8642",        # 2A, 42
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11ED")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DB")
    Sound(14, 0, 100, 0)
    OP_74(0xF, 0x1E)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5DE, 1)"), scpexpr(EXPR_END)), "loc_1764")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5DE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_17D6")

    label("loc_1764")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5DE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5DE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17D6")

    Jump("loc_1820")

    label("loc_17DB")

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

    label("loc_1820")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16DB end

    def Function_6_182C(): pass

    label("Function_6_182C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_19D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192F")

    #C0004
    ChrTalk(
        0xFE,
        (
            "そこの屋敷に住んでいた\x01",
            "《ハイブラッズ》とかいう\x01",
            "３人組の若者じゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "結界が無くなったと知るや、\x01",
            "さっさと故郷の共和国の方に\x01",
            "向かっていったようじゃの。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "前と違って車も無いようじゃし、\x01",
            "どうするつもりなのかのう……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19D0")

    label("loc_192F")


    #C0007
    ChrTalk(
        0xFE,
        (
            "そこの屋敷に住んでいた若者たちは、\x01",
            "さっさと故郷の共和国の方に\x01",
            "向かっていったようじゃの。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "前と違って車も無いようじゃし、\x01",
            "どうするつもりなのかのう……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D0")

    Jump("loc_24A0")

    label("loc_19D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19E3")
    Jump("loc_24A0")

    label("loc_19E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFA")

    #C0009
    ChrTalk(
        0xFE,
        (
            "ディーター殿の演説を聴いて、\x01",
            "４、５年前に起こった導力車の\x01",
            "爆発事故を思い出したわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "当時は事故だと報じられたが、\x01",
            "もしあれが帝国と共和国の\x01",
            "『暗闘』の結果じゃったならば……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "むう……\x01",
            "クロスベルには相当な闇が\x01",
            "潜んでいたと言えるじゃろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B98")

    label("loc_1AFA")


    #C0012
    ChrTalk(
        0xFE,
        (
            "４、５年前に起こった爆発事故……\x01",
            "あの時の被害者は、\x01",
            "確か小さな女の子じゃったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "むう……\x01",
            "クロスベルには相当な闇が\x01",
            "潜んでいたと言えるじゃろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B98")

    Jump("loc_24A0")

    label("loc_1B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C19")

    #C0014
    ChrTalk(
        0xFE,
        (
            "この間の襲撃事件は、\x01",
            "ひどいもんじゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "あれ以来、夜が恐ろしゅうてな。\x01",
            "ろくに眠れやせんのじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A0")

    label("loc_1C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C7A")

    #C0016
    ChrTalk(
        0xFE,
        (
            "しかし、占領事件とは\x01",
            "穏やかでないのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "一体何者の仕業なのじゃろうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24A0")

    label("loc_1C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C88")
    Jump("loc_24A0")

    label("loc_1C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF4")

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
            "はっ……\x01",
            "何かあったのかのう？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_1D41")

    label("loc_1CF4")


    #C0020
    ChrTalk(
        0xFE,
        (
            "ああ、すっかり\x01",
            "眠ってしまっておったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "……何かあったのかのう？\x02",
    )

    CloseMessageWindow()

    label("loc_1D41")

    Jump("loc_24A0")

    label("loc_1D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1DA7")

    #C0022
    ChrTalk(
        0xFE,
        (
            "ふあああ……\x01",
            "如何ともしがたい眠気じゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "このまま眠ってしまうかのう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24A0")

    label("loc_1DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E65")

    #C0024
    ChrTalk(
        0xFE,
        (
            "例の住民投票の日が\x01",
            "近づいてきたのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "若い世代のこれからの為にも\x01",
            "軽い気持ちで望むわけにはいかん。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "当日までじっくりと\x01",
            "自分の考えを纏めておかねばな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EE6")

    label("loc_1E65")


    #C0027
    ChrTalk(
        0xFE,
        (
            "独立の是非は、\x01",
            "若い世代のためにも\x01",
            "真剣に考えねばならんじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "投票日まで、じっくりと\x01",
            "自分の考えを纏めておかねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE6")

    Jump("loc_24A0")

    label("loc_1EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_200C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA7")

    #C0029
    ChrTalk(
        0xFE,
        (
            "先ほど、大聖堂のほうに\x01",
            "導力車が向かって行ったぞい。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "確かあれは、首脳たちの\x01",
            "送迎に使われとった\x01",
            "リムジンのようじゃったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "はて、見間違いかのう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2007")

    label("loc_1FA7")


    #C0032
    ChrTalk(
        0xFE,
        (
            "先ほど、大聖堂のほうに\x01",
            "リムジンが向かって\x01",
            "行ったようじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "はて、見間違いかのう。\x02",
    )

    CloseMessageWindow()

    label("loc_2007")

    Jump("loc_24A0")

    label("loc_200C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2070")

    #C0034
    ChrTalk(
        0xFE,
        (
            "おお、だいぶ暗くなって\x01",
            "しもうたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "わしもそろそろ\x01",
            "家路につくとするかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A0")

    label("loc_2070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_216B")

    #C0036
    ChrTalk(
        0xFE,
        (
            "そういえば、最近は\x01",
            "ピザの配達人をあまり見かけんのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "以前は毎日と言っていいほど\x01",
            "この辺りで見かけたもんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#00003F（多分、ヨナが頼んでたヤツだな……）\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#00100F（今は確かレマン自治州にいるのよね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21F4")

    label("loc_216B")


    #C0040
    ChrTalk(
        0xFE,
        (
            "以前はこのあたりに、\x01",
            "毎日といっていいほど\x01",
            "ピザの配達人が来ておった。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "ほほ、よほどピザが好きなもんが\x01",
            "住んでおったんじゃろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F4")

    Jump("loc_24A0")

    label("loc_21F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2379")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F7")

    #C0042
    ChrTalk(
        0xFE,
        (
            "最近そこの家に越してきた\x01",
            "若者たちに挨拶したんじゃが、\x01",
            "無視されてしまったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "それどころか犬を見るような目で\x01",
            "わしを見下して、鼻で笑いおった……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "うむむ……\x01",
            "前に住んでいた家族の方が\x01",
            "よっぽど愛想がよかったがのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2374")

    label("loc_22F7")


    #C0045
    ChrTalk(
        0xFE,
        (
            "聞けば、そこに越してきた連中は\x01",
            "たいそうな会社の\x01",
            "役員の息子という話じゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "うむむ……\x01",
            "鼻持ちならん連中じゃわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2374")

    Jump("loc_24A0")

    label("loc_2379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2387")
    Jump("loc_24A0")

    label("loc_2387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_24A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23E5")

    #C0047
    ChrTalk(
        0xFE,
        (
            "やれやれ、またあの若者たちか……\x01",
            "うるさくてかなわんわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A0")

    label("loc_23E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2454")

    #C0048
    ChrTalk(
        0xFE,
        "う～む、なんという心地よい陽気じゃ。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "ついつい欠伸がでてしまうのう。\x01",
            "ふぁ～ああ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24A0")

    label("loc_2454")


    #C0050
    ChrTalk(
        0xFE,
        "やはりこの辺りは静かでええのう。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "日向ぼっこにはちょうどええわい。\x02",
    )

    CloseMessageWindow()

    label("loc_24A0")

    TalkEnd(0xFE)
    Return()

    # Function_6_182C end

    def Function_7_24A4(): pass

    label("Function_7_24A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2595")

    #C0052
    ChrTalk(
        0xFE,
        "ディーター大統領が拘束されたそうだな。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "私は彼を支持していたのだが……\x01",
            "彼のやり方は強引な部分も多かった。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "やはり、悪事を働くとどこかで\x01",
            "揺れ戻しがあるのが世の常というもの。\x01",
            "私も気をつけなければな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_261C")

    label("loc_2595")


    #C0055
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "あの青白く光る大樹は、\x01",
            "一体どういうことなのだろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "大統領もいない今、\x01",
            "あれの対処は誰がやってくれるんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_261C")

    Jump("loc_34A1")

    label("loc_2621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_262F")
    Jump("loc_34A1")

    label("loc_262F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_279B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2705")

    #C0057
    ChrTalk(
        0xFE,
        (
            "《クロスベル独立国》……\x01",
            "いまいち実感が湧いてこないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "もしこのまま実現すれば、\x01",
            "クロスベルにとっては大きな前進だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "私はディーター大統領を\x01",
            "強く支持していくことにするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2796")

    label("loc_2705")


    #C0060
    ChrTalk(
        0xFE,
        (
            "私はディーター大統領を\x01",
            "強く支持していくことにするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "もしこのまま独立が実現すれば、\x01",
            "クロスベルにとって\x01",
            "大きな前進になるだろうからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2796")

    Jump("loc_34A1")

    label("loc_279B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_28F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286C")

    #C0062
    ChrTalk(
        0xFE,
        (
            "イリアが倒れたことで\x01",
            "アルカンシェルも休業状態……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "復旧活動は進んではいるが、\x01",
            "我々市民の心には\x01",
            "どこか影が差している。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "ひとつでも明るいニュースが\x01",
            "あればいいのだがな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28EB")

    label("loc_286C")


    #C0065
    ChrTalk(
        0xFE,
        (
            "復旧活動は進んではいるが、\x01",
            "我々市民の心には\x01",
            "どこか影が差している。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "ひとつでも明るいニュースが\x01",
            "あればいいのだがな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EB")

    Jump("loc_34A1")

    label("loc_28F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C9")

    #C0067
    ChrTalk(
        0xFE,
        (
            "マインツ山道では、\x01",
            "今も警備隊と武装集団が\x01",
            "交戦しているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "あの警備隊が一晩経っても\x01",
            "まだ解決できないところを見ると……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "むむむ、かなり厄介な相手なのは\x01",
            "間違いなさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A68")

    label("loc_29C9")


    #C0070
    ChrTalk(
        0xFE,
        (
            "警備隊は戦闘のプロフェッショナルだ。\x01",
            "そんな彼らが、いまだに事件を\x01",
            "解決できないところを見ると……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "むむむ、かなり厄介な相手なのは\x01",
            "間違いなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A68")

    Jump("loc_34A1")

    label("loc_2A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A7B")
    Jump("loc_34A1")

    label("loc_2A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2B4B")

    #C0072
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの公演……\x01",
            "噂では、シュリとかいう新人に\x01",
            "追加シーンを任せるつもりらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "かつて新人だったリーシャ・マオが\x01",
            "あれほどの活躍をみせているのだ……\x01",
            "どうしても期待してしまうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A1")

    label("loc_2B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2BDA")

    #C0074
    ChrTalk(
        0xFE,
        (
            "アルカンシェル公演まで\x01",
            "残すところあと２日か……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "首尾よくＡ席チケットも\x01",
            "確保できたことだし、\x01",
            "楽しみにしていなければな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A1")

    label("loc_2BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CBF")

    #C0076
    ChrTalk(
        0xFE,
        (
            "国家としての独立……\x01",
            "あまりに難しい事だと私は思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "宗主国である帝国や共和国が\x01",
            "認めるとはとても思えないのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "市長の考えは分かるが……\x01",
            "あまりに無謀な提案だと\x01",
            "言わざるをえないだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D5B")

    label("loc_2CBF")


    #C0079
    ChrTalk(
        0xFE,
        (
            "宗主国である帝国や共和国が\x01",
            "クロスベルの独立などを\x01",
            "認めるとは思えない。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "市長の考えは分かるが……\x01",
            "あまりに無謀な提案だと\x01",
            "言わざるをえないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5B")

    Jump("loc_34A1")

    label("loc_2D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E44")

    #C0081
    ChrTalk(
        0xFE,
        (
            "オルキスタワー内の\x01",
            "テナントスペースには、\x01",
            "私の参加している事業もあってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "それらは通商会議終了後に\x01",
            "運営が始まる予定なのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "果たして、\x01",
            "どの程度の成果をあげるか……\x01",
            "楽しみでならないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EDC")

    label("loc_2E44")


    #C0084
    ChrTalk(
        0xFE,
        (
            "オルキスタワー内の\x01",
            "テナントスペースには、\x01",
            "私の参加している事業もあってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "通商会議終了後に\x01",
            "どの程度の成果をあげるか……\x01",
            "楽しみでならないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EDC")

    Jump("loc_34A1")

    label("loc_2EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_301B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F91")

    #C0086
    ChrTalk(
        0xFE,
        (
            "あの屋敷から\x01",
            "女の子の声のようなものが\x01",
            "聞こえた気がするのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "はて、この屋敷には\x01",
            "誰も住んでいないはずだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "ふむ、まあ空耳だろうな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3016")

    label("loc_2F91")


    #C0089
    ChrTalk(
        0xFE,
        (
            "そういえば１０年ほど前に、\x01",
            "この屋敷にオバケが出るとか\x01",
            "言われていたことがあったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "まあ、愚にも付かない\x01",
            "ただの噂話だがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3016")

    Jump("loc_34A1")

    label("loc_301B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3159")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E4")

    #C0091
    ChrTalk(
        0xFE,
        (
            "ついにオルキスタワーが\x01",
            "そのヴェールを脱いだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "しかしまさか、\x01",
            "あそこまでの建造物を\x01",
            "見せ付けられるとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "うむ、今後の発展に\x01",
            "大いに期待せざるをえないだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3154")

    label("loc_30E4")


    #C0094
    ChrTalk(
        0xFE,
        (
            "オルキスタワー……\x01",
            "あそこまでの建造物だったとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "うむ、今後の発展に\x01",
            "大いに期待せざるをえないだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3154")

    Jump("loc_34A1")

    label("loc_3159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323B")

    #C0096
    ChrTalk(
        0xFE,
        (
            "そういえば、アルカンシェルの\x01",
            "次の公演の情報が出ていたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "なにやら《金の太陽、銀の月》の\x01",
            "リニューアル版をやるということだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "ふむ、チケットは急ぎ\x01",
            "確保しておいたほうがよさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32CC")

    label("loc_323B")


    #C0099
    ChrTalk(
        0xFE,
        (
            "《金の太陽、銀の月》の\x01",
            "リニューアル版は、果たして\x01",
            "どのような出来になるのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "ふむ、チケットは急いで\x01",
            "確保しておいたほうがよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32CC")

    Jump("loc_34A1")

    label("loc_32D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_32DF")
    Jump("loc_34A1")

    label("loc_32DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_337A")

    #C0101
    ChrTalk(
        0xFE,
        (
            "最近、やたら乱暴な運転をする\x01",
            "導力車を見かけるのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "まったく……事故でも起こしたら\x01",
            "どうするつもりなのだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A1")

    label("loc_337A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3429")

    #C0103
    ChrTalk(
        0xFE,
        (
            "先日、ようやく新市庁ビルが\x01",
            "完成したようなのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "着工からかなりの期間が\x01",
            "経ってしまったようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "いやはや、月末の除幕式が\x01",
            "楽しみでならんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34A1")

    label("loc_3429")


    #C0106
    ChrTalk(
        0xFE,
        (
            "新市庁ビルには、私も事業家として\x01",
            "一部の事業計画に参加していてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "いやはや、月末の除幕式が\x01",
            "楽しみでならんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A1")

    TalkEnd(0xFE)
    Return()

    # Function_7_24A4 end

    def Function_8_34A5(): pass

    label("Function_8_34A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3565")
    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0108
    ChrTalk(
        0xFE,
        (
            "クク、この導力車を\x01",
            "ここまで乗りこなせるのは\x01",
            "お前くらいのものだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "レジー、次も\x01",
            "楽しいドライブを頼むぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xC,
        "へへっ、任せとけっつーの。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_35AD")

    label("loc_3565")


    #C0111
    ChrTalk(
        0xFE,
        (
            "フフ、この導力車を\x01",
            "ここまで乗りこなせるのは\x01",
            "お前くらいのものだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AD")

    TalkEnd(0xFE)
    Return()

    # Function_8_34A5 end

    def Function_9_35B1(): pass

    label("Function_9_35B1")

    TalkBegin(0xFE)

    #C0112
    ChrTalk(
        0xFE,
        (
            "レジーはこう見えて、\x01",
            "導力車の運転が超上手いんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "やっぱ、親父がヴェルヌ社の\x01",
            "導力車開発部の一員だからかねえ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_35B1 end

    def Function_10_3636(): pass

    label("Function_10_3636")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F5")
    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0114
    ChrTalk(
        0xFE,
        (
            "いやー、やっぱり\x01",
            "街道をかっ飛ばすのは\x01",
            "サイコーだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        (
            "へへ、街の中と違って\x01",
            "余計な障害物もねえしなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        "フフ、次も頼むぞレジー。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 4)
    Jump("loc_3779")

    label("loc_36F5")


    #C0117
    ChrTalk(
        0xFE,
        (
            "いやー、やっぱり\x01",
            "街道をかっ飛ばすのは\x01",
            "サイコーだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "これからもガンガン\x01",
            "チューンナップをかけて\x01",
            "スピードを追及しねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3779")

    TalkEnd(0xFE)
    Return()

    # Function_10_3636 end

    def Function_11_377D(): pass

    label("Function_11_377D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_380C")

    #C0119
    ChrTalk(
        0xFE,
        (
            "うぅ、雨のせいかどうかは\x01",
            "分かりませんが、今日はお化粧の\x01",
            "ノリがいまいちですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        "ああ、直したくてたまりません……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3879")

    label("loc_380C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3879")

    #C0121
    ChrTalk(
        0xFE,
        (
            "さてと……\x01",
            "今日もお仕事に行きませんと。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "ふぅ、ですが雨の日は\x01",
            "どうにも出勤が億劫ですわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3879")

    TalkEnd(0xFE)
    Return()

    # Function_11_377D end

    def Function_12_387D(): pass

    label("Function_12_387D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF8")

    #C0123
    ChrTalk(
        0x101,
        (
            "#00005Fあれ、ハロルドさん……\x01",
            "もしかしてどこかに\x01",
            "お出かけになるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xF,
        (
            "#03600Fええ、少し前に\x01",
            "アルモリカ村から招待を受けまして。\x02\x03",

            "#03604Fイアン先生の勧めもあったので、\x01",
            "家族みんなでしばらく\x01",
            "滞在するつもりでしたが……\x02\x03",

            "#03608Fまさか出発の朝に、クロスベルが\x01",
            "こんな大変なことになってしまうとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        "#00103F……私たちも、動揺している所です。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#00300Fでもまあ、せっかくの招待なんだし\x01",
            "行った方がいいんじゃないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x103,
        (
            "#00200Fそうですね……ハロルドさんも\x01",
            "久しぶりの休暇みたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xF,
        (
            "#03603Fいえ……\x01",
            "ソフィアとコリンを村に届けたら\x01",
            "一旦私だけ街に戻ってくるつもりです。\x02\x03",

            "#03600F取引でお世話になっている人たちにも\x01",
            "かなり混乱が出ているようですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00003Fそうですか……\x02\x03",

            "#00001F正直、何が起こってもおかしくは\x01",
            "ない状態だと思います。\x02\x03",

            "街道への移動も\x01",
            "十分に気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xF,
        (
            "#03600Fはは……ありがとうございます。\x01",
            "みなさんもどうかお気をつけて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 0)
    Jump("loc_3D59")

    label("loc_3BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CDE")

    #C0131
    ChrTalk(
        0xF,
        (
            "#03600Fソフィアとコリンを村に届けたら\x01",
            "一旦私だけ街に戻ってくるつもりです。\x02\x03",

            "#03603F楽しみにしてくれた\x01",
            "コリンたちには悪いですが……\x01",
            "かなり混乱が出ているようですし。\x02\x03",

            "#03600F……みなさんもどうかお気をつけて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3D59")

    label("loc_3CDE")


    #C0132
    ChrTalk(
        0xF,
        (
            "#03603Fソフィアとコリンを村に届けたら\x01",
            "私だけ一旦街に戻ってくるつもりです。\x02\x03",

            "#03600F……みなさんもどうかお気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D59")

    TalkEnd(0xFE)
    Return()

    # Function_12_387D end

    def Function_13_3D5D(): pass

    label("Function_13_3D5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E1E")

    #C0133
    ChrTalk(
        0xFE,
        (
            "今日は久しぶりに家族そろって\x01",
            "夕食をとることになったから、\x01",
            "これから買い物に行くんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "あのバカでかい樹が\x01",
            "イヤでも目に入ってきてさ、\x01",
            "どうも不安になっちまうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3EA7")

    label("loc_3E1E")


    #C0135
    ChrTalk(
        0xFE,
        (
            "……こういうときこそ、\x01",
            "婆ちゃんの言うとおり\x01",
            "平常心でいかないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "あんなバカでかい樹がなんだ！\x01",
            "口笛でも吹いてりゃ怖くねえさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EA7")

    TalkEnd(0xFE)
    Return()

    # Function_13_3D5D end

    def Function_14_3EAB(): pass

    label("Function_14_3EAB")

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
            "#11504F#11Pフンフフ～ン……\x02\x03",

            "#11505F……おっ、魚影発見！\x01",
            "近頃は新種もいるっていうのは\x01",
            "本当だったみたいだなァ。\x02\x03",

            "#11509Fやれやれ、こんなことなら\x01",
            "釣り竿を持ってきておけばよかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#00001F#5Pレクターさん……\x01",
            "こんな所で何をやってるんですか？\x02",
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
            "おおっと、竿もないのに\x01",
            "獲物がかかったみてえだぜェ。\x02\x03",

            "２本ずつ手足が生えた獲物が５匹……\x01",
            "ま、釣果としちゃ上出来か。\x02",
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
        "#10105F#5Pなっ……！\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        (
            "#00301F#5P俺たちが釣られてここに来た、\x01",
            "とでも言いたげだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "#11509F#11Pハハ、そう言ってる\x01",
            "つもりなんだけどなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#00003F#5P（……この人のペースに\x01",
            "  乗せられちゃダメだ。）\x02\x03",

            "#00001F……レクターさん、\x01",
            "質問を変えさせていただきます。\x02\x03",

            "『赤い星座』をクロスベル入りさせた\x01",
            "帝国軍情報局の人間である貴方が、\x01",
            "こんな所で何をやってるんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0144
    ChrTalk(
        0xFE,
        "#11509F#11Pハハ、言うようになったな。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x105,
        (
            "#10302F#5Pフフ、まあ貴方に対しては\x01",
            "このくらいストレートなくらいが\x01",
            "丁度いいんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 500)

    #C0146
    ChrTalk(
        0xFE,
        (
            "#11504F#12Pはは、まあいいか。\x01",
            "質問に答えてやるよ。\x02\x03",

            "#11500Fここに来たのは見ての通りの\x01",
            "息抜きってとこだ。\x02\x03",

            "#11506Fいくら俺でも、あのオッサンの\x01",
            "お守りばかりじゃ気疲れしちまうからな。\x02",
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
            "#00005F#5Pオ、オッサンって……\x01",
            "オズボーン宰相閣下のことですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        (
            "#00101F#5P気になっていたんですが……\x01",
            "やっぱり貴方は宰相閣下の側近か何かと\x01",
            "考えていいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "#11502F#4Pクク、さあなァ。\x01",
            "少なくともそんな大層なモンを\x01",
            "名乗った覚えは一度だってないな。\x02\x03",

            "#11504F……さーて、\x01",
            "そろそろ休憩時間も終わりだし\x01",
            "オッサンのとこに戻るとすっか。\x02\x03",

            "#11500Fそんじゃあな、\x01",
            "せいぜいお仕事がんばってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x109,
        "#10105F#5Pあ、あの……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x2D, 0x1F4)

    def lambda_469F():

        label("loc_469F")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_469F")

    QueueWorkItem2(0x101, 2, lambda_469F)

    def lambda_46B1():

        label("loc_46B1")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_46B1")

    QueueWorkItem2(0x102, 2, lambda_46B1)

    def lambda_46C3():

        label("loc_46C3")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_46C3")

    QueueWorkItem2(0x104, 2, lambda_46C3)

    def lambda_46D5():

        label("loc_46D5")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_46D5")

    QueueWorkItem2(0x109, 2, lambda_46D5)

    def lambda_46E7():

        label("loc_46E7")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_46E7")

    QueueWorkItem2(0x105, 2, lambda_46E7)
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
            "#00306F#5Pやれやれ、\x01",
            "はぐらかされちまったな……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_END)), "loc_4782")
    Call(0, 15)

    label("loc_4782")

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

    # Function_14_3EAB end

    def Function_15_47C7(): pass

    label("Function_15_47C7")

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
            "#00003F#6Pレクターさん、キリカさん……\x02\x03",

            "帝国と共和国の諜報員が、\x01",
            "似たようなタイミングで\x01",
            "市内に出てきていた。\x02\x03",

            "#00001F……みんな、どう思う？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_48A3():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_48A3)
    Sleep(50)

    def lambda_48B3():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_48B3)
    Sleep(50)

    def lambda_48C3():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_48C3)
    Sleep(50)

    def lambda_48D3():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_48D3)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0153
    ChrTalk(
        0x109,
        "#10103F#6P……なんだかキナ臭いですね。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x105,
        (
            "#10302F#6Pフフ、だったらこのまま\x01",
            "彼らを追跡してみるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        (
            "#00108F#6Pそれも難しいんじゃないかしら。\x02\x03",

            "#00103Fどちらも、私たちが辿り着くのは\x01",
            "分かっていたような雰囲気だったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#00003F#6P……ダドリーさんたちに\x01",
            "報告しに行ってみないか？\x02\x03",

            "#00000F捜査一課の情報と合わせれば\x01",
            "何か分かるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x109,
        "#10105F#6Pあ……よさそうですね。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x104,
        (
            "#00300F#6Pよっしゃ、そうと決まれば\x01",
            "警察本部に行ってみるとすっか。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA3, 0x1, 0xC)
    Return()

    # Function_15_47C7 end

    def Function_16_4AC2(): pass

    label("Function_16_4AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 6)), scpexpr(EXPR_END)), "loc_4B1F")
    EventBegin(0x2)
    ClearMapFlags(0x20)

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "共和国派・キャンベル議員の邸宅だ。\x01",
            "特に訪ねる用事はない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Jump("loc_4F3E")

    label("loc_4B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E8B")
    TalkBegin(0xFF)

    #C0160
    ChrTalk(
        0x101,
        "#00005Fここは確か……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#00100F共和国派議員をまとめている\x01",
            "キャンベル議員の屋敷ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        (
            "#10105F確か、例の教団に\x01",
            "関係していた議員たちは\x01",
            "失脚したという話でしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x102,
        (
            "#00103Fええ、キャンベル議員には\x01",
            "そういった繋がりは\x01",
            "確認されなかったみたい。\x02\x03",

            "#00100F《黒月》と関わりはあるみたい\x01",
            "だけれど、今のところは\x01",
            "違法なものではないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、キナ臭い人物であることは\x01",
            "間違いないってわけだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4E0B")

    #C0165
    ChrTalk(
        0x101,
        (
            "#00000Fそういえば、エリィは確か\x01",
            "キャンベル議員の娘さんと\x01",
            "知り合いだったな？\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#00100Fカーラさんのことね。\x01",
            "うん、日曜学校が同じだったの。\x02\x03",

            "#00104Fそういう意味では、彼女のお父様が\x01",
            "教団と繋がっていなかった事には\x01",
            "本当に安心したわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x109,
        (
            "#10108Fそうですね……\x01",
            "知人の父親がそんな人だなんて\x01",
            "あまり考えたくないですし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E0B")


    #C0168
    ChrTalk(
        0x101,
        (
            "#00000Fまあ、とにかく……\x01",
            "今は用事もないし訪ねるのは\x01",
            "やめておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x102,
        (
            "#00100Fええ、そうね。\x01",
            "行きましょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 6)
    TalkEnd(0xFF)
    Jump("loc_4F3E")

    label("loc_4E8B")

    TalkBegin(0xFF)

    #C0170
    ChrTalk(
        0x101,
        (
            "#00000Fここは確か……\x01",
            "共和国派議員をまとめている\x01",
            "キャンベル議員の屋敷だったな。\x02\x03",

            "今は用事もないし訪ねるのは\x01",
            "やめておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#00100Fええ、そうね。\x01",
            "行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 6)
    TalkEnd(0xFF)

    label("loc_4F3E")

    Return()

    # Function_16_4AC2 end

    def Function_17_4F3F(): pass

    label("Function_17_4F3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F6D")
    Call(0, 39)
    Return()

    label("loc_4F6D")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_17_4F3F end

    def Function_18_4FA4(): pass

    label("Function_18_4FA4")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_18_4FA4 end

    def Function_19_4FD9(): pass

    label("Function_19_4FD9")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0174
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50A8")
    OP_E2(0x2)
    MiniGame(0x6, 0x2, 0xFFFFEAA2, 0xFFFFE890, 0xFFFF5DB2, 0x10E, 0xFFFFD90E, 0xFFFFE69C, 0xFFFF5C36)

    label("loc_50A8")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_19_4FD9 end

    def Function_20_50AD(): pass

    label("Function_20_50AD")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51B8")
    SetChrFlags(0x9, 0x8000)
    EndChrThread(0x9, 0xFF)
    SetChrPos(0x9, -5000, 0, -5000, 180)

    def lambda_51A8():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_51A8)

    label("loc_51B8")

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

    # Function_20_50AD end

    def Function_21_5239(): pass

    label("Function_21_5239")

    SetChrPos(0xFE, 25550, 0, -4600, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -6000, 0, -4600)
    OP_9F(0x1, -15000, 0, -3100)
    OP_9F(0x1, -16000, 0, 7900)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_21_5239 end

    def Function_22_5282(): pass

    label("Function_22_5282")

    Sleep(2000)
    OP_95(0xFE, 0, 0, -5600, 2000, 0x1)
    OP_95(0xFE, -14000, 0, -5600, 2000, 0x1)
    Return()

    # Function_22_5282 end

    def Function_23_52AE(): pass

    label("Function_23_52AE")

    Sound(468, 2, 100, 0)
    Sound(458, 0, 100, 0)
    Sleep(4500)
    Sound(494, 0, 70, 0)
    Return()

    # Function_23_52AE end

    def Function_24_52C4(): pass

    label("Function_24_52C4")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5568")
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

    def lambda_53F2():
        OP_97(0x101, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53F2)
    Sleep(50)

    def lambda_540F():
        OP_97(0x102, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_540F)
    Sleep(50)

    def lambda_542C():
        OP_97(0x109, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_542C)
    Sleep(50)

    def lambda_5449():
        OP_97(0x105, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5449)
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
        "#00005Fこの音は……？\x02",
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
    Jump("loc_5748")

    label("loc_5568")

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

    def lambda_561B():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_561B)
    Sleep(50)

    def lambda_5638():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5638)
    Sleep(50)

    def lambda_5655():
        OP_97(0x109, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5655)
    Sleep(50)

    def lambda_5672():
        OP_97(0x105, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5672)
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
        "#00005Fこの音は……？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-14390, 500, 10820, 0)
    MoveCamera(70, 35, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(23150, 0)
    OP_0D()

    label("loc_5748")

    OP_68(-13920, 500, -3320, 1000)
    MoveCamera(31, 31, 0, 1000)
    OP_6E(620, 1000)
    SetCameraDistance(20000, 1000)
    BeginChrThread(0x13, 1, 0, 25)
    BeginChrThread(0x17, 1, 0, 26)

    #N0178
    NpcTalk(
        0x12,
        "青年の声",
        "#10Aィヤッホーーーー！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_68(8360, 1450, -3280, 1500)
    MoveCamera(39, 29, 0, 1500)

    #N0179
    NpcTalk(
        0x12,
        "青年の声",
        "#5Aハハッ、最高だぜ！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)

    def lambda_57EF():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57EF)
    Sleep(50)

    def lambda_57FF():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57FF)
    Sleep(50)

    def lambda_580F():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_580F)
    Sleep(50)

    def lambda_581F():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_581F)
    OP_6F(0x79)
    OP_0D()
    Sleep(1500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_58C1")
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
    Jump("loc_59EE")

    label("loc_58C1")

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

    def lambda_593E():
        OP_95(0x102, 4970, 0, -5120, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_593E)
    Sleep(100)

    def lambda_595B():
        OP_95(0x101, 3840, 0, -3970, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_595B)
    Sleep(100)

    def lambda_5978():
        OP_95(0x109, 6070, 0, -3420, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5978)
    Sleep(100)

    def lambda_5995():
        OP_95(0x105, 7190, 0, -4250, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5995)
    WaitChrThread(0x109, 1)

    def lambda_59B3():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_59B3)
    WaitChrThread(0x105, 1)

    def lambda_59C4():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_59C4)
    WaitChrThread(0x101, 1)

    def lambda_59D5():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59D5)
    WaitChrThread(0x102, 1)

    def lambda_59E6():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_59E6)

    label("loc_59EE")


    #C0180
    ChrTalk(
        0x101,
        (
            "#00005Fい、今のは……？\x01",
            "滅茶苦茶スピードが\x01",
            "出てたみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x109,
        (
            "#10101F明らかにスピード違反ですね……\x02\x03",

            "あんな運転をしたら\x01",
            "導力車が可哀想ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#00101F危険運転をする導力車……\x01",
            "最近、市内でもよく\x01",
            "目撃されてるみたいね。\x02\x03",

            "#00103Fいろんなところで\x01",
            "迷惑をかけてるらしいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x105,
        "#10305Fふうん、なるほどね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(50)

    #C0184
    ChrTalk(
        0x105,
        (
            "#10300Fで、特務支援課としては\x01",
            "どうするべきなのかな？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B76():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B76)
    Sleep(50)

    def lambda_5B86():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B86)
    Sleep(50)

    def lambda_5B96():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B96)
    Sleep(50)

    #C0185
    ChrTalk(
        0x101,
        (
            "#00003Fもちろん、\x01",
            "見過ごすわけには\x01",
            "いかないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C69")
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
            "◆港湾区でケイト巡査と？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【話している】\x01",        # 0
            "【話していない】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 4)), scpexpr(EXPR_END)), "loc_5D1D")

    #C0187
    ChrTalk(
        0x101,
        (
            "#00004F確か、車が向かった\x01",
            "歓楽街のほうには\x01",
            "ケイト先輩がいたよな。\x02\x03",

            "#00000Fエニグマで連絡して\x01",
            "相談してみよう。\x02\x03",

            "こういった案件だったら\x01",
            "広域防犯課が適任のはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB8")

    label("loc_5D1D")


    #C0188
    ChrTalk(
        0x101,
        (
            "#00003F……広域防犯課の\x01",
            "ケイト先輩に\x01",
            "相談してみよう。\x02\x03",

            "#00000F先輩ならとっくに\x01",
            "対処に動いてるかも\x01",
            "しれないしな。\x02\x03",

            "エニグマで連絡して\x01",
            "相談してみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB8")

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
    SetChrName("ケイトの声")

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──はい、こちら\x01",
            "広域防犯課のケイト巡査です。\x02",
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
            "#00000Fケイト先輩、お疲れさまです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ケイトの声")

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、ロイド君。\x01",
            "何かあったのかしら？\x02",
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
            "#00003Fえっと、実は先輩に\x01",
            "相談したいことがあるんですが……\x02",
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
            "ロイドは先ほどの\x01",
            "暴走車の件について\x01",
            "一通り説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ケイトの声")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、ロイド君たちも\x01",
            "目撃したのね。\x02\x03",

            "そうね、せっかくだし……\x01",
            "協力してもらおうかな。\x02",
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
            "#00005F協力……ですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ケイトの声")

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もし時間があったら、\x01",
            "ちょっと私のところに\x01",
            "来てもらえるかしら？\x02\x03",

            "歓楽街のホテルのあたりで\x01",
            "待ってるわね。\x02",
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
            "#00000Fは、はい。\x01",
            "了解しました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ケイトの声")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それじゃ、また後でね。\x02",
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
        "#00100F……ケイトさんは何て？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#00000Fああ、なんだか俺たちに\x01",
            "協力して欲しいことがあるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x109,
        "#10105F広域防犯課と協力ですか？\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x105,
        (
            "#10309F力ずくで導力車を止めて！\x01",
            "……とか言われたりしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#00006Fさ、さすがにそんなの\x01",
            "危なすぎるだろ……\x02\x03",

            "#00000Fとにかく、歓楽街のホテルに\x01",
            "行ってみるとしよう。\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6310")
    SetChrPos(0x0, -320, 0, -25290, 0)
    Jump("loc_6321")

    label("loc_6310")

    SetChrPos(0x0, 3840, 0, -3970, 90)

    label("loc_6321")

    EventEnd(0x5)
    Return()

    # Function_24_52C4 end

    def Function_25_6324(): pass

    label("Function_25_6324")

    SetChrPos(0x13, -15860, 300, 20000, 180)
    OP_96(0xFE, 0xFFFFBD7A, 0x0, 0xFFFFF8B2, 0x4E20, 0x0)
    OP_9F(0x0, 0x13)
    OP_9F(0x1, -16800, 0, -2530)
    OP_9F(0x1, -14190, 0, -5130)
    OP_9F(0x1, -12700, 0, -5370)
    OP_9F(0x2, 0x13, 11000, 0x6)
    OP_96(0xFE, 0x767A, 0x0, 0xFFFFE85E, 0x4E20, 0x0)
    Return()

    # Function_25_6324 end

    def Function_26_6395(): pass

    label("Function_26_6395")

    Sound(486, 0, 100, 0)
    Sleep(1000)
    Sound(487, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Return()

    # Function_26_6395 end

    def Function_27_63AB(): pass

    label("Function_27_63AB")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6484")
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
            "#1K◆「暴走車の取り締まり」を？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",        # 0
            "【やっている】\x01",        # 1
            "【やっていない】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6470")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_6484")

    label("loc_6470")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6484")
    OP_29(0x69, 0x3, 0x10)

    label("loc_6484")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_653E")

    #C0205
    ChrTalk(
        0x101,
        (
            "#00005Fこれは……\x01",
            "昨日の不良青年たちが\x01",
            "乗り回していた導力車か。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        "#00105Fどうしてこんな所に……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x109,
        (
            "#10106F分かりませんが……\x01",
            "何だかイヤな予感がしますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_665F")

    label("loc_653E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65A6")

    #C0208
    ChrTalk(
        0x101,
        "#00006Fあの３人組の導力車、か。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、ほんと\x01",
            "不相応な代物だよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_665F")

    label("loc_65A6")


    #C0210
    ChrTalk(
        0x101,
        (
            "#00005Fこれは……\x01",
            "何だかすごい導力車だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x105,
        (
            "#10300Fふぅん、なかなか\x01",
            "気取ったデザインじゃないか。\x02\x03",

            "#10304Fまあ、こういうのって\x01",
            "持ち主と釣り合っていなければ\x01",
            "滑稽なだけだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665F")

    TalkEnd(0xFF)
    Return()

    # Function_27_63AB end

    def Function_28_6663(): pass

    label("Function_28_6663")

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
            "#12P#00000Fマクダエル邸の隣……\x01",
            "ここで間違いないな。\x02",
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
            "#12P#00000Fごめんください、\x01",
            "誰かいらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0214
    ChrTalk(
        0x101,
        "#12P#00003Fダメだ、反応がないな。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        "#12P#00105F鍵はかかっているの？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0216
    ChrTalk(
        0x101,
        (
            "#5P#00001Fいや、それが……\x01",
            "開いているみたいなんだ。\x02\x03",

            "#00003F中から話し声のようなものも\x01",
            "聞こえるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x109,
        (
            "#12P#10105F会話に夢中で\x01",
            "気付かなかったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x105,
        (
            "#12P#10300Fま、とにかく開いてるんなら\x01",
            "勝手に入ってもいいんじゃない？\x02\x03",

            "#10302F大体ほら、僕たちは\x01",
            "立派な警察官なワケなんだし。\x02",
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
            "#5P#00006F警察官だからといって勝手に\x01",
            "入っていいわけじゃないんだが……\x02\x03",

            "#00000Fまあ、いずれにしても\x01",
            "放っておくわけにはいかないし、\x01",
            "中に入って声を掛けてみるか。\x02",
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

    # Function_28_6663 end

    def Function_29_69FF(): pass

    label("Function_29_69FF")

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
            "#12P#10302Fやれやれ、ちょっとばかり\x01",
            "浮かれすぎてるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x102,
        (
            "#11P#00106Fええ、まさに絵に描いたような\x01",
            "ドラ息子って感じだったわね。\x02\x03",

            "#00108Fそれにしても、\x01",
            "この住宅があんな連中の\x01",
            "手に渡っていたなんて……\x02\x03",

            "#00103Fこれじゃ、ボンドさんも\x01",
            "浮かばれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x109,
        (
            "#6P#10101Fでも、契約には特に\x01",
            "違法性もないみたいですし……\x02\x03",

            "#10106Fその点に関して、文句の１つも\x01",
            "言えないのが悔しい所ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#5P#00003Fああ……だが、今のところは\x01",
            "放っておくしかなさそうだな。\x02\x03",

            "#00000F……とにかく、\x01",
            "これで住宅街の調査は終了だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DA6")
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
            "◆「調査状況は？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",                    # 0
            "【新ボンド邸を訪ねていない】\x01",      # 1
            "【まだ残りがある】\x01",                # 2
            "【６箇所の確認が終わった】\x01",        # 3
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
        (0, "loc_6D77"),
        (1, "loc_6D7C"),
        (2, "loc_6D84"),
        (3, "loc_6D95"),
        (SWITCH_DEFAULT, "loc_6DA6"),
    )


    label("loc_6D77")

    Jump("loc_6DA6")

    label("loc_6D7C")

    ClearScenarioFlags(0x131, 7)
    Jump("loc_6DA6")

    label("loc_6D84")

    SetScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_6DA6")

    label("loc_6D95")

    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    SetScenarioFlags(0x132, 2)
    Jump("loc_6DA6")

    label("loc_6DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E92")

    #C0225
    ChrTalk(
        0x102,
        (
            "#11P#00100Fねえ、ロイド。\x01",
            "次はボンドさんの所へ行かない？\x02\x03",

            "引越しの経緯について、\x01",
            "詳しい事情を聞いておきたいし。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#5P#00003Fああ、確かに心配だしな。\x02\x03",

            "#00000Fそれじゃ、次は東通りの\x01",
            "ボンドさんの所を訪ねるとするか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F44")

    label("loc_6E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6EF2")

    #C0227
    ChrTalk(
        0x101,
        (
            "#5P#00000Fよし、それじゃ引き続き\x01",
            "残りの調査にあたろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F44")

    label("loc_6EF2")


    #C0228
    ChrTalk(
        0x101,
        (
            "#5P#00000Fよし、これで一通り調査は済んだな。\x02\x03",

            "市民会館へ報告に戻ろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x6)

    label("loc_6F44")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_65(0x2, 0x1)
    SetMapObjFlags(0xB, 0x10)
    SetScenarioFlags(0x131, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -17150, -6000, -18250, 180)
    EventEnd(0x5)
    Return()

    # Function_29_69FF end

    def Function_30_6F74(): pass

    label("Function_30_6F74")

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

    def lambda_7041():
        OP_95(0xFE, -6050, -6000, -22480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7041)
    Sleep(50)

    def lambda_705E():
        OP_95(0xFE, -4650, -6000, -22780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_705E)
    Sleep(50)

    def lambda_707B():
        OP_95(0xFE, -5250, -6000, -21350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_707B)
    Sleep(50)

    def lambda_7098():
        OP_95(0xFE, -3850, -6000, -21480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7098)
    Sleep(50)

    def lambda_70B5():
        OP_95(0xFE, -6850, -6000, -21200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_70B5)
    FadeToBright(1000, 0)
    OP_0D()

    #C0229
    ChrTalk(
        0x1A3,
        "#04602Fあ～っ、いたいた！\x02",
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

    def lambda_717F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_717F)
    Sleep(50)

    def lambda_718F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_718F)
    Sleep(50)

    def lambda_719F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_719F)
    Sleep(50)

    def lambda_71AF():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_71AF)
    Sleep(50)

    def lambda_71BF():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_71BF)
    Sleep(1000)
    Fade(500)
    OP_68(-4050, 1670, -12540, 0)
    MoveCamera(42, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14080, 0)
    OP_0D()

    def lambda_7203():

        label("loc_7203")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7203")

    QueueWorkItem2(0x101, 1, lambda_7203)

    def lambda_7215():

        label("loc_7215")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7215")

    QueueWorkItem2(0x104, 1, lambda_7215)

    def lambda_7227():

        label("loc_7227")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7227")

    QueueWorkItem2(0x102, 1, lambda_7227)

    def lambda_7239():

        label("loc_7239")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7239")

    QueueWorkItem2(0x109, 1, lambda_7239)

    def lambda_724B():

        label("loc_724B")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_724B")

    QueueWorkItem2(0x105, 1, lambda_724B)
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
            "#5P#04600Fあんまり遅いから\x01",
            "勝手に捜し始めちゃったよ。\x02\x03",

            "#04609Fそれで、どこの家なのさ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        (
            "#12P#00000Fああ、この家だけど……\x02\x03",

            "#00006F……って、君の同行を\x01",
            "認めたわけじゃないんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x109, 0x3E8, 0x7D0, 0x0)
    Sleep(300)

    #C0232
    ChrTalk(
        0x1A3,
        (
            "#04600Fねえ、お姉さん。\x01",
            "イヌ派とネコ派、どっち？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x109,
        (
            "#12P#10105Fあ、あたし？\x02\x03",

            "#10104Fえっと……\x01",
            "どちらかというとネコ派かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x1A3,
        (
            "#04609Fあはは！\x01",
            "シャーリィと同じだね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0235
    ChrTalk(
        0x104,
        (
            "#6P#00303F（……諦めろ。\x01",
            "  何を言っても無駄だぜ。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0236
    ChrTalk(
        0x101,
        "#12P#00006F（はあ……そうみたいだな。）\x02",
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

    # Function_30_6F74 end

    def Function_31_751E(): pass

    label("Function_31_751E")

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
        "#12P#04609Fそれじゃ、次行ってみよう！\x02",
    )

    CloseMessageWindow()
    OP_95(0x1A3, -11560, -6000, -23410, 2000, 0x0)

    #C0238
    ChrTalk(
        0x101,
        "#00006F何というか……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x102,
        (
            "#00106Fええ……\x01",
            "凄い迫力だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x109,
        (
            "#10101Fあの細腕で、大の男を２人も\x01",
            "吊るし上げてましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、さすがは最強の\x01",
            "猟兵団の娘ってところか。\x02\x03",

            "#10302Fさっきの殺気はランディにも\x01",
            "通じるところがあるよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#6P#00303F……一緒にすんなっつーの。\x02",
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
            "#12P#04606Fもう、何してんのさ？\x02\x03",

            "#04602F早く行かないと\x01",
            "見つけらんないよー？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        "#6P#00000Fああ……すぐ行くよ。\x02",
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

    # Function_31_751E end

    def Function_32_7910(): pass

    label("Function_32_7910")


    def lambda_7915():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7915)

    def lambda_7926():
        OP_95(0xFE, -18140, -5600, -17170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7926)
    WaitChrThread(0x101, 1)
    OP_95(0x101, -17710, -6000, -18270, 2000, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Return()

    # Function_32_7910 end

    def Function_33_795B(): pass

    label("Function_33_795B")


    def lambda_7960():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7960)

    def lambda_7971():
        OP_95(0xFE, -18140, -5600, -17170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7971)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -16500, -6000, -17480, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_33_795B end

    def Function_34_79A6(): pass

    label("Function_34_79A6")


    def lambda_79AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_79AB)

    def lambda_79BC():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_79BC)
    WaitChrThread(0x104, 1)
    OP_95(0x104, -15930, -6000, -19920, 2000, 0x0)
    OP_93(0x104, 0x87, 0x1F4)
    Return()

    # Function_34_79A6 end

    def Function_35_79F1(): pass

    label("Function_35_79F1")


    def lambda_79F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_79F6)

    def lambda_7A07():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7A07)
    WaitChrThread(0x109, 1)
    OP_95(0x109, -16510, -6000, -18800, 2000, 0x0)
    OP_93(0x109, 0x87, 0x1F4)
    Return()

    # Function_35_79F1 end

    def Function_36_7A3C(): pass

    label("Function_36_7A3C")


    def lambda_7A41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7A41)

    def lambda_7A52():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7A52)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -15400, -6000, -18710, 2000, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_36_7A3C end

    def Function_37_7A87(): pass

    label("Function_37_7A87")


    def lambda_7A8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_7A8C)

    def lambda_7A9D():
        OP_95(0xFE, -14830, -6000, -20120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7A9D)
    WaitChrThread(0x1A3, 1)
    OP_93(0x1A3, 0x13B, 0x1F4)
    Return()

    # Function_37_7A87 end

    def Function_38_7ABE(): pass

    label("Function_38_7ABE")

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
        "#6P#00105Fねえ、ロイド……あれ！\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#00000Fああ、たぶんマリーだろう。\x01",
            "#6Pやっと見つかったな。\x02",
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

    def lambda_7DF7():
        OP_95(0xFE, 19310, 0, -4050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DF7)
    Sleep(50)

    def lambda_7E14():
        OP_95(0xFE, 18810, 0, -2750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7E14)
    Sleep(50)

    def lambda_7E31():
        OP_95(0xFE, 18610, 0, -5350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E31)
    Sleep(50)

    def lambda_7E4E():
        OP_95(0xFE, 17110, 0, -2950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E4E)
    Sleep(50)

    def lambda_7E6B():
        OP_95(0xFE, 16910, 0, -5250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E6B)
    Sleep(50)

    def lambda_7E88():
        OP_95(0xFE, 16309, 0, -4250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E88)
    WaitChrThread(0x1A3, 1)
    SetChrChipByIndex(0x1A3, 0xFF)
    SetChrSubChip(0x1A3, 0x0)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    #C0247
    ChrTalk(
        0x104,
        "#6P#00306F行っちまったか。\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x1A3,
        "#5P#04602Fでも、後は捕まえるだけだね。\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#12P#00000Fああ、すぐに後を追おう！\x02",
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

    # Function_38_7ABE end

    def Function_39_7F83(): pass

    label("Function_39_7F83")

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
            "#00005Fえっと……\x01",
            "届け先の住所は\x01",
            "ここで間違いないのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        "#00103Fええ、そうなんだけど……\x02",
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
            "#00303F……人のいる気配は\x01",
            "ねえみてえだなあ。\x02\x03",

            "#00301Fやっぱりなにかの\x01",
            "間違いなんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x109,
        (
            "#10105Fもしかして、\x01",
            "ご近所の住所と\x01",
            "書き間違えてたりとか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00001Fでもこの伝票……\x01",
            "住所は書いているけど\x01",
            "届け先の名前がないんだよな。\x02\x03",

            "#00003Fどちらにしろ尋ねてみないと\x01",
            "分からないだろうな。\x02",
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
        "#00005F……ん、どうしたティオ？\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x103,
        "#00205Fあ、いえ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x105,
        "#10305Fあれ、もしかして……\x02",
    )

    CloseMessageWindow()

    def lambda_82F9():
        OP_95(0xFE, 17650, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_82F9)
    Sleep(300)

    def lambda_8316():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8316)
    Sleep(100)

    def lambda_8326():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8326)
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
        "#00005F門の鍵が開いてる……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0259
    ChrTalk(
        0x105,
        (
            "#10304Fスキ間があいてたから\x01",
            "もしやと思ったけど……\x02\x03",

            "#10300Fま、ひとまず家の人に\x01",
            "聞いてみようよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        "#00003Fそ、そうだな……\x02",
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

    # Function_39_7F83 end

    def Function_40_850A(): pass

    label("Function_40_850A")

    EventBegin(0x1)

    #C0262
    ChrTalk(
        0x1A3,
        (
            "#04605Fえー、なんで戻ろうとするわけ。\x01",
            "目的の家は目の前なんだよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x101,
        (
            "#00000Fああ、すぐに向かおう。\x02\x03",

            "#00006F（……ランディの言う通り、\x01",
            "  何を言っても無駄そうだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -5250, -1550, -11110, 180)
    EventEnd(0x4)
    Return()

    # Function_40_850A end

    def Function_41_85CD(): pass

    label("Function_41_85CD")

    EventBegin(0x1)

    #C0264
    ChrTalk(
        0x1A3,
        (
            "#04600Fもう、何してんのさ。\x01",
            "早くマリーを追いかけるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#00000Fああ、歓楽街に急ごう。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 6340, 0, -5780, 90)
    EventEnd(0x4)
    Return()

    # Function_41_85CD end

    def Function_42_8642(): pass

    label("Function_42_8642")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_42_8642 end

    SaveToFile()

Try(main)
