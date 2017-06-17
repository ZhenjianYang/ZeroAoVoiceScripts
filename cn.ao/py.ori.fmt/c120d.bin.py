from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c120d.bin",                # FileName
        "c120d",                    # MapName
        "c120d",                    # Location
        0x001A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 4, 0, 5],
    )

    BuildStringList((
        "c120d",                  # 0
        "约纳",                   # 1
        "警官",                   # 2
        "警备队员",               # 3
        "警备队员",               # 4
        "库妮娅",                 # 5
        "奥赛尔",                 # 6
        "毕肖普",                 # 7
        "奎因老人",               # 8
        "亚米萨",                 # 9
        "警官",                   # 10
        "国防军士兵",             # 11
        "装甲车",                 # 12
        "尼尔森",                 # 13
        "玛丽亚贝尔",             # 14
        "警备员比尔斯",           # 15
        "车",                     # 16
        "车",                     # 17
        "bc1200",                 # 18
        "中央广场",               # 19
        "西街",                   # 20
        "行政区",                 # 21
        "住宅街",                 # 22
        "欢乐街",                 # 23
        "东街",                   # 24
        "旧城区",                 # 25
        "港湾区",                 # 26
        "ＩＢＣ",                 # 27
        "站前街道",               # 28
        "后巷",                   # 29
        "乌尔斯拉间道",           # 30
        "东克洛斯贝尔街道",       # 31
        "西克洛斯贝尔街道",       # 32
        "玛因兹山道",             # 33
        "兰花塔",                 # 34
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_A4", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_B4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_D8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_DC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_E0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_E4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_E8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_EC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_F4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_114", 0x0000, 99, 6, 60, 4, 1, 25, 0, "bc1200", "Sepith_A4", 60, 25, 10, 5,
        (
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7450", "ed7453", "ATBonus_94"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7450", "ed7453", "ATBonus_94"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7450", "ed7453", "ATBonus_94"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    AddCharChip((
        "chr/ch06100.itc",                   # 00
        "chr/ch30000.itc",                   # 01
        "chr/ch31200.itc",                   # 02
        "chr/ch31300.itc",                   # 03
        "chr/ch22100.itc",                   # 04
        "chr/ch25200.itc",                   # 05
        "chr/ch26000.itc",                   # 06
        "chr/ch24000.itc",                   # 07
        "chr/ch21500.itc",                   # 08
        "chr/ch30000.itc",                   # 09
        "chr/ch41400.itc",                   # 0A
        "chr/ch45102.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
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

    DeclNpc(75500,   -2500,   20000,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(22079,   0,       15050,   180,  389,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(3130,    2000,    25149,   180,  389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(5530,    2000,    25000,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-13199,  0,       11500,   90,   385,  0x0, 0,   4,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(-10470,  0,       13340,   180,  385,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-52470,  2000,    21149,   90,   385,  0x0, 0,   6,   0,   0,   2,   0,   14,  255,  0)
    DeclNpc(39669,   -2500,   -19379,  135,  385,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(40919,   -2500,   -18989,  135,  385,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-17799,  0,       13369,   180,  389,  0x0, 0,   9,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-18479,  0,       12000,   180,  389,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-21239,  0,       14350,   90,   196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(7820,    -400,    3200,    180,  389,  0x0, 0,   11,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(3140,    -1200,   -700,    0x10100E1,    "BattleInfo_114", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(38750,   1370,    -2500,   0x10100E1,    "BattleInfo_114", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-16760,  9670,    -10,     0x10100E1,    "BattleInfo_114", 0,   16,  0xFFFF, 0,  1)

    DeclActor(16750,   -1000,   -15740,  1200,    16750,   0,       -15740,  0x007C, 0,  6,  0x0000)
    DeclActor(82470,   -2500,   15010,   1200,    79890,   -3500,   8810,    0x007C, 0,  20, 0x0000)
    DeclActor(20620,   10,      15670,   2000,    20620,   1500,    15670,   0x007C, 0,  35, 0x0000)
    DeclActor(4550,    2000,    25990,   2000,    4550,    3000,    25990,   0x007C, 0,  36, 0x0000)
    DeclActor(77220,   -2500,   20290,   2000,    77220,   -1000,   20290,   0x007C, 0,  21, 0x0000)

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

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_854",          # 00, 0
        "Function_1_904",          # 01, 1
        "Function_2_9B5",          # 02, 2
        "Function_3_A9C",          # 03, 3
        "Function_4_AC4",          # 04, 4
        "Function_5_E63",          # 05, 5
        "Function_6_14AE",         # 06, 6
        "Function_7_15E9",         # 07, 7
        "Function_8_15FC",         # 08, 8
        "Function_9_1612",         # 09, 9
        "Function_10_1704",        # 0A, 10
        "Function_11_1779",        # 0B, 11
        "Function_12_17FD",        # 0C, 12
        "Function_13_1B44",        # 0D, 13
        "Function_14_1E31",        # 0E, 14
        "Function_15_2092",        # 0F, 15
        "Function_16_22B0",        # 10, 16
        "Function_17_2498",        # 11, 17
        "Function_18_2581",        # 12, 18
        "Function_19_25F6",        # 13, 19
        "Function_20_269E",        # 14, 20
        "Function_21_2766",        # 15, 21
        "Function_22_28CC",        # 16, 22
        "Function_23_3B92",        # 17, 23
        "Function_24_3E2D",        # 18, 24
        "Function_25_3EB8",        # 19, 25
        "Function_26_3F00",        # 1A, 26
        "Function_27_52B6",        # 1B, 27
        "Function_28_52F3",        # 1C, 28
        "Function_29_5348",        # 1D, 29
        "Function_30_539D",        # 1E, 30
        "Function_31_53F2",        # 1F, 31
        "Function_32_5447",        # 20, 32
        "Function_33_549C",        # 21, 33
        "Function_34_54F1",        # 22, 34
        "Function_35_67AE",        # 23, 35
        "Function_36_681A",        # 24, 36
    ))


    def Function_0_854(): pass

    label("Function_0_854")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_88C"),
        (1, "loc_898"),
        (2, "loc_8A4"),
        (3, "loc_8B0"),
        (4, "loc_8BC"),
        (5, "loc_8C8"),
        (6, "loc_8D4"),
        (SWITCH_DEFAULT, "loc_8E0"),
    )


    label("loc_88C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_898")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_903")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_903")

    Return()

    # Function_0_854 end

    def Function_1_904(): pass

    label("Function_1_904")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B4")
    OP_95(0xFE, 14600, 0, 11500, 1000, 0x0)
    OP_95(0xFE, 20200, 0, 8200, 1000, 0x0)
    OP_95(0xFE, 20200, 0, -6200, 1000, 0x0)
    OP_95(0xFE, 14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -20000, 0, -6400, 1000, 0x0)
    OP_95(0xFE, -20000, 0, 6000, 1000, 0x0)
    OP_95(0xFE, -13200, 0, 11500, 1000, 0x0)
    Jump("Function_1_904")

    label("loc_9B4")

    Return()

    # Function_1_904 end

    def Function_2_9B5(): pass

    label("Function_2_9B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A9B")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 5000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, -13000, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 5000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 5000, 0x0)
    Jump("Function_2_9B5")

    label("loc_A9B")

    Return()

    # Function_2_9B5 end

    def Function_3_A9C(): pass

    label("Function_3_A9C")

    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_AC3")
    SetMapObjFlags(0x4, 0x2000000)
    ClearMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)

    label("loc_AC3")

    Return()

    # Function_3_A9C end

    def Function_4_AC4(): pass

    label("Function_4_AC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFF")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B86")
    SetChrPos(0x0, 4870, 3350, 31570, 180)
    SetChrPos(0x1, 4870, 3350, 31570, 180)
    SetChrPos(0x2, 4870, 3350, 31570, 180)
    SetChrPos(0x3, 4870, 3350, 31570, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B59")
    SetChrPos(0x4, 4870, 3350, 31570, 180)
    SetChrPos(0x5, 4870, 3350, 31570, 180)
    Jump("loc_B78")

    label("loc_B59")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B78")
    SetChrPos(0x4, 4870, 3350, 31570, 180)

    label("loc_B78")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CFF")

    label("loc_B86")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C5E")
    SetChrPos(0x0, -28110, 2000, 23520, 90)
    SetChrPos(0x1, -28110, 2000, 23520, 90)
    SetChrPos(0x2, -28110, 2000, 23520, 90)
    SetChrPos(0x3, -28110, 2000, 23520, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C31")
    SetChrPos(0x4, -28110, 2000, 23520, 90)
    SetChrPos(0x5, -28110, 2000, 23520, 90)
    Jump("loc_C50")

    label("loc_C31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C50")
    SetChrPos(0x4, -28110, 2000, 23520, 90)

    label("loc_C50")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CFF")

    label("loc_C5E")

    SetChrPos(0x0, -19600, 0, -27950, 0)
    SetChrPos(0x1, -19600, 0, -27950, 0)
    SetChrPos(0x2, -19600, 0, -27950, 0)
    SetChrPos(0x3, -19600, 0, -27950, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD7")
    SetChrPos(0x4, -19600, 0, -27950, 0)
    SetChrPos(0x5, -19600, 0, -27950, 0)
    Jump("loc_CF6")

    label("loc_CD7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF6")
    SetChrPos(0x4, -19600, 0, -27950, 0)

    label("loc_CF6")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CFF")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1B")
    ClearChrFlags(0x8, 0x80)

    label("loc_D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D38")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D6E")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_E30")

    label("loc_D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D7C")
    Jump("loc_E30")

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DD0")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, -16840, 0, -5150, 180)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, -16810, 0, -6100, 0)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_E30")

    label("loc_DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E30")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, 21190, 0, 1100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, 22390, 0, 1100, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -17800, 0, 13370, 180)

    label("loc_E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E3F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 23)

    label("loc_E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E4E")
    ClearScenarioFlags(0x22, 1)
    Event(0, 8)

    label("loc_E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E62")
    SetScenarioFlags(0x0, 6)
    Event(0, 34)

    label("loc_E62")

    Return()

    # Function_4_AC4 end

    def Function_5_E63(): pass

    label("Function_5_E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_E78")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 6)

    label("loc_E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E91")
    OP_10(0x1, 0x0)
    OP_10(0x8, 0x1)
    Jump("loc_E97")

    label("loc_E91")

    OP_10(0x1, 0x1)
    OP_10(0x8, 0x0)

    label("loc_E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2B")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F72")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x2D, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8A")
    ClearMapFlags(0x2000)
    Jump("loc_F91")

    label("loc_F8A")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1007")
    SetMapObjFrame(0xFF, "koge2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    SetMapObjFrame(0xFF, "syugeki01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "body03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "keepout", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sakutoka", 0x1, 0x1)
    SetMapObjFrame(0xFF, "atokabuse", 0x1, 0x1)
    Jump("loc_10E5")

    label("loc_1007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_107D")
    SetMapObjFrame(0xFF, "koge2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    SetMapObjFrame(0xFF, "syugeki01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "body03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "keepout", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sakutoka", 0x1, 0x1)
    SetMapObjFrame(0xFF, "atokabuse", 0x1, 0x1)
    Jump("loc_10E5")

    label("loc_107D")

    SetMapObjFrame(0xFF, "koge2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x1, 0x1)
    SetMapObjFrame(0xFF, "syugeki01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "body03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "keepout", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sakutoka", 0x0, 0x1)
    SetMapObjFrame(0xFF, "atokabuse", 0x0, 0x1)

    label("loc_10E5")

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
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 79890, -3500, 8810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B5")
    OP_70(0x7, 0x0)
    Jump("loc_13B9")

    label("loc_13B5")

    OP_70(0x7, 0x1E)

    label("loc_13B9")

    SetMapObjFlags(0x4, 0x4)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DC")
    OP_70(0x8, 0x0)
    Jump("loc_13F6")

    label("loc_13DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_13F2")
    OP_70(0x8, 0x28)
    OP_65(0x4, 0x1)
    Jump("loc_13F6")

    label("loc_13F2")

    OP_66(0x4, 0x1)

    label("loc_13F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_144A")
    ClearChrFlags(0x13, 0x80)
    OP_78(0xA, 0x13)
    SetChrPos(0x13, -20340, 0, 14300, 90)
    OP_D5(0x13, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)

    label("loc_144A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_145E")
    SetMapObjFlags(0x5, 0x4)

    label("loc_145E")

    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x13DE4, 0x0, 0x71E8)
    OP_E3(0x13C54, 0x0, 0xD1B0)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_14AD")
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_14AD")

    Return()

    # Function_5_E63 end

    def Function_6_14AE(): pass

    label("Function_6_14AE")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A0")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('粉红液体', 1)"), scpexpr(EXPR_END)), "loc_1531")
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
    Jump("loc_159B")

    label("loc_1531")

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
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_159B")

    Jump("loc_15DD")

    label("loc_15A0")

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

    label("loc_15DD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_14AE end

    def Function_7_15E9(): pass

    label("Function_7_15E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15FB")
    Call(0, 26)
    Return()

    label("loc_15FB")

    Return()

    # Function_7_15E9 end

    def Function_8_15FC(): pass

    label("Function_8_15FC")

    EventBegin(0x0)
    SetChrPos(0x0, 75710, -2500, 20230, 270)
    EventEnd(0x5)
    Return()

    # Function_8_15FC end

    def Function_9_1612(): pass

    label("Function_9_1612")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16AB")

    #C0004
    ChrTalk(
        0xFE,
        (
            "还没找到\x01",
            "黑月的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "倒塌的房屋中\x01",
            "也没有线索。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "他们到底到\x01",
            "什么地方去了？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "是潜伏在自治州内，\x01",
            "还是逃亡到了国外……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1700")

    label("loc_16AB")


    #C0008
    ChrTalk(
        0xFE,
        (
            "黑月的那些人\x01",
            "到底到什么\x01",
            "地方去了？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "是潜伏在自治州内，\x01",
            "还是逃亡到了国外……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1700")

    TalkEnd(0xFE)
    Return()

    # Function_9_1612 end

    def Function_10_1704(): pass

    label("Function_10_1704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1716")
    Call(0, 22)
    Jump("loc_1778")

    label("loc_1716")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        (
            "倒塌的ＩＢＣ大楼\x01",
            "如今就像是瓦砾堆成的山。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "都损坏成那样了，\x01",
            "要重建恐怕很困难吧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_1778")

    Return()

    # Function_10_1704 end

    def Function_11_1779(): pass

    label("Function_11_1779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178B")
    Call(0, 22)
    Jump("loc_17FC")

    label("loc_178B")

    TalkBegin(0xFE)

    #C0012
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ大小姐的视察\x01",
            "好像也没取得什么成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "能迅速把银行的业务\x01",
            "转移到兰花塔，\x01",
            "总算是不幸中的大幸。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_17FC")

    Return()

    # Function_11_1779 end

    def Function_12_17FD(): pass

    label("Function_12_17FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1889")

    #C0014
    ChrTalk(
        0xFE,
        (
            "雾气总算消失了，\x01",
            "我向天上一望，却看到那种东西……\x01",
            "那棵树到底是什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "看起来也不像是兵器……\x01",
            "那也是总统制造的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B40")

    label("loc_1889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1897")
    Jump("loc_1B40")

    label("loc_1897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196D")

    #C0016
    ChrTalk(
        0xFE,
        (
            "事情的发展太过突然，我自然有些吃惊……\x01",
            "但态度如果不强硬一点，\x01",
            "肯定会被两大国小看。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "所以我坚决支持\x01",
            "迪塔总统！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "再加上还有亚里欧斯长官在……\x01",
            "总不能永远都任由\x01",
            "两大国为所欲为！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19CA")

    label("loc_196D")


    #C0019
    ChrTalk(
        0xFE,
        (
            "虽然肯定有些不安……\x01",
            "但我坚决支持\x01",
            "迪塔总统！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "我可不希望永远都任由\x01",
            "两大国为所欲为！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CA")

    Jump("loc_1B40")

    label("loc_19CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB6")

    #C0021
    ChrTalk(
        0xFE,
        (
            "公园附近那个全毁的公司……\x01",
            "据说是受雇于共和国政府的。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "既然如此，应该就是得知了此事的帝国\x01",
            "雇佣猎兵团发动了袭击吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "那种事情随便怎样都好……\x01",
            "总之，我可不希望克洛斯贝尔\x01",
            "再被卷进这种事情了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B40")

    label("loc_1AB6")


    #C0024
    ChrTalk(
        0xFE,
        (
            "之所以会发生如此事态，\x01",
            "主要还是因为克洛斯贝尔\x01",
            "一直都是从属州吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "既然如此，我们显然\x01",
            "还是应该向周边诸国\x01",
            "明确表达独立的意志。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B40")

    TalkEnd(0xFE)
    Return()

    # Function_12_17FD end

    def Function_13_1B44(): pass

    label("Function_13_1B44")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1BA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC1")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E28")

    label("loc_1BC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD5")
    Jump("loc_1E28")

    label("loc_1BD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E28")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1CF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9D")

    #C0026
    ChrTalk(
        0xFE,
        (
            "苦难就是为了被克服而存在的……\x01",
            "没有任何苦难是不能克服的！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "两大国算什么，古怪的大树算什么！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "不管发生什么事，\x01",
            "我也会一直在这里做面条！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CF2")

    label("loc_1C9D")


    #C0029
    ChrTalk(
        0xFE,
        "两大国算什么，古怪的大树算什么！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "不管发生什么事，\x01",
            "我也会一直在这里做面条！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF2")

    Jump("loc_1E28")

    label("loc_1CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1D05")
    Jump("loc_1E28")

    label("loc_1D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1D6E")

    #C0031
    ChrTalk(
        0xFE,
        "唔，终于到此地步了吗……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "我也要拿出相应的觉悟。\x01",
            "事到如今，我们也只能抗战到底了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E28")

    label("loc_1D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E28")

    #C0033
    ChrTalk(
        0xFE,
        (
            "多年来一直和我甘苦与共的摊子\x01",
            "被毁坏时，真是受了相当大的打击……\x01",
            "但无论在什么时候，也必须要积极向前看！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "趁着这次弃旧换新，我也得重新振奋精神，\x01",
            "今后要和新摊子一起加油！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E28")

    Jump("loc_1B51")

    label("loc_1E2D")

    TalkEnd(0xFE)
    Return()

    # Function_13_1B44 end

    def Function_14_1E31(): pass

    label("Function_14_1E31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EE0")

    #C0035
    ChrTalk(
        0xFE,
        (
            "呼，好忙好忙……\x01",
            "因为戒严令的影响，\x01",
            "快递工作已经很久没有这么繁忙过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "呵呵，但快递员这份工作\x01",
            "本来就应该忙成这样嘛。\x01",
            "如此繁忙，反而很有活着的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208E")

    label("loc_1EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1EEE")
    Jump("loc_208E")

    label("loc_1EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_201D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB3")

    #C0037
    ChrTalk(
        0xFE,
        (
            "从今天早上开始，铁路货运就停止了，\x01",
            "送货数量一下少了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "……话说回来，如果再这么下去，\x01",
            "克洛斯贝尔究竟会变得怎样呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        "和工作相比，还是这个问题更重要啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2018")

    label("loc_1FB3")


    #C0040
    ChrTalk(
        0xFE,
        (
            "说起来，如果再这么下去，\x01",
            "克洛斯贝尔究竟会变得怎样呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "和工作相比，还是这个问题更重要啊……\x02",
    )

    CloseMessageWindow()

    label("loc_2018")

    Jump("loc_208E")

    label("loc_201D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_208E")

    #C0042
    ChrTalk(
        0xFE,
        (
            "袭击事件已经过去一周了……\x01",
            "这一带也终于恢复了平静。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "总之，真希望那样的事件\x01",
            "别再发生第二次了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208E")

    TalkEnd(0xFE)
    Return()

    # Function_14_1E31 end

    def Function_15_2092(): pass

    label("Function_15_2092")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_211D")

    #C0044
    ChrTalk(
        0xFE,
        (
            "总统的行动也好，\x01",
            "那棵大树也好，\x01",
            "净是一些莫名其妙的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "不过，无论今后\x01",
            "发生什么情况，\x01",
            "我都会一心保护好亚米萨。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22AC")

    label("loc_211D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_212B")
    Jump("loc_22AC")

    label("loc_212B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2249")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E6")

    #C0046
    ChrTalk(
        0xFE,
        (
            "真是愚蠢透顶的演说啊……\x01",
            "就算能欺骗所有人，\x01",
            "也别想欺骗老头子我！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "什么独立国！什么国防军！\x01",
            "他们真的以为自己能在两大国的\x01",
            "威胁之下，保证我们的安全吗！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2244")

    label("loc_21E6")


    #C0048
    ChrTalk(
        0xFE,
        (
            "女神啊……\x01",
            "无论让我遭遇到什么事情都无所谓。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "但无论如何也请\x01",
            "救救我的孙女亚米萨……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2244")

    Jump("loc_22AC")

    label("loc_2249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22AC")

    #C0050
    ChrTalk(
        0xFE,
        (
            "当时如果逃得稍微慢些，\x01",
            "我和亚米萨恐怕就都……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "……如今回想起来，\x01",
            "仍然无比后怕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22AC")

    TalkEnd(0xFE)
    Return()

    # Function_15_2092 end

    def Function_16_22B0(): pass

    label("Function_16_22B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2379")

    #C0052
    ChrTalk(
        0xFE,
        (
            "爷爷和我说，\x01",
            "今后可能还会发生\x01",
            "各种各样的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "要是再发生之前那种袭击事件，\x01",
            "那就太可怕了……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "不过，只要和最喜欢的\x01",
            "爷爷在一起，不管遇到\x01",
            "什么困难我都能坚持。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_23F0")

    label("loc_2379")


    #C0055
    ChrTalk(
        0xFE,
        (
            "要是再发生之前那种袭击事件，\x01",
            "可就太可怕了……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "不过，只要和最喜欢的\x01",
            "爷爷在一起，不管遇到\x01",
            "什么困难我都能坚持。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F0")

    Jump("loc_2494")

    label("loc_23F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2403")
    Jump("loc_2494")

    label("loc_2403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_245A")

    #C0057
    ChrTalk(
        0xFE,
        (
            "真的会像爷爷说的一样，\x01",
            "爆发战争吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "……不要啊，好可怕………\x02",
    )

    CloseMessageWindow()
    Jump("loc_2494")

    label("loc_245A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2494")

    #C0059
    ChrTalk(
        0xFE,
        (
            "那边那座东方式建筑……\x01",
            "完全变成一堆废墟了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2494")

    TalkEnd(0xFE)
    Return()

    # Function_16_22B0 end

    def Function_17_2498(): pass

    label("Function_17_2498")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_257D")

    #C0060
    ChrTalk(
        0xFE,
        (
            "虽然黑月的事务所遭到彻底破坏，\x01",
            "但经过这一周时间的沉淀，\x01",
            "这一带的气氛好像已经平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "也许是因为即将召开\x01",
            "居民投票活动，\x01",
            "情绪消沉的市民似乎并不多……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "这让人充分感受到了大家在\x01",
            "处于危难时刻的强韧信念。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257D")

    TalkEnd(0xFE)
    Return()

    # Function_17_2498 end

    def Function_18_2581(): pass

    label("Function_18_2581")

    TalkBegin(0xFE)

    #C0063
    ChrTalk(
        0xFE,
        (
            "该怎么说呢，\x01",
            "穿上新制服之后，\x01",
            "就觉得精神很振奋啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "总之，我今后一定\x01",
            "要为克洛斯贝尔独立国\x01",
            "鞠躬尽瘁。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2581 end

    def Function_19_25F6(): pass

    label("Function_19_25F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_269A")

    #C0065
    ChrTalk(
        0xFE,
        "发出蓝色光芒的大树……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "这不禁让人联想到利贝尔\x01",
            "方舟出现在利贝尔王国\x01",
            "的那起事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "据说利贝尔方舟\x01",
            "曾是一座古代都市，\x01",
            "那棵大树又是什么呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_269A")

    TalkEnd(0xFE)
    Return()

    # Function_19_25F6 end

    def Function_20_269E(): pass

    label("Function_20_269E")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0068
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(75920, 0, 7460, 1500)
    MoveCamera(45, 24, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(11500, 1500)
    Sleep(1000)
    SetChrName("")

    #A0069
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2761")
    OP_E2(0x2)
    MiniGame(0x6, 0x1, 0x14226, 0xFFFFF63C, 0x3AA2, 0xB4, 0x13812, 0xFFFFF254, 0x226A)

    label("loc_2761")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_269E end

    def Function_21_2766(): pass

    label("Function_21_2766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D8")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『羽扇河·第一灯塔』\x01\x01",
            " 无关人员禁止入内。\x01",
            "　　　　～克洛斯贝尔市～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Jump("loc_28CB")

    label("loc_27D8")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是通向地下空间Ｃ区域的门。\x01",
            "要打开吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C0")
    Fade(500)
    OP_68(75060, 800, 20060, 0)
    MoveCamera(43, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20250, 0)
    OP_0D()
    Sleep(500)
    Sound(100, 0, 70, 0)
    OP_71(0x8, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x8)
    Sleep(500)
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    OP_71(0x8, 0xB, 0x28, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    Sleep(500)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x0, 7)

    label("loc_28C0")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_28CB")

    Return()

    # Function_21_2766 end

    def Function_22_28CC(): pass

    label("Function_22_28CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28CB")
    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x109, 4330, 2000, 23330, 0)
    SetChrPos(0x102, 2900, 2000, 23240, 0)
    SetChrPos(0x101, 5350, 2000, 22780, 0)
    SetChrPos(0x103, 3280, 2000, 22060, 0)
    SetChrPos(0x104, 4150, 2000, 21040, 0)
    SetChrPos(0x105, 5950, 2000, 21600, 0)
    OP_68(4530, 3000, 23340, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15800, 0)
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    LoadChrToIndex("chr/ch28600.itc", 0x1F)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x15, 4700, 6500, 42400, 180)
    SetChrPos(0x16, 5750, 6500, 43250, 180)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    #C0072
    ChrTalk(
        0x109,
        "#10100F大家辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        (
            "啊，诺艾尔上士……\x01",
            "辛苦了！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "和上士在一起的这几位……\x01",
            "就是特别任务支援科的成员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        "你们来这里，是要执行什么公务吗？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00000F不，并没有什么\x01",
            "特别的工作……\x02\x03",

            "#00003F只是ＩＢＣ大楼被炸毁的时候，\x01",
            "我们就在现场附近，\x01",
            "所以比较担心这里的状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#12P#00101F……看来情况果然\x01",
            "很严重吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "是啊……瓦砾已经\x01",
            "堆积成山了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "老实说，要想重建大楼，\x01",
            "恐怕是很困难的。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xB,
        (
            "对了，那位大小姐现在\x01",
            "正在里面视察……\x02",
        )
    )

    CloseMessageWindow()

    #N0081
    NpcTalk(
        0x15,
        "女性的声音",
        (
            "哎呀，艾莉和各位……\x01",
            "你们在这种地方\x01",
            "做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_2CD7():
        OP_93(0xA, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2CD7)
    Sleep(50)

    def lambda_2CE7():
        OP_93(0xB, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2CE7)
    Sleep(300)
    SetChrPos(0x15, 3900, 5000, 37400, 180)
    SetChrPos(0x16, 4950, 5000, 39500, 180)
    OP_68(4640, 3200, 24370, 2000)
    MoveCamera(45, 15, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(19450, 2000)

    def lambda_2D47():
        OP_95(0x15, 3900, 5000, 27400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2D47)
    Sleep(200)

    def lambda_2D64():
        OP_95(0x16, 4950, 5000, 28000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2D64)
    Sleep(3000)

    #C0082
    ChrTalk(
        0x102,
        "#00105F#12P贝尔……！\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        "#00200F#12P玛丽亚贝尔小姐。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0084
    AnonymousTalk(
        0x15,
        (
            "嗯，我正好来\x01",
            "视察ＩＢＣ。\x02\x03",

            "呵呵，如果你们不赶时间，\x01",
            "就一起聊几句吧。\x02",
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
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0x0, 0x0)
    SetChrPos(0x15, 1350, 2000, 22900, 90)
    SetChrPos(0x16, 700, 2000, 24100, 90)
    OP_93(0x101, 0x10E, 0x0)
    OP_93(0x102, 0x10E, 0x0)
    OP_93(0x104, 0x10E, 0x0)
    OP_93(0x103, 0x10E, 0x0)
    OP_93(0x109, 0x10E, 0x0)
    OP_93(0x105, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_93(0xB, 0x10E, 0x0)
    OP_68(4570, 2700, 23870, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16720, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    #C0085
    ChrTalk(
        0x101,
        (
            "#00000F玛丽亚贝尔小姐……\x01",
            "好久不见了。\x02\x03",

            "#00004F上次见面，\x01",
            "还是在米修拉姆\x01",
            "招待我们的时候吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x15,
        (
            "#02900F#3P如此说来，\x01",
            "确实有很久\x01",
            "没见了。\x02\x03",

            "#02904F听说ＩＢＣ倒塌的时候，\x01",
            "你们就在现场，\x01",
            "还好大家都平安无事。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#11P#00100F贝尔……事件发生的时候，\x01",
            "你好像正巧去了米修拉姆吧？\x02\x03",

            "#00104F你平安无事，真是太好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x15,
        (
            "#02900F#3P呵呵，艾莉……\x01",
            "你竟然如此\x01",
            "担心我吗？\x02\x03",

            "#02909F啊，这真是因爱\x01",
            "而结下的羁绊啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0089
    ChrTalk(
        0x102,
        (
            "#11P#00106F贝、贝尔，你可真是的……\x01",
            "我当然会担心你啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        (
            "#00300F不过，该怎么说呢……\x01",
            "ＩＢＣ都被毁掉了，你却还是\x01",
            "一副轻松自如的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00000F嗯，是啊。看你这么气定神闲，\x01",
            "我也感觉轻松了不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x15,
        (
            "#02904F#3P呵……我看上去很轻松吗？\x02\x03",

            "#02901F其实我们的处境相当严峻。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0093
    ChrTalk(
        0x105,
        (
            "#10305F情况果然还是很糟糕啊？\x02\x03",

            "#10303F我们刚刚听说，\x01",
            "大楼已经化为一片废墟瓦砾了……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x15,
        (
            "#02901F#3P这已经不是糟糕的程度了！\x02\x03",

            "#02903F真是的，他们炸什么不好，\x01",
            "偏偏要炸ＩＢＣ大楼……！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x16,
        (
            "我作为护卫，陪同大小姐一起进去看过了。\x01",
            "里面一片狼藉，情况真是十分棘手。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x16,
        (
            "这次视察的目的是为了\x01",
            "回收保存在地下的\x01",
            "耀晶片和金库保管品……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x15,
        (
            "#02906F#3P但说实话，现在根本束手无策。\x02\x03",

            "#02901F想重建全毁的大楼十分困难，\x01",
            "单是清除堆积如山的瓦砾就要花费大量时间。\x02\x03",

            "#02906F所幸及时采用了紧急措施，\x01",
            "把银行的业务\x01",
            "全部转移到了兰花塔……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        (
            "#00204F#2P我们已经听说了。\x01",
            "好像是通过备份数据\x01",
            "迅速恢复了原有的机能吧？\x02\x03",

            "#00200FＩＢＣ这次的紧急\x01",
            "应对措施如此完善，\x01",
            "备受各国好评呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x15,
        (
            "#02902F#3P身为系统管理者，\x01",
            "我只是尽到了应尽职责而已。\x02\x03",

            "#02906F总之，现在至少可以\x01",
            "在兰花塔接待客户，\x01",
            "从结果来看，还算可以接受吧……\x02\x03",

            "#02901F那个叫做『赤色星座』的猎兵团\x01",
            "真是令人气愤啊。\x02\x03",

            "#02903F本来就已经忙得不行了，\x01",
            "却还来添乱，给我找了这么多麻烦……\x02\x03",

            "#02901F以后要是能逮到他们，\x01",
            "我一定会用尽一切手段，\x01",
            "把那些家伙大卸八块！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x102,
        (
            "#11P#00103F（唔，感觉真是\x01",
            "  怒气冲天啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0101
    ChrTalk(
        0x102,
        (
            "#11P#00105F对了……贝尔。\x02\x03",

            "你珍藏的那些\x01",
            "罗赞贝尔克人偶\x01",
            "怎么样了？\x02\x03",

            "#00103F该不会被埋在\x01",
            "瓦砾中了吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0102
    ChrTalk(
        0x15,
        (
            "#02903F#3P呵呵，怎么会。\x02\x03",

            "#02903F我早就对负责打扫房间的女仆下过指示，\x01",
            "一旦发生紧急情况，\x01",
            "就把它们装进皮箱里带出去。\x02\x03",

            "#02900F多亏我有先见之明，\x01",
            "那些孩子们全都毫发无伤。\x02\x03",

            "#02909F呵呵，也许是因为我平日\x01",
            "一直行善，因此才有了回报吧。\x01",
            "这也算是不幸中的大幸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#00009F（哈哈，一谈起人偶，\x01",
            "  她马上就显得很开心呢。）\x02\x03",

            "#00006F（……要是对待我\x01",
            "  也能这么和气\x01",
            "  就好了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x15, 500)

    #C0104
    ChrTalk(
        0x16,
        (
            "那个，玛丽亚贝尔小姐，\x01",
            "时间已经差不多了……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x15,
        (
            "#02905F#3P哎呀……聊得有点\x01",
            "太忘我了。\x02\x03",

            "#02900F好啦，艾莉，还有各位，\x01",
            "我就先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#00005F啊，在你百忙之中，\x01",
            "还占用你的宝贵时间，\x01",
            "真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        "#11P#00100F再见啦，贝尔。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x15,
        "#02902F#3P呵呵，再会。\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    def lambda_3ABC():
        OP_95(0x15, -6000, 2000, 22900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3ABC)
    OP_68(2500, 2700, 23800, 5000)

    def lambda_3AE7():

        label("loc_3AE7")

        TurnDirection(0x16, 0x15, 500)
        Yield()
        Jump("loc_3AE7")

    QueueWorkItem2(0x16, 2, lambda_3AE7)
    Sleep(1050)
    EndChrThread(0x16, 0x2)

    def lambda_3B00():
        OP_95(0x16, -6000, 2000, 24100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3B00)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_68(2500, 2700, 23800, 0)
    Sleep(500)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 4320, 2000, 22960, 0)
    SetScenarioFlags(0x191, 3)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_28CC end

    def Function_23_3B92(): pass

    label("Function_23_3B92")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, 21190, 0, 1100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, 22390, 0, 1100, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 7310, 0, 14850, 225)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xB, 0x17)
    OP_49()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    ClearChrFlags(0x18, 0x80)
    OP_78(0xC, 0x18)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x17, 3000, 2000, 21500, 0)
    OP_D5(0x17, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x18, 6000, 5300, 40000, 180)
    OP_D5(0x18, 0x2710, 0x2BF20, 0x0, 0x0)
    OP_68(19250, 2500, 10000, 0)
    MoveCamera(30, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30000, 0)
    OP_68(21000, 1000, 19800, 8000)
    MoveCamera(35, 15, 0, 8000)
    SetCameraDistance(20000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    Sound(459, 0, 50, 0)
    OP_6F(0x79)
    Fade(500)
    SetMapObjFrame(0xFF, "keepout", 0x0, 0x1)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(4450, 3200, 25750, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    MoveCamera(40, 30, 0, 7000)
    SetCameraDistance(25000, 7000)

    def lambda_3DB2():
        OP_95(0xFE, 500, 2000, 25450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3DB2)

    def lambda_3DCC():
        OP_95(0xFE, 8100, 2000, 25450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3DCC)
    BeginChrThread(0x17, 1, 0, 24)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x1F4)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0x10E, 0x1F4)
    BeginChrThread(0x18, 1, 0, 25)
    Sleep(3500)
    Sound(459, 0, 100, 0)
    OP_6F(0x79)
    StopSound(459, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c140D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_3B92 end

    def Function_24_3E2D(): pass

    label("Function_24_3E2D")

    Sound(492, 0, 50, 0)
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x8)
    OP_96(0xFE, 0xBB8, 0x7D0, 0x57E4, 0x3E8, 0x0)
    OP_79(0xB)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    StopSound(459, 200, 40)
    OP_71(0xB, 0x3C, 0x5A, 0x0, 0x8)
    OP_79(0xB)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3000, 2000, 23500)
    OP_9F(0x1, 3000, 2200, 25500)
    OP_9F(0x1, 3000, 6700, 45500)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_24_3E2D end

    def Function_25_3EB8(): pass

    label("Function_25_3EB8")

    OP_71(0xC, 0x5B, 0x78, 0x0, 0x8)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 6000, 6700, 45500)
    OP_9F(0x1, 6000, 2500, 27500)
    OP_9F(0x2, 0xFE, 4000, 0x6)
    OP_79(0xC)
    OP_71(0xC, 0x3C, 0x5A, 0x0, 0x8)
    OP_79(0xC)
    Return()

    # Function_25_3EB8 end

    def Function_26_3F00(): pass

    label("Function_26_3F00")

    EventBegin(0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02300.itp")
    Fade(500)
    OP_68(74500, -1600, 20000, 0)
    MoveCamera(41, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 73000, -2500, 19300, 90)
    SetChrPos(0x102, 73400, -2500, 20700, 90)
    SetChrPos(0x103, 72600, -2500, 18000, 45)
    SetChrPos(0x104, 72300, -2500, 21100, 90)
    SetChrPos(0x109, 71600, -2500, 18500, 90)
    SetChrPos(0x105, 71300, -2500, 20000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CF1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_408C")
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0109
    AnonymousTalk(
        0x8,
        (
            "怎么回事，\x01",
            "这也太慢了吧。\x02\x03",

            "算了，\x01",
            "咱们快走吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_410A")

    label("loc_408C")

    OP_63(0x8, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0110
    AnonymousTalk(
        0x8,
        (
            "哟，正等你们呢。\x02\x03",

            "好，\x01",
            "咱们快走吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_410A")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0111
    ChrTalk(
        0x101,
        (
            "#6P#00011F等等……\x01",
            "这么突然，你是要干什么呀？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#00306F真是的，这小鬼一点都没变，\x01",
            "还是这么我行我素。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "#02305F#11P哦，对了，\x01",
            "还没和你们仔细说过呢。\x02\x03",

            "#02309F哎呀，其实是这样。\x01",
            "我想让你们带我去\x01",
            "地下空间的终端室。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x109,
        "#6P#10105F地下空间的终端室……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x105,
        "#6P#10301F就是上次被炸毁的那个房间？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "#02303F#11P那是在地下空间Ｂ区域的\x01",
            "『第八控制终端』。\x02\x03",

            "#02300F这次想让你们带我去的是\x01",
            "在Ｃ区域的『第四控制终端』啦。\x02\x03",

            "#02309F嘿嘿～因为其它控制终端\x01",
            "用起来总是不那么自由。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0117
    ChrTalk(
        0x103,
        "#6P#00211F约纳，你还是这么不安分啊……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#00106F『导力网络基本法』\x01",
            "已经开始施行了。\x02\x03",

            "#00101F我们可不能协助\x01",
            "你违法占用终端哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#00013F而且，既然我们知道了这件事，\x01",
            "就必须阻止你这么做……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0120
    ChrTalk(
        0x8,
        (
            "#02305F#11P不、不不！\x01",
            "这并不能算是违法行为啦！\x02\x03",

            "#02303F因为我现在的身份是\x01",
            "财团的工程师！\x02\x03",

            "#02301F我也有管理地下空间\x01",
            "控制终端的权限！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(150)

    #C0121
    ChrTalk(
        0x101,
        "#5P#00001F……缇欧，怎么办？\x02",
    )

    CloseMessageWindow()

    def lambda_45DE():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_45DE)
    Sleep(50)

    def lambda_45EE():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_45EE)
    Sleep(50)

    def lambda_45FE():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_45FE)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0122
    ChrTalk(
        0x103,
        (
            "#6P#00206F虽然他确实拥有管理权限，\x01",
            "但还是觉得不够光明正大呢。\x02\x03",

            "#00200F看来导力网络基本法\x01",
            "还需稍加完善。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        "#5P#00108F嗯……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#00301F情况实在是\x01",
            "有些特殊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x109,
        (
            "#6P#10106F是啊，我们总不能帮你\x01",
            "钻法律的空子吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "#02311F#11P哎呀，真是的，你们太死脑筋了！\x02\x03",

            "#02310F那个团伙是叫『结社』吧？\x01",
            "他们好像在导力网络上\x01",
            "动了许多手脚。\x02\x03",

            "现在谁也不能保证他们\x01",
            "没做出什么事来吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4795():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4795)
    Sleep(50)

    def lambda_47A5():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_47A5)
    Sleep(50)

    def lambda_47B5():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_47B5)
    Sleep(50)

    def lambda_47C5():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_47C5)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    #C0127
    ChrTalk(
        0x101,
        "#6P#00005F这……\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x105,
        (
            "#6P#10303F……这的确\x01",
            "是个问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#02303F#11P主任大叔也很担心这件事，\x01",
            "但他太忙了，实在抽不出时间。\x02\x03",

            "所以我这个自由人\x01",
            "才特地前来援助。\x02\x03",

            "#02301F你们不但不感谢我，\x01",
            "反倒百般阻挠，这不是很奇怪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#00306F真是的，这小鬼\x01",
            "只有嘴上功夫最厉害。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#6P#00203F……但确实如他所说，\x01",
            "这些情况很令人在意。\x02\x03",

            "#00208F那个自称『小丑』的少年……\x01",
            "还有名叫诺华提斯的博士……\x02\x03",

            "#00201F他们恐怕拥有比财团\x01",
            "还要先进的网络技术。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#6P#00008F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0133
    ChrTalk(
        0x101,
        (
            "#6P#00001F好吧，我们帮你。\x02\x03",

            "#00003F但是，不要做出明显违法\x01",
            "的黑客行为。\x02\x03",

            "另外，不要在地下一待就是好几天，\x01",
            "要回自己房间的床上睡觉。\x02\x03",

            "#00000F这就是条件。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "#02306F#11P喂喂，饶了我吧～\x02\x03",

            "#02302F我天才约纳大人为何\x01",
            "要向这现实世界妥协……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#6P#00013F（瞪……）\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        "#02305F#11P呜……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，罗伊德在这方面\x01",
            "还是很严厉的。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#6P#00204F这些条件并不算苛刻，\x01",
            "你还是乖乖接受了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#02311F#11P唉，真是的，我知道了！\x02\x03",

            "我接受刚才说的条件，\x01",
            "赶快带我过去吧！\x02\x03",

            "#02307F兰花塔的所有终端\x01",
            "都有各种各样的权限限制，\x01",
            "我已经受够了！\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        "#00302F哈，这才是你的真心话啊。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x109,
        (
            "#6P#10108F唔……\x01",
            "他的心态果然有些不健全啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#02306F#11P烦、烦死了。\x02\x03",

            "#02300F我们要去的是Ｃ区域……\x01",
            "你们准备好了吗？\x02\x03",

            "那里应该和地下空间的其它区域一样，\x01",
            "也会有魔兽之类的东西出没。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#6P#00008F嗯……\x02",
    )

    CloseMessageWindow()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x181, 3)
    Jump("loc_4D78")

    label("loc_4CF1")


    #C0144
    ChrTalk(
        0x8,
        (
            "#02305F#11P怎么样，已经准备好了吗？\x02\x03",

            "#02300F和地下空间的其它区域一样，\x01",
            "Ｃ区域应该也会有魔兽之类的东西出没。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#6P#00008F嗯……\x02",
    )

    CloseMessageWindow()

    label("loc_4D78")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "准备完毕\x01",          # 0
            "还需继续准备\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SoundLoad(145)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4DCB"),
        (1, "loc_5241"),
        (SWITCH_DEFAULT, "loc_52B5"),
    )


    label("loc_4DCB")


    #C0146
    ChrTalk(
        0x8,
        (
            "#02309F#11P嘿嘿，那我们\x01",
            "就赶快下去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0147
    ChrTalk(
        0x109,
        "#6P#10105F下去……？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x104,
        "#00305F什么意思？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "#02304F#11P哦，Ｃ区域的入口\x01",
            "就在这座灯塔中啊。\x02\x03",

            "#02302F你们不知道吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#6P#00011F是、是吗？\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        "#02309F#11P哼哼，你们看。\x02",
    )

    CloseMessageWindow()
    OP_68(77500, -1000, 20000, 1500)
    MoveCamera(49, 15, 0, 1500)
    SetCameraDistance(21000, 1500)
    OP_93(0x8, 0x5A, 0x1F4)

    def lambda_4F76():
        OP_95(0xFE, 76400, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4F76)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    Sound(100, 0, 70, 0)
    OP_71(0x8, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x8)
    Sleep(1000)
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    OP_71(0x8, 0xB, 0x28, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0152
    ChrTalk(
        0x102,
        "#00105F竟然在这种地方……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x105,
        (
            "#6P#N#10302F哎呀呀，\x01",
            "真是趣味性十足的构造。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x1F4)

    #C0154
    ChrTalk(
        0x8,
        (
            "#11P#02302F#11P好，那我们就\x01",
            "快点进去吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    OP_63(0x8, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)

    def lambda_5126():
        OP_95(0xFE, 77500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5126)
    WaitChrThread(0x8, 1)
    Sound(102, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)

    def lambda_515F():
        OP_95(0xFE, 80500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_515F)
    BeginChrThread(0x101, 3, 0, 27)
    Sleep(900)
    BeginChrThread(0x102, 3, 0, 27)
    Sleep(300)
    BeginChrThread(0x103, 3, 0, 27)
    Sleep(800)
    BeginChrThread(0x104, 3, 0, 27)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 27)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 27)
    StopSound(126, 1000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0155
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约纳以保护对象的身份加入队伍，\x01",
            "当其ＨＰ降为０时，游戏就会结束。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddParty(0x3D, 0xFF, 0xFF)
    SetScenarioFlags(0x181, 4)
    OP_29(0xAC, 0x1, 0x8)
    StopBGM(0xFA0)
    WaitBGM()
    EventEnd(0x5)
    NewScene("m0200", 100, 0, 0)
    IdleLoop()
    Jump("loc_52B5")

    label("loc_5241")


    #C0156
    ChrTalk(
        0x8,
        (
            "#02303F#11P是吗，那就\x01",
            "快去准备吧。\x02\x03",

            "#02300F我在这里等你们。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 72500, -2500, 20000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_24(0x91)
    EventEnd(0x5)
    Jump("loc_52B5")

    label("loc_52B5")

    Return()

    # Function_26_3F00 end

    def Function_27_52B6(): pass

    label("Function_27_52B6")


    def lambda_52BB():
        OP_95(0xFE, 76000, -2500, 20000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_52BB)
    WaitChrThread(0xFE, 1)

    def lambda_52D9():
        OP_95(0xFE, 80500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_52D9)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_52B6 end

    def Function_28_52F3(): pass

    label("Function_28_52F3")


    def lambda_52F8():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_52F8)

    def lambda_5312():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5312)
    WaitChrThread(0xFE, 1)

    def lambda_5327():
        OP_95(0xFE, 66900, -2500, 17100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5327)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_52F3 end

    def Function_29_5348(): pass

    label("Function_29_5348")


    def lambda_534D():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_534D)

    def lambda_5367():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5367)
    WaitChrThread(0xFE, 1)

    def lambda_537C():
        OP_95(0xFE, 69300, -2500, 18400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_537C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_29_5348 end

    def Function_30_539D(): pass

    label("Function_30_539D")


    def lambda_53A2():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53A2)

    def lambda_53BC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_53BC)
    WaitChrThread(0xFE, 1)

    def lambda_53D1():
        OP_95(0xFE, 68500, -2500, 17300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53D1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_539D end

    def Function_31_53F2(): pass

    label("Function_31_53F2")


    def lambda_53F7():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53F7)

    def lambda_5411():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5411)
    WaitChrThread(0xFE, 1)

    def lambda_5426():
        OP_95(0xFE, 69800, -2500, 16600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5426)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_53F2 end

    def Function_32_5447(): pass

    label("Function_32_5447")


    def lambda_544C():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_544C)

    def lambda_5466():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5466)
    WaitChrThread(0xFE, 1)

    def lambda_547B():
        OP_95(0xFE, 70600, -2500, 17700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_547B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_5447 end

    def Function_33_549C(): pass

    label("Function_33_549C")


    def lambda_54A1():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_54A1)

    def lambda_54BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_54BB)
    WaitChrThread(0xFE, 1)

    def lambda_54D0():
        OP_95(0xFE, 68300, 0, 19100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_54D0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_549C end

    def Function_34_54F1(): pass

    label("Function_34_54F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51522.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    SoundLoad(145)
    SoundLoad(3520)
    SoundLoad(3521)
    SoundLoad(3522)
    SetChrPos(0x101, 79000, -2500, 20000, 270)
    SetChrPos(0x102, 79000, -2500, 20000, 270)
    SetChrPos(0x103, 79000, -2500, 20000, 270)
    SetChrPos(0x104, 79000, -2500, 20000, 270)
    SetChrPos(0x109, 79000, -2500, 20000, 270)
    SetChrPos(0x105, 79000, -2500, 20000, 270)
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
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xEE, 0x98, 0x84, 0x2D, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    PlayBGM("ed7514", 0)
    OP_68(79000, -1500, 20000, 0)
    MoveCamera(59, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26500, 0)
    OP_70(0x8, 0xB)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    ClearMapObjFlags(0x8, 0x10)
    OP_71(0x8, 0xB, 0x28, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    Sound(102, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)
    OP_68(69000, -1500, 17600, 7500)
    MoveCamera(59, 17, 0, 7500)
    SetCameraDistance(22500, 7500)
    BeginChrThread(0x101, 3, 0, 28)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 30)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 29)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 31)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 33)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 32)
    Sleep(1500)
    Sound(102, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    OP_71(0x8, 0x28, 0x47, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    OP_6F(0x79)

    #C0157
    ChrTalk(
        0x101,
        "#5P#00008F刚好到了傍晚……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#5P#00106F今晚要在外面吃饭……\x01",
            "工作就到此为止了吧？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 3)

    #C0159
    ChrTalk(
        0x109,
        "#10108F#5P是的……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x105)
    OP_64(0x109)
    Sleep(500)
    Fade(2000)
    OP_68(79000, 3000, 10000, 0)
    MoveCamera(55, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45000, 0)
    MoveCamera(75, 0, 0, 12000)
    SetCameraDistance(40000, 12000)
    OP_6F(0x79)
    Fade(500)
    OP_68(68300, -1500, 18500, 0)
    MoveCamera(59, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(24000, 2000)

    def lambda_58D2():
        OP_96(0xFE, 0x10ACC, 0xFFFFF63C, 0x4C2C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_58D2)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0160
    AnonymousTalk(
        0x109,
        (
            "#3520V#30W在这段日子里，\x01",
            "真是承蒙各位照顾了。\x02\x03",

            "#3521V虽然共处的时间很短暂……\x01",
            "但我学到了很多东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDC1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)

    def lambda_59D5():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_59D5)
    Sleep(50)

    def lambda_59E5():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_59E5)
    Sleep(50)

    def lambda_59F5():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_59F5)
    Sleep(50)

    def lambda_5A05():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5A05)
    Sleep(50)

    def lambda_5A15():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5A15)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    Sleep(150)

    #C0161
    ChrTalk(
        0x101,
        (
            "#12P#00004F诺艾尔……\x01",
            "那些话应该由我们来说才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        (
            "#00102F#12P……正好过了\x01",
            "三个月呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#12P#00206F和我则是一起过了\x01",
            "两个月左右……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x104,
        (
            "#12P#00302F该怎么说呢……\x01",
            "你走了之后，我们肯定会很寂寞的。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x109,
        (
            "#10112F#5P哈哈……\x01",
            "我也很舍不得大家啊。\x02\x03",

            "#10108F而且，结社和猎兵团……\x01",
            "还有幻兽和蓝花等问题都还没解决……\x02\x03",

            "#10106F在这种情况下，我却要离开队伍，\x01",
            "真是十分抱歉……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        "#12P#00008F诺艾尔……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x105,
        (
            "#10304F#11P不必介意，虽然身份不同，\x01",
            "但我们热爱克洛斯贝尔的心情却是一样的，\x01",
            "这就足够了吧？\x02\x03",

            "#10302F不过，从我口中说出这样的话，\x01",
            "好像有些奇怪呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x105, 500)
    Sleep(150)

    #C0168
    ChrTalk(
        0x109,
        "#10102F#5P瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x105,
        (
            "#10304F#11P等这次的事情告一段落之后，\x01",
            "你再回支援科就是了。\x02\x03",

            "#10302F毕竟你是个\x01",
            "前途无量的未来之星。\x02\x03",

            "#10309F相比在警备队打打杀杀，\x01",
            "还是在这里工作更能开阔眼界，\x01",
            "学习到更多的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x109,
        (
            "#10101F#5P真、真是的……\x01",
            "都要分别了，口气还这么得意忘形。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#12P#00012F哈哈……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        (
            "#12P#00304F说起来，索妮亚司令\x01",
            "正是抱此希望，所以才会\x01",
            "把你外派到这边的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#00102F#12P只要诺艾尔小姐愿意，\x01",
            "我们以后还要在一起工作哦。\x02\x03",

            "#00109F就算不能一起工作，\x01",
            "在假日也可以一起出去玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        (
            "#12P#00204F……我还想让诺艾尔小姐\x01",
            "教我开车呢。\x02\x03",

            "#00202F可惜现在还没到驾驶年龄，\x01",
            "以后可一定要教我哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0175
    ChrTalk(
        0x109,
        (
            "#10112F#5P啊哈哈……（忍住眼泪）。\x01",
            "乐意效劳！\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        "#12P#00008F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0177
    ChrTalk(
        0x101,
        (
            "#12P#00004F谢谢，诺艾尔。\x02\x03",

            "你的驾驶技巧、战斗技术和优秀的\x01",
            "行动力给我们带来了很多帮助……\x02\x03",

            "#00000F更重要的是，你那率直的性格\x01",
            "总能使我们勇气倍增。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x109,
        "#10105F#5P罗伊德警官……\x02",
    )

    CloseMessageWindow()
    OP_68(68400, -1400, 18800, 1800)
    MoveCamera(44, 13, 0, 1800)
    SetCameraDistance(22500, 1800)

    def lambda_6013():

        label("loc_6013")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6013")

    QueueWorkItem2(0x109, 2, lambda_6013)

    def lambda_6025():
        OP_95(0xFE, 67300, -2500, 19200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6025)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x109, 500)
    EndChrThread(0x109, 0x2)
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x8)
    SetChrFlags(0x109, 0x10)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x20)
    Sound(802, 0, 100, 0)
    Sleep(110)
    SetChrSubChip(0x101, 0x1)
    Sleep(110)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0179
    ChrTalk(
        0x101,
        (
            "#6P#00002F分别之后，我们依然是同伴。\x02\x03",

            "如果以后在警备队遇到了困难，\x01",
            "一定要告诉我们哦。\x02\x03",

            "#00009F我们今后要是需要你的帮助，\x01",
            "也会毫不客气地直接求助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x109,
        "#11P#10114F……啊…………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x109, 0xB)
    Sleep(130)
    SetChrSubChip(0x109, 0xC)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0181
    ChrTalk(
        0x109,
        "#11P#10112F好的！没问题！\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1300)

    #C0182
    ChrTalk(
        0x105,
        "#10302F#11P（呵呵，不愧是队长。）\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#12P#00211F（瞬间就抓住\x01",
            "  博取好感的机会了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        "#11P#00113F（真、真是的……）\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        (
            "#12P#00302F（哈哈，大小姐可要\x01",
            "  再加一把劲才行哦。）\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#11P#00112F（我、我才没有……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x6)
    Sleep(50)
    SetChrSubChip(0x109, 0xE)
    Sleep(200)

    #C0187
    ChrTalk(
        0x101,
        "#5P#00005F怎么了？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0188
    ChrTalk(
        0x109,
        "#5P#10114F#3522V#12A#30W哎……啊啊……！\x02",
    )
    #Auto

    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x10)
    ClearChrFlags(0x109, 0x2)
    ClearChrFlags(0x109, 0x20)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_63C3():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_63C3)

    def lambda_63D0():

        label("loc_63D0")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_63D0")

    QueueWorkItem2(0x102, 2, lambda_63D0)

    def lambda_63E2():

        label("loc_63E2")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_63E2")

    QueueWorkItem2(0x105, 2, lambda_63E2)

    def lambda_63F4():

        label("loc_63F4")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_63F4")

    QueueWorkItem2(0x104, 2, lambda_63F4)
    OP_68(69100, -1400, 18800, 650)
    SetCameraDistance(23000, 650)

    def lambda_6420():
        OP_96(0xFE, 0x10D88, 0xFFFFF63C, 0x4DBC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6420)
    WaitChrThread(0x109, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)

    #C0189
    ChrTalk(
        0x109,
        (
            "#10112F#5P对、对不起，\x01",
            "并不是你们想象中的那种……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#12P#00309F嗯？我们想象\x01",
            "什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，单从这层意义上说，\x01",
            "我也很希望你今后回到支援科，\x01",
            "不然就看不到后续发展了。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x109,
        "#10114F#5P前、前辈！瓦吉！\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        "#11P#00113F呼……真是的。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        "#6P#00011F？？？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(69290, -1400, 18560, 1800)

    def lambda_656F():

        label("loc_656F")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_656F")

    QueueWorkItem2(0x101, 2, lambda_656F)

    def lambda_6581():
        OP_96(0xFE, 0x10810, 0xFFFFF63C, 0x4394, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6581)
    WaitChrThread(0x101, 1)
    EndChrThread(0x101, 0x2)
    OP_6F(0x79)

    #C0195
    ChrTalk(
        0x101,
        "#6P#00008F（……缇欧，怎么回事？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_662D")

    #C0196
    ChrTalk(
        0x103,
        (
            "#12P#00211F（……唉，\x01",
            "  请你自己去想吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        "#6P#00006F（好像生气了……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6687")

    label("loc_662D")


    #C0198
    ChrTalk(
        0x103,
        (
            "#12P#00204F（呼，看来罗伊德前辈\x01",
            "  还是不够成熟呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        "#6P#00006F（被教训了……）\x02",
    )

    CloseMessageWindow()

    label("loc_6687")

    SetCameraDistance(23500, 2000)
    StopSound(126, 1000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    SetChrName("")

    #A0200
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当晚，罗伊德一行人在中央广场的餐厅\x01",
            "为诺艾尔举行了送别会。\x02\x03",

            "赛尔盖和琪雅自不必说，\x01",
            "连蔡特也被破例招待入店，\x01",
            "令人依依不舍的快乐夜晚就这样过去了……\x02\x03",

            "翌日上午，诺艾尔收拾好行李之后，\x01",
            "离开了特别任务支援科的大楼。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    OP_BC(0x8)
    OP_BC(0x4)
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x91)
    SetScenarioFlags(0x22, 2)
    NewScene("m0209", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_54F1 end

    def Function_35_67AE(): pass

    label("Function_35_67AE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　 ～　地皮待售　～ 　　\x01",
            "克洛斯贝尔市·城市规划科\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_67AE end

    def Function_36_681A(): pass

    label("Function_36_681A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　＜此区域禁止入内＞\x01",
            "      此处危险，\x01",
            "      请勿入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_36_681A end

    SaveToFile()

Try(main)
