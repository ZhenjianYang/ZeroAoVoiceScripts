from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1000.bin",                # FileName
        "c1000",                    # MapName
        "c1000",                    # Location
        0x0010,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c1000", "c1000_1", "c1000_2", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 8, 0, 9],
    )

    BuildStringList((
        "c1000",                  # 0
        "库隆克",                 # 1
        "迪因兹",                 # 2
        "莉莉",                   # 3
        "玛尔缇",                 # 4
        "戴纳",                   # 5
        "安奈",                   # 6
        "卢诺爷爷",               # 7
        "洛依",                   # 8
        "梅琳",                   # 9
        "斯赞",                   # 10
        "基雷",                   # 11
        "库塔",                   # 12
        "摩尔斯老人",             # 13
        "搜查官",                 # 14
        "车",                     # 15
        "飙车族",                 # 16
        "警车",                   # 17
        "赛尔丹分部长",           # 18
        "克潘",                   # 19
        "彼德",                   # 20
        "谢莉",                   # 21
        "国防军士兵",             # 22
        "国防军士兵",             # 23
        "市民１",                 # 24
        "市民２",                 # 25
        "市民３",                 # 26
        "市民４",                 # 27
        "市民５",                 # 28
        "市民６",                 # 29
        "市民７",                 # 30
        "警官",                   # 31
        "警官",                   # 32
        "警官",                   # 33
        "警官",                   # 34
        "帕欧拉婆婆",             # 35
        "bc1000",                 # 36
        "中央广场",               # 37
        "西街",                   # 38
        "行政区",                 # 39
        "住宅街",                 # 40
        "欢乐街",                 # 41
        "东街",                   # 42
        "旧城区",                 # 43
        "港湾区",                 # 44
        "ＩＢＣ",                 # 45
        "站前街道",               # 46
        "后巷",                   # 47
        "乌尔斯拉间道",           # 48
        "东克洛斯贝尔街道",       # 49
        "西克洛斯贝尔街道",       # 50
        "玛因兹山道",             # 51
        "兰花塔",                 # 52
    ))

    ATBonus("ATBonus_950", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_B612", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_9A0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_9A4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_9A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_9AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_9B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_9B4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_9B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_9BC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_A00", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_A04", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_A08", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_A0C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_A10", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_A14", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_A18", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_A1C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_980", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_984", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_988", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_98C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_990", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_994", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_998", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_99C", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_A20", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc1000", "Sepith_B612", 60, 30, 10, 0,
        (
            ("ms85100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_9A0", "MonsterBattlePostion_A00", "ed7450", "ed7453", "ATBonus_950"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_980", "MonsterBattlePostion_A00", "ed7450", "ed7453", "ATBonus_950"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_9A0", "MonsterBattlePostion_A00", "ed7450", "ed7453", "ATBonus_950"),
            (),
        )
    )

    AddCharChip((
        "chr/ch23500.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch24800.itc",                   # 02
        "chr/ch24900.itc",                   # 03
        "chr/ch21100.itc",                   # 04
        "chr/ch24000.itc",                   # 05
        "chr/ch21200.itc",                   # 06
        "chr/ch21500.itc",                   # 07
        "chr/ch10300.itc",                   # 08
        "chr/ch26200.itc",                   # 09
        "chr/ch21400.itc",                   # 0A
        "chr/ch20800.itc",                   # 0B
        "chr/ch49800.itc",                   # 0C
        "chr/ch49600.itc",                   # 0D
        "chr/ch49700.itc",                   # 0E
        "chr/ch49900.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "chr/ch27600.itc",                   # 12
        "chr/ch24200.itc",                   # 13
    ))

    DeclNpc(-24409,  -3000,   5239,    180,  261,  0x0, 0,   1,   0,   0,   0,   2,   0,   255,  0)
    DeclNpc(-13039,  -3000,   -810,    225,  261,  0x0, 0,   2,   0,   0,   0,   2,   1,   255,  0)
    DeclNpc(-16500,  -3000,   2920,    45,   261,  0x0, 0,   3,   0,   0,   7,   2,   2,   255,  0)
    DeclNpc(-4559,   -3000,   -8949,   180,  261,  0x0, 0,   0,   0,   0,   0,   2,   3,   255,  0)
    DeclNpc(-5559,   -3000,   -8949,   180,  389,  0x0, 0,   19,  0,   0,   0,   2,   15,  255,  0)
    DeclNpc(26200,   -300,    -1049,   270,  261,  0x0, 0,   4,   0,   0,   1,   2,   7,   255,  0)
    DeclNpc(-40490,  -300,    15850,   90,   261,  0x0, 0,   5,   0,   0,   6,   2,   8,   255,  0)
    DeclNpc(-18200,  -300,    18139,   270,  261,  0x0, 0,   6,   0,   0,   0,   2,   9,   255,  0)
    DeclNpc(-22280,  -300,    18370,   225,  261,  0x0, 0,   7,   0,   0,   2,   2,   10,  255,  0)
    DeclNpc(-8470,   -3000,   -7349,   45,   261,  0x0, 0,   8,   0,   0,   0,   2,   12,  255,  0)
    DeclNpc(-7420,   -3000,   -8600,   45,   261,  0x0, 0,   9,   0,   0,   0,   2,   13,  255,  0)
    DeclNpc(-15939,  -3000,   -600,    45,   261,  0x0, 0,   10,  0,   0,   3,   2,   14,  255,  0)
    DeclNpc(-18200,  -300,    18139,   270,  389,  0x0, 0,   11,  0,   0,   0,   2,   11,  255,  0)
    DeclNpc(-3049,   -3000,   -13779,  315,  385,  0x0, 0,   18,  0,   0,   0,   2,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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

    DeclMonster(-17640,  14650,   -310,    0x10100E1,    "BattleInfo_A20", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(530,     -13160,  -3000,   0x101013B,    "BattleInfo_A20", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 12,  -26.8700008392334,     4.059999942779541,     -4.0,                  20.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   8.956666946411133,     -1.3533333539962769,   0.800000011920929,     1.0])
    DeclEvent(0x0000, 0, 13,  -15.1899995803833,     -5.800000190734863,    -6.5,                  37.515625,             [0.20203045010566711,  0.20203058421611786,   -0.0,                  0.0,                   -0.20203058421611786,  0.20203045010566711,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.8970650434494019,    4.240621089935303,     1.3000000715255737,    1.0])

    DeclActor(-30000,  -5500,   4000,    1200,    -30000,  -4500,   4000,    0x007C, 0,  10, 0x0000)
    DeclActor(-23010,  -14900,  -4830,   1200,    -23010,  -13900,  -4830,   0x007C, 0,  11, 0x0000)
    DeclActor(-190,    340,     6410,    2000,    -190,    1540,    6410,    0x007C, 0,  35, 0x0000)
    DeclActor(17360,   -300,    4630,    1200,    17530,   1500,    5120,    0x007C, 0,  17, 0x0000)
    DeclActor(-15920,  240,     24020,   2000,    -15920,  1540,    24020,   0x007C, 0,  36, 0x0000)
    DeclActor(17360,   -300,    4630,    1200,    17530,   1500,    5120,    0x007C, 0,  37, 0x0000)
    DeclActor(12360,   250,     5680,    1200,    12360,   1540,    5680,    0x007C, 0,  41, 0x0000)
    DeclActor(-33350,  -5500,   9380,    1200,    -33350,  -4000,   9380,    0x007C, 0,  14, 0x0000)

    PlaceName(-111.26000213623047, 0.0, 15.239999771118164, 0x0000, 0x0000, "中央广场")
    PlaceName(-186.8800048828125, 0.0, 20.40999984741211, 0x0000, 0x0000, "西街")
    PlaceName(-80.20999908447266, 0.0, 117.58999633789062, 0x0000, 0x0000, "行政区")
    PlaceName(-257.0299987792969, 0.0, 106.08999633789062, 0x0000, 0x0000, "住宅街")
    PlaceName(-173.0800018310547, 0.0, 96.88999938964844, 0x0000, 0x0000, "欢乐街")
    PlaceName(-17.829999923706055, 0.0, -11.210000038146973, 0x0000, 0x0000, "东街")
    PlaceName(23.0, 0.0, -74.45999908447266, 0x0000, 0x0000, "旧城区")
    PlaceName(14.380000114440918, 0.0, 64.69000244140625, 0x0000, 0x0000, "港湾区")
    PlaceName(-15.529999732971191, 0.0, 172.7899932861328, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-98.33000183105469, 0.0, -64.11000061035156, 0x0000, 0x0000, "站前街道")
    PlaceName(-152.3800048828125, 0.0, 55.4900016784668, 0x0000, 0x0000, "后巷")
    PlaceName(-101.77999877929688, 0.0, -99.76000213623047, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(44.279998779296875, 0.0, 4.889999866485596, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-245.52999877929688, 0.0, 18.690000534057617, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-238.6300048828125, 0.0, 133.69000244140625, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-88.0, 0.0, 269.0, 0x0000, 0x0000, "兰花塔")
    PlaceName(-136.55999755859375, 0.0, -0.8600000143051147, 0x0000, 0x0051, "")
    PlaceName(-74.75, 0.0, 29.040000915527344, 0x0000, 0x0054, "")
    PlaceName(-108.38999938964844, 0.0, -10.0600004196167, 0x0000, 0x0057, "")
    PlaceName(-137.42999267578125, 0.0, 32.4900016784668, 0x0000, 0x0053, "")
    PlaceName(-113.8499984741211, 0.0, 60.09000015258789, 0x0000, 0x0053, "")
    PlaceName(-172.2100067138672, 0.0, 26.739999771118164, 0x0000, 0x0053, "")
    PlaceName(-183.42999267578125, 0.0, 50.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-155.8300018310547, 0.0, 87.69000244140625, 0x0000, 0x0052, "")
    PlaceName(-150.36000061035156, 0.0, 72.73999786376953, 0x0000, 0x0053, "")
    PlaceName(-140.3000030517578, 0.0, 62.959999084472656, 0x0000, 0x0053, "")
    PlaceName(-107.52999877929688, 0.0, 144.61000061035156, 0x0000, 0x0051, "")
    PlaceName(21.280000686645508, 0.0, -11.210000038146973, 0x0000, 0x0052, "")
    PlaceName(1.7300000190734863, 0.0, -115.29000091552734, 0x0000, 0x0053, "")
    PlaceName(-13.229999542236328, 0.0, -94.01000213623047, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_B94",          # 00, 0
        "Function_1_C44",          # 01, 1
        "Function_2_CDD",          # 02, 2
        "Function_3_D08",          # 03, 3
        "Function_4_D7D",          # 04, 4
        "Function_5_E1A",          # 05, 5
        "Function_6_E67",          # 06, 6
        "Function_7_F28",          # 07, 7
        "Function_8_F75",          # 08, 8
        "Function_9_169B",         # 09, 9
        "Function_10_1C33",        # 0A, 10
        "Function_11_1D6E",        # 0B, 11
        "Function_12_1EA9",        # 0C, 12
        "Function_13_20A2",        # 0D, 13
        "Function_14_22CE",        # 0E, 14
        "Function_15_2A32",        # 0F, 15
        "Function_16_2AE5",        # 10, 16
        "Function_17_2CD7",        # 11, 17
        "Function_18_2CD8",        # 12, 18
        "Function_19_30C5",        # 13, 19
        "Function_20_32B8",        # 14, 20
        "Function_21_361F",        # 15, 21
        "Function_22_36C3",        # 16, 22
        "Function_23_3AFC",        # 17, 23
        "Function_24_3E47",        # 18, 24
        "Function_25_4351",        # 19, 25
        "Function_26_468F",        # 1A, 26
        "Function_27_4ADF",        # 1B, 27
        "Function_28_4EAF",        # 1C, 28
        "Function_29_56D7",        # 1D, 29
        "Function_30_6768",        # 1E, 30
        "Function_31_6784",        # 1F, 31
        "Function_32_67A0",        # 20, 32
        "Function_33_67BC",        # 21, 33
        "Function_34_67D8",        # 22, 34
        "Function_35_67F4",        # 23, 35
        "Function_36_6DF2",        # 24, 36
        "Function_37_6F29",        # 25, 37
        "Function_38_8E8B",        # 26, 38
        "Function_39_90EE",        # 27, 39
        "Function_40_92C1",        # 28, 40
        "Function_41_A73A",        # 29, 41
        "Function_42_A871",        # 2A, 42
        "Function_43_B174",        # 2B, 43
        "Function_44_B1AB",        # 2C, 44
        "Function_45_B1F6",        # 2D, 45
        "Function_46_B2A7",        # 2E, 46
        "Function_47_B543",        # 2F, 47
    ))


    def Function_0_B94(): pass

    label("Function_0_B94")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_BCC"),
        (1, "loc_BD8"),
        (2, "loc_BE4"),
        (3, "loc_BF0"),
        (4, "loc_BFC"),
        (5, "loc_C08"),
        (6, "loc_C14"),
        (SWITCH_DEFAULT, "loc_C20"),
    )


    label("loc_BCC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BD8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BE4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BF0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BFC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C08")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C14")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C20")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C43")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C43")

    Return()

    # Function_0_B94 end

    def Function_1_C44(): pass

    label("Function_1_C44")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CDC")
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -40270, -300, 12170, 2000, 0x0)
    Sleep(2500)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, 26200, -300, -1050, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    Jump("Function_1_C44")

    label("loc_CDC")

    Return()

    # Function_1_C44 end

    def Function_2_CDD(): pass

    label("Function_2_CDD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D07")
    OP_94(0xFE, 0xFFFFB000, 0x4ECA, 0xFFFFA8EE, 0x3F01, 0x3E8)
    Sleep(300)
    Jump("Function_2_CDD")

    label("loc_D07")

    Return()

    # Function_2_CDD end

    def Function_3_D08(): pass

    label("Function_3_D08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D7C")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_3_D08")

    label("loc_D7C")

    Return()

    # Function_3_D08 end

    def Function_4_D7D(): pass

    label("Function_4_D7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E19")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_95(0xFE, -8470, -3000, -7350, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    Jump("Function_4_D7D")

    label("loc_E19")

    Return()

    # Function_4_D7D end

    def Function_5_E1A(): pass

    label("Function_5_E1A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E66")
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -9950, -3000, -6670, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_5_E1A")

    label("loc_E66")

    Return()

    # Function_5_E1A end

    def Function_6_E67(): pass

    label("Function_6_E67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F27")
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, 26030, -300, 2230, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -40490, -300, 15850, 2000, 0x0)
    Sleep(2400)
    Jump("Function_6_E67")

    label("loc_F27")

    Return()

    # Function_6_E67 end

    def Function_7_F28(): pass

    label("Function_7_F28")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F74")
    OP_95(0xFE, -15130, -3000, 1420, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    OP_95(0xFE, -16500, -3000, 2920, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    Jump("Function_7_F28")

    label("loc_F74")

    Return()

    # Function_7_F28 end

    def Function_8_F75(): pass

    label("Function_8_F75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1195")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1040")
    SetChrPos(0x0, -20760, -310, 33300, 180)
    SetChrPos(0x1, -20760, -310, 33300, 180)
    SetChrPos(0x2, -20760, -310, 33300, 180)
    SetChrPos(0x3, -20760, -310, 33300, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1013")
    SetChrPos(0x4, -20760, -310, 33300, 180)
    SetChrPos(0x5, -20760, -310, 33300, 180)
    Jump("loc_1032")

    label("loc_1013")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1032")
    SetChrPos(0x4, -20760, -310, 33300, 180)

    label("loc_1032")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1195")

    label("loc_1040")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F4")
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    SetChrPos(0x1, 1910, -3000, -35980, 0)
    SetChrPos(0x2, 1910, -3000, -35980, 0)
    SetChrPos(0x3, 1910, -3000, -35980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C7")
    SetChrPos(0x4, 1910, -3000, -35980, 0)
    SetChrPos(0x5, 1910, -3000, -35980, 0)
    Jump("loc_10E6")

    label("loc_10C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E6")
    SetChrPos(0x4, 1910, -3000, -35980, 0)

    label("loc_10E6")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1195")

    label("loc_10F4")

    SetChrPos(0x0, -29790, -330, 13830, 90)
    SetChrPos(0x1, -29790, -330, 13830, 90)
    SetChrPos(0x2, -29790, -330, 13830, 90)
    SetChrPos(0x3, -29790, -330, 13830, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116D")
    SetChrPos(0x4, -29790, -330, 13830, 90)
    SetChrPos(0x5, -29790, -330, 13830, 90)
    Jump("loc_118C")

    label("loc_116D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118C")
    SetChrPos(0x4, -29790, -330, 13830, 90)

    label("loc_118C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1195")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11B1")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_154F")

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_11F6")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_154F")

    label("loc_11F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1237")
    SetChrPos(0x10, -22760, -3000, 5010, 0)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0xF, -21950, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_1237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_124F")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_154F")

    label("loc_124F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1290")
    SetChrPos(0x10, -14890, -300, 9170, 225)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0xF, -22760, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_1290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12C3")
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xE)
    SetChrChipByIndex(0xD, 0xC)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x13, 0xF)
    BeginChrThread(0x13, 0, 0, 4)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_12C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_12F2")
    SetChrPos(0xF, -23170, -3000, 5100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_154F")

    label("loc_12F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_133D")
    SetChrPos(0x10, -19280, -320, 18240, 90)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0xF, -22760, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x12, 0x80)
    Jump("loc_154F")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1383")
    SetChrPos(0x10, -14890, -300, 9170, 225)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0xF, -26620, -3000, 5100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_154F")

    label("loc_1383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13C3")
    SetChrPos(0xF, -23170, -3000, 5100, 270)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x8, -24410, -3000, 5240, 90)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_154F")

    label("loc_13C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1413")
    SetChrPos(0xF, -22760, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, -21950, -3000, 5010, 0)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_154F")

    label("loc_1413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1489")
    SetChrPos(0x10, -17150, -300, 16600, 315)
    BeginChrThread(0x10, 0, 0, 0)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1484")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1484")
    SetChrFlags(0x8, 0x10)

    label("loc_1484")

    Jump("loc_154F")

    label("loc_1489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_14FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_END)), "loc_14AA")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_14DC")

    label("loc_14AA")

    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xE)
    SetChrPos(0x10, -17150, -300, 16600, 315)
    BeginChrThread(0x10, 0, 0, 0)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    SetChrFlags(0x10, 0x10)

    label("loc_14DC")

    SetChrChipByIndex(0xD, 0xC)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x13, 0xF)
    BeginChrThread(0x13, 0, 0, 4)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_14FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_154F")
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x10, -17150, -300, 16600, 315)
    BeginChrThread(0x10, 0, 0, 0)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_154F")
    SetChrFlags(0x10, 0x10)

    label("loc_154F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1563")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)
    Jump("loc_162A")

    label("loc_1563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1577")
    ClearScenarioFlags(0x22, 1)
    Event(0, 19)
    Jump("loc_162A")

    label("loc_1577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_158B")
    ClearScenarioFlags(0x22, 2)
    Event(0, 20)
    Jump("loc_162A")

    label("loc_158B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_159F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 23)
    Jump("loc_162A")

    label("loc_159F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_15B3")
    ClearScenarioFlags(0x22, 4)
    Event(0, 24)
    Jump("loc_162A")

    label("loc_15B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_15C7")
    ClearScenarioFlags(0x22, 5)
    Event(0, 27)
    Jump("loc_162A")

    label("loc_15C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_15E0")
    ClearScenarioFlags(0x22, 6)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_162A")

    label("loc_15E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_15F4")
    ClearScenarioFlags(0x22, 7)
    Event(0, 42)
    Jump("loc_162A")

    label("loc_15F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_161B")
    ClearScenarioFlags(0x23, 0)
    OP_1B(0x2, 0x0, 0x2C)
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    Jump("loc_162A")

    label("loc_161B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_162A")
    ClearScenarioFlags(0x23, 1)
    Event(0, 16)

    label("loc_162A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1655")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_1655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_166D")
    Event(0, 22)

    label("loc_166D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_169A")
    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_169A")

    Return()

    # Function_8_F75 end

    def Function_9_169B(): pass

    label("Function_9_169B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1744")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xF, 0x64, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D8")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x5F, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_17D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_181F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_181F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1837")
    ClearMapFlags(0x2000)
    Jump("loc_183E")

    label("loc_1837")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_183E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_185A")
    SetMapObjFrame(0xFF, "turi00", 0x0, 0x1)
    Jump("loc_1868")

    label("loc_185A")

    SetMapObjFrame(0xFF, "turi01", 0x0, 0x1)

    label("loc_1868")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1881")
    ClearMapObjFlags(0x9, 0x4)
    Jump("loc_1887")

    label("loc_1881")

    SetMapObjFlags(0x9, 0x4)

    label("loc_1887")

    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0x1E)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18C8")
    OP_1B(0x8, 0x0, 0x2D)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x0)

    label("loc_18C8")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18FB")
    OP_66(0x6, 0x1)
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x0)

    label("loc_18FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1920")
    OP_1B(0x2, 0x0, 0x2C)

    label("loc_1920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_192E")
    OP_1B(0x2, 0x0, 0x2F)

    label("loc_192E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193D")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_193D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1950")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1963")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1976")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1989")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1989")

    OP_52(0x2B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3E")
    OP_70(0x6, 0x0)
    Jump("loc_1B42")

    label("loc_1B3E")

    OP_70(0x6, 0x1E)

    label("loc_1B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B55")
    OP_70(0x7, 0x0)
    Jump("loc_1B59")

    label("loc_1B55")

    OP_70(0x7, 0x1E)

    label("loc_1B59")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B7F")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    OP_66(0x2, 0x1)
    Jump("loc_1BAD")

    label("loc_1B7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BAD")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_1BAD")

    OP_65(0x3, 0x1)
    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BCB")
    OP_66(0x7, 0x1)

    label("loc_1BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BDC")
    OP_66(0x7, 0x1)

    label("loc_1BDC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BFB")
    OP_10(0x2, 0x0)
    OP_10(0xB, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0xC, 0x1)
    Jump("loc_1C07")

    label("loc_1BFB")

    OP_10(0x2, 0x1)
    OP_10(0xB, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0xC, 0x0)

    label("loc_1C07")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C32")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1C32")

    Return()

    # Function_9_169B end

    def Function_10_1C33(): pass

    label("Function_10_1C33")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D25")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('Ｕ材料', 1)"), scpexpr(EXPR_END)), "loc_1CB6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1D20")

    label("loc_1CB6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D20")

    Jump("loc_1D62")

    label("loc_1D25")

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

    label("loc_1D62")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1C33 end

    def Function_11_1D6E(): pass

    label("Function_11_1D6E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E60")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('封魔之刃', 1)"), scpexpr(EXPR_END)), "loc_1DF1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x98),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1E5B")

    label("loc_1DF1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x98),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x98),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E5B")

    Jump("loc_1E9D")

    label("loc_1E60")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_1E9D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1D6E end

    def Function_12_1EA9(): pass

    label("Function_12_1EA9")

    EventBegin(0x0)
    Fade(500)
    OP_68(-25670, -1400, 3480, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_E2(0x3)
    SetChrPos(0x101, -24530, -3000, 3820, 270)
    SetChrPos(0x102, -24620, -3000, 4610, 270)
    SetChrPos(0x103, -26670, -3000, 3480, 270)
    SetChrPos(0x104, -23080, -3000, 4470, 270)
    SetChrPos(0xF4, -23280, -3000, 3480, 270)
    SetChrPos(0xF5, -23030, -3000, 2550, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0007
    ChrTalk(
        0x103,
        "#11P#00205F……………………\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#00005F……缇欧？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#11P#00105F发现什么状况了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_68(-32299, -1400, 3240, 3000)
    OP_6F(0x79)

    #C0010
    ChrTalk(
        0x103,
        (
            "#11P#00200F在这个方向感觉到了\x01",
            "微弱的气息……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0011
    ChrTalk(
        0x103,
        (
            "#6P#00203F……抱歉，应该不是什么\x01",
            "值得在意的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00005F是吗……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0x1BF, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -24530, -3000, 3820, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_12_1EA9 end

    def Function_13_20A2(): pass

    label("Function_13_20A2")

    EventBegin(0x0)
    Fade(500)
    OP_68(-16840, -3900, -5030, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_E2(0x3)
    SetChrPos(0x101, -15840, -5500, -6030, 315)
    SetChrPos(0x102, -15430, -5500, -4830, 270)
    SetChrPos(0x103, -16840, -5500, -5030, 315)
    SetChrPos(0x104, -14440, -5500, -5410, 270)
    SetChrPos(0xF4, -14440, -5500, -6610, 315)
    SetChrPos(0xF5, -14850, -5500, -7820, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0013
    ChrTalk(
        0x103,
        "#11P#00205F……………………\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00005F……缇欧？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#00105F发现什么状况了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_68(-30570, -3900, 4350, 5000)
    OP_6F(0x79)
    Sleep(2000)
    Fade(500)
    OP_68(-16840, -3900, -5030, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()

    #C0016
    ChrTalk(
        0x103,
        (
            "#11P#00200F在这个方向感觉到了\x01",
            "微弱的气息……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0017
    ChrTalk(
        0x103,
        (
            "#6P#00203F……抱歉，应该不是什么\x01",
            "值得在意的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00005F是吗……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0x1BF, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -15840, -5500, -6030, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_13_20A2 end

    def Function_14_22CE(): pass

    label("Function_14_22CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22DB")
    Call(0, 15)
    Return()

    label("loc_22DB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-33380, -3950, 5900, 0)
    MoveCamera(25, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15420, 0)
    SetChrPos(0x101, -33000, -5500, 6670, 0)
    SetChrPos(0x102, -32000, -5500, 5870, 0)
    SetChrPos(0x103, -34000, -5500, 5660, 0)
    SetChrPos(0x104, -33000, -5500, 5160, 0)
    SetChrPos(0xF4, -34400, -5500, 4450, 0)
    SetChrPos(0xF5, -31790, -5500, 4570, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2766")
    SetScenarioFlags(0x2, 2)
    SetChrName("")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从倚立在墙边的木板缝隙中\x01",
            "看到了一片黑暗。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x101,
        (
            "#12P#00005F这……\x01",
            "似乎可以通到什么地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#12P#00105F莫非是通向地下空间吗？\x02\x03",

            "#00103F看起来，板子是\x01",
            "可以挪动的……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#12P#00305F莫非阿缇刚才\x01",
            "感觉到的反应就是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        "#6P#00200F嗯，我想就是这里。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_250E")

    #C0024
    ChrTalk(
        0x10A,
        "#12P#00603F唔……有点令人在意啊。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2581")

    label("loc_250E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2547")

    #C0025
    ChrTalk(
        0x109,
        "#12P#10105F……有人在里面吗？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2581")

    label("loc_2547")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2581")

    #C0026
    ChrTalk(
        0x105,
        "#12P#10405F……莫非有人不慎误入吗？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2581")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25B6")

    #C0027
    ChrTalk(
        0x106,
        "#12P#10701F要进去确认吗？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2625")

    label("loc_25B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25EF")

    #C0028
    ChrTalk(
        0x105,
        "#12P#10400F要进去确认一下吗？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2625")

    label("loc_25EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2625")

    #C0029
    ChrTalk(
        0x109,
        "#12P#10101F要不要进去确认一下？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2625")

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
            "【进去查看】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2712")

    #C0030
    ChrTalk(
        0x101,
        (
            "#12P#00001F这个嘛……\x01",
            "谨慎起见，我们就进去确认一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        "#6P#00200F那我们就赶快进去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("m0304", 0, 0, 0)
    IdleLoop()
    Jump("loc_2761")

    label("loc_2712")


    #C0032
    ChrTalk(
        0x101,
        (
            "#12P#00003F……算了，现在\x01",
            "没时间到处乱走。\x02\x03",

            "#00000F这个地方就先不要管了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2761")

    Jump("loc_28F9")

    label("loc_2766")

    SetChrName("")

    #A0033
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从倚立在墙边的木板缝隙中\x01",
            "看到了一片黑暗。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
            "【进去查看】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28AA")

    #C0034
    ChrTalk(
        0x101,
        (
            "#12P#00003F谨慎起见……\x01",
            "还是进去确认一下好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        "#12P#00101F是啊，总觉得有些在意。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        "#6P#00200F那我们就赶快进去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("m0304", 0, 0, 0)
    IdleLoop()
    Jump("loc_28F9")

    label("loc_28AA")


    #C0037
    ChrTalk(
        0x101,
        (
            "#12P#00003F……算了，现在\x01",
            "没时间到处乱走。\x02\x03",

            "#00000F这个地方就先不要管了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F9")

    Jump("loc_29FB")

    label("loc_28FE")

    SetChrName("")

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从倚立在墙边的木板缝隙中\x01",
            "看到了一片黑暗。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0039
    ChrTalk(
        0x101,
        (
            "#12P#00003F（雷因兹先生……\x01",
            "  竟然是调查公司\x01",
            "  的成员啊。）\x02",
        )
    )

    CloseMessageWindow()
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
            "【进入雷因兹潜伏的场所】\x01",      # 0
            "【放弃】\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29FB")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("m0304", 100, 0, 0)
    IdleLoop()
    Jump("loc_29FB")

    label("loc_29FB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -33410, -5500, 5850, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_14_22CE end

    def Function_15_2A32(): pass

    label("Function_15_2A32")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB1")
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "墙边竖立着木板，\x01",
            "固定得非常牢固。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00005F自那次之后，雷因兹先生\x01",
            "就把这里彻底堵住了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_2AE1")

    label("loc_2AB1")

    SetChrName("")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "墙边竖立着木板，\x01",
            "固定得非常牢固。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2AE1")

    TalkEnd(0xFF)
    Return()

    # Function_15_2A32 end

    def Function_16_2AE5(): pass

    label("Function_16_2AE5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-33310, -3750, 5030, 0)
    MoveCamera(57, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14690, 0)
    SetChrPos(0x101, -33000, -5500, 6670, 180)
    SetChrPos(0x102, -31600, -5500, 6070, 225)
    SetChrPos(0x103, -31790, -5500, 5070, 270)
    SetChrPos(0x104, -33000, -5500, 3860, 0)
    SetChrPos(0xF4, -34400, -5500, 4450, 45)
    SetChrPos(0xF5, -34400, -5500, 5660, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0043
    ChrTalk(
        0x103,
        (
            "#00203F话说回来，\x01",
            "Ｒ＆Ａ调查所…\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#12P#00301F嗯，似乎是个\x01",
            "相当优秀的组织呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#5P#00100F嗯，再怎么说，\x01",
            "毕竟是理查德前上校创办的公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00003F算了，我们也没有\x01",
            "进一步猜测的必要。\x02\x03",

            "#00001F现在还是专心做好\x01",
            "突入兰花塔的准备工作吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -33410, -5500, 5850, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1BF, 3)
    OP_2C(0xB1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_16_2AE5 end

    def Function_17_2CD7(): pass

    label("Function_17_2CD7")

    Return()

    # Function_17_2CD7 end

    def Function_18_2CD8(): pass

    label("Function_18_2CD8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1600, -900, -42250, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x101, 1600, -3000, -47000, 0)
    SetChrPos(0x102, 2500, -3000, -47900, 0)
    SetChrPos(0x109, 700, -3000, -48500, 0)
    SetChrPos(0x105, 1600, -3000, -40500, 0)

    def lambda_2D5B():
        OP_96(0xFE, 0x640, 0xFFFFF448, 0xFFFF88DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2D5B)
    Sleep(50)

    def lambda_2D78():
        OP_96(0xFE, 0x640, 0xFFFFF448, 0xFFFF7B30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D78)
    Sleep(50)

    def lambda_2D95():
        OP_96(0xFE, 0x9C4, 0xFFFFF448, 0xFFFF77AC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D95)
    Sleep(50)

    def lambda_2DB2():
        OP_96(0xFE, 0x2BC, 0xFFFFF448, 0xFFFF7554, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2DB2)
    OP_68(1600, -1900, -32250, 7000)
    MoveCamera(40, 15, 0, 7000)
    SetCameraDistance(15000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x105, 1)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x101, 1)

    #C0047
    ChrTalk(
        0x101,
        "#12P#00008F#30W瓦吉……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)

    #C0048
    ChrTalk(
        0x109,
        "#12P#10106F#30W瓦吉，你……\x02",
    )

    CloseMessageWindow()
    OP_64(0x105)
    Sleep(500)
    OP_93(0x105, 0xB4, 0x190)
    Sleep(150)

    #C0049
    ChrTalk(
        0x105,
        (
            "#5P#10304F#30W……哈哈，\x01",
            "让你们看到了丢人的场面呢。\x02\x03",

            "#10302F似乎稍微有些冲动，\x01",
            "不太符合我的作风吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#12P#00006F不……\x02\x03",

            "#00000F……该怎么说呢，\x01",
            "男人就应该那样吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        (
            "#00103F我虽然不太懂得\x01",
            "男生的心情……\x02\x03",

            "#00100F但我至少明白，你是怀着\x01",
            "诚意来面对他的。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x109,
        (
            "#12P#10112F嗯嗯……！\x02\x03",

            "#10100F我想他总有一天\x01",
            "会明白这一点的！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3023")

    #C0053
    ChrTalk(
        0x105,
        (
            "#5P#10304F#30W呵呵……\x01",
            "但愿如此吧。\x02\x03",

            "#10300F耽误了不少时间，\x01",
            "赶快去其它地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3082")

    label("loc_3023")


    #C0054
    ChrTalk(
        0x105,
        (
            "#5P#10304F#30W呵呵……\x01",
            "但愿如此吧。\x02\x03",

            "#10300F耽误了不少时间，\x01",
            "赶快去完成剩下的支援请求吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3082")

    SetCameraDistance(15500, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x0, 1530, -3000, -23230, 0)
    SetScenarioFlags(0x128, 6)
    SetScenarioFlags(0x2, 6)
    OP_1B(0x2, 0x0, 0x2F)
    OP_32(0xFF, 0xFE, 0x0)
    OP_C9(0x1, 0x1000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_2CD8 end

    def Function_19_30C5(): pass

    label("Function_19_30C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10500, 2000, -1000, 0)
    MoveCamera(65, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 27600, -300, -2700, 0)
    SetChrPos(0x1, 27600, -300, -2700, 0)
    SetChrPos(0x2, 27600, -300, -2700, 0)
    SetChrPos(0x3, 27600, -300, -2700, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xF7, 0xCD, 0xB7, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0xE, 0x8000)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xE, -4200, -300, -500, 315)
    SetChrFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0xD, -5200, -300, 500, 135)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -13300, -300, 12700, 135)

    def lambda_31FD():
        OP_98(0xFE, 0x2AF8, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_31FD)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -14300, -300, 11700, 135)

    def lambda_322D():
        OP_98(0xFE, 0x2AF8, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_322D)
    OP_68(-10500, 1000, -1000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-7500, 2100, 14100, 0)
    MoveCamera(75, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(17500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x22, 0)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_30C5 end

    def Function_20_32B8(): pass

    label("Function_20_32B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30000.itc", 0x1E)
    SoundLoad(835)
    SoundLoad(821)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xD, 0, 0, 0)
    BeginChrThread(0xE, 0, 0, 0)
    BeginChrThread(0x10, 0, 0, 0)
    BeginChrThread(0x13, 0, 0, 0)
    SetChrChipByIndex(0x26, 0x1E)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    BeginChrThread(0x26, 0, 0, 0)
    SetChrChipByIndex(0x27, 0x1E)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    BeginChrThread(0x27, 0, 0, 0)
    SetChrChipByIndex(0x28, 0x1E)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    BeginChrThread(0x28, 0, 0, 0)
    SetChrChipByIndex(0x29, 0x1E)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    BeginChrThread(0x29, 0, 0, 0)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x26, -23200, -340, 16500, 180)
    SetChrPos(0x27, -18350, -300, 16500, 180)
    SetChrPos(0x28, -18150, -300, 11450, 0)
    SetChrPos(0x29, 1900, -300, -2300, 0)
    SetChrPos(0xF, -19750, -300, 18450, 180)
    SetChrPos(0x10, -18650, -300, 18900, 180)
    SetChrPos(0xE, -20200, -300, 19900, 180)
    SetChrPos(0xD, -22800, -300, 18500, 180)
    SetChrPos(0x13, -21300, -300, 20900, 180)
    SetChrPos(0x11, -18200, -300, 21250, 180)
    SetChrPos(0x8, -18600, -600, 9150, 0)
    SetChrPos(0x9, -17550, -830, 8850, 0)
    SetChrPos(0xA, 1250, -580, -4500, 0)
    SetChrPos(0xB, 2600, -310, -4150, 0)
    SetChrPos(0x12, 2150, -1030, -5050, 0)
    BeginChrThread(0xF, 3, 0, 21)
    BeginChrThread(0xE, 3, 0, 21)
    BeginChrThread(0xD, 3, 0, 21)
    BeginChrThread(0x11, 3, 0, 21)
    BeginChrThread(0x8, 3, 0, 21)
    BeginChrThread(0x9, 3, 0, 21)
    BeginChrThread(0xA, 3, 0, 21)
    BeginChrThread(0xB, 3, 0, 21)
    BeginChrThread(0x12, 3, 0, 21)
    OP_68(-24900, 1000, 12950, 0)
    MoveCamera(55, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(-19900, 1000, 12950, 5000)
    MoveCamera(50, 30, 0, 5000)
    SetCameraDistance(15000, 5000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x11, 3160, -950, -4950, 0)
    SetChrPos(0xE, 2160, -1250, -5340, 0)
    SetChrPos(0xD, 550, -350, -4150, 0)
    OP_68(-850, 1000, -7900, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    OP_68(11450, 1750, -350, 5000)
    MoveCamera(60, 20, 0, 5000)
    SetCameraDistance(15000, 5000)
    Sleep(4000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_32B8 end

    def Function_21_361F(): pass

    label("Function_21_361F")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3657"),
        (1, "loc_365F"),
        (2, "loc_3667"),
        (3, "loc_366F"),
        (4, "loc_3677"),
        (5, "loc_367F"),
        (6, "loc_3687"),
        (SWITCH_DEFAULT, "loc_368F"),
    )


    label("loc_3657")

    Sleep(100)
    Jump("loc_3697")

    label("loc_365F")

    Sleep(200)
    Jump("loc_3697")

    label("loc_3667")

    Sleep(300)
    Jump("loc_3697")

    label("loc_366F")

    Sleep(400)
    Jump("loc_3697")

    label("loc_3677")

    Sleep(500)
    Jump("loc_3697")

    label("loc_367F")

    Sleep(600)
    Jump("loc_3697")

    label("loc_3687")

    Sleep(700)
    Jump("loc_3697")

    label("loc_368F")

    Sleep(800)
    Jump("loc_3697")

    label("loc_3697")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36C2")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_3697")

    label("loc_36C2")

    Return()

    # Function_21_361F end

    def Function_22_36C3(): pass

    label("Function_22_36C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-19500, 1020, 24400, 0)
    MoveCamera(39, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -20800, -320, 24400, 90)
    SetChrPos(0x102, -20000, -320, 23100, 45)
    SetChrPos(0x104, -18400, -320, 25100, 270)
    SetChrPos(0x109, -20000, -320, 25700, 135)
    SetChrPos(0x105, -18400, -320, 23700, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    MoveCamera(49, 25, 0, 3000)
    SetCameraDistance(16500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0055
    ChrTalk(
        0x101,
        (
            "#6P#00012F呼……\x01",
            "真是好累啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#12P#00102F是啊……\x01",
            "不过总算是顺利\x01",
            "找到了玛丽。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#00306F……抱歉啊，\x01",
            "我那顽劣的妹妹给大家添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x109,
        (
            "#5P#10112F哈哈……\x01",
            "这并不是前辈的错嘛。\x02\x03",

            "#10100F而且她是个\x01",
            "很好的孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#12P#00100F是啊，不管怎么说，\x01",
            "她确实努力帮助了我们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#00302F哈哈……\x01",
            "她确实没有什么恶意。\x02\x03",

            "#00306F但这正是她最危险的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#6P#00008F原来如此……\x01",
            "听起来好像很复杂呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        (
            "#11P#10304F呵呵，忍耐女孩子\x01",
            "那反复无常的性格，\x01",
            "也正是男人的义务嘛。\x02\x03",

            "#10300F那么，接下来该做什么？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A07")

    #C0063
    ChrTalk(
        0x101,
        (
            "#6P#00004F这个嘛……\x01",
            "支援请求已经全部完成了。\x02\x03",

            "#00000F我们可以先回支援科，\x01",
            "稍微休息一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A6E")

    label("loc_3A07")


    #C0064
    ChrTalk(
        0x101,
        (
            "#6P#00003F这个嘛……\x01",
            "支援请求还没有全部完成呢。\x02\x03",

            "#00000F不过我们也可以先回支援科，\x01",
            "稍微休息一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A6E")


    #C0065
    ChrTalk(
        0x102,
        (
            "#12P#00104F嗯，是啊……\x01",
            "那就这么办吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#00300F好，那我们就回\x01",
            "支援科喘口气吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -18400, -310, 24400, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x140, 5)
    OP_29(0xA3, 0x1, 0xF)
    EventEnd(0x5)
    Return()

    # Function_22_36C3 end

    def Function_23_3AFC(): pass

    label("Function_23_3AFC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    SoundLoad(821)
    SoundLoad(835)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x8, 0x16)
    OP_49()
    SetChrPos(0x16, -18400, -300, 16800, 225)
    OP_D5(0x16, 0x0, 0x4CE78, 0x0, 0x0)
    SetMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x2)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -20800, -320, 16200, 225)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -17500, -310, 12900, 225)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x1F, 0x2)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -22000, -300, 12900, 90)
    SetChrChipByIndex(0x20, 0x3)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -22650, -300, 13500, 90)
    SetChrChipByIndex(0x21, 0x4)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -20200, -300, 12100, 45)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -21700, -300, 11300, 45)
    SetChrChipByIndex(0x23, 0x6)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -19200, -300, 11300, 45)
    SetChrChipByIndex(0x24, 0x8)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -22500, -300, 15200, 90)
    SetChrChipByIndex(0x25, 0xB)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -24100, -300, 12850, 90)
    OP_63(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-20000, 3300, 13800, 0)
    MoveCamera(33, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_68(-20000, 1300, 13800, 10000)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMessageWindowPos(120, 90, -1, -1)
    SetChrName("迪塔总统")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "正如各位所想，\x01",
            "邪恶的意志当然不止一个。\x02\x03",

            "『卡尔瓦德共和国政府』……\x02\x03",

            "他们与狡猾的犯罪组织狼狈为奸，\x01",
            "是将克洛斯贝尔的和平与尊严\x01",
            "践踏在脚下的第二元凶。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x22, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(851, 1500, 60)
    StopSound(835, 1500, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_3AFC end

    def Function_24_3E47(): pass

    label("Function_24_3E47")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(13890, -1330, -14740, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(13890, -1330, -14740, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 16400, -2500, -15030, 270)
    SetChrPos(0x102, 18400, -2500, -15030, 270)
    SetChrPos(0x109, 20400, -2500, -15030, 270)
    SetChrPos(0x105, 22400, -2500, -15030, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    OP_68(1120, -1400, -15440, 3000)
    MoveCamera(45, 13, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(12000, 3000)
    OP_0D()

    def lambda_3FB1():
        OP_95(0x101, 1000, -3000, -14740, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FB1)

    def lambda_3FCB():
        OP_95(0x102, 2600, -3000, -13540, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FCB)

    def lambda_3FE5():
        OP_95(0x109, 2000, -3000, -15940, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3FE5)

    def lambda_3FFF():
        OP_95(0x105, 3600, -2930, -14740, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3FFF)

    def lambda_4019():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4019)
    Sleep(300)

    def lambda_402D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_402D)
    Sleep(300)

    def lambda_4041():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4041)
    Sleep(300)

    def lambda_4055():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4055)
    Sleep(1500)
    SetMapObjFlags(0x4, 0x0)
    WaitChrThread(0x101, 1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0x102, 1)

    def lambda_40A3():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40A3)
    Sleep(300)

    def lambda_40B3():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40B3)
    Sleep(300)

    def lambda_40C3():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_40C3)
    Sleep(300)

    def lambda_40D3():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_40D3)
    Sleep(300)

    def lambda_40E3():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40E3)
    Sleep(300)

    def lambda_40F3():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40F3)
    Sleep(300)

    def lambda_4103():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4103)
    Sleep(300)

    def lambda_4113():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4113)
    Sleep(300)
    OP_0D()

    def lambda_4124():
        OP_93(0x101, 0x5A, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4124)

    def lambda_4131():
        OP_93(0x102, 0xB4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4131)

    def lambda_413E():
        OP_93(0x109, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_413E)

    def lambda_414B():
        OP_93(0x105, 0x10E, 0x5DC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_414B)
    OP_0D()
    WaitChrThread(0x101, 1)

    #C0068
    ChrTalk(
        0x101,
        "#6P#00001F糟糕……找不到了。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x109,
        (
            "#12P#10106F真、真是个不得了的人啊。\x02\x03",

            "#10101F简直就像是早就料到我们会来，\x01",
            "故意设计了那种陷阱……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#00103F那种程度的手段，\x01",
            "对他来说实在是不值一提……\x02\x03",

            "#00101F真不愧是\x01",
            "情报机关的大尉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，但他的做事方式\x01",
            "完全不像个军人呢。\x02\x03",

            "#10302F接下来要怎么办，就此放弃吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#6P#00003F不……\x01",
            "我们继续追吧。\x02\x03",

            "#00000F问问街上的行人，\x01",
            "说不定可以掌握到他的行踪。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#00100F知道了。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x109,
        "#12P#10100F我们出发吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x4, 0x10)
    SetScenarioFlags(0x130, 3)
    OP_29(0x66, 0x1, 0x3)
    SetChrPos(0x0, 1000, -3000, -14740, 225)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_3E47 end

    def Function_25_4351(): pass

    label("Function_25_4351")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(975)
    OP_68(-23060, 4740, 24030, 0)
    MoveCamera(63, 44, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17480, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetMapObjFlags(0xB, 0x1000)
    ClearMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0x17)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x17, -20760, -310, 40300, 180)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_D5(0x17, 0x0, 0x2BF20, 0x0, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    OP_78(0xA, 0x18)
    OP_49()
    SetChrPos(0x18, -13070, -300, 11900, 315)
    OP_D5(0x18, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    Sound(486, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(-25830, 4740, 8470, 1500)
    MoveCamera(42, 17, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(14250, 1500)

    def lambda_44B4():
        OP_9B(0x1, 0xFE, 0x0, 0x61A8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_44B4)

    def lambda_44C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_44C9)
    OP_71(0xB, 0xB5, 0xF0, 0x0, 0x20)
    Sleep(1000)
    Sound(492, 0, 100, 0)
    StopSound(486, 300, 100)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x17, 1)
    OP_0D()

    #N0075
    NpcTalk(
        0x17,
        "塞克斯",
        "哈哈，有埋伏啊！\x02",
    )

    CloseMessageWindow()

    #N0076
    NpcTalk(
        0x17,
        "尤利",
        "哼，真是白痴。\x02",
    )

    CloseMessageWindow()

    #N0077
    NpcTalk(
        0x17,
        "尤利",
        "瑞吉，能甩开吗？\x02",
    )

    CloseMessageWindow()

    #N0078
    NpcTalk(
        0x17,
        "瑞吉",
        (
            "当然了，\x01",
            "那种家伙怎么可能是我的对手！\x02",
        )
    )

    CloseMessageWindow()
    Sound(493, 0, 100, 0)
    OP_9B(0x1, 0x17, 0x0, 0xFFFFF830, 0x1388, 0x0)
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x20)
    Sleep(200)
    OP_71(0xB, 0xB5, 0xF0, 0x0, 0x20)
    OP_9F(0x0, 0x17)
    OP_9F(0x1, -22600, -330, 15200)
    OP_9F(0x1, -28560, -330, 14320)
    OP_9F(0x2, 0x17, 11000, 0x6)

    def lambda_4601():
        OP_9B(0x1, 0x17, 0x0, 0x2710, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4601)
    Sleep(50)
    Sound(494, 0, 100, 0)
    Sound(975, 2, 100, 0)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    OP_96(0x18, 0xFFFFC6A8, 0xFFFFFED4, 0x35DE, 0x1388, 0x0)
    WaitChrThread(0x18, 1)
    OP_9F(0x0, 0x18)
    OP_9F(0x1, -15680, -300, 13790)
    OP_9F(0x1, -18990, -300, 13910)
    OP_9F(0x2, 0x18, 11000, 0x6)
    OP_9B(0x1, 0x18, 0x0, 0x3A98, 0x3A98, 0x0)
    StopSound(975, 300, 100)
    SetScenarioFlags(0x24, 2)
    NewScene("c0100", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_25_4351 end

    def Function_26_468F(): pass

    label("Function_26_468F")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch24200.itc", 0x1F)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrPos(0x1A, 1200, 0, 7800, 225)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrPos(0x1B, 1200, 0, 7800, 225)
    OP_68(-790, 690, 5800, 0)
    MoveCamera(44, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16700, 0)
    SetChrPos(0x101, -1400, -300, 4400, 45)
    SetChrPos(0x102, -2150, -300, 5100, 45)
    SetChrPos(0x109, -1700, -300, 3200, 45)
    SetChrPos(0x105, -3400, -300, 4800, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 5)), scpexpr(EXPR_END)), "loc_4898")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0079
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～正在准备中～　　\x01",
            "　　　——钓皇俱乐部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0080
    ChrTalk(
        0x101,
        "#12P#00003F唔～和上次来的时候一样啊……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        (
            "#6P#00105F罗伊德，\x01",
            "你没有什么头绪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#12P#00001F嗯，老实说，\x01",
            "我完全不清楚\x01",
            "发生了什么呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0083
    ChrTalk(
        0x101,
        (
            "#12P#00005F哎……看样子，\x01",
            "门好像没有锁啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4979")

    label("loc_4898")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～正在准备中～　　\x01",
            "　　　——钓皇俱乐部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0085
    ChrTalk(
        0x101,
        (
            "#12P#00003F准备中吗……\x01",
            "不过……钓皇俱乐部？这究竟是……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0086
    ChrTalk(
        0x101,
        (
            "#12P#00005F哎……看样子，\x01",
            "门好像没有锁啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4979")


    #N0087
    NpcTalk(
        0x1A,
        "青年的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P你、你……\x01",
            "你也能算是垂钓爱好者的说！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0088
    NpcTalk(
        0x1B,
        "男人的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P就、就是啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0089
    NpcTalk(
        0x1B,
        "男人的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P我绝对不能接受\x01",
            "这种强硬的做法！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0090
    ChrTalk(
        0x102,
        "#6P#00105F罗伊德，刚才那是……？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#12P#00001F嗯，是我们熟悉的声音，\x01",
            "进去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetScenarioFlags(0x22, 0)
    NewScene("c1020", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_468F end

    def Function_27_4ADF(): pass

    label("Function_27_4ADF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch24200.itc", 0x1F)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -2600, -300, 4800, 225)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -1800, -300, 4000, 225)
    SetChrFlags(0xD, 0x80)
    EndChrThread(0xD, 0x0)
    OP_68(-1990, 90, 4670, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15630, 0)
    SetChrPos(0x101, -3300, 0, 2500, 45)
    SetChrPos(0x102, -4100, 0, 3300, 45)
    SetChrPos(0x109, -3300, 0, 1400, 45)
    SetChrPos(0x105, -5200, 0, 3300, 45)
    FadeToBright(1000, 0)
    OP_0D()

    #C0092
    ChrTalk(
        0x1A,
        (
            "#5P为什么会发生这种事……\x01",
            "我绝对不能接受的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x1B,
        (
            "#11P嗯，分部居然会\x01",
            "被人夺走。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x1B,
        (
            "#11P总之，再去和\x01",
            "赛尔丹分部长谈谈吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#12P#00006F那个……彼德先生，\x01",
            "我还完全不清楚到底\x01",
            "发生了什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x1B,
        (
            "#11P嗯，因为你之前\x01",
            "休息了一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x1B,
        (
            "#11P总之，全体集合之后\x01",
            "再仔细说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x1B,
        (
            "#11P我这就和分部长说一声，\x01",
            "到后巷的爵士酒吧\x01",
            "『加兰特』见面。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x1B,
        "#11P罗伊德，请你也过来吧。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x1A,
        (
            "#5P那我们就\x01",
            "先走一步的说。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D62():
        OP_9B(0x0, 0x1A, 0x5A, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4D62)
    Sleep(50)

    def lambda_4D7A():
        OP_93(0x101, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D7A)
    Sleep(50)

    def lambda_4D8A():
        OP_93(0x102, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D8A)
    Sleep(50)
    WaitChrThread(0x1B, 1)

    def lambda_4D9E():
        OP_9B(0x0, 0x1B, 0x5A, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4D9E)
    Sleep(50)

    def lambda_4DB6():
        OP_93(0x109, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4DB6)
    Sleep(50)

    def lambda_4DC6():
        OP_93(0x105, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4DC6)
    Sleep(50)
    WaitChrThread(0x1B, 1)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)

    #C0101
    ChrTalk(
        0x102,
        "#5P#00105F究竟发生什么事了？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#11P#00003F不清楚，\x01",
            "总之，必须要过去确认一下。\x02\x03",

            "#00000F我们也到那家爵士酒吧去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_65(0x2, 0x1)
    SetMapObjFlags(0x0, 0x10)
    OP_D7(0x1E)
    OP_D7(0x1F)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 26200, -300, -1050, 270)
    BeginChrThread(0xD, 1, 0, 1)
    SetScenarioFlags(0x132, 0)
    OP_29(0x6A, 0x1, 0x3)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -4200, 0, 2400, 225)
    EventEnd(0x5)
    Return()

    # Function_27_4ADF end

    def Function_28_4EAF(): pass

    label("Function_28_4EAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(4570, 40, -12620, 0)
    MoveCamera(44, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(33000, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_4F4C")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_4F8B")

    label("loc_4F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_4F6E")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_4F8B")

    label("loc_4F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_4F8B")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_4F8B")

    OP_68(4570, 40, -12620, 5000)
    MoveCamera(44, 13, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(37220, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(-23840, 1240, 8210, 7000)
    MoveCamera(33, 13, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(37220, 7000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-20080, 1440, 21740, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16560, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_50FF")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x104, -20350, -310, 27200, 180)

    def lambda_5091():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_5091)

    def lambda_50AB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50AB)
    Sleep(100)

    def lambda_50C8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50C8)
    Sleep(50)

    def lambda_50E5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50E5)
    Jump("loc_52A2")

    label("loc_50FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_51D3")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x109, -20350, -310, 27200, 180)

    def lambda_5165():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_5165)

    def lambda_517F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_517F)
    Sleep(100)

    def lambda_519C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_519C)
    Sleep(50)

    def lambda_51B9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_51B9)
    Jump("loc_52A2")

    label("loc_51D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_52A2")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x105, -20350, -310, 27200, 180)

    def lambda_5239():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_5239)

    def lambda_5253():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5253)
    Sleep(100)

    def lambda_5270():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5270)
    Sleep(50)

    def lambda_528D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_528D)

    label("loc_52A2")

    SetCameraDistance(14560, 3000)
    OP_6F(0x79)

    #C0103
    ChrTalk(
        0x1A2,
        "这里就是东街啊……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x1A2,
        (
            "来到自治州之后，\x01",
            "我还是第一次如此悠闲地眺望街景呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0105
    ChrTalk(
        0x102,
        (
            "#6P#00100F呵呵，因为这里与故乡很相似，\x01",
            "所以能使你心情放松吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0106
    ChrTalk(
        0x1A2,
        "#11P嗯，或许正是如此。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x1A2,
        (
            "#11P呵呵，但话说回来，\x01",
            "真正的东方人街，\x01",
            "生机活力可是远不止如此的。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x1A2,
        (
            "#11P如果有机会，\x01",
            "下次换我带大姐姐\x01",
            "游览共和国。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x1A2,
        "#11P这么一说，还真是好想带大姐姐一起回国！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_54D5")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0110
    ChrTalk(
        0x102,
        "#6P#00112F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#00006F交际手腕还真是厉害啊。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#00300F嗯，措词\x01",
            "也不差呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5661")

    label("loc_54D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_55A4")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0113
    ChrTalk(
        0x102,
        "#00112F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#00006F交际手腕还真是厉害啊。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x109,
        (
            "#10109F啊哈哈，从某种意义上说，\x01",
            "还真是有点羡慕他啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5661")

    label("loc_55A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_5661")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0x102,
        "#00112F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        "#00006F交际手腕还真是厉害啊。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x105,
        "#10300F呵呵，直来直去的态度倒也不错啊。\x02",
    )

    CloseMessageWindow()

    label("loc_5661")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    OP_1B(0x8, 0x0, 0x2D)
    SetScenarioFlags(0x153, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -19750, -310, 26000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_4EAF end

    def Function_29_56D7(): pass

    label("Function_29_56D7")

    EventBegin(0x0)
    Fade(500)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04600.itp")
    SoundLoad(3949)
    OP_68(-5300, -1400, -11050, 0)
    MoveCamera(44, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13490, 0)
    SetChrPos(0x101, -5200, -3000, -10840, 0)
    SetChrPos(0x102, -3970, -3000, -10800, 0)
    SetChrPos(0x109, -6270, -3000, -10440, 45)
    SetChrPos(0x104, -2970, -3000, -11500, 315)
    SetChrPos(0x105, -3950, -3000, -12150, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_0D()

    #C0119
    ChrTalk(
        0xB,
        "哦？有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，稍微有点事情\x01",
            "想问问您。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将事情经过做了说明，\x01",
            "询问对方是否见到过小猫玛丽。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0122
    ChrTalk(
        0xB,
        (
            "哦，是本德先生家的小猫啊。\x01",
            "有警察帮忙找，就让人放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "但很不巧，\x01",
            "我今天并没见过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xB,
        (
            "我特意准备了\x01",
            "它喜欢吃的鱼干，\x01",
            "但一直原封不动地留在那里……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xB,
        (
            "至少可以确定，从昨晚开始，\x01",
            "它就没有来过这边。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#12P#00103F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "那家人一直都很\x01",
            "照顾我的生意，\x01",
            "我也很想帮帮他们……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        "请各位一定尽力找到它啊。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#12P#00000F嗯，当然。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        "#12P#00100F多谢您的协助。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 32)
    Sleep(100)
    BeginChrThread(0x105, 3, 0, 34)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 31)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 30)
    Sleep(100)
    BeginChrThread(0x109, 3, 0, 33)
    OP_68(2580, -1400, -13440, 5000)
    MoveCamera(32, 28, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(15530, 5000)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)

    #C0131
    ChrTalk(
        0x104,
        "#00303F刚一开始就白跑了一趟啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0132
    ChrTalk(
        0x109,
        (
            "#12P#10105F罗伊德警官，\x01",
            "接下来该怎么办？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0133
    ChrTalk(
        0x101,
        (
            "#00000F嗯，先在这一带\x01",
            "询问一番……\x02\x03",

            "#00003F接下来的搜索范围将会比较广阔，\x01",
            "大概也只能借助蔡特的鼻子了。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        (
            "#11P#00105F这个主意不错，可是……\x02\x03",

            "#00106F……缇欧现在不在，\x01",
            "不知道能不能顺利与蔡特沟通啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#00006F是啊……\x02\x03",

            "#00000F不过，我们可以\x01",
            "用手势来比划……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 2270, -220, -3590, 180)
    OP_C9(0x0, 0x80000000)

    #N0136
    NpcTalk(
        0x1C,
        "少女的声音",
        "#3949V哎？你们在做什么？\x02",
    )

    CloseMessageWindow()
    OP_24(0xF6D)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-1420, 800, -15420, 3000)
    MoveCamera(35, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13050, 3000)

    def lambda_5C64():

        label("loc_5C64")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5C64")

    QueueWorkItem2(0x101, 1, lambda_5C64)

    def lambda_5C76():

        label("loc_5C76")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5C76")

    QueueWorkItem2(0x104, 1, lambda_5C76)

    def lambda_5C88():

        label("loc_5C88")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5C88")

    QueueWorkItem2(0x102, 1, lambda_5C88)

    def lambda_5C9A():

        label("loc_5C9A")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5C9A")

    QueueWorkItem2(0x109, 1, lambda_5C9A)

    def lambda_5CAC():

        label("loc_5CAC")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5CAC")

    QueueWorkItem2(0x105, 1, lambda_5CAC)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0137
    ChrTalk(
        0x101,
        "#12P#00011F什么……！\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#00105F是兰迪的……\x02",
    )

    CloseMessageWindow()
    OP_68(870, -1400, -12100, 4000)
    MoveCamera(53, 30, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(14790, 4000)
    OP_95(0x1C, 1340, -3000, -9310, 2000, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    WaitChrThread(0x1C, 1)
    OP_6F(0x79)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0139
    AnonymousTalk(
        0x1C,
        (
            "兰迪哥……\x01",
            "还有几位哥哥姐姐。\x02\x03",

            "你们在这里做什么呢？\x02",
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
        0x104,
        (
            "#00303F……做什么也都和你无关，\x01",
            "赶快从我眼前消失。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x104, 500)
    Sleep(300)

    #C0141
    ChrTalk(
        0x1C,
        (
            "#04606F唔，好无情啊。\x02\x03",

            "#04600F既然如此，我就去问问\x01",
            "那位姐姐的身体吧。\x02\x03",

            "#04609F真想再次尽情地揉一揉⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        "#00112F等、等一下……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_9B(0x1, 0x102, 0xB4, 0x1F4, 0x5DC, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x102)

    #C0143
    ChrTalk(
        0x101,
        (
            "#12P#00003F……如你所见，\x01",
            "特别任务支援科正在工作。\x02\x03",

            "#00001F工作内容与你们毫无关系，\x01",
            "能否不要纠缠我们呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0xB4, 0x1F4)
    Sleep(300)

    #C0144
    ChrTalk(
        0x1C,
        (
            "#04606F唔……我并没打算\x01",
            "纠缠你们的。\x02\x03",

            "#04600F顺便问一下，是什么工作呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#12P#00006F呼……真是没办法。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0146
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将寻找小猫的事情\x01",
            "做了简要说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0147
    ChrTalk(
        0x1C,
        (
            "#04605F嗯～原来如此。\x02\x03",

            "#04600F那么，你们准备如何寻找\x01",
            "那只叫玛丽的小猫？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#12P#00000F我们准备借助警犬的嗅觉，\x01",
            "顺着它的气味来……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x1C,
        "#04609F啊哈哈，那可不行哦。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0150
    ChrTalk(
        0x101,
        "#12P#00005F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x1C,
        (
            "#04602F小哥，你虽然很了解狗，\x01",
            "但好像并不太了解猫吧？\x02\x03",

            "#04604F应该多考虑考虑\x01",
            "小猫玛丽的心情哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#12P#00006F这、这是什么意思？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x1C,
        (
            "#04600F我虽然不了解详情，\x01",
            "不过，那家人最近搬过家吧？\x02\x03",

            "#04604F所以，我想答案只有一个。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0154
    ChrTalk(
        0x102,
        (
            "#00105F啊！\x01",
            "我之前怎么就没想到呢！\x02\x03",

            "#00100F是住宅街。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x1C,
        "#04600F嗯～它以前的家就在那里吧？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0156
    ChrTalk(
        0x101,
        (
            "#12P#00005F是这样啊，玛丽其实\x01",
            "从一开始就想回家……！\x02\x03",

            "#00001F只是它没有回到新家，\x01",
            "而是回到了以前居住的住宅街。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x109,
        (
            "#12P#10103F原来如此，\x01",
            "这样的确可以解释得通呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x105,
        (
            "#12P#10303F猫狗相比，狗认主人，\x01",
            "而猫却更加认家。\x02\x03",

            "#10300F只要想想猫在与主人\x01",
            "失散之后的行动模式，\x01",
            "马上就可以想到了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        (
            "#00303F……确实，柯贝也一直\x01",
            "不离开支援科大楼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x1C,
        (
            "#04609F啊哈哈，正是如此。\x02\x03",

            "#04602F那我就先走一步啦¤\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x1F4)
    Sleep(300)

    def lambda_64E1():
        OP_95(0xFE, 2270, -220, -3590, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_64E1)
    Sleep(1000)
    OP_68(1440, -1400, -13650, 3000)
    MoveCamera(27, 27, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14300, 3000)
    OP_6F(0x79)
    SetChrFlags(0x1C, 0x80)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0161
    ChrTalk(
        0x101,
        (
            "#00005F难、难道说……\x01",
            "她想参与进来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，好像是呢。\x02\x03",

            "#10300F真是个情绪善变的小猫……\x01",
            "不，应该形容为幼虎才对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x109,
        "#6P#10106F实在是笑不出来啊……\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x102,
        (
            "#00106F唔……\x01",
            "到底该怎么办才好呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x104,
        (
            "#00303F……算了，只要没有涉及战争，\x01",
            "她也并不是很危险的家伙。\x02\x03",

            "#00300F说不定她很快就会失去耐心了，\x01",
            "先看看情况再说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#00000F明白了……\x01",
            "我们也赶快前往住宅街吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x155, 1)
    OP_29(0x74, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2000, -3000, -11920, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_29_56D7 end

    def Function_30_6768(): pass

    label("Function_30_6768")

    OP_95(0x101, 750, -3000, -12700, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_30_6768 end

    def Function_31_6784(): pass

    label("Function_31_6784")

    OP_95(0x102, 2530, -3000, -11630, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_31_6784 end

    def Function_32_67A0(): pass

    label("Function_32_67A0")

    OP_95(0x104, 3790, -3000, -12940, 2000, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_32_67A0 end

    def Function_33_67BC(): pass

    label("Function_33_67BC")

    OP_95(0x109, 1400, -3000, -14510, 2000, 0x0)
    OP_93(0x109, 0x2D, 0x1F4)
    Return()

    # Function_33_67BC end

    def Function_34_67D8(): pass

    label("Function_34_67D8")

    OP_95(0x105, 3200, -3000, -14560, 2000, 0x0)
    OP_93(0x105, 0x13B, 0x1F4)
    Return()

    # Function_34_67D8 end

    def Function_35_67F4(): pass

    label("Function_35_67F4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B87")

    #C0167
    ChrTalk(
        0x1A2,
        "钓皇俱乐部……？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#00000F嗯，这是一个钓鱼爱好者\x01",
            "聚集交流的俱乐部。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x1A2,
        (
            "哼，虽然不太明白，但大致就是\x01",
            "一群只懂钓鱼的傻瓜聚集的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x1A2,
        (
            "原来克洛斯贝尔也有\x01",
            "这样的人啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0171
    ChrTalk(
        0x102,
        "#00105F共和国也有钓鱼爱好者吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0172
    ChrTalk(
        0x1A2,
        "嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x1A2,
        (
            "顺便一说，我的祖父\x01",
            "就很喜欢钓鱼，\x01",
            "但我完全无法理解。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x1A2,
        (
            "如果想捉鱼，\x01",
            "用网捕捞的效率\x01",
            "不是高得多吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6A30")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_69E1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69E1)
    Sleep(50)

    def lambda_69F1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_69F1)
    Sleep(50)

    def lambda_6A01():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A01)
    Sleep(300)

    #C0175
    ChrTalk(
        0x104,
        "#00306F完全无法反驳啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B7F")

    label("loc_6A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6AD8")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_6A89():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A89)
    Sleep(50)

    def lambda_6A99():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A99)
    Sleep(50)

    def lambda_6AA9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6AA9)
    Sleep(300)

    #C0176
    ChrTalk(
        0x109,
        "#10106F完全无法反驳呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B7F")

    label("loc_6AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6B7F")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_6B31():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B31)
    Sleep(50)

    def lambda_6B41():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B41)
    Sleep(50)

    def lambda_6B51():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6B51)
    Sleep(300)

    #C0177
    ChrTalk(
        0x105,
        "#10304F呵呵，完全无法反驳呢。\x02",
    )

    CloseMessageWindow()

    label("loc_6B7F")

    SetScenarioFlags(0x1, 6)
    Jump("loc_6BAE")

    label("loc_6B87")


    #C0178
    ChrTalk(
        0x1A2,
        (
            "我对这种地方没有兴趣，\x01",
            "去别处吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BAE")

    Jump("loc_6DEE")

    label("loc_6BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BC9")
    Call(0, 26)
    Jump("loc_6DEE")

    label("loc_6BC9")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D60")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁，\x01",
            "上面挂着告示板。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0180
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～正在准备中～　　\x01",
            "　　　——钓皇俱乐部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0181
    ChrTalk(
        0x101,
        (
            "#00005F准备中吗……\x01",
            "说起来……钓皇俱乐部……？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#00105F这里就是罗伊德加入的那个\x01",
            "『钓公师团』的分部吧？\x02\x03",

            "#00100F你没听其他成员\x01",
            "说过什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#00003F嗯，因为最近一直很忙，\x01",
            "根本没有钓鱼的时间。\x02\x03",

            "#00000F大门上着锁，\x01",
            "还是下次再来吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 5)
    Jump("loc_6DEE")

    label("loc_6D60")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁，\x01",
            "上面挂着告示板。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0185
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～正在准备中～　　\x01",
            "　　　——钓皇俱乐部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6DEE")

    TalkEnd(0xFF)
    Return()

    # Function_35_67F4 end

    def Function_36_6DF2(): pass

    label("Function_36_6DF2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EC3")

    #C0186
    ChrTalk(
        0x1A2,
        "嗯？这里是公寓吧？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x1A2,
        (
            "莫非里面有什么\x01",
            "有趣的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#00000F不，并没有\x01",
            "什么特别的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x1A2,
        (
            "哼，那就没有进去的意义吧。\x01",
            "赶快带我去下一个地方。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_6F25")

    label("loc_6EC3")


    #C0190
    ChrTalk(
        0x1A2,
        (
            "又没有什么事情要进这里，\x01",
            "我可没有冒昧闯入\x01",
            "他人住所的爱好。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x1A2,
        "好了，赶快带我去下一个地方。\x02",
    )

    CloseMessageWindow()

    label("loc_6F25")

    TalkEnd(0xFF)
    Return()

    # Function_36_6DF2 end

    def Function_37_6F29(): pass

    label("Function_37_6F29")

    EventBegin(0x2)
    SetChrName("")

    #A0192
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "供奉着东方的地藏菩萨。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_706D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_706A")

    #C0193
    ChrTalk(
        0x1A2,
        (
            "地藏吗……\x01",
            "简直就像是东方人街啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        "#00005F那里肯定有很多地藏吧？\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x1A2,
        (
            "是啊，包括预防火灾的地藏，\x01",
            "消灾解厄的地藏等等，\x01",
            "按照作用的不同，分为很多种类。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x1A2,
        (
            "不过我并不相信\x01",
            "那种虚无缥缈的\x01",
            "东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        "#00006F是、是吗……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DC, 4)
    EventEnd(0x3)
    Return()

    label("loc_706A")

    EventEnd(0x3)
    Return()

    label("loc_706D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72A2")

    #C0198
    ChrTalk(
        0x101,
        (
            "#00000F这里的地藏……\x01",
            "总是被人打扫得如此干净呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00100F看来有人一直在\x01",
            "诚心参拜。\x02\x03",

            "机会难得，我们也把\x01",
            "做好的料理供奉给地藏吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7187")

    #C0200
    ChrTalk(
        0x105,
        (
            "#10300F哎，支援科\x01",
            "还会做这种事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……也不是经常做啦。\x01",
            "不过，这也是个锻炼烹饪技术的方式吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71BD")

    label("loc_7187")


    #C0202
    ChrTalk(
        0x104,
        (
            "#00300F好，那就试试吧，\x01",
            "顺便也可以练习料理技术。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7240")

    #C0203
    ChrTalk(
        0x109,
        (
            "#10100F好啊，我赞成！\x01",
            "给自己定下目标，\x01",
            "才能取得进步……\x02\x03",

            "如果做出了高水平的料理，\x01",
            "就拿到这里献给地藏吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_729F")

    label("loc_7240")


    #C0204
    ChrTalk(
        0x103,
        (
            "#00200F给自己定下目标，\x01",
            "才能进步得更快。\x02\x03",

            "如果做出了高水平的料理，\x01",
            "就拿到这里献给地藏吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_729F")

    SetScenarioFlags(0x20B, 0)

    label("loc_72A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E88")
    Call(0, 38)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7304")

    #C0205
    ChrTalk(
        0x101,
        (
            "#0000F现在似乎没有\x01",
            "可以供奉的高水平料理呢。\x02\x03",

            "下次再来供奉吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x3)
    Return()

    label("loc_7304")

    Call(0, 39)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 6)), scpexpr(EXPR_END)), "loc_7327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7322")
    Call(0, 40)
    Return()

    label("loc_7322")

    Jump("loc_8E88")

    label("loc_7327")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7665")
    SetChrName("")

    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "小包的旁边放着一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "致经常前来供奉料理的朋友。\x01",
            "各位为地藏菩萨供奉了这么多料理，\x01",
            "请容我致以诚挚谢意。\x02",
        )
    )

    CloseMessageWindow()

    #A0208
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我幼时曾与父亲生活在这个地区，\x01",
            "从那时起，便每日前来参拜地藏。\x01",
            "对我而言，这尊地藏雕像是饱含无数回忆的东西。\x01",
            "前来参拜地藏的人\x01",
            "如今已经寥寥无几了。\x01",
            "但即使如此，也仍然存在着各位这样的善良人士。\x01",
            "这让我暗暗欣喜，甚至产生了被救赎般的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "得知除了自己之外，还有其他的志同道合者，\x01",
            "使我感到十分开心。\x01",
            "行文冗长，实在失礼。\x01",
            "在此准备了些不成敬意的薄礼，\x01",
            "请务必接受我的谢意。\x02",
        )
    )

    CloseMessageWindow()

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "至今未能与各位直接会面，实在遗憾。\x01",
            "但我的身体还很健康，\x01",
            "今后仍会坚持每日前来参拜。\x01",
            "说不定有朝一日能与各位会面。\x01\x01",
            "　　　　　　～一名素不相识的邻人\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从小包中取出了大回复药。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0212
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了２个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('大回复药', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 6)
    SetScenarioFlags(0x2, 0)
    Jump("loc_8E88")

    label("loc_7665")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7964")
    SetChrName("")

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "中回复药的旁边\x01",
            "放着一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0214
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在明媚的阳光下，青草茁壮成长，\x01",
            "夏日的感觉终于渐渐来了。\x01",
            "在此祝愿经常前来供奉料理的朋友\x01",
            "身体健康，万事顺利。\x02",
        )
    )

    CloseMessageWindow()

    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "日前路过市政厅时，\x01",
            "我偶然遇到了学生时代的知己。\x01",
            "虽然她之前长年未回克洛斯贝尔，\x01",
            "但如今已随儿子与儿媳的工作调动而回归此地。\x01",
            "这意外的重逢\x01",
            "让我们二人大为吃惊。\x02",
        )
    )

    CloseMessageWindow()

    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "只要年轻时性情相投，无论经过多少岁月，\x01",
            "彼此间的情谊也不会改变。虽然长年来已经\x01",
            "连书信联系都没有了，但从当年的流行趋势，\x01",
            "到战争的残酷，怀旧的话题实在是聊之不尽。\x02",
        )
    )

    CloseMessageWindow()

    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如此偶然的幸运能眷顾于我，\x01",
            "说不定也是因为这地藏菩萨的保佑呢。\x01",
            "又和各位说了这么多无聊的事情，实在抱歉。\x01",
            "祝愿各位身体安康，\x01",
            "我的信就到此为止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0218
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('中回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 5)
    Jump("loc_8E88")

    label("loc_7964")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C18")
    SetChrName("")

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "中回复药的旁边\x01",
            "放着一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "经常前来供奉料理的朋友，\x01",
            "今天过得如何？\x01",
            "你们时常前来参拜地藏，\x01",
            "请容我致以诚挚谢意。\x02",
        )
    )

    CloseMessageWindow()

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不久之前，当我站在厨房中准备做饭时，\x01",
            "无意中想起了各位供奉的美味料理，\x01",
            "于是便突然产生了制作\x01",
            "那种料理的想法。\x02",
        )
    )

    CloseMessageWindow()

    #A0222
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我从幼年开始，便在母亲的严厉教导下\x01",
            "学习烹饪，本以为可以轻松做好，\x01",
            "但学习新事物果然不是那么容易的事情啊。\x01",
            "经过一番手忙脚乱的尝试，最终做出了\x01",
            "味道与平时稍有不同的奶油炖锅。\x01",
            "不过，万幸得到了家人的认可。\x02",
        )
    )

    CloseMessageWindow()

    #A0223
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在这事件不断的世态下，\x01",
            "能过着如此平和的生活，\x01",
            "我深怀感谢之情。\x01",
            "祝愿各位也能继续享受安宁平稳的生活。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0224
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('中回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 4)
    Jump("loc_8E88")

    label("loc_7C18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ED8")
    SetChrName("")

    #A0225
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "中回复药的旁边\x01",
            "放着一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0226
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在这个季节，降雨的日子稍显频繁，\x01",
            "各位过得还好吗？\x01",
            "我想，经常前来供奉料理的朋友\x01",
            "一定会阅读我写的信件，\x01",
            "于是情不自禁，再次提笔写下了这封信。\x02",
        )
    )

    CloseMessageWindow()

    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "几日前的中午，我来到繁华热闹的街区，\x01",
            "看到几个活泼的孩子正在\x01",
            "开心地追跑玩耍。\x01",
            "在这一带经常能见到这几个孩子，\x01",
            "他们能一直友好相处，让人无比欣慰。\x02",
        )
    )

    CloseMessageWindow()

    #A0228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "克洛斯贝尔在世界中备受瞩目，\x01",
            "我认为，对这个城市来说，\x01",
            "让这些孩子健康成长才是重要的事情。\x01",
            "最近闲来无事时，我经常想到这些。\x01",
            "希望安稳的生活可以持续到永远。\x02",
        )
    )

    CloseMessageWindow()

    #A0229
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "最后，我再次自作主张，\x01",
            "准备了一点不成敬意的小谢礼，\x01",
            "希望能够用得到。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('中回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 3)
    Jump("loc_8E88")

    label("loc_7ED8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8099")
    SetChrName("")

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "中回复药的旁边\x01",
            "放着一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "经常前来供奉料理的朋友，\x01",
            "请容我致以诚挚谢意。\x01",
            "每当我看到除自己之外，还有其他人\x01",
            "诚意前来参拜，并供奉如此美味的料理时，\x01",
            "都会感到内心温暖，进而度过愉快的一天。\x02",
        )
    )

    CloseMessageWindow()

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "虽然素不相识，但今日我且自作主张，\x01",
            "准备了一点不成敬意的小谢礼。\x01",
            "请将其当作长期虔诚参拜的答谢，\x01",
            "务必收下。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0234
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('中回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 2)
    Jump("loc_8E88")

    label("loc_8099")

    SetChrName("")

    #A0235
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要供奉大成功料理吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_80C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E88")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8119")
    MenuCmd(1, 1, "天上面『日轮』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_END)), "loc_810F")
    Call(2, 6)

    label("loc_810F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8152")
    MenuCmd(1, 1, "神仙麻婆『麒麟』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_END)), "loc_8148")
    Call(2, 6)

    label("loc_8148")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8187")
    MenuCmd(1, 1, "天下一品炒饭")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_817D")
    Call(2, 6)

    label("loc_817D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81BE")
    MenuCmd(1, 1, "极品牛排『刚』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_81B4")
    Call(2, 6)

    label("loc_81B4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81F3")
    MenuCmd(1, 1, "三日久煮炖菜")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_81E9")
    Call(2, 6)

    label("loc_81E9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_822A")
    MenuCmd(1, 1, "大地锅『烂漫』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_8220")
    Call(2, 6)

    label("loc_8220")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_822A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8261")
    MenuCmd(1, 1, "天河锅『瑞云』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_8257")
    Call(2, 6)

    label("loc_8257")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8298")
    MenuCmd(1, 1, "特快炸鱼『疾』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_END)), "loc_828E")
    Call(2, 6)

    label("loc_828E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_82CB")
    MenuCmd(1, 1, "丰盛蛋包饭")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_END)), "loc_82C1")
    Call(2, 6)

    label("loc_82C1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_82CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8302")
    MenuCmd(1, 1, "翠玉面『治愈』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_END)), "loc_82F8")
    Call(2, 6)

    label("loc_82F8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8333")
    MenuCmd(1, 1, "双层汉堡")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_8329")
    Call(2, 6)

    label("loc_8329")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8368")
    MenuCmd(1, 1, "四味奶酪比萨")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_835E")
    Call(2, 6)

    label("loc_835E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_839B")
    MenuCmd(1, 1, "强效三明治")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_END)), "loc_8391")
    Call(2, 6)

    label("loc_8391")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_839B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83D2")
    MenuCmd(1, 1, "真心盒饭『诚』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_END)), "loc_83C8")
    Call(2, 6)

    label("loc_83C8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_83D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8401")
    MenuCmd(1, 1, "辉煌汤")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_END)), "loc_83F7")
    Call(2, 6)

    label("loc_83F7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8432")
    MenuCmd(1, 1, "奇幻糖果")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_END)), "loc_8428")
    Call(2, 6)

    label("loc_8428")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_846B")
    MenuCmd(1, 1, "天上甜点『夜月』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_END)), "loc_8461")
    Call(2, 6)

    label("loc_8461")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_846B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84A4")
    MenuCmd(1, 1, "宝物甜点『白雪』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_END)), "loc_849A")
    Call(2, 6)

    label("loc_849A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84DD")
    MenuCmd(1, 1, "冰凉甜点『七彩』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_END)), "loc_84D3")
    Call(2, 6)

    label("loc_84D3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8516")
    MenuCmd(1, 1, "绝品甜点『瞬动』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_END)), "loc_850C")
    Call(2, 6)

    label("loc_850C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_854B")
    MenuCmd(1, 1, "玉露『绿风』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_END)), "loc_8541")
    Call(2, 6)

    label("loc_8541")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_854B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8580")
    MenuCmd(1, 1, "甘露『紫绀』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_END)), "loc_8576")
    Call(2, 6)

    label("loc_8576")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_85B9")
    MenuCmd(1, 1, "黑茶『梦魇杀手』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_END)), "loc_85AF")
    Call(2, 6)

    label("loc_85AF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_85F0")
    MenuCmd(1, 1, "秘水『桃源乡』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_END)), "loc_85E6")
    Call(2, 6)

    label("loc_85E6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85F0")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8632")
    Sleep(500)
    Jump("loc_8E83")

    label("loc_8632")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_869F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8695")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天上面『日轮』', 1)
    SetScenarioFlags(0x208, 0)

    #A0236
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x190),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8695")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_869F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_86ED")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86E3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('神仙麻婆『麒麟』', 1)
    SetScenarioFlags(0x208, 1)

    #A0237
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x193),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_86E3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_86ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_873B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8731")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天下一品炒饭', 1)
    SetScenarioFlags(0x208, 2)

    #A0238
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x196),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8731")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_873B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8789")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_877F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('极品牛排『刚』', 1)
    SetScenarioFlags(0x208, 3)

    #A0239
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x199),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_877F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_87D7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87CD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('三日久煮炖菜', 1)
    SetScenarioFlags(0x208, 4)

    #A0240
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_87CD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8825")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_881B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大地锅『烂漫』', 1)
    SetScenarioFlags(0x208, 5)

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_881B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8873")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8869")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天河锅『瑞云』', 1)
    SetScenarioFlags(0x208, 6)

    #A0242
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8869")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_88C1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88B7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('特快炸鱼『疾』', 1)
    SetScenarioFlags(0x208, 7)

    #A0243
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_88B7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_890F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8905")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('丰盛蛋包饭', 1)
    SetScenarioFlags(0x209, 0)

    #A0244
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8905")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_890F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_895D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8953")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('翠玉面『治愈』', 1)
    SetScenarioFlags(0x209, 1)

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8953")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_895D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_89AB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89A1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('双层汉堡', 1)
    SetScenarioFlags(0x209, 2)

    #A0246
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_89A1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_89F9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89EF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('四味奶酪比萨', 1)
    SetScenarioFlags(0x209, 3)

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_89EF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8A47")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A3D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('强效三明治', 1)
    SetScenarioFlags(0x209, 4)

    #A0248
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8A3D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8A95")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A8B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('真心盒饭『诚』', 1)
    SetScenarioFlags(0x209, 5)

    #A0249
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8A8B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8AE3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AD9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('辉煌汤', 1)
    SetScenarioFlags(0x209, 6)

    #A0250
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8AD9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B31")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B27")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('奇幻糖果', 1)
    SetScenarioFlags(0x209, 7)

    #A0251
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8B27")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B7F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B75")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天上甜点『夜月』', 1)
    SetScenarioFlags(0x20A, 0)

    #A0252
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8B75")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BCD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BC3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('宝物甜点『白雪』', 1)
    SetScenarioFlags(0x20A, 1)

    #A0253
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8BC3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C1B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C11")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('冰凉甜点『七彩』', 1)
    SetScenarioFlags(0x20A, 2)

    #A0254
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8C11")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C69")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C5F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('绝品甜点『瞬动』', 1)
    SetScenarioFlags(0x20A, 3)

    #A0255
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8C5F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8CB7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CAD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('玉露『绿风』', 1)
    SetScenarioFlags(0x20A, 4)

    #A0256
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8CAD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D05")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CFB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('甘露『紫绀』', 1)
    SetScenarioFlags(0x20A, 5)

    #A0257
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8CFB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D53")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D49")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('黑茶『梦魇杀手』', 1)
    SetScenarioFlags(0x20A, 6)

    #A0258
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8D49")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8DA1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D97")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('秘水『桃源乡』', 1)
    SetScenarioFlags(0x20A, 7)

    #A0259
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出去了。\x02",
        )
    )


    label("loc_8D97")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DA1")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E80")

    #C0260
    ChrTalk(
        0x101,
        (
            "#00000F好，这样就行了。\x01",
            "……下次再把料理带来供奉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E7D")

    #C0261
    ChrTalk(
        0x102,
        (
            "#00100F如果总是供奉相同的料理，\x01",
            "未免太过失礼，\x01",
            "每种料理还是只供奉一次为好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        "#00000F嗯，说的对。\x02",
    )

    CloseMessageWindow()

    label("loc_8E7D")

    SetScenarioFlags(0x20B, 1)

    label("loc_8E80")

    SetScenarioFlags(0x2, 0)

    label("loc_8E83")

    Jump("loc_80C6")

    label("loc_8E88")

    EventEnd(0x3)
    Return()

    # Function_37_6F29 end

    def Function_38_8E8B(): pass

    label("Function_38_8E8B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EAE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EC7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EE0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EF9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F12")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F2B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F44")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F5D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F76")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F8F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FA8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FC1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FDA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FF3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_900C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_900C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9025")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_903E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_903E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9057")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9070")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9089")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90A2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90BB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90D4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90ED")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90ED")

    Return()

    # Function_38_8E8B end

    def Function_39_90EE(): pass

    label("Function_39_90EE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_END)), "loc_910B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_910B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_END)), "loc_911E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_911E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_9131")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_9144")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_9157")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_916A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_916A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_917D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_917D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_END)), "loc_9190")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_END)), "loc_91A3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_END)), "loc_91B6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_91C9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_91DC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_END)), "loc_91EF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_END)), "loc_9202")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_END)), "loc_9215")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_END)), "loc_9228")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_END)), "loc_923B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_923B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_END)), "loc_924E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_924E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_END)), "loc_9261")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_END)), "loc_9274")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_END)), "loc_9287")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_END)), "loc_929A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_929A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_END)), "loc_92AD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_END)), "loc_92C0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92C0")

    Return()

    # Function_39_90EE end

    def Function_40_92C1(): pass

    label("Function_40_92C1")

    EventBegin(0x0)
    Fade(1000)
    OP_68(14950, 1450, 2880, 0)
    MoveCamera(44, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14180, 0)
    SetChrPos(0x101, 16200, -300, 2570, 0)
    SetChrPos(0x102, 17600, -300, 2700, 0)
    SetChrPos(0x103, 15750, -300, 1260, 0)
    SetChrPos(0x104, 17570, -300, 1120, 0)
    SetChrPos(0xF4, 15720, -300, 20, 0)
    SetChrPos(0xF5, 16940, -300, 30, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    LoadChrToIndex("chr/ch23300.itc", 0x1E)
    SetChrChipByIndex(0x2A, 0x1E)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -3400, -300, 1670, 0)
    OP_0D()

    #C0263
    ChrTalk(
        0x101,
        (
            "#00000F（……供奉着料理的地藏吗……\x01",
            "  虽然并没有恳求神明的想法，但是……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0264
    ChrTalk(
        0x101,
        (
            "#00002F各位，难得来到这里，\x01",
            "在出发之前，先来参拜一下如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    #C0265
    ChrTalk(
        0x102,
        "#00100F啊，好啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94A2")

    #C0266
    ChrTalk(
        0x109,
        (
            "#10100F是要祈祷将小琪雅平安救出吧？\x01",
            "……我赞成！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94DA")

    #C0267
    ChrTalk(
        0x10A,
        (
            "#00606F哼，虽然时间紧迫，\x01",
            "不过……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94DA")


    #C0268
    ChrTalk(
        0x103,
        (
            "#00202F反正也花费不了多少时间，\x01",
            "而且参拜一下，对我们的精神状态有益无害。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x104,
        (
            "#00300F考虑到接下来需要保持士气，\x01",
            "一起在这里集中一下精神也不坏呢。\x02\x03",

            "#00309F好，咱们开始吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)

    #C0270
    ChrTalk(
        0x102,
        (
            "#00100F按照东方的风俗习惯，\x01",
            "首先要这样合拢双掌。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0271
    ChrTalk(
        0x101,
        "#00005F哦，是这样吗……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9630")

    #C0272
    ChrTalk(
        0x105,
        (
            "#10402F呵呵，然后弯腰\x01",
            "四十五度左右就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9630")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96D1")

    #C0273
    ChrTalk(
        0x106,
        (
            "#10702F其实还有很多\x01",
            "繁琐的规矩……\x02\x03",

            "#10704F不过，我们现在只要按照在七耀教会\x01",
            "祈祷时的要领来参拜就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x101,
        "#00000F明白了，一起来参拜吧。\x02",
    )

    CloseMessageWindow()

    label("loc_96D1")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrName("")

    #A0275
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人双手合十，闭上双眼，\x01",
            "向地藏做了祈祷。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(1000)
    Sound(491, 0, 100, 0)
    Sleep(300)
    Sound(491, 0, 80, 0)
    Sleep(500)

    #N0276
    NpcTalk(
        0x2A,
        "声音",
        (
            "哎呀呀，真抱歉，\x01",
            "我的耳朵很背。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(500)
    OP_68(-3070, 1450, 2110, 0)
    MoveCamera(44, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14180, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_93(0x2A, 0x5A, 0x1F4)
    Sleep(100)

    def lambda_9817():
        OP_95(0xFE, 12120, -300, 1430, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9817)
    Sleep(1000)
    OP_68(12510, 1450, 1570, 8000)
    MoveCamera(57, 25, 0, 8000)
    Sleep(4000)
    WaitChrThread(0x2A, 1)
    Sleep(500)

    #C0277
    ChrTalk(
        0x2A,
        "哎，你们是……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    Sleep(500)

    def lambda_9886():

        label("loc_9886")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_9886")

    QueueWorkItem2(0x101, 2, lambda_9886)
    Sleep(50)

    def lambda_989B():

        label("loc_989B")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_989B")

    QueueWorkItem2(0x102, 2, lambda_989B)
    Sleep(50)

    def lambda_98B0():

        label("loc_98B0")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_98B0")

    QueueWorkItem2(0x103, 2, lambda_98B0)
    Sleep(50)

    def lambda_98C5():

        label("loc_98C5")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_98C5")

    QueueWorkItem2(0x104, 2, lambda_98C5)
    Sleep(50)

    def lambda_98DA():

        label("loc_98DA")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_98DA")

    QueueWorkItem2(0xF4, 2, lambda_98DA)
    Sleep(50)

    def lambda_98EF():

        label("loc_98EF")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_98EF")

    QueueWorkItem2(0xF5, 2, lambda_98EF)
    Sleep(50)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0278
    ChrTalk(
        0x102,
        "#00105F……嗯？\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x2A,
        (
            "难道说……一直给\x01",
            "地藏菩萨供奉料理的人\x01",
            "就是你们吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        "#00005F啊……也就是说……！？\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        "#00205F留下那些信的人就是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0282
    ChrTalk(
        0x2A,
        "哎呀呀，原来真的是你们啊！？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x2A,
        (
            "没想到竟然是这么多\x01",
            "可爱的孩子……\x01",
            "本以为是和我年纪相仿的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#00002F啊哈哈，其实我们只是在练习\x01",
            "制作料理的同时顺便过来供奉……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#00300F哎呀，我也很吃惊啊。\x01",
            "您好像就是……经常待在\x01",
            "旧城区的那位老婆婆吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        (
            "#00104F通过信中那优美的字迹\x01",
            "与有礼的措辞，\x01",
            "倒也想过写信人可能是位长辈……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x2A,
        (
            "呵呵呵，我总是时隔好久才写信，\x01",
            "真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x2A,
        (
            "不过，原来是这样啊……\x01",
            "这个世界上果真\x01",
            "有很多意外的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_9C06():
        OP_95(0xFE, 14600, -300, 3080, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9C06)
    Sleep(800)
    EndChrThread(0x101, 0x2)
    OP_93(0x101, 0x0, 0x12C)

    def lambda_9C2E():
        OP_96(0xFE, 0x3F34, 0xFFFFFED4, 0x898, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C2E)
    Sleep(50)
    EndChrThread(0x103, 0x2)
    OP_93(0x103, 0x0, 0x0)

    def lambda_9C56():
        OP_96(0xFE, 0x3B92, 0xFFFFFED4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9C56)
    FadeToDark(2000, 0, -1)
    Sleep(50)
    EndChrThread(0xF4, 0x2)

    def lambda_9C81():
        OP_96(0xFE, 0x3D68, 0xFFFFFED4, 0xFFFFFF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9C81)
    WaitChrThread(0x2A, 1)

    def lambda_9C9F():
        OP_95(0xFE, 17260, -300, 3820, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9C9F)
    OP_0D()
    Sleep(1000)
    OP_68(14150, 1450, 840, 0)
    MoveCamera(62, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12970, 0)
    SetChrPos(0x2A, 17260, -300, 3820, 0)
    SetChrPos(0x101, 16000, -300, 1250, 0)
    SetChrPos(0x102, 18000, -300, 1340, 0)
    SetChrPos(0x103, 14800, -300, 50, 0)
    SetChrPos(0x104, 18800, -300, 370, 0)
    SetChrPos(0xF4, 16400, -300, -650, 0)
    SetChrPos(0xF5, 18200, -300, -730, 0)
    SetChrName("")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "帕欧拉双手合十，静静地向地藏祈祷。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(12770, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x2A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(2000)

    #C0290
    ChrTalk(
        0x2A,
        (
            "这座地藏经历过\x01",
            "克洛斯贝尔的整个动乱时代，\x01",
            "曾经还被毁坏过数次。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x2A,
        (
            "但在市内各位的努力之下，\x01",
            "每次都将它重新建起。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x2A,
        (
            "……虽然前来参拜地藏的人\x01",
            "如今已经寥寥无几了……\x01",
            "但是并不用担心哦，呵呵。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2A, 0xB4, 0x190)

    #C0293
    ChrTalk(
        0x2A,
        (
            "对了，我正好\x01",
            "带着一个好东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x2A,
        (
            "虽然把别人赠与的东西转送出去不太好……\x01",
            "但希望各位能把它收下。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        "#00005F那个，可是……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x2A,
        (
            "呵呵，没关系的，\x01",
            "只是我的一些心意。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x2A, 16010, -300, 2000, 1500, 0x0)
    TurnDirection(0x2A, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('草⑿', 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FA3")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0297
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xEC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('草⑿', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x2, 7)
    Jump("loc_9FEA")

    label("loc_9FA3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0298
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('风耀珠', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_9FEA")


    def lambda_9FEF():
        OP_96(0xFE, 0x3E80, 0xFFFFFED4, 0xA00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9FEF)

    def lambda_A009():

        label("loc_A009")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A009")

    QueueWorkItem2(0x101, 2, lambda_A009)

    def lambda_A01B():

        label("loc_A01B")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A01B")

    QueueWorkItem2(0x102, 2, lambda_A01B)

    def lambda_A02D():

        label("loc_A02D")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A02D")

    QueueWorkItem2(0x103, 2, lambda_A02D)

    def lambda_A03F():

        label("loc_A03F")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A03F")

    QueueWorkItem2(0x104, 2, lambda_A03F)

    def lambda_A051():

        label("loc_A051")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A051")

    QueueWorkItem2(0xF4, 2, lambda_A051)

    def lambda_A063():

        label("loc_A063")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A063")

    QueueWorkItem2(0xF5, 2, lambda_A063)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0299
    ChrTalk(
        0x2A,
        (
            "这是一个晚辈送给我的东西，\x01",
            "但放在我这里，也只是个装饰品而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x2A,
        (
            "……呵呵呵，伊梅尔达也真是的。\x01",
            "她总是这么粗枝大叶，\x01",
            "太不会送东西了。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x2A,
        (
            "再见了，孩子们。\x01",
            "只是偶尔过来也无妨，\x01",
            "以后还要来参拜地藏哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2A, 0x10E, 0x1F4)

    def lambda_A1EF():
        OP_95(0xFE, -1050, -300, 2150, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A1EF)
    Sleep(5000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A285")

    #C0302
    ChrTalk(
        0x109,
        (
            "#10102F唔……不知道那位\x01",
            "老婆婆是什么人。\x01",
            "总觉得她的一举一动都很有风度呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2C6")

    label("loc_A285")


    #C0303
    ChrTalk(
        0x104,
        (
            "#00302F唔……\x01",
            "那位老婆婆是什么人呢，\x01",
            "一举一动都那么有风度。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A36A")

    #C0304
    ChrTalk(
        0x106,
        (
            "#10702F那位老婆婆经常在我\x01",
            "住的公寓附近晒太阳。\x02\x03",

            "#10704F虽然她现在居住在旧城区，\x01",
            "但以前好像住在其它地方……\x01",
            "总之，我认为她是个很出色的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3A8")

    label("loc_A36A")


    #C0305
    ChrTalk(
        0x103,
        (
            "#00202F那位婆婆的年龄已经相当大了，\x01",
            "但看上去很有活力呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_A3F7")

    #C0306
    ChrTalk(
        0x101,
        (
            "#00005F这是核心回路……\x01",
            "而且她还将伊梅尔达夫人\x01",
            "称为晚辈……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A43E")

    label("loc_A3F7")


    #C0307
    ChrTalk(
        0x101,
        (
            "#00005F这是稀有的高等回路……\x01",
            "而且她还将伊梅尔达夫人\x01",
            "称为晚辈……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A43E")


    #C0308
    ChrTalk(
        0x102,
        (
            "#00100F真是个心地善良，\x01",
            "而且不可思议的人呢。\x02\x03",

            "#00103F（说起来……据说在外公的上一代人之中，\x01",
            "  有一位相当优秀的女性\x01",
            "  被称作『社交界之花』……）\x02\x03",

            "（难、难道说……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A55E")

    #C0309
    ChrTalk(
        0x10A,
        (
            "#00606F（……这些小鬼都不知道吗？\x01",
            "  她可是当年风靡克洛斯贝尔，\x01",
            "  迷倒了整整一代人的知名贵妇啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A55E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A632")

    #C0310
    ChrTalk(
        0x105,
        (
            "#10404F呵呵，偶尔来此\x01",
            "参拜一下倒也不坏啊。\x02\x03",

            "#10400F不过，队长，\x01",
            "我们现在不能耽搁太久吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#00005F哦，说的没错，\x01",
            "参拜过后，现在干劲已经更加充足了……\x02\x03",

            "#00000F好，那我们就赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6C1")

    label("loc_A632")


    #C0312
    ChrTalk(
        0x101,
        (
            "#00004F只是想参拜一下而已，\x01",
            "结果却发生了意想不到的状况……\x01",
            "不过，现在已经鼓足干劲了。\x02\x03",

            "#00000F好，我们差不多也该出发了。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x104,
        "#00300F是！\x02",
    )

    CloseMessageWindow()

    label("loc_A6C1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 17130, -300, 2670, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 26200, -300, -1050, 270)
    BeginChrThread(0xD, 1, 0, 1)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -40490, -300, 15850, 90)
    BeginChrThread(0xE, 1, 0, 6)
    EndChrThread(0x2A, 0xFF)
    SetChrFlags(0x2A, 0x80)
    OP_D7(0x1E)
    SetScenarioFlags(0x20B, 7)
    EventEnd(0x5)
    Return()

    # Function_40_92C1 end

    def Function_41_A73A(): pass

    label("Function_41_A73A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A86D")
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0314
    ChrTalk(
        0x1A2,
        "这里是……？\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        (
            "#00100F这里是克洛斯贝尔\x01",
            "工商协会会长的家哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#00000F我们与会长先生有过一些往来，\x01",
            "他对我们很亲切。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x1A2,
        "唔，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x1A2,
        (
            "既然是工商协会的会长，\x01",
            "曹他们想必也很\x01",
            "重视这个人……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x1A2,
        (
            "好，那就进去\x01",
            "打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C5, 3)
    OP_65(0x6, 0x1)
    SetMapObjFlags(0x3, 0x10)

    label("loc_A86D")

    TalkEnd(0xFF)
    Return()

    # Function_41_A73A end

    def Function_42_A871(): pass

    label("Function_42_A871")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32200.itc", 0x1E)
    LoadChrToIndex("chr/ch23600.itc", 0x1F)
    LoadChrToIndex("chr/ch24200.itc", 0x20)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -2200, -300, 4400, 225)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -3000, -300, 5200, 225)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -1400, -300, 3600, 225)
    OP_68(-4790, 1690, 1740, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, -3700, -300, 2600, 45)
    SetChrPos(0x102, -4650, -300, 1000, 45)
    SetChrPos(0x104, -5350, -300, 1750, 45)
    SetChrPos(0x109, -4650, -300, -100, 45)
    SetChrPos(0x105, -6350, -300, 1750, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0320
    ChrTalk(
        0x101,
        (
            "#00003F『爆钓比赛』吗……\x01",
            "好像发展到了很难收场的局面啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x1A,
        "嘿嘿，不过一定可以轻松取胜的说。\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x1A,
        (
            "只要我们四人中的任意一人\x01",
            "能打败那个雷克罗德\x01",
            "就可以了的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x1B,
        (
            "这、这可真是……\x01",
            "老实说，凭我的实力，\x01",
            "恐怕不足以成为战力。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x19,
        (
            "『钓杰四天王』\x01",
            "也很令人在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x19,
        (
            "根据比赛规则，并没有挑战次数限制。\x01",
            "只要坚持下去，\x01",
            "总有取胜的机会……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x19,
        (
            "但我并不认为会像\x01",
            "克潘说的那么简单哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x19,
        (
            "据说他们的实力\x01",
            "全都在我们所谓的\x01",
            "『特级钓师』之上呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0328
    ChrTalk(
        0x101,
        "#00005F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x1B,
        (
            "呼……\x01",
            "我果然是没希望啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x1A,
        (
            "嘿嘿，原来如此……\x01",
            "这不是很有趣嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x19,
        (
            "好，那我们就先回\x01",
            "新分部召开作战会议吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0332
    ChrTalk(
        0x101,
        "#00005F新分部吗？\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x1B,
        (
            "哦，对了，还没\x01",
            "和罗伊德说呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x1B,
        (
            "分部长在东克洛斯贝尔街道\x01",
            "找到了一座可以当作\x01",
            "新事务所的建筑物。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x1B,
        (
            "那本是一座租船小屋，\x01",
            "自从在数年前废弃之后\x01",
            "就一直无人使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x1A,
        (
            "虽然又小又破旧，\x01",
            "但在小屋附近的河边就可以钓鱼，\x01",
            "倒也是个很不错的场所的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x19,
        (
            "嗯，那里简直就是个\x01",
            "为从头再来的我们\x01",
            "量身定做的合适场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x19,
        (
            "在东克洛斯贝尔街道的三岔路口\x01",
            "往唐古拉姆门方向走，\x01",
            "可以看到一块路牌……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x19,
        (
            "接下来，只要按照路牌\x01",
            "上的标记再往南走几步，\x01",
            "就能找到新分部了。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x19,
        (
            "罗伊德团员，等你有空时，\x01",
            "也去那里露个面吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        "#00000F好的，知道了。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x19,
        (
            "另外，罗伊德团员，\x01",
            "虽然计划是由我们几个\x01",
            "尽力赢得爆钓比赛……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x19,
        (
            "但同伴的数量\x01",
            "自然还是越多越好。\x01",
            "也拜托你努力加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#00004F好的，我也不希望\x01",
            "从此失去自己喜欢的\x01",
            "钓鱼场所。\x02\x03",

            "#00000F一定会拼尽全力的。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x1A,
        (
            "嘿嘿，罗伊德团员，\x01",
            "我也不会输的说～\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x1B,
        "那我们这就告辞了。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x19,
        "再见啦，祝你旗开得胜！\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        "#00000F嗯，分部长，你们也一样！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 43)
    Sleep(200)
    BeginChrThread(0x19, 3, 0, 43)
    Sleep(200)
    BeginChrThread(0x1A, 3, 0, 43)
    Sleep(1000)

    def lambda_AFEB():

        label("loc_AFEB")

        TurnDirection(0x101, 0x1A, 500)
        Yield()
        Jump("loc_AFEB")

    QueueWorkItem2(0x101, 2, lambda_AFEB)

    def lambda_AFFD():

        label("loc_AFFD")

        TurnDirection(0x102, 0x1A, 500)
        Yield()
        Jump("loc_AFFD")

    QueueWorkItem2(0x102, 2, lambda_AFFD)

    def lambda_B00F():

        label("loc_B00F")

        TurnDirection(0x109, 0x1A, 500)
        Yield()
        Jump("loc_B00F")

    QueueWorkItem2(0x109, 2, lambda_B00F)

    def lambda_B021():

        label("loc_B021")

        TurnDirection(0x105, 0x1A, 500)
        Yield()
        Jump("loc_B021")

    QueueWorkItem2(0x105, 2, lambda_B021)

    def lambda_B033():

        label("loc_B033")

        TurnDirection(0x104, 0x1A, 500)
        Yield()
        Jump("loc_B033")

    QueueWorkItem2(0x104, 2, lambda_B033)
    WaitChrThread(0x1B, 3)

    #C0349
    ChrTalk(
        0x102,
        (
            "#00109F（唔～罗伊德可真是的，\x01",
            "  一副跃跃欲试的样子啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x109,
        (
            "#10100F（钓鱼吗……\x01",
            "  虽然不太了解，但热衷于此\x01",
            "  的人还真是有很多呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetScenarioFlags(0x1C0, 2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, 26200, -300, -1050, 270)
    BeginChrThread(0xD, 0, 0, 1)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -40490, -300, 15850, 90)
    BeginChrThread(0xE, 0, 0, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -3700, -300, 2600, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_42_A871 end

    def Function_43_B174(): pass

    label("Function_43_B174")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_95(0xFE, 110, -300, 1300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    OP_95(0xFE, 14590, -300, 1300, 2000, 0x0)
    Return()

    # Function_43_B174 end

    def Function_44_B1AB(): pass

    label("Function_44_B1AB")

    EventBegin(0x1)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0351
    ChrTalk(
        0x1A2,
        (
            "没必要带我去这里，\x01",
            "赶快去别的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    EventEnd(0x4)
    Return()

    # Function_44_B1AB end

    def Function_45_B1F6(): pass

    label("Function_45_B1F6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B267")

    #C0352
    ChrTalk(
        0x1A2,
        (
            "喂，往这边走\x01",
            "不就要离开市区了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    #C0353
    ChrTalk(
        0x101,
        (
            "#00000F啊，的确如此，\x01",
            "我们还是回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_B293")

    label("loc_B267")


    #C0354
    ChrTalk(
        0x101,
        (
            "#00000F现在不能离开市区，\x01",
            "还是回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B293")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_45_B1F6 end

    def Function_46_B2A7(): pass

    label("Function_46_B2A7")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B31B")

    #C0355
    ChrTalk(
        0x101,
        (
            "#00000F前方是东克洛斯贝尔街道。\x02\x03",

            "现在并没有需要离开市区的事情，\x01",
            "还是不要出去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_B351")

    label("loc_B31B")


    #C0356
    ChrTalk(
        0x101,
        (
            "#00000F并没有事情需要往这边走，\x01",
            "还是不要出去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B41B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3CF")

    #C0357
    ChrTalk(
        0x101,
        (
            "#00001F前方是东克洛斯贝尔街道。\x02\x03",

            "现在不要四处乱逛了，\x01",
            "还是集中精力，专心调查列车事故吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_B41B")

    label("loc_B3CF")


    #C0358
    ChrTalk(
        0x101,
        (
            "#00001F并没有事情需要往这边走，\x01",
            "现在还是集中精力，专心调查列车事故吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B46E")

    #C0359
    ChrTalk(
        0x101,
        (
            "#00001F现在必须要尽快\x01",
            "调查兰迪的行踪，\x01",
            "并不是去别处乱逛的时候。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B4BA")

    #C0360
    ChrTalk(
        0x101,
        (
            "#00001F现在并不是前往市外的时候，\x01",
            "还是老老实实地回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B52F")

    #C0361
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

    label("loc_B52F")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_46_B2A7 end

    def Function_47_B543(): pass

    label("Function_47_B543")

    EventBegin(0x1)

    #C0362
    ChrTalk(
        0x105,
        (
            "#10303F……罗伊德，不好意思，\x01",
            "可以过段时间\x01",
            "再回旧城区吗？\x02\x03",

            "#10308F哪怕只过一会也好，\x01",
            "至少不要现在\x01",
            "回去就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        "#00003F嗯……知道了。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1610, -3000, -35150, 0)
    EventEnd(0x4)
    Return()

    # Function_47_B543 end

    SaveToFile()

Try(main)
