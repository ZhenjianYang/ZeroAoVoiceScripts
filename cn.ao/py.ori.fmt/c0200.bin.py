from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0200.bin",                # FileName
        "c0200",                    # MapName
        "c0200",                    # Location
        0x000A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c0200", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 33140, -4000, -18370, 0, 0, 1, 10, 0, 11, 0, 12],
    )

    BuildStringList((
        "c0200",                  # 0
        "隆",                     # 1
        "亨利",                   # 2
        "庞斯",                   # 3
        "布利克",                 # 4
        "小桃",                   # 5
        "爱尔莎",                 # 6
        "卢威克老人",             # 7
        "卡缇莉娜",               # 8
        "琪露露",                 # 9
        "奥丽加夫人",             # 10
        "市民",                   # 11
        "警备队员",               # 12
        "赛尔盖科长",             # 13
        "莉丝",                   # 14
        "蔡特",                   # 15
        "琪雅",                   # 16
        "白隼",                   # 17
        "特别任务支援科导力车",   # 18
        "SE控制",                 # 19
        "bc0200",                 # 20
        "中央广场",               # 21
        "西街",                   # 22
        "行政区",                 # 23
        "住宅街",                 # 24
        "欢乐街",                 # 25
        "东街",                   # 26
        "旧城区",                 # 27
        "港湾区",                 # 28
        "ＩＢＣ",                 # 29
        "站前街道",               # 30
        "后巷",                   # 31
        "乌尔斯拉间道",           # 32
        "东克洛斯贝尔街道",       # 33
        "西克洛斯贝尔街道",       # 34
        "玛因兹山道",             # 35
        "兰花塔",                 # 36
    ))

    ATBonus("ATBonus_6D4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_A67A", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_724", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_72C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_730", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_734", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_738", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_73C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_740", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_784", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_788", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_78C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_790", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_794", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_798", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_79C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_704", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_708", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_70C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_710", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_714", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_718", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_7A4", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0200", "Sepith_A67A", 60, 25, 10, 0,
        (
            ("ms85100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_724", "MonsterBattlePostion_784", "ed7450", "ed7453", "ATBonus_6D4"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_704", "MonsterBattlePostion_784", "ed7450", "ed7453", "ATBonus_6D4"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_724", "MonsterBattlePostion_784", "ed7450", "ed7453", "ATBonus_6D4"),
            (),
        )
    )

    AddCharChip((
        "chr/ch20600.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20402.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch10400.itc",                   # 05
        "chr/ch21600.itc",                   # 06
        "chr/ch24500.itc",                   # 07
        "chr/ch20500.itc",                   # 08
        "chr/ch20100.itc",                   # 09
        "chr/ch49000.itc",                   # 0A
        "chr/ch48500.itc",                   # 0B
        "chr/ch31300.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
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

    DeclNpc(-1000,   0,       610,     90,   261,  0x0, 0,   0,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(449,     0,       610,     90,   261,  0x0, 0,   1,   0,   0,   1,   0,   18,  255,  0)
    DeclNpc(-15119,  0,       5829,    270,  261,  0x0, 0,   2,   0,   0,   2,   0,   19,  255,  0)
    DeclNpc(6570,    -150,    5119,    90,   325,  0x0, 0,   3,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(5360,    3000,    17690,   0,    261,  0x0, 0,   4,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(9159,    3000,    17489,   225,  261,  0x0, 0,   5,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-6690,   0,       4460,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(10800,   0,       -3480,   270,  389,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(10729,   0,       -4780,   270,  389,  0x0, 0,   8,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-5280,   0,       4489,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-850,    3000,    27399,   180,  385,  0x0, 0,   10,  0,   0,   10,  0,   27,  255,  0)
    DeclNpc(1360,    -300,    7380,    180,  385,  0x0, 0,   12,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(250,     3470,    0,       0x10100E1,    "BattleInfo_7A4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4800,    -9360,   0,       0x101013B,    "BattleInfo_7A4", 0,   16,  0xFFFF, 0,  1)

    DeclActor(33490,   -4000,   -16740,  1500,    33490,   -2000,   -16740,  0x007C, 0,  32, 0x0000)
    DeclActor(33490,   -4000,   -16740,  1500,    33490,   -2000,   -16740,  0x007C, 0,  32, 0x0000)
    DeclActor(37220,   -4000,   -19150,  1000,    37220,   -3000,   -19150,  0x007C, 0,  29, 0x0000)
    DeclActor(18220,   -210,    -11950,  1000,    18220,   1000,    -11950,  0x007C, 0,  29, 0x0000)
    DeclActor(14500,   -6500,   -13500,  1200,    14500,   -5500,   -13500,  0x007C, 0,  13, 0x0000)
    DeclActor(19330,   3000,    15550,   1200,    19330,   4500,    15550,   0x007C, 0,  30, 0x0000)
    DeclActor(40950,   -4000,   -19220,  1200,    40950,   -2500,   -19220,  0x007C, 0,  52, 0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "中央广场")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "西街")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "行政区")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "住宅街")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "欢乐街")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "东街")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "旧城区")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "港湾区")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "站前街道")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "后巷")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(91.0, 0.0, 213.0, 0x0000, 0x0000, "兰花塔")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_92C",          # 00, 0
        "Function_1_9DC",          # 01, 1
        "Function_2_A3D",          # 02, 2
        "Function_3_A9E",          # 03, 3
        "Function_4_AC9",          # 04, 4
        "Function_5_B9D",          # 05, 5
        "Function_6_C71",          # 06, 6
        "Function_7_D45",          # 07, 7
        "Function_8_E19",          # 08, 8
        "Function_9_EED",          # 09, 9
        "Function_10_F18",         # 0A, 10
        "Function_11_F79",         # 0B, 11
        "Function_12_1B16",        # 0C, 12
        "Function_13_20E6",        # 0D, 13
        "Function_14_2221",        # 0E, 14
        "Function_15_28B5",        # 0F, 15
        "Function_16_296A",        # 10, 16
        "Function_17_2A24",        # 11, 17
        "Function_18_2B2D",        # 12, 18
        "Function_19_30F2",        # 13, 19
        "Function_20_3DF3",        # 14, 20
        "Function_21_45A2",        # 15, 21
        "Function_22_4836",        # 16, 22
        "Function_23_4D2F",        # 17, 23
        "Function_24_532B",        # 18, 24
        "Function_25_5372",        # 19, 25
        "Function_26_53B2",        # 1A, 26
        "Function_27_541C",        # 1B, 27
        "Function_28_54F0",        # 1C, 28
        "Function_29_5685",        # 1D, 29
        "Function_30_56EA",        # 1E, 30
        "Function_31_5734",        # 1F, 31
        "Function_32_5AAB",        # 20, 32
        "Function_33_6075",        # 21, 33
        "Function_34_6136",        # 22, 34
        "Function_35_61CA",        # 23, 35
        "Function_36_6275",        # 24, 36
        "Function_37_677E",        # 25, 37
        "Function_38_7C7D",        # 26, 38
        "Function_39_7CD4",        # 27, 39
        "Function_40_7D69",        # 28, 40
        "Function_41_7E02",        # 29, 41
        "Function_42_7E36",        # 2A, 42
        "Function_43_7E6A",        # 2B, 43
        "Function_44_7E9E",        # 2C, 44
        "Function_45_7ED2",        # 2D, 45
        "Function_46_7EE2",        # 2E, 46
        "Function_47_9864",        # 2F, 47
        "Function_48_9894",        # 30, 48
        "Function_49_98D3",        # 31, 49
        "Function_50_9CB5",        # 32, 50
        "Function_51_A32A",        # 33, 51
        "Function_52_A5C1",        # 34, 52
    ))


    def Function_0_92C(): pass

    label("Function_0_92C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_964"),
        (1, "loc_970"),
        (2, "loc_97C"),
        (3, "loc_988"),
        (4, "loc_994"),
        (5, "loc_9A0"),
        (6, "loc_9AC"),
        (SWITCH_DEFAULT, "loc_9B8"),
    )


    label("loc_964")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_970")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_97C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_988")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_994")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9DB")

    Return()

    # Function_0_92C end

    def Function_1_9DC(): pass

    label("Function_1_9DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A3C")
    OP_95(0xFE, 7000, -300, 610, 6000, 0x0)
    OP_95(0xFE, 7000, 0, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, -10, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, 0, 610, 6000, 0x0)
    Jump("Function_1_9DC")

    label("loc_A3C")

    Return()

    # Function_1_9DC end

    def Function_2_A3D(): pass

    label("Function_2_A3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A9D")
    OP_95(0xFE, -10000, 0, 5750, 800, 0x0)
    OP_95(0xFE, -10000, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 5750, 800, 0x0)
    Jump("Function_2_A3D")

    label("loc_A9D")

    Return()

    # Function_2_A3D end

    def Function_3_A9E(): pass

    label("Function_3_A9E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC8")
    OP_94(0xFE, 0xFFFF8F3A, 0x9EC, 0xFFFFAD9E, 0x18EC, 0x3E8)
    Sleep(300)
    Jump("Function_3_A9E")

    label("loc_AC8")

    Return()

    # Function_3_A9E end

    def Function_4_AC9(): pass

    label("Function_4_AC9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B9C")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B08")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF40C, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B30")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF3A8, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B58")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF344, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B80")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF2E0, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B80")

    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF27C, 0x12C, 0x0)

    label("loc_B94")

    Sleep(500)
    Jump("Function_4_AC9")

    label("loc_B9C")

    Return()

    # Function_4_AC9 end

    def Function_5_B9D(): pass

    label("Function_5_B9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C70")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BDC")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF40C, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_BDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C04")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF3A8, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_C04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C2C")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF344, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_C2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C54")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF2E0, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_C54")

    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF27C, 0xC8, 0x0)

    label("loc_C68")

    Sleep(600)
    Jump("Function_5_B9D")

    label("loc_C70")

    Return()

    # Function_5_B9D end

    def Function_6_C71(): pass

    label("Function_6_C71")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D44")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CB0")
    OP_96(0xFE, 0x11A8, 0x0, 0xFFFFF1AA, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_CB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CD8")
    OP_96(0xFE, 0x11DA, 0x0, 0xFFFFF1DC, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_CD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D00")
    OP_96(0xFE, 0x120C, 0x0, 0xFFFFF20E, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_D00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D28")
    OP_96(0xFE, 0x123E, 0x0, 0xFFFFF240, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_D28")

    OP_96(0xFE, 0x1270, 0x0, 0xFFFFF272, 0x12C, 0x0)

    label("loc_D3C")

    Sleep(500)
    Jump("Function_6_C71")

    label("loc_D44")

    Return()

    # Function_6_C71 end

    def Function_7_D45(): pass

    label("Function_7_D45")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E18")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D84")
    OP_96(0xFE, 0xE24, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_D84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DAC")
    OP_96(0xFE, 0xDF2, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_DAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DD4")
    OP_96(0xFE, 0xDC0, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_DD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DFC")
    OP_96(0xFE, 0xD8E, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_DFC")

    OP_96(0xFE, 0xD5C, 0x0, 0xFFFFF92A, 0xFA, 0x0)

    label("loc_E10")

    Sleep(550)
    Jump("Function_7_D45")

    label("loc_E18")

    Return()

    # Function_7_D45 end

    def Function_8_E19(): pass

    label("Function_8_E19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EEC")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E58")
    OP_96(0xFE, 0x910, 0x0, 0xFFFFF272, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_E58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E80")
    OP_96(0xFE, 0x942, 0x0, 0xFFFFF240, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_E80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EA8")
    OP_96(0xFE, 0x974, 0x0, 0xFFFFF20E, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_EA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ED0")
    OP_96(0xFE, 0x9A6, 0x0, 0xFFFFF1DC, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_ED0")

    OP_96(0xFE, 0x9D8, 0x0, 0xFFFFF1AA, 0xC8, 0x0)

    label("loc_EE4")

    Sleep(600)
    Jump("Function_8_E19")

    label("loc_EEC")

    Return()

    # Function_8_E19 end

    def Function_9_EED(): pass

    label("Function_9_EED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F17")
    OP_94(0xFE, 0xFFFFFC18, 0xFFFFDCD8, 0x1B58, 0x0, 0x3E8)
    Sleep(300)
    Jump("Function_9_EED")

    label("loc_F17")

    Return()

    # Function_9_EED end

    def Function_10_F18(): pass

    label("Function_10_F18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F78")
    OP_95(0xFE, -1630, 0, 5050, 2000, 0x0)
    OP_95(0xFE, 9840, 0, -6290, 2000, 0x0)
    OP_95(0xFE, 40380, 2060, -8580, 2000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, -850, 3000, 27400, 180)
    Jump("Function_10_F18")

    label("loc_F78")

    Return()

    # Function_10_F18 end

    def Function_11_F79(): pass

    label("Function_11_F79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E5")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1044")
    SetChrPos(0x0, 110, 3000, 22760, 180)
    SetChrPos(0x1, 110, 3000, 22760, 180)
    SetChrPos(0x2, 110, 3000, 22760, 180)
    SetChrPos(0x3, 110, 3000, 22760, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1017")
    SetChrPos(0x4, 110, 3000, 22760, 180)
    SetChrPos(0x5, 110, 3000, 22760, 180)
    Jump("loc_1036")

    label("loc_1017")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1036")
    SetChrPos(0x4, 110, 3000, 22760, 180)

    label("loc_1036")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10E5")

    label("loc_1044")

    SetChrPos(0x0, 24460, 0, -8180, 270)
    SetChrPos(0x1, 24460, 0, -8180, 270)
    SetChrPos(0x2, 24460, 0, -8180, 270)
    SetChrPos(0x3, 24460, 0, -8180, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BD")
    SetChrPos(0x4, 24460, 0, -8180, 270)
    SetChrPos(0x5, 24460, 0, -8180, 270)
    Jump("loc_10DC")

    label("loc_10BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DC")
    SetChrPos(0x4, 24460, 0, -8180, 270)

    label("loc_10DC")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10E5")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1102")
    OP_C9(0x1, 0x1000)

    label("loc_1102")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A6")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118F")
    SetScenarioFlags(0x38, 0)

    label("loc_118F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A5")
    SetScenarioFlags(0x38, 1)

    label("loc_11A5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BB")
    SetScenarioFlags(0x38, 2)

    label("loc_11BB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D1")
    SetScenarioFlags(0x38, 3)

    label("loc_11D1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E7")
    SetScenarioFlags(0x38, 4)

    label("loc_11E7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FD")
    SetScenarioFlags(0x38, 5)

    label("loc_11FD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1213")
    SetScenarioFlags(0x38, 6)

    label("loc_1213")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1229")
    SetScenarioFlags(0x38, 7)

    label("loc_1229")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123F")
    SetScenarioFlags(0x39, 0)

    label("loc_123F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1255")
    SetScenarioFlags(0x39, 1)

    label("loc_1255")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126B")
    SetScenarioFlags(0x39, 2)

    label("loc_126B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1281")
    SetScenarioFlags(0x39, 3)

    label("loc_1281")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1297")
    SetScenarioFlags(0x39, 4)

    label("loc_1297")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AD")
    SetScenarioFlags(0x39, 5)

    label("loc_12AD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C3")
    SetScenarioFlags(0x39, 6)

    label("loc_12C3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D9")
    SetScenarioFlags(0x39, 7)

    label("loc_12D9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EF")
    SetScenarioFlags(0x3A, 0)

    label("loc_12EF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1305")
    SetScenarioFlags(0x3A, 1)

    label("loc_1305")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131B")
    SetScenarioFlags(0x3A, 2)

    label("loc_131B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1331")
    SetScenarioFlags(0x3A, 3)

    label("loc_1331")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1347")
    SetScenarioFlags(0x3A, 4)

    label("loc_1347")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135D")
    SetScenarioFlags(0x3A, 5)

    label("loc_135D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    SetScenarioFlags(0x3A, 6)

    label("loc_1373")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1389")
    SetScenarioFlags(0x3A, 7)

    label("loc_1389")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139F")
    SetScenarioFlags(0x3B, 0)

    label("loc_139F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B5")
    SetScenarioFlags(0x3B, 1)

    label("loc_13B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CB")
    SetScenarioFlags(0x3B, 2)

    label("loc_13CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E1")
    SetScenarioFlags(0x3B, 3)

    label("loc_13E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F7")
    SetScenarioFlags(0x3B, 4)

    label("loc_13F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140D")
    SetScenarioFlags(0x3B, 5)

    label("loc_140D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1423")
    SetScenarioFlags(0x3B, 6)

    label("loc_1423")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1439")
    SetScenarioFlags(0x3B, 7)

    label("loc_1439")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144F")
    SetScenarioFlags(0x3D, 5)

    label("loc_144F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1465")
    SetScenarioFlags(0x3D, 6)

    label("loc_1465")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147B")
    SetScenarioFlags(0x3D, 7)

    label("loc_147B")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B6")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_15A6")

    label("loc_14B6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D9")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_15A6")

    label("loc_14D9")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FC")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_15A6")

    label("loc_14FC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_151F")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_15A6")

    label("loc_151F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1542")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_15A6")

    label("loc_1542")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1565")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_15A6")

    label("loc_1565")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1588")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_15A6")

    label("loc_1588")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A6")
    SetScenarioFlags(0x3C, 7)

    label("loc_15A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15BC")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EE")
    SetChrPos(0x0, 33260, -4000, -18040, 278)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 34)

    label("loc_15EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_1621")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1621")
    SetChrPos(0x0, 33490, -4000, -16740, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_1621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1635")
    ClearScenarioFlags(0x22, 0)
    Event(0, 35)
    Jump("loc_1644")

    label("loc_1635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1644")
    ClearScenarioFlags(0x22, 1)
    Event(0, 37)

    label("loc_1644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1655")
    Event(0, 36)

    label("loc_1655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1680")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_1680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1691")
    Event(0, 46)

    label("loc_1691")

    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1727")
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x8, 4620, 0, -3570, 315)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D6")
    SetChrFlags(0x8, 0x10)

    label("loc_16D6")

    SetChrPos(0x9, 3520, 0, -1750, 180)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FC")
    SetChrFlags(0x9, 0x10)

    label("loc_16FC")

    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1722")
    SetChrFlags(0xC, 0x10)

    label("loc_1722")

    Jump("loc_1B15")

    label("loc_1727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1753")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_1B15")

    label("loc_1753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_179E")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_1B15")

    label("loc_179E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_17E9")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1B15")

    label("loc_17E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_180E")
    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 8)
    Jump("loc_1B15")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1879")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, -5710, 0, 1570, 180)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xA, 0xB)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_1B15")

    label("loc_1879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_18F1")
    SetChrPos(0x8, 30090, -4000, -15230, 225)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 6330, -300, 1950, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xC, 4390, -40, 1630, 90)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -6690, 0, 4460, 90)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_1B15")

    label("loc_18F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1953")
    SetChrPos(0x8, 30090, -4000, -15230, 225)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1920")
    SetChrFlags(0x8, 0x10)

    label("loc_1920")

    SetChrPos(0x9, 11110, -300, 5400, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 9)
    Jump("loc_1B15")

    label("loc_1953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_19D5")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1982")
    SetChrFlags(0x8, 0x10)

    label("loc_1982")

    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A8")
    SetChrFlags(0x9, 0x10)

    label("loc_19A8")

    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 8130, 3000, 13940, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19D0")
    SetChrFlags(0xB, 0x80)

    label("loc_19D0")

    Jump("loc_1B15")

    label("loc_19D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19F7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_1B15")

    label("loc_19F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1A0F")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_1B15")

    label("loc_1A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A31")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_1B15")

    label("loc_1A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AB1")
    SetChrPos(0x8, 4620, 0, -3570, 315)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A60")
    SetChrFlags(0x8, 0x10)

    label("loc_1A60")

    SetChrPos(0x9, 3520, 0, -1750, 180)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A86")
    SetChrFlags(0x9, 0x10)

    label("loc_1A86")

    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAC")
    SetChrFlags(0xC, 0x10)

    label("loc_1AAC")

    Jump("loc_1B15")

    label("loc_1AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AF8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, -5710, 0, 1570, 180)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xA, 0xB)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_1B15")

    label("loc_1AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B15")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)

    label("loc_1B15")

    Return()

    # Function_11_F79 end

    def Function_12_1B16(): pass

    label("Function_12_1B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BE2")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x5F, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C99")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x5F, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)

    label("loc_1C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D03")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)

    label("loc_1D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D1B")
    ClearMapFlags(0x2000)
    Jump("loc_1D22")

    label("loc_1D1B")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_1D22")

    MiniGame(0x2F, 0x0, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1DA0")
    SetMapObjFrame(0xFF, "tuika_mul", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kabuse", 0x0, 0x1)
    Jump("loc_1E2E")

    label("loc_1DA0")

    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika", 0x0, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kabuse", 0x1, 0x1)
    SetMapObjFlags(0xA, 0x4)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 18500, -1000, -11500, 5000, 5000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 37500, -5000, -19000, 5000, 5000, 90000)

    label("loc_1E2E")

    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4B")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E5E")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E71")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E84")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E97")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E97")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EB5")
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_1EB5")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED1")
    OP_66(0x5, 0x1)
    ClearMapObjFlags(0x3, 0x10)

    label("loc_1ED1")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EED")
    OP_66(0x6, 0x1)
    ClearMapObjFlags(0x5, 0x10)

    label("loc_1EED")

    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_209D")
    Jump("loc_20AC")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_20AC")
    SetMapObjFlags(0xC, 0x4)

    label("loc_20AC")

    MiniGame(0x2F, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E1")
    OP_70(0xD, 0x0)
    Jump("loc_20E5")

    label("loc_20E1")

    OP_70(0xD, 0x1E)

    label("loc_20E5")

    Return()

    # Function_12_1B16 end

    def Function_13_20E6(): pass

    label("Function_13_20E6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D8")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＺＷＥＩ２企鹅', 1)"), scpexpr(EXPR_END)), "loc_2169")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_21D3")

    label("loc_2169")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_21D3")

    Jump("loc_2215")

    label("loc_21D8")

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

    label("loc_2215")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_20E6 end

    def Function_14_2221(): pass

    label("Function_14_2221")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2277")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223F")
    Call(0, 17)
    Jump("loc_2272")

    label("loc_223F")


    #C0004
    ChrTalk(
        0xFE,
        "啊，大哥哥！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市\x01",
            "就交给我们吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2272")

    Jump("loc_28B1")

    label("loc_2277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2285")
    Jump("loc_28B1")

    label("loc_2285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_234F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230D")

    #C0006
    ChrTalk(
        0xFE,
        (
            "大家好像都在为\x01",
            "什么帝国和共和国的问题烦恼……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "我虽然不懂\x01",
            "什么独立……\x01",
            "但这难道不是一件高兴的事吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_234A")

    label("loc_230D")


    #C0008
    ChrTalk(
        0xFE,
        (
            "独立难道不是\x01",
            "一件高兴的事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "我实在是不明白啊……\x02",
    )

    CloseMessageWindow()

    label("loc_234A")

    Jump("loc_28B1")

    label("loc_234F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23A7")

    #C0010
    ChrTalk(
        0xFE,
        (
            "我去叫小桃一起玩，\x01",
            "但是阿姨却\x01",
            "不让她出来玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "呼，真是扫兴啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28B1")

    label("loc_23A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_23C9")

    #C0012
    ChrTalk(
        0xFE,
        "呀哈！等等我！\x02",
    )

    CloseMessageWindow()
    Jump("loc_28B1")

    label("loc_23C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2469")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_242D")

    #C0013
    ChrTalk(
        0xFE,
        "小桃那家伙好慢啊。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "不就是帮家里买个东西嘛，\x01",
            "赶快搞定就是了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2464")

    label("loc_242D")


    #C0015
    ChrTalk(
        0xFE,
        (
            "小桃那家伙，不就是帮家里买个东西嘛，\x01",
            "赶快搞定啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2464")

    Jump("loc_28B1")

    label("loc_2469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_252D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CC")

    #C0016
    ChrTalk(
        0xFE,
        (
            "小桃那家伙真是\x01",
            "很不擅长捉人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "都已经有些不耐烦了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2528")

    label("loc_24CC")


    #C0018
    ChrTalk(
        0xFE,
        (
            "一直待在原地不动，\x01",
            "我都已经不耐烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "真希望她赶快把我找到，\x01",
            "然后去玩别的游戏啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2528")

    Jump("loc_28B1")

    label("loc_252D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2681")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2636")
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    #C0020
    ChrTalk(
        0xFE,
        (
            "哦……\x01",
            "什么嘛，原来是你们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "哎～吓了我一跳。\x01",
            "还以为被小桃\x01",
            "发现了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00006F喂……\x01",
            "不要擅自钻到\x01",
            "这种地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "嘿嘿，不要计较\x01",
            "这种小事嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "不要和小桃说\x01",
            "我藏在这里啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0xE1, 0x0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_267C")

    label("loc_2636")


    #C0025
    ChrTalk(
        0xFE,
        (
            "我正在和亨利、小桃\x01",
            "玩捉迷藏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "不要和小桃说\x01",
            "我藏在这里啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_267C")

    Jump("loc_28B1")

    label("loc_2681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_26E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269C")
    Call(0, 15)
    Jump("loc_26DF")

    label("loc_269C")


    #C0027
    ChrTalk(
        0xFE,
        (
            "对了，琪雅那家伙\x01",
            "最近没什么精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "下次叫她也一起玩吧～\x02",
    )

    CloseMessageWindow()

    label("loc_26DF")

    Jump("loc_28B1")

    label("loc_26E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_26F2")
    Jump("loc_28B1")

    label("loc_26F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2805")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B9")

    #C0029
    ChrTalk(
        0xFE,
        (
            "明天好像要在兰花塔\x01",
            "举行一个叫做\x01",
            "通商什么的活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "虽然不太了解，\x01",
            "但机会难得，\x01",
            "我准备和亨利他们一起去参观。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "嘿嘿，那肯定是一场\x01",
            "有趣的宴会吧，\x01",
            "好期待明天啊～¤\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2800")

    label("loc_27B9")


    #C0032
    ChrTalk(
        0xFE,
        (
            "那个叫通商什么的活动\x01",
            "多半是一场宴会吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "嘿嘿，好期待明天啊～\x02",
    )

    CloseMessageWindow()

    label("loc_2800")

    Jump("loc_28B1")

    label("loc_2805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2813")
    Jump("loc_28B1")

    label("loc_2813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_289A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_282E")
    Call(0, 16)
    Jump("loc_2895")

    label("loc_282E")


    #C0034
    ChrTalk(
        0xFE,
        (
            "对了，琪雅今天\x01",
            "好像是去找一个\x01",
            "叫小滴的朋友玩了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "难得的机会，不然就把\x01",
            "那家伙也一起叫去吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2895")

    Jump("loc_28B1")

    label("loc_289A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_28A8")
    Jump("loc_28B1")

    label("loc_28A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_28B1")

    label("loc_28B1")

    TalkEnd(0xFE)
    Return()

    # Function_14_2221 end

    def Function_15_28B5(): pass

    label("Function_15_28B5")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0036
    ChrTalk(
        0x8,
        (
            "小桃今天要在\x01",
            "店里帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "啧，只有我和亨利两个人，\x01",
            "可以选择的游玩项目就太少了～\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "隆可真是的……\x01",
            "竟然说那样的话，\x01",
            "对我未免也太失礼了吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_15_28B5 end

    def Function_16_296A(): pass

    label("Function_16_296A")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0039
    ChrTalk(
        0x8,
        (
            "明天大家\x01",
            "一起去看\x01",
            "兰花塔吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "嗯，好主意啊，\x01",
            "大家一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xC,
        "小、小桃也要去……！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "OK，\x01",
            "那明天一大早\x01",
            "在百货店门口集合！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_296A end

    def Function_17_2A24(): pass

    label("Function_17_2A24")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0043
    ChrTalk(
        0x8,
        (
            "好，我们要开始在\x01",
            "市里巡逻了！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        "准备好了吗？亨利、小桃！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        "是的！隆队长！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xC,
        "出发！\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "好，我们行动吧！\x01",
            "克洛斯贝尔少年支援科！出动！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00002F（哈哈，少年支援科……）\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#00109F（真让人开心呢。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_17_2A24 end

    def Function_18_2B2D(): pass

    label("Function_18_2B2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4B")
    Call(0, 17)
    Jump("loc_2BB2")

    label("loc_2B4B")


    #C0050
    ChrTalk(
        0xFE,
        (
            "少年支援科……\x01",
            "隆偶尔也能想出一些\x01",
            "不错的主意嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "既然决定要干，我们就要\x01",
            "努力帮助市里的各位。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BB2")

    Jump("loc_30EE")

    label("loc_2BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2BC5")
    Jump("loc_30EE")

    label("loc_2BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2CD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C61")

    #C0052
    ChrTalk(
        0xFE,
        (
            "我的爸爸和妈妈\x01",
            "都从外国回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "虽然我很开心，\x01",
            "但他们的心情好像很复杂……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "呼，看来独立果然是一件\x01",
            "很严肃的问题啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CD0")

    label("loc_2C61")


    #C0055
    ChrTalk(
        0xFE,
        (
            "爸爸和妈妈回来了，\x01",
            "虽然我很开心，\x01",
            "但他们的心情好像很复杂……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "呼，看来独立果然是一件\x01",
            "很严肃的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD0")

    Jump("loc_30EE")

    label("loc_2CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D34")

    #C0057
    ChrTalk(
        0xFE,
        (
            "小桃的妈妈\x01",
            "好像很担心小桃。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "真没办法啊……\x01",
            "毕竟发生了\x01",
            "那样的袭击事件。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30EE")

    label("loc_2D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D9F")

    #C0059
    ChrTalk(
        0xFE,
        (
            "等、等一下啊，隆！？\x01",
            "还没有决定\x01",
            "要玩什么吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "就这样一直跑太累了，\x01",
            "先休息一下吧～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30EE")

    label("loc_2D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E23")

    #C0061
    ChrTalk(
        0xFE,
        (
            "今天早上，隆突然\x01",
            "来找我，要一起去\x01",
            "兰花塔的广场。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "隆可真是的，为什么非要\x01",
            "在这种下雨天过去啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E7F")

    label("loc_2E23")


    #C0063
    ChrTalk(
        0xFE,
        (
            "隆邀请的太突然了，\x01",
            "小桃一时过不来也没办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "在她买完东西之前，\x01",
            "就在这里慢慢等吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E7F")

    Jump("loc_30EE")

    label("loc_2E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2F45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EFB")

    #C0065
    ChrTalk(
        0xFE,
        "呼，被找到了。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "说起来，隆到底\x01",
            "藏到什么地方了……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "但愿他别再跑进\x01",
            "奇怪的地方。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F40")

    label("loc_2EFB")


    #C0068
    ChrTalk(
        0xFE,
        (
            "说起来，刚才开过了\x01",
            "好几辆急救车呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "难道发生事故了吗……？\x02",
    )

    CloseMessageWindow()

    label("loc_2F40")

    Jump("loc_30EE")

    label("loc_2F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FA7")

    #C0070
    ChrTalk(
        0xFE,
        (
            "最近只要一玩捉迷藏，\x01",
            "就要到傍晚才能结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "小桃到底有没有\x01",
            "认真找我们啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30EE")

    label("loc_2FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_303A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC2")
    Call(0, 15)
    Jump("loc_3035")

    label("loc_2FC2")


    #C0072
    ChrTalk(
        0xFE,
        (
            "小桃加入以后，\x01",
            "可以选择的游戏项目\x01",
            "确实丰富了很多，很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "不过，既然今天她要在\x01",
            "店里帮忙，也没办法啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3035")

    Jump("loc_30EE")

    label("loc_303A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3048")
    Jump("loc_30EE")

    label("loc_3048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3056")
    Jump("loc_30EE")

    label("loc_3056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3064")
    Jump("loc_30EE")

    label("loc_3064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_30D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307F")
    Call(0, 16)
    Jump("loc_30D2")

    label("loc_307F")


    #C0074
    ChrTalk(
        0xFE,
        (
            "听说兰花塔\x01",
            "有２５０赛尔矩\x01",
            "高呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "到底是个什么样的建筑物呢……\x01",
            "真期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30D2")

    Jump("loc_30EE")

    label("loc_30D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_30E5")
    Jump("loc_30EE")

    label("loc_30E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_30EE")

    label("loc_30EE")

    TalkEnd(0xFE)
    Return()

    # Function_18_2B2D end

    def Function_19_30F2(): pass

    label("Function_19_30F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3199")

    #C0076
    ChrTalk(
        0xFE,
        (
            "如此巨大，而且还\x01",
            "散发着蓝白光芒的大树……\x01",
            "竟然会出现这样的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "虽然还不知接下来将会发生什么，\x01",
            "但必须要将这些记录下来，\x01",
            "使其流传至后世啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DEF")

    label("loc_3199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_31A7")
    Jump("loc_3DEF")

    label("loc_31A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_321C")

    #C0078
    ChrTalk(
        0xFE,
        (
            "迪塔总统的发言……\x01",
            "对我们这些居民造成了很强的触动。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "即使要与两大国\x01",
            "为敌……\x01",
            "我也坚决支持他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DEF")

    label("loc_321C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3354")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E5")

    #C0080
    ChrTalk(
        0xFE,
        (
            "我正在拍摄参加复兴活动的人们，\x01",
            "还有ＩＢＣ等遭到破坏\x01",
            "的建筑物。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "绝不能让那种恐怖的事件\x01",
            "再度发生……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "就算是为了让大家不将这起事件遗忘，\x01",
            "我也必须要认真做好记录。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_334F")

    label("loc_32E5")


    #C0083
    ChrTalk(
        0xFE,
        (
            "绝不能让那种恐怖的事件\x01",
            "再度发生……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "就算是为了让大家不将这起事件遗忘，\x01",
            "我也必须要认真做好记录。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334F")

    Jump("loc_3DEF")

    label("loc_3354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F7")

    #C0085
    ChrTalk(
        0xFE,
        (
            "从昨晚开始，\x01",
            "就有数辆警备队装甲车\x01",
            "开往玛因兹方向。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "他们应该是要过去\x01",
            "增援吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "那个武装集团\x01",
            "竟然是如此强大的对手吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3462")

    label("loc_33F7")


    #C0088
    ChrTalk(
        0xFE,
        (
            "警备队的增援部队\x01",
            "驾驶着好几辆装甲车\x01",
            "前往玛因兹地区了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "那个武装集团\x01",
            "竟然是如此强大的对手吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3462")

    Jump("loc_3DEF")

    label("loc_3467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_34F9")

    #C0090
    ChrTalk(
        0xFE,
        (
            "虽然我也不清楚详情……\x01",
            "但听说昨天的那起列车事故\x01",
            "是由一只来历不明的怪物所引发的。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "唔，不知它是否会再次出现，真让人不安啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DEF")

    label("loc_34F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3557")

    #C0092
    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "我很怕听到急救车的警笛声呢。\x01",
            "不知为什么，只要听到，就会感到不安……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DEF")

    label("loc_3557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_369E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_363A")

    #C0093
    ChrTalk(
        0xFE,
        (
            "我有一本克洛斯贝尔通讯社\x01",
            "出版的观光向导册\x01",
            "《克洛斯贝尔百景》。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "这本书里记录了很多\x01",
            "景色优美的景点，\x01",
            "对摄影有很大帮助呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "不过，那些景色优美的景点\x01",
            "大多都比较远。\x01",
            "接下来要去哪里拍摄呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3699")

    label("loc_363A")


    #C0096
    ChrTalk(
        0xFE,
        (
            "今天要去什么地方\x01",
            "拍照片好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "《克洛斯贝尔百景》\x01",
            "上记载的观光景点\x01",
            "大多都比较远啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3699")

    Jump("loc_3DEF")

    label("loc_369E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_37F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3769")

    #C0098
    ChrTalk(
        0xFE,
        (
            "不久前，我去乌尔斯拉间道\x01",
            "的河滩一带拍了照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "在河滩深处，我发现了一条\x01",
            "以前从没见过的小路呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "看上去总觉得很危险，\x01",
            "所以我没有进去……\x01",
            "那条路究竟通往什么地方呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37F2")

    label("loc_3769")


    #C0101
    ChrTalk(
        0xFE,
        (
            "我在乌尔斯拉间道的河滩深处发现了一条\x01",
            "以前从没见过的小路呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "看上去总觉得很危险，\x01",
            "所以我没有进去……\x01",
            "那条路究竟通往什么地方呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37F2")

    Jump("loc_3DEF")

    label("loc_37F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_392D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38CA")

    #C0103
    ChrTalk(
        0xFE,
        (
            "兰花塔的周边地区\x01",
            "现在已经禁止\x01",
            "无关人员接近了。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "从安保角度来考虑，这也是没办法的事，\x01",
            "但还是觉得有点遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "昨天拍了不少兰花塔的照片，\x01",
            "今天本想去近一些的地方再拍一些呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3928")

    label("loc_38CA")


    #C0106
    ChrTalk(
        0xFE,
        (
            "兰花塔的周边地区\x01",
            "现在已经禁止\x01",
            "无关人员接近了。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "今天就去百货店\x01",
            "的楼顶拍摄吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3928")

    Jump("loc_3DEF")

    label("loc_392D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3A05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CA")

    #C0108
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "感光回路\x01",
            "已经用完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "看来是在白天的揭幕式上\x01",
            "拍了太多照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "在导力商店关门之前，\x01",
            "得赶快去买个新的感光回路。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A00")

    label("loc_39CA")


    #C0111
    ChrTalk(
        0xFE,
        (
            "在导力商店关门之前，\x01",
            "得赶快去买个\x01",
            "新的感光回路。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A00")

    Jump("loc_3DEF")

    label("loc_3A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ABE")

    #C0112
    ChrTalk(
        0xFE,
        (
            "揭幕式结束以后，\x01",
            "我去拍了很多\x01",
            "兰花塔的照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "哎呀呀，话说回来，\x01",
            "那真是个相当巨大的建筑物啊。\x01",
            "高达四十层吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        "哎呀，真想把照片赶快显像出来啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B10")

    label("loc_3ABE")


    #C0115
    ChrTalk(
        0xFE,
        (
            "我拍了很多\x01",
            "兰花塔的照片呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "那座建筑物大概会\x01",
            "成为克洛斯贝尔的新象征吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B10")

    Jump("loc_3DEF")

    label("loc_3B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BAD")

    #C0117
    ChrTalk(
        0xFE,
        "通商会议已经临近了。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "各国要人将会来访，\x01",
            "同时还将举行市政厅大楼\x01",
            "的揭幕式……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "一定不能错过\x01",
            "抓拍好镜头的机会啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C07")

    label("loc_3BAD")


    #C0120
    ChrTalk(
        0xFE,
        "各国要人的来访，还有揭幕式……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "在通商会议中，\x01",
            "一定不能错过\x01",
            "抓拍好镜头的机会啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C07")

    Jump("loc_3DEF")

    label("loc_3C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3C89")

    #C0122
    ChrTalk(
        0xFE,
        (
            "唔，和平时相比，\x01",
            "下雨天的景色另有一番风味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "在下雨天摄影，需要相当\x01",
            "高超的技巧……\x01",
            "不过这也很有趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DEF")

    label("loc_3C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3DEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D4F")

    #C0124
    ChrTalk(
        0xFE,
        (
            "西克洛斯贝尔街道\x01",
            "中有个名为『诺克斯森林地带』\x01",
            "的场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "那里林木茂密，\x01",
            "应该是个很不错的\x01",
            "摄影地点……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "但由于警察学校坐落在那个地方，\x01",
            "所以一般人是不得入内的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DEF")

    label("loc_3D4F")


    #C0127
    ChrTalk(
        0xFE,
        (
            "拍摄照片是我的爱好。\x01",
            "为了寻找优秀的拍摄对象，\x01",
            "我会前往各种各样的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "虽然『诺克斯森林地带』\x01",
            "禁止一般人入内，\x01",
            "但如果以后有机会，真想去那里拍些照片。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DEF")

    TalkEnd(0xFE)
    Return()

    # Function_19_30F2 end

    def Function_20_3DF3(): pass

    label("Function_20_3DF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3EEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E93")

    #C0129
    ChrTalk(
        0xFE,
        (
            "好久没喝『摩尔吉』\x01",
            "的咖啡了。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "总之……\x01",
            "希望克洛斯贝尔从此能\x01",
            "慢慢恢复正常。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "……不过，那棵巨大的树\x01",
            "实在是让人担心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EE9")

    label("loc_3E93")


    #C0132
    ChrTalk(
        0xFE,
        (
            "希望克洛斯贝尔从此能\x01",
            "慢慢恢复正常。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "……不过，那棵巨大的树\x01",
            "实在是让人担心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE9")

    Jump("loc_459E")

    label("loc_3EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3EFC")
    Jump("loc_459E")

    label("loc_3EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3FD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA9")

    #C0134
    ChrTalk(
        0xFE,
        (
            "最近这期克洛斯贝尔时代周刊\x01",
            "上的报道真是让我震惊……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "没想到竟然会\x01",
            "公然发表那种敌视\x01",
            "两大国的演说啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "真担心克洛斯贝尔\x01",
            "今后的局势……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3FCE")

    label("loc_3FA9")


    #C0137
    ChrTalk(
        0xFE,
        (
            "真担心克洛斯贝尔\x01",
            "今后的局势……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FCE")

    Jump("loc_459E")

    label("loc_3FD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4040")

    #C0138
    ChrTalk(
        0xFE,
        (
            "这一带基本没有\x01",
            "遭到破坏，\x01",
            "算是不幸中的万幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "行政区和港湾区的状况\x01",
            "似乎是最惨重的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_4040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4081")

    #C0140
    ChrTalk(
        0xFE,
        (
            "被武装集团占领了吗……\x01",
            "真担心玛因兹的人啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_4081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_408F")
    Jump("loc_459E")

    label("loc_408F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_40BE")

    #C0141
    ChrTalk(
        0xFE,
        (
            "今天看到了很多\x01",
            "急救车呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_40BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_412C")

    #C0142
    ChrTalk(
        0xFE,
        (
            "捉迷藏吗……\x01",
            "我以前也经常玩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "每当看到这些开心玩耍的小孩子，\x01",
            "心情就会变得很愉快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_412C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4251")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41EA")

    #C0144
    ChrTalk(
        0xFE,
        (
            "市长所提议的\x01",
            "克洛斯贝尔独立……\x01",
            "真是个很复杂的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "不然也去问问普鲁娜和利娜莉\x01",
            "的意见吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "……还是算了，\x01",
            "她们两个应该不会\x01",
            "用心思考这种问题……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_424C")

    label("loc_41EA")


    #C0147
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔独立……\x01",
            "真是个很复杂的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "看看克洛斯贝尔时代周刊，\x01",
            "然后仔细思考一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_424C")

    Jump("loc_459E")

    label("loc_4251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_42F1")

    #C0149
    ChrTalk(
        0xFE,
        (
            "『帝国时报社』和\x01",
            "雷米菲利亚的『热点报道』\x01",
            "好像也要报道会议状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "话说回来，还真想看看\x01",
            "他们写的报道，\x01",
            "然后和克洛斯贝尔时代周刊比较一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_42F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4370")

    #C0151
    ChrTalk(
        0xFE,
        (
            "在这里边喝咖啡边看书，\x01",
            "不知不觉就已经这么晚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "（抖）……\x01",
            "晚上果然很冷啊，\x01",
            "趁着还没感冒，赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_4370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4408")

    #C0153
    ChrTalk(
        0xFE,
        (
            "雷米菲利亚的阿尔伯特大公\x01",
            "好像是出资建设乌尔斯拉\x01",
            "医科大学的赞助人之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "听说麦克道尔议长\x01",
            "从很久以前开始一直\x01",
            "和大公保持友好往来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_4408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_454E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44D4")

    #C0155
    ChrTalk(
        0xFE,
        (
            "西塞姆里亚通商会议……\x01",
            "最近总能在克洛斯贝尔时代周刊\x01",
            "上看到这件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "听说会议的中心\x01",
            "是经济方面的问题，\x01",
            "具体将会有怎样的议题呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "唔，下次还是仔细问问\x01",
            "玛布尔老师吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4549")

    label("loc_44D4")


    #C0158
    ChrTalk(
        0xFE,
        (
            "西塞姆里亚通商会议……\x01",
            "只知道那是经济方面的会议，\x01",
            "具体都会谈些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "唔，下次还是仔细问问\x01",
            "玛布尔老师吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4549")

    Jump("loc_459E")

    label("loc_454E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_455C")
    Jump("loc_459E")

    label("loc_455C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_459E")

    #C0160
    ChrTalk(
        0xFE,
        (
            "今天傍晚有\x01",
            "主日学校的课。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "一定不能忘了带作业。\x02",
    )

    CloseMessageWindow()

    label("loc_459E")

    TalkEnd(0xFE)
    Return()

    # Function_20_3DF3 end

    def Function_21_45A2(): pass

    label("Function_21_45A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_45F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C0")
    Call(0, 17)
    Jump("loc_45F3")

    label("loc_45C0")


    #C0162
    ChrTalk(
        0xFE,
        (
            "我要和隆他们一起，\x01",
            "在市里帮助有困难的人……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45F3")

    Jump("loc_4832")

    label("loc_45F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4606")
    Jump("loc_4832")

    label("loc_4606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4614")
    Jump("loc_4832")

    label("loc_4614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4622")
    Jump("loc_4832")

    label("loc_4622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_465D")

    #C0163
    ChrTalk(
        0xFE,
        (
            "啊、啊啊……\x01",
            "我很不擅长追着跑的游戏……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4832")

    label("loc_465D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_466B")
    Jump("loc_4832")

    label("loc_466B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_46F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C5")

    #C0164
    ChrTalk(
        0xFE,
        (
            "终于找到了\x01",
            "亨利……！\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "好……\x01",
            "接下来要把\x01",
            "隆也找到……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_46F0")

    label("loc_46C5")


    #C0166
    ChrTalk(
        0xFE,
        (
            "不过，实在想不到\x01",
            "隆会躲在什么地方……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46F0")

    Jump("loc_4832")

    label("loc_46F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4794")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4766")

    #C0167
    ChrTalk(
        0xFE,
        (
            "我正在与隆和亨利\x01",
            "玩捉迷藏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "可是根本找不到他们……\x01",
            "到底藏到哪里了呢……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_478F")

    label("loc_4766")


    #C0169
    ChrTalk(
        0xFE,
        (
            "隆和亨利到底\x01",
            "藏到什么地方了呢……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_478F")

    Jump("loc_4832")

    label("loc_4794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47A2")
    Jump("loc_4832")

    label("loc_47A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47B0")
    Jump("loc_4832")

    label("loc_47B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_47BE")
    Jump("loc_4832")

    label("loc_47BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47CC")
    Jump("loc_4832")

    label("loc_47CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_481B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E7")
    Call(0, 16)
    Jump("loc_4816")

    label("loc_47E7")


    #C0170
    ChrTalk(
        0xFE,
        (
            "大家明天要在\x01",
            "百货店集合。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        "好期待……\x02",
    )

    CloseMessageWindow()

    label("loc_4816")

    Jump("loc_4832")

    label("loc_481B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4829")
    Jump("loc_4832")

    label("loc_4829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4832")

    label("loc_4832")

    TalkEnd(0xFE)
    Return()

    # Function_21_45A2 end

    def Function_22_4836(): pass

    label("Function_22_4836")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4847")
    Jump("loc_4D2B")

    label("loc_4847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4855")
    Jump("loc_4D2B")

    label("loc_4855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4863")
    Jump("loc_4D2B")

    label("loc_4863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4871")
    Jump("loc_4D2B")

    label("loc_4871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_48D0")

    #C0172
    ChrTalk(
        0xFE,
        "矿、矿山镇竟然被占领了……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "真让人害怕啊……\x01",
            "小桃怎么还不快点回家呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D2B")

    label("loc_48D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_48DE")
    Jump("loc_4D2B")

    label("loc_48DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_492D")

    #C0174
    ChrTalk(
        0xFE,
        (
            "从刚才开始，不断有\x01",
            "急救车来来往往。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        "发生什么事了……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D2B")

    label("loc_492D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4977")

    #C0176
    ChrTalk(
        0xFE,
        (
            "伊安律师好像\x01",
            "非常忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "今天也出入事务所\x01",
            "很多次。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D2B")

    label("loc_4977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A0D")

    #C0178
    ChrTalk(
        0xFE,
        (
            "自从通商会议召开之后，\x01",
            "我和老公多次\x01",
            "认真讨论了有关独立的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "因为这个问题关系到\x01",
            "我们克洛斯贝尔的所有居民，\x01",
            "必须要用心思考。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D2B")

    label("loc_4A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A1B")
    Jump("loc_4D2B")

    label("loc_4A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4A29")
    Jump("loc_4D2B")

    label("loc_4A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ABB")

    #C0180
    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "小桃今天和朋友们一起去看\x01",
            "揭幕式了。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "呵呵，等她回来以后，\x01",
            "一定要让她给我\x01",
            "好好讲讲今天的见闻。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4B03")

    label("loc_4ABB")


    #C0183
    ChrTalk(
        0xFE,
        (
            "小桃今天和朋友们一起去看\x01",
            "揭幕式了。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "呵呵，希望她能\x01",
            "玩的开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B03")

    Jump("loc_4D2B")

    label("loc_4B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C0A")

    #C0185
    ChrTalk(
        0xFE,
        (
            "不久前的一个下雨天，\x01",
            "小桃去帮我买东西，\x01",
            "结果好久都不回来，让我担心死了。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "问过她之后，\x01",
            "才知道是把伞弄丢了，一直在找。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "小桃可真是的，不过就是一把伞而已，\x01",
            "买把新的不就行了嘛……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "只要别让我担心，\x01",
            "那种东西不算什么。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4C6D")

    label("loc_4C0A")


    #C0189
    ChrTalk(
        0xFE,
        (
            "不过，珍惜东西\x01",
            "是种很好的品性。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "虽然让家长担心是不好的，\x01",
            "但希望小桃能一直\x01",
            "保持这种品性。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C6D")

    Jump("loc_4D2B")

    label("loc_4C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4C80")
    Jump("loc_4D2B")

    label("loc_4C80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4D2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CE9")

    #C0191
    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "这里就是为本地居民\x01",
            "提供各种日常用品的\x01",
            "『塔利兹商店』哦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D2B")

    label("loc_4CE9")


    #C0193
    ChrTalk(
        0xFE,
        (
            "小桃去主日学校\x01",
            "努力学习了……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "我们也一定要加油\x01",
            "工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D2B")

    TalkEnd(0xFE)
    Return()

    # Function_22_4836 end

    def Function_23_4D2F(): pass

    label("Function_23_4D2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D40")
    Jump("loc_5327")

    label("loc_4D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4D4E")
    Jump("loc_5327")

    label("loc_4D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4DCA")

    #C0195
    ChrTalk(
        0xFE,
        (
            "从今天早上开始，我看到\x01",
            "很多开往边境大门方向的导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "看样子，是那些滞留在此地\x01",
            "的外国人纷纷回国了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5327")

    label("loc_4DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4DD8")
    Jump("loc_5327")

    label("loc_4DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4DE6")
    Jump("loc_5327")

    label("loc_4DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4DF4")
    Jump("loc_5327")

    label("loc_4DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4F37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB9")

    #C0197
    ChrTalk(
        0xFE,
        (
            "我们去贝尔加德门\x01",
            "那边兜风回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "在归途中看到了\x01",
            "西克洛斯贝尔街道的事故现场……\x01",
            "那里真是一片混乱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "竟然会发生那种惊人的脱轨事故，\x01",
            "我真是连想都没想过……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4F32")

    label("loc_4EB9")


    #C0200
    ChrTalk(
        0xFE,
        (
            "我们在兜风的归途中看到了\x01",
            "西克洛斯贝尔街道的事故现场……\x01",
            "那里真是一片混乱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "有很多警察和警备队员\x01",
            "聚集在那里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F32")

    Jump("loc_5327")

    label("loc_4F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4F45")
    Jump("loc_5327")

    label("loc_4F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F53")
    Jump("loc_5327")

    label("loc_4F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F61")
    Jump("loc_5327")

    label("loc_4F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4F6F")
    Jump("loc_5327")

    label("loc_4F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_50B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_503B")

    #C0202
    ChrTalk(
        0xFE,
        (
            "老婆子生气了，\x01",
            "怎么哄都哄不好。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "难得邀请她一起去\x01",
            "观看揭幕式，\x01",
            "竟然无视我。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "一边欣赏烟花一边品尝葡萄酒，\x01",
            "绝对是至高的享受，可她却……\x01",
            "唉，真是个不解风情的女人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_50B4")

    label("loc_503B")


    #C0205
    ChrTalk(
        0xFE,
        (
            "哼，这算什么啊。\x01",
            "只不过是买了件高价的东西而已，\x01",
            "要唠叨我到什么时候啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "既然老婆子如此固执，\x01",
            "我不理她就是了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50B4")

    Jump("loc_5327")

    label("loc_50B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_50C7")
    Jump("loc_5327")

    label("loc_50C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_50D5")
    Jump("loc_5327")

    label("loc_50D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52D7")

    #C0207
    ChrTalk(
        0xFE,
        (
            "呵呵呵，\x01",
            "导力车果然是好东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "虽然老婆子\x01",
            "一直说我浪费钱财，\x01",
            "但买下它真是正确的决定。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x109,
        (
            "#10109F乌尔努公司制造的导力车……\x01",
            "外观雅致，\x01",
            "是种很不错的车型呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "哦，真是难得啊……\x01",
            "年纪轻轻，却很有见识。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_520C")
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    label("loc_520C")

    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5235")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5235")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_525B")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_525B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5281")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5281")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52A7")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_52A7")

    Sleep(1000)

    #C0211
    ChrTalk(
        0x101,
        "#00012F（他们好像很说得来……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5327")

    label("loc_52D7")


    #C0212
    ChrTalk(
        0xFE,
        (
            "驾驶这辆导力车出去兜风\x01",
            "真是最高享受。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "真希望老婆子\x01",
            "也能明白这一点啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5327")

    TalkEnd(0xFE)
    Return()

    # Function_23_4D2F end

    def Function_24_532B(): pass

    label("Function_24_532B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_533C")
    Jump("loc_536E")

    label("loc_533C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_536E")

    #C0214
    ChrTalk(
        0xFE,
        (
            "总觉得很不安呢……\x01",
            "是发生事故了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_536E")

    TalkEnd(0xFE)
    Return()

    # Function_24_532B end

    def Function_25_5372(): pass

    label("Function_25_5372")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5383")
    Jump("loc_53AE")

    label("loc_5383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_53AE")

    #C0215
    ChrTalk(
        0xFE,
        "我不是很喜欢急救车的声音……\x02",
    )

    CloseMessageWindow()

    label("loc_53AE")

    TalkEnd(0xFE)
    Return()

    # Function_25_5372 end

    def Function_26_53B2(): pass

    label("Function_26_53B2")

    TalkBegin(0xFE)

    #C0216
    ChrTalk(
        0xFE,
        (
            "在看到列车脱轨的时候，\x01",
            "我甚至都怀疑自己的眼睛。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "好像有很多人\x01",
            "都负伤了，\x01",
            "他们不要紧吧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_53B2 end

    def Function_27_541C(): pass

    label("Function_27_541C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5492")

    #C0218
    ChrTalk(
        0xFE,
        (
            "真是的，不知不觉间，\x01",
            "鞋子里就湿成\x01",
            "一片了！\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "所以我很讨厌下雨。\x01",
            "赶快把事情办完，早点回家吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54EC")

    label("loc_5492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_54EC")

    #C0220
    ChrTalk(
        0xFE,
        (
            "唉，真是的……下雨好讨厌！\x01",
            "让人心情郁闷。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        "赶快把事情办完，早点回家吧。\x02",
    )

    CloseMessageWindow()

    label("loc_54EC")

    TalkEnd(0xFE)
    Return()

    # Function_27_541C end

    def Function_28_54F0(): pass

    label("Function_28_54F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55ED")

    #C0222
    ChrTalk(
        0xFE,
        (
            "竟然发生了\x01",
            "那样的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "虽然我的力量微不足道，\x01",
            "但还是要认真做好警戒工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "假如袭击事件的幕后真凶真是帝国，\x01",
            "短时间内再次前来袭击\x01",
            "的可能性应该也很低……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "话虽如此，\x01",
            "但在三天后的居民投票日之前，\x01",
            "还是不能放松警惕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5681")

    label("loc_55ED")


    #C0226
    ChrTalk(
        0xFE,
        (
            "假如袭击事件的幕后真凶真是帝国，\x01",
            "短时间内再次前来袭击\x01",
            "的可能性应该也很低……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "话虽如此，\x01",
            "但在三天后的居民投票日之前，\x01",
            "还是不能放松警惕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5681")

    TalkEnd(0xFE)
    Return()

    # Function_28_54F0 end

    def Function_29_5685(): pass

    label("Function_29_5685")

    TalkBegin(0xFF)

    #C0228
    ChrTalk(
        0x101,
        (
            "#00005F赛尔盖科长好像\x01",
            "在为支援科建造什么东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x102,
        (
            "#00104F总之，\x01",
            "还是不要从这里走了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_29_5685 end

    def Function_30_56EA(): pass

    label("Function_30_56EA")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门紧紧关闭着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5730")
    TalkEnd(0xFF)
    Call(0, 31)
    Return()

    label("loc_5730")

    TalkEnd(0xFF)
    Return()

    # Function_30_56EA end

    def Function_31_5734(): pass

    label("Function_31_5734")

    EventBegin(0x0)
    Fade(1000)
    OP_68(15530, 4300, 15700, 0)
    MoveCamera(60, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13270, 0)
    SetChrPos(0x101, 15530, 3000, 15700, 90)
    SetChrPos(0x102, 14820, 3000, 16800, 90)
    SetChrPos(0x103, 13710, 3000, 16700, 90)
    SetChrPos(0x104, 12510, 3000, 15490, 90)
    SetChrPos(0xF4, 13100, 3000, 14500, 90)
    SetChrPos(0xF5, 14690, 3000, 14290, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0231
    ChrTalk(
        0x101,
        (
            "#6P#00008F…………………………………………\x02\x03",

            "#00003F（根据尼尔森先生的分析，\x01",
            "  还有皮特和昆特先生说过的话……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_587E")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_587E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58A4")
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_58A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58CA")
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_58CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58F0")
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_58F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5916")
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_5916")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_593C")
    OP_63(0x5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_593C")

    Sleep(1000)

    def lambda_5944():
        TurnDirection(0x102, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5944)
    Sleep(50)

    def lambda_5954():
        TurnDirection(0x103, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5954)

    def lambda_5961():
        TurnDirection(0x104, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5961)
    Sleep(50)

    def lambda_5971():
        TurnDirection(0xF4, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_5971)
    Sleep(50)

    def lambda_5981():
        TurnDirection(0xF5, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_5981)
    WaitChrThread(0xF5, 2)

    #C0232
    ChrTalk(
        0x102,
        "#6P#00105F罗伊德……怎么了？\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        (
            "#6P#00200F伊安律师的事务所\x01",
            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        "#6P#00301F现在似乎没人在……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    OP_93(0x101, 0x111, 0x1F4)

    #C0235
    ChrTalk(
        0x101,
        (
            "#11P#00006F……不，没什么。\x01",
            "我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A8B")

    #C0236
    ChrTalk(
        0x10A,
        "#12P#00605F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_5A8B")

    OP_5A()
    SetScenarioFlags(0x1BE, 0)
    OP_2C(0xB1, 0x3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_31_5734 end

    def Function_32_5AAB(): pass

    label("Function_32_5AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AC2")
    Call(0, 49)
    Return()

    label("loc_5AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AD4")
    Call(0, 50)
    Return()

    label("loc_5AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B26")

    #C0237
    ChrTalk(
        0x101,
        (
            "#00000F现在并无需要前往市外的任务，\x01",
            "好像没有驾驶车辆的必要啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_5B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C18")
    CreatePortrait(0, 67, 20, 547, 276, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis241.itp")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0238
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※支援科的车辆已经可以使用了。\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0x80FFFFFF, 0x1F4, 0x0, 0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0x12B, 2)
    SetScenarioFlags(0x31, 1)
    OP_C9(0x1, 0x200000)

    label("loc_5C18")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C33")
    Jump("loc_5CA3")

    label("loc_5C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C42")
    Jump("loc_5CA3")

    label("loc_5C42")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C5D")
    SetScenarioFlags(0x31, 2)

    label("loc_5C5D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5CA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_5C9D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C92")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_5C98")

    label("loc_5C92")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_5C98")

    Jump("loc_5CA3")

    label("loc_5C9D")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_5CA3")

    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_605F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_5D2B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5D0B"),
        (SWITCH_DEFAULT, "loc_5D1C"),
    )


    label("loc_5D0B")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_5D26")

    label("loc_5D1C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D26")

    Jump("loc_605A")

    label("loc_5D2B")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_5D83")
    MenuCmd(1, 0, "在导力车内休息")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5D83")

    MenuCmd(1, 0, "改装导力车")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E16")

    #C0239
    ChrTalk(
        0x101,
        (
            "#00003F导力车就停放在这里。\x02\x03",

            "#00001F在作战开始之前，\x01",
            "我们先去车站吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FC0")

    label("loc_5E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E6E")

    #C0240
    ChrTalk(
        0x101,
        (
            "#00001F现在必须要尽快\x01",
            "调查兰迪的行踪，\x01",
            "先在市内展开彻底调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FC0")

    label("loc_5E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EC1")

    #C0241
    ChrTalk(
        0x101,
        (
            "#00000F现在并无需要前往市外的任务，\x01",
            "好像没有驾驶车辆的必要啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FC0")

    label("loc_5EC1")

    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EF2")
    OP_70(0xA, 0x12C)
    OP_71(0xA, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_5F02")

    label("loc_5EF2")

    OP_70(0xA, 0xF0)
    OP_71(0xA, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_5F02")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F58")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F58")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F7B")
    Sound(461, 0, 100, 0)

    label("loc_5F7B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F9B")
    OP_70(0xA, 0x14A)
    OP_71(0xA, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_5FAB")

    label("loc_5F9B")

    OP_70(0xA, 0x10E)
    OP_71(0xA, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_5FAB")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0xA, "light", 0x1, 0x1)
    OP_70(0xA, 0x0)

    label("loc_5FC0")

    Jump("loc_605A")

    label("loc_5FC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_603B")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_5FFE")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_6016")

    label("loc_5FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_6011")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_6016")

    label("loc_6011")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_6016")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_605A")

    label("loc_603B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6050")
    Call(0, 33)
    Jump("loc_605A")

    label("loc_6050")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_605A")

    Jump("loc_5CBA")

    label("loc_605F")

    SetMapObjFrame(0xA, "light", 0x1, 0x1)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_32_5AAB end

    def Function_33_6075(): pass

    label("Function_33_6075")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF000000), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60BB")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_60BB")

    SetMapObjFrame(0xFF, "main7", 0x0, 0x1)
    MiniGame(0x33, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFrame(0xFF, "main7", 0x1, 0x1)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6124")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_6124")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    SetMapFlags(0x80)
    Return()

    # Function_33_6075 end

    def Function_34_6136(): pass

    label("Function_34_6136")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_6191")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6186")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_618C")

    label("loc_6186")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_618C")

    Jump("loc_61B5")

    label("loc_6191")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_61AF")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_61B5")

    label("loc_61AF")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_61B5")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_34_6136 end

    def Function_35_61CA(): pass

    label("Function_35_61CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_68(40100, -2850, -19150, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18000, 0)
    OP_68(25400, -2250, -16450, 10000)
    MoveCamera(40, 30, 0, 10000)
    SetCameraDistance(24000, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0180", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_61CA end

    def Function_36_6275(): pass

    label("Function_36_6275")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x1A5, 0x4)
    SetChrPos(0x101, 43000, -4000, -18500, 270)
    SetChrPos(0x102, 43200, -4000, -19600, 270)
    SetChrPos(0x105, 44200, -4000, -18500, 270)
    SetChrPos(0x109, 44400, -4000, -19600, 270)
    SetChrPos(0x1A5, 46400, -4000, -19000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(20000, -1500, -18000, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    OP_68(28000, -1500, -18000, 6000)
    SetCameraDistance(23000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x5)
    Fade(500)
    OP_68(39500, -3100, -19000, 0)
    MoveCamera(53, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18000, 2500)

    def lambda_63D6():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_63D6)
    Sleep(100)

    def lambda_63F3():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_63F3)
    Sleep(300)

    def lambda_6410():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6410)
    Sleep(100)

    def lambda_6424():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6424)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x102, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6471():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6471)
    Sleep(100)

    def lambda_648E():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_648E)
    Sleep(100)

    def lambda_64AB():
        OP_97(0x1A5, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A5, 0, lambda_64AB)
    Sleep(800)

    def lambda_64C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_64C8)
    Sleep(100)

    def lambda_64DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_64DC)
    Sleep(1000)

    def lambda_64F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A5, 2, lambda_64F0)
    OP_6F(0x79)

    #C0242
    ChrTalk(
        0x101,
        "#00005F#5P这是……\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x102,
        "#11P#00105F什、什么时候变成这样的？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0244
    ChrTalk(
        0x109,
        (
            "#10105F#11P哎，支援科的后门\x01",
            "原来是这样的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x105,
        (
            "#10302F#5P嘿，看样子，\x01",
            "似乎像是个建筑工地啊。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1A5, 0)

    #C0246
    ChrTalk(
        0x1A5,
        (
            "#11P#01105F哦，对了，\x01",
            "大家还不知道呢。\x02\x03",

            "#01100F那个……罗伊德出差之后，\x01",
            "来了几个建筑工人。\x02\x03",

            "好像是科长叫来的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6629():
        TurnDirection(0x101, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6629)
    Sleep(50)

    def lambda_6639():
        TurnDirection(0x102, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6639)
    Sleep(50)

    def lambda_6649():
        TurnDirection(0x105, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6649)
    Sleep(50)

    def lambda_6659():
        TurnDirection(0x109, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6659)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0247
    ChrTalk(
        0x101,
        (
            "#6P#00006F这样啊……\x01",
            "昨天都没注意到呢。\x02\x03",

            "#00001F不过，科长究竟\x01",
            "要做什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#6P#00103F唔……在这里开工，\x01",
            "肯定有某种理由吧……\x02\x03",

            "#00100F总之，我们就\x01",
            "不要从这里走了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#6P#00000F嗯，从一层的正门出去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x1A5, 0x4)
    SetScenarioFlags(0x126, 3)
    EventEnd(0x5)
    NewScene("c0110", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_36_6275 end

    def Function_37_677E(): pass

    label("Function_37_677E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    LoadChrToIndex("chr/ch02710.itc", 0x1F)
    LoadChrToIndex("apl/ch51107.itc", 0x20)
    SoundLoad(468)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01200.itp")
    OP_68(18000, 1660, -9000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 19000, 0, -8600, 180)
    SetChrPos(0x102, 19000, 0, -8600, 180)
    SetChrPos(0x109, 19000, 0, -8600, 180)
    SetChrPos(0x105, 19000, 0, -8600, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 19000, 0, -8600, 180)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12500, 0, 500, 270)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x2)
    SetChrSubChip(0x16, 0x29)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 42450, 2400, -22230, 315)
    SetChrFlags(0x16, 0x8)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 10050, 0, -8400, 90)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 9350, 0, -6250, 90)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0x19, 0x80)
    OP_78(0xA, 0x19)
    OP_49()
    SetChrPos(0x19, -36200, 0, 4000, 90)
    OP_D5(0x19, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kabuse", 0x0, 0x1)
    SetMapObjFlags(0xC, 0x4)
    SetChrFlags(0xB, 0x8)
    FadeToBright(1000, 0)
    Sound(468, 2, 80, 0)
    Sound(457, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 38)
    OP_68(-27750, 4250, 6400, 0)
    MoveCamera(69, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(-27750, 1250, 6400, 7500)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    EndChrThread(0x19, 0x3)
    Sound(459, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 39)
    BeginChrThread(0x1A, 1, 0, 45)
    OP_68(1950, 2350, -8400, 0)
    MoveCamera(22, 26, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13650, 0)
    OP_68(18950, 2350, -8400, 7500)
    MoveCamera(22, 7, 0, 7500)
    OP_6F(0x79)
    WaitChrThread(0x19, 3)
    OP_0D()
    Sleep(500)

    #C0250
    ChrTalk(
        0x101,
        "#00005F#5P啊……\x02",
    )

    CloseMessageWindow()
    OP_68(23200, 450, -21750, 3500)
    MoveCamera(30, 26, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(19850, 3500)
    OP_6F(0x79)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(462, 0, 100, 0)
    Sleep(1000)
    OP_68(19430, 800, -10000, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14350, 0)
    FadeToBright(1000, 0)
    OP_68(19430, 800, -8970, 2000)
    SetChrPos(0x101, 19600, 0, -10400, 180)
    SetChrPos(0x102, 20900, 0, -9500, 180)
    SetChrPos(0x109, 19600, 0, -9050, 180)
    SetChrPos(0x105, 18300, 0, -9950, 180)
    SetChrPos(0x14, 17550, 0, -8850, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_70(0xA, 0x10E)
    OP_6F(0x79)
    OP_0D()

    #C0251
    ChrTalk(
        0x14,
        "#01002F#5P嗯，建造得不错啊。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        "#00002F#5P科长，这是……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        (
            "#00102F#5P莫非是为\x01",
            "这辆导力车造的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x14,
        (
            "#01004F#5P嗯，建设了斜坡路面\x01",
            "和停车空间。\x02\x03",

            "#01004F建造费用都由\x01",
            "警察总部来出。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x109,
        (
            "#10102F#5P嘿……真棒啊！\x02\x03",

            "#10109F既然有这么充足的空间，\x01",
            "连检修改装导力车应该都可以在这里完成呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x105,
        (
            "#10302F#5P呵呵，这就是有车生活吗，\x01",
            "看样子好像很不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x101,
        (
            "#00004F#5P哈哈……琪雅看到以后，\x01",
            "大概会高兴得跳起来吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)

    #N0258
    NpcTalk(
        0x8,
        "男孩的声音",
        "哇～这是什么啊！？\x02",
    )

    CloseMessageWindow()

    #N0259
    NpcTalk(
        0x9,
        "男孩的声音",
        "好漂亮的车……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6E7F():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6E7F)
    Sleep(50)

    def lambda_6E8F():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6E8F)
    Sleep(50)

    def lambda_6E9F():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6E9F)
    Sleep(50)

    def lambda_6EAF():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6EAF)
    Sleep(50)

    def lambda_6EBF():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6EBF)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x14, 0)
    Fade(500)
    OP_68(13350, 800, -8750, 0)
    MoveCamera(30, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15800, 0)
    OP_68(18150, 800, -8750, 3000)
    SetCameraDistance(13800, 3000)

    def lambda_6F30():
        OP_96(0xFE, 0x3C8C, 0x0, 0xFFFFDAE4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6F30)

    def lambda_6F4A():
        OP_96(0xFE, 0x3BC4, 0x0, 0xFFFFE08E, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6F4A)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()

    #C0260
    ChrTalk(
        0x101,
        "#00002F#11P呀，是隆和亨利啊。\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        "#00109F#11P呵呵，又见面啦。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "#6P好棒啊！\x01",
            "从没见过这样的导力车！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        (
            "#6P大哥哥，这辆车难道\x01",
            "是你们买的吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#00004F#11P哈哈，不是啦。\x02\x03",

            "#00002F不过，以后会由\x01",
            "支援科来使用。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0265
    ChrTalk(
        0x9,
        "#6P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "#6P大哥哥，你们什么时候\x01",
            "混得这么出人头地了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#00012F#11P哪里，并没\x01",
            "出人头地啦……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0268
    ChrTalk(
        0x101,
        (
            "#00000F#11P对了，琪雅今天\x01",
            "没和你们在一起啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x102,
        (
            "#00100F#11P她是不是和\x01",
            "小桃在一起？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0270
    ChrTalk(
        0x8,
        "#6P不知道呢。\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#6P我们没有一起\x01",
            "从主日学校回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        "#00005F#11P哎，这样啊？\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x9,
        (
            "#6P琪雅被玛布尔老师留下了，\x01",
            "好像是有什么事。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x9,
        (
            "#6P说不定她还在\x01",
            "大圣堂呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#00001F#11P是吗……\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        "#00108F#11P这是怎么回事呢……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    def lambda_729A():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_729A)
    Sleep(50)

    def lambda_72AA():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_72AA)
    Sleep(50)

    def lambda_72BA():
        TurnDirection(0x14, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_72BA)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x14, 0)
    OP_64(0x101)
    OP_64(0x102)

    #C0277
    ChrTalk(
        0x105,
        (
            "#10302F#6P哎呀呀，你们还是\x01",
            "这么过度保护啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x109,
        (
            "#10109F#5P小琪雅实在太可爱了，\x01",
            "这也没办法嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#00012F#11P哪、哪里……\x01",
            "我觉得并没有过度保护啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        (
            "#00112F#11P是、是啊，\x01",
            "这只是监护人的正常保护范畴。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x14,
        (
            "#01004F#6P呵呵，既然你们那么担心，\x01",
            "不如就去大圣堂接她吧？\x02\x03",

            "#01002F正好现在有了座驾。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0282
    ChrTalk(
        0x101,
        "#00000F#11P啊，说的也是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0283
    ChrTalk(
        0x102,
        "#00102F#11P诺艾尔小姐，可以拜托你来驾驶吗？\x02",
    )

    CloseMessageWindow()

    def lambda_7488():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7488)
    Sleep(50)

    def lambda_7498():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7498)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    #C0284
    ChrTalk(
        0x109,
        "#10102F#5P嗯，没问题。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#6P什、什么！？\x01",
            "要去接琪雅吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "#6P我也要去！\x01",
            "让我也坐上去吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7516():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7516)
    Sleep(15)

    def lambda_7526():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7526)
    Sleep(15)

    def lambda_7536():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7536)
    Sleep(15)

    def lambda_7546():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7546)
    Sleep(15)

    def lambda_7556():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7556)
    Sleep(15)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x14, 0)
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x9, 0x8, 500)

    #C0287
    ChrTalk(
        0x9,
        "#5P等、等一下啊，隆！\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x9,
        (
            "#5P叔叔不是让你\x01",
            "早点回家吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0289
    ChrTalk(
        0x8,
        "#12P呜，差点忘了。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "#12P因为姐姐今天\x01",
            "难得回家一次……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#00004F#11P哈哈，那你可要\x01",
            "早点回家才行啊。\x02\x03",

            "#00002F下次再带你们\x01",
            "两个一起坐车。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_766A():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_766A)
    Sleep(50)

    def lambda_767A():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_767A)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    #C0292
    ChrTalk(
        0x8,
        "#6P说、说话算数啊！\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x9,
        (
            "#6P那我们就先\x01",
            "走啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x102,
        "#00109F#11P呵呵，路上小心啊。\x02",
    )

    CloseMessageWindow()

    def lambda_76E8():
        OP_93(0x8, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_76E8)
    Sleep(50)

    def lambda_76F8():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_76F8)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    OP_68(19000, 800, -8750, 2500)

    def lambda_7721():
        OP_96(0xFE, 0x2742, 0x0, 0xFFFFDF30, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7721)
    Sleep(50)

    def lambda_773E():
        OP_96(0xFE, 0x2486, 0x0, 0xFFFFE796, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_773E)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    OP_93(0x14, 0x87, 0x1F4)

    #C0295
    ChrTalk(
        0x14,
        (
            "#01003F#5P好，那你们就\x01",
            "赶快出发吧。\x02\x03",

            "#01000F我先回去了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_77B1():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_77B1)
    Sleep(50)

    def lambda_77C1():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_77C1)
    Sleep(50)

    def lambda_77D1():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_77D1)
    Sleep(50)

    def lambda_77E1():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_77E1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0296
    ChrTalk(
        0x101,
        "#00000F#12P嗯，知道了。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        "#00100F#11P那我们就出发吧。\x02",
    )

    CloseMessageWindow()
    OP_68(19000, 800, -9350, 2500)

    def lambda_7850():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7850)

    def lambda_785D():
        OP_93(0xFE, 0xB4, 0xFA)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_785D)

    def lambda_786A():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_786A)

    def lambda_7877():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7877)
    OP_93(0x14, 0xB4, 0x1F4)
    OP_96(0x14, 0x43C6, 0x0, 0xFFFFD27E, 0x9C4, 0x1)
    OP_96(0x14, 0x4A38, 0xFFFFF9C0, 0xFFFFC022, 0x9C4, 0x1)
    SetChrFlags(0x14, 0x80)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    #C0298
    ChrTalk(
        0x109,
        (
            "#10104F#5P呵呵，是要前往\x01",
            "大圣堂吧？\x02\x03",

            "#10100F如果从这里出发，就要从\x01",
            "中央广场向欢乐街方向行驶。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_792D():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_792D)
    Sleep(50)

    def lambda_793D():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_793D)
    Sleep(50)

    def lambda_794D():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_794D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    #C0299
    ChrTalk(
        0x101,
        (
            "#00002F#12P好的，拜托你了。\x02\x03",

            "#00004F……嗯，琪雅的惊讶面孔\x01",
            "好像已经浮现在我的眼前了。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        (
            "#00109F#12P呵呵，那孩子\x01",
            "很喜欢导力车呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x105,
        (
            "#10302F#6P哎呀呀，真是\x01",
            "溺爱孩子的父母啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(19000, 800, -6740, 6000)
    MoveCamera(45, 18, 0, 6000)
    Sleep(250)
    BeginChrThread(0x109, 3, 0, 44)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 43)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 41)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 42)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)
    Sound(461, 0, 100, 0)
    OP_71(0xA, 0x10F, 0x12C, 0x1, 0x8)
    Sleep(1000)
    Sleep(500)
    OP_68(11650, 1300, 450, 9000)
    MoveCamera(60, 21, 0, 9000)
    OP_6E(700, 9000)
    SetCameraDistance(16000, 9000)
    Sound(457, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 40)
    OP_6F(0x79)
    EndChrThread(0x19, 0x3)
    SetMapObjFlags(0xA, 0x4)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    SetCameraDistance(20000, 8000)

    def lambda_7AF8():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7AF8)

    def lambda_7B0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_7B0D)
    Sleep(1500)
    Sound(100, 0, 100, 0)
    OP_71(0x4, 0xA, 0x0, 0x0, 0x0)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    SetChrFlags(0x15, 0x80)
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Fade(1000)
    ClearChrFlags(0x16, 0x8)
    OP_68(41750, 3600, -21850, 0)
    MoveCamera(340, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16000, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_63(0x16, 0xFFFFFE70, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    #Sound(3053, 255, 100, 0)    #voice#Zeit

    #A0302
    AnonymousTalk(
        0x16,
        "#30W…………咕呜呜………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToDark(1000, 0, -1)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_677E end

    def Function_38_7C7D(): pass

    label("Function_38_7C7D")

    SetChrPos(0xFE, -36200, 0, 4000, 90)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -5850, 0, 4000)
    OP_9F(0x1, 800, 0, 1800)
    OP_9F(0x1, 8050, 0, -5950)
    OP_9F(0x1, 15500, 0, -6700)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_38_7C7D end

    def Function_39_7CD4(): pass

    label("Function_39_7CD4")

    SetChrPos(0xFE, 1250, 0, -1000, 180)
    OP_D5(0x19, 0x0, 0x2BF20, 0x0, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 5000, 0, -5500)
    OP_9F(0x1, 9000, 0, -6750)
    OP_9F(0x1, 16000, 0, -6750)
    OP_9F(0x2, 0xFE, 4000, 0x6)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xBB8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x1)
    OP_71(0xA, 0x5B, 0x78, 0x1, 0x8)
    Return()

    # Function_39_7CD4 end

    def Function_40_7D69(): pass

    label("Function_40_7D69")

    SetChrPos(0xFE, 19000, 0, -6740, 90)
    OP_D5(0xFE, 0x0, 0x15F90, 0x0, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x5DC, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0xBB8, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 27150, 50, -6740)
    OP_9F(0x1, 51600, 3950, -6740)
    OP_9F(0x2, 0xFE, 3500, 0x6)
    Return()

    # Function_40_7D69 end

    def Function_41_7E02(): pass

    label("Function_41_7E02")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_7E25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7E25)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_41_7E02 end

    def Function_42_7E36(): pass

    label("Function_42_7E36")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_7E59():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7E59)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_7E36 end

    def Function_43_7E6A(): pass

    label("Function_43_7E6A")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_7E8D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7E8D)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_7E6A end

    def Function_44_7E9E(): pass

    label("Function_44_7E9E")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_7EC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7EC1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_44_7E9E end

    def Function_45_7ED2(): pass

    label("Function_45_7ED2")

    Sleep(4500)
    StopSound(468, 1000, 80)
    Sound(492, 0, 80, 0)
    Return()

    # Function_45_7ED2 end

    def Function_46_7EE2(): pass

    label("Function_46_7EE2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13800.itc", 0x1E)
    LoadChrToIndex("chr/ch13801.itc", 0x1F)
    LoadChrToIndex("chr/ch13802.itc", 0x20)
    LoadChrToIndex("chr/ch08200.itc", 0x21)
    LoadChrToIndex("chr/ch08201.itc", 0x22)
    LoadChrToIndex("apl/ch50005.itc", 0x23)
    SoundLoad(847)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis244.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu08000.itp")
    OP_68(34500, -2900, -19000, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 38000, -4000, -19700, 270)
    SetChrPos(0x102, 38400, -4000, -18400, 270)
    SetChrPos(0x109, 39300, -4000, -19700, 270)
    SetChrPos(0x105, 39700, -4000, -18400, 270)
    SetChrPos(0x104, 40800, -4000, -19000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x20)
    SetChrPos(0x18, 32700, 200, -36200, 0)
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 42000, -4000, -19000, 270)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0xA)
    SetCameraDistance(16500, 3000)

    def lambda_8068():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8068)
    Sleep(50)

    def lambda_8085():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8085)
    Sleep(50)

    def lambda_80A2():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_80A2)
    Sleep(50)

    def lambda_80BF():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_80BF)
    Sleep(50)

    def lambda_80DC():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_80DC)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x5)
    WaitChrThread(0x101, 0)
    Sound(846, 0, 100, 0)
    Sleep(300)
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    def lambda_81A1():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_81A1)
    Sleep(50)

    def lambda_81B1():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_81B1)
    Sleep(50)

    def lambda_81C1():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_81C1)
    Sleep(50)

    def lambda_81D1():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_81D1)
    Sleep(50)

    def lambda_81E1():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_81E1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    #C0303
    ChrTalk(
        0x101,
        "#5P#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        "#00105F#5P鸟叫声？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(10)
    WaitBGM()
    PlayBGM("ed7519", 0)
    Fade(250)
    OP_68(33700, -500, -27700, 0)
    MoveCamera(30, 27, 15, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_68(34700, -1000, -23700, 3000)
    MoveCamera(27, 27, 11, 3000)
    SetCameraDistance(15500, 3000)
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 33200, -4000, -20000, 180)
    SetChrPos(0x102, 31800, -4000, -20300, 180)
    SetChrPos(0x109, 34600, -4000, -20000, 180)
    SetChrPos(0x104, 34700, -4000, -18700, 180)
    SetChrPos(0x105, 33300, -4000, -18700, 180)
    ClearChrFlags(0x18, 0x80)

    def lambda_8313():

        label("loc_8313")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_8313")

    QueueWorkItem2(0x18, 2, lambda_8313)

    def lambda_8325():
        OP_96(0xFE, 0x7FBC, 0xFFFFF8F8, 0xFFFFAD30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8325)
    Sound(847, 2, 70, 0)
    WaitChrThread(0x18, 1)
    BeginChrThread(0x18, 3, 0, 47)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8367():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8367)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_838F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_838F)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_83B7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_83B7)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_83DF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_83DF)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8407():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8407)
    Sleep(2000)
    Fade(500)
    OP_68(34300, -1800, -20900, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    #C0305
    ChrTalk(
        0x101,
        "#00011F#6P什、什么！？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x109,
        "#10111F#6P白、白鹰……？\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x105,
        (
            "#10305F#6P……不，\x01",
            "好像是隼。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#00301F#6P喂喂，为何会\x01",
            "出现在城市里……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x18, 0x3)
    WaitChrThread(0x18, 1)
    EndChrThread(0x18, 0x0)
    OP_68(33300, -2800, -20900, 3000)
    MoveCamera(40, 21, 0, 3000)

    def lambda_851E():
        OP_9E(0xFE, 0x878C, 0xFFFFAD30, 0x50910, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_851E)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x73A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x76C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x79E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x802), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x834), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x866), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8CA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x92E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x992), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9F6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA28), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA5A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA8C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xABE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB22), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB54), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB86), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_86A1():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_86A1)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBEA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC1C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC4E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_86EA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_86EA)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC80), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCB2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCE4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD16), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_8733():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8733)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD7A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDDE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_877C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_877C)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE10), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE42), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE74), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xEA6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_87C5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_87C5)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xED8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF0A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF3C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF6E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xFD2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1004), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x18, 1)
    StopSound(847, 700, 60)
    Fade(250)
    EndChrThread(0x18, 0x2)
    SetChrPos(0x18, 33400, -3100, -21900, 0)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x1)

    def lambda_8869():
        OP_96(0xFE, 0x8278, 0xFFFFF1F0, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8869)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x2)
    Sleep(300)
    WaitChrThread(0x18, 1)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0309
    AnonymousTalk(
        0x18,
        (
            "啾。\x02\x03",

            "啾、啾、啾。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0310
    ChrTalk(
        0x101,
        (
            "#00001F#5P莫、莫非……\x01",
            "找我们有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x102,
        (
            "#5P#00108F和蔡特找我们说话时\x01",
            "的感觉一样呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x104,
        (
            "#5P#00306F唔，如果阿缇在这里，\x01",
            "就能听懂它在说什么了……\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x5)
    ClearChrFlags(0x17, 0x80)

    def lambda_8A6C():
        OP_96(0xFE, 0x9A4C, 0xFFFFF060, 0xFFFFB5C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8A6C)

    def lambda_8A86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_8A86)
    WaitChrThread(0x17, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)

    #C0313
    ChrTalk(
        0x17,
        "#01105F#12P哎，怎么了？\x02",
    )

    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)

    def lambda_8AF6():
        OP_95(0xFE, 37500, -4000, -19000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8AF6)
    WaitChrThread(0x17, 1)

    def lambda_8B14():
        OP_95(0xFE, 34500, -4000, -21300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8B14)
    Sleep(300)

    def lambda_8B31():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8B31)
    Sleep(100)

    def lambda_8B41():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8B41)
    Sleep(100)

    def lambda_8B51():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8B51)
    Sleep(100)

    def lambda_8B61():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8B61)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0xE1, 0x1F4)
    #Sound(3029, 255, 100, 0)    #voice#KeA

    #C0314
    ChrTalk(
        0x17,
        (
            "#01110F#11P哇，白鸟！\x02\x03",

            "#01109F嘴巴尖尖的，\x01",
            "好漂亮啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    TurnDirection(0x18, 0x17, 0)
    Sleep(300)

    #C0315
    ChrTalk(
        0x18,
        (
            "#6P#08009F啾⊥\x02\x03",

            "啾、啾、啾¤\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x17,
        (
            "#01103F#11P嗯，嗯。\x02\x03",

            "#01102F原来如此，是这样啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    #C0317
    ChrTalk(
        0x101,
        (
            "#00012F#5P（琪雅……\x01",
            "  果然能听懂啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x109,
        "#10112F#5P（好、好厉害啊……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    def lambda_8CFF():

        label("loc_8CFF")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8CFF")

    QueueWorkItem2(0x17, 2, lambda_8CFF)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x2)

    #C0319
    ChrTalk(
        0x17,
        (
            "#01100F#11P那个……这个孩子\x01",
            "的名字是『基库』。\x02\x03",

            "它说有传话要转达给你们，\x01",
            "请你们收下。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8D74():
        TurnDirection(0x101, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8D74)
    Sleep(50)

    def lambda_8D84():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8D84)
    Sleep(50)

    def lambda_8D94():
        TurnDirection(0x109, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8D94)
    Sleep(50)

    def lambda_8DA4():
        TurnDirection(0x105, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8DA4)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0320
    ChrTalk(
        0x101,
        "#00011F#5P是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#5P#00305F啊，它的脚上确实\x01",
            "绑着一张纸条呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8E11():
        OP_95(0xFE, 33200, -4000, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8E11)
    TurnDirection(0x18, 0x101, 500)
    WaitChrThread(0x101, 1)
    EndChrThread(0x17, 0x2)
    SetChrName("")

    #A0322
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德从白隼的脚上\x01",
            "取下了纸条。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "克洛斯贝尔警察局·特别任务支援科敬启\x02\x03",

            "听闻诸位事迹，\x01",
            "特此冒昧联络。\x02\x03",

            "若时间方便，\x01",
            "望秘密前来会谈。\x02\x03",

            "今日傍晚，于克洛斯贝尔空港的\x01",
            "候船露台静候各位。\x02\x03",

            "另，如各位不便赴邀，\x01",
            "无需另行答复。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)

    #A0324
    AnonymousTalk(
        0x101,
        "#00005F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0325
    AnonymousTalk(
        0x102,
        "#00101F这、这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0326
    AnonymousTalk(
        0x109,
        (
            "#10106F内容奇怪，又没有写明寄信人，\x01",
            "未免也太可疑了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0327
    AnonymousTalk(
        0x105,
        (
            "#10302F不过，字迹相当漂亮，\x01",
            "措辞也十分有礼呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0328
    AnonymousTalk(
        0x104,
        (
            "#00301F更重要的是，字条上印着的\x01",
            "白隼徽章不就是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0329
    AnonymousTalk(
        0x18,
        (
            "#08000F啾。\x02\x03",

            "啾、啾、啾。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    Sound(847, 2, 70, 0)

    def lambda_90FC():
        OP_96(0xFE, 0x8278, 0xFFFFF3E4, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_90FC)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    WaitChrThread(0x18, 1)
    OP_68(33300, -1800, -24900, 5000)
    MoveCamera(46, 21, 0, 5000)
    SetCameraDistance(16000, 5000)
    Fade(250)
    SetChrPos(0x18, 33400, -3600, -21900, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x1)

    def lambda_9182():

        label("loc_9182")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_9182")

    QueueWorkItem2(0x18, 2, lambda_9182)
    BeginChrThread(0x18, 3, 0, 48)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDDE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD7A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD16), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCE4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCB2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC80), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC4E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC1C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBEA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB86), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB54), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB22), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xABE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA8C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA5A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA28), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9F6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x992), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x92E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8CA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x866), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x834), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x802), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x79E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x76C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x73A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x18, 3)

    def lambda_93B7():
        OP_96(0xFE, 0x8278, 0xFFFFFED4, 0xFFFF7B94, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_93B7)
    Sleep(300)

    def lambda_93D4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_93D4)
    Sleep(100)

    def lambda_93E4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_93E4)
    Sleep(100)

    def lambda_93F4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_93F4)
    Sleep(100)

    def lambda_9404():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9404)
    StopSound(847, 2000, 60)
    WaitChrThread(0x18, 1)
    EndChrThread(0x18, 0xFF)
    SetChrFlags(0x18, 0x80)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)
    OP_6F(0x79)
    Fade(500)
    OP_68(33300, -2800, -20900, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    TurnDirection(0x101, 0x17, 500)

    #C0330
    ChrTalk(
        0x101,
        (
            "#6P#00011F那个……\x01",
            "琪雅，它在说什么？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    #C0331
    ChrTalk(
        0x17,
        (
            "#01111F#11P嗯……去或不去，\x01",
            "由你们自行决定。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x101,
        "#6P#00003F是吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_956D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_956D)
    Sleep(50)

    def lambda_957D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_957D)
    Sleep(50)

    def lambda_958D():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_958D)
    Sleep(50)

    def lambda_959D():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_959D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0333
    ChrTalk(
        0x102,
        (
            "#6P#00108F怎、怎么办呢？\x02\x03",

            "#00101F我想应该不会\x01",
            "是那里的人士……\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x104,
        "#5P#00306F嗯，终究不太可能啊。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x109,
        (
            "#10108F#11P可是，白隼徽章……\x01",
            "再加上刚才那只白隼……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x105,
        (
            "#10309F#5P啊哈哈，越来越\x01",
            "期待了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(450)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(150)

    #C0337
    ChrTalk(
        0x101,
        (
            "#12P#00003F既然对方特意发来邀请，\x01",
            "我们就接受好了。\x02\x03",

            "#00000F距离傍晚还有一些时间，\x01",
            "把要做的事情做完之后再去也无妨。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x102,
        "#6P#00106F知、知道了。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x109,
        "#10106F#11P真、真紧张……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x104,
        (
            "#5P#00309F不过，应该不用\x01",
            "换上正装去吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x105,
        (
            "#10302F#5P呵呵，先把要办的事情办完，\x01",
            "然后就去南出口的克洛斯贝尔空港吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x17, 0x13B, 0x1F4)
    Sleep(150)

    #C0342
    ChrTalk(
        0x17,
        (
            "#11P#01110F虽然不知道是怎么回事，\x01",
            "不过大家要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    SetChrFlags(0x17, 0x80)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, 34000, -4000, -19000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 7)
    OP_29(0xA3, 0x1, 0x11)
    OP_C9(0x1, 0x1000)
    OP_24(0x34F)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_46_7EE2 end

    def Function_47_9864(): pass

    label("Function_47_9864")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9893")

    def lambda_9874():
        OP_9E(0xFE, 0x8980, 0xFFFFAD30, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9874)
    WaitChrThread(0x18, 1)
    Jump("Function_47_9864")

    label("loc_9893")

    Return()

    # Function_47_9864 end

    def Function_48_9894(): pass

    label("Function_48_9894")


    def lambda_9899():
        OP_9E(0xFE, 0x846C, 0xFFFFAA74, 0x2BF20, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9899)
    WaitChrThread(0x18, 1)

    def lambda_98B8():
        OP_9E(0xFE, 0x8084, 0xFFFFAA74, 0x57E40, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_98B8)
    WaitChrThread(0x18, 1)
    Return()

    # Function_48_9894 end

    def Function_49_98D3(): pass

    label("Function_49_98D3")

    EventBegin(0x0)
    Fade(500)
    OP_68(33500, -2700, -18100, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 32600, -4000, -19400, 0)
    SetChrPos(0x102, 31300, -4000, -18800, 45)
    SetChrPos(0x103, 34100, -4000, -19500, 315)
    SetChrPos(0x104, 35400, -4000, -18300, 270)
    SetChrPos(0x109, 33500, -4000, -17600, 0)
    SetChrPos(0x105, 31000, -4000, -17700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sleep(300)

    #C0343
    ChrTalk(
        0x103,
        (
            "#00206F#12P说起来……\x02\x03",

            "#00200F过了今天，就乘坐不到\x01",
            "诺艾尔小姐驾驶的车了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_99DA():
        OP_93(0x109, 0xB3, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_99DA)
    Sleep(400)

    #C0344
    ChrTalk(
        0x101,
        "#12P#00006F嗯……的确如此啊。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x109,
        (
            "#10112F#5P啊哈哈……\x01",
            "我也觉得很遗憾。\x02\x03",

            "因为我很喜爱\x01",
            "这辆车呢。\x02\x03",

            "#10100F不过，你们的驾驶水平\x01",
            "也都很不错了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#12P#00004F嗯，多亏你在\x01",
            "休息日用心教导我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x102,
        (
            "#6P#00109F呵呵，教得简单易懂，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x105,
        (
            "#6P#10306F唔，不过，\x01",
            "还真是超级严厉啊。\x02\x03",

            "#10302F与其说是上士，\x01",
            "感觉倒更像是鬼教官呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x109, 0x105, 500)
    Sleep(300)

    #C0349
    ChrTalk(
        0x109,
        (
            "#11P#10101F那、那还不是因为你\x01",
            "整天胡说八道。\x02\x03",

            "#10106F如果认真，明明可以做得很好，\x01",
            "但你却故意不记交通规则。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        (
            "#00304F#11P毕竟诺艾尔是经常接受\x01",
            "严厉教导的军人嘛。\x02\x03",

            "#00300F总之，今天就让我们\x01",
            "尽情享受专业人士的驾驶水平吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#12P#00002F嗯，诺艾尔，\x01",
            "拜托你啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0352
    ChrTalk(
        0x109,
        "#10109F#5P好的，交给我吧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 33500, -4000, -18000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x180, 4)
    EventEnd(0x5)
    Return()

    # Function_49_98D3 end

    def Function_50_9CB5(): pass

    label("Function_50_9CB5")

    EventBegin(0x0)
    Fade(500)
    OP_68(33500, -2900, -17100, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 33500, -4000, -17600, 0)
    SetChrPos(0x102, 32600, -4000, -19400, 0)
    SetChrPos(0x103, 34100, -4000, -19500, 315)
    SetChrPos(0x104, 35400, -4000, -18300, 315)
    SetChrPos(0xF4, 31300, -4000, -18800, 45)
    SetChrPos(0xF5, 31000, -4000, -17700, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0353
    ChrTalk(
        0x101,
        (
            "#11P#00002F我们的车……\x01",
            "似乎平安无事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A142")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DE6")

    #C0354
    ChrTalk(
        0x109,
        "#6P#10109F太好了……总算松了口气。\x02",
    )

    CloseMessageWindow()

    label("loc_9DE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FB3")

    #C0355
    ChrTalk(
        0x105,
        (
            "#6P#10405F话说回来，我们当时\x01",
            "能得到这辆车，在一定程度上\x01",
            "也是因为迪塔市长的通融吧？\x02\x03",

            "#10409F呵呵，但现在却要\x01",
            "开着这辆车去逮捕他，\x01",
            "还真是很具讽刺意义啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E98():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9E98)
    Sleep(50)

    def lambda_9EA8():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9EA8)
    Sleep(50)

    def lambda_9EB8():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9EB8)
    Sleep(50)

    def lambda_9EC8():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9EC8)
    Sleep(50)

    def lambda_9ED8():
        TurnDirection(0xF4, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_9ED8)
    Sleep(50)

    def lambda_9EE8():
        TurnDirection(0xF5, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_9EE8)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0356
    ChrTalk(
        0x102,
        "#12P#00106F……是啊，确实。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F95")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F73")

    #C0357
    ChrTalk(
        0x109,
        "#12P#10101F瓦吉，我说你啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F95")

    label("loc_9F73")


    #C0358
    ChrTalk(
        0x109,
        "#6P#10101F瓦吉，我说你啊……\x02",
    )

    CloseMessageWindow()

    label("loc_9F95")


    #C0359
    ChrTalk(
        0x103,
        "#00211F并不好笑……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A13D")

    label("loc_9FB3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A13D")

    #C0360
    ChrTalk(
        0x10A,
        (
            "#6P#00603F嗯……\x01",
            "看起来好像没有问题。\x02\x03",

            "#00600F话说回来，听说你们当时\x01",
            "能得到这辆车，在一定程度上也是\x01",
            "因为迪塔前市长的通融，是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A052():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A052)
    Sleep(50)

    def lambda_A062():
        TurnDirection(0x103, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A062)
    Sleep(50)

    def lambda_A072():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A072)
    Sleep(50)

    def lambda_A082():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A082)
    Sleep(50)

    def lambda_A092():
        TurnDirection(0xF4, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_A092)
    Sleep(50)

    def lambda_A0A2():
        TurnDirection(0xF5, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_A0A2)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0361
    ChrTalk(
        0x102,
        "#12P#00108F说、说起来……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A11E")

    #C0362
    ChrTalk(
        0x109,
        (
            "#6P#10106F赛尔盖科长\x01",
            "确实这样说过呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A11E")


    #C0363
    ChrTalk(
        0x103,
        "#00211F……真是很讽刺啊。\x02",
    )

    CloseMessageWindow()

    label("loc_A13D")

    Jump("loc_A272")

    label("loc_A142")


    #C0364
    ChrTalk(
        0x109,
        (
            "#6P#10104F太好了……总算松了口气。\x02\x03",

            "#10105F……话说回来，我们当时\x01",
            "能得到这辆车，在一定程度上\x01",
            "也是因为迪塔市长的通融吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A1C4():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A1C4)
    Sleep(50)

    def lambda_A1D4():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A1D4)
    Sleep(50)

    def lambda_A1E4():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A1E4)
    Sleep(50)

    def lambda_A1F4():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A1F4)
    Sleep(50)

    def lambda_A204():
        TurnDirection(0xF4, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_A204)
    Sleep(50)

    def lambda_A214():
        TurnDirection(0xF5, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_A214)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0365
    ChrTalk(
        0x102,
        "#12P#00108F说、说起来……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x103,
        "#00211F……真是很讽刺啊。\x02",
    )

    CloseMessageWindow()

    label("loc_A272")

    OP_93(0x104, 0x13B, 0x1F4)
    Sleep(150)

    #C0367
    ChrTalk(
        0x104,
        (
            "#00304F不管这辆车是怎么来的，\x01",
            "总之它也是支援科的一员。\x02\x03",

            "#00302F先检查一下内部状况，\x01",
            "确认是否可以正常使用吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0368
    ChrTalk(
        0x101,
        "#11P#00000F嗯，说的对。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 1)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_50_9CB5 end

    def Function_51_A32A(): pass

    label("Function_51_A32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3AC")
    EventBegin(0x1)

    #C0369
    ChrTalk(
        0x101,
        (
            "#00000F前方是西克洛斯贝尔街道。\x02\x03",

            "虽然有通缉魔兽要处理……\x01",
            "但现在还是先完成市内的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_A3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A46A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A41E")

    #C0370
    ChrTalk(
        0x101,
        (
            "#00000F前方是西克洛斯贝尔街道。\x02\x03",

            "现在没有什么重要的事情，\x01",
            "还是不要出去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A456")

    label("loc_A41E")


    #C0371
    ChrTalk(
        0x101,
        (
            "#00000F现在没有需要去这边的事情，\x01",
            "还是不要出去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A456")

    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_A46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A4D3")
    EventBegin(0x1)

    #C0372
    ChrTalk(
        0x101,
        (
            "#00001F现在必须要尽快\x01",
            "调查兰迪的行踪，\x01",
            "并不是去别处乱逛的时候。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_A4D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A535")
    EventBegin(0x1)

    #C0373
    ChrTalk(
        0x101,
        (
            "#00001F现在并不是前往市外的时候，\x01",
            "还是老老实实地回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_A535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5C0")
    EventBegin(0x1)

    #C0374
    ChrTalk(
        0x101,
        (
            "#00001F都已经走到了这一步，\x01",
            "没有离开城市的理由。\x02\x03",

            "突入兰花塔的作战行动……\x01",
            "无论如何也要取得成功。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_A5C0")

    Return()

    # Function_51_A32A end

    def Function_52_A5C1(): pass

    label("Function_52_A5C1")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A614")

    #C0375
    ChrTalk(
        0x101,
        (
            "#00000F似乎在内侧\x01",
            "上了锁。\x02\x03",

            "还是从正面入口进去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A64E")

    label("loc_A614")

    SetChrName("")

    #A0376
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁。\x01",
            "看来是从内侧\x01",
            "锁住的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_A64E")

    TalkEnd(0xFF)
    Return()

    # Function_52_A5C1 end

    SaveToFile()

Try(main)
